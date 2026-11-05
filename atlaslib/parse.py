"""Parser for content/chXX.md against the fixed template in PLAN §5.

The template is strict: there are no free-form sections, and a structural deviation is an error
rather than something the parser guesses at.

Returned structure (plain dicts, so they dump straight to persons.json):

chapter = {
  "no": 2, "title": "...", "intro": "...", "files": [...],
  "groups": [ {"id": "BCE06", "heading": "...", "context": "...", "persons": [...], "line": n} ],
  "editorial": ["- ...", ...]            # các mục Ghi chú biên tập (giữ nguyên markdown)
  "parse_errors": [(line, msg)]          # lỗi cấu trúc thô (thiếu heading, metadata sai…)
}
person = {
  "id": "CH02-BCE06-01", "name_vi": "...", "name_orig": "...", "labels": ["Truyền thuyết"],
  "meta_raw": "...", "years_raw": "...", "born": -551, "died": -479, "approx": False, "alive": False, "years_ok": True,
  "place": "...", "region": "...", "fields": [...], "confidence": "Cao", "wikidata": "Q4604" | None, "big_questions": [...],
  "ideas": "...", "why": "...", "sources": "...",
  "inherits": [{"target": "...", "relation": "...", "evidence": "...", "raw": "..."}], "influences": [...],
  "group": "BCE06", "chapter": 2, "line": n, "file": "ch02.md"
}
"""
from __future__ import annotations

import re
from pathlib import Path

from . import common as C

H1_RE = re.compile(r"^#\s+Chapter\s+(\d+)\s*[·•:–-]\s*(.+?)\s*$", re.I)
H2_GROUP_RE = re.compile(r"^##\s+Nhóm\s+([A-Z0-9_]+)\s*(?:[·•:–-]\s*(.*))?$", re.I)
H2_NOTE_RE = re.compile(r"^##\s+Ghi chú biên tập\s*$", re.I)
H3_RE = re.compile(r"^###\s+(CH\d{2}-[A-Z0-9_]+-\d{2})\s*[·•:–-]\s*(.+?)\s*$")
BOLD_RE = re.compile(r"^\*\*([^*]+?)\s*(?:\([^)]*\))?\s*:\*\*\s*(.*)$")
META_RE = re.compile(r"^`(.+)`\s*$")
LABEL_RE = re.compile(r"\s*\[(Truyền thuyết|Tranh cãi lịch sử)\]", re.I)

# khoá bold → trường. So khớp theo tiền tố đã chuẩn hoá.
BOLD_KEYS = [
    ("gioi thieu chapter", "intro"),
    ("boi canh", "context"),
    ("tu tuong", "ideas"),
    ("dong gop", "ideas"),
    ("vi sao chon", "why"),
    ("ke thua tu", "inherits"),
    ("anh huong toi", "influences"),
    ("nguon", "sources"),
]
META_KEYS = {
    "nam": "years_raw", "noi": "place", "vung": "region", "linh vuc": "fields",
    "do tin cay nien dai": "confidence", "do tin cay": "confidence", "wikidata": "wikidata", "cau hoi lon": "big_questions",
}


def _key(s: str) -> str:
    return C.norm_name(s)


def _bold_field(label: str) -> str | None:
    k = _key(label)
    for prefix, field in BOLD_KEYS:
        if k.startswith(prefix):
            return field
    return None


def split_name(s: str) -> tuple[str, str, list[str]]:
    """'Khổng Tử (孔子 Kǒng Zǐ) [Tranh cãi lịch sử]' → ('Khổng Tử', '孔子 Kǒng Zǐ', ['Tranh cãi lịch sử'])."""
    labels = [m.group(1) for m in LABEL_RE.finditer(s)]
    s = LABEL_RE.sub("", s).strip()
    m = re.match(r"^(.*?)\s*\((.+)\)\s*$", s)
    if m:
        return m.group(1).strip(), m.group(2).strip(), labels
    return s, "", labels


