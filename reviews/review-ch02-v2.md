# Đánh giá độc lập vòng 2 — Chapter 2 · Thời kỳ Trục (800–401 TCN)

**Người rà soát:** agent độc lập vòng 2, không viết chapter và không viết các bản sửa vòng 1.
**Ngày:** 2026-10-30
**Phạm vi:** 38 mục (BCE08 ×8, BCE07 ×8, BCE06 ×12, BCE05 ×10). Ưu tiên: (1) hồi quy từ 33 sửa đổi vòng 1, (2) năm mục mới, (3) liên kết chéo, (4) nhất quán nội bộ, (5) những điểm vòng 1 không kiểm được.
**Phương pháp:** đọc `reports/review-ch02.md`, rồi đọc toàn bộ `content/ch02.md` hiện tại; kiểm độc lập bằng Wikidata (JSON), Wikipedia, sardisexpedition.org, Hesperia/ASCSA, ISAC/OIP 24, các bài JSOT/Iraq/Water History; chạy một đoạn Python đếm danh sách và soát liên kết theo cả hai chiều (lint chỉ soát một chiều). **Không** dựa vào các dossier `reports/new-*.md`.

---

## Kết luận

**CÔNG BỐ ĐƯỢC SAU KHI SỬA — các sửa đổi vòng 1 đúng, năm mục mới vững, nhưng có một lỗi liên kết niên đại và bốn chỗ ghi chú lỗi thời.**

Toàn bộ các sửa đổi được yêu cầu kiểm (Jeremiah, Quản Trọng, Yajnavalkya/Uddālaka, Piye, Darius, Dracon, Mahāvīra, Solon, Cyrus, Hesiod/Archilochus, Zarathustra, ba mức bằng chứng N3, Psamtik I, Diêm thiết luận, vệ sinh trích dẫn) **đều được thực hiện đúng về nội dung**, không có sửa nào đưa vào lỗi sự kiện mới. Năm mục mới: 5/5 Q-ID đúng người; 10/10 nguồn có thật và đúng nhân vật; toàn bộ con số tải trọng (577/408, 55 km, 280 m, 703–688, 750 ha, 46 thành, 533 m, >2.000 quai lmlk, 8,1 g, 13,3:1, 1/48, 1988/2002/2021, 8–9 quyển/~10.000/~650 dòng) đã đối chiếu và đúng.

Vấn đề còn lại nằm ở **tầng liên kết và ghi chú**: một liên kết ngược niên đại có sẵn từ bản đầu nhưng bị sửa S7 làm lộ rõ (Cyrus → Jeremiah); cặp Hezekiah ↔ Sennacherib được ghi chéo sai quy ước; hai con số trong Ghi chú biên tập chưa cập nhật sau khi thêm Croesus.

**Số phát hiện:** Hồi quy 2 · Mục mới Sai 0 · Mục mới Đáng ngờ 4 · Liên kết 5 (1 Sai) · Nhất quán 5.

Ba mục nghiêm trọng nhất: **L1** (Cyrus "ảnh hưởng tới" Jeremiah — Jeremiah mất k. 570, Cyrus chiếm Babylon 539), **L2** (Hezekiah và Sennacherib ghi nhau cùng ở "Ảnh hưởng tới", không mục nào ghi ở "Kế thừa từ"), **C1/C2** (Ghi chú biên tập còn "1/35" và "BCE06 còn đúng một chỗ dưới trần 12" trong khi chapter đã 38 người và BCE06 đã kín 12).

---

## Hồi quy — các sửa đổi vòng 1 sai hoặc chưa trọn

### H1 · Ghi chú biên tập (Heraclitus) — câu biện minh đã lỗi thời sau khi thêm Croesus

> `Heraclitus (TK 6–5 TCN): […] nhóm BCE06 còn đúng một chỗ dưới trần 12, và nếu Zarathustra chuyển sang Chapter 1 thì Heraclitus là ứng viên đầu tiên cho chỗ đó.`

Câu này đúng khi BCE06 có 11 người (sau khi thêm Sappho 22:48, trước khi thêm Croesus 23:22 — theo mốc giờ tệp). Hiện BCE06 có **12/12** (01 Khổng Tử … 11 Sappho, 12 Croesus), trần nhóm theo CONTRIBUTING dòng 13 và `prompts/atlas-prompt.md` dòng 18 là 12. Không còn chỗ nào.

**Sửa:** "nhóm BCE06 đã kín trần 12; Heraclitus chỉ có chỗ nếu Zarathustra chuyển sang Chapter 1."

### H2 · Ghi chú "Về độ phủ giới" — mẫu số sai

> `Tỉ lệ 1/35 phản ánh hai thứ chồng lên nhau`

Chapter có 38 người (Giới thiệu ghi 38, `reports/stats.txt` ghi 38, tôi đếm được 38). 35 là con số trước khi thêm Croesus, Sennacherib, Hezekiah.

**Sửa:** `1/38`.

*(Các sửa đổi vòng 1 khác đều đúng — xem "Đã kiểm, đúng". Hai mục dưới đây không phải hồi quy mà là lỗi cũ bị sửa S7 làm lộ, ghi ở phần Liên kết.)*

---

## Mục mới — Sai

Không có. Tôi không tìm được khẳng định sự kiện nào trong năm mục mới là sai.

