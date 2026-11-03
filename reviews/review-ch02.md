# Đánh giá độc lập — Chapter 2 · Thời kỳ Trục (800–401 TCN)

**Người rà soát:** agent độc lập, không viết chapter này.
**Ngày:** 2026-10-30
**Phạm vi:** toàn bộ 33 mục, 4 nhóm (BCE08 ×7, BCE07 ×6, BCE06 ×10, BCE05 ×10), theo CONTRIBUTING.md §"Quy trình một chapter", bước 8.

---

## Kết luận

**CÔNG BỐ ĐƯỢC SAU KHI SỬA** — không cần làm lại.

Phần văn xuôi vững hơn mức tôi dự đoán: phần lớn các khẳng định kiểm được đều đúng, và những chỗ dễ bịa nhất (số mảnh đất sét Nineveh, độ dài Đường Hoàng gia, số quy tắc Aṣṭādhyāyī, năm dựng vở *Người Ba Tư*, các trích dẫn Aristotle và Herodotus) đều chính xác. 33/33 Q-ID đúng người, 21/21 sách có thật với đúng tác giả–nhan đề–năm.

Vấn đề tập trung ở **tầng trích nguồn**, đúng như CONTRIBUTING cảnh báo: 5 mục Nguồn hỏng hoặc sai tên, trong đó một nguồn hoàn toàn không nói gì về nhân vật nó được gán cho. Thêm 3 lỗi sự kiện và một lỗ hổng tuyển chọn rõ rệt (Sappho).

**Số phát hiện:** Sai 8 · Đáng ngờ 10 · Nên sửa 15.

Ba mục nghiêm trọng nhất: **S1** (nguồn SEP gán cho Solon không nhắc Solon một chữ nào), **S6** (Tử Sản được nêu là "cùng thời" với Quản Trọng — lệch 100 năm, làm sụp cả lập luận chọn), **N1/N12** (độ phủ: chapter không có người nữ nào, bỏ sót Sappho, và bỏ sót Sennacherib, Baudhāyana, Croesus — những người mạnh hơn các mục châu Âu yếu nhất đang được chọn).

---

## SAI — phải sửa trước khi commit

### S1 · CH02-BCE06-08 (Solon) — nguồn chính không hề nhắc tới Solon

> `**Nguồn:** Stanford Encyclopedia of Philosophy, "Ancient Political Philosophy" (https://plato.stanford.edu/entries/ancient-political/); Aristotle, Athenaion Politeia, 5–12.`

URL phân giải bình thường (HTTP 200), nhưng **chữ "Solon" không xuất hiện một lần nào** trong bài lẫn trang `notes.html` của nó. Bài của Melissa Lane bàn Socrates, Plato, Aristotle, các trường phái Hy Lạp hoá và Cicero; không có seisachtheia, không có bốn hạng công dân theo thu nhập, không có quyền khởi kiện thay người bị hại — tức không có bất kỳ điều gì mục này khẳng định. Đây là trích nguồn trang trí đúng nghĩa.

Nguồn thứ hai (*Ath. Pol.* 5–12) thì **đúng và có hỗ trợ**: chương 7 nêu nguyên bốn hạng *pentakosiomedimnoi / hippeis / zeugitai / thetes*.

**Sửa:** bỏ mục SEP, thay bằng Plutarch, *Solon*, hoặc M. L. West, *Iambi et Elegi Graeci* tập II (chứa chính thơ Solon).

### S2 · CH02-BCE07-03 (Uddālaka Āruṇi) — mục Britannica không tồn tại

> `Britannica, mục "Uddalaka Aruni"`

Britannica **không có** mục độc lập cho nhân vật này. Ông chỉ xuất hiện bên trong `/topic/Hinduism/The-Upanishads` và `/topic/tat-tvam-asi`.

**Sửa:** dẫn thẳng hai bài topic đó, hoặc bỏ hẳn — Olivelle (*The Early Upaniṣads*, đã dẫn ở cùng mục) là nguồn đủ và đúng.

### S3 · CH02-BCE07-02 (Quản Trọng) — mục Britannica không tồn tại

> `Britannica, mục "Guan Zhong"`

Không có mục độc lập. Quản Trọng chỉ được nhắc trong `/biography/Huangong` (Tề Hoàn Công) và `/place/Qi-ancient-state-China-771-221-BCE`.

**Sửa:** dẫn "Huangong", hoặc dựa hẳn vào Rickett (đã dẫn).

### S4 · CH02-BCE06-04 (Mahāvīra) — sai tên mục Britannica

> `Britannica, mục "Mahavira"`

Mục chính của Britannica mang tên **"Vardhamāna"** (`/biography/Vardhamana`). "Mahavira" chỉ tồn tại ở kids.britannica (bản Students), không phải bài chính.

### S5 · CH02-BCE05-09 (Tôn Tử) — sai tên mục Britannica

> `Britannica, mục "Sunzi"`

Mục chính mang tên **"Sun Tzu"** (`/biography/Sun-Tzu`). "Sunzi" cũng chỉ là bài Students.

### S6 · CH02-BCE07-02 (Quản Trọng) — Tử Sản không hề cùng thời

> `**Vì sao chọn:** Ứng viên cùng thời là Tử Sản nước Trịnh, người công bố hình thư trên đỉnh đồng […] trong khi cải cách của Tử Sản chỉ còn trong sử liệu.`

**Quản Trọng mất năm 645 TCN. Tử Sản (Công Tôn Kiều) sống k. 581–522 TCN, làm chấp chính nước Trịnh 543–522 TCN, đúc hình thư năm 536 TCN.** Hai người cách nhau khoảng 100–125 năm; Tử Sản sinh ra sau khi Quản Trọng chết hơn sáu mươi năm. Toàn bộ phép so sánh dựng trên một tiền đề sai.

Bằng chứng: Wikipedia "Zichan", dẫn *Tả truyện* — "In 536 BCE Zheng state had its penal statutes inscribed on a bronze tripod cauldron".

**Lưu ý:** cũng chính Tử Sản được nêu trong CH02-BCE06-01 (Khổng Tử) là "cùng thời" — ở đó thì **đúng** (Khổng Tử sinh 551, Tử Sản mất 522, hai người có giao thoa và Luận ngữ có ghi Khổng Tử khen Tử Sản). Chỉ mục Quản Trọng sai.

