# Patch ch11 — áp các mục BẮT BUỘC của review độc lập

- File sửa: `content/ch11.md` (duy nhất). Bản trước khi sửa: `rv/ch11.before.md`.
- Nguồn review: `rv/review-ch11.md`. Chỉ áp 9 mục **BẮT BUỘC**; NÊN / CÂN NHẮC / [KHÔNG KIỂM ĐƯỢC] để owner quyết.
- Kiểm thêm trong vòng này (WebFetch/WebSearch, 2026-11-04): ynharari.com/about ("His books have sold 55 million copies in 65 languages"); Wikipedia "High-Z Supernova Search Team" (lập 1994, Schmidt khi ấy postdoc ở Harvard; 1995 nhóm bầu Schmidt ở Mount Stromlo/ANU điều phối); bài Rappler 148007 ("26 fake accounts… influences at least 3 million other accounts"); chú thích Wikipedia bài Harari: Hallpike, C. R. (December 2017), "A Response to Yuval Harari's 'Sapiens: A Brief History of Humankind'", *New English Review*.

## Bảng áp dụng

| # | Review | Mục | Trường | Trước (rút gọn) | Sau (rút gọn) | Kết quả |
|---|---|---|---|---|---|---|
| 1 | #12 | CH11-CE21-04 | Tư tưởng | "năm 2005 … thay uridine bằng pseudouridine thì ARN không còn kích hoạt…, lại được dịch mã mạnh hơn hẳn" | "năm 2005 …: ARN mang nucleoside biến đổi — trong đó có pseudouridine thay cho uridine — gần như không còn kích hoạt phản ứng ấy; các bài 2008 và 2010 cho thấy nó còn được dịch mã mạnh hơn hẳn" | Áp dụng (nguyên văn đề xuất). Ghi chú: câu cuối "đứng trên bài báo ấy" (NÊN #13) không sửa — owner quyết. |
| 2 | #19 | CH11-CE21-06 | Tiêu đề (name_orig) | "(Demis Hassabis Kyriacou)" | "(Sir Demis Hassabis)" | Áp dụng. Dạng "Sir Demis Hassabis" là alias có trong Wikidata (theo review); giữ ngoặc để không sinh WARN "thiếu tên gốc" mới. |
| 3 | #34 | CH11-CE21-10 | Tư tưởng | "vài trăm tài khoản giả … tới hàng triệu người" | "một mạng lưới hai mươi sáu tài khoản Facebook giả … tới ít nhất ba triệu tài khoản khác" | Điều chỉnh nhẹ: số viết bằng chữ theo văn phong chapter; con số đã tự đối chiếu với bài Rappler. |
| 4 | #45 | CH11-CE21-12 | Tư tưởng | "Sách bán khoảng bốn mươi lăm triệu bản ở sáu mươi lăm ngôn ngữ." | "Tính chung các sách của ông, không riêng *Sapiens*, trang của tác giả ghi năm mươi lăm triệu bản ở sáu mươi lăm ngôn ngữ." | Điều chỉnh: dùng đúng số đã tự kiểm trên ynharari.com/about và nêu rõ nguồn số; bỏ vế "Sapiens dịch ~45 thứ tiếng (số của tác giả và nhà xuất bản)" vì con số 45 lấy từ Wikipedia, không phải tác giả/NXB — gán nguồn sai; và để giữ trần ~100 chữ. |
| 5 | #46 | CH11-CE21-12 | Nguồn | "Christopher Robert Hallpike, "A Response to Yuval Harari's *Sapiens*", *Cliodynamics* 8 (2017)" | "C. R. Hallpike, "A Response to Yuval Harari's *Sapiens: A Brief History of Humankind*", *New English Review* (2017)" | Điều chỉnh: xoá tạp chí + số tập bịa; venue *New English Review* và năm 2017 đã tự xác nhận qua chú thích Wikipedia (12/2017). Không ghi tháng (chưa mở trang NER — K4 vẫn mở). Tên rút về "C. R." theo dạng của chính chú thích; tên đầy đủ chưa kiểm. |
| 6 | #47 | CH11-CE21-12 | Vì sao chọn | "Diamond bị loại theo nhóm thời gian: sách chính của ông ra năm 1997." | "Diamond (*Guns, Germs, and Steel*, 1997) không được xét vì ảnh hưởng chính của ông định hình trước 2000." | Điều chỉnh: bỏ vế "mục này ghi nhận ông là nguồn kế thừa **trực tiếp**" của đề xuất vì mâu thuẫn với cạnh "Jared Diamond · kế thừa · qua trường phái"; rút gọn để không vượt ~80 chữ (bản dài sinh WARN 110 chữ). Lý do mới khớp với ngưỡng "ảnh hưởng sau 2000" — quy tắc xếp nhóm C2 (NÊN) vẫn chưa viết vào Ghi chú, owner quyết. |
| 7 | C1 | Chapter | Giới thiệu + Ghi chú biên tập | Giới thiệu: "(b), (d) **chưa dùng được**"; Ghi chú tiêu đề "hai tiêu chí không dùng được"; mRNA "vào theo (a) và (c)" | Giới thiệu: "**khó dùng** …; năm mục vẫn dùng chúng, là chỗ yếu nhất"; Ghi chú: tiêu đề "hai tiêu chí khó dùng" + câu liệt kê (d) ở -01, -02, -04, -07, (b) ở -09; mRNA (`CH11-CE21-04`) "theo (d)" | Điều chỉnh: sửa claim cấp chapter cho khớp mục (phương án được giao), không sửa 5 mục. Không dùng phương án (ii) của review ("chỉ dùng được cho công trình thế kỷ trước") vì sai với -04 (Karikó 2005 dùng (d)). Cụm "Hệ quả thấy ngay trong danh sách:" thay bằng "Vì thế" để bù số chữ. |
| 8 | C3 | Chapter | Ghi chú biên tập | "…AlphaFold 2021, mô hình ngôn ngữ lớn sau 2022 — thì vào atlas theo (a) và (c)" | "…AlphaFold 2021 — thì CRISPR và AlphaFold vào theo (a) và (c), vắc-xin mRNA theo (d), còn (b) để trống ở cả ba; mô hình ngôn ngữ lớn sau 2022 thì chưa có mục nào được chọn vì mạch ấy." | Điều chỉnh: bỏ lý do "vì chưa ai đạt mười năm theo D4" của đề xuất — đó là phán đoán mới, và mâu thuẫn với chính mục -06 (Sutskever bị loại theo (c), không theo D4). Gộp cùng câu với sửa C1. |
| 9 | C5 | Chapter | Ghi chú biên tập (Trường `vùng`) | "nhóm được lập và dẫn từ đài Mount Stromlo … nên nơi thành hình là Canberra" | "nhóm được lập năm 1994 khi Schmidt còn làm nghiên cứu sau tiến sĩ ở Harvard; nhưng từ 1995 nhóm được điều phối từ đài Mount Stromlo … — theo nghĩa nơi dẫn dắt, không phải nơi lập nhóm, và vì thế đây là ca tranh cãi" | Điều chỉnh: dữ kiện 1994/1995 đã tự kiểm (Wikipedia High-Z). Bỏ vế "đó là nơi phân tích dẫn tới kết quả 1998 được tổ chức" (chưa kiểm) và vế so sánh Berkeley/Riess (thêm dữ kiện mới); thay bằng ghi rõ ca tranh cãi như review cho phép. Kết luận `vùng: Châu Đại Dương` giữ nguyên. |

**Tổng:** 2 áp dụng nguyên văn (#12, #19) · 7 điều chỉnh (#34, #45, #46, #47, C1, C3, C5) · 0 không áp dụng.

## Cạnh đối xứng ở chapter khác

Không có. Không edit nào đổi liên kết ID, loại quan hệ hay mức bằng chứng.

Lưu ý ngoài chapter (không phải cạnh đối xứng): `data/persons.json` vẫn giữ văn bản cũ (name_orig "Demis Hassabis Kyriacou", câu "vài trăm tài khoản giả", nguồn Cliodynamics, câu Mount Stromlo) cho tới khi chạy build đầy đủ; `--lint-only` không tái sinh file này.

## Lint (`python3 build.py --offline --lint-only`)

- Trước: `Lint: 0 lỗi · 6 cảnh báo · 287 ghi chú` — WARN ch11 duy nhất: `CH11-CE21-05: thiếu tên gốc trong ngoặc` (đã có từ trước, Ghi chú giải thích).
- Sau: `Lint: 0 lỗi · 6 cảnh báo · 287 ghi chú` — WARN ch11 giữ nguyên, không WARN mới. (Một bản nháp của #47 từng sinh `CH11-CE21-12: 'why' 110 chữ` — đã rút gọn và hết.)
