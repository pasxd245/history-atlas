# Bình duyệt độc lập — `content/ch03.md`, nhóm **BCE02** (TK 2 TCN, 200–101 TCN)

Người rà: agent bình duyệt độc lập (không viết chapter này). Ngày: 2026-10-31.
Phạm vi: dòng `**Bối cảnh**` của nhóm BCE02 + 11 mục `CH03-BCE02-01` → `-11`.
Đối chiếu: Wikidata API (`wbgetentities`), nguồn gốc nơi mở được, `prompts/atlas-prompt.md` §5, `CONTRIBUTING.md`.

Xếp loại: **Sai** (khẳng định sai sự thật) · **Nghi vấn** (không đứng vững / không kiểm được / trình bày gây hiểu nhầm) · **Thiếu** (bỏ sót cần bổ sung) · **Thể thức** (vi phạm template §5 hoặc quy tắc trung lập).

---

## Tóm tắt Wikidata (đã kiểm bằng API, 2026-10-31)

| ID | Q-ID | Nhãn Wikidata (en) | P569 / P570 | Trường `năm:` trong mục | Kết luận |
|---|---|---|---|---|---|
| -01 | Q445626 | Dong Zhongshu | −179 / −104 | k. 179–104 | khớp |
| -02 | Q7225 | Emperor Wu of Han | −156-06-07 / −87-03-29 | 156–87 | khớp |
| -03 | Q159905 | Hipparchus | −190 / −120 | k. 190–120 | khớp |
| -04 | Q131169 | Polybius | −200/−212/−211 / −120,−132,−130,−129 | k. 200–118 | khớp (trong ±25) |
| -05 | Q197276 | Zhang Qian | **−200** (precision 11!) / −114 | **k. 164**–114 | **lệch 36 năm** — xem phát hiện -05 |
| -06 | Q231680 | Patanjali | không có P569/P570 | hoạt động k. 160–140 | không đối chiếu được |
| -07 | Q347878 | Menander I | −300 (prec. thế kỷ) / −130 | trị vì k. 165–130 | khớp |
| -08 | Q180109 | Apollonius of Perga | −262/−260/−240 / −190/−180/−170 | k. 240–190 | khớp (độ tin cậy Thấp) |
| -09 | Q212109 | Tiberius Gracchus | −162 / −133 | k. 163–133 | khớp, đúng người (quan bảo dân, không phải cha ông) |
| -10 | Q284994 | Carneades | −213 / −129 | k. 214–129 | khớp |
| -11 | Q111559 | Judah Maccabee | −500 (prec. thiên niên kỷ) / −160 | hoạt động k. 167–160 | khớp; mục đã xử lý đúng chỗ P569 vô dụng |

Mọi Q-ID đều trỏ đúng nhân vật định trỏ. **Không có lỗi Q-ID trỏ nhầm người trong nhóm này.**

---

## Bản đồ liên kết (đã mở từng đích đến để đọc tên)

| Nguồn | Đích | Tên thật của đích | Chiều/đúng? |
|---|---|---|---|
| -01 kế thừa | CH03-BCE04-04 | Mạnh Tử | đúng |
| -01 kế thừa | CH02-BCE06-01 | Khổng Tử | đúng |
| -01 ảnh hưởng | CH03-BCE02-02 | Hán Vũ Đế | đúng |
| -02 kế thừa | CH03-BCE02-01 / CH03-BCE03-02 | Đổng Trọng Thư / Tần Thủy Hoàng | đúng |
| -02 ảnh hưởng | CH03-BCE02-05 / CH90-BCE03_01-02 / CH03-BCE01-06 | Trương Khiên / **Triệu Đà** / Tư Mã Thiên | xem phát hiện -02 |
| -03 kế thừa | CH03-BCE04-09 / CH03-BCE03-09 / CH03-BCE02-08 | Eudoxus / Eratosthenes / Apollonius | đúng |
| -04 kế thừa | CH02-BCE05-03 / CH03-BCE03-12 | **Herodotus** / **Hannibal** | xem phát hiện -04 |
| -04 ảnh hưởng | CH03-BCE01-03 | Cicero | đúng |
| -05 kế thừa | CH03-BCE02-02 | Hán Vũ Đế | đúng |
| -05 ảnh hưởng | CH03-BCE01-06 | Tư Mã Thiên | đúng |
| -06 kế thừa | CH02-BCE05-08 | Pāṇini | đúng |
| -07 kế thừa | CH03-BCE03-01 / CH03-BCE04-03 | Ashoka / Alexander Đại đế | đúng |
| -08 kế thừa | CH03-BCE03-03 / CH03-BCE03-05 | Euclid / Archimedes | đúng |
| -08 ảnh hưởng | CH03-BCE02-03 | Hipparchus | đúng |
| -09 ảnh hưởng | CH03-BCE01-01 | Julius Caesar | đúng |
| -10 kế thừa | CH03-BCE04-01 | Plato | đúng |
| -10 ảnh hưởng | CH03-BCE01-03 | Cicero | đúng |
| -11 ảnh hưởng | CH03-BCE01-07 | **Hillel Trưởng lão** | xem phát hiện -11 |

---

_(các phát hiện chi tiết được ghi tăng dần bên dưới, theo thứ tự mục)_

## Dòng `**Bối cảnh**` của nhóm

**Nghi vấn — "quyền lực duy nhất ở Địa Trung Hải"**
Trích: *"Rome thắng Carthage và Macedonia, trở thành quyền lực duy nhất ở Địa Trung Hải nhưng bắt đầu khủng hoảng ruộng đất trong nước."*
Cái đúng: trong TK 2 TCN Rome là **bá quyền** chứ chưa phải quyền lực duy nhất. Ai Cập Ptolemaic giữ độc lập tới 30 TCN (chính chapter này có mục Cleopatra VII `CH03-BCE01-09` ở nhóm sau), nhà Seleukos vẫn tồn tại sau Magnesia (190 TCN) tới 63 TCN, và chính nhóm BCE02 này có hai mục Hellenistic–Hy Lạp Ấn còn đang cai trị (`-07` Menandros). Chữ "duy nhất" là tô vẽ, prompt dự án cấm.
Nguồn: chính các mục trong cùng file (`CH03-BCE01-09`, `CH03-BCE02-07`).
Đề xuất: *"Rome thắng Carthage và Macedonia, thành bá quyền ở Địa Trung Hải nhưng bắt đầu khủng hoảng ruộng đất trong nước."*

**Nghi vấn — "đặt Nho học làm học vấn chính thức" mâu thuẫn với chính Ghi chú biên tập của file**
Trích: *"Nhà Hán củng cố đế chế, đặt Nho học làm học vấn chính thức…"*
Vấn đề: dòng 822 của chính file ghi *"mức độ ông thực sự quyết định việc nhà Hán tôn Nho học là điểm tranh luận; Loewe (2011) cho rằng vai trò ấy do truyền thống sau gán"*, và mục `-01` cũng nhắc lại. Nhưng Bối cảnh lại khẳng định trơn việc "đặt Nho học làm học vấn chính thức" như một sự kiện đã rồi của TK 2 TCN. Đây đúng là mệnh đề mà Loewe và Nylan phản bác (họ cho rằng việc "độc tôn Nho thuật" là cấu trúc hồi cố thời Đông Hán trở đi).
Đề xuất: *"Nhà Hán củng cố đế chế, đưa kinh điển Nho gia vào bộ máy tuyển quan và mở đường sang Trung Á."*

**Thể thức — vượt trần 60 chữ**
Dòng Bối cảnh dài 63 chữ (đếm âm tiết), template §5 quy định ≤ 60. Cắt chữ "duy nhất" theo đề xuất trên là về đúng trần.

---

## CH03-BCE02-01 · Đổng Trọng Thư

**Sai — "khoa cử … thời Hán" là lỗi niên đại thể chế**
Trích (`**Ảnh hưởng tới:**`): *"- Thể chế khoa cử và kinh học thời Hán · kế thừa · qua trường phái"*
Cái đúng: **nhà Hán không có khoa cử.** Chế độ tuyển quan thời Hán là **sát cử / tiến cử** (察舉, hiếu liêm, mậu tài) cộng với chế độ đệ tử viên ở Thái học; thi tuyển theo khoa mục (khoa cử) bắt đầu từ nhà Tùy (thường tính 587 CN) và định hình dưới nhà Đường. Viết "thể chế khoa cử … thời Hán" là gộp hai thiết chế cách nhau bảy thế kỷ.
Nguồn: chinaknowledge.de, mục *boshi* 博士 và *Taixue*; Wikipedia *Imperial examination* ("the imperial examination system… Sui dynasty").
Đề xuất: *"- Chế độ sát cử và kinh học thời Hán · kế thừa · qua trường phái"*

**Sai — gán cho Công Tôn Hoằng việc đặt chức bác sĩ Ngũ kinh năm 136 TCN**
Trích: *"Ứng viên cùng thời là Công Tôn Hoằng, thừa tướng xuất thân Nho sinh và là người thực sự đẩy việc đặt chức bác sĩ Ngũ kinh"*
Cái đúng: chức bác sĩ Ngũ kinh được đặt năm **136 TCN**, khi Công Tôn Hoằng **chưa làm thừa tướng** (ông nhậm thừa tướng năm **124 TCN**). Việc ông thật sự đẩy, với tư cách thừa tướng, là tờ tấu năm 124 TCN lập **Thái học** và đặt **đệ tử viên** (học trò) cho các chức bác sĩ — tức thiết chế 124, không phải 136. Mục `-02` trong cùng nhóm ghi đúng hai mốc này (136 và 124), nên mục `-01` tự mâu thuẫn với mục kế bên.
Nguồn: chinaknowledge.de mục *boshi* 博士 ("In 136 BCE, Emperor Wu created the first posts for erudites for the whole corpus of the Five Classics"); Wikipedia *Taixue* / *Gongsun Hong* ("The Taixue… came into existence by recommendation of Gongsun Hong, chancellor under Wu", 124 TCN).
Đề xuất: *"Ứng viên cùng thời là Công Tôn Hoằng (k. 200–121 TCN), thừa tướng xuất thân Nho sinh, người dâng tấu lập Thái học và đặt đệ tử viên năm 124 TCN, và Lưu An (179–122 TCN), chủ biên Hoài Nam tử."*