**Sửa:** thay bằng ứng viên thật sự cùng thời — ví dụ Tề Hoàn Công (đã nêu) và Bào Thúc Nha, hoặc Tấn Văn Công, bá chủ kế tiếp.

### S7 · CH02-BCE07-06 (Jeremiah) — năm mất sai, và mâu thuẫn với chính văn xuôi của mục

> `năm: k. 645–587 TCN`
> `**Tư tưởng:** Ngôn sứ chứng kiến Jerusalem thất thủ năm 587 TCN.`

Trường `năm:` đặt năm mất đúng bằng năm Jerusalem thất thủ, nhưng Jeremiah **sống sót qua biến cố đó**: sách Jeremiah 40–44 kể ông được quân Babylon thả, ở lại Mizpah, rồi bị đưa sang Ai Cập cùng thư ký Baruch và sống nốt phần đời ở đó. Niên đại tiêu chuẩn là **k. 650 – k. 570 TCN**, mất ở Ai Cập, không có ghi chép xác thực về cái chết.

Wikidata Q158825 cũng ghi P570 = −587, nên **lint online sẽ không bắt được lỗi này** — đây là ví dụ cho thấy khớp Wikidata không đồng nghĩa với đúng.

**Sửa:** `năm: k. 650–k. 570 TCN` (hoặc `hoạt động k. 627–585 TCN` nếu muốn bám bước 1 của sách).

### S8 · Ghi chú biên tập — quan hệ Psamtik I ↔ Piye bị đảo ngược

> `Taharqa, Psamtik I, Sargon II, Nebuchadnezzar II: các vua cùng thời bị loại vì kế thừa mô hình do Piye và Tiglath-Pileser III tạo ra.`

Psamtik I (664–610 TCN) **không kế thừa mô hình của Piye** — ông lập vương triều 26 (Sais) bằng cách hất người Kush ra khỏi Ai Cập, ban đầu dưới ô của Assyria rồi tự lập. Ông là người chấm dứt vương triều 25, không phải người nối tiếp nó. Taharqa thì đúng là kế thừa Piye; Nebuchadnezzar II kế thừa mô hình Assyria ở mức lỏng.

**Sửa:** tách Psamtik I ra và nêu lý do loại thật (ông thuộc TK 7, và đóng góp là phục hưng Sais/mở cửa cho lính đánh thuê Hy Lạp, không trùng trục nào của chapter).

---

## ĐÁNG NGỜ — không kiểm chứng được hoặc nói quá so với đồng thuận

### D1 · CH02-BCE06-04 (Mahāvīra) — anekāntavāda và syādvāda là phát triển về sau

> `Ba đóng góp lan ra ngoài phạm vi Jaina: […] thuyết anekāntavāda […]; và syādvāda, lối phát biểu có điều kiện kèm theo.`

Giới nghiên cứu xem **syādvāda / saptabhaṅgī (thất cú) là phát triển muộn**, không phải giáo lý của chính Mahāvīra. Hệ biện chứng cổ điển được Umāsvāti, Siddhasena Divākara và Mallavādin củng cố rồi Samantabhadra đưa thành dạng hoàn chỉnh — tức khoảng TK 2–6 CN, sau Mahāvīra 700–1000 năm. anekāntavāda ở dạng mầm thì khả tín hơn (có nguồn gọi nó là giáo lý nền tảng của Mahāvīra), nhưng dạng học thuyết có tên gọi và cấu trúc thì không.

**Sửa:** giữ ahiṃsā là đóng góp của ông; chuyển anekāntavāda/syādvāda sang dạng "truyền thống Jaina về sau khai triển từ lập trường của ông".

### D2 · CH02-BCE06-07 (Cyrus) — khẳng định tính nguyên bản vượt đồng thuận

> `Cyrus được chọn theo tính nguyên bản (c) […]: mô hình đế chế đa sắc tộc dựa trên khoan dung thiết chế là của ông, Darius chỉ hệ thống hoá.`

Phần văn xuôi xử lý Trụ Cyrus **đúng** (chỉ nói nó ghi việc phục hồi đền thờ Babylon, không gọi nó là "tuyên ngôn nhân quyền" — tốt). Nhưng luận điểm (c) thì đi quá: Amélie Kuhrt và trường phái theo bà lập luận rằng việc phục hồi tượng thần và cho dân bị đày hồi hương là **công cụ hành chính quy ước của đế chế Lưỡng Hà, không phải sáng tạo của Cyrus**, và hình ảnh "khoan dung" phần lớn là sản phẩm của tuyên truyền trên Trụ cộng với tiếp nhận Kinh Thánh.

**Sửa:** hạ xuống "ông vận dụng ở quy mô chưa từng có" thay vì "là của ông".

### D3 · CH02-BCE08-07 ↔ CH02-BCE07-03 — thứ tự Yajnavalkya / Uddālaka ngược truyền thống

> BCE08-07: `năm: hoạt động k. 750–700 TCN`
> BCE07-03: `năm: hoạt động k. 700–650 TCN`
> BCE07-03: `Yajnavalkya được xếp trước theo tính nguyên bản (c)`

Truyền thống (danh sách truyền thừa *vaṃśa* trong Bṛhadāraṇyaka và các cảnh tranh biện) đặt **Uddālaka Āruṇi là thầy của Yājñavalkya**, không phải ngược lại. Chapter xếp Yajnavalkya sớm hơn một nhóm thế kỷ và tự nói thẳng rằng việc xếp trước là **theo tiêu chí nguyên bản** — nhưng quy tắc của dự án là xếp nhóm **theo floruit**, không theo xếp hạng nguyên bản.

Thêm nữa: Olivelle — nguồn được dẫn cho cả hai mục — đặt Bṛhadāraṇyaka và Chāndogya vào khoảng TK 7–6 TCN, nên **nguồn được dẫn không hỗ trợ việc đặt Yajnavalkya ở TK 8 TCN**.

**Sửa:** hoặc đưa cả hai về BCE07, hoặc đảo thứ tự, và bỏ câu biện minh bằng tiêu chí (c) khỏi lập luận xếp nhóm.

### D4 · CH02-BCE05-07 (Mặc Tử) — "duy nhất" nói quá

> `truyền thống lập luận hình thức duy nhất bản địa trước khi Phật giáo đưa nhân minh vào`

