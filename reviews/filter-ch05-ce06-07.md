# Lọc lỗi dữ kiện trong báo cáo cũ — Chapter 5, nhóm CE06 + CE07 (kèm Giới thiệu chapter)

- **Phạm vi:** `content/ch05.md` dòng 1–420 (Giới thiệu chapter, nhóm CE06, nhóm CE07) và các khối `## Ghi chú biên tập` bàn về CE06/CE07 (dòng 1076–1162). Báo cáo đã đọc: `ch05-ce06-facts.md`, `ch05-ce06-facts2.md`, `ch05-ce06-notes-review.md`, `ch05-ce06-review.md`, `ch05-ce06-slot12.md`, `ch05-ce07-facts.md`, `ch05-ce07-notes-review.md`, `ch05-ce07-review.md`, `ch05-ce07-select.md`, và Ca 4–8 + Bảng tổng kết của `tructiep-ch04-05-review.md`. Dùng thêm `ro1-nguon-ngoai-review.md` (ngoài phạm vi) làm chứng cứ cho một mục (Braulio).
- **Ngày:** 2026-11-04.
- **Chế độ:** chỉ lọc + xác minh, **không sửa file content nào** (một agent khác đang làm trên `ch05.md`). Mỗi mục `sửa`/`làm mềm` có `old_str` (chuỗi nguyên văn, đã kiểm xuất hiện **đúng một lần** trong `W/content/ch05.md` hiện tại, sha256 `e5401bd9…2662e`) và `new_str`. Bản máy đọc được: `rv/filter-ch05-ce06-07.edits.json` (16 cặp, áp tuần tự bằng `str.replace` một lần mỗi cặp).
- **Phương pháp:** lấy mọi mục NÊN / CÂN NHẮC / "PHẢI SỬA" / không nhãn mà nội dung là khẳng định dữ kiện hoặc mâu thuẫn nội bộ; mục BẮT BUỘC chỉ kiểm đã áp chưa. Đối chiếu với content hiện tại. Mục còn mở thì kiểm độc lập bằng web (SEP, Thematic Dictionary of Ancient Arabia, ORA Oxford, Wikipedia làm điểm khởi đầu). Áp thử cả 16 cặp trên một bản sao (`rv/tmp-ce0607/wk`) rồi chạy lint + test.
- **Giới hạn:** Britannica trả lỗi (Cloudflare) nên không dùng được; không mở được Pingree 1981 / Neugebauer–Pingree, Robin 2008, Barney 2006 bản in. Vì thế ba mục là `làm mềm` chứ không `sửa`. Báo cáo cũ là nguồn ứng viên, không phải bằng chứng. Hai mục mà **câu thay thế của reviewer cũ đã được áp và chính nó sai** (Bồ-đề-đạt-ma, Bối cảnh CE07) được đánh dấu riêng.

## 1. Ứng viên lọc được

Loại: **DK** = khẳng định dữ kiện · **MT** = mâu thuẫn nội bộ · **BB** = mục BẮT BUỘC (chỉ kiểm đã áp chưa).