**Thể thức — "và Lưu An" nêu tên trần, không có lý do**
Trích: *"…và Lưu An."* §5 đòi nêu đích danh ứng viên **kèm lý do người được chọn vượt trội theo (a)–(d)**. Lưu An được thả vào câu không một chữ mô tả, nên không đáp ứng. (Về mặt niên đại thì ông **đúng là cùng thời**: 179–122 TCN so với Đổng k. 179–104 TCN — chỗ này không sai.)
Đề xuất: ghép vào câu sửa ở trên.

**Nghi vấn — "lập luận sớm được dẫn nhiều nhất"**
Trích: *"Các đối sách ông dâng lên Hán Vũ Đế là lập luận sớm được dẫn nhiều nhất cho việc lấy Nho học làm học vấn nhà nước."*
Mệnh đề so sánh tối cao ("được dẫn nhiều nhất") không quy thuộc. Nhẹ hơn các lỗi trên vì nó nói về tần suất trích dẫn chứ không về sự thật lịch sử, nhưng vẫn nên quy thuộc hoặc hạ giọng.
Đề xuất: *"Các đối sách ông dâng lên Hán Vũ Đế, chép trong Hán thư, là lập luận thường được dẫn nhất cho việc lấy Nho học làm học vấn nhà nước."*

**Đã kiểm, không có lỗi:** Q445626 = Dong Zhongshu, P569 −179 / P570 −104, khớp `k. 179–104 TCN`. Cả hai nguồn có thật: Sarah A. Queen, *From Chronicle to Canon: The Hermeneutics of the Spring and Autumn according to Tung Chung-shu*, Cambridge UP 1996; Michael Loewe, *Dong Zhongshu, a 'Confucian' Heritage and the Chunqiu fanlu*, Brill 2011 — và Loewe 2011 **đúng là** công trình lập luận rằng vai trò của Đổng bị truyền thống sau phóng đại, tức nguồn có bàn đúng điều được dẫn. Phần nêu caveat Loewe trong "Vì sao chọn" là điểm mạnh của mục này.

---

## CH03-BCE02-02 · Hán Vũ Đế

**Thể thức (nặng) — cả hai "ứng viên" đều KHÔNG cùng thời**
Trích: *"Ứng viên cùng triều là Hán Cao Tổ, người lập nhà Hán, và Hán Văn Đế, người để lại thời thịnh trị."*
Cái đúng: Hán Cao Tổ (Lưu Bang) mất **195 TCN**, tức **39 năm trước khi Hán Vũ Đế sinh (156 TCN)**. Hán Văn Đế (203–157 TCN) mất **157 TCN**, đúng **một năm trước** khi Hán Vũ Đế sinh. Không ai trong hai người sống cùng lúc với nhân vật được chọn một ngày nào. Đây đúng loại lỗi mà `CONTRIBUTING.md` mục 5 ("Ứng viên cùng thời phải thật sự cùng thời") liệt kê. Chữ "cùng triều" thay cho "cùng thời" không cứu được, vì §5 viết rõ "cùng lĩnh vực, **cùng thời**".
Nguồn: Wikidata Q7225 (P569 −156-06-07); niên đại Lưu Bang và Lưu Hằng theo Hán thư/Sử ký.
Đề xuất: *"Ứng viên cùng thời là Hoài Nam vương Lưu An (179–122 TCN), người tập hợp Hoài Nam tử và chủ trương vô vi làm đường lối trị nước, và thừa tướng Công Tôn Hoằng (k. 200–121 TCN). Hán Vũ Đế được chọn theo counterfactual (d): …"* — hoặc giữ Cao Tổ/Văn Đế nhưng nói thẳng rằng đây là **so với người tiền nhiệm, không phải ứng viên cùng thời**, và nêu lý do vì sao nhóm này không có vua cùng thời nào cạnh tranh được.

**Nghi vấn — liên kết `Ảnh hưởng tới: CH90-BCE03_01-02` (Triệu Đà) lệch 26 năm và sai loại quan hệ**
Trích: *"- CH90-BCE03_01-02 · phản bác · trực tiếp"*; lý do nêu ở Ghi chú biên tập dòng 816: *"việc nhà Hán diệt Nam Việt năm 111 TCN là sự kiện mở đầu thời Bắc thuộc"*.
Vấn đề: mục đích đến (`content/ch90.md` dòng 23) ghi **Triệu Đà trị vì 207–137 TCN**. Sự kiện 111 TCN xảy ra **26 năm sau khi Triệu Đà mất**, dưới đời Triệu Kiến Đức và tể tướng Lữ Gia — mà Lữ Gia chính là người được nêu trong mục Triệu Đà. Hán Vũ Đế (trị vì 141–87 TCN) chỉ chồng lấn với Triệu Đà đúng 4 năm (141–137), và trong 4 năm đó không có xung đột nào được viện ra. Thêm nữa, `phản bác` trong từ vựng dự án là **quan hệ tư tưởng** (bác bỏ một luận điểm), dùng cho một cuộc chinh phạt quân sự là sai ngữ nghĩa.
Đây là loại lỗi mà lint **không bắt được**, vì lint chỉ quét chiều `Kế thừa từ` (xác nhận: `reports/lint-ch03.txt` dòng 21 chỉ báo INFO về việc thiếu chiều ngược, không kiểm nội dung).
Đề xuất: bỏ liên kết này, hoặc giữ nhưng sửa thành quan hệ đúng chiều lịch sử và nói rõ đích đến là **nhà nước** chứ không phải **con người**: *"- Nhà nước Nam Việt do Triệu Đà lập, bị nhà Hán diệt năm 111 TCN (xem CH90-BCE03_01-02) · phản bác · trực tiếp"*, kèm sửa dòng 816 cho khớp.

**Nghi vấn — "mở đường cho việc quan lại được chọn qua kinh điển thay vì qua dòng dõi"**
Trích như trên. Thời Hán, cửa chính vào quan trường vẫn là **tiến cử** (hiếu liêm, hiền lương phương chính) và **nhậm tử** (ấm chức theo cha), chứ không phải thi theo kinh điển; Thái học 124 TCN mới chỉ tạo ra một kênh song song quy mô nhỏ (ban đầu 50 đệ tử viên). Câu hiện tại dễ khiến người đọc hiểu là Hán đã thay thế chế độ dòng dõi.
Đề xuất: *"…mở thêm một kênh để quan lại được chọn qua kinh điển bên cạnh tiến cử và ấm chức."*

**Đã kiểm, KHÔNG có lỗi — toàn bộ chuỗi niên đại của mục này đúng:**
- "năm mươi tư năm trị vì" — 141–87 TCN ✔
- chức bác sĩ Ngũ kinh **136 TCN** ✔ (chinaknowledge.de, *boshi*)
- Thái học **124 TCN** ✔
- độc quyền muối và sắt **117 TCN** ✔ (Wikipedia *Han dynasty*: "nationalized private salt and iron industries in 117 BC"; Khổng Cẩn và Đông Quách Hàm Dương được bổ năm 117)
- diệt Nam Việt **111 TCN** ✔
- đặt quận ở Triều Tiên **108 TCN** ✔ (Lạc Lãng và bốn quận)
- Q7225 = Emperor Wu of Han, −156/−87 ✔ khớp `156–87 TCN`, độ tin cậy Cao hợp lệ
- Nguồn Michael Loewe, *Crisis and Conflict in Han China, 104 BC to AD 9* (Allen & Unwin, 1974) có thật; *Sử ký*, **Hiếu Vũ bản kỷ** (q. 12) và **Bình chuẩn thư** (q. 30) là hai thiên có thật và đúng là nơi chép chính sách quân thâu bình chuẩn — mục này **không** ghi số quyển nên không vướng lỗi "số quyển bịa".

---

## CH03-BCE02-03 · Hipparchus xứ Nicaea

**Thể thức (nặng) — cả hai "ứng viên" đều không cùng thời, và một người còn KHÔNG bị loại**
Trích: *"Ứng viên là Aristarchus xứ Samos, người đề xuất mô hình nhật tâm sớm hơn, và Apollonius xứ Perga, người cung cấp hình học ngoại luân."*
Hai lỗi chồng lên nhau:
1. **Aristarchus** (k. 310–230 TCN) mất khoảng **40 năm trước khi Hipparchus sinh** (k. 190 TCN). **Apollonius** theo chính mục `-08` là **k. 240–190 TCN**, tức mất đúng vào năm Hipparchus sinh. Không ai cùng thời.
2. **Apollonius không hề bị loại** — ông là mục `CH03-BCE02-08` **trong chính nhóm này**, và mục `-03` còn ghi ông ở `Kế thừa từ`. Nêu một người đã được chọn làm "ứng viên bị loại" là vô nghĩa về thể thức. (Mục `-08` làm chuyện tương tự với Archimedes nhưng **nói thẳng** "đã được chọn ở nhóm trước", nên ở đó là minh bạch; ở đây thì không.)
Nguồn: niên đại Aristarchus theo mục chuẩn của Dictionary of Scientific Biography; niên đại Apollonius lấy từ chính `CH03-BCE02-08` và Wikidata Q180109.
Đề xuất: *"Ứng viên cùng thời là Seleukos xứ Seleukia (hoạt động k. 150 TCN), người duy nhất thời ấy còn bênh mô hình nhật tâm của Aristarchus, và Hypsicles xứ Alexandria (k. 190–120 TCN), người đưa cách chia 360 độ của Babylon vào thiên văn Hy Lạp. Hipparchus được chọn theo…"*