Danh gia (名家 — Đặng Tích, Doãn Văn, Huệ Thi, Công Tôn Long) là một truyền thống bản địa riêng về danh–thực, thường được xếp cạnh Hậu Mặc gia chứ không đồng nhất với nó.

**Sửa:** "truyền thống lập luận hình thức bản địa sớm nhất và hệ thống nhất".

### D5 · CH02-BCE08-06 (Piye) — "toàn bộ Ai Cập" và "lập vương triều 25"

> `chinh phục Ai Cập đang chia rẽ và lập vương triều thứ 25 — lần duy nhất một thế lực hạ Sahara cai trị toàn bộ Ai Cập`

Hai chỗ nhẹ tay hơn thì chính xác hơn: (i) sau chiến dịch k. 727 TCN, Piye nhận sự quy phục của các vua Đồng bằng rồi **rút về Napata**; Tefnakht chỉ nhận thua bằng thư và từ chối đích thân triều kiến, và quyền kiểm soát Hạ Ai Cập phải đợi Shabaka mới thành thực chất. (ii) Kashta, người tiền nhiệm của Piye, thường được tính là vua đầu của vương triều 25.

**Đã kiểm và đúng:** niên đại trị vì 744–714 TCN ✓; bia chiến thắng Gebel Barkal 159 dòng, "among the longest, most detailed, and most literarily accomplished royal texts in Egyptian history" ✓ — khẳng định "một trong những văn bản tự sự dài nhất còn lại bằng chữ tượng hình" đứng vững.

### D6 · CH02-BCE08-02 ↔ CH02-BCE07-04 — hai lần "người đầu tiên" chỏi nhau

> BCE08-02 (Hesiod): `đây cũng là văn bản Hy Lạp đầu tiên nói ở ngôi thứ nhất về đời sống riêng của tác giả`
> BCE07-04 (Archilochus): `ông mở ra lối viết lấy cái tôi cụ thể làm trung tâm […] ông là người đầu tiên đặt kinh nghiệm cá nhân […] làm đề tài hợp lệ của thơ`

Khẳng định về Hesiod **đã kiểm và đúng** ("his is the first distinctively individual voice in European literature… He is the first Greek poet to have done so"). Nhưng chapter rồi lại trao danh hiệu tương tự cho Archilochus, người đến sau. Hai mục cạnh nhau trong cùng một chapter không nên cùng là "người đầu tiên".

**Sửa:** phân biệt rõ — Hesiod là ngôi thứ nhất trong sử thi giáo huấn; Archilochus là cái tôi trong thơ trữ tình đơn ca/iambic, kể cả kinh nghiệm đáng xấu hổ.

### D7 · CH02-BCE05-10 (Darius I) — "hai mươi satrapy" cần ghi nguồn

> `chia hai mươi satrapy có định mức cống nạp cố định`

Con số 20 là của **Herodotus III.89** (đơn vị thu thuế). Bia Behistun của chính Darius liệt kê **23 xứ**, và số satrapy dao động 20–28 trong suốt triều đại.

**Sửa:** "theo Herodotus là hai mươi khu thuế".

### D8 · CH02-BCE05-10 (Darius I) — "khoảng một tuần" hơi ngắn

> `cho phép tin tức đi từ Susa tới Sardis trong khoảng một tuần`

Con số chuẩn rút từ Herodotus là **chín ngày** cho trạm ngựa (so với chín mươi ngày đi bộ).

**Đã kiểm và đúng:** "dài hơn hai nghìn cây số" ✓ — Đường Hoàng gia ≈ 2.699 km.

### D9 · CH02-BCE07-05 (Dracon) — niên đại lệch một năm, và Ath. Pol. 4 cần cảnh báo

> `năm: hoạt động k. 622–621 TCN`

Niên đại chuẩn là **621/620 TCN** (năm chấp chính Aristaechmus); chính OCD ghi "Draco, lawgiver, c. 624–621/0 bce".

Ngoài ra, *Ath. Pol.* chương 4 ("hiến pháp Dracon": quyền công dân theo hoplite, Hội đồng 401 người bốc thăm) **bị phần lớn giới nghiên cứu coi là nguỵ tạo đời sau**. Dẫn nó ngang hàng với chương 7 mà không chú thích là cho nó quá nhiều trọng lượng. Chương 7 thì đúng và hữu dụng ("they ceased to observe the ordinances of Draco, except those relating to homicide").

### D10 · CH02-BCE06-04 (Mahāvīra) — độ tin cậy niên đại không nhất quán với Đức Phật

> Mahāvīra: `k. 599–527 TCN | độ tin cậy niên đại: Trung bình`
> Đức Phật: `k. 563–483 TCN (niên đại dài; niên đại ngắn: k. 480–400 TCN) | độ tin cậy niên đại: Thấp`

Niên đại Mahāvīra bị tranh cãi bởi **đúng cuộc tranh luận niên đại dài/ngắn đó**: Wikidata Q9422 mang song song cả 599–527 lẫn 540–468. Đức Phật được để "Thấp" kèm ghi chú; Mahāvīra để "Trung bình" không ghi chú gì.

**Sửa:** hạ xuống "Thấp" và thêm biên độ thứ hai, cho nhất quán.

---

## NÊN SỬA — lập luận yếu, mất cân đối, lỗi quy ước

### N1 · Sappho bị bỏ sót hoàn toàn — và chapter không có người nữ nào

`grep` toàn file: **"Sappho" không xuất hiện một lần nào** — không phải mục, cũng không nằm trong danh sách ứng viên bị loại ở Ghi chú biên tập. Trong 33 nhân vật, **không có một phụ nữ nào**, và Ghi chú biên tập không nhắc tới chuyện đó một chữ.

Sappho (k. 630–570 TCN) đáp ứng cả bốn tiêu chí: (a) phạm vi — một trong Chín nhà thơ trữ tình của kinh điển Alexandria, Plato gọi là "Nàng Thơ thứ mười"; (b) độ bền — truyền liên tục qua Catullus, Ovid, tới Byron, Shelley và văn học hiện đại, "influence on Western poetry out of all proportion to their brevity"; (c) nguyên bản — thơ trữ tình đơn ca ngôi thứ nhất, thể Sapphic mang tên bà. Về độ bền bà **mạnh hơn Archilochus**, người đã được chọn.

Floruit của bà rơi vào **nhóm BCE07, nhóm đang chỉ có 6/10 người**. Tức là không phải đánh đổi với ai cả — có sẵn bốn chỗ trống.

