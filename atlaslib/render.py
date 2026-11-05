"""Sinh HTML tĩnh (PLAN §6.3, §8). Mọi file mở được bằng file://, dùng chung assets/, không CDN."""
from __future__ import annotations

import html
import json
import re
from collections import Counter

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
    """Timeline sắp ĐÚNG theo thứ tự thời gian.

    Mermaid vẽ một mũi tên ngang chạy trái → phải, tín hiệu phổ quát cho
    "thời gian tăng dần". Bản trước nhóm theo lĩnh vực chính rồi mới sắp theo
    năm trong từng nhóm, nên thứ tự ngang KHÔNG đơn điệu theo thời gian: ở
    nhóm BCE08, Isaiah (740 TCN) bị vẽ trước Homer (750 TCN) và Piye (744 TCN)
    bị vẽ sau Hesiod (730 TCN). Với một trang tham khảo học thuật thì đó là
    lỗi nội dung, không phải lỗi thẩm mỹ.

    Nay phát một dãy phẳng sắp theo năm sinh, lĩnh vực chuyển vào nhãn.
    Khoảng cách giữa các mục vẫn đều nhau — thứ tự đúng, tỉ lệ thì không;
    caption nói rõ điều đó. Trục thời gian theo tỉ lệ thật để dành cho P5 (D3).
    """
    ps = sorted(group["persons"], key=lambda x: (x["born"] if x["born"] is not None else 0, x["id"]))
    if not ps:
        return ""
    lines = ["timeline"]
    for p in ps:
        field = p["fields"][0] if p["fields"] else "Khác"
        lines.append(f"    {mm_text(tl_years(p))} : {mm_text(p['name_vi'])} · {mm_text(field)}")
    return "\n".join(lines)


def tl_years(p: dict) -> str:
    """Nhãn năm gọn cho timeline: '760–745 TCN' thay vì 'k. 760 TCN – 745 TCN'.

    Nhãn dài đẩy bề rộng nội tại của SVG lên, khiến Mermaid co chữ; nó còn hay
    bị ngắt dòng thành '745TCN' (mất dấu cách). Thẻ nhân vật bên dưới đã ghi
    đầy đủ cả 'k.' lẫn độ tin cậy nên ở đây không cần lặp lại."""
    if not p["years_ok"]:
        return p["years_raw"] or "?"
    b, d = p["born"], p["died"]
    if p["alive"]:
        return f"{C.year_label(b)}–nay"
    if b is not None and d is not None and b < 0 and d < 0:
        return f"{-b}–{-d} TCN"        # cùng TCN thì chỉ ghi hậu tố một lần
    return f"{C.year_label(b)}–{C.year_label(d)}"


def mermaid_block(code: str, caption: str = "", names: str = "") -> str:
    """SVG của Mermaid không có aria-label nên vô hình với screen reader;
    kèm một figcaption thật và một danh sách văn bản để đọc thay."""
    cap = f'<figcaption class="small muted">{E(caption)}</figcaption>' if caption else ""
    alt = f'<p class="vh">Thứ tự theo năm: {E(names)}.</p>' if names else ""
    return (f'<figure class="mermaid-wrap" role="group">{cap}{alt}'
            f'<pre class="mermaid" aria-hidden="true">{E(code)}</pre>'
            f'<pre class="mermaid-src">{E(code)}</pre></figure>')


ASSET_V = C.PROJECT["version"].lstrip("v")


def page(title: str, body: str, depth: int, extra_head: str = "", body_class: str = "", scripts: str = "") -> str:
    rel = "../" * depth
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · {E(C.PROJECT["title"])}</title>
<link rel="stylesheet" href="{rel}assets/style.css?v={ASSET_V}">
<link rel="icon" href="{rel}favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{rel}assets/img/apple-touch-icon.png">
<script>/* đặt theme trước khi vẽ: để sau sẽ nháy nền sáng một nhịp */
try{{var r=document.documentElement,t=localStorage.getItem("ha-theme");
if(t==="light"||t==="dark")r.setAttribute("data-theme",t);
if(localStorage.getItem("ha-reading")==="on")r.setAttribute("data-reading","on");}}catch(e){{}}</script>
<script defer src="{rel}assets/theme.js?v={ASSET_V}"></script>
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


