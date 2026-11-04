# Lọc lỗi dữ kiện trong báo cáo bình duyệt cũ — ch90 (Phụ lục Việt Nam)

- **Phạm vi:** `content/ch90.md`. Báo cáo đã đọc hết: `review-ch90.md`, `review-ch90-v2.md`, `review-ch90-CE01_09.md`, `review-ch90-CE10_14.md`, `review-ch90-CE15_18.md`, `review-ch90-CE19_20.md`, `audit-nguon-ch90.md`, `patch-ch90-CE10_14-notes.md`, `patch-ch90-CE19_20-notes.md`. Thêm cờ `CH90-CE10_14-07` (Trần Hưng Đạo) chuyển từ bình duyệt ch06-CE13.
- **Ngày:** 2026-11-04.
- **Phương pháp:** lấy mọi mục NÊN / CÂN NHẮC / Đáng ngờ / không gắn mức, cùng các mục Sai/BẮT BUỘC, rồi đối chiếu với content hiện tại. Mục đã sửa ở vòng sau thì ghi "đã sửa trước". Mục còn lại tôi tự kiểm bằng web (Wikipedia chỉ dùng làm điểm khởi đầu, Britannica nếu mở được) hoặc kiểm trong chính atlas (`atlaslib/common.py`, các mục khác của ch90). Sau đó quyết `sửa` / `làm mềm` / `giữ nguyên`.
- **Giới hạn:** zh.wikisource (ĐVSKTT) và vi.wikipedia không mở được trong phiên này (url_not_found); trang Izumi Shikibu trên Britannica cũng lỗi. Vì vậy hai mục (Bà Triệu, Hồ Xuân Hương) xử lý theo hướng **làm mềm**: không thay bằng chi tiết mới chưa kiểm. Các tranh luận sử học Việt Nam (quốc thống nhà Triệu, mốc 713 của Mai Thúc Loan, luật Hồng Đức) chỉ ghi nhận, không phân xử.

- **Kết quả:** 71 dòng ứng viên. 61 dòng đã sửa trước; một dòng có thể gộp nhiều phát hiện của các báo cáo. 10 mục còn lại được xử lý như sau:
  - **sửa:** 4 (B, C, G, H)
  - **vừa sửa vừa làm mềm:** 1 (D)
  - **làm mềm:** 3 (A, E, F)
  - **giữ nguyên:** 2 (I, J)

## 1. Ứng viên lọc được

Các mục Sai/BẮT BUỘC của vòng 1 đều đã được áp. Tôi kiểm nhanh từng mục trên content hiện tại, kết quả ở bảng 1b.

### 1a. Còn sai hoặc cần xét (8 mục còn sai, 2 mục reviewer sai)