## Mục mới — Đáng ngờ

### M1 · CH02-BCE08-07 (Hezekiah) — năm Marduk-apla-iddina bị đánh bật

> `Marduk-apla-iddina bị loại theo độ bền (b): bị Sennacherib đánh bật năm 702 TCN`

Triều thứ hai của ông kéo dài chín tháng 703–702 TCN; chiến dịch thứ nhất của Sennacherib và trận Kish theo quy ước được đặt **703 TCN** (Grayson, biên niên Babylon), một số tác giả đặt đầu 702. Không sai hẳn, nhưng 703 là con số thường gặp hơn.

**Sửa:** `703/702 TCN`. Các con số khác trong câu (722–710 và 703; Babylon độc lập lại 626 TCN) đúng.

### M2 · CH02-BCE08-08 (Baudhāyana) — "sớm nhất còn lại" phụ thuộc vào niên đại cao

> `Đây là phát biểu bằng lời ở dạng tổng quát sớm nhất còn lại của quan hệ về sau mang tên Pythagoras.`

Nội dung đúng (Wikipedia "Baudhayana sutras": "earliest extant verbal expression of the Pythagorean theorem"; quy tắc phát biểu cho hình chữ nhật bất kỳ). Nhưng khoảng niên đại học thuật cho Baudhāyana là **k. 800–500 TCN** (Plofker 2009), và mục đặt ông ở đầu khoảng đó (`hoạt động k. 800–700`), tức nhóm BCE08. Nếu lấy đầu thấp (TK 6–5 TCN), ông cùng thời hoặc muộn hơn Pythagoras và chữ "sớm nhất" chỉ còn là "độc lập". Mục đã gắn nhãn [Tranh cãi lịch sử] và độ tin cậy Thấp — đủ; nhưng (i) câu trên nên rào "theo niên đại cao", và (ii) ông **không** có mặt trong Ghi chú "Nhân vật có thể thuộc thế kỷ khác" trong khi biên độ của ông rộng ba thế kỷ, rộng hơn Darius hay Mặc Tử là hai người đang được ghi ở đó (xem C4).

Bằng chứng khác đã kiểm đúng: 577/408 = 1,414215…, trùng √2 tới năm chữ số ✓; bốn bộ ba (3,4,5), (5,12,13), (8,15,17), (12,35,37) có trong văn bản ✓; Plofker xếp Mānava cùng tầng với Baudhāyana và đặt Kātyāyana sau Pāṇini ✓; Pingree xếp Āpastamba, Kātyāyana, Mānava sau Baudhāyana theo dấu vết vay mượn ✓; trường phái Taittirīya của Kṛṣṇa Yajurveda ✓; Wikidata Q3384944 = "Baudhayana, ancient Indian mathematician", P31 = Q5 ✓.

### M3 · CH02-BCE07-08 (Sennacherib) — "chưa thấy ở đâu trước thời La Mã" đúng cho cầu máng, nhưng câu dễ bị đọc rộng

> `cầu máng đá vôi đẽo dài 280 m, khắc bi ký của ông — kiểu công trình chưa thấy ở đâu trước thời La Mã`

Đúng nếu hiểu "kiểu công trình" = **cầu máng đá bắc qua thung lũng** (Wikipedia Jerwan: "some consider it the world's oldest aqueduct, predating anything the Romans built by five centuries"). Nhưng kênh dẫn nước dài có trước: kênh Menua của Urartu (k. 800 TCN, ~50 km) và đường hầm Eupalinos ở Samos (TK 6 TCN). Câu hiện tại đứng được; chỉ nên ghi rõ "cầu máng" để không bị đọc thành "hệ kênh dẫn nước".

Các con số đã kiểm đúng: kênh Khinis 55 km ✓ (Water History 2024); bốn giai đoạn 703–688 TCN ✓ (Kisiri 702, Musri 694, Bắc 690, Khinis 688 — Reade; Ur); Jerwan 280 m × 22 m × 9 m, >2 triệu khối đá ✓ (Jacobsen–Lloyd 1935); Nineveh 750 ha, tường 12 km, dân >100.000 ✓; cung "Không đối thủ", phù điêu Lachish ở Cung Tây Nam ✓; phá Babylon 689 TCN, nước Arahtu ✓; Sargon II 722–705, Taharqa 690–664, Kawa và Karnak ✓; Wikidata Q207140 P569 −745, P570 −681 ✓ khớp `k. 745–681`, độ tin cậy Cao trong dung sai 5 năm ✓.

### M4 · CH02-BCE06-12 (Croesus) — gán vùng không cùng quy ước với Ionia

> `nơi: Sardis, xứ Lydia, nay thuộc tỉnh Manisa, Thổ Nhĩ Kỳ | vùng: Trung Đông/Bắc Phi`

Homer, Thales, Anaximander — đều ở bờ tây Anatolia, cách Sardis chưa tới 100 km — được gán `Châu Âu`. Gán theo văn hoá (Hy Lạp vs Lydia) thì bảo vệ được, nhưng đang không có một dòng nào nói ra quy ước đó, và nó ảnh hưởng trực tiếp tới con số 39,5% Châu Âu mà chapter dùng để tự đánh giá. Cùng loại với N4 vòng 1 (Zarathustra = Trung Á duy nhất).

