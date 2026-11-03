# Bình duyệt độc lập — Chapter 3, nhóm BCE03 (TK 3 TCN)

Phạm vi: `content/ch03.md`, dòng `**Bối cảnh**` của nhóm BCE03 và 12 mục `CH03-BCE03-01` … `CH03-BCE03-12`.
Người duyệt: agent bình duyệt độc lập (không viết chapter này).
Ngày: 2026-10-31.

Xếp loại: **Sai** (khẳng định sai sự thật) · **Nghi vấn** (chưa chứng minh được / nguồn không chống đỡ nổi) · **Thiếu** (thiếu thông tin bắt buộc) · **Thể thức** (vi phạm §5 của `prompts/atlas-prompt.md`).

Ghi chú về phương pháp: môi trường này **không gọi được `curl` ra ngoài** (connection timed out), nên các truy vấn Wikidata được thực hiện qua công cụ fetch web trên cùng endpoint `wbgetentities`. Những chỗ không mở được sẽ ghi rõ **"không kiểm được"**.

---

## 0. Đối chiếu Wikidata toàn nhóm (làm trước, để khỏi lặp)

Truy vấn qua SPARQL endpoint của Wikidata (`query.wikidata.org/sparql`, `wdt:P569`/`wdt:P570`). Lưu ý: SPARQL trả năm theo đánh số thiên văn, nên năm TCN = |giá trị| + 1 (đã đối chiếu chéo với `wbgetentities` cho Q8589: API trả `-0304`, SPARQL trả `-0303`).

| ID | Q-ID | Nhãn EN Wikidata | Khớp người? | P569/P570 (TCN) | Trường `năm:` | Kết luận |
|---|---|---|---|---|---|---|
| 01 | Q8589 | Ashoka | ✓ | 304 – 232 | k. 304–232 | khớp |
| 02 | Q7192 | Qin Shi Huang | ✓ | 259 – 210 | 259–210 (Cao) | khớp, trong ±5 |
| 03 | Q8747 | Euclid | ✓ | 334 – 285 | hoạt động k. 305–282 (Thấp) | độ tin cậy Thấp → bỏ đối chiếu |
| 04 | Q168261 | Ptolemy I Soter | ✓ | 366 – 286 | k. 367–282 | khớp, trong ±25 |
| 05 | Q8739 | Archimedes | ✓ | 287 – 212 | k. 287–212 | khớp |
| 06 | Q28959 | Han Fei | ✓ | 280 – 233 | k. 280–233 | khớp |
| 07 | Q171303 | Zeno of Citium | ✓ | 334 – 263 | k. 334–262 | khớp |
| 08 | Q43216 | Epicurus | ✓ | 342 – 270 | k. 341–270 | khớp |
| 09 | Q43182 | Eratosthenes | ✓ | 276 – 194 | k. 276–194 | khớp |
| 10 | Q152919 | Li Si | ✓ | 280 – 208 | k. 280–208 | khớp |
| 11 | Q216072 | Xunzi | ✓ | 313 – 231 | k. 313–230 | khớp |
| 12 | Q36456 | Hannibal | ✓ | 247 – 183 | k. 247–183 | khớp |

**Không có Q-ID nào trỏ nhầm người, và không có trường `năm:` nào lệch ngoài dung sai.** Theo cảnh báo ở `CONTRIBUTING.md` mục 4, điều này không chứng minh nội dung đúng — các phát hiện dưới đây đều là loại lint và Wikidata đều mù.

---

## 1. Dòng **Bối cảnh** của nhóm

**Nghi vấn — `## Nhóm BCE03`, dòng Bối cảnh.**
Nguyên văn: *"Tần diệt sáu nước, lập đế chế quan liêu đầu tiên của Đông Á."*
Vấn đề: mệnh đề tối cao ("đầu tiên") không quy thuộc. Nó đúng nếu hiểu "đế chế" là nhà nước quan liêu quy mô toàn Trung Hoa, nhưng chế độ quận–huyện do quan lại bổ nhiệm đã được chính nước Tần dùng từ cải cách Thương Ưởng (TK 4 TCN) và nước Sở, nước Tấn đã lập huyện từ TK 7–6 TCN — nên "lập ... đầu tiên" bỏ mất chuyện Tần phổ quát hoá một thiết chế đã có.
Đề xuất: *"Tần diệt sáu nước, lần đầu áp dụng chế độ quận–huyện trên toàn Trung Hoa."*
Nguồn: Mark Edward Lewis, *The Early Chinese Empires: Qin and Han* (2007) — chính nguồn đã được dẫn ở mục 02 và 10.

**Nghi vấn — dòng Bối cảnh.**
Nguyên văn: *"Rome thắng Carthage, bắt đầu kiểm soát Địa Trung Hải."*
Vấn đề: trong khung thời gian của nhóm (300–201 TCN), Rome thắng Carthage **hai lần** (241 và 201 TCN) nhưng Carthage chưa bị diệt (146 TCN, thuộc nhóm BCE02) và phía đông Địa Trung Hải còn thuộc Seleucid/Ptolemy suốt TK 3 TCN. "Kiểm soát Địa Trung Hải" là chuyện của TK 2 TCN.
Đề xuất: *"Rome thắng Carthage hai lần, giành quyền kiểm soát tây Địa Trung Hải."*

---

## 2. CH03-BCE03-01 · Ashoka

**Nghi vấn — Tư tưởng / đóng góp chính.**
Nguyên văn: *"là lần đầu một nhà nước công bố chính sách trực tiếp cho dân chúng bằng tiếng địa phương"*
Vấn đề: mệnh đề tối cao không quy thuộc, và có phản ví dụ sớm hơn gần ba thế kỷ. Bi ký Behistun của Darius I (k. 520 TCN) được khắc bằng ba thứ tiếng của đế chế và — theo bản sao giấy cói Aramaic tìm được ở Elephantine — được chép và phát tán ra các tỉnh bằng tiếng Aramaic hành chính. Trước nữa, bia luật Hammurabi (TK 18 TCN) cũng là văn bản nhà nước công bố cho dân bằng tiếng Akkad. Đáng chú ý: chính Darius I đã có mặt trong atlas ở `CH02-BCE05-10`.
Cái đúng: điều thật sự khác thường ở Ashoka là **quy mô phân tán** (chỉ dụ khắc ở hàng chục địa điểm trải khắp tiểu lục địa, mỗi nơi bằng phương ngữ địa phương) và **nội dung đạo đức chứ không phải pháp lệnh**, chứ không phải tính "lần đầu".
Đề xuất: *"...và là bộ chỉ dụ nhà nước được phân tán rộng nhất của thế giới cổ đại: khắc ở hàng chục địa điểm trải khắp tiểu lục địa, mỗi nơi theo phương ngữ địa phương, có bản song ngữ Hy Lạp và Aramaic ở Kandahar."*
Nguồn: Romila Thapar, *Aśoka and the Decline of the Mauryas* (1961/2012) — chính nguồn đã dẫn; về Behistun: bản Aramaic Elephantine (TAD C2.1).

**Thể thức — Vì sao chọn.**
Nguyên văn: *"Ứng viên cạnh tranh là Chandragupta Maurya, ông nội và người lập đế chế, và Bindusara."*
Vấn đề hai tầng:
(a) **Chandragupta Maurya không hề bị loại** — ông có mục riêng `CH03-BCE04-08` trong cùng chapter này. Nêu một người đã được chọn làm "ứng viên cạnh tranh" bị loại là sai thể thức §5 và làm hỏng công dụng của mục (người đọc tưởng ông bị loại).
(b) **Không ai trong hai người là "cùng thời" theo nghĩa cạnh tranh.** Chandragupta mất k. 297 TCN, khi Ashoka (sinh k. 304) còn là trẻ nhỏ; cả hai là tiền bối trực hệ chứ không phải ứng viên song song.
Đề xuất: *"Ứng viên cùng thời đã cân nhắc là Antiochus I Soter của Seleucid và Ptolemaios II của Ai Cập — hai quân chủ Hy Lạp hoá mà chính chỉ dụ số 13 của Ashoka nêu đích danh. Ashoka vượt theo độ bền (b) và tính nguyên bản (c): ..."* (giữ nguyên phần lập luận sau).
Ghi chú: nếu muốn giữ Chandragupta, phải viết rõ ông **đã được chọn ở `CH03-BCE04-08`**, giống cách mục 05 và 11 đã làm với Apollonius và Mạnh Tử.

**Kiểm nguồn — đạt.**
- Romila Thapar, *Aśoka and the Decline of the Mauryas*, Oxford UP 1961, bản in lại có lời bạt 2012 — **tồn tại, năm đúng**.
- Ulrich Schneider, *Die großen Felsen-Edikte Aśokas: kritische Ausgabe, Übersetzung und Analyse der Texte*, Freiburger Beiträge zur Indologie Bd. 11, Wiesbaden: Otto Harrassowitz, **1978** — **tồn tại, năm đúng, đúng nội dung** (bản phê bình + dịch các đại thạch chỉ dụ). Xác minh qua mục lục Penn State Libraries và bài điểm sách trên *BSOAS*.

**Kiểm liên kết — đạt, trừ một lưu ý.**
- `Kế thừa từ CH03-BCE04-08` → Chandragupta Maurya ✓ đúng người, đúng chiều (ông nội).
- `Kế thừa từ CH02-BCE06-03` → Đức Phật ✓ đúng người.
- `Ảnh hưởng tới CH03-BCE02-07` → Menandros I ✓ đúng người, đúng chiều (Menandros TK 2 TCN, sau Ashoka).
- Chỉ dụ Kalinga k. 261 TCN ✓; bi ký song ngữ Hy Lạp–Aramaic ở Kandahar ✓; phái đoàn tới Sri Lanka ✓.

---

## 3. CH03-BCE03-02 · Tần Thủy Hoàng