def parse_meta(line: str) -> dict:
    out: dict = {}
    for part in line.split("|"):
        if ":" not in part:
            continue
        k, v = part.split(":", 1)
        k, v = _key(k), v.strip()
        field = None
        for mk, f in META_KEYS.items():
            if k == mk or k.startswith(mk):
                field = f
                break
        if not field:
            out.setdefault("_unknown", []).append(k)
            continue
        if field in ("fields", "big_questions"):
            out[field] = [x.strip() for x in re.split(r"[,;]", v) if x.strip()]
        elif field == "wikidata":
            v = v.strip('"\' ')
            out[field] = None if v in ("?", "", "—", "-", "null", "None") else v
        else:
            out[field] = v
    return out


def parse_link(item: str) -> dict:
    """'- CH02-BCE06-01 · kế thừa · trực tiếp' → dict. Giữ raw để lint báo lỗi rõ."""
    raw = item.strip().lstrip("-*•").strip()
    parts = [p.strip() for p in re.split(r"\s*[·•]\s*|\s+\|\s+", raw)]
    d = {"target": parts[0] if parts else raw, "relation": parts[1] if len(parts) > 1 else "",
         "evidence": parts[2] if len(parts) > 2 else "", "raw": raw}
    d["undetermined"] = _key(d["target"]).startswith("khong xac dinh")
    return d


