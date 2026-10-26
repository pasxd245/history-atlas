"""Lint theo PLAN §6.2. ERROR chặn build; WARN không chặn. Ghi reports/lint-chXX.txt."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from . import common as C

WORD_TARGET = {"ideas": 100, "why": 80, "intro": 100, "context": 60}


def words(s: str) -> int:
    return len([w for w in s.split() if w])


class Report:
    def __init__(self):
        self.items: list[tuple[str, str, str]] = []

    def error(self, where, msg): self.items.append(("ERROR", where, msg))
    def warn(self, where, msg): self.items.append(("WARN", where, msg))
    def info(self, where, msg): self.items.append(("INFO", where, msg))

    def count(self, level): return sum(1 for l, _, _ in self.items if l == level)
    def by_level(self, level): return [(w, m) for l, w, m in self.items if l == level]


def lint_chapter(ch: dict, all_persons: dict[str, dict], images: dict | None, rep: Report):
    no = ch["no"]
    w = f"ch{no:02d}" if no is not None else "ch??"
    for _, msg in ch["parse_errors"]:
        rep.error(w, msg)
    if no is None:
        rep.error(w, "thiếu dòng '# Chapter N · Tên'")
        return
    is_sample = no == C.SAMPLE_CHAPTER_NO
    if not is_sample and no not in C.CHAPTER_BY_NO:
        rep.error(w, f"chapter {no} không có trong PLAN §4")
    if not ch["intro"]:
        rep.error(w, "thiếu 'Giới thiệu chapter'")
    elif words(ch["intro"]) > 130:
        rep.warn(w, f"'Giới thiệu chapter' {words(ch['intro'])} chữ (≤ 100)")
    if not ch["editorial"]:
        rep.error(w, "thiếu '## Ghi chú biên tập'")
    else:
        txt = C.norm_name(" ".join(ch["editorial"]))
        if "viet" not in txt and "vietnam" not in txt:
            rep.warn(w, "Ghi chú biên tập không nhắc ứng viên Việt Nam (D5 yêu cầu nêu, kể cả khi không có)")

    allowed_groups = set(C.CHAPTER_BY_NO[no]["groups"]) if no in C.CHAPTER_BY_NO else None
    for g in ch["groups"]:
        gw = f"{w}/{g['id']}"
        rng = C.group_range(g["id"])
        if rng is None:
            rep.error(gw, "ID nhóm sai quy ước (BCE05 / CE18 / BCE20_18)")
        elif allowed_groups is not None and g["id"] not in allowed_groups:
            rep.error(gw, f"nhóm không thuộc chapter {no} (cho phép: {', '.join(sorted(allowed_groups))})")
        if not g["context"]:
            rep.warn(gw, "thiếu 'Bối cảnh'")
        elif words(g["context"]) > 80:
            rep.warn(gw, f"'Bối cảnh' {words(g['context'])} chữ (≤ 60)")
        if len(g["persons"]) > C.PROJECT["max_per_group"]:
            rep.error(gw, f"{len(g['persons'])} nhân vật (> {C.PROJECT['max_per_group']})")
        if not g["persons"]:
            rep.warn(gw, "nhóm rỗng")
        fields = Counter(f for p in g["persons"] for f in p["fields"])
        regions = Counter(p["region"] for p in g["persons"] if p["region"])
        if g["persons"] and len(fields) < 4:
            rep.warn(gw, f"chỉ {len(fields)} lĩnh vực (khuyến nghị ≥ 4)")
        if g["persons"] and len(regions) < 3:
            rep.warn(gw, f"chỉ {len(regions)} vùng (khuyến nghị ≥ 3)")

        for p in g["persons"]:
            pw = f"{w}/{p['id']}"
            m = C.ID_RE.match(p["id"])
            if not m:
                rep.error(pw, "ID sai quy ước CHxx-GROUP-nn")
            else:
                if int(m.group(1)) != no:
                    rep.error(pw, f"ID mang số chapter {m.group(1)} ≠ {no:02d}")
                if m.group(2) != g["id"]:
                    rep.error(pw, f"ID mang nhóm {m.group(2)} nhưng nằm trong nhóm {g['id']}")
            if not p["name_vi"]:
                rep.error(pw, "thiếu tên")
            if not p["name_orig"]:
                rep.warn(pw, "thiếu tên gốc trong ngoặc")
            if not p["meta_raw"]:
                rep.error(pw, "thiếu dòng metadata trong dấu `…`")
            else:
                for k, lbl in (("years_raw", "năm"), ("place", "nơi"), ("region", "vùng"), ("confidence", "độ tin cậy niên đại")):
                    if not p.get(k):
                        rep.error(pw, f"metadata thiếu '{lbl}'")
                if not p["fields"]:
                    rep.error(pw, "metadata thiếu 'lĩnh vực'")
                if not p["big_questions"]:
                    rep.error(pw, "metadata thiếu 'câu hỏi lớn'")
                if "wikidata" not in p["meta_raw"].lower():
                    rep.error(pw, "metadata thiếu 'wikidata'")
            if p["region"] and p["region"] not in C.REGIONS:
                rep.error(pw, f"vùng '{p['region']}' ngoài từ vựng")
            for f in p["fields"]:
                if f not in C.FIELDS:
                    rep.error(pw, f"lĩnh vực '{f}' ngoài từ vựng")
            if len(p["fields"]) > 2:
                rep.error(pw, f"{len(p['fields'])} lĩnh vực (tối đa 2)")
            for q in p["big_questions"]:
                if q not in C.BIG_QUESTIONS:
                    rep.error(pw, f"câu hỏi lớn '{q}' ngoài từ vựng")
            if len(p["big_questions"]) > 2:
                rep.error(pw, f"{len(p['big_questions'])} câu hỏi lớn (tối đa 2)")
            if p["confidence"] and p["confidence"] not in C.CONFIDENCE:
                rep.error(pw, f"độ tin cậy '{p['confidence']}' ngoài từ vựng")
            if p["wikidata"] is None:
                rep.warn(pw, "wikidata: ? — không đối chiếu được niên đại")
            elif not C.QID_RE.match(p["wikidata"]):
                rep.error(pw, f"wikidata '{p['wikidata']}' sai dạng Q123")
            if p["years_raw"] and not p["years_ok"]:
                rep.warn(pw, f"không phân tích được 'năm: {p['years_raw']}' — ghi dạng 'sinh–mất [TCN]'")
            if p["born"] is not None and p["died"] is not None and p["died"] < p["born"]:
                rep.error(pw, f"năm mất ({p['died']}) trước năm sinh ({p['born']})")
            if rng and p["years_ok"]:
                b, d = p["born"], p["died"] if p["died"] is not None else C.PROJECT["reference_year"]
                if d < rng[0] or b > rng[1]:
                    rep.warn(pw, f"đời sống {C.year_label(b)}–{C.year_label(d)} không giao với nhóm {g['id']} ({C.year_label(rng[0])}–{C.year_label(rng[1])})")
            if p["alive"]:
                rep.info(pw, "người còn sống — đã kiểm tra ảnh hưởng ≥ 10 năm? (D4)")
            for k in ("ideas", "why"):
                if not p[k]:
                    rep.error(pw, f"thiếu '{'Tư tưởng / đóng góp chính' if k == 'ideas' else 'Vì sao chọn'}'")
                else:
                    n, t = words(p[k]), WORD_TARGET[k]
                    if abs(n - t) > 0.3 * t:
                        rep.warn(pw, f"'{k}' {n} chữ, lệch > 30% so với ~{t}")
            if not p["sources"]:
                rep.error(pw, "thiếu 'Nguồn'")
            for kind in ("inherits", "influences"):
                links = p[kind]
                if not links:
                    rep.error(pw, f"thiếu '{'Kế thừa từ' if kind == 'inherits' else 'Ảnh hưởng tới'}' (nếu không rõ ghi '- Không xác định')")
                    continue
                real = [l for l in links if not l["undetermined"]]
                if len(real) > 3:
                    rep.warn(pw, f"'{kind}' có {len(real)} mục (tối đa 3)")
                for l in real:
                    if l["relation"] not in C.RELATION_TYPES:
                        rep.error(pw, f"loại quan hệ '{l['relation']}' ngoài từ vựng ({l['raw'][:50]})")
                    if l["evidence"] not in C.EVIDENCE_LEVELS:
                        rep.error(pw, f"mức bằng chứng '{l['evidence']}' ngoài từ vựng ({l['raw'][:50]})")
                    t = l["target"]
                    if C.ID_RE.match(t) and t not in all_persons:
                        rep.warn(pw, f"liên kết tới ID chưa tồn tại: {t}")
                    if t == p["id"]:
                        rep.error(pw, "liên kết tới chính mình")
            # ảnh nhúng phải có giấy phép (§6.2)
            if images and p["id"] in images.get("images", {}):
                im = images["images"][p["id"]]
                if im.get("embed") and not im.get("license"):
                    rep.error(pw, f"ảnh {im.get('file')} được nhúng nhưng không có thông tin giấy phép")


def lint_global(chapters: list[dict], all_persons: dict[str, dict], rep: Report):
    seen_ids: dict[str, str] = {}
    by_name: dict[str, list[str]] = {}
    by_q: dict[str, list[str]] = {}
    for ch in chapters:
        for g in ch["groups"]:
            for p in g["persons"]:
                if p["id"] in seen_ids:
                    rep.error(p["id"], f"ID trùng ({seen_ids[p['id']]} và {p['file']})")
                seen_ids[p["id"]] = p["file"]
                by_name.setdefault(C.norm_name(p["name_vi"]), []).append(p["id"])
                if p["wikidata"]:
                    by_q.setdefault(p["wikidata"], []).append(p["id"])
    for k, ids in by_name.items():
        if len(ids) > 1 and len({i[:4] for i in ids}) > 1:
            rep.warn(ids[0], f"cùng tên xuất hiện ở nhiều chapter: {', '.join(ids)}")
    for q, ids in by_q.items():
        if len(ids) > 1:
            rep.warn(ids[0], f"cùng Wikidata {q} ở nhiều mục: {', '.join(ids)}")
    # liên kết một chiều (kiểm tra đầy đủ ở P4)
    for p in all_persons.values():
        for l in p["inherits"]:
            t = l["target"]
            if t in all_persons and not any(x["target"] == p["id"] for x in all_persons[t]["influences"]):
                rep.info(p["id"], f"kế thừa từ {t} nhưng {t} không ghi 'Ảnh hưởng tới' {p['id']} (P4 sẽ đồng bộ)")


def lint_wikidata(all_persons: dict[str, dict], rep: Report, http: C.Http | None = None):
    qids = sorted({p["wikidata"] for p in all_persons.values() if p["wikidata"] and C.QID_RE.match(p["wikidata"])})
    if not qids:
        return
    cache = C.JsonCache(C.WD_CACHE)
    http = http or C.Http(min_interval=1.0)
    ents = C.wd_fetch(http, cache, qids)
    for p in all_persons.values():
        q = p["wikidata"]
        if not q or not C.QID_RE.match(q):
            continue
        pw = p["id"]
        info = ents.get(q)
        if not info or "error" in info:
            rep.warn(pw, f"Wikidata {q}: không lấy được ({(info or {}).get('error')})")
            continue
        names = C.wd_names(info)
        mine = {C.norm_name(p["name_vi"]), C.norm_name(p["name_orig"])}
        mine |= {C.norm_name(x) for x in p["name_orig"].replace("/", ",").split(",")}
        mine = {m for m in mine if m}
        if not (names & mine) and not any(m in n or n in m for m in mine for n in names if len(m) > 3):
            lbl = info["labels"].get("vi") or info["labels"].get("en") or "?"
            rep.warn(pw, f"nhãn Wikidata {q} = '{lbl}' không khớp tên '{p['name_vi']}' — kiểm tra Q-ID")
        if info["P31"] and "Q5" not in info["P31"] and not p["labels"]:
            rep.warn(pw, f"Wikidata {q} không phải người (P31={info['P31'][:3]}) — cần nhãn [Truyền thuyết]?")
        tol = C.DATE_TOLERANCE.get(p["confidence"])
        if tol is None:
            rep.info(pw, "độ tin cậy Thấp — bỏ qua đối chiếu niên đại")
            continue
        for label, mine_y, wd in (("năm sinh", p["born"], info["P569"]), ("năm mất", p["died"], info["P570"])):
            if mine_y is None or not wd:
                continue
            best = None
            for it in wd:
                if it["year"] is None:
                    continue
                t = tol
                if it["precision"] <= 7:
                    t = max(t, 60)
                elif it["precision"] == 8:
                    t = max(t, 12)
                d = abs(it["year"] - mine_y)
                if best is None or d < best[0]:
                    best = (d, it["year"], t, it["precision"])
            if best and best[0] > best[2]:
                rep.warn(pw, f"{label}: atlas {C.year_label(mine_y)} ≠ Wikidata {C.year_label(best[1])} (lệch {best[0]} > {best[2]} năm, độ tin cậy {p['confidence']})")
        if p["alive"] and info["P570"]:
            rep.warn(pw, f"ghi còn sống nhưng Wikidata có năm mất {C.year_label(info['P570'][0]['year'])}")


def write_reports(chapters: list[dict], rep: Report, reports_dir: Path):
    reports_dir.mkdir(parents=True, exist_ok=True)
    for ch in chapters:
        if ch["no"] is None:
            continue
        tag = f"ch{ch['no']:02d}"
        mine = [(l, w, m) for l, w, m in rep.items if w.startswith(tag) or w.startswith(f"CH{ch['no']:02d}-")]
        lines = [f"LINT {tag} — {ch['title']} ({', '.join(ch['files'])})",
                 f"ERROR {sum(1 for l, _, _ in mine if l == 'ERROR')} · WARN {sum(1 for l, _, _ in mine if l == 'WARN')} · INFO {sum(1 for l, _, _ in mine if l == 'INFO')}", ""]
        for level in ("ERROR", "WARN", "INFO"):
            for l, w, m in mine:
                if l == level:
                    lines.append(f"[{l}] {w}: {m}")
        (reports_dir / f"lint-{tag}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(chapters: list[dict], images: dict | None, online: bool, reports_dir: Path, http: C.Http | None = None) -> Report:
    rep = Report()
    all_persons = {p["id"]: p for ch in chapters for g in ch["groups"] for p in g["persons"]}
    for ch in chapters:
        lint_chapter(ch, all_persons, images, rep)
    lint_global(chapters, all_persons, rep)
    if online:
        if rep.count("ERROR") == 0:
            lint_wikidata(all_persons, rep, http)
        else:
            rep.info("lint", "bỏ qua đối chiếu Wikidata vì còn lỗi cấu trúc")
    write_reports(chapters, rep, reports_dir)
    return rep
