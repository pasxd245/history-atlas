# Bình duyệt độc lập — `content/ch04.md`, nhóm CH04-CE01 (TK 1 CN)

Người rà: agent bình duyệt độc lập (không viết chapter này).
Ngày: 2026-10-31.
Phạm vi: dòng `**Giới thiệu chapter**` (dòng 2), dòng `**Bối cảnh**` của nhóm CE01 (dòng 5), và 12 mục `CH04-CE01-01` … `-12` (dòng 7–203).
Đối chiếu: `prompts/atlas-prompt.md` §5, `CONTRIBUTING.md` (8 quy tắc).

Xếp loại: **Sai** (sự kiện sai, sửa được bằng nguồn) · **Nghi vấn** (chưa chứng minh được / nghiêng lệch / quá tự tin) · **Thiếu** (lỗ hổng phải bổ sung) · **Thể thức** (vi phạm template §5 hoặc quy tắc CONTRIBUTING).

---

## 0. Kiểm nền: 12 Q-ID

Một lượt `wbgetentities` cho cả 12 Q-ID (`Q302 Q9200 Q7250 Q7268 Q2054 Q189597 Q82778 Q297776 Q134461 Q319329 Q439681 Q177081`), đọc `labels|descriptions|claims` (P31, P569, P570, P106).

**Kết quả: 12/12 trỏ đúng người, không có trang định hướng, không có mục họ tên, tất cả đều `P31 = Q5` (trừ Q302 còn mang thêm các lớp thần học).** Nhãn Wikidata khớp tên tiếng Việt ở mục: Q302 Giê-su, Q7250 Vương Mãng, Q7268 Hán Quang Vũ Đế, Q319329 Vương Sung, Q439681 Ban Cố, Q177081 Ban Chiêu.

Niên đại trong dung sai, không mục nào lệch quá ngưỡng. Hai điểm cần ghi, dù lint không bắt:

| ID | Mục ghi | Wikidata | Nhận xét |
|---|---|---|---|
| -07 Pliny | `23–79 CN`, **Cao** | P569 có cả 23 và 24 (và một giá trị 20) | trong ±5, nhưng năm sinh Pliny vốn là 23 **hoặc** 24; để **Cao** là sát trần |
| -09 Josephus | `37–100 CN`, **Cao** | `c. 37 – c. 100` | năm sinh 37/38 vững, **năm mất chỉ là ước lượng** ("sau 100"). Để **Cao** (±5) là quá tự tin — xem mục -09 |

Đây là áp dụng quy tắc 4 CONTRIBUTING: khớp Wikidata là sàn, không phải trần. Không mục nào trong nhóm này mắc lỗi "Wikidata cùng sai" kiểu Jeremiah, theo những gì kiểm được.

---

## 1. Dòng `**Giới thiệu chapter**` (dòng 2)

**Nghi vấn — "Manichaeism" không dịch.** Nguyên văn: *"Kitô giáo, Phật giáo Đại thừa, Manichaeism, Đạo giáo có tổ chức."* Ba tên kia là tiếng Việt, riêng một tên để nguyên tiếng Anh. §5 ("Ngôn ngữ") yêu cầu viết tiếng Việt, giữ thuật ngữ gốc chỉ khi bản dịch dễ gây hiểu sai — không phải trường hợp này. Chính mục `CH04-CE03-04` trong cùng file ghi là **Mani**.
→ Sửa: `… Kitô giáo, Phật giáo Đại thừa, Mani giáo, Đạo giáo có tổ chức.`

**Nghi vấn — mệnh đề "chưa ai vượt" không quy thuộc.** *"Ptolemy, Galen và Trương Trọng Cảnh để lại những tổng hợp mà hơn một nghìn năm sau vẫn chưa ai vượt."* Đây là phán xét giá trị viết như sự kiện, đúng loại "câu chuyện tiến bộ" mà đầu `prompts/atlas-prompt.md` yêu cầu tránh.
→ Sửa: `… để lại những tổng hợp giữ vị trí sách chuẩn trong hơn một nghìn năm.`

---

## 2. Dòng `**Bối cảnh**` của nhóm CE01 (dòng 5)

Nguyên văn: *"Đế chế La Mã ổn định dưới chế độ nguyên thủ; nhà Hán bị Vương Mãng cắt ngang rồi phục hồi và dời đô về Lạc Dương. Ở Judea, một phong trào trong lòng Do Thái giáo tách ra và bắt đầu truyền sang người ngoại. Giấy, thiên văn và y dược được ghi chép thành sách ở cả hai đầu Á–Âu."*

**Sai — "Giấy … được ghi chép thành sách" trong TK 1.** Mốc giấy mà atlas này dùng là Thái Luân, và chính atlas xếp ông ở **`CH04-CE02-01`** (TK 2) — bản tấu của ông là **năm 105 CN**, nằm ngoài nhóm CE01. Dòng Bối cảnh của CE01 vì thế mượn một sự kiện của nhóm sau. (Giấy khảo cổ Tây Hán có sớm hơn, nhưng là giấy gói, không phải vật mang chữ thành sách — nên câu này không cứu được bằng cách lùi mốc.)
→ Sửa: bỏ "Giấy", để `Thiên văn và y dược được ghi chép thành sách ở cả hai đầu Á–Âu.`

**Thiếu — Bối cảnh không có một chữ nào về Nam Á.** TK 1 là giai đoạn đế quốc Kushan hình thành và Phật giáo Đại thừa khởi phát — chính hai thứ mà dòng Giới thiệu chapter hứa. Dòng Bối cảnh chỉ nói La Mã, Hán, Judea. Vấn đề này lặp lại ở cấp danh sách nhân vật (xem phần "Đánh giá lựa chọn nhân vật" cuối báo cáo); ít nhất Bối cảnh nên nói ra khoảng trống thay vì im lặng.

**Nghi vấn — "tách ra" là quá sớm cho TK 1.** Việc phong trào Giê-su "tách ra" khỏi Do Thái giáo (parting of the ways) là một quá trình mà nghiên cứu hiện nay đẩy về TK 2–4, không phải TK 1; trong TK 1 nó vẫn là một phái trong lòng Do Thái giáo có thêm thành viên người ngoại. Chính mục `-02` trong nhóm viết đúng hơn: *"biến một phong trào trong lòng Do Thái giáo thành một tôn giáo có thể nhận bất kỳ ai"* — tức mở cửa, chưa phải tách.
→ Sửa: `Ở Judea, một phong trào trong lòng Do Thái giáo bắt đầu nhận cả người ngoại.`

---

## 3. `CH04-CE01-01` · Giê-su thành Nazareth

**Q-ID.** `Q302` = "Jesus Christ" / vi "Giê-su". Đúng người. P569 có ba giá trị (−7, −5, −2), P570 có 30 và 33. Mục ghi `k. 4 TCN – 30 CN`, **Trung bình** (±25) — hợp lệ.

**Nguồn — Tacitus, Biên niên sử, q. XV, 44: ĐÚNG.** Đã kiểm đúng quyển đúng đoạn. *Annales* XV.44 là đoạn về vụ cháy Rome và việc Nero đổ tội cho các Christiani, trong đó có câu nói "Christus" bị tổng trấn Pontius Pilatus hành hình dưới thời Tiberius. Đây là đúng quyển, đúng chương, và **có bàn tới điều được dẫn** (cả việc đóng đinh lẫn tên Pilatus). Không có lỗi ở trích dẫn này.

**Nguồn — E. P. Sanders, *The Historical Figure of Jesus* (1993): có thật, đúng thể loại (chuyên khảo phổ thông học thuật, Penguin 1993), đúng chủ đề. Nhưng bị DẪN NGƯỢC LUẬN ĐIỂM CỦA CHÍNH NÓ — xem lỗi dưới.**

### 3.1 **Sai** — Galilee không thuộc "tỉnh Judea" vào thời Giê-su

> `nơi: Galilee và Jerusalem, tỉnh Judea`

Trong toàn bộ quãng đời Giê-su (k. 4 TCN – 30 CN), **Galilee không nằm trong tỉnh Judea**. Tỉnh Judaea của La Mã lập năm 6 CN gồm Judea, Samaria và Idumea; Galilee (cùng Perea) là lãnh địa chư hầu của tetrarch Herod Antipas (trị vì 4 TCN – 39 CN) và chỉ bị sáp nhập vào tỉnh sau năm 44 CN. Chính vì thế Phúc Âm mới có chi tiết Pilatus chuyển Giê-su cho Antipas vì ông là người Galilee — một thao tác chỉ có nghĩa khi hai nơi thuộc hai quyền tài phán khác nhau.
*Nguồn dùng:* Wikipedia EN "Herod Antipas" (dẫn Mommsen và A. N. Sherwin-White về chính điểm tài phán này).
→ **Câu thay thế:** `nơi: Galilee (lãnh địa của tetrarch Herod Antipas) và Jerusalem, tỉnh Judea`

### 3.2 **Sai + trung lập** — câu "rẽ khỏi các nhóm Do Thái đương thời" đi ngược chính nguồn được dẫn

> *"Các câu như yêu kẻ thù hay quy toàn bộ lề luật về hai điều răn là chỗ phong trào này rẽ khỏi các nhóm Do Thái đương thời."*

Ba vấn đề chồng lên nhau, và vấn đề nặng nhất là quy tắc 7 CONTRIBUTING ("nguồn tồn tại, đúng chủ đề, vẫn có thể bị dùng ngược"):

1. **Dẫn ngược nguồn.** E. P. Sanders là người đặt nền cho đúng lập trường ngược lại. Luận điểm trung tâm của ông — từ *Paul and Palestinian Judaism* (1977) qua *Jesus and Judaism* (1985) tới chính *The Historical Figure of Jesus* (1993) — là Giê-su **nằm trong** Do Thái giáo, là người khởi một "renewal movement within Judaism" (cụm từ của chính Sanders), và nội dung đạo đức trong lời giảng của ông **không** phải chỗ ông tách khỏi các phái Do Thái. Dùng Sanders để đỡ cho câu "đây là chỗ rẽ khỏi các nhóm Do Thái đương thời" là dùng ông chống lại ông.
2. **Sai về nội dung.** "Hai điều răn" là hai câu **trích từ chính Ngũ thư** — Đệ nhị luật 6:5 và Lêvi 19:18. Lấy hai câu Torah làm bằng chứng cho việc rẽ khỏi Do Thái giáo là tự mâu thuẫn.
3. **Trượt giọng — nguy cơ motif "Do Thái giáo nệ luật, Kitô giáo đem lòng thương xót".** Câu trước đó (*"đặt lòng thương xót lên trên việc giữ nghi thức khi hai điều xung đột"*) cộng với câu này tái dựng đúng sơ đồ bài Do Thái cổ điển mà nghiên cứu sau 1977 đã bác. Đây là chỗ duy nhất trong mục `-01` mà giọng trượt — không trượt sang tín lý, mà trượt sang **hạ thấp phía Do Thái** để làm nổi phía Kitô. Vi phạm yêu cầu trung lập.
4. **Mâu thuẫn nội bộ.** Chính mục này ghi `Kế thừa từ: CH03-BCE01-07` = **Hillel Trưởng lão**, người có đúng công thức quy toàn bộ lề luật về một điều ("điều ngươi ghét, chớ làm cho người khác — phần còn lại là chú giải"). Mục vừa nói Giê-su *kế thừa* Hillel ở điểm đó, vừa nói điểm đó là chỗ ông *rẽ khỏi* Do Thái giáo đương thời.

→ **Câu thay thế:** `Các câu như yêu kẻ thù, hay việc quy toàn bộ lề luật về hai điều răn lấy từ Ngũ thư, nằm trong mạch tranh luận nội bộ của Do Thái giáo đương thời — Hillel Trưởng lão có một công thức tương tự. Phần sử gia tranh luận không phải là nội dung ấy có mới không, mà là trọng tâm cánh chung trong lời giảng của ông nặng tới đâu.`

### 3.3 **Nghi vấn** — `Kế thừa từ: CH03-BCE01-07 (Hillel) · kế thừa · qua trường phái`

Đã mở đích đọc tên: `CH03-BCE01-07 · Hillel Trưởng lão`. Đúng người, đúng chiều, đúng niên đại (Hillel mất k. 10 CN).

Nhưng **loại quan hệ sai mức**. Không có bằng chứng tiếp xúc hay truyền thừa từ Hillel sang Giê-su; cái tồn tại là một **song song** mà giới nghiên cứu ghi nhận. §5 nói rõ: *"Loại quan hệ 'tương đồng độc lập' là hợp lệ và nên dùng khi không có bằng chứng tiếp xúc; không suy diễn quan hệ kế thừa khi thiếu bằng chứng."*
→ **Sửa:** `- CH03-BCE01-07 · tương đồng độc lập · suy đoán học giả`

(`Gioan Tẩy Giả · kế thừa · trực tiếp` thì **đúng** — phép rửa là một trong hai chi tiết được đồng thuận rộng nhất.)

### 3.4 **Thể thức** — `Ảnh hưởng tới` có 3 mục nhưng 2 mục là mệnh đề, không phải nhân vật/trào lưu

> `- Kitô giáo và toàn bộ lịch sử tư tưởng phương Tây · kế thừa · qua trường phái`

"Toàn bộ lịch sử tư tưởng phương Tây" không phải một trào lưu; đó là một mệnh đề phạm vi không giới hạn, không kiểm được, và là đúng loại văn "tô vẽ" mà §5 cấm.
→ **Sửa:** `- Kitô giáo · kế thừa · qua trường phái`

### 3.5 Trung lập — phần làm ĐÚNG (ghi để khỏi sửa nhầm)

Ranh giới "phần sử gia chấp nhận / phần đến qua Phúc Âm" được đặt **đúng chỗ** và nên giữ nguyên:
- *"Sự kiện ấy, cùng với **việc môn đệ tuyên bố** ông sống lại, là điểm khởi của…"* — quy thuộc đúng: tường thuật hành vi tuyên bố, không khẳng định biến cố. Không trượt tín lý.
- *"Phần cốt lõi — việc ông chịu phép rửa và bị đóng đinh — được **hầu hết sử gia chấp nhận**; nội dung lời giảng thì **đến qua các sách Phúc Âm soạn bốn tới bảy thập niên sau**"* — đây là cách đặt ranh giới chuẩn, và nó cũng giải thích đúng vì sao niên đại để Trung bình.
- Không có chỗ nào dùng danh hiệu tín lý ("Chúa", "Đấng Cứu thế") như mô tả khách quan; cũng không có giọng bài bác (không "huyền thoại", không "bịa đặt").

Tức mục `-01` **không** trượt sang tín lý, và **có** trượt một lần sang hạ thấp — nhưng hạ thấp phía Do Thái giáo, không phải hạ thấp Giê-su (xem 3.2). Đó là chỗ duy nhất cần sửa về giọng.

### 3.6 **Thể thức** — ứng viên bị loại: chỉ còn **một** người thật

> *"Ứng viên cùng thời cùng vùng là Gioan Tẩy Giả, người Josephus chép độc lập, và Hillel Trưởng lão, **đã chọn ở Chapter 3**."*

Việc khai báo Hillel đã có mục riêng là **đúng quy tắc 6** và nên giữ. Nhưng hệ quả: chỉ còn Gioan Tẩy Giả là ứng viên bị loại thật. §5 đòi "1–2 người", nên một người là đủ ở mức tối thiểu — ghi ở đây để đối chiếu với kiểu lỗi lặp đi lặp lại ở các mục -06, -07, -08 dưới đây, nơi con số thật rơi xuống **không**.

---

## 4. `CH04-CE01-02` · Phaolô thành Tarsus

**Q-ID.** `Q9200` = "Paul the Apostle" / vi "Sứ đồ Phaolô". Đúng người. P569 = 5; P570 có 64, 65 và **66**. Mục ghi `k. 5–66 CN`, **Trung bình** — hợp lệ.

