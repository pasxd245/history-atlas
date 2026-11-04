# Lọc lỗi dữ kiện trong báo cáo cũ — Chapter 4 (Đế chế cổ điển, tôn giáo lan tỏa)

- **Phạm vi:** `content/ch04.md`. Báo cáo đã đọc hết: `review-ch04-CE01.md` … `review-ch04-CE05.md` (xếp loại Sai / Nghi vấn / Thiếu / Thể thức — không dùng nhãn BẮT BUỘC/NÊN; ở đây "Sai" được đọc như BẮT BUỘC, "Nghi vấn"/"Thiếu"/"Thể thức" như NÊN), `rebalance-ch04-a.md` (B, C, D1–D4), `rebalance-ch04-b.md` (C1–C3, D-S1…D-F4), `rebalance-facts.md` (§1 Ezana, §3 K'inich Yax K'uk' Mo' / Siyaj K'ak'; §2, §4, §5 là ứng viên không vào ch04), `rebalance-regions.md` (chỉ hai đoạn cảnh báo về Ch4: §A.5 và kết luận), và Ca 1–3 của `tructiep-ch04-05-review.md`.
- **Ngày:** 2026-11-04.
- **Phương pháp:** lấy mọi mục Nghi vấn/Thiếu/Thể thức có nội dung là khẳng định dữ kiện sai hoặc câu tự mâu thuẫn với atlas; mục "Sai" chỉ kiểm đã áp chưa. Đối chiếu từng mục với `content/ch04.md` hiện tại (bản trước khi sửa lưu ở `rv/ch04.before.md`). Mục còn sai: kiểm độc lập bằng web (Britannica, SEP, Encyclopaedia Iranica, Wikipedia làm điểm khởi đầu, văn bản gốc ctext/Wikisource khi có). Sửa trực tiếp `content/ch04.md`.
- **Giới hạn:** không mở được sách in (Schmithausen 1987, Munro-Hay, Bielenstein BMFEA, Plofker, Falk); mục nào chỉ dựa vào chúng thì **làm mềm**, không thêm con số mới. Báo cáo cũ là nguồn ứng viên, không phải bằng chứng. Không đụng dòng `năm:` nào. Các vấn đề thuần quan hệ (`kế thừa` cho định chế/bảo trợ, liên kết "mỏng") không xử lý ở đây, trừ một cạnh `trực tiếp` mà quy ước mức bằng chứng loại thẳng (xem #17).

- **Kết quả:** 108 dòng ứng viên lọc được · 46 đã sửa trước · 56 dòng còn sai (55 quyết định, vì #49 gộp hai dòng) · 6 dòng không phải lỗi dữ kiện đã biết, chuyển KNOWN-ISSUES hoặc không cần xử. Cộng 1 mục ngoài báo cáo (#56) → **56 quyết định: 34 sửa · 20 làm mềm · 2 giữ nguyên.** Không đụng dòng `năm:` nào nên không có độ vênh Wikidata mới phải ghi vào Ghi chú biên tập.
- **Kiểm tra sau patch:** lint ch04 từ `WARN 0` qua tối đa 9 WARN độ dài trong lúc sửa, đã cắt chữ về lại `WARN 0` (xem §5). Bản trước khi sửa: `rv/ch04.before.md`.

## 1. Ứng viên lọc được

Loại: **D** = dữ kiện · **M** = mâu thuẫn nội bộ · **B** = mục "Sai" (≈BẮT BUỘC) chưa áp. Trạng thái: **đã sửa trước** / **còn sai** (→ số ở bảng quyết định).

| Báo cáo · mục gốc | ID | Trường | Trích ngắn | Loại | Trạng thái |
|---|---|---|---|---|---|
| CE01 §2 | Bối cảnh CE01 | Bối cảnh | "Giấy, thiên văn và y dược được ghi chép thành sách" | B/M | còn sai → #1 |
| CE01 §2 | Bối cảnh CE01 | Bối cảnh | "phong trào … tách ra" ở TK 1 | — | tranh luận học thuật → KNOWN-ISSUES |
| CE01 §3.1 | CE01-01 | nơi | "Galilee và Jerusalem, tỉnh Judea" | B | còn sai → #2 |
| CE01 §3.2 | CE01-01 | Tư tưởng | "rẽ khỏi các nhóm Do Thái", dẫn ngược Sanders | B | đã sửa trước |
| CE01 §4.1 | CE01-02 | Vì sao chọn | vai Giacôbê đảo ngược | B | đã sửa trước |
| CE01 §5.1 | CE01-03 | Vì sao chọn | "phép thử duy nhất" | B | đã sửa trước |
| CE01 §5.2 | CE01-03 | Vì sao chọn | "Quang Vũ Đế, người lật ông" | B | đã sửa trước |
| CE01 §5.3 | CE01-03 | Tư tưởng | "khởi nghĩa Xích Mi, và ông bị giết" | D | còn sai → #3 |
| CE01 §6.1 | CE01-04 | Tư tưởng | "trung hưng mà ông tạo ra" | B | đã sửa trước |
| CE01 §7.2 | CE01-05 | Tư tưởng | "thể văn ấy … là đóng góp riêng của ông" | D | còn sai → #4 |
| CE01 §8.1 | CE01-06 | Vì sao chọn | "Aristobulus xứ Paneas" (niên đại đã sửa, tên chưa) | B | còn sai → #5 |
| CE01 §10.3 | CE01-08 | vùng | Châu Âu cho Cilicia | B | đã sửa trước |
| CE01 §12.1 | CE01-10 | Vì sao chọn | "Luận hành còn nguyên" | D | còn sai → #6 |
| CE01 §12.2 | CE01-10 | Vì sao chọn | Hoàn Đàm "cùng thời" | B | đã sửa trước |
| CE01 §12.4 | CE01-10 | Vì sao chọn | "văn bản hoài nghi có hệ thống sớm nhất của Đông Á" (bác bởi chính dòng Kế thừa Tuân Tử) | M | còn sai → #7 |
| CE01 §13.1 + rebal-a Sai-01 | CE01-11 | Tư tưởng | 24 bộ chính sử "đều"/"23 trên 24" | B | đã sửa trước |
| CE01 §14.2 | CE01-12 | Ảnh hưởng tới | trỏ Trương Vĩnh Ký | B | đã sửa trước |
| CE01 §14.3 | CE01-12 | Tư tưởng | Thiên văn chí "có lẽ không phải của bà" | D | còn phải xử → #8 |
| CE01 §14.4 | CE01-12 | Tư tưởng | "suốt gần hai nghìn năm" | D | còn sai → #9 |
| CE01 §14.5 | CE01-12 | Vì sao chọn | "không văn bản nào khác … đạt mức lưu hành như Nữ giới" | D | còn sai → #10 |
| rebal-a Thể-04 | CE01-03 / -04 | Vì sao chọn | "Ngôi Hiêu" / "Ngỗi Hiêu" | M | còn sai → #11 |
| rebal-a Nghi-07 | CE01-04 | Nguồn | Bielenstein "(1953–1979)", ghi như sách | D | còn sai → #12 |
| CE02 Bối cảnh | Bối cảnh CE02 | Bối cảnh | "Ở Alexandria và Pergamon … y học được tổng hợp" | D | còn sai → #13 |
| CE02 §1 | CE02-01 | Vì sao chọn | "không người thợ … nào để lại tên" | B | đã sửa trước |
| CE02 §2 + rebal-a Nghi-06 | CE02-02 | Vì sao chọn | "không có tiền lệ ở bất kỳ nền văn minh nào và không có hậu duệ"; "cơ cấu không được chép lại" | B | còn sai → #14 |
| CE02 §3 | CE02-03 | Nguồn | Lefèvre, *L'art du Gandhara* (sách ma) | B | đã sửa trước |
| CE02 §3 | CE02-03 + Ghi chú | Vì sao chọn; Điểm cần kiểm chứng | "đề xuất trải từ 78 tới 144 CN" | D | còn sai → #15 |
| CE02 §3 | CE02-03 | Tư tưởng | Gandhāra "định hình mọi hình tượng Phật" | D | còn sai → #16 |
| CE02 §3 + rebal-a Nghi-04 | CE02-03 ↔ CE02-04 | quan hệ | `kế thừa · trực tiếp`, tiếp xúc chỉ có trong truyền thống muộn | D | còn sai → #17 |
| CE02 §4 | CE02-04 | Tư tưởng | Nanda "em họ"; "kāvya hoàn chỉnh" | B | đã sửa trước |
| CE02 §4 | CE02-04 | Vì sao chọn | Kālidāsa "chọn ở nhóm khác" (đã sửa) / "thuộc thế kỷ sau" (chưa) | B | còn sai → #18 |
| CE02 §5 | CE02-05 | Vì sao chọn | chu vi Trái Đất quy cho Ptolemy | B | đã sửa trước |
| CE02 §6 | CE02-06 | Tư tưởng | "Vesalius mổ xác người năm 1543" | B | đã sửa trước |
| CE02 §6 | CE02-06 | Vì sao chọn | Soranus "cùng thời" | D (quy tắc 5) | còn sai → #19 |
| CE02 §6 | CE02-06 | độ tin cậy | `Cao` cho năm mất 216 (suy ra) | — | KNOWN-ISSUES |
| CE02 §7 | CE02-07 | Vì sao chọn | Hadot dẫn ngược | B | đã sửa trước |
| CE02 §7 | CE02-07 | Vì sao chọn | Epictetus "người thầy ông" | D | còn sai → #20 |
| CE02 §8 | CE02-08 | Ảnh hưởng tới | trỏ Lý Thái Tổ | B | đã sửa trước |
| CE02 §8 | CE02-08 | Vì sao chọn | "phái Trung quán … là nền chung … Trung Hoa, Triều Tiên, Nhật Bản, Việt Nam" | D | còn sai → #21 |
| CE02 §9 | CE02-09 | Tư tưởng | "ông đặt ra ba công cụ" (truyền thừa tông đồ đã có ở Hegesippus) | D | còn sai → #22 |
| CE02 §10 | CE02-10 | Tư tưởng | persona/substantia/sacramentum "đi vào Latinh qua ông" | B | đã sửa trước |
| CE02 §10 | CE02-10 | Vì sao chọn | Minucius Felix "cùng vùng cùng thời" | D | còn sai → #23 |
| CE02 §11 | CE02-11 | Ảnh hưởng tới | trỏ Tôn Thất Tùng | B | đã sửa trước |
| CE02 §11 | CE02-11 | Vì sao chọn | "còn lại và được chú giải liên tục mười tám thế kỷ" | B | còn sai → #24 |
| CE02 §11 | CE02-11 | Tư tưởng | "ông đưa ra lối biện chứng luận trị" (nhãn hiện đại) | D | còn sai → #25 |
| CE03 §-02 | CE03-02 | Tư tưởng | Hexapla "phê bình văn bản có hệ thống sớm nhất của lịch sử, trước khi khái niệm ấy tồn tại" | B | còn sai → #26 |
| CE03 §-02 | CE03-02 | Tư tưởng | De Principiis "dựng ra chính thể loại" | D | đã sửa trước |
| CE03 §-03 | CE03-03 | Vì sao chọn | "không văn bản triết học nào … lâu như Isagoge" | B | đã sửa trước |
| CE03 §-04 | CE03-04 | Vì sao chọn; Nguồn | "tới thế kỷ 14"; Bardaisan "cùng thời"; CMC | B | đã sửa trước |
| CE03 §-05 | CE03-05 | Tư tưởng | "kinh Avesta bắt đầu được tập hợp" nêu như dữ kiện | D | còn sai → #27 |
| CE03 §-05 + rebal-a Sai-03 | CE03-05 | Tư tưởng | "quốc giáo có tổ chức sớm nhất ở Cận Đông" | B | đã sửa trước |
| CE03 §-06 | CE03-06 | Tư tưởng | bi ký Shapur lẫn với Kartir | B | đã sửa trước |
| CE03 §-07 + rebal-a Thể-05 | CE03-07 | Vì sao chọn | "duy nhất" (đã sửa) → câu treo "— Maximianus thoái vị cùng ngày" | M | còn sai → #28 |
| CE03 §-08 | CE03-08 | Tư tưởng | "khoảng 130 bài toán" | B | đã sửa trước |
| CE03 §-09 | CE03-09 | Tư tưởng | nguyên lý thiết diện quy cho Lưu Huy; 3072 cạnh | B | đã sửa trước |
| CE03 §-10 | CE03-10 | Tư tưởng | hai bản chú "thay thế mọi bản" (Hàn Khang Bá) | B | đã sửa trước |
| CE03 §-10 | CE03-10 | Tư tưởng | "Phật giáo … lần đầu diễn đạt tính không bằng tiếng Hán" | D | còn sai → #29 |
| CE03 §-11 | CE03-11 | Nguồn | de Crespigny *Generals of the South* | B | đã sửa trước |
| CE04 §1.2–1.3, §13.2, rebal-b D-S2 | CE04-01, Bối cảnh CE04 | Tư tưởng | "lần đầu … tín lý"; "triệu tập và chủ toạ" | B | đã sửa trước |
| CE04 §1.4 | CE04-01 | Tư tưởng | chiếu Milan "chấm dứt việc nhà nước bách hại" | D | còn sai → #30 |
| CE04 §2.3 | CE04-02 | Tư tưởng | Đời thánh Antôn "khởi phát phong trào đan tu" | D | còn sai → #31 |
| CE04 §3.1–3.2 | CE04-03 | Tư tưởng | "bản dịch của ông"; nhãn Arius | D | đã sửa trước |
| CE04 §3.2 | CE04-03 | Tư tưởng | "nên các vương quốc German về sau cũng vậy" | D | còn sai → #32 |
| rebal-b D-N3 | CE04-03 | Vì sao chọn | "không ai khác … để lại văn bản" (rune) | M | còn sai → #33 |
| CE04 §4.1 | CE04-04 | Tư tưởng | "nên ta thua" gán cho Julianus | B | đã sửa trước |
| CE04 §4.2 | CE04-04 | Tư tưởng | "sau hai năm trị vì" | D | còn sai → #34 |
| CE04 §4.3 | CE04-04 | Tư tưởng; Vì sao chọn | "thử một việc chưa ai làm"; "phép thử duy nhất trong lịch sử" | D | còn sai → #35 |
| CE04 §5.3 | CE04-05 | Tư tưởng; Vì sao chọn | chuẩn hoá Avesta nêu như dữ kiện và làm trụ (b) | D | còn sai → #36 |
| CE04 §6.2 | CE04-06 | Tư tưởng | "bốn đường thẳng … phương pháp cũ không giải nổi" | D | còn sai → #37 |
| CE04 §7.2 | CE04-07 | Vì sao chọn | Chung Diêu "thế hệ trước" | B | đã sửa trước |
| CE04 §7.3 + rebal-b D-N1 | CE04-07 | độ tin cậy | `Cao` cho 303–361 (có hệ 321–379) | D | còn sai → #38 |
| CE04 §8.1 | (Cố Khải Chi, nay là Ghi chú) | Ghi chú biên tập | "tranh Cố Khải Chi chỉ còn bản mô đời Đường"; "Ba mục" | D/M | còn sai → #39 |
| CE04 §9.2–9.4, rebal-b D-N8 | CE04-09 (cũ) | — | Chandragupta II: Sarnath, trụ sắt | B | đã xử trước (mục bị thay bằng Ezana) |
| CE04 §10.1 | CE04-10 | Tư tưởng; Vì sao chọn | "ông đưa ra khái niệm a-lại-da thức"; "khung … là của ông" | D | còn sai → #40 |
| CE04 §11.1 | CE04-11 | Tư tưởng | Câu-xá "chuẩn ở mọi truyền thống" | B | đã sửa trước |
| CE04 §11.5, §12.5 | CE04-11 → CE05-07; CE04-12 → CE05-07 | quan hệ | Kumārajīva | — | đã gỡ trước (chiều CE05-07 ← CE04-11 còn: KNOWN-ISSUES) |
| CE04 §12.2, §12.4 | CE04-12 | Tư tưởng; Vì sao chọn | "qua Java" (Deeg); Nghĩa Tịnh không niên đại | B | đã sửa trước |
| CE04 §12.3 + rebal-b D-N6 | CE04-12 | Tư tưởng; Vì sao chọn | "ký sự đầu tiên"; "người Đông Á đầu tiên đi trọn hành trình" | D | còn sai → #41 |
| CE05 -01 §1 + rebal-b D-N4 | CE05-01 | Vì sao chọn | "không tác giả Kitô giáo nào khác được cả Aquinas lẫn Luther và Calvin viện dẫn" | D/M | còn sai → #42 |
| CE05 -01 §4 | CE05-01 | nơi | "Thagaste, Milano và Hippo Regius, Bắc Phi" | D | còn sai → #43 |
| CE05 -02 §2 | CE05-02 | Tư tưởng | "người đầu tiên lập luận có hệ thống" về quyền Phêrô | D | còn sai → #44 |
| CE05 -02 §3 | CE05-02 | Tư tưởng | "đi gặp Attila …, và quân Hung rút" (nhân quả ngầm) | D | còn sai → #45 |
| CE05 -03 §1 | CE05-03 | Tư tưởng | 210 mệnh đề | B | đã sửa trước |
| CE05 -04 §1–3, rebal-b D-S3 | CE05-04 | Tư tưởng; Vì sao chọn; Nguồn | di cư German; counterfactual; Priscus "qua Jordanes" | B | đã sửa trước |
| CE05 -05 §1, §3 | CE05-05 | Tư tưởng; Kế thừa | "gần một nghìn năm"; liên kết Cicero | B | đã sửa trước |
| rebal-b D-N5 | CE05-05 | Tư tưởng | tường thành "giữ được thành phố … tới 1453" (1204) | D | còn sai → #46 |
| CE05 -06, rebal-b D-S1 | CE05-06 | Tư tưởng; Vì sao chọn | "các nguồn gần thời"; ba tác phẩm cùng mức; "nữ toán học sớm nhất" | B | đã sửa trước |
| rebal-b D-S5 | CE05-07 | độ tin cậy | `Cao` cho 344–413 | B | đã sửa trước |
| CE05 -08 §1 | CE05-08 | Nguồn | Crosby "A New History" | B | đã sửa trước |
| CE05 -08 §2 | CE05-08 | Vì sao chọn | "mười lăm thế kỷ" cho cả năm nước | D | còn sai → #47 |
| CE05 -09 §1 | CE05-09 | Tư tưởng | "bảng sin đầu tiên" | B | đã sửa trước |
| rebal-b D-N2 | CE05-09 | độ tin cậy | `Cao` cho năm mất 550 (ước đoán) | — | KNOWN-ISSUES |
| CE05 -10 §1, rebal-b D-S4 | CE05-10 | Tư tưởng | "nguồn sớm nhất về Giao Chỉ"; "lần đầu phụ nữ" | B | đã sửa trước |
| CE05 -11 §3 | CE05-11 | Vì sao chọn | Hà Thừa Thiên "cùng thời" | D (quy tắc 5) | còn sai → #48 |
| CE05 -12 §2 | CE05-12 | Tư tưởng | quân điền quy cho ông, tự mâu thuẫn | B | đã sửa trước |
| CE05 -12 §3 | CE05-12 | Tư tưởng | "kế thừa nguyên chế độ", "Việt Nam phỏng theo" | D | còn sai → #55 |
| CE05 GC B1–B3 | Ghi chú "nặng về tôn giáo" | Ghi chú | 17/58; Hoả giáo | B | đã sửa trước (thành 22/60) — **nay sai lại** → #49 |
| CE05 GC B2 | Ghi chú "nặng về tôn giáo" | Ghi chú | "ở cả bốn vùng" | M | còn sai → #49 |
| CE05 GC E3 | Ghi chú "Ứng viên mạnh" | Ghi chú | Iamblichus, Epictetus "không để lại văn bản đủ" | D | còn sai → #50 |
| CE05 GC F3, D | Ghi chú | Ghi chú | "ba phụ nữ"; Lâm Ấp "không ai định danh" | B | đã sửa trước |
| rebal-b D-N7 | CE04-08 Theodosius I | Vì sao chọn | sám hối 390 "tiền lệ đầu tiên" (Callinicum 388) | D | còn sai → #51 |
| CE01 §11.2 | CE01-09 | độ tin cậy | `Cao` cho năm mất k. 100 | — | KNOWN-ISSUES |
| rebal-facts §1.3–1.6 | CE04-09 Ezana + Ghi chú | Tư tưởng; Ghi chú | thánh giá "đầu tiên", "nhà nước thứ hai", "diệt Kush", Frumentius | — | đã áp trước |
| rebal-facts §3.5 | Ghi chú "Châu Mỹ" | Ghi chú | "El Perú 8/1/378, Tikal 14/1/378" | D/M | còn sai → #52 |
| rebal-facts §3.3 | Ghi chú "Châu Mỹ" | Ghi chú | đồng vị: "lớn lên ở vùng Tikal/Petén" | D | còn sai → #53 |
| rebal-b C3 / Ghi chú | Ghi chú "Châu Mỹ" | Ghi chú | Teotihuacan "lớn nhất châu Mỹ tiền Columbus" | D | còn phải xử → #54 |
| rebal-regions §A.5, kết luận | — | — | "Sihyaj K'ahk' vào Tikal 15/5/378" | — | không có trong ch04; ngày này **không** nên chép (vênh với cả hai nguồn khác) |
| tructiep Ca 1–3 | CE01-01, CE05-04, CE05-06 | quan hệ | `trực tiếp` → Gioan, Rugila, Theon | — | báo cáo kết luận GIỮ; content đúng |

## 2. Quyết định cho mục còn sai

| # | ID | Trường | Trước | Sau | Quyết định | Bằng chứng |
|---|---|---|---|---|---|---|
| 1 | Bối cảnh CE01 | Bối cảnh | "Giấy, thiên văn và y dược được ghi chép thành sách…" | "Thiên văn và y dược được ghi chép thành sách…" | sửa (nhất quán nội bộ). Mốc giấy của atlas là Thái Luân 105 CN (`CH04-CE02-01`), và Bối cảnh CE02 đã ghi "Nhà Đông Hán có giấy". | kiểm trong atlas: `content/ch04.md` CE02-01, Bối cảnh CE02 |
| 2 | CE01-01 Giê-su | nơi | "Galilee và Jerusalem, tỉnh Judea" | "Galilee, lãnh địa của Herod Antipas, và Jerusalem, tỉnh Judea" | sửa. Antipas là tetrarch Galilee–Perea suốt thời Giê-su; Galilee không thuộc tỉnh Judaea. | https://www.britannica.com/biography/Herod-Antipas |
| 3 | CE01-03 Vương Mãng | Tư tưởng | "dẫn tới khởi nghĩa Xích Mi, và ông bị giết năm 23 CN" | "dẫn tới các cuộc khởi nghĩa như Xích Mi và Lục Lâm, và ông bị giết năm 23 CN khi quân của Canh Thuỷ Đế hạ Trường An" | sửa (quy kết theo vị trí câu). Quân Canh Thuỷ (Lục Lâm) hạ Trường An 4/10/23; Xích Mi không dự trận ấy. | https://en.wikipedia.org/wiki/Wang_Mang |
| 4 | CE01-05 Seneca | Tư tưởng | "là đóng góp riêng của ông" | "không do ông đặt ra, vì Epicurus đã viết thư triết học gửi môn đệ, nhưng ở ông nó thành cả một chương trình tu dưỡng qua hơn trăm lá thư" | sửa. Diogenes Laertius giữ ba thư của Epicurus (Herodotus, Pythocles, Menoeceus). Không thêm Cicero/consolatio như reviewer đề xuất. | https://plato.stanford.edu/entries/epicurus/ |
| 5 | CE01-06 Philo | Vì sao chọn | "Aristobulus xứ Paneas" | "Aristobulus xứ Alexandria" | sửa. "Paneas" là dịch sai từ ὁ πάνυ trong bản Latinh của Rufinus; định danh ấy đã bị bỏ. | https://en.wikipedia.org/wiki/Aristobulus_of_Alexandria |
| 6 | CE01-10 Vương Sung | Vì sao chọn | "Luận hành còn nguyên" | "Luận hành truyền lại gần trọn — thiên 44 chỉ còn tên" | sửa. 85 thiên, nhưng thiên 44 *Chiêu trí* chỉ còn đầu đề. | https://en.wikipedia.org/wiki/Lunheng |
| 7 | CE01-10 Vương Sung | Vì sao chọn | "là văn bản hoài nghi có hệ thống sớm nhất của Đông Á" | "là bộ sách hoài nghi có hệ thống được đọc lại mỗi khi…" | **làm mềm** (mâu thuẫn nội bộ). Chính mục ghi kế thừa từ Tuân Tử (`CH03-BCE03-11`), mà thiên 17 *Thiên luận* đã lập luận trời không đáp hành vi người. Bỏ "sớm nhất", không thay bằng hạng mới. | https://plato.stanford.edu/entries/xunzi/ |
| 8 | CE01-12 Ban Chiêu | Tư tưởng | "soạn các bảng niên biểu và thiên Thiên văn chí" | (giữ) | **giữ nguyên — reviewer sai một phần.** *Hậu Hán thư · Liệt nữ truyện*: "其八表及天文志未及竟而卒，和帝詔昭…踵而成之", rồi "後又詔融兄續繼昭成之" — tức chính bà được giao hoàn thành cả tám bảng lẫn Thiên văn chí, Mã Tục làm tiếp sau. | https://ctext.org/hou-han-shu/lie-nv-zhuan |
| 9 | CE01-12 Ban Chiêu | Tư tưởng | "khuôn ràng buộc nữ giới suốt gần hai nghìn năm ở…" | "khuôn ràng buộc nữ giới ở Trung Hoa, Triều Tiên và Việt Nam, lưu hành rộng nhất từ cuối Minh khi được xếp vào Nữ tứ thư" | **làm mềm.** Bỏ con số thời lượng; giữ mốc kiểm được. | https://en.wikipedia.org/wiki/Lessons_for_Women |
| 10 | CE01-12 Ban Chiêu | Vì sao chọn | "không văn bản nào khác do phụ nữ Đông Á viết đạt mức lưu hành như Nữ giới" | "Nữ giới là một trong những văn bản do phụ nữ Đông Á viết được lưu hành lâu và rộng nhất" | **làm mềm.** Mệnh đề tuyệt đối không kiểm được (Nội huấn cùng nằm trong Nữ tứ thư). | (bỏ so sánh tuyệt đối; không cần nguồn mới) |
| 11 | CE01-03 Vương Mãng | Vì sao chọn | "Ngôi Hiêu" | "Ngỗi Hiêu" | sửa (nhất quán nội bộ: mục CE01-04 viết "Ngỗi Hiêu"; viwiki dùng "Ngỗi Hiêu" 隗囂). | https://vi.wikipedia.org/wiki/Ngỗi_Hiêu |
| 12 | CE01-04 Quang Vũ Đế | Nguồn | "The Restoration of the Han Dynasty (1953–1979)" | "…, loạt bốn phần trên Bulletin of the Museum of Far Eastern Antiquities (1954–1979)" | sửa. BMFEA 26 (1954), 31 (1959), 39 (1967), 51 (1979); không phải sách, và năm đầu là 1954. Không ghi số tập/trang vào dòng Nguồn. | https://en.wikipedia.org/wiki/Hans_Bielenstein |
| 13 | Bối cảnh CE02 | Bối cảnh | "Ở Alexandria và Pergamon, thiên văn và y học…" | "Ở Alexandria và Rome, …" | sửa. Galen tới Rome năm 162 và viết phần lớn trước tác ở triều đình Rome; chính trường `nơi:` của CE02-06 có Rome. Số chữ không đổi. | https://en.wikipedia.org/wiki/Galen |
| 14 | CE02-02 Trương Hành | Vì sao chọn | "không có tiền lệ ở bất kỳ nền văn minh nào và không có hậu duệ trực tiếp, tức nó là một sáng chế đơn độc. Cơ cấu bên trong máy không được chép lại…" | "không có tiền lệ được biết ở nền văn minh nào. Hậu Hán thư chỉ chép sơ lược cơ cấu bên trong — một trụ giữa và tám đường dẫn — nên mọi bản phục dựng…" | **làm mềm + sửa.** "Không được chép lại" sai: nguồn có câu về trụ giữa và tám đường. Vế "không có hậu duệ" bị reviewer bác bằng hai sách đời Bắc Tề/Tuỳ mà tôi không mở được, nên bỏ vế ấy chứ không chép tên sách vào. | https://en.wikipedia.org/wiki/Seismometer |
| 15 | CE02-03 Kanishka + Ghi chú "Điểm cần kiểm chứng" | Vì sao chọn; Ghi chú | "đề xuất trải từ 78 tới 144 CN" | "đề xuất trải từ năm 78 tới tận thế kỷ 3" | sửa (2 chỗ). Các đề xuất đã có: 78, 103, 134, 142, 144, 232, 248/249, 278 (và 58 TCN, nay bị bác). | https://ar.unesco.org/silkroad/sites/default/files/knowledge-bank-article/vol_II%20silk%20road_the%20kushans.pdf |
| 16 | CE02-03 Kanishka | Tư tưởng | "Nghệ thuật Gandhāra tạc Phật theo lối tượng người, định hình mọi hình tượng Phật về sau" | "Nghệ thuật Gandhāra và Mathura tạc Phật theo lối tượng người, có lẽ độc lập với nhau" | sửa. Britannica: "It is possible that the two schools independently developed…"; câu hỏi nơi nào có trước "insoluble". | https://www.britannica.com/art/South-Asian-arts/Indian-sculpture-from-the-1st-to-4th-centuries-ce-Mathura |
| 17 | CE02-03 ↔ CE02-04 | quan hệ (hai chiều) | `kế thừa · trực tiếp` | `kế thừa · suy đoán học giả` | **làm mềm.** Quy ước mức bằng chứng điều 1 đòi tiếp xúc "chứng minh được bằng nguồn"; việc Aśvaghoṣa làm cố vấn Kanishka chỉ là "seems probable", dựa vào truyền thống Hán văn đời sau. | https://en.wikipedia.org/wiki/A%C5%9Bvagho%E1%B9%A3a · CONTRIBUTING.md "Quy ước mức bằng chứng" |
| 18 | CE02-04 Aśvaghoṣa | Vì sao chọn | "Kālidāsa, thuộc thế kỷ sau" | "Kālidāsa, sống sau ông vài thế kỷ" | sửa (quy tắc 5). Aśvaghoṣa k. 80–150; Kālidāsa thường đặt TK 4–5 — chính Ghi chú biên tập ch04 nói vậy. | kiểm trong atlas: Ghi chú "Ứng viên mạnh đã bị loại" |
| 19 | CE02-06 Galen | Vì sao chọn | "Ứng viên cùng thời là Soranus…, và Aretaeus" | "Ứng viên cùng lĩnh vực là Soranus xứ Ephesus, hoạt động ở thế hệ trước ông, …, và Aretaeus…, niên đại không xác định được" | sửa (quy tắc 5). Soranus hành nghề dưới Trajan–Hadrian (98–138); Galen sinh 129. | https://en.wikipedia.org/wiki/Soranus_of_Ephesus |
| 20 | CE02-07 Marcus Aurelius | Vì sao chọn | "Epictetus, người thầy ông đọc và trích" | "Epictetus, người ông chỉ biết qua bản chép Rusticus đưa" | sửa. *Suy tưởng* 1.7: biết lời giảng Epictetus qua bộ chép Rusticus cho mượn; không có ghi nhận hai người gặp nhau. | https://en.wikipedia.org/wiki/Junius_Rusticus |
| 21 | CE02-08 Nāgārjuna | Vì sao chọn | "phái Trung quán do ông lập là nền chung của Phật giáo Đại thừa ở Tây Tạng, Trung Hoa, Triều Tiên, Nhật Bản và Việt Nam" | "phái Trung quán do ông lập được Tây Tạng xếp làm kiến giải cao nhất, còn ở Đông Á giáo lý tính không của ông thấm vào các tông về sau, dù Tam luận tông suy tàn" | **làm mềm.** Tam luận tông "declined considerably", tư tưởng thấm vào Thiền/Thiên Thai. Đồng thời cắt 2 chữ ở câu đầu để không thêm WARN. | https://en.wikipedia.org/wiki/Sanlun |
| 22 | CE02-09 Irenaeus | Tư tưởng | "ông đặt ra ba công cụ" | "ông dựng thành hệ thống ba công cụ …; nguyên tắc truyền thừa từ các tông đồ…, mà Hegesippus đã lập danh sách trước ông" | **làm mềm.** Hegesippus: "when I was in Rome, I made a succession up to Anicetus" (k. 157–168). | https://en.wikipedia.org/wiki/Hegesippus_(chronicler) |
| 23 | CE02-10 Tertullianô | Vì sao chọn | "Ứng viên cùng vùng cùng thời là Minucius Felix" | "Ứng viên gần nhất là Minucius Felix, cũng viết biện giáo Latinh nhưng không rõ trước hay sau ông" | **làm mềm.** Thứ tự với Tertullianô tranh luận; Jerome ghi Minucius hành nghề ở Rome, gốc châu Phi chỉ là suy đoán. | https://iep.utm.edu/minucius |
| 24 | CE02-11 Trương Trọng Cảnh | Vì sao chọn | "văn bản của ông còn lại và được chú giải liên tục mười tám thế kỷ" | "văn bản của ông còn lại qua bản Vương Thúc Hoà sắp lại đời Tấn và bản hiệu đính năm 1065, rồi được chú giải liên tục từ thế kỷ 12" | sửa. Vương Thúc Hoà sắp lại bộ sách; Hiệu chính y thư cục in năm 1065; *Chú giải Thương hàn luận* của Thành Vô Kỷ xong trước 1144. | https://cbook.qq.com/read/1027613602/8 · https://square.umin.ac.jp/mayanagi/paper02/ShanghanlunLishi.pdf |
| 25 | CE02-11 | Tư tưởng | "Thương hàn tạp bệnh luận đưa ra lối biện chứng luận trị" | "đặt nền cho lối mà Trung y về sau gọi là biện chứng luận trị" | **làm mềm.** Không gán nhãn đời sau cho văn bản TK 2–3; không ghi năm chuẩn hoá thuật ngữ vì chưa kiểm. | (không thêm khẳng định mới) |
| 26 | CE03-02 Origen | Tư tưởng | "Đây là bản phê bình văn bản có hệ thống sớm nhất của lịch sử, làm ra trước khi khái niệm ấy tồn tại." | "Đây là lần đầu phép phê bình văn bản mà các học giả Alexandria từng làm trên Homer được áp có hệ thống cho Kinh Thánh, và ông dùng lại cả các ký hiệu obelos và asteriskos của Aristarchus." | sửa. Origen dùng "the symbols used by Aristarchus in his edition of Homer". | https://www.newadvent.org/cathen/07316a.htm |
| 27 | CE03-05 Ardashir I | Tư tưởng | "kinh Avesta bắt đầu được tập hợp, và công thức tôn giáo cùng vương quyền là anh em sinh đôi trở thành lý thuyết chính thống" | "và theo nguồn Hoả giáo muộn, kinh Avesta bắt đầu được tập hợp và tôn giáo cùng vương quyền được coi là anh em sinh đôi" | **làm mềm.** Dēnkard quy việc gom Avesta cho Tansar thời Ardashir; giới nghiên cứu nay coi Avesta được truyền khẩu và chỉ viết ra khoảng TK 5–6. Số chữ 129 (trước 130). | https://en.wikipedia.org/wiki/Avesta |
| 28 | CE03-07 Diocletianus | Vì sao chọn | "…sụp ngay sau khi ông thoái vị năm 305 — ông là hoàng đế La Mã đầu tiên tự nguyện về hưu — Maximianus thoái vị cùng ngày với ông." | "…sụp ngay sau khi ông và Maximianus cùng thoái vị năm 305; ông là hoàng đế La Mã đầu tiên tự nguyện rời ngôi." | sửa (câu tự mâu thuẫn). "the first (and arguably only) Roman emperor to voluntarily abdicate"; Maximianus theo Lactantius bị ép. | https://en.wikipedia.org/wiki/Diocletian |
| 29 | CE03-10 Vương Bật | Tư tưởng | "là thứ Phật giáo dùng khi lần đầu diễn đạt tính không bằng tiếng Hán" | "Phật giáo Trung Hoa thế kỷ 4 mượn chính khung từ vựng ấy khi bàn tính không." | sửa. Bản dịch Bát-nhã bát thiên tụng đầu tiên (Chi Lâu Ca Sấm, 179) có trước Vương Bật; các nhóm Bát-nhã đọc tính không theo lối "bản vô" của Huyền học là chuyện về sau. Câu ngắn lại để giữ ≤130 chữ. | https://ntireader.org/taisho/t0224.html · https://www.rep.routledge.com/articles/overview/buddhist-philosophy-chinese/v-1/sections/sinicizing-buddhist-concepts-emptiness |
| 30 | CE04-01 Constantinus | Tư tưởng | "ban chiếu Milan cho phép tự do thờ phụng, chấm dứt việc nhà nước bách hại Kitô giáo" | "…cho phép tự do thờ phụng, nối tiếp chiếu khoan dung năm 311 của Galerius, văn bản chấm dứt cuộc bách hại" | sửa. Sắc chỉ Serdica 311 "officially ended the Diocletianic Persecution". Bỏ luôn "suốt mười lăm thế kỷ" (đánh giá không quy thuộc, CE04 §1.5) để giữ số chữ. | https://en.wikipedia.org/wiki/Edict_of_Serdica |
| 31 | CE04-02 Athanasius | Tư tưởng | "…vào phương Tây và khởi phát phong trào đan tu." | "…và khởi phát phong trào đan tu ở đó." | sửa. Antôn "was not the first ascetic"; Pachomius lập đan tu cộng đoàn trước đó; bản Latinh của Evagrius lan sang phương Tây. Khớp dòng `Ảnh hưởng tới: Phong trào đan tu phương Tây`. | https://en.wikipedia.org/wiki/Life_of_Anthony |
| 32 | CE04-03 Wulfila | Tư tưởng | "…quen gọi gộp là Arius, nên các vương quốc German về sau cũng vậy." | "…, và bản dịch ấy góp phần đưa nhiều vương quốc German về sau theo lập trường này." | **làm mềm** (quan hệ nhân quả). Không thêm Valens vào. Bỏ "mực bạc trên da tím" (thiếu mực vàng) để giữ số chữ. | (hạ khẳng định; không thêm dữ kiện) |
| 33 | CE04-03 Wulfila | Vì sao chọn | "không ai khác trong thế giới German thế kỷ 4 để lại văn bản" | "ngoài các khắc rune ngắn, không ai khác … để lại văn bản dài" | sửa (lệch với thân mục, vốn viết "văn bản dài"). Lược Vimose có rune từ k. 160. Không dùng sừng Gallehus như reviewer vì nó thuộc đầu TK 5. | https://en.wikipedia.org/wiki/Vimose_inscriptions · https://en.wikipedia.org/wiki/Golden_Horns_of_Gallehus |
| 34 | CE04-04 Julianus | Tư tưởng | "khi ông tử trận ở Ba Tư sau hai năm trị vì" | "khi ông tử trận ở Ba Tư năm 363, chưa đầy hai năm sau khi thành hoàng đế duy nhất" | sửa. Augustus từ 2/360, một mình từ 3/11/361, mất 26/6/363. | https://en.wikipedia.org/wiki/Julian_(emperor) |
| 35 | CE04-04 Julianus + Ghi chú "Hoán đổi" | Tư tưởng; Vì sao chọn; Ghi chú | "ông thử một việc chưa ai làm"; "phép thử duy nhất trong lịch sử"; "phép thử phản chứng duy nhất" | "ông thử làm điều Maximinus Daia từng phác ra ở phía đông"; "phép thử rõ nhất"; "phép thử phản chứng rõ nhất" | **làm mềm.** Maximinus Daia đã dựng hệ thống thượng tế ngoại giáo theo tỉnh (Barnes, dẫn trong Nicholson 1994). Vế Maximinus là **bằng chứng tôi tìm thêm**, reviewer chỉ nêu §4.3 (siêu cấp không quy thuộc). | https://www.cambridge.org/core/journals/journal-of-ecclesiastical-history/article/abs/pagan-churches-of-maximinus-daia-and-julian-the-apostate/C9D273A215AAAB806B7FAB192756D390 |
| 36 | CE04-05 Shapur II | Tư tưởng; Vì sao chọn | "ông đẩy việc tập hợp và chuẩn hoá kinh Avesta…"; "việc chuẩn hoá Avesta dưới triều ông là bước quyết định cho hình dạng Hoả giáo về sau" | "truyền thống Hoả giáo (Dēnkard) gắn triều ông và thượng tế Ādurbād với việc định lại kinh Avesta"; "Việc định kinh Avesta mà truyền thống gắn với triều ông thì có lẽ chỉ khép lại dưới Khosrow I ở thế kỷ 6." | **làm mềm.** Iranica: Ādurbād "may have helped define" quy điển; "the final canon seems to have been set under Khosrow I". Trụ (b) giờ chỉ còn biên giới Rome–Ba Tư. | https://www.iranicaonline.org/articles/adurbad-i-mahrspandan |
| 37 | CE04-06 Pappus | Tư tưởng | "bài toán về quỹ tích ứng với bốn đường thẳng — … nói rõ rằng phương pháp cũ không giải nổi" | "bài toán quỹ tích ứng với ba, bốn hay nhiều đường thẳng, trình bày được trường hợp ba và bốn đường nhưng không bàn trường hợp tổng quát — … khi giải trường hợp tổng quát mà người xưa không làm được" | sửa. SEP: Pappus "presents a solution to the three and four line versions"; Descartes giải trường hợp n đường. | https://plato.stanford.edu/entries/descartes-mathematics/ |
| 38 | CE04-07 Vương Hi Chi | độ tin cậy niên đại | `Cao` | `Trung bình` | sửa (hai báo cáo cùng chỉ ra). Ngoài 303–361 còn các hệ 321–379, 305–363, 307–365. Dòng `năm:` giữ nguyên, nên không cần ghi độ vênh Wikidata. | https://en.wikipedia.org/wiki/Wang_Xizhi |
| 39 | Ghi chú "Điểm cần kiểm chứng thêm" | Ghi chú | "Ba mục có nguồn chỉ còn qua bản dịch hoặc bản mô: … tranh Cố Khải Chi chỉ còn bản mô đời Đường" | "Ba người … tranh Cố Khải Chi (nay chỉ còn trong danh sách bị loại) chỉ còn qua bản chép đời sau, niên đại còn bàn — Bảo tàng Anh ghi cuộn Nữ sử châm đồ là thế kỷ 5–7, không gọi là bản mô đời Đường" | sửa. Cố Khải Chi không còn là "mục"; BM ghi "5thC–7thC", không ghi "Tang copy". | https://www.britishmuseum.org/collection/object/A_1903-0408-0-1 |
| 40 | CE04-10 Asaṅga | Tư tưởng; Vì sao chọn | "Ông đưa ra khái niệm a-lại-da thức"; "khung a-lại-da thức là của ông" | "Ông hệ thống hoá khái niệm a-lại-da thức, vốn đã manh nha trong Giải thâm mật kinh và các tầng sớm của Du-già sư địa luận"; "việc dựng khung … thành một học thuyết hoàn chỉnh là công của ông" | sửa. SEP: điểm khởi của thuyết ālaya ở *Samāhitā Bhūmi*; Asaṅga và Vasubandhu "building on and systemising these early materials". | https://plato.stanford.edu/entries/yogacara/ |
| 41 | CE04-12 Pháp Hiển | Tư tưởng; Vì sao chọn | "ký sự đầu tiên của một người Đông Á về Nam Á"; "Không có ứng viên cùng thời: ông là người Đông Á đầu tiên đi trọn hành trình này và về được." | "ký sự sớm nhất còn lại …"; "Không nêu được ứng viên cùng thời: ông là người Đông Á sớm nhất còn để lại ký sự về trọn hành trình này." | **làm mềm.** Britannica không gọi ông là người đầu tiên. Thêm "còn lại" thay vì khẳng định ưu tiên. | https://www.britannica.com/biography/Faxian |
| 42 | CE05-01 Augustinô | Vì sao chọn | "không tác giả Kitô giáo nào khác được cả Thomas Aquinas lẫn Luther và Calvin cùng viện dẫn làm thẩm quyền" | "ngoài các tác giả Tân Ước, hiếm tác giả Kitô giáo nào được cả … viện dẫn làm thẩm quyền dày đặc như ông" | sửa (mâu thuẫn nội bộ). Mục `CH04-CE01-02` ghi thư Rôma của Phaolô là văn bản Augustinô **rồi Luther** đều đọc lại; cả ba cũng dẫn Hieronymus, người câu ngay trước vừa nêu. | kiểm trong atlas: CE01-02, CE05-01 |
| 43 | CE05-01 Augustinô | nơi | "Thagaste, Milano và Hippo Regius, Bắc Phi" | "Thagaste và Hippo Regius ở Bắc Phi, và Milano" | sửa (Milano không ở Bắc Phi). | (địa lý hiển nhiên) |
| 44 | CE05-02 Lêô I | Tư tưởng | "Ông cũng là người đầu tiên lập luận có hệ thống…" | "…là một trong những người đầu tiên lập luận có hệ thống…" | **làm mềm.** Wikipedia: "one of the first bishops of Rome to promote papal primacy based on succession from Peter"; Damasus, Innocentê I đi trước. | https://en.wikipedia.org/wiki/Pope_Leo_I |
| 45 | CE05-02 Lêô I | Tư tưởng | "Năm 452 ông đi gặp Attila ở bắc Italia, và quân Hung rút." | "…và quân Hung rút, dù Hydatius quy việc rút cho nạn đói, dịch bệnh và quân Đông La Mã." | **làm mềm** (nhân quả ngầm). | https://en.wikipedia.org/wiki/Attila |
| 46 | CE05-05 Theodosius II | Tư tưởng | "Tường thành Constantinopolis dựng dưới triều ông giữ được thành phố hơn một nghìn năm, tới năm 1453." | "Tường thành phía đất liền dựng dưới triều ông là tuyến phòng thủ chính của Constantinopolis hơn một nghìn năm, tới năm 1453." | sửa. Năm 1204 thành thất thủ qua tường biển Sừng Vàng. (Câu "quân Thập tự năm 1204 vào thành từ phía biển" đã thử thêm rồi bỏ để không vượt trần chữ.) | https://en.wikipedia.org/wiki/Walls_of_Constantinople |
| 47 | CE05-08 Buddhaghosa | Vì sao chọn | "sách chuẩn của Theravāda ở Sri Lanka, Miến Điện, Thái Lan, Lào và Campuchia suốt mười lăm thế kỷ" | "…ở Sri Lanka suốt mười lăm thế kỷ, rồi ở Miến Điện, Thái Lan, Lào và Campuchia khi Theravāda thành dòng chủ lưu ở đó" | sửa. Theravāda ở Pagan phục hưng dưới Anawrahta (1014–1077); Khmer thế kỷ 9–13 theo Ấn giáo/Đại thừa. Không ghi thế kỷ cụ thể cho từng nước. | https://en.wikipedia.org/wiki/Buddhism_in_Southeast_Asia |
| 48 | CE05-11 Tổ Xung Chi | Vì sao chọn | "Hà Thừa Thiên, nhà lịch pháp cùng thời" | "Hà Thừa Thiên, nhà lịch pháp thế hệ trước, tác giả lịch Nguyên Gia mà ông chê là chưa chính xác" | sửa (quy tắc 5). Hà 370–447, Tổ 429–500; Tổ cho lịch Nguyên Gia (443/445) còn sai và soạn lịch Đại Minh. | https://www.zdic.net/hant/何承天 · https://mathshistory.st-andrews.ac.uk/BEA/zu_chongzhi_bea.pdf |
| 49 | Ghi chú "Vì sao chapter này nặng về tôn giáo" | Ghi chú | "Hai mươi hai trên sáu mươi … hơn một phần ba … ở cả bốn vùng của chapter — Kitô giáo ở Địa Trung Hải, …"; "con số hai mươi hai" | "Hai mươi tư trên sáu mươi … hai phần năm … ở cả năm vùng của chapter — Kitô giáo ở Địa Trung Hải và ở Aksum, …"; "con số hai mươi tư" | sửa (nhất quán nội bộ). Đếm lại trên `content/ch04.md`: 24 dòng metadata có Tôn giáo/Tâm linh (Theodosius I và Ezana thêm sau khi con số 22 được chốt). Vẫn cao nhất atlas (ch05: 23/60). Lint: "phủ 5/9 vùng". Khối này tự nhận "mọi con số lấy từ persons.json", nên con số sai là lỗi chặn. | kiểm trong atlas (`grep` dòng `lĩnh vực:` của 11 chapter) |
| 50 | Ghi chú "Ứng viên mạnh đã bị loại" | Ghi chú | "Epictetus, …, Iamblichus, Damascius, Syrianus: xếp sau ở độ bền hoặc không để lại văn bản đủ." | "…: đều để lại văn bản (riêng Musonius chỉ còn qua bản ghi của học trò) và đều đáng xét, nhưng xếp sau ở ít nhất một tiêu chí so với các mục đã chọn; Iamblichus và Syrianus là hai ca sát nút nhất vì mạch Tân Plato mà Proclus kế thừa đi qua họ." | **làm mềm.** Lý do cũ sai với Iamblichus (*De mysteriis*…) và Epictetus (*Encheiridion*). Không thêm lý do cụ thể mới ngoài điều mục Proclus đã nêu (Syrianus là thầy ông). | kiểm trong atlas: CE05-03 |
| 51 | CE04-08 Theodosius I | Vì sao chọn | "vụ sám hối năm 390 là tiền lệ đầu tiên cho việc quyền giáo hội đứng trên hoàng đế…" | "vụ sám hối năm 390, sau lần Ambrôsiô buộc ông lùi về vụ đốt nhà hội Do Thái năm 388, là tiền lệ cho…" | sửa. Britannica: "In 388 he rebuked the emperor Theodosius…" rồi 390 bắt sám hối. | https://www.britannica.com/biography/Saint-Ambrose |
| 52 | Ghi chú "Vì sao Châu Mỹ bằng 0" | Ghi chú | "hành trình của ông được chép theo ngày (El Perú 8/1/378, Tikal 14/1/378)" | "…được chép theo ngày, qua El Perú rồi tới Tikal trong tháng 1 năm 378 (các nguồn đổi lịch vênh nhau vài ngày nên ở đây không ghi ngày)" | **làm mềm.** `rebalance-facts` §3.5 ghi Tikal 16/1 (tám ngày sau El Perú), `rebalance-ch04-b` ghi 14/1, `rebalance-regions` ghi 15/5; Wikipedia chỉ ghi "January 378". Không chọn con số nào. | https://en.wikipedia.org/wiki/Siyaj_K%27ak%27 |
| 53 | Ghi chú "Vì sao Châu Mỹ bằng 0" | Ghi chú | "đồng vị stronti cho thấy K'inich Yax K'uk' Mo' lớn lên ở vùng Tikal/Petén" | "…không sinh ra ở Copán, với chữ ký tương thích vùng Petén chứ không phải Teotihuacan (đồng vị không trỏ được một thành phố cụ thể, và giả thuyết gốc Caracol còn mở)" | **làm mềm.** Price et al. 2010 chỉ kết luận "not born in the local area"; "Tikal" là nói quá (rebalance-facts §3.3, đã đọc tóm tắt bài và Helmke & Vepretskii 2022). Kết luận "bác cách đọc Teotihuacan" giữ nguyên. | https://doi.org/10.1016/j.jaa.2009.10.001 (theo rebalance-facts §3.3; tôi không mở lại) |
| 54 | Ghi chú "Vì sao Châu Mỹ bằng 0" | Ghi chú | "Teotihuacan … 100.000–200.000 dân, lớn nhất châu Mỹ tiền Columbus" | (giữ) | **giữ nguyên.** Wikipedia: "the largest and most populated center in the pre-Columbian Americas"; dân số ~100.000, ước tính cao tới 250.000. | https://en.wikipedia.org/wiki/Teotihuacan |
| 55 | CE05-12 Hiếu Văn Đế | Tư tưởng | "Nhà Tuỳ và nhà Đường kế thừa nguyên chế độ này, và Nhật Bản cùng Việt Nam về sau đều phỏng theo" | "Nhà Tuỳ và nhà Đường kế thừa chế độ này có sửa đổi, và Nhật Bản phỏng theo bản nhà Đường" | **làm mềm.** Bỏ "nguyên" và bỏ vế Việt Nam (phép quân điền Lê–Nguyễn chia ruộng công làng xã, cơ chế khác — không kiểm thêm nên bỏ chứ không viết lại). | (hạ khẳng định) |
| 56 | Ghi chú "Ứng viên mạnh đã bị loại" | Ghi chú | "…Đạo An, Tông Bính, Tạ Hách, Vương Hiến Chi, Trần Thọ: đều xứng đáng xét tới, nêu đích danh trong mục tương ứng" | bỏ Tông Bính, Tạ Hách khỏi danh sách ấy; thêm "Tông Bính và Tạ Hách từng được nêu ở mục Cố Khải Chi, nay đã rút" | sửa (mâu thuẫn nội bộ phát sinh theo thời gian). **Ngoài báo cáo** — phát hiện khi kiểm lại khẳng định E2 của CE05: hai tên này nay chỉ xuất hiện 1 lần trong ch04. | kiểm trong atlas: `grep -c` |

## 3. Cho KNOWN-ISSUES

Mục mỏng/yếu, tranh luận còn mở, hoặc độ tin cậy niên đại chưa chặt. Không phải lỗi dữ kiện đã biết, nên chưa sửa.

- **Độ tin cậy `Cao` cho năm mất là ước đoán:** `CH04-CE01-09` Josephus (mất "k. 100", `reviews/review-ch04-CE01.md` §11.2), `CH04-CE02-06` Galen (216 là suy ra; truyền thống cũ ghi 199, `review-ch04-CE02.md` §6), `CH04-CE05-09` Āryabhaṭa (550 không có nguồn tư liệu, `rebalance-ch04-b.md` D-N2). Cần một quy ước chung: Cao cho cả dòng hay chỉ cho đầu chắc.
- **Quan hệ `kế thừa` cho một quan hệ không phải kế thừa tư tưởng** (vấn đề từ vựng, không phải dữ kiện): Hillel → Giê-su nên là `tương đồng độc lập` (`review-ch04-CE01.md` §3.3); Seneca → Marcus Aurelius (§7.3); Hippocrates → Dioscorides (§10.5); Đổng Trọng Thư → Trương Hành (`review-ch04-CE02.md` §2); Constantinus ↔ Athanasius, thực tế là xung đột (`review-ch04-CE04.md` §1.6); Shapur I → Mani là "bảo trợ" mà từ vựng không có (`rebalance-ch04-a.md` Nghi-01); Thái Luân → Cưu-ma-la-thập (Nghi-02); Vasubandhu ← Cưu-ma-la-thập vẫn còn ở chiều `CH04-CE05-07 · Kế thừa từ CH04-CE04-11` (`review-ch04-CE04.md` §11.5); Pháp Hiển ← Kanishka là quan hệ "viết về" (§12.5); Rugila → Attila theo tiêu chuẩn chính chapter đặt khi gỡ cặp Quang Vũ Đế–Hai Bà Trưng (`review-ch04-CE05.md` -04 §6).
- **Vương Mãng ← Lưu Hướng `trực tiếp`:** đúng người cần trỏ là Lưu Hâm (không có mục); cặp này vẫn qua điều kiện cần của `trực tiếp` (cùng triều), nên để vòng quan hệ quyết (`review-ch04-CE01.md` §5.4).
- **Mệnh đề tối thượng đúng nhưng chưa quy thuộc:** Vương Mãng "lần đầu thiên mệnh…" (`review-ch04-CE01.md` §5.6); Philo "nỗ lực có hệ thống sớm nhất còn lại", có Sách Khôn ngoan làm phản ví dụ khả dĩ (§8.3); Ban Cố hai mệnh đề "đầu tiên/cổ nhất" (§13.2); Proclus "nỗ lực sớm nhất" (`review-ch04-CE05.md` -03 §3); Shapur II "triều dài nhất lịch sử Iran" (`review-ch04-CE04.md` §5.1); Vương Hi Chi "suốt mười bảy thế kỷ" (§7.5); Tổ Xung Chi "giữ kỷ lục lâu hơn bất kỳ kết quả tính toán nào khác thời cổ"; Julianus "phép thử rõ nhất" (đã hạ từ "duy nhất", vẫn là đánh giá).
- **Tranh luận học thuật còn mở, nên nêu ra thay vì im lặng:** "parting of the ways" ở TK 1 trong Bối cảnh CE01 (`review-ch04-CE01.md` §2); Origen bị kết án "năm 553" hay sắc chỉ 543 (`review-ch04-CE03.md` -02); Clement "thầy ông" chỉ theo Eusebius (-02); Hậu Xuất sư biểu có thể là nguỵ tác (-11); luận đề Harnack về Marcion (`review-ch04-CE02.md` §9); *Lan Đình tự* và tranh luận Quách Mạt Nhược 1965 (`review-ch04-CE04.md` §7.4); bức tranh "quốc giáo Hoả giáo ngay từ Ardashir" trong Bối cảnh CE03 (`review-ch04-CE03.md` Bối cảnh); "mười sáu năm" ở Lương Châu (384–401 cho 17, `review-ch04-CE05.md` -07 §1); "bản tụng niệm chuẩn ở Việt Nam" (-07 §3).
- **Văn mỏng / thiếu ngữ cảnh:** Josephus thiếu *Vita* và *Bác Apion* (`review-ch04-CE01.md` §11.3); Ban Chiêu thiếu *Liệt nữ truyện* (§14.7) và có thể thuộc CE02 mà Ghi chú "Nhân vật có thể thuộc thế kỷ khác" chưa ghi (§14.8); Pappus không nói quyển I đã mất (`review-ch04-CE04.md` §6.1); Athanasius không nói phần Cựu Ước của thư 367 khác quy điển nay (§2.2); Codex Argenteus chép ở Ý k. 520, cách Wulfila gần 150 năm (§3.3); Ptolemy: bản đồ Geographia không còn từ thời cổ (`review-ch04-CE02.md` §5); Tertullianô thiếu câu gốc *De carne Christi* 5.4 (§10) và nhãn lĩnh vực `Luật` dựa trên phép đồng nhất đã bị Barnes bác (§10); Āryabhaṭa: đường truyền sang Arab qua Brahmagupta (`review-ch04-CE05.md` -09 §5).
- **Ứng viên bị loại không cùng thời mà chưa "viết thẳng là không có":** Mã Quân/Vương Sung ở Trương Hành (`review-ch04-CE02.md` §2); Hero/Pappus ở Diophantus (`review-ch04-CE03.md` -08); Varāhamihira/Brahmagupta ở Āryabhaṭa (`review-ch04-CE05.md` -09 §4, đã sửa một phần); Trần Thọ/Tư Mã Bưu ở Phạm Diệp (-10 §3, có Bùi Tùng Chi cùng thời). Đây là quy tắc 5 nhưng không phải câu sai, nên để vòng bổ sung ứng viên.
- **Độ phủ** (quyết định biên tập, đã có khối Ghi chú biên tập tương ứng): Nam Á CE01, Ba Tư Sasan CE05, Đông Nam Á CE05, phụ nữ (Phùng thị, Pulcheria), quy tắc gán vùng cho Anatolia (Galen `Châu Âu` theo ngoại lệ Pergamon).
- **Sổ ghi cho vòng sau:** `rebalance-regions.md` (§A.5 và kết luận) ghi "Sihyaj K'ahk' vào Tikal ngày 15/5/378". Con số này vênh với cả `rebalance-facts.md` §3.5 (16/1) lẫn `rebalance-ch04-b.md` C3 (14/1). Đừng chép vào bất kỳ chapter nào khi chưa có bản đọc Trường kỷ kèm tương quan lịch.

## 4. Ghi chú cho vòng sau

- #17 là chỗ duy nhất tôi đổi mức bằng chứng. Lý do: quy ước điều 1 đòi tiếp xúc "chứng minh được bằng nguồn", và Wikipedia chỉ viết "seems probable". Nếu chủ dự án coi truyền thống Hán văn là đủ, có thể trả về `trực tiếp`, nhưng phải ghi rõ vào Ghi chú biên tập rằng đó là truyền thống.
- #35 dùng Barnes qua chú thích của Nicholson (1994), không mở được Barnes. Câu mới chỉ nói Maximinus Daia "từng phác ra" hệ tăng lữ ở phía đông, không nói quy mô hay kết quả.
- #36: Iranica dùng "seems to have been set under Khosrow I", nên câu mới giữ chữ "có lẽ".
- Dòng `Ảnh hưởng tới: Chuẩn hoá kinh Avesta và Hoả giáo hậu kỳ` ở Shapur II vẫn giữ. Nó là đích văn bản tự do `qua trường phái`, không khẳng định ông là người chuẩn hoá.

## 5. Kết quả kiểm tra

`python3 build.py --offline --lint-only` (chạy từ W, sau patch):

```
Lint: 0 lỗi · 6 cảnh báo · 284 ghi chú → reports/lint-chXX.txt (offline, không đối chiếu Wikidata)
```

`reports/lint-ch04.txt`: `ERROR 0 · WARN 0 · INFO 57` (trước patch cũng `WARN 0 · INFO 57`). Sáu cảnh báo toàn cục nằm ở ch01/ch10/ch11/ch90, giống trước patch; con số này có thể đổi vì các agent khác đang sửa chapter khác song song. `python3 -m pytest -q tests` → `35 passed`.
