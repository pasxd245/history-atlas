# history-atlas — Atlas nhân vật ảnh hưởng (2000 TCN – 2026)

Website tĩnh, mở được bằng `file://`, deploy được lên GitHub Pages/Vercel. Nội dung do model viết dưới dạng Markdown theo template cố định; `build.py` lint, đối chiếu Wikidata và sinh HTML. Ảnh lấy từ Wikimedia Commons theo chính sách giấy phép cứng.

Trạng thái: **P2 xong** — Chapter 2 (Axial Age, 33 nhân vật) và Phụ lục Việt Nam (40 nhân vật). Atlas chính mới phủ 1/11 chapter · 4/33 nhóm. PLAN đã duyệt nằm trong Project "[Z] MY-PJ" (`claude/history-atlas-PLAN.md`).

## Bản chất và giới hạn của nội dung

Đây là **dự án nghiên cứu cá nhân**, không phải bách khoa thư và không phải sản phẩm thương mại.

- **Văn xuôi do mô hình AI (Claude) viết** theo prompt cố định ở `prompts/atlas-prompt.md`. Không có nhà sử học nào viết hay bình duyệt. Đây là tổng hợp do model thực hiện, không phải nghiên cứu sơ cấp.
- **Tên, niên đại, định danh** được đối chiếu tự động với Wikidata (CC0) bởi `build.py`; lệch quá ngưỡng thì lint chặn build.
- **Lựa chọn nhân vật là phán đoán biên tập** theo bốn tiêu chí (a) phạm vi, (b) độ bền, (c) tính nguyên bản, (d) counterfactual — không phải xếp hạng khách quan. Trần 10 người/nhóm buộc phải loại nhiều người xứng đáng; danh sách bị loại và lý do nằm ở `## Ghi chú biên tập` cuối mỗi chapter.
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
├── tests/                  # ch99-bad.md (23 lỗi cài sẵn) · ch98-wikidata.md (lệch niên đại)
├── build.py · fetch_images.py · requirements.txt
├── README.md · LICENSE (MIT) · CONTRIBUTING.md
```

## Yêu cầu

Python 3.11+ và gói `markdown` (`pip install -r requirements.txt`). Tuỳ chọn: `PyYAML` (đọc `images.yaml` đầy đủ hơn), `Pillow` (thu nhỏ ảnh gốc khi Commons không trả thumbnail). Không cần Node, không cần server.

## Quy trình mỗi chapter (P2/P3)

1. `python build.py --groups 2` → copy dòng `{{DANH SÁCH NHÓM}}`, thay biến trong `prompts/atlas-prompt.md`.
2. Soạn nội dung vào `content/ch02.md` (chapter lớn: `.part1.md`, `.part2.md`, mỗi phần ≤ ~30 nhân vật). **Tra Wikidata Q-ID và kiểm URL nguồn TRƯỚC khi viết** — xem `CONTRIBUTING.md`.
3. `python build.py` → lint (chặn build khi có ERROR) + đối chiếu Wikidata + sinh HTML. Xem `reports/lint-ch02.txt`, sửa content, chạy lại. `--offline` nếu không muốn gọi Wikidata.
4. `python fetch_images.py CH02` → tải ảnh theo §7; xem `reports/images-review.txt`, chỉnh `content/images.yaml` nếu cần; `python fetch_images.py --recaption` để tính lại chú thích không cần mạng.
5. `python build.py` lần nữa để nhúng ảnh. Mở `index.html`.
6. **Agent đánh giá độc lập** (bắt buộc, xem `CONTRIBUTING.md` mục *Quy trình một chapter*), sửa theo kết quả, rồi mới commit.
7. Checklist review PLAN §11. Cứ 3 chapter → ZIP checkpoint.

Lệnh khác: `--lint-only [FILE]` (chỉ lint; FILE bất kỳ → báo cáo vào `reports/tests/`), `--force` (vẫn sinh HTML dù có lỗi, chỉ để xem giao diện), `--list-ids`.

## Lint (PLAN §6.2)

**Lỗi (chặn build):** thiếu trường / metadata sai format; ID trùng hoặc sai quy ước `CHxx-GROUP-nn`; nhóm không thuộc chapter; lĩnh vực / vùng / câu hỏi lớn / loại quan hệ / mức bằng chứng / độ tin cậy ngoài từ vựng; quá 2 lĩnh vực hoặc 2 câu hỏi lớn; nhóm > 10 người; năm mất trước năm sinh; liên kết tới chính mình; thiếu `## Ghi chú biên tập`; ảnh nhúng không có giấy phép.

**Cảnh báo:** số chữ lệch > 30% (~100 / ~80 / ≤100 / ≤60); nhóm < 4 lĩnh vực hoặc < 3 vùng; liên kết tới ID chưa tồn tại; cùng tên / cùng Wikidata ở nhiều chapter; `wikidata: ?`; nhãn Wikidata không khớp tên; **niên đại lệch Wikidata** (P569/P570) quá 5 năm với độ tin cậy Cao, 25 năm với Trung bình, bỏ qua Thấp (dung sai tự nới khi Wikidata chỉ ghi thập kỷ/thế kỷ); ghi còn sống nhưng Wikidata có năm mất; đời sống không giao với nhóm; Ghi chú biên tập không nhắc ứng viên Việt Nam (D5).

**Ghi chú (INFO):** liên kết một chiều (P4 đồng bộ), người còn sống (D4), độ tin cậy Thấp bỏ qua đối chiếu.

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
- `commons.wikimedia.org/w/api.php` trả **429** từ IP cloud dùng chung → script tự chuyển sang đọc trang `File:` (machine-readable `licensetpl_*`) + Structured Data on Commons (P275/P6216) khi API không trả lời; khi đó trường `Restrictions` không kiểm tra được bằng API nên ghi `[info]` vào images-review. Chạy trên máy Owner thì API thường bình thường. Mọi request đều có User-Agent mô tả rõ, giãn cách ≥ 1–1.5 s, tôn trọng `Retry-After`, cache.

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
- **P3** Sản xuất Ch3 → Ch1 → Ch4 (2 phần) → Ch5 (2 phần) → Ch6…Ch11; ZIP mỗi 3 chapter.
  **Mỗi chapter phải qua một lượt agent đánh giá độc lập trước khi commit** — xem `CONTRIBUTING.md`, mục *Quy trình một chapter*.
- **P4** Rà soát toàn cục: trùng nhân vật, liên kết tên → ID, hai chiều, 10% nguồn, ảnh/chú thích.
- **P5** Overview: timeline toàn cục + graph dòng chảy tư tưởng bằng D3, bộ lọc, thống kê xuyên vùng, (bản đồ).
- **P6** Bàn giao: rà credits, ZIP cuối, tuỳ chọn deploy.
