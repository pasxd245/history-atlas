"""Linting per PLAN §6.2. ERROR blocks the build; WARN does not. Writes reports/lint-chXX.txt.

A warning usually marks a deliberate decision rather than a defect; the reason is written into the
chapter's editorial note instead of being silenced here."""
from __future__ import annotations

from collections import Counter
from pathlib import Path

from . import common as C

WORD_TARGET = {"ideas": 100, "why": 80, "intro": 100, "context": 60}


def words(s: str) -> int:
    return len([w for w in s.split() if w])


# Thay một mảnh thay vì thay cả trường thì sinh cụm lặp liền kề, và trần chữ không bắt được
# vì bản hỏng vẫn dưới trần (CH05-CE08-09 từng là 120/130). Ngưỡng 2 từ: trên toàn content/
# hiện tại nó không báo nhầm ca nào, còn ngưỡng 1 từ vướng láy đôi ("song song").
REPEAT_MIN, REPEAT_MAX = 2, 12


def repeats(s: str) -> list[str]:
    toks, out, covered = s.split(), [], set()
    for k in range(REPEAT_MAX, REPEAT_MIN - 1, -1):
        for i in range(len(toks) - 2 * k + 1):
            if i not in covered and toks[i:i + k] == toks[i + k:i + 2 * k]:
                out.append(" ".join(toks[i:i + k]))
                covered.update(range(i, i + 2 * k))
    return out


def check_repeats(rep: Report, where: str, label: str, s: str) -> None:
    for frag in repeats(s or ""):
        rep.warn(where, f"'{label}' lặp liền kề một cụm {len(frag.split())} từ: {frag[:60]}")


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
    check_repeats(rep, w, "Giới thiệu chapter", ch["intro"])
    if not ch["editorial"]:
        rep.error(w, "thiếu '## Ghi chú biên tập'")
    else:
        check_repeats(rep, w, "Ghi chú biên tập", "\n".join(ch["editorial"]))
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
        check_repeats(rep, gw, "Bối cảnh", g["context"])
        if len(g["persons"]) > C.PROJECT["max_per_group"]:
            rep.error(gw, f"{len(g['persons'])} nhân vật (> {C.PROJECT['max_per_group']})")
        if not g["persons"]:
            rep.warn(gw, "nhóm rỗng")
        fields = Counter(f for p in g["persons"] for f in p["fields"])
        regions = Counter(p["region"] for p in g["persons"] if p["region"])
        if g["persons"] and len(fields) < 4:
            rep.warn(gw, f"chỉ {len(fields)} lĩnh vực (khuyến nghị ≥ 4)")
        # Đa dạng vùng là tiêu chí của atlas toàn cầu; phụ lục theo một vùng là đúng thiết kế.
        if g["persons"] and len(regions) < 3 and C.is_main(no):
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
                    check_repeats(rep, pw, k, p[k])
            if not p["sources"]:
                rep.error(pw, "thiếu 'Nguồn'")
            else:
                check_repeats(rep, pw, "Nguồn", p["sources"])
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
            # data/images.json là dict phẳng {pid: {status, license, file, …}} do fetch_images.py
            # ghi. Bản trước đọc images["images"][pid]["embed"] — một khoá không tồn tại — nên
            # cổng này chưa bao giờ chạy.
            im = (images or {}).get(p["id"])
            if isinstance(im, dict):
                if im.get("status") == "embedded" and not im.get("license"):
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
    def tracks(ids: list[str]) -> set[str]:
        """Track của từng ID. Trùng giữa atlas chính và phụ lục là CÓ CHỦ Ý (D: liên kết chéo),
        nên hạ xuống INFO; trùng trong cùng một track mới là điều cần cảnh báo."""
        return {C.track_of(int(i[2:4])) for i in ids if C.ID_RE.match(i)}

    for k, ids in by_name.items():
        if len(ids) > 1 and len({i[:4] for i in ids}) > 1:
            if len(tracks(ids)) > 1:
                rep.info(ids[0], f"cùng tên ở cả atlas chính và phụ lục — có chủ ý: {', '.join(ids)}")
            else:
                rep.warn(ids[0], f"cùng tên xuất hiện ở nhiều chapter: {', '.join(ids)}")
    for q, ids in by_q.items():
        if len(ids) > 1:
            if len(tracks(ids)) > 1:
                rep.info(ids[0], f"cùng Wikidata {q} ở cả atlas chính và phụ lục — có chủ ý: {', '.join(ids)}")
            else:
                rep.warn(ids[0], f"cùng Wikidata {q} ở nhiều mục: {', '.join(ids)}")
    # Độ phủ vùng. Kiểm theo nhóm (≥3 vùng, lint_chapter) là chưa đủ: một chapter
    # có thể đạt 4 vùng ở MỌI nhóm mà vẫn là cùng 4 vùng ấy, để 5/9 vùng trống suốt.
    # Ch4 từng qua cổng lint sạch trong khi Châu Mỹ, Đông Nam Á và Châu Đại Dương
    # bằng 0 trên toàn atlas. Hai vòng dưới đây làm khe hở đó hiện ra — ở mức INFO,
    # vì vùng trống có thể là khoảng trống tư liệu thật chứ không phải lỗi chọn người.
    for ch in chapters:
        no = ch["no"]
        if no is None or not C.is_main(no):
            continue
        ps = [p for g in ch["groups"] for p in g["persons"] if p["region"]]
        if not ps:
            continue
        cnt = Counter(p["region"] for p in ps)
        tag = f"ch{no:02d}"
        missing = [r for r in C.REGIONS if r not in cnt]
        if missing:
            rep.info(tag, f"phủ {len(cnt)}/{len(C.REGIONS)} vùng — vắng: {', '.join(missing)}")
        top, n = cnt.most_common(1)[0]
        if n / len(ps) >= 0.6:
            rep.warn(tag, f"{top} chiếm {n}/{len(ps)} ({n / len(ps):.0%}) cả chapter — thiên lệch vùng")
    main_ps = [p for p in all_persons.values()
               if C.ID_RE.match(p["id"]) and C.is_main(int(p["id"][2:4])) and p["region"]]
    if main_ps:
        total = Counter(p["region"] for p in main_ps)
        thin = [r for r in C.REGIONS if total.get(r, 0) <= 1]
        if thin:
            rep.info("atlas", f"vùng ≤1 nhân vật trên {len(main_ps)} mục của atlas chính: "
                              + "; ".join(f"{r} ({total.get(r, 0)})" for r in thin))

    # liên kết một chiều — kiểm cả hai hướng. Lint chỉ quét 'Kế thừa từ' cho tới P2,
    # nên mọi 'Ảnh hưởng tới' trỏ sai đích đều lọt miễn ID có tồn tại; hai vòng đánh
    # giá độc lập đều tìm ra lỗi loại đó. Vòng đối xứng dưới đây đóng khe hở ấy.
    for p in all_persons.values():
        for l in p["inherits"]:
            t = l["target"]
            if t in all_persons and not any(x["target"] == p["id"] for x in all_persons[t]["influences"]):
                rep.info(p["id"], f"kế thừa từ {t} nhưng {t} không ghi 'Ảnh hưởng tới' {p['id']} (P4 sẽ đồng bộ)")
        for l in p["influences"]:
            t = l["target"]
            if t in all_persons and not any(x["target"] == p["id"] for x in all_persons[t]["inherits"]):
                rep.info(p["id"], f"ảnh hưởng tới {t} nhưng {t} không ghi 'Kế thừa từ' {p['id']} (P4 sẽ đồng bộ)")

    # nghịch niên đại: A tác động lên B thì A không thể sinh sau khi B đã mất.
    # 'tương đồng độc lập' loại trừ vì nó khẳng định KHÔNG có tiếp xúc.
    DIRECTED = {"kế thừa", "tổng hợp", "phản bác"}
    for p in all_persons.values():
        pairs = [(p["id"], l["target"], l) for l in p["influences"]]
        pairs += [(l["target"], p["id"], l) for l in p["inherits"]]
        for src_id, dst_id, l in pairs:
            if l.get("relation") not in DIRECTED:
                continue
            src, dst = all_persons.get(src_id), all_persons.get(dst_id)
            if not src or not dst:
                continue
            if src["born"] is not None and dst["died"] is not None and src["born"] > dst["died"]:
                rep.warn(p["id"], f"nghịch niên đại: {src_id} sinh {src['born']} sau khi {dst_id} mất {dst['died']} — không thể '{l.get('relation')}'")
    direct_no_overlap(all_persons, rep)