**Sửa:** thêm một câu ở Ghi chú biên tập: "Anatolia được gán theo ngôn ngữ–văn hoá: thành bang Hy Lạp Ionia → Châu Âu; Lydia → Trung Đông/Bắc Phi."

Các con số đã kiểm đúng: Herodotus I.94 người Lydia đúc tiền vàng–bạc đầu tiên ✓; Kroll 2010 (sardisexpedition.org, URL đúng) — Croesus thu hồi electrum, đổi sang lưỡng kim vàng ròng–bạc ròng ✓, stater vàng nhẹ 8,06 g ✓, siglos = 1/20 stater vàng tức 1 stater vàng = 10 stater bạc ✓, tỉ giá 13,3:1 ✓, Croeseid tiếp tục đúc ~30 năm sau khi Croesus mất tới gần cuối TK 6 ✓, WALWET trên electrum đầu sư tử ✓; mệnh giá bạc tới 1/48 ✓ (Wikipedia "Croeseid": "from 1/3 to 1/48"); tiền trong/dưới tầng phá huỷ: 1988 (1/24 bạc bên bộ xương), 2002 (1/12 vàng và bạc dưới tường thành), 2021 (chín đồng bạc ở Field 49) ✓ (Cahill 2005 AJA; Cahill et al., *Hesperia* 94.2, 2025, 143–183 ✓ đúng tập, số, trang); bài Hesperia quả thật ủng hộ Wallace 2016 đẩy năm lên ngôi về thập niên 580 ✓; Amasis II 570–526, Naukratis, Herodotus II.178 ✓; Wikidata Q184462 P569 k. −596, P570 "sau 546" ✓.

*(Sappho — CH02-BCE06-11 — không có mục nào đáng ngờ. Xem "Đã kiểm, đúng".)*

---

## Liên kết

### L1 · SAI — CH02-BCE06-07 (Cyrus) "ảnh hưởng tới" CH02-BCE07-06 (Jeremiah): ngược niên đại

> Cyrus: `**Ảnh hưởng tới:** […] - CH02-BCE07-06 · kế thừa · suy đoán học giả`

Jeremiah nay ghi `k. 650–k. 570 TCN` (sửa S7, đúng). Cyrus lên ngôi Anshan k. 559, chiếm Babylon 539, ra sắc lệnh hồi hương 538. **Một người mất k. 570 không thể "kế thừa" từ một người chỉ nổi lên sau đó.** Lỗi này có sẵn từ bản đầu (khi Jeremiah còn ghi mất 587 thì vẫn ngược, nhưng khó thấy hơn), vòng 1 bỏ sót, và chính việc sửa năm mất đã làm nó lộ rõ. Jeremiah cũng **không** ghi Cyrus ở "Kế thừa từ", nên lint (chỉ soát chiều Kế thừa từ → Ảnh hưởng tới) không bắt.

Quan hệ thật nằm ở chiều ngược: sách Ezra 1:1 và 2 Sử ký 36:22 trình bày sắc lệnh của Cyrus như sự ứng nghiệm lời Jeremiah về bảy mươi năm (Jer 25:11–12; 29:10). Đó là **cách đời sau đọc Cyrus qua Jeremiah**, không phải ảnh hưởng của Cyrus lên Jeremiah.

**Sửa:** xoá dòng này khỏi Cyrus. Nếu muốn giữ mạch, thêm vào Jeremiah `**Ảnh hưởng tới:** - CH02-BCE06-07 · kế thừa · suy đoán học giả` kèm ghi chú "qua Ezra 1:1" — nhưng Jeremiah đang có 2 mục ở đó nên còn chỗ. Cyrus sau khi xoá còn 1 mục "Ảnh hưởng tới" (Darius), hợp lệ.

### L2 · CH02-BCE08-07 (Hezekiah) ↔ CH02-BCE07-08 (Sennacherib) — ghi chéo cùng ở "Ảnh hưởng tới"

> Hezekiah: `**Ảnh hưởng tới:** - CH02-BCE07-08 · phản bác · trực tiếp`
> Sennacherib: `**Ảnh hưởng tới:** - CH02-BCE08-07 · phản bác · trực tiếp`

Hai mục ghi **nhau** ở "Ảnh hưởng tới", và **không mục nào** ghi mục kia ở "Kế thừa từ". Quy ước của prompt là một quan hệ có hướng: A ảnh hưởng tới B ⇔ B kế thừa từ A. Cách ghi hiện tại (i) không phải cặp gương, (ii) đếm một quan hệ thành hai lần trong `stats.txt`, (iii) lọt lưới lint vì lint chỉ soát chiều Kế thừa từ. Về nội dung, "phản bác · trực tiếp" là đúng — xung đột 701 TCN được cả lăng trụ Sennacherib lẫn 2 Các Vua 18–19 ghi.

**Sửa:** chọn một hướng. Hợp lý nhất: Sennacherib giữ `Ảnh hưởng tới: CH02-BCE08-07 · phản bác · trực tiếp`; Hezekiah chuyển dòng đó sang `Kế thừa từ: CH02-BCE07-08 · phản bác · trực tiếp`. "Kế thừa từ" của Hezekiah đang đủ 3, nên phải bỏ một — bỏ dòng yếu nhất là `CH02-BCE08-05 · phản bác · suy đoán học giả` (xem L5). "Ảnh hưởng tới" của Hezekiah còn Josiah và Jeremiah, hợp lệ.

