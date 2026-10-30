"""Sinh HTML tĩnh (PLAN §6.3, §8). Mọi file mở được bằng file://, dùng chung assets/, không CDN."""
from __future__ import annotations

import html
import json
import re
from collections import Counter
from pathlib import Path

from . import common as C

try:
    import markdown as _md

    def md_inline(text: str) -> str:
        h = _md.markdown(text or "", extensions=["nl2br"])
        return h
except ImportError:  # fallback tối thiểu
    def md_inline(text: str) -> str:
        t = html.escape(text or "")
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
        t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
        t = re.sub(r"(https?://[^\s)]+)", r'<a href="\1" rel="noopener">\1</a>', t)
        return "<p>" + t.replace("\n", "<br>") + "</p>"

E = html.escape
CSS_PATH = Path(__file__).resolve().parent / "style.css"


# ============================================================ tiện ích

def life_label(p: dict) -> str:
    if p["years_ok"]:
        b = ("k. " if p["approx"] else "") + C.year_label(p["born"])
        return f"{b} – nay" if p["alive"] else f"{b} – {C.year_label(p['died'])}"
    return p["years_raw"] or "?"


def chapter_tag(no: int) -> str:
    return f"ch{no:02d}"


def chapter_title(ch: dict) -> str:
    cfg = C.CHAPTER_BY_NO.get(ch["no"])
    return cfg["title"] if cfg else ch["title"]


def chapter_label(no: int) -> str:
    cfg = C.CHAPTER_BY_NO.get(no)
    return cfg["label"] if cfg else "mẫu"


def anchor_link(target: str, persons: dict[str, dict], from_root: bool) -> str:
    """Liên kết nội bộ nếu target là ID đã có; nếu không, in tên thường."""
    if target in persons:
        p = persons[target]
        href = f"{'chapters/' if from_root else ''}{chapter_tag(p['chapter'])}.html#{p['id']}"
        return f'<a href="{href}">{E(p["name_vi"])}</a> <span class="muted small mono">{E(target)}</span>'
    if C.ID_RE.match(target):
        return f'<span class="mono" title="ID chưa tồn tại">{E(target)}</span>'
    return E(target)


def mm_text(s: str) -> str:
    """Escape cho Mermaid timeline: bỏ ký tự phân tách."""
    return re.sub(r"[:;#`]", lambda m: {":": "：", ";": ",", "#": "№", "`": "'"}[m.group(0)], s).replace("\n", " ").strip()


def mermaid_timeline(group: dict) -> str:
    """D3: build.py tự sinh timeline từ metadata, nhóm theo lĩnh vực chính."""
    lines = ["timeline"]
    by_field: dict[str, list[dict]] = {}
    for p in sorted(group["persons"], key=lambda x: (x["born"] if x["born"] is not None else 0)):
        by_field.setdefault(p["fields"][0] if p["fields"] else "Khác", []).append(p)
    for field, ps in by_field.items():
        lines.append(f"    section {mm_text(field)}")
        for p in ps:
            lines.append(f"        {mm_text(life_label(p))} : {mm_text(p['name_vi'])}")
    return "\n".join(lines)


def mermaid_block(code: str) -> str:
    return f'<div class="mermaid-wrap"><pre class="mermaid">{E(code)}</pre><pre class="mermaid-src">{E(code)}</pre></div>'