# Nút theme/reading. assets/theme.js đọc localStorage rồi vẽ lại nhãn nút theme và
# aria-pressed của nút chế độ đọc; chữ ở đây chỉ là mặc định khi JS chưa chạy.
# Nút theme không mang aria-pressed: nó có ba trạng thái, aria-pressed là nhị phân.
TOOLS = ('<span class="tools">'
         '<button type="button" class="toolbtn" data-toggle="theme"'
         ' title="Giao diện sáng / tối / theo hệ thống">◐ Theo hệ thống</button>'
         '<button type="button" class="toolbtn" data-toggle="reading" aria-pressed="false"'
         ' title="Chế độ đọc: cột hẹp, giãn dòng, ẩn badge và ảnh">¶ Chế độ đọc</button>'
         '</span>')


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
    return '<nav class="topnav">' + " · ".join(parts) + TOOLS + "</nav>"


def footer(depth: int) -> str:
    rel = "../" * depth
    return (f'<div class="footer">{E(C.PROJECT["title"])} · bản dựng {E(C.PROJECT["version"])} · HTML sinh bởi build.py từ content/*.md<br>'
            f'<b>Phép thử năng lực viết của AI, không phải công trình sử học. Đừng trích dẫn làm chứng cứ.</b> '
            f'<a href="{rel}overview.html#ve-du-an">Đọc giới hạn của dự án</a> · '
            f'Dữ liệu danh tính/niên đại: <a href="https://www.wikidata.org" rel="noopener">Wikidata</a> (CC0) · '
            f'Ảnh: <a href="{rel}credits.html">Credits</a> · Mã: MIT · Nội dung: CC BY-SA 4.0</div>')


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
        return f'<div class="sec"><h4>{title}</h4><ul class="links">{"".join(li)}</ul></div>'

    # cạnh ngược: ai ghi "Kế thừa từ" người này (tính tự động)
    rev = [(q, l) for q in persons.values() for l in q["inherits"] if l["target"] == p["id"]]
    rev_html = ""
    if rev:
        li = "".join(f'<li>{anchor_link(q["id"], persons, False)} <span class="badge rel rel-{E(C.slug(l["relation"]))}">{E(l["relation"])}</span> <span class="badge ev ev-{E(C.slug(l["evidence"]))}">{E(l["evidence"])}</span></li>' for q, l in rev)
        rev_html = f'<div class="sec"><h4>Được ghi là nguồn kế thừa bởi <span class="muted small">(tự động từ dữ liệu)</span></h4><ul class="links">{li}</ul></div>'

    return f'''<article class="person" id="{E(p["id"])}">
  {figure_html(p, images, wd_cache, depth)}
  <div class="body">
    <h3><a class="anchor" href="#{E(p["id"])}">#</a>{E(p["name_vi"])}{labels}{alive} <span class="orig">{E(p["name_orig"])}</span></h3>
    <div class="badges">{" ".join(badges)}</div>
    <div class="sec"><h4>Tư tưởng / đóng góp chính</h4>{md_inline(p["ideas"])}</div>
    <div class="sec"><h4>Vì sao chọn</h4>{md_inline(p["why"])}</div>
    {links(p["inherits"], "Kế thừa từ")}
    {links(p["influences"], "Ảnh hưởng tới")}
    {rev_html}
    <div class="sec sources"><h4>Nguồn</h4>{md_inline(p["sources"])}</div>
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
            seq = sorted(g["persons"], key=lambda x: (x["born"] if x["born"] is not None else 0, x["id"]))
            parts.append(mermaid_block(
                mermaid_timeline(g),
                caption="Xếp theo năm, khoảng cách không theo tỉ lệ thời gian.",
                names=" → ".join(f'{p["name_vi"]} ({life_label(p)})' for p in seq)))
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
    body = f'''<a class="skip-link" href="#frame">Bỏ qua điều hướng, tới nội dung</a>
