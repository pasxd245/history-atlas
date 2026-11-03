# Design + UX review — Atlas nhân vật ảnh hưởng

Phạm vi: `index.html`, `chapters/ch02.html` (33 thẻ), `chapters/ch90.html` (phụ lục VN, 40 thẻ), `overview.html`, `credits.html`.
Đo bằng trình duyệt thật tại 1440 / 1024 / 810 / 768 / 375 px, cả light và dark.
Nội dung chữ nghĩa nằm ngoài phạm vi — mọi mục dưới đây là layout / typography / tương tác / a11y.

**Kết luận ngắn:** nền tảng design lành mạnh. Thang màu sepia, cấu trúc thẻ, hệ thống token CSS, và routing hash đều hợp lý và đúng tinh thần học thuật. Không cần làm lại. Phần lớn vấn đề là **tham số sai** (độ dài dòng, chiều rộng cột, vài giá trị màu) chứ không phải kiến trúc sai — và đều sửa được bằng CSS. Hai ngoại lệ cần đụng `render.py` là nhóm a11y thuộc tính và cái timeline Mermaid.

---

## Sửa rẻ, tác động cao

Toàn bộ mục trong phần này chỉ sửa `assets/style.css`, không đụng `render.py`, không rebuild logic.

### 1. Độ dài dòng 86–101 ký tự — quá dài cho văn xuôi tiếng Việt
**Severity: high**

Đo tại 1440px trên `chapters/ch02.html`, đoạn "Tư tưởng / đóng góp chính" của thẻ đầu tiên:

| viewport | bề rộng đoạn | số dòng | ký tự/dòng (TB) |
|---|---|---|---|
| 1440 | 734px | 6 | **86** (dòng 1: **101**) |
| 1024 (trong iframe → 704px) | ~500px | 8 | 64 |
| 768 | 502px | 8 | **64** ✓ |
| 375 | 297px | 13 | 40 |

Khoảng dễ đọc là 45–75 ký tự. Ở 1440 — tức là cấu hình desktop phổ biến nhất — mỗi dòng dài **86 ký tự**, vượt trần 15%. Nghịch lý: trang đọc tốt nhất ở 768px và tệ nhất ở màn hình lớn.

Nguyên nhân: `body:not(.index) { max-width: 1000px }` (style.css:17) giới hạn *trang*, nhưng không có gì giới hạn *đoạn văn*. Thẻ `.person` là grid `170px 1fr`, nên cột `1fr` nuốt toàn bộ phần còn lại.

**Fix** — giới hạn ở chính khối văn xuôi, không đụng badge/link list (những thứ này nên được rộng):

```css
.person .sec p,
.person .sec > p,
.intro p,
.context,
.note p { max-width: 68ch; }
```

`ch` ở Georgia 16px ≈ 8.0px → 68ch ≈ 544px, cho ~70 ký tự/dòng. Dùng `ch` thay vì `px` để tự co theo font-size người dùng.

### 2. Timeline Mermaid bị ép co — chữ 16px render ra 3–9px
**Severity: high** (đây là lý do nó trông như "decorative noise")

Đây là lỗi đo được rõ nhất trong cả bản review. SVG có `viewBox="0 0 1590 519.23"`, tức bề rộng nội tại **1590px**. Nhưng nó bị ép vừa khung chứa:

| viewport | bề rộng SVG render | tỉ lệ | chữ 16px hiển thị thực |
|---|---|---|---|
| 1440 (standalone) | 934px | 0.587 | **9.4px** |
| 768 | 702px | 0.442 | **7.1px** |
| 375 | 309px | 0.194 | **3.1px** |

Ở *mọi* breakpoint timeline đều dưới ngưỡng đọc được. Trên mobile nó là 3.1px — không phải chữ nữa, là texture.

Nguyên nhân là hai dòng đánh nhau trong style.css:54–55:

```css
.mermaid-wrap { overflow-x: auto; }               /* ý định: cho cuộn ngang */
.mermaid-wrap .mermaid svg { max-width: 100%; }   /* nhưng dòng này ép co thay vì cho cuộn */
```

`overflow-x: auto` không bao giờ kích hoạt vì SVG luôn tự co vừa khung. Đã xác nhận: `mermaid-wrap.scrollWidth === clientWidth` ở cả 375 và 1440.

**Fix** — để SVG giữ kích thước thật và cho khung cuộn ngang, đúng như ý định ban đầu:

```css
.mermaid-wrap .mermaid svg {
  max-width: none;   /* huỷ cả max-width:100% ở đây lẫn style="max-width:1590px" mermaid tự chèn */
  width: auto;
  height: auto;
}
.mermaid-wrap { overflow-x: auto; overscroll-behavior-x: contain; }
```