| # | Báo cáo · mục gốc | ID | Trường | Trích ngắn (content trước lượt này) | Loại | Trạng thái |
|---|---|---|---|---|---|---|
| A | brief (cờ từ bình duyệt ch06-CE13) | CH90-CE10_14-07 Trần Hưng Đạo | Tư tưởng | "Hịch tướng sĩ là văn bản động viên quân đội sớm nhất còn lại" | dữ kiện (so sánh tuyệt đối) | còn sai |
| B | brief (cờ từ bình duyệt ch06-CE13) | CH90-CE10_14-07 | Vì sao chọn | "đánh bại đế chế Mông Cổ ở đỉnh cao … đưa Đại Việt vào lịch sử quân sự thế giới, bên cạnh Nhật Bản và Ai Cập" | dữ kiện | còn sai |
| C | review-ch90-CE10_14 #17 (Đáng ngờ), bản vá mới sửa nửa | CH90-CE10_14-06 Trần Thủ Độ | Vì sao chọn | "các thiết chế … đều do ông thiết kế", trong khi Tư tưởng cùng mục viết "sử không chép ông là người thiết kế cả chế độ" | mâu thuẫn nội bộ | còn sai |
| D | review-ch90-CE15_18 #15; review-ch90-v2 "Không kiểm chứng được" mục 3 | CH90-CE15_18-04 Nguyễn Bỉnh Khiêm | Tư tưởng | "giai thoại chỉ chép trong Đại Nam thực lục tiền biên hai thế kỷ rưỡi sau" | dữ kiện (số năm; "chỉ" chưa kiểm) | còn sai |
| E | review-ch90 TL4; review-ch90-v2 T4 | CH90-CE19_20-03 Hồ Xuân Hương | Vì sao chọn | "giọng điệu và đề tài của bà không có tiền lệ trong văn học Đông Á" | dữ kiện (phủ định toàn xưng) | còn sai |
| F | review-ch90 D3 ↔ review-ch90-CE01_09 #17 (hai báo cáo vênh nhau) | CH90-CE01_09-02 Bà Triệu | Tư tưởng | "tên, tuổi và câu nói nổi tiếng chỉ đến từ nguồn Việt thế kỷ 17 như Thiên Nam ngữ lục" | dữ kiện (xuất xứ chưa thống nhất) | còn sai / chưa kiểm được |
| G | review-ch90 TL3 (bảng: Gia Long, Trương Vĩnh Ký chỉ "hình thức") | ch90 Ghi chú, "Chuẩn ghi mặt trái" | Ghi chú biên tập | "Gia Long, Triệu Đà, Hồ Quý Ly và Trương Vĩnh Ký đều có câu như vậy" | mâu thuẫn nội bộ | còn sai |
| H | review-ch90-v2 G3 (vá chưa trọn) | ch90 Ghi chú, dòng Lê Văn Hưu | Ghi chú biên tập | "nhóm CE10_14 đã kín … Nếu trần nhóm được nới" (nhóm có 10 mục, trần 12, và Ghi chú cùng file ghi "trần nay là 12") | mâu thuẫn nội bộ | còn sai |
| I | review-ch90 N13 (Nên sửa) | CH90-CE10_14-01 Ngô Quyền | Tư tưởng | "Sau chiến thắng ông bỏ chức tiết độ sứ" | dữ kiện (reviewer cho là ông chưa từng giữ chức) | content đứng được |
| J | review-ch90-CE10_14 #1 (Sai) | CH90-CE10_14-01 | Tư tưởng | "Lê Hoàn và Trần Hưng Đạo dùng lại ngay trên khúc sông ấy" | dữ kiện | content đứng được (patch-ch90-CE10_14-notes §A đã bác) |

### 1b. Đã sửa trước (kiểm trên content hiện tại, không động tới)