**Nghi vấn — "trục quay Trái Đất dịch chậm" là khung khái niệm thời sau, gán ngược cho Hipparchus**
Trích: *"ông phát hiện trục quay Trái Đất dịch chậm, tức hiện tượng tiến động điểm xuân phân"*
Cái đúng: trong khung địa tâm của Hipparchus **không có "trục quay Trái Đất"** để mà dịch. Điều ông kết luận là **các điểm phân dịch chuyển dọc hoàng đạo**, với tốc độ "không nhỏ hơn 1 độ mỗi thế kỷ". Giải thích bằng trục quay Trái Đất là cách đọc sau Copernicus–Newton.
Nguồn: Wikipedia *Hipparchus*: "he concluded that the equinoxes were moving ('precessing') through the zodiac, and that the rate of precession was not less than 1° in a century."
Đề xuất: *"…ông phát hiện các điểm phân dịch chuyển chậm dọc hoàng đạo — hiện tượng tiến động điểm xuân phân, mà vật lý sau này quy về chuyển động của trục quay Trái Đất…"*

**Nghi vấn — "lập danh mục sao có ghi độ sáng" là quy thuộc còn tranh cãi, nêu như sự thật**
Trích: *"Ông lập danh mục sao có ghi độ sáng"*
Cái đúng: việc Hipparchus lập **danh mục sao** thì có cơ sở (Ptolemy dẫn lại), nhưng việc ông sáng tạo **hệ cấp sao / độ sáng** chỉ dựa vào một câu mơ hồ của Pliny Cả và **không kiểm được** từ chính tác phẩm còn lại của ông (bình giải thơ Aratus). Nhiều học giả quy hệ cấp sao cho Ptolemy.
Nguồn: Wikipedia *Hipparchus*: "This hypothesis is based on the vague statement by Pliny the Elder but cannot be proven by the data in Hipparchus's commentary on Aratus's poem."
Đề xuất: *"Ông lập danh mục sao — truyền thống về sau, dựa vào một ghi chép của Pliny Cả, còn gán cho ông cả hệ cấp sao, nhưng điều này không kiểm được."*

**Đã kiểm, KHÔNG có lỗi:**
- Q159905 = Hipparchus, −190/−120 ✔ khớp `k. 190–120 TCN`.
- "số liệu của Timocharis một thế kỷ rưỡi trước" ✔ — Timocharis quan trắc k. 295–272 TCN, Hipparchus k. 130 TCN, cách nhau ~150 năm; Ptolemy đúng là chép việc Hipparchus so sao Spica với số liệu Timocharis và Aristillus.
- **Số quyển Almagest đúng** — mục ghi "q. III và VII". Mục lục Almagest: **q. III** = độ dài năm và chuyển động Mặt Trời, nơi phát biểu phát hiện tiến động của Hipparchus; **q. VII–VIII** = chuyển động định tinh, tiến động và danh mục 1022 sao. Cả hai số đều mở mục lục ra kiểm được, **không phải số bịa**.
- Toomer, "Hipparchus", *Dictionary of Scientific Biography* (1978) có thật — đây là mục tiêu chuẩn của DSB, do chính Toomer viết.

---

## CH03-BCE02-04 · Polybius

**Thể thức (nặng) — Timaeus xứ Tauromenium không cùng thời (cách 60 năm)**
Trích: *"Ứng viên cùng lĩnh vực là Cato Cả, người viết bộ sử Latinh đầu tiên, và Timaeus xứ Tauromenium, người ông phê phán nhiều nhất."*
Cái đúng: Timaeus sinh k. **356/350 TCN**, mất k. **260 TCN** — tức mất khoảng **60 năm trước khi Polybius sinh** (k. 200 TCN). Ông là **đối tượng phê phán trong quyển XII**, không phải ứng viên cạnh tranh cùng thời. (Cato Cả, 234–149 TCN, thì **đúng là cùng thời** với Polybius k. 200–118 TCN — nửa đúng.)
Nguồn: Wikipedia *Timaeus (historian)*: "born 356 or 350 BC; died c. 260 BC"; Wikipedia *Polybius* (phê phán Timaeus ở Book XII).
Đề xuất: *"Ứng viên cùng lĩnh vực và cùng thời là Cato Cả (234–149 TCN), người viết bộ sử Latinh đầu tiên, và Posidonius thì muộn hơn một thế hệ nên đã được xét ở nhóm BCE01."* — hoặc giữ Timaeus nhưng đổi vai: ghi rõ ông là **đối tượng phê phán**, và thay bằng một ứng viên cùng thời thật (vd. Agatharchides xứ Cnidus, k. 215–145 TCN).

**Nghi vấn — `Kế thừa từ: CH02-BCE05-03` (Herodotus) đặt sai tổ tiên**
Trích: *"- CH02-BCE05-03 · kế thừa · qua trường phái"*
Vấn đề: người Polybius tự nhận nối tiếp là **Thucydides** (về tính khách quan, truy nguyên nhân, dùng nhân chứng) — chính ba đặc trưng mà đoạn "Tư tưởng" của mục này liệt kê. Với **Herodotus** thì quan hệ của ông là phê phán/xa cách, không phải kế thừa. Thucydides không có mục trong atlas (`content/ch02.md` không có), nên liên kết này có vẻ là "chọn người gần nhất còn có ID" chứ không phải quan hệ thật.
Đề xuất: đổi loại quan hệ thành `tương đồng độc lập`, hoặc thay bằng một dòng văn bản tự do: *"- Thucydides (không có mục trong atlas) · kế thừa · qua trường phái"*.

**Nghi vấn — `Kế thừa từ: CH03-BCE03-12` (Hannibal) · `kế thừa` · `suy đoán học giả` là sai ngữ nghĩa quan hệ**
Trích: *"- CH03-BCE03-12 · kế thừa · suy đoán học giả"*
Vấn đề: Hannibal là **đề tài** của Polybius (quyển III), không phải nguồn tư tưởng ông kế thừa. "Kế thừa từ Hannibal" không có nội dung kiểm được. Nếu ý là Polybius dựa vào tư liệu phía Carthage và lời kể về Hannibal, thì đó là quan hệ **sử liệu**, mà từ vựng bốn loại của dự án (`kế thừa|tổng hợp|phản bác|tương đồng độc lập`) không có chỗ cho — tức nên bỏ chứ không nên ép.
Đề xuất: xoá dòng này; nếu muốn giữ liên hệ Hannibal–Polybius thì đặt ở phía Hannibal (`Ảnh hưởng tới`) với diễn đạt "là đề tài trung tâm của…", hoặc bỏ hẳn.

**Trung lập — mệnh đề tối cao không quy thuộc**
Trích: *"nên ông ảnh hưởng tới thiết kế hiến pháp cận đại nhiều hơn bất kỳ sử gia cổ đại nào khác."*
Đây là so sánh tối cao ("nhiều hơn bất kỳ… nào khác") không nói theo ai. Prompt §Ngôn ngữ cấm tô vẽ; `CONTRIBUTING.md` xếp loại này là "mục nghiêng lệch".
Đề xuất: *"…nên quyển VI là văn bản cổ đại được giới lập hiến thế kỷ 18 dẫn lại nhiều nhất bên cạnh Aristotle."* — hoặc quy thuộc thẳng: *"theo Walbank và Fritz, …"*

**Đã kiểm, KHÔNG có lỗi:**
- Q131169 = Polybius; P569 −200/−212/−211, P570 −120/−132/−130/−129 — `k. 200–118 TCN` nằm trong dung sai Trung bình (±25) ✔
- **"bộ Lịch sử bốn mươi quyển" ĐÚNG** — Britannica: Histories gồm **40 quyển**, quyển cuối là mục lục; chỉ I–V còn nguyên. (Wikipedia EN có chỗ ghi 39; con số 40 là con số chuẩn, mục này không sai.)
- "trong năm mươi ba năm" ✔ — đúng công thức nổi tiếng của chính Polybius (220–168 TCN).
- "Bị đưa sang Rome làm con tin sau năm 167 TCN" ✔ (sau Pydna 168, nhóm 1000 con tin Achaea sang Rome năm 167).
- **"Quyển VI trình bày thuyết anacyclosis … thể chế hỗn hợp" ĐÚNG** — mở mục lục kiểm được: Book VI đúng là quyển về anacyclosis và hiến pháp hỗn hợp (chấp chính–nguyên lão–hội nghị). Dòng `**Nguồn:** Polybius, Lịch sử, q. VI` **khớp**, không phải số bịa.
- Walbank, *A Historical Commentary on Polybius*, 3 tập, 1957/1967/1979 ✔ — khoảng "(1957–1979)" đúng.
- `Ảnh hưởng tới: CH03-BCE01-03` = Cicero ✔ đúng người, đúng chiều (De re publica dùng lại thể chế hỗn hợp).

---

## CH03-BCE02-05 · Trương Khiên

**Nghi vấn (niên đại) — năm sinh "k. 164" không có chỗ dựa và lệch 36 năm so với Wikidata**
Trích: *"`năm: k. 164–114 TCN … độ tin cậy niên đại: Trung bình | wikidata: Q197276`"*
Cái đúng: **năm sinh của Trương Khiên không được biết.** Wikidata Q197276 ghi P569 = **−200** (và ở độ chính xác "ngày": −0200-09-28, một con số vô nghĩa với một nhân vật như ông); Wikipedia EN ghi infobox "Born 195 BC" trong khi một bản mẫu ở cuối trang lại ghi "(164 BC–113 BC)" — tức chính nguồn tự mâu thuẫn. Britannica chỉ ghi "died 114 BCE". Con số 164 vì vậy là **một trong ba phương án không được chọn có lý do**, và với `độ tin cậy: Trung bình` (dung sai ±25 năm theo `CONTRIBUTING.md`) thì nó **lệch 36 năm** so với giá trị Wikidata, tức vượt dung sai. `reports/lint-ch03.txt` không báo gì về chỗ này (các dòng BCE02 ở đó đều là INFO về liên kết), nên lỗi lọt.
Nguồn: Wikidata Q197276 (P569 −200, P570 −114); Wikipedia *Zhang Qian*.
Đề xuất: theo bảng quy ước `năm:` trong `CONTRIBUTING.md`, dùng dạng "chỉ biết khoảng hoạt động": *"`năm: hoạt động 138–114 TCN (năm sinh không rõ) | … | độ tin cậy niên đại: Thấp`"* — hạ xuống Thấp để khỏi bị đối chiếu với một P569 vốn không đáng tin.