def _life(p: dict) -> tuple[int, int] | None:
    """Khoảng đời (sinh, mất) dùng được để so chồng đời; None nếu không đủ dữ kiện.
    'trị vì …' / 'hoạt động …' không phải năm sinh–mất: khoảng trị vì nằm TRONG đời, nên
    hai khoảng trị vì không giao nhau không chứng minh hai đời không giao nhau — bỏ qua."""
    if p["born"] is None or C.NON_BIO_YEARS_RE.match((p.get("years_raw") or "").strip()):
        return None
    d = p["died"] if p["died"] is not None else (C.PROJECT["reference_year"] if p["alive"] else None)
    return (p["born"], d) if d is not None else None


def direct_no_overlap(all_persons: dict[str, dict], rep: Report) -> None:
    """CONTRIBUTING quy tắc 9: `trực tiếp` = tiếp xúc người với người, nên hai đời phải giao nhau.
    Vòng bình duyệt ch06–ch11 (2026-11-04) tìm ra 12 cạnh vi phạm điều này bằng phép cộng trừ năm —
    loại lỗi máy bắt được, nên bắt bằng máy. Chồng đời là điều kiện CẦN chứ không ĐỦ: cạnh qua
    được kiểm này vẫn có thể không có tiếp xúc nào được ghi nhận."""
    seen = set()
    for p in all_persons.values():
        edges = [(l["target"], p["id"], l) for l in p["inherits"]] + [(p["id"], l["target"], l) for l in p["influences"]]
        for src_id, dst_id, l in edges:
            if l.get("evidence") != "trực tiếp" or (src_id, dst_id) in seen:
                continue
            src, dst = all_persons.get(src_id), all_persons.get(dst_id)
            if not src or not dst:
                continue
            a, b = _life(src), _life(dst)
            if not a or not b:
                continue
            if a[1] < b[0] or b[1] < a[0]:
                seen.add((src_id, dst_id))
                rep.warn(p["id"], f"`trực tiếp` giữa hai đời không giao nhau: {src_id} ({C.year_label(a[0])}–{C.year_label(a[1])}) "
                                  f"→ {dst_id} ({C.year_label(b[0])}–{C.year_label(b[1])}) — hạ xuống `qua trường phái` (quy tắc 9)")


