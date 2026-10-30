#!/usr/bin/env python3
"""fetch_images.py — lấy ảnh chân dung từ Wikimedia Commons theo PLAN §7.

    python fetch_images.py              # mọi nhân vật trong data/persons.json chưa có ảnh (chạy build.py trước)
    python fetch_images.py CH00         # chỉ các ID bắt đầu bằng tiền tố
    python fetch_images.py --refresh    # làm lại cả ảnh đã có
    python fetch_images.py --dry-run    # chỉ tra metadata & quyết định, không tải, không ghi images.json

Luồng (§7.1): Wikidata P18 → Commons imageinfo/extmetadata (fallback: trang File + Structured Data khi API bị 429)
→ quyết định theo §7.2 → tải thumbnail 500px vào assets/img/ (không hotlink) → data/images.json + reports/images-review.txt.
Override thủ công: content/images.yaml (đổi ảnh, viết lại chú thích, bỏ ảnh, danh sách nhạy cảm về hình tượng).
Sau khi chạy xong: `python build.py` để nhúng ảnh vào HTML.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from atlaslib import common as C, parse as P  # noqa: E402

COMMONS_API = "https://commons.wikimedia.org/w/api.php"
COMMONS_FILE = "https://commons.wikimedia.org/wiki/"
UPLOAD = "https://upload.wikimedia.org/wikipedia/commons"
THUMB_HOST = "https://thumb.wikimedia.org/wikipedia/commons"
THUMB_WIDTH = 500                       # Commons chỉ còn phục vụ thumbnail ở cỡ cố định; 400 không còn được chấp nhận
ALLOWED_WIDTHS = [250, 330, 500, 960, 1280]
MAX_ORIGINAL = 25_000_000
IMG_DIR = ROOT / "assets" / "img"
IMAGES_JSON = ROOT / "data" / "images.json"
REVIEW_TXT = ROOT / "reports" / "images-review.txt"
YAML_PATH = ROOT / "content" / "images.yaml"

PD_RE = re.compile(r"\bpublic domain\b|^pd\b|^pd-|\bcc0\b|\bpdm\b|no known copyright|public domain mark", re.I)
CCBY_RE = re.compile(r"\bcc[- ]by(?:[- ]sa)?\b(?![- ]n[cd])", re.I)
BAD_RE = re.compile(r"\bnc\b|\bnd\b|non[- ]?commercial|no[- ]derivatives|fair use|non-free|all rights reserved", re.I)
RESTRICT_HTML_RE = re.compile(
    r"Personality rights|Quyền nhân thân|Trademarked|insignia|Freedom of panorama"
    r"|ita-mibac|mibac|communist|Nazi symbol|currency|costume|design|soviet", re.I)


def strip_tags(s: str) -> str:
    s = re.sub(r"<style.*?</style>", " ", s or "", flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


# ============================================================ images.yaml

def load_yaml(path: Path) -> dict:
    """Đọc content/images.yaml. Dùng PyYAML nếu có; nếu không, parser tối giản cho cấu trúc 2 cấp + list."""
    if not path.exists():
        return {"overrides": {}, "sensitive": []}
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        data = yaml.safe_load(text) or {}
    except ImportError:
        data = _mini_yaml(text)
    data.setdefault("overrides", {})
    data.setdefault("sensitive", [])
    return data


def _mini_yaml(text: str) -> dict:
    root: dict = {}
    cur_top = None
    cur_key = None
    for raw in text.splitlines():
        line = raw.split(" #")[0].rstrip() if not raw.strip().startswith("#") else ""
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        s = line.strip()
        if indent == 0 and s.endswith(":"):
            cur_top = s[:-1]
            root[cur_top] = {} if cur_top != "sensitive" else []
            cur_key = None
        elif indent == 2 and s.startswith("- "):
            root.setdefault(cur_top, []).append(_scalar(s[2:]))
        elif indent == 2 and s.endswith(":"):
            cur_key = s[:-1]
            root.setdefault(cur_top, {})[cur_key] = {}
        elif indent >= 4 and ":" in s and cur_key:
            k, v = s.split(":", 1)
            root[cur_top][cur_key][k.strip()] = _scalar(v.strip())
    return root


def _scalar(v: str):
    v = v.strip()
    if v in ("true", "True", "yes"):
        return True
    if v in ("false", "False", "no"):
        return False
    return v.strip('"\'')


# ============================================================ metadata

def meta_from_api(http: C.Http, title: str) -> dict | None:
    url = COMMONS_API + "?" + urllib.parse.urlencode({
        "action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|extmetadata|size|mime", "iiurlwidth": THUMB_WIDTH,
        "iiextmetadatafilter": "LicenseShortName|License|LicenseUrl|Artist|Credit|Attribution|AttributionRequired|Restrictions|DateTimeOriginal|ObjectName|ImageDescription",
        "format": "json"})
    status, data = http.get_json(url)
    if status != 200 or not data:
        return None
    for p in data.get("query", {}).get("pages", {}).values():
        if "missing" in p or "imageinfo" not in p:
            return {"missing": True}
        ii = p["imageinfo"][0]
        em = ii.get("extmetadata", {})

        def g(k):
            return strip_tags(em.get(k, {}).get("value", "")) if em.get(k) else ""
        return {"via": "api", "license_short": g("LicenseShortName"), "license_long": g("License"), "license_url": em.get("LicenseUrl", {}).get("value", ""),
                "author": g("Artist") or g("Credit"), "attribution": g("Attribution"), "attribution_required": g("AttributionRequired").lower() == "true",
                "restrictions": g("Restrictions"), "date": g("DateTimeOriginal"), "object_name": g("ObjectName"), "description": g("ImageDescription")[:300],
                "source_url": ii.get("descriptionurl", COMMONS_FILE + urllib.parse.quote(title.replace(" ", "_"))),
                "thumb_url": ii.get("thumburl"), "orig_url": ii.get("url"), "size": ii.get("size"), "mime": ii.get("mime"), "license_all": []}
    return None


def meta_from_html(http: C.Http, wd_http: C.Http, cache: C.JsonCache, title: str) -> dict | None:
    """Fallback khi api.php bị 429: trang File: (machine-readable licensetpl_*) + Structured Data on Commons (P275/P6216)."""
    page_url = COMMONS_FILE + urllib.parse.quote(title.replace(" ", "_"))
    status, body, _ = http.get(page_url, accept="text/html")
    if status == 404:
        return {"missing": True}
    if status != 200:
        return None
    s = html.unescape(body.decode("utf-8", "replace"))

    def cls_all(cls):
        return [strip_tags(x) for x in re.findall(r'class="%s"[^>]*>(.*?)</(?:span|td|div|p)>' % cls, s, re.S)]

    def row(fid):
        m = re.search(r'id="%s"[^>]*>.*?</td>\s*<td[^>]*>(.*?)</td>' % fid, s, re.S)
        return strip_tags(m.group(1))[:300] if m else ""
    shorts = [x for x in cls_all("licensetpl_short") if x]
    longs = [x for x in cls_all("licensetpl_long") if x]
    links = [x for x in cls_all("licensetpl_link") if x]
    attr_req = [x.lower() for x in cls_all("licensetpl_attr_req")]
    author = row("fileinfotpl_aut") or row("fileinfotpl_credit")
    if author.startswith(".mw-parser-output"):  # bảng creator có CSS inline
        author = re.sub(r"^\.mw-parser-output.*?\}\s*", "", author).strip()[:200]
    sdc = {}
    m = re.search(r'"wgArticleId":(\d+)', s)
    if m:
        st, data = http.get_json(f"https://commons.wikimedia.org/wiki/Special:EntityData/M{m.group(1)}.json")
        if st == 200 and data:
            ent = next(iter(data.get("entities", {}).values()), {})
            stm = ent.get("statements") or ent.get("claims") or {}
            ids = [c["mainsnak"]["datavalue"]["value"]["id"] for prop in ("P275", "P6216") for c in stm.get(prop, [])
                   if isinstance(c.get("mainsnak", {}).get("datavalue", {}).get("value"), dict) and "id" in c["mainsnak"]["datavalue"]["value"]]
            if ids:
                labels = C.wd_fetch(wd_http, cache, ids, ["en"])
                sdc = {q: (labels.get(q) or {}).get("labels", {}).get("en", q) for q in ids}
    restr = RESTRICT_HTML_RE.search(s)
    return {"via": "html", "license_short": shorts[0] if shorts else ("; ".join(sdc.values()) if sdc else ""), "license_long": longs[0] if longs else "",
            "license_url": links[0] if links else "", "license_all": shorts + longs + list(sdc.values()),
            "author": author, "attribution": "", "attribution_required": "true" in attr_req,
            "restrictions": restr.group(0) if restr else "", "restrictions_unverified": True,
            "date": row("fileinfotpl_date"), "object_name": "", "description": row("fileinfotpl_desc"),
            "source_url": page_url, "thumb_url": None, "orig_url": None, "size": None, "mime": None}


# ============================================================ chính sách §7.2

def classify_license(meta: dict) -> tuple[str, str]:
    """→ ('pd' | 'ccby' | 'none', nhãn giấy phép)."""
    cands = [meta.get("license_short", ""), meta.get("license_long", "")] + list(meta.get("license_all", []))
    parts = []
    for c in cands:
        for part in re.split(r"[;/]|\bor\b|\band\b", c or ""):
            part = part.strip()
            if part:
                parts.append(part)
    if not parts:
        return "none", "không rõ giấy phép"
    pd = [p for p in parts if PD_RE.search(p) and not BAD_RE.search(p)]
    if pd:
        return "pd", pd[0]
    cc = [p for p in parts if CCBY_RE.search(p) and not BAD_RE.search(p)]
    if cc:
        return "ccby", cc[0]
    return "none", parts[0]


def artwork_year(date_str: str) -> int | None:
    if not date_str:
        return None
    s = date_str.lower()
    m = re.search(r"\b(\d{3,4})\b", s)
    if m:
        y = int(m.group(1))
        if re.search(r"\b(bc|bce|tcn)\b", s):
            y = -y
        return y
    m = re.search(r"(\d{1,2})(?:st|nd|rd|th)?\s*century", s)
    if m:
        c = int(m.group(1))
        return -(c * 100 - 50) if re.search(r"\b(bc|bce)\b", s) else c * 100 - 50
    return None


def build_caption(person: dict, meta: dict, lic_label: str) -> tuple[str, bool, str]:
    """→ (chú thích, tưởng tượng?, ghi chú cho images-review). Quy tắc §7.3:
    "(tưởng tượng)" khi niên đại tác phẩm cách thời nhân vật > 100 năm, hoặc không rõ niên đại với nhân vật trước TK 15."""
    name = person["name_vi"]
    # mốc "thời nhân vật": năm mất; nếu không rõ thì cuối nhóm thế kỷ
    ref = person.get("died")
    if ref is None and not person.get("alive"):
        rng = C.group_range(person.get("group") or "")
        ref = rng[1] if rng else person.get("born")
    date_raw = meta.get("date", "")
    ay = artwork_year(date_raw)
    note = ""
    # DateTimeOriginal thường là ngày CHỤP (≥ 1826) chứ không phải niên đại tác phẩm → không tin với nhân vật tiền hiện đại
    if ay is not None and ay >= 1826 and ref is not None and ref < 1400:
        note = f"niên đại '{date_raw}' có vẻ là ngày chụp, không phải niên đại tác phẩm — bỏ khỏi chú thích; sửa tay nếu cần"
        ay = None
    imaginary = False
    if ref is not None and ay is not None and ay - ref > 100:
        imaginary = True
    elif ay is None and ref is not None and ref < 1400:
        imaginary = True
    desc = ""
    rng_m = re.search(r"(\d{3,4})\s*[–-]\s*(\d{3,4})", date_raw)
    if ay is not None and rng_m and ay >= 1000:
        desc = f"khoảng {rng_m.group(1)}–{rng_m.group(2)}"
    elif ay is not None:
        if re.search(r"century", date_raw, re.I):
            c = C.century_of(ay)
            desc = f"thế kỷ {abs(c)}{' TCN' if c < 0 else ''}"
        elif re.search(r"circa|\bc\.|\bca\.|khoảng|after|before|\?", date_raw, re.I):
            desc = f"khoảng {C.year_label(ay)}"
        else:
            desc = C.year_label(ay)
    obj = meta.get("object_name", "")
    parts = [f"Chân dung {name}"]
    if obj and C.norm_name(name) not in C.norm_name(obj) and len(obj) < 80:
        parts.append(obj)
    if desc:
        parts.append(desc)
    cap = ", ".join(parts) + (" (tưởng tượng)" if imaginary else "") + f". Ảnh: Wikimedia Commons, {lic_label}."
    return cap, imaginary, note


# ============================================================ tải

def md5_path(filename: str) -> str:
    h = hashlib.md5(filename.encode("utf-8")).hexdigest()
    return f"{h[0]}/{h[:2]}/{urllib.parse.quote(filename)}"


def thumb_name(filename: str, w: int) -> str:
    ext = filename.rsplit(".", 1)[-1].lower()
    base = f"{w}px-{filename}"
    if ext == "svg":
        return base + ".png"
    if ext in ("tif", "tiff", "pdf", "djvu"):
        return f"page1-{base}.jpg"
    return base


def out_ext(filename: str) -> str:
    ext = filename.rsplit(".", 1)[-1].lower()
    return {"svg": "png", "tif": "jpg", "tiff": "jpg", "pdf": "jpg", "djvu": "jpg", "jpeg": "jpg"}.get(ext, ext)


def download(http: C.Http, filename: str, dest: Path) -> tuple[bool, str, int]:
    w = min(ALLOWED_WIDTHS, key=lambda x: abs(x - THUMB_WIDTH))
    rel, tn = md5_path(filename), urllib.parse.quote(thumb_name(filename, w))
    for url in (f"{UPLOAD}/thumb/{rel}/{tn}", f"{THUMB_HOST}/thumb/{rel}/{tn}"):
        status, body, _ = http.get(url, accept="image/*")
        if status == 200 and len(body) > 500 and not body.lstrip().startswith(b"<"):
            dest.write_bytes(body)
            return True, f"thumbnail {w}px", w
    status, body, _ = http.get(f"{UPLOAD}/{rel}", accept="image/*")
    if status != 200 or len(body) < 500:
        return False, f"không tải được (HTTP {status})", 0
    if len(body) > MAX_ORIGINAL:
        return False, f"ảnh gốc {len(body) // 1024} KB vượt giới hạn", 0
    try:
        import io
        from PIL import Image
        im = Image.open(io.BytesIO(body))
        im.thumbnail((w, w * 2))
        if im.mode not in ("RGB", "L"):
            im = im.convert("RGB")
        im.save(dest, quality=88)
        return True, f"ảnh gốc thu nhỏ {w}px (Pillow)", w
    except Exception as e:  # noqa: BLE001
        dest.write_bytes(body)
        return False, f"ảnh gốc không thu nhỏ được ({e})", 0


# ============================================================ main

def load_persons() -> dict:
    pj = ROOT / "data" / "persons.json"
    if pj.exists():
        return json.loads(pj.read_text(encoding="utf-8"))["persons"]
    chapters = P.load_all(ROOT / "content")
    return {p["id"]: p for ch in chapters for g in ch["groups"] for p in g["persons"]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix", nargs="?", default="")
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--recaption", action="store_true", help="tính lại chú thích từ metadata đã lưu, không gọi mạng")
    a = ap.parse_args()

    persons = load_persons()
    yml = load_yaml(YAML_PATH)
    overrides, sensitive = yml.get("overrides") or {}, set(yml.get("sensitive") or [])
    images = json.loads(IMAGES_JSON.read_text(encoding="utf-8")) if IMAGES_JSON.exists() else {}
    cache = C.JsonCache(C.WD_CACHE)
    wd_http = C.Http(min_interval=1.0)
    http = C.Http(min_interval=1.5, max_retries=2)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    review: list[str] = []
    api_dead = False

    if a.recaption:
        n = 0
        for pid, rec in images.items():
            if rec.get("status") != "embedded" or pid not in persons:
                continue
            ov = overrides.get(pid, {}) if isinstance(overrides, dict) else {}
            meta = {"date": rec.get("artwork_date", ""), "object_name": rec.get("object_name", "")}
            cap, imaginary, cap_note = build_caption(persons[pid], meta, rec.get("license", ""))
            rec["caption"], rec["imaginary"] = ov.get("caption") or cap, imaginary
            if cap_note and not ov.get("caption"):
                review.append(f"[caption] {pid} {persons[pid]['name_vi']}: {cap_note}")
            n += 1
        IMAGES_JSON.write_text(json.dumps(images, ensure_ascii=False, indent=1), encoding="utf-8")
        REVIEW_TXT.write_text("IMAGES REVIEW — các mục cần Owner xem xét (sinh bởi fetch_images.py --recaption)\n\n" + ("\n".join(review) if review else "(không có)") + "\n", encoding="utf-8")
        print(f"Đã tính lại chú thích cho {n} ảnh → data/images.json")
        return 0
    stats = {"embedded": 0, "skip": 0, "review": 0, "no-license": 0, "no-image": 0, "fail": 0, "skipped": 0}

    for pid, p in sorted(persons.items()):
        if a.prefix and not pid.startswith(a.prefix):
            continue
        prev = images.get(pid)
        if prev and not a.refresh and (prev.get("status") != "embedded" or (IMG_DIR / prev.get("file", "")).exists()):
            stats["skip"] += 1
            continue
        ov = overrides.get(pid, {}) if isinstance(overrides, dict) else {}
        q = p.get("wikidata")
        rec = {"status": None, "title": None, "source_url": None, "note": "", "via": None}

        if ov.get("skip") or pid in sensitive or (q and q in sensitive):
            rec.update(status="skipped", note=ov.get("note") or "nhân vật nhạy cảm về hình tượng / bỏ ảnh theo images.yaml")
            if ov.get("file"):
                rec["note"] += f" (ảnh thay thế đề xuất: {ov['file']} — chưa tự động tải)"
            images[pid] = rec
            review.append(f"[skipped] {pid} {p['name_vi']}: {rec['note']}")
            stats["skipped"] += 1
            print(f"  - {pid}: bỏ ảnh ({rec['note'][:60]})")
            continue

        # 1. tên file
        title = ov.get("file")
        if not title and q and C.QID_RE.match(q):
            info = C.wd_fetch(wd_http, cache, [q]).get(q) or {}
            if info.get("P18"):
                title = "File:" + info["P18"]
        if not title:
            rec.update(status="no-image", note="không có Wikidata ID" if not q else "Wikidata không có P18")
            images[pid] = rec
            review.append(f"[no-image] {pid} {p['name_vi']}: {rec['note']} → đặt overrides.{pid}.file trong images.yaml nếu muốn")
            stats["no-image"] += 1
            print(f"  - {pid}: không có ảnh ({rec['note']})")
            continue
        if not title.startswith("File:"):
            title = "File:" + title
        filename = title[5:].replace(" ", "_")
        rec["title"] = title

        # 2. metadata
        meta = None
        if not api_dead:
            meta = meta_from_api(http, title)
            if meta is None:
                api_dead = True
                print("  [i] Commons API không trả lời (429/ lỗi) → chuyển sang đọc trang File + Structured Data")
        if meta is None:
            meta = meta_from_html(http, wd_http, cache, title)
        if meta is None or meta.get("missing"):
            rec.update(status="no-image", note=f"{title} không tồn tại hoặc không đọc được", source_url=COMMONS_FILE + urllib.parse.quote(filename))
            images[pid] = rec
            review.append(f"[missing] {pid} {p['name_vi']}: {rec['note']}")
            stats["fail"] += 1
            print(f"  - {pid}: {rec['note']}")
            continue
        rec.update(source_url=meta["source_url"], via=meta["via"], author=(meta.get("author") or "").strip()[:200],
                   license=None, license_url=meta.get("license_url", ""), artwork_date=meta.get("date", ""), object_name=meta.get("object_name", ""))

        # 3. chính sách
        kind, lic_label = classify_license(meta)
        if meta.get("restrictions"):
            rec.update(status="review", note=f"Restrictions: {meta['restrictions']}; giấy phép: {lic_label}", license=lic_label)
            images[pid] = rec
            review.append(f"[review] {pid} {p['name_vi']}: {title} — {rec['note']} → quyết định tay (overrides.{pid}.file hoặc skip)")
            stats["review"] += 1
            print(f"  - {pid}: CHỜ XEM XÉT ({rec['note'][:70]})")
            continue
        if kind == "none":
            rec.update(status="no-license", note=f"giấy phép không thuộc danh sách cho phép: {lic_label}", license=None)
            images[pid] = rec
            review.append(f"[no-license] {pid} {p['name_vi']}: {title} — {lic_label}")
            stats["no-license"] += 1
            print(f"  - {pid}: KHÔNG NHÚNG ({lic_label})")
            continue
        caption, imaginary, cap_note = build_caption(p, meta, lic_label)
        if ov.get("caption"):
            caption = ov["caption"]
        elif cap_note:
            review.append(f"[caption] {pid} {p['name_vi']}: {cap_note}")
        rec.update(license=lic_label, attribution_required=(kind == "ccby") or bool(meta.get("attribution_required")),
                   caption=caption, imaginary=imaginary)
        if meta.get("restrictions_unverified"):
            rec.update(status="review", license=lic_label,
                       note=f"đọc qua fallback (trang File) — KHÔNG xác minh được Restrictions; giấy phép: {lic_label}")
            images[pid] = rec
            review.append(f"[review] {pid} {p['name_vi']}: {title} — {rec['note']} → chạy lại khi Commons API trả lời, hoặc quyết định tay qua images.yaml")
            stats["review"] += 1
            print(f"  - {pid}: CHỜ XEM XÉT (không xác minh được Restrictions qua fallback)")
            continue
        if a.dry_run:
            print(f"  - {pid}: OK [{kind}] '{lic_label}' — {rec['author'] or '?'} — {caption[:70]} (dry-run)")
            stats["embedded"] += 1
            continue

        # 4. tải
        dest = IMG_DIR / f"{pid}.{out_ext(filename)}"
        ok, how, w = download(http, filename, dest)
        if not ok:
            rec.update(status="no-image", note=how)
            images[pid] = rec
            review.append(f"[download-failed] {pid} {p['name_vi']}: {title} — {how}")
            stats["fail"] += 1
            print(f"  - {pid}: {how}")
            continue
        rec.update(status="embedded", file=dest.name, width=w, how=how)
        images[pid] = rec
        stats["embedded"] += 1
        print(f"  - {pid}: OK [{kind}] '{lic_label}' — {rec['author'] or '?'} [{meta['via']}, {how}]{' (tưởng tượng)' if imaginary else ''}")

    if not a.dry_run:
        IMAGES_JSON.parent.mkdir(exist_ok=True)
        IMAGES_JSON.write_text(json.dumps(images, ensure_ascii=False, indent=1), encoding="utf-8")
        REVIEW_TXT.parent.mkdir(exist_ok=True)
        REVIEW_TXT.write_text("IMAGES REVIEW — các mục cần Owner xem xét (sinh bởi fetch_images.py)\n\n" + ("\n".join(review) if review else "(không có)") + "\n", encoding="utf-8")
    print(f"\nẢnh: {stats['embedded']} nhúng · {stats['skip']} đã có · {stats['review']} chờ xem xét · {stats['no-license']} thiếu giấy phép · "
          f"{stats['no-image']} không có ảnh · {stats['skipped']} bỏ theo yaml · {stats['fail']} lỗi → data/images.json, reports/images-review.txt. Chạy lại `python build.py`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