def page(title: str, body: str, depth: int, extra_head: str = "", body_class: str = "", scripts: str = "") -> str:
    rel = "../" * depth
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · {E(C.PROJECT["title"])}</title>
<link rel="stylesheet" href="{rel}assets/style.css">
{extra_head}
</head>
<body class="{body_class}">
{body}
{scripts}
</body>
</html>'''


MERMAID_SCRIPT = '''<script src="{rel}assets/mermaid.min.js"></script>
<script>
(function () {{
  var dark = matchMedia("(prefers-color-scheme: dark)").matches;
  if (!window.mermaid) {{ document.querySelectorAll(".mermaid-src").forEach(function (p) {{ p.style.display = "block"; }}); return; }}
  mermaid.initialize({{ startOnLoad: false, securityLevel: "strict", theme: dark ? "dark" : "default", timeline: {{ disableMulticolor: true }} }});
  mermaid.run({{ querySelector: ".mermaid" }}).catch(function (e) {{
    document.querySelectorAll(".mermaid-wrap").forEach(function (w) {{ var p = w.querySelector(".mermaid"); if (p) p.remove(); var s = w.querySelector(".mermaid-src"); if (s) s.style.display = "block"; }});
  }});
}})();
</script>'''


def topnav(ch_no: int | None, chapters: list[dict], depth: int) -> str:
    rel = "../" * depth
    parts = [f'<a href="{rel}index.html" target="_top">☰ Mục lục</a>']
    if ch_no is not None:
        nos = [c["no"] for c in chapters]
        i = nos.index(ch_no)
        if i > 0:
            parts.append(f'<a href="{chapter_tag(nos[i-1])}.html">← Ch.{nos[i-1]} {E(chapter_label(nos[i-1]))}</a>')
        if i < len(nos) - 1:
            parts.append(f'<a href="{chapter_tag(nos[i+1])}.html">Ch.{nos[i+1]} {E(chapter_label(nos[i+1]))} →</a>')
    parts.append(f'<a href="{rel}overview.html">Overview</a>')
    parts.append(f'<a href="{rel}credits.html">Credits</a>')
    return '<nav class="topnav">' + " · ".join(parts) + "</nav>"


def footer(depth: int) -> str:
    rel = "../" * depth
    return (f'<div class="footer">{E(C.PROJECT["title"])} · bản dựng {E(C.PROJECT["version"])} · HTML sinh bởi build.py từ content/*.md · '
            f'Dữ liệu danh tính/niên đại: <a href="https://www.wikidata.org" rel="noopener">Wikidata</a> (CC0) · Ảnh: <a href="{rel}credits.html">Credits</a></div>')


# ============================================================ ảnh

def figure_html(p: dict, images: dict, wd_cache: dict, depth: int) -> str:
    rel = "../" * depth
    im = images.get(p["id"]) if images else None
    name = E(p["name_vi"])
    q = p.get("wikidata")
    wd_info = wd_cache.get(f"wd:{q}") if q else None
    wiki_url = None
    if wd_info and wd_info.get("sitelinks"):
        sl = wd_info["sitelinks"]
        if "viwiki" in sl:
            wiki_url = "https://vi.wikipedia.org/wiki/" + sl["viwiki"].replace(" ", "_")
        elif "enwiki" in sl:
            wiki_url = "https://en.wikipedia.org/wiki/" + sl["enwiki"].replace(" ", "_")
    if not wiki_url and q:
        wiki_url = f"https://www.wikidata.org/wiki/{q}"

    if im and im.get("status") == "embedded":
        lic = f'<a href="{E(im["license_url"])}" rel="noopener">{E(im["license"])}</a>' if im.get("license_url") else E(im["license"])
        author = E(im.get("author") or "không rõ tác giả")
        credit = f'Ảnh: <a href="{E(im["source_url"])}" rel="noopener">Wikimedia Commons</a>, {author}, {lic}'
        if im.get("attribution_required"):
            credit += ", đã thu nhỏ"
        cap_main = re.sub(r"\s*Ảnh: Wikimedia Commons.*$", "", im.get("caption") or "").strip()
        return f'''<figure class="portrait">
  <img src="{rel}assets/img/{E(im["file"])}" alt="{name}" loading="lazy" width="{im.get("width", 500)}">
  <figcaption>{E(cap_main)}<span class="credit">{credit}.</span></figcaption>