Đây là lỗ hổng tuyển chọn rõ nhất **bên trong vùng châu Âu** (xem N12 cho các lỗ hổng ngoài châu Âu). Tối thiểu, bà phải được nêu đích danh trong danh sách "Ứng viên mạnh đã bị loại" kèm lý do thật — và nếu lý do là "không đủ chỗ" thì nó không đứng được, vì nhóm BCE07 còn trống bốn chỗ.

Lưu ý thêm: việc chapter có 0 người nữ mà Ghi chú biên tập **không nhắc tới một chữ** là vấn đề riêng, độc lập với việc có thêm Sappho hay không. Cho giai đoạn này, số lượng ứng viên nữ có nguồn quả thật rất ít — nhưng đó là một **phát hiện phải viết ra**, không phải một khoảng lặng.

### N2 · CH02-BCE06-09 (Zarathustra) — "Vì sao chọn" không nêu ứng viên bị loại nào

> `Không có ứng viên cùng vùng nào tương đương về ảnh hưởng.`

Quy tắc của dự án đòi nêu đích danh 1–2 ứng viên được cân nhắc và bị loại. Mục này không nêu ai, dùng toàn bộ đoạn để bàn vấn đề niên đại. Nếu quả thật không có nhân vật nào cùng vùng được định danh bằng nguồn, thì **nói ra điều đó như một phát hiện** ("không có cá nhân nào khác ở đông Iran TK 6 TCN được nguồn đương thời định danh"), đừng viết như một khẳng định trống.

### N3 · Mức bằng chứng "trực tiếp" bị dùng sai ở ba quan hệ

- **CH02-BCE05-03 (Herodotus)** `Kế thừa từ: CH02-BCE06-08 · kế thừa · trực tiếp` — và chiều ngược lại ở mục Solon. Solon mất k. 558 TCN, Herodotus sinh k. 484 TCN: không thể có quan hệ trực tiếp. Solon là **nhân vật trong tác phẩm** (Hist. I.29–33), nên mức đúng là "qua trường phái".
- **CH02-BCE07-04 (Archilochus)** `Kế thừa từ: CH02-BCE08-01 · phản bác · trực tiếp` — phản ứng văn học suy ra từ nội dung thơ, nên là "suy đoán học giả".
- **CH02-BCE07-01 (Ashurbanipal)** `Kế thừa từ: CH02-BCE08-05 · kế thừa · trực tiếp` — cách nhau ~80 năm và khác dòng (Sargonid); là liên tục thiết chế, không trực tiếp.

### N4 · Gán vùng cho Zarathustra không nhất quán

> `nơi: đông Iran hoặc Trung Á | vùng: Trung Á`

Cyrus và Darius, cũng Iran, được gán `Trung Đông/Bắc Phi`. Zarathustra là **mục Trung Á duy nhất của cả chapter**, và việc gán đó vừa đúng lúc nâng số vùng của nhóm BCE06 lên 5. Không phải lỗi chặn build, nhưng nên thống nhất một quy ước và nói rõ lý do.

### N5 · Nhóm BCE07 chỉ có 6/10 trong khi BCE06 và BCE05 đầy

Ghi chú biên tập loại Heraclitus với lý do "nhóm BCE06 đã đủ 10" và gọi đó là "mục loại gây tiếc nhất". Trong khi đó TK 7 TCN bỏ trống bốn chỗ. Ngoài Sappho, TK 7 còn Nabopolassar, Taharqa, Periander, Alcman, Terpander, Zaleucus chưa được cân nhắc công khai. Nên hoặc lấp chỗ, hoặc nói rõ vì sao TK 7 TCN thưa nhân vật đủ chuẩn.

### N6 · CH02-BCE07-02 (Quản Trọng) — câu về Diêm thiết luận đọc ra nghĩa sai

> `mô hình tài chính được nhà Hán tái lập và tranh luận suốt hai nghìn năm trong Diêm thiết luận`

*Diêm thiết luận* ghi lại **một cuộc tranh luận năm 81 TCN**. Câu hiện tại đọc như thể cuộc tranh luận kéo dài hai nghìn năm bên trong văn bản đó.

**Sửa:** "…được nhà Hán tái lập, và tranh luận quanh nó — mở đầu bằng *Diêm thiết luận* năm 81 TCN — còn kéo dài suốt hai nghìn năm."

### N7 · CH02-BCE06-06 (Pythagoras) — một câu chưa được rào như các câu khác

> `chứng minh qua quan hệ giữa độ dài dây đàn và cao độ`

Câu chuyện dây đàn/búa là truyền thuyết (bản búa còn sai về vật lý), và Burkert — chính nguồn được dẫn — là người hoài nghi tiêu biểu về mọi quy công cho cá nhân Pythagoras. Mục đã rào rất tốt ở câu cuối ("Tiểu sử bị truyền thuyết phủ dày nên mọi quy công cho cá nhân ông đều phải dè dặt"); chỉ cần kéo cái rào đó phủ lên câu này.

### N8 · CH02-BCE05-02 (Parmenides) — hai nguồn đều là SEP

> `Stanford Encyclopedia of Philosophy, "Parmenides"; Stanford Encyclopedia of Philosophy, "Presocratic Philosophy".`

Mỏng cho một mục đưa ra khẳng định counterfactual mạnh ("chính thách thức của ông […] định hình chương trình nghị sự của toàn bộ triết học Hy Lạp sau đó"). Thêm một nguồn khác loại — Barnes (đã dùng ở mục Democritus) hoặc Coxon, *The Fragments of Parmenides*.

### N9 · Vệ sinh trích dẫn

- Mục SEP slug `presocratics` có **nhan đề là "Presocratic Philosophy"**, không phải "Presocratics" — chapter ghi đúng rồi, giữ nguyên.
- `Encyclopaedia Iranica, mục "Zoroaster"` là một **mục hợp thành nhiều phần** (i. The Name, ii. General Survey, iii. In the Avesta…). Nên dẫn đích danh tiểu mục.
- `W. Allyn Rickett, Guanzi (Princeton, 1985)` là **tập I**; tập II là 1998. Ghi rõ tập nếu năm 1985 mang trọng lượng.
- `George Cardona, Pāṇini: His Work and Its Traditions (1997)` là **tập I, bản sửa lần 2**; bản đầu 1988.
- `The Oxford Handbook of the Prophets (2016)` thiếu chủ biên — **Carolyn J. Sharp**, OUP, 2016.

