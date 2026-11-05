"""Unit test cho phần logic dễ sai nhất: phân tích năm, khoảng nhóm, bucket Wikidata,
và hai cổng lint từng hỏng âm thầm. Chạy: `uv run --group dev pytest -q`.

Fixture lint (ch99-bad.md, ch98-wikidata.md) cũng chạy ở đây để con số trong README
không trôi nữa."""
from __future__ import annotations

import json
import re
import sys
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from atlaslib import common as C, lint as L, parse as P, render as R  # noqa: E402


# ---------------------------------------------------------------- parse_years
@pytest.mark.parametrize("raw, born, died, approx, alive, ok", [
    ("551–479 TCN", -551, -479, False, False, True),
    ("k. 470 – 399 TCN", -470, -399, True, False, True),
    ("c. 563 – c. 483 TCN", -563, -483, True, False, True),
    ("63 TCN – 14", -63, 14, False, False, True),
    ("1643–1727", 1643, 1727, False, False, True),
    ("1643-1727", 1643, 1727, False, False, True),
    ("1928–nay", 1928, None, False, True, True),
    ("1928–", 1928, None, False, True, True),
    ("~500 – 430 TCN", -500, -430, True, False, True),     # lỗi cũ: ~ không được nhận
    ("≈ 1200 – 1250", 1200, 1250, True, False, True),
    ("khoảng 1010–1080", 1010, 1080, True, False, True),
    ("TK 6 TCN", None, None, False, False, False),
    ("?", None, None, False, False, False),
    ("", None, None, False, False, False),
])
def test_parse_years(raw, born, died, approx, alive, ok):
    y = C.parse_years(raw)
    assert (y["born"], y["died"], y["approx"], y["alive"], y["ok"]) == (born, died, approx, alive, ok)


# ---------------------------------------------------------------- nhóm / thế kỷ
@pytest.mark.parametrize("gid, rng", [
    ("BCE05", (-500, -401)),
    ("BCE01", (-100, -1)),
    ("CE01", (1, 100)),
    ("CE18", (1701, 1800)),
    ("BCE20_18", (-2000, -1701)),
    ("CE10_14", (901, 1400)),
    ("XYZ", None),
])
def test_group_range(gid, rng):
    assert C.group_range(gid) == rng


@pytest.mark.parametrize("year, wd, prec, inside", [
    (216, 300, 7, True),       # Galen: "thế kỷ 3" = 201..300
    (201, 300, 7, True),
    (200, 300, 7, False),
    (-1250, -1300, 7, True),   # TK 13 TCN = -1300..-1201
    (-1200, -1300, 7, False),
    (-1500, -2000, 6, True),   # thiên niên kỷ 2 TCN
])
def test_year_in_bucket(year, wd, prec, inside):
    assert C.year_in_bucket(year, wd, prec) is inside


# ---------------------------------------------------------------- cổng lint
def _chapter(path: Path) -> list[dict]:
    return [P.parse_chapter([path])]


def test_image_license_gate_fires_on_flat_images_json(tmp_path):
    chs = _chapter(ROOT / "tests" / "ch98-wikidata.md")
    pid = chs[0]["groups"][0]["persons"][0]["id"]
    images = {pid: {"status": "embedded", "file": f"{pid}.jpg", "license": None}}
    rep = L.run(chs, images, online=False, reports_dir=tmp_path)
    assert any("không có thông tin giấy phép" in m for _, m in rep.by_level("ERROR"))
    images[pid]["license"] = "Public domain"
    rep = L.run(chs, images, online=False, reports_dir=tmp_path)
    assert not any("giấy phép" in m for _, m in rep.by_level("ERROR"))


def test_lint_atlas_report_is_rewritten_when_empty(tmp_path):
    stale = tmp_path / "lint-atlas.txt"
    stale.write_text("[INFO] atlas: số cũ\n", encoding="utf-8")
    L.write_reports([], L.Report(), tmp_path)
    assert "số cũ" not in stale.read_text(encoding="utf-8")


def test_bad_fixture_error_count_matches_readme(tmp_path):
    rep = L.run(_chapter(ROOT / "tests" / "ch99-bad.md"), {}, online=False, reports_dir=tmp_path)
    n = rep.count("ERROR")
    readme = (ROOT / "docs" / "vi" / "README.md").read_text(encoding="utf-8")
    m = re.search(r"ch99-bad\.md` → (\d+) ERROR", readme)
    assert m and int(m.group(1)) == n, f"README ghi {m and m.group(1)}, lint ra {n}"


# ---------------------------------------------------------------- version / UA
def test_versions_agree():
    py = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
    disp = C.PROJECT["version"]                      # "v0.0.1-rc.1"
    m = re.fullmatch(r"v(\d+\.\d+\.\d+)-rc\.(\d+)", disp) or re.fullmatch(r"v(\d+\.\d+\.\d+)()", disp)
    assert m, disp
    assert py == m.group(1) + (f"rc{m.group(2)}" if m.group(2) else "")