def parse_file(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    ch = {"no": None, "title": "", "intro": "", "groups": [], "editorial": [], "parse_errors": [], "files": [path.name]}
    group = None
    person = None
    mode = None        # trường đang nhận nội dung nhiều dòng
    in_notes = False

    def err(n, msg):
        ch["parse_errors"].append((n, f"{path.name}:{n}: {msg}"))

    def new_person(pid, rest, n):
        name_vi, name_orig, labels = split_name(rest)
        return {"id": pid, "name_vi": name_vi, "name_orig": name_orig, "labels": labels, "meta_raw": "",
                "years_raw": "", "born": None, "died": None, "approx": False, "alive": False, "years_ok": False,
                "place": "", "region": "", "fields": [], "confidence": "", "wikidata": None, "big_questions": [],
                "ideas": "", "why": "", "sources": "", "inherits": [], "influences": [],
                "group": group["id"] if group else None, "chapter": ch["no"], "line": n, "file": path.name}

    for n, raw in enumerate(lines, 1):
        line = raw.rstrip()
        s = line.strip()
        if not s:
            if mode in ("ideas", "why", "sources", "intro", "context"):
                mode = None
            continue
        m = H1_RE.match(s)
        if m:
            ch["no"] = int(m.group(1))
            ch["title"] = m.group(2).strip()
            in_notes, mode = False, None
            continue
        if H2_NOTE_RE.match(s):
            in_notes, mode, person = True, None, None
            continue
        m = H2_GROUP_RE.match(s)
        if m:
            group = {"id": m.group(1).strip(), "heading": (m.group(2) or "").strip(), "context": "", "persons": [], "line": n}
            ch["groups"].append(group)
            person, mode, in_notes = None, None, False
            continue
        m = H3_RE.match(s)
        if m:
            if group is None:
                err(n, "nhân vật xuất hiện trước khi có '## Nhóm …'")
                group = {"id": "?", "heading": "", "context": "", "persons": [], "line": n}
                ch["groups"].append(group)
            person = new_person(m.group(1), m.group(2), n)
            group["persons"].append(person)
            mode = None
            continue
        if s.startswith("### "):
            err(n, f"heading nhân vật sai quy ước: '{s[:60]}' (cần '### CHxx-GROUP-nn · Tên (Tên gốc)')")
            person, mode = None, None
            continue
        if in_notes:
            ch["editorial"].append(s)
            continue
        m = META_RE.match(s)
        if m and person is not None and not person["meta_raw"]:
            person["meta_raw"] = m.group(1)
            md = parse_meta(m.group(1))
            for k, v in md.items():
                if k != "_unknown":
                    person[k] = v
            if md.get("_unknown"):
                err(n, f"khoá metadata lạ: {md['_unknown']}")
            y = C.parse_years(person["years_raw"])
            person.update({k: y[k] for k in ("born", "died", "approx", "alive")})
            person["years_ok"] = y["ok"]
            mode = None
            continue
        m = BOLD_RE.match(s)
        if m:
            field = _bold_field(m.group(1))
            rest = m.group(2).strip()
            if field is None:
                err(n, f"nhãn đậm không nhận ra: '**{m.group(1)}:**'")
                mode = None
                continue
            if field == "intro":
                ch["intro"] = rest
                mode = "intro"
            elif field == "context":
                if group is None:
                    err(n, "'Bối cảnh' nằm ngoài nhóm")
                else:
                    group["context"] = rest
                    mode = "context"
            elif person is None:
                err(n, f"'{m.group(1)}' nằm ngoài nhân vật")
                mode = None
            elif field in ("inherits", "influences"):
                mode = field
                if rest:  # cho phép viết ngay sau nhãn trên cùng dòng
                    person[field].append(parse_link(rest))
            else:
                person[field] = rest
                mode = field
            continue
        # dòng nội dung tiếp theo
        if mode in ("inherits", "influences") and person is not None:
            if re.match(r"^[-*•]\s+", s):
                person[mode].append(parse_link(s))
            elif s.startswith("("):
                pass  # dòng hướng dẫn trong template bị dán lại — bỏ qua
            else:
                err(n, f"dòng lạ trong '{mode}': '{s[:60]}'")
            continue
        if mode == "intro":
            ch["intro"] += " " + s
        elif mode == "context" and group is not None:
            group["context"] += " " + s
        elif mode in ("ideas", "why", "sources") and person is not None:
            person[mode] += ("\n" if mode == "sources" and re.match(r"^[-*•]\s+", s) else " ") + s
        else:
            err(n, f"dòng không thuộc trường nào: '{s[:60]}'")
    return ch


def chapter_files(content_dir: Path) -> dict[int, list[Path]]:
    """Gom content/chXX.md, chXX.partN.md, ch00-sample.md theo số chapter, parts theo thứ tự N."""
    out: dict[int, list[tuple[int, Path]]] = {}
    for p in sorted(content_dir.glob("ch*.md")):
        m = re.match(r"^ch(\d{2})(?:-[a-z0-9-]+)?(?:\.part(\d+))?\.md$", p.name)
        if not m:
            continue
        out.setdefault(int(m.group(1)), []).append((int(m.group(2) or 0), p))
    return {k: [p for _, p in sorted(v)] for k, v in sorted(out.items())}


def parse_chapter(paths: list[Path]) -> dict:
    merged = None
    for p in paths:
        ch = parse_file(p)
        if merged is None:
            merged = ch
            continue
        merged["files"].append(p.name)
        if ch["no"] is not None and merged["no"] is not None and ch["no"] != merged["no"]:
            merged["parse_errors"].append((0, f"{p.name}: số chapter {ch['no']} khác phần trước ({merged['no']})"))
        if merged["no"] is None:
            merged["no"], merged["title"] = ch["no"], ch["title"]
        if not merged["intro"]:
            merged["intro"] = ch["intro"]
        merged["groups"].extend(ch["groups"])
        merged["editorial"].extend(ch["editorial"])
        merged["parse_errors"].extend(ch["parse_errors"])
    # ghép nhóm trùng id giữa các part
    byid: dict[str, dict] = {}
    groups = []
    for g in merged["groups"]:
        if g["id"] in byid:
            byid[g["id"]]["persons"].extend(g["persons"])
            if not byid[g["id"]]["context"]:
                byid[g["id"]]["context"] = g["context"]
        else:
            byid[g["id"]] = g
            groups.append(g)
    merged["groups"] = groups
    for g in groups:
        for p in g["persons"]:
            p["chapter"] = merged["no"]
    return merged


def load_all(content_dir: Path) -> list[dict]:
    return [parse_chapter(paths) for _, paths in chapter_files(content_dir).items()]