**Thể thức — Vì sao chọn.**
Nguyên văn: *"Ứng viên cùng chức năng là Lý Tư, thừa tướng thiết kế phần lớn chính sách, và Hán Cao Tổ, người lập triều đại giữ được lâu dài."*
Vấn đề: **Lý Tư không bị loại** — ông là mục `CH03-BCE03-10` ngay trong chính nhóm này, cách đó bốn mục. Và theo tiêu chí của đề bài, Lý Tư là **cộng sự** (thừa tướng của chính ông), không phải ứng viên cạnh tranh. Hai mục còn chéo nhau: mục 10 lại nêu "chính Tần Thuỷ Hoàng" làm ứng viên bị loại của Lý Tư. Hai người cùng được chọn mà mỗi mục lại kể người kia là ứng viên bị loại — đọc liền nhau thì mâu thuẫn.
Hán Cao Tổ (Lưu Bang, 256–195 TCN) **đúng là cùng thời** ✓ và là ứng viên hợp lệ.
Đề xuất: *"Ứng viên cùng thời đã cân nhắc là Hán Cao Tổ (Lưu Bang), người lập triều đại giữ được lâu dài, và Lã Bất Vi, tướng quốc đã dựng bộ máy nước Tần trước khi ông thân chính. (Lý Tư, thừa tướng thiết kế phần lớn chính sách, được chọn riêng ở `CH03-BCE03-10`.)"*

**Kiểm nội dung — đạt.**
- Diệt sáu nước và bãi phong kiến lập quận–huyện năm 221 TCN ✓.
- Thống nhất văn tự (tiểu triện), đo lường, tiền tệ, khoảng cách trục bánh xe (車同軌) ✓.
- Đốt sách **213 TCN** ✓ — đúng, theo *Sử ký* q. 6 (năm thứ 34 đời Thuỷ Hoàng).
- "Nhà Tần sụp sau mười lăm năm" ✓ — 221 → 206 TCN.
- "quyết định bãi bỏ phong kiến năm 221 TCN được Sử ký chép là do ông chọn giữa hai phương án trái ngược của triều đình" ✓ — *Sử ký*, Tần Thuỷ Hoàng bản kỷ chép thừa tướng Vương Oản đề nghị phong các hoàng tử ra Yên–Tề–Sở, Lý Tư phản đối, hoàng đế theo Lý Tư.

**Kiểm nguồn — đạt.** Tư Mã Thiên, *Sử ký*, Tần Thuỷ Hoàng bản kỷ (q. 6) ✓ — số quyển không ghi trong văn bản nên không có rủi ro bịa số. Mark Edward Lewis, *The Early Chinese Empires: Qin and Han*, Harvard UP (Belknap), **2007** ✓ tồn tại, năm đúng, đúng chủ đề.

**Kiểm liên kết — đạt.** `CH03-BCE04-06` → Thương Ưởng ✓ · `CH03-BCE03-10` → Lý Tư ✓ · `CH03-BCE03-06` → Hàn Phi ✓ · `CH03-BCE02-02` → Hán Vũ Đế ✓ (đúng chiều, sau 210 TCN).

---

## 4. CH03-BCE03-03 · Euclid

**Sai — dòng Nguồn. Đây là lỗi nghiêm trọng nhất của mục.**
Nguyên văn: *"Stanford Encyclopedia of Philosophy, \"Euclid\" (https://plato.stanford.edu/entries/euclid/)."*
Thực tế: URL này trả **HTTP 404**. SEP **không có** mục từ nào về Euclid. Đây đúng loại lỗi mà `CONTRIBUTING.md` mục 2 đã cảnh báo (slug SEP bịa).
Cái đúng: các mục SEP có bàn tới *Cơ sở* nhưng không phải tiểu sử Euclid là `epistemology-geometry` và `geometry-19th`; không mục nào đứng tên "Euclid".
Đề xuất thay bằng: *"Euclid, Cơ sở, bản dịch và chú giải Thomas Heath (1908); Benno Artmann, Euclid: The Creation of Mathematics (Springer, 1999)."* — hoặc nếu muốn giữ một mục SEP thì phải đổi cả tên lẫn phạm vi dẫn: *"Stanford Encyclopedia of Philosophy, \"Epistemology of Geometry\" (https://plato.stanford.edu/entries/epistemology-geometry/)"*, và chỉ dùng nó để chống đỡ câu về định đề song song, không dùng cho tiểu sử.

**Thể thức — Vì sao chọn. Vi phạm rõ rệt điều kiện "cùng thời".**
Nguyên văn: *"Ứng viên là chính các tác giả mà ông tổng hợp: Eudoxus cho Quyển V và Theaetetus cho Quyển X."*
Vấn đề:
(a) **Theaetetus (k. 417–369 TCN) mất khoảng 65 năm trước floruit của Euclid (k. 300 TCN)** — hoàn toàn không cùng thời. Đây đúng dạng lỗi mà `CONTRIBUTING.md` mục 5 liệt kê.
(b) **Eudoxus (k. 390–337 TCN) cũng không cùng thời**, và hơn nữa **không bị loại**: ông là mục `CH03-BCE04-09` ngay chapter này.
(c) Cả hai là **tiền bối được tổng hợp**, không phải ứng viên cạnh tranh — đúng loại lỗi "cộng sự / tiền bối chứ không phải ứng viên".
Cái đúng: ứng viên toán học **thật sự cùng thời** với Euclid gồm Autolycus xứ Pitane (k. 360–290 TCN, tác giả hai chuyên luận hình cầu còn nguyên vẹn, sớm hơn *Cơ sở*) và Aristaeus Trưởng lão (k. 370–300 TCN, tác giả *Conics* đã mất).
Đề xuất: *"Ứng viên cùng thời là Autolycus xứ Pitane, người để lại hai chuyên luận hình học cầu còn nguyên vẹn sớm hơn Cơ sở, và Aristaeus Trưởng lão, tác giả bộ Conics nay đã mất. Euclid được chọn theo độ bền (b): ..."* (giữ phần sau). Riêng Eudoxus và Theaetetus nên chuyển xuống thành câu về nguồn tổng hợp, không gọi là "ứng viên".

**Nghi vấn — Vì sao chọn, mệnh đề tối cao không quy thuộc.**
Nguyên văn: *"là một trong những văn bản được in nhiều nhất sau Kinh Thánh"*
Vấn đề: đây là một mệnh đề lưu truyền rộng nhưng không ai kiểm đếm được, và văn bản không nói là theo ai.
Đề xuất: *"theo Thomas Heath, Cơ sở là một trong những sách được in lại nhiều nhất của văn minh phương Tây"* — hoặc bỏ hẳn, vì câu "được dùng làm sách giáo khoa liên tục hơn hai mươi thế kỷ" đã đủ.

**Nghi vấn — Vì sao chọn, câu về Proclus.**
Nguyên văn: *"tiểu sử chỉ dựa vào Proclus viết sau tám thế kỷ"*
Vấn đề hai điểm nhỏ: (a) Proclus viết *Chú giải Quyển I Cơ sở* khoảng 450 CN, cách floruit Euclid (k. 300 TCN) khoảng **bảy thế kỷ rưỡi**, "tám thế kỷ" là làm tròn lên; (b) **không phải "chỉ"** — Pappus xứ Alexandria (k. 320 CN) cũng để lại một mẩu tiểu sử về Euclid và các học trò của ông ở Alexandria, sớm hơn Proclus hơn một thế kỷ.
Đề xuất: *"...vì tiểu sử chỉ còn qua Pappus (k. 320 CN) và Proclus (k. 450 CN), tức bảy thế kỷ sau, và có giả thuyết đây là tên một nhóm tác giả."*

**Kiểm nội dung — đạt.** 13 quyển ✓ · Quyển V (tỉ lệ) quy cho Eudoxus và Quyển X (vô ước) quy cho Theaetetus ✓ đúng quy thuộc chuẩn · định đề song song là xuất phát điểm hình học phi Euclid TK 19 ✓.

**Kiểm nguồn — đạt (phần còn lại).** Thomas L. Heath, *The Thirteen Books of Euclid's Elements*, Cambridge UP, **1908** (3 tập; tái bản có sửa 1926) ✓ tồn tại, năm đúng.

**Kiểm liên kết — đạt.** `CH03-BCE04-09` → Eudoxus ✓ · `CH03-BCE04-02` → Aristotle ✓ · `Ảnh hưởng tới CH03-BCE03-05` → Archimedes ✓ đúng người, đúng chiều (Archimedes dẫn *Cơ sở* trong *Về hình cầu và hình trụ*).

---

## 5. CH03-BCE03-04 · Ptolemaios I Soter

**Sai — Tư tưởng / đóng góp chính. Mệnh đề tối cao có phản ví dụ nằm ngay trong cùng nhóm.**
Nguyên văn: *"Đó là mô hình tài trợ nghiên cứu công sớm nhất được ghi chép."*
Thực tế: **Học cung Tắc Hạ (稷下學宮) của nước Tề ở Lâm Tri** đi trước. Nó được lập khoảng 374 TCN (có nguồn ghi k. 318 TCN), tức sớm hơn Mouseion (k. 295 TCN) từ hai tới tám thập kỷ, và mô tả cổ của nó trùng khít từng chi tiết với đoạn văn ở trên: học giả được cấp **nhà ở và bổng lộc ngang hàng thượng đại phu**, **không phải nhận học trò trả tiền**, và được nuôi để bàn luận chứ không để làm quan. Điều làm lỗi này nặng hơn: **Tuân Tử, mục `CH03-BCE03-11` cách đó bảy mục, ba lần làm tế tửu của chính Học cung Tắc Hạ** — chapter tự mâu thuẫn với chính nó.
Đề xuất: *"Đó là mô hình tài trợ nghiên cứu công được ghi chép đầy đủ nhất của thế giới Địa Trung Hải; Học cung Tắc Hạ của nước Tề đã làm điều tương tự sớm hơn ở Đông Á."*
Nguồn: Nathan Sivin / John Knoblock về Tắc Hạ; Knoblock, *Xunzi: A Translation and Study of the Complete Works*, q. I (1988) về ba nhiệm kỳ tế tửu của Tuân Tử.

**Sai — Vì sao chọn. Ba người được nêu không hề cùng làm việc với nhau.**
Nguyên văn: *"việc Euclid, Eratosthenes và Herophilos cùng làm việc ở một thành phố là hệ quả trực tiếp của thiết chế ông dựng"*
Thực tế: ba người này **cách nhau nhiều thế hệ, không ai từng trùng thời với cả hai người kia**. Euclid hoạt động k. 300 TCN; Herophilos hoạt động k. 290–260 TCN; **Eratosthenes mới sinh năm 276 TCN và chỉ tới Alexandria khoảng 245 TCN, do Ptolemaios III triệu** — tức khoảng **37 năm sau khi Ptolemaios I mất (282 TCN)**. Gọi đó là "hệ quả trực tiếp" của thiết chế ông dựng là gán công quá xa; chính văn bản ở mục `CH03-BCE03-09` cũng ghi Eratosthenes 276–194 TCN, nên hai mục đọc liền nhau sẽ lộ mâu thuẫn.
Đề xuất: *"...việc Alexandria nuôi được Euclid ở thế hệ đầu rồi Herophilos, Eratosthenes và Apollonius ở các thế hệ sau là hệ quả của thiết chế ông dựng, còn vương quốc Seleucid không để lại một cơ sở nghiên cứu tương đương dù giàu hơn."*