def test_user_agent_contact(monkeypatch):
    monkeypatch.setenv("HISTORY_ATLAS_CONTACT", "https://example.org/atlas")
    assert C.user_agent().endswith("; https://example.org/atlas)")
    monkeypatch.delenv("HISTORY_ATLAS_CONTACT")
    # Bám PROJECT["version"] chứ không ghim chuỗi: ghim thì mỗi lần bump phiên bản
    # test đỏ mà không có lỗi thật nào.
    assert C.user_agent().startswith(f"history-atlas/{C.PROJECT['version'].lstrip('v')} ")


# ---------------------------------------------------------------- quy tắc 9
def _p(pid, born, died, years_raw=None, inherits=(), influences=()):
    link = lambda t, ev: {"target": t, "relation": "kế thừa", "evidence": ev, "raw": "", "undetermined": False}
    return {"id": pid, "born": born, "died": died, "alive": False,
            "years_raw": years_raw or f"{born}–{died}",
            "inherits": [link(t, ev) for t, ev in inherits], "influences": [link(t, ev) for t, ev in influences]}


def _direct_warns(persons):
    rep = L.Report()
    L.direct_no_overlap({p["id"]: p for p in persons}, rep)
    return [m for _, m in rep.by_level("WARN")]


def test_direct_edge_without_overlap_warns_once():
    # Rousseau mất 1778, Bolívar sinh 1783; cạnh ghi ở cả hai đầu → chỉ báo một lần
    a = _p("CH08-CE18-02", 1712, 1778, influences=[("CH09-CE19-09", "trực tiếp")])
    b = _p("CH09-CE19-09", 1783, 1830, inherits=[("CH08-CE18-02", "trực tiếp")])
    assert len(_direct_warns([a, b])) == 1


def test_direct_edge_overlap_or_weaker_evidence_is_clean():
    a = _p("CH08-CE18-02", 1712, 1778, influences=[("CH08-CE18-03", "trực tiếp")])
    b = _p("CH08-CE18-03", 1724, 1804)
    c = _p("CH09-CE19-09", 1783, 1830, inherits=[("CH08-CE18-02", "qua trường phái")])
    assert _direct_warns([a, b, c]) == []


def test_direct_edge_skips_reign_years():
    a = _p("CH05-CE10-01", 900, 920, years_raw="trị vì 900–920", influences=[("CH05-CE10-02", "trực tiếp")])
    b = _p("CH05-CE10-02", 930, 960)
    assert _direct_warns([a, b]) == []


# ---------------------------------------------------------------- theme / reading mode

CSS = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")


