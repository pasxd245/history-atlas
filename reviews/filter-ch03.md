# Lọc lỗi dữ kiện trong báo cáo bình duyệt cũ — Chapter 3

- **Phạm vi:** `content/ch03.md` (BCE04 → BCE01 + Ghi chú biên tập). Báo cáo đã đọc hết: `review-ch03-BCE04.md`, `review-ch03-BCE03.md`, `review-ch03-BCE02.md`, `review-ch03-BCE01.md`, và Ca 4 (11 cạnh ch03) của `tructiep-ch01-03-review.md`. Báo cáo cũ dùng nhãn **Sai / Nghi vấn / Thiếu / Trung lập / Thể thức** thay cho BẮT BUỘC/NÊN; "Sai" được coi như BẮT BUỘC (chỉ kiểm đã áp chưa), các nhãn còn lại được lọc theo nội dung.
- **Ngày:** 2026-11-04.
- **Phương pháp:** (1) lọc mọi mục có nội dung là khẳng định dữ kiện sai, câu tự mâu thuẫn với atlas (gồm quy tắc 6: nêu làm ứng viên một người có mục riêng), hoặc mức `trực tiếp` trái định nghĩa chặt của CONTRIBUTING; (2) đối chiếu `content/ch03.md` hiện tại; (3) tự kiểm phần còn sai bằng nguồn ngoài (SEP, Britannica, Livius, MacTutor, bản dịch Plutarch trên LacusCurtius, MMDC Leiden, Wikipedia làm điểm khởi đầu) hoặc bằng chính atlas (`data/persons.json`, `data/wikidata-cache.json`, ch02/ch04/ch90); (4) quyết định `sửa` / `làm mềm` / `giữ nguyên`. Có chạy thêm một phép dò quy tắc 6 bằng script (tên trong mọi trường "Vì sao chọn" của ch03 đối với `persons.json`).
- **Giới hạn:** không mở được Perseus (robots) và ctext (chặn bot); Plutarch *Antonius* 27 đọc qua LacusCurtius, Ứng đế vương xác nhận qua bài Kwek (2019) và trang tổng quan. Không mở trực tiếp Diodorus 16.91 (dựa vào Wikipedia "Philip II of Macedon"). Ngày Tư Mã Thiên chịu cung hình (99 hay 98 TCN) không phân xử được, nên giữ nguyên. Chỉ sửa `content/ch03.md`. Đã chạy cả `build.py --offline` (không chỉ `--lint-only`) một lần, nên `index.html`, `chapters/`, `data/persons.json` đã được sinh lại từ content hiện tại của mọi chapter.
- **Kết quả:** 100 ứng viên (97 từ báo cáo + 3 phát hiện thêm khi xác minh) · **54 đã sửa trước** · **25 sửa** · **11 làm mềm** · **10 giữ nguyên**. Không đụng dòng `năm:` nào nên không có ghi chú Wikidata mới.
- **Mục đã biết (đề bài giao):** cạnh `CH03-BCE04-03 → CH03-BCE03-04` hai đầu lệch mức. Ptolemaios I là somatophylax (một trong bảy cận vệ) và bạn của Alexander, còn tự viết *History of Alexander* mà Arrian dùng (Livius), đời hai người chồng lấn 356–323 TCN. Đủ cả hai điều kiện của `trực tiếp` → đầu Alexander (`Ảnh hưởng tới`) nâng `qua trường phái` → `trực tiếp`, khớp đầu Ptolemaios (`Kế thừa từ`, đã là `trực tiếp`).

## 1. Ứng viên lọc được

Trạng thái: **ĐST** = đã sửa trước (content hiện tại đã đúng) · **còn** = còn sai/còn mở, xem bảng quyết định.