### N10 · CH02-BCE06-10 (Anaximander) và CH02-BCE06-05 (Thales) dùng chung một nguồn SEP

Cả hai đều dẫn `"Presocratic Philosophy"` làm nguồn thứ nhất. Hợp lệ, nhưng khi hai mục liền kề cùng dựa vào một bài tổng quan thì nguồn thứ hai (Aristotle *Met.* A3 và Kahn 1960) đang gánh toàn bộ sức nặng. Không phải lỗi, chỉ là điểm yếu nên biết.

### N11 · CH02-BCE07-01 (Ashurbanipal) — lĩnh vực "Sử học" hơi gượng

Ông là người **bảo tồn** tri thức, không phải người viết sử theo nghĩa Herodotus. "Giáo dục" (lĩnh vực vừa được Owner bổ sung) hoặc chỉ "Chính trị/Nhà nước" có lẽ sát hơn. Không chặn build.

### N12 · Bốn ứng viên ngoài châu Âu mạnh hơn các mục châu Âu yếu nhất, và không mục nào được nêu là đã cân nhắc

Rà soát có hệ thống các vùng ngoài châu Âu trong cửa sổ 800–401 TCN cho ra bốn cái tên không hề xuất hiện trong chapter — cả ở thân bài lẫn ở danh sách "Ứng viên mạnh đã bị loại":

- **Sennacherib** (Assyria, trị vì 705–681 TCN) — hệ kênh dẫn nước ~50 km từ Khinis về Nineveh, trong đó **cầu máng đá Jerwan** (k. 703–690 TCN, khoảng 2 triệu khối đá đẽo) là công trình cùng loại cổ nhất được biết ở bất kỳ đâu; tái thiết Nineveh thành đô thị lớn nhất thế giới đương thời. Bằng chứng xuất sắc: bi ký hoàng gia có niên đại của chính ông, bi ký xây dựng tại chỗ ở Jerwan, di tích vật chất, phù điêu Khinnis, cộng đối chứng ngoài (Kinh Thánh, Berossus, Herodotus). **Đây là mục bỏ sót mạnh nhất của chapter** — và lưu ý chapter đã có hai vua Assyria rồi, nên vấn đề không phải "thiếu chỗ cho Lưỡng Hà" mà là chọn nhầm người cho tiêu chí Kỹ thuật/Công nghệ.
- **Baudhāyana** (Ấn Độ, k. 800–700 TCN, Toán học) — *Baudhāyana Śulbasūtra* chứa phát biểu bằng lời sớm nhất còn lại của định lý "Pythagoras" ở dạng tổng quát, các phép dựng bàn thờ, biến đổi hình tròn–hình vuông, và xấp xỉ √2 ≈ 577/408 (đúng tới năm chữ số thập phân). **Mục này làm chapter tự mâu thuẫn:** mục Pythagoras đã tự viết "Định lý mang tên ông đã được biết trước ở Babylon và Ấn Độ" — tức thừa nhận truyền thống đó tồn tại — rồi không chọn ai đại diện cho nó, trong khi vẫn chọn Pāṇini trên **đúng loại bằng chứng ấy** (văn bản truyền nguyên vẹn, tác giả theo quy ước truyền thống, niên đại theo tầng ngôn ngữ).
- **Croesus** (Lydia, trị vì k. 560–546 TCN, Kinh tế) — tiền Croeseid đúc ở Sardis k. 550 TCN là **tiền đúc vàng ròng và bạc ròng chuẩn hoá đầu tiên theo tỉ giá lưỡng kim cố định**, thay cho electrum pha không đều. Cyrus giữ nguyên hệ này và tiếp tục đúc Croeseid ở Sardis tới k. 520 TCN; nó là tổ tiên trực tiếp của daric/siglos Achaemenid — tức của chính đồng daric mà mục Darius I ca ngợi. Chapter nói "Hy Lạp chuyển sang… tiền đúc" ở phần Bối cảnh BCE07 rồi không chọn ai cho bước đó. **Anatolia có 0/33 mục.**
- **Hezekiah xứ Judah** (trị vì k. 715–687 TCN) — tập trung phụng tự về Jerusalem (bước khiến độc thần giáo trở nên khả thi về mặt thiết chế), hệ bình LMLK, đường hầm Siloam dài 533 m kèm bi ký tiếng Hebrew cổ. Bằng chứng thuộc loại tốt nhất trong số các cá nhân vùng Levant: ấn bulla cá nhân khai quật ở Ophel (2009–10, công bố 2015), bi ký Siloam, lăng trụ của chính Sennacherib nêu tên ông. **Được chứng thực tốt hơn Josiah — người chapter có nêu là đã loại — và tốt hơn phần lớn các ngôn sứ được chọn.**

Karib'il Watar bin Dhamar'alī (Saba, Yemen, đầu TK 7 TCN, bi ký RES 3945) ngang ngửa Piye chứ không hơn; Deng Xi (鄧析, mất 501 TCN) ngang Dracon chứ không hơn. Hai người này tôi **không** đề nghị thêm.

### N13 · Ngưỡng tuyển chọn bất đối xứng: giữ Dracon nhưng loại Tử Sản

Ghi chú biên tập loại Tử Sản với lý do "xếp sau Quản Trọng, Mặc Tử và Tôn Tử theo độ bền". Nhưng hình thư đúc trên đỉnh đồng của Tử Sản (536 TCN) được chứng thực **tốt hơn** luật Dracon — *Tả truyện* ghi đương thời, so với Dracon chỉ còn một điều khoản qua bi ký khắc lại năm 409/8 TCN và tường thuật của Aristotle/Plutarch sau nhiều thế kỷ — và hệ quả thì tương đương: công bố luật thành văn, tước độc quyền diễn giải của quý tộc. Giữ Dracon mà loại Tử Sản là **dấu hiệu rõ nhất của một ngưỡng không áp đồng đều cho hai vùng**.

Tương tự, Homer được giữ dù tính lịch sử bị tranh cãi ở mức ít nhất ngang với những nhân vật Đông Á mà chapter loại vì "chỉ là tên gắn với một truyền thống".

### N14 · Tiêu chí "cá nhân được định danh" tự nó thiên vị Hy Lạp — và chapter không nói ra điều đó

