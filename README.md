# history-atlas — Atlas nhân vật ảnh hưởng (2000 TCN – 2026)

Website tĩnh, mở được bằng `file://`, deploy được lên GitHub Pages/Vercel. Nội dung do model viết dưới dạng Markdown theo template cố định; `build.py` lint, đối chiếu Wikidata và sinh HTML. Ảnh lấy từ Wikimedia Commons theo chính sách giấy phép cứng.

Trạng thái: **v0.0.1-rc.1** — đủ **11/11 chapter · 33/33 nhóm · 377 nhân vật** ở atlas chính, cộng **40 nhân vật** ở phụ lục Việt Nam. Build: 0 lỗi. PLAN đã duyệt nằm trong Project "[Z] MY-PJ" (`claude/history-atlas-PLAN.md`).

> **Đây là bản ứng viên, không phải bản hoàn chỉnh.** Mọi chapter đã qua bình duyệt độc lập ít nhất một vòng (ch06–ch11 vòng 1 ngày 2026-11-04: 14 báo cáo, toàn bộ mục BẮT BUỘC đã xử lý). Còn lại là các mục NÊN / CÂN NHẮC chờ Owner quyết. Xem *Việc còn lại* ở cuối file.

## Bản chất và giới hạn của nội dung

Đây là **dự án nghiên cứu cá nhân**, không phải bách khoa thư và không phải sản phẩm thương mại.

- **Văn xuôi do mô hình AI (Claude) viết** theo prompt cố định ở `prompts/atlas-prompt.md`. Không có nhà sử học nào viết hay bình duyệt. Đây là tổng hợp do model thực hiện, không phải nghiên cứu sơ cấp.
- **Tên, niên đại, định danh** được đối chiếu tự động với Wikidata (CC0) bởi `build.py`; sai cấu trúc thì lint chặn build; tên hoặc niên đại lệch Wikidata quá ngưỡng thì lint **cảnh báo** (không chặn) — xem mục *Lint*.
- **Lựa chọn nhân vật là phán đoán biên tập** theo bốn tiêu chí (a) phạm vi, (b) độ bền, (c) tính nguyên bản, (d) counterfactual — không phải xếp hạng khách quan. Trần 12 người/nhóm buộc phải loại nhiều người xứng đáng; danh sách bị loại và lý do nằm ở `## Ghi chú biên tập` cuối mỗi chapter.
- **Mỗi mục chỉ có 1–2 nguồn**, và nội dung bên trong nguồn chưa được đối chiếu từng câu. Đủ để lần đầu mối, không đủ để trích dẫn. Hãy đi tới nguồn.
- **Phụ lục Việt Nam dùng hệ quy chiếu Việt Nam / Đông Nam Á**, không phải nhân loại, nên bị loại khỏi mọi thống kê toàn cục.
- **"Ảnh hưởng" không đồng nghĩa với "đáng ngưỡng mộ".**

Bản đầy đủ của các tuyên bố này nằm ở `overview.html` (mục *Về dự án*, *Giới hạn*, *Về những giai đoạn còn tranh luận*) và hiển thị trên chính trang web.

## Giấy phép

Mã nguồn và văn xuôi của dự án: **MIT** (xem `LICENSE`).

Ba nhóm KHÔNG thuộc MIT, giữ nguyên giấy phép riêng: **ảnh** trong `assets/img/` (Public domain / CC0 / CC BY-SA, từng ảnh liệt kê ở `credits.html`), **thư viện bên thứ ba** trong `assets/` (`LICENSE-mermaid.txt`, `LICENSE-d3.txt`), và **dữ liệu Wikidata** (CC0). Chi tiết ở phần PHẠM VI cuối `LICENSE`.

Đóng góp: xem `CONTRIBUTING.md`.

## Cây thư mục