</figure>'''
    # không nhúng: placeholder + link tham khảo
    if im and im.get("status") in ("review", "no-license", "skipped") and im.get("source_url"):
        link = f'<a href="{E(im["source_url"])}" rel="noopener">Xem ảnh tại Wikimedia Commons</a>'
        why = {"review": "ảnh chờ Owner xem xét (có hạn chế quyền)", "no-license": "ảnh trên Commons thiếu/không rõ giấy phép", "skipped": "không dùng chân dung theo images.yaml"}[im["status"]]
    elif wiki_url:
        link = f'<a href="{E(wiki_url)}" rel="noopener">Xem trên {"Wikipedia" if "wikipedia" in wiki_url else "Wikidata"}</a>'
        why = "chưa có ảnh trên Wikidata (P18)" if not im else im.get("note", "")
    else:
        link, why = "", "không có Wikidata ID"
    ini = "".join(w[0] for w in p["name_vi"].split()[:2]).upper()
    return f'<figure class="portrait"><div class="ph" title="{E(why)}">{E(ini)}</div><figcaption><span class="credit">{link}</span></figcaption></figure>'


# ============================================================ nhân vật

def person_card(p: dict, persons: dict, images: dict, wd_cache: dict, depth: int) -> str:
    labels = "".join(f' <span class="badge legend-lbl">{E(l)}</span>' for l in p["labels"])
    alive = ' <span class="badge alive">còn sống</span>' if p["alive"] else ""
    badges = [f'<span class="badge year" title="năm">{E(life_label(p))}</span>']
    if p["place"]:
        badges.append(f'<span class="badge place" title="nơi">{E(p["place"])}</span>')
    if p["region"]:
        badges.append(f'<span class="badge region" title="vùng">{E(p["region"])}</span>')
    badges += [f'<span class="badge field" title="lĩnh vực">{E(f)}</span>' for f in p["fields"]]
    if p["confidence"]:
        badges.append(f'<span class="badge conf conf-{E(C.slug(p["confidence"]))}" title="độ tin cậy niên đại">niên đại: {E(p["confidence"])}</span>')
    badges += [f'<span class="badge bq" title="câu hỏi lớn">{E(q)}</span>' for q in p["big_questions"]]
    if p["wikidata"]:
        badges.append(f'<a class="badge wd" href="https://www.wikidata.org/wiki/{E(p["wikidata"])}" rel="noopener">{E(p["wikidata"])}</a>')
    else:
        badges.append('<span class="badge wd muted">wikidata: ?</span>')

    def links(items, title):
        if not items:
            return ""
        li = []
        for l in items:
            if l["undetermined"]:
                li.append('<li class="muted">Không xác định</li>')
                continue
            li.append(f'<li>{anchor_link(l["target"], persons, False)} <span class="badge rel rel-{E(C.slug(l["relation"]))}">{E(l["relation"])}</span> <span class="badge ev ev-{E(C.slug(l["evidence"]))}">{E(l["evidence"])}</span></li>')
        return f'<div class="sec"><b>{title}</b><ul class="links">{"".join(li)}</ul></div>'

    # cạnh ngược: ai ghi "Kế thừa từ" người này (tính tự động)
    rev = [(q, l) for q in persons.values() for l in q["inherits"] if l["target"] == p["id"]]
    rev_html = ""
    if rev:
        li = "".join(f'<li>{anchor_link(q["id"], persons, False)} <span class="badge rel rel-{E(C.slug(l["relation"]))}">{E(l["relation"])}</span> <span class="badge ev ev-{E(C.slug(l["evidence"]))}">{E(l["evidence"])}</span></li>' for q, l in rev)
        rev_html = f'<div class="sec"><b>Được ghi là nguồn kế thừa bởi</b> <span class="muted small">(tự động từ dữ liệu)</span><ul class="links">{li}</ul></div>'

    return f'''<article class="person" id="{E(p["id"])}">
  {figure_html(p, images, wd_cache, depth)}
  <div class="body">
    <h3><a class="anchor" href="#{E(p["id"])}">#</a>{E(p["name_vi"])}{labels}{alive} <span class="orig">{E(p["name_orig"])}</span></h3>
    <div class="badges">{" ".join(badges)}</div>
    <div class="sec"><b>Tư tưởng / đóng góp chính</b>{md_inline(p["ideas"])}</div>
    <div class="sec"><b>Vì sao chọn</b>{md_inline(p["why"])}</div>
    {links(p["inherits"], "Kế thừa từ")}
    {links(p["influences"], "Ảnh hưởng tới")}
    {rev_html}
    <div class="sec sources"><b>Nguồn</b>{md_inline(p["sources"])}</div>
    <div class="small muted mono">{E(p["id"])}</div>
  </div>