Con số 42,4% không chỉ là kết quả của lựa chọn, mà một phần là **sản phẩm của phương pháp**. Hy Lạp cổ phong và cổ điển phát triển tập quán ký tên tác phẩm, cộng với cả một ngành tiểu sử–doxography (Diogenes Laertius, Plutarch) **sản xuất ngược ra các cá nhân được định danh**, cộng với truyền bản Byzantine liên tục. Trong khi đó học thuật Lưỡng Hà, văn chương minh triết Ai Cập, biên tập Deuteronomy ở Israel, biên soạn Vệ Đà–Upanishad và kinh điển lễ nhạc Trung Hoa đều quy cho **trường phái, dòng truyền thừa, hoặc không ai cả**.

Hệ quả cụ thể: tác giả của MUL.APIN và của chuỗi *Astronomical Diaries* Babylon — một kho quan trắc liên tục có niên đại từ **652 TCN**, không có đối ứng Hy Lạp nào — tính điểm bằng không vì vô danh. Deutero-Isaiah vô danh. *Tả truyện* vô danh (chapter đúng khi không chọn Tả Khâu Minh). Zapotec ở Monte Albán có Stela 12–13 (k. 500 TCN) ghi lễ đăng quang của một người tên "8 Water" — **cá nhân được định danh sớm nhất ở Tây bán cầu** — nhưng ngoài sự kiện đăng quang thì không biết gì thêm, nên Châu Mỹ 0 mục là **giới hạn tư liệu thật, không phải lỗi tuyển chọn**.

Đây là điều **phải được nói thẳng trong chapter**, không nên để nó lặng lẽ tan vào một con số phần trăm. Phần "Ứng viên Việt Nam" đã làm đúng việc này cho một trường hợp; cần một đoạn tương tự ở cấp chapter.

### N15 · Đánh giá trung thực về con số 42,4%

**Không đứng vững ở mức đó.** Con số trung thực nằm quanh **30–35%**.

Cụ thể: thêm Sennacherib, Baudhāyana, Croesus và Hezekiah, đồng thời bỏ Dracon và Archilochus (hoặc gộp Homer + Hesiod thành một mục về truyền thống sử thi cổ phong), sẽ đưa chapter về khoảng **12/35 ≈ 34%**. Vẫn cao — và ở mức đó thì tôi cho là **bảo vệ được**: Hy Lạp giai đoạn 600–401 TCN thật sự có mật độ đổi mới trí tuệ quy được cho cá nhân một cách bất thường. Nhưng 42,4% thì vượt quá mức tư liệu còn lại chống đỡ được.

Ba chỗ hụt cụ thể, theo thứ tự nghiêm trọng: **Anatolia (0 mục, không bào chữa được khi có tiền đúc Lydia)** · **Lưỡng Hà thiếu đúng một người, là Sennacherib** · **truyền thống toán học–nghi lễ Ấn Độ (chọn Pāṇini, bỏ Baudhāyana)**.

---

## ĐÃ KIỂM, ĐÚNG

Đây là phần tôi thực sự đối chiếu và thấy không có vấn đề.

**Wikidata — 33/33 đúng người.** Không có trùng tên, không có mục sách thay cho tác giả, không có tượng. Đáng chú ý: `Q37151` đúng là **Tôn Vũ con người** (không phải *Binh pháp*, vốn là một Q-ID khác). `Q2724299` nhãn "Aruni", mô tả "Vedic sage" — đúng Uddālaka Āruṇi. Trường `năm:` khớp P569/P570 trong dung sai đã khai báo cho toàn bộ 33 mục; các mục `Thấp` được lint bỏ qua đúng theo thiết kế.

**Ghi chú biên tập về Wikidata — chính xác từng chi tiết.** Đã xác minh: Isaiah `Q188794` và Jeremiah `Q158825` có `P31 = Q20643955` (nhân vật Kinh Thánh) và **không** có `Q5`; Mahāvīra `Q9422` có `P31 = Q1077817, Q21070568`, cũng **không** có `Q5`. Và `Q35811` (Zoroaster) quả thật ghi **P569 = −628, P570 = −551**, đúng như ghi chú nói.

**`atlaslib/common.py` — khớp với Ghi chú biên tập.** `FIELDS` có đủ 16 mục và **có** cả `"Giáo dục"` lẫn `"Ngôn ngữ học"`; `Pāṇini` dùng `"Ngôn ngữ học, Triết học"` hợp lệ.

**Nguồn sách — 21/21 có thật, đúng tác giả, nhan đề, nhà xuất bản, năm.** Lord 1960 (Harvard) · West *Theogony* 1966 (Clarendon) · West *IEG* 1971–72 · Blenkinsopp *Isaiah 1–39* AB19 2000 · Radner 2015 · Török 1997 (Brill, HdO I/31) · Olivelle 1998 · Rickett 1985 · Holladay *Jeremiah 1* 1986 / *Jeremiah 2* 1989 (Hermeneia) · Henricks 2000 (Columbia) · Gombrich 2009 (Equinox) · Dundas 2002 (Routledge, ấn bản 2) · Burkert 1972 (Harvard) · Briant 2002 (Eisenbrauns) · Boyce 1979 · Kahn 1960 (Columbia) · Nutton 2013 (Routledge, ấn bản 2) · Barnes 1982 · Fraser 2016 (Columbia) · Cardona 1997 · Mair 2007 (Columbia).

**URL SEP — 10/10 phân giải, đúng mục** (`confucius`, `laozi`, `buddha`, `presocratics`, `pythagoras`, `ancient-political`, `parmenides`, `socrates`, `democritus`, `mohism`). Cảnh báo ở CONTRIBUTING đã được tuân thủ: chapter dùng **`mohism`** chứ không phải `mozi`, và **không** bịa slug `thales`, `anaximander`, `herodotus`, `hippocrates` — bốn nhân vật đó được dẫn qua OCD/Britannica/`presocratics`. (Vấn đề duy nhất của nhóm URL là nội dung của `ancient-political`, xem S1.)

**OCD — 6/6 mục tồn tại:** Homer, Hesiod, Archilochus, Draco, Herodotus, Aeschylus.

**Britannica — 11/15 mục tồn tại đúng tên:** Amos, Isaiah, Tiglath-pileser III, Piye, Yajnavalkya, Ashurbanipal, Jeremiah, Cyrus the Great, Hippocrates, Panini, Darius I. (Bốn mục còn lại: xem S2–S5.)