```
history-atlas/
├── index.html              # sidebar (chapter → nhóm) + iframe; hash routing #ch02/BCE05, #ch02/CH02-BCE06-01, #overview, #credits
├── overview.html           # P5 (bản khung): độ phủ 33 nhóm + thống kê trung tính; graph D3 làm ở P5
├── credits.html            # toàn bộ ảnh: tác giả, giấy phép, link gốc, chú thích
├── chapters/chXX.html      # sinh tự động, mỗi file mở riêng được
├── content/
│   ├── chXX.md             # nguồn do model viết theo prompts/atlas-prompt.md; chapter lớn: chXX.part1.md, chXX.part2.md
│   │                       # ch02.md (Axial Age) · ch90.md (phụ lục Việt Nam — track riêng, ngoài thống kê chính)
│   └── images.yaml         # override ảnh: đổi file, viết lại chú thích, bỏ ảnh, danh sách nhạy cảm (aniconism)
├── assets/
│   ├── style.css · app.js
│   ├── mermaid.min.js (11.4.1, MIT) · d3.min.js (7.9.0, ISC) · LICENSE-*.txt   # vendored, không CDN
│   └── img/                # thumbnail đã tải về (không hotlink), tên = ID nhân vật
├── data/
│   ├── persons.json        # toàn bộ nhân vật + liên kết + ảnh (do build.py sinh)
│   ├── persons.js          # bản rút gọn cho ô tìm kiếm trong index.html (file:// không fetch được JSON)
│   ├── images.json         # metadata ảnh + giấy phép (do fetch_images.py sinh)
│   └── wikidata-cache.json # cache Wikidata (P18/P569/P570/nhãn) — chạy lại không gọi API nữa
├── reports/                # lint-chXX.txt · stats.txt · images-review.txt · tests/
├── prompts/atlas-prompt.md # prompt research v2 (PLAN §5, nguyên văn) + bảng biến theo chapter
├── atlaslib/               # common (hằng số, năm/thế kỷ, HTTP, Wikidata) · parse · lint · render
├── tests/                  # ch99-bad.md (23 lỗi cài sẵn) · ch98-wikidata.md (lệch niên đại) · test_core.py (pytest)
├── build.py · fetch_images.py · pyproject.toml · uv.lock
├── README.md · LICENSE (MIT) · CONTRIBUTING.md · KNOWN-ISSUES.md (backlog vấn đề còn mở)
```

## Yêu cầu