| # | Báo cáo · mục gốc | ID | Trường | Trích ngắn (lúc báo cáo) | Loại | Trạng thái content |
|---|---|---|---|---|---|---|
| 1 | ce06-review CE06-01 P1 | CE06-01 Justinianus | Tư tưởng | hội đồng 528 "do Tribonianus đứng đầu" | BB | đã sửa trước |
| 2 | ce06-review CE06-01 P2, P3 | CE06-01 | quan hệ | Bologna / Theodosius II `trực tiếp` | DK | đã sửa trước |
| 3 | ce06-review CE06-02 P1, P2 | CE06-02 Biển Đức | Tư tưởng, quan hệ | "Ông soạn Regula" (Dunn); phòng chép `trực tiếp` vs "ngoài ý định" | DK/MT | đã sửa trước |
| 4 | ce06-review CE06-03 P1 | CE06-03 Khosrow I | quan hệ | Shapur II `trực tiếp` (122 năm) | DK | đã sửa trước |
| 5 | ce06-review CE06-04 P1 | CE06-04 Varāhamihira | ch04 Ghi chú | vẫn liệt là ứng viên bị loại | BB | đã sửa trước (`ch04.md:1045`) |
| 6 | ce06-review CE06-04 P2 | CE06-04 | Kế thừa từ | `CH04-CE02-05` (Ptolemy) cho mạch Romaka/Pauliśa tiền Ptolemy | DK | **còn nguyên** → bảng 2 |
| 7 | ce06-review CE06-04 P3 | CE06-04 | Vì sao chọn, Ảnh hưởng tới | "thiên văn Ấn Độ trước thế kỷ 5" (×2) | DK | **còn nguyên** → bảng 2 |
| 8 | ce06-review CE06-05 P1, P2 | CE06-05 Trần-na | quan hệ, Tư tưởng | Pháp Xứng tự do + `trực tiếp`; "bánh xe lý do gồm ba điều kiện" | BB/DK | đã sửa trước |
| 9 | ce06-review CE06-06 P1, P2 | CE06-06 Tùy Văn Đế | quan hệ | quân điền tự do; khoa cử `trực tiếp` vs "mầm" | DK/MT | đã sửa trước |
| 10 | ce06-review CE06-07 P1, P2 | CE06-07 Trí Di | Tư tưởng, quan hệ | "năm thời tám giáo" gán thẳng; Kumārajīva `trực tiếp` | DK | đã sửa trước |
| 11 | ce06-review CE06-08 P1 | CE06-08 Bồ-đề-đạt-ma | Ảnh hưởng tới | Huệ Năng tự do | BB | đã sửa trước |
| 12 | ce06-review CE06-08 P2 (**câu thay thế đã áp**) | CE06-08 | Vì sao chọn | "xuất thân Nam Ấn không có trong nguồn thế kỷ 6" | DK | **còn sai** (lời tựa Đàm Lâm, TK 6, ghi Nam Ấn) → bảng 2 |
| 13 | ce06-review CE06-09 P1 | CE06-09 Kaleb | Nguồn | dòng Hatke "không kiểm được" | BB | đã áp dạng rào, **nhưng rào nay sai**: mục từ điển có thật, có DOI → bảng 2 |
| 14 | ce06-review CE06-10 P1–P3 | CE06-10 Bumin | quan hệ, Nguồn, Tư tưởng | Nhu Nhiên `phản bác`; thiếu Klyashtorny; mốc 563 | BB/DK | đã sửa trước |
| 15 | ce06-review CE06-11 P1, P3 | CE06-11 Bhavavarman | Tư tưởng, `nơi:` | K.53 "ở Ba Phnom"; "thấy gắn riêng"; "vị vua đầu tiên" | DK | đã sửa trước |
| 16 | ce06-review CE06-12 P1, P2 | CE06-12 Boethius | Tư tưởng, Vì sao chọn | "đầu thế kỷ 13"; "hai lần" đã rữa | BB/DK | đã sửa trước |
| 17 | ce06-review §13 P1, P2 | Ghi chú "Một liên kết tự do…" | Ghi chú | 206/65; "lint không nhắc được" | BB | đã sửa trước |
| 18 | ce06-facts2 B1–B3 | CE06-11 | Tư tưởng, `nơi:`, Vì sao chọn | "vua sớm nhất…"; Thái Lan/Lào; "không bi ký Śaka" | BB | đã sửa trước |
| 19 | ce06-facts2 B4, B5 | CE06-12 | Tư tưởng, quan hệ | "làn sóng dịch từ tiếng Ả Rập"; Porphyry `trực tiếp` | BB | đã sửa trước |
| 20 | ce06-facts2 B6 | CE06-10 | Tư tưởng | ba chinh phục "dưới tên Mộc Hãn" | BB | đã sửa trước |
| 21 | ce06-facts2 B7 | CE06-09 | Tư tưởng | tiền đúc; "độc lập với mọi nguồn Kitô giáo" | BB | đã sửa trước |
| 22 | ce06-facts2 1a (câu thay thế) / B7 | CE06-09 | Tư tưởng | trích Sabaic dịch là "các chúa **của chúng tôi**" | DK | **còn sai** (nguồn: "their lords") → bảng 2 |
| 23 | ce06-facts2 B8–B12 | Ghi chú Bumin, Trung Á, Wikidata | Ghi chú | Sinor "bác"; Bắc sử; Trung Á 1 người; Q854920; Q705378 | BB | đã sửa trước |
| 24 | ce06-facts2 N1 | CE06-12 | Tư tưởng | "dịch và chú giải bộ Organon" (chỉ chú giải Phạm trù, Về mệnh đề) | DK | **còn nguyên** → bảng 2 |
| 25 | *(ngoài báo cáo, cùng câu với #24)* | CE06-12 | Tư tưởng | "Ông chọn không viết triết học riêng" — trong khi có sách logic riêng, Opuscula sacra, và chính mục kể Consolatio | DK/MT | **còn sai** → bảng 2 (gộp với #24) |
| 26 | ce06-facts2 N2 | CE06-12 | `nơi:` | "Rome và Pavia" (Pavia không có trong SEP) | DK | còn nguyên → giữ nguyên |
| 27 | ce06-facts2 N4 | CE06-10 | `nơi:` | Ötükän/Orkhon không đặt chính Bumin | DK | còn nguyên → giữ nguyên |
| 28 | ce06-facts2 N6 | Ghi chú "Năm 525 của Kaleb" | Ghi chú | bi ký Sabaic "quanh Najrān… do chính bên gây ra sự kiện khắc" | DK | còn nguyên → giữ nguyên |
| 29 | ce06-facts2 N8, N11, N12, N13 | CE06-09; Ghi chú | Tư tưởng, Ghi chú | chuỗi `klb…`; 26,9%; "sai ở cả bốn"; Goodall & Revire | DK | đã sửa trước |
| 30 | ce06-facts2 C4 | CE06-09 | Vì sao chọn | "lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia" | DK | còn nguyên → giữ nguyên |
| 31 | ce06-facts2 C6 | CE06-12 | Vì sao chọn | "Boethius thì tác phẩm còn nguyên vẹn" vs "bản Phân tích hậu đã mất" | MT | **còn sai** → bảng 2 |
| 32 | ce06-notes-review Khối 11 (BB) + facts2 C8/N9 + slot12 §7.2 | Ghi chú "Bốn điều không được viết về Boethius" | Ghi chú | "lăng kính đó là của ông" | BB | **chưa áp hết**: đoạn đính chính đã thêm, nhưng hai câu cũ vẫn ở cuối đoạn và đá nhau với nó → bảng 2 |
| 33 | ce06-notes-review Khối 2, 3, 6, 9, 10, 13 | Ghi chú CE06 | Ghi chú | Khúc Thừa Dụ; Ô Châu Mỹ; tiêu đề Wikidata; HAL; Trung Á; Lý Xuân Q11096818; ô lĩnh vực | BB/DK | đã sửa trước |
| 34 | ce06-notes-review Khối 11 NÊN, CÂN NHẮC (4) | Ghi chú Boethius | Ghi chú | "±25 nên lint sạch"; "điều làm nó nổi tiếng" | DK | đã sửa trước |
| 35 | ce06-notes-review Khối 11 CÂN NHẮC (2) | CE06-12 + Ghi chú | Tư tưởng | "kế hoạch dịch trọn Plato lẫn Aristotle không xong" không có trên SEP | DK | còn nguyên → giữ nguyên |
| 36 | ce06-notes-review Khối 7 (CÂN NHẮC ×3), Khối 10 (CÂN NHẮC) | Ghi chú Kaleb; CE07-09 | Ghi chú, Vì sao chọn | "ba mươi lăm năm"; nhan đề Robin; Gregory "cùng thời" ở CE07 | DK | đã sửa trước |
| 37 | ce06-facts §1–4 · ce06-slot12 §3.1, §7 (tiền-viết) | CE06-09…12 | — | "Q854920 sinh 600 mất 600"; "Aristotle của Boethius là Aristotle tới làn sóng Ả Rập"; năm 480–524 | DK | đã sửa trước hoặc không có trong content |
| 38 | ce07-review G-1 (**bản cắt đã áp**) | Bối cảnh CE07 | Bối cảnh | "Nhà Đường … quy hoạch lại kinh đô Trường An" | DK | **còn sai** (Tùy dựng Đại Hưng năm 582; Đường đổi tên năm 618) → bảng 2 |
| 39 | ce07-review 01-1, 01-2, 02-1, 02-2 | CE07-01, -02 | Tư tưởng, Vì sao chọn, quan hệ, lĩnh vực | Donner ngược; "chỉ còn qua Ibn Hisham"; Hijri `trực tiếp`; `Luật` | BB/DK | đã sửa trước |
| 40 | ce07-review 03-3 | CE07-03 Ali | Vì sao chọn | Madelung "nghiêng về phía Alid rõ nhất" | DK | đã sửa trong mục |
| 41 | ce07-notes-review Khối 8 · ce07-facts (cảnh báo quy tắc 7) | Ghi chú "Bốn nguồn phải đọc kèm cảnh báo" | Ghi chú | cùng cấp nhất "rõ nhất trong giới hiện đại" vẫn ở ghi chú | DK | **còn nguyên** → bảng 2 |
| 42 | ce07-review 04-1, 04-2, 04-3 | CE07-04 Thái Tông | Vì sao chọn, Tư tưởng | Đường luật ở why; khoa cử; "sử do triều ông soạn" | BB/DK | đã sửa trước |
| 43 | ce07-facts CE07-04 PHẢI SỬA 2 | CE07-04 | Vì sao chọn | "việc ông can thiệp vào khởi cư chú" — khởi cư chú bị Chử Toại Lương từ chối cho xem; cái ông xem và bắt chép lại là quốc sử/thực lục (643) | DK | **còn sai** → bảng 2 |
| 44 | ce07-review 05-1, 05-2, 06-1, 06-2, 06-3 | CE07-05, -06 | nhiều | Võ Tắc Thiên nguồn; quý tộc tây bắc; 629/627; độ tin cậy; `trực tiếp` | BB/DK | đã sửa trước |
| 45 | ce07-facts CE07-05 PHẢI SỬA 2 | CE07-05 | Tư tưởng | "người phụ nữ duy nhất … xưng hoàng đế theo đúng nghĩa" | DK | còn nguyên → giữ nguyên |
| 46 | ce07-review 07-1 · ce07-facts CE07-07 | CE07-07 Huệ Năng | Tư tưởng, Vì sao chọn | "bộ duy nhất … gọi là kinh"; Hồ Thích/McRae | DK | đã sửa trước |
| 47 | ce07-review 08-1 | CE07-08 Brahmagupta | Vì sao chọn | "dấu vết trong mạch toán học Ả Rập … rõ nhất" | DK | còn nguyên → giữ nguyên |
| 48 | ce07-facts CE07-08 · ce07-review 08-1 | CE07-08 | Tư tưởng | "khoảng năm 770"; Bakhshali | DK | đã sửa trước |
| 49 | ce07-review 09-1, 09-2, 09-3 · ce07-facts CE07-09 | CE07-09 Isiđôrô; CE06-04 | Vì sao chọn, Tư tưởng | "Pappus và Wulfila"; Gregory; "sắp theo truy nguyên từ"; "hơn một nghìn"; 20 quyển | BB/DK | đã sửa trước (cả CE06-04) |
| 50 | ce07-review 09-4 | CE07-09 | Tư tưởng | "Braulio, học trò ông" | DK | còn nguyên → giữ nguyên |
| 51 | ce07-facts CE07-09 (2) · ro1 | Ghi chú "Bốn mệnh đề bị vòng kiểm sự kiện bác" | Ghi chú | "việc chia hai mươi quyển là do Braulio" — mục nay ghi "con số hai mươi có lẽ của khâu sao chép" | MT | **còn sai** → bảng 2 |
| 52 | ce07-review 10-1, 10-2, 10-3, 10-4 | CE07-10 Pháp Xứng | Tư tưởng, quan hệ, Vì sao chọn, Nguồn | apoha "của ông"; `trực tiếp`; "tám thế kỷ"; URL SEP | BB/DK | đã sửa trước |
| 53 | ce07-review 11-1, 11-2, 11-4 | CE07-11 Tùng Tán Cán Bố | Tư tưởng, Nguồn, độ tin cậy | công chúa; Old Tibetan Annals từ 650; độ tin cậy | BB/DK | đã sửa trước |
| 54 | ce07-review 11-3 (BB) | CE07-11 ↔ CE07-04 | quan hệ (hai đầu) | `tương đồng độc lập` cho một cặp có hôn nhân triều đình 641 | BB/MT | **áp sai**: chỉ đổi mức sang `trực tiếp`, loại vẫn khẳng định "không tiếp xúc" (`lint.py:265`) → bảng 2 |
| 55 | ce07-review 12-1, 12-2, 12-3 | CE07-12 Pakal | Tư tưởng, Nguồn, Vì sao chọn | "rơi vào cây vũ trụ"; Tiesler; "dày nhất" | DK | đã sửa trước |
| 56 | ce07-notes-review Khối 2–7, 9, 10 (10 BB + NÊN) | Ghi chú CE07 | Ghi chú | lint mù; CE08 trước/sau; 24-3/29-8; Đông Nam Á, Trung Á %; 629; Lý Tự Tiên; 46/47; sáu ngày | BB/DK | đã sửa trước |
| 57 | ce07-notes-review Khối 8 | Ghi chú "Bốn nguồn…" | Ghi chú | Bodleian lùi niên đại Bakhshali "tháng 10/2024 … 799–1102" | DK | còn nguyên → giữ nguyên |
| 58 | ce07-select §0.1, §4, §5 · tructiep Ca 5–8 | CE07-12, CE07-11; CE06-09/-10/-11, CE07-12 | wikidata, Tư tưởng, quan hệ | Q311215 con bướm; Thönmi; bốn đích hỗn hợp `trực tiếp` | BB/DK | đã sửa trước |
| 59 | tructiep Ca 7 (khuyến nghị kèm) | CE06-11 | Tư tưởng | phả hệ Īśānavarman I: cha là Mahendravarman, không phải Bhavavarman | DK | đúng sẵn (mục ghi "cùng cha ông Vīravarman và Citrasena-Mahendravarman", không nói Īśānavarman là con ông) |
| 60 | *(ngoài báo cáo)* | Giới thiệu chapter | Giới thiệu | "chữ viết lần đầu xuất hiện … ở quần đảo Mã Lai" | DK | **còn sai** (bi ký Kutai nửa sau TK 4) → bảng 2 |

## 2. Quyết định cho mục còn sai / còn mở

`old_str` là chuỗi nguyên văn trong `W/content/ch05.md` hiện tại, mỗi chuỗi xuất hiện đúng một lần. Ở E6, E8, E9, E14 chuỗi gồm cả khoảng trắng đầu hoặc ký tự xuống dòng cuối (`\n`), xem bản JSON.

| # | Edit | ID | Trường | old_str (verbatim) | new_str | Quyết định | Bằng chứng |
|---|---|---|---|---|---|---|---|
| 1 | E1 | Giới thiệu chapter *(ngoài báo cáo)* | Giới thiệu | `Cùng lúc, chữ viết lần đầu xuất hiện trên thảo nguyên Turk, ở Tây Tạng và ở quần đảo Mã Lai.` | `Cùng lúc, chữ viết lần đầu xuất hiện trên thảo nguyên Turk và ở Tây Tạng, còn tiếng Mã Lai lần đầu thành văn bản.` | **sửa.** Bi ký cổ nhất quần đảo là bi ký yupa Kutai, nửa sau TK 4, tức trước khung 501–1000. Cái mới của giai đoạn này là tiếng Mã Lai cổ lần đầu thành văn bản (Sojomerto, Kedukan Bukit, TK 7). Không ghi năm 682 vì trang dẫn chỉ cho "TK 7". | https://en.wikipedia.org/wiki/Sanskrit_inscriptions_in_Maritime_Southeast_Asia · https://en.wikipedia.org/wiki/Old_Malay |
| 2 | E2 | Bối cảnh CE07 | Bối cảnh | `Nhà Đường mở thời Trinh Quán và quy hoạch lại kinh đô Trường An.` | `Nhà Đường mở thời Trinh Quán ở kinh đô Trường An, tức thành Đại Hưng do nhà Tùy dựng.` | **sửa.** Câu này là bản cắt mà ce07-review G-1 đề xuất, và chính nó gán sai: Tùy Văn Đế dựng Đại Hưng năm 582, Đường đổi tên thành Trường An năm 618 ở cùng vị trí. Nhà Đường không quy hoạch lại thành. Cũng khớp `nơi:` của CE06-06 ("Đại Hưng, nay là Tây An"). Bối cảnh sau sửa 59 chữ. | https://en.wikipedia.org/wiki/Chang%27an |
| 3 | E3 | `CH05-CE06-08` Bồ-đề-đạt-ma | Vì sao chọn | `xuất thân Nam Ấn không có trong nguồn thế kỷ 6 mà đến từ nguồn muộn hơn.` | `xuất thân Nam Ấn đến từ lời tựa Nhị nhập tứ hạnh luận, không từ nguồn năm 547.` | **sửa** (reviewer cũ sai). Lời tựa của Đàm Lâm (506–574) cho *Nhị nhập tứ hạnh luận* là nguồn TK 6 và gọi ông là "người Nam Thiên Trúc". Còn *Lạc Dương già lam ký* (547) gọi ông là người Tây Vực, gốc Ba Tư. Câu mới giữ ý "Nam Ấn không đến từ nguồn 547". why = 104 chữ, đúng trần. `nơi:` ("Nam Ấn Độ, rồi Lạc Dương…") nay khớp với văn xuôi, không cần đổi. | https://en.wikipedia.org/wiki/Bodhidharma (mục "Tanlin", "Luoyang") |
| 4 | E4 | `CH05-CE06-12` Boethius | Tư tưởng | `Ông chọn không viết triết học riêng mà đổ gần cả đời vào việc dịch và chú giải bộ Organon của Aristotle sang Latinh.` | `Ông đổ phần lớn sức lực vào việc dịch bộ Organon của Aristotle sang Latinh và chú giải phần đầu của nó.` | **sửa.** SEP: ông viết "logical text-books on division, categorical syllogisms…" và bốn *Theological Treatises*; chính mục kể *Consolatio*. Vậy "chọn không viết triết học riêng" sai. Ông chú giải *Categories* (1) và *On Interpretation* (2), không chú giải cả *Organon* (facts2 N1). Câu sau ("Lựa chọn ấy…") vẫn nối được. ideas 128 chữ. | https://plato.stanford.edu/entries/boethius/ |
| 5 | E5 | `CH05-CE06-12` | Vì sao chọn | `Boethius thì tác phẩm còn nguyên vẹn.` | `Boethius thì các tác phẩm chính còn nguyên vẹn.` | **sửa** (mâu thuẫn nội bộ). Chính Tư tưởng cùng mục nói "bản Phân tích hậu đã mất". SEP: "except for that of the Posterior Analytics, which was lost". why 103 chữ. | https://plato.stanford.edu/entries/boethius/ · kiểm trong atlas |
| 6 | E6 | Ghi chú "Bốn điều không được viết về Boethius" | Ghi chú | ` Ông mang sang cho thời trung cổ cả những biến dạng Tân Plato của bộ Aristotle, và chính ông lặp lại tham vọng của Porphyry là chứng minh Plato với Aristotle hoà hợp. Tức châu Âu trung cổ đọc Aristotle **qua lăng kính Tân Plato**, và lăng kính đó là của ông.` (kèm dấu cách đầu) | *(xoá)* | **sửa** (BB chưa áp hết). ce06-notes-review Khối 11 cho đoạn thay thế, và đoạn ấy đã được chèn vào. Nhưng hai câu cũ vẫn ở cuối, nên đoạn vừa nói "lăng kính … là Porphyry, kéo về phía Aristotle" vừa nói "lăng kính Tân Plato … là của ông". SEP (Marenbon): các bình luận của ông "because more Porphyrian, so more Aristotelian". Xoá hai câu, không thay. | https://plato.stanford.edu/entries/boethius/ |
| 7 | E7 | `CH05-CE07-04` Đường Thái Tông | Vì sao chọn | `việc ông can thiệp vào khởi cư chú vẫn được chép.` | `việc ông đòi đọc quốc sử triều mình vẫn được chép.` | **sửa** (ce07-facts PHẢI SỬA 2 chưa áp). Chử Toại Lương, người giữ ký chú, từ chối cho ông xem. Năm 643 ông đòi đọc quốc sử Phòng Huyền Linh soạn và bắt chép lại biến cố Huyền Vũ môn cho đủ. Ông không "can thiệp vào khởi cư chú". Cùng số chữ (why 104). | https://en.wikipedia.org/wiki/Chu_Suiliang · https://en.wikipedia.org/wiki/Fang_Xuanling |
| 8 | E8 + E9 | `CH05-CE07-04` (Ảnh hưởng tới) ↔ `CH05-CE07-11` (Kế thừa từ) | quan hệ (hai đầu) | E8 (dòng 279, trong CE07-04): `- CH05-CE07-11 · tương đồng độc lập · trực tiếp\n` · E9 (dòng 393, trong CE07-11): `- CH05-CE07-04 · tương đồng độc lập · trực tiếp\n` | *(xoá cả hai dòng)* | **làm mềm** (BB 11-3 áp sai). `tương đồng độc lập` khẳng định không có tiếp xúc (`atlaslib/lint.py:265`, `prompts/atlas-prompt.md:79`). Nhưng chính Tư tưởng CE07-11 kể nhà Đường gả công chúa Văn Thành (641, thời Thái Tông), và sứ Tạng tới triều Đường từ 634. Không thay bằng `kế thừa` vì chiều vay mượn thể chế chưa kiểm được (ce07-review 11-3 (b)). Sau khi xoá: CE07-04 còn 2 dòng Ảnh hưởng tới, CE07-11 còn 1 dòng Kế thừa từ, cả hai hợp lệ. | https://en.wikipedia.org/wiki/Princess_Wencheng · kiểm trong atlas |
| 9 | E10 | `CH05-CE06-09` Kaleb | Tư tưởng | `gọi thẳng "các chúa của chúng tôi, những vua Aksum"` | `gọi thẳng "các chúa của họ, những vua Aksum"` | **sửa** (trích dẫn dịch sai). Hatke: "their lords, the kings of the Aksumites" (ʾmrʾ-hmw ngs²t ʾks¹mn), hậu tố -hmw là "của họ". | https://ancientarabia.huma-num.fr/dictionary/definition/aksum-arabia-and |
| 10 | E11 | `CH05-CE06-09` | Nguồn | `George Hatke, mục "Aksum", trong *A Thematic Dictionary of Ancient Arabia* — **dòng trích này chưa giải được**: không tìm thấy bản ghi nào ở OpenLibrary lẫn Crossref, và dòng không có NXB, năm, trang hay URL, nên không được dùng để đỡ mệnh đề nào cho tới khi có bản trích đầy đủ;` | `George Hatke, "Aksum [and South Arabia]" và "Kālēb (r. ca. 510–540 CE)", *Thematic Dictionary of Ancient Arabia* (ấn bản trực tuyến 2023), doi 10.60667/tdaa-0005 và 10.60667/tdaa-0059;` | **sửa.** Rào hiện tại (từ ce06-review BB 5) nay sai: cả hai mục từ điển có thật, có DOI, và tự trang ghi cách dẫn như trên. Hai mục đỡ đúng các mệnh đề của thân mục (vương hiệu RIÉth 191, con Tāzēnā, tên ʾƎlla ʾAṣbəḥā, mùa xuân 529) và của khối ghi chú "Năm 525 của Kaleb". Không thêm số trang Drewes & Schneider như facts2 2b đề xuất, vì chưa kiểm. | https://ancientarabia.huma-num.fr/dictionary/definition/aksum-arabia-and · https://ancientarabia.huma-num.fr/dictionary/definition/kaleb |
| 11 | E12 | Ghi chú "Bốn mệnh đề bị vòng kiểm sự kiện bác…" | Ghi chú | `và việc chia hai mươi quyển là do Braulio làm sau chứ không phải Isiđôrô)` | `và việc chia quyển là do Braulio làm sau chứ không phải Isiđôrô, còn con số hai mươi có lẽ của khâu sao chép)` | **sửa** (mâu thuẫn nội bộ). Mục `CH05-CE07-09` đã được sửa theo Barney 2006 n. 56 ("it seems that Braulio divided the work into fifteen books; the division into twenty books developed during the course of the manuscript diffusion"), nhưng ghi chú vẫn khẳng định trần là hai mươi. Câu mới lấy đúng chữ của mục. Wikipedia vẫn ghi 20, nên giữ chữ "có lẽ". | `reviews/ro1-nguon-ngoai-review.md` (trích Barney, PDF CUP) · https://en.wikipedia.org/wiki/Etymologiae |
| 12 | E13 | Ghi chú "Bốn nguồn phải đọc kèm cảnh báo (quy tắc 7)" | Ghi chú | `Madelung 1997 là chuyên khảo nghiêng về phía Alid rõ nhất trong giới hiện đại,` | `Madelung 1997 là chuyên khảo đọc nghiêng về phía Alid,` | **làm mềm.** Mục `CH05-CE07-03` đã bỏ cấp nhất này theo ce07-review 03-3 (không có bài điểm sách nào xếp hạng như vậy), nhưng ghi chú vẫn giữ. Chiều thiên Alid thì vẫn giữ. | ce07-review 03-3 · kiểm trong atlas (`CH05-CE07-03` Vì sao chọn) |
| 13 | E14 | `CH05-CE06-04` Varāhamihira | Kế thừa từ | `- CH04-CE02-05 · kế thừa · qua trường phái\n` | `- Thiên văn Hy Lạp qua các bộ Romaka và Pauliśa · kế thừa · qua trường phái\n` | **làm mềm.** Mục nêu mạch Hy Lạp qua Romaka/Pauliśa, không nhắc Ptolemy một chữ. Theo hướng nghiên cứu Pingree–Neugebauer, phần Hy Lạp trong *Pañcasiddhāntikā* là tiền Ptolemy. Tôi **không** mở được Pingree 1981 để xác nhận thay bằng `CH03-BCE02-03` Hipparchus. Hipparchus cũng đã đủ 3 dòng Ảnh hưởng tới, nên không đối xứng được. Vì thế bỏ ID Ptolemy và chỉ giữ đúng điều văn xuôi đỡ. Lint mất 1 INFO đối xứng. | kiểm trong atlas (Tư tưởng cùng mục; `ch03.md` Hipparchus) · ce06-review CE06-04 P2 [KHÔNG KIỂM ĐƯỢC] |
| 14 | E15 + E16 | `CH05-CE06-04` | Vì sao chọn; Ảnh hưởng tới | `phần lớn thiên văn Ấn Độ trước thế kỷ 5 biến mất khỏi tầm với` · `- Hiểu biết hiện đại về thiên văn Ấn Độ trước thế kỷ 5 · kế thừa` | `phần lớn thiên văn Ấn Độ trước thời ông biến mất khỏi tầm với` · `- Hiểu biết hiện đại về thiên văn Ấn Độ trước Varāhamihira · kế thừa` | **làm mềm.** Năm hệ ông tóm là các bộ "đang lưu hành ở Ấn Độ thời ông" (chính Tư tưởng cùng mục). Chưa kiểm được niên đại soạn của từng bộ, nên mốc "trước thế kỷ 5" không có cơ sở. "Trước thời ông" đúng theo định nghĩa, không thêm mốc mới. | kiểm trong atlas · ce06-review CE06-04 P3 |

### Mục giữ nguyên (content đúng, hoặc reviewer không đứng)

| # | ID | Trường | Câu hiện tại | Lý do giữ | Bằng chứng |
|---|---|---|---|---|---|
| G1 | `CH05-CE06-12` | `nơi:` | "Rome và Pavia" | Ông bị giam ở Pavia và chôn ở San Pietro in Ciel d'Oro (Pavia). SEP không nêu địa danh, nhưng không mâu thuẫn. | https://en.wikipedia.org/wiki/Boethius |
| G2 | `CH05-CE06-12` + Ghi chú | Tư tưởng | "Kế hoạch dịch trọn Plato lẫn Aristotle thì không xong" | SEP có nói: "a wider project … translate and comment on all the writings of Plato and Aristotle". Reviewer (notes-review Khối 11) tìm sai cụm. | https://plato.stanford.edu/entries/boethius/ |
| G3 | `CH05-CE06-10` | `nơi:` | "cao nguyên Mông Cổ, núi Ötükän (都斤山) và lưu vực Orkhon" | Chu thư chép nha trướng khả hãn ở 都斤山; đây là nơi hoạt động, không khẳng định nơi sinh. facts2 N4 là đề xuất chính xác hoá, không phải lỗi. | ce06-facts2 N4 (đọc chính văn) |
| G4 | Ghi chú "Năm 525 của Kaleb" | Ghi chú | bi ký Sabaic "quanh Najrān … do chính bên gây ra sự kiện khắc" | Vị trí (Bir Ḥimā gần Najrān), niên đại 633 và tên Yūsuf đều đúng (facts2 (5) A, C, E). Ja 1028 có nhắc Najrān. Ghi chú không nói các bi ký chép trực tiếp cuộc tàn sát. Sắc thái của Hatke đưa xuống KNOWN-ISSUES. | ce06-facts2 §(5) D |
| G5 | `CH05-CE06-09` | Vì sao chọn | "Đây là lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia" | facts2 C4 tự ghi "Mệnh đề *lần cuối* không sai"; chỉ mốc kết thúc (Abraha tới k. 570) chưa được nói. Đưa xuống KNOWN-ISSUES. | https://ancientarabia.huma-num.fr/dictionary/definition/aksum-arabia-and |
| G6 | `CH05-CE07-09` | Tư tưởng | "Braulio, học trò ông" | Barney gọi "his disciple Braulio", và Braulio học ở trường của Isiđôrô. Đề xuất 09-4 sai. | `reviews/ro1-nguon-ngoai-review.md` (trích Barney) |
| G7 | `CH05-CE07-08` | Vì sao chọn | "dấu vết trong mạch toán học Ả Rập đời sau rõ nhất" | Văn xuôi đã hạ chuyện 772/773 xuống giai thoại. Câu so sánh giới hạn "trong các tác giả siddhānta", và lời khuyên của 08-1 (dùng dạng "có dấu vết") đã được áp. Không có bằng chứng ngược. | ce07-review 08-1 |
| G8 | `CH05-CE07-05` | Tư tưởng | "người phụ nữ duy nhất … xưng hoàng đế theo đúng nghĩa" | ce07-facts xếp "Nhẹ" và tự xác nhận câu đúng; "theo đúng nghĩa" đã loại hai ca biên (528, 653). | ce07-facts CE07-05 |
| G9 | Ghi chú "Bốn nguồn…" | Ghi chú | Bodleian lùi niên đại Bakhshali "tháng 10/2024 … 799–1102" | ORA Oxford: Chivall et al., "Radiocarbon dating of the Bakhshālī manuscript", ngày 14-10-2024. Dải 799–1102 nằm trong PDF, notes-review Khối 8 đã đọc. | https://ora.ox.ac.uk/objects/uuid:5a6d1dd7-f20c-4209-adb6-33849f5b08f4 |

Không edit nào chạm dòng `năm:`, nên không có dòng Wikidata mới cho Ghi chú biên tập.

## 3. Cho KNOWN-ISSUES (mỏng/yếu/chưa kiểm, không sửa ở lượt này)

- `CH05-CE06-09` Kaleb: "lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia". Thời Ethiopia cai trị Ḥimyar kéo tới k. 570 dưới Abraha, người đã tự trị khỏi Aksum. Câu chưa nói điều đó. `reviews/ch05-ce06-facts2.md #1f / C4`.
- `CH05-CE06-09`: "dựng vua bù nhìn" (số ít), trong khi Hatke ghi hai vua bù nhìn (Maʿdīkarib Yaʿfur 518, Sumūyafaʿ Ashwaʿ 529). Hatke cũng tự vênh giữa PAN 2023 (525) và từ điển (529). `reviews/ch05-ce06-facts2.md #(4).4, #2e`.
- Ghi chú "Năm 525 của Kaleb": theo Hatke, nhóm Ja 1028 / Ry 507 / Ry 508 chép chiến dịch Ẓafār và phong toả bờ biển, còn cuộc tàn sát Najrān thì không bi ký Sabaic nào chép trực tiếp. Phép quy đổi 633 HE → 523 có bản cho 524. `reviews/ch05-ce06-facts2.md #(5) B, D`.
- `CH05-CE06-11` Bhavavarman: "chính là khuôn mà Īśānapura rồi Angkor kế tục" là mệnh đề tổng hợp, không nguồn nào được dẫn phát biểu. Heng & Lavy chỉ có URL trần. `reviews/ch05-ce06-facts2.md #C2, #C3`.
- `CH05-CE06-04`: nếu mở được Pingree 1981 hoặc Neugebauer–Pingree, xét nối lại một ID Hy Lạp (Hipparchus `CH03-BCE02-03`, nhưng mục ấy đã đủ 3 dòng Ảnh hưởng tới) thay cho dòng tự do E14. `reviews/ch05-ce06-review.md #4 P2`.
- `CH05-CE06-06` Tùy Văn Đế: "Khai Hoàng luật năm 583" bỏ mất bản 581. `reviews/ch05-ce06-review.md #6 P3`.
- Nhóm CE06: bốn mục (CE06-09, -10, -11) không nêu đích danh ứng viên bị loại ở Vì sao chọn (lệch template §5). CE06-12 nay đã nêu. `reviews/ch05-ce06-review.md #9 P2, #11 P2`.
- Nhiều trường ideas sát trần 130 (CE06-09 129, CE06-12 128, CE07-04 127), nên mọi rào thêm phải cắt chỗ khác. `reviews/ch05-ce06-review.md` "Trần chữ".
- `CH05-CE07-03` Ali: Tư tưởng không chứa đóng góp nào của chính ông, và thiếu mắt xích Nahrawān (658). `reviews/ch05-ce07-review.md #03-1` · `reviews/ch05-ce07-facts.md` CE07-03 (2).
- `CH05-CE07-07` Huệ Năng: chưa ghi niên đại bản Đôn Hoàng (k. 780; chép k. 830–860), và người truyền y bát (Hoằng Nhẫn) không được nêu tên. `reviews/ch05-ce07-facts.md` CE07-07 (2) · `reviews/ch05-ce07-review.md #07-2`.
- `CH05-CE07-08` Brahmagupta: khai `Khoa học tự nhiên` + `Vũ trụ` mà không có chữ nào về thiên văn. Có một lỗi dấu câu ("chỗ trống: Ông cũng nêu…"). Cảnh báo Plofker/Bakhshali chưa vào mục. `reviews/ch05-ce07-review.md #08-2, #08-3` · `reviews/ch05-ce07-notes-review.md` Khối 8.
- `CH05-CE07-01` Muhammad: không nêu tên ứng viên bị loại; con số "CE07 12/12" ở khối ghi chú 44 nên là 11/12 hoặc 10/12. `reviews/ch05-ce07-review.md` "Hai nhận xét ở tầng nhóm".
- `CH05-CE07-12` Pakal: mục không nhắc tranh luận tuổi thọ (bi ký 80 / xương 40–50). Tiesler & Cucina chỉ đứng ở trường Nguồn. `reviews/ch05-ce07-review.md #12-2`.
- `CH05-CE07-11`: sau khi gỡ E8/E9, cặp Thái Tông – Tùng Tán Cán Bố không còn cạnh nào. Nếu có nguồn cho chiều ảnh hưởng (hôn nhân 641, phong tước 649) thì nối lại bằng `kế thừa`. `reviews/ch05-ce07-review.md #11-3 (b)`.
- Ghi chú "HTTP 200…": "một thread diễn đàn trả 202" không nêu URL nên không kiểm lại được. `reviews/ch05-ce06-notes-review.md` Khối 9.
- Ghi chú D5 CE07: câu "không ai trong hai người vượt được bốn tiêu chí ở thang toàn nhân loại" bị lặp hai lần trong cùng khối (văn, không phải dữ kiện). `content/ch05.md` khối "Ứng viên Việt Nam trong nhóm CE07".

## 4. Kết quả kiểm tra (áp thử trên bản sao, không chạm `W/`)

Áp cả 16 cặp trong `rv/filter-ch05-ce06-07.edits.json` lên bản sao `rv/tmp-ce0607/wk` (`python3 ../edits.py content/ch05.md write`, mỗi `old_str` đếm đúng 1 lần):

- `python3 build.py --offline --lint-only` → `Lint: 0 lỗi · 6 cảnh báo · 283 ghi chú`. Trước khi áp là `0 lỗi · 6 cảnh báo · 284 ghi chú`: không có WARN mới, mất đúng 1 INFO (dòng đối xứng `CH05-CE06-04 ↔ CH04-CE02-05`, do E14).
- `reports/lint-ch05.txt` → `ERROR 0 · WARN 0 · INFO 33`.
- Số chữ sau khi áp: CE06-08 why 104 · CE06-12 ideas 128 / why 103 · CE07-04 why 104 · Bối cảnh CE07 59 · Giới thiệu chapter 129 (đều trong ngưỡng cảnh báo).
- `python3 -m pytest -q tests` → `35 passed`.
- `W/content/ch05.md` không bị sửa (sha256 trước và sau lượt này: `e5401bd9339ac1095e050e5ef7dc6873c0f585946d485f112c5917438bf2662e`). Nếu agent kia đổi file trước khi áp, chạy lại phép đếm `old_str` trước.

## Tóm tắt số

Ứng viên lọc được: 60 dòng (gom từ khoảng 140 mục gốc). Đã sửa trước hoặc đúng sẵn: 36 (35 đã sửa trước, #59 đúng sẵn). Còn mở: 24 dòng, gồm 22 từ báo cáo và 2 ngoài báo cáo (#25 Boethius "chọn không viết triết học riêng", #60 Giới thiệu chapter). Quyết định: **sửa 10** (E1–E7, E10–E12, phủ 11 dòng ứng viên vì E4 gộp #24 và #25; trong đó E2 và E3 là câu thay thế của reviewer cũ tự nó sai) · **làm mềm 4** (E8+E9, E13, E14, E15+E16) · **giữ nguyên 9** (G1–G9). Tổng cộng 16 cặp old/new.