| Báo cáo · mục | ID | Trích ngắn của lỗi cũ | Content hiện tại |
|---|---|---|---|
| review-ch90 S1 · CE10_14 #5 | CE10_14-04 | Chiếu dời đô "chứ không bằng điềm triệu" | lập luận hai tầng, có mệnh trời, "rồng cuộn hổ ngồi" |
| review-ch90 S2 · CE10_14 #9 | CE10_14-07 | "hoạch định toàn cục cả ba lần" | "dự cả ba lần … hoạch định toàn cục hai lần sau" |
| review-ch90 S3 · CE10_14 #8 · audit | CE10_14-07 | Binh thư yếu lược ghi như trước tác thật, có trong dòng Nguồn | đã gỡ, có câu "không sớm hơn 1869" |
| review-ch90-v2 H7 | CE10_14-07 | nhan đề Ngô Đức Thọ thiếu "hiện có" | đã có "hiện có" |
| review-ch90 S5 · audit | CE01_09-01/-07, CE10_14-01/-06/-10 | số chương Taylor lệch +1 | chương 1/5/1/3/3–4 |
| review-ch90 S6 · CE10_14 #2 | CE10_14-01 | "Bản kỷ q.5" | "Ngoại kỷ, quyển 5" |
| review-ch90 S7 · CE10_14 #22 | CE10_14-08 | Bản kỷ q.6 | q.5–6 |
| review-ch90 S8 · v2 H1 | CE01_09-01 | 65 thành gán cho Mã Viện truyện | Nguồn trỏ Hậu Hán thư q.86 |
| review-ch90-v2 H5 | CE01_09-01/-07 | "Hậu Hán thư đương thời", "sử Đường đương thời" | "(thế kỷ 5)"; bỏ "đương thời" |
| review-ch90-v2 L1 | CE01_09-01 | Ảnh hưởng tới `-04` | `-05` |
| review-ch90 S9 · CE01_09 #5/#6/#7 · v2 H11 | CE01_09-06 | "giữ được mười năm", chiếm Tống Bình, 723, quy năm 722 cho Tân Đường thư | quy 722 cho Tư trị thông giám và Toàn thư; 713 và Tống Bình là tái dựng của Phan Huy Lê; năm k. 713–722 |
| review-ch90 S10 · CE19_20 #1 · audit | CE19_20-09 | bài Presse Médicale không có thật | The Lancet 281 (1963) |
| review-ch90 N18 · v2 H10 | CE19_20-09 | "thời gian mổ" | "thì cắt nhu mô gan" |
| review-ch90 S11 · CE15_18 #6 | CE15_18-02 | chủ biên Nguyễn Huệ Chi | Mai Quốc Liên |
| review-ch90 S12 · CE10_14 #10 | CE10_14-09 | Thất trảm sớ năm 1339 | "dưới triều Trần Dụ Tông … thường dẫn là 1358" |
| review-ch90 S13/N16 · CE10_14 #11/#12 | CE10_14-10 | Nôm vào thi cử; dịch trọn Kinh Thi, Kinh Thư | thi bằng chữ Hán; thiên Vô dật + Quốc ngữ Thi nghĩa |
| review-ch90 S14/D4 · CE15_18 #12 | CE15_18-03 | dựa vào luật Minh; quyền phụ nữ trình bày như đã ngã ngũ | Đường luật; nêu hai phía (Yu/Tạ ↔ Tran), Yao Takao |
| review-ch90 TL4 · CE15_18 #2 | CE15_18-03 | văn bản luật học so sánh được viện dẫn nhiều nhất Đông Á | "văn bản pháp luật Việt Nam tiền hiện đại được nghiên cứu nhiều nhất" |
| review-ch90 N11 · CE15_18 #14 | CE15_18-03 | "gần bốn thế kỷ" | "hơn ba thế kỷ, tới Hoàng Việt luật lệ 1812–1815" |
| CE15_18 #11/#13 | CE15_18-03 | 13 đạo (không mốc); 37 năm | "mười hai rồi mười ba (1466, 1471)"; "gần ba mươi bảy năm" |
| review-ch90 S15 · v2 H8 | CE15_18-04, CE19_20-03 | Lương Thế Vinh "cùng thế kỷ"; Đoàn Thị Điểm / Bà Huyện Thanh Quan "cùng thời" | Nguyễn Dữ, Phùng Khắc Khoan; "thế hệ trước / thế hệ sau" |
| review-ch90-v2 H6 | CE15_18-04 | Nguyễn Dữ "là học trò ông" | "mà truyền thống coi là học trò ông (quan hệ này còn tranh luận)" |
| review-ch90 N7 · CE15_18 #1 | CE15_18-04 | gộp hai tập thơ | Bạch Vân am thi tập + Bạch Vân quốc ngữ thi tập |
| CE15_18 #15 (phần chữ) / #16 | CE15_18-04 | "vạn đại"; "về quê dạy học gần bốn mươi năm" | "khả dĩ" kèm ghi chú dị bản; "vẫn được triều Mạc hỏi ý" |
| CE15_18 #3/#18/#19 | CE15_18-05 | "mở đầu Nam tiến"; Bồ Đào Nha, Khmer quy cả cho ông | "giai đoạn quyết định … đã bắt đầu từ 1069"; tách đời sau |
| CE15_18 #20/#21/#22 | CE15_18-06 | bảy lần giao tranh; cấm thi nêu như sự thật; "hai thế kỷ" | sau khi luỹ dựng xong (1631–1672); "Theo Đại Nam thực lục"; bốn thập niên |
| review-ch90 N8/N9 · CE15_18 #4/#5/#23 | CE15_18-07 | 20 năm truyền giáo; quốc ngữ là lý do biết chữ; năm sinh "Cao" | khoảng chín năm; Bình dân học vụ; ghi 1593, độ tin cậy Trung bình |
| CE15_18 #24/#25 | CE15_18-09 | 1720; chỉ chữa thế tử Cán | 1724 (có bản 1720); Trịnh Sâm và Trịnh Cán |
| CE15_18 #7/#8/#9 | CE15_18-01 | "mười năm"; rút 1427; "mười vạn" | gần mười một năm; cuối 1427 – đầu 1428; 84.640 |
| CE15_18 #10 | CE15_18-02 | "hai mươi năm" | hai mươi hai năm |
| CE15_18 #26/#27 · review-ch90 N20 | CE15_18-10 | "khoảng một tháng"; "mười tám năm ông"; nguồn Thực lục không chú | 39 ngày; "phong trào Tây Sơn"; Liệt truyện q.30 kèm chú thiên kiến |
| review-ch90-v2 L5 | CE15_18-10 | nhãn "tương đồng độc lập" với Hồ Quý Ly | "kế thừa · suy đoán học giả" |
| review-ch90 N1 · CE10_14 #4 | CE10_14-02 | niên hiệu Thái Bình năm 968 | "đến năm 970" |
| review-ch90 N3 · CE10_14 #14 | CE10_14-05 | lĩnh vực Văn học, ngầm nhận tác quyền | Quân sự, Chính trị/Nhà nước; "không thư tịch cổ nào ghi tác giả" |
| CE10_14 #15 | CE10_14-05 | Ung Châu năm 1075 | "phá Ung Châu tháng 3/1076" |
| review-ch90 N6/N14 · CE10_14 #18/#19/#20 | CE10_14-03 | "sớm nhất"; năm mất; "học trò ông nuôi từ nhỏ" | sau Quốc tộ, Vương lang quy; nêu cả 1025 và 1018; Lý Khánh Văn nuôi |
| CE10_14 #6/#16/#17 (nửa) | CE10_14-06 | "khi quân Nguyên áp sát"; điền trang; tự thiết kế chế độ Thái thượng hoàng | Mông Cổ 1258; chỉ ghi thái ấp; sớ 1226 (nửa còn lại là mục C ở trên) |
| CE10_14 #21 | CE10_14-07 | 1288 | 1287–1288 |
| CE01_09 #2/#12/#13 | CE01_09-05 | đuổi Tiêu Tư năm 544; chùa Khai Quốc; "nhà Hậu Lý" | 542/544; "chỉ có trong bia … không có trong Toàn thư"; Lý Phật Tử |
| CE01_09 #4 · v2 H9 | CE01_09-03 | Mâu Tử là tăng sĩ; Khương Tăng Hội cùng hoạt động; mức "trực tiếp" | nho sĩ; sau 247; "qua trường phái" |
| CE01_09 #8/#9 · review-ch90 D6 (nửa đầu) | CE01_09-03 | con số kinh, tháp; "Nam Giao học tổ" | "chỉ có trong Thiền uyển tập anh thế kỷ 14"; "một mỹ hiệu đặt muộn" |
| review-ch90 D5 · CE01_09 #10/#11 | CE01_09-04 | 19 đời nêu như dữ kiện; Khương Tăng Hội dịch ở Giao Châu | Cuong Tu Nguyen 1997; Trường An 582; "dịch kinh ở Kiến Nghiệp" |
| CE01_09 #14/#15 · review-ch90 TL5 | CE01_09-07 | 791 vs 802; "bố/cái" là cha mẹ | năm k. 766–791 kèm ba cách dựng; "cha mẹ" hay "vua lớn" còn tranh luận |
| CE01_09 #16 | CE01_09-01 | "sử liệu cả hai phía đều ghi" | Hậu Hán thư TK 5 sớm hơn Toàn thư một nghìn năm |
| review-ch90 N12 · v2 H2 | BCE03_01-02 | "gần một thế kỷ"; ĐVSKTT 207–136 | bảy mươi năm; năm: 207–137 theo ĐVSKTT, k. 204 theo sử học hiện đại |
| review-ch90 N4 · v2 G7 | BCE03_01-02 | không nêu ứng viên | Lữ Gia |
| review-ch90 N5 · v2 G2 | BCE03_01-02 + Ghi chú | bỏ sót Lê Văn Hưu | có Lê Văn Hưu ở thân bài và Ghi chú |
| review-ch90 TL1 | Bối cảnh BCE03_01 | mốc Bắc thuộc chỉ ghi 111 TCN | nêu cả 179 và 111 TCN |
| review-ch90-v2 H3 | BCE03_01-01 | khuôn đúc "ở Cầu Vực" | "khuôn và lò đúc ngay trong Thành Nội" |
| review-ch90 N2 · CE19_20 #3/#4/#6/#7 | CE19_20-02 | "viện trợ Pháp"; quốc hiệu năm 1802; địa bạ toàn quốc; "mở" đường thiên lý | Versailles 1787 không thi hành, dưới trăm lính tình nguyện; 1804 do nhà Thanh đảo tên; địa bạ Bắc Hà 1805; "tu bổ, nối dài" |
| review-ch90 N17 · CE19_20 #8 | CE19_20-03 | UNESCO "vinh danh" năm 2021 | nghị quyết 2021, cùng kỷ niệm 2022–2023 |
| review-ch90 N15 · v2 H4 · CE19_20 #5 · audit | CE19_20-04 | "chủ bút"; Gia Định báo 1869–1897 | chánh tổng tài, Huỳnh Tịnh Của là chủ bút; 1865–1909 |
| CE19_20 #2 | CE19_20-05 | trục xuất du học sinh năm 1909 | 1908, chính ông bị trục xuất đầu 1909 |
| review-ch90 D1 · CE19_20 #9 | CE19_20-07 | Yêu sách 1919 quy cho cá nhân; "nêu tại diễn đàn quốc tế" | soạn chung, ký tên chung; hội nghị không tiếp nhận |
| review-ch90 D2 · CE19_20 #10/#11 | CE19_20-08 | "lần đầu" không định ngữ; "hai tháng" | công thức Windrow, có ca Adwa; gần bảy tuần |
| review-ch90 N19 · v2 L2 | CE19_20-10 | MLK "tương đồng độc lập · trực tiếp" | "kế thừa · trực tiếp" |
| CE19_20 #12/#13 | CE19_20-10 | sách in 1974; "cả hai miền suốt gần bốn mươi năm" | viết 1974, in 1975; "rồi từ 1975 là nhà nước thống nhất" |
| review-ch90-v2 G1/G4/G5 | Ghi chú | "bốn chỗ"; đếm thiếu lĩnh vực Văn học; 95 trích dẫn | ba chỗ; 2 + 2 mục; ghi rõ "bản kiểm ngày 30/10/2026" |
| review-ch90 TL2 · v2 T1 | Ghi chú 1954–1975 | tuyên bố đã cân "cả hai miền" | Ghi chú tự nói thẳng là chưa cân |
| review-ch90 TL3 · v2 T2/T3 | CE19_20-07/-08 | không có câu ghi mặt trái | đã thêm (cải cách ruộng đất; 1951) |
| audit (YẾU) | CE15_18-01, CE19_20-02, CE19_20-03 | Lam Sơn thực lục, Thực lục chính biên, Lưu Hương ký không chú | đã chú tình trạng văn bản, đệ nhất kỷ, tác quyền còn khảo chứng |