**Nghi vấn — Tư tưởng / đóng góp chính, quy công lập Thư viện.**
Nguyên văn: *"Đóng góp có hệ quả xa nhất là việc lập Mouseion và Thư viện Alexandria"*
Vấn đề: viết như một sự kiện đã định, trong khi đây là điểm tranh luận của giới nghiên cứu. Quan điểm phổ biến hiện nay: Demetrius xứ Phalerum đề xuất với Ptolemaios I, Ptolemaios I đặt nền, nhưng **Thư viện nhiều khả năng chỉ thành hình dưới Ptolemaios II**. Chính mục này sau đó gọi Ptolemaios II là "người hoàn thiện Thư viện", nghĩa là tác giả đã biết có vấn đề nhưng câu chính vẫn viết dứt khoát.
Đề xuất: *"Đóng góp có hệ quả xa nhất là việc đặt nền cho Mouseion và Thư viện Alexandria — theo truyền thống là do Demetrius xứ Phalerum hiến kế, và phần lớn giới nghiên cứu cho rằng Thư viện chỉ thành hình dưới đời con ông."*
Nguồn: Roy MacLeod (chủ biên), *The Library of Alexandria* (2000) — chính nguồn đã được dẫn trong mục.

**Thể thức — Vì sao chọn, một trong hai "ứng viên" là người kế vị.**
Nguyên văn: *"Ptolemaios II, người hoàn thiện Thư viện"*
Vấn đề: Ptolemaios II là **con và từng đồng trị vì với ông (285–283 TCN)** — cộng sự/người kế thừa, không phải ứng viên cạnh tranh. Seleucus I Nicator (k. 358–281 TCN) thì **đúng là cùng thời và đúng là đối thủ** ✓.
Đề xuất: thay Ptolemaios II bằng một Diadochi khác thật sự cạnh tranh, ví dụ *"Antigonus I Monophthalmus, người suýt gom lại được toàn bộ đế chế"* hoặc *"Lysimachus"*.

**Kiểm nội dung — đạt.** Chiếm Ai Cập (làm thái thú) 323 TCN ✓ · xưng vương 305 TCN ✓ · triều đại tới 30 TCN ✓ · Arrian trong lời tựa *Anabasis* nêu Ptolemaios và Aristobulus là hai nguồn ông tin cậy nhất ✓.

**Kiểm nguồn — đạt.** Günther Hölbl, *A History of the Ptolemaic Empire*, Routledge, **2001** (bản dịch Tina Saavedra của *Geschichte des Ptolemäerreiches*) ✓ tồn tại, năm đúng, đúng phạm vi (323–30 TCN). Roy MacLeod (chủ biên), *The Library of Alexandria*, I.B. Tauris, **2000** ✓ tồn tại, năm đúng — lưu ý sách có hai phụ đề tuỳ lần in (*Centre of Learning in the Ancient World* / *Rediscovering the Cradle of Western Culture*), nên ghi kèm phụ đề sẽ an toàn hơn.

**Kiểm liên kết — đạt.** `CH03-BCE04-03` → Alexander Đại đế ✓ · `Ảnh hưởng tới CH03-BCE03-03` → Euclid ✓ · `Ảnh hưởng tới CH03-BCE03-09` → Eratosthenes ✓ đúng người; nhãn "qua trường phái" là đúng mức bằng chứng vì quan hệ chỉ là thiết chế, không phải cá nhân.

---

## 6. CH03-BCE03-05 · Archimedes

**Kiểm con số — ĐẠT, không có lỗi.**
Nguyên văn: *"Bằng đa giác chín mươi sáu cạnh ông chặn số pi giữa ba phẩy một bốn không tám và ba phẩy một bốn hai chín."*
Đối chiếu: *Đo đường tròn*, mệnh đề 3 cho chặn 3 10/71 < π < 3 1/7, tức **3,14084… < π < 3,14285…** → làm tròn 3,1408 và 3,1429. **Khớp chính xác.** Đa giác 96 cạnh ✓. Tỉ số 2/3 giữa hình cầu và hình trụ ngoại tiếp, khắc trên mộ ✓.

**Nghi vấn — Tư tưởng / đóng góp chính, về niên đại đọc được *Phương pháp*.**
Nguyên văn: *"Văn bản Phương pháp, tìm lại trên một palimpsest năm 1906 và đọc được đầy đủ sau năm 1998"*
Vấn đề: câu này dễ bị đọc thành "từ 1906 tới 1998 không ai đọc được". Thực tế **Heiberg đã đọc và công bố *Phương pháp* ngay từ 1907**, và bản dịch Anh ngữ của Heath ra trong tập bổ sung 1912. Năm 1998 là năm palimpsest **được bán đấu giá** ở Christie's; đợt chụp ảnh đa phổ và huỳnh quang tia X tại Walters Art Museum (1999–2008) mới bổ sung những đoạn Heiberg không đọc nổi.
Đề xuất: *"Văn bản Phương pháp, Heiberg tìm lại và công bố từ một palimpsest năm 1906–1907, rồi được chụp lại bằng ảnh đa phổ sau khi bản thảo đổi chủ năm 1998, bổ sung những đoạn trước đó không đọc được."*

**Nghi vấn — trung lập, mệnh đề tối cao không quy thuộc.**
Nguyên văn: *"Phương pháp cho thấy một lối làm việc hai tầng chưa thấy ở đâu khác trong toán học cổ"*
Vấn đề: đây là luận điểm của Reviel Netz, không phải sự kiện; văn bản không nói là theo ai. Prompt dự án cấm "tô vẽ" và mục Trung lập yêu cầu quy thuộc.
Đề xuất: *"...và theo Reviel Netz, Phương pháp cho thấy một lối làm việc hai tầng không có song song nào còn lại trong toán học Hy Lạp."*

**Nghi vấn — `Ảnh hưởng tới`, quan hệ không chống đỡ được. (Lint không quét chiều này.)**
Nguyên văn: *"- CH03-BCE02-03 · kế thừa · qua trường phái"* → đích là **Hipparchus xứ Nicaea** ✓ đúng người, đúng chiều niên đại (Archimedes mất 212 TCN, Hipparchus hoạt động k. 150–120 TCN).
Vấn đề: **tôi không tìm được bằng chứng nào cho một quan hệ kế thừa Archimedes → Hipparchus.** Hipparchus là nhà thiên văn cầu và lượng giác; các mạch truyền thừa của Archimedes được ghi chép là qua Hero xứ Alexandria, Pappus và Eutocius. Ghi thẳng: **không kiểm được** rằng Hipparchus kế thừa Archimedes.
Đề xuất: thay bằng *"- Hero xứ Alexandria và Pappus · kế thừa · qua trường phái"*, hoặc giữ Hipparchus nhưng hạ xuống `tương đồng độc lập` theo đúng khuyến nghị ở mục Kiểm soát chất lượng của prompt ("không suy diễn quan hệ kế thừa khi thiếu bằng chứng").

**Thể thức — Vì sao chọn: ĐẠT, và là mục làm đúng nhất nhóm.**
Ctesibius (hoạt động k. 285–222 TCN) **thật sự cùng thời** ✓ và cùng lĩnh vực kỹ thuật ✓. Apollonius xứ Perga (k. 262–190 TCN) cùng thời ✓, và mục **ghi rõ ông "được chọn riêng ở nhóm sau"** — đây chính là cách xử lý đúng mà các mục 01, 02, 03 và 10 đã bỏ sót.

**Kiểm nguồn — đạt.** Reviel Netz & William Noel, *The Archimedes Codex*, **2007** ✓ tồn tại, năm đúng, đúng nội dung (palimpsest + *Phương pháp*). Thomas L. Heath, *The Works of Archimedes*, Cambridge UP, **1897** ✓ tồn tại, năm đúng (tập bổ sung chứa *Phương pháp* ra 1912 — nếu dòng Nguồn định chống đỡ câu về *Phương pháp* thì nên ghi "1897, kèm tập bổ sung 1912").

**Kiểm liên kết — đạt.** `CH03-BCE04-09` → Eudoxus ✓ (Archimedes tự dẫn Eudoxus trong lời tựa *Về hình cầu và hình trụ*) · `CH03-BCE03-03` → Euclid ✓.

---

## 7. CH03-BCE03-06 · Hàn Phi

**Sai — dòng Nguồn. URL SEP không tồn tại.**
Nguyên văn: *"Stanford Encyclopedia of Philosophy, \"Han Fei\" (https://plato.stanford.edu/entries/han-fei/)"*
Thực tế: URL trả **HTTP 404**. SEP **không có** mục từ "Han Fei". Mục từ đúng là **"Legalism in Chinese Philosophy"** của Yuri Pines, tại `https://plato.stanford.edu/entries/chinese-legalism/` — và mục từ đó chống đỡ được gần như toàn bộ đoạn văn xuôi.
Đề xuất: *"Stanford Encyclopedia of Philosophy, Yuri Pines, \"Legalism in Chinese Philosophy\" (https://plato.stanford.edu/entries/chinese-legalism/); Hàn Phi Tử."*
Ghi chú: đây là lỗi SEP thứ hai trong cùng một nhóm (xem mục 4, Euclid). Hai lỗi cùng dạng trong 12 mục gợi ý rằng các URL SEP trong nhóm này được sinh theo khuôn `tên-người` chứ không tra — nên kiểm lại cả các nhóm khác của `ch03.md`.