**Thể thức (nặng) — cả hai "ứng viên" đều cách nhân vật hai thế kỷ**
Trích: *"Ứng viên cùng chức năng là Ban Siêu, người sau này thực sự kiểm soát Tây Vực, và Cam Anh, người đi xa về phía tây hơn."*
Cái đúng: **Ban Siêu 32–102 CN**, **Cam Anh** đi sứ năm **97 CN** — cách Trương Khiên (mất 114 TCN) khoảng **210 năm**. §5 đòi ứng viên *cùng thời*. Mục có nói "Ban Siêu hoạt động hai thế kỷ sau" nên **không giấu giếm** — đó là điểm trung thực — nhưng vẫn không đáp ứng thể thức, và còn tự mâu thuẫn: không thể vừa gọi là "ứng viên" vừa nói người ấy sống hai thế kỷ sau.
Đề xuất: *"Ứng viên cùng thời là Vệ Thanh và Hoắc Khứ Bệnh, hai tướng cùng chiến dịch Hung Nô với ông, và sứ thần Vương Khôi. Trương Khiên được chọn theo counterfactual (d) và tính nguyên bản (c)… Ban Siêu (32–102 CN) thường được so sánh nhưng hoạt động hai thế kỷ sau, trên chính hiểu biết do ông mang về."* — tức chuyển Ban Siêu/Cam Anh ra khỏi vai "ứng viên" và đặt vào vai "người kế tục".

**Nghi vấn — nguồn Hansen (2012) được dẫn để đỡ cho một câu mà chính luận điểm của sách phản bác**
Trích: *"Các đoàn sứ và buôn bán theo sau hình thành mạng đường mà sau gọi là Con đường tơ lụa."* kèm `**Nguồn:** … Valerie Hansen, The Silk Road: A New History (2012).`
Vấn đề: sách **có thật**, **có bàn** về Trương Khiên (Hansen mở đầu bằng chính ông), nên không phải nguồn ma. Nhưng luận điểm trung tâm của Hansen đi **ngược chiều** với câu được dẫn: bà lập luận rằng thương mại đường dài trên tuyến này là **nhỏ lẻ, chủ yếu là buôn bán địa phương**, và gọi Con đường tơ lụa là *"one of the least traveled routes in human history"* — nhiều đồng nghiệp còn nghi ngờ chính luận điểm đó của bà. Hansen cũng nhấn rằng bản chép sớm nhất về chuyến đi của Trương Khiên ra đời **ít nhất 150 năm sau** và thiếu cả lộ trình cụ thể. Dẫn Hansen mà viết như thể bà chứng minh "mạng buôn bán hình thành" là dùng nguồn ngược ý.
Nguồn: Wikipedia *The Silk Road: A New History*; nội dung dẫn lại từ chính sách.
Đề xuất: *"Các đoàn sứ theo sau mở ra tuyến tiếp xúc Á–Âu mà đời sau gọi là Con đường tơ lụa; Hansen (2012) nhấn rằng lưu lượng thương mại thực tế trên tuyến này nhỏ hơn hình dung phổ biến nhiều, và rằng bản chép sớm nhất về chuyến đi ra đời ít nhất 150 năm sau."*

**Đã kiểm, KHÔNG có lỗi:**
- Đi **138 TCN** ✔, về **126 TCN** ✔ (Hansen ghi "returned around 126 BCE"; Wikipedia EN ghi 125 — 126 là con số thường dùng, chấp nhận được), "bị bắt giữ hơn mười năm" ✔.
- Danh sách nước: Đại Uyển (Ferghana), Khang Cư (Transoxiana), Đại Hạ (Bactria), An Tức (Parthia), tin tức về Thân Độc (Ấn Độ) ✔ — đúng đúng danh sách của Sử ký 123.
- 鑿空 "tạc không" ✔ là chữ trong chính thiên đó.
- **Số quyển Sử ký ĐÚNG và đã mở mục lục kiểm**: *Đại Uyển liệt truyện* **đúng là quyển 123** (Wikipedia *Dayuan* dẫn trực tiếp "Shiji, 123"; Burton Watson, *Records of the Grand Historian: Han Dynasty II*, dịch "Shi Ji 123, The Account of Dayuan"). Đây là một trong số ít dòng Nguồn trong nhóm có ghi số quyển — và nó **không bịa**.
- Q197276 = Zhang Qian ✔ đúng người; liên kết `-02` (Hán Vũ Đế) và `CH03-BCE01-06` (Tư Mã Thiên) đều đúng người, đúng chiều, đúng niên đại.

---

## CH03-BCE02-06 · Patañjali

**Sai (nguồn không nói điều được dẫn) — Bronkhorst (1985) KHÔNG bàn tới nhà văn phạm**
Trích (Ghi chú biên tập, dòng 821): *"Bronkhorst (1985) lập luận đây là những người khác nhau."* và `**Nguồn:** … Johannes Bronkhorst, "Patañjali and the Yoga Sūtras", Studien zur Indologie und Iranistik 10 (1985).`
Tôi đã **tải và đọc toàn văn bài báo** (bản tác giả tự lưu trên kho UNIL/SERVAL). Kết quả:
- Trang đầu ghi đúng: *"Published in: Studien zur Indologie und Iranistik 10 (1984 [1985]), pp. 191-212"* — vậy bài **có thật**, và ghi năm 1985 là chấp nhận được (dạng chuẩn hơn: `10 (1984 [1985]), 191–212`).
- **Nhưng nội dung không phải điều được dẫn.** Bài hoàn toàn bàn về quan hệ giữa *Yogasūtra* và *Yogabhāṣya*. Kết luận của Bronkhorst (mục 3): các Yoga sūtra **vốn không thuộc cùng một chỉnh thể**, chúng được **chính tác giả của Yogabhāṣya gom lại**, và người đó là một trong hai thầy Sāṃkhya mà *Yuktidīpikā* biết tới — **Patañjali hoặc Vindhyavāsin**. Nguyên văn phần kết: *"the available evidence points to two persons, Patañjali and Vindhyavāsin, both of whom are known as Sāṃkhya teachers"*.
- Trong toàn bài **không có một lần nào** các chữ *grammar / grammarian*; cũng không có đoạn nào so sánh tác giả *Mahābhāṣya* với tác giả Yoga. Tức bài **không hề lập luận** rằng nhà văn phạm và tác giả Yoga Sūtra là hai người khác nhau. Nó còn nghiêng về phía *gộp* hai vai Yogasūtra–Yogabhāṣya làm một.
Hệ quả kép: (1) câu ở Ghi chú biên tập gán cho Bronkhorst một luận điểm ông không nêu trong bài được dẫn; (2) với **chính mục `-06`** — vốn viết **chỉ** về nhà văn phạm và bộ *Mahābhāṣya* — thì Bronkhorst 1985 **không bàn tới bất kỳ điều gì trong mục**, nên một trong hai nguồn của mục là nguồn không liên quan. Đây đúng loại lỗi mà `CONTRIBUTING.md` gọi là "nguồn… không nói điều được dẫn" và nêu làm tiền lệ (ca SEP không nhắc Solon ở Ch2).
Đề xuất: thay bằng nguồn thật sự bàn chuyện định danh, ví dụ **Philipp A. Maas, "A Concise Historiography of Classical Yoga Philosophy", trong *Periodization and Historiography of Indian Philosophy*, Vienna 2013** (khảo sát thẳng việc quy thuộc Patañjali), hoặc giữ Bronkhorst nhưng sửa câu ở dòng 821 thành: *"Bronkhorst (1984 [1985]) lập luận rằng chính Yogasūtra không phải tác phẩm của một tác giả duy nhất mà do người soạn Yogabhāṣya gom lại — tức ngay trong nhánh Yoga, 'Patañjali' đã là một danh xưng có vấn đề; việc nhà văn phạm có phải cùng người hay không là một câu hỏi khác, xem Maas (2013)."*

**Thiếu — chỗ Wikidata gộp người KHÔNG được xử lý trong chính mục**
Vấn đề: Q231680 tự mô tả là *"ancient Indian scholar(s) of grammar and linguistics, of yoga, of medical treatises"* (tôi đã kiểm bằng API: mục này **không có P569 và không có P570** — tức Wikidata cũng không dám gán niên đại cho một thực thể gộp). Mục `-06` xử lý một phần: `độ tin cậy: Thấp` ✔, `lĩnh vực: Ngôn ngữ học` (không lấn sang Y học/Tôn giáo) ✔, và câu *"bộ ba Pāṇini – Kātyāyana – Patañjali"* nói rõ ngữ cảnh văn phạm ✔. **Nhưng phần thân mục không nói một chữ nào** về việc Q-ID này là thực thể gộp; cảnh báo chỉ nằm ở Ghi chú biên tập cuối file, nơi người đọc một mục đơn lẻ (và trang HTML sinh ra cho từng nhân vật) sẽ không thấy.
Thêm nữa, so sánh **trong cùng chapter** thì cách xử lý không nhất quán: Euclid (`CH03-BCE03-03`) và Kauṭilya (`CH03-BCE04-07`) đều được gắn nhãn `[Tranh cãi lịch sử]` cho những vấn đề định danh tương đương, còn Patañjali thì không. Theo quy tắc 8 của prompt, đây đúng là ca "còn tranh cãi" đáng gắn nhãn.
Đề xuất: đổi tiêu đề thành `### CH03-BCE02-06 · Patañjali (पतञ्जलि) [Tranh cãi lịch sử]` và chèn vào cuối đoạn "Tư tưởng": *"Mục này chỉ nói về nhà văn phạm. Truyền thống Ấn Độ còn gán tên Patañjali cho tác giả Yoga Sūtra và một y thư; Wikidata Q231680 gộp cả ba vai và vì thế không ghi năm sinh năm mất."*

