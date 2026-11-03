# Bình duyệt độc lập — `content/ch01.md`, nhóm **BCE17_15** (TK 17–15 TCN, 1700–1401 TCN)

Người duyệt: agent độc lập, không viết chapter. Ngày: 2026-10-31.
Phạm vi: dòng `**Bối cảnh**` của nhóm + 8 mục `CH01-BCE17_15-01` → `-08`. Không rà nhóm khác (trừ khi cần đối chiếu chéo để bắt mâu thuẫn nội bộ).
Chuẩn đối chiếu: `prompts/atlas-prompt.md` §5 (template + quy tắc chọn), `CONTRIBUTING.md` (8 lỗi hệ thống đã biết).

Xếp loại: **Sai** (khẳng định sai sự thật) · **Nghi vấn** (không đứng vững / mệnh đề tối cao không quy thuộc) · **Thiếu** (nguồn hoặc lập luận chưa đủ) · **Thể thức** (vi phạm template §5 hoặc quy tắc CONTRIBUTING).

---

## 0. Kiểm nền — Q-ID và độ phủ

### 0.1 Q-ID: tất cả 8 mục trỏ đúng người ✅

Tra `wbgetentities` ngày 2026-10-31:

| ID | Tên trong atlas | Q-ID | Nhãn Wikidata (en) | Mô tả | Kết luận |
|---|---|---|---|---|---|
| -01 | Thành Thang | Q471820 | Tang | Legendary first king of the Shang dynasty | ✅ đúng người |
| -02 | Khyan | Q440496 | Khyan | Egyptian pharaoh of the 15th dynasty | ✅ |
| -03 | Ahmose I | Q7222 | Ahmose I | Pharaoh of Ancient Egypt | ✅ |
| -04 | Hatshepsut | Q129234 | Hatshepsut | 5th Pharaoh of the 18th Dynasty | ✅ |
| -05 | Thutmose III | Q157899 | Thutmose III | sixth Egyptian Pharaoh of the 18th Dynasty | ✅ |
| -06 | Mursili I | Q222536 | Mursili I | Hittite king | ✅ |
| -07 | Ahmes | Q1073335 | Ahmes | Egyptian scribe and mathematician (1680BC–1620BC) | ✅ (xem 7.3) |
| -08 | Viśvāmitra | Q2773345 | Viśvāmitra | ancient Indian sage | ✅ |

Không có ca "trỏ đúng ID nhưng sai người". Lưu ý theo CONTRIBUTING #4: **khớp Wikidata không đồng nghĩa với đúng** — các phát hiện dưới đây phần lớn là lỗi mà Wikidata không bắt được.

### 0.2 Độ phủ nhóm — đạt ngưỡng §5 nhưng lệch nặng về Ai Cập

- **Lĩnh vực:** Chính trị/Nhà nước, Quân sự, Nghệ thuật/Kiến trúc, Toán học, Tôn giáo/Tâm linh, Văn học = **6 lĩnh vực** ≥ 4 ✅
- **Vùng:** Đông Á (1), Trung Đông/Bắc Phi (6), Nam Á (1) = **3 vùng** ≥ 3 ✅
- Nhưng **5/8 là vua hoặc người chép Ai Cập** (-02 Khyan, -03 Ahmose I, -04 Hatshepsut, -05 Thutmose III, -07 Ahmes), và 4/8 là pharaoh. Trong đó -03, -04, -05 là ba đời kế tiếp của **cùng một vương triều XVIII**. Ghi chú biên tập có giải thích thiên lệch vùng chung của cả chapter (lý do tư liệu), nhưng **không giải thích vì sao riêng nhóm này dành ba suất cho ba vua liên tiếp của một triều**, trong khi Lưỡng Hà — vùng để lại nhiều văn bản nhất giai đoạn này — không có mục nào ngoài -06 (và -06 là người Hatti, không phải Lưỡng Hà).

**→ Thiếu (cấp nhóm).** Xem §9 "Đánh giá lựa chọn nhân vật".

### 0.3 Dòng `**Bối cảnh**`

> "Ở Trung Hoa, nhà Thương thay nhà Hạ."

**Nghi vấn.** Câu này phát biểu nhà Hạ như một thực thể lịch sử đã xác lập. Ghi chú biên tập của chính chapter thừa nhận ngược lại: *"bản thân nhà Hạ vẫn chưa có chứng cứ văn tự đương thời"*. Mục -01 cũng gắn nhãn [Tranh cãi lịch sử] cho chính biến cố ấy. Dòng Bối cảnh, vốn là chỗ người đọc gặp đầu tiên, lại khẳng định trơn tru hơn phần thân.

- *Câu thay thế đề xuất:* "Ở Trung Hoa, nhà Thương nổi lên — truyền thống chép là thay nhà Hạ, nhưng nhà Hạ chưa có chứng cứ văn tự đương thời."

> "Các bài tụng Rigveda bắt đầu được soạn ở tây bắc Nam Á."

Chấp nhận được: niên đại thông dụng của Rigveda là k. 1500–1200 TCN, nằm trong nửa sau của nhóm. Không có lỗi.

---

## 1. `CH01-BCE17_15-01` · Thành Thang

### 1.1 Khẳng định "Đại Ất trên giáp cốt" — **đúng về sự kiện, sai về chữ "đương thời"**

> "tên Đại Ất xuất hiện trong danh sách tổ tiên được tế trên giáp cốt thời Thương, tức chính triều đình ấy coi ông là người lập nghiệp"

**Phần sự kiện: đúng.** Đại Ất (大乙) / Thái Ất (太乙) là tên miếu hiệu của Thành Thang trong giáp cốt văn, và việc đồng nhất Đại Ất với Thành Thang là **đã xác lập vững trong giới nghiên cứu giáp cốt**, không phải suy đoán của atlas. Ông đứng đầu danh sách các vua đã lập triều trong tế tự tổ tiên Thương. ✅

**Phần "tư liệu đương thời": Sai.** Xem 1.2.

Nguồn dùng: en.wikipedia.org/wiki/Tang_of_Shang; chinaknowledge.de — *Shang Period Religion* (danh sách tổ tiên trong miếu bắt đầu từ Thượng Giáp 上甲, lùi xa hơn Đại Ất).

### 1.2 **Sai** — mệnh đề tối cao "nhân vật sớm nhất của Đông Á vừa có trình thuật truyền thống vừa có tên trong tư liệu đương thời"

> "ông là nhân vật sớm nhất của Đông Á vừa có trình thuật truyền thống vừa có tên trong tư liệu đương thời"

**Phản ví dụ tìm được, ngay trong cùng kho giáp cốt:**

- **Vương Hợi (王亥, Wang Hai)** — tổ tiên tiền triều của nhà Thương, được giáp cốt gọi là "cao tổ" (高祖). Có **hơn 130 khắc giáp cốt** nhắc tới ông, nhiều nhất trong số các tổ tiên tiền triều. Đồng thời ông có trình thuật truyền thống phong phú: *Sơn hải kinh*, *Sở từ · Thiên vấn*, *Trúc thư kỉ niên*, *Sử ký*.
- **Thượng Giáp (上甲, Shang Jia)** — tổ tiên tiền triều, vừa có trong danh sách tế tự giáp cốt vừa có trong *Sử ký*.

Cả hai **sớm hơn Thành Thang vài thế hệ** và thoả đúng hai điều kiện mà câu văn nêu. Mệnh đề tối cao do đó sai.

**Lỗi thứ hai, nghiêm trọng hơn: "tư liệu đương thời" không đúng.** Giáp cốt văn bắt đầu từ thời **Vũ Đinh (k. 1250 TCN)** — chính atlas xếp Vũ Đinh ở nhóm sau, `CH01-BCE14_12-10`. Đại Ất xuất hiện trên giáp cốt là **cách thời Thành Thang (k. 1600 TCN) khoảng 350 năm**. Đó là tư liệu đương thời *với triều Thương hậu kỳ*, không đương thời với ông. Chapter này còn tự viết ở Ghi chú biên tập rằng "giáp cốt sớm nhất còn hai trăm năm nữa" tính từ năm 1700 TCN — tức chính tác giả biết khoảng cách này.

- *Câu thay thế đề xuất:* "…có một mạch chứng cứ độc lập: tên Đại Ất đứng đầu danh sách các vua đã lập triều trong tế tự tổ tiên khắc trên giáp cốt — tuy giáp cốt chỉ bắt đầu từ thời Vũ Đinh, tức khoảng ba trăm năm sau ông, nên đây là bằng chứng về *điều triều Thương hậu kỳ tin*, không phải tư liệu đương thời với ông. Những tổ tiên tiền triều như Vương Hợi và Thượng Giáp cũng có mặt trong cùng danh sách ấy."

Nguồn dùng: en.wikipedia.org/wiki/Wang_Hai_of_Shang (130+ khắc giáp cốt, danh hiệu 高祖); en.wikipedia.org/wiki/Shang_Jia; en.wikipedia.org/wiki/Tang_of_Shang.

### 1.3 **Thể thức** — "Hạ Vũ" nêu làm ứng viên nhưng **không cùng thời**, và mục không nói ra

> "Ứng viên thay thế là Y Doãn… và Hạ Vũ."

§5 đòi "1–2 người cùng lĩnh vực, **cùng thời**". Hạ Vũ theo niên đại truyền thống ở k. 2100 TCN — **sớm hơn Thành Thang hơn 400 năm**, và **ngoài hẳn mốc 2000 TCN của atlas**. Ghi chú biên tập cuối chapter có nói điều đó ("Hạ Vũ: niên đại truyền thống đặt ông trước năm 2000 TCN nên ngoài phạm vi"), nhưng **mục -01 không nói**, nên người đọc mục ấy hiểu nhầm là một đánh đổi cùng thời đã xảy ra. Đây đúng là lỗi hệ thống CONTRIBUTING #5 (nêu người không cùng thời mà không nói ra).