Đánh đổi: phải cuộn ngang. Với một timeline 7–10 người thì cuộn ngang đọc được vẫn tốt hơn nhiều so với 7 nhãn không đọc nổi. Thêm gợi ý cuộn:

```css
.mermaid-wrap { background-image: linear-gradient(to left, var(--panel), rgba(0,0,0,0) 24px); }
```

### 3. Thanh thống kê ở overview chỉ rộng 41px
**Severity: high**

Trên `overview.html`, `.bars .row` tính ra `grid-template-columns: 150px 41.33px 80px` bên trong thẻ `.cards2 .c` rộng 313px. Nghĩa là:

- Thanh dài nhất (giá trị 100%) = **41px**
- Thanh ngắn nhất ("Châu Phi hạ Sahara", "Trung Á") = **2.89px**

Một biểu đồ cột mà cột lớn nhất 41px và nhỏ nhất 3px thì không so sánh được gì — con số bên phải đang làm toàn bộ công việc, còn thanh chỉ là nhiễu. Đồng thời cột nhãn cố định `150px` chiếm 48% bề rộng thẻ trong khi nhãn thật chỉ cần ~50px ("Nam Á", "Đông Á").

Nguồn: style.css:82 (`.bars .row { grid-template-columns: 150px 1fr 80px }`) + style.css:79 (`.cards2 { minmax(280px, 1fr) }`).

**Fix** — cho thanh ăn trọn bề ngang, nhãn và số lên một dòng riêng:

```css
.bars .row {
  display: grid;
  grid-template-columns: 1fr max-content;
  gap: 2px 8px;
  margin: 7px 0;
}
.bars .row > span:first-child { grid-column: 1; }
.bars .n { grid-column: 2; text-align: right; }
.bars .bar { grid-column: 1 / -1; height: 8px; }
```

Thanh dài nhất khi đó ≈ 289px thay vì 41px — gấp 7 lần, đọc được ngay. Giữ nguyên `render.py`.

### 4. Bảy lỗi tương phản ở badge — sai ở **cả** light và dark
**Severity: high**

Đo bằng công thức WCAG 2.1 trên DOM thật. Badge là `font: 600 .72rem` = **11.52px bold** → *không* tính là large text, nên ngưỡng AA là **4.5:1**.

| badge | light | dark | ngưỡng |
|---|---|---|---|
| `.person h3 .anchor` ("#") | **1.33** | **1.27** | 4.5 |
| `.badge.conf-thap` | **2.86** | **4.23** | 4.5 |
| `.badge.conf-trung-binh` | **3.08** | **3.92** | 4.5 |
| `.badge.ev-suy-doan-hoc-gia` | **3.45** | **3.45** | 4.5 |
| `.badge.ev-qua-truong-phai` | **3.72** | **3.72** | 4.5 |
| `.badge.conf-cao` | **4.17** | **2.90** | 4.5 |
| `.badge.rel-tuong-dong-doc-lap` | **4.39** | **4.39** | 4.5 |

Các badge còn lại đạt: `rel-ke-thua` 5.04, `ev-truc-tiep` 5.23, `year` 5.43, `rel-phan-bac` 6.54, `legend-lbl` 7.33, `bq` 8.45, `place/region/field/wd` 9.55.

Lỗi gốc của nhóm `conf-*`: style.css:38 chỉ đặt `color`, để nền là `var(--chip)` — mà `--chip` lật màu theo theme còn chữ thì không. Nên `conf-cao` tốt hơn ở light (4.17) và tệ hơn ở dark (2.90).

**Fix** — chỉnh giá trị token cho đủ 4.5:1, và cho `conf-*` một token riêng theo theme:

```css
:root {
  --rel-tuong-dong-doc-lap: #4d6673;   /* 4.39 → 6.06 với #fff */
  --ev-qua-truong-phai:     #8a5f14;   /* 3.72 → 5.63 */
  --ev-suy-doan-hoc-gia:    #6b6b6b;   /* 3.45 → 5.33 */
  --conf-cao: #216139; --conf-trung-binh: #7d560f; --conf-thap: #5f5f5f;  /* 6.14 / 5.42 / 5.29 trên --chip */
}
@media (prefers-color-scheme: dark) {
  :root {
    --conf-cao: #7fc79b; --conf-trung-binh: #e0b05a; --conf-thap: #a79e94;  /* 7.33 / 7.31 / 5.53 */
  }
}
```

Và cho cái `#` neo (1.33:1 — gần như vô hình, nhưng nó *là* một link có thể focus):

```css
.person h3 .anchor { color: var(--muted); opacity: .45; }
.person h3 .anchor:hover,
.person h3 .anchor:focus-visible { opacity: 1; color: var(--accent); }
```