**Sai — `Ảnh hưởng tới`. Quan hệ bị đảo và bị chính nguồn của mục phủ nhận. (Lint chỉ quét chiều `Kế thừa từ` nên lỗi này lọt.)**
Nguyên văn: *"- CH03-BCE03-10 · kế thừa · trực tiếp"* → đích là **Lý Tư** ✓ đúng người, nhưng **quan hệ sai**.
Thực tế:
(a) SEP "Legalism in Chinese Philosophy" gọi Lý Tư là **"bạn đồng môn và kẻ thù" (fellow student and nemesis)** của Hàn Phi, không phải người kế thừa. Chính Lý Tư là người dàn xếp để Hàn Phi chết trong ngục năm 233 TCN — sự việc mà mục này tự ghi ở câu cuối "Vì sao chọn".
(b) **Niên đại không cho phép.** Lý Tư vào Tần và lên guồng từ khoảng 247 TCN; Hàn Phi chỉ tới Tần năm 233 TCN và chết gần như ngay. Phần lớn chính sách của Lý Tư có trước khi hai người gặp nhau.
(c) Lỗi này **lặp ở chiều ngược lại**: mục `CH03-BCE03-10` ghi `Kế thừa từ: CH03-BCE03-06 · kế thừa · trực tiếp`. Phải sửa **cả hai chỗ**.
Cái đúng: cả hai là đồng môn của Tuân Tử — đúng loại quan hệ là `tương đồng độc lập`, hoặc bỏ hẳn.
Đề xuất: ở mục 06 đổi thành *"- CH03-BCE03-10 · tương đồng độc lập · qua trường phái"* (cùng thầy Tuân Tử), và ở mục 10 bỏ dòng `CH03-BCE03-06 · kế thừa · trực tiếp` hoặc đổi tương ứng. Riêng `Ảnh hưởng tới CH03-BCE03-02` (Tần Thuỷ Hoàng) thì **giữ nguyên** — *Sử ký* chép hoàng đế đọc *Cô phẫn* và *Ngũ đố* rồi muốn gặp tác giả, đây là liên kết có bằng chứng văn bản.

**Kiểm nội dung — đạt.** Ba mạch pháp (法) / thuật (術) / thế (勢) ✓ · **Thận Đáo ↔ thế** và **Thân Bất Hại ↔ thuật** ✓ đúng quy thuộc chuẩn, xác nhận bằng SEP "Legalism in Chinese Philosophy" · Thương Ưởng ↔ pháp ✓ · Hàn Phi là người tổng hợp ✓ (SEP dẫn thiên 43 *Định pháp* và thiên 40 *Nạn thế*) · ngụ ngôn 守株待兔 "ôm gốc cây đợi thỏ" trong thiên *Ngũ đố* ✓ · chết trong ngục nước Tần **233 TCN** ✓ (SEP "Xunzi" cũng ghi d. 233 BCE).

**Kiểm liên kết — còn lại đạt.** `CH03-BCE04-06` → Thương Ưởng ✓ · `CH03-BCE03-11` → Tuân Tử ✓ (thầy, có chép trong *Sử ký*) · dòng tự do "Thận Đáo và Thân Bất Hại" ✓.

---

## 8. CH03-BCE03-07 · Zeno xứ Citium

**Thể thức — Vì sao chọn. Ứng viên duy nhất được nêu là người kế vị, không phải đối thủ cùng thời.**
Nguyên văn: *"Ứng viên trong chính trường phái là Chrysippus, người hệ thống hoá và viết phần lớn giáo lý Khắc kỷ"*
Vấn đề: Chrysippus (k. 279–206 TCN) **chỉ khoảng 17 tuổi khi Zeno mất (262 TCN)** và vào phái dưới thời Cleanthes, tức là **người kế vị đời thứ ba**, không phải ứng viên song song. Mục chỉ nêu một tên duy nhất, nên sau khi loại Chrysippus thì không còn ứng viên cùng thời nào — không đạt yêu cầu "1–2 người cùng lĩnh vực, cùng thời" của §5.
Cái đúng: đối thủ **thật sự cùng thời và cùng lĩnh vực** của Zeno ở Athens là **Arcesilaus xứ Pitane (k. 316–241 TCN)**, người đưa Viện Hàn lâm sang hướng hoài nghi và tranh luận trực tiếp với phái Khắc kỷ về tiêu chuẩn chân lý; và **Cleanthes (k. 330–230 TCN)**, học trò rồi người kế vị ngay sau Zeno.
Đề xuất: *"Ứng viên cùng thời là Arcesilaus xứ Pitane, người cùng thời ở Athens đã kéo Viện Hàn lâm sang hoài nghi và công kích thẳng tiêu chuẩn chân lý của Khắc kỷ. Trong chính trường phái, Chrysippus (k. 279–206 TCN, thế hệ sau) hệ thống hoá và viết phần lớn giáo lý, tới mức có câu nói không có ông thì không có Stoa; Zeno vẫn được chọn theo tính nguyên bản (c): ..."* (giữ phần sau).

**Nghi vấn — `Ảnh hưởng tới`, quan hệ với Cicero. (Chiều lint không quét.)**
Nguyên văn: *"- CH03-BCE01-03 · kế thừa · qua trường phái"* → đích là **Cicero** ✓ đúng người, đúng chiều niên đại.
Vấn đề: Cicero tự nhận thuộc **Viện Hàn lâm hoài nghi** và bác bỏ tri thức luận Khắc kỷ (rõ nhất trong *Academica* và *De Natura Deorum*); ông truyền lại **đạo đức học** Khắc kỷ (*De Officiis*, theo Panaetius) nhưng đồng thời phê phán nó. Gọi gọn là `kế thừa` làm mất nửa quan hệ.
Đề xuất: *"- CH03-BCE01-03 · tổng hợp · qua trường phái"*, hoặc giữ `kế thừa` nhưng đổi đích sang *"Panaetius và Khắc kỷ Trung kỳ"*.

**Kiểm nội dung — đạt.** Stoa Poikile ✓ · chia triết học thành luận lý / vật lý / đạo đức "từ Zeno trở đi" ✓ (SEP "Stoicism", §1.2 nói đúng điều này) · học thuyết *adiaphora* về sức khoẻ, danh vọng, sinh mạng ✓ (SEP §4.3) · "không có ông thì không có Stoa" ✓ — Diogenes Laërtius VII.183 · trước tác mất hết, chỉ còn qua trích dẫn ✓.

**Kiểm nguồn — đạt.** SEP **"Stoicism"** tại `https://plato.stanford.edu/entries/stoicism/` ✓ **tồn tại** (first published 20/01/2023) và **thật sự bàn đúng hai điểm được dẫn**. Diogenes Laërtius, *Cuộc đời các triết gia danh tiếng*, **q. VII** ✓ — đúng, Quyển VII là quyển về Zeno và phái Khắc kỷ. Số quyển này đã được kiểm, không phải đoán.

**Lưu ý nhỏ (không xếp loại).** `vùng: Châu Âu` cho một người sinh ở Citium trên đảo Síp, gốc Phoenicia. Chọn Châu Âu vì ông dạy ở Athens là bảo vệ được, nhưng nếu nhóm đang thiếu vùng thì đây là chỗ đáng cân nhắc lại.

---

## 9. CH03-BCE03-08 · Epicurus

**Thiếu — dòng Nguồn không chống đỡ một khẳng định có sức nặng.**
Nguyên văn: *"Trường của ông, gọi là Khu vườn, nhận cả phụ nữ và nô lệ làm học trò — điều hiếm trong các trường triết Athens đương thời."*
Tình trạng: tôi đã mở mục SEP "Epicurus" (David Konstan) và **mục này không nói gì về việc Khu vườn nhận phụ nữ và nô lệ** — nó chỉ chép việc Epicurus mua mảnh đất gọi là Khu vườn. Khẳng định này đứng được trên **Diogenes Laërtius q. X** (Leontion và các nữ môn sinh; di chúc của Epicurus giải phóng nô lệ Mys), tức nguồn thứ hai của mục, nên không phải lỗi sự thật — nhưng dòng Nguồn hiện tại để người đọc tưởng SEP là chỗ kiểm.
Đề xuất: ghi rõ chỗ dựa — *"Diogenes Laërtius, Cuộc đời các triết gia danh tiếng, q. X (danh sách môn sinh và di chúc)"*.

**Kiểm nội dung — đạt.** Nhận nguyên tử luận từ Democritus ✓ (SEP: "Epicurus inherited this scheme from the earlier atomists, above all Democritus") · *ataraxia* ✓ (SEP bàn kỹ) · linh hồn tan khi chết, thần không can thiệp ✓ · sinh ở Samos, lập trường ở Athens ✓ (Khu vườn, k. 306 TCN) · *De rerum natura* được Poggio Bracciolini tìm lại **năm 1417** ✓ đúng năm.

**Kiểm nguồn — đạt.** SEP **"Epicurus"**, David Konstan, `https://plato.stanford.edu/entries/epicurus/` ✓ **tồn tại**, đúng nhân vật. Diogenes Laërtius **q. X** ✓ — đúng, Quyển X là quyển về Epicurus và chứa ba bức thư cùng *Chủ đạo nghĩa*. Đã kiểm, không phải đoán.

**Kiểm thể thức — đạt.** Pyrrho (k. 360–270 TCN) **thật sự cùng thời** với Epicurus (k. 341–270) ✓, cùng lĩnh vực ✓, và mục ghi rõ Democritus "đã được chọn ở chapter trước" ✓ — xử lý đúng. §5 cho phép 1–2 ứng viên nên một tên hợp lệ là đủ.

**Kiểm liên kết — đạt.** `CH02-BCE05-05` → Democritus ✓ · `Ảnh hưởng tới CH03-BCE01-04` → Lucretius ✓ đúng người, đúng chiều · "Gassendi và nguyên tử luận cận đại" ✓.

---

## 10. CH03-BCE03-09 · Eratosthenes

**Số quyển/chương Cleomedes — ĐÃ KIỂM, ĐÚNG.** (Đây là điểm được yêu cầu kiểm riêng.)
Nguyên văn: *"Cleomedes, Caelestia, q. I, 7 (ghi lại phép đo)"*
Xác minh: *Caelestia* (còn gọi *Meteora*, *The Heavens*) có **hai quyển**; Quyển I có **tám chương**, và **chương 7 chính là chương về kích thước Trái Đất**, trình bày cả phép của Posidonius lẫn phép của Eratosthenes; chương 8 nối tiếp về việc kích thước Trái Đất không đáng kể trong quan trắc thiên thể. Số quyển và số chương **khớp** với cách đánh số chuẩn của bản Todd (Teubner) và bản dịch Bowen–Todd, *Cleomedes' Lectures on Astronomy: A Translation of The Heavens*, University of California Press, 2004. **Không có lỗi "+1" ở đây.**