**Trích dẫn văn bản cổ — 3/3 đúng:**
- *Ath. Pol.* 4 mở bằng "in the archonship of Aristaechmus, Draco enacted his ordinances"; ch. 7 có cả việc Solon bãi luật Dracon trừ tội giết người **và** bốn hạng tài sản. ✓
- *Poetics* 1449a đúng là chỗ nói Aeschylus nâng số diễn viên từ một lên hai, thu hẹp dàn đồng ca, và Sophocles đưa diễn viên thứ ba. ✓
- Herodotus III.38 đúng là giai thoại Darius – người Hy Lạp – người Callatiae, kết bằng câu Pindar "tập tục là vua của tất cả". ✓

**Các khẳng định sự kiện đã đối chiếu và đúng:**
- Amos là **ngôn sứ đầu tiên có sách mang tên mình** ✓ ("no earlier instance of a literary prophet is known").
- Isaiah là **sách ngôn sứ được trích nhiều nhất trong Tân Ước** ✓ (câu được rào đúng vào "sách ngôn sứ" — Thánh vịnh mới là sách Cựu Ước được trích nhiều nhất nói chung).
- Thư viện Nineveh: **"hơn ba mươi nghìn mảnh"** ✓ (British Museum đếm 30.943); cháy **612 TCN** ✓; khai quật **từ 1849** ✓ (Layard, cuối 1849); **Esarhaddon là cha ông** ✓; giữ **bản Gilgamesh đầy đủ nhất** ✓.
- Tiglath-Pileser III **trị vì 745–727 TCN** ✓.
- Piye **744–714 TCN** ✓; bia chiến thắng nằm trong nhóm văn bản tự sự dài nhất của Ai Cập ✓ (159 dòng).
- Hesiod là **người Hy Lạp đầu tiên nói ngôi thứ nhất về đời mình** ✓.
- Archilochus **k. 680–645 TCN** ✓ (khớp chính xác Wikidata); nhịp iambic thành nhịp đối thoại của kịch Athens ✓; Horace tự nhận kế thừa ✓.
- Dracon: từ nguyên "hà khắc" ✓; chỉ luật giết người sống sót (bia khắc lại 409/8 TCN) ✓.
- Solon **được trao quyền năm 594 TCN** ✓ (niên đại chính thống 594/3).
- Bản Quách Điếm **khai quật 1993** ✓.
- Cuộn Isaiah Biển Chết **TK 2 TCN** ✓.
- Aeschylus: *Người Ba Tư* dựng **472 TCN, tám năm sau Salamis (480)** ✓; **diễn viên thứ hai** ✓; Oresteia kết bằng việc lập toà Areopagus ✓.
- Đức Phật: lệch **gần tám mươi năm** giữa niên đại dài và ngắn ✓ (563 vs 480 = 83).
- Mahāvīra là **tổ thứ 24**, Pārśvanātha là tổ 23 ✓.
- *tat tvam asi* là **một trong bốn đại cú (mahāvākya)** ✓; *neti neti* và học thuyết nghiệp đúng là của Yajnavalkya trong Bṛhadāraṇyaka ✓.
- Pāṇini: **khoảng bốn nghìn quy tắc** ✓ (3.959 sūtra); "sớm hơn hai mươi lăm thế kỷ" ✓ theo niên đại TK 5 TCN.
- Đường Hoàng gia **hơn 2.000 km** ✓ (≈2.699); **Behistun ba thứ tiếng** ✓, là chìa khoá giải mã chữ hình nêm ✓; Darius **sinh k. 550, lên ngôi 522, mất 486** ✓.
- Thales: nhật thực **585 TCN** ✓ và được rào đúng là "truyền thống gán cho ông"; Aristotle coi ông là người khởi đầu triết học ✓.
- Anaximenes quay về **mô hình trái đất phẳng trên không khí** ✓.
- Định lý Pythagoras **đã biết trước ở Babylon và Ấn Độ** ✓.
- Zichan/Tử Sản đúng là **cùng thời với Khổng Tử** ở mục BCE06-01 ✓ (chỉ mục Quản Trọng sai — xem S6).

**Các ứng viên ngoài châu Âu tôi đã kiểm và thấy chapter loại/bỏ qua là ĐÚNG** (nêu ra để Owner khỏi phải tự rà lại):
- **Biển Thước (扁鵲)** — không định niên đại được. Tiểu sử trong *Sử ký* trải các giai thoại từ k. 501 tới k. 310 TCN, khoảng 190 năm; "Biển Thước" là danh hiệu của một thầy thuốc thần thoại cổ hơn được dùng như tên hiệu/tên phái. Không đạt ngay tiêu chí định danh.
- **Tả Khâu Minh (左丘明)** — quy thuộc đã bị học giả đời Đường (Triệu Khuông) bác, đồng thuận hiện nay xem *Tả truyện* là biên soạn vô danh đầu Chiến Quốc. Tác phẩm đủ chuẩn, cái tên thì không.
- **Sư Khoáng (師曠)** — chỉ còn giai thoại khuyên răn, không tác phẩm, không đổi mới kỹ thuật quy được.
- **Naburimannu và Kidinnu** — niên đại "fl. 491 TCN" cho Naburimannu đến từ Strabo và Pliny chứ không từ nguồn Babylon; Hệ A được chứng thực từ cuối TK 5–4 TCN, Kidinnu k. 400–350 TCN. Nằm ngoài hoặc ở rìa cửa sổ. Loại đúng.
- **Hanno nhà hàng hải** — tiếng Hy Lạp của *Periplus* mang đặc điểm hậu cổ điển; một khối học thuật đáng kể định niên đại văn bản còn lại vào TK 2–1 TCN và nghi ngờ cả tính lịch sử của chuyến đi.
- **Bimbisāra và Ajātaśatru** — quan trọng thật, nhưng niên đại dao động trọn một thế kỷ giữa niên đại dài và ngắn, nguồn đều là kinh điển Phật–Jaina không có bi ký đương thời.
- **Shabaka** — từ Junge (1973) quan điểm chủ đạo xem Thần học Memphis là sáng tác phỏng cổ đời vương triều 25 chứ không phải văn bản Cổ vương quốc được cứu, nên lập luận "người bảo tồn minh triết cổ" yếu đi. Xếp dưới Piye — chapter chọn đúng.
- **Kapila, Pakudha Kaccāyana, Sañjaya Belaṭṭhiputta** — Kapila không định niên đại được; hai người kia chỉ còn bốn dòng biếm hoạ trong một nguồn Phật giáo thù địch duy nhất (*Sāmaññaphala Sutta*). Yếu hơn cả Gosāla, người chapter đã loại.
- **Châu Mỹ và Triều Tiên** — rà kỹ, kết quả là **số không về tư liệu thật, không phải lỗi tuyển chọn**: Chavín và Olmec không để lại tên người đọc được; Đàn Quân là truyền thuyết, Vệ Mãn thuộc TK 2 TCN.
- **Midas và Gyges** (Anatolia) — có niên đại vững (Mita trong thư tịch Sargon II; gò Gordion MM định niên đại vòng cây 740 TCN; Gugu trong biên niên Ashurbanipal) nhưng không có đóng góp quy được ngoài việc lập triều, và phủ truyền thuyết dày.