## 2. Quyết định cho mục còn sai

| # | ID | Trường | Trước | Sau | Quyết định | Bằng chứng |
|---|---|---|---|---|---|---|
| A | CH90-CE10_14-07 Trần Hưng Đạo | Tư tưởng | "Hịch tướng sĩ là văn bản động viên quân đội sớm nhất còn lại;" | "Hịch tướng sĩ (1284) là lời hiệu triệu tướng sĩ trước cuộc kháng chiến thứ hai;" | **làm mềm.** Hiểu theo nghĩa rộng thì câu sai: thể 誓 trong Kinh Thư là lời vua tuyên trước trận đánh (甘誓, 牧誓, 費誓), có trước khoảng hai thiên niên kỷ. Hiểu theo nghĩa hẹp ("sớm nhất của Việt Nam") thì tôi không tìm được nguồn học thuật nào khẳng định. Vì vậy bỏ so sánh, chỉ giữ năm 1284, là năm mọi nguồn đều cho. | https://en.wikipedia.org/wiki/Book_of_Documents · https://en.wikipedia.org/wiki/H%E1%BB%8Bch_t%C6%B0%E1%BB%9Bng_s%C4%A9 |
| B | CH90-CE10_14-07 | Vì sao chọn | "…hai lần sau, và việc đánh bại đế chế Mông Cổ ở đỉnh cao là sự kiện đưa Đại Việt vào lịch sử quân sự thế giới, bên cạnh Nhật Bản và Ai Cập." | "…hai lần sau; nhờ đó Đại Việt thuộc số ít nơi các cuộc viễn chinh Mông Cổ – Nguyên thất bại, cùng Ai Cập Mamluk, Nhật Bản và Java." | **sửa.** Có ba điểm. (i) Đế chế Mông Cổ bắt đầu phân rã từ 1260, nên đối thủ năm 1285 và 1288 là nhà Nguyên, không phải "đế chế ở đỉnh cao". (ii) Danh sách "Nhật Bản và Ai Cập" thiếu: Java (1293) cũng thắng theo cùng khuôn với Đại Việt, Delhi đẩy lui quân Mông Cổ, Miến Điện thắng năm 1301. (iii) "Đưa vào lịch sử quân sự thế giới" là tu từ kiểu tự sự dân tộc. Câu mới chỉ nói "số ít nơi" và nêu ba ví dụ, không khẳng định đã kể đủ. | https://en.wikipedia.org/wiki/Mongol_invasions_and_conquests ("fragment from 1260"; Đại Việt, Java "ultimately resulted in defeat for the Mongols"; Ain Jalut) · https://www.britannica.com/place/Vietnam/The-Tran-dynasty |
| C | CH90-CE10_14-06 Trần Thủ Độ | Vì sao chọn | "các thiết chế quyết định sức bền của nhà Trần đều do ông thiết kế," | "các thiết chế quyết định sức bền của nhà Trần phần lớn hình thành dưới tay ông," | **sửa (nhất quán nội bộ).** Tư tưởng của cùng mục, sau bản vá CE10_14 #17, đã viết "dù sử không chép ông là người thiết kế cả chế độ". Chế độ điền trang có từ 1266, tức sau khi ông mất (1264). | kiểm trong atlas: `content/ch90.md` mục CH90-CE10_14-06 · review-ch90-CE10_14 #16–17 |
| D | CH90-CE15_18-04 Nguyễn Bỉnh Khiêm | Tư tưởng | "là giai thoại chỉ chép trong Đại Nam thực lục tiền biên hai thế kỷ rưỡi sau," | "là giai thoại thấy chép trong Đại Nam thực lục tiền biên, soạn hơn hai thế kỷ rưỡi sau," | **sửa + làm mềm.** Quốc sử quán lập năm 1821, bản thảo xong 1824, bản sửa xong 1835, Tiền biên in năm 1844. Tính từ 1558 là 266–286 năm, tức "hơn" chứ không đúng 250 năm. Chữ "chỉ" (không có bản chép nào sớm hơn) thì chưa ai chứng minh (review-ch90-v2 tự khai không kiểm được), nên bỏ. | https://en.wikipedia.org/wiki/%C4%90%E1%BA%A1i_Nam_th%E1%BB%B1c_l%E1%BB%A5c |
| E | CH90-CE19_20-03 Hồ Xuân Hương | Vì sao chọn | "giọng điệu và đề tài của bà không có tiền lệ trong văn học Đông Á." | "lối nói hai nghĩa trong khuôn Đường luật là dấu ấn riêng của bà." | **làm mềm.** Câu phủ định cho cả ba nền văn học thì không kiểm được, và về đề tài là sai: thơ tình đầy ham muốn của nữ sĩ đã có từ thời Heian, ví dụ Izumi Shikibu. Câu mới chỉ tả đặc điểm mà chính Tư tưởng cùng mục đã nêu, không so sánh. | https://en.wikipedia.org/wiki/Izumi_Shikibu · review-ch90.md TL4 |
| F | CH90-CE01_09-02 Bà Triệu | Tư tưởng | "chỉ đến từ nguồn Việt thế kỷ 17 như Thiên Nam ngữ lục;" | "chỉ đến từ nguồn Việt muộn, không sớm hơn thế kỷ 17;" | **làm mềm.** Hai báo cáo vênh nhau: `review-ch90-CE01_09` #17 nói các chi tiết ấy đến từ Thiên Nam ngữ lục (TK 17), còn `review-ch90` D3 nói câu nói chỉ có trong Thanh Hoá kỷ thắng của Vương Duy Trinh (TK 19). Tôi không mở được vi.wikipedia, còn en.wikipedia chỉ dẫn tới Trần Trọng Kim. Câu mới đúng với cả hai giả thuyết và không gán xuất xứ cho tác phẩm nào. | https://en.wikipedia.org/wiki/Lady_Tri%E1%BB%87u · reviews/review-ch90.md D3 ↔ reviews/review-ch90-CE01_09.md #17 |
| G | ch90 Ghi chú "Chuẩn ghi mặt trái" | Ghi chú biên tập | "Gia Long, Triệu Đà, Hồ Quý Ly và Trương Vĩnh Ký đều có câu như vậy." | "Gia Long, Triệu Đà, Hồ Quý Ly và Trương Vĩnh Ký có nhắc mặt gây tranh cãi nhưng chưa chặt bằng thể thức này — chẳng hạn mục Trương Vĩnh Ký chưa nêu đích danh việc cộng tác nào." | **sửa (nhất quán nội bộ).** Thể thức mà chính đoạn ấy đặt ra gồm: câu cuối "Vì sao chọn", nêu đích danh sự việc, quy cho chính nhân vật. Bốn mục kia không đạt. Gia Long viết "không gộp phán xét về đường lối đối ngoại"; Trương Vĩnh Ký chỉ ghi chung "phần cộng tác"; Triệu Đà chỉ ghi tranh luận quốc thống. Không thêm câu mặt trái mới cho mục nào, vì đó là quyết định biên tập. | kiểm trong atlas: các mục CE19_20-02, -04, BCE03_01-02, CE10_14-10 · review-ch90.md TL3 |
| H | ch90 Ghi chú, dòng Lê Văn Hưu | Ghi chú biên tập | "nhưng nhóm CE10_14 đã kín và ông xếp sau … ở tiêu chí (b). Nếu trần nhóm được nới hoặc một mục bị chuyển đi, ông là ứng viên đầu tiên." | "nhưng ông xếp sau … ở tiêu chí (b). Nhóm CE10_14 đang có 10 mục, dưới trần 12; nếu Owner dùng chỗ còn trống ở P4, ông là ứng viên đầu tiên." | **sửa (nhất quán nội bộ).** `atlaslib/common.py` đặt `max_per_group: 12`, nhóm CE10_14 có 10 mục, và dòng ngay trên của Ghi chú ghi "trần nay là 12". | kiểm trong atlas: `atlaslib/common.py:27`; `content/ch90.md` |
| I | CH90-CE10_14-01 Ngô Quyền | Tư tưởng | "Sau chiến thắng ông bỏ chức tiết độ sứ" | (không đổi) | **giữ nguyên.** Reviewer (N13) cho rằng ông chưa từng giữ chức. Wikipedia lại ghi ông là "Jiedushi of Tĩnh Hải quân" năm 938–939, kế Kiều Công Tiễn; Taylor viết "abandonment of T'ang-style political titles". "Bỏ" vẫn đứng được, và phần tranh chấp là cách gọi chứ không phải lỗi dữ kiện. | https://en.wikipedia.org/wiki/Ng%C3%B4_Quy%E1%BB%81n |
| J | CH90-CE10_14-01 | Tư tưởng | "Lê Hoàn và Trần Hưng Đạo dùng lại ngay trên khúc sông ấy" | (không đổi) | **giữ nguyên.** Bản vá trước đã bác reviewer: ĐVSKTT q.1 năm 981 viết 「劉澄至白藤江。帝自將禦之，使士卒植樁捍江」, tức đóng cọc ở Bạch Đằng, còn Chi Lăng là nơi quân Tống rút về. Lượt này không mở lại được zh.wikisource, nên dựa vào bản tra trực tiếp của ghi chú vá. | reviews/patch-ch90-CE10_14-notes.md §A · https://zh.wikisource.org/zh-hant/大越史記全書/本紀卷之一 |