</article>'''


# ============================================================ trang chapter

def render_chapter(ch: dict, chapters: list[dict], persons: dict, images: dict, wd_cache: dict) -> str:
    no = ch["no"]
    title = chapter_title(ch)
    sample = ' <span class="badge sample">MẪU</span>' if no == C.SAMPLE_CHAPTER_NO else ""
    cfg = C.CHAPTER_BY_NO.get(no)
    group_order = cfg["groups"] if cfg else [g["id"] for g in ch["groups"]]
    gmap = {g["id"]: g for g in ch["groups"]}
    n_persons = sum(len(g["persons"]) for g in ch["groups"])
    parts = [topnav(no, chapters, 1), f'''<header class="chapter-head">
  <div class="kicker">{f"Phụ lục · {E(chapter_label(no))}" if not C.is_main(no) else f"Chapter {no} · {E(chapter_label(no))}"}</div>
  <h1>{E(title)}{sample}</h1>
  <div class="meta">{n_persons} nhân vật · {len([g for g in ch["groups"] if g["persons"]])}/{len(group_order)} nhóm có dữ liệu · nguồn: {E(", ".join(ch["files"]))}</div>
</header>
<div class="intro">{md_inline(ch["intro"])}</div>
<p class="small groupnav">''' + " · ".join(f'<a href="#{E(g)}">{E(C.group_label(g))}</a> <span class="muted">({len(gmap[g]["persons"]) if g in gmap else 0})</span>' for g in group_order) + "</p>"]
    for gid in group_order:
        g = gmap.get(gid)
        rng = C.group_range(gid)
        rng_s = f"{C.year_label(rng[0])} – {C.year_label(rng[1])}" if rng else ""
        parts.append(f'<section class="group" id="{E(gid)}"><h2>{E(C.group_label(gid))} <span class="cnt">{rng_s} · {len(g["persons"]) if g else 0} nhân vật</span></h2>')
        if not g:
            parts.append('<p class="muted">Chưa có dữ liệu cho nhóm này.</p></section>')
            continue
        if g["context"]:
            parts.append(f'<div class="context"><b>Bối cảnh.</b> {md_inline(g["context"])[3:-4] if g["context"] else ""}</div>')
        if len(g["persons"]) >= 2:  # D3: timeline tự sinh; 1 người thì không cần
            parts.append(mermaid_block(mermaid_timeline(g)))
        for p in g["persons"]:
            parts.append(person_card(p, persons, images, wd_cache, 1))
        parts.append("</section>")
    if ch["editorial"]:
        parts.append(f'<section class="note" id="editorial"><h2>Ghi chú biên tập</h2>{md_inline(chr(10).join(ch["editorial"]))}</section>')
    parts.append(footer(1))
    return page(f"Ch.{no} {title}", "\n".join(parts), depth=1, scripts=MERMAID_SCRIPT.format(rel="../"))


# ============================================================ index

def render_index(chapters: list[dict], persons: dict) -> str:
    present = {c["no"]: c for c in chapters}
    items = []
    if C.SAMPLE_CHAPTER_NO in present:
        ch = present[C.SAMPLE_CHAPTER_NO]
        items.append(_sidebar_chapter(0, ch["title"], "mẫu P1", [g["id"] for g in ch["groups"]], ch, sample=True))
    for cfg in C.CHAPTERS:
        ch = present.get(cfg["no"])
        items.append(_sidebar_chapter(cfg["no"], cfg["title"], cfg["label"], cfg["groups"], ch))
    app_items = []
    for cfg in C.APPENDICES:
        ch = present.get(cfg["no"])
        app_items.append(_sidebar_chapter(cfg["no"], cfg["title"], cfg["label"], cfg["groups"], ch, num_label=cfg.get("num_label")))
    app_block = (f'<div class="group-title">Phụ lục <span class="muted small">(ngoài thống kê chính)</span></div>{"".join(app_items)}'
                 if app_items else "")
    body = f'''<button class="menu-btn" id="menu-btn" aria-label="Menu">☰</button>