<button class="menu-btn" id="menu-btn" aria-label="Mở mục lục" aria-controls="sidebar" aria-expanded="false">☰</button>
<aside class="sidebar" id="sidebar" aria-label="Mục lục">
  <div class="brand"><a href="#intro" id="brand-link"><h1>{E(C.PROJECT["title"])}</h1></a><div class="sub">{E(C.PROJECT["subtitle"])}</div></div>
  <label class="vh" for="q">Tìm nhân vật theo tên, lĩnh vực hoặc vùng</label>
  <input id="q" type="search" placeholder="Tìm tên, lĩnh vực, vùng…" autocomplete="off">
  <div id="hits" role="region" aria-live="polite" aria-label="Kết quả tìm kiếm"></div>
  <div class="group-title">Tổng quan</div>
  <a class="item top" href="overview.html" data-page="overview.html"><span class="lbl">Overview — timeline &amp; dòng chảy tư tưởng</span></a>
  <a class="item top" href="credits.html" data-page="credits.html"><span class="lbl">Credits — ảnh &amp; giấy phép</span></a>
  <nav aria-label="Chapter và phụ lục">
  <div class="group-title">Chapter</div>
  {"".join(items)}
  {app_block}
  </nav>
  <div class="foot">{len(persons)} nhân vật · bản dựng {E(C.PROJECT["version"])}<br><a id="open-new" href="overview.html" target="_blank">Mở trang hiện tại trong tab mới ↗</a></div>