**Thể thức — không có ứng viên nào cùng thời**
Trích: *"Ứng viên trong cùng mạch là Kātyāyana, người soạn các vārttika mà ông bình giải, và Bhartṛhari ở thế kỷ 5 CN."*
Cái đúng: **Kātyāyana** thường đặt ở **TK 3 TCN**, tức trước Patañjali (hoạt động k. 160–140 TCN) khoảng **150 năm**, và ông là **tiền bối được bình giải**, không phải đối thủ cùng thời — mục còn tự ghi ông ở `Kế thừa từ`, nên nêu lại ở vai "ứng viên" là mâu thuẫn. **Bhartṛhari** TK 5 CN, muộn hơn **sáu thế kỷ** (mục tự nhận).
Thực tế: **không có ứng viên Ngôn ngữ học Nam Á nào cùng thời với Patañjali mà tư liệu cho phép nêu đích danh** — đó là kết luận hợp lệ, và §5 cho phép nói ra (quy tắc 2: "nếu thiếu ứng viên xứng đáng… ghi lý do").
Đề xuất: *"Không có nhà văn phạm nào cùng thời còn để lại tên để so sánh — nguồn Ấn Độ TK 2 TCN quá mỏng. Ứng viên được cân nhắc nằm ở hai đầu truyền thống: Kātyāyana (TK 3 TCN, tiền bối ông bình giải) và Bhartṛhari (TK 5 CN). Patañjali được chọn theo độ bền (b): …"*

**Đã kiểm, KHÔNG có lỗi:**
- Bộ ba **muni-traya** (Pāṇini – Kātyāyana – Patañjali) và nguyên tắc *yathottaraṃ munīnāṃ prāmāṇyam* ("vị sau có thẩm quyền hơn") ✔ — câu "với ông ở vị trí sau cùng, tức người chốt lại" đúng với truyền thống vyākaraṇa, không phải suy diễn.
- George Cardona, *Pāṇini: A Survey of Research* (Mouton, 1976) ✔ có thật và đúng là khảo sát bao gồm Mahābhāṣya.
- `Kế thừa từ: CH02-BCE05-08` = Pāṇini ✔ đúng người, đúng chiều.
- Trường `năm: hoạt động k. 160–140 TCN` đúng quy ước "chỉ biết khoảng hoạt động" của `CONTRIBUTING.md` ✔.

---

## CH03-BCE02-07 · Menandros I

**Thể thức — cả hai "ứng viên" đều không cùng thời, dù ứng viên cùng thời thật thì có sẵn**
Trích: *"Ứng viên cùng loại là Demetrios I, người mở đầu việc Hy Lạp tiến vào Ấn Độ, và Kanishka ở thế kỷ 2 CN."*
Cái đúng: **Demetrios I trị vì k. 200 – k. 180 TCN** (có bản kéo tới 167), tức **kết thúc trước khi Menandros lên ngôi** (k. 165/155 TCN) — không chồng lấn. **Kanishka** TK 2 CN, muộn gần **ba thế kỷ** (mục tự nhận). Trong khi đó **ứng viên cùng thời thật sự thì có**: **Eucratides I** (trị vì k. 170–145 TCN) là vua Hy Lạp–Bactria đối địch trực tiếp và chồng lấn gần như toàn bộ triều Menandros; **Antialcidas** và **Zoilus I** cũng nằm trong khung.
Nguồn: Wikipedia *Demetrius I of Bactria* ("c. 200 – c. 180 BC"); bảng niên biểu vua Hy Lạp–Ấn cùng trang.
Đề xuất: *"Ứng viên cùng thời là Eucratides I (trị vì k. 170–145 TCN), vua Hy Lạp–Bactria mạnh nhất cùng giai đoạn và là đối thủ trực tiếp, và Demetrios I (k. 200–180 TCN), người mở đầu việc Hy Lạp tiến vào Ấn Độ một thế hệ trước. Menandros được chọn theo tính nguyên bản (c): …"*

**Trung lập — "duy nhất" không quy thuộc**
Trích: *"ông là vị vua Hy Lạp duy nhất còn lại dấu vết dưới dạng một cuộc đối thoại triết học được chính truyền thống Phật giáo giữ"*
Mệnh đề "duy nhất" là loại khẳng định mà prompt yêu cầu quy thuộc hoặc hạ giọng. Ở đây nó nhiều khả năng đúng, nhưng vẫn nên viết thành *"vị vua Hy Lạp duy nhất mà ta biết còn lại dấu vết…"*.

**Đã kiểm, KHÔNG có lỗi:**
- Q347878 = Menander I, "Indo-Greek king" ✔ đúng người. P569 chỉ có độ chính xác thế kỷ nên mục dùng `trị vì k. 165–130 TCN` là xử lý đúng; con số này khớp mốc chuẩn **165/155 – 130 TCN**, và là chính niên đại Bopearachchi dùng — tức nguồn thứ hai của mục đúng là nguồn của con số.
- *Milindapañha* được xếp vào tạng kinh (Khuddaka Nikāya) của truyền thống **Miến Điện** ✔.
- Tiền hai mặt Hy Lạp / Kharoṣṭhī, có đồng mang pháp luân ✔.
- "trải từ Kabul tới vùng Punjab" ✔; Sagala = Sialkot, nay thuộc Pakistan ✔ (`vùng: Nam Á` nhất quán với quy ước "theo nơi làm việc thực tế" mà chapter tự đặt ở dòng 805).
- T. W. Rhys Davids, *The Questions of King Milinda*, Sacred Books of the East t. 35 (1890) và 36 (1894) ✔ — khoảng "(1890–1894)" đúng.
- Osmund Bopearachchi, *Monnaies gréco-bactriennes et indo-grecques: catalogue raisonné* (Bibliothèque nationale, 1991) ✔ có thật, đúng năm.

---

## CH03-BCE02-08 · Apollonius xứ Perga

**Sai — Fried & Unguru (2001) KHÔNG phải bản dịch**
Trích: *"`**Nguồn:** Apollonius, Conics, bản dịch và dẫn luận Michael N. Fried và Sabetai Unguru (2001)`"*
Cái đúng: Michael N. Fried & Sabetai Unguru, ***Apollonius of Perga's Conica: Text, Context, Subtext***, Leiden: Brill, 2001 (Mnemosyne Supplement 222, xii + 499 tr.) là một **chuyên khảo nghiên cứu**, không phải bản dịch *Conics*. Luận điểm chính của sách là phê phán truyền thống diễn giải *Conics* như "đại số hình học" và chứng minh mối quan tâm của Apollonius là thuần hình học. (Bản dịch tiếng Anh thì có, nhưng là việc khác: Fried dịch **riêng quyển IV** cho Green Lion Press, 2002; bản cổ điển là của T. L. Heath, 1896.)
Nguồn: Bryn Mawr Classical Review 2002.09.34; Isis (University of Chicago Press) ghi "Leiden: Brill, 2001. xii + 499 pp."
Đề xuất: *"**Nguồn:** Michael N. Fried và Sabetai Unguru, Apollonius of Perga's Conica: Text, Context, Subtext (Brill, 2001); Thomas Heath, A History of Greek Mathematics (1921), t. II."*

**Đã kiểm, KHÔNG có lỗi — và đây là mục làm "Vì sao chọn" đúng nhất nhóm:**
- *"Ứng viên là Archimedes, cũng làm việc trên hình cong và **đã được chọn ở nhóm trước**, và Conon xứ Samos."* — cả hai **thật sự cùng thời**: Archimedes 287–212 TCN chồng lấn Apollonius (k. 240–190) ở quãng 240–212; Conon xứ Samos (k. 280–220 TCN) chồng lấn ở quãng 240–220, và chính Apollonius nhắc Conon trong lời tựa quyển IV *Conics*. Thêm nữa, mục **nói thẳng** Archimedes đã được chọn ở nhóm trước thay vì giả vờ ông bị loại — đây là cách xử lý minh bạch mà các mục `-03`, `-05`, `-06`, `-07` nên theo.
- Q180109 = Apollonius of Perga ✔; `độ tin cậy: Thấp` + câu *"Niên đại chỉ suy từ các mốc gián tiếp"* là xử lý đúng với một P569 có **ba giá trị mâu thuẫn** (−262/−260/−240) và P570 cũng ba (−190/−180/−170).
- *Conics* **tám quyển** ✔; "Bốn quyển đầu còn bản Hy Lạp, ba quyển tiếp chỉ còn bản dịch Arab, quyển cuối mất" ✔ (I–IV Hy Lạp, V–VII Arab, VIII mất).
- Tên *ellipse / parabola / hyperbola* do ông đặt ✔; ba đường cong là ba lát cắt của **cùng một mặt nón** ✔ (trước ông, Menaechmus phải dùng ba nón khác nhau).
- Tương đương hình học giữa mô hình lệch tâm và ngoại luân ✔ (Ptolemy dẫn lại, Almagest XII.1).
- Heath, *A History of Greek Mathematics* (1921), **t. II** ✔ — bộ này đúng 2 tập, Apollonius nằm ở tập II (*From Aristarchus to Diophantus*). Số tập **không bịa**.
- `Ảnh hưởng tới: CH03-BCE02-03` = Hipparchus ✔ đúng người, đúng chiều, đúng niên đại.

---

## CH03-BCE02-09 · Tiberius Gracchus

**Thiếu / Nghi vấn — `Kế thừa từ: "Không xác định"` là bỏ sót, không phải sự thật về tư liệu**
Trích: *"**Kế thừa từ:**\n- Không xác định"*
Vấn đề: nguồn cổ đại **có** nêu đích danh những người đứng sau chương trình của ông: **Blossius xứ Cumae** (triết gia Khắc kỷ, cố vấn riêng) và **Diophanes xứ Mytilene** (thầy hùng biện) — Plutarch, *Tiberius Gracchus* 8 và 20, tức **chính nguồn mà mục này đã dẫn**; cộng với **Appius Claudius Pulcher** (bố vợ, nguyên lão trưởng) và **P. Mucius Scaevola** (chấp chính, nhà luật học) trong uỷ ban ruộng đất. Ghi "Không xác định" trong khi nguồn đã dẫn nói ra tên là bỏ sót có thể sửa được.
Đề xuất:
```
**Kế thừa từ:**
- Blossius xứ Cumae, triết gia Khắc kỷ cố vấn cho ông · kế thừa · trực tiếp
- CH03-BCE03-07 · kế thừa · qua trường phái
```
(mục `CH03-BCE03-07` là Zeno xứ Citium — đã kiểm, đúng người; liên kết này chỉ hợp lệ nếu chấp nhận mạch Khắc kỷ qua Blossius, nên để `qua trường phái`.)