Không mục nào chạm dòng `năm:` metadata, nên không phải thêm dòng độ vênh Wikidata vào Ghi chú.

## 3. Cho KNOWN-ISSUES (mỏng / yếu / chưa kiểm, không sửa)

- **Mệnh đề tối cao chưa kiểm, còn sót** (`reviews/review-ch90.md` #TL4, `reviews/review-ch90-v2.md` #T4):
  - Lý Thái Tổ: "quyết định quy hoạch có hệ quả dài nhất trong lịch sử Việt Nam".
  - Lý Thường Kiệt: "hiếm gặp ở Đông Á đương thời".
  - Trần Nhân Tông: "trường hợp hiếm trong lịch sử thế giới".
  - Nguyễn Du: "văn bản duy nhất gần như ai cũng trích được".
  - Hồ Quý Ly: "gói cải cách triệt để nhất".
  - Lê Quý Đôn: "trước tác đồ sộ nhất"; Phủ biên tạp lục là nguồn "chi tiết nhất".
  - Nguyễn Bỉnh Khiêm: "nhân vật duy nhất được cả ba thế lực hỏi ý".
  - Phan Bội Châu: "văn bản tuyên truyền chính trị hiện đại sớm nhất".
  - Mai Hắc Đế: "cuộc nổi dậy duy nhất thời Bắc thuộc có bằng chứng liên minh".
  - Hồ Xuân Hương (Tư tưởng): "chưa từng có".
  - Triệu Đà: "một trong những tranh luận kéo dài nhất".

  Lượt này chỉ làm mềm những câu mà tôi tìm được phản chứng hoặc mà brief nêu đích danh.
- **Sĩ Nhiếp:** câu "phần lớn công lao thực chất thuộc về lớp di dân" là một diễn giải mà Taylor không đỡ (`reviews/review-ch90.md` #D6). Đây là tranh luận, cần thêm góc nhìn.
- **Chuẩn ghi mặt trái chưa đều** (`reviews/review-ch90.md` #TL3):
  - Gia Long: chưa nêu cách đối xử với nhà Tây Sơn sau 1802.
  - Trương Vĩnh Ký: chưa nêu việc cụ thể (thông ngôn 1860, giúp Paul Bert 1886).
  - de Rhodes: chưa nhắc nội dung Phép giảng tám ngày.

  Ghi chú biên tập nay đã thừa nhận khoảng trống này (mục G).
- **Thể thức "Vì sao chọn":** bốn mục Hồ Quý Ly, de Rhodes, Lê Thánh Tông, Phùng Hưng đã được Ghi chú ghi nhận (`reviews/review-ch90-v2.md` #G7, #H8).
- **Giai đoạn 1954–1975, Đổi mới 1986:** chưa có nhân vật Việt Nam Cộng hoà, chưa có người đại diện cho Đổi mới. Ghi chú đã nói thẳng; để P4 (`reviews/review-ch90.md` #TL2).
- **Nguồn chưa kiểm trên bản in** (`reviews/audit-nguon-ch90.md` "KHÔNG KIỂM ĐƯỢC"):
  - Trần Văn Giáp cho mục Chu Văn An.
  - Bản kỷ tục biên năm 1585 cho mục Nguyễn Bỉnh Khiêm.
  - Li Tana cho mục Đào Duy Từ.
  - Vị trí khuôn đúc Cổ Loa trong Kim/Lai/Trịnh 2010 (`reviews/review-ch90-v2.md` #H3).
  - Khoảng 22 công trình hiện đại chưa đối chiếu thư mục (`reviews/review-ch90.md` "Không kiểm chứng được" #13).
- **Bà Triệu:** cần chốt xuất xứ câu nói, Thiên Nam ngữ lục (TK 17) hay Thanh Hoá kỷ thắng (TK 19), rồi mới ghi lại tên tác phẩm (mục F).
- **Quang Trung:** việc dùng chữ Nôm trong khoa cử có tư liệu mỏng, chủ yếu dựa Hoàng Xuân Hãn (`reviews/review-ch90.md` "Không kiểm chứng được" #9). Bốn mục CE15_18-05/-06/-08/-09 chưa được tra độc lập đủ (`reviews/review-ch90-v2.md` "Không kiểm chứng được" #5).
- **Bối cảnh CE01_09:** câu "Phật giáo vào Giao Châu bằng đường biển từ Ấn Độ trước khi qua Trung Hoa" là luận điểm của một dòng nghiên cứu (Lê Mạnh Thát, Nguyễn Lang), nên ghi là quan điểm. Mục này không có trong báo cáo nào; tôi bắt gặp khi đọc.

## 4. Kiểm tra sau sửa

- `python3 build.py --offline --lint-only` → `Lint: 0 lỗi · 6 cảnh báo · 284 ghi chú` (toàn atlas, đúng 6 WARN như trước). `reports/lint-ch90.txt`: `ERROR 0 · WARN 1 · INFO 0`. WARN duy nhất là `ch90/BCE03_01: chỉ 2 lĩnh vực`, đã có từ trước và đã được Ghi chú giải thích.
- Số chữ các trường đã sửa (hàm `words()` của lint):
  - Trần Hưng Đạo: Tư tưởng 129, Vì sao chọn 88.
  - Trần Thủ Độ: Vì sao chọn 97.
  - Nguyễn Bỉnh Khiêm: Tư tưởng 129.
  - Hồ Xuân Hương: Vì sao chọn 88.

  Tất cả trong ngưỡng ±30%.
- `python3 -m pytest -q tests` → `35 passed`.