</aside>
<main class="main"><div class="framebar"><button id="prev" title="Chapter trước" aria-label="Chapter trước">←</button><span id="crumb"></span><button id="next" title="Chapter sau" aria-label="Chapter sau">→</button>{TOOLS}</div><iframe id="frame" name="frame" src="overview.html" title="Nội dung"></iframe></main>
<script src="data/persons.js"></script>
<script src="assets/app.js?v={ASSET_V}"></script>'''
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
    def dist(items: list[str], universe: list[str] | None = None) -> dict:
        """universe: liệt kê cả giá trị đếm 0. Một vùng không ai thuộc về sẽ biến mất
        khỏi bảng nếu chỉ đếm cái có mặt — mà đó đúng là con số cần nhìn thấy nhất."""
        c = Counter(items)
        tot = sum(c.values()) or 1
        keys = [k for k, _ in c.most_common()]
        if universe:
            keys += [k for k in universe if k not in c]
        return {k: {"n": c.get(k, 0), "pct": round(100 * c.get(k, 0) / tot, 1)} for k in keys}
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
    out["all"] = {"regions": dist(all_regions, C.REGIONS), "fields": dist(all_fields, C.FIELDS), "relations": dist(all_rel), "evidence": dist(all_ev), "big_questions": dist(all_bq)}
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
<section class="note" id="ve-du-an">
<h2>Về dự án — đọc trước khi dùng</h2>
<p><b>Đây là một phép thử năng lực viết của mô hình ngôn ngữ, không phải một công trình sử học.</b> Câu hỏi mà dự án đặt ra là: dưới một bộ ràng buộc chặt — trần chữ, từ vựng đóng, tiêu chí chọn công khai, lint và một vòng bình duyệt — thì một mô hình ngôn ngữ viết được tới đâu, và hỏng ở đâu. Lịch sử tư tưởng ở đây là <b>vật liệu đem ra thử</b>, không phải sản phẩm được bảo chứng.</p>
<p><b>Sử học là một ngành có phương pháp, và atlas này không làm theo phương pháp đó.</b> Nghiên cứu lịch sử tử tế đòi đọc sử liệu gốc, phê phán nguồn, biết một luận điểm đang đứng ở đâu trong tranh luận chuyên môn, và chịu trách nhiệm trước đồng nghiệp trong ngành. Không khâu nào trong số đó có ở đây. Vì vậy, nói thẳng ba điều:</p>
<ul>
<li><b>Đừng dùng thay cho việc nghiên cứu lịch sử.</b> Nó không thay được, và không nhằm thay.</li>
<li><b>Đừng trích dẫn nó làm chứng cứ</b> — trong bài vở, bài báo, bài viết, hay một cuộc tranh luận.</li>
<li><b>Đừng coi nó là tài liệu tham khảo.</b> Mục "Nguồn" là chỗ để bạn đi tiếp, không phải chỗ để dừng lại.</li>
</ul>
<p>Việc nó làm được: cho bạn một điểm khởi hành và một cái cớ để tò mò, rồi đẩy bạn tới nguồn thật. Và cho người làm AI một mẫu vật để xem mô hình viết hỏng kiểu gì khi bị ép vào ràng buộc — những chỗ hỏng tìm được đều ghi lại công khai, không xoá dấu. Mô tả trên ứng với bản này; nếu sau này có chuyên gia thật bình duyệt thì đoạn này sẽ phải viết lại.</p>
<p><b>Phần văn xuôi do mô hình AI viết.</b> Toàn bộ phần "Tư tưởng / đóng góp chính", "Vì sao chọn", bối cảnh nhóm, giới thiệu chapter và ghi chú biên tập đều do mô hình ngôn ngữ (Claude của Anthropic) soạn theo một prompt cố định lưu tại <code>prompts/atlas-prompt.md</code>. Không có nhà sử học hay chuyên gia nào viết hoặc bình duyệt những đoạn này. Văn bản là <i>tổng hợp</i> do model thực hiện, không phải nghiên cứu sơ cấp.</p>
<p><b>Phần nào KHÔNG do model quyết định.</b> Tên, năm sinh, năm mất, định danh nhân vật và liên kết ảnh được đối chiếu tự động với <a href="https://www.wikidata.org" rel="noopener">Wikidata</a> (CC0) bằng <code>build.py</code>; chênh lệch niên đại vượt ngưỡng sẽ bị báo và phải xử lý tay. Ảnh lấy từ Wikimedia Commons theo chính sách giấy phép cứng trong <code>fetch_images.py</code>. Cấu trúc chapter, từ vựng lĩnh vực/vùng/quan hệ và mọi ngưỡng kiểm tra là do người đặt ra.</p>
<p><b>Về mục "Nguồn".</b> Mỗi nhân vật có 1–2 nguồn tham khảo do model liệt kê. Với nguồn có đường dẫn, sự tồn tại của trang đã được kiểm tự động trước khi đưa vào; với sách và mục từ bách khoa thì chỉ kiểm ở mức tên tài liệu. <b>Nội dung bên trong nguồn chưa được đối chiếu từng câu với phần văn xuôi.</b> Hãy coi mục Nguồn là điểm khởi đầu để tự kiểm tra, không phải bằng chứng đã được xác minh — trích dẫn sai hoặc bịa là lỗi đã biết của mô hình ngôn ngữ.</p>
<p><b>Mỏng thì được, sai thì không.</b> Bản này cố ý giữ một khung gọn để nhìn được suốt chiều dài lịch sử. Mọi chapter đã qua ít nhất một vòng bình duyệt độc lập (do agent AI, không phải chuyên gia); lỗi dữ kiện tìm được đã sửa, phần còn phải Owner quyết thì ghi ở §11 của file dưới đây. Những gì còn mỏng, còn thiếu góc nhìn, còn tranh luận hoặc chưa kiểm được đều được ghi công khai trong <a href="KNOWN-ISSUES.md"><code>KNOWN-ISSUES.md</code></a>, kèm báo cáo bình duyệt gốc trong <code>reviews/</code>.</p>
<p class="small muted">Nếu bạn phát hiện một chi tiết sai, một nguồn không tồn tại, hoặc một quy kết không có cơ sở — xin báo lại. Đó là cách dự án này khá lên.</p>
</section>

<section class="note" id="gioi-han">
<h2>Giới hạn của atlas này</h2>
<p><b>Đây không phải bảng xếp hạng.</b> Mỗi mục được chọn theo bốn tiêu chí, xếp theo thứ tự ưu tiên: (a) phạm vi ảnh hưởng, (b) độ bền theo thời gian, (c) tính nguyên bản, (d) counterfactual — nếu không có người này thì thay đổi có đến muộn hơn đáng kể không. Bốn tiêu chí đó là một khung do người đặt ra, không phải một phép đo. Đổi khung thì đổi danh sách. Mục "Vì sao chọn" của mỗi nhân vật nêu đích danh 1–2 người cùng thời đã bị loại và lý do, để bạn tự đánh giá được phán đoán đó thay vì phải tin.</p>
<p><b>Mỗi nhóm tối đa 12 người.</b> Đó là ràng buộc của định dạng, không phải kết luận lịch sử. Nhiều nhân vật xứng đáng bị loại chỉ vì nhóm đã đầy; danh sách bị loại và lý do nằm ở mục "Ghi chú biên tập" cuối mỗi chapter — nên đọc phần đó cùng với danh sách chính.</p>
<p><b>Độ sâu nguồn rất mỏng.</b> Mỗi mục dẫn 1–2 nguồn. Đủ để lần ra đầu mối, không đủ để dùng làm căn cứ. Đừng trích atlas này trong bài viết học thuật — hãy đi tới nguồn, rồi trích nguồn.</p>
<p><b>Niên đại nhiều mục không chắc chắn.</b> Huy hiệu "niên đại: Cao / Trung bình / Thấp" trên mỗi thẻ là mức tin cậy của chính niên đại đó. Với nhân vật cổ đại, trường "năm" đôi khi là khoảng hoạt động hoặc thời gian trị vì chứ không phải năm sinh–mất, và điều này được ghi rõ trong Ghi chú biên tập. Có những trường hợp giới nghiên cứu lệch nhau hàng trăm năm — atlas ghi nhận sự bất định đó thay vì giấu đi.</p>
<p><b>Thiên lệch tư liệu, không chỉ thiên lệch châu Âu.</b> Prompt research có chỉ thị chủ động xét Trung Hoa, Ấn Độ, Ba Tư, thế giới Hồi giáo, châu Phi, châu Mỹ và Đông Nam Á; phân bố theo vùng được công bố ngay trên trang này để bạn tự kiểm tra thay vì phải tin lời hứa. Nhưng còn một thiên lệch sâu hơn không sửa được bằng ý chí: <b>bản thân tư liệu đã thiên lệch</b>. Nền văn minh nào có chữ viết sớm, có truyền thống chép sử, có văn bản sống sót thì có tên người; nền văn minh nào không, thì không. Văn hoá Đông Sơn để lại trống đồng và kỹ thuật đúc đồng ở trình độ cao mà không để lại một cái tên nào — nên nó vắng mặt. Vắng mặt ở đây nghĩa là <i>không có tên được ghi lại</i>, không phải <i>không có đóng góp</i>.</p>
<p><b>Phụ lục Việt Nam dùng thước đo khác.</b> Phụ lục giữ nguyên bốn tiêu chí nhưng đổi hệ quy chiếu: ảnh hưởng được đo trong phạm vi Việt Nam và Đông Nam Á, không phải toàn nhân loại. Vì là hai thước đo khác nhau nên phụ lục <b>không</b> được tính vào thống kê và lưới độ phủ trên trang này. Đừng so sánh trực tiếp một mục ở phụ lục với một mục ở chapter chính — chúng không đo cùng một thứ.</p>
<p><b>"Ảnh hưởng" không có nghĩa là "đáng ngưỡng mộ".</b> Atlas ghi nhận mức độ một người định hình đường đi của tư tưởng hay thiết chế về sau. Nhiều người trong danh sách đạt được điều đó bằng chinh phạt, cưỡng ép hoặc những cách mà hôm nay ta lên án. Có mặt trong atlas là một nhận định về hệ quả, không phải một lời tán thành.</p>
</section>

<section class="note" id="trung-lap">
<h2>Về những giai đoạn còn tranh luận</h2>
<p>Atlas đi qua nhiều giai đoạn mà giới sử học chưa thống nhất, và nhiều nhân vật còn trong ký ức sống của người đang đọc. Nguyên tắc làm việc gồm bốn điều:</p>
<p><b>1. Ghi nhận tranh luận, không phân xử.</b> Khi một vấn đề còn chưa khép lại trong giới nghiên cứu — nhà Triệu có thuộc quốc thống Việt Nam hay không là ví dụ rõ nhất — atlas trình bày các lập trường và nguồn của chúng, rồi dừng ở đó. Mục đích là để bạn thấy được cuộc tranh luận, không phải để nhận một kết luận có sẵn.</p>
<p><b>2. Nhân vật được chọn vì hệ quả, không vì lập trường.</b> Có mặt trong atlas nghĩa là người đó đã định hình đáng kể đường đi về sau — không phải một đánh giá đạo đức, không phải lời tán thành, cũng không phải lời lên án.</p>
<p><b>3. Giai đoạn càng gần, kết luận càng tạm.</b> Tiêu chí (b) độ bền cần thời gian mới đo được. Vì vậy phụ lục Việt Nam dừng ở thế kỷ 20 và không lập nhóm thế kỷ 21; với giai đoạn 1954–1975, phụ lục hiện phản ánh một góc nhìn: đánh giá độc lập cho thấy nhân vật phía Việt Nam Cộng hoà và giai đoạn Đổi mới chưa được cân nhắc, và điều đó được ghi rõ trong Ghi chú biên tập thay vì che đi.</p>
<p><b>4. Phân biệt sự kiện với quy kết.</b> Atlas nêu những gì có nguồn và tránh gán động cơ cho người đã khuất hay người còn sống. Với nhân vật đương đại hoặc mới qua đời, phạm vi chỉ gồm những gì đã được ghi chép công khai và liên quan trực tiếp tới ảnh hưởng của họ.</p>
<p class="small muted">Nếu bạn thấy một mục nghiêng lệch, thiếu một lập trường có cơ sở, hoặc nêu sai một sự kiện — xin báo kèm nguồn. Phản hồi có nguồn sẽ được sửa; phản hồi chỉ là quan điểm sẽ được ghi nhận nhưng không làm đổi nội dung.</p>
</section>

<div class="note"><p><b>Trạng thái.</b> Trang này hiện chỉ gồm thống kê trung tính và độ phủ theo nhóm (sinh từ <code>data/persons.json</code>). Ở P5 sẽ bổ sung: timeline toàn cục và graph dòng chảy tư tưởng bằng D3 (đã vendored tại <code>assets/d3.min.js</code>), lọc theo loại quan hệ / lĩnh vực / vùng / giai đoạn, liên kết xuyên vùng theo thời gian, bản đồ vị trí. Việc đối chiếu với giả thuyết do Owner tự làm ngoài pipeline (§9).</p></div>

<h2>Độ phủ theo nhóm (33 nhóm)</h2>
<div class="grid-groups">{"".join(cells)}</div>

<h2>Các chapter</h2>
<div class="tbl-wrap"><table class="tbl">
<thead><tr><th scope="col">#</th><th scope="col">Chapter</th><th scope="col">Giai đoạn</th><th scope="col">Nhóm có dữ liệu</th><th scope="col">Nhân vật</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>

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
    rows, review, nolic, boqua, none = [], [], [], [], []
    for p in sorted(persons.values(), key=lambda x: (x["chapter"], x["group"], x["id"])):
        im = images.get(p["id"]) if images else None
        link = anchor_link(p["id"], persons, True)
        if im and im.get("status") == "embedded":
            lic = f'<a href="{E(im["license_url"])}" rel="noopener">{E(im["license"])}</a>' if im.get("license_url") else E(im["license"])
            rows.append(f'<tr><td><img src="assets/img/{E(im["file"])}" alt="" class="thumb"></td><td>{link}</td><td><a href="{E(im["source_url"])}" rel="noopener">{E(im["title"][5:])}</a></td><td>{E(im.get("author") or "—")}</td><td>{lic}{" <span class=badge>ghi công bắt buộc</span>" if im.get("attribution_required") else ""}</td><td class="small">{E(im.get("caption") or "")}</td></tr>')
        elif im and im.get("status") == "review":
            review.append(f'<li>{link} — <a href="{E(im["source_url"])}" rel="noopener">{E(im["title"])}</a>: {E(im.get("note") or "")}</li>')
        elif im and im.get("status") == "skipped":
            boqua.append(f'<li>{link} — {E(im.get("note") or "bỏ theo content/images.yaml")}</li>')
        elif im and im.get("status") == "no-license":
            nolic.append(f'<li>{link} — <a href="{E(im["source_url"])}" rel="noopener">{E(im["title"])}</a>: {E(im.get("note") or "không rõ giấy phép")}</li>')
        else:
            none.append(link)
    body = topnav(None, chapters, 0) + f'''