<aside class="sidebar" id="sidebar">
  <div class="brand"><a href="#intro" id="brand-link"><h1>{E(C.PROJECT["title"])}</h1></a><div class="sub">{E(C.PROJECT["subtitle"])}</div></div>
  <input id="q" type="search" placeholder="Tìm tên, lĩnh vực, vùng…" autocomplete="off">
  <div id="hits"></div>
  <div class="group-title">Tổng quan</div>
  <a class="item top" href="overview.html" data-page="overview.html"><span class="lbl">Overview — timeline &amp; dòng chảy tư tưởng</span></a>
  <a class="item top" href="credits.html" data-page="credits.html"><span class="lbl">Credits — ảnh &amp; giấy phép</span></a>
  <div class="group-title">Chapter</div>
  {"".join(items)}
  {app_block}
  <div class="foot">{len(persons)} nhân vật · bản dựng {E(C.PROJECT["version"])}<br><a id="open-new" href="overview.html" target="_blank">Mở trang hiện tại trong tab mới ↗</a></div>
</aside>
<main class="main"><div class="framebar"><button id="prev" title="Chapter trước">←</button><span id="crumb"></span><button id="next" title="Chapter sau">→</button></div><iframe id="frame" name="frame" src="overview.html" title="Nội dung"></iframe></main>
<script src="data/persons.js"></script>
<script src="assets/app.js"></script>'''
    return page("Mục lục", body, depth=0, body_class="index")


def _sidebar_chapter(no: int, title: str, label: str, groups: list[str], ch: dict | None, sample: bool = False, num_label: str | None = None) -> str:
    gmap = {g["id"]: g for g in ch["groups"]} if ch else {}
    n = sum(len(g["persons"]) for g in ch["groups"]) if ch else 0
    tag = chapter_tag(no)
    sub = "".join(
        f'<a class="item sub" href="chapters/{tag}.html#{gid}" data-page="chapters/{tag}.html#{gid}"><span class="lbl">{E(C.group_label(gid))}</span><span class="cnt">{len(gmap[gid]["persons"]) if gid in gmap else "–"}</span></a>'
        for gid in groups)
    cls = "item chap" + ("" if ch else " empty")
    badge = ' <span class="badge sample">MẪU</span>' if sample else ""
    return f'''<details class="chapter" {"open" if ch else ""}>