### L3 · CH02-BCE08-04 (Isaiah) → CH02-BCE08-07 (Hezekiah) — mức "qua trường phái" không khớp với chính mục

> Isaiah: `- CH02-BCE08-07 · kế thừa · qua trường phái`
> Hezekiah: `- CH02-BCE08-04 · kế thừa · qua trường phái` và ngay trên đó `- Ahaz (vua Judah, cha ông) · phản bác · trực tiếp`

Hai đầu khớp nhau — tốt. Nhưng Isaiah và Hezekiah là hai người **cùng thời, cùng thành phố**, và nguồn duy nhất về quan hệ giữa họ (Isaiah 36–39 ∥ 2 Các Vua 19–20) mô tả họ nói chuyện trực tiếp. Trong cùng mục, quan hệ với Ahaz — cũng chỉ có trong 2 Các Vua — được đánh "trực tiếp". Dùng hai mức khác nhau cho hai quan hệ có cùng loại nguồn là không nhất quán. Nếu lý do là "văn bản Isaiah 36–39 là phụ lục sao từ 2 Các Vua, không phải của ngôn sứ" thì đó là lập luận hợp lệ, nhưng phải nói ra.

**Sửa:** hoặc nâng lên "trực tiếp" ở cả hai đầu, hoặc hạ Ahaz xuống cùng mức và ghi lý do.

### L4 · CH02-BCE08-07 (Hezekiah) → CH02-BCE07-06 (Jeremiah) — "phản bác" đi ngược chính sách Jeremiah

> Hezekiah: `- CH02-BCE07-06 · phản bác · qua trường phái`
> Jeremiah: `- CH02-BCE08-07 · phản bác · qua trường phái`

Hai đầu khớp nhau. Nhưng chỗ duy nhất sách Jeremiah nhắc tên Hezekiah là **Jer 26:18–19**, và ở đó ông là **mẫu tích cực**: vua đã nghe Micah và "cầu khẩn Đức Chúa" thay vì giết ngôn sứ. Lập luận "phản bác" chỉ đứng được nếu hiểu là Jeremiah bác bỏ thần học Sion-bất-khả-xâm-phạm mà việc Jerusalem sống sót năm 701 củng cố (Jer 7). Đó là một suy luận hai bước, cần ghi chú; để trần "phản bác" thì người đọc sẽ hiểu là Jeremiah chống Hezekiah.

**Sửa:** hoặc đổi sang `kế thừa · qua trường phái` (Jeremiah tiếp nối mạch cải cách Hezekiah–Josiah), hoặc giữ "phản bác" kèm chú "(bác thần học Sion sau 701, Jer 7)".

### L5 · CH02-BCE08-07 (Hezekiah) ← CH02-BCE08-05 (Tiglath-Pileser III) — "phản bác" nhắm sai vua

> Hezekiah: `- CH02-BCE08-05 · phản bác · suy đoán học giả`

Tiglath-Pileser III mất 727 TCN; Hezekiah lên ngôi k. 715. Cuộc nổi dậy của Hezekiah nhắm vào **Sargon II rồi Sennacherib**, không phải Tiglath-Pileser. Mối liên hệ thật của Tiglath-Pileser với Judah là qua Ahaz (2 Các Vua 16) — và Ahaz đã có dòng riêng. Dòng này vừa yếu về nội dung vừa chiếm chỗ cần cho L2. Lint đã đánh INFO vì Tiglath-Pileser không ghi chiều ngược (danh sách của ông đã đủ 3).

**Sửa:** bỏ, thay bằng dòng Sennacherib theo L2.

### Đã kiểm, nhất quán hai đầu

- Pythagoras ↔ Baudhāyana: `tương đồng độc lập · suy đoán học giả` ở cả hai đầu ✓ — đúng loại và đúng mức (không có bằng chứng truyền bá).
- Croesus → Cyrus: `kế thừa · trực tiếp` hai đầu ✓ — Cyrus giữ xưởng Sardis và tiếp tục đúc Croeseid, Kroll xác nhận.
- Croesus → Darius: `kế thừa · qua trường phái` hai đầu ✓ — daric/siglos kế thừa hệ cân qua giai đoạn Croeseid Ba Tư.
- Sennacherib → Ashurbanipal: `kế thừa · trực tiếp` hai đầu ✓. Lưu ý: Ashurbanipal (sinh k. 685) mới khoảng bốn tuổi khi ông nội mất (681), nên "trực tiếp" ở đây là kế thừa triều đại–cung điện chứ không phải tiếp xúc cá nhân; chấp nhận được vì cùng cách dùng với Piye → Taharqa.
- Isaiah → Hezekiah, Hezekiah → Jeremiah: khớp hai đầu ✓ (nội dung xem L3, L4).
- Không danh sách nào vượt 3 mục (kiểm bằng script trên cả 38 mục) ✓.
- Bốn liên kết một chiều lint báo INFO (Hezekiah và Sennacherib ← Tiglath-Pileser; Sappho và Archilochus ← Homer) đều do danh sách "Ảnh hưởng tới" của đích đã đủ 3 — chấp nhận được theo quy ước "P4 sẽ đồng bộ".
- Chiều ngược (Ảnh hưởng tới X mà X không ghi Kế thừa từ) có 9 trường hợp lint không thấy; ngoài L1 và L2, bảy trường hợp còn lại là liên kết cũ và vô hại (ví dụ Zarathustra → Cyrus, Thales → Democritus), chỉ nên đồng bộ ở P4.