Python 3.11+ (dự án ghim 3.12 qua `.python-version`) và [uv](https://docs.astral.sh/uv/):

```bash
uv sync --extra images
# tuỳ chọn: export HISTORY_ATLAS_CONTACT="<URL repo công khai>"   # thêm liên hệ vào User-Agent; xem dưới
uv run python build.py
```

Gói bắt buộc là `markdown`. Extra `images` thêm `PyYAML` (đọc `images.yaml` đầy đủ hơn) và `Pillow` (thu nhỏ ảnh gốc khi Commons không trả thumbnail); thiếu hai gói này thì code vẫn chạy ở mức thấp hơn, nhưng bản dựng chuẩn với 356 ảnh nhúng thì cần. Không cần Node, không cần server.

Trang **cố ý không gọi `fetch()`**: nội dung hiển thị qua `<iframe>`, dữ liệu tìm kiếm nạp bằng thẻ `<script src="data/persons.js">` — cả hai đều chạy được dưới `file://`. (`data/persons.json` 1,2 MB là sản phẩm cho công cụ khác, trang không đụng tới.) Một điểm **suy giảm đã biết** dưới `file://`: Chrome coi mỗi file là một origin riêng nên chặn đọc `contentWindow` của iframe, khiến việc bấm link **bên trong** khung nội dung không đồng bộ hash và menu trái — `assets/app.js:77` bắt lỗi ấy rồi bỏ qua, nên không có thông báo nào. Muốn nav đầy đủ thì chạy một server tĩnh:

```bash
uv run --frozen python -m http.server 8099   # rồi mở http://localhost:8099/
```

## Quy trình mỗi chapter (P2/P3)

1. `python build.py --groups 2` → copy dòng `{{DANH SÁCH NHÓM}}`, thay biến trong `prompts/atlas-prompt.md`.
2. Soạn nội dung vào `content/ch02.md` (chapter lớn: `.part1.md`, `.part2.md`, mỗi phần ≤ ~30 nhân vật). **Tra Wikidata Q-ID và kiểm URL nguồn TRƯỚC khi viết** — xem `CONTRIBUTING.md`.
3. `python build.py` → lint (chặn build khi có ERROR) + đối chiếu Wikidata + sinh HTML. Xem `reports/lint-ch02.txt`, sửa content, chạy lại. `--offline` nếu không muốn gọi Wikidata.
4. `python fetch_images.py CH02` → tải ảnh theo §7; xem `reports/images-review.txt`, chỉnh `content/images.yaml` nếu cần; `python fetch_images.py --recaption` để tính lại chú thích không cần mạng.
5. `python build.py` lần nữa để nhúng ảnh. Mở `index.html`.
6. **Agent đánh giá độc lập** (bắt buộc, xem `CONTRIBUTING.md` mục *Quy trình một chapter*), sửa theo kết quả, rồi mới commit.
7. Checklist review PLAN §11. Cứ 3 chapter → ZIP checkpoint.

Lệnh khác: `--lint-only [FILE]` (chỉ lint; FILE bất kỳ → báo cáo vào `reports/tests/`), `--force` (vẫn sinh HTML dù có lỗi, chỉ để xem giao diện), `--list-ids`.

Kiểm thử: `uv run --group dev pytest -q` — unit test cho `parse_years`, `group_range`, `year_in_bucket`, hai cổng lint (giấy phép ảnh, `lint-atlas.txt`), số lỗi của `ch99-bad.md` khớp README, version `pyproject.toml` khớp `PROJECT["version"]`. Chạy trước mỗi commit đụng `atlaslib/`.

## Lint (PLAN §6.2)

**Lỗi (chặn build):** thiếu trường / metadata sai format; ID trùng hoặc sai quy ước `CHxx-GROUP-nn`; nhóm không thuộc chapter; lĩnh vực / vùng / câu hỏi lớn / loại quan hệ / mức bằng chứng / độ tin cậy ngoài từ vựng; quá 2 lĩnh vực hoặc 2 câu hỏi lớn; nhóm > 12 người; năm mất trước năm sinh; liên kết tới chính mình; thiếu `## Ghi chú biên tập`; ảnh nhúng không có giấy phép.

**Cảnh báo:** số chữ lệch > 30% (~100 / ~80 / ≤100 / ≤60); nhóm < 4 lĩnh vực hoặc < 3 vùng; liên kết tới ID chưa tồn tại; cùng tên / cùng Wikidata ở nhiều chapter; `wikidata: ?`; nhãn Wikidata không khớp tên; **niên đại lệch Wikidata** (P569/P570) quá 5 năm với độ tin cậy Cao, 25 năm với Trung bình, bỏ qua Thấp (dung sai tự nới khi Wikidata chỉ ghi thập kỷ/thế kỷ); ghi còn sống nhưng Wikidata có năm mất; cạnh `trực tiếp` giữa hai đời không giao nhau (quy tắc 9; bỏ qua mục ghi `trị vì`/`hoạt động`); đời sống không giao với nhóm; Ghi chú biên tập không nhắc ứng viên Việt Nam (D5).

**Ghi chú (INFO):** liên kết một chiều, người còn sống (D4), độ tin cậy Thấp bỏ qua đối chiếu.

### `Ảnh hưởng tới` là một lựa chọn top-3, không phải đồ thị ảnh hưởng đầy đủ

Mỗi mục chỉ được ghi **tối đa 3** dòng ở `Ảnh hưởng tới`, nên với những người có nhiều hậu
duệ tư tưởng, trường ấy **buộc phải cắt**. Đo ngày 2026-11-03: sau khi đã thêm mọi cạnh
ngược còn chỗ, **91 cạnh ở 40 mục** vẫn không ghi lại được — Plato và Aristotle mỗi người
thiếu 6, Augustinô 5, Euclid, Zeno xứ Citium và Đức Phật mỗi người 4.

Đây là **ràng buộc thiết kế, không phải lỗi dữ liệu**. Nới trần lên 4–6 sẽ phá một quy ước
đã áp xuyên toàn bộ atlas và vẫn không đủ cho Plato. Vì vậy: **chiều đọc đầy đủ là gom
`Kế thừa từ` của mọi mục sau**, không phải đọc `Ảnh hưởng tới` của mục trước. `Kế thừa từ`
cũng trần 3, nhưng nó nhìn ngược về quá khứ nên hiếm khi chạm trần.

Lint in INFO khi một cạnh chỉ có một chiều. Những dòng ấy là **thông tin, không phải việc
tồn đọng**: phần lớn trong số chúng không đóng được.

## Ảnh & giấy phép (PLAN §7)

`fetch_images.py`: Wikidata P18 → Commons `imageinfo/extmetadata` (LicenseShortName, LicenseUrl, Artist, AttributionRequired, Restrictions, DateTimeOriginal, ObjectName) → quyết định → tải thumbnail vào `assets/img/` → `data/images.json`, `reports/images-review.txt`.

| Commons | Xử lý |
|---|---|
| Public domain / PD-* / CC0 / PDM | nhúng, ghi nguồn kèm link |
| CC BY / CC BY-SA (mọi phiên bản) | nhúng; credit tác giả + giấy phép có link + link tệp gốc + "đã thu nhỏ" |
| có `Restrictions` (quyền nhân thân, nhãn hiệu…) | **không nhúng**, ghi `images-review.txt` → Owner quyết định qua `images.yaml` |
| NC / ND / fair use / GFDL-only / không rõ | không nhúng; thẻ nhân vật đặt link "Xem ảnh tại Wikimedia Commons" |
| không có P18 | link tới Wikipedia (vi → en) hoặc Wikidata |
| trong `sensitive:` của `images.yaml` | không dùng chân dung, chỉ link |

Chú thích tự sinh: *"Chân dung X, [tên tác phẩm], [niên đại]. Ảnh: Wikimedia Commons, <giấy phép>."* — gắn **"(tưởng tượng)"** khi niên đại tác phẩm cách thời nhân vật > 100 năm, hoặc không rõ niên đại với nhân vật trước TK 15. `DateTimeOriginal` ≥ 1826 với nhân vật tiền hiện đại được coi là ngày chụp → bỏ khỏi chú thích và ghi vào images-review để sửa tay.

Hai điểm kỹ thuật lệch nhẹ so với PLAN §7.1 (không đụng §2):
- Commons chỉ còn phục vụ thumbnail ở **cỡ cố định** (250/330/500/960/1280) → dùng **500px**, không phải 400.
- `commons.wikimedia.org/w/api.php` trả **429** từ IP cloud dùng chung → script tự chuyển sang đọc trang `File:` (machine-readable `licensetpl_*`) + Structured Data on Commons (P275/P6216) khi API không trả lời; khi đó trường `Restrictions` không kiểm tra được bằng API nên ghi `[info]` vào images-review. Chạy trên máy Owner thì API thường bình thường. Mọi request đều có User-Agent `history-atlas/<version> (personal research project)` — mặc định trung lập, không kèm liên hệ (xem `reviews/README.md`). Chính sách Wikimedia khuyến nghị kèm liên hệ; muốn thêm thì đặt biến môi trường `HISTORY_ATLAS_CONTACT` (nên là URL repo công khai, không phải email; không ghi vào repo). Giãn cách ≥ 1–1.5 s, tôn trọng `Retry-After`, cache.

## Kết quả P1 (tiêu chí §10)

| Tiêu chí | Kết quả |
|---|---|
| Build file mẫu không lỗi | `python build.py` → 0 lỗi, 9 cảnh báo (đa dạng lĩnh vực/vùng — đúng vì mẫu chỉ 5 người) |
| Lint bắt lỗi cài sẵn | `tests/ch99-bad.md` → 23 ERROR, exit 1; `tests/ch98-wikidata.md` → cảnh báo nhãn không khớp + lệch 176/158 năm |
| Fetch ảnh PD lẫn CC BY-SA | 4 ảnh Public domain (Khổng Tử, Lão Tử, Socrates, Aristotle) + 1 CC BY-SA 2.0 (Chomsky, ghi công đầy đủ) |
| `index.html` mở bằng `file://` | OK (Chromium headless): iframe, hash routing, tìm kiếm, prev/next, không lỗi console |
| Mermaid hiển thị offline | 4/4 timeline render từ `assets/mermaid.min.js`, không CDN |
| Giao diện mobile | sidebar thu thành menu ☰, thẻ nhân vật xếp dọc; light/dark theo hệ thống |

## Việc còn lại theo PLAN

- ~~**P2** Pilot Ch2 (Axial Age)~~ — xong. 33 nhân vật, lint 0 lỗi, 33/33 Q-ID khớp Wikidata.
- ~~**P3** Sản xuất Ch3 → Ch1 → Ch4 → Ch5 → Ch6…Ch11~~ — **xong ở v0.0.1-rc.1**, 11/11 chapter.
- ~~**P4** Rà soát toàn cục~~ — xong phần máy kiểm được: không trùng Q-ID, không liên kết treo, không vượt trần quan hệ, 69/69 URL trong `content/` còn sống, không có thông tin cá nhân trong repo.

### Việc còn lại, xếp theo mức quan trọng

1. **Bình duyệt ch06–ch11 vòng 1 — xong (2026-11-04).** 14 báo cáo trong `reviews/` (`review-ch06-CE11..14`, `review-ch07-CE15/16`, `review-ch08-CE17/18`, `review-ch09..11`); toàn bộ mục BẮT BUỘC đã áp, nhật ký từng sửa đổi ở `reviews/patch-ch06..11-review-notes.md`. **Còn lại:** các mục NÊN / CÂN NHẮC, gom theo chủ đề ở `KNOWN-ISSUES.md` (Owner chọn; 26 mục NÊN thực chất là lỗi dữ kiện đã được kiểm lại và sửa trước, xem `reviews/patch-release-facts-notes.md`); mục chỉ báo `[KHÔNG KIỂM ĐƯỢC]` vì Wikidata live và sách in không mở được trong phiên bình duyệt; một lượt `build.py` online để đối chiếu Wikidata sau các sửa niên đại (Mulla Sadra, Lý Thời Trân, Ockham — cố ý lệch Wikidata, đã ghi ở Ghi chú). Một cặp cạnh hai đầu lệch mức bằng chứng có từ trước, ngoài phạm vi vòng này: `CH03-BCE04-03` ↔ `CH03-BCE03-04` (`qua trường phái` / `trực tiếp`).
2. **Một mục chỉ mang được một Q-ID.** Nhóm CE21 có 4/12 mục phải loại người đồng tác giả không theo tiêu chí nào (Charpentier, Weissman, Jumper, Perlmutter/Riess) — khoa học thế kỷ 21 đóng góp theo nhóm, còn dữ liệu thì một mục một người. Sửa được nhưng đụng parser, lint và render.
3. **Phép đếm Thích Nhất Hạnh** — so độ phủ đường truyền với `CH11-CE21-12` Harari để quyết việc chuyển từ phụ lục sang mạch chính. Là một phép đếm, không phải một cuộc tranh luận.
4. **Hai ô vùng mỏng** — `Trung Á` 8/377 (vắng ở cả CE20 lẫn CE21), `Châu Đại Dương` còn 2 mục (`CH09-CE19-11`, `CH11-CE21-11`) sau khi quy tắc `vùng` chuyển Rutherford sang Châu Âu.
5. **`ch01` thiên lệch vùng 79%** (Trung Đông/Bắc Phi 30/38); nhóm `BCE20_18` chỉ 1 vùng. Có thể là khoảng trống hồ sơ thật của giai đoạn 2000–1700 TCN — nhưng ch01 hiện **chưa có dòng nào nói điều đó**.
6. **Vụn** — ~127 dòng `[KHÔNG KIỂM ĐƯỢC]` trong `reviews/` cần nguồn ngoại tuyến · `ch90/BCE03_01` chỉ 2 lĩnh vực · Mahāvīra `Q9422` P31 (giữ có chủ đích) · ch02 còn treo (Zarathustra, Tôn Tử, lỗ hổng từ vựng §5) · Tì-ni-đa-lưu-chi phụ lục → mạch chính.

- **P5** Overview: timeline toàn cục + graph dòng chảy tư tưởng bằng D3, bộ lọc, thống kê xuyên vùng, (bản đồ).
- **P6** Bàn giao: rà credits, ZIP cuối, tuỳ chọn deploy.