**Sai — con số stadia không khớp chính nguồn được dẫn.**
Nguyên văn: *"Kết quả hai trăm năm mươi hai nghìn stadia"*, với dòng Nguồn ghi *"Cleomedes, Caelestia, q. I, 7 (ghi lại phép đo)"*.
Thực tế: **Cleomedes I.7 cho 250.000 stadia**, không phải 252.000 — ông chép phép tính dạng giản lược: khoảng cách Alexandria–Syene 5.000 stadia nhân 50 (vì bóng nắng ứng 1/50 vòng tròn) = 250.000. Con số **252.000 stadia đến từ Pliny** (và được Strabo nhắc), và giới nghiên cứu tranh luận liệu Eratosthenes có tự chỉnh 250.000 → 252.000 cho chia chẵn (252.000 ÷ 360 = 700 stadia/độ) hay không. Như hiện trạng, mục nêu một con số rồi dẫn một nguồn ghi con số khác.
Đề xuất: *"Kết quả Cleomedes chép lại là 250.000 stadia; Pliny truyền con số 252.000, chia chẵn thành 700 stadia mỗi độ. Sai số là bao nhiêu thì còn tuỳ đơn vị stadion nào được dùng, nhưng phương pháp thì không phụ thuộc điều đó."*
Và bổ sung nguồn: *"Pliny, Naturalis Historia, q. II"* nếu muốn giữ con số 252.000.

**Sai — Tư tưởng / đóng góp chính, mệnh đề "đầu tiên" có người đi trước.**
Nguyên văn: *"Bộ Địa lý học của ông là công trình đầu tiên đặt các địa điểm lên lưới kinh tuyến và vĩ tuyến"*
Thực tế: **Dicaearchus xứ Messana (hoạt động k. 340–290 TCN)**, học trò Aristotle, là người đầu tiên kẻ lên bản đồ một đường vĩ tuyến và một đường kinh tuyến chia oikoumene (cái mà giới nghiên cứu hiện đại gọi là *diaphragma*). **Eratosthenes xây tiếp trên diaphragma của Dicaearchus**, thậm chí dùng lại một phần đường vĩ tuyến gốc của ông, rồi mới thêm hệ thống đường nhiều hơn và toạ độ hệ thống hơn.
Đề xuất: *"Bộ Địa lý học của ông mở rộng đường chia của Dicaearchus thành một lưới kinh tuyến và vĩ tuyến phủ toàn bộ thế giới đã biết, lần đầu đặt các địa điểm lên toạ độ một cách hệ thống."*
Nguồn: *The History of Cartography*, q. I, ch. 9 "The Growth of an Empirical Cartography in Hellenistic Greece" (University of Chicago Press).

**Sai — `Ảnh hưởng tới`, quan hệ ngược với bằng chứng duy nhất còn lại. (Chiều lint không quét — đúng chỗ hai vòng trước đã tìm ra lỗi.)**
Nguyên văn: *"- CH03-BCE02-03 · kế thừa · qua trường phái"* → đích là **Hipparchus xứ Nicaea** ✓ đúng người, đúng chiều niên đại.
Thực tế: tác phẩm **duy nhất** của Hipparchus liên quan tới Eratosthenes mà ta biết tên là ***Chống lại Địa lý học của Eratosthenes*** (Πρὸς τὴν Ἐρατοσθένους γεωγραφίαν), **ba quyển**, còn lại qua trích dẫn của Strabo. Nội dung là công kích: Hipparchus chê Eratosthenes không dùng đủ dữ liệu thiên văn để đặt các đường chuẩn và không đủ tính toán học, rồi sửa hàng loạt vị trí và khoảng cách. Gọi quan hệ này là `kế thừa` là nói ngược.
Đề xuất: *"- CH03-BCE02-03 · phản bác · trực tiếp"* — và đây là một quan hệ **mạnh hơn** `kế thừa`, vì có tên tác phẩm và trích dẫn còn lại, nên nên dùng mức bằng chứng `trực tiếp` chứ không phải `qua trường phái`.
Ghi chú: cùng một dòng `CH03-BCE02-03 · kế thừa · qua trường phái` cũng xuất hiện ở mục `CH03-BCE03-05` (Archimedes) — xem phần 6; hai mục khác nhau trỏ cùng một đích với cùng một nhãn quan hệ mơ hồ là dấu hiệu dòng này được điền theo khuôn chứ không theo bằng chứng.

**Thể thức — Vì sao chọn. CẢ HAI ứng viên đều không cùng thời.**
Nguyên văn: *"Ứng viên cùng lĩnh vực là Pytheas xứ Massalia, người đi thuyền tới Bắc Âu và đo vĩ độ bằng bóng nắng sớm hơn, và Posidonius, người đo lại chu vi Trái Đất sau đó."*
Thực tế:
- **Pytheas** hoạt động khoảng 325 TCN, tức **khoảng 50 năm trước khi Eratosthenes sinh (276 TCN)**. Không cùng thời.
- **Posidonius** khoảng **135–51 TCN**, tức sinh **khoảng 60 năm sau khi Eratosthenes mất (194 TCN)**. Không cùng thời. (Chính chapter này đặt Posidonius ở `CH03-BCE01-12`, cách hai nhóm.)
Mục còn tự tố giác: "sớm hơn" và "sau đó" là chữ của chính tác giả. §5 đòi ứng viên **cùng thời**, nên mục này hiện không có ứng viên hợp lệ nào.
Cái đúng — ứng viên thật sự cùng thời với Eratosthenes (276–194 TCN) và cùng mạch "đo vũ trụ bằng hình học": **Aristarchus xứ Samos (k. 310–230 TCN)**, người tính tỉ lệ kích thước và khoảng cách Mặt Trời – Mặt Trăng và đưa ra mô hình nhật tâm; và **Conon xứ Samos (k. 280–220 TCN)**, nhà thiên văn ở Alexandria, bạn thư từ của Archimedes.
Đề xuất: *"Ứng viên cùng thời là Aristarchus xứ Samos, người quy kích thước và khoảng cách Mặt Trời – Mặt Trăng về một phép đo góc, và Conon xứ Samos, nhà thiên văn cùng làm việc trong quỹ đạo Alexandria. Eratosthenes được chọn theo tính nguyên bản (c) và phạm vi (a): ..."* — còn Pytheas và Posidonius nên chuyển thành một câu về bối cảnh "trước và sau", không gọi là ứng viên.

**Nghi vấn — diễn đạt phép đo.**
Nguyên văn: *"so góc bóng nắng cùng một thời điểm ở Alexandria và Syene"*
Vấn đề: theo Cleomedes I.7, Syene không phải một phép đo song song mà là một **tiền đề** — ở Syene vào trưa hạ chí, gnomon không có bóng. Phép đo thật sự chỉ thực hiện ở Alexandria. "So góc bóng nắng ... ở Alexandria và Syene" gợi ý hai phép đo đồng thời, điều mà nguồn không nói.
Đề xuất: *"lấy sự kiện ở Syene trưa hạ chí cọc không đổ bóng làm chuẩn, rồi đo góc bóng ở Alexandria cùng thời khắc ấy và nhân khoảng cách giữa hai nơi theo tỉ lệ cung."*

**Kiểm nội dung — phần còn lại đạt.** Quản thủ Thư viện Alexandria ✓ (do Ptolemaios III triệu, k. 245 TCN) · sàng Eratosthenes ✓.

**Kiểm nguồn — đạt.** Duane W. Roller, *Eratosthenes' Geography: Fragments Collected and Translated, with Commentary and Additional Material*, **Princeton University Press, 2010** ✓ tồn tại, năm đúng, đúng nội dung (hơn 150 mảnh, chủ yếu qua Strabo). Cleomedes *Caelestia* I.7 ✓ — xem trên.

**Kiểm liên kết — còn lại đạt.** `CH03-BCE03-04` → Ptolemaios I Soter ✓ · `CH03-BCE03-03` → Euclid ✓ · `Ảnh hưởng tới CH03-BCE01-11` → Strabo ✓ đúng người, đúng chiều, và là liên kết **mạnh nhất** của mục (phần lớn mảnh *Địa lý học* còn lại là nhờ Strabo trích).

---

## 11. CH03-BCE03-10 · Lý Tư

**Sai — `Kế thừa từ`. Nửa còn lại của lỗi đã nêu ở phần 7.**
Nguyên văn: *"- CH03-BCE03-06 · kế thừa · trực tiếp"* → đích là **Hàn Phi** ✓ đúng người, **quan hệ sai**.
Lý do chi tiết xem phần 7. Tóm tắt: SEP "Legalism in Chinese Philosophy" gọi Lý Tư là *"bạn đồng môn và kẻ thù"* của Hàn Phi; Lý Tư đã ở Tần từ khoảng 247 TCN, Hàn Phi chỉ tới năm 233 TCN và chết ngay trong năm đó do chính Lý Tư dàn xếp. Hai chiều `Ảnh hưởng tới` (mục 06) và `Kế thừa từ` (mục 10) đang nói cùng một điều sai, phải sửa cả hai.
Đề xuất: đổi thành *"- CH03-BCE03-06 · tương đồng độc lập · qua trường phái"*, hoặc bỏ hẳn và giữ hai dòng còn lại.

**Thể thức — Vì sao chọn. Lặp lại lỗi đối xứng với mục 02.**
Nguyên văn: *"Ứng viên cùng vị trí là Triệu Cao, người thao túng triều đình sau khi Tần Thuỷ Hoàng chết, và chính Tần Thuỷ Hoàng."*
Vấn đề: **Tần Thuỷ Hoàng không bị loại** — ông là `CH03-BCE03-02` trong chính nhóm này. Và mục 02 lại nêu Lý Tư làm ứng viên bị loại của Tần Thuỷ Hoàng. Hai mục kể nhau là ứng viên thua cuộc trong khi cả hai đều được chọn; đọc liền nhau thì tự mâu thuẫn, và người đọc không biết ai bị loại thật.
Triệu Cao (mất 207 TCN) **đúng là cùng thời** ✓ và là ứng viên hợp lệ.
Đề xuất: *"Ứng viên cùng vị trí là Triệu Cao, người thao túng triều đình sau khi Tần Thuỷ Hoàng chết, và Mông Điềm, tướng phụ trách trường thành và đường trực đạo. (Tần Thuỷ Hoàng được chọn riêng ở `CH03-BCE03-02`.)"*