---

## Nhất quán

### C1 · "Tỉ lệ 1/35" — xem H2. Sửa thành 1/38.

### C2 · "BCE06 còn đúng một chỗ dưới trần 12" — xem H1. BCE06 đã kín.

### C3 · CH02-BCE05-10 (Darius I) — dấu gạch ngang mở không đóng làm câu đọc sai

> `chia các satrapy có định mức cống nạp cố định — Herodotus đếm hai mươi khu thuế, bia Behistun của chính ông liệt kê hai mươi ba xứ, đặt thanh tra lưu động kiểm soát tổng đốc, đúc đồng tiền vàng daric […]`

Phần chèn "Herodotus đếm… hai mươi ba xứ" mở bằng gạch ngang nhưng không đóng, nên "đặt thanh tra lưu động…" đọc như một vế tiếp của bia Behistun. Lỗi này sinh ra từ sửa D7 (đúng về nội dung: Herodotus III.89 = 20, Behistun §6 = 23 ✓).

**Sửa:** đóng gạch ngang sau "hai mươi ba xứ —" hoặc dùng ngoặc đơn.

Ghi chú thêm về D8: "chín ngày" không có trong Herodotus — ông chỉ cho 111 trạm và 90 ngày đi bộ (V.52–53) và tả hệ trạm ngựa (VIII.98); chín ngày là ước tính hiện đại. Câu hiện tại không gán con số cho Herodotus nên chấp nhận được; nếu muốn chặt hơn, viết "ước tính khoảng chín ngày".

### C4 · Baudhāyana vắng mặt trong "Nhân vật có thể thuộc thế kỷ khác"

Mục này liệt kê Homer, Hesiod, Yajnavalkya, Darius, Mặc Tử, Democritus. Baudhāyana có biên độ niên đại học thuật 800–500 TCN (xem M2) và được xếp ở đầu biên — nếu lấy giữa biên, ông thuộc BCE07 hoặc BCE06. Đây đúng loại thông tin mục này tồn tại để ghi.

**Sửa:** thêm một dòng: "Baudhāyana (CH02-BCE08-08): Plofker cho khoảng 800–500 TCN; xếp BCE08 theo đầu cao của biên, cùng cách với Zarathustra theo niên đại truyền thống."

### C5 · Sappho ở BCE06 trong khi vòng 1 gợi ý BCE07 — không sai, nhưng chưa nói lý do

Floruit của Sappho (Suda: Ol. 42 = 612–608; lưu đày Sicily k. 600; mất k. 570) nằm vắt qua ranh 601/600, nên BCE06 và BCE07 đều bảo vệ được. Vòng 1 đề nghị BCE07 vì nhóm đó còn trống; chapter chọn BCE06 và không nói vì sao. Một câu trong Ghi chú biên tập là đủ.

### Đã kiểm, nhất quán