Y Doãn thì hợp lệ: cùng thời, có tên trong tế tự giáp cốt, không có mục riêng trong atlas (đã kiểm `grep '^### '` toàn bộ `content/ch0*.md` + `ch90.md`). ✅

- *Câu thay thế đề xuất:* "Ứng viên thay thế cùng thời là Y Doãn, tể tướng được truyền thống gắn với ông và cũng có tên trong tế tự giáp cốt. Hạ Vũ thường được nêu nhưng niên đại truyền thống đặt ông trước mốc 2000 TCN của atlas nên không phải ứng viên cùng thời."

### 1.4 **Nghi vấn** — liên kết "Ảnh hưởng tới CH01-BCE11_9-03" (Chu Công Đán) là lập luận vòng

Mục lập luận rằng trình thuật Thành Thang nhận lỗi thay dân là "hạt giống sớm nhất của ý niệm vua chịu trách nhiệm trước trời", rồi nối ông tới Chu Công Đán. Nhưng chính mục cũng thừa nhận trình thuật ấy "chỉ có ở văn bản đời sau" — mà "đời sau" ở đây là **thư tịch thời Chu**. Thiên mệnh là khái niệm do nhà Chu đặt ra; hình tượng Thành Thang nhận lỗi là do người Chu dựng. Nói Thành Thang "ảnh hưởng tới" Chu Công Đán là đảo ngược chiều tạo tác.

Liên kết đích đã mở kiểm: `CH01-BCE11_9-03` = Chu Công Đán ✅ đúng người; `CH01-BCE14_12-10` = Vũ Đinh ✅ đúng người, và đúng chiều niên đại.

- *Đề xuất:* giữ liên kết nhưng hạ mức bằng chứng xuống `suy đoán học giả`, hoặc đổi loại quan hệ, và sửa câu văn thành "…hình tượng vua nhận lỗi thay dân — do thư tịch thời Chu dựng nên — về sau trở thành tiền lệ mà học thuyết Thiên mệnh viện tới."

---

## 2. `CH01-BCE17_15-02` · Khyan

### 2.1 Hiện vật ở Knossos — **đúng**, nhưng phần mô tả gộp hai thứ khác loại

> "ấn và vật khắc tên ông được tìm thấy ở Knossos trên đảo Crete và ở Baghdad"

**Knossos: đúng.** Một **nắp bình bằng alabaster** khắc tước hiệu Khyan do Arthur Evans tìm được ở cung điện Knossos. ✅

**Baghdad: đúng về vật, nhưng "được tìm thấy ở Baghdad" gây hiểu sai nghiêm trọng.** Vật là một **sư tử bằng đá granite** mang cartouche Seuserenre. Nó **không phải hiện vật khai quật có tầng vị**: nguồn mô tả nó hoặc là bị xây lại vào tường một ngôi nhà ở Baghdad, hoặc là **mua trên thị trường đồ cổ ở Baghdad**. Giới nghiên cứu cho rằng nó **có lẽ có gốc từ Levant**, không phải từ Lưỡng Hà. Dùng nó làm bằng chứng cho một mạng nối Avaris với Lưỡng Hà là vượt quá điều hiện vật chịu được.

**→ Nghi vấn (suy luận vượt bằng chứng).**

> "tức Avaris dưới thời ông nằm trong một mạng trao đổi nối Aegean với Lưỡng Hà"

Chữ "tức" biến hai hiện vật không có tầng vị chắc thành một kết luận về cấu trúc thương mại. Cả hai vật đều thiếu bối cảnh khảo cổ an toàn (nắp Knossos: bối cảnh tầng vị không rõ; sư tử Baghdad: không có xuất xứ khai quật).

- *Câu thay thế đề xuất:* "…để lại dấu vết vật chất trải rộng khác thường: một nắp bình alabaster khắc tước hiệu ông ở cung điện Knossos trên đảo Crete, một bình ở Hattusa, và một tượng sư tử granite mang tên ngai Seuserenre xuất hiện ở Baghdad — vật cuối không có xuất xứ khai quật và nhiều khả năng có gốc từ Levant. Các hiện vật này được đọc như dấu hiệu tiếp xúc ngoại giao của Avaris, dù bối cảnh của từng vật đều không đủ chắc để dựng một tuyến thương mại cụ thể."

### 2.2 **Thiếu** — bỏ sót hiện vật ở Hattusa, chính là chỗ nối với mục -06 của cùng nhóm

Vật thứ ba mang tên Khyan được tìm thấy ở **Boğazköy / Hattusa** (Anatolia). Mục bỏ qua nó. Đáng tiếc vì Hattusa là kinh đô của **Mursili I (`CH01-BCE17_15-06`)**, mục kế trong chính nhóm này — một liên hệ nội bộ bị bỏ lỡ, và là hiện vật củng cố luận điểm "tầm liên hệ" tốt hơn con sư tử Baghdad.

### 2.3 **Thể thức / Sai** — `năm: trị vì k. 1700–1600 TCN` là một triều đại 100 năm

Trường `năm:` ghi "trị vì k. 1700–1600 TCN". Đó là **đúng hai giá trị P569/P570 thô của Wikidata** (born −1700, died −1600) đọc nhầm thành niên đại trị vì. Không ai cho rằng Khyan trị vì một thế kỷ: ước tính thông dụng là **10–30 năm**, nằm đâu đó trong biên `k. 1700–1580 TCN` (biên *floruit*, không phải biên trị vì).

Độ tin cậy Thấp nên lint bỏ qua đối chiếu — đây đúng là ca CONTRIBUTING #4: Wikidata không lệch, nhưng cách đọc Wikidata thì sai.

- *Câu thay thế đề xuất:* `năm: hoạt động k. 1700–1580 TCN` (dùng dạng "hoạt động" theo bảng quy ước `năm:` của CONTRIBUTING, vì biên này là biên *floruit* chứ không phải độ dài một triều đại).

### 2.4 Nguồn Moeller & Marouard — **có thật, đúng năm, đúng tạp chí, đúng nội dung** ✅, nhưng **tên bài bị cắt**

Atlas ghi:
> Nadine Moeller và Gregory Marouard, "Discussion of Late Middle Kingdom and Early Second Intermediate Period History", *Ägypten und Levante* 21 (2011).

Kiểm:
- (a) **Có thật** ✅
- (b) **Đúng năm** ✅ — 2011
- (c) **Đúng tạp chí** ✅ — *Ägypten und Levante / Egypt and the Levant* XXI, tr. 87–121
- (d) **Có bàn tới điều được dẫn** ✅ — bài này chính là công bố các khuôn ấn (sealings) Khyan ở Tell Edfu, tìm thấy chung bối cảnh với khuôn ấn của vua vương triều XIII Sobekhotep IV, và lập luận đẩy Khyan sớm hơn trong vương triều XV. Đúng y câu "Khai quật ở Tell Edfu đã đẩy niên đại trị vì của ông sớm hơn so với niên biểu cũ".
- (e) **Thể loại** ✅ — bài tạp chí học thuật bình duyệt, đúng như atlas ghi.
- (f) **Không bị dẫn ngược luận điểm** ✅ — bài ủng hộ đúng điều được dẫn.

**Lỗi nhỏ:** tên bài đầy đủ là *"Discussion of Late Middle Kingdom and Early Second Intermediate Period History and Chronology **in Relation to the Khayan Sealings from Tell Edfu**"*. Atlas cắt mất nửa sau — chính nửa nói về Khyan. Người đọc tra theo tên bị cắt sẽ khó tìm, và dòng trích mất đúng phần chứng minh nó liên quan tới mục.

- *Đề xuất:* ghi đủ tên bài + số trang: `Nadine Moeller và Gregory Marouard, "Discussion of Late Middle Kingdom and Early Second Intermediate Period History and Chronology in Relation to the Khayan Sealings from Tell Edfu", Ägypten und Levante 21 (2011), tr. 87–121.`

Nguồn Shaw ch. 8 cũng **đúng**: ch. 8 của *The Oxford History of Ancient Egypt* (2000) là "The Second Intermediate Period (c.1650–1550 BC)" của Janine Bourriau — đúng chương cho Khyan. ✅ (Đây là ca hiếm: số chương đúng, khác hẳn mẫu +1 mà CONTRIBUTING cảnh báo — xem §6.3 cho ca ngược lại.)

### 2.5 **Sai** — liên kết `Ảnh hưởng tới: CH01-BCE17_15-03 · phản bác · trực tiếp` là nghịch niên đại

Đích đã mở đọc tên: `CH01-BCE17_15-03` = **Ahmose I** ✅ đúng người. Nhưng quan hệ thì sai:

- Khyan: *floruit* k. 1700–1580 TCN (muộn nhất k. 1580).
- Ahmose I: `năm: k. 1560–1525 TCN` — **sinh sau khi Khyan đã chết**, theo chính trường `năm:` của hai mục trong atlas.

Hai người **chưa từng cùng sống**. Ahmose I đánh đuổi **Apophis và Khamudi**, không phải Khyan. Mức bằng chứng `trực tiếp` giữa họ là không thể.

Đây đúng là lỗi CONTRIBUTING #8: lint quét đối xứng và nghịch niên đại, nhưng chỉ bắt khi người tác động sinh sau khi người kia đã mất — ở đây chiều là Khyan → Ahmose nên "đúng thứ tự", lint im. Lỗi cùng tồn tại ở cả hai đầu: mục -03 ghi `Kế thừa từ: CH01-BCE17_15-02 · phản bác · trực tiếp`.

