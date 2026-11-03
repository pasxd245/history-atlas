# Ghi chú patch nhóm CE19_20 (TK 19–20)

Kèm file `reports/patch-ch90-CE19_20.json` — 12 patch: 4 `sai`, 6 `dangngo`, 2 `trunglap` (tuỳ chọn, owner quyết riêng). Mọi `old` đã kiểm là xuất hiện đúng một lần trong `content/ch90.md`; số chữ sau khi áp toàn bộ patch (kể cả hai patch `trunglap`) đã tính bằng đúng hàm `words()` của `atlaslib/lint.py`:

| Mục | Tư tưởng | Vì sao chọn |
|---|---|---|
| Gia Long | 109 → 129 | 78 |
| Hồ Xuân Hương | 107 → 119 | 82 |
| Phan Bội Châu | 113 → 126 | 83 |
| Hồ Chí Minh | 119 → 128 | 79 → 103 (nếu nhận trunglap) |
| Võ Nguyên Giáp | 116 → 127 | 70 → 103 (nếu nhận trunglap) |
| Thích Nhất Hạnh | 103 → 111 | 79 |

## Kết quả kiểm lại 13 phát hiện của báo cáo

Tất cả 13 phát hiện đều **đứng vững** khi tra lại; không có mục nào bị bác. Nguồn đã tra: PMC8489969 (trích dẫn Lancet 1963;281:192–3); Wikipedia tiếng Việt "Phong trào Đông Du" + baotanglichsu.vn; Wikipedia EN "Gia Long", "French assistance to Nguyễn Ánh", "Treaty of Versailles (1787)"; baophapluat.vn và mocban.vn về quốc hiệu 1804; Wikipedia EN "Gia Dinh Bao" + Tuổi Trẻ; baotanglichsu.vn về địa bạ 1805/1836; thanhdiavietnamhoc.com và baodanang.vn về đường thiên lý 1809–1810; vietnamnews.vn, nhandan.vn về nghị quyết 41C/15; docsteach.org (thư gửi Lansing 18/6/1919) và Thảo luận Wikipedia tiếng Việt về bút danh chung; Wikipedia EN "Battle of Dien Bien Phu" (nguyên văn Windrow); nhandan.vn, vnexpress.net về 26/1 và 13/3/1954; langmai.org, budsas.org về năm in *Phép lạ của sự tỉnh thức*; plumvillage.org, encyclopedia.com về 39 năm lưu vong.

## Những chỗ owner cần biết trước khi áp

1. **Ba patch gộp cả đoạn.** Gia Long (phát hiện 3, 4, 6, 7), Hồ Chí Minh (9) và Võ Nguyên Giáp (10, 11) thay nguyên đoạn "Tư tưởng / đóng góp chính", vì sửa rời từng câu sẽ vượt trần 130 chữ (agent trước đã vỡ ở đúng chỗ này: 153 và 134 chữ). Hệ quả: hai phát hiện `dangngo` (6 địa bạ, 7 đường thiên lý) nằm chung patch với hai phát hiện `sai` (3, 4) của Gia Long — nếu owner không đồng ý điểm 6 hoặc 7 thì cần sửa tay trong `new`. Tương tự 11 ("hai tháng") nằm chung với 10 (Adwa). Để lấy chỗ, tôi đã lược vài chữ không mang thông tin: Gia Long mất "lưu vong và" (còn "hai mươi lăm năm giao tranh"), Giáp mất "dẫn tới chiến thắng" sau "bước ngoặt" và "Việt Nam" sau "quân đội"; Hồ Chí Minh được sắp lại theo trình tự thời gian (1919 → 1930 → 1941 → 1945) và câu về cương lĩnh giữ nguyên ý, chỉ bớt "mà", "một", "sau đó".
2. **Câu 1919 của Hồ Chí Minh** nay ghi ba điều: soạn chung với Phan Châu Trinh và Phan Văn Trường, ký tên chung Nguyễn Ái Quốc, Hội nghị Versailles không tiếp nhận nhưng qua *L'Humanité* vấn đề Việt Nam lần đầu ra dư luận quốc tế. Tôi bỏ tên Nguyễn Thế Truyền vì vai trò của ông trong tháng 6/1919 còn tranh cãi giữa các nguồn, và bỏ chi tiết "gửi bưu điện tới các phái đoàn" vì thiếu chỗ — chi tiết này nằm trong trường `why`.
3. **Câu Adwa của Võ Nguyên Giáp** theo đúng công thức Windrow; tôi bổ sung *The Last Valley* (2004) vào dòng Nguồn để người đọc tra được xuất xứ. Nếu owner không muốn thêm nguồn thì bỏ patch thứ hai của mục 08, câu văn vẫn đứng được.
4. **Bernard Fall (1966)** — không sửa. Bản quyền ghi 1966, phát hành 1/1967; cả hai đều gặp trong thư mục.
5. **Hai điểm tôi không tra được tận gốc:** trang thelancet.com chặn truy cập (HTTP 403) nên trích dẫn Lancet dựa vào cách PMC8489969 dẫn lại; câu của Windrow dựa vào bản dẫn trên Wikipedia EN chứ không phải trang sách. Con số "~14 sĩ quan, ~80 lính" của Pigneau lấy từ Wikipedia EN "French assistance to Nguyễn Ánh"; câu trong file chỉ nói "dưới trăm" nên an toàn.

