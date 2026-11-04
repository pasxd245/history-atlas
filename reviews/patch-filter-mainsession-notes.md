# Hậu kiểm của phiên chính — lượt lọc ch01–ch05, ch90 (2026-11-04)

## 1. Áp sửa đổi ch05 (tuần tự, từ ba báo cáo lọc chỉ-xác-minh)

Nguồn: `filter-ch05-ce06-07.md` (16 cặp), `filter-ch05-ce08-10.md` (18 cặp), `filter-crosscutting.md` (4 cặp).
Mỗi cặp được kiểm `count(old_str) == 1` ngay trước khi thay.

| Nhóm | Áp | Bỏ qua | Lý do bỏ qua |
|---|---|---|---|
| CE06–CE07 | 16/16 | 0 | — |
| CE08–CE10 | 18/18 | 0 | — |
| Xuyên chapter | 2/4 | 2 | E1 (Braulio) trùng CE06–07 E12; E2 (Madelung) trùng CE06–07 E13 — đã áp ở bước trước, chuỗi gốc không còn |

## 2. Bốn câu "bắt gặp ngoài báo cáo" mà agent lọc đưa ra nhưng chưa xác minh

Theo nguyên tắc "sai thì không": phiên chính xác minh và xử lý.

| ID | Trước | Sau | Quyết định | Căn cứ |
|---|---|---|---|---|
| CH05-CE10-05 (Khúc Thừa Dụ) | "Từ ông tới 938 là một chuỗi liên tục" | "trừ quãng Nam Hán chiếm Giao Châu năm 930–931, quyền cai trị phần lớn nằm trong tay người bản địa" | sửa | Nam Hán bắt Khúc Thừa Mỹ năm 930; Dương Đình Nghệ đuổi quân Nam Hán năm 931 (ĐVSKTT; en.wikipedia "Khúc Thừa Mỹ", "Dương Đình Nghệ") |
| CH05-CE10-08 (A Bảo Cơ) | "*Liêu sử* … sau ba trăm năm" | "(1343–1344), tức hơn bốn trăm năm sau" | sửa | *Liêu sử* soạn 1343–1344; sự kiện Thần Sách 5 = năm 920 (en.wikipedia "History of Liao") |
| CH05-CE08-12 (Yikʼin) | "Đền IV, cao 70 mét" | "cao khoảng 65–70 mét tuỳ nguồn" | làm mềm | nguồn vênh 64,6–70 m (báo cáo `filter-ch05-ce08-10.md` §3) |
| CH03-BCE04-12 (Khuất Nguyên) | "Tết Đoan Ngọ tưởng niệm ông vẫn được giữ ở cả Trung Quốc lẫn Việt Nam" + dòng Ảnh hưởng tới "…Trung Quốc và Việt Nam" | Tết Đoan Ngọ ở Trung Quốc gắn với việc tưởng niệm ông; ở Việt Nam chủ yếu là "Tết diệt sâu bọ", ít gắn với ông; dòng quan hệ chỉ còn Trung Quốc | sửa | `filter-ch03.md` §3 (mục thêm sau vòng bình duyệt, chưa ai rà) |

## 3. Hai mục agent xếp vào KNOWN-ISSUES nhưng thuộc loại "sai" → sửa ngay

| ID | Trước | Sau | Lý do |
|---|---|---|---|
| CH02-BCE05-? Pāṇini · Vì sao chọn + Ghi chú ch02 | Patañjali nêu làm ứng viên bị loại; "Patañjali chỉ chú giải" | "Patañjali … có mục riêng ở `CH03-BCE02-06` nên không phải ứng viên bị loại"; bỏ vế "chỉ chú giải" (mâu thuẫn với chính mục ch03: "Ông không chỉ chú giải mà tranh…") | Quy tắc 6 + mâu thuẫn nội bộ (`filter-ch02.md` §3) |
| ch90 · Bối cảnh CE01_09 | "Phật giáo vào Giao Châu bằng đường biển từ Ấn Độ trước khi qua Trung Hoa." (nêu như sự thật) | quy thuộc cho một dòng nghiên cứu (Lê Mạnh Thát, Nguyễn Lang) | Quan điểm còn tranh luận được viết như dữ kiện (`filter-ch90.md` §3); chính sách atlas: ghi nhận tranh luận, không phân xử |

## 4. Báo động nhầm đã gỡ

`filter-crosscutting.md` nêu `assets/` thiếu `mermaid.min.js`, `d3.min.js`, `LICENSE-*.txt` (compliance B3). Đó là giới hạn của **bản sao làm việc** (chỉ chép file nguồn cần sửa), không phải của repo: danh sách thư mục trên máy Owner có đủ `assets/mermaid.min.js`, `assets/d3.min.js`, `assets/LICENSE-mermaid.txt`, `assets/LICENSE-d3.txt`. Không đưa vào KNOWN-ISSUES.

## 5. Kiểm cuối

`python3 build.py --offline` → 0 lỗi · 6 cảnh báo (không đổi) · `pytest` 35 passed. Số dòng content thay đổi so với bản trên máy trước lượt này: ch01 35 · ch02 12 · ch03 41 · ch04 58 · ch05 37 · ch90 9.