- *Đề xuất:* hạ mức bằng chứng xuống `qua trường phái` ở **cả hai mục** (-02 và -03), hoặc chuyển đích sang "Vương triều Hyksos ở Avaris" thay vì cá nhân Khyan. Nếu muốn giữ một quan hệ cá nhân `trực tiếp` thì đối thủ đúng của Ahmose I là Khamudi, người không có mục trong atlas.

### 2.6 §5 "ứng viên bị loại" — hợp lệ nhưng chữ "cùng giai đoạn" che một lệch niên đại

> "Ứng viên cùng giai đoạn là Apophis, vua Hyksos cuối cùng, và Nehesy."

- **Apophis** — k. 1590–1550 TCN. Khyan mất muộn nhất k. 1580. Chồng lấn mỏng hoặc không có; "cùng giai đoạn" (chứ không phải "cùng thời") là cách diễn đạt đã né được, chấp nhận được.
- **Nehesy** — vua vương triều XIV, k. 1700 TCN. Cùng giai đoạn ✅.
- Cả hai **không có mục riêng** trong atlas (đã kiểm toàn bộ `### ` của `content/ch0*.md` + `ch90.md`) ✅ — không vi phạm CONTRIBUTING #6.

Không có lỗi chặn, nhưng nên nêu rõ niên đại hai ứng viên như các mục khác của chapter đã làm.

---

## 3. `CH01-BCE17_15-03` · Ahmose I

### 3.1 Phần sự kiện — **đúng** ✅

- "chiếm Avaris, đuổi người Hyksos khỏi Ai Cập rồi truy kích tới Sharuhen ở nam Canaan" ✅
- "lập vương triều XVIII và mở Tân vương quốc" ✅
- "Kamose, anh ông" ✅ (quan hệ anh em là cách hiểu thông dụng); "Ahhotep, mẹ ông" ✅
- "Tiểu sử khắc trong mộ của người lính Ahmose con bà Ibana" ✅ — mộ ở El-Kab, đúng như dòng Nguồn ghi.
- `năm: k. 1560–1525 TCN` khớp Wikidata Q7222 (−1560 / −1525), sai số 0 ✅ (dung sai Trung bình ±25).
- Nguồn Shaw ch. 9 ✅ — ch. 9 là "The Eighteenth Dynasty before the Amarna Period (c.1550 BC)" của Betsy M. Bryan, đúng chương.

### 3.2 **Nghi vấn** — quy toàn bộ bước ngoặt đế chế về một quyết định của ông

> "Thay đổi có hệ quả dài nhất là về học thuyết: thay vì giữ biên giới, Ai Cập **từ đây** duy trì quân thường trực và vùng đệm ở Levant"

và

> "chính việc truy kích sang Sharuhen chứ không dừng ở biên giới là chỗ rẽ sang chính sách đế chế, và **việc đó thuộc về quyết định của ông**"

Vây Sharuhen là một chiến dịch **trừng phạt truy kích**, không phải việc lập vùng đệm có quản trị. Hệ chư hầu Levant có cơ cấu — biên giới tới Euphrates, chư hầu nộp cống, con tin ở Thebes — là sản phẩm của **Thutmose I và Thutmose III**, tức một tới ba đời sau. Mâu thuẫn nội bộ: chính mục `-05` của atlas viết rằng "hệ chư hầu kèm nuôi con tin là mô hình cai trị gián tiếp **ông [Thutmose III] dựng**". Hai mục cùng nhóm đang trao cùng một sáng kiến cho hai người.

- *Câu thay thế đề xuất (cho -03):* "Hệ quả dài nhất là tiền lệ: Ai Cập lần đầu đưa quân vượt biên giới đông bắc để truy kích chứ không chỉ phòng thủ. Cơ cấu chư hầu và vùng đệm có quản trị ở Levant thì phải tới Thutmose I và Thutmose III mới thành hình."
- Và sửa "việc đó thuộc về quyết định của ông" thành "quyết định không dừng ở biên giới là của ông; phần xây dựng thiết chế thì thuộc các đời sau."

### 3.3 **Sai** (kế thừa từ §2.5) — `Kế thừa từ: CH01-BCE17_15-02 · phản bác · trực tiếp`

Xem §2.5. Ahmose I sinh k. 1560 TCN, Khyan mất muộn nhất k. 1580 TCN — **không chồng lấn**. Đối thủ Hyksos của Ahmose I là Apophis và Khamudi. Mức `trực tiếp` phải hạ.

### 3.4 §5 — hợp lệ ✅

Kamose và Ahhotep: cùng thời thật (cùng gia tộc, cùng thế hệ/đời trước sát), và **không ai có mục riêng** trong atlas. Không vi phạm CONTRIBUTING #5 hay #6.

---

## 4. `CH01-BCE17_15-04` · Hatshepsut

### 4.1 Phần sự kiện — **đúng** ✅

- "nhiếp chính cho con chồng" ✅ — Thutmose III là con riêng của chồng bà (Thutmose II).
- "tạc mình với râu giả và trang phục vua" ✅
- "khắc trình thuật thần Amun là cha ruột" ✅ — phù điêu "divine birth" ở Deir el-Bahari.
- "đền tang ở Deir el-Bahari với ba tầng hiên cột" ✅ — Djeser-Djeseru, ba sân thềm.
- "Phù điêu… ghi chuyến đi Punt: cây hương, khỉ, người và nhà sàn" ✅ — cây trầm hương, khỉ đầu chó, dân Punt, nhà sàn.
- `năm: k. 1507–1458 TCN` khớp Wikidata Q129234 (−1507 / −1458) sai số 0 ✅

### 4.2 **Thể thức — lỗi nặng, đúng mẫu CONTRIBUTING #6**: nêu Thutmose III làm "ứng viên cùng thời" trong khi ông **đã được chọn ngay mục kế tiếp**

> "Ứng viên cùng thời là Senenmut… và **Thutmose III**, người cùng mang danh hiệu vua với bà."

Thutmose III có mục riêng: `CH01-BCE17_15-05`, **cùng nhóm, ngay bên dưới**. Câu văn tự mâu thuẫn — **không có đánh đổi nào xảy ra**, cả hai đều được chọn. Đây chính xác là lỗi mà CONTRIBUTING #6 mô tả ("mục Tần Thủy Hoàng nêu Lý Tư… tất cả đều có mục riêng").

Nghiêm trọng hơn vì **lỗi đối xứng**: mục `-05` cũng nêu Hatshepsut làm "ứng viên cùng thời" (xem §5.4). Hai mục liền nhau nêu nhau làm ứng viên bị loại, trong khi cả hai đều nằm trong atlas. Một người rà qua loa sẽ thấy cả hai đoạn "có nêu đích danh" và cho qua.

Senenmut thì hợp lệ ✅ — cùng thời, không có mục riêng.

- *Câu thay thế đề xuất:* "Ứng viên cùng thời là Senenmut, quan quản lý và có thể là kiến trúc sư đền Deir el-Bahari, và Ineni, kiến trúc sư hoàng gia của ba đời vua trước. Thutmose III cùng mang danh hiệu vua với bà nhưng **có mục riêng ở `CH01-BCE17_15-05` nên không phải ứng viên bị loại**."

### 4.3 **Thiếu** — nguồn thứ cấp duy nhất là một tiểu sử phổ thông mang tính suy đoán

> **Nguồn:** Kara Cooney, *The Woman Who Would Be King* (2014); phù điêu Punt, đền Deir el-Bahari.