## Hai patch `trunglap` — owner quyết riêng

Theo TL3 của `reports/review-ch90.md`: Hồ Chí Minh và Võ Nguyên Giáp là hai mục quyền lực duy nhất không có câu ghi mặt trái, trong khi Trần Thủ Độ, Gia Long, Triệu Đà, Hồ Quý Ly, Trương Vĩnh Ký đều có. Tôi đề xuất mỗi mục một câu, đặt ở "Vì sao chọn" (cùng vị trí với câu mẫu của Trần Thủ Độ), nêu đích danh sự việc, không bình luận:

- **Hồ Chí Minh:** cải cách ruộng đất 1953–1956 — luật do ông ký 12/1953, Hội nghị TƯ 10 (9/1956) kết luận sai lầm nghiêm trọng, Trường Chinh từ chức Tổng Bí thư, thư ông gửi đồng bào nông thôn 18/8/1956 thừa nhận sai lầm. Đây là sự việc chính sử Việt Nam tự thừa nhận, nên không có vấn đề "quan điểm".
- **Võ Nguyên Giáp:** ba đợt tấn công đồng bằng Bắc Bộ 1951 (Vĩnh Yên, Mạo Khê, sông Đáy) thất bại nặng trước de Lattre; mức thương vong ông chấp nhận là điểm Fall và Windrow đều bàn. Tôi chọn 1951 thay vì Mậu Thân 1968 vì 1968 chủ yếu là quyết định của Lê Duẩn và ông không ủng hộ.

Cả hai câu đều chỉ dùng sự kiện có niên đại và nguồn; không dùng số người chết vì các ước tính (3.000–15.000 cho cải cách ruộng đất; 6.000 ở Vĩnh Yên) chênh nhau nhiều.

## Nhận định của tôi về lựa chọn nhân vật nhóm này (owner hỏi)

**Chín trong mười mục đứng được bằng chính tiêu chí (a)–(d)**; Võ Nguyên Giáp là ca ranh giới mà ghi chú biên tập đã tự thừa nhận. Vấn đề không nằm ở ai được chọn mà ở **ai chưa từng được cân**:

1. **Khẳng định "các nhân vật chính trị và quân sự của cả hai miền đều đã được xem xét" không có bằng chứng trong file.** Danh sách 20 ứng viên bị loại nêu được Phạm Quỳnh và Nguyễn Thái Học — tức không thuần một phả hệ — nhưng không một ai thuộc nhà nước Việt Nam Cộng hoà 1955–1975. Theo chuẩn của chính file (mọi mục đều nêu đích danh ứng viên bị loại kèm lý do theo tiêu chí), việc này là chưa làm. Tôi đồng ý với TL2 của bản rà soát toàn file.
2. **Ứng viên cụ thể đáng ra phải có mặt ít nhất trong danh sách bị loại:**
   - **Ngô Đình Diệm** — (d) rất mạnh: lập nhà nước 1955, cái chết 11/1963 là bước ngoặt của cả cuộc chiến; (b) thiết chế tồn tại tới 1975, di sản còn sống trong cộng đồng hải ngoại. Có thể loại ông vì (a) phạm vi chỉ nửa nước, nhưng phải nói ra lý do đó.
   - **Trần Trọng Kim** — *Việt Nam sử lược* (1920) định hình cách nhiều thế hệ học sử Việt; (b) và (c) mạnh hơn vài mục đã được chọn; thêm vai trò Thủ tướng Đế quốc Việt Nam 1945. Ông cũng lấp lỗ hổng lĩnh vực Sử học của nhóm.
   - **Nguyễn Văn Linh hoặc Võ Văn Kiệt** — Đổi mới 1986 được chính đoạn Bối cảnh của nhóm nêu ra nhưng không có ai đại diện; đây là thay đổi nội tại lớn nhất nửa sau TK 20 theo (a), (b), (d). Theo tôi **đây mới là lỗ hổng lớn nhất**, lớn hơn cả câu hỏi hai miền, vì nó không vướng tranh cãi chính trị mà chỉ là bỏ sót.
3. **Kết luận:** lựa chọn hiện tại **phản ánh mạch lịch sử của nhà nước Việt Nam thống nhất hiện nay**, không phải kết quả của việc cân cả hai miền. Điều đó tự nó không sai — một phụ lục có quyền chọn phạm vi — nhưng ghi chú biên tập đang mô tả sai việc đã làm. Hai cách sửa, owner chọn một: (i) viết lại ghi chú thành lời nói thẳng về phạm vi và nêu tên các ứng viên trên trong danh sách bị loại kèm lý do theo tiêu chí; hoặc (ii) dùng hai chỗ trống còn lại (trần 12) cho Trần Trọng Kim và một đại diện Đổi mới — phương án này mở rộng lĩnh vực (Sử học, Kinh tế/Nhà nước) và tránh được câu hỏi "chọn ai của miền Nam" trong khi vẫn trung thực hơn hiện trạng. Tôi không thêm hay bớt người nào trong patch này theo đúng yêu cầu.