**Con số "7 lá thư": ĐÚNG.** Đã kiểm. Nhóm không tranh cãi là Rôma, 1–2 Côrintô, Galat, Philípphê, 1 Thêxalônica, Philêmôn — đúng bảy. Sáu lá còn lại chia thành "tranh luận" (Côlôxê, 2 Thêxalônica, Êphêxô) và "đa số coi là giả danh" (1–2 Timôthê, Titô).
*Nguồn dùng:* Wikipedia EN "Authorship of the Pauline epistles" / "Pauline epistles".

**Câu "văn bản Kitô giáo sớm nhất còn lại, viết trước các sách Phúc Âm": ĐÚNG**, là đồng thuận rộng.

**Nguồn — E. P. Sanders, *Paul: The Apostle's Life, Letters, and Thought* (2015): có thật, đúng thể loại (chuyên khảo, Fortress Press 2015), đúng chủ đề.** Ở mục này Sanders **không** bị dẫn ngược: câu về Rôma chỉ nói Augustinô và Luther "đọc lại để tự định vị" — tức mô tả lịch sử tiếp nhận, không khẳng định cách đọc ấy là cách đọc đúng. Giữ nguyên.

### 4.1 **Sai** — vai trò của Giacôbê ở công nghị Jerusalem bị đảo ngược

> *"Phaolô được chọn theo counterfactual (d): **nếu lập trường của Giacôbê thắng ở công nghị Jerusalem**, phong trào nhiều khả năng ở lại trong Do Thái giáo như một phái."*
> (và trước đó: *"Giacôbê, **người chủ trương giữ luật**"*)

Theo tường thuật Công vụ 15 — tường thuật duy nhất về "công nghị Jerusalem" — lập trường của Giacôbê **đã thắng**, và lập trường ấy chính là **miễn cắt bì** cho người ngoại. Giacôbê là người chủ toạ, đưa ra phán quyết, và Sắc lệnh Tông đồ (kiêng của cúng, máu, thú chết ngạt, dâm dật) là đề nghị của ông. Phe đòi cắt bì trong Công vụ 15 là "mấy người từ Judea xuống" và "mấy người thuộc phái Pharisêu đã tin", **không phải Giacôbê**. Việc gán nhãn "người chủ trương giữ luật" cho Giacôbê là trộn ông với nhóm "những kẻ từ phía Giacôbê" ở Galat 2:12 — mà ngay cả ở đó Phaolô cũng xếp Giacôbê vào hàng "cột trụ" đã bắt tay giao ước với ông (Gl 2:9).
*Nguồn dùng:* Wikipedia EN "Council of Jerusalem" — *"on the initiative of Peter, and of James, the head of the Jerusalem church, it was agreed that acceptance of the Noachian Laws … should be demanded"*; và chính văn bản Cv 15:13–21, Gl 2:9.

Hệ quả: lập luận counterfactual (d) của cả mục đang dựng trên một phản-thực tế **không tồn tại**. Đây là chân đỡ duy nhất cho việc chọn Phaolô, nên lỗi này không phải chi tiết phụ.

→ **Câu thay thế:**
`Ứng viên cùng thế hệ là Phêrô, người lãnh đạo nhóm ở Jerusalem, và Giacôbê, người đứng đầu cộng đoàn Jerusalem. Phaolô được chọn theo counterfactual (d): công nghị Jerusalem miễn cắt bì cho người ngoại, nhưng chính Phaolô mới là người đẩy nguyên tắc ấy tới cùng ở Antioch và trong thư Galat, tới mức nó thành nền thần học chứ không chỉ là một nhân nhượng mục vụ. Nếu không có lập trường ấy, phong trào nhiều khả năng ở lại trong Do Thái giáo như một phái.`

### 4.2 Trung lập — phần làm **đúng**

Mục `-02` giữ được ranh giới: mô tả "quyết định có hệ quả lớn nhất" bằng tiêu chí lịch sử (phạm vi tuyển mộ), không bằng tiêu chí thần học (chân lý của ân sủng). Không có chỗ nào khẳng định biến cố Damascus như sự kiện. Không có giọng bài bác. **Không cần sửa về giọng.**

Một lưu ý nhỏ: *"Bảy lá thư được **giới nghiên cứu** nhận là của chính ông"* — quy thuộc đúng chuẩn. Đây là mẫu mà mục `-06`, `-10`, `-11`, `-12` nên bắt chước (xem các mệnh đề tối cao không quy thuộc bên dưới).

### 4.3 **Thể thức** — ứng viên bị loại: Phêrô và Giacôbê đều **không** có mục riêng

Đã đối chiếu `grep '^### ' content/ch0*.md content/ch90.md` (221 mục): **không** có mục nào cho Phêrô hay Giacôbê. Vậy đây là hai ứng viên bị loại thật, cùng thời, cùng lĩnh vực. **Mục `-02` là một trong hai mục duy nhất của nhóm CE01 đạt đúng yêu cầu §5 về ứng viên bị loại** (mục kia là `-09`). Giữ nguyên cấu trúc, chỉ sửa nội dung sai ở 4.1.

### 4.4 Liên kết — đã mở đích đọc tên, **tất cả đúng**

| Dòng | Đích | Tên thật | Chiều / niên đại |
|---|---|---|---|
| Kế thừa từ `CH04-CE01-01` | — | Giê-su | đúng chiều, đối xứng với `-01` |
| Ảnh hưởng tới `CH04-CE05-01` | — | **Augustinô thành Hippo** | đúng người, đúng chiều (354–430 sau Phaolô) |

---

## 5. `CH04-CE01-03` · Vương Mãng

**Q-ID.** `Q7250` = "Wang Mang" / vi "Vương Mãng". Đúng người. P569 = −45, P570 = 23-10-06. Mục ghi `45 TCN – 23 CN`, **Cao** — khớp chính xác.

**Con số: ĐÚNG cả hai.** Lập nhà Tân **năm 9 CN** — đúng. Chết **năm 23 CN** — đúng (tháng 10 năm 23, khi Trường An thất thủ).
*Nguồn dùng:* Wikidata Q7250 (P570 chính xác tới ngày); Wikipedia EN "Wang Mang".