**Nghi vấn — Tư tưởng / đóng góp chính. Quy công cho tiểu triện quá rộng.**
Nguyên văn: *"lấy tiểu triện làm chuẩn, bước có hệ quả dài nhất vì nó giữ cho văn tự Trung Hoa thống nhất qua mọi phân liệt về sau"*
Vấn đề: cổ văn tự học hiện đại không chống đỡ mệnh đề nhân quả này. (a) Qiu Xigui chỉ ra chính các bản khắc chiếu thư đời Tần cho thấy **triện thư đương thời chưa nhất quán**, tức việc "chuẩn hoá" trên thực địa lỏng hơn ghi chép truyền thống. (b) **Lệ thư (隸書) đã hình thành từ cuối Chiến Quốc** và nhanh chóng thay tiểu triện trong văn bản hành dụng vì viết nhanh hơn; dòng chảy giữ cho chữ Hán thống nhất về sau là lệ thư → khải thư, không phải tiểu triện, vốn chủ yếu còn dùng cho ấn chương và văn bia.
Đề xuất: *"...loại bỏ các dị thể của sáu nước và lấy hệ chữ nước Tần làm chuẩn. Tiểu triện là thể chính thức, còn lệ thư — vốn đã hình thành cuối Chiến Quốc — mới là thể thực dụng lan ra, và chính mạch này giữ cho văn tự Trung Hoa thống nhất qua mọi phân liệt về sau."*

**Kiểm nội dung — phần còn lại đạt.** Tờ tâu bác phong đất, đề nghị quận–huyện, năm 221 TCN ✓ (*Sử ký* q. 6) · dâng kiến nghị đốt sách **213 TCN** ✓ · **bị xử tử năm 208 TCN** ✓ (SEP "Xunzi" cũng ghi Li Si d. 208 BCE).

**Kiểm nguồn — đạt.** Tư Mã Thiên, *Sử ký*, **Lý Tư liệt truyện** ✓ tồn tại (q. 87) — mục không ghi số quyển nên không có rủi ro bịa số. Mark Edward Lewis, *The Early Chinese Empires: Qin and Han*, 2007 ✓ (xem phần 3).

**Kiểm liên kết — còn lại đạt.** `CH03-BCE03-11` → Tuân Tử ✓ đúng người, đúng chiều (thầy, chép trong *Sử ký*) · `CH03-BCE04-06` → Thương Ưởng ✓ · `Ảnh hưởng tới CH03-BCE03-02` → Tần Thuỷ Hoàng ✓.

---

## 12. CH03-BCE03-11 · Tuân Tử

**Nghi vấn — Vì sao chọn. Nguồn được dẫn của chính mục lại bác lập luận được dùng.**
Nguyên văn: *"Tuân Tử được chọn theo counterfactual (d): hai học trò của ông, Hàn Phi và Lý Tư, mang lập luận về bản tính và chế tác sang Pháp gia và sang bộ máy nhà Tần, nên mạch từ ông tới thiết chế đế chế là ngắn nhất trong các nhà Nho tiên Tần."*
Vấn đề: mục dẫn SEP "Xunzi" (Paul R. Goldin) làm nguồn. Mục SEP ấy **có** xác nhận hai học trò (Hàn Phi, mất 233 TCN; Lý Tư, mất 208 TCN) ✓, nhưng đồng thời **trình bày chính câu chuyện "qua hai học trò này Tuân Tử tiếp sức cho Pháp gia và phản bội nguyên lý cao đẹp" như một lời buộc tội đời sau, một cách hiểu sai chứ không phải ý đồ của Tuân Tử**. Tức lập luận chọn của mục dựa trên một mạch nhân quả mà nguồn duy nhất bằng tiếng Anh của mục đang phản đối. Đây không phải lỗi sự thật, nhưng là lỗi "nguồn không chống đỡ điều được dẫn" theo đúng cảnh báo ở `CONTRIBUTING.md` mục 2.
Đề xuất: giữ counterfactual nhưng nói rõ đây là mạch **thiết chế**, không phải mạch **chủ trương**: *"...hai học trò của ông, Hàn Phi và Lý Tư, là hai người thiết kế bộ máy nhà Tần, nên mạch từ lớp học của ông tới thiết chế đế chế là ngắn nhất trong các nhà Nho tiên Tần — dù giới nghiên cứu hiện nay (Goldin) cho rằng gán bản thân học thuyết Tuân Tử cho Pháp gia là cách đọc đời sau."*

**Thể thức — Vì sao chọn. Chỉ một ứng viên, và không hẳn cùng thời.**
Nguyên văn: *"Ứng viên trong cùng truyền thống là Mạnh Tử, người ông phản bác trực tiếp và đã được chọn ở nhóm trước."*
Vấn đề: Mạnh Tử (k. 372–289 TCN) mất khi Tuân Tử (k. 313–230) mới khoảng 24 tuổi; hai người **không từng gặp nhau**, và Tuân Tử phản bác **văn bản** chứ không phải người đương thời. Quan trọng hơn: Mạnh Tử **đã được chọn** (`CH03-BCE04-04`) — mục có ghi rõ điều này ✓ (xử lý đúng, khác mục 01/02/03/10), nhưng kết quả là mục **không nêu được ứng viên nào thật sự bị loại**.
Cái đúng — ứng viên Nho gia **cùng thời** thật sự: **Thận Đáo** và các học giả Tắc Hạ cùng thế hệ, hoặc trong mạch truyền Nho thì **Tử Tư học phái / tác giả *Trung dung*** (sớm hơn) và **Thi Giảo**. Ứng viên sát nhất về thời gian và lĩnh vực là **Trâu Diễn (k. 305–240 TCN)**, người cùng ở Học cung Tắc Hạ, cùng bàn quan hệ trời–người, và đưa ra thuyết Ngũ đức chung thuỷ mà nhà Tần dùng làm chính danh.
Đề xuất: *"Ứng viên cùng thời, cùng ở Học cung Tắc Hạ, là Trâu Diễn, người đưa ra thuyết Ngũ đức chung thuỷ mà nhà Tần dùng làm chính danh. (Mạnh Tử, người ông phản bác trực tiếp, được chọn riêng ở `CH03-BCE04-04`.)"*

**Thiếu — Tư tưởng / đóng góp chính bỏ sót dữ kiện tiểu sử quan trọng nhất của mục, và dữ kiện ấy lại là phản ví dụ cho mục 04.**
Vấn đề: trường `nơi:` ghi "nước Triệu, nước Tề và đất Lan Lăng nước Sở" ✓ đúng, nhưng văn xuôi **không nhắc Học cung Tắc Hạ**, nơi Tuân Tử **ba lần làm tế tửu** (chức chủ toạ). Đây vừa là dữ kiện tiểu sử trung tâm, vừa là thiết chế mà mục `CH03-BCE03-04` (Ptolemaios I) đã bỏ qua khi khẳng định Mouseion là "mô hình tài trợ nghiên cứu công sớm nhất được ghi chép" — xem phần 5. Bổ sung một câu ở đây sẽ đồng thời vá lỗi kia.
Đề xuất: thêm vào cuối đoạn *"Tư tưởng / đóng góp chính"*: *"Ông ba lần làm tế tửu Học cung Tắc Hạ của nước Tề, cơ sở học thuật được nhà nước cấp nhà ở và bổng lộc sớm nhất còn được ghi chép."*

**Nghi vấn — trung lập, mệnh đề tối cao không quy thuộc.**
Nguyên văn: *"Đây là lập trường tự nhiên chủ nghĩa rõ nhất trong Nho học cổ."*
Đề xuất: *"Thiên Thiên luận thường được coi là lập trường tự nhiên chủ nghĩa rõ nhất trong Nho học tiên Tần."* — hoặc quy thuộc đích danh cho Goldin.

**Kiểm nội dung — đạt.** Bác tính thiện, chủ trương tính ác và "thiện là nguỵ (chế tác có chủ ý)" ✓ · lễ là chế tác của tiên vương để điều hoà ham muốn trong điều kiện vật chất hữu hạn ✓ · thiên **Thiên luận** (天論) tách trời khỏi đạo đức, cầu đảo chỉ còn giá trị nghi thức ✓ — SEP "Xunzi" §4 ("The Source of the Rituals: Heaven and the Way") bàn đúng nội dung này, dù không tách riêng thiên Thiên luận thành một mục.

**Kiểm nguồn — đạt.** SEP **"Xunzi"**, **Paul R. Goldin**, `https://plato.stanford.edu/entries/xunzi/` ✓ **tồn tại** (công bố 06/7/2018, sửa lớn 02/6/2025), đúng nhân vật, có bàn tới cả hai học trò.

**Kiểm liên kết — đạt.** `CH02-BCE06-01` → Khổng Tử ✓ · `CH03-BCE04-04` → Mạnh Tử ✓, `phản bác · trực tiếp` đúng (Tuân Tử bác tính thiện trong thiên *Tính ác*) · `Ảnh hưởng tới CH03-BCE03-06` → Hàn Phi ✓ và `CH03-BCE03-10` → Lý Tư ✓ — **hai liên kết này đúng**, khác với liên kết Hàn Phi↔Lý Tư ở phần 7 và 11.

---

## 13. CH03-BCE03-12 · Hannibal Barca

**Nghi vấn — `Ảnh hưởng tới`, mức bằng chứng quá mạnh. (Chiều lint không quét.)**
Nguyên văn: *"- Scipio Africanus · kế thừa · trực tiếp"*, cùng câu trong Vì sao chọn: *"Scipio phần lớn là học và áp dụng lại chính cách đánh ấy trên chiến trường Hispania"*.
Vấn đề: đây là **suy luận của sử học hiện đại**, không phải điều nguồn cổ nói. Polybius — chính nguồn được dẫn của mục — **không viết rằng Scipio bắt chước Hannibal**; ông mô tả Ilipa (206 TCN) và Zama như những bố trí riêng của Scipio. Hơn nữa phần lớn chiến dịch Hispania của Scipio là từ 210 TCN trở đi, khi Hannibal đang ở Italia, nên "học trực tiếp" không có kênh ghi chép nào.
Đề xuất: đổi mức bằng chứng thành *"- Scipio Africanus · kế thừa · suy đoán học giả"*, và sửa câu trong Vì sao chọn thành *"...còn chiến thuật bao vây Scipio dùng ở Ilipa thường được giới nghiên cứu đọc như một đáp lại Cannae, dù Polybius không nói ông học của Hannibal."*