<summary><a class="{cls}" href="chapters/{tag}.html" data-page="chapters/{tag}.html"><span class="num">{E(num_label) if num_label else no}</span><span class="lbl">{E(title)}{badge}<span class="range">{E(label)}</span></span><span class="cnt">{n or "–"}</span></a></summary>
{sub}
</details>'''


# ============================================================ overview (P5 — bản khung) & credits

def stats(chapters: list[dict], persons: dict) -> dict:
    def dist(items: list[str]) -> dict:
        c = Counter(items)
        tot = sum(c.values()) or 1
        return {k: {"n": v, "pct": round(100 * v / tot, 1)} for k, v in c.most_common()}
    main_persons = {pid: p for pid, p in persons.items() if C.is_main(p["chapter"])}
    out = {"total_persons": len(main_persons), "appendix_persons": len(persons) - len(main_persons), "chapters": {}}
    all_regions, all_fields, all_rel, all_ev, all_bq = [], [], [], [], []
    for ch in chapters:
        ps = [p for g in ch["groups"] for p in g["persons"]]
        regions = [p["region"] for p in ps if p["region"]]
        fields = [f for p in ps for f in p["fields"]]
        rels = [l["relation"] for p in ps for k in ("inherits", "influences") for l in p[k] if not l["undetermined"]]
        evs = [l["evidence"] for p in ps for k in ("inherits", "influences") for l in p[k] if not l["undetermined"]]
        bqs = [q for p in ps for q in p["big_questions"]]
        out["chapters"][chapter_tag(ch["no"])] = {"persons": len(ps), "track": C.track_of(ch["no"]), "regions": dist(regions), "fields": dist(fields), "relations": dist(rels), "evidence": dist(evs), "big_questions": dist(bqs)}
        if not C.is_main(ch["no"]):
            continue  # phụ lục: thống kê riêng theo chapter, không dồn vào "Toàn bộ"
        all_regions += regions; all_fields += fields; all_rel += rels; all_ev += evs; all_bq += bqs
    out["all"] = {"regions": dist(all_regions), "fields": dist(all_fields), "relations": dist(all_rel), "evidence": dist(all_ev), "big_questions": dist(all_bq)}
    # bậc vào/ra
    deg = {pid: {"in": 0, "out": 0} for pid, p in persons.items() if C.is_main(p["chapter"])}
    for p in persons.values():
        if not C.is_main(p["chapter"]):
            continue  # liên kết từ phụ lục không làm phồng bậc của atlas chính
        for l in p["inherits"]:
            if l["target"] in deg and not l["undetermined"]:
                deg[p["id"]]["out"] += 1
                deg[l["target"]]["in"] += 1
    out["degree"] = deg
    return out


def stats_txt(st: dict) -> str:
    lines = [f"STATS — {st['total_persons']} nhân vật (atlas chính)"
             + (f" + {st['appendix_persons']} ở phụ lục (không tính vào thống kê toàn cục)" if st.get("appendix_persons") else ""), ""]

    def block(title, d):
        lines.append(title)
        for k, v in d.items():
            lines.append(f"  {k:<28} {v['n']:>4}  {v['pct']:>5}%")
        lines.append("")
    for key, title in (("regions", "Vùng"), ("fields", "Lĩnh vực"), ("relations", "Loại quan hệ"), ("evidence", "Mức bằng chứng"), ("big_questions", "Câu hỏi lớn")):
        block(f"[Toàn bộ] {title}", st["all"][key])
    for tag, cs in st["chapters"].items():
        lines.append(f"=== {tag} ({cs['persons']} nhân vật){' — PHỤ LỤC, ngoài thống kê toàn cục' if cs.get('track') not in (None, 'main') else ''} ===")
        for key, title in (("regions", "Vùng"), ("fields", "Lĩnh vực"), ("relations", "Loại quan hệ")):
            block(f"[{tag}] {title}", cs[key])
    return "\n".join(lines)


def _bars(d: dict) -> str:
    if not d:
        return '<p class="muted small">chưa có dữ liệu</p>'
    mx = max(v["n"] for v in d.values())
    return '<div class="bars">' + "".join(f'<div class="row"><span>{E(k)}</span><div class="bar" style="width:{v["n"] / mx * 100:.0f}%"></div><span class="n">{v["n"]} · {v["pct"]}%</span></div>' for k, v in d.items()) + "</div>"


def render_overview(chapters: list[dict], persons: dict, st: dict) -> str:
    rows = []
    present = {c["no"]: c for c in chapters}
    for cfg in C.CHAPTERS:
        ch = present.get(cfg["no"])
        n = sum(len(g["persons"]) for g in ch["groups"]) if ch else 0
        gs = sum(1 for g in ch["groups"] if g["persons"]) if ch else 0
        rows.append(f'<tr><td><a href="chapters/{chapter_tag(cfg["no"])}.html">Ch.{cfg["no"]}</a></td><td>{E(cfg["title"])}</td><td>{E(cfg["label"])}</td><td>{gs}/{len(cfg["groups"])}</td><td>{n}</td></tr>')
    # lưới thế kỷ (độ phủ)
    cells = []
    for cfg in C.CHAPTERS:
        ch = present.get(cfg["no"])
        gmap = {g["id"]: g for g in ch["groups"]} if ch else {}
        for gid in cfg["groups"]:
            n = len(gmap[gid]["persons"]) if gid in gmap else 0
            lvl = 0 if n == 0 else 1 if n <= 3 else 2 if n <= 6 else 3 if n <= 9 else 4
            cells.append(f'<a class="l{lvl}" href="chapters/{chapter_tag(cfg["no"])}.html#{gid}" title="{E(C.group_label(gid))}: {n}"><span>{E(C.group_label(gid).replace("TK ", ""))}</span><b>{n}</b></a>')
    n_main_ch = sum(1 for ch in chapters if C.is_main(ch["no"]))
    app_meta = (f' · phụ lục: {st["appendix_persons"]} nhân vật (thống kê riêng)' if st.get("appendix_persons") else "")
    deg = sorted(((v["in"] + v["out"], v["in"], v["out"], k) for k, v in st["degree"].items()), reverse=True)[:15]
    deg_rows = "".join(f'<tr><td>{anchor_link(k, persons, True)}</td><td>{i}</td><td>{o}</td></tr>' for _, i, o, k in deg if i + o)
    body = topnav(None, chapters, 0) + f'''