**Trung lập (nhẹ) — hai mệnh đề cần quy thuộc**
1. Trích: *"Đây là lần đổ máu chính trị đầu tiên ở Rome sau nhiều thế kỷ."* Đây là **phát biểu của Plutarch** ("the first sedition among the citizens of Rome that fell out with murder and bloodshed, since the expulsion of the kings") và Appian, chứ không phải một dữ kiện trung lập — và nó là mệnh đề "đầu tiên" theo đúng loại mà prompt bắt phải cẩn trọng. Plutarch đã có trong dòng Nguồn, nên chỉ cần thêm "theo Plutarch".
2. Trích: *"hai bước đúng luật về hình thức nhưng phá vỡ thông lệ nhường nhịn giữa các cơ quan."* Việc bãi chức Marcus Octavius có "đúng luật về hình thức" hay không **chính là** điểm tranh cãi của giới nghiên cứu (nhiều người coi đó là hành vi vượt quyền chứ không phải hợp thức). Viết khẳng định một phía là nghiêng lệch.
Đề xuất: *"…— theo Plutarch là lần đổ máu chính trị đầu tiên ở Rome kể từ khi đuổi vua."* và *"…hai bước mà ông bảo vệ là đúng thẩm quyền bảo dân, còn phe nguyên lão coi là vượt quyền; dù đọc cách nào thì chúng cũng phá vỡ thông lệ nhường nhịn giữa các cơ quan."*

**Đã kiểm, KHÔNG có lỗi:**
- Q212109 = Tiberius Gracchus, P569 −162 / P570 −133, **đúng là quan bảo dân năm 133 chứ không phải người cha cùng tên** (P39 có chức bảo dân) ✔; `k. 163–133 TCN` khớp trong dung sai Trung bình.
- Quan bảo dân **133 TCN** ✔; *lex Sempronia agraria* giới hạn công điền ✔; đem luật ra hội nghị bình dân và bãi chức đồng liêu phủ quyết (Marcus Octavius) ✔; bị giết trong chính năm đó bởi đám do nguyên lão **Scipio Nasica Serapio** cầm đầu ✔.
- *"Ứng viên là Gaius Gracchus, em ông, … và Scipio Aemilianus."* — **cả hai đều thật sự cùng thời** ✔ (Gaius 154–121 TCN; Scipio Aemilianus 185–129 TCN). Đây là mục thứ hai trong nhóm vượt được quy tắc "cùng thời". (Gaius là em ruột, nhưng vẫn là ứng viên cạnh tranh thật cho chỗ này, không phải cộng sự.)
- Plutarch, *Tiberius Gracchus* ✔ có thật, không ghi số chương nên không vướng rủi ro số bịa.
- **Mary Beard, *SPQR* (2015), ch. 6 ĐÚNG** — đã mở mục lục kiểm: chương 6 tên *"New Politics"*, bắt đầu tr. 209, và **đúng là chương bàn về anh em Gracchi**. Số chương **không bịa**.
- `Ảnh hưởng tới: CH03-BCE01-01` = Julius Caesar ✔ đúng người, đúng chiều.

---

## CH03-BCE02-10 · Carneades xứ Cyrene

**Sai — "lời giải đầu tiên cho bài toán hành động mà không có chắc chắn" mâu thuẫn với chính câu trước đó**
Trích: *"Carneades được chọn theo tính nguyên bản (c): thang mức thuyết phục là **lời giải đầu tiên** cho bài toán hành động mà không có chắc chắn…"*
Cái đúng: lời giải **đầu tiên** cho bài toán này (bài toán *apraxia*, "không thể hành động") là của **Arcesilaus**, với tiêu chuẩn **to eulogon** ("cái hợp lý") — tức của chính người mà mục này vừa nêu ở câu trước như "người đưa Academy sang hướng hoài nghi trước đó", và cũng là người mục này ghi ở `Kế thừa từ`. Carneades đưa ra *pithanon* **sau đó vài thế hệ** và tinh chỉnh thêm (thang ba bậc: ấn tượng thuyết phục / thuyết phục và không bị bác / thuyết phục, không bị bác và đã được kiểm kỹ).
Nguồn: SEP, *Ancient Skepticism*: *"the skeptic, in acting without assenting, adheres to the reasonable (eulogon)"* — nói về Arcesilaus, và đặt ông trước Carneades "by several generations".
Đề xuất: *"…: Arcesilaus đã nêu tiêu chuẩn 'cái hợp lý' (eulogon) trước đó, nhưng Carneades là người biến nó thành một **thang có bậc** — ấn tượng thuyết phục, thuyết phục và không bị bác, thuyết phục đã qua kiểm kỹ — tức một lời giải có cấu trúc chứ không chỉ một nhãn."*

**Thể thức — ứng viên không cùng thời, dù hai ứng viên cùng thời hoàn hảo có sẵn ngay trong chính đoạn văn**
Trích: *"Ứng viên là Arcesilaus, người đưa Academy sang hướng hoài nghi trước đó, và Sextus Empiricus ở thế kỷ 2 CN, người để lại văn bản đầy đủ nhất."*
Cái đúng: **Arcesilaus 316/5 – 241/0 TCN**, mất **27 năm trước khi Carneades sinh** (k. 214/213 TCN) — không cùng thời. **Sextus Empiricus** TK 2 CN, muộn hơn **ba thế kỷ** (mục tự nhận). Trớ trêu là **đoạn "Tư tưởng" ngay phía trên đã nhắc sứ bộ 155 TCN**, mà sứ bộ ấy gồm đúng **ba triết gia cùng thời**: Carneades (Academy), **Diogenes xứ Babylon** (Khắc kỷ, k. 230–150/140 TCN) và **Critolaus** (Tiêu dao). Diogenes xứ Babylon là đối thủ tranh luận trực tiếp và cùng thời của ông; **Antipater xứ Tarsus** (mất k. 130/129 TCN) cũng vậy. Tức ứng viên cùng thời có sẵn, chỉ là không được dùng.
Nguồn: Wikipedia *Arcesilaus* ("316/5–241/0 BC"); SEP *Ancient Skepticism* (Diogenes xứ Babylon là đối thủ Khắc kỷ; sứ bộ ba triết gia năm 156/5 TCN).
Đề xuất: *"Ứng viên cùng thời là Diogenes xứ Babylon (k. 230–150 TCN), người đứng đầu phái Khắc kỷ và cùng đi sứ sang Rome với ông, và Antipater xứ Tarsus (mất k. 130 TCN), đối thủ tranh luận thường trực. Carneades được chọn theo tính nguyên bản (c): …"*

**Trung lập — "tổ tiên trực tiếp" không quy thuộc**
Trích: *"…và nó là tổ tiên trực tiếp của chủ nghĩa khả tín và của lập trường khả sai hiện đại."*
Quan hệ bắc cầu hai nghìn năm, viết ở mức "tổ tiên **trực tiếp**", không nói theo ai. Prompt yêu cầu không suy diễn quan hệ kế thừa khi thiếu bằng chứng tiếp xúc.
Đề xuất: *"…và giới nghiên cứu thường đọc nó như tiền thân của chủ nghĩa khả tín và của lập trường khả sai hiện đại."*

**Nghi vấn (nhẹ) — năm sứ bộ**
Trích: *"Trong sứ bộ sang Rome năm 155 TCN"*. SEP ghi **156/5 TCN**; 155 là con số thường dùng nên không sai, nhưng nếu muốn khớp đúng nguồn đang dẫn thì nên viết "156/155 TCN".

**Đã kiểm, KHÔNG có lỗi:**
- Q284994 = Carneades, −213/−129 ✔ khớp `k. 214–129 TCN` trong dung sai Trung bình.
- *pithanon* và tiêu chuẩn hành động ✔ (SEP: *"The persuasive (pithanon) is the convincing, or perhaps even the plausible"*).
- Hai bài giảng bênh rồi bác công lý ở Rome, khiến **Cato Cả** đòi trục xuất ✔ (SEP dẫn lại giai thoại, kèm lưu ý rằng mục đích là chứng minh các triết gia trước không có lập luận đủ mạnh — một sắc thái mục này bỏ qua nhưng không sai).
- **Nguồn SEP tồn tại và đúng chủ đề** — tôi đã mở `https://plato.stanford.edu/entries/skepticism-ancient/`: bài có thật, mục 3.2 bàn trực tiếp về Carneades, có cả *pithanon* lẫn sứ bộ Rome. Đây **không** phải ca "slug tồn tại nhưng không nhắc tới nhân vật" như Ch2 từng vướng.
- Cicero, *Academica* ✔ — đúng là nguồn chính còn lại về Carneades.
- `vùng: Châu Âu` cho người sinh ở Cyrene (Libya) nhưng làm việc ở Athens ✔ **nhất quán** với quy ước "theo nơi làm việc thực tế" mà chapter tự đặt ở dòng 805.
- `Ảnh hưởng tới: CH03-BCE01-03` = Cicero ✔ đúng người, đúng chiều (Cicero theo Academy hoài nghi qua Philo xứ Larissa).

---

## CH03-BCE02-11 · Judah Maccabee