def lint_wikidata(all_persons: dict[str, dict], rep: Report, http: C.Http | None = None):
    qids = sorted({p["wikidata"] for p in all_persons.values() if p["wikidata"] and C.QID_RE.match(p["wikidata"])})
    if not qids:
        return
    cache = C.JsonCache(C.WD_CACHE)
    http = http or C.Http(min_interval=1.0)
    ents = C.wd_fetch(http, cache, qids)
    # Wikidata xếp nhiều người thật vào lớp con của Q5 (vd Q20643955 "human biblical
    # figure"). Giải một tầng P279 để chỉ cảnh báo khi lớp đó thật sự không phải người.
    classes = sorted({c for e in ents.values() if e and "error" not in e
                      for c in e.get("P31", []) if c != "Q5"})
    cls_info = C.wd_fetch(http, cache, classes) if classes else {}
    human_cls = {c for c in classes
                 if "Q5" in (cls_info.get(c) or {}).get("P279", [])}

    def cls_label(c):
        e = cls_info.get(c) or {}
        return (e.get("labels", {}).get("vi") or e.get("labels", {}).get("en") or c)

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
        p31 = info.get("P31") or []
        if p31 and not ({"Q5"} & set(p31)) and not (human_cls & set(p31)) and not p["labels"]:
            lbls = ", ".join(f"{cls_label(c)} ({c})" for c in p31[:3])
            rep.warn(pw, f"Wikidata {q} không được xếp là người: P31 = {lbls} — cần nhãn [Tranh cãi lịch sử]?")
        tol = C.DATE_TOLERANCE.get(p["confidence"])
        if tol is None:
            rep.info(pw, "độ tin cậy Thấp — bỏ qua đối chiếu niên đại")
            continue
        # 'trị vì X–Y' và 'hoạt động X–Y' KHÔNG phải năm sinh–mất, nên đem so với
        # P569/P570 là so nhầm loại. Quy ước này có trong CONTRIBUTING cho các vua
        # không rõ năm sinh; ch4–11 sẽ có nhiều mục như vậy.
        if C.NON_BIO_YEARS_RE.match(p["years_raw"].strip()):
            rep.info(pw, f"'năm' ghi theo {p['years_raw'].strip().split()[0]} chứ không phải sinh–mất — bỏ qua đối chiếu niên đại Wikidata")
            continue
        for label, mine_y, wd in (("năm sinh", p["born"], info["P569"]), ("năm mất", p["died"], info["P570"])):
            if mine_y is None or not wd:
                continue
            best = None
            for it in wd:
                if it["year"] is None:
                    continue
                # Với mức chính xác thế kỷ hoặc thiên niên kỷ, giá trị Wikidata là một
                # KHOẢNG chứ không phải một điểm: +0300/p7 nghĩa là "thế kỷ 3", tức
                # 201–300. So bằng khoảng cách tới điểm sẽ báo sai đúng ở đầu khoảng
                # (Galen mất k. 216 bị kêu lệch 84 năm so với "thế kỷ 3" chứa nó).
                if it["precision"] <= 7 and C.year_in_bucket(mine_y, it["year"], it["precision"]):
                    best = (0, it["year"], tol, it["precision"])
                    break
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
    # Mục phạm vi toàn atlas ("atlas", "lint") không khớp tag chapter nào nên
    # trước đây rơi vào khoảng không — không in ra console, không vào report.
    tags = tuple(f"ch{ch['no']:02d}" for ch in chapters if ch["no"] is not None)
    tags += tuple(f"CH{ch['no']:02d}-" for ch in chapters if ch["no"] is not None)
    rest = [(l, w, m) for l, w, m in rep.items if not w.startswith(tags)]
    # Luôn ghi, kể cả khi rỗng: chỉ ghi khi có mục thì một lần chạy sạch để lại
    # nguyên báo cáo cũ (từng báo "365 mục, Châu Đại Dương (1)" khi thực tế là 377 và 2).
    lines = ["LINT toàn atlas — mục không thuộc chapter riêng nào", ""]
    lines += [f"[{l}] {w}: {m}" for level in ("ERROR", "WARN", "INFO") for l, w, m in rest if l == level] or ["(không có mục nào)"]
    (reports_dir / "lint-atlas.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


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