def _tokens(block: str) -> dict[str, str]:
    return dict(re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", block))


def _block_after(selector: str) -> str:
    """Thân khối CSS ngay sau `selector` (giả định không có ngoặc lồng bên trong)."""
    i = CSS.index(selector) + len(selector)
    j = CSS.index("{", i)
    return CSS[j + 1 : CSS.index("}", j)]


def test_dark_khai_bao_hai_lan_phai_giong_het_nhau():
    """CSS thuần không gộp được @media với selector thường, nên khối dark phải viết hai
    lần. Sửa một chỗ mà quên chỗ kia thì nút bấm lệch màu so với 'theo hệ thống'."""
    auto = _tokens(_block_after(':root:not([data-theme="light"])'))
    tay = _tokens(_block_after(':root[data-theme="dark"]'))
    assert auto and tay, "không tìm thấy một trong hai khối dark"
    assert auto == tay


def test_moi_token_dark_deu_duoc_khai_bao_o_light():
    """Token chỉ có ở dark sẽ không có giá trị khi quay lại light."""
    light = _tokens(_block_after(":root"))
    dark = _tokens(_block_after(':root[data-theme="dark"]'))
    assert set(dark) <= set(light), f"token thiếu bản light: {sorted(set(dark) - set(light))}"


def test_moi_trang_dat_theme_truoc_khi_ve():
    """Script đặt data-theme phải nằm trong <head>, trước <body>: để sau thì nháy nền
    sáng một nhịp rồi mới sang tối."""
    html = R.page("T", "<p>x</p>", depth=0)
    assert html.index("ha-theme") < html.index("<body")


def test_nut_theme_va_reading_co_mat_tren_trang_chapter():
    nav = R.topnav(2, [{"no": 2}, {"no": 3}], depth=1)
    assert 'data-toggle="theme"' in nav and 'data-toggle="reading"' in nav


def test_credits_tach_anh_bo_co_chu_dich_khoi_nhom_thieu_P18():
    """Ảnh bỏ có chủ đích có lý do ghi lại; xếp chung với 'thiếu P18 hoặc chưa fetch'
    là nói sai và giấu mất lý do."""
    persons = {
        "CH01-BCE20_18-01": {"id": "CH01-BCE20_18-01", "chapter": 1, "group": "BCE20_18",
                             "name_vi": "A", "slug": "a"},
        "CH01-BCE20_18-02": {"id": "CH01-BCE20_18-02", "chapter": 1, "group": "BCE20_18",
                             "name_vi": "B", "slug": "b"},
    }
    images = {
        "CH01-BCE20_18-01": {"status": "skipped", "note": "lý do riêng của ca này"},
        # CH01-BCE20_18-02 không có bản ghi → đúng nghĩa "không có ảnh"
    }
    html = R.render_credits([{"no": 1}], persons, images)
    assert "1 bỏ có chủ đích · 1 không có ảnh" in html
    assert "lý do riêng của ca này" in html, "lý do phải hiện ra, không chỉ đếm"


def test_uv_lock_khop_phien_ban_pyproject():
    """`uv sync` tự viết lại uv.lock khi phiên bản lệch, nên lockfile cũ làm cây bẩn
    ngay sau khi clone. Mọi lệnh trong dự án đều chạy `--frozen` nên uv không bao giờ
    tự báo — phải kiểm ở đây."""
    ver = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
    lock = (ROOT / "uv.lock").read_text(encoding="utf-8")
    m = re.search(r'name = "history-atlas"\nversion = "([^"]+)"', lock)
    assert m, "không tìm thấy mục history-atlas trong uv.lock"
    assert m.group(1) == ver, f"uv.lock ghi {m.group(1)}, pyproject ghi {ver} — chạy `uv lock`"


# ---------------------------------------------------------------- tài liệu đa ngôn ngữ

def _so_lieu_that() -> dict[str, int | str]:
    """Số liệu lấy thẳng từ dữ liệu build, không chép tay."""
    persons = json.loads((ROOT / "data" / "persons.json").read_text(encoding="utf-8"))["persons"]
    images = json.loads((ROOT / "data" / "images.json").read_text(encoding="utf-8"))
    sts = [v.get("status") for v in images.values()]
    marker = sum(1 for f in (ROOT / "reviews").glob("*.md")
                 for ln in f.read_text(encoding="utf-8").splitlines() if "[KHÔNG KIỂM ĐƯỢC]" in ln)
    co_marker = sum(1 for f in (ROOT / "reviews").glob("*.md")
                    if "[KHÔNG KIỂM ĐƯỢC]" in f.read_text(encoding="utf-8"))
    return {
        "chinh": sum(1 for v in persons.values() if str(v["chapter"]) != "90"),
        "phu_luc": sum(1 for v in persons.values() if str(v["chapter"]) == "90"),
        "anh": sts.count("embedded"),
        "bo": sts.count("skipped"),
        "khong_anh": sts.count("no-image"),
        "marker": marker,
        "file_marker": co_marker,
        "bao_cao": len(list((ROOT / "reviews").glob("*.md"))),
        "phien_ban": C.PROJECT["version"],
    }


# Ba tài liệu cùng kể một bộ số. Bro chọn tách docs/en + docs/vi, nên bề mặt trôi lệch
# nhân lên — bảng này buộc mỗi con số phải khớp dữ liệu build, chứ không khớp trí nhớ.
# (Phiên 2026-11-05 đã bắt ba ca lệch kiểu này: "356 ảnh", "~127 dòng", uv.lock.)
TAI_LIEU = {
    "README.md": ["{chinh} people in the main track", "plus {phu_luc} in a",
                  "{anh} embedded images", "{marker} lines still carry",
                  "{file_marker} of {bao_cao} review reports"],
    "docs/en/README.md": ["**{chinh} people** in the main track", "**{phu_luc}-person Vietnam appendix**",
                          "{anh} are embedded", "{bo} are deliberately omitted",
                          "the {khong_anh} that simply have no image",
                          "**{marker} lines across {file_marker} of the {bao_cao} review reports",
                          "`reviews/` holds all {bao_cao} reports"],
    "docs/vi/README.md": ["{chinh} nhân vật** ở atlas chính", "cộng **{phu_luc} nhân vật**",
                          "{marker} dòng `[KHÔNG KIỂM ĐƯỢC]` trong `reviews/`",
                          "({file_marker}/{bao_cao} báo cáo)"],
}


@pytest.mark.parametrize("ten", sorted(TAI_LIEU))
def test_so_lieu_trong_tai_lieu_khop_du_lieu_build(ten):
    so = _so_lieu_that()
    van_ban = (ROOT / ten).read_text(encoding="utf-8")
    thieu = [m.format(**so) for m in TAI_LIEU[ten] if m.format(**so) not in van_ban]
    assert not thieu, f"{ten} lệch số liệu build, thiếu: {thieu}"


def test_cong_vao_dan_duoc_sang_ca_hai_ngon_ngu():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "docs/en/README.md" in readme and "docs/vi/README.md" in readme
    for ten in ("docs/en/README.md", "docs/vi/README.md"):
        assert (ROOT / ten).exists()


def test_canh_bao_khong_duoc_chi_co_mot_ngon_ngu():
    """Cảnh báo 'đừng trích dẫn làm chứng cứ' mà chỉ có tiếng Việt thì chỉ bảo vệ được
    người đọc tiếng Việt — trong khi ai cũng dịch máy được phần nội dung."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for cau in ("Do not use it in place of historical research",
                "Do not cite it as evidence",
                "Do not treat it as a reference work"):
        assert cau in readme, f"cổng vào thiếu: {cau}"