**Nghi vấn — `Ảnh hưởng tới: CH03-BCE01-07` (Hillel Trưởng lão) không có nội dung đỡ**
Trích: *"- CH03-BCE01-07 · kế thừa · qua trường phái"* (và chiều ngược lại ở mục Hillel, dòng 715: *"- CH03-BCE02-11 · kế thừa · qua trường phái"*).
Vấn đề: tôi đã mở mục đích đến — đúng là **Hillel Trưởng lão**, nên không phải lỗi trỏ nhầm người. Nhưng **không có gì trong mục Hillel đỡ cho quan hệ này**: phần "Tư tưởng" của ông nói về bảy quy tắc diễn giải, prosbul và tranh luận Hillel–Shammai, không một chữ nào về Maccabee hay Hasmonean. Về mặt lịch sử, quan hệ giữa phái Pharisee (mạch của Hillel) và triều Hasmonean phần lớn là **đối kháng** — John Hyrcanus đoạn tuyệt với họ, Alexander Jannaeus đàn áp họ — nên "kế thừa qua trường phái" đi ngược chiều với điều đã biết. Liên kết này trông như được sinh ra từ **nhan đề cuốn sách** trong dòng Nguồn của Hillel (*From the Maccabees to the Mishnah*), mà một nhan đề bắc qua một giai đoạn không phải là lập luận về quan hệ kế thừa. Đây là lỗi mà lint **không bắt được** vì nó hợp lệ cả hai chiều về mặt cú pháp.
Đề xuất: bỏ cặp liên kết này ở cả hai mục; nếu muốn giữ mạch Judea thì nối Judah Maccabee với **nhà nước Hasmonean** (đã có dòng văn bản tự do) và nối Hillel với mạch Pharisee–Mishnah (ông đã có dòng đó). Hoặc nếu vẫn muốn giữ, đổi loại quan hệ thành `tương đồng độc lập` thì cũng không đúng — tốt nhất là bỏ.

**Thể thức (nhẹ) — hai "ứng viên" đều là người nhà cùng phe, không phải ứng viên cạnh tranh**
Trích: *"Ứng viên trong cùng gia tộc là Simon Thassi, người giành được độc lập trên thực tế và lập triều đại, và Mattathias, cha ông."*
Về **niên đại thì đạt**: Mattathias mất 166 TCN (chồng lấn 167–166 với khoảng hoạt động của Judah), Simon mất 135 TCN — cả hai **thật sự cùng thời** ✔. Nhưng cả hai là **cha và em ruột cùng chiến đấu trong cùng cuộc khởi nghĩa**, tức cộng sự chứ không phải ứng viên từ một hướng khác; mục tự gọi họ là "trong cùng gia tộc" nên cũng không giấu. §5 đòi "người **cùng lĩnh vực**, cùng thời" — đọc chặt thì họ hợp lệ (cùng lĩnh vực, cùng thời, và là lựa chọn thay thế thật cho chỗ này trong atlas), đọc theo tinh thần thì đoạn so sánh mất sức thuyết phục vì không có đối trọng nào ngoài gia đình.
Đề xuất: thêm một ứng viên ngoài gia tộc, cùng thời, cùng vùng: *"…và Antiochus IV Epiphanes (mất 164 TCN), người ra chính các sắc lệnh — đã được xét và loại ở Ghi chú biên tập."* (Antiochus IV **đã có** trong danh sách bị loại cuối file, nên nêu lại ở đây là nhất quán.)

**Nghi vấn (nhẹ) — hai mệnh đề căng với chính caveat Gruen mà mục tự nêu**
Trích: *"Điều đáng kể về mặt lịch sử là mục tiêu của cuộc chiến: không phải đất đai hay triều cống mà là quyền giữ một tập tục tôn giáo, điều hiếm thấy trong tư liệu Cận Đông cổ."*
Vấn đề: đây đúng là cách đọc mà **Gruen phản bác** — và mục **tự dẫn Gruen** ở đoạn dưới ("đây đồng thời là xung đột nội bộ giữa các nhóm Do Thái, không thuần tuý là kháng chiến chống ngoại bang"). Hai câu đặt cạnh nhau thì câu trên nói như một dữ kiện, câu dưới mới hạ giọng. Thêm nữa "điều hiếm thấy trong tư liệu Cận Đông cổ" là một khẳng định so sánh phạm vi rộng, không quy thuộc và **tôi không kiểm được** trong khuôn khổ lượt rà này.
Đề xuất: gộp caveat lên trên: *"Theo cách đọc truyền thống, điều đáng kể là mục tiêu của cuộc chiến: không phải đất đai hay triều cống mà là quyền giữ một tập tục tôn giáo. Gruen (1998) đọc khác: …"*

**Đã kiểm, KHÔNG có lỗi:**
- Q111559 = Judah Maccabee ✔ đúng người. P569 = −500 ở **độ chính xác thiên niên kỷ** (precision 6) — tức Wikidata không biết gì về năm sinh; Ghi chú biên tập dòng 823 mô tả chỗ này là "mức chính xác thế kỷ", **hơi sai một bậc** (thực tế còn thô hơn: thiên niên kỷ), nhưng kết luận "không dùng được" thì **đúng**, và cách xử lý — dùng `hoạt động k. 167–160 TCN` + `độ tin cậy: Thấp` — là **đúng quy ước** `CONTRIBUTING.md`. P570 = −160 khớp.
- Thanh tẩy Đền thờ **164 TCN** ✔; sắc lệnh cấm hành đạo của Antiochus IV ✔; nhà nước Hasmonean tồn tại tới can thiệp của Rome **63 TCN** ✔ (Pompey chiếm Jerusalem).
- *Sách Maccabee thứ nhất* ✔ có thật, mô tả đúng các chiến dịch và lễ cung hiến lại (1 Mcb 4); **không ghi số chương** nên không có rủi ro số bịa.
- Erich S. Gruen, *Heritage and Hellenism: The Reinvention of Jewish Tradition* (University of California Press, 1998) ✔ có thật, đúng năm, và **đúng là** công trình lập luận rằng xung đột mang tính nội bộ Do Thái — tức nguồn **có nói điều được dẫn**.
- `Kế thừa từ: Mattathias` ✔ đúng chiều, đúng niên đại.

---

## Độ phủ lĩnh vực và vùng của nhóm

**Lĩnh vực (10/16 lĩnh vực có mặt — vượt xa trần tối thiểu 4):** Triết học (-01, -10) · Chính trị/Nhà nước (-01, -02, -07, -09) · Khoa học tự nhiên (-03) · Toán học (-03, -08) · Sử học (-04) · Khám phá/Địa lý (-05) · Ngôn ngữ học (-06) · Tôn giáo/Tâm linh (-07, -11) · Luật (-09) · Quân sự (-11).
**Vắng mặt đáng chú ý:**
- **Kinh tế — không có ai**, dù chính mục `-02` lấy *"độc quyền muối và sắt năm 117 TCN cùng chế độ quân thâu bình chuẩn"* làm một trong hai lý do chọn Hán Vũ Đế. Nhóm coi chính sách kinh tế là thành tựu bản lề nhưng không có một mục nào mang lĩnh vực Kinh tế.
- **Văn học — không có ai**, dù TK 2 TCN có Terence, Ennius (mất 169 TCN), Ben Sira và cả nền phê bình văn bản Alexandria.
- Y học, Nghệ thuật/Kiến trúc, Kỹ thuật/Công nghệ, Giáo dục: cũng trống, nhưng đây là nhóm chỉ 11 người nên không phải lỗi.

**Vùng (4/9 — đạt trần tối thiểu 3):** Đông Á (-01, -02, -05) · Châu Âu (-03, -04, -09, -10) · Nam Á (-06, -07) · Trung Đông/Bắc Phi (-08, -11).
**Nhận xét:** **Trung Á trống**, dù Bối cảnh của nhóm viết "mở đường sang Trung Á" và nhóm có hẳn một mục Khám phá/Địa lý về Tây Vực. Thế giới Hy Lạp–Bactria (Eucratides I) là mục Trung Á tự nhiên nhất của TK 2 TCN và chưa từng được cân nhắc ở bất kỳ đâu trong file.
**Một điểm nhất quán cần ghi nhận:** quy ước vùng "theo nơi làm việc thực tế" mà chapter tự đặt (dòng 805) được áp dụng **đúng và nhất quán** trong nhóm này — Apollonius (Perga → Alexandria) ghi Trung Đông/Bắc Phi, Carneades (Cyrene → Athens) ghi Châu Âu, Hipparchus (Nicaea → Rhodes) ghi Châu Âu. Không tìm thấy lỗi quy ước vùng trong BCE02.

---

## Đánh giá lựa chọn nhân vật

Nhóm hiện có **11 người, trần là 12** — nên còn **một chỗ trống**, và kiến nghị bổ sung dưới đây **không cần loại ai**.

Tôi đã rà toàn bộ danh sách "Ứng viên mạnh đã bị loại" ở Ghi chú biên tập (Theophrastus, Chrysippus, Lưu Hâm, Ptolemaios II, Bindusara, Gaius Gracchus, Kātyāyana, Scipio Africanus, Aristarchus xứ Samos, Pyrrho, Arcesilaus, Herod Cả, Demosthenes, Isocrates, Lysippos, Apelles, Ctesibius, Seleucus I, Berossus, Manetho, Pytheas, Megasthenes, Mithridates I của Parthia, Antiochus IV, Cato Cả, Horace, Catullus, Sallust, Pompey, Sulla). **Bốn ứng viên dưới đây không có tên trong danh sách đó, cũng không xuất hiện trong bất kỳ mục "Vì sao chọn" nào của chapter — tức chưa từng được cân nhắc, kể cả để loại.**