<header class="chapter-head"><div class="kicker">Overview</div><h1>Timeline toàn cục &amp; dòng chảy tư tưởng</h1>
<div class="meta">{st["total_persons"]} nhân vật · {n_main_ch}/{len(C.CHAPTERS)} chapter có dữ liệu{app_meta} · <span class="badge sample">P5 — bản khung</span> graph D3 có bộ lọc sẽ hoàn thiện ở P5</div></header>
<div class="note"><p><b>Trạng thái.</b> Trang này hiện chỉ gồm thống kê trung tính và độ phủ theo nhóm (sinh từ <code>data/persons.json</code>). Ở P5 sẽ bổ sung: timeline toàn cục và graph dòng chảy tư tưởng bằng D3 (đã vendored tại <code>assets/d3.min.js</code>), lọc theo loại quan hệ / lĩnh vực / vùng / giai đoạn, liên kết xuyên vùng theo thời gian, bản đồ vị trí. Việc đối chiếu với giả thuyết do Owner tự làm ngoài pipeline (§9).</p></div>

<h2>Độ phủ theo nhóm (33 nhóm)</h2>
<div class="grid-groups">{"".join(cells)}</div>

<h2>Các chapter</h2>
<table class="tbl"><tr><th>#</th><th>Chapter</th><th>Giai đoạn</th><th>Nhóm có dữ liệu</th><th>Nhân vật</th></tr>{"".join(rows)}</table>

<h2>Thống kê toàn bộ</h2>
<div class="cards2">
  <div class="c"><b>Vùng</b>{_bars(st["all"]["regions"])}</div>
  <div class="c"><b>Lĩnh vực</b>{_bars(st["all"]["fields"])}</div>
  <div class="c"><b>Loại quan hệ</b>{_bars(st["all"]["relations"])}</div>
  <div class="c"><b>Mức bằng chứng</b>{_bars(st["all"]["evidence"])}</div>
  <div class="c"><b>Câu hỏi lớn</b>{_bars(st["all"]["big_questions"])}</div>
</div>