| # | Báo cáo · mục gốc | ID | Trường | Trích ngắn (bản cũ) | Loại | Trạng thái |
|---|---|---|---|---|---|---|
| 1 | BCE04 · -01 Nghi vấn | CH03-BCE04-01 | Vì sao chọn | "trước tác của họ chỉ còn một phần" (Xenophon) | dữ kiện | còn → D1 |
| 2 | BCE04 · -01 Thiếu | CH03-BCE04-01 | Vì sao chọn | "suốt mười lăm thế kỷ" | dữ kiện (số không cơ sở) | còn → D2 |
| 3 | BCE04 · -02 Sai | CH03-BCE04-02 | Tư tưởng | "độc tôn cho tới khi Frege" | BẮT BUỘC | ĐST |
| 4 | BCE04 · -02 Nghi vấn | CH03-BCE04-02 | Tư tưởng | "công trình thực nghiệm" | dữ kiện | còn → D3 |
| 5 | BCE04 · -02 Thể thức | CH03-BCE04-02 | Vì sao chọn | "chính Plato" làm ứng viên | mâu thuẫn nội bộ (QT6) | ĐST |
| 6 | BCE04 · -03 Sai | CH03-BCE04-03 | Kế thừa từ | `CH02-BCE05-10 · phản bác · trực tiếp` | BẮT BUỘC | ĐST |
| 7 | BCE04 · -03 Nghi vấn + đề bài | CH03-BCE04-03 / CH03-BCE03-04 | Ảnh hưởng tới | `CH03-BCE03-04 · … · qua trường phái` vs `trực tiếp` | mâu thuẫn nội bộ (QT9) | còn → D4 |
| 8 | BCE04 · -03 Nghi vấn | CH03-BCE04-03 / -08 | Ảnh hưởng tới | `CH03-BCE04-08 · kế thừa · trực tiếp` | mức bằng chứng | còn → D5 |
| 9 | BCE04 · -03 Thiếu | CH03-BCE04-03 | Vì sao chọn | "kế hoạch của Philip, vốn chỉ nhắm Tiểu Á" | dữ kiện | còn → D6 |
| 10 | BCE04 · -04 Sai | CH03-BCE04-04 | Vì sao chọn | khoa cử "Nhật Bản" | BẮT BUỘC | ĐST |
| 11 | BCE04 · -04 Sai | CH03-BCE04-04 | Vì sao chọn | "suốt bảy thế kỷ" | BẮT BUỘC | ĐST |
| 12 | BCE04 · -04 Nghi vấn | CH03-BCE04-04 | Tư tưởng | "lập luận quy nạp" | dữ kiện | còn → D7 |
| 13 | BCE04 · -04 Nghi vấn + BCE03 · -11 Thể thức | CH03-BCE04-04 / CH03-BCE03-11 | Ảnh hưởng tới / Kế thừa từ | `phản bác · trực tiếp` (hai người không gặp nhau) | mức bằng chứng (QT9) | còn → D8 |
| 14 | BCE04 · -04 Thể thức | CH03-BCE04-04 | Vì sao chọn | Tuân Tử làm ứng viên | QT6 | ĐST (đã ghi "được chọn riêng ở nhóm sau") |
| 15 | BCE04 · -05 Sai | CH03-BCE04-05 | Vì sao chọn | "văn bản của ông còn nguyên vẹn" | BẮT BUỘC | ĐST |
| 16 | BCE04 · -05 Nghi vấn | CH03-BCE04-05 | Tư tưởng | "ông không bàn phép trị nước" | dữ kiện | còn → D9 |
| 17 | BCE04 · -06 Nghi vấn | CH03-BCE04-06 | Tư tưởng | "hai mươi bậc tước" | dữ kiện (niên đại thể chế) | còn → D10 |
| 18 | BCE04 · -06 Nghi vấn | CH03-BCE04-06 | Ảnh hưởng tới | `CH03-BCE03-02 · kế thừa · trực tiếp` | QT9 | ĐST |
| 19 | BCE04 · -07 Sai | CH03-BCE04-07 | Vì sao chọn | Trautmann + "thế kỷ 2 CN" | BẮT BUỘC | ĐST |
| 20 | BCE04 · -07 Sai (nội bộ) | Ghi chú | Điểm cần kiểm chứng | Olivelle "thế kỷ 2 CN" | BẮT BUỘC | ĐST (175–300 CN) |
| 21 | BCE04 · -07 Thể thức | CH03-BCE04-07 | Vì sao chọn | "chính Chandragupta Maurya" | QT6 | ĐST |
| 22 | BCE04 · -08 Nghi vấn | CH03-BCE04-08 | Tư tưởng | "nền cho các chỉ dụ của Ashoka" | dữ kiện | còn → D11 |
| 23 | BCE04 · -08 Thiếu | CH03-BCE04-08 | Vì sao chọn | Bindusara "mở rộng đế chế về phía nam" | dữ kiện | còn → D12 |
| 24 | BCE04 · -08 Trung lập | CH03-BCE04-08 | Vì sao chọn | "bước không có tiền lệ" | dữ kiện | còn → D13 |
| 25 | BCE04 · -09 Sai | CH03-BCE04-09 | Kế thừa từ | `tương đồng độc lập` với Plato | BẮT BUỘC | ĐST |
| 26 | BCE04 · -10 Sai | CH03-BCE04-10 | Nguồn | SEP `cynicism` 404 | BẮT BUỘC chưa áp đúng | còn → D14 (bản thay `diogenes-sinope` cũng không có bài) |
| 27 | BCE04 · -10 Thể thức | CH03-BCE04-10 | Vì sao chọn | Crates (học trò) làm ứng viên | mâu thuẫn nội bộ | ĐST |
| 28 | (phát hiện thêm, liền với #27) | CH03-BCE04-10 | Vì sao chọn | Monimus xứ Syracuse làm ứng viên | dữ kiện | còn → D15 |
| 29 | BCE04 · -11 Trung lập | CH03-BCE04-11 | Vì sao chọn | "không có tiền lệ" | dữ kiện (tuyệt đối) | còn → D16 |
| 30 | BCE04 · Đánh giá lựa chọn | Ghi chú | Ứng viên bị loại | "các nhóm tương ứng đã đủ 11–12 người" | mâu thuẫn nội bộ | ĐST (BCE04 nay 12/12, câu đã bỏ) |
| 31 | BCE03 · §1 Nghi vấn | Bối cảnh BCE03 | Bối cảnh | "đế chế quan liêu đầu tiên của Đông Á" | dữ kiện | còn → D17 |
| 32 | BCE03 · §1 Nghi vấn | Bối cảnh BCE03 | Bối cảnh | "bắt đầu kiểm soát Địa Trung Hải" | dữ kiện | còn → D18 |
| 33 | BCE03 · §2 Nghi vấn | CH03-BCE03-01 | Tư tưởng | "lần đầu một nhà nước công bố … bằng tiếng địa phương" | mâu thuẫn với CH02-BCE05-10 (Behistun) | còn → D19 |
| 34 | BCE03 · §2 Thể thức | CH03-BCE03-01 | Vì sao chọn | Chandragupta ứng viên | QT6 | ĐST |
| 35 | BCE03 · §3 Thể thức | CH03-BCE03-02 | Vì sao chọn | Lý Tư ứng viên | QT6 | ĐST |
| 36 | BCE03 · §4 Sai | CH03-BCE03-03 | Nguồn | SEP `euclid` 404 | BẮT BUỘC | ĐST |
| 37 | BCE03 · §4 Thể thức | CH03-BCE03-03 | Vì sao chọn | Eudoxus/Theaetetus ứng viên | QT5/QT6 | ĐST |
| 38 | BCE03 · §4 Nghi vấn | CH03-BCE03-03 + Ghi chú | Vì sao chọn | "chỉ dựa vào Proclus viết sau tám thế kỷ" | dữ kiện | còn → D20 |
| 39 | BCE03 · §4 Nghi vấn | CH03-BCE03-03 | Vì sao chọn | "in nhiều nhất sau Kinh Thánh" | dữ kiện | còn → D21 |
| 40 | BCE03 · §5 Sai | CH03-BCE03-04 | Tư tưởng | Mouseion "sớm nhất" (Tắc Hạ) | BẮT BUỘC | ĐST |
| 41 | BCE03 · §5 Sai | CH03-BCE03-04 | Vì sao chọn | Euclid–Eratosthenes–Herophilos "cùng làm việc" | BẮT BUỘC | ĐST |
| 42 | BCE03 · §6 Nghi vấn | CH03-BCE03-05 | Tư tưởng | "đọc được đầy đủ sau năm 1998" | dữ kiện | còn → D22 |
| 43 | BCE03 · §7 Sai | CH03-BCE03-06 | Nguồn | SEP `han-fei` 404 | BẮT BUỘC | ĐST |
| 44 | BCE03 · §7/§11 Sai | CH03-BCE03-06 / -10 | liên kết | Hàn Phi → Lý Tư `kế thừa · trực tiếp` | BẮT BUỘC | ĐST (cả hai đầu đã gỡ) |
| 45 | BCE03 · §10 Sai | CH03-BCE03-09 | Tư tưởng | 252.000 stadia gán Cleomedes | BẮT BUỘC | ĐST |
| 46 | BCE03 · §10 Sai | CH03-BCE03-09 | Tư tưởng | lưới kinh–vĩ "đầu tiên" | BẮT BUỘC | ĐST (Dicaearchus) |
| 47 | BCE03 · §10 Sai | CH03-BCE03-09 | Ảnh hưởng tới | → Hipparchus `kế thừa` | BẮT BUỘC | ĐST (`phản bác`) |
| 48 | BCE03 · §11 Thể thức | CH03-BCE03-10 | Vì sao chọn | "và chính Tần Thuỷ Hoàng" | mâu thuẫn nội bộ (QT6) | còn → D23 |
| 49 | BCE03 · §13 Nghi vấn | CH03-BCE03-12 | Ảnh hưởng tới | Scipio `trực tiếp` | mức bằng chứng | còn → D24 |
| 50 | BCE03 · §15.3 Sai | Ghi chú | Ứng viên bị loại | Aristarchus "chỉ còn qua một câu trích" | BẮT BUỘC | ĐST |
| 51 | (phát hiện thêm) | CH03-BCE03-03 / -05 | Ảnh hưởng tới / Kế thừa từ | Euclid ↔ Archimedes `kế thừa · trực tiếp` | QT9 | còn → D25 |
| 52 | BCE02 · Bối cảnh Nghi vấn | Bối cảnh BCE02 | Bối cảnh | "quyền lực duy nhất ở Địa Trung Hải" | mâu thuẫn với CH03-BCE01-09 | còn → D26 |
| 53 | BCE02 · -01 Sai | CH03-BCE02-01 | Ảnh hưởng tới | "khoa cử … thời Hán" | BẮT BUỘC | ĐST |
| 54 | BCE02 · -01 Sai | CH03-BCE02-01 | Vì sao chọn | Công Tôn Hoằng / 136 TCN | BẮT BUỘC | ĐST |
| 55 | BCE02 · -02 Nghi vấn | CH03-BCE02-02 | Ảnh hưởng tới | → Triệu Đà `phản bác · trực tiếp` | mâu thuẫn niên đại | ĐST (dòng đã gỡ) |
| 56 | (hệ quả của #55) | Ghi chú · Ứng viên Việt Nam | Ghi chú | "mục Hán Vũ Đế trỏ tới Triệu Đà" | mâu thuẫn nội bộ | còn → D27 |
| 57 | BCE02 · -03 Nghi vấn | CH03-BCE02-03 | Tư tưởng | "trục quay Trái Đất dịch chậm" | dữ kiện (gán ngược) | còn → D28 |
| 58 | BCE02 · -03 Nghi vấn | CH03-BCE02-03 | Tư tưởng | "danh mục sao có ghi độ sáng" | dữ kiện (quy thuộc) | còn → D29 |
| 59 | BCE02 · -03 Thể thức | CH03-BCE02-03 | Vì sao chọn | Apollonius ứng viên | QT6 | ĐST |
| 60 | (phát hiện thêm) | CH03-BCE02-08 / -03 | Ảnh hưởng tới / Kế thừa từ | Apollonius ↔ Hipparchus `kế thừa · trực tiếp` | QT9 | còn → D30 |
| 61 | BCE02 · -04 Thể thức | CH03-BCE02-04 | Vì sao chọn | Timaeus "cùng thời" | QT5 | ĐST ("thuộc thế hệ trước") |
| 62 | BCE02 · -04 Trung lập | CH03-BCE02-04 | Vì sao chọn | "nhiều hơn bất kỳ sử gia cổ đại nào khác" | dữ kiện (tuyệt đối) | còn → D31 |
| 63 | BCE02 · -05 Nghi vấn | CH03-BCE02-05 | `năm:` | k. 164 | dữ kiện | ĐST (`hoạt động 138–114`) |
| 64 | BCE02 · -05 Thể thức | CH03-BCE02-05 | Vì sao chọn | Ban Siêu/Cam Anh "ứng viên" | QT5 | ĐST |
| 65 | BCE02 · -05 Nghi vấn | CH03-BCE02-05 | Tư tưởng | Hansen dùng ngược | QT7 | ĐST |
| 66 | BCE02 · -06 Sai | CH03-BCE02-06 | Nguồn | Bronkhorst (1985) | BẮT BUỘC | ĐST ở dòng Nguồn |
| 67 | BCE02 · -06 Sai (phần Ghi chú) | Ghi chú · Patañjali | Điểm cần kiểm chứng | "Bronkhorst (1985) lập luận đây là những người khác nhau" | BẮT BUỘC chưa áp + mâu thuẫn với khối "đã qua bình duyệt" | còn → D32 |
| 68 | BCE02 · -07 Thể thức | CH03-BCE02-07 | Vì sao chọn | "Kanishka ở thế kỷ 2 CN" (nay có `CH04-CE02-03`) | QT6 (phát sinh theo thời gian) | còn → D33 |
| 69 | BCE02 · -08 Sai | CH03-BCE02-08 | Nguồn | Fried & Unguru "bản dịch" | BẮT BUỘC | ĐST |
| 70 | BCE02 · -10 Sai | CH03-BCE02-10 | Vì sao chọn | pithanon "lời giải đầu tiên" | BẮT BUỘC | ĐST |
| 71 | BCE02 · -10 Thể thức | CH03-BCE02-10 | Vì sao chọn | Arcesilaus/Sextus ứng viên | QT5 | ĐST |
| 72 | BCE02 · -11 Nghi vấn | CH03-BCE02-11 | Ảnh hưởng tới | → Hillel | mâu thuẫn | ĐST (cả hai đầu đã gỡ) |
| 73 | BCE02 · -11 Nghi vấn | CH03-BCE02-11 | Tư tưởng | "điều hiếm thấy trong tư liệu Cận Đông cổ" | dữ kiện (so sánh không kiểm) | còn → D34 |
| 74 | BCE02 · Đã kiểm (ghi chú về precision) | Ghi chú · Judah | Điểm cần kiểm chứng | P569 "mức chính xác thế kỷ" | dữ kiện | còn → D35 |
| 75 | BCE01 · §1 Nghi vấn | Bối cảnh BCE01 | Bối cảnh | "Vương quốc Hellenistic cuối cùng" | dữ kiện | còn → D36 |
| 76 | BCE01 · §2 Sai | CH03-BCE01-01 | Nguồn | SPQR "ch. 7–8" | BẮT BUỘC | ĐST |
| 77 | BCE01 · §2 Nghi vấn | CH03-BCE01-01 | Ảnh hưởng tới | lịch Gregory `trực tiếp` | QT9 | ĐST |
| 78 | BCE01 · §3 Nghi vấn | CH03-BCE01-02 | Vì sao chọn | "bị giết sau năm tháng" | dữ kiện | còn → D37 |
| 79 | BCE01 · §4 Sai ×2 | CH03-BCE01-03 | Kế thừa từ | Carneades, Polybius `trực tiếp` | BẮT BUỘC | ĐST |
| 80 | BCE01 · §4 Trung lập | CH03-BCE01-03 | Tư tưởng | "sách đạo đức được đọc liên tục nhất" | dữ kiện (tuyệt đối) | còn → D38 |
| 81 | BCE01 · §5 Nghi vấn | CH03-BCE01-04 | Tư tưởng | "trình bày đầy đủ duy nhất còn lại" | dữ kiện | còn → D39 |
| 82 | BCE01 · §5 Nghi vấn | CH03-BCE01-04 | Vì sao chọn | "bản sao duy nhất" Poggio 1417 | dữ kiện | còn → D40 |
| 83 | BCE01 · §6 Sai | CH03-BCE01-05 | Tư tưởng | Bucolica "dựng ra khuôn thơ điền viên" | BẮT BUỘC | ĐST (Theocritus) |
| 84 | BCE01 · §6 Trung lập | CH03-BCE01-05 | Vì sao chọn | "không tác giả Latinh nào khác có" | dữ kiện (tuyệt đối) | còn → D41 |
| 85 | BCE01 · §7 Sai | CH03-BCE01-06 | Ảnh hưởng tới | `CH90-CE10_14-02` (Đinh Bộ Lĩnh) | BẮT BUỘC | ĐST |
| 86 | BCE01 · §7 Thể thức | CH03-BCE01-06 | Vì sao chọn | Ban Cố "cùng thời" | QT5 | ĐST |
| 87 | BCE01 · §7 Nghi vấn | CH03-BCE01-06 | Tư tưởng | "chịu cung hình năm 99 TCN" | dữ kiện | còn → D42 |
| 88 | BCE01 · §7 Nghi vấn | CH03-BCE01-06 / CH03-BCE02-05 | Kế thừa từ / Ảnh hưởng tới | Trương Khiên ↔ Tư Mã Thiên `trực tiếp` | QT9 | còn → D43 |
| 89 | BCE01 · §8 Sai | CH03-BCE01-07 | Kế thừa từ | `CH03-BCE02-11` Judah Maccabee | BẮT BUỘC | ĐST |
| 90 | BCE01 · §9 Thể thức | CH03-BCE01-08 | Vì sao chọn | Hermogenes/Frontinus không báo khoảng cách | QT5 | ĐST |
| 91 | BCE01 · §9 Nghi vấn | CH03-BCE01-08 | Tư tưởng | Poggio "St Gallen … năm 1414" | dữ kiện | còn → D44 |
| 92 | BCE01 · §10 Nghi vấn | CH03-BCE01-09 | Tư tưởng | "Plutarch chép … người duy nhất trong dòng họ" | quy thuộc sai | còn → D45 |
| 93 | BCE01 · §11 Sai | CH03-BCE01-10 | Ảnh hưởng tới | `CH90-CE15_18-05` (Nguyễn Hoàng) | BẮT BUỘC | ĐST (`-08` Lê Quý Đôn) |
| 94 | BCE01 · §11 Nghi vấn | CH03-BCE01-10 | Tư tưởng | Thất lược "bảy ngành" | dữ kiện | ĐST |
| 95 | BCE01 · §12 Thể thức | CH03-BCE01-11 | Vì sao chọn | "Ptolemy ở thế kỷ 2 CN" (có `CH04-CE02-05`) | QT6 | còn → D46 |
| 96 | BCE01 · §12 Nghi vấn | CH03-BCE01-11 | `vùng:` | Strabo Trung Đông/Bắc Phi vs Hipparchus | mâu thuẫn nội bộ | ĐST (Châu Âu, có câu quy ước) |
| 97 | BCE01 · §13 Sai | CH03-BCE01-12 | Tư tưởng | thuỷ triều "sớm nhất" | BẮT BUỘC | ĐST (Seleucus) |
| 98 | BCE02 · -02 Thể thức | CH03-BCE02-02 | Vì sao chọn | Cao Tổ/Văn Đế "cùng thời" | QT5 | ĐST (đã ghi "thuộc các đời trước") |
| 99 | tructiep · 4.4 | CH03-BCE02-03 | Ảnh hưởng tới | "Ptolemy và Almagest · trực tiếp" | QT9 | ĐST |
| 100 | tructiep · 4.5 | CH03-BCE02-06 | Kế thừa từ | "Kātyāyana · trực tiếp" | QT9 | ĐST |

Tổng: 100 ứng viên · 54 ĐST · 46 còn (D1–D46). Ba mục "phát hiện thêm" (#28, #51, #60) không có trong báo cáo cũ nhưng nằm sát mục được nêu và cùng loại lỗi.

## 2. Quyết định cho mục còn sai

| # | ID | Trường | Trước | Sau | Quyết định | Bằng chứng |
|---|---|---|---|---|---|---|
| D1 | CH03-BCE04-01 | Vì sao chọn | "toàn bộ trước tác của ông còn nguyên trong khi của họ chỉ còn một phần" | "trước tác của ông còn trọn, Isocrates chỉ còn một phần, Xenophon cũng còn đủ nhưng không sinh ra truyền thống nối tiếp" | **sửa** — Britannica: "Xenophon produced a large body of work, all of which survives". | https://www.britannica.com/biography/Xenophon |
| D2 | CH03-BCE04-01 | Vì sao chọn | "… thần học Kitô giáo lẫn Hồi giáo suốt mười lăm thế kỷ" | "… nhiều thế kỷ" | **làm mềm** — con số không có mốc đo; bỏ số, không thay số mới. | (không có nguồn cho con số 15) |
| D3 | CH03-BCE04-02 | Tư tưởng | "công trình thực nghiệm quy mô lớn sớm nhất còn lại" | — | **giữ nguyên** — trong tiếng Việt "thực nghiệm" (khoa học thực nghiệm) phủ nghĩa *empirical*, không chỉ *experimental*; câu ngay trước đã nói "dựa trên quan sát trực tiếp". Reviewer đọc theo nghĩa hẹp. | không cần nguồn ngoài — điểm là nghĩa từ tiếng Việt |
| D4 | CH03-BCE04-03 | Ảnh hưởng tới | `- CH03-BCE03-04 · kế thừa · qua trường phái` | `- CH03-BCE03-04 · kế thừa · trực tiếp` | **sửa** (mục đề bài giao) — chồng đời 356–323 TCN và tiếp xúc có nguồn: Ptolemaios là somatophylax, bạn và người viết sử Alexander mà Arrian dùng. Đầu `CH03-BCE03-04 · Kế thừa từ` đã là `trực tiếp`, nay hai đầu khớp. | https://livius.org/articles/person/ptolemy-i-soter |
| D5 | CH03-BCE04-03 ↔ -08 | Ảnh hưởng tới / Kế thừa từ | `kế thừa · trực tiếp` | — | **giữ nguyên** — đời chồng lấn (340–323) và có một nguồn cổ ghi cuộc gặp (Plutarch, *Alexander* 62: "Androcottus" thời trẻ gặp Alexander). Bằng chứng mỏng nhưng không trái định nghĩa, cùng loại với các ca GIỮ dựa nguồn hậu kỳ ở `tructiep` §"Bốn ca GIỮ". Ghi vào KNOWN-ISSUES. | Plutarch, *Alexander* 62, theo review-ch03-BCE04.md §CH03-BCE04-03 (chưa tự mở văn bản) |
| D6 | CH03-BCE04-03 | Vì sao chọn | "từ kế hoạch của Philip, vốn chỉ nhắm Tiểu Á." | "từ kế hoạch của Philip, mà phần còn biết chắc chỉ là đội tiền trạm năm 336 TCN sang giải phóng các thành Hy Lạp ở Tiểu Á." | **làm mềm** — Philip là thống soái Liên minh Corinth "for a planned invasion of the Achaemenid Empire"; không nguồn nào nói ông "chỉ nhắm Tiểu Á". Lập luận (d) vẫn đứng. | https://en.wikipedia.org/wiki/Philip_II_of_Macedon (Diodorus 16.91) |
| D7 | CH03-BCE04-04 | Tư tưởng | "là lập luận quy nạp về bản tính" | "là thí nghiệm tư tưởng về bản tính" | **sửa** — SEP: "the thought experiment of the child at the well". | https://plato.stanford.edu/entries/mencius/ |
| D8 | CH03-BCE04-04 → CH03-BCE03-11 (hai đầu) | Ảnh hưởng tới / Kế thừa từ | `phản bác · trực tiếp` | `phản bác · qua trường phái` | **sửa** — đời chồng 313–289 nhưng không nguồn nào ghi hai người gặp nhau; Tuân Tử bác Mạnh Tử trong văn bản (thiên *Tính ác*, *Phi thập nhị tử*). Cả hai báo cáo BCE04 và BCE03 đều ghi "không từng gặp nhau". Thiếu vế tiếp xúc → mặc định `qua trường phái` (QT9). | https://plato.stanford.edu/entries/xunzi/ |
| D9 | CH03-BCE04-05 | Tư tưởng | "Khác Lão Tử ở chỗ ông không bàn phép trị nước, mà hướng vào …" | "Khác Lão Tử ở chỗ trọng tâm của ông không đặt vào phép trị nước, dù thiên Ứng đế vương có bàn tới, mà vào …" | **sửa** — thiên 7 của Nội thiên là *Ứng đế vương* (應帝王, "Responding to Emperors and Kings"). | https://orca.cardiff.ac.uk/115829/7/Kwek2019_Article_CritiqueOfImperialReasonLesson.pdf |
| D10 | CH03-BCE04-06 | Tư tưởng | "bằng hai mươi bậc tước ban theo quân công," | "bằng một hệ bậc tước ban theo quân công, về sau thành hai mươi bậc," | **sửa** — SEP (Pines): "The system of 20 (initially fewer) ranks of merit introduced by Shang Yang". | https://plato.stanford.edu/entries/chinese-legalism/ |
| D11 | CH03-BCE04-08 | Tư tưởng | "là nền cho các chỉ dụ của Ashoka sau đó." | "là nền hành chính mà Ashoka thừa hưởng." | **sửa** — chỉ dụ Ashoka bàn dhamma, không bàn thuế khoá hay đo đạc; chính mục `CH03-BCE03-01` mô tả nội dung chỉ dụ như vậy (mâu thuẫn nội bộ). | `content/ch03.md` CH03-BCE03-01 |
| D12 | CH03-BCE04-08 | Vì sao chọn | "Bindusara, con ông, người giữ và mở rộng đế chế về phía nam," | "Bindusara, con ông, người giữ đế chế và được truyền thống muộn gán việc mở rộng về phía nam," | **làm mềm** — nguồn duy nhất là Tāranātha (TK 16); bi ký Ashoka ở nam Ấn không nhắc; giới sử học chia rẽ. | https://en.wikipedia.org/wiki/Bindusara |
| D13 | CH03-BCE04-08 | Vì sao chọn | "hợp nhất tiểu lục địa dưới một chính quyền là bước không có tiền lệ" | — | **giữ nguyên** — Nanda lớn nhưng chỉ ở đồng bằng sông Hằng; việc đặt vùng tây bắc tới Bengal dưới một chính quyền đúng là lần đầu được ghi nhận, và văn xuôi mục đã nói phạm vi ("từ Bengal tới biên giới Afghanistan"). Reviewer phản đối cách nói, không chỉ ra phản ví dụ. | Thapar, *The Mauryas Revisited* (nguồn của mục) |
| D14 | CH03-BCE04-10 | Nguồn | SEP "Diogenes of Sinope" (`…/entries/diogenes-sinope/`) | SEP "Cosmopolitanism" (`…/entries/cosmopolitanism/`) | **sửa** — vòng trước thay `cynicism` (404) bằng `diogenes-sinope`, nhưng URL đó chỉ là trang giữ chỗ "Not Yet Available", không có bài. "Cosmopolitanism" (Kleingeld & Brown) dẫn đúng câu "I am a citizen of the world [kosmopolitês]" (DL VI 63) — chính mệnh đề trung tâm của mục. | https://plato.stanford.edu/entries/diogenes-sinope/ (placeholder) · https://plato.stanford.edu/entries/cosmopolitanism/ |
| D15 | CH03-BCE04-10 | Vì sao chọn | "Antisthenes, … và Monimus xứ Syracuse. Crates xứ Thebes không được tính là ứng viên vì chính mục này ghi ông là học trò Diogenes." | "Antisthenes, … Crates xứ Thebes và Monimus xứ Syracuse không được tính là ứng viên vì cả hai đều là học trò Diogenes." | **sửa** (phát hiện thêm) — Monimus, người vòng trước thêm vào thay Crates, cũng là học trò Diogenes (DL VI 82). Câu cũ loại Crates vì là học trò nhưng giữ Monimus cùng cảnh. | https://en.wikipedia.org/wiki/Monimus |
| D16 | CH03-BCE04-11 | Vì sao chọn | "ở tượng Cnidus không có tiền lệ và" | "ở tượng Cnidus không có tiền lệ được ghi nhận và" | **làm mềm** — khớp hedge mà chính đoạn Tư tưởng đã dùng ("đầu tiên được ghi nhận"). | `content/ch03.md` CH03-BCE04-11 |
| D17 | Bối cảnh BCE03 | Bối cảnh | "lập đế chế quan liêu đầu tiên của Đông Á" | — | **giữ nguyên** — quận huyện có trước Tần, nhưng câu nói *đế chế*, và Tần là đế chế thống nhất đầu tiên. Reviewer muốn thêm sắc thái, không chỉ ra câu sai. | Lewis (2007), nguồn của mục 02 |
| D18 | Bối cảnh BCE03 | Bối cảnh | "Rome thắng Carthage, bắt đầu kiểm soát Địa Trung Hải" | — | **giữ nguyên** — chữ "bắt đầu" đã đúng mức cho 241–201 TCN. | — |
| D19 | CH03-BCE03-01 | Tư tưởng | "là lần đầu một nhà nước công bố chính sách trực tiếp cho dân chúng bằng tiếng địa phương" | "là lần đầu một nhà nước Nam Á công bố …" | **sửa** (mâu thuẫn với atlas) — `CH02-BCE05-10` Darius I đã ghi bia Behistun ba thứ tiếng là "tuyên ngôn chính trị", sớm hơn gần ba thế kỷ. Giới hạn về Nam Á thì câu đúng và khớp vế trước ("sớm nhất của Nam Á"). | `content/ch02.md` CH02-BCE05-10 |
| D20 | CH03-BCE03-03 + Ghi chú | Vì sao chọn; Điểm cần kiểm chứng | "tiểu sử chỉ dựa vào Proclus viết sau tám thế kỷ" · "toàn bộ tiểu sử dựa vào Proclus" | "tiểu sử chủ yếu dựa vào Proclus, viết sau khoảng bảy thế kỷ rưỡi, cùng vài dòng của Pappus" · "gần như hoàn toàn dựa vào Proclus …; ngoài ông chỉ còn vài dòng của Pappus (TK 4 CN)" | **sửa** — Pappus (và Stobaeus) cũng để lại chi tiết về Euclid; ~300 TCN → ~450 CN là ~750 năm. | https://mathshistory.st-andrews.ac.uk/Biographies/Euclid/ |
| D21 | CH03-BCE03-03 | Vì sao chọn | "một trong những văn bản được in nhiều nhất sau Kinh Thánh" | — | **giữ nguyên** — đã có "một trong những"; đây là nhận định chuẩn của lịch sử toán học, không phải xếp hạng tuyệt đối. | MacTutor (như trên) |
| D22 | CH03-BCE03-05 | Tư tưởng | "tìm lại trên một palimpsest năm 1906 và đọc được đầy đủ sau năm 1998" | — | **giữ nguyên** — câu nói "đọc được *đầy đủ*", đúng: Heiberg công bố 1907 nhưng thiếu nhiều đoạn, các đoạn còn lại chỉ đọc được nhờ chụp đa phổ sau khi bản thảo đổi chủ năm 1998. | Netz & Noel (2007), nguồn của mục |
| D23 | CH03-BCE03-10 | Vì sao chọn | "Triệu Cao, …, và chính Tần Thuỷ Hoàng." | "Triệu Cao, …; Tần Thuỷ Hoàng có mục riêng ngay trong nhóm này nên không phải ứng viên bị loại." | **sửa** — QT6; Tần Thủy Hoàng là `CH03-BCE03-02`, và mục ấy đã sửa chiều ngược lại theo đúng câu này. | `data/persons.json` |
| D24 | CH03-BCE03-12 | Ảnh hưởng tới | `Scipio Africanus Lớn · kế thừa · trực tiếp` | — | **giữ nguyên** — đời chồng 235–183; Polybius XV.6–8 chép cuộc hội đàm mặt đối mặt trước Zama. `tructiep` 4.10 đã GIỮ. | tructiep-ch01-03-review.md §4.10 |
| D25 | CH03-BCE03-03 ↔ CH03-BCE03-05 (hai đầu) | Ảnh hưởng tới / Kế thừa từ | `kế thừa · trực tiếp` | `kế thừa · qua trường phái` | **sửa** (phát hiện thêm) — Euclid chỉ có khoảng hoạt động (k. 305–282 TCN), nên lint bỏ qua cặp này; Archimedes sinh k. 287 ở Syracuse. Không nguồn nào ghi hai người gặp nhau; đường truyền là văn bản (Archimedes dẫn *Cơ sở*, và MacTutor ghi ngay cả câu dẫn ấy cũng bị nghi). | https://mathshistory.st-andrews.ac.uk/Biographies/Euclid/ |
| D26 | Bối cảnh BCE02 | Bối cảnh | "trở thành quyền lực duy nhất ở Địa Trung Hải" | "thành bá quyền ở Địa Trung Hải" | **sửa** (mâu thuẫn với atlas) — Ai Cập Ptolemy độc lập tới 30 TCN (`CH03-BCE01-09`), Seleucid tới 63 TCN. Dòng nay 57 chữ (trước 60). | `content/ch03.md` CH03-BCE01-09 |
| D27 | Ghi chú · Ứng viên Việt Nam | Ghi chú | "Liên hệ giữa hai tầng được ghi bằng một liên kết chéo: mục Hán Vũ Đế (`CH03-BCE02-02`) trỏ tới Triệu Đà, vì việc nhà Hán diệt Nam Việt năm 111 TCN là sự kiện mở đầu thời Bắc thuộc." | "Chapter này hiện không có liên kết chéo nào tới hai mục ấy; việc nhà Hán diệt Nam Việt năm 111 TCN, một trong hai mốc thường dùng để tính khởi điểm Bắc thuộc, được ghi trong văn xuôi của mục Hán Vũ Đế (`CH03-BCE02-02`)." | **sửa** (mâu thuẫn nội bộ) — dòng Triệu Đà đã bị gỡ khỏi `Ảnh hưởng tới` của Hán Vũ Đế (nay là `CH04-CE05-12`), nhưng Ghi chú vẫn tả nó. "Mốc mở đầu" sửa theo `ch90.md` Bối cảnh (179 hay 111 TCN tuỳ cách tính). | `content/ch03.md` CH03-BCE02-02; `content/ch90.md` dòng 6 |
| D28 | CH03-BCE02-03 | Tư tưởng | "ông phát hiện trục quay Trái Đất dịch chậm, tức hiện tượng tiến động" | "ông phát hiện các sao dịch dần so với các điểm phân, tức hiện tượng tiến động" | **sửa** — trong khung địa tâm không có "trục quay Trái Đất"; Britannica: "certain stars near the ecliptic had moved about 2° relative to the equinoxes". | https://www.britannica.com/EBchecked/topic/266559/Hipparchus |
| D29 | CH03-BCE02-03 | Tư tưởng | "Ông lập danh mục sao có ghi độ sáng," | "Ông lập danh mục sao," | **làm mềm** — việc gán hệ cấp sao cho Hipparchus chỉ dựa vào một câu mơ hồ của Pliny; Britannica không quy cho ông. Bỏ chi tiết, không thay. | Britannica (như trên) |
| D30 | CH03-BCE02-08 ↔ CH03-BCE02-03 (hai đầu) | Ảnh hưởng tới / Kế thừa từ | `kế thừa · trực tiếp` | `kế thừa · qua trường phái` | **sửa** (phát hiện thêm) — Apollonius k. 240–190, Hipparchus k. 190–120: đời chạm nhau đúng một năm theo chính atlas, và không có tiếp xúc nào được ghi. Ghi chú "Nhân vật có thể thuộc thế kỷ khác" nói "Hipparchus dựa trực tiếp vào ông" theo nghĩa thường (dùng hình học), không phải mức bằng chứng nên để nguyên. | `content/ch03.md` trường `năm:` hai mục; QT9 |
| D31 | CH03-BCE02-04 | Vì sao chọn | "nên ông ảnh hưởng tới thiết kế hiến pháp cận đại nhiều hơn bất kỳ sử gia cổ đại nào khác." | "nên ông ảnh hưởng trực tiếp tới thiết kế hiến pháp cận đại." | **làm mềm** — so sánh tuyệt đối không quy thuộc; bỏ so sánh, giữ chuỗi Machiavelli–Montesquieu–Federalist đã nêu. | — |
| D32 | Ghi chú · Patañjali | Điểm cần kiểm chứng | "Bronkhorst (1985) lập luận đây là những người khác nhau." | (bỏ câu) | **sửa** (BẮT BUỘC chưa áp) — reviewer đã đọc toàn văn: bài bàn Yogasūtra/Yogabhāṣya, không nhắc nhà văn phạm. Dòng Nguồn của mục đã bỏ Bronkhorst, và khối "Chapter này đã qua bình duyệt" còn kể việc ấy là đã sửa, nên câu sót lại tự mâu thuẫn. | review-ch03-BCE02.md §CH03-BCE02-06 (toàn văn trên UNIL/SERVAL) |
| D33 | CH03-BCE02-07 | Vì sao chọn | "… Demetrios I, …, và Kanishka ở thế kỷ 2 CN. Menandros" | "… Demetrios I, …, còn Kanishka ở thế kỷ 2 CN có mục riêng ở Chapter 4 nên không tính là ứng viên. Menandros" | **sửa** — QT6 phát sinh theo thời gian: Kanishka nay là `CH04-CE02-03`. | `data/persons.json` |
| D34 | CH03-BCE02-11 | Tư tưởng | "là quyền giữ một tập tục tôn giáo, điều hiếm thấy trong tư liệu Cận Đông cổ." | "là quyền giữ một tập tục tôn giáo." | **làm mềm** — so sánh phạm vi rộng không kiểm được (reviewer cũng không kiểm được). | — |
| D35 | Ghi chú · Judah Maccabee | Điểm cần kiểm chứng | "Wikidata ghi năm sinh ở mức chính xác thế kỷ" | "… mức chính xác thiên niên kỷ" | **sửa** — Q111559 P569 = −500, precision 6. | `data/wikidata-cache.json` (`wd:Q111559`) |
| D36 | Bối cảnh BCE01 | Bối cảnh | "Vương quốc Hellenistic cuối cùng mất độc lập năm 30 TCN." | — | **giữ nguyên** — đây là cách định kỳ chuẩn (30 TCN kết thúc thời Hellenistic); atlas cũng tách "Vương quốc Hy Lạp–Ấn" khỏi "các vương triều Hellenistic" ở Bối cảnh BCE02, nên không tự mâu thuẫn. | `content/ch03.md` Bối cảnh BCE02 |
| D37 | CH03-BCE01-02 | Vì sao chọn | "Caesar nắm quyền tuyệt đối nhưng bị giết sau năm tháng vì …" | "… bị giết chỉ vài tuần sau khi nhận chức độc tài trọn đời, vì …" | **sửa** — *dictator perpetuo* tháng 1 hoặc 2 năm 44 TCN, bị giết 15/3/44 TCN. "Năm tháng" không khớp mốc nào câu nêu. | https://en.wikipedia.org/wiki/Dictator_perpetuo |
| D38 | CH03-BCE01-03 | Tư tưởng | "và là sách đạo đức được đọc liên tục nhất ở châu Âu" | "và là một trong những sách đạo đức được đọc liên tục nhất ở châu Âu" | **làm mềm** — xếp hạng tuyệt đối không quy thuộc. | — |
| D39 | CH03-BCE01-04 | Tư tưởng | "trình bày đầy đủ duy nhất còn lại" | "trình bày đầy đủ nhất còn lại" | **làm mềm** — thư gửi Herodotus của Epicurus (DL X, nguồn atlas dẫn ở `CH03-BCE03-08`) là bản tóm vật lý nguyên tử còn trọn; "duy nhất" đọc chặt thì sai. | `content/ch03.md` CH03-BCE03-08 |
| D40 | CH03-BCE01-04 | Vì sao chọn | "bản sao duy nhất được Poggio Bracciolini tìm thấy năm 1417" | "bản thảo Poggio Bracciolini tìm thấy năm 1417" | **sửa** — hai bản TK 9 (Oblongus, Quadratus) còn ở Leiden, độc lập với bản Poggio. | https://mmdc.nl/static/site/highlights/352/Scribe_and_corrector.html |
| D41 | CH03-BCE01-05 | Vì sao chọn | "…, điều không tác giả Latinh nào khác có." | (bỏ vế) | **làm mềm** — xếp hạng tuyệt đối; chính *Thần khúc* cho Statius đi cùng Dante qua phần cuối Luyện ngục, nên vế này đọc chặt là sai. Bỏ vế, giữ dẫn chứng Dante. | — |
| D42 | CH03-BCE01-06 | Tư tưởng | "Ông chịu cung hình năm 99 TCN vì bênh Lý Lăng" | — | **giữ nguyên** — reviewer đề nghị 98 TCN nhưng tự ghi không kiểm được; nguồn tham khảo phổ biến đặt việc này trong năm 99 TCN. Không đủ cơ sở để đổi. | https://en.wikipedia.org/wiki/99_BC |
| D43 | CH03-BCE02-05 ↔ CH03-BCE01-06 (hai đầu) | Ảnh hưởng tới / Kế thừa từ | `kế thừa · trực tiếp` | `kế thừa · qua trường phái` | **sửa** — đời chồng lấn (145–114) nhưng không nguồn nào ghi tiếp xúc; Tư Mã Thiên dùng báo cáo của Trương Khiên cho *Đại Uyển liệt truyện* (đường văn bản). Reviewer BCE01 nêu đúng điều này. | review-ch03-BCE01.md §7; QT9 |
| D44 | CH03-BCE01-08 | Tư tưởng | "cho tới khi Poggio Bracciolini làm cho bản ở tu viện St Gallen được biết tới năm 1414." | "cho tới khi giới nhân văn Ý, trong đó có Poggio Bracciolini, đưa nó trở lại lưu thông đầu thế kỷ 15." | **làm mềm** — nguồn vênh 1414/1416, chuyến St Gallen của Poggio thường đặt năm 1416; bỏ năm và nơi, không thay bằng năm khác. Mục lên 128 chữ (trần 130). | review-ch03-BCE01.md §9; https://historyofinformation.com/detail.php?entryid=2197 (Harley 2767, k. 800) |
| D45 | CH03-BCE01-09 | Tư tưởng | "Plutarch chép rằng bà là người duy nhất trong dòng họ chịu học tiếng Ai Cập," | "Plutarch chép rằng các vua Ai Cập trước bà không hề chịu học tiếng Ai Cập," | **sửa** — *Antonius* 27.4: "the kings of Egypt before her had not even made an effort to learn the native language". | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Antony*.html |
| D46 | CH03-BCE01-11 | Vì sao chọn | "… và Ptolemy ở thế kỷ 2 CN, người lập bảng toạ độ." | "… và Ptolemy ở thế kỷ 2 CN, người lập bảng toạ độ và có mục riêng ở Chapter 4; cả hai đều không phải ứng viên bị loại." | **sửa** — QT6: Claudius Ptolemy là `CH04-CE02-05`. | `data/persons.json` |

Tổng: **25 sửa · 11 làm mềm · 10 giữ nguyên.** Bản trước khi sửa: `rv/ch03.before.md`.

## 3. Cho KNOWN-ISSUES (mỏng / yếu / tranh luận còn mở, không sửa ở lượt này)

**Cần xác minh trước khi phát hành (nghi là dữ kiện, ngoài phạm vi báo cáo cũ):**
- `CH03-BCE04-12` Khuất Nguyên — "Tết Đoan Ngọ tưởng niệm ông vẫn được giữ ở cả Trung Quốc lẫn Việt Nam" (và dòng `Ảnh hưởng tới` tương ứng). Ở Việt Nam, Đoan Ngọ thường được hiểu là "Tết diệt sâu bọ", còn tích Khuất Nguyên chỉ là một lời giải thích du nhập. Mục này được thêm sau vòng bình duyệt nên chưa ai rà (Ghi chú "Nhân vật có thể thuộc thế kỷ khác"). Không có báo cáo cũ để trỏ; đề xuất do `reviews/review-ch03-BCE04.md #Đánh giá lựa chọn nhân vật` (mục 1).

**Mức bằng chứng đứng trên nguồn mỏng (GIỮ, nhưng nên biết):**
- `CH03-BCE04-03 ↔ CH03-BCE04-08` `trực tiếp` chỉ dựa vào giai thoại Plutarch *Alex.* 62 ("Androcottus"). `reviews/review-ch03-BCE04.md #CH03-BCE04-03`.
- `CH03-BCE04-07 → CH03-BCE04-08` `trực tiếp`: quan hệ thầy–vua chỉ có trong truyền thống muộn, trong khi chính mục mang nhãn [Tranh cãi lịch sử]. `reviews/review-ch03-BCE04.md #CH03-BCE04-07`.
- `CH03-BCE04-02 → CH03-BCE03-03` (Aristotle → Euclid) là luận điểm học giả, có thể là `suy đoán học giả`. `reviews/review-ch03-BCE04.md #CH03-BCE04-02`.
- `CH03-BCE03-05 → CH03-BCE02-03` (Archimedes → Hipparchus `kế thừa`) không kiểm được. `reviews/review-ch03-BCE03.md #6`.

**Mệnh đề chưa quy thuộc / tranh luận còn mở:**
- `CH03-BCE04-05`: "là thành phần Trung Hoa hoà vào Phật giáo để thành Thiền tông" viết như dữ kiện. `reviews/review-ch03-BCE04.md #CH03-BCE04-05`.
- `CH03-BCE04-06`: "cải cách của Thân Bất Hại không sống quá đời ông" là phán đoán của *Hàn Phi Tử*. `#CH03-BCE04-06`.
- `CH03-BCE04-11`: "thay cho thế đứng cân bằng của thế kỷ 5 TCN" dễ đọc thành bỏ contrapposto. `#CH03-BCE04-11`.
- `CH03-BCE03-04`: quy công lập Thư viện cho Ptolemaios I trong khi Thư viện có lẽ thành hình dưới Ptolemaios II. `reviews/review-ch03-BCE03.md #5`.
- `CH03-BCE03-10`: "tiểu triện … giữ cho văn tự Trung Hoa thống nhất" (mạch thực dụng là lệ thư). `#11`.
- `CH03-BCE03-11`: lập luận (d) dựa trên mạch "Tuân Tử sinh ra Pháp gia" mà chính nguồn SEP (Goldin) coi là cách đọc đời sau. `#12`.
- `CH03-BCE03-12`: "Scipio phần lớn là học lại" (cũng ở Ghi chú) và "vẫn nằm trong chương trình các học viện quân sự" chưa quy thuộc. `#13`.
- Bối cảnh BCE02 "đặt Nho học làm học vấn chính thức" căng với caveat Loewe ở chính Ghi chú. `reviews/review-ch03-BCE02.md #Bối cảnh`.
- `CH03-BCE02-02`: "thay vì qua dòng dõi" quá mạnh (tiến cử, nhậm tử vẫn là cửa chính). `#CH03-BCE02-02`.
- `CH03-BCE02-09`: "đúng luật về hình thức" là điểm tranh cãi; "lần đổ máu đầu tiên" là lời Plutarch; `Kế thừa từ: Không xác định` trong khi Plutarch nêu Blossius. `#CH03-BCE02-09`.
- `CH03-BCE02-11`: caveat Gruen đặt sau mệnh đề khẳng định. `#CH03-BCE02-11`.
- Bối cảnh BCE01 "Nhà Hán ở đỉnh cao" (đỉnh Tây Hán thường đặt thời Vũ Đế, ở BCE02). `reviews/review-ch03-BCE01.md #1`.
- `CH03-BCE01-09`: lập luận (a)–(d) cho Cleopatra yếu; "vương quốc giàu nhất Địa Trung Hải" chưa quy thuộc. `#10`.
- `CH03-BCE01-12`: Strabo, nguồn duy nhất của quan sát Gades, cũng chất vấn nó. `#13`.
- `CH03-BCE01-06`: ngày cung hình 99 hay 98 TCN chưa phân xử. `#7`.

**Thể thức §5 / quan hệ (lựa chọn biên tập, không phải sai):**
- Ứng viên không cùng thời hoặc là người nhà/tiền bối, đã ghi rõ khoảng cách nhưng mục vẫn không có ứng viên cùng thời hợp lệ: `CH03-BCE04-05` (Dương Chu, Liệt Tử), `CH03-BCE03-04` (Ptolemaios II là con), `CH03-BCE03-07` (Chrysippus đời sau), `CH03-BCE03-09` (Pytheas, Dicaearchus), `CH03-BCE02-06` (Kātyāyana, Bhartṛhari), `CH03-BCE02-07` (Demetrios I), `CH03-BCE01-10` (Ban Cố, nay có `CH04-CE01-11`, được nhắc như mốc chứ không gọi là bị loại).
- `Kế thừa` dùng cho quan hệ bảo trợ/liên minh: `CH03-BCE01-01 ↔ -09` (Caesar–Cleopatra), `CH03-BCE01-02 → -05/-08` (Augustus–Virgil/Vitruvius). `reviews/review-ch03-BCE01.md #2, #3, #6`.
- Cạnh còn thiếu do trần 3 dòng: Cicero không ghi Posidonius ở `Kế thừa từ`; Virgil không ghi Lucretius. `#4, #6`.
- `CH03-BCE02-04 ← CH02-BCE05-03` (Herodotus) trong khi người Polybius tự nhận nối tiếp là Thucydides. `reviews/review-ch03-BCE02.md #CH03-BCE02-04`.
- Ghi chú "Ứng viên mạnh đã bị loại": Kātyāyana được xếp chung nhóm "kế tục … người đứng ngay trước" dù ông là tiền bối của Patañjali.

## 4. Lint

`python3 build.py --offline --lint-only` (sau patch):

```
Lint: 0 lỗi · 6 cảnh báo · 284 ghi chú → reports/lint-chXX.txt (offline, không đối chiếu Wikidata)
reports/lint-ch03.txt: ERROR 0 · WARN 0 · INFO 16
```

Sáu WARN toàn atlas đều ở ch01/ch09/ch10/ch11/ch90, không có WARN nào ở ch03 trước hay sau patch. (Ở một lần chạy giữa chừng có 8 WARN, hai WARN thêm là `why` quá dài ở ch01 do agent khác đang sửa song song; lần chạy cuối quay lại 6.) Các trường đã chạm vẫn dưới trần: lớn nhất là `CH03-BCE01-08` ideas 128/130 và `CH03-BCE03-03` why 102/104.
