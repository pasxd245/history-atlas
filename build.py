#!/usr/bin/env python3
"""build.py — parse content/*.md → lint → data/persons.json → HTML (index, chapters/, overview, credits).

    python build.py                 # lint (có đối chiếu Wikidata, dùng cache data/wikidata-cache.json) + build
    python build.py --offline       # không gọi Wikidata
    python build.py --lint-only     # chỉ lint, không sinh HTML
    python build.py --lint-only tests/ch99-bad.md   # lint một file bất kỳ (test case)
    python build.py --force         # vẫn sinh HTML dù lint có lỗi (chỉ để xem giao diện)
    python build.py --groups 4      # in dòng {{DANH SÁCH NHÓM}} cho prompt
    python build.py --list-ids      # in toàn bộ ID nhân vật hiện có

Mã thoát: 0 = OK, 1 = lint có lỗi (không sinh HTML trừ khi --force).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from atlaslib import common as C, lint as L, parse as P, render as R  # noqa: E402


def load_images() -> dict:
    p = ROOT / "data" / "images.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("  [!] data/images.json hỏng — bỏ qua ảnh")
    return {}


def write_persons(chapters: list[dict], persons: dict, images: dict):
    data = {
        "project": {k: C.PROJECT[k] for k in ("title", "subtitle", "version", "start_year", "end_year", "reference_year")},
        "chapters": [{"no": ch["no"], "title": R.chapter_title(ch), "label": R.chapter_label(ch["no"]), "files": ch["files"],
                      "intro": ch["intro"], "editorial": ch["editorial"],
                      "groups": [{"id": g["id"], "label": C.group_label(g["id"]), "range": C.group_range(g["id"]), "context": g["context"],
                                  "persons": [p["id"] for p in g["persons"]]} for g in ch["groups"]]} for ch in chapters],
        "persons": {pid: {k: v for k, v in p.items() if k not in ("meta_raw", "line")} | {"image": images.get(pid)} for pid, p in persons.items()},
    }
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "persons.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    # bản rút gọn cho tìm kiếm trong index.html (file:// không fetch được JSON)
    search = [{"id": p["id"], "n": p["name_vi"], "o": p["name_orig"], "f": p["fields"], "r": p["region"], "g": C.group_label(p["group"]),
               "u": f"chapters/{R.chapter_tag(p['chapter'])}.html#{p['id']}"} for p in persons.values()]
    present = {c["no"] for c in chapters}
    chs = [{"no": c["no"], "title": c["title"], "has": c["no"] in present} for c in C.CHAPTERS]
    if C.SAMPLE_CHAPTER_NO in present:
        chs.insert(0, {"no": 0, "title": "Mẫu", "has": True})
    (ROOT / "data" / "persons.js").write_text(
        "window.ATLAS_PERSONS = " + json.dumps(search, ensure_ascii=False) + ";\nwindow.ATLAS_CHAPTERS = " + json.dumps(chs, ensure_ascii=False) + ";\n",
        encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--lint-only", nargs="?", const="__all__", metavar="FILE")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--groups", type=int, metavar="N")
    ap.add_argument("--list-ids", action="store_true")
    a = ap.parse_args()

    if a.groups is not None:
        cfg = C.CHAPTER_BY_NO.get(a.groups)
        if not cfg:
            print(f"Không có chapter {a.groups}")
            return 1
        print(", ".join(f"{g} ({C.group_label(g)})" for g in cfg["groups"]))
        return 0

    if a.lint_only and a.lint_only != "__all__":
        chapters = [P.parse_chapter([Path(a.lint_only)])]
    else:
        chapters = P.load_all(ROOT / "content")
    if not chapters:
        print("Không có content/ch*.md")
        return 1
    persons = {p["id"]: p for ch in chapters for g in ch["groups"] for p in g["persons"]}

    if a.list_ids:
        print("\n".join(sorted(persons)))
        return 0

    images = load_images()
    print(f"Parse: {len(chapters)} chapter, {len(persons)} nhân vật")
    reports_dir = ROOT / "reports" / "tests" if (a.lint_only and a.lint_only != "__all__") else ROOT / "reports"
    rep = L.run(chapters, images, online=not a.offline, reports_dir=reports_dir)
    for level in ("ERROR", "WARN"):
        for w, m in rep.by_level(level):
            print(f"  {level:5} {w}: {m}")
    print(f"Lint: {rep.count('ERROR')} lỗi · {rep.count('WARN')} cảnh báo · {rep.count('INFO')} ghi chú → {reports_dir.relative_to(ROOT)}/lint-chXX.txt"
          + ("" if not a.offline else " (offline, không đối chiếu Wikidata)"))
    if a.lint_only:
        return 1 if rep.count("ERROR") else 0
    if rep.count("ERROR") and not a.force:
        print("Lint có lỗi — không sinh HTML. Sửa content/ hoặc dùng --force để xem giao diện.")
        return 1

    write_persons(chapters, persons, images)
    wd_cache = C.JsonCache(C.WD_CACHE).data
    (ROOT / "chapters").mkdir(exist_ok=True)
    for ch in chapters:
        (ROOT / "chapters" / f"{R.chapter_tag(ch['no'])}.html").write_text(R.render_chapter(ch, chapters, persons, images, wd_cache), encoding="utf-8")
    st = R.stats(chapters, persons)
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / "stats.txt").write_text(R.stats_txt(st), encoding="utf-8")
    (ROOT / "overview.html").write_text(R.render_overview(chapters, persons, st), encoding="utf-8")
    (ROOT / "credits.html").write_text(R.render_credits(chapters, persons, images), encoding="utf-8")
    (ROOT / "index.html").write_text(R.render_index(chapters, persons), encoding="utf-8")
    n_img = sum(1 for v in images.values() if v.get("status") == "embedded")
    print(f"Build: index.html · {len(chapters)} chapter · overview.html · credits.html · {n_img} ảnh nhúng · data/persons.json · reports/stats.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