**Cấu trúc và độ phủ:**
- Đếm nhóm: BCE08 = 7, BCE07 = 6, BCE06 = 10, BCE05 = 10, **tổng 33** ✓ khớp phần Giới thiệu; không nhóm nào vượt trần 10.
- Châu Âu **14/33 = 42,4%** ✓ đúng con số được nêu.
- Độ phủ **≥ 4 lĩnh vực và ≥ 3 vùng mỗi nhóm**: đạt ở cả bốn nhóm. BCE08 — 5 lĩnh vực / 4 vùng; BCE07 — 7 / 4; BCE06 — 6 / 5; BCE05 — 8 / 4.
- Không mục nào quá 2 lĩnh vực hoặc 2 câu hỏi lớn; mọi giá trị đều nằm trong từ vựng cố định.
- Khối minh bạch "Cách chapter này được soạn" có mặt ở đầu Ghi chú biên tập ✓.
- Các mục Ghi chú biên tập khác kiểm được đều nhất quán với thân bài: Heraclitus bị loại vì "BCE06 đã đủ 10" ✓ (đúng là đủ 10); Cleisthenes "k. 508 TCN" ✓; danh sách ứng viên Đông Á bị loại khớp với các tên nêu trong thân bài ✓; phần "Ứng viên Việt Nam" lập luận đúng và trung thực (Đông Sơn không có cá nhân được định danh bằng nguồn đương thời; Hùng Vương / An Dương Vương chỉ có trong thư tịch TK 13–15) ✓.

---

## Không kiểm chứng được

Những chỗ dưới đây tôi **không** xác nhận được, nên đừng coi chúng là đã qua kiểm:

1. **Nội dung thực của các mục Britannica và OCD.** Tôi xác nhận chúng *tồn tại* và đúng/sai tên, nhưng không đọc được toàn văn (paywall/chặn bot) để kiểm chúng có *nói* điều được dẫn hay không. Áp dụng cho toàn bộ 11 mục Britannica và 6 mục OCD. Với SEP thì ngược lại — đọc được toàn văn, và đó là cách phát hiện S1.
2. **Encyclopaedia Iranica "Zoroaster"** — `iranicaonline.org` trả 403 với mọi truy cập tự động. Sự tồn tại được xác nhận gián tiếp qua chỉ mục tìm kiếm; nội dung thì không.
3. **Nội dung 21 cuốn sách.** Đã xác minh tác giả/nhan đề/năm/nhà xuất bản là có thật; **chưa xác minh cuốn nào thực sự hỗ trợ câu nào**. Đây là giới hạn lớn nhất của lượt rà soát này và đúng bằng điều Ghi chú biên tập tự thừa nhận ("Mục Nguồn là điểm khởi đầu để tự kiểm tra, chưa được đối chiếu từng câu").
4. **Các khẳng định định tính về ảnh hưởng dài hạn** — "khuôn mẫu lâu dài của vật lý" (Democritus), "chạy thẳng tới Plato, Kepler và vật lý toán hiện đại" (Pythagoras), "Bloomfield và sau đó giới khoa học máy tính đọc lại Aṣṭādhyāyī" (Pāṇini), "qua Raychandbhai, chính ahiṃsā Jaina định hình trực tiếp đường lối bất bạo động của Gandhi" (Mahāvīra). Đều hợp lý và đều là diễn giải, không phải sự kiện kiểm được. Riêng mệnh đề Gandhi dùng chữ "trực tiếp" mạnh hơn mức tôi xác nhận được — Raychandbhai Mehta có ảnh hưởng lên Gandhi là thật, nhưng "định hình trực tiếp đường lối bất bạo động" là một bước suy rộng.
5. **"Bộ công cụ cai trị này được Babylon, Ba Tư rồi Hy Lạp hoá tiếp nhận gần như nguyên vẹn"** (Tiglath-Pileser III) và **"được Alexander, Seleucid, Parthia rồi Rome tiếp nhận"** (Darius I). Có truyền thừa thiết chế là điều được chấp nhận rộng rãi; mức "gần như nguyên vẹn" thì không kiểm được và nhiều khả năng là nói mạnh.
6. **Mức bằng chứng của các quan hệ xuyên vùng** đánh "tương đồng độc lập · suy đoán học giả" — theo thiết kế là không kiểm chứng được, và cách dùng ở đây nhất quán, thận trọng. Tôi không coi đó là vấn đề.

**Tôi đã đọc và rà toàn bộ 33 mục.** Không mục nào bị bỏ qua vì hết ngân sách.

---

## Ghi chú về lint

Đã chạy `build.py --offline` để đối chiếu: **0 lỗi**, 1 cảnh báo (thuộc `ch90`, không phải Ch2). Tức là **không một phát hiện nào trong báo cáo này bị lint bắt được** — tất cả đều ở tầng nội dung, nằm ngoài tầm với của cổng tự động. Điều đáng lo nhất là S7 (năm mất Jeremiah): nó **khớp Wikidata**, nên cả lint offline lẫn lint online đều sẽ báo sạch, trong khi nó vẫn sai. Khớp Wikidata không phải là bằng chứng đúng.

*(Lệnh build này sinh lại các tệp HTML và `data/persons.json` như thường lệ — đúng hành vi mà CONTRIBUTING mô tả, nội dung không đổi vì `content/` không bị sửa.)*