**1. Tang Hoằng Dương / Sang Hongyang (桑弘羊, 152–80 TCN) — Đông Á, Kinh tế · Chính trị/Nhà nước. Kiến nghị mạnh nhất.**
Ông là người **thiết kế** chính các chính sách mà mục `-02` ghi công cho Hán Vũ Đế: độc quyền muối và sắt (quản qua khoảng năm mươi xưởng sắt của triều đình), **quân thâu** (均輸, độc quyền vận chuyển cống phẩm theo giá nhà nước) và **bình chuẩn** (平準, mua vào năm được mùa, bán ra năm mất mùa). Theo bốn tiêu chí: (a) phạm vi — mô hình nhà nước nắm độc quyền tài nguyên chiến lược được các triều đại Trung Hoa dùng lại suốt hai nghìn năm; (c) tính nguyên bản — ba cơ chế trên là thiết kế của ông, không phải kế thừa; (b) độ bền — cuộc tranh luận 81 TCN về chính sách của ông được chép thành **Diêm thiết luận** (鹽鐵論), **một trong những văn bản sớm nhất của nhân loại chuyên bàn chính sách kinh tế**, và vẫn là văn bản được dẫn trong tranh luận nhà nước–thị trường ở Trung Quốc tới nay. Việc nhóm nói về độc quyền muối sắt mà không có mục nào thuộc lĩnh vực **Kinh tế** là một lỗ hổng do chính ông để lại.
Lưu ý xếp nhóm: ông mất 80 TCN, nhưng giai đoạn ảnh hưởng chính (117–110 TCN) nằm hẳn ở BCE02 theo quy tắc 3 của prompt.
Nguồn kiểm: Wikipedia *Sang Hongyang*, *Discourses on Salt and Iron*; Columbia Asia for Educators, "A Record of the Debate on Salt and Iron".

**2. Aristarchus xứ Samothrace (k. 216–144 TCN) — Trung Đông/Bắc Phi (Alexandria), Văn học · Ngôn ngữ học.**
Quản thủ Thư viện Alexandria, người lập **bản hiệu đính phê phán** của Homer và hệ **ký hiệu phê bình văn bản** (obelos, asteriskos — nay vẫn gọi là *Aristarchian symbols*); chính ông chia Iliad và Odyssey thành **24 quyển mỗi bộ**, cách chia còn dùng đến hôm nay. Theo (c) và (b): ông là người biến việc đọc văn bản cổ thành một **kỷ luật có phương pháp** — tức tổ tiên của toàn bộ ngành phê bình văn bản phương Tây, bao gồm cả cách các văn bản Hy Lạp (và sau này Kinh Thánh) đến được với chúng ta. Nhóm BCE02 đã chọn **Patañjali** đúng vì vai trò song song ấy trong truyền thống Ấn Độ; không chọn người làm đúng việc đó ở Alexandria, cùng thế kỷ, là một bất đối xứng khó biện minh.
**Cảnh báo dễ nhầm:** danh sách bị loại có "Aristarchus xứ **Samos**" — nhà thiên văn nhật tâm, **một người hoàn toàn khác**, sống trước đó gần một thế kỷ. Việc tên gần giống có thể chính là lý do người thứ hai chưa bao giờ được xét.
Nguồn kiểm: Wikipedia *Aristarchus of Samothrace*, *Aristarchian symbols*; Oxford Classical Dictionary ("Aristarchus (2) of Samothrace, librarian of Alexandria, c. 216–144 BCE").

**3. Tư Mã Đàm (司馬談, mất 110 TCN) — Đông Á, Sử học · Triết học.**
Cha của Tư Mã Thiên, người **khởi thảo Sử ký** và là tác giả **"Luận lục gia yếu chỉ"** (論六家要指) — bản phân loại có hệ thống đầu tiên của tư tưởng Trung Hoa thành sáu nhà (Âm dương, Nho, Mặc, Danh, Pháp, Đạo đức). Theo (c) và (b): cái khung "bách gia" mà mọi sách sử tư tưởng Trung Hoa — kể cả Chapter 2 và Chapter 3 của chính atlas này — dùng để sắp xếp nhân vật **chính là khung của ông**. Atlas đã có Tư Mã Thiên ở `CH03-BCE01-06`; không nhắc người cha dù chỉ một dòng ở phần loại bỏ là một chỗ hở.
Phản biện công bằng: ông thua ở (d) vì con trai ông hoàn thành công trình, và prompt có quy tắc "người kế tục thua ở counterfactual" — nhưng ở đây **ngược lại**, ông là người đi trước. Ít nhất nên có tên trong danh sách bị loại kèm lý do.

**4. Ben Sira / Yeshua ben Sira (hoạt động k. 180 TCN) — Trung Đông/Bắc Phi, Tôn giáo/Tâm linh · Văn học.**
Tác giả **Sách Huấn ca (Sirach / Ecclesiasticus)**, văn bản khôn ngoan Do Thái đầu tiên có tên tác giả; lời tựa do cháu ông viết (k. 132 TCN) là **bằng chứng sớm nhất về cấu trúc ba phần của quy điển Hebrew** (Luật – Ngôn sứ – các sách khác). Ông nằm **ngay trước** cuộc khủng hoảng Maccabee mà mục `-11` mô tả, và cho thấy mặt kia của câu chuyện: Do Thái giáo Hellenistic trước khi nổ ra xung đột. Theo (b): sách này nằm trong quy điển Công giáo và Chính thống giáo tới nay. Đây là ứng viên yếu hơn ba người trên, nhưng vẫn mạnh hơn vài tên đã có trong danh sách loại (Berossus, Manetho).

**Hai tên khác đáng ít nhất một dòng trong danh sách loại, không phải để chọn:**
- **Eucratides I** (trị vì k. 170–145 TCN) — như đã nêu ở phát hiện `-07`, ông là đối thủ cùng thời thật của Menandros và là mục **Trung Á** tự nhiên nhất của nhóm. Nếu loại, hãy loại có lý do.
- **Terence** (k. 195/185–159 TCN) — sáu vở hài kịch của ông là nền văn phong Latin cổ điển và mạch hài kịch châu Âu qua Molière; nhóm không có mục Văn học nào.

**Về chiều ngược lại — có ai trong 11 người nên bị loại để nhường chỗ không?** Theo bốn tiêu chí thì **không**. Người yếu nhất về (a) phạm vi là `-11` Judah Maccabee (ảnh hưởng tập trung ở một cộng đồng), nhưng ông rất mạnh về (b) độ bền — một lễ hội còn được giữ liên tục 2.190 năm là bằng chứng độ bền hiếm có — nên lập luận giữ ông đứng được. Vì nhóm còn một chỗ trống, kiến nghị thực tế là **thêm Tang Hoằng Dương vào chỗ thứ 12**, và đưa Aristarchus xứ Samothrace, Tư Mã Đàm, Ben Sira, Eucratides I, Terence vào danh sách "ứng viên mạnh đã bị loại" kèm lý do.

---

## Tổng kết

| Loại | Số lượng | Ở các mục |
|---|---|---|
| **Sai** | 5 | `-01` (khoa cử thời Hán; Công Tôn Hoằng/136 TCN), `-06` (Bronkhorst không bàn nhà văn phạm), `-08` (Fried & Unguru không phải bản dịch), `-10` ("lời giải đầu tiên") |
| **Nghi vấn** | 12 | Bối cảnh (×2), `-01`, `-02` (×2), `-03` (×2), `-04` (×2), `-05` (×2), `-09`, `-10`, `-11` (×2) |
| **Thiếu** | 2 | `-06` (không ghi chú chỗ Wikidata gộp người trong thân mục), `-09` ("Kế thừa từ: Không xác định" trong khi nguồn đã dẫn có tên) |
| **Thể thức** | 8 | Bối cảnh (quá 60 chữ), `-01`, `-02`, `-03`, `-04`, `-05`, `-06`, `-07`, `-10`, `-11` — chủ yếu là **ứng viên không cùng thời** |

**Vấn đề hệ thống lớn nhất của nhóm: quy tắc "ứng viên cùng thời" của §5 bị vi phạm ở 8/11 mục.**
Chỉ **3 mục đạt**: `-01` (Công Tôn Hoằng, Lưu An), `-08` (Archimedes, Conon), `-09` (Gaius Gracchus, Scipio Aemilianus). Tám mục còn lại nêu người cách nhân vật từ **27 năm tới ba thế kỷ**. Khuôn mẫu lặp lại rất đều: mục nêu **một tiền bối** (người đặt nền) và **một hậu bối** (người hoàn thiện) rồi gọi cả hai là "ứng viên" — đúng cái mà `CONTRIBUTING.md` mục 5 đã cảnh báo sau khi bắt được 6 ca ở vòng trước. Đây không phải lỗi rải rác mà là **một thói quen viết**, nên nếu sửa thì nên sửa cả 8 mục cùng lúc theo một mẫu thống nhất.

**Điểm sáng cần giữ khi sửa:**
- **Không có Q-ID nào trỏ nhầm người** — cả 11 mục đều đúng.
- **Không có số quyển/chương nào bị bịa.** Tôi đã mở mục lục kiểm cả bốn chỗ có số: Sử ký **q. 123** (Đại Uyển liệt truyện) ✔, Polybius **q. VI** (anacyclosis, thể chế hỗn hợp) ✔, Almagest **q. III và VII** ✔, Heath **t. II** ✔, cộng SPQR **ch. 6** ✔. Khác hẳn kết quả kiểm toán phụ lục Keith Taylor (5/6 số chương sai, đều lệch +1).
- Cách xử lý niên đại không chắc ở `-08` và `-11` (hạ `độ tin cậy` xuống Thấp, dùng dạng "hoạt động k.", nói thẳng "niên đại chỉ suy từ các mốc gián tiếp") là **mẫu đúng** — `-05` nên được sửa theo chính mẫu này.
- Các caveat Loewe (`-01`) và Gruen (`-11`) là đúng việc phải làm; chỉ cần đặt chúng **trước** mệnh đề khẳng định thay vì sau.

**Ba chỗ nên sửa trước nếu phải chọn:**
1. `-06` — nguồn Bronkhorst không bàn tới điều được dẫn, và dòng 821 của Ghi chú biên tập gán cho ông một luận điểm ông không nêu. Đây là lỗi nặng nhất vì nó đúng loại lỗi mà `CONTRIBUTING.md` nói là "loại báo lỗi hữu ích nhất".
2. `-01` — "khoa cử thời Hán" là lỗi niên đại thể chế bảy thế kỷ, và nó nằm ở dòng liên kết nên sẽ hiển thị ra trang HTML.
3. Tám mục vi phạm "cùng thời" — sửa một lượt theo mẫu của `-08`.