### 5. Lưới độ phủ ở overview: ô đậm nhất fail tương phản
**Severity: medium**

| | light | dark |
|---|---|---|
| `.l3` (#c9834c + #fff) | **3.07** | **3.07** |
| `.l4` (`var(--accent)` + #fff) | 7.73 ✓ | **2.53** |

`.l4` hỏng riêng ở dark vì `--accent` lật từ `#8a3b12` (nâu đậm) sang `#e0905c` (cam nhạt) mà chữ vẫn cứng `#fff` → chữ trắng trên nền cam nhạt. Trớ trêu là **l3/l4 chính là các ô có nhiều nhân vật nhất** — thông tin quan trọng nhất lại khó đọc nhất.

Ngoài ra `.l1`/`.l2` hardcode màu sáng (`#f0d9c6`, `#e2b48f`) không có override dark → ở dark mode chúng là những khối hồng chói trên nền tối. Tương phản chữ vẫn đạt (8.21) nên đây thuần tuý là lệch tông.

**Fix:**

```css
.grid-groups a.l3 { background: #a85f2a; color: #fff; }   /* 4.84:1 */
.grid-groups a.l4 { background: var(--accent); color: var(--panel); } /* 7.73 light / 6.64 dark */
@media (prefers-color-scheme: dark) {
  .grid-groups a.l1 { background: #40301f; color: #e8cdb4; }
  .grid-groups a.l2 { background: #6b472c; color: #f5e3d4; }
}
```

### 6. Không có `prefers-reduced-motion` — không một dòng nào
**Severity: medium**

Quét toàn bộ `document.styleSheets`: **0 rule** chứa `prefers-reduced-motion`. Trong khi đó đang bật:

- `html { scroll-behavior: smooth }` (style.css:15) — toàn cục
- `.sidebar { transition: transform .2s }` (style.css:119)

Hệ quả cụ thể: `chapters/ch02.html` cao **52.925px** (62 màn hình ở mobile). Bấm một link trong `.groupnav` kích hoạt một cú cuộn mượt đi qua hàng chục nghìn pixel — vừa gây khó chịu vừa là vấn đề thật với người nhạy cảm chuyển động.

**Fix:**

```css
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
  }
}
```

### 7. Không có style focus nào được định nghĩa
**Severity: medium**

Quét stylesheet: **0 rule** chứa `:focus` hoặc `:focus-visible`. Toàn bộ hiển thị focus đang phó mặc cho mặc định của trình duyệt. Chrome vẫn vẽ ring nên *không phải* lỗi blocking, nhưng:

- `.sidebar a.item.active` có nền `--accent-soft` → ring mặc định chìm vào nền đó
- `.grid-groups a` có nền riêng từng cấp
- `.person h3 .anchor` ở 1.33:1 thì focus ring là tín hiệu *duy nhất* nhận ra nó

Trang có **70 điểm dừng tab** chỉ riêng ở sidebar — focus phải thấy rõ, không thể để mặc định.

**Fix:**

```css
:where(a, button, summary, input, [tabindex]):focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: 6px;
}
```

### 8. Sidebar chiếm tới 40% màn hình ở vùng 801–1000px
**Severity: medium**

Breakpoint thu gọn sidebar đặt ở `max-width: 800px` (style.css:116) trong khi `--sidebar-w` cố định `320px`:

| viewport | sidebar | iframe | sidebar chiếm |
|---|---|---|---|
| 1440 | 320px | 1120px | 22% ✓ |
| 1024 | 320px | 704px | **31%** |
| 810 | 320px | **490px** | **40%** |

Ở 810px, khung đọc chỉ còn 490px trong khi điều hướng ăn 320px. Đây là vùng tệ nhất của cả layout — và nó nằm ngay trên breakpoint, tức là tablet ngang và cửa sổ desktop hẹp rơi đúng vào đó.

**Fix** — nâng breakpoint và cho sidebar co lại trước khi biến mất:

```css
:root { --sidebar-w: clamp(240px, 24vw, 320px); }
@media (max-width: 1000px) { /* đổi từ 800px */
  body.index { grid-template-columns: 1fr; }
  .menu-btn { display: block; }
  /* … phần còn lại của block giữ nguyên … */
}
```

### 9. Hàng badge là một bức tường chip không phân cấp
**Severity: medium**

Đếm trên ch02: **7–9 badge/thẻ** ở hàng `.badges`, cộng thêm **12 badge nữa** trong các `ul.links` của cùng một thẻ → khoảng 19–21 chip mỗi nhân vật. Trên mobile hàng badge cao 95px, chiếm **4 dòng**.

Vấn đề không phải số lượng mà là **không phân biệt được**. Đo computed style, 4 loại badge khác hẳn nhau về ngữ nghĩa lại giống hệt nhau về hình thức:

| badge | nền | chữ |
|---|---|---|
| `.badge.place` (Ionia, nay thuộc bờ tây…) | `rgb(239,233,223)` | `rgb(74,68,61)` |
| `.badge.region` (Châu Âu) | `rgb(239,233,223)` | `rgb(74,68,61)` |
| `.badge.field` (Văn học) | `rgb(239,233,223)` | `rgb(74,68,61)` |
| `.badge.wd` (Q6691) | `rgb(239,233,223)` | `rgb(74,68,61)` |

Byte-for-byte y hệt. Người đọc không có cách nào biết "Châu Âu" là *vùng* còn "Văn học" là *lĩnh vực* ngoài việc tự suy ra từ nội dung. Thêm nữa `.badge.place` chứa chuỗi dài ("Ionia, nay thuộc bờ tây Thổ Nhĩ Kỳ") với `white-space: nowrap` — một chip dài gần hết hàng, đứng cạnh các chip một từ.

Tin tốt: `render.py:187–195` **đã** phát class riêng (`place`, `region`, `field`, `wd`). Chỉ là CSS chưa dùng tới. Nên đây là fix thuần CSS.

**Fix** — tách 3 tầng: nhận dạng (năm) → phân loại (vùng/lĩnh vực) → siêu dữ liệu (ID, độ tin cậy):

```css
/* tầng 2: phân loại — viền thay vì nền đặc, phân biệt bằng sắc độ */
.badge.region { background: transparent; box-shadow: inset 0 0 0 1px var(--line); color: var(--muted); }
.badge.field  { background: var(--chip); color: var(--chip-ink); }
.badge.place  { background: transparent; color: var(--muted); padding-left: 0;
                white-space: normal; font-weight: 400; }
/* tầng 3: siêu dữ liệu — đẩy xuống cuối, nhạt đi */
.badge.wd, .badge.conf { background: transparent; box-shadow: inset 0 0 0 1px var(--line); }
.badges { gap: .3em .45em; align-items: center; }
```

Gợi ý mạnh hơn (cần `render.py`): bỏ `.badge.place` khỏi hàng chip, đưa xuống thành một dòng `.small.muted` dưới tên — nó là câu chứ không phải nhãn. Sửa ở `render.py:187`.

### 10. `line-height` và `font-size` tuyệt đối
**Severity: nice-to-have**

Đã kiểm tra va chạm dấu phụ một cách cụ thể: hộp inline 18.0px, bước dòng 25.6px → khoảng hở **7.6px**. Dấu chồng (Ồ, Ẫ, ộ, ậ) **không** va vào descender dòng dưới ở `line-height: 1.6`. **Không có vấn đề va chạm** — đừng sửa vì lý do đó.

Nhưng 1.6 là sàn, và nó đang đi kèm dòng dài 86 ký tự (mục 1) — dòng càng dài thì leading càng phải rộng để mắt quét ngược không nhảy dòng. Sau khi áp mục 1, nâng lên 1.7 cho riêng văn xuôi:

```css
.person .sec p, .intro p, .context { line-height: 1.72; }
```

Riêng `body { font: 16px/1.6 … }` (style.css:16) đặt font-size bằng **px tuyệt đối**, ghi đè thiết lập cỡ chữ mặc định của trình duyệt người dùng. Đổi sang đơn vị tương đối:

```css
body { font: 1rem/1.6 "Noto Serif", Georgia, "Times New Roman", serif; }
```

---

## Cần sửa `atlaslib/render.py`

### 11. Timeline Mermaid nhóm theo lĩnh vực nhưng vẽ như trục thời gian — gây hiểu sai
**Severity: high** — đây là vấn đề *khái niệm*, không phải thẩm mỹ

Trả lời trực tiếp câu hỏi "có hữu ích hay chỉ là nhiễu trang trí": **hiện tại là nhiễu, và tệ hơn nhiễu — nó sai lệch.**

`render.py:69–79` nhóm người theo `p["fields"][0]` rồi phát ra `timeline` của Mermaid. Mermaid vẽ một **mũi tên ngang chạy từ trái sang phải** — tín hiệu thị giác phổ quát cho "thời gian tăng dần". Nhưng vị trí ngang thực tế chỉ là thứ tự tuần tự trong từng section, hoàn toàn không phải thời gian.

Đo toạ độ x thật của nhóm TK 8 TCN:

| vị trí x | nhân vật | năm sinh |
|---|---|---|
| 356 | Amos | 760 TCN |
| 473 | Isaiah | **740** TCN |
| 589 | Homer | **750** TCN |
| 706 | Hesiod | 730 TCN |
| 813 | Yajnavalkya | **750** TCN |
| 919 | Tiglath-Pileser III | 745 TCN |
| 1064 | Piye | **744** TCN |

Piye (744 TCN) nằm **bên phải** Hesiod (730 TCN) — tức người sớm hơn bị vẽ muộn hơn. Thứ tự đúng theo thời gian phải là Amos → Homer → Yajnavalkya → Tiglath → Piye → Isaiah → Hesiod. Với một trang tham khảo học thuật, một trục thời gian không theo thời gian là lỗi nội dung chứ không phải lỗi style.

Cộng thêm (đo được):
- `timeline: { disableMulticolor: true }` ở `render.py:109` **không có tác dụng**: vẫn ra 4 màu section khác nhau — `rgb(134,134,255)`, `rgb(255,255,120)`, `rgb(215,255,134)`, `rgb(195,134,255)`. Tím/vàng neon/xanh chanh, chỏi hoàn toàn với bảng màu sepia.
- Chữ trắng trên các dải đó: **3.06:1** và **2.57:1** — fail AA. Mermaid tự chọn trắng/đen không nhất quán (cùng một hàng, "Tôn giáo/Tâm linh" trắng còn "Văn học" đen).
- Ở **dark mode**, dải section tính ra `rgb(31,32,32)` trên nền panel `rgb(32,29,25)` → tương phản **1.03:1**. Nhóm section biến mất hoàn toàn.
- Nhãn bị nối sai khi wrap: `"k. 760 TCN – 745TCN"` (mất dấu cách).

**Ba lựa chọn, theo thứ tự tôi khuyến nghị:**

**(a) Bỏ hẳn timeline Mermaid, thay bằng dải năm thuần CSS.** Dữ liệu đã có sẵn (`born`/`died`), bố cục theo *thời gian thật*, không cần thư viện 2.5MB, tự động hợp theme. Sửa `render.py:260–261`:

```python
def century_strip(group: dict) -> str:
    ps = [p for p in group["persons"] if p["born"] is not None]
    if len(ps) < 2:
        return ""
    lo = min(p["born"] for p in ps); hi = max(p["born"] for p in ps)
    span = (hi - lo) or 1
    items = []
    for p in sorted(ps, key=lambda x: x["born"]):
        pct = 100 * (p["born"] - lo) / span
        fld = C.slug(p["fields"][0]) if p["fields"] else "khac"
        items.append(
            f'<a class="tl-item f-{E(fld)}" style="left:{pct:.1f}%" '
            f'href="#{E(p["id"])}" title="{E(life_label(p))}">'
            f'<span class="tl-dot"></span><span class="tl-name">{E(p["name_vi"])}</span></a>')
    return (f'<div class="tl" role="list" aria-label="Dòng thời gian nhóm">'
            f'<div class="tl-axis"><span>{E(C.year_label(lo))}</span>'
            f'<span>{E(C.year_label(hi))}</span></div>'
            f'<div class="tl-track">{"".join(items)}</div></div>')
```

Màu theo lĩnh vực đặt bằng class `.f-*`, dùng chính token sepia hiện có.

**(b) Giữ Mermaid nhưng sửa cho đúng nghĩa:** đổi `section` từ lĩnh vực sang **khoảng thời gian** (ví dụ mỗi 25 năm), để trục x thật sự là thời gian; lĩnh vực chuyển thành màu/tiền tố nhãn. Vẫn phải xử lý mục 2 (co chữ) và đè `themeVariables` cho khớp palette.

**(c) Giữ nguyên nhưng gắn nhãn trung thực:** đổi caption thành "Nhóm theo lĩnh vực chính (không theo tỉ lệ thời gian)" và **bỏ mũi tên trục**. Rẻ nhất, nhưng vẫn giữ lại một đồ hoạ chữ 9.4px.

### 12. Timeline hoàn toàn vô hình với screen reader
**Severity: high**

SVG do Mermaid sinh có `role="graphics-document document"`, `aria-roledescription="timeline"`, nhưng:
- `aria-label`: **null**
- `<title>`: **không có**
- `<desc>`: **không có**

Và `.mermaid-src` (bản text dự phòng) bị `display: none` (style.css:56) nên cũng bị loại khỏi cây accessibility. Kết quả: screen reader đọc ra "timeline graphic" và không gì nữa.

**Fix** — vì mọi tên trong timeline đều đã lặp lại ở các thẻ ngay bên dưới, cách đúng là đánh dấu nó là trang trí. Sửa `render.py:82–83`:

```python
def mermaid_block(code: str) -> str:
    return (f'<figure class="mermaid-wrap" role="group" aria-label="Dòng thời gian — '
            f'thông tin tương đương có trong các thẻ nhân vật bên dưới">'
            f'<div aria-hidden="true"><pre class="mermaid">{E(code)}</pre></div>'
            f'<pre class="mermaid-src">{E(code)}</pre></figure>')
```

### 13. Nhóm thuộc tính a11y còn thiếu ở `index.html`
**Severity: high** (gộp, vì cùng một chỗ sửa: `render.py:288–301`)

Đo trên DOM thật:

| phần tử | thiếu | ảnh hưởng |
|---|---|---|
| `#q` (ô tìm kiếm) | `label` **và** `aria-label` đều null | Ô input không có tên — screen reader đọc "edit, blank" |
| `#hits` | `aria-live` null, `role` null | Kết quả tìm kiếm xuất hiện im lặng; "không có kết quả" không được báo |
| `#menu-btn` | `aria-expanded`, `aria-controls` null | Không biết menu đang mở hay đóng |
| `#prev` / `#next` | `aria-label` null, nội dung là "←" / "→" | Đọc thành "leftwards arrow" |
| `<aside>` | `aria-label` null; **0 phần tử `<nav>`** trên trang | Cây chapter — điều hướng chính — không phải landmark điều hướng |
| trang | không có skip link | **70 điểm dừng tab** trước khi tới nội dung |
| `#frame` | `title="Nội dung"` cố định, không đổi khi điều hướng | Tiêu đề frame luôn là "Nội dung" dù đang xem chapter nào |

**Fix** trong `render.py:288–301`:

```python
body = f'''<a class="skip-link" href="#frame">Tới nội dung</a>
<button class="menu-btn" id="menu-btn" aria-label="Mục lục" aria-expanded="false" aria-controls="sidebar">☰</button>
<nav class="sidebar" id="sidebar" aria-label="Mục lục atlas">
  <div class="brand">…</div>
  <label class="sr-only" for="q">Tìm nhân vật theo tên, lĩnh vực hoặc vùng</label>
  <input id="q" type="search" placeholder="Tìm tên, lĩnh vực, vùng…" autocomplete="off">
  <div id="hits" role="region" aria-live="polite" aria-label="Kết quả tìm kiếm"></div>
  …
</nav>
<main class="main"><div class="framebar">
  <button id="prev" aria-label="Chapter trước" title="Chapter trước">←</button>
  <span id="crumb" aria-live="polite"></span>
  <button id="next" aria-label="Chapter sau" title="Chapter sau">→</button></div>
  <iframe id="frame" name="frame" src="overview.html" title="Nội dung atlas"></iframe></main>'''
```

(`<aside>` → `<nav>`; CSS selector `.sidebar` giữ nguyên nên không vỡ style.)

Kèm CSS:

```css
.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.skip-link { position: absolute; left: -9999px; z-index: 30; }
.skip-link:focus { left: 8px; top: 8px; background: var(--panel); color: var(--ink);
  padding: 8px 14px; border: 2px solid var(--accent); border-radius: 8px; }
```

Và trong `assets/app.js`, cập nhật `title` của iframe khi điều hướng — thêm vào cuối `setActive()` (app.js:~55, ngay sau `crumb.textContent = title`):

```js
frame.title = title;
```

### 14. Sidebar off-canvas vẫn nằm trong tab order ở mobile
**Severity: high**

Đo ở 375px, menu đóng: sidebar ở `x = -319px`, `transform: translateX(-100%)`, nhưng `visibility: visible`, **không** `inert`, **không** `aria-hidden`. Bên trong còn **67 phần tử focus được**.

Người dùng bàn phím trên mobile phải Tab qua 67 link vô hình, con trỏ focus chạy ra ngoài màn hình, trước khi tới nội dung. Người dùng screen reader thì đọc được toàn bộ một menu đang đóng.

Và khi mở: không có `aria-expanded`, không có backdrop, không bẫy focus, không đóng bằng Esc, focus không chuyển vào sidebar (`activeElement` vẫn là nút menu), iframe bên dưới **vẫn tương tác được** trong khi sidebar che 85% màn hình.

**Fix** trong `assets/app.js` — thay handler ở app.js:~95:

```js
var mb = document.getElementById("menu-btn");
var sidebar = document.getElementById("sidebar");
function setMenu(open) {
  body.classList.toggle("menu-open", open);
  mb.setAttribute("aria-expanded", open ? "true" : "false");
  // chỉ khoá khi sidebar thực sự off-canvas
  var offCanvas = matchMedia("(max-width: 1000px)").matches;
  if (offCanvas && !open) { sidebar.setAttribute("inert", ""); }
  else { sidebar.removeAttribute("inert"); }
  if (open) { var f = sidebar.querySelector("input, a"); if (f) f.focus(); }
}
if (mb) mb.addEventListener("click", function () {
  setMenu(!body.classList.contains("menu-open"));
});
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && body.classList.contains("menu-open")) { setMenu(false); mb.focus(); }
});
matchMedia("(max-width: 1000px)").addEventListener("change", function () {
  setMenu(false);
});
setMenu(false);
```

Và trong `go()` (app.js:~60) đổi `body.classList.remove("menu-open")` thành `setMenu(false)`.

### 15. Nhãn section trong thẻ nhân vật không phải heading
**Severity: medium**

Thứ tự heading hợp lệ (h1 → h2 ×5 → h3 ×33, không nhảy cấp — **không có vấn đề** ở đây). Nhưng "Tư tưởng / đóng góp chính", "Vì sao chọn", "Kế thừa từ", "Ảnh hưởng tới", "Nguồn" được phát ra là `<b>` (`render.py:222–227`) dù được style hệt heading (uppercase, letter-spacing, màu accent, `display: block`).

Hệ quả: `h4` count = **0**. Screen reader không điều hướng được *bên trong* một thẻ — mà thẻ cao tới 1578px ở mobile. Người dùng rơi vào giữa thẻ không có cách nào nhảy tới "Nguồn".

**Fix** — đổi `<b>` thành `<h4>` ở `render.py:208, 215, 222, 223, 227`, ví dụ:

```python
# render.py:222
<div class="sec"><h4>Tư tưởng / đóng góp chính</h4>{md_inline(p["ideas"])}</div>
```

CSS chỉ cần đổi selector (style.css:68), giữ nguyên hình thức:

```css
.person .sec > h4 { font-family: "Noto Sans", system-ui, sans-serif; font-size: .76rem;
  text-transform: uppercase; letter-spacing: .06em; color: var(--accent);
  display: block; margin: 0 0 .1em; font-weight: 700; }
```

### 16. Bảng credits: không `<thead>`, không `scope`, tràn khung
**Severity: medium**

`credits.html` có bảng **57 dòng** nhưng `render.py:447` phát `<tr><th>` thẳng vào `<table>` — không `<thead>`, không `scope="col"` trên một `<th>` nào (đo được: cả 6 đều null). Với bảng dữ liệu dài, screen reader không liên kết được ô với tiêu đề cột.

Bảng cũng rộng **1036px** trong khung chứa 960px (`table.tbl { width: 100% }` nhưng table-layout auto nên nội dung đẩy rộng ra). Ở 1440 không thấy vì body căn giữa còn dư chỗ, nhưng từ ~1000px trở xuống sẽ tràn ngang.

**Fix** — `render.py:447`:

```python
<div class="tbl-wrap"><table class="tbl">
<thead><tr><th scope="col"><span class="sr-only">Ảnh</span></th><th scope="col">Nhân vật</th>
<th scope="col">Tệp gốc trên Commons</th><th scope="col">Tác giả</th>
<th scope="col">Giấy phép</th><th scope="col">Chú thích</th></tr></thead>
<tbody>{"".join(rows) or '…'}</tbody></table></div>
```

```css
.tbl-wrap { overflow-x: auto; }
table.tbl td:last-child { min-width: 14em; }
```

(Áp dụng tương tự cho 2 bảng ở `render.py:412` và `render.py:424`.)

---

## Nhận xét theo từng hạng mục được hỏi

**Font stack — "Noto Serif"/"Noto Sans" không hề được tải.**
Đo bằng so sánh metric: chuỗi test render ở `"Noto Serif"` ra đúng **387.7px**, bằng y hệt `serif` generic và bằng y hệt một tên font bịa (`"ZZNotARealFont"`). Tức Noto Serif **không tồn tại** trên máy. Stack khai báo cho ra 414.9px = đúng bằng **Georgia**. Tương tự, `"Noto Sans"` = 519.8px = font bịa, còn stack thật cho 523.3px = `system-ui`.

Nên trang thực tế đang chạy **Georgia + system-ui**, không phải Noto. Không có `@font-face` nào, không có file font trong `assets/`.

Tin tốt: đã kiểm tra từng glyph tiếng Việt (ẵ ẫ ỗ ự ặ ỷ ẳ Ẵ Ỗ Ự Ặ Ỹ đ Đ ơ ư) — Georgia trên macOS phủ **toàn bộ**, không glyph nào rơi về font khác. Nên **không có hiện tượng chữ lẫn font** trên macOS/Windows.

Rủi ro thật nằm ở Linux (không có Georgia → rơi về serif generic, thường là DejaVu/Liberation — metric khác hẳn, trang sẽ trông khác đáng kể). Nếu muốn ổn định xuyên nền tảng: vendor `NotoSerif-Regular.woff2` + `NotoSans-Regular.woff2` vào `assets/` và khai `@font-face` với đường dẫn tương đối — hợp lệ với ràng buộc file:// và không-CDN (font không phải library). Nếu chấp nhận lệ thuộc font hệ thống thì nên **bỏ "Noto Serif"/"Noto Sans"** khỏi stack cho khỏi hiểu nhầm.

**Mật độ thông tin thẻ nhân vật.** Xem mục 9. Phân cấp dọc (ảnh → tên → badge → section có nhãn → link list → nguồn) **hoạt động tốt** — đọc từ trên xuống rất rõ. Chỗ hỏng là *trong* hàng badge, nơi 4 loại ngữ nghĩa khác nhau dùng chung đúng một hình thức. Thêm số liệu: thẻ cao 659–806px ở desktop, **1578px** ở mobile; ch02 dài 52.925px (62 màn hình mobile, 32 ở tablet) mà không có nav dính hay nút "lên đầu trang" — cân nhắc `position: sticky` cho `.group > h2`:

```css
.group > h2 { position: sticky; top: 0; background: var(--bg); z-index: 2; padding-top: 8px; }
```

**Sidebar & ô tìm kiếm.** Cấu trúc cây `<details>` + chỉ số đếm + nhãn khoảng năm là tốt, không cần đổi. Logic tìm kiếm **đặc biệt tốt**: `norm()` ở app.js:~100 chuẩn hoá NFD, bóc dấu thanh, và xử lý riêng `đ`/`Đ` — đúng chính xác cách người Việt gõ tìm kiếm. Giữ nguyên. Vấn đề chỉ ở lớp a11y (mục 13) và không có điều hướng bằng phím mũi tên xuống danh sách kết quả (nice-to-have — Tab vẫn đi được vì chúng là `<a>`).

**Light vs dark.** Hệ token tổ chức đúng: `:root` định nghĩa đủ, dark chỉ ghi đè. Lỗi nằm ở các màu **nằm ngoài** hệ token đó — `--rel-*`, `--ev-*`, `--conf-*` không có bản dark (mục 4), `.grid-groups .l1–.l4` hardcode (mục 5), Mermaid tự quản màu (mục 11). Quy tắc rút ra: mọi giá trị màu hardcode trong file đều là một lỗi dark-mode tiềm ẩn.

**Responsive.** Không trang nào tràn ngang ở bất kỳ breakpoint nào đã kiểm tra (375/768/810/1024/1440) — `documentElement.scrollWidth === innerWidth` ở mọi mức. Lưới `.grid-groups` 11→6 cột hoạt động đúng, 0/33 ô tràn ở cả 1440 và 810. `.person` sập về một cột ở 680px đúng ý đồ, và vì đo theo viewport của *iframe* nên nó phản ứng đúng theo khung đọc thật chứ không theo cửa sổ — đây là một quyết định hay, cố ý giữ lại. Vấn đề duy nhất là mục 8. Vùng chạm: `#menu-btn` 39×30px và `#prev`/`#next` 35×22px, đều dưới mức 44×44 khuyến nghị:

```css
.menu-btn { min-width: 44px; min-height: 44px; }
.framebar button { min-width: 44px; min-height: 36px; }
```

**Thứ tự heading.** Không có vấn đề. ch02: h1 → h2×5 → h3×33, không nhảy cấp. overview và credits: h1 → h2. Chỉ thiếu tầng h4 (mục 15).

**Alt text.** `render.py:164` dùng `alt="{name}"` cho chân dung, `alt=""` cho thumbnail trong bảng credits (đúng — tên đã có ở ô bên cạnh). Hợp lý, **không có vấn đề**. Chi tiết nhỏ: `alt="Chân dung {name}"` sẽ nói rõ hơn đây là tranh/tượng chứ không phải ảnh chụp, nhất là với nhân vật cổ đại chỉ có chân dung tưởng tượng.

---

## Thứ tự thực hiện đề xuất

**Đợt 1 — chỉ `assets/style.css`, khoảng 60 dòng, không rebuild:**
mục 1 (độ dài dòng) · 2 (mermaid co chữ) · 3 (thanh 41px) · 4 (contrast badge) · 5 (lưới độ phủ) · 6 (reduced-motion) · 7 (focus) · 8 (breakpoint sidebar) · 9 (phân cấp badge).
Đây là nơi gần như toàn bộ tác động nằm, với rủi ro gần bằng không.

**Đợt 2 — a11y, cần `render.py` + `app.js`:**
mục 13 (thuộc tính index) · 14 (inert sidebar) · 12 (mermaid aria) · 15 (h4) · 16 (bảng).

**Đợt 3 — quyết định thiết kế, cần cân nhắc:**
mục 11 (timeline nhóm-theo-lĩnh-vực vs trục thời gian thật) và việc có vendor font Noto hay bỏ nó khỏi stack.