- Giới thiệu ghi 38; đếm thực 8 + 8 + 12 + 10 = 38 ✓; `stats.txt` 38 ✓; không nhóm nào vượt trần 12 ✓.
- Châu Âu 15/38 = 39,5% ✓ (Homer, Hesiod, Archilochus, Dracon, Thales, Pythagoras, Solon, Anaximander, Sappho, Socrates, Parmenides, Herodotus, Hippocrates, Democritus, Aeschylus). Chapter không còn nêu con số 42,4% ở đâu nữa ✓.
- Ghi chú Josiah ↔ mục Hezekiah: cùng lập luận (2 Các Vua 18:4, Arad/Beersheba theo Herzog, bulla–Siloam–lăng trụ) và cùng rào (Na'aman, Edelman) ✓.
- Ghi chú Taharqa/Sargon II/Nebuchadnezzar II đã tách Psamtik I và dẫn tới Sennacherib ✓; mục Sennacherib cũng nêu Sargon II và Taharqa là ứng viên bị loại ✓.
- Ghi chú Śulbasūtra (Āpastamba, Kātyāyana, Mānava) khớp "Vì sao chọn" của Baudhāyana ✓.
- Ghi chú Wikidata đã thêm Hezekiah (Q244912 thiếu Q5) ✓ — tôi xác nhận P31 = Q20643955, không có Q5.
- Ghi chú Yajnavalkya chuyển nhóm: nêu đúng lý do (Olivelle đặt BU và ChU ở TK 7–6; quy tắc xếp theo floruit) ✓; mục BCE07-07 không còn dùng tiêu chí (c) để biện minh *xếp nhóm*, chỉ dùng cho *chọn* ✓.
- Ghi chú Tiglath-Pileser/Piye về trường `năm:` đã bổ sung Hezekiah và nêu hai hệ niên đại trị vì (715 hay 727 – 687 hay 698) ✓ đúng với tranh luận Thiele/Young/Galil.
- Bối cảnh BCE07 "Hy Lạp chuyển … tiền đúc" vẫn đúng; bước Lydia nay có Croesus ở BCE06 đại diện ✓.

---

## Đã kiểm, đúng

### Hồi quy — từng sửa đổi vòng 1

| Vòng 1 | Hiện trạng | Kết luận |
|---|---|---|
| S1 Solon — nguồn SEP không nhắc Solon | Nay `Ath. Pol. 5–12 (chương 7 liệt kê bốn hạng); Plutarch, Solon` | ✓ đúng, hai nguồn đều bàn Solon |
| S2 Uddālaka — Britannica không có mục | Chỉ còn Olivelle 1998, ChU VI.1–16 | ✓ |
| S3 Quản Trọng — Britannica không có mục | Rickett tập I (Princeton 1985); Sử ký, Quản Yến liệt truyện | ✓ (đúng tập — N9) |
| S4 Mahāvīra — tên mục Britannica | "Vardhamāna" | ✓ |
| S5 Tôn Tử — tên mục Britannica | "Sun Tzu" | ✓ |
| S6 Quản Trọng — Tử Sản không cùng thời | Nay: Bào Thúc Nha (người tiến cử — đúng theo Sử ký), Tề Hoàn Công (chủ ông), Tấn Văn Công (bá chủ 636–628, kế tiếp) | ✓ ba người đều là ứng viên hợp lệ; câu "nghiệp bá của Hoàn Công tan rã ngay sau khi ông mất" đúng (loạn kế vị 643) |
| S7 Jeremiah — năm mất | `k. 650–k. 570 TCN`, nơi "sau bị đưa sang Ai Cập" | ✓; với độ tin cậy Trung bình, lệch 17 năm so với Wikidata −587 nằm trong dung sai 25 nên lint sạch — và CONTRIBUTING dòng 49 nay dùng đúng ví dụ này |
| S8 Psamtik I | Tách riêng, nêu đúng lý do (lập vương triều 26, chấm dứt vương triều 25) | ✓ |
| D1 Mahāvīra — anekāntavāda/syādvāda | Chuyển thành "truyền thống Jaina về sau khai triển… qua Umāsvāti, Siddhasena rồi Samantabhadra, tức bảy tới mười thế kỷ sau" | ✓ đúng thứ tự và đúng khoảng (TK 2–6 CN) |
| D2 Cyrus — tính nguyên bản | Nay: "công cụ hành chính quy ước của các đế chế Lưỡng Hà, nhưng ông vận dụng ở quy mô chưa từng có"; tiêu chí đổi (c) → (a)+(d) | ✓ đúng tinh thần Kuhrt |
| D3 Yajnavalkya/Uddālaka | Yajnavalkya về BCE07-07, cùng floruit 700–650; câu "Truyền thống phần lớn đặt Uddālaka ở vai thầy, nhưng chính Bṛhadāraṇyaka lại dựng hai người thành đối thủ tranh biện ở triều Janaka" | ✓ **đúng cả hai vế**: BU 6.5.3 và Śatapatha Brāhmaṇa đặt Uddālaka là thầy; BU 3.7 cho Uddālaka chất vấn Yājñavalkya về *sūtra* và *antaryāmin* rồi thua. Hướng liên kết Uddālaka → Yajnavalkya · kế thừa · qua trường phái khớp hai đầu ✓ |
| D4 Mặc Tử — "duy nhất" | "sớm nhất và hệ thống nhất, bên cạnh Danh gia" | ✓ |
| D5 Piye | "buộc các vua Đồng bằng quy phục rồi rút về Napata… dù Kashta trước ông thường được tính là vua đầu triều và quyền kiểm soát Hạ Ai Cập chỉ thành thực chất dưới thời Shabaka" | ✓ đúng từng vế |
| D6 Hesiod/Archilochus | Archilochus nay: "Hesiod đã nói ở ngôi thứ nhất nhưng trong khuôn sử thi giáo huấn" | ✓ |
| D7 Darius — 20 satrapy | "Herodotus đếm hai mươi khu thuế, bia Behistun của chính ông liệt kê hai mươi ba xứ" | ✓ nội dung (xem C3 về dấu câu) |
| D8 Darius — một tuần | "chín ngày, so với chín mươi ngày đi bộ" | ✓ (xem ghi chú C3) |
| D9 Dracon | `hoạt động k. 624–621 TCN`; nguồn ghi "Ath. Pol. 7 (chương 4… phần lớn giới nghiên cứu coi là nguỵ tạo đời sau)" | ✓ khớp OCD "c. 624–621/0"; cảnh báo chương 4 đã có |
| D10 Mahāvīra — độ tin cậy | Thấp, kèm "biên khác k. 540–468 TCN" | ✓ nhất quán với Đức Phật |
| N1 Sappho | Thêm CH02-BCE06-11; ghi chú "Về độ phủ giới" nêu Enheduanna, Gārgī, Maitreyī | ✓ (xem C1, C5) |
| N2 Zarathustra | "Không cá nhân nào khác ở đông Iran hay Trung Á TK 6 TCN được nguồn đương thời định danh — chính sự trống vắng ấy là một phát hiện về tư liệu" | ✓ đúng yêu cầu |
| N3 ba mức "trực tiếp" | Herodotus ↔ Solon → qua trường phái (hai đầu); Archilochus ← Homer → suy đoán học giả; Ashurbanipal ← Tiglath-Pileser → qua trường phái | ✓ cả ba |
| N6 Diêm thiết luận | "tranh luận quanh nó — mở đầu bằng Diêm thiết luận năm 81 TCN — còn kéo dài suốt hai nghìn năm" | ✓ |
| N7 Pythagoras dây đàn | "mà truyền thống minh hoạ bằng" | ✓ |
| N8 Parmenides nguồn thứ hai | Coxon, *The Fragments of Parmenides* (bản sửa, 2009) | ✓ có thật (ed. McKirahan, Parmenides Publishing 2009) |
| N9 vệ sinh trích dẫn | Iranica "Zoroaster ii. General Survey"; Rickett tập I; Cardona tập I bản sửa lần 2; Sharp (chủ biên) OUP 2016 | ✓ cả bốn |
| N11 Ashurbanipal lĩnh vực | "Chính trị/Nhà nước, Giáo dục" | ✓ trong `FIELDS` |
| N12 bốn ứng viên ngoài châu Âu | Sennacherib BCE07-08, Baudhāyana BCE08-08, Croesus BCE06-12, Hezekiah BCE08-07 | ✓ cả bốn đã vào, mỗi người có dossier |

Không đổi (vòng 1 chỉ nêu là "nên biết", không bắt buộc): N4 vùng Zarathustra; N5 lý do BCE07 thưa (nay đã 8/12 nên bớt gay gắt); N10 hai mục dùng chung SEP; N13 Dracon vs Tử Sản; N14 đoạn cấp chapter về thiên lệch phương pháp — **chưa có** đoạn tương đương; N15 tỉ lệ châu Âu nay 39,5%, nằm trên mức 30–35% vòng 1 cho là "trung thực" nhưng đã giảm. Câu Mahāvīra "định hình trực tiếp đường lối bất bạo động của Gandhi" vẫn giữ chữ "trực tiếp" mà vòng 1 cho là mạnh hơn mức kiểm được.

### Năm mục mới — những gì tôi thực sự đối chiếu

**Wikidata 5/5 đúng người, trường `năm:` khớp:** Q17892 Sappho (Q5) · Q3384944 Baudhayana "ancient Indian mathematician" (Q5, P569 = P570 = −800) · Q184462 Croesus "King of Lydia" (Q5, −596 / sau 546) · Q207140 Sennacherib "king of Assyria" (Q5, −745 / −681-10-20) · Q244912 Hezekiah "King of Judah" (P31 = Q20643955, **không** Q5; −741 / −686 — chapter ghi 741–687, lệch 1 năm trong dung sai 25).

**Nguồn 10/10 có thật, đúng nhân vật:**
- Voigt, *Sappho et Alcaeus: Fragmenta* (Amsterdam: Athenaeum–Polak & Van Gennep, 1971) ✓ — bản hiệu đính chuẩn, hệ đánh số mảnh 1/16/31 dùng trong mục khớp Voigt = Lobel–Page ✓.
- Bierl & Lardinois (chủ biên), *The Newest Sappho: P. Sapph. Obbink and P. GC inv. 105, Frs. 1–4* (Brill, 2016) ✓ nguyên nhan đề.
- Sen & Bag, *The Śulbasūtras of Baudhāyana, Āpastamba, Kātyāyana and Mānava* (INSA, 1983) ✓.
- Plofker, *Mathematics in India* (Princeton, 2009), chương 2 ✓ — chương 2 là "Mathematical Thought in Vedic India", đúng chỗ bàn Śulbasūtra.
- Kroll, "The Coins of Sardis", trong Cahill (chủ biên), *The Lydians and Their World* (2010) ✓ — URL sardisexpedition.org phân giải, đúng bài, nội dung hỗ trợ từng khẳng định của mục.
- Cahill, Bruce, Kroll et al., "A New Find of Croeseid Coins from Sardis", *Hesperia* 94.2 (2025), 143–183 ✓ (trang ASCSA xác nhận tập/số/trang; tôi không xác nhận được DOI vì MUSE trả 403 — số DOI trùng với mã bài MUSE 963374 nên nhiều khả năng đúng).
- Jacobsen & Lloyd, *Sennacherib's Aqueduct at Jerwan*, OIP 24 (1935) ✓ — URL isac-assets PDF là bản chính thức của ISAC.
- Russell, *Sennacherib's Palace Without Rival at Nineveh* (Chicago, 1991) ✓.
- Grabbe (chủ biên), *'Like a Bird in a Cage': The Invasion of Sennacherib in 701 BCE*, JSOTSup 363 (Sheffield Academic Press, 2003) ✓.
- Finkelstein & Silberman, "Temple and Dynasty: Hezekiah, the Remaking of Judah and the Rise of the Pan-Israelite Ideology", *JSOT* 30/3 (2006), 259–285 ✓.

**Sappho (CH02-BCE06-11) — toàn bộ khẳng định kiểm được đều đúng:** bản Alexandria 8 hoặc 9 quyển (mục rào "ít nhất tám") ✓; ước ~10.000 dòng ✓; còn ~650 dòng ✓; chỉ mảnh 1 chắc chắn trọn vẹn ✓; mảnh 31 → Catullus 51 ✓; mảnh 16 đối lập kỵ binh–hạm thuyền ✓; Mytilene/Eresos ✓; Alcaeus cùng thành, cùng khổ thơ ✓; Stesichorus 26 quyển (Suda) ✓; "người nữ duy nhất trong Chín nhà thơ trữ tình" ✓; Terpander xứ Antissa, Lesbos ✓; `k. 630–570` khớp mô tả Wikidata ✓. "Vì sao chọn" nêu hai người thật sự cùng thời ✓.

**Baudhāyana (CH02-BCE08-08):** xem M2 — mọi con số đúng; ứng viên Mānava, Āpastamba, Kātyāyana là người cùng truyền thống và thứ tự tương đối nêu đúng theo Pingree/Plofker ✓.

**Croesus (CH02-BCE06-12):** xem M4 — mọi con số đúng; ứng viên Alyattes và Amasis II là người cùng thời ✓.

**Sennacherib (CH02-BCE07-08):** xem M3 — mọi con số đúng; ứng viên Sargon II và Taharqa cùng thời ✓; "Kế thừa từ: Truyền thống vườn thượng uyển Assyria (Ashurnasirpal II ở Kalhu)" đúng (kênh Patti-ḫegalli, vườn Kalhu) ✓; "Esarhaddon (tái thiết Babylon) · phản bác · trực tiếp" đúng — con đảo ngược chính sách cha ✓.

**Hezekiah (CH02-BCE08-07):** 2 Các Vua 18:4 (bāmôt, Nehushtan) ✓; 18:2 tuổi 25 ✓; 20:20 đường hầm ✓; Siloam 533 m ✓; >2.000 quai lmlk ✓ (≥21 loại ấn); bulla "Thuộc về Hezekiah [con] Ahaz vua Judah" khai quật ở Ophel (đào 2009, nhận diện–công bố 2015, Eilat Mazar) ✓; lăng trụ 46 thành có tường ✓; cả hai nguồn thừa nhận Jerusalem không thất thủ ✓; Arad tầng VIII / Beersheba theo Herzog vs Na'aman, Edelman (2008) ✓ đúng tên hai phía; Ahaz k. 732–716 ✓ (Thiele 735/732–716/715); Marduk-apla-iddina 722–710 và 703 ✓ (xem M1 về 702/703); Babylon độc lập lại 626 ✓. Floruit 715–687 vắt hai thế kỷ; xếp BCE08 vì khủng hoảng 701 và cải cách đầu triều thuộc TK 8 — bảo vệ được, và ghi chú đã nêu tranh luận niên đại ✓.

### Những điều vòng 1 "không kiểm được" mà vòng này giải quyết được

1. **Nội dung mục Britannica/OCD:** vẫn không đọc được toàn văn; nhưng năm mục mới **không dùng** Britannica/OCD nào — toàn bộ nguồn mới là sách, bài tạp chí và trang khai quật đọc được, nên tầng "nguồn trang trí" không tái xuất ở phần mới.
2. **Iranica "Zoroaster":** đã được dẫn đích danh tiểu mục "ii. General Survey" — tiểu mục này tồn tại (Iranica chia i. The Name, ii. General Survey, iii. In the Avesta…). Nội dung vẫn không truy cập được (403).
3. **Kroll 2010 và Jacobsen–Lloyd 1935** là hai nguồn mới mà tôi đọc được toàn văn hoặc mục lục và xác nhận **từng câu** mục dẫn chúng đều có trong nguồn — khác với 21 cuốn sách vòng 1 chỉ xác nhận tồn tại.

### Lint

`reports/lint-ch02.txt` sau sửa: 0 lỗi, 0 cảnh báo, 4 INFO (đều là liên kết một chiều hợp lệ). Không phát hiện nào trong báo cáo này bị lint bắt — L1 và L2 nằm đúng ở hướng lint không soát. Đề nghị P4 mở rộng lint soát cả chiều "Ảnh hưởng tới X ⇒ X ghi Kế thừa từ" (ít nhất ở mức INFO) để bắt loại lỗi L1/L2.

---

## Không kiểm chứng được

1. **Nội dung các mục Britannica và OCD** của 33 mục cũ — như vòng 1, chỉ xác nhận tồn tại.
2. **Nội dung toàn văn** của Russell 1991, Grabbe 2003, Finkelstein–Silberman 2006, Sen–Bag 1983, Plofker 2009, Voigt 1971, Bierl–Lardinois 2016 — xác nhận tồn tại, đúng nhan đề, đúng nhân vật, và (với Plofker, Finkelstein–Silberman) đúng chương/tóm tắt; chưa đối chiếu từng câu.
3. **DOI của bài Hesperia 2025** (`10.2972/hes.2025.a963374`) — MUSE trả 403; mã bài 963374 trùng, nhiều khả năng đúng nhưng chưa xác nhận trực tiếp.
4. **Dossier `reports/new-*.md`** — theo yêu cầu, tôi không dùng chúng làm bằng chứng và cũng không rà bảng xác minh bên trong; mọi kết luận về năm mục mới ở trên là kiểm độc lập trên văn bản chapter.
5. **Mức độ "chưa từng có" của quy mô Cyrus** (D2 sau sửa) và **"định hình trực tiếp" Gandhi** (Mahāvīra) — diễn giải, không kiểm được.
6. **Tỉ lệ 1/38 là đủ hay chưa** — ngoài phạm vi kiểm sự kiện; ghi chú "Về độ phủ giới" đã nói đúng hai nguyên nhân chồng nhau, tôi không có gì bổ sung.

**Tôi đã đọc toàn bộ 38 mục và toàn bộ Ghi chú biên tập.** Không mục nào bị bỏ qua.