**Nguồn — Hans Bielenstein trong *The Cambridge History of China*, t. 1 (1986): ĐÚNG mọi mặt.** Tập 1 (*The Ch'in and Han Empires, 221 B.C.–A.D. 220*) in năm 1986; Bielenstein viết chương "Wang Mang, the restoration of the Han dynasty, and Later Han". Đúng năm, đúng tập, đúng tác giả, và **có bàn đúng điều được dẫn**. Không có lỗi.

### 5.1 **Sai** — "phép thử **duy nhất** trong lịch sử Trung Hoa"

> *"ông là **phép thử duy nhất trong lịch sử Trung Hoa** cho câu hỏi liệu có thể cải tạo xã hội theo mô hình kinh điển bằng sắc lệnh"*

Phản ví dụ hiển nhiên: **Tân pháp của Vương An Thạch** (1069–1076, Bắc Tống). Cải cách của ông được giới nghiên cứu phân tích chính qua ảnh hưởng của **Chu lễ** (*Rites of Zhou*) — tức đúng mô hình "cải tạo xã hội theo kinh điển bằng sắc lệnh", quy mô toàn đế quốc, và cũng thất bại rồi để lại một di sản tranh cãi kéo dài. Phản ví dụ thứ hai: cải cách quan chế theo Chu lễ của Vũ Văn Thái / Bắc Chu (TK 6).
*Nguồn dùng:* Wikipedia EN "Wang Anshi" — *"Wang Anshi's ideas are usually analyzed in terms of the influence the Rites of Zhou or Legalism had on him."*

Chữ "duy nhất" cũng tự phá lập luận: nếu đúng là duy nhất thì không giải thích được vì sao Nho gia đời sau phải viện tới ông — họ viện tới ông **vì** có những lần sau.

→ **Câu thay thế:** `… ông là phép thử sớm nhất và triệt để nhất trong lịch sử Trung Hoa cho câu hỏi liệu có thể cải tạo xã hội theo mô hình kinh điển bằng sắc lệnh, và thất bại của ông thành tiền lệ mà phe phản đối Tân pháp của Vương An Thạch một nghìn năm sau còn viện tới.`

### 5.2 **Sai** — "Hán Quang Vũ Đế, người lật ông"

> *"Ứng viên cùng giai đoạn là Hán Quang Vũ Đế, **người lật ông** và được chọn riêng ở mục sau"*

Không phải Quang Vũ Đế lật Vương Mãng. Trường An thất thủ tháng 10 năm 23 dưới tay quân **Lục Lâm** của **Canh Thuỷ Đế** (Lưu Huyền), và Vương Mãng chết trong trận ấy. Lưu Tú khi đó là một tướng dưới trướng Canh Thuỷ Đế (ông thắng trận Côn Dương năm 23), và chỉ lên ngôi **năm 25**, sau khi Xích Mi phế Canh Thuỷ Đế.

Đáng chú ý: **chính mục `-04` trong cùng nhóm viết đúng** — *"Ông dẹp các lực lượng cát cứ **sau loạn Vương Mãng**, khôi phục nhà Hán năm 25 CN"*. Hai mục cạnh nhau mâu thuẫn nhau.
*Nguồn dùng:* Wikipedia EN "Wang Mang" — *"In October AD 23, the capital Chang'an was overrun … Wang Mang was killed in the battle. The Han dynasty was re-established, the Gengshi Emperor taking the throne in the year 23 and the Guangwu Emperor taking the throne in the year 25 after defeating the Red Eyebrows who had deposed the Gengshi Emperor."*

→ **Câu thay thế:** `Ứng viên cùng giai đoạn là Hán Quang Vũ Đế, người dựng lại nhà Hán hai năm sau khi ông chết và được chọn riêng ở mục sau, và Lưu Hâm, học giả đã cung cấp nền kinh học cho ông.`

### 5.3 **Nghi vấn** — "khởi nghĩa Xích Mi" bị gán sai vai, và nguyên nhân bị cắt mất một vế

> *"lạm phát và nạn đói dẫn tới khởi nghĩa Xích Mi, và ông bị giết năm 23 CN"*

Hai điểm:
- Câu đặt cạnh nhau khiến người đọc hiểu Xích Mi giết ông. Không phải — xem 5.2. Có **hai** phong trào lớn: Lục Lâm (lật ông) và Xích Mi (lật Canh Thuỷ Đế sau đó).
- Nguyên nhân gần nhất của nạn đói là **trận vỡ Hoàng Hà năm 11 CN**, chứ không chỉ là hệ quả tiền tệ. Chính sự kiện này mới sinh ra lời sấm rằng ông đã mất thiên mệnh — một chi tiết ăn khớp rất chặt với luận điểm mở đầu của mục (ông dùng thiên mệnh để lên, rồi bị thiên mệnh dùng ngược lại) mà mục đang bỏ qua.

→ **Câu thay thế:** `Phần lớn thất bại nhanh; trận vỡ Hoàng Hà năm 11 CN cộng với lạm phát sinh nạn đói và hàng loạt khởi nghĩa nông dân — Lục Lâm và Xích Mi. Quân Lục Lâm hạ Trường An năm 23 CN và ông bị giết trong trận ấy.`

### 5.4 **Nghi vấn** — `Kế thừa từ: CH03-BCE01-10 · kế thừa · trực tiếp` không khớp với chính "Vì sao chọn"

Đã mở đích đọc tên: `CH03-BCE01-10 · **Lưu Hướng**` (Liu Xiang, 77–6 TCN). Nhưng phần "Vì sao chọn" của chính mục này nêu **Lưu Hâm** (Liu Xin, con của Lưu Hướng) là *"học giả đã cung cấp nền kinh học cho ông"* — và đó mới là người đúng: Lưu Hâm là quốc sư của Vương Mãng, người đẩy Cổ văn kinh học và Chu lễ làm nền cho chương trình cải cách.

Lưu Hướng mất năm 6 TCN, khi Vương Mãng 39 tuổi và chưa nắm quyền — hai người có cùng thời ở triều nên `trực tiếp` không nghịch niên đại, nhưng **người đúng cho quan hệ này là Lưu Hâm**, và Lưu Hâm không có mục riêng trong atlas (đã kiểm 221 mục). Đây là dạng lỗi quy tắc 8: ID trỏ đúng một người có thật, sai người cần trỏ.

→ **Sửa:** đổi dòng thành `- Lưu Hâm · kế thừa · trực tiếp` (dùng tên, vì không có ID), hoặc giữ `CH03-BCE01-10` nhưng hạ xuống `qua trường phái` và nói rõ trong phần văn xuôi rằng kênh truyền là Lưu Hâm.

### 5.5 Liên kết còn lại — đã mở đích, đúng

| Dòng | Đích | Tên thật | Nhận xét |
|---|---|---|---|
| Kế thừa từ `CH03-BCE02-01` | — | **Đổng Trọng Thư** | đúng: thiên mệnh / thiên nhân cảm ứng là nền lý luận cho việc soán ngôi. Đúng chiều |
| Ảnh hưởng tới `CH04-CE01-04` | — | Hán Quang Vũ Đế | `phản bác · trực tiếp`, đối xứng với `-04`. Đúng |

### 5.6 **Nghi vấn** — "lần đầu thiên mệnh được dùng để chính đáng hoá soán ngôi không qua chiến tranh": không quy thuộc

Mệnh đề tối cao viết như sự kiện. Nội dung thì đứng được (mô hình **thiện nhượng** 禪讓 trước đó chỉ có trong truyền thuyết Nghiêu–Thuấn; Vương Mãng là lần áp dụng lịch sử đầu tiên), nhưng theo yêu cầu trung lập, mệnh đề tối cao phải có chủ thể phát ngôn.
→ **Sửa:** `… — giới nghiên cứu coi đây là lần đầu học thuyết thiên mệnh được dùng để chính đáng hoá một cuộc soán ngôi không qua chiến tranh, theo mô hình thiện nhượng vốn trước đó chỉ có trong truyền thuyết Nghiêu–Thuấn.`

---

## 6. `CH04-CE01-04` · Hán Quang Vũ Đế

**Q-ID.** `Q7268` = "Emperor Guangwu of Han" / vi "Hán Quang Vũ Đế". Đúng người. P569 = −5-01-15, P570 = 57-03-29. Mục ghi `5 TCN – 57 CN`, **Cao** — khớp chính xác tới ngày.

**Con số: ĐÚNG.** Phục Hán **25 CN** — đúng (ông xưng đế năm 25; thống nhất xong cả nước năm 36). Dời đô Lạc Dương — đúng. Dập khởi nghĩa Hai Bà Trưng **năm 43 CN** — đúng (khởi nghĩa 40 CN, chiến dịch Mã Viện kết thúc 43).
*Nguồn dùng:* Wikidata Q7268; Wikipedia EN "Emperor Guangwu of Han", "Trưng sisters".

**Nguồn — Hans Bielenstein, *The Restoration of the Han Dynasty* (1953–1979): có thật, đúng thể loại (chuyên khảo, đăng nhiều kỳ trên *BMFEA*, 4 phần: 1953, 1959, 1967, 1979), đúng chủ đề — đây là công trình chuyên sâu nhất về đúng giai đoạn này.** Không có lỗi. Ghi khoảng năm `1953–1979` là cách ghi đúng cho một công trình nhiều kỳ.

### 6.1 **Sai** — "chính khái niệm trung hưng **mà ông tạo ra**"

> *"chính khái niệm **trung hưng mà ông tạo ra** là thứ các triều đại sau viện tới"*
> (và trước đó: *"Mô hình trung hưng ấy … thành tiền lệ mà sử học Đông Á dùng để đọc **mọi** giai đoạn gián đoạn về sau"*)

Khái niệm **trung hưng** (中興) có trước ông khoảng tám thế kỷ. Nguyên mẫu kinh điển là **Tuyên vương trung hưng** (宣王中興) — Chu Tuyên vương (trị vì k. 827/825–782 TCN), người khôi phục vương quyền nhà Chu sau thời Cộng Hoà nhiếp chính; đây là điển cố có sẵn trong truyền thống kinh học mà đời Hán dùng lại, chứ không phải Quang Vũ Đế sáng tạo. Cái ông làm là **lần hiện thực hoá quy mô đế chế đầu tiên** của khuôn ấy, không phải tạo ra khuôn.
*Nguồn dùng:* Wikipedia EN "King Xuan of Zhou" — *"He worked to restore royal authority after the Gonghe Regency."*

Chữ "mọi" cũng là phóng đại không kiểm được.

→ **Câu thay thế:** `Quang Vũ Đế được chọn theo độ bền (b) và counterfactual (d): Đông Hán tồn tại gần hai thế kỷ sau ông, và triều ông là lần đầu khuôn trung hưng — vốn có sẵn trong kinh điển từ điển cố Chu Tuyên vương — được thực hiện ở quy mô một đế chế, nên thành tiền lệ cụ thể mà các triều sau viện tới.`

### 6.2 **Thể thức** — ứng viên bị loại không cùng lĩnh vực theo nghĩa §5

> *"Ứng viên cùng thời là Công Tôn Thuật và Ngỗi Hiêu, hai thủ lĩnh cát cứ ông đánh bại."*

Đã kiểm: **cả hai có thật, đúng là cùng thời, và đúng là bị ông đánh bại** — Công Tôn Thuật xưng đế ở Thành Gia (Ích Châu, Tứ Xuyên ngày nay), Ngỗi Hiêu cát cứ vùng đông Cam Túc. Đã đối chiếu 221 mục: **cả hai đều không có mục riêng trong atlas**, nên không vi phạm quy tắc 6.
*Nguồn dùng:* Wikipedia EN "Emperor Guangwu of Han".

Nhưng về **thể thức §5** thì đây là một lập luận rỗng: "người này vượt trội vì đã đánh bại hai người kia" không phải so sánh theo tiêu chí (a)–(d), mà là nhắc lại kết quả quân sự. Hai kẻ bại trận không bao giờ là ứng viên thật cho một atlas ảnh hưởng tư tưởng. Ứng viên thật cùng thời cùng lĩnh vực nên là **Canh Thuỷ Đế (Lưu Huyền)** — người thực sự dựng lại nhà Hán trước ông năm 23 và sau đó mất ngôi — vì đó mới là một đánh đổi có nội dung.

→ **Câu thay thế:** `Ứng viên cùng thời là Canh Thuỷ Đế (Lưu Huyền), người xưng Hán trước ông hai năm và hạ được Vương Mãng, và Công Tôn Thuật, người xưng đế ở Thành Gia. Quang Vũ Đế được chọn theo độ bền (b): chính quyền của Canh Thuỷ Đế đổ sau hai năm, còn khuôn ông dựng trụ gần hai thế kỷ.`

### 6.3 **Thiếu** — `Ảnh hưởng tới` chỉ có một dòng, và là một mệnh đề trừu tượng

`- Khuôn trung hưng trong sử học Đông Á · kế thừa · qua trường phái` là mục duy nhất. Với một nhân vật mà chính mục khẳng định "các triều đại sau viện tới", việc không nêu được **một** người cụ thể nào là lỗ hổng. Ứng viên hiển nhiên nằm ngay trong atlas: nhóm CE01 có `CH04-CE01-11` **Ban Cố** — người viết Hán thư dưới triều Minh Đế, con ông, và chính Quang Vũ Đế là người cho phép sử quan nhà Hán viết lại lịch sử đứt đoạn Vương Mãng theo khuôn ấy.

### 6.4 Liên kết — đã mở đích, đúng

`Kế thừa từ: CH04-CE01-03 · phản bác · trực tiếp` → Vương Mãng. Đúng người, đúng chiều, đối xứng với dòng `Ảnh hưởng tới` ở `-03`. Niên đại khớp (hai người cùng sống). **Không có lỗi.**

### 6.5 Một điểm **đúng** đáng giữ

Câu *"Dưới triều ông, năm 43 CN, nhà Hán cũng dập cuộc khởi nghĩa Hai Bà Trưng ở Giao Chỉ"* là một chi tiết đặt đúng chỗ: nó gắn nhân vật với vùng Đông Nam Á mà nhóm này không có mục nào, và nó **không** tô hồng nhân vật. Giữ.

---

## 7. `CH04-CE01-05` · Seneca

**Q-ID.** `Q2054` = "Seneca" / vi "Seneca". Đúng người (Seneca Trẻ, không nhầm sang Seneca Cha — P570 = 65-04-12 xác nhận). Mục ghi `k. 4 TCN – 65 CN`, **Trung bình** — khớp.

**Nguồn — Emily Wilson, *The Greatest Empire: A Life of Seneca* (2014): ĐÚNG mọi mặt.** Có thật, Oxford University Press 2014, ISBN 978-0199926640, **đúng thể loại (tiểu sử/chuyên khảo, không phải bản dịch)**, đúng chủ đề. *Nguồn dùng:* Wikipedia EN "Emily Wilson (classicist)", "Seneca the Younger" (mục thư mục).

**Nguồn — Seneca, *Thư gửi Lucilius*: có thật, là nguồn sơ cấp đúng chỗ.** Mục **không** ghi số thư nào — đúng quy tắc 3 CONTRIBUTING ("không ghi số chương nếu chưa mở mục lục"). Giữ cách làm này.

### 7.1 **Thể thức + đúng niên đại** — ứng viên bị loại: phần này làm **đúng**, ghi để đối chiếu

> *"Ứng viên cùng truyền thống là Musonius Rufus, thầy của Epictetus và **cũng sống cùng thời**, và Epictetus ở **thế hệ sau**."*

Đã kiểm cả hai vế:
- **Musonius Rufus**: triết gia Khắc kỷ La Mã TK 1, dạy ở Rome dưới thời Nero, **bị đày năm 65** — đúng năm Seneca chết. Thật sự cùng thời. Đúng là thầy của Epictetus. Đúng là chỉ còn mảnh (một tập trích bài giảng).
- **Epictetus**: mục ghi rõ "ở thế hệ sau" — **khai báo đúng**, không giấu lệch thế hệ.
- Đã đối chiếu 221 mục: **cả Musonius lẫn Epictetus đều không có mục riêng** trong atlas, nên không vi phạm quy tắc 6.
*Nguồn dùng:* Wikipedia EN "Gaius Musonius Rufus".

**Đây là mục làm đúng nhất về ứng viên bị loại trong cả nhóm**: một người thật sự cùng thời, một người khai báo rõ là khác thế hệ, không ai trùng với mục đã chọn. Đối chiếu với `-06`, `-07`, `-08`, `-10` bên dưới.

### 7.2 **Nghi vấn** — "thể văn ấy … là **đóng góp riêng của ông**"

> *"Thể văn ấy — triết học như lời khuyên có địa chỉ — là đóng góp riêng của ông"*

Không đứng được. Thư triết học gửi một người cụ thể có trước Seneca ít nhất ba thế kỷ: **Epicurus** (*Thư gửi Menoeceus*, *Thư gửi Herodotus*, *Thư gửi Pythocles*), và ở Latinh có **Cicero** (*De Senectute* đề tặng Atticus, *Tusculanae Disputationes*, toàn bộ tập *Ad Familiares*). Thể **consolatio** — an ủi người đang mất mát — là một thể loại hùng biện cổ điển đã định hình trước ông, với Crantor (*Peri Penthous*) là nguyên mẫu; chính Seneca viết ba bài *Consolatio* theo thể đã có sẵn.
*Nguồn dùng:* Wikipedia EN "Consolatio" — *"one of the most popular classical rhetoric topics"*.

Cái thật sự riêng của Seneca là **quy mô và tính hệ thống** (124 lá thư soạn thành một chương trình tu dưỡng liên tục), không phải việc phát minh ra thể loại.

→ **Câu thay thế:** `Ông không phát minh thể thư triết học — Epicurus và Cicero đã dùng — nhưng là người đầu tiên dựng cả một chương trình tu dưỡng liên tục bằng thể ấy, và đó là lý do ông được đọc liên tục trong khi phần lớn Khắc kỷ Hy Lạp thất truyền.`

### 7.3 **Nghi vấn** — `Ảnh hưởng tới: CH04-CE02-07 (Marcus Aurelius) · kế thừa · qua trường phái`

Đã mở đích đọc tên: `CH04-CE02-07 · **Marcus Aurelius**` (121–180). Đúng người, đúng chiều, niên đại thuận.

Nhưng **không có bằng chứng Marcus đọc Seneca**: *Suy tưởng* không nhắc tên Seneca một lần nào, và kênh Khắc kỷ của Marcus là Epictetus (qua bản ghi của Arrian, do Junius Rusticus đưa cho ông). Điểm tự tố cáo nằm ngay trong atlas: mục `CH04-CE02-07` viết *"Ứng viên cùng truyền thống là **Epictetus, người thầy ông đọc và trích**"* — tức atlas biết kênh thật là Epictetus, nhưng vì Epictetus không có mục riêng nên dòng `Kế thừa từ` của Marcus phải mượn Seneca thay vào.

Đây đúng là dạng lỗi quy tắc 8: ID trỏ đúng người, nhưng quan hệ được gán không có thật. `qua trường phái` có đỡ bớt (cả hai cùng trường phái Khắc kỷ), nhưng loại quan hệ `kế thừa` vẫn khẳng định một dòng truyền không tồn tại.

→ **Sửa:** `- CH04-CE02-07 · tương đồng độc lập · suy đoán học giả`, hoặc bỏ dòng này và thay bằng `- Epictetus và truyền thống Khắc kỷ La Mã · kế thừa · qua trường phái`. Cần sửa **đối xứng** ở `CH04-CE02-07` dòng `Kế thừa từ: CH04-CE01-05`.

### 7.4 Liên kết còn lại — đã mở đích, đúng

| Dòng | Đích | Tên thật | Nhận xét |
|---|---|---|---|
| Kế thừa từ `CH03-BCE03-07` | — | **Zeno xứ Citium** | người sáng lập Khắc kỷ. Đúng, `qua trường phái` đúng mức |
| Kế thừa từ `CH03-BCE01-12` | — | **Posidonius** (k. 135–51 TCN) | đúng: Seneca trích Posidonius nhiều lần trong *Thư gửi Lucilius*. Niên đại thuận |

### 7.5 Một điểm **đúng** đáng giữ

Câu *"Khoảng cách giữa lời khuyên và đời sống của chính ông là điểm bị phê phán từ thời cổ"* — quy thuộc đúng (phê phán cổ đại có thật: Suillius trong Tacitus, *Annales* XIII; Cassius Dio). Không tô vẽ. Giữ.

> **Ghi chú về từ vựng liên kết** (áp dụng cho toàn báo cáo): theo `atlaslib/common.py` dòng 78–79, trường thứ hai là **loại quan hệ** (`kế thừa · tổng hợp · phản bác · tương đồng độc lập`) và trường thứ ba là **mức bằng chứng** (`trực tiếp · qua trường phái · suy đoán học giả`) — **không** phải mức độ tiếp xúc cá nhân. Vì thế `trực tiếp` giữa hai người cách nhau hàng thế kỷ là hợp lệ khi người sau **trích đích danh** người trước. Các nhận xét liên kết dưới đây đọc theo nghĩa ấy.

---

## 8. `CH04-CE01-06` · Philo xứ Alexandria

**Q-ID.** `Q189597` = "Philo of Alexandria" (không có nhãn vi). Đúng người. P569 = −15, P570 = 45 và 50. Mục ghi `k. 15 TCN – 50 CN`, **Trung bình** — hợp lệ. (Dạng thường gặp hơn trong tài liệu là `k. 20 TCN – k. 50 CN`; chênh 5 năm, nằm trong dung sai, không phải lỗi.)

**Vùng `Trung Đông/Bắc Phi` cho Alexandria: ĐÚNG** theo danh sách 9 vùng. (Đối chiếu với lỗi vùng ở mục `-08` bên dưới.)

**Nguồn — Maren Niehoff, *Philo of Alexandria: An Intellectual Biography* (2018): ĐÚNG mọi mặt.** Có thật, Yale University Press / Anchor Yale Bible Reference Library, 2018, ISBN 978-0-300-17523-3. Đúng thể loại (tiểu sử trí thức, chuyên khảo), đúng chủ đề, là công trình mới nhất và trung tâm nhất về đúng nhân vật này.
*Nguồn dùng:* Wikipedia EN "Anchor Bible Series" (mục thư mục); Open Library.

**Nguồn — Philo, *De Opificio Mundi* và *Legum Allegoriae*: có thật, đúng tên Latinh, và là đúng hai tác phẩm minh hoạ cho điều được dẫn** (*De Opificio Mundi* mở bộ Chú giải Ngũ thư; *Legum Allegoriae* là chính bộ chú giải ngụ ý). Mục **không** ghi số quyển — đúng quy tắc 3. Giữ.

### 8.1 **Sai** — "Aristobulus xứ Paneas" là định danh đã bị bác, và ông **không** cùng thời với Philo

> *"Ứng viên **cùng vùng cùng thời** là Aristobulus xứ Paneas trước ông, người cũng đọc ngụ ý nhưng chỉ còn mảnh vụn"*

Hai lỗi trong một câu:

1. **Tên sai.** Nhân vật này nay được gọi là **Aristobulus xứ Alexandria** (hoặc Aristobulus phái Tiêu dao). *"Aristobulus xứ Paneas"* là một định danh cũ **đã bị giới nghiên cứu bác bỏ** — Wikipedia EN ghi nguyên văn: *"also called Aristobulus the Peripatetic and **once believed to be** Aristobulus of Paneas"*. Mục đang dùng cách gọi sai.
2. **Không cùng thời, và câu tự mâu thuẫn.** Aristobulus hoạt động **k. 181–124 TCN**; Philo sống k. 15 TCN – 50 CN. Cách nhau **khoảng 150–200 năm**. Câu vừa viết "cùng thời" vừa viết "trước ông" trong cùng một mệnh đề — đúng kiểu lỗi hệ thống (i) mà quy tắc 5 CONTRIBUTING liệt kê (Tử Sản / Quản Trọng, Ban Siêu / Trương Khiên).
*Nguồn dùng:* Wikipedia EN "Aristobulus of Alexandria".

### 8.2 **Thể thức** — hệ quả: mục `-06` có **không** ứng viên bị loại nào thật sự cùng thời

Ứng viên thứ hai được nêu là **Josephus**, kèm khai báo *"chọn riêng ở mục sau"* (`CH04-CE01-09`) — khai báo này đúng quy tắc 6 và nên giữ, nhưng nó có nghĩa Josephus không phải một ứng viên bị loại. Cộng với 8.1:

| Người được nêu | Có phải ứng viên bị loại thật? |
|---|---|
| Aristobulus xứ Alexandria | **không cùng thời** (sớm hơn ~175 năm) |
| Josephus | **đã được chọn** ở `CH04-CE01-09`; ngoài ra sinh năm 37, tức ~13 tuổi khi Philo mất — cũng không cùng thời |

Vậy mục này nêu **0** ứng viên bị loại hợp lệ. §5 đòi "nêu ĐÍCH DANH 1–2 người cùng lĩnh vực, cùng thời đã được cân nhắc". Vi phạm.

→ **Câu thay thế** (dùng người cùng thời thật, hoặc nói thẳng là không có — quy tắc 5 cho phép và khuyến khích vế thứ hai):
`Không có ứng viên cùng thời cùng vùng nào ngang tầm: người đọc ngụ ý gần nhất, Aristobulus xứ Alexandria, sống trước ông gần hai thế kỷ và chỉ còn mảnh vụn, còn Josephus thuộc thế hệ sau và được chọn riêng ở mục sau. Đó tự nó là một phát hiện về tư liệu — bộ Philo là thứ gần như duy nhất còn nguyên từ Do Thái giáo Hy Lạp hoá. Philo được chọn theo tính nguyên bản (c) và counterfactual (d): bộ phương pháp của ông là cái Origen và Augustinô tiếp quản.`

### 8.3 **Nghi vấn** — mệnh đề tối cao không quy thuộc, và có phản ví dụ

> *"Đây là **nỗ lực có hệ thống sớm nhất còn lại** nhằm hoà một truyền thống mặc khải với triết học Hy Lạp."*

Chữ "còn lại" gánh gần hết trọng lượng, và nó loại được Aristobulus (chỉ còn mảnh). Nhưng vẫn còn phản ví dụ **còn nguyên vẹn**:

- **Sách Khôn ngoan (Wisdom of Solomon)** — soạn bằng tiếng Hy Lạp bởi một tác giả Do Thái ở Alexandria, phần lớn học giả định niên đại **TK 1 TCN**, tức **trước Philo**, và còn trọn vẹn trong Bản Bảy Mươi. Nội dung là đúng thao tác ấy: khái niệm Sophia được diễn giải bằng từ vựng Khắc kỷ–Platon và ghép vào mạch mặc khải Do Thái.
- **Thư Aristeas** (TK 3 hoặc đầu TK 2 TCN), còn nguyên, cũng làm thao tác hoà giải ấy ở dạng tường thuật chứ không ở dạng chú giải.
*Nguồn dùng:* Wikipedia EN "Book of Wisdom", "Letter of Aristeas".

Phản ví dụ không phá được mệnh đề nếu thêm chữ hạn định đúng (Philo là người đầu tiên làm việc ấy thành **một bộ chú giải có phương pháp nhất quán trên toàn bộ Ngũ thư**), nhưng mệnh đề như đang viết thì quá rộng — và **không quy thuộc**, tức không nói ai cho rằng vậy. Theo yêu cầu trung lập, mệnh đề tối cao không quy thuộc là lỗi.

→ **Câu thay thế:** `Giới nghiên cứu coi bộ chú giải của ông là nỗ lực sớm nhất còn lại nhằm hoà một truyền thống mặc khải với triết học Hy Lạp một cách có hệ thống và xuyên suốt toàn bộ Ngũ thư — các văn bản trước đó như Sách Khôn ngoan làm thao tác ấy rời rạc hơn, còn Aristobulus xứ Alexandria thì chỉ còn mảnh vụn.`

### 8.4 Liên kết — đã mở đích đọc tên, **tất cả đúng**

| Dòng | Đích | Tên thật | Nhận xét |
|---|---|---|---|
| Kế thừa từ `CH03-BCE04-01` | — | **Plato** | đúng: Philo là người Platon Trung kỳ. Mức `qua trường phái` đúng |
| Kế thừa từ `CH03-BCE03-07` | — | **Zeno xứ Citium** | đúng: phương pháp ngụ ý của Philo lấy từ thực hành Khắc kỷ. Mức `qua trường phái` đúng |
| Ảnh hưởng tới `CH04-CE03-02` | — | **Origen** | đúng người, đúng chiều. `trực tiếp` hợp lệ: Origen trích Philo đích danh |

### 8.5 Một điểm **đúng** đáng giữ

*"Nghịch lý là ảnh hưởng của ông đi về phía Kitô giáo … trong khi Do Thái giáo rabbi gần như không giữ ông"* — đúng và được xác nhận: *"His allegorical exegesis was important for many Christian Church Fathers, but he had very little reception history within Rabbinic Judaism."* Trung lập, không bên nào bị hạ thấp. Giữ.

---

## 9. `CH04-CE01-07` · Pliny Cả

**Q-ID.** `Q82778` = "Pliny the Elder" / vi "Gaius Plinius Secundus". Đúng người (Pliny Cả, không nhầm sang Pliny Trẻ `Q168707`). Xem bảng ở mục 0 về `Cao`.

**Con số "37 quyển": ĐÚNG.** Đã kiểm mục lục: *"The Natural History consists of **37 books**"*, chia thành 10 tập. **Và mục lục Quyển I: ĐÚNG** — *"Book I serves as Pliny's preface, explaining his approach and providing a table of contents"*; Pliny gọi nó là *summarium*, kèm *indices auctorum*.
*Nguồn dùng:* Wikipedia EN "Natural History (Pliny)".

**Nguồn — Trevor Murphy, *Pliny the Elder's Natural History: The Empire in the Encyclopedia* (2004): ĐÚNG mọi mặt.** Có thật, Oxford University Press 2004, đúng thể loại (chuyên khảo), đúng chủ đề. *Nguồn dùng:* Open Library.

**Cái chết năm 79 qua lời Pliny Trẻ: ĐÚNG** (Thư 6.16 gửi Tacitus). Mục không ghi số thư — đúng quy tắc 3.

### 9.1 **Nghi vấn** — `Kế thừa từ: CH03-BCE01-11` trỏ **Strabo**, người Pliny có lẽ chưa từng dùng

Đã mở đích đọc tên: `CH03-BCE01-11 · **Strabo**` (k. 64 TCN – 24 CN). Đúng người, niên đại thuận.

Nhưng phần "Sources" của *Naturalis Historia* liệt kê các nguồn chính của Pliny là **Varro, Agrippa, Aristotle, Juba II, Theophrastus, Herodotus, Thucydides, Diodorus Siculus** — **Strabo không xuất hiện**. Đây là một điểm quen thuộc trong nghiên cứu Pliny: ông không nhắc Strabo, dù hai người gần như cùng thời và cùng viết về địa lý.
*Nguồn dùng:* Wikipedia EN "Natural History (Pliny)", mục **Sources** (tìm chuỗi "Strabo" trong toàn bài: **không có**).

Người đúng cho vị trí này là **Theophrastus** — Pliny tự dịch Theophrastus từ Hy Lạp sang Latinh, nêu tên ông trong *Indices*, và dùng *Peri Lithōn* làm nguồn về khoáng vật. Đã đối chiếu 221 mục: **Theophrastus không có mục nào trong atlas**, nên dùng tên trần là hợp lệ theo §5 ("ID **hoặc tên**").

→ **Sửa:** thay `- CH03-BCE01-11 · kế thừa · qua trường phái` bằng `- Theophrastus · kế thừa · trực tiếp` (Pliny nêu tên ông trong Indices và đã dịch ông), hoặc `- Varro · kế thừa · trực tiếp`.

(`CH03-BCE04-02` → **Aristotle**, `kế thừa · qua trường phái`: **đúng** — Pliny dùng chính phân loại động/thực/khoáng của Aristotle làm khung và dựa vào ông cho phần động vật.)

### 9.2 **Nghi vấn** — "việc ghi nguồn ấy khiến tác phẩm thành kho lưu giữ hàng trăm công trình nay đã mất"

Câu này đúng ở kết quả, nhưng mô tả cơ chế thì quá rộng. *Indices auctorum* của Pliny **không** phải danh sách những gì ông thực sự đọc: *"His indices auctorum sometimes list the authorities he actually consulted, **though not exhaustively**; in other cases, they cover the principal writers on the subject, **whose names are borrowed second-hand** from his immediate authorities."* Tức một phần danh sách là tên chép lại từ nguồn trung gian.

Điều này cũng ăn khớp với câu cuối của chính mục (*"chính ông cũng không phân biệt quan sát với lời đồn"*) — nên sửa là làm mục nhất quán hơn, không phải hạ thấp nhân vật.
→ **Câu thay thế:** `Chính danh sách ấy khiến tác phẩm thành kho lưu giữ tên tuổi và nội dung của hàng trăm công trình nay đã mất, dù không phải tên nào trong danh sách cũng là sách ông thực sự đọc — một phần là tên chép lại từ nguồn trung gian.`

### 9.3 **Nghi vấn nhẹ** — "hơn hai trăm bản chép tay còn lại"

Con số đúng theo nghĩa đen nhưng thấp hơn con số chuẩn: *"In total there are some **307** extant medieval manuscripts of the work"*. Viết "hơn hai trăm" khi con số là 307 làm yếu đúng luận điểm mà mục đang dựng (độ bền b).
→ **Sửa:** `với khoảng ba trăm bản chép tay trung cổ còn lại`.
*Nguồn dùng:* Wikipedia EN "Natural History (Pliny)", mục Manuscripts.

### 9.4 **Thể thức** — ứng viên bị loại: đạt mức tối thiểu, nhưng sát ngưỡng

> *"Ứng viên **cùng loại** là Celsus … và Dioscorides, **chọn riêng ở mục sau**."*

- **Celsus**: đã kiểm, có thật — Aulus Cornelius Celsus, k. 25 TCN – k. 50 CN, nhà bách khoa La Mã, và mô tả *"bộ bách khoa trước đó mà nay chỉ còn phần y học"* là **chính xác** (chỉ *De Medicina* còn lại từ một bộ bách khoa lớn hơn gồm cả nông học, quân sự, hùng biện, luật). Khoảng sống của ông chồng lên Pliny khoảng 27 năm, nên "cùng thời" tạm đứng được — nhưng bộ *Artes* của ông viết dưới thời Augustus–Tiberius, khi Pliny còn nhỏ. Mục **tránh** chữ "cùng thời" và viết "cùng loại"; đó là cách nói trung thực nhưng cũng là cách lách yêu cầu §5.
- **Dioscorides**: khai báo "chọn riêng ở mục sau" — **đúng quy tắc 6**.
- Đã đối chiếu 221 mục: Celsus **không** có mục riêng.
*Nguồn dùng:* Wikipedia EN "Aulus Cornelius Celsus".

Kết luận: còn **một** ứng viên bị loại thật. Đạt mức tối thiểu "1–2" của §5, nhưng nên nói rõ quan hệ thế hệ.
→ **Sửa:** `Ứng viên gần nhất là Celsus, nhà bách khoa thế hệ trước (k. 25 TCN – k. 50 CN) mà bộ Artes nay chỉ còn phần y học, và Dioscorides, chọn riêng ở mục sau.`

---

## 10. `CH04-CE01-08` · Dioscorides

**Q-ID.** `Q297776` = "Pedanius Dioscorides". Đúng người. P569 = 40, P570 = 90. Mục ghi `k. 40–90 CN`, **Thấp** — hợp lệ (và để Thấp là đúng: niên đại ông thực sự chỉ là ước lượng).

### 10.1 Con số — **ĐÚNG cả ba**

| Mục ghi | Kiểm | Kết quả |
|---|---|---|
| **năm quyển** | *"a **5-volume** Greek encyclopedic pharmacopeia"* | đúng |
| **khoảng sáu trăm loài thực vật** | *"In total, **about 600 plants** are covered"* | đúng |
| **gần một nghìn vị thuốc** | *"and **around 1,000 medicines** made from them"* | đúng |

*Nguồn dùng:* Wikipedia EN "Dioscorides", "De materia medica".

### 10.2 Nguồn — **ĐÚNG cả hai, kể cả số hiệu bản thảo**

- **Lily Y. Beck (2005)**: có thật (Olms-Weidmann, 2005), và **được ghi đúng thể loại là "bản dịch"** — đây đúng là bản dịch Anh ngữ đầy đủ, không phải chuyên khảo. Đối chiếu với lỗi Fried & Unguru ở quy tắc 7 CONTRIBUTING: mục này **không** mắc lỗi ấy.
- **Vienna Dioscurides, Thư viện Quốc gia Áo, Med. Gr. 1**: **số hiệu ĐÚNG**. Ký hiệu chuẩn là `Wien, Österreichische Nationalbibliothek, **Cod. med. gr. 1**` (cũng viết `Cod. Vindob. med. gr. 1`). Mục viết `Med. Gr. 1` — đúng nội dung, chỉ thiếu tiền tố `Cod.` và viết hoa khác quy ước.
- **Niên đại "năm 512": ĐÚNG** — bản Juliana Anicia soạn ở Constantinople **512/513 CN**.
*Nguồn dùng:* Wikipedia EN "De materia medica" (*"the lavishly illustrated Vienna Dioscurides (the Juliana Anicia Codex), written in the original Greek in Byzantine Constantinople in 512/513 AD"*); "Manuscripts of the Austrian National Library" (*"Cod. Vindob. med. gr. 1, the Vienna Dioscurides, Constantinople, c. 512"*).

→ **Sửa (nhỏ):** `Vienna Dioscurides, Thư viện Quốc gia Áo, Cod. med. gr. 1`.

### 10.3 **Sai** — `vùng: Châu Âu` cho một người xứ Cilicia

> `nơi: Anazarbus xứ Cilicia … | vùng: **Châu Âu**`

Anazarbus nằm ở Cilicia, nay thuộc tỉnh Adana, **miền nam Thổ Nhĩ Kỳ** — Anatolia, không phải châu Âu dưới bất kỳ cách chia nào trong danh sách 9 vùng của atlas.

Bằng chứng mạnh nhất là **mâu thuẫn ngay trong cùng nhóm**: `CH04-CE01-02` **Phaolô thành Tarsus** — Tarsus cũng ở **Cilicia**, cách Anazarbus khoảng 70 km — được gán `vùng: **Trung Đông/Bắc Phi**`. Hai người cùng một xứ, cùng một nhóm, hai vùng khác nhau.

Lỗi này lan ra ngoài phạm vi rà: `CH04-CE02-06` **Galen** (Pergamon, cũng Anatolia) cũng được gán `Châu Âu`. Nghĩa là file đang chạy **hai quy ước mâu thuẫn** cho Anatolia, và nhóm CE01 chứa cả hai.
*Nguồn dùng:* vị trí Anazarbus (Adana, Thổ Nhĩ Kỳ) — Wikipedia EN "Dioscorides"; đối chiếu nội bộ `content/ch04.md` dòng 26 và 124.

→ **Sửa:** `vùng: Trung Đông/Bắc Phi` cho `-08`, và Owner cần chốt một quy ước duy nhất cho Anatolia rồi áp lại cho `CH04-CE02-06`. Lưu ý: đổi `-08` sang Trung Đông/Bắc Phi **không** phá yêu cầu §5 về 3 vùng — CE01 vẫn còn Châu Âu nhờ `-05` Seneca và `-07` Pliny.

### 10.4 **Thể thức** — ứng viên bị loại: **0** người hợp lệ

> *"Ứng viên **cùng thời** là Pliny Cả, **chọn ở mục trước**, và Crateuas **ở thế kỷ 1 TCN**, người vẽ cây thuốc nhưng chỉ còn mảnh."*

| Người được nêu | Có phải ứng viên bị loại thật? |
|---|---|
| Pliny Cả | **đã được chọn** ở `CH04-CE01-07` — mục tự khai báo, đúng quy tắc 6, nhưng vì thế không phải ứng viên bị loại |
| Crateuas | **không cùng thời**: thầy thuốc của Mithridates VI, TK 1 **TCN**, sớm hơn Dioscorides hơn một thế kỷ. Mục tự ghi "ở thế kỷ 1 TCN" ngay sau chữ "cùng thời" |

Vậy câu mở đầu bằng "Ứng viên **cùng thời**" rồi liệt kê hai người, **không ai** là ứng viên cùng thời bị loại. Giống hệt cấu trúc lỗi ở `-06`. Vi phạm §5.

→ **Câu thay thế** (theo đúng chỉ dẫn quy tắc 5: nếu không có ai thì viết thẳng là không có):
`Không có đối thủ cùng thời nào trong ngành dược: Crateuas, người vẽ cây thuốc, sống trước ông hơn một thế kỷ và chỉ còn mảnh, còn Pliny Cả viết dược liệu như một phần của bộ bách khoa và đã được chọn ở mục trước. Khoảng trống ấy tự nó nói lên vị trí của ông. Dioscorides được chọn theo độ bền (b): bản chép Vienna Dioscurides năm 512 là một trong các bản thảo khoa học cổ nhất còn nguyên, và tác phẩm được dùng liên tục tới thế kỷ 17.`

### 10.5 **Nghi vấn** — `Kế thừa từ: CH02-BCE05-04` trỏ **Hippocrates**: sai dòng truyền

Đã mở đích đọc tên: `CH02-BCE05-04 · **Hippocrates xứ Cos**`. Đúng người, niên đại thuận.

Nhưng Hippocrates không phải tiền thân của *De materia medica*: tập Hippocrates là y học lâm sàng và lý thuyết thể dịch, **không phải một bộ dược điển**. Dòng truyền thật của Dioscorides, theo chính bài về ông, là **Theophrastus** (*Historia Plantarum*, *De Causis Plantarum* — phân loại thực vật) và **Crateuas** (dược đồ có hình vẽ), cộng Sextius Niger. Wikipedia EN "De materia medica" đặt ông đúng vào mạch ấy khi so với *"the natural history studies of Aristotle and **Theophrastus**"*.

Trớ trêu là mục `-08` tự nêu Crateuas trong phần "Vì sao chọn" mà không đưa ông vào `Kế thừa từ`.

→ **Sửa:** `- Crateuas · kế thừa · qua trường phái` và/hoặc `- Theophrastus · kế thừa · qua trường phái` thay cho dòng Hippocrates. (Cả hai đều không có mục riêng trong atlas — đã kiểm 221 mục — nên dùng tên trần là hợp lệ.)

### 10.6 Liên kết còn lại — đã mở đích, **đúng**

`Ảnh hưởng tới: CH04-CE02-06` → **Galen** (129–216). Đúng người, đúng chiều, niên đại thuận, và có thật về nội dung: Galen dùng và phê bình Dioscorides. `qua trường phái` là mức an toàn; `trực tiếp` cũng biện hộ được vì Galen nêu tên ông.

### 10.7 Một điểm **đúng** đáng giữ

*"ông sắp xếp theo tác dụng dược lý chứ không theo thứ tự chữ cái"* — đây là luận điểm trung tâm của nghiên cứu Dioscorides hiện đại (John Riddle) và là lý do đúng để chọn ông. Giữ nguyên. Tương tự *"nói rõ mình đã tự đi xem cây ở nơi mọc"* — khớp với lời tựa của chính ông.

---

## 11. `CH04-CE01-09` · Josephus

**Q-ID.** `Q134461` = "Josephus". Đúng người. P569 = 37 và 38, P570 = 100.

**Niên đại cuộc chiến "66–73 CN": ĐÚNG.** Chiến tranh Do Thái–La Mã lần thứ nhất là **66–73/74 CN**. *Nguồn dùng:* Wikipedia EN "First Jewish–Roman War".

**Tiểu sử: ĐÚNG.** Chỉ huy quân Do Thái ở Galilee, đầu hàng Vespasianus năm 67 sau cuộc vây Yodfat, được trả tự do năm 69, theo Titus trong cuộc vây Jerusalem năm 70.

**Nguồn — Josephus, *Chiến tranh Do Thái* và *Cổ sử Do Thái*: có thật, đúng tên, là nguồn sơ cấp đúng chỗ.** Không ghi số quyển — đúng quy tắc 3.

### 11.1 **Thể thức — mục này làm ĐÚNG về ứng viên bị loại**

> *"Ứng viên cùng thời là Philo, **chọn ở mục trước** …, và **Justus xứ Tiberias**, đối thủ ông bút chiến mà tác phẩm đã mất."*

- **Justus xứ Tiberias: có thật, k. 35 – k. 100 CN** — tức **thật sự cùng thời**, cùng lĩnh vực (sử học), cùng vùng, cùng đề tài (ông viết *Lịch sử chiến tranh Do Thái* riêng), và **tác phẩm đúng là đã mất** (chỉ còn mảnh qua trích dẫn của người khác). Đã đối chiếu 221 mục: **không có mục riêng**.
- Mô tả "đối thủ ông bút chiến" cũng **đúng**: Josephus viết *Vita* chính là để đáp lại những khẳng định của Justus.
*Nguồn dùng:* Wikipedia EN "Justus of Tiberias".

**Cùng với `-02`, đây là một trong hai mục duy nhất của nhóm CE01 nêu được một ứng viên bị loại vừa cùng thời vừa chưa được chọn ở nơi khác.** Phần Philo thì khai báo đúng quy tắc 6.

Một điểm nhỏ: gọi Philo (mất k. 50) là "cùng thời" với Josephus (sinh 37) là kéo căng — Josephus khoảng 13 tuổi khi Philo mất. Nhưng vì Philo đã được khai báo là đã chọn, điều này không ảnh hưởng tới số ứng viên hợp lệ.

### 11.2 **Nghi vấn** — `độ tin cậy niên đại: Cao` là quá tự tin

Năm sinh 37/38 vững (Josephus tự ghi là năm thứ nhất đời Caligula). **Năm mất thì không**: mọi tài liệu ghi `k. 100` / `sau 100`, suy ra từ việc *Vita* nhắc tới cái chết của Agrippa II. Mức **Cao** tương ứng dung sai ±5 năm, tức khẳng định ta biết năm mất trong khoảng 95–105 — ta không biết.

Đây đúng là tình huống quy tắc 4 CONTRIBUTING mô tả: Wikidata ghi `+0100` nên lint báo sạch, nhưng con số ấy là ước lượng không nguồn.
→ **Sửa:** `độ tin cậy niên đại: Trung bình` (hoặc giữ Cao nhưng ghi `37 – k. 100 CN`).

### 11.3 **Thiếu** — bỏ mất *Vita*, chính là tác phẩm mà lập luận của mục cần

> *"ông viết Chiến tranh Do Thái và Cổ sử Do Thái — **hai bộ còn lại gần trọn**"*
> *"Vị trí đứng giữa khiến ông vừa phải biện hộ cho dân mình trước độc giả La Mã **vừa phải giải thích việc mình đổi phe**."*

Câu thứ hai mô tả chính xác nội dung của ***Vita* (Tự truyện)** — tác phẩm Josephus viết để tự bào chữa trước Justus — và của ***Contra Apionem*** (biện hộ cho Do Thái giáo trước độc giả Hy–La). Cả hai còn nguyên. Mục nêu luận điểm mà không nêu hai văn bản chứng minh nó, và vì thế cũng bỏ lỡ mối nối với Justus ở ngay đoạn dưới.
→ **Sửa:** `… ông viết Chiến tranh Do Thái và Cổ sử Do Thái, cùng hai tác phẩm ngắn hơn — Tự truyện (Vita) và Bác Apion — tất cả đều còn lại gần trọn …`

### 11.4 **Nghi vấn nhẹ** — nguồn thứ cấp lệch tâm, và năm in cần xác nhận

**Steve Mason, *Josephus and the New Testament*: có thật** (Hendrickson; bản 1 năm **1992**, bản 2 ghi **2002 hoặc 2003** tuỳ mục lục thư viện — mục ghi 2003, hợp lý nhưng nên xác nhận lại trên bìa sách). Đúng thể loại (chuyên khảo), đúng tác giả — Mason là một trong các chuyên gia Josephus hàng đầu.
*Nguồn dùng:* Open Library (trả về 1992 và 2002).

Nhưng **phạm vi sách lệch với luận điểm của mục**: cuốn này bàn Josephus **trong quan hệ với Tân Ước**, trong khi mục lại dựng luận điểm về Josephus như nguồn cho Judea TK 1 nói chung và về vị trí đứng giữa của ông. Nguồn trung tâm hơn: Tessa Rajak, *Josephus: The Historian and His Society*, hoặc chính bộ *Flavius Josephus: Translation and Commentary* do Mason chủ biên.
→ **Sửa:** cân nhắc thay hoặc bổ sung một nguồn đúng tâm hơn; nếu giữ, xác nhận lại năm in.

### 11.5 Liên kết — đã mở đích đọc tên, **đúng cả hai**

| Dòng | Đích | Tên thật | Nhận xét |
|---|---|---|---|
| Kế thừa từ `CH03-BCE02-04` | — | **Polybius** (k. 200–118 TCN) | đúng chiều; Josephus đọc và dùng Polybius. `qua trường phái` đúng mức |
| Ảnh hưởng tới `CH04-CE03-02` | — | **Origen** | đúng người, đúng chiều. Origen trích Josephus đích danh, nên `trực tiếp` cũng biện hộ được |

Dòng `Hiểu biết hiện đại về Judea thế kỷ 1 · kế thừa · trực tiếp` là một mệnh đề chứ không phải nhân vật/trào lưu, nhưng ở đây nó **đúng** và kiểm được — khác với dòng "toàn bộ lịch sử tư tưởng phương Tây" ở `-01`.

### 11.6 Một điểm **đúng** đáng giữ

*"Chính sự lấp lửng ấy làm tư liệu của ông vừa quý giá vừa phải đọc có bảo lưu"* — đặt đúng mức, không tô vẽ, không hạ thấp, và nói rõ giới hạn của nguồn. Đây là mẫu tốt.

---

## 12. `CH04-CE01-10` · Vương Sung

**Q-ID.** `Q319329` = "Wang Chong" / vi "Vương Sung". Đúng người. P569 = 27, P570 = 97. Mục ghi `27–97 CN`, **Cao** — khớp. (Một số tài liệu ghi mất "khoảng năm 100"; chênh 3 năm, trong dung sai.)

### 12.1 Con số "85 thiên" — **ĐÚNG, nhưng câu "còn nguyên" thì không**

> *"Bộ Luận hành **tám mươi lăm thiên**"* … *"còn Luận hành **còn nguyên**"*

- **85 thiên: đúng.** Bản truyền thế gồm **85 thiên** (篇) trong 30 quyển (卷), hơn 200.000 chữ.
- **"Còn nguyên": không chính xác.** *"Actually, **84 pian is more accurate** because the text only contains the title of Chapter 44 Zhaozhi 招致."* Tức thiên 44 **Chiêu trí** chỉ còn lại cái tên.
*Nguồn dùng:* Wikipedia EN "Lunheng", mục **Text**.

→ **Sửa:** `… còn Luận hành truyền lại gần trọn — 85 thiên, trong đó thiên 44 Chiêu trí chỉ còn tên …`

### 12.2 **Sai** — Hoàn Đàm **không** cùng thời với Vương Sung

> *"Ứng viên **cùng thời** là **Hoàn Đàm**, người cũng phê phán sấm vĩ và bị biếm vì việc đó"*

**Hoàn Đàm: k. 43 TCN – 28 CN. Vương Sung: 27–97 CN.** Hoàn Đàm chết khi Vương Sung **khoảng một tuổi**. Hai người không có một ngày nào cùng hoạt động.

Đây đúng là lỗi hệ thống (i) mà quy tắc 5 CONTRIBUTING liệt kê, và lệch còn nặng hơn các ca đã bắt (Tử Sản/Quản Trọng: 64 năm; ở đây: cả một đời người). Mô tả nội dung thì **đúng** — Hoàn Đàm có phê phán sấm vĩ và bị Quang Vũ Đế trị vì việc đó.

Thêm một tầng: Hoàn Đàm không phải "ứng viên bị loại" theo nghĩa đánh đổi, mà là **người Vương Sung ngưỡng mộ và kế thừa** — *Luận hành* ca ngợi Hoàn Đàm và *Tân luận* của ông là tiền thân trực tiếp của mạch phê phán ấy. Nêu một tiền bối làm "đối thủ bị loại" là đảo ngược quan hệ.
*Nguồn dùng:* Wikipedia EN "Huan Tan" (*"c. 43 BC – AD 28"*); Wikidata Q319329.

### 12.3 **Thể thức** — hệ quả: mục `-10` có **0** ứng viên bị loại hợp lệ

Người thứ hai được nêu là **Ban Cố**, kèm khai báo *"chọn riêng ở mục sau"* (`CH04-CE01-11`) — đúng quy tắc 6, nhưng vì thế không phải ứng viên bị loại. Cộng với 12.2: **không ai** trong hai người là ứng viên cùng thời bị loại. Cấu trúc lỗi giống hệt `-06` và `-08`.

→ **Câu thay thế** (chuyển Hoàn Đàm về đúng vai, và nói thẳng là thế hệ ông không có đối thủ):
`Người gần nhất trong cùng mạch là Hoàn Đàm (k. 43 TCN – 28 CN), tác giả Tân luận, nhưng ông chết khi Vương Sung mới một tuổi, nên là tiền bối chứ không phải đối thủ cùng thời; trước tác của ông cũng gần như mất hết. Ban Cố, người cùng thế hệ duy nhất có thể đặt cạnh, được chọn riêng ở mục sau với lý do khác. Vương Sung được chọn theo tính nguyên bản (c) và độ bền (b): Luận hành truyền lại gần trọn, trong khi Tân luận thì không.`
(Và chuyển Hoàn Đàm lên dòng `Kế thừa từ` — xem 12.5.)

### 12.4 **Nghi vấn** — mệnh đề tối cao "sớm nhất của Đông Á": không quy thuộc, và có phản ví dụ trong chính mục

> *"Luận hành … là **văn bản hoài nghi có hệ thống sớm nhất của Đông Á**"*

Phản ví dụ nằm ngay trong dòng `Kế thừa từ` của chính mục: `CH03-BCE03-11` = **Tuân Tử**. Thiên **Thiên luận** (天論) của Tuân Tử, TK 3 TCN, lập luận chính xác cùng một điều — trời vận hành theo lẽ thường của nó, không đáp lại hành vi người, nên điềm lạ không phải lời quở trách — và còn nguyên. Mục vừa nói Vương Sung *kế thừa* Tuân Tử, vừa nói văn bản của Vương Sung là văn bản hoài nghi có hệ thống **sớm nhất**. Hai câu không thể cùng đúng.

Phản ví dụ khác: thiên **Hiển học** (顯學) của *Hàn Phi Tử* bác các phái bằng đúng thao tác đòi bằng chứng và chỉ mâu thuẫn nội tại; và **Tân luận** của Hoàn Đàm thì sớm hơn (chỉ không còn trọn).

Mệnh đề cũng **không quy thuộc** — không nói ai cho rằng vậy.

→ **Câu thay thế:** `… còn Luận hành truyền lại gần trọn, và giới nghiên cứu thường coi đây là bộ sách hoài nghi dài hơi và hệ thống nhất còn lại của Đông Á cổ đại — một thao tác phê phán mà Tuân Tử đã mở trong thiên Thiên luận, nhưng Vương Sung là người đầu tiên triển khai thành cả một công trình.`

### 12.5 **Nghi vấn** — liên kết: thiếu Hoàn Đàm, và `Ảnh hưởng tới Vương Bật` mỏng

Đã mở từng đích đọc tên:

| Dòng | Đích | Tên thật | Nhận xét |
|---|---|---|---|
| Kế thừa từ `CH03-BCE03-11` | — | **Tuân Tử** | **đúng** và là liên kết mạnh nhất của mục |
| Kế thừa từ `CH03-BCE02-01` | — | **Đổng Trọng Thư** · `phản bác` | **đúng**: thiên nhân cảm ứng là đích công kích chính. Đúng loại quan hệ |
| Ảnh hưởng tới `CH04-CE03-10` | — | **Vương Bật** (226–249) | **nghi vấn**, xem dưới |

**Thiếu:** không có dòng nào cho **Hoàn Đàm**, dù ông là tiền thân trực tiếp. Còn chỗ (tối đa 3, hiện 2).
→ **Thêm:** `- Hoàn Đàm · kế thừa · qua trường phái`

**Về `CH04-CE03-10` Vương Bật:** niên đại thuận, ID trỏ đúng người. Nhưng dòng truyền yếu. *Luận hành* **bị bỏ quên gần như suốt đời tác giả**; nó chỉ vào được giới học thuật kinh đô khi Thái Ung (132–192) ca ngợi và Vương Lãng (mất 228) mang một bản tới Hứa Xương **năm 198**. Vương Bật sinh 226 — tức có thể tiếp cận, nhưng huyền học của ông là chú giải *Lão Tử* và *Chu Dịch* theo hướng bản thể luận, không phải nối mạch hoài nghi đòi bằng chứng của Vương Sung. Đây là suy đoán, không phải dòng truyền có bằng chứng.
*Nguồn dùng:* Wikipedia EN "Wang Chong" (*"largely ignored during his lifetime … Cai Yong (132–192) wrote of his admiration … Wang Lang (d. 228) acquired a copy … brought it with him on his trip in 198"*).
→ **Sửa:** hạ xuống `- CH04-CE03-10 · tương đồng độc lập · suy đoán học giả`, hoặc thay bằng `- Thái Ung và Vương Lãng, những người đưa Luận hành vào kinh đô năm 198 · kế thừa · trực tiếp`.

Thêm một hệ quả cho phần văn xuôi: câu *"được đọc lại mỗi khi học thuật Trung Hoa cần một tiền lệ phê phán"* bỏ qua việc sách này suýt thất truyền và chỉ lưu hành từ cuối TK 2. Nên nói ra — nó làm mục trung thực hơn, không yếu đi.

### 12.6 **Nghi vấn** — nguồn thứ cấp lệch tâm

**Michael Nylan, *The Five "Confucian" Classics* (2001): có thật** (Yale University Press, 2001), đúng thể loại (chuyên khảo), và đúng là về học thuật đời Hán. Nhưng đây là sách về **Ngũ kinh**, không phải về Vương Sung; nó **không** là nguồn đỡ được cho các khẳng định riêng của mục (85 thiên, nội dung bác ma quỷ, vị trí "sớm nhất của Đông Á"). **Không kiểm được** Nylan có bàn tới Vương Sung ở mức nào và có nêu con số 85 thiên không — cần mở mục lục / chỉ mục sách mới kết luận được.

Nguồn đúng tâm sẵn có: bản dịch **Alfred Forke, *Lun-hêng*** (1907–1911, 2 tập) — bản dịch Anh ngữ đầy đủ duy nhất; và **Rafe de Crespigny, *A Biographical Dictionary of Later Han to the Three Kingdoms*** (2007) cho phần tiểu sử.
→ **Sửa:** `Vương Sung, Luận hành (bản dịch Alfred Forke, Lun-hêng, 1907–1911); Michael Nylan, The Five "Confucian" Classics (2001)` — giữ Nylan làm nguồn bối cảnh, thêm một nguồn đỡ trực tiếp.

---

## 13. `CH04-CE01-11` · Ban Cố

**Q-ID.** `Q439681` = "Ban Gu" / vi "Ban Cố". Đúng người. P569 = 32, P570 = 92. Mục ghi `32–92 CN`, **Cao** — khớp (một số tài liệu ghi "31 hoặc 32"; trong ±5).

**Nguồn — Hans van Ess, *Politik und Geschichtsschreibung im alten China* (2014): ĐÚNG mọi mặt, và là nguồn đúng tâm nhất trong cả nhóm CE01.** Có thật, 2 tập, Harrassowitz 2014, series *Lun Wen — Studien zur Geistesgeschichte und Literatur in China*. Đúng thể loại (chuyên khảo). Và phụ đề **Pan-Ma i-t'ung** (班馬異同, "chỗ khác nhau giữa Ban Cố và Tư Mã Thiên") cho thấy nó bàn **chính xác** điều mục dẫn nó ra để đỡ: sự khác biệt về phạm vi giữa *Hán thư* và *Sử ký*.
*Nguồn dùng:* Open Library.

**"Ông chết trong ngục năm 92 CN": ĐÚNG** — bị bắt vì dính líu gia tộc Đậu thái hậu (Đậu Hiến) và chết trong ngục cùng năm, 61 tuổi.

**"Hán thư là bộ sử đầu tiên lấy một triều đại làm phạm vi trọn vẹn": ĐÚNG về nội dung.** Ban Bưu định viết **Hậu truyện** (後傳) tiếp nối *Sử ký*; chính Ban Cố mới bỏ khuôn tiếp nối ấy và khởi một bộ sử bắt đầu từ đầu nhà Hán — đúng như mục nói, **quyết định hình thức là của ông**.
*Nguồn dùng:* Wikipedia EN "Book of Han" — *"After Ban Biao's death, his eldest son Ban Gu was dissatisfied with what his father had completed, and he began a new history that started with the beginning of the Han dynasty. This distinguished it from Sima Qian's history, which had begun with China's earl[iest times]."*

**"Thiên Nghệ văn chí … là bản mục lục thư viện cổ nhất còn lại của Đông Á": ĐÚNG về nội dung.** *Nghệ văn chí* dựa trên **Thất lược** của Lưu Hâm, vốn là bản rút gọn **Biệt lục** của Lưu Hướng — cả hai bản gốc đều **đã mất**, nên bản của Ban Cố là bản còn lại sớm nhất, và nó thành khuôn cho mọi thư mục hoàng gia về sau.
*Nguồn dùng:* Wikipedia EN "Yiwenzhi", "Liu Xin (scholar)", "Shizi (book)".

### 13.1 **Sai** — "hai mươi bốn bộ chính sử Trung Hoa **đều** theo khuôn một triều một bộ"

Chữ "đều" sai, và sai ngay ở bộ đứng đầu danh sách:

- ***Sử ký*** là **một trong 24 bộ chính sử**, và nó **không** theo khuôn một triều một bộ — nó chạy từ Tam Hoàng Ngũ Đế tới đương thời. Chính mục này, ở câu trước, lấy *Sử ký* làm ví dụ cho cái khuôn **ngược lại**. Hai câu cạnh nhau tự phủ định.
- Ngoài ra còn **Nam sử** và **Bắc sử**, mỗi bộ bao nhiều triều đại.
- *Hán thư* là bộ **thứ hai** trong 24 bộ, không phải bộ đầu.
*Nguồn dùng:* Wikipedia EN "Twenty-Four Histories" (*"detailing the dynasties of China, **from the legendary Three Sovereigns and Five Emperors in the 4th millennium BC** to the Ming dynasty"*); "Ban Gu" (*"the Book of Han, **the second** of China's 24 dynastic histories"*).

→ **Câu thay thế:** `Quyết định ấy định hình thể chính sử: từ đó mỗi triều soạn sử cho triều trước, và phần lớn trong hai mươi bốn bộ chính sử Trung Hoa theo khuôn một triều một bộ — ngoại lệ chính là Sử ký, bộ mở đầu danh sách, cùng Nam sử và Bắc sử.`

### 13.2 **Nghi vấn** — hai mệnh đề tối cao không quy thuộc

Hai mệnh đề của mục này **đúng về nội dung** (đã kiểm ở trên), nhưng cả hai đều viết như sự kiện trần thuật, không nói ai cho rằng vậy:
- *"bộ sử **đầu tiên** lấy một triều đại làm phạm vi trọn vẹn"*
- *"là bản mục lục thư viện **cổ nhất còn lại** của Đông Á"*

Ngay nguồn tham chiếu phổ thông cũng hạ giọng: *"**It has been argued that** tendency of scholars to view China's history in a dynastic framework is a direct result of Ban Gu's decision."* Theo yêu cầu trung lập, mệnh đề tối cao không quy thuộc là lỗi.
→ **Sửa:** `Hán thư là bộ sử sớm nhất còn lại lấy một triều đại làm phạm vi trọn vẹn …` và `… và là bản mục lục thư viện cổ nhất còn lại của Đông Á — Biệt lục của Lưu Hướng và Thất lược của Lưu Hâm, hai bản nó rút từ đó, đều đã mất.`

### 13.3 **Thể thức** — ứng viên bị loại: đạt mức tối thiểu, nhưng cả hai đều là người nhà

> *"Ứng viên trực tiếp là **Ban Bưu**, cha ông, người khởi thảo, và **Ban Chiêu**, em gái ông, **chọn riêng ở mục sau** vì phần bà hoàn thành."*

- **Ban Bưu**: có thật, mất năm 54 CN, là sử gia có tiếng, và đúng là người khởi thảo (**Hậu truyện**). Cùng thời với Ban Cố (hai cha con sống chung 22 năm). Đã đối chiếu 221 mục: **không có mục riêng** → là ứng viên bị loại hợp lệ.
- **Ban Chiêu**: khai báo "chọn riêng ở mục sau" — **đúng quy tắc 6**.

Vậy còn **một** ứng viên bị loại thật, đủ mức tối thiểu §5. Nhưng cả hai người được nêu đều là người trong gia đình Ban, nên đoạn này không thật sự chứng minh Ban Cố vượt trội **trong lĩnh vực sử học đương thời** — nó chỉ phân công trong nội bộ một dự án. Nếu muốn mạnh hơn, ứng viên ngoài nhà có sẵn: **Lưu Hâm** và **Dương Hùng**, cả hai cũng soạn phần tiếp nối *Sử ký* và đều không có mục riêng trong atlas.
*Nguồn dùng:* Wikipedia EN "Book of Han" (*"Other scholars of the time, including Liu Xin and Yang Xiong also worked on continuations of Sima's history"*).

### 13.4 Liên kết — đã mở đích đọc tên, **tất cả đúng**

| Dòng | Đích | Tên thật | Nhận xét |
|---|---|---|---|
| Kế thừa từ `CH03-BCE01-06` | — | **Tư Mã Thiên** | đúng. `trực tiếp` hợp lệ: *Hán thư* hấp thu nguyên văn nhiều phần *Sử ký* |
| Kế thừa từ `CH03-BCE01-10` | — | **Lưu Hướng** | đúng người. `trực tiếp` biện hộ được, nhưng kênh thật là **Thất lược của Lưu Hâm**, bản rút từ *Biệt lục* của Lưu Hướng — tức một bước trung gian. Cân nhắc đổi sang `qua trường phái`, hoặc thêm Lưu Hâm |
| Ảnh hưởng tới `CH04-CE01-12` | — | **Ban Chiêu** | đúng người, đúng chiều, đối xứng với `-12`. Đúng |

---

## 14. `CH04-CE01-12` · Ban Chiêu

**Q-ID.** `Q177081` = "Ban Zhao" / vi "Ban Chiêu". Đúng người. P569 = 45, P570 = 116. Mục ghi `k. 45–116 CN`, **Trung bình** — hợp lệ (tài liệu ghi `45 hoặc 49 – k. 117/120`).

### 14.1 Con số và mệnh đề tối cao — **ĐÚNG cả hai**

| Mục ghi | Kiểm | Kết quả |
|---|---|---|
| **Nữ giới bảy thiên** | *"The book contains only **7 chapters**"* | **đúng** |
| *"người phụ nữ đầu tiên của Trung Hoa **được ghi là** sử gia có tên"* | *"She was the **first known female Chinese historian** and, along with Pamphile of Epidaurus, one of the first known female historians"* | **đúng**, và cụm "được ghi là" là chữ hạn định đặt đúng chỗ |

Đã tìm phản ví dụ: không có nữ sử gia Trung Hoa nào có tên được ghi trước bà. Mệnh đề đứng vững. **Nhưng nó vẫn không quy thuộc** — nên thêm chủ thể phát ngôn cho nhất quán với các mục khác.
→ **Sửa:** `… — theo ghi chép còn lại, bà là người phụ nữ đầu tiên của Trung Hoa được ghi là sử gia có tên.`
*Nguồn dùng:* Wikipedia EN "Ban Zhao", "Lessons for Women".

**Nguồn — Nancy Lee Swann, *Pan Chao: Foremost Woman Scholar of China* (1932): ĐÚNG mọi mặt.** Có thật, The Century Co., **1932** (tái bản 1968 và 2001), đúng thể loại (tiểu sử kèm bản dịch), đúng chủ đề — đây vẫn là chuyên khảo Anh ngữ tiêu chuẩn về bà. *Nguồn dùng:* Open Library.

### 14.2 **Sai** — liên kết `CH90-CE19_20-04` trỏ **nhầm người** (lỗi quy tắc 8)

> `**Ảnh hưởng tới:**`
> `- CH90-CE19_20-04 · phản bác · qua trường phái`

Đã mở đích đọc tên: **`CH90-CE19_20-04 · Trương Vĩnh Ký (張永記, Pétrus Ký)`**, 1837–1898, nhà ngôn ngữ học, chánh tổng tài *Gia Định báo*.

Không có quan hệ nào — nói gì tới quan hệ `phản bác` — giữa *Nữ giới* của Ban Chiêu và Trương Vĩnh Ký. Mục của ông không nhắc một chữ nào về giáo dục nữ giới hay về khuôn mẫu nữ đức; `Kế thừa từ` của ông là `CH90-CE15_18-07`, `CH90-CE15_18-08`, `CH90-CE19_20-01`, **không có Ban Chiêu** — tức liên kết này cũng **không đối xứng**.

Đích gần như chắc chắn là **`CH90-CE19_20-03 · Hồ Xuân Hương`** (k. 1772–1822), người mà mục trong `ch90.md` mô tả đúng là *"công kích thói đạo đức giả của nam giới có học"* và viết về *"thân phận làm lẽ, sinh nở, goá bụa và ham muốn"* — tức đúng một quan hệ `phản bác` với khuôn *Nữ giới*. Lệch đúng **một chữ số** trong ID.

Đây chính xác là loại lỗi mà quy tắc 8 CONTRIBUTING mô tả (Tư Mã Thiên "ảnh hưởng tới" Đinh Bộ Lĩnh; Lưu Hướng "ảnh hưởng tới" Nguyễn Hoàng): ID hợp lệ, lint không bắt được vì niên đại vẫn thuận, chỉ mở đích đọc tên mới thấy.
*Nguồn dùng:* `content/ch90.md` dòng 537–569 (đọc trực tiếp cả hai mục).

→ **Sửa:** `- CH90-CE19_20-03 · phản bác · qua trường phái`
→ Và **bổ sung chiều đối xứng** ở `CH90-CE19_20-03`: thêm `- CH04-CE01-12 · phản bác · qua trường phái` vào `Kế thừa từ` của Hồ Xuân Hương (hiện chỉ có một dòng "Truyền thống ca dao và hát đối").

### 14.3 **Nghi vấn** — thiên Thiên văn chí có lẽ **không** phải của bà

> *"soạn các bảng niên biểu **và thiên Thiên văn chí**"*

Phần **tám bảng niên biểu** (八表, quyển 13–20) thì đúng là của bà, không tranh cãi. Phần **Thiên văn chí** (天文志, quyển 26) thì không:
- Bài "Book of Han": *"she is thought to have written volumes 13–20 (eight chronological tables) and 26 (treatise on astronomy), the latter **with the help of Ma Xu**."*
- Bài "Ban Zhao" còn mạnh hơn: *"Ban Zhao helped finish the work by making up for the missing part of the Babiao (八表 Eight Tables). … **Later, Ma Xu added a treatise on astronomy (天文志)**, making Hanshu a complete work."*

Tức ở phiên bản thận trọng nhất, Thiên văn chí là công của **Mã Tục**, không phải của bà. Gán trọn cho bà là **nâng** công trạng — lỗi ngược chiều với lỗi hạ thấp, nhưng vẫn là lỗi.
→ **Câu thay thế:** `… hoàn thành Hán thư, soạn tám bảng niên biểu còn dang dở, rồi giảng bộ sử ấy cho các học giả trong triều; thiên Thiên văn chí thì do Mã Tục bổ sung, có tài liệu ghi là với sự tham gia của bà.`

### 14.4 **Nghi vấn** — "suốt gần hai nghìn năm" phóng đại thời gian lưu hành

> *"sách của bà trở thành khuôn ràng buộc nữ giới **suốt gần hai nghìn năm** ở Trung Hoa, Triều Tiên và Việt Nam"*

*Nữ giới* được lưu hành ngay ở triều đình khi mới viết, nhưng giai đoạn nó thành **khuôn chuẩn mực phổ biến** là khi được xếp vào **Nữ tứ thư** (女四書): *"As one of the Four Books for Women, Lessons had wide circulation in the **late Ming and Qing dynasties (i.e. 16th–early 20th centuries)**."* Tức khoảng bốn thế kỷ ở đỉnh, không phải hai nghìn năm liên tục.
*Nguồn dùng:* Wikipedia EN "Lessons for Women".

→ **Câu thay thế:** `… đồng thời sách của bà, sau khi được xếp vào bộ Nữ tứ thư, thành khuôn ràng buộc nữ giới ở Trung Hoa, Triều Tiên và Việt Nam suốt từ cuối Minh tới đầu thế kỷ 20.`

### 14.5 **Nghi vấn** — mệnh đề tối cao thứ hai, không quy thuộc và không kiểm được

> *"**không văn bản nào khác do phụ nữ Đông Á viết đạt mức lưu hành như Nữ giới**"*

Không quy thuộc, và "mức lưu hành" không được định nghĩa nên **không kiểm được** như một mệnh đề. Phản ví dụ tuỳ cách đo:
- **Nội huấn** (內訓) của Nhân Hiếu Hoàng hậu nhà Minh — cũng nằm trong **Nữ tứ thư**, in và phát hành theo lệnh triều đình, nên lưu hành song song chứ không dưới.
- **Nguyên thị vật ngữ** (源氏物語) của Murasaki Shikibu, nếu đo bằng số bản chép và tầm phổ cập văn hoá.
→ **Sửa:** thu hẹp và quy thuộc — `Ban Chiêu được chọn theo độ bền (b) và tính nguyên bản (c): Nữ giới là văn bản do phụ nữ Đông Á viết có ảnh hưởng chuẩn mực lâu nhất, và vai trò sử gia của bà là tiền lệ được dẫn lại suốt các đời sau.`

### 14.6 **Nghi vấn nhẹ** — "nữ công dung ngôn hạnh" là một cụm bị dính

Tứ đức trong *Nữ giới* là **婦德 · 婦言 · 婦容 · 婦功** — tiếng Việt quen gọi là **công, dung, ngôn, hạnh**. Mục viết liền thành *"nữ công dung ngôn hạnh"*, làm dính "nữ công" (vốn là một từ khác, chỉ việc may vá bếp núc) vào đầu chuỗi.
→ **Sửa:** `sách dạy tứ đức — công, dung, ngôn, hạnh`
*Nguồn dùng:* Wikipedia EN "Lessons for Women" (liệt kê fude, fuyan, fuyong, fugong).

### 14.7 **Thiếu** — bỏ mất *Liệt nữ truyện*, công trình nối thẳng bà với `-11` và với Lưu Hướng

Ban Chiêu còn **sắp xếp lại và mở rộng *Liệt nữ truyện* của Lưu Hướng** khi làm quản thủ thư viện trong cung. Chi tiết này đáng có vì: (a) nó nối bà với `CH03-BCE01-10` Lưu Hướng, cùng người mà anh bà `-11` kế thừa; (b) nó cho thấy vai trò học thuật của bà rộng hơn "hoàn thành sách của anh"; (c) nó làm "di sản trái chiều" mà mục nêu trở nên có căn cứ văn bản.
*Nguồn dùng:* Wikipedia EN "Ban Zhao" — *"In this capacity, she rearranged and enlarged the Biographies of Eminent Women by Liu Xiang."*

### 14.8 **Nghi vấn** — nhân vật có thể thuộc nhóm CE02

Quy tắc 3 §5: *"Xếp nhân vật vào thế kỷ của **giai đoạn ảnh hưởng chính** (floruit / tác phẩm hoặc hành động quan trọng nhất), không theo năm sinh."* Với Ban Chiêu, mọi mốc ấy nằm ở **thế kỷ 2**:
- *Hán thư* **hoàn thành năm 111 CN**;
- bà làm cố vấn cho Đặng thái hậu khi bà này nhiếp chính — **từ 106 CN**;
- bà mất k. 116/120.
Bà chỉ bắt đầu công việc sau khi Ban Cố chết (92 CN), tức chưa tới một thập niên nằm trong TK 1.
*Nguồn dùng:* Wikipedia EN "Book of Han" (*"Ban Zhao finished writing the book in **111**"*), "Ban Zhao".

Lập luận giữ bà ở CE01 có tồn tại (bà gắn liền với dự án *Hán thư* khởi từ TK 1, và đặt cạnh `-11` thì mạch đọc liền hơn), nhưng **CONTRIBUTING yêu cầu mục `## Ghi chú biên tập` ghi "nhân vật nào có thể thuộc thế kỷ khác"** — cần kiểm xem Ghi chú biên tập của Ch4 đã ghi ca này chưa; nếu chưa, bổ sung.

### 14.9 **Thể thức** — ứng viên bị loại: một người hợp lệ nhưng lệch lĩnh vực

> *"Ứng viên cùng thời là **Hoàng hậu Đặng Tuy**, người bà làm cố vấn, và **Ban Cố**, anh bà, **chọn ở mục trước**."*

- **Đặng Tuy (Đặng Thái hậu, 81–121)**: có thật, **thật sự cùng thời**, quan hệ cố vấn đúng, và đã đối chiếu 221 mục — **không có mục riêng**. Hợp lệ về niên đại và về quy tắc 6.
- **Ban Cố**: khai báo đúng quy tắc 6.

Nhưng §5 đòi ứng viên **cùng lĩnh vực**: Ban Chiêu có `lĩnh vực: Sử học, Giáo dục`, còn Đặng Tuy là nhiếp chính — `Chính trị/Nhà nước`. Không có đánh đổi thật nào xảy ra giữa hai người. Đây là dạng yếu hơn của cùng một vấn đề thấy ở `-04` (hai thủ lĩnh cát cứ).
→ **Gợi ý:** ứng viên cùng lĩnh vực cùng thời sát hơn là **Mã Tục**, người bổ sung Thiên văn chí cho *Hán thư* (xem 14.3) — một đánh đổi có nội dung thật, và ông cũng không có mục riêng trong atlas.

### 14.10 Liên kết còn lại — đã mở đích, **đúng**

`Kế thừa từ: CH04-CE01-11 · kế thừa · trực tiếp` → **Ban Cố**. Đúng người, đúng chiều, đối xứng với `-11`, `trực tiếp` chính xác (bà viết tiếp đúng bộ sách của ông).

`Ảnh hưởng tới: Giáo dục nữ giới ở Trung Hoa, Triều Tiên và Việt Nam · kế thừa · qua trường phái` — mệnh đề, nhưng kiểm được và đúng.

### 14.11 Một điểm **đúng** đáng giữ

*"Hai việc ấy kéo theo hai di sản trái chiều: bà là tiền lệ cho phụ nữ làm học thuật, đồng thời sách của bà trở thành khuôn ràng buộc nữ giới"* — đây là cách xử lý trung lập đúng mực cho một nhân vật mà đánh giá hiện đại chia rẽ (tài liệu ghi rõ có học giả cho rằng đọc bà như người nữ quyền là sai chỗ). Không tô hồng, không kết án. Giữ nguyên cấu trúc, chỉ sửa phần thời gian ở 14.4.

---

## 15. Tổng hợp phát hiện

### 15.1 Bảng xếp loại

| # | ID | Loại | Vấn đề |
|---|---|---|---|
| 1 | Giới thiệu chapter | Nghi vấn | "Manichaeism" không dịch; "chưa ai vượt" không quy thuộc |
| 2 | Bối cảnh CE01 | **Sai** | "Giấy… thành sách" là mốc của CE02 (Thái Luân, 105 CN) |
| 3 | Bối cảnh CE01 | Thiếu / Nghi vấn | không có chữ nào về Nam Á; "tách ra" quá sớm cho TK 1 |
| 4 | `-01` Giê-su | **Sai** | `nơi … tỉnh Judea` — Galilee thuộc tetrarchy Herod Antipas, không thuộc tỉnh Judea |
| 5 | `-01` Giê-su | **Sai** + trung lập | câu "rẽ khỏi các nhóm Do Thái đương thời" **dẫn ngược E. P. Sanders**, sai về nội dung (hai điều răn là trích Ngũ thư), và mâu thuẫn với chính dòng `Kế thừa từ Hillel` |
| 6 | `-01` Giê-su | Nghi vấn | `Hillel · kế thừa` nên là `tương đồng độc lập · suy đoán học giả` |
| 7 | `-01` Giê-su | Thể thức | `Ảnh hưởng tới: toàn bộ lịch sử tư tưởng phương Tây` — mệnh đề vô hạn |
| 8 | `-02` Phaolô | **Sai** | vai trò Giacôbê ở công nghị Jerusalem bị đảo ngược — lập trường ông **đã thắng**, và đó là lập trường miễn cắt bì. Phản-thực tế của mục không tồn tại |
| 9 | `-03` Vương Mãng | **Sai** | "phép thử **duy nhất** trong lịch sử Trung Hoa" — Tân pháp Vương An Thạch |
| 10 | `-03` Vương Mãng | **Sai** | "Hán Quang Vũ Đế, **người lật ông**" — quân Lục Lâm của Canh Thuỷ Đế mới là bên hạ Trường An; mâu thuẫn với chính mục `-04` |
| 11 | `-03` Vương Mãng | Nghi vấn | Xích Mi bị gán sai vai; thiếu trận vỡ Hoàng Hà 11 CN; `Kế thừa từ Lưu Hướng` nên là Lưu Hâm; mệnh đề "lần đầu" không quy thuộc |
| 12 | `-04` Quang Vũ Đế | **Sai** | "khái niệm trung hưng **mà ông tạo ra**" — điển cố Chu Tuyên vương có trước 800 năm |
| 13 | `-04` Quang Vũ Đế | Thể thức / Thiếu | ứng viên bị loại là hai kẻ bại trận, không phải so sánh theo (a)–(d); `Ảnh hưởng tới` chỉ có một mệnh đề trừu tượng |
| 14 | `-05` Seneca | Nghi vấn | "thể văn ấy là **đóng góp riêng của ông**" — Epicurus, Cicero, thể *consolatio* có trước |
| 15 | `-05` Seneca | Nghi vấn | `Ảnh hưởng tới Marcus Aurelius · kế thừa` — không có bằng chứng; kênh thật là Epictetus, người không có mục riêng |
| 16 | `-06` Philo | **Sai** | "Aristobulus **xứ Paneas**" là định danh đã bị bác; ông hoạt động **k. 181–124 TCN**, không cùng thời (câu tự mâu thuẫn: "cùng thời … trước ông") |
| 17 | `-06` Philo | **Thể thức** | **0** ứng viên bị loại hợp lệ (một người lệch 175 năm, một người đã được chọn) |
| 18 | `-06` Philo | Nghi vấn | "nỗ lực có hệ thống **sớm nhất còn lại**" không quy thuộc; Sách Khôn ngoan (TK 1 TCN, còn nguyên) là phản ví dụ |
| 19 | `-07` Pliny | Nghi vấn | `Kế thừa từ Strabo` — Strabo **không** nằm trong các nguồn của *Naturalis Historia*; người đúng là Theophrastus |
| 20 | `-07` Pliny | Nghi vấn | *indices auctorum* không phải danh sách sách ông thực đọc; "hơn hai trăm bản chép tay" nên là ~307 |
| 21 | `-08` Dioscorides | **Sai** | `vùng: Châu Âu` cho Anazarbus xứ Cilicia (Thổ Nhĩ Kỳ) — mâu thuẫn với `-02` Phaolô xứ Tarsus, cùng xứ, gán `Trung Đông/Bắc Phi` |
| 22 | `-08` Dioscorides | **Thể thức** | **0** ứng viên bị loại hợp lệ (Pliny đã được chọn; Crateuas sớm hơn một thế kỷ) |
| 23 | `-08` Dioscorides | Nghi vấn | `Kế thừa từ Hippocrates` sai dòng truyền; đúng là Theophrastus / Crateuas |
| 24 | `-09` Josephus | Nghi vấn | `Cao` quá tự tin (năm mất chỉ là `k. 100`); thiếu *Vita* và *Bác Apion*; nguồn Mason lệch tâm |
| 25 | `-10` Vương Sung | **Sai** | **Hoàn Đàm (k. 43 TCN – 28 CN) không cùng thời** — chết khi Vương Sung một tuổi; và ông là tiền bối, không phải đối thủ |
| 26 | `-10` Vương Sung | **Thể thức** | **0** ứng viên bị loại hợp lệ |
| 27 | `-10` Vương Sung | Nghi vấn | "văn bản hoài nghi có hệ thống **sớm nhất** của Đông Á" — Tuân Tử, *Thiên luận*, chính là người mục ghi là nguồn kế thừa; "còn nguyên" — thiên 44 chỉ còn tên |
| 28 | `-10` Vương Sung | Nghi vấn | `Ảnh hưởng tới Vương Bật` mỏng; thiếu Hoàn Đàm ở `Kế thừa từ`; nguồn Nylan lệch tâm (**không kiểm được** có bàn Vương Sung không) |
| 29 | `-11` Ban Cố | **Sai** | "hai mươi bốn bộ chính sử **đều** theo khuôn một triều một bộ" — *Sử ký* nằm trong 24 bộ và không theo khuôn đó; còn *Nam sử*, *Bắc sử* |
| 30 | `-11` Ban Cố | Nghi vấn | hai mệnh đề tối cao không quy thuộc; ứng viên bị loại đều là người trong nhà |
| 31 | `-12` Ban Chiêu | **Sai** | `Ảnh hưởng tới CH90-CE19_20-04` trỏ **Trương Vĩnh Ký**, không liên quan; đích đúng là `-03` **Hồ Xuân Hương**; liên kết cũng **không đối xứng** |
| 32 | `-12` Ban Chiêu | Nghi vấn | Thiên văn chí có lẽ là công **Mã Tục**; "gần hai nghìn năm" phóng đại (Nữ tứ thư: cuối Minh – đầu TK 20); "không văn bản nào khác… " không kiểm được |
| 33 | `-12` Ban Chiêu | Thiếu / Nghi vấn | bỏ mất *Liệt nữ truyện*; "nữ công dung ngôn hạnh" là cụm bị dính; có thể thuộc **CE02** mà Ghi chú biên tập chưa ghi |

**Đếm:** 12 lỗi **Sai**, 16 **Nghi vấn**, 3 **Thể thức** nặng (0 ứng viên hợp lệ), phần còn lại là **Thiếu**.

### 15.2 Những thứ đã kiểm và **ĐÚNG** (ghi lại để không bị sửa nhầm)

- **Tacitus, Biên niên sử q. XV, 44** — đúng quyển, đúng chương, đúng nội dung (Christus bị Pilatus hành hình). Đã mở ra kiểm.
- **Vienna Dioscurides, Med. Gr. 1, năm 512** — số hiệu và niên đại **đúng** (chuẩn đầy đủ: `Cod. med. gr. 1`, ÖNB, 512/513).
- **Naturalis Historia 37 quyển** — đúng. **Quyển I là mục lục kèm danh sách tác giả** — đúng.
- **Dioscorides: 5 quyển, ~600 loài, ~1000 vị thuốc** — đúng cả ba.
- **Luận hành 85 thiên** — đúng (bản truyền thế; 84 thiên còn văn).
- **Nữ giới 7 thiên** — đúng.
- **Phaolô 7 lá thư được nhận là của ông** — đúng.
- **Vương Mãng lập nhà Tân năm 9 CN, chết 23 CN** — đúng.
- **Quang Vũ Đế phục Hán 25 CN** — đúng. **Hai Bà Trưng bị dập năm 43 CN** — đúng.
- **Ban Cố chết trong ngục năm 92** — đúng. **Ban Chiêu là nữ sử gia có tên đầu tiên của Trung Hoa** — đúng.
- **12/12 Q-ID trỏ đúng người**, không trang định hướng, không mục họ tên.
- **Nguồn thứ cấp có thật, đúng năm, đúng thể loại, đúng chủ đề**: Sanders 1993 và 2015 · Bielenstein (CHOC t.1, 1986) · Bielenstein (*Restoration*, 1953–1979) · Wilson 2014 · Niehoff 2018 · Murphy 2004 · Beck 2005 (**ghi đúng là "bản dịch"**) · Mason 2003 (năm cần xác nhận) · Nylan 2001 · van Ess 2014 (**đúng tâm nhất**) · Swann 1932. **Không có nguồn ma nào trong nhóm này.**
- `-02`, `-05`, `-09`, `-11` khai báo người-đã-được-chọn đúng quy tắc 6. `-05`, `-07` ghi rõ quan hệ thế hệ.
- Không mục nào ghi số chương/quyển mà chưa mở mục lục — quy tắc 3 được tuân thủ sạch.

### 15.3 Hai lỗi hệ thống của các chapter trước — có lặp lại không?

| Lỗi hệ thống | Có lặp ở CE01? |
|---|---|
| (i) nêu người **không cùng thời** mà không nói ra | **CÓ, 2 ca nặng**: `-06` Aristobulus (lệch ~175 năm, lại viết "cùng thời"), `-10` Hoàn Đàm (chết khi Vương Sung 1 tuổi, viết "cùng thời"). Một ca khai báo đúng: `-08` Crateuas ("thế kỷ 1 TCN"), `-05` Epictetus ("thế hệ sau"), `-06` Aristobulus ("trước ông" — nhưng mâu thuẫn với "cùng thời" ngay trước đó) |
| (ii) nêu làm "ứng viên bị loại" người **đã được chọn ở chỗ khác** | **KHÔNG, 0 ca.** Đã đối chiếu toàn bộ tên trong "Vì sao chọn" với `grep '^### ' content/ch0*.md content/ch90.md` (221 mục). Mọi ca trùng — Hillel, Quang Vũ Đế, Dioscorides, Pliny, Philo, Josephus, Ban Cố, Ban Chiêu — **đều được khai báo rõ** là đã có mục riêng. Quy tắc 6 được tuân thủ sạch |
| (bonus) nguồn **bị dẫn ngược luận điểm của chính nó** (quy tắc 7) | **CÓ, 1 ca**: `-01` dẫn E. P. Sanders để đỡ cho câu mà Sanders dành cả sự nghiệp để bác |
| (bonus) liên kết **trỏ đúng ID sai người** (quy tắc 8) | **CÓ, 1 ca chắc chắn**: `-12` → `CH90-CE19_20-04` Trương Vĩnh Ký (lệch một chữ số so với Hồ Xuân Hương); và 3 ca "đúng người, sai quan hệ": `-05`→Marcus Aurelius, `-07`←Strabo, `-08`←Hippocrates |

**Kết luận về quy tắc 6: đây là nhóm đầu tiên được rà mà lỗi (ii) bằng 0.** Nhưng cái giá là lỗi thể thức mới: vì phải khai báo người đã chọn, ba mục (`-06`, `-08`, `-10`) rơi xuống **không còn ứng viên bị loại nào hợp lệ**, và chỗ trống được lấp bằng một người lệch thế kỷ. Đổi một lỗi lấy một lỗi khác.

---

## 16. Đánh giá lựa chọn nhân vật

### 16.1 Nhóm kín 12/12

Đã xác nhận qua Ghi chú biên tập của chính chapter: *"Tổng số mục là 59: bốn nhóm đủ 12, riêng CE02 có 11."* Tức **CE01 kín 12/12** — thêm ai thì phải bỏ ai.

**Độ phủ đạt mức §5 nhưng sát sàn:**

| Chiều | Yêu cầu §5 | CE01 |
|---|---|---|
| Lĩnh vực | ≥ 4 | **9** — Tôn giáo/Tâm linh, Triết học, Chính trị/Nhà nước, Kinh tế, Văn học, Khoa học tự nhiên, Y học, Sử học, Giáo dục. Dư dả |
| Vùng | ≥ 3 | **3** — Đông Á 5 · Trung Đông/Bắc Phi 4 · Châu Âu 3. **Đúng sàn.** (Nếu sửa lỗi vùng ở `-08` thành 5·5·2 thì vẫn 3 vùng) |
| Giới | — | **1/12** (Ban Chiêu). Ghi chú biên tập đã tự nhận điểm này ở cấp chapter và hoãn tới P4 |

Sáu trong chín vùng của atlas trống ở CE01: **Nam Á, Trung Á, Đông Nam Á, Châu Phi hạ Sahara, Châu Mỹ, Châu Đại Dương**.

### 16.2 Khoảng trống Nam Á: **KHÔNG được biện minh**

Đây là phát hiện nặng nhất ở cấp nhóm, vì nó là lỗ hổng **không được thừa nhận ở bất kỳ đâu** — khác hẳn các khoảng trống khác của chapter.

**Chapter này biết cách thừa nhận khoảng trống. Nó đã làm ba lần — và bỏ sót đúng lần thứ tư:**

1. Khối *"Ứng viên Việt Nam đã được cân nhắc"* — nêu đích danh Hai Bà Trưng, Bà Triệu, Sĩ Nhiếp, giải thích vì sao không vào atlas chính, trỏ sang phụ lục. Mẫu mực.
2. Khối *"Một khoảng trống Nam Á đã được lấp sau bình duyệt"* — nhận rằng bản thảo đầu có hình 3–0–3 ở **CE02–CE03–CE04**, *"một cái hố … mà không khối nào trong Ghi chú biên tập thừa nhận"*, rồi lấp bằng `CH04-CE03-12` Āryadeva.
3. Khối *"Vì sao chapter này nặng về tôn giáo"* — nhận và phân tích một thiên lệch của chính bộ tiêu chí.

Nhưng **hình thật không phải 3–0–3. Nó là 0–3–0(→1)–3–0** nếu đếm cả năm nhóm, và hình ấy mở đầu bằng **một số không ở CE01** mà khối thứ hai không đếm tới. Việc đi sửa đúng cái hố ở giữa rồi để nguyên cái hố ở đầu cho thấy lỗ hổng CE01 chưa từng được nhìn tới, chứ không phải đã cân nhắc rồi quyết bỏ.

**Và chapter tự để lại bằng chứng rằng chỗ ấy có người:** khối *"Điểm cần kiểm chứng thêm"* viết — *"Niên đại trị vì của Kanishka (CH04-CE02-03) … với đề xuất trải từ 78 tới 144 CN. Mục này dùng khoảng 127–150 theo Falk; **nếu lấy mốc 78 thì ông thuộc nhóm CE01.**"* Tức chapter đã biết một ứng viên Nam Á có thể thuộc CE01, ghi điều đó ra, rồi không rút ra hệ quả nào.

**Ba ứng viên CE01 cụ thể, đều không có mục nào trong atlas (đã đối chiếu 221 mục):**

| Ứng viên | Niên đại | Vùng / lĩnh vực | Lập luận |
|---|---|---|---|
| **Kujula Kadphises** (Κοζουλου Καδφιζου) | trị vì **30–80 CN** (Bopearachchi: 40–90; Benjamin: 25–85) | Nam Á / Trung Á · Chính trị–Nhà nước | Người hợp nhất liên minh Nguyệt Chi ở Bactria và **sáng lập đế quốc Kushan**, cụ nội của Kanishka theo bi ký Rabatak. Niên đại nằm **gọn trong TK 1**, không tranh cãi về thế kỷ. Chính đế quốc ông lập ra là cái mà Bối cảnh CE02 gọi là *"nối Trung Á với Ấn Độ và bảo trợ Phật giáo Đại thừa đang hình thành"* — nhưng atlas hiện bắt đầu câu chuyện ấy từ người chắt |
| **Charaka** (चरक) | *Charaka Saṃhitā* quy cho ông, **k. TK 1–2 CN**; bản văn được soát lại trong khoảng 100 TCN – 200 CN | Nam Á · Y học | Một trong hai nền tảng của y học Ấn Độ cổ còn lại. Đặt ông ở CE01 cũng cân lại chiều lĩnh vực: nhóm hiện có **hai** mục y–dược và **cả hai đều Hy–La** (Dioscorides, và Pliny ở phần dược liệu). Niên đại tranh cãi mạnh (truyền thống còn đẩy về TK 4 TCN) nên phải gắn nhãn **[Tranh cãi lịch sử]** và `độ tin cậy: Thấp` — nhưng §5 quy tắc 8 **cho phép đúng điều đó**, và chapter đã dùng cơ chế ấy cho Nāgārjuna, Asaṅga, Vasubandhu |
| **Kanishka** | nếu lấy mốc 78 CN | Nam Á | Không khuyến nghị — ông đã có mục `CH04-CE02-03` và chuyển sẽ tạo hố ở CE02. Nêu ra vì **chính chapter đã nêu** |

*Nguồn dùng:* Wikipedia EN "Kujula Kadphises" (*"r. 30–80 CE … united the Yuezhi confederation in Bactria during the 1st century CE, and became the first Kushan emperor … considered the founder of the Kushan Empire"*); "Charaka Samhita" (*"attributed to Charaka (c. 1st–2nd century CE)"*); `content/ch04.md` khối Ghi chú biên tập.

**Ai phải nhường chỗ.** Vì nhóm kín, khuyến nghị phải nêu người bị thay — đúng yêu cầu CONTRIBUTING mục "Phản hồi mà không cần viết code". Hai ứng viên yếu nhất của nhóm theo bốn tiêu chí:

- **`-04` Hán Quang Vũ Đế** là mục mỏng nhất. Lập luận chọn ông dựa trên việc ông "tạo ra" khái niệm trung hưng — mà đó là **sai** (xem 6.1). Bỏ mệnh đề ấy đi thì còn lại: một hoàng đế khôi phục triều đại, với `Ảnh hưởng tới` chỉ một mệnh đề trừu tượng và `Kế thừa từ` chỉ một dòng. Tiêu chí (c) tính nguyên bản gần như bằng không. Nhóm cũng **đã có 5 mục Đông Á trên 12** — cao nhất trong ba vùng.
- **`-07` Pliny Cả** là ca sát nút thứ hai: mục tự nhận *"mức chính xác thì không đều, và chính ông cũng không phân biệt quan sát với lời đồn"*, và tiêu chí (c) của ông là biên soạn chứ không phải khởi xướng. Nhưng (a) và (b) thì rất mạnh (~307 bản chép tay, sách tham khảo chuẩn suốt trung cổ), nên khuyến nghị **giữ**.

→ **Khuyến nghị:** thay `-04` Hán Quang Vũ Đế bằng **Kujula Kadphises**. Khi đó vùng thành Đông Á 4 · Trung Đông/Bắc Phi 5 · Châu Âu 2 · **Nam Á 1** (sau khi sửa lỗi vùng `-08`) — **bốn vùng**, vượt sàn §5, và lấp đúng chỗ hở mà Giới thiệu chapter đã hứa (*"Phật giáo Đại thừa"*) nhưng nhóm đầu không giao.

Nếu Owner muốn giữ cả 12 mục hiện có, thì **tối thiểu phải viết một khối trong `## Ghi chú biên tập`** thừa nhận rằng CE01 không có mục Nam Á nào, nêu đích danh Kujula Kadphises và Charaka là hai người đã cân nhắc, và nói rõ lý do loại — theo đúng mẫu của khối *"Ứng viên Việt Nam"*. **Im lặng là không chấp nhận được**, vì chính chapter đã đặt ra chuẩn cao hơn cho mình ở ba khối kia.

### 16.3 Hai khoảng trống còn lại: **được biện minh**

- **Đông Nam Á**: đã xử lý **đúng và đầy đủ** qua khối *"Ứng viên Việt Nam đã được cân nhắc"* — Hai Bà Trưng (40–43 CN, đúng nhóm CE01) được nêu đích danh, lý do loại khỏi atlas chính được nêu, và bà có mục riêng ở phụ lục `CH90-CE01_09-01`. Thêm nữa, sự kiện 43 CN được đưa vào phần văn xuôi của `-04`. Đây là mẫu mà khoảng trống Nam Á nên theo.
- **Châu Phi hạ Sahara, Châu Mỹ, Châu Đại Dương**: không có nhân vật nào định danh được bằng nguồn đương thời cho TK 1 CN. Khoảng trống này là **thật** và thuộc về tư liệu, không thuộc về người soạn. Không cần sửa, nhưng một câu trong Ghi chú biên tập nói ra điều đó sẽ nhất quán hơn.

### 16.4 Nhận xét cuối về chất lượng nhóm

Nhóm CE01 là nhóm **sạch nhất về nguồn** trong các nhóm đã rà: 12/12 nguồn thứ cấp có thật, đúng năm, đúng thể loại, đúng chủ đề — không có một nguồn ma nào, và lỗi "ghi sai thể loại" kiểu Fried & Unguru không lặp lại (Beck 2005 được ghi đúng là bản dịch). Quy tắc 3 (không bịa số chương) được tuân thủ tuyệt đối. Quy tắc 6 (ứng viên đã được chọn) lần đầu đạt 0 lỗi.

Điểm yếu tập trung vào **ba chỗ khác**:
1. **Mệnh đề tối cao không quy thuộc** — 7 ca trong 12 mục. Đây là lỗi lặp đi lặp lại và sửa được bằng một lượt rà cơ học: tìm mọi chuỗi "đầu tiên / sớm nhất / duy nhất / cổ nhất / không ai khác", và với mỗi chuỗi hoặc thêm chủ thể phát ngôn, hoặc thêm chữ hạn định ("còn lại", "theo ghi chép"), hoặc bỏ.
2. **Ứng viên bị loại không cùng thời** — việc tuân thủ quy tắc 6 đã đẩy ba mục xuống 0 ứng viên hợp lệ, và chỗ trống bị lấp bằng người lệch thế kỷ. Hướng sửa đúng không phải tìm thêm tên, mà là dùng **vế thứ hai của quy tắc 5**: *"Nếu giai đoạn đó thật sự không có ai để so, viết thẳng là không có — đó là một phát hiện về tư liệu."*
3. **Một lỗ hổng vùng không được thừa nhận** — xem 16.2.

Về **trung lập tôn giáo**, kết luận riêng: mục `-01` **không** trượt sang giọng tín lý ở bất kỳ đâu, và **không** trượt sang giọng bài bác. Ranh giới "phần sử gia chấp nhận / phần đến qua Phúc Âm" được đặt **đúng chỗ**, được nói rõ hai lần (trong mục và trong Ghi chú biên tập), và giải thích được vì sao niên đại để Trung bình. Chỗ duy nhất giọng trượt là **một câu**, và nó trượt theo hướng ít ai ngờ: không hạ thấp Giê-su mà **hạ thấp Do Thái giáo đương thời**, bằng đúng sơ đồ "nệ luật / thương xót" mà nguồn được dẫn ra để đỡ nó đã dành cả sự nghiệp để bác. Sửa một câu ấy là đủ. Mục `-02` không cần sửa về giọng.