**Nghi vấn — trung lập, mệnh đề không quy thuộc.**
Nguyên văn: *"Trận này vẫn nằm trong chương trình các học viện quân sự hiện đại như ví dụ chuẩn về tiêu diệt gọn một lực lượng đông hơn."*
Vấn đề: khẳng định về hiện tại, không nêu theo ai và không kiểm được bằng một nguồn học thuật cụ thể. **Không kiểm được** trong phạm vi vòng duyệt này.
Đề xuất: dựa vào dòng liên kết đã có mà viết chắc hơn: *"Alfred von Schlieffen lấy Cannae làm hình mẫu cho lý thuyết trận tiêu diệt của ông trong chuyên luận Cannae (1913), và trận này vẫn được dẫn như ví dụ chuẩn về bao vây toàn phần."*

**Kiểm nội dung — đạt, không tìm thấy lỗi niên đại hay số liệu.**
Vượt Alps vào Italia **218 TCN** ✓ · Cannae **216 TCN** ✓ · cơ chế trận Cannae (trung quân lồi ra rồi lùi có kiểm soát, hai cánh khép lại, kỵ binh Numidia/Iberia vòng sau lưng) ✓ · ở lại Italia **mười lăm năm** ✓ (218 → 203 TCN, khi ông được gọi về) · thua ở **Zama 202 TCN** ✓ · chọn đường bộ vì Rome trội hải quân sau Chiến tranh Punic I ✓.

**Kiểm nguồn — đạt.** Polybius, *Lịch sử*, **q. III** ✓ — **đúng quyển**: Quyển III là quyển về nguyên nhân Chiến tranh Punic II, hành quân vượt Alps, Trebia, Trasimene và Cannae. Số quyển này đã được kiểm, không phải đoán. Dexter Hoyos, *Hannibal's Dynasty: Power and Politics in the Western Mediterranean, 247–183 BC*, **Routledge, 2003** ✓ tồn tại, năm đúng, đúng phạm vi.

**Kiểm thể thức — đạt.** Scipio Africanus (236–183 TCN) **thật sự cùng thời** với Hannibal (k. 247–183) ✓, cùng lĩnh vực ✓, là **đối thủ cạnh tranh thật** ✓, và **không có mục riêng trong atlas** nên đúng là ứng viên bị loại. Cùng với mục 05 (Archimedes), đây là một trong hai mục làm đúng thể thức §5 của cả nhóm.

**Kiểm liên kết — còn lại đạt.** `Hamilcar Barca` ✓ (cha) · `Lý thuyết trận tiêu diệt của Schlieffen` ✓ đúng chiều.

---

## 14. Tổng hợp phát hiện

| # | Mục | Loại | Tóm tắt |
|---|---|---|---|
| 1 | Bối cảnh | Nghi vấn | "đế chế quan liêu đầu tiên" không quy thuộc; quận–huyện có trước Tần |
| 2 | Bối cảnh | Nghi vấn | "kiểm soát Địa Trung Hải" là chuyện TK 2 TCN, không phải TK 3 |
| 3 | BCE03-01 | Nghi vấn | "lần đầu nhà nước công bố chính sách bằng tiếng địa phương" — Behistun, Hammurabi đi trước |
| 4 | BCE03-01 | Thể thức | Chandragupta được nêu là "ứng viên bị loại" nhưng đã được chọn ở `CH03-BCE04-08`; cả hai ứng viên không cùng thời |
| 5 | BCE03-02 | Thể thức | Lý Tư được nêu là ứng viên bị loại nhưng là `CH03-BCE03-10`, và là cộng sự |
| 6 | BCE03-03 | **Sai** | **URL SEP "Euclid" trả 404 — SEP không có mục từ này** |
| 7 | BCE03-03 | Thể thức | Theaetetus mất ~65 năm trước floruit Euclid; Eudoxus đã được chọn ở `CH03-BCE04-09` |
| 8 | BCE03-03 | Nghi vấn | "in nhiều nhất sau Kinh Thánh" không quy thuộc; "chỉ dựa vào Proclus" bỏ sót Pappus |
| 9 | BCE03-04 | **Sai** | **"mô hình tài trợ nghiên cứu công sớm nhất" — Học cung Tắc Hạ đi trước, và Tuân Tử ở cùng nhóm từng làm tế tửu ở đó** |
| 10 | BCE03-04 | **Sai** | Euclid, Eratosthenes, Herophilos **không hề cùng làm việc**; Eratosthenes tới Alexandria ~37 năm sau khi Ptolemaios I mất |
| 11 | BCE03-04 | Nghi vấn | Quy công lập Thư viện cho Ptolemaios I viết như sự kiện đã định |
| 12 | BCE03-04 | Thể thức | Ptolemaios II là con và đồng trị vì, không phải ứng viên cạnh tranh |
| 13 | BCE03-05 | Nghi vấn | "đọc được đầy đủ sau 1998" — Heiberg đã công bố *Phương pháp* từ 1907 |
| 14 | BCE03-05 | Nghi vấn | "chưa thấy ở đâu khác" là luận điểm Netz, không quy thuộc; `Ảnh hưởng tới` Hipparchus **không kiểm được** |
| 15 | BCE03-06 | **Sai** | **URL SEP "Han Fei" trả 404 — mục từ đúng là `chinese-legalism`** |
| 16 | BCE03-06 | **Sai** | **Hàn Phi → Lý Tư `kế thừa · trực tiếp` bị chính SEP bác ("fellow student and nemesis") và bị niên đại bác** |
| 17 | BCE03-07 | Thể thức | Chrysippus là người kế vị đời thứ ba, không phải ứng viên cùng thời; mục còn lại không ứng viên hợp lệ |
| 18 | BCE03-07 | Nghi vấn | Zeno → Cicero gọi gọn là `kế thừa` bỏ mất việc Cicero bác tri thức luận Khắc kỷ |
| 19 | BCE03-08 | Thiếu | SEP "Epicurus" không nói gì về phụ nữ và nô lệ trong Khu vườn; chỗ dựa là Diogenes Laërtius X |
| 20 | BCE03-09 | **Sai** | **252.000 stadia không phải con số của Cleomedes (250.000); 252.000 đến từ Pliny** |
| 21 | BCE03-09 | **Sai** | "lưới kinh–vĩ tuyến đầu tiên" — Dicaearchus xứ Messana đi trước |
| 22 | BCE03-09 | **Sai** | **Eratosthenes → Hipparchus `kế thừa` nói ngược: tác phẩm duy nhất còn biết tên là *Chống lại Địa lý học của Eratosthenes*, 3 quyển** |
| 23 | BCE03-09 | Thể thức | **Cả hai** ứng viên (Pytheas, Posidonius) đều không cùng thời — chính văn bản viết "sớm hơn" và "sau đó" |
| 24 | BCE03-09 | Nghi vấn | Diễn đạt phép đo gợi hai phép đo đồng thời; Syene là tiền đề, không phải phép đo |
| 25 | BCE03-10 | **Sai** | Nửa còn lại của #16: `Kế thừa từ CH03-BCE03-06` |
| 26 | BCE03-10 | Thể thức | Tần Thuỷ Hoàng được nêu là ứng viên bị loại nhưng là `CH03-BCE03-02` — đối xứng với #5 |
| 27 | BCE03-10 | Nghi vấn | Quy công "tiểu triện giữ cho văn tự Trung Hoa thống nhất" — thực tế là mạch lệ thư → khải thư |
| 28 | BCE03-11 | Nghi vấn | Nguồn SEP của mục trình bày chính mạch "Tuân Tử sinh ra Pháp gia" như cách đọc sai của đời sau |
| 29 | BCE03-11 | Thể thức | Ứng viên duy nhất (Mạnh Tử) đã được chọn; không nêu được ai bị loại thật |
| 30 | BCE03-11 | Thiếu | Không nhắc Học cung Tắc Hạ, dữ kiện vá được lỗi #9 |
| 31 | BCE03-11 | Nghi vấn | "rõ nhất trong Nho học cổ" không quy thuộc |
| 32 | BCE03-12 | Nghi vấn | Hannibal → Scipio `trực tiếp` quá mạnh; Polybius không nói Scipio học Hannibal |
| 33 | BCE03-12 | Nghi vấn | "vẫn nằm trong chương trình các học viện quân sự hiện đại" — **không kiểm được** |

**Đã kiểm và ĐÚNG (ghi lại để khỏi kiểm lại ở vòng sau):**
- Toàn bộ 12 Q-ID trỏ đúng người; không trường `năm:` nào lệch ngoài dung sai.
- **Cleomedes, *Caelestia*, q. I, 7** — **đúng quyển, đúng chương**; Quyển I có 8 chương, chương 7 là chương về kích thước Trái Đất. Không có lỗi "+1".
- **Diogenes Laërtius q. VII** (Zeno/Khắc kỷ) và **q. X** (Epicurus) — đúng quyển.
- **Polybius q. III** (vượt Alps, Cannae) — đúng quyển.
- SEP `stoicism`, `epicurus`, `xunzi` — **tồn tại và thật sự bàn tới điều được dẫn**.
- Sách: Thapar 1961/2012 · Schneider 1978 · Lewis 2007 · Heath 1908 và 1897 · Hölbl 2001 · MacLeod 2000 · Netz & Noel 2007 · Roller 2010 · Hoyos 2003 — **tất cả tồn tại, năm xuất bản đúng, đúng chủ đề**.
- Chặn số pi của Archimedes (3,1408 < π < 3,1429, đa giác 96 cạnh) — **đúng**.
- Đốt sách **213 TCN**, Lý Tư bị xử tử **208 TCN**, Hàn Phi chết **233 TCN**, Cannae **216 TCN**, Zama **202 TCN**, Poggio tìm lại Lucretius **1417** — tất cả **đúng**.
- Quy thuộc Pháp gia: Thương Ưởng ↔ pháp, Thân Bất Hại ↔ thuật, Thận Đáo ↔ thế — **đúng**, xác nhận bằng SEP `chinese-legalism`.

