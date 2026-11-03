"""Hằng số dùng chung (PLAN §4, §5), tiện ích năm/thế kỷ, HTTP lịch sự với Wikimedia, cache JSON.

Chỉ dùng thư viện chuẩn. Python 3.11+.
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROJECT = {
    "title": "Atlas nhân vật ảnh hưởng",
    "subtitle": "Những người định hình tư tưởng nhân loại, 2000 TCN – 2026",
    "version": "P2",
    "start_year": -2000,
    "end_year": 2026,
    "reference_year": 2026,
    "max_per_group": 12,
    "living_min_influence_years": 10,
    "user_agent": "history-atlas/0.1 (research)",
}

# ---- PLAN §4: chapter → nhóm. Nhóm = 1 thế kỷ, trước TK 8 TCN gộp 3 thế kỷ.
CHAPTERS = [
    {"no": 1,  "title": "Văn minh cổ đại sớm",                    "label": "2000–801 TCN", "groups": ["BCE20_18", "BCE17_15", "BCE14_12", "BCE11_9"]},
    {"no": 2,  "title": "Thời kỳ Trục – Axial Age",               "label": "TK 8–5 TCN",   "groups": ["BCE08", "BCE07", "BCE06", "BCE05"]},
    {"no": 3,  "title": "Hellenistic, Tần–Hán, Maurya",           "label": "TK 4–1 TCN",   "groups": ["BCE04", "BCE03", "BCE02", "BCE01"]},
    {"no": 4,  "title": "Đế chế cổ điển, tôn giáo lan tỏa",       "label": "TK 1–5",       "groups": ["CE01", "CE02", "CE03", "CE04", "CE05"]},
    {"no": 5,  "title": "Hồi giáo, nhà Đường, Islamic Golden Age", "label": "TK 6–10",      "groups": ["CE06", "CE07", "CE08", "CE09", "CE10"]},
    {"no": 6,  "title": "Tống, Trung cổ, Mông Cổ, Lý–Trần",       "label": "TK 11–14",     "groups": ["CE11", "CE12", "CE13", "CE14"]},
    {"no": 7,  "title": "Phục Hưng, Khám phá, Cải cách",          "label": "TK 15–16",     "groups": ["CE15", "CE16"]},
    {"no": 8,  "title": "Cách mạng khoa học, Khai sáng",          "label": "TK 17–18",     "groups": ["CE17", "CE18"]},
    {"no": 9,  "title": "Cách mạng công nghiệp",                  "label": "TK 19",        "groups": ["CE19"]},
    {"no": 10, "title": "Thế kỷ 20",                              "label": "TK 20",        "groups": ["CE20"]},
    {"no": 11, "title": "Thế kỷ 21 (đến 2026)",                   "label": "TK 21",        "groups": ["CE21"]},
]

# ---- Phụ lục: track riêng, KHÔNG tính vào thống kê/độ phủ toàn cục.
# Tiêu chí (a)-(d) giữ nguyên nhưng hệ quy chiếu là Việt Nam + Đông Nam Á, không phải nhân loại —
# đó là lý do phụ lục tách khỏi atlas chính chứ không trộn vào.
# ID nhóm đều là dạng gộp nhiều thế kỷ, không trùng nhóm nào của 11 chapter chính.
APPENDICES = [
    {"no": 90, "title": "Phụ lục · Việt Nam qua các thời kỳ", "label": "TK 3 TCN – TK 20", "track": "vn", "num_label": "VN",
     "groups": ["BCE03_01", "CE01_09", "CE10_14", "CE15_18", "CE19_20"]},
]
for _c in CHAPTERS:
    _c.setdefault("track", "main")
ALL_CHAPTERS = CHAPTERS + APPENDICES

CHAPTER_BY_NO = {c["no"]: c for c in ALL_CHAPTERS}
GROUP_TO_CHAPTER = {g: c["no"] for c in ALL_CHAPTERS for g in c["groups"]}
SAMPLE_CHAPTER_NO = 0  # content/ch00-sample.md — chỉ dùng ở P1


def track_of(no: int | None) -> str:
    """Track của chapter: 'main' cho 11 chapter PLAN §4, 'vn' cho phụ lục Việt Nam."""
    return CHAPTER_BY_NO.get(no, {}).get("track", "main")


def is_main(no: int | None) -> bool:
    return track_of(no) == "main"

# ---- PLAN §5: từ vựng cố định
FIELDS = ["Triết học", "Tôn giáo/Tâm linh", "Toán học", "Khoa học tự nhiên", "Y học", "Kỹ thuật/Công nghệ",
          "Chính trị/Nhà nước", "Quân sự", "Luật", "Kinh tế", "Văn học", "Nghệ thuật/Kiến trúc", "Sử học", "Khám phá/Địa lý",
          "Giáo dục", "Ngôn ngữ học"]
REGIONS = ["Đông Á", "Nam Á", "Đông Nam Á", "Trung Đông/Bắc Phi", "Châu Phi hạ Sahara", "Châu Âu", "Châu Mỹ", "Trung Á", "Châu Đại Dương"]
BIG_QUESTIONS = ["Vũ trụ", "Con người", "Thực tại", "Không áp dụng"]
CONFIDENCE = ["Cao", "Trung bình", "Thấp"]
RELATION_TYPES = ["kế thừa", "tổng hợp", "phản bác", "tương đồng độc lập"]
EVIDENCE_LEVELS = ["trực tiếp", "qua trường phái", "suy đoán học giả"]
LABELS = ["Truyền thuyết", "Tranh cãi lịch sử"]
# dung sai lint niên đại theo độ tin cậy (PLAN §6.2)
DATE_TOLERANCE = {"Cao": 5, "Trung bình": 25, "Thấp": None}

ID_RE = re.compile(r"^CH(\d{2})-((?:BCE|CE)\d{2}(?:_\d{1,2})?)-(\d{2})$")
GROUP_RE = re.compile(r"^(BCE|CE)(\d{2})(?:_(\d{1,2}))?$")
QID_RE = re.compile(r"^Q\d+$")


# ============================================================ năm / thế kỷ

def group_range(gid: str) -> tuple[int, int] | None:
    """BCE05 → (-500, -401); CE18 → (1701, 1800); BCE20_18 → (-2000, -1701)."""
    m = GROUP_RE.match(gid)
    if not m:
        return None
    era, a, b = m.group(1), int(m.group(2)), m.group(3)
    b = int(b) if b else a
    if era == "CE":
        lo, hi = min(a, b), max(a, b)
        return (lo - 1) * 100 + 1, hi * 100
    hi_c, lo_c = max(a, b), min(a, b)  # TK 20 TCN → -2000..-1901
    return -hi_c * 100, -(lo_c - 1) * 100 - 1


def group_label(gid: str) -> str:
    m = GROUP_RE.match(gid)
    if not m:
        return gid
    era, a, b = m.group(1), int(m.group(2)), m.group(3)
    s = f"TK {a}" + (f"–{int(b)}" if b else "")
    return s + (" TCN" if era == "BCE" else "")


def century_of(year: int) -> int:
    if year > 0:
        return (year - 1) // 100 + 1
    if year < 0:
        return -((-year - 1) // 100 + 1)
    return 1


def year_label(y: int | None) -> str:
    if y is None:
        return "?"
    return f"{abs(y)} TCN" if y < 0 else str(y)


_APPROX_RE = re.compile(r"\b(k\.|kh\.|khoảng|c\.|ca\.|circa|fl\.|~|≈)", re.I)


# 'năm:' ghi theo thời gian trị vì hoặc theo floruit — các số trong đó không phải
# năm sinh–mất, nên không đối chiếu được với P569/P570 của Wikidata.
NON_BIO_YEARS_RE = re.compile(r"^(trị vì|hoạt động)\b", re.I)


def year_in_bucket(year: int, wd_year: int, precision: int) -> bool:
    """Giá trị Wikidata ở mức thế kỷ (p7) hoặc thiên niên kỷ (p6) là một KHOẢNG.
    Trả True nếu `year` nằm trong khoảng mà `wd_year` đại diện.

    +0300/p7 → thế kỷ 3 CN → 201..300;  -1300/p7 → thế kỷ 13 TCN → -1300..-1201.
    """
    size = 1000 if precision <= 6 else 100
    if wd_year > 0:
        hi = ((wd_year + size - 1) // size) * size
        return hi - size + 1 <= year <= hi
    lo = -(((-wd_year) + size - 1) // size) * size
    return lo <= year <= lo + size - 1


def parse_years(s: str) -> dict:
    """Phân tích chuỗi `năm:` tự do → {born, died, approx, alive, ok}.

    Chấp nhận: "551–479 TCN", "k. 470 – 399 TCN", "63 TCN – 14", "1643–1727", "1928–nay", "1928–",
    "c. 563 – c. 483 TCN", "TK 6 TCN" (→ born/died None, ok False), "?".
    """
    raw = s.strip()
    out = {"born": None, "died": None, "approx": bool(_APPROX_RE.search(raw)), "alive": False, "ok": False, "raw": raw}
    if not raw or raw in ("?", "không rõ"):
        return out
    if re.search(r"\b(TK|thế kỷ|century|thiên niên kỷ)\b", raw, re.I):
        return out  # chỉ có thế kỷ, không có năm → không đối chiếu được
    txt = raw.replace("—", "–").replace("--", "–").replace(" - ", " – ")
    if re.search(r"\b(nay|hiện tại|còn sống|present)\b", txt, re.I) or re.search(r"\d\s*[–-]\s*$", txt):
        out["alive"] = True
    # tách hai vế quanh dấu gạch dài
    parts = re.split(r"\s*–\s*|(?<=\d)\s*-\s*(?=\d|$)", txt, maxsplit=1)
    def side(p: str) -> tuple[int | None, bool | None]:
        """→ (năm, có 'TCN' trong vế này?) ; None nếu không có số."""
        if p is None:
            return None, None
        m = re.search(r"(\d{1,4})", p)
        if not m:
            return None, None
        bce = bool(re.search(r"TCN|BCE?\b|tr\.?\s*CN", p, re.I))
        return int(m.group(1)), bce
    b, b_bce = side(parts[0])
    d, d_bce = side(parts[1] if len(parts) > 1 else None)
    if b is None and d is None:
        return out
    # quy tắc TCN: nếu chỉ vế sau có TCN → cả hai TCN; nếu chỉ vế trước có → chỉ vế trước
    if d is not None:
        if d_bce and not b_bce:
            b_bce = True
        if b is not None:
            out["born"] = -b if b_bce else b
        out["died"] = -d if d_bce else d
    else:
        out["born"] = -b if b_bce else b
    if out["alive"]:
        out["died"] = None
    out["ok"] = out["born"] is not None and (out["died"] is not None or out["alive"])
    return out


def norm_name(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    s = s.replace("đ", "d").replace("Đ", "D")
    return re.sub(r"[^a-z0-9㐀-鿿]+", " ", s.lower()).strip()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", norm_name(s)).strip("-")


# ============================================================ HTTP

class Http:
    """GET với User-Agent rõ ràng, giãn cách tối thiểu, tôn trọng Retry-After, backoff mũ."""

    def __init__(self, user_agent: str = PROJECT["user_agent"], min_interval: float = 1.0, max_retries: int = 4, verbose: bool = True):
        self.ua, self.min_interval, self.max_retries, self.verbose = user_agent, min_interval, max_retries, verbose
        self._last = 0.0

    def get(self, url: str, accept: str = "*/*", timeout: int = 60) -> tuple[int, bytes, dict]:
        delay = 2.0
        for attempt in range(self.max_retries + 1):
            dt = time.time() - self._last
            if dt < self.min_interval:
                time.sleep(self.min_interval - dt)
            req = urllib.request.Request(url, headers={"User-Agent": self.ua, "Accept": accept})
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    self._last = time.time()
                    return r.status, r.read(), dict(r.headers)
            except urllib.error.HTTPError as e:
                self._last = time.time()
                body = e.read() if e.fp else b""
                if (e.code == 429 or e.code >= 500) and attempt < self.max_retries:
                    ra = e.headers.get("Retry-After")
                    wait = min(max(float(ra) if ra and ra.isdigit() else delay, 1.0), 60.0)
                    if self.verbose:
                        print(f"    [http] {e.code} {url[:70]}… chờ {wait:.0f}s ({attempt + 1}/{self.max_retries})", file=sys.stderr)
                    time.sleep(wait)
                    delay *= 2
                    continue
                return e.code, body, dict(e.headers)
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                self._last = time.time()
                if attempt < self.max_retries:
                    if self.verbose:
                        print(f"    [http] lỗi mạng {e} — chờ {delay:.0f}s", file=sys.stderr)
                    time.sleep(delay)
                    delay *= 2
                    continue
                return 0, b"", {}
        return 0, b"", {}

    def get_json(self, url: str):
        status, body, _ = self.get(url, accept="application/json")
        if status != 200:
            return status, None
        try:
            return status, json.loads(body.decode("utf-8"))
        except json.JSONDecodeError:
            return status, None


class JsonCache:
    def __init__(self, path: Path):
        self.path = path
        self.data: dict = {}
        if path.exists():
            try:
                self.data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, ensure_ascii=False, indent=1), encoding="utf-8")


# ============================================================ Wikidata

WD_API = "https://www.wikidata.org/w/api.php"
WD_CACHE = ROOT / "data" / "wikidata-cache.json"


def wd_time_to_year(t: str) -> int | None:
    m = re.match(r"^([+-])(\d{1,16})-", t)
    if not m:
        return None
    y = int(m.group(2))
    return -y if m.group(1) == "-" else y


def _extract(entity: dict) -> dict:
    claims = entity.get("claims", {})

    def times(prop):
        out = []
        for c in claims.get(prop, []):
            dv = c.get("mainsnak", {}).get("datavalue", {}).get("value")
            if isinstance(dv, dict) and "time" in dv:
                out.append({"year": wd_time_to_year(dv["time"]), "precision": dv.get("precision", 9), "rank": c.get("rank", "normal")})
        out.sort(key=lambda x: 0 if x["rank"] == "preferred" else 1)
        return out

    def items(prop):
        return [c["mainsnak"]["datavalue"]["value"]["id"] for c in claims.get(prop, [])
                if isinstance(c.get("mainsnak", {}).get("datavalue", {}).get("value"), dict) and "id" in c["mainsnak"]["datavalue"]["value"]]

    def string(prop):
        for c in claims.get(prop, []):
            dv = c.get("mainsnak", {}).get("datavalue", {}).get("value")
            if isinstance(dv, str):
                return dv
        return None

    sl = entity.get("sitelinks", {})
    return {
        "id": entity.get("id"),
        "labels": {k: v["value"] for k, v in entity.get("labels", {}).items()},
        "aliases": {k: [a["value"] for a in v] for k, v in entity.get("aliases", {}).items()},
        "P31": items("P31"), "P279": items("P279"), "P569": times("P569"), "P570": times("P570"), "P18": string("P18"),
        "sitelinks": {k: sl[k]["title"] for k in ("viwiki", "enwiki") if k in sl},
        "fetched": int(time.time()),
    }


def wd_fetch(http: Http, cache: JsonCache, qids: list[str], languages=("vi", "en")) -> dict[str, dict | None]:
    """{qid: info}; info có 'error' nếu không lấy được. Cache theo 'wd:Q…'."""
    result, todo = {}, []
    for q in qids:
        if not QID_RE.match(q):
            result[q] = {"error": "bad-id"}
            continue
        c = cache.get(f"wd:{q}")
        if c is not None and "error" not in c:
            result[q] = c
        else:
            todo.append(q)
    for i in range(0, len(todo), 50):
        batch = todo[i:i + 50]
        url = WD_API + "?" + urllib.parse.urlencode({"action": "wbgetentities", "ids": "|".join(batch),
                                                     "props": "labels|aliases|claims|sitelinks", "languages": "|".join(languages),
                                                     "sitefilter": "viwiki|enwiki", "format": "json"})
        status, data = http.get_json(url)
        if status != 200 or not data or "entities" not in data:
            for q in batch:
                result[q] = {"error": f"HTTP {status}"}
            continue
        for q, ent in data["entities"].items():
            info = {"error": "missing"} if "missing" in ent else _extract(ent)
            cache.set(f"wd:{q}", info)
            result[q] = info
    cache.save()
    return result


def wd_names(info: dict) -> set[str]:
    names = {norm_name(v) for v in info.get("labels", {}).values()}
    for al in info.get("aliases", {}).values():
        names |= {norm_name(a) for a in al}
    # Một số mục không có nhãn vi lẫn en (vd Q379887 Olaudah Equiano chỉ có nhãn ar và zh),
    # nên so tên chỉ bằng labels/aliases thì báo lệch dù Q-ID đúng. Tiêu đề bài Wikipedia
    # cũng là một tên của thực thể, và wd_fetch đã lấy sẵn viwiki|enwiki, nên dùng luôn.
    names |= {norm_name(v) for v in info.get("sitelinks", {}).values()}
    return {n for n in names if n}