Kiểm thể loại (CONTRIBUTING #7 yêu cầu kiểm **thể loại**, không chỉ chủ đề):
- (a) Có thật ✅ — Kara Cooney, Oneworld / Crown, 2014.
- (b) Đúng năm ✅
- (c) Có bàn tới Hatshepsut ✅ — là tiểu sử về chính bà.
- (d) **Thể loại: không khớp với cách dùng.** Đây là **tiểu sử phổ thông mang tính suy đoán (speculative biography)**, không phải chuyên khảo. Giới điểm sách nhất quán gọi nó vậy; chính tác giả nói rõ phần lớn là suy luận, và bản thân sách bị phê là dùng khung nữ quyền hiện đại để giải thích động cơ. Dùng nó làm **nguồn thứ cấp duy nhất** cho một mục mà luận điểm trung tâm là *chiến lược chính danh* (một luận điểm diễn giải, đúng chỗ Cooney suy đoán nhiều nhất) là chỗ yếu nhất về nguồn của cả nhóm.

Mục này cũng là mục **duy nhất trong 4 mục Ai Cập** của nhóm **không dẫn Shaw (2000)** — trong khi ch. 9 của Shaw (Bryan) phủ đúng triều đại của bà và đã được -03 và -05 dùng.

- *Đề xuất:* `Ian Shaw (chủ biên), The Oxford History of Ancient Egypt (2000), ch. 9; phù điêu Punt và phù điêu thần sinh, đền Deir el-Bahari.` — giữ Cooney thì nên ghi rõ thể loại: `Kara Cooney, The Woman Who Would Be King (2014) — tiểu sử phổ thông, phần diễn giải động cơ là suy đoán của tác giả.`

### 4.4 **Nghi vấn** — mệnh đề tối cao "được ghi chép đầy đủ nhất… ở Cận Đông cổ" không quy thuộc

> "bà là trường hợp **được ghi chép đầy đủ nhất** về một phụ nữ nắm trọn vương quyền ở Cận Đông cổ"

Mệnh đề này mainstream và có lẽ đúng, nhưng **không quy thuộc cho ai**. Các ứng viên đối chiếu tồn tại (Sobekneferu cuối vương triều XII, Twosret cuối vương triều XIX, Kubaba ở Kish), nên nó là một phán đoán so sánh cần người đứng tên.

- *Đề xuất:* "…bà là phụ nữ nắm trọn vương quyền mà tư liệu còn lại nhiều hơn bất kỳ trường hợp nào khác ở Ai Cập cổ — Sobekneferu trước bà và Twosret sau bà đều chỉ còn vài mảnh."

### 4.5 Liên kết — đích đúng người ✅

- `Kế thừa từ: CH01-BCE17_15-03` = Ahmose I ✅ (chắt của ông; mất 1525 trước khi bà sinh 1507 → `qua trường phái` là mức đúng).
- `Ảnh hưởng tới: CH01-BCE17_15-05` = Thutmose III ✅, `trực tiếp` ✅ (đồng trị thật).

---

## 5. `CH01-BCE17_15-05` · Thutmose III

### 5.1 "Mười bảy chiến dịch" — **đúng số** ✅

Con số 17 chiến dịch ở Syria–Palestine là con số chuẩn trong tài liệu Ai Cập học. ✅

**Lưu ý kèm theo (Thiếu, nhỏ):** Biên niên ở Karnak **không** chép đủ 17 — bản khắc mô tả chi tiết **14 chiến dịch**. Mục nêu "mười bảy chiến dịch" ngay cạnh "được khắc chi tiết trong Biên niên ở Karnak", nên người đọc dễ hiểu là Biên niên chép cả 17. Thêm mấy chữ là xong.

- *Đề xuất:* "Mười bảy chiến dịch của ông (Biên niên ở Karnak chép chi tiết mười bốn trong số đó)…"

### 5.2 Megiddo 1457 TCN — **con số đúng theo niên biểu đang dùng** ✅, nhưng nên ghi biên

1457 TCN là mốc thông dụng (năm trị vì thứ 23). Các xuất bản khác đặt trận này ở **1482** hoặc **1479 TCN** tuỳ niên biểu. Mục ghi "năm 1457 TCN" trần trụi, trong khi Ghi chú biên tập của chapter lại dặn "mọi con số trước năm 1400 TCN… nên đọc như vị trí tương đối". Không sai, nhưng lệch với nguyên tắc chapter tự đặt.

- *Đề xuất:* "trận Megiddo năm 1457 TCN (các niên biểu khác cho 1482 hoặc 1479)".

### 5.3 **Nghi vấn** — hai mệnh đề tối cao trong cùng một mục, một cái có phản ví dụ nặng

**(a) "đây là trận đánh sớm nhất còn lại một tường thuật đủ để dựng lại diễn biến"**

Đây là phát biểu mainstream (thường gặp dưới dạng "trận đánh đầu tiên được ghi chép với mức chi tiết tương đối đáng tin"), nhưng trong atlas nó **không quy thuộc cho ai** — tức vi phạm nguyên tắc trung lập.

Phản ví dụ cần nói tới, và nó nằm **ngay trong nhóm này**: **bia Kamose và bảng Carnarvon** (k. 1542 TCN, sớm hơn Megiddo ~85 năm) chép một chiến dịch với tuyến hành quân, các thị trấn bị hạ, bức thư chặn được giữa Apophis và vua Kush, và lý do rút quân — **"văn bản quân sự chi tiết nhất còn lại của Ai Cập trước Tân vương quốc"**. Chính mục `-03` của atlas nêu Kamose làm ứng viên, nên atlas biết tới ông mà không đối chiếu.

Phân biệt cứu được mệnh đề: Megiddo còn lại chi tiết **chiến thuật của một trận** (họp bàn chọn lối đi, thế trận, vây thành), còn Kamose là tường thuật **chiến dịch**. Nhưng phân biệt ấy phải được viết ra thì câu mới đứng được.

- *Câu thay thế đề xuất:* "…thường được coi là trận đánh sớm nhất mà diễn biến chiến thuật — chứ không chỉ kết quả chiến dịch — còn dựng lại được; bia Kamose sớm hơn tám mươi năm nhưng chép chiến dịch chứ không chép thế trận."

**(b) "Biên niên Karnak là nguồn quân sự chi tiết sớm nhất của nhân loại" — Sai, và mâu thuẫn với chính atlas**

Phản ví dụ dứt khoát: **văn khố Mari** dưới thời Zimri-Lim (trị vì k. 1775–1761 TCN) — **sớm hơn Biên niên Karnak khoảng 300 năm** — gồm thư từ giữa vua và các tướng, báo cáo của sứ giả và do thám, quân số cụ thể (có lá ghi Hammurabi gửi 10.000 quân), việc điều chuyển quân giữa các nước. Khoảng hai mươi nghìn phiến.

Mâu thuẫn nội bộ nặng: **chính atlas chọn Zimri-Lim (`CH01-BCE20_18-05`) và Shamshi-Adad I (`CH01-BCE20_18-04`) đúng vì kho tư liệu ấy**, và mục Zimri-Lim viết: *"Văn khố Mari ghi thư ngoại giao, danh sách khẩu phần, hợp đồng, báo cáo của sứ giả… điều không nguồn nào khác cùng thời làm được ở quy mô ấy."* Hai mục của cùng một chapter đang tranh nhau một ngôi "sớm nhất".

- *Câu thay thế đề xuất:* "…còn Biên niên Karnak là tường thuật chiến dịch do chính nhà nước khắc công khai, chi tiết nhất của Ai Cập và một trong những nguồn quân sự tường thuật đầy đủ nhất của thiên niên kỷ 2 TCN." (bỏ hẳn "sớm nhất của nhân loại")

### 5.4 **Thể thức — lỗi đối xứng với §4.2**: nêu Hatshepsut làm "ứng viên cùng thời"

> "Ứng viên cùng thời là **Hatshepsut**, người cùng mang danh hiệu vua trong hai mươi năm đầu, và Amenhotep II, con ông."

Hatshepsut có mục riêng `CH01-BCE17_15-04`, **ngay mục trên**. Vi phạm CONTRIBUTING #6, y như §4.2 — và vì hai mục nêu nhau nên lỗi này sinh đôi.

Amenhotep II hợp lệ ✅ (không có mục riêng; được nêu trong danh sách bị loại ở Ghi chú biên tập).

- *Câu thay thế đề xuất:* "Ứng viên cùng thời là Amenhotep II, con ông, người kế tục các chiến dịch Levant, và Tjaneni, viên thư lại quân vụ đã chép Biên niên. Hatshepsut cùng mang danh hiệu vua trong hai mươi năm đầu nhưng **có mục riêng ở `CH01-BCE17_15-04` nên không phải ứng viên bị loại**."

### 5.5 **Nghi vấn** — "hệ chư hầu kèm nuôi con tin là mô hình cai trị gián tiếp ông dựng"

Việc đưa con các thủ lĩnh chư hầu về Thebes nuôi dạy **có thật và được chép trong Biên niên** ✅. Nhưng chữ "**ông dựng**" là quy nguyên bản cho một cá nhân, trong khi cấu trúc chư hầu Levant hình thành dần từ Thutmose I. Xem thêm mâu thuẫn ở §3.2: mục `-03` trao cùng sáng kiến ấy cho Ahmose I ("Ai Cập từ đây duy trì… vùng đệm ở Levant").

- *Đề xuất:* "…hệ chư hầu kèm nuôi con tin đạt hình thái đầy đủ dưới tay ông và Ai Cập dùng suốt Tân vương quốc."

### 5.6 Nguồn — **đúng cả bốn tiêu chí** ✅

> Donald B. Redford, *The Wars in Syria and Palestine of Thutmose III* (2003)

- (a) Có thật ✅ — Brill, Leiden, 2003, *Culture and History of the Ancient Near East* vol. 16, ISBN 9789004129894.
- (b) Đúng năm ✅
- (c) Có bàn tới điều được dẫn ✅ — Phần Một là bản đối chiếu mới của **chính Biên niên** kèm chú giải; Phần Hai là bản dịch các nguồn bổ trợ; kết bằng bình luận lịch sử. Đúng chỗ atlas dẫn.
- (d) Thể loại ✅ — chuyên khảo học thuật, không phải bản dịch hay sách phổ thông; atlas không ghi sai thể loại.
- Không bị dẫn ngược luận điểm ✅.

`Biên niên Thutmose III, đền Karnak` — nguồn sơ cấp, ghi đúng ✅.

### 5.7 Liên kết — đích đúng người ✅

- `Kế thừa từ: CH01-BCE17_15-04` = Hatshepsut ✅, `trực tiếp` ✅
- `Kế thừa từ: CH01-BCE17_15-03` = Ahmose I ✅, `qua trường phái` ✅ (mất 1525, Thutmose III sinh 1481 → không chồng lấn, mức đúng)
- `Ảnh hưởng tới: CH01-BCE14_12-06` = **Ramesses II** ✅ đúng người, đúng chiều niên đại (k. 1303–1213 TCN), `qua trường phái` ✅

---

## 6. `CH01-BCE17_15-06` · Mursili I

### 6.1 Phần sự kiện — **đúng gần như toàn bộ** ✅

Đối chiếu trực tiếp với bản PDF Bryce (2005) đã tải và trích văn bản:

| Khẳng định trong atlas | Kiểm | Kết quả |
|---|---|---|
| `năm: trị vì k. 1620–1590 TCN` | Bryce, bảng "Hittite Kings": "Mursili I **1620–1590** (grandson, adopted son)" | ✅ khớp chính xác |
| "chiếm Aleppo rồi… đánh vào Babylon khoảng năm 1595 TCN" | Bryce: "the Hittite offensive must have taken place around the time of his [Samsuditana's] death, dated to c.1595 on the basis of the so-called Middle Chronology" | ✅ |
| "chấm dứt vương triều của Hammurabi" | Bryce: "the demise of the dynasty of Hammurabi, thus bringing to an end an illustrious era in Babylon's history" | ✅ |
| "không nhằm chiếm đóng — ông rút ngay" | Bryce: "He could not have hoped to convert the entire region from Aleppo to Babylon into Hittite subject territory… would have made such a prospect unthinkable" | ✅ |
| "mở đường cho người Kassite cai trị Babylon hơn bốn thế kỷ" | Bryce: "his conquest paved the way for the eventual establishment of a Kassite dynasty in Babylonia" | ✅ (triều Kassite k. 1595–1155 ≈ 440 năm) |
| "bị **em rể** ám sát khi trở về" | Bryce: "The assassin was his brother-in-law Hantili, husband of his sister Harapsili" | ✅ đúng cả quan hệ (chồng của em/chị gái) |
| "Hattusili I, **cha nuôi** ông" | Bryce: Mursili I là "grandson, adopted son" của Hattusili I | ✅ chấp nhận được |

Đây là mục chắc nhất của nhóm về mặt sự kiện.

### 6.2 **Thiếu** — con số "hơn tám trăm cây số" không quy thuộc

Khoảng cách Aleppo → Babylon là chừng 700 km đường chim bay, dài hơn nếu đi dọc Euphrates — nên "hơn tám trăm cây số" nằm trong biên hợp lý, nhưng **không nguồn nào trong mục đưa ra con số này**. Theo CONTRIBUTING #3 (tinh thần: đừng ghi con số chưa tra), nên hoặc bỏ con số hoặc ghi "hơn bảy trăm cây số đường chim bay".

### 6.3 **Sai** — số chương Bryce lệch: atlas ghi **ch. 4**, đúng là **ch. 5**

> **Nguồn:** Trevor Bryce, *The Kingdom of the Hittites* (2005), **ch. 4**; Sắc lệnh Telipinu.

Đã mở mục lục bản PDF (bản 2005, new edition):

- **Ch. 4** — "The Foundations of the Kingdom: The Reigns of **Labarna and Hattusili I** (–c.1620)", tr. 61
- **Ch. 5** — "The Struggles for the Royal Succession: **From Mursili I to Muwattalli I** (c.1620–1400)", tr. 96

Mursili I, chiến dịch Aleppo–Babylon, vụ ám sát của Hantili và Sắc lệnh Telipinu đều nằm ở **ch. 5**. Ch. 4 dừng trước khi Mursili lên ngôi.

Đây đúng loại lỗi CONTRIBUTING #3 cảnh báo (số chương sinh ra chứ không tra cứu), chỉ khác dấu: lệch **−1** thay vì +1. Theo tinh thần mục ấy, một số chương sai làm hỏng cả dòng Nguồn.

- *Câu thay thế đề xuất:* `Trevor Bryce, The Kingdom of the Hittites (2005), ch. 5 ("The Struggles for the Royal Succession: From Mursili I to Muwattalli I"); Sắc lệnh Telipinu.`

Phần còn lại của nguồn **đạt cả bốn tiêu chí**: sách có thật ✅, đúng năm (OUP, bản mới 2005) ✅, có bàn tới điều được dẫn ✅, thể loại đúng (chuyên khảo học thuật) ✅, không bị dẫn ngược luận điểm ✅. *Sắc lệnh Telipinu* là nguồn sơ cấp đúng — chính nó chép câu "Zidanta âm mưu với Hantili… Họ giết Mursili" mà Bryce dẫn.

### 6.4 **Thể thức** — Telipinu không cùng thời, và mục chỉ nói lướt

> "Ứng viên cùng nhà là Hattusili I, cha nuôi ông, người khởi cuộc nam tiến, và **Telipinu, người về sau ban sắc lệnh kế vị**."

Theo bảng vua của Bryce: Mursili I 1620–1590; **Telipinu 1525–1500** — cách nhau **65–90 năm**, qua bốn đời vua trung gian (Hantili I, Zidanta I, Ammuna, Huzziya I). Không cùng thời.

Mục có dùng chữ "về sau", nên không hoàn toàn che giấu — nhẹ hơn ca Hạ Vũ ở §1.3. Nhưng §5 đòi ứng viên **cùng thời**, và cách viết "Ứng viên cùng nhà là A… và B" gộp một người cùng thời với một người cách gần một thế kỷ vào cùng một mệnh đề. Cả hai **không có mục riêng** trong atlas ✅ (không vi phạm #6).

- *Câu thay thế đề xuất:* "Ứng viên cùng thời là Hattusili I, cha nuôi ông, người khởi cuộc nam tiến, và Hantili I, kẻ ám sát rồi kế vị ông. Telipinu, người ban sắc lệnh kế vị, ở cách gần một thế kỷ nên không phải ứng viên cùng thời."

### 6.5 Liên kết — đích đúng người ✅

- `Ảnh hưởng tới: CH01-BCE14_12-01` = **Suppiluliuma I** ✅ đúng người (vua Hatti, k. 1350–1322 TCN), đúng chiều, `qua trường phái` là mức đúng cho khoảng cách 240 năm.
- `Kế thừa từ: Hattusili I · kế thừa · trực tiếp` ✅ — hai người thật sự chồng lấn.

### 6.6 Ghi chú rìa (ngoài 8 mục, nhưng thuộc ghi chú của -06)

Ghi chú biên tập viết: *"Mốc Babylon sụp… có thể là 1595, 1531 hoặc 1499 TCN… chênh gần một thế kỷ."* Bryce liệt kê **bốn** giá trị: **1651**, 1595, 1531, 1499 — tức biên là **152 năm**, không phải "gần một thế kỷ". Nhỏ, nhưng là chỗ con số bị thu hẹp so với nguồn chính của mục.

---

## 7. `CH01-BCE17_15-07` · Ahmes

### 7.1 Bài 50 và giá trị pi — **đúng cả công thức lẫn con số** ✅

> "Cách tính diện tích hình tròn ở bài 50, lấy bình phương của tám phần chín đường kính, tương đương một giá trị xấp xỉ cho số pi quanh 3,16."

- **Công thức ✅** — Bài 50 của giấy cói Rhind: ruộng tròn đường kính 9 khet, diện tích 64 setat; quy tắc là diện tích = (8/9 × đường kính)². Đúng y nguyên văn atlas.
- **Con số ✅** — 4 × (8/9)² = 256/81 = **3,16049…**, tức "quanh 3,16" là đúng (sai số ~0,63 % so với π).

Đây là mục chính xác nhất về kỹ thuật trong nhóm.

### 7.2 Số hiệu Bảo tàng Anh và số bài toán — **đúng** ✅

- **EA10057–10058 ✅** — hai mảnh chính của giấy cói Rhind mang đúng số hiệu BM EA 10057 (dài 295,5 cm) và EA 10058 (dài 199,5 cm). Bản khảo dịch kinh điển của Chace (1927–29) còn lấy luôn hai số ấy làm tên sách: *The Rhind Mathematical Papyrus, British Museum 10057 and 10058*.
- **"tám mươi tư bài toán" ✅** — con số chuẩn (84), dù vài cách đánh số cho 87.
- **"chép từ một bản có từ thời Trung vương quốc" ✅** — Ahmes tự ghi trong tiêu đề rằng chép lại từ một văn bản thời Nimaatre (Amenemhat III).

### 7.3 Mệnh đề tối cao "người sớm nhất… ký tên vào một văn bản toán học" — **đứng được**, nhưng chữ "ký tên" hơi lệch

Khác với các mệnh đề tối cao khác trong nhóm, cái này **tìm không ra phản ví dụ**: Ahmes được giới sử toán coi là người có tên sớm nhất gắn với một văn bản toán học còn lại. Không một người chép Lưỡng Hà nào của thời Cổ Babylon được biết tên qua các bản toán — các phiến toán Cổ Babylon phong phú nhưng khuyết danh. ✅

Hai điều chỉnh nhỏ:
1. **"ký tên"** gợi ý chữ ký tác giả. Thực tế Ahmes tự xưng trong **tiêu đề mở đầu** là "người chép Ahmose", tức ông tự nhận là **người sao chép**, không phải tác giả — và mục có nói điều đó ở câu sau, nhưng chữ "ký tên" đứng trước làm câu tự đá nhau.
2. Nên quy thuộc, vì đây vẫn là mệnh đề tối cao: Imhausen (2016) — nguồn atlas đã dẫn — là chỗ quy thuộc sẵn có.

- *Câu thay thế đề xuất:* "…và tự xưng trong tiêu đề là 'người chép Ahmose', chép lại từ một bản thời Trung vương quốc — nên ông là cái tên sớm nhất mà giới sử toán gắn được với một văn bản toán học còn lại, dù ông tự nhận là người sao chép chứ không phải tác giả."

### 7.4 **Sai** — trường `năm:` và Ghi chú biên tập: lời giải thích **không đúng sự thật**

Mục ghi: `năm: hoạt động k. 1650–1550 TCN`.
Ghi chú biên tập giải thích: *"trường `năm:` **ghi theo biên Wikidata đưa ra**, nhưng giấy cói Rhind thường được định niên vào khoảng năm 1550 TCN theo niên hiệu Apophis ghi trên chính văn bản. Hai cách định niên chưa được dung hoà ở đây."*

**Lời giải thích này sai.** Tra Wikidata Q1073335 ngày 2026-10-31:

- P569 (sinh): **−1660**
- P570 (mất): **−1620**
- mô tả en: "Egyptian scribe and mathematician (**1680BC–1620BC**)"

Wikidata **không hề đưa ra biên 1650–1550**. Biên trong atlas không trùng Wikidata ở cả hai đầu (lệch 10 năm đầu dưới, **70 năm** đầu trên), và quan trọng hơn: **đầu trên 1550 lại chính là niên đại Apophis** mà ghi chú nói là cách định niên *kia*.

Tức trường `năm:` thực ra là một **biên lai ghép tự chế**: lấy đầu dưới gần Wikidata, đầu trên từ niên hiệu Apophis, rồi nối lại thành một "khoảng hoạt động" 100 năm mà **không nguồn nào chủ trương**. Rồi Ghi chú biên tập mô tả sai nguồn gốc của nó.

Vì `độ tin cậy niên đại: Thấp` nên lint bỏ qua đối chiếu (xác nhận ở `reports/lint-ch01.txt`: `[INFO] CH01-BCE17_15-07: độ tin cậy Thấp — bỏ qua đối chiếu niên đại`). Đây là ca sách giáo khoa của CONTRIBUTING #4: lint sạch, nội dung sai.

**Đánh giá cách xử lý hiện tại: chưa đủ.** Ghi chú biên tập có nêu *tồn tại* một mâu thuẫn — tốt hơn im lặng — nhưng nó (a) **quy sai** một trong hai đầu cho Wikidata, (b) để nguyên một biên 100 năm không ai chủ trương làm con số hiển thị, (c) nói "chưa được dung hoà" trong khi **giới nghiên cứu đã dung hoà rồi**: niên đại k. 1550 TCN theo niên hiệu năm 33 của Apophis ghi trên chính văn bản là niên đại tiêu chuẩn, và Imhausen (2016) — nguồn của chính mục — dùng mốc ấy. Đây không phải hai trường phái ngang nhau: một bên là dữ liệu Wikidata không nguồn, một bên là niên đại nội chứng của văn bản.

- *Sửa đề xuất:*
  - Trường: `năm: hoạt động k. 1550 TCN (năm 33 triều Apophis, theo niên hiệu ghi trên chính giấy cói)`
  - Ghi chú biên tập, câu thay thế: "**Ahmes (CH01-BCE17_15-07):** trường `năm:` lấy theo niên hiệu năm 33 triều Apophis ghi trên chính giấy cói Rhind, tức k. 1550 TCN — đây là niên đại tiêu chuẩn trong nghiên cứu. Wikidata (Q1073335) ghi 1660–1620 TCN không nguồn; atlas không theo con số đó, và vì độ tin cậy để Thấp nên lint bỏ qua đối chiếu."

### 7.5 Nguồn — **đạt cả bốn tiêu chí** ✅

> Annette Imhausen, *Mathematics in Ancient Egypt: A Contextual History* (2016)

- (a) Có thật ✅ — Princeton University Press, 2016.
- (b) Đúng năm ✅
- (c) Có bàn tới điều được dẫn ✅ — sách bàn giấy cói Rhind, bài 50, hệ phân số đơn vị, và chính chỗ Ahmes tự xưng "người chép Ahmose" trong tiêu đề.
- (d) Thể loại ✅ — chuyên khảo học thuật ("contextual history"), atlas không ghi sai thể loại.
- Không bị dẫn ngược ✅ — ngược lại, luận điểm trung tâm của Imhausen (đọc toán Ai Cập **trong bối cảnh hành chính** thay vì như toán học thuần tuý) lại **ủng hộ** cách mục này đặt Ahmes là "chỗ sớm nhất tri thức kỹ thuật gắn được với một cái tên".

`Giấy cói toán học Rhind, Bảo tàng Anh EA10057–10058` — nguồn sơ cấp, số hiệu đúng ✅.

### 7.6 §5 — **xử lý đúng chuẩn, nên ghi nhận** ✅

> "Không nêu được ứng viên cùng thời: không người chép Ai Cập nào khác của giai đoạn này để lại tên gắn với một văn bản toán học. Giấy cói Moskva… hoàn toàn khuyết danh."

Đây **đúng y điều CONTRIBUTING #5 dặn**: khi giai đoạn thật sự không có ai để so thì "viết thẳng là không có — đó là một phát hiện về tư liệu". Mục còn nêu đích danh vật đối chiếu (giấy cói Moskva, khuyết danh — đúng). Là mục xử lý §5 tốt nhất trong nhóm.

### 7.7 Liên kết — đích đúng người, mức bằng chứng đúng ✅

- `Ảnh hưởng tới: CH02-BCE06-05` = **Thales xứ Miletus** ✅ đúng người, `suy đoán học giả` ✅ — mức đúng cho truyền thuyết Thales học ở Ai Cập. Lint có báo thiếu chiều ngược (`[INFO] … CH02-BCE06-05 không ghi 'Kế thừa từ'`), P4 sẽ đồng bộ.

---

## 8. `CH01-BCE17_15-08` · Viśvāmitra

### 8.1 Số hiệu câu Gāyatrī — **đúng** ✅

> "trong đó có câu **3.62.10** về sau gọi là Gāyatrī"

Đúng: Gāyatrī Mantra là **Rigveda 3.62.10** — câu thứ 10 của bài tụng 62 trong Mandala 3, quy cho rishi Viśvāmitra theo truyền thống, hướng về thần Savitr (nên cũng gọi là Sāvitrī; "Gāyatrī" vốn là tên **thể thơ**). Atlas ghi "lời cầu xin ánh sáng soi trí tuệ" — sát nghĩa, chấp nhận được. ✅

### 8.2 **Nghi vấn** — "câu được đọc lại nhiều lần nhất trong lịch sử Ấn Độ" là mệnh đề tối cao **không kiểm chứng được**

> "là **câu được đọc lại nhiều lần nhất trong lịch sử Ấn Độ**, vẫn dùng hằng ngày tới nay"

**Không kiểm được** — và quan trọng hơn, **không ai kiểm được**: không tồn tại dữ liệu nào đếm số lần tụng niệm trong ba nghìn năm. Đây không phải mệnh đề tối cao *chưa* quy thuộc mà là loại mệnh đề **không quy thuộc được cho ai**, vì không có phương pháp xác lập nó. Theo nguyên tắc trung lập mà prompt §5 đặt ra ("không tô vẽ"), nó phải bị bỏ.

Các ứng viên đối chiếu hiển nhiên — "Oṃ", "Oṃ namaḥ Śivāya", Mahāmṛtyuñjaya mantra (bản thân nó cũng là Rigveda, 7.59.12) — đủ để thấy mệnh đề không đứng vững, dù không cái nào "chứng minh ngược" được.

Phần **kiểm chứng được** của câu thì đúng và đủ mạnh để thay thế: Gāyatrī là câu Rigveda nằm trong nghi thức *sandhyāvandana* hằng ngày và trong lễ *upanayana*, tức nó **được thiết chế hoá vào sinh hoạt bắt buộc** — đó là một sự kiện về thể chế, không phải một phép đếm.

- *Câu thay thế đề xuất:* "…lời cầu xin ánh sáng soi trí tuệ, được đưa vào nghi thức tụng niệm hằng ngày (sandhyāvandana) và lễ nhập môn upanayana, nên là một trong số rất ít câu Rigveda còn hiện diện liên tục trong sinh hoạt tôn giáo tới nay."

Lưu ý: câu trong **"Vì sao chọn"** — *"không câu nào khác của Rigveda có mức hiện diện liên tục như Gāyatrī"* — đã là một phiên bản **hẹp hơn và đứng được** của cùng ý. Mục tự có sẵn cách diễn đạt đúng; chỉ cần đưa nó lên thay cho câu tối cao ở phần trên.

### 8.3 **Nghi vấn** — "được kể đi kể lại suốt ba nghìn năm" và chỗ xuất xứ của trình thuật

> "ông vốn thuộc hàng chiến binh mà đạt được địa vị hiền giả… được kể đi kể lại **suốt ba nghìn năm** như một ngoại lệ có thẩm quyền"

Hai vấn đề:

1. **Trình thuật này không có trong Rigveda.** Câu chuyện kshatriya Viśvāmitra khổ tu thành brahmarṣi là của **sử thi và Purāṇa** (*Rāmāyaṇa*, *Mahābhārata*, các Purāṇa) — tức muộn hơn Mandala 3 khoảng một nghìn năm. Mục không nói ra, nên người đọc dễ hiểu là trình thuật ấy thuộc cùng tầng văn bản với câu 3.62.10 vừa nhắc ở câu trước.
2. **"Ba nghìn năm" là con số quá tay.** Tính từ khi trình thuật xuất hiện (sử thi, khoảng giữa thiên niên kỷ 1 TCN) tới nay là chừng **2.500 năm**, không phải 3.000. Con số 3.000 chỉ đúng nếu tính từ Mandala 3 — nhưng Mandala 3 không chứa câu chuyện ấy.

- *Câu thay thế đề xuất:* "Trình thuật về ông — do sử thi và Purāṇa dựng, muộn hơn Mandala 3 khoảng một nghìn năm — còn mang một luận điểm xã hội: ông vốn thuộc hàng chiến binh mà đạt được địa vị hiền giả, tức một trường hợp phá rào trong hệ thân phận, được kể lại suốt hơn hai nghìn năm như một ngoại lệ có thẩm quyền."

### 8.4 §5 — **xử lý Vasiṣṭha đúng chuẩn CONTRIBUTING #6** ✅ (và là mẫu cho §4.2/§5.4)

> "Ứng viên trong cùng tập là Vasiṣṭha, chủ Mandala 7 và **cũng được chọn riêng ở nhóm sau**, và Gritsamada."

Đây **chính xác** là cách CONTRIBUTING #6 yêu cầu: nói rõ người kia có mục riêng (`CH01-BCE14_12-12` = Vasiṣṭha ✅ đã kiểm) nên không phải ứng viên bị loại. Gritsamada (rishi của Mandala 2) không có mục riêng ✅ và được nêu trong danh sách bị loại ở Ghi chú biên tập ✅.

**Đối chiếu gay gắt:** mục này làm đúng, trong khi hai mục `-04` và `-05` của **cùng nhóm** mắc đúng lỗi ấy với nhau. Chứng tỏ tác giả biết quy tắc nhưng áp không nhất quán — nên khi sửa, chép thẳng cách diễn đạt của mục này sang -04 và -05.

### 8.5 Nhãn [Truyền thuyết] và cách tự giới hạn — **đạt** ✅

> "Nhãn [Truyền thuyết] là bắt buộc: các mandala là sáng tác tập thể của những dòng tư tế, và việc quy về một cá nhân là quy ước của truyền thống chứ không phải kết luận của nghiên cứu."

Đúng, trung thực, và lặp lại ở Ghi chú biên tập. Đây là chỗ xử lý tốt nhất về minh bạch trong cả nhóm — không có gì để phê.

### 8.6 Nguồn — **đúng cả bốn tiêu chí** ✅

> Stephanie W. Jamison và Joel P. Brereton, *The Rigveda: The Earliest Religious Poetry of India* (2014)

- (a) Có thật ✅ — Oxford University Press, bộ 3 tập, ISBN 9780199370184.
- (b) Đúng năm ✅ — 2014 (phát hành 22/5/2014).
- (c) Có bàn tới điều được dẫn ✅ — bản dịch đầy đủ Rigveda đầu tiên sang tiếng Anh kể từ Griffith (1889–92), kèm dẫn luận từng mandala; phủ Mandala 3 và 3.62.10.
- (d) **Thể loại ✅** — atlas **không** ghi sai: không gọi nó là chuyên khảo, chỉ nêu tên. Đây là bản dịch kèm chú giải — và vì mục dẫn nó cho *nội dung văn bản*, thể loại khớp đúng mục đích.
- Không bị dẫn ngược ✅.

`Rigveda, Mandala 3` — nguồn sơ cấp, ghi đúng ✅.

### 8.7 Liên kết — đích đúng người ✅

- `Ảnh hưởng tới: CH02-BCE07-03` = **Uddālaka Āruṇi** ✅ đúng người (hiền giả Upaniṣad, TK 7 TCN), đúng chiều, `qua trường phái` ✅.
- `Ảnh hưởng tới: Truyền thống tụng Gāyatrī trong Ấn giáo · kế thừa · trực tiếp` ✅ hợp lý.

---

## 9. Tổng hợp phát hiện

### 9.1 Bảng

| # | Mục | Loại | Tóm tắt |
|---|---|---|---|
| 1 | Bối cảnh | Nghi vấn | "nhà Thương thay nhà Hạ" phát biểu nhà Hạ như sự kiện đã xác lập, ngược với Ghi chú biên tập của chính chapter |
| 2 | -01 | **Sai** | "nhân vật sớm nhất Đông Á vừa có trình thuật truyền thống vừa có tên trong tư liệu đương thời" — phản ví dụ: Vương Hợi (130+ khắc giáp cốt), Thượng Giáp |
| 3 | -01 | **Sai** | "tư liệu đương thời" — giáp cốt bắt đầu từ Vũ Đinh, **sau Thành Thang ~350 năm** |
| 4 | -01 | Thể thức | Hạ Vũ nêu làm ứng viên nhưng sớm hơn 400 năm và ngoài phạm vi atlas; mục không nói ra (CONTRIBUTING #5) |
| 5 | -01 | Nghi vấn | Liên kết → Chu Công Đán là lập luận vòng: hình tượng Thành Thang nhận lỗi do thư tịch Chu dựng |
| 6 | -02 | Nghi vấn | Sư tử Baghdad **không có xuất xứ khai quật**, nhiều khả năng gốc Levant; chữ "tức" biến nó thành kết luận về mạng thương mại |
| 7 | -02 | Thiếu | Bỏ sót hiện vật thứ ba ở **Hattusa** — chỗ nối với mục -06 cùng nhóm |
| 8 | -02 | **Sai**/Thể thức | `trị vì k. 1700–1600 TCN` = một triều đại 100 năm; đọc nhầm P569/P570 thô của Wikidata thành niên đại trị vì |
| 9 | -02 | Thiếu | Tên bài Moeller & Marouard bị cắt mất nửa nói về Khyan (nguồn **có thật, đúng năm, đúng tạp chí, đúng nội dung, đúng thể loại** ✅) |
| 10 | -02, -03 | **Sai** | `Khyan ↔ Ahmose I · phản bác · trực tiếp` — hai người **chưa từng cùng sống** (Ahmose sinh k.1560, Khyan mất muộn nhất k.1580). CONTRIBUTING #8 |
| 11 | -03 | Nghi vấn | Quy toàn bộ bước ngoặt đế chế về quyết định của Ahmose I; mâu thuẫn với -05 vốn trao cùng sáng kiến cho Thutmose III |
| 12 | **-04** | **Thể thức (nặng)** | Nêu **Thutmose III** làm "ứng viên cùng thời" — ông có mục riêng `-05` **ngay bên dưới**. CONTRIBUTING #6 |
| 13 | -04 | Thiếu | Nguồn thứ cấp duy nhất là **tiểu sử phổ thông mang tính suy đoán** (Cooney 2014), dùng cho đúng luận điểm diễn giải nhất của mục |
| 14 | -04 | Nghi vấn | "được ghi chép đầy đủ nhất… ở Cận Đông cổ" — mệnh đề tối cao không quy thuộc |
| 15 | -05 | Thiếu | "mười bảy chiến dịch" đúng ✅ nhưng Biên niên Karnak chỉ chép chi tiết **14**; đặt cạnh nhau gây hiểu nhầm |
| 16 | -05 | Nghi vấn | "trận đánh sớm nhất còn lại tường thuật đủ dựng lại diễn biến" — mainstream nhưng không quy thuộc; bia Kamose (k.1542) sớm hơn ~85 năm |
| 17 | **-05** | **Sai** | "Biên niên Karnak là **nguồn quân sự chi tiết sớm nhất của nhân loại**" — văn khố Mari sớm hơn ~300 năm; **mâu thuẫn với mục Zimri-Lim của chính atlas** |
| 18 | **-05** | **Thể thức (nặng)** | Nêu **Hatshepsut** làm "ứng viên cùng thời" — bà có mục riêng `-04`. Lỗi đối xứng với #12 |
| 19 | -05 | Nghi vấn | "hệ chư hầu kèm nuôi con tin là mô hình **ông dựng**" — xung đột với -03 |
| 20 | **-06** | **Sai** | Số chương Bryce: atlas ghi **ch. 4**, Mursili I nằm ở **ch. 5**. CONTRIBUTING #3 (lệch −1) |
| 21 | -06 | Thiếu | "hơn tám trăm cây số" không nguồn |
| 22 | -06 | Thể thức | Telipinu (1525–1500) cách Mursili I 65–90 năm, không cùng thời |
| 23 | -06 | Thiếu | Ghi chú biên tập nói biên niên đại Babylon "gần một thế kỷ"; Bryce cho **bốn** giá trị 1651/1595/1531/1499 = **152 năm** |
| 24 | **-07** | **Sai** | Ghi chú biên tập nói `năm:` "ghi theo biên Wikidata" — **Wikidata ghi 1660–1620**, không phải 1650–1550. Trường `năm:` là biên tự ghép không nguồn nào chủ trương |
| 25 | -07 | Nghi vấn | "ký tên" gợi ý tác giả; Ahmes tự xưng là **người chép** (mệnh đề tối cao thì **đứng được** ✅) |

**Tổng: 25 phát hiện — 8 Sai · 9 Nghi vấn · 8 Thiếu/Thể thức** (một số mục xếp kép).

### 9.2 Những gì đã kiểm và **đúng** (ghi nhận để không phải kiểm lại)

- **8/8 Q-ID trỏ đúng người.**
- Đại Ất = Thành Thang trên giáp cốt: **đúng và đã xác lập**.
- Nắp bình Khyan ở Knossos: **đúng**.
- Moeller & Marouard, *Ägypten und Levante* 21 (2011): **có thật, đúng năm, đúng tạp chí, đúng nội dung, đúng thể loại, không dẫn ngược** — chỉ cụt tên.
- Shaw (2000) **ch. 8** cho Khyan và **ch. 9** cho vương triều XVIII: **cả hai số chương đúng**.
- Thutmose III **17 chiến dịch**: đúng. Megiddo **1457 TCN**: đúng theo niên biểu đang dùng.
- Redford (2003): **đúng cả bốn tiêu chí**, đúng cả thể loại (chuyên khảo).
- Mursili I: niên đại trị vì, năm 1595, "rút ngay", khoảng trống Kassite, **bị em rể Hantili ám sát** — **toàn bộ khớp Bryce nguyên văn**.
- Ahmes: **bài 50 = (8/9 × đường kính)²**, **π ≈ 3,1605 ≈ 3,16**, **84 bài toán**, **EA10057–10058** — **tất cả đúng**.
- Ahmes là người có tên sớm nhất gắn với văn bản toán học: **không tìm ra phản ví dụ**, mệnh đề đứng được.
- Imhausen (2016), Jamison & Brereton (2014): **đúng cả bốn tiêu chí**.
- **Gāyatrī = RV 3.62.10**: đúng.
- Xử lý §5 ở **-07** (nói thẳng là không có ứng viên) và **-08** (nói rõ Vasiṣṭha có mục riêng): **đúng chuẩn**, nên dùng làm mẫu sửa cho -04 và -05.

---

## 10. Đánh giá lựa chọn nhân vật

Nhóm có **8/12 suất** — còn **4 chỗ trống**, nên các đề xuất dưới đây **không đòi loại ai**. Đã đối chiếu với toàn bộ danh sách bị loại ở `## Ghi chú biên tập` của Ch1 (Amenhotep II, Kamose, Ahhotep, Senenmut, Puduhepa, Tushratta, Mursili II, Y Doãn, Bàn Canh, Bharadvāja, Gritsamada, Tutankhamun, Hạ Vũ) và với các tên nêu trong "Vì sao chọn" của 8 mục (Apophis, Nehesy, Hattusili I, Telipinu).

### 10.1 Lỗ hổng cấu trúc: **Lưỡng Hà biến mất, và Mitanni chưa bao giờ xuất hiện**

Nhóm BCE17_15 phủ Ai Cập (5), Anatolia (1), Đông Á (1), Nam Á (1). **Lưỡng Hà — vùng để lại nhiều văn bản nhất giai đoạn này — không có mục nào.** Nhóm liền trước (BCE20_18) dành 3/6 suất cho Lưỡng Hà (Hammurabi, Shamshi-Adad I, Zimri-Lim); tới nhóm này nó rơi về 0, không một dòng giải thích. Lý do "không có chữ viết" mà Ghi chú biên tập dùng cho châu Mỹ hay Đông Nam Á **không áp dụng được ở đây**.

Tương tự, **Mitanni** — một trong các cường quốc lớn của Hậu kỳ Đồ đồng, đối thủ chính của Ai Cập ở bắc Syria trong chính giai đoạn Thutmose III — **không xuất hiện ở bất kỳ đâu trong Ch1**, kể cả danh sách bị loại. (Tushratta có trong danh sách bị loại nhưng ông thuộc TK 14, tức nhóm sau.) Mục `-05` viết Thutmose III "đưa quyền kiểm soát Ai Cập tới Euphrates" mà không nói ông đẩy lùi ai.

### 10.2 Ứng viên đáng có mặt mà **chưa từng được cân nhắc**

**(1) Ammi-ṣaduqa của Babylon (trị vì k. 1646–1626 TCN) — đề xuất mạnh nhất**

- **Vì sao mạnh:** "Phiến Kim Tinh của Ammi-ṣaduqa" chép quan sát mọc–lặn của Kim Tinh suốt **21 năm** kể từ năm đầu triều ông. Đây là **bộ ghi chép thiên văn có hệ thống sớm nhất còn lại của nhân loại**, và là **dữ liệu nền của toàn bộ niên biểu tuyệt đối Cận Đông**: bốn niên biểu High / Middle / Low / Ultra-Low (khởi điểm 1702 / 1646–1638 / 1582 / 1550 TCN) đều là bốn cách đọc **cùng một phiến đất sét này**.
- **Counterfactual (d) rất rõ**, và mang tính tự quy chiếu đáng chú ý: **chính chapter này phụ thuộc vào ông**. Ghi chú biên tập viết "Niên đại tuyệt đối của cả nửa đầu chapter phụ thuộc vào tranh luận niên biểu cao–thấp" và "Mốc Babylon sụp… có thể là 1595, 1531 hoặc 1499 TCN" — cả ba con số ấy **sinh ra từ phiến của Ammi-ṣaduqa**. Bryce (nguồn của mục `-06`) nói thẳng điều đó. Atlas dùng dữ liệu của ông ở ít nhất 5 mục mà không một lần nhắc tên ông.
- **Lĩnh vực:** Khoa học tự nhiên (+ Chính trị/Nhà nước). **Vùng:** Trung Đông/Bắc Phi. Lấp đúng khoảng trống Lưỡng Hà **và** khoảng trống lĩnh vực: nhóm hiện không có mục Khoa học tự nhiên nào.
- **Phản biện công bằng:** ông là vua được ghi công cho một văn bản do các nhà quan sát trong triều lập, giống hệt ca Zimri-Lim ở `BCE20_18-05` — mà atlas đã chấp nhận logic ấy và nói thẳng: *"Đây là mục được chọn vì cái ông để lại, không vì cái ông làm."* Tiền lệ có sẵn trong chính Ch1.
- *Nguồn khởi đầu:* Wikipedia "Venus tablet of Ammisaduqa"; Bryce (2005), Appendix 1 "Chronology"; webspace.science.uu.nl/~gent0113/babylon (thư mục niên đại thiên văn Babylon).

**(2) Idrimi của Alalakh (TK 15 TCN) — đề xuất mạnh thứ hai**

- **Vì sao mạnh:** tượng Idrimi mang **bản khắc tự thuật 104 dòng bằng tiếng Akkad**, kể việc ông chạy khỏi Aleppo, nương nhờ nhóm Habiru, rồi giành ngôi và lập vương quốc Mukish. Thường được gọi là **tiểu sử hoàn chỉnh sớm nhất của một nhân vật chính trị** còn lại, và tới nay vẫn là **nguồn sơ cấp chính cho lịch sử Levant thế kỷ 15 TCN**. Tượng hiện ở Bảo tàng Anh (tìm thấy 1939, Leonard Woolley, Tell Atchana).
- **Tính nguyên bản (c):** đây là thể loại mới — không phải biên niên chiến công do nhà nước khắc như Biên niên Karnak, mà là **trình thuật ngôi thứ nhất về một sự nghiệp cá nhân gồm cả thất bại và lưu vong**. Đúng chỗ atlas hay tìm: một bước ngoặt về *dạng tư liệu*, không chỉ về quyền lực.
- **Bổ trợ cho hai lỗi đã nêu:** nó là đối trọng trực tiếp với mệnh đề tối cao ở `-05` (§5.3) và cùng loại luận cứ với `-07` Ahmes (tri thức/tiếng nói gắn được với một cái tên).
- **Lĩnh vực:** Chính trị/Nhà nước, Văn học. **Vùng:** Trung Đông/Bắc Phi. Lấp khoảng trống Levant.
- *Nguồn khởi đầu:* en.wikipedia.org/wiki/Idrimi; Bảo tàng Anh, tượng Idrimi; worldhistory.org/image/509.

**(3) Một vua Mitanni — Parattarna hoặc Shaushtatar (k. 1480–1430 TCN) — đề xuất có điều kiện**

- **Vì sao đáng xét:** Mitanni là cường quốc đã chặn Ai Cập ở bắc Syria và là đối thủ xác định hình thái đế chế Tân vương quốc. Idrimi trở thành chư hầu của Parattarna — tức hai đề xuất (2) và (3) móc vào nhau.
- **Vì sao chỉ "có điều kiện":** chứng thực đương thời cho từng cá nhân vua Mitanni mỏng (phần lớn qua con dấu và qua tư liệu của nước khác), niên đại rất rộng. Nếu không đủ, **thì vẫn nên nêu đích danh trong Ghi chú biên tập là đã xét và loại vì lý do tư liệu** — hiện Mitanni không được nhắc một chữ nào, nên người đọc không biết nó đã được cân nhắc hay bị quên.

**(4) Seqenenre Tao (mất k. 1555 TCN) — bổ sung vào danh sách bị loại, không nhất thiết thành mục**

Danh sách bị loại có Kamose và Ahhotep nhưng **thiếu Seqenenre Tao**, cha của cả hai người kia và người khởi chiến. Xác ướp ông mang **vết thương chiến trận trên sọ** — một trong rất ít bằng chứng vật lý trực tiếp về bạo lực chính trị ở thiên niên kỷ 2 TCN. Mục `-03` dựng cả mạch Kamose → Ahmose mà bỏ mắt xích đầu.

**(5) Thutmose I (trị vì k. 1506–1493 TCN) — nêu để chủ động loại, không nên thêm**

Ông là người thật sự đầu tiên đưa quân Ai Cập tới Euphrates, và là tiền lệ cho cả `-03` lẫn `-05` (xem §3.2 và §5.5, nơi hai mục tranh nhau công lao vốn một phần thuộc về ông). **Nhưng không nên thêm**: Ai Cập đã chiếm 5/8 suất, thêm một pharaoh nữa làm hỏng mục tiêu §5 về đa dạng. Cách xử lý đúng là **nêu ông trong "Vì sao chọn" của `-05`** như ứng viên bị loại cùng thời — vừa vá được lỗi §5 ở §5.4 (chỗ đang sai vì nêu Hatshepsut), vừa sửa được chỗ quy công quá tay.

### 10.3 Kết luận về lựa chọn

Tám mục hiện có **đều xứng đáng**; không mục nào nên bị loại. Vấn đề không phải ai có mặt mà là **ai chưa bao giờ được đưa lên bàn**:

- Thêm **Ammi-ṣaduqa** và **Idrimi** đưa nhóm lên 10/12, **lấp cả Lưỡng Hà lẫn Levant**, thêm lĩnh vực **Khoa học tự nhiên** (hiện trống), và **kéo tỉ lệ Ai Cập từ 5/8 xuống 5/10**.
- Nêu đích danh **Mitanni** và **Seqenenre Tao** trong Ghi chú biên tập, dù chỉ để nói đã xét và loại.
- Chuyển **Thutmose I** vào "Vì sao chọn" của `-05`, thay cho Hatshepsut (vốn là lỗi §5).

Một nhận xét cuối về quy trình: lỗi nặng nhất của nhóm (#12, #18 — hai mục liền nhau nêu nhau làm "ứng viên bị loại") **không phải lỗi tri thức**. Mục `-08` làm đúng quy tắc ấy trong cùng nhóm, với đúng cách diễn đạt CONTRIBUTING #6 yêu cầu. Tác giả biết quy tắc; chỗ hỏng là **không có bước đối chiếu cơ học** mọi tên trong "Vì sao chọn" với `data/persons.json`. CONTRIBUTING #6 đã đề xuất đúng script ấy — nhóm này là bằng chứng nó cần được chạy chứ không chỉ được khuyến nghị.