<h2>Liên kết vào / ra (theo ID trong atlas)</h2>
<table class="tbl"><tr><th>Nhân vật</th><th>Vào (được kế thừa)</th><th>Ra (kế thừa từ)</th></tr>{deg_rows or '<tr><td colspan=3 class=muted>chưa có liên kết theo ID</td></tr>'}</table>
<p class="small muted">Chi tiết dạng text: <code>reports/stats.txt</code>.</p>
''' + footer(0)
    return page("Overview", body, depth=0)


def render_credits(chapters: list[dict], persons: dict, images: dict) -> str:
    rows, review, nolic, none = [], [], [], []
    for p in sorted(persons.values(), key=lambda x: (x["chapter"], x["group"], x["id"])):
        im = images.get(p["id"]) if images else None
        link = anchor_link(p["id"], persons, True)
        if im and im.get("status") == "embedded":
            lic = f'<a href="{E(im["license_url"])}" rel="noopener">{E(im["license"])}</a>' if im.get("license_url") else E(im["license"])
            rows.append(f'<tr><td><img src="assets/img/{E(im["file"])}" alt="" class="thumb"></td><td>{link}</td><td><a href="{E(im["source_url"])}" rel="noopener">{E(im["title"][5:])}</a></td><td>{E(im.get("author") or "—")}</td><td>{lic}{" <span class=badge>ghi công bắt buộc</span>" if im.get("attribution_required") else ""}</td><td class="small">{E(im.get("caption") or "")}</td></tr>')
        elif im and im.get("status") == "review":
            review.append(f'<li>{link} — <a href="{E(im["source_url"])}" rel="noopener">{E(im["title"])}</a>: {E(im.get("note") or "")}</li>')
        elif im and im.get("status") == "no-license":
            nolic.append(f'<li>{link} — <a href="{E(im["source_url"])}" rel="noopener">{E(im["title"])}</a>: {E(im.get("note") or "không rõ giấy phép")}</li>')
        else:
            none.append(link)
    body = topnav(None, chapters, 0) + f'''
<header class="chapter-head"><div class="kicker">Credits</div><h1>Ảnh &amp; giấy phép</h1><div class="meta">{len(rows)} ảnh nhúng · {len(review)} chờ xem xét · {len(nolic)} thiếu giấy phép · {len(none)} không có ảnh</div></header>
<div class="note"><p><b>Chính sách (PLAN §7.2).</b> Public domain / CC0: nhúng, vẫn ghi nguồn. CC BY / CC BY-SA: nhúng kèm tác giả, tên giấy phép có link, link tệp gốc và ghi chú "đã thu nhỏ". Ảnh có hạn chế quyền (quyền nhân thân, nhãn hiệu…): không nhúng tự động, chờ Owner. Thiếu hoặc không rõ giấy phép: không nhúng, chỉ đặt link tham khảo. Không có P18: link tới Wikipedia/Wikidata. Ảnh được tải về <code>assets/img/</code> (không hotlink) từ Wikimedia Commons theo P18 của <a href="https://www.wikidata.org" rel="noopener">Wikidata</a> (dữ liệu CC0). Override thủ công: <code>content/images.yaml</code>.</p></div>
<table class="tbl"><tr><th></th><th>Nhân vật</th><th>Tệp gốc trên Commons</th><th>Tác giả</th><th>Giấy phép</th><th>Chú thích</th></tr>{"".join(rows) or '<tr><td colspan=6 class=muted>chưa có ảnh</td></tr>'}</table>
{"<h2>Chờ Owner xem xét</h2><ul>" + "".join(review) + "</ul>" if review else ""}
{"<h2>Thiếu hoặc không rõ giấy phép (không nhúng)</h2><ul>" + "".join(nolic) + "</ul>" if nolic else ""}
{"<h2>Không có ảnh (thiếu P18 hoặc chưa fetch)</h2><p class=small>" + " · ".join(none) + "</p>" if none else ""}
<h2>Thư viện</h2><p class="small">Mermaid 11.4.1 (MIT, <code>assets/LICENSE-mermaid.txt</code>) · D3 7.9.0 (ISC, <code>assets/LICENSE-d3.txt</code>) · Python-Markdown. Không dùng CDN.</p>
''' + footer(0)
    return page("Credits", body, depth=0)