**Hai mục làm đúng thể thức §5 (dùng làm mẫu để sửa 10 mục còn lại):** `CH03-BCE03-05` (Archimedes — ghi rõ Apollonius "được chọn riêng ở nhóm sau") và `CH03-BCE03-12` (Hannibal — Scipio cùng thời, đối thủ thật, không có mục riêng).

**Hình dạng lỗi đáng chú ý:** 7/12 mục nêu làm "ứng viên bị loại" một người **đã được chọn ở nơi khác trong atlas** hoặc **không cùng thời**. Danh sách "Ứng viên mạnh đã bị loại" trong `## Ghi chú biên tập` thì lại **chính xác** — nó chỉ liệt kê người thật sự bị loại (Theophrastus, Chrysippus, Ptolemaios II, Bindusara, Pytheas, Ctesibius, Seleucus I, Aristarchus, Arcesilaus, Pyrrho...). Tức là phần văn xuôi "Vì sao chọn" được viết độc lập với danh sách ấy, và nên được dò chéo với nó một lượt.

---

## 15. Đánh giá lựa chọn nhân vật

### 15.1 Độ phủ
- **Lĩnh vực: 10/16** — Chính trị/Nhà nước (4), Triết học (4), Toán học (3), Giáo dục (2), và mỗi lĩnh vực 1 người: Tôn giáo, Kỹ thuật, Luật, Khám phá/Địa lý, Ngôn ngữ học, Quân sự. **Đạt** yêu cầu "ít nhất 4 lĩnh vực".
- **Vùng: 4/9** — Trung Đông/Bắc Phi 4, Đông Á 4, Châu Âu 3, Nam Á 1. **Đạt** yêu cầu "ít nhất 3 vùng".
- **Trống hoàn toàn: Y học, Khoa học tự nhiên, Văn học, Sử học, Nghệ thuật/Kiến trúc, Kinh tế.** Không có phụ nữ.
- **Mất cân đối đáng chú ý: Nam Á chỉ 1/12** trong đúng thế kỷ đế chế Maurya đạt cực thịnh, trong khi **ba mục (02, 06, 10) đều nói về cùng một bộ chính sách của nhà Tần**, cộng thêm 11 (Tuân Tử, thầy của hai người kia) là **4/12 suất cho một mạch duy nhất**. Đây là chỗ nên lấy suất nếu muốn thêm ai.

### 15.2 Ứng viên đáng ra phải được cân nhắc mà **chưa từng xuất hiện**, kể cả trong danh sách bị loại

**(1) Herophilos xứ Chalcedon (k. 335–280 TCN) — ca bỏ sót nặng nhất.**
Tên ông **đã xuất hiện trong chính chapter** — ở dòng "Vì sao chọn" của `CH03-BCE03-04` — nhưng ông **không có mục riêng và cũng không có tên trong danh sách bị loại**. Tức là chapter viện ông ra làm bằng chứng cho giá trị của Mouseion rồi bỏ rơi ông.
Lập luận theo bốn tiêu chí: (c) **tính nguyên bản** — ông là người đầu tiên mổ xác người một cách hệ thống, trong khoảng bốn mươi năm duy nhất của lịch sử y học Hy Lạp mà lệnh cấm được dỡ; ông tách thần kinh khỏi gân và mạch, phân loại thần kinh vận động và cảm giác, mô tả và **đặt tên tá tràng (duodenum)** và tuyến tiền liệt, mô tả não thất và hội lưu xoang màng cứng (nay vẫn mang tên *torcular Herophili*). (b) **độ bền** — thuật ngữ do ông đặt còn dùng trong giải phẫu học hôm nay. (a) **phạm vi** — qua Galen, giải phẫu học của ông chi phối y học châu Âu và Hồi giáo tới thế kỷ 16.
Hệ quả: đưa ông vào sẽ lấp **lỗ hổng lĩnh vực duy nhất nghiêm trọng của nhóm (Y học)**, và vá luôn lỗi #10 — vì ông và Euclid **thật sự** cùng thời ở Alexandria, khác với Eratosthenes.
Đi kèm có thể xét **Erasistratus xứ Ceos (k. 304–250 TCN)**, cộng sự mổ xác và nhà sinh lý học thực nghiệm đầu tiên — nhưng theo đúng logic (d) của chapter thì nên chọn một.

**(2) Trâu Diễn (鄒衍 Zou Yan, k. 305–240 TCN).**
Cùng ở Học cung Tắc Hạ với Tuân Tử, tức **cùng thời, cùng nơi, cùng lĩnh vực**. (b) **độ bền** cực cao: thuyết Ngũ hành và Ngũ đức chung thuỷ của ông trở thành khung vũ trụ luận chung của y học, lịch pháp, phong thuỷ và — quan trọng nhất — **lý thuyết chính danh của mọi triều đại Trung Hoa**, bắt đầu từ chính nhà Tần nhận đức Thuỷ. (d) counterfactual mạnh: không có khung này thì cách Đông Á nói về biến đổi trong hai nghìn năm sẽ khác hẳn. Ông không có tên ở bất cứ đâu trong `ch03.md`.

**(3) Lý Băng (李冰, làm thái thú Thục k. 272–235 TCN).**
Công trình Đô Giang Yển trên sông Mân, khởi công khoảng 256 TCN, **vẫn đang tưới đồng bằng Thành Đô cho tới hôm nay** — hơn 2.250 năm vận hành liên tục, và vận hành **không có đập**, bằng cách dẫn dòng chứ không chặn dòng. Theo tiêu chí (b) độ bền thì đây có lẽ là hiện vật bền nhất của cả nhóm BCE03. Nhóm hiện chỉ có **1 người thuộc Kỹ thuật/Công nghệ** (Archimedes, và kiêm Toán học). Không có tên ở bất cứ đâu trong `ch03.md`.

**(4) Callimachus xứ Cyrene (k. 310–240 TCN).**
Soạn bộ *Pinakes* — mục lục phân loại Thư viện Alexandria theo 120 quyển, **hệ thống phân loại thư mục sớm nhất được ghi chép**, tổ tiên của mọi mục lục thư viện về sau; đồng thời là người định hình thi pháp Hy Lạp hoá chi phối thơ Latinh (Catullus, Propertius, Ovid). Việc chapter dành một mục cho **người cấp kinh phí** Thư viện (`CH03-BCE03-04`) mà không cân nhắc **người tổ chức tri thức bên trong nó** là một bất đối xứng đáng nêu. Không có tên ở bất cứ đâu trong `ch03.md`.

**(5) Khuất Nguyên (屈原, k. 340–278 TCN) — nếu muốn lấp lỗ hổng Văn học.**
Tác giả có tên sớm nhất của thi ca Trung Hoa (*Ly tao*, *Sở từ*), mở ra truyền thống tác giả cá nhân đối lập với thi ca vô danh của *Kinh Thi*. Nhóm BCE03 hiện **không có một mục Văn học nào**, và cả nhóm BCE04 cũng không. Niên đại của ông vắt ranh 301/300 TCN nên cần quyết đặt ở BCE04 hay BCE03.

### 15.3 Hai ghi chú về danh sách bị loại ở `## Ghi chú biên tập`

**Sai — lý do loại Aristarchus xứ Samos ghi sai sự kiện.**
Nguyên văn: *"Aristarchus xứ Samos: ... nhưng chỉ còn qua một câu trích của Archimedes và không tạo được truyền thống nối tiếp"*
Thực tế: **chuyên luận *Về kích thước và khoảng cách Mặt Trời và Mặt Trăng* của Aristarchus còn nguyên vẹn bằng tiếng Hy Lạp** và là một trong những văn bản toán–thiên văn Hy Lạp hoàn chỉnh cổ nhất còn lại. Thứ **chỉ** còn qua một đoạn trong *Người đếm cát* của Archimedes là **giả thuyết nhật tâm**, không phải toàn bộ công trình của ông. Lý do loại vì thế đang dựa trên một dữ kiện sai, và nếu sửa lại thì hồ sơ của Aristarchus mạnh hơn hẳn — đủ để xét lại suất, nhất là khi mục `CH03-BCE03-09` đang cần một ứng viên cùng thời hợp lệ (xem #23).
Đề xuất: *"Aristarchus xứ Samos: chuyên luận Về kích thước và khoảng cách Mặt Trời và Mặt Trăng còn nguyên, nhưng giả thuyết nhật tâm của ông chỉ còn qua một đoạn trong Người đếm cát của Archimedes và không tạo được truyền thống nối tiếp cho tới Copernicus; thua ở (b)."*

**Nhất quán — Pyrrho và Arcesilaus.**
Danh sách loại ghi *"Pyrrho, Arcesilaus: ... cả hai không để lại trước tác"* ✓ đúng, và điều này **ủng hộ** đề xuất ở phần 8: Arcesilaus là ứng viên cùng thời hợp lệ duy nhất đã được cân nhắc cho Zeno, nên nêu đích danh ông ở "Vì sao chọn" của `CH03-BCE03-07` vừa đúng thể thức §5 vừa nhất quán với Ghi chú biên tập.

### 15.4 Nếu phải lấy suất
Nhóm đã đủ 12/12, nên theo `CONTRIBUTING.md` mọi đề xuất thêm phải nêu người bị thay. Ứng viên yếu nhất theo bốn tiêu chí, theo đánh giá của vòng duyệt này:
1. **`CH03-BCE03-10` Lý Tư** — trùng lặp nặng nhất: ba mục (02, 06, 10) cùng kể một bộ chính sách, và hai trong ba mục còn nêu nhau làm "ứng viên bị loại". Phần đóng góp riêng của ông (thống nhất văn tự) lại chính là phần bị cổ văn tự học hiện đại thu hẹp (xem #27).
2. **`CH03-BCE03-04` Ptolemaios I Soter** — hồ sơ gần như toàn bộ dựa vào việc lập Thư viện, mà việc quy công ấy là điểm tranh luận (#11) và mệnh đề "sớm nhất" chống đỡ nó thì sai (#9).
Thay bằng **Herophilos** (lấp Y học, sửa #10) là nước đi có lợi nhất cho độ phủ; thay bằng **Trâu Diễn** hoặc **Lý Băng** thì giữ cân bằng vùng Đông Á mà vẫn đổi được mạch.

---

*Hết. Vòng duyệt này không sửa `content/ch03.md`; mọi câu "Đề xuất" ở trên là đề nghị để Owner quyết.*