<header class="chapter-head"><div class="kicker">Credits</div><h1>Ảnh &amp; giấy phép</h1><div class="meta">{len(rows)} ảnh nhúng · {len(review)} chờ xem xét · {len(nolic)} thiếu giấy phép · {len(boqua)} bỏ có chủ đích · {len(none)} không có ảnh</div></header>
<div class="note"><p><b>Chính sách (PLAN §7.2).</b> Public domain / CC0: nhúng, vẫn ghi nguồn. CC BY / CC BY-SA: nhúng kèm tác giả, tên giấy phép có link, link tệp gốc và ghi chú "đã thu nhỏ". Ảnh có hạn chế quyền (quyền nhân thân, nhãn hiệu…): không nhúng tự động, chờ Owner. Thiếu hoặc không rõ giấy phép: không nhúng, chỉ đặt link tham khảo. Không có P18: link tới Wikipedia/Wikidata. Ảnh được tải về <code>assets/img/</code> (không hotlink) từ Wikimedia Commons theo P18 của <a href="https://www.wikidata.org" rel="noopener">Wikidata</a> (dữ liệu CC0). Override thủ công: <code>content/images.yaml</code>.</p></div>
<div class="tbl-wrap"><table class="tbl">
<thead><tr><th scope="col"><span class="vh">Ảnh</span></th><th scope="col">Nhân vật</th><th scope="col">Tệp gốc trên Commons</th><th scope="col">Tác giả</th><th scope="col">Giấy phép</th><th scope="col">Chú thích</th></tr></thead>
<tbody>{"".join(rows) or '<tr><td colspan=6 class=muted>chưa có ảnh</td></tr>'}</tbody></table></div>
{"<h2>Chờ Owner xem xét</h2><ul>" + "".join(review) + "</ul>" if review else ""}
{"<h2>Thiếu hoặc không rõ giấy phép (không nhúng)</h2><ul>" + "".join(nolic) + "</ul>" if nolic else ""}
{"<h2>Bỏ ảnh có chủ đích</h2><p class=small>Ảnh có tồn tại và giấy phép thường là dùng được, nhưng Owner quyết không nhúng. Lý do ghi ở <code>content/images.yaml</code> và chép lại dưới đây.</p><ul>" + "".join(boqua) + "</ul>" if boqua else ""}
{"<h2>Không có ảnh (thiếu P18 hoặc chưa fetch)</h2><p class=small>" + " · ".join(none) + "</p>" if none else ""}
<h2>Thư viện</h2><p class="small">Mermaid 11.4.1 (MIT, <code>assets/LICENSE-mermaid.txt</code>) · D3 7.9.0 (ISC, <code>assets/LICENSE-d3.txt</code>) · Python-Markdown. Không dùng CDN.</p>
''' + footer(0)
    return page("Credits", body, depth=0)
