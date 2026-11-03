# Vòng kiểm sự kiện độc lập — Chapter 5, nhóm CE08 (TK 8, 701–800 CN)

Người rà **không** viết nhóm CE08 và **không** thực hiện vòng cổng (`reports/ch05-ce08-gate.md`).
Ngày rà: 2026-10-31. Báo cáo được viết **tăng dần** — mỗi mục kiểm xong ghi ngay.

**Quy ước đánh dấu**
- **BẮT BUỘC SỬA** — mệnh đề sai sự kiện, vi phạm quy tắc, hoặc liên kết trỏ sai người.
- **NÊN SỬA** — đúng nhưng nói quá, thiếu chính xác, hoặc dễ gây hiểu nhầm.
- **CÂN NHẮC** — vấn đề phương pháp / cách diễn đạt, không chặn.
- **[KHÔNG KIỂM ĐƯỢC]** — không mở được nguồn gốc; nêu rõ lý do.

**User-Agent dùng cho mọi request:** `history-atlas/0.1 (research)`. Không nhúng thông tin cá nhân vào bất kỳ header/URL/payload nào.

---

## §0 · Cổng Q-ID: tự chạy lại, không chép từ vòng trước

`wbgetentities` (props=labels|claims, lang=en|vi), HTTP 200, nội dung thật.

| ID mục | Tên trong atlas | Q-ID | Nhãn Wikidata | P31 | P569 | P570 | Khớp? |
|---|---|---|---|---|---|---|---|
| -01 | Abu Muslim al-Khurasani | Q335210 | Abu Muslim al Khorasani | Q5 | 718 | 755-02 | ✔ |
| -02 | Al-Mansur | Q31066 | Al-Mansur | Q5 | 714 / 713-11 | 775-10-07 / 775-10-18 | ✔ |
| -03 | Jaʿfar al-Sadiq | Q170046 | Ja'far al-Sadiq | Q5 | 702-04-20 / 699 | 765-12-16 / 765 | ✔ |
| -04 | Abu Hanifa | Q190896 | Abu Hanifa | Q5 | 699-09-05 / 699 | 767 | ✔ |
| -05 | Sibawayh | Q983355 | Sibawayh | Q5 | 760 | 797 | ✔ |
| -06 | Charlemagne | Q3044 | Charlemagne | Q5 | **5 giá trị**: 748-04-02, 742, 747, 742-04-02, 742-04-10 | 814-01-28 / 814-02-01 | ✔ |
| -07 | Bêđa | Q154938 | Bêđa (nhãn vi) | Q5 | 672 ×2 / 673 | 735 / 734 / 735-05-25 | ✔ |
| -08 | Tăng Nhất Hạnh | Q710705 | Nhất Hạnh (nhãn vi) | Q5 | 683 | 727 | ✔ |
| -09 | Đỗ Phủ | Q33772 | Đỗ Phủ | Q5 | 712 | 770 | ✔ |
| -10 | Trisong Detsen | Q366661 | Trisong Detsen | Q5 | 742 ×2 | **4 giá trị**: 798, 797 ×2, 800 | ✔ |
| -11 | Ādi Shankara | Q180967 | Adi Shankara | Q5 | 788 | 820 ×2 | ✔ |
| -12 | Yikʼin Chan Kʼawiil | Q2620151 | Yik'in Chan K'awiil | Q5 | (không có) | (không có) | ✔ |

**Kết luận §0: cả 12 Q-ID trỏ đúng người, cả 12 đều `P31 = Q5`.** Không có ca "chi bướm". Vòng cổng đúng ở điểm này.

Hai Q-ID phụ được kiểm kèm vì ghi chú biên tập có nêu:
- `Q154332` Alcuin — P569 có **đúng ba giá trị: 724 / 735 / 740**, biên độ **16 năm**. Mệnh đề trong ghi chú **đúng**.
- `Q42798` Borobudur — `P31 = [Q5393308, Q839954, Q2736554]`, **không** có `Q5`. Mệnh đề "Borobudur là một công trình, không phải người" **đúng**.
- `Q310913` Thích Nhất Hạnh — 1926-10-11 / 2022-01-22, khớp mô tả trong mục -08 và trong ghi chú.

---

## §A · Kiểm sự kiện từng mục

### A-01 · `CH05-CE08-01` Abu Muslim al-Khurasani — Q335210

**Đúng và kiểm được**
- `Q335210` = Abu Muslim al Khorasani, `P31 = Q5`. Đúng người.
- "Năm 745 ông được phái từ Iraq về Khurasan" — nguồn ghi **745/6**. Khớp.
- "Năm 747 ông giương cờ đen công khai" — đúng.
- "cuối năm ấy chiếm Merv, đánh bật tổng đốc Umayyad Nasr ibn Sayyar" — đúng: Merv rơi **tháng 12-747 (một số nguồn: tháng 1-748)**. Cách viết "cuối năm ấy" nằm trong khung nguồn, chấp nhận được.
- "Divashtich thua trận năm 722" — đúng.
- `lĩnh vực: Chính trị/Nhà nước, Quân sự` — 2 giá trị, đều trong `FIELDS`. ✔
- `năm: k. 718–755` với `Trung bình` (±25) — nguồn cho **718/9 hoặc 723/7**, biên độ ~9 năm. Tương xứng. ✔

**NÊN SỬA — "trong ba năm" là phép đếm bị nén**
> "Trong ba năm, một cuộc nổi dậy ở rìa đông lật được triều đình ở trung tâm"

Từ cờ đen (6-747) tới trận Zab và sự sụp đổ của Marwan II (1-750 / 8-750) là **khoảng ba năm** nếu đếm từ 747, nhưng câu đứng ngay sau mệnh đề "chiếm Merv" nên dễ đọc thành "ba năm kể từ khi ông tới Khurasan" (745) — khi đó là **năm năm**. Đề nghị: *"Từ lúc giương cờ đến khi nhà Umayyad sụp (750) là chưa đầy ba năm."*

**CÂN NHẮC — `Ảnh hưởng tới: CH05-CE08-02 · kế thừa`**
Al-Mansur **xử tử** Abu Muslim (755). Loại quan hệ `kế thừa` mô tả đúng việc nhà nước Abbasid kế thừa thành quả cuộc nổi dậy, nhưng đọc trơ thì nghịch với chính câu "Abu Muslim bị ông xử tử năm 755" ở mục -02. Không sai từ vựng; có thể cân nhắc thêm một cặp `phản bác` như mục -12 đã làm với Calakmul.

**`vùng: Trung Á`** — xem §E. Kết luận ngắn: **đứng vững theo quy ước 1**, nhưng lập luận bảo vệ nó trong Ghi chú biên tập dựa trên một dữ kiện sai (xem B-11).

---

### A-02 · `CH05-CE08-02` Al-Mansur — Q31066

**Đúng và kiểm được**
- `Q31066` = Al-Mansur, `P31 = Q5`. Đúng người.
- "Al-Saffah lên ngôi trước" — đúng (al-Saffah 749–754, anh ông).
- "Hai mươi mốt năm cầm quyền" — 754–775 = **21 năm**. ✔
- "một quyết định năm 762: dựng kinh đô mới Madinat al-Salam" — đúng.
- "Abu Muslim bị ông xử tử năm 755" — đúng.
- `lĩnh vực: Chính trị/Nhà nước` (1), `vùng: Trung Đông/Bắc Phi` (Baghdad/Kufa). ✔

**NÊN SỬA — lý do cho `độ tin cậy niên đại: Trung bình` nêu sai biến số**
> "Niên đại ghi Trung bình vì các nguồn cho ba ngày mất khác nhau."

Hai vấn đề. (a) `Q31066` hiện có **hai** giá trị `P570` (775-10-07 và 775-10-18), không phải ba — con số "ba" **[KHÔNG KIỂM ĐƯỢC]** từ Wikidata; nếu nó đến từ nguồn cổ điển thì phải dẫn nguồn ấy. (b) Quan trọng hơn: `DATE_TOLERANCE` của atlas đo bằng **năm** (Cao ±5, Trung bình ±25). Mấy **ngày** lệch nhau trong cùng tháng 10-775 không thể là lý do hạ từ `Cao` xuống `Trung bình`. Biến số thật là **năm sinh** — `P569` cho 713-11 và 714, và nguồn cổ điển còn cho 709.

Đề nghị thay: *"Niên đại ghi Trung bình vì năm sinh không chắc — các nguồn cho 709, 713 và 714; năm mất 775 thì chắc."*

**NÊN SỬA — "Abu Hanifa chết trong ngục Baghdad năm 767" nói chắc hơn tư liệu**
Năm 767 và nơi Baghdad là chắc; việc **chết trong ngục** là tường thuật truyền thống, và giới nghiên cứu hiện đại (kể cả Melchert, chính là nguồn mục -04) đọc mạch truyện tử đạo ấy như lớp thánh truyện về sau. Đề nghị: *"Abu Hanifa chết ở Baghdad năm 767, theo truyền thống là trong ngục."* (Áp dụng cho cả mục -04, xem A-04.)

**CÂN NHẮC** — "giữ vai trung tâm của thế giới Hồi giáo suốt năm thế kỷ": 762–1258 đúng là ~5 thế kỷ về mặt danh nghĩa caliph, nhưng quyền lực chính trị thật của Baghdad đã mất từ 945 (Buyid). Không sai, nhưng là cách đọc rộng tay.

---

### A-03 · `CH05-CE08-03` Jaʿfar al-Sadiq — Q170046

**Đúng và kiểm được**
- `Q170046` = Ja'far al-Sadiq, `P31 = Q5`. Đúng người.
- `năm: k. 702–765` — `P569` 702-04-20 / 699; `P570` 765. Khớp. `Trung bình` tương xứng với biên độ 699–702. ✔
- `Ảnh hưởng tới:` **3 mục** — đúng trần. `lĩnh vực` 2 giá trị hợp lệ. ✔
- `Kế thừa từ: CH05-CE07-03` → mở ra đọc: **Ali ibn Abi Talib**. Đúng người, đúng chiều (tổ tiên bốn đời).
- `Ảnh hưởng tới: CH05-CE08-04` → **Abu Hanifa**. Đúng người.

**Điểm mạnh đáng ghi nhận:** phần "Vì sao chọn" tự giới hạn ở *vị trí* của Jaʿfar thay vì nội dung gán cho ông, và nói rõ việc quy hadith cho ông đang bị đặt dấu hỏi. Đây là cách viết đúng với tình trạng tư liệu.

**CÂN NHẮC — `mức bằng chứng: trực tiếp` cho liên kết Ali → Jaʿfar**
Ali mất **661**, Jaʿfar sinh **~702**; hai người cách nhau 41 năm và không thể gặp nhau. `CONTRIBUTING.md` quy tắc 8 cảnh báo đúng hình dạng này ("`trực tiếp` giữa hai người cách nhau 130 năm mà vẫn đúng thứ tự"). Nếu `trực tiếp` trong atlas nghĩa là *bằng chứng trực tiếp về quan hệ* (chứ không phải *tiếp xúc trực tiếp*) thì nhãn này ổn — nhưng quy ước ấy chưa được viết ra ở đâu, và nhóm CE08 dùng `trực tiếp` cho ít nhất bốn cặp không cùng thời (Ali→Jaʿfar, Isiđôrô→Bêđa, Gauḍapāda→Shankara, Pháp Xứng→Shankara). **Đề nghị cho Owner: ghi quy ước này thành văn ở `CONTRIBUTING.md`**, vì nếu không thì mỗi vòng rà sẽ đọc nó một kiểu.

**CÂN NHẮC — căng nhẹ giữa văn xuôi và liên kết**
Văn xuôi nói "không viết 'Jaʿfar dạy rằng X' từ các tuyển tập hadith", nhưng `Ảnh hưởng tới: Malik ibn Anas và trường phái Medina · kế thừa · trực tiếp` lại chính là mệnh đề truyền thống ấy ở dạng liên kết. Hoặc hạ xuống `qua trường phái`, hoặc nói rõ trong văn xuôi rằng quan hệ thầy–trò này cũng thuộc lớp truyền thống.

---

### A-04 · `CH05-CE08-04` Abu Hanifa — Q190896

**Đúng và kiểm được**
- `Q190896` = Abu Hanifa, `P31 = Q5`. Đúng người.
- `năm: k. 699–767` — `P569` 699-09-05 / 699, `P570` 767. Khớp.
- Ba thuật ngữ `qiyās` / `istiḥsān` / `raʾy` dùng đúng nghĩa, và mô tả `istiḥsān` ("chọn giải pháp hợp lý hơn khi loại tỷ cho kết quả cứng nhắc") là định nghĩa chuẩn.
- "Trường phái Hanafī ... trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi" — đúng.
- `vùng: Trung Đông/Bắc Phi` **và mục tự giải thích vì sao** ("quy ước của atlas lấy nơi hoạt động chính, và nơi ấy là Kufa"). Đây là cách xử lý đúng quy ước 1, và đáng khen vì nó viết ra lý do thay vì để người đọc đoán.

**NÊN SỬA — "ông bị tù dưới cả Umayyad lẫn Abbasid ... và chết trong ngục Baghdad"**
Cùng vấn đề với A-02: cả hai lần tù và cái chết trong ngục đều là **tường thuật truyền thống**, không phải dữ kiện được xác lập; Melchert (1997) — nguồn thứ nhất của chính mục này — đọc khối truyện ấy như xây dựng về sau của trường phái. Viết trần như sự kiện là **dùng nguồn ngược với luận điểm của nó** (quy tắc 7).
Đề nghị: *"Truyền thống kể ông bị tù dưới cả Umayyad lẫn Abbasid vì từ chối chức qāḍī và chết trong ngục Baghdad năm 767; giới nghiên cứu hiện nay đọc mạch truyện ấy như lớp thánh truyện của trường phái, nhưng việc ông không bao giờ nhận chức quan toà thì không ai tranh cãi."*

**[KHÔNG KIỂM ĐƯỢC] — "các nguồn cổ điển cho bốn năm sinh"**
Không tìm được bảng bốn năm sinh ấy trong nguồn mở được; Wikidata chỉ cho một năm (699). Con số "bốn" có thể đúng nhưng chưa xác minh — hoặc dẫn nguồn, hoặc viết "nhiều năm sinh khác nhau".

**Liên quan:** mệnh đề "nguồn nói ông gốc Trung Á" trong mục này là **đúng** (ông nội/cha gốc Kabul–Ba Tư), nhưng Ghi chú biên tập đã biến nó thành "**sinh** ở Trung Á" — sai. Xem B-11.


---

### §A-05 · CH05-CE08-05 · Sibawayh

**Kiểm hình thức.** `wikidata: Q983355` → nhãn en "Sibawayh", P31 = Q5 ✓ (xem §0). `lĩnh vực: Ngôn ngữ học` — 1 trường, nằm trong FIELDS ✓. `vùng: Trung Đông/Bắc Phi` ✓ (Basra và Baghdad là nơi hoạt động chính; quy ước 1 — nơi hoạt động chứ không phải nơi sinh — được tôn trọng, và mục còn tự ghi "gốc vùng Shiraz" ở trường `nơi:` thay vì để nó kéo `vùng:` đi, đúng cách). `Ảnh hưởng tới:` 2 mục ≤ 3 ✓.

**`độ tin cậy niên đại: Thấp` — ĐÚNG, và đúng vì lý do đúng.** Mục viết: *"Niên đại ghi Thấp vì nguồn cho hai khung chết loại trừ nhau, khác cả nơi chết."* Kiểm được: truyền thống cổ điển cho hai khung mất là **161 AH / 777 CN ở Basra** và **180 AH / 796 CN ở Shiraz** — cách nhau 19 năm và khác nơi. 19 năm vượt ngưỡng `DATE_TOLERANCE["Trung bình"] = 25`? Không — nhưng hai khung *loại trừ nhau về nơi chết*, tức không phải một sai số đo mà là hai tường thuật cạnh tranh; `Thấp` là lựa chọn đúng. Đây là một trong ít mục của nhóm nêu **độ chênh giữa các giá trị học thuật** chứ không chép `precision` của Wikidata — đúng yêu cầu.

**BẮT BUỘC SỬA — một mệnh đề sai hẳn.**

> *"Nó vẫn là mốc quy chiếu của ngữ pháp Ả Rập sau mười hai thế kỷ, và là bộ mô tả ngôn ngữ còn nguyên vẹn cổ nhất ngoài truyền thống Ấn Độ của Pāṇini."*

Vế sau sai. Có ít nhất ba bộ mô tả ngôn ngữ còn **nguyên vẹn** và **cổ hơn** al-Kitāb, không thuộc truyền thống Ấn Độ:
- *Technē grammatikē* gán cho Dionysius Thrax (bản còn lại muộn nhất cũng thuộc thời cổ đại hậu kỳ),
- *Ars grammatica* (Ars minor / Ars maior) của Aelius Donatus, thế kỷ 4 CN,
- *Institutiones grammaticae* của Priscianus, khoảng năm 500 CN — 18 quyển, còn đủ, và là sách giáo khoa chuẩn của chính châu Âu Latin thời Charlemagne (mục CE08-06 cùng nhóm).

Al-Kitāb soạn cuối thế kỷ 8, tức sau cả ba. Cái thực sự đặc biệt ở al-Kitāb không phải "cổ nhất" mà là **mức độ hệ thống và tính liên tục**: nó mô tả cả âm vị, hình thái, cú pháp lẫn biến thể vùng miền trong một khung lý thuyết duy nhất, và chưa bao giờ bị thay thế trong truyền thống của chính nó.

Câu thay thế đề nghị: *"Nó vẫn là mốc quy chiếu của ngữ pháp Ả Rập sau mười hai thế kỷ: khác với các sách ngữ pháp Hy Lạp và Latin cùng thời còn lại, al-Kitāb không bị một công trình nào trong truyền thống của nó thay thế, mà trở thành văn bản mà mọi nhà ngữ pháp Ả Rập về sau phải chú giải hoặc phản bác."*

**CÂN NHẮC — `CH02-BCE05-08 · tương đồng độc lập · suy đoán học giả`.** Đích trỏ đúng người (Pāṇini) ✓ và `tương đồng độc lập` thỏa điều kiện "hai bên không biết nhau" theo nghĩa hiển nhiên (cách nhau hơn một nghìn năm, không có tiếp xúc cá nhân). Nhưng có một dòng học thuật (Danecki; Vivien Law) đặt giả thuyết Sibawayh *gián tiếp* biết tới ngữ pháp Ấn Độ qua môi giới Ba Tư — tức chính cái mà `tương đồng độc lập` phủ định. Mục đã phòng hờ bằng `suy đoán học giả` ở ô mức bằng chứng, đó là cách xử lý chấp nhận được; chỉ lưu ý rằng ô mức bằng chứng ở đây đang gánh một việc mà tên quan hệ không gánh.

**Các mệnh đề khác — đúng.** "Sách không mang tên do chính ông đặt; đời sau gọi nó là *Quyển sách*" ✓. Chân dung tiểu sử nghèo nàn (tên Amr ibn Uthman, tới Baghdad, tranh luận, bị làm nhục, về Ba Tư, chết trẻ) khớp với truyền thống *al-masʾala al-zunbūriyya* như Carter 2004 trình bày ✓. Hai nguồn đều là sách có thật, đúng tác giả, đúng nhà xuất bản ✓.

---

### §A-06 · CH05-CE08-06 · Charlemagne

**Kiểm hình thức.** `wikidata: Q3044` ✓ (§0). `lĩnh vực: Chính trị/Nhà nước, Giáo dục` — 2 trường, đều trong FIELDS ✓. `vùng: Châu Âu` ✓. `Kế thừa từ:` 3, `Ảnh hưởng tới:` 3 — đúng trần ✓.

**`k. 748–814 CN` + `Trung bình` — ĐÚNG, có kiểm bằng số.** Tôi tự truy Q3044: có **5 phát biểu P569**, phủ **3 năm phân biệt — 742, 747, 748**. Độ chênh 742→748 là **6 năm**, vượt `DATE_TOLERANCE["Cao"] = 5` và nằm gọn trong `["Trung bình"] = 25`. Vậy `Trung bình` là nấc đúng, và nó đúng theo *độ chênh giữa các giá trị học thuật* chứ không theo `precision` — đây là cách làm mà yêu cầu đặt ra. Chọn `k. 748` làm con số hiển thị cũng khớp với phát biểu xếp hạng `preferred` của Wikidata (748-04-02) và với dòng học thuật hiện hành dựa trên *Annales Petaviani*.

**NÊN SỬA — "bốn phương án" không khớp dữ liệu nào.**

> *"...nên ngày lên ngôi xác định tới từng ngày trong khi năm sinh của Charlemagne cùng thế kỷ vẫn còn bốn phương án."* (câu này nằm ở mục CE08-12, nhưng nó nói về Charlemagne nên kiểm ở đây)

Q3044 có 5 phát biểu / **3 năm phân biệt** (742, 747, 748). Con số "bốn" không khớp số phát biểu, cũng không khớp số năm. Nếu ý định là đếm theo văn liệu chứ không theo Wikidata thì cần dẫn nguồn cho con số 4 — tôi **không tìm được** danh sách học thuật chuẩn nào cho đúng bốn năm sinh cạnh tranh. **[KHÔNG KIỂM ĐƯỢC]** cho con số 4.

Câu thay thế đề nghị: *"...nên ngày lên ngôi xác định tới từng ngày, trong khi năm sinh của Charlemagne cùng thế kỷ vẫn còn ba phương án cạnh tranh là 742, 747 và 748."*

**NÊN SỬA — Charles Martel "không để lại thiết chế nào" là nói quá.**

> *"Ứng viên bị loại là Charles Martel, ông nội ông: trận Tours năm 732 nổi tiếng hơn nhưng không để lại thiết chế nào."*

Quan hệ huyết thống đúng (Charles Martel → Pepin Lùn → Charlemagne) ✓. Nhưng vế sau sai theo đúng nghĩa đen của từ "thiết chế": Charles Martel (a) biến chức *maior domus* thành quyền cai trị thực tế và truyền được cho con, tức dựng chính cái nền mà Pepin đứng lên để phế Merovingian năm 751; (b) chia vương quốc cho các con khi chết như một ông vua; (c) bảo trợ công cuộc truyền giáo và tổ chức lại giáo hội Frank của Boniface — chính mạng lưới giám mục mà Charlemagne sau này dùng làm bộ khung hành chính; (d) việc ông cấp đất nhà thờ dưới dạng *precaria verbo regis* để nuôi kỵ binh là một trong những chủ đề kinh điển của sử học về nguồn gốc chế độ phong kiến. Nói "không để lại thiết chế nào" là phủ định đúng cái mà sử học coi là di sản chính của ông.

Câu thay thế đề nghị: *"Ứng viên bị loại là Charles Martel, ông nội ông: trận Tours năm 732 nổi tiếng hơn, và ông đã dựng nền quyền lực Carolingian — nhưng chương trình học thuật và việc gộp Tây Âu Latin thành một quyền cai trị, tức hai thứ atlas đo theo tiêu chí phạm vi, là công của người cháu."*

**CÂN NHẮC — "các bản chép thời ông" lệch khoảng một thế hệ.**

> *"...phần lớn tác phẩm Latin cổ điển còn tới nay là còn qua các bản chép thời ông."*

Mệnh đề nền (Reynolds & Wilson, *Scribes and Scholars*) đúng: bản chép cổ nhất còn lại của phần lớn tác gia Latin cổ điển là bản Carolingian. Nhưng phần lớn những bản ấy thuộc **thế kỷ 9**, tức sau khi Charlemagne mất năm 814 — chúng là sản phẩm của chương trình do ông khởi động chứ không phải của "thời ông". Đề nghị đổi "thời ông" thành "phong trào chép sách do ông khởi động".

**Các mệnh đề khác — đúng.** Vua Frank từ 768 ✓; diệt vương quốc Lombard 774 ✓; thu phục Bavaria 788 (phế Tassilo III) ✓; chiến dịch Avar 791–796 ✓; đăng quang 25/12/800 do Lêô III ✓. Hai nguồn có thật, đúng tác giả và nhà xuất bản; *Vita Karoli Magni* niên đại tranh luận (817–833) nên viết "k. 830" là hợp lệ ✓.

---

### §A-07 · CH05-CE08-07 · Bêđa

**Kiểm hình thức.** `wikidata: Q154938` ✓ (§0). `lĩnh vực: Sử học, Tôn giáo/Tâm linh` — 2, trong FIELDS ✓. `vùng: Châu Âu` ✓. `Kế thừa từ:` 3, `Ảnh hưởng tới:` 3 ✓.

**`k. 672–735 CN` + `Cao` — ĐÚNG.** Năm mất 735 là chắc chắn (26/5/735, tường thuật của Cuthbert về cái chết của ông là văn bản gần như đương thời). Năm sinh do chính Bêđa cho gián tiếp ở cuối *Historia ecclesiastica* ("năm thứ 59 của đời tôi" khi viết, năm 731) nên chỉ dao động 672/673 — **1 năm**, nằm sâu trong `DATE_TOLERANCE["Cao"] = 5` ✓. Mục còn tự giải thích đúng cơ chế này: *"phần lớn những gì ta biết về đời ông do chính ông viết ở chương cuối bộ sử ấy."* Đây là cách ghi `Cao` mà tôi muốn thấy ở cả nhóm.

**Xếp nhóm CE08 — ĐÚNG, và là ca kiểm tra tốt cho §3.** Bêđa sinh 672 (TK 7), mất 735 (TK 8). Nếu xếp theo năm sinh ông sẽ rơi vào CE07. Atlas xếp theo giai đoạn ảnh hưởng chính: *Historia ecclesiastica* hoàn tất **731** và *De temporum ratione* năm **725** — cả hai ở thế kỷ 8 ✓.

**Các mệnh đề nội dung — đúng.** *Historia ecclesiastica gentis Anglorum* hoàn tất khoảng 731 ✓. Dionysius Exiguus đặt ra niên lịch Anno Domini ở thế kỷ 6 (bảng Phục sinh năm 525) ✓, và chính việc Bêđa dùng nó xuyên suốt một bộ sử được đọc khắp châu Âu Latin đã biến nó thành mặc định ✓ — đây là mệnh đề chuẩn của sử học, không phải nói quá. Khái niệm *gens Anglorum* như một dân tộc duy nhất thay vì một tập hợp vương quốc cũng là luận điểm trung tâm của học giới về bộ sử này ✓.

**Liên kết — đúng người, và `trực tiếp` lần này dùng chuẩn.** `CH05-CE07-09` = **Isiđôrô thành Seville** (k. 560–636) ✓. Hai người không cùng thời, nhưng Bêđa đọc và dùng trực tiếp *De natura rerum* cùng *Etymologiae* của Isiđôrô — có dấu vết văn bản. Đây chính là trường hợp `trực tiếp` hợp lệ **qua văn bản** mà tôi nêu nghi vấn ở §A-03: nó hợp lệ vì có bằng chứng văn bản cụ thể, chứ không chỉ vì "ở sau trong cùng truyền thống". Khác biệt ấy nên được quy ước hóa. `CH04-CE05-01` = Augustinô thành Hippo ✓, `qua trường phái` ✓ đúng mức.

**Quy tắc 6 — sạch.** Alcuin xứ York được nêu làm *ứng viên bị loại* ở đây. Tôi đã quét toàn bộ `content/` và `data/persons.json`: **Alcuin không có mục riêng ở bất kỳ đâu** ✓. Mục còn nói rõ lý do loại (chương trình Carolingian của ông đã tính trong mục Charlemagne) và CE08-06 quả thật liệt Alcuin ở `Ảnh hưởng tới:` — hai mục khớp nhau, không mâu thuẫn ✓.

---

### §A-08 · CH05-CE08-08 · Tăng Nhất Hạnh (Yi Xing)

**Kiểm hình thức.** `wikidata: Q710705` ✓ (§0). `lĩnh vực: Toán học, Khoa học tự nhiên` — 2, trong FIELDS ✓. `câu hỏi lớn: Vũ trụ` ✓ trong BIG_QUESTIONS. `vùng: Đông Á` ✓. `Ảnh hưởng tới:` 2 ✓.

**`683–727 CN` + `Trung bình`.** Năm mất 727 chắc chắn; năm sinh có hai dòng (**683** và **673**) — chênh **10 năm**, vượt `Cao = 5`, trong `Trung bình = 25` ✓. Nấc đúng. Chỉ lưu ý: mục ghi `683–727` **không có "k."** ở năm sinh, trong khi chính độ chênh 10 năm là lý do hạ xuống `Trung bình`. Đề nghị đổi thành `k. 683–727 CN` để trường `năm:` và trường `độ tin cậy niên đại:` nói cùng một điều. **NÊN SỬA.**

**BẮT BUỘC SỬA — Lịch Đại Diễn không dùng "suốt phần còn lại của nhà Đường".**

> *"Lịch Đại Diễn do ông soạn được dùng suốt phần còn lại của nhà Đường."*

Sai, và sai khá xa. Đại Diễn lịch (大衍曆) được ban hành dùng từ năm **729** và bị thay bằng **Ngũ Kỷ lịch (五紀曆)** vào năm **762**, tức khoảng **33 năm**. Nhà Đường còn tồn tại tới **907**, và trong quãng còn lại ấy triều đình còn thay lịch nhiều lần nữa (Chính Nguyên lịch, Tuyên Minh lịch...). Nói "suốt phần còn lại của nhà Đường" phóng đại khoảng 33 năm thành khoảng 178 năm.

*(Cảnh báo phương pháp: tra bằng tiếng Anh cho ra con số "dùng khoảng 98 năm, tới k. 857" — đó là thời gian lịch Đại Diễn được dùng ở **Nhật Bản** (764–857), không phải ở Trung Quốc. Hai con số này rất dễ bị trộn. Nguồn tôi dùng để chốt là mục 大衍曆 tiếng Trung.)*

Câu thay thế đề nghị: *"Lịch Đại Diễn do ông soạn được triều đình ban hành năm 729 và dùng hơn ba mươi năm trước khi bị thay, nhưng phương pháp nội suy phi tuyến trong đó thì còn được lịch pháp Đông Á dùng lại rất lâu sau."*

**NÊN SỬA — "tổ tiên của mọi đồng hồ cơ" là luận điểm của Needham, không phải sự kiện.**

> *"...một cơ cấu hồi — bộ phận buộc bánh răng nhích từng nấc thay vì quay trơn, tổ tiên của mọi đồng hồ cơ."*

Việc Nhất Hạnh và Lương Lệnh Toản lắp cơ cấu hồi vào thiên cầu chạy bằng nước (k. 725) là có thật ✓. Nhưng "tổ tiên của **mọi** đồng hồ cơ" là **luận đề truyền bá** của Needham, và là phần gây tranh cãi nhất trong công trình của ông: chưa ai chỉ ra được đường truyền văn bản hay kỹ thuật nào nối cơ cấu hồi thủy lực Trung Hoa với cơ cấu hồi kiểu trục đứng (verge-and-foliot) xuất hiện ở châu Âu cuối thế kỷ 13. Hai nguồn của mục đều là sách của chính Needham — tức mệnh đề này đang được chống đỡ bởi đúng người đề ra nó, mà mục lại trình bày như dữ kiện.

Đây là **chỗ mục tự mâu thuẫn**: phần "Vì sao chọn" làm rất đúng việc *tách hai tầng* cho phép đo kinh tuyến (*"gọi nó là 'phép đo cung kinh tuyến đầu tiên' là diễn giải của học giới hiện đại đặt lên trên nó"*) nhưng lại không áp cùng kỷ luật ấy cho cơ cấu hồi.

Câu thay thế đề nghị: *"...một cơ cấu hồi — bộ phận buộc bánh răng nhích từng nấc thay vì quay trơn. Needham coi đây là tiền thân của cơ cấu hồi trong đồng hồ cơ, tuy đường truyền sang châu Âu thì chưa chứng minh được."*

**Các mệnh đề khác — đúng, và phần "Vì sao chọn" là điểm mạnh của nhóm.** Khảo trắc 724–725 trên chuỗi trạm bắc–nam, lấy chênh lệch bóng nắng giữa trưa và độ cao sao Bắc Cực để tính độ dài một độ cung ✓. Lời cảnh báo *"chính nguồn ghi rằng Nhất Hạnh không cho rằng Trái Đất hình cầu, nên không được viết ông 'đo chu vi Trái Đất'"* ✓ khớp với Needham và là đúng kiểu kỷ luật mà quy tắc 7 đòi. Câu phân biệt với **Thích Nhất Hạnh (1926–2022)** ✓ — tôi đã kiểm `CH90-CE19_20-10` trỏ đúng Thích Nhất Hạnh ở phụ lục, và Q310913 cho 1926–2022 ✓. Liên kết `Thiện Vô Uý (Śubhakarasiṃha) · trực tiếp` ✓ (hai người cùng dịch và sớ *Đại Nhật kinh*). `Tô Tụng và đồng hồ thiên văn thế kỷ 11 · qua trường phái` ✓ (tháp đồng hồ 1092) — và lưu ý mức `qua trường phái` ở đây đã tự giảm nhẹ chính mệnh đề "tổ tiên của mọi đồng hồ cơ" nói trên.

---

### §A-09 · CH05-CE08-09 · Đỗ Phủ

**Kiểm hình thức.** `wikidata: Q33772` ✓ (§0). `lĩnh vực: Văn học` — 1 ✓. `câu hỏi lớn: Con người` ✓. `vùng: Đông Á` ✓. `Kế thừa từ:` 2, `Ảnh hưởng tới:` 3 ✓.

**`712–770 CN` + `Cao` — ĐÚNG.** Hai niên đại này không có dòng cạnh tranh nào đáng kể trong học giới; độ chênh 0 năm ✓.

**Các mệnh đề nội dung — đúng.** "Gần 1.500 bài thơ còn lại" ✓ (con số thường dẫn là khoảng 1.400–1.500). Loạn An Lộc Sơn từ **755** ✓. Danh hiệu **Thi sử** (詩史) và **Thi thánh** (詩聖) ✓. Chi tiết "một đứa con chết vì thiếu ăn" ✓ — lấy từ chính bài *Tự kinh phó Phụng Tiên huyện vịnh hoài ngũ bách tự*, nên không phải thêu dệt. Mệnh đề *"gần như tất cả những gì ta biết về đời ông đều rút từ chính thơ ông"* ✓ khớp William Hung 1952. Ảnh hưởng tới thơ chữ Hán Việt Nam, Nhật Bản, Triều Tiên ✓.

**CÂN NHẮC — "biến cố lớn nhất thế kỷ 8 ở Đông Á".** Tuyệt đối hóa, nhưng bảo vệ được: loạn An Lộc Sơn (755–763) làm sụp hệ thống quân điền và phủ binh, đổi cả cơ cấu thuế khóa, và là bước ngoặt mà sử học Trung Quốc đồng thuận coi là chia đôi nhà Đường. Không đề nghị sửa, chỉ ghi nhận là một superlative chứ không phải dữ kiện.

**Quy tắc 6 — sạch, và đây là ca đáng khen.** **Lý Bạch** xuất hiện hai lần trong mục: ở `Kế thừa từ:` (dạng chữ tự do, không phải ID) và ở "Vì sao chọn" với tư cách *ứng viên bị loại*. Tôi đã kiểm: **Lý Bạch không có mục riêng** ở bất kỳ chapter nào, kể cả phụ lục ✓. Việc viết ông ở dạng chữ tự do thay vì ID là **đúng** — nếu viết ID thì lint mới bắt lỗi, còn ở đây soạn giả đã chủ động không giả vờ ông có mục. `trực tiếp` cũng đúng: hai người gặp nhau năm 744 và Đỗ Phủ viết nhiều bài tặng ông ✓.

**CÂN NHẮC — liên kết sang track phụ lục.** `Ảnh hưởng tới: CH90-CE19_20-01` = **Nguyễn Du** ✓ đúng người, và quan hệ có thật (Nguyễn Du có bài *Độc Tiểu Thanh ký* và đặc biệt *Lỗi Dương Đỗ Thiếu Lăng mộ*). Nhưng đây là liên kết từ **track chính** trỏ sang **track phụ lục**, mà track phụ lục theo thiết kế là cô lập khỏi thống kê chính. Cần Owner xác nhận hướng liên kết này có được phép không — đây là câu hỏi quy ước, không phải lỗi sự kiện.

---

### §A-10 · CH05-CE08-10 · Trisong Detsen

**Kiểm hình thức.** `wikidata: Q366661` ✓ (§0). `lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh` — 2 ✓. `vùng: Đông Á` ✓ — đúng quy ước 3 (REGIONS không có ô Nội Á, nên cao nguyên Tây Tạng về Đông Á), và **nhất quán** với `CH05-CE07-11` Tùng Tán Cán Bố cũng ghi `Đông Á` ✓. `Kế thừa từ:` 2, `Ảnh hưởng tới:` 2 ✓.

**`trị vì 755–797 CN` + `Trung bình` — ĐÚNG.** 755–797 là khung chuẩn; năm mất có dòng cạnh tranh (797 so với k. 800/804), độ chênh dưới 10 năm → `Trung bình` ✓. Dùng `trị vì` thay vì năm sinh–năm mất cũng đúng với quy ước định dạng.

**NÊN SỬA — "sắc chỉ năm 791" trình bày một trong hai niên đại cạnh tranh như đã chốt.**

> *"Cùng người ấy ra sắc chỉ năm 791 lấy Phật giáo làm quốc giáo..."*

Có hai niên đại được dùng song song trong học giới cho việc tuyên Phật giáo làm quốc giáo: **779** (gắn với việc hoàn thành và khánh thành Samye, lễ xuất gia của những tăng sĩ Tây Tạng đầu tiên) và **791** (gắn với sắc chỉ về giới luật và trụ đá dựng ở Samye). Quan trọng hơn: **trụ đá Samye không mang niên đại khắc trên mình nó** — con số là do học giới suy ra. Mục đang chọn một đầu mà không nói là có hai.

Câu thay thế đề nghị: *"Cùng người ấy ra sắc chỉ lấy Phật giáo làm quốc giáo — niên đại được dẫn khi thì 779, khi thì 791, vì trụ đá Samye ghi lại việc ấy không mang niên đại — cho dựng Samye..."*

**NÊN SỬA — "Phía Ấn Độ thắng" là tường thuật của một bên, viết như dữ kiện.**

> *"...tổ chức cuộc tranh biện Samye khoảng 792–794 để chọn giữa đường tu tiệm ngộ của Ấn Độ và đường tu đốn ngộ của Thiền Trung Hoa. Phía Ấn Độ thắng, và lựa chọn ấy định hình Phật giáo Tây Tạng tới hôm nay."*

Niên đại 792–794 ✓ đúng. Nhưng "Phía Ấn Độ thắng" chỉ là **tường thuật của nguồn Tây Tạng**. Văn bản Hán ở Đôn Hoàng — *Đốn ngộ đại thừa chính lý quyết* (頓悟大乘正理決) của Vương Tích, tức tường thuật của chính phía Ma-ha-diễn — khẳng định ngược lại rằng phía Thiền thắng. Đây là một trong những ca kinh điển của sử học Phật giáo về việc hai truyền thống ghi hai kết cục cho cùng một sự kiện (Demiéville, *Le Concile de Lhasa*, 1952). Mục đang chép kết cục của bên thắng mà không nói là có bên kia — mà chính mục này lại rất kỷ luật ở chỗ khác (phần "Vì sao chọn" loại Padmasambhava rất chuẩn), nên đây là một chỗ lệch đáng tiếc.

Câu thay thế đề nghị: *"...tổ chức cuộc tranh biện Samye khoảng 792–794 để chọn giữa đường tu tiệm ngộ của Ấn Độ và đường tu đốn ngộ của Thiền Trung Hoa. Truyền thống Tây Tạng chép phía Ấn Độ thắng — văn bản Hán ở Đôn Hoàng chép ngược lại — nhưng điều kiểm được là kết quả: dòng Ấn Độ thành dòng định hình Phật giáo Tây Tạng về sau."*

**CÂN NHẮC — "người kế vị ông" nói gọn quá một bậc.**

> *"...trụ đá Kar-cun do chính người kế vị ông dựng xác nhận việc lập chùa Samye..."*

Trụ đá sKar-chung do **Tride Songtsen (Sadnalegs, trị vì k. 800–815)** dựng. Ông là **con** Trisong Detsen, nhưng **không phải người kế vị ngay**: giữa hai người còn Muné Tsenpo (và theo một số nguồn là Mutik Tsenpo). "Người kế vị" không sai hẳn nhưng gợi ý sai về khoảng cách. Đề nghị: "do con ông, vua Tride Songtsen, dựng khoảng một thế hệ sau".

**Các mệnh đề khác — đúng, và phần loại Padmasambhava là chỗ mạnh nhất nhóm.** Năm 763 quân Tây Tạng vào Trường An và lập một hoàng đế bù nhìn ✓. Năm 783 hiệp ước Thanh Thủy buộc nhà Đường ký lại đường biên ✓. Samye là tu viện đầu tiên của Tây Tạng ✓. Lý do loại **Liên Hoa Sinh** — bản Đôn Hoàng có nhắc một đạo sư kīlaya cùng tên nhưng không gắn với Trisong Detsen, tiểu sử đầu tiên (*Padma bkaʼ thang* / *Zangs gling ma*) ra đời khoảng bốn thế kỷ sau — ✓ đúng, và đúng kiểu lập luận mà quy tắc 7 muốn. Liên kết `CH05-CE07-11` = Tùng Tán Cán Bố ✓ đúng người. Hai nguồn (Kapstein 2000; Dotson 2009) có thật, đúng tác giả và nhà xuất bản, và đều thực sự chống đỡ mệnh đề mà chúng được gắn vào ✓.

---

### §A-11 · CH05-CE08-11 · Ādi Shankara

**Kiểm hình thức.** `wikidata: Q180967` ✓ (§0). `lĩnh vực: Triết học, Tôn giáo/Tâm linh` — 2 ✓. `câu hỏi lớn: Thực tại` ✓. `vùng: Nam Á` ✓. `Kế thừa từ:` 3, `Ảnh hưởng tới:` 3 ✓.

**`k. 700 – k. 750 CN` + `Thấp` — ĐÚNG, và tôi đã cố bác bỏ nhưng không bác được.** Xem §D-2 cho phần phản biện đầy đủ. Tóm tắt: hai "k." và nấc `Thấp` là cách ghi đúng khi các khung cạnh tranh cách nhau hơn một nghìn ba trăm năm (thế kỷ 5 TCN của các maṭha so với 788–820 so với 700–750); `DATE_TOLERANCE["Thấp"] = None` đúng là ô dành cho ca này. Khung 700–750 cũng là khung mà nguồn tham chiếu phổ thông gọi là "được chấp nhận rộng rãi nhất hiện nay" ✓.

**NÊN SỬA — Vācaspati Miśra "nửa đầu thế kỷ 9" là một bên của tranh luận, và mục đang dựa vào nó để chặn đầu trên.**

> *"Học giới hiện nay chặn hai đầu bằng văn bản: ông trích Pháp Xứng, nên sau giữa thế kỷ 7; Vācaspati Miśra sớ cho ông ở nửa đầu thế kỷ 9."*

Vế đầu đúng ✓ (`CH05-CE07-10` = Pháp Xứng, k. 600 – k. 660 ✓ đúng người; việc Śaṅkara phản biện Pháp Xứng là mệnh đề mà SEP có chống đỡ, tôi đã mở và đọc). Vế sau thì không chắc như mục viết: niên đại của Vācaspati Miśra phụ thuộc vào việc con số **898** trong *Nyāyasūcīnibandha* của ông được đọc theo **lịch Vikrama** (→ **841 CN**, tức nửa đầu thế kỷ 9) hay theo **lịch Śaka** (→ **976 CN**, tức cuối thế kỷ 10). Chênh lệch **135 năm**, và không có đồng thuận.

Vấn đề không chỉ là sai số: **đây là chân chịu lực**. Nếu Vācaspati ở nửa đầu thế kỷ 9 thì khung 788–820 bị ép rất chặt, gần như loại. Nếu ông ở cuối thế kỷ 10 thì cái chặn đầu trên lỏng ra tới mức **không loại được 788–820 nữa**. Mục đang lấy phương án có lợi cho kết luận của mình và trình bày nó như đã chốt — đúng kiểu lỗi mà quy tắc 7 cảnh báo, chỉ khác là ở đây nguồn không bị dẫn ngược mà bị dẫn chọn lọc.

Câu thay thế đề nghị: *"Học giới hiện nay chặn đầu dưới bằng văn bản: ông trích Pháp Xứng, nên phải sau giữa thế kỷ 7. Đầu trên thì lỏng hơn người ta tưởng — nó thường được chặn bằng Vācaspati Miśra, người sớ cho ông, nhưng niên đại của chính Vācaspati dao động giữa 841 và 976 tùy cách đọc lịch Vikrama hay lịch Śaka."*

**CÂN NHẮC — nguồn thứ hai không chống đỡ toàn bộ đoạn.** Mục `Nguồn:` gồm Nakamura 1983 và mục "Śaṅkara" của Stanford Encyclopedia of Philosophy. Tôi đã mở URL SEP: **URL sống ✓**, và nó **có** chống đỡ hai mệnh đề — khung 700–750 kiểu Nakamura, và việc Śaṅkara phản biện Pháp Xứng ✓. Nhưng SEP **không nhắc tới Vācaspati Miśra** trong phần niên đại, nên cái chặn đầu trên đang phải dựa hoàn toàn vào Nakamura. Nakamura 1983 là nguồn có thật và đúng chủ đề; tôi **không có bản để mở** nên **[KHÔNG KIỂM ĐƯỢC]** việc Nakamura có đặt Vācaspati ở nửa đầu thế kỷ 9 hay không.

**Các mệnh đề triết học — đúng và được diễn đạt chính xác.** Ba bộ sớ (Brahma-sūtra, các Upaniṣad chính, Bhagavad-gītā) ✓. Ba luận điểm Advaita được tóm đúng, và điểm tinh tế nhất — *"thế giới nhiều vẻ ta thấy không phải ảo giác mà là một cách nhìn sai do vô minh"* — là cách phân biệt **đúng** giữa *māyā* như ảo ảnh và *avidyā* như nhận thức sai, tức mục tránh được đúng cái hiểu lầm phổ biến nhất về Advaita ✓. Mệnh đề *"Advaita vừa là triết học vừa là chú giải"* ✓. Liên kết `CH05-CE07-10 · phản bác · trực tiếp` ✓ đúng người và đúng loại quan hệ (Śaṅkara phản bác Pháp Xứng qua văn bản). `Gauḍapāda và Māṇḍūkya-kārikā · trực tiếp` ✓ (truyền thống coi Gauḍapāda là sư tổ của thầy ông).

---

### §A-12 · CH05-CE08-12 · Yikʼin Chan Kʼawiil

**Kiểm hình thức.** `wikidata: Q2620151` ✓ (§0). `lĩnh vực: Chính trị/Nhà nước, Nghệ thuật/Kiến trúc` — 2 ✓. `vùng: Châu Mỹ` ✓ (Tikal). `Kế thừa từ:` 2, `Ảnh hưởng tới:` 2 ✓.

**BẮT BUỘC SỬA — "kim tự tháp cao nhất thế giới Maya" sai.**

> *"...và chuyển chiến thắng thành đá — Đền IV, kim tự tháp cao nhất thế giới Maya, với các rầm gỗ chạm ghi chính những chiến dịch ấy."*

Đền IV ở Tikal cao **70 m**. **La Danta ở El Mirador cao khoảng 72 m** (một số đo cho tới 75 m tùy có tính cả nền bệ hay không) và được coi là kim tự tháp cao nhất từng được dựng trong thế giới Maya — chưa kể thể tích của nó (~2,8 triệu m³) lớn hơn Đền IV nhiều lần. Mệnh đề đúng và vẫn ấn tượng là: Đền IV là **kiến trúc cao nhất ở Tikal**, và là công trình cao nhất thế giới Maya **thời Cổ điển** (La Danta thuộc thời Tiền Cổ điển, dựng trước đó khoảng tám thế kỷ).

Câu thay thế đề nghị: *"...và chuyển chiến thắng thành đá — Đền IV, cao 70 mét, công trình cao nhất Tikal và cao nhất thế giới Maya thời Cổ điển, với các rầm gỗ chạm ghi chính những chiến dịch ấy."*

**NÊN SỬA — `trị vì 734–766` ghi dứt khoát một con số mà chính mục nói là "còn để ngỏ".**

> `năm: trị vì 734–766 CN` ... *"Ghi Trung bình chứ không phải Cao vì năm mất còn để ngỏ."*

Hai dòng này mâu thuẫn nhau về mặt hình thức: trường `năm:` không có "k." nào, trong khi phần giải thích nói năm mất để ngỏ. Và nó để ngỏ thật: tôi tự truy `Q2620151` — Wikidata ghi **P570 = no value**, tức không có năm mất nào được khẳng định ✓. Tài liệu tham khảo phổ thông cho triều đại kết thúc **khoảng 746 hoặc 755**, và năm mất **k. 755**; người kế vị Yaxʼ Nuun Ahiin II lên ngôi năm **768**, để lại một khoảng trống. **Tôi không tìm được chỗ nào xác nhận con số 766** — **[KHÔNG KIỂM ĐƯỢC]** cho mốc 766 (tôi không có bản Martin & Grube 2008 tr. tương ứng để đối chiếu, và các nguồn mở được thì cho 746/755).

Đề nghị: *`năm: trị vì 734 – k. 766 CN`*, hoặc nếu giữ nguyên thì phải ghi trong "Vì sao chọn" rằng 766 là mốc **văn bản cuối cùng nhắc tên ông** chứ không phải năm mất.

**Các mệnh đề khác — đúng.** Lên ngôi **8 tháng 12 năm 734** ✓ (khắc bằng Long Count nên xác định tới ngày — đúng như mục lập luận). Đánh bại Calakmul **736** ✓, El Perú **743** ✓, Naranjo **744** ✓. "Phá vỡ thế đối đầu hai thế kỷ giữa Tikal và Calakmul" ✓ là cách đọc chuẩn của Martin & Grube. Rầm gỗ chạm ở Đền IV ghi các chiến dịch ấy ✓. `Jasaw Chan Kʼawiil I, cha ông` ✓ đúng quan hệ. `Yaxʼ Nuun Ahiin II · trực tiếp` ✓ đúng người kế vị. `Calakmul, qua thế đối đầu kéo dài · phản bác · trực tiếp` — dùng `phản bác` cho một quan hệ **quân sự** giữa một người và một **thành bang** là cách dùng co giãn so với nghĩa "bác bỏ tư tưởng"; không sai theo từ vựng cố định nhưng là chỗ Owner nên quyết có chấp nhận không. **CÂN NHẮC.**

**Quy tắc 6 — sạch.** *"Kʼinich Janaabʼ Pakal có mục riêng ở nhóm CE07"* ✓ — `CH05-CE07-12` tồn tại và đúng là Pakal. Mục này **không** nêu Pakal làm ứng viên bị loại mà nêu đúng cách: như một người **đã có mục**, để tránh trùng. Đây là cách xử lý mẫu mực cho quy tắc 6.

---

## §B · Mười lăm khối ghi chú biên tập, kiểm từng mệnh đề

Tôi đọc 15 khối ở `content/ch05.md` dòng 712–758. Nhìn chung các khối này **chất lượng cao hơn phần lớn ghi chú biên tập mà tôi từng rà**: chúng nêu số hiệu property, dẫn mã HTTP, và chủ động ghi lại những ngõ cụt. Chính vì vậy các lỗi còn lại đáng sửa — một khối ghi chú tự trình bày là đã kiểm thì độc giả sẽ không kiểm lại.

### §B-01 · "Charlemagne ở nhóm thế kỷ 8"

**ĐÚNG TOÀN BỘ.** Tôi đã cố bác và không bác được; chi tiết ở §D-1. Các mệnh đề kiểm được: `group_range('CE08') → (701, 800)` ✓ (tôi tự chạy); lễ đăng quang 25-12-800 nằm trong khoảng ✓; 33/46 năm trị vì (768–814, trong đó 768–800 là 33 năm) ✓; diệt Lombard 774, Bavaria 788, Avar 791–796, Alcuin tới triều 782 — đều thế kỷ 8 ✓; sứ bộ với Harun al-Rashid (trị vì 786–809) diễn ra từ 797 trở đi ✓ thế kỷ 8. Lập luận "lint im lặng ở cả hai phương án nên đây thuần tuý là quyết định nội dung" ✓ đúng.

### §B-02 · "Khung 788–820 của Shankara không đến từ truyền thống Ấn Độ"

Khối này đúng ở kết luận nhưng có **ba chỗ cần sửa**, và một chỗ trong đó là lỗi suy luận chứ không phải lỗi dữ kiện.

**NÊN SỬA (1) — "K.P. Tiele" sai tên người.**
> *"Khung ấy do giới Đông phương học châu Âu cuối thế kỷ 19 đề xuất, theo sau K.P. Tiele..."*

Người được nói tới là **Cornelis Petrus Tiele (C.P. Tiele, 1830–1902)**, sử gia tôn giáo ở Leiden, tác giả *Outlines of the History of Religion*. "K.P." là một lỗi viết tắt lan truyền — nó có mặt trong mục Wikipedia tiếng Anh về Ādi Shankara, nên khối ghi chú chép **trung thành nguồn của nó**, nhưng nguồn ấy sai. Đề nghị đổi thành "C.P. Tiele".

**BẮT BUỘC SỬA (2) — "không đến từ truyền thống Ấn Độ" là sai ở đúng chữ then chốt.**
Tiêu đề khối và câu mở đều khẳng định khung 788–820 **không** đến từ truyền thống Ấn Độ. Thực tế: Tiele rút con số ấy từ một chuỗi văn bản **Ấn Độ** — chuyên luận *Āryavidyā-sudhākara* của Yajñeśvara Śāstrī, vốn dẫn lại *Śaṅkara-mandāra-saurabha* của Bhaṭṭa Nīlakaṇṭha. Nói cách khác, đóng góp của giới Đông phương học châu Âu là **chọn và phổ biến** một niên đại Ấn Độ, chứ không phải chế ra nó.

Điều khối ghi chú **đúng** và nên giữ là vế hẹp hơn: khung 788–820 **không phải truyền thống của các maṭha** (các maṭha cho thế kỷ 5 TCN), và không phải "truyền thống Śṛṅgeri" như bản nháp viết. Đó mới là cái cần bác.

Câu thay thế đề nghị cho tiêu đề: *"Khung 788–820 của Shankara không phải truyền thống của các maṭha"*. Và cho câu mở: *"Bản nháp mô tả 788–820 là 'truyền thống Śṛṅgeri'. Sai. Khung ấy được giới Đông phương học châu Âu cuối thế kỷ 19 phổ biến — C.P. Tiele lấy nó từ chuyên luận Āryavidyā-sudhākara của Yajñeśvara Śāstrī, vốn dẫn lại Bhaṭṭa Nīlakaṇṭha — rồi Max Müller, Macdonell, Deussen và Radhakrishnan chấp nhận theo lệ. Truyền thống của chính các maṭha thì đặt ông ở thế kỷ 5 trước Công nguyên."*

**BẮT BUỘC SỬA (3) — số học của Vikramāditya II không ra kết luận mà khối ghi chú rút.**
> *"...cách đọc được chấp nhận hiện nay quy về Vikramāditya II của triều Cālukya (733–746), tức ủng hộ khung **sớm**."*

Bản ghi Śṛṅgeri nói Śaṅkara sinh vào **năm thứ mười bốn** đời vua ấy. Nếu vua ấy là Vikramāditya II trị vì 733–746 thì năm thứ 14 rơi vào khoảng **746/747** — tức một Śaṅkara **sinh giữa thế kỷ 8**, hoạt động nửa sau thế kỷ 8. Đó **không** ủng hộ khung `k. 700 – k. 750` mà mục CE08-11 dùng; nó ngả về phía **muộn hơn**, gần với 788–820 hơn là với 700–750. Hơn nữa triều Vikramāditya II chỉ dài 13–14 năm, nên "năm thứ mười bốn" rơi đúng vào cuối triều — một trùng hợp đáng ngờ mà khối ghi chú không bàn.

Chữ "sớm" chỉ đúng **so với thế kỷ 5 TCN của các maṭha là muộn, so với 788–820 là sớm** — tức nó là một so sánh tương đối bị viết như một kết luận tuyệt đối, và nó đang được dùng để chống đỡ chính cái khung mà nó không chống đỡ.

Câu thay thế đề nghị: *"Bản ghi Śṛṅgeri thật sự chỉ nói ông sinh vào năm thứ mười bốn đời một vua tên Vikramāditya mà không cho biết là Vikramāditya nào. Một cách đọc quy về Vikramāditya II của triều Cālukya (733–746) — nhưng năm thứ mười bốn của triều ấy rơi vào khoảng 746, tức một Śaṅkara muộn hơn khung mục này dùng. Bản ghi ấy vì vậy không chốt được gì: nó chỉ loại thế kỷ 5 TCN."*

**ĐÚNG — phần còn lại.** Ba niên đại maṭha (Śṛṅgeri 483 TCN, Kanchipuram 509 TCN, Dvārakā 491 TCN) ✓. Danh sách người chấp nhận theo lệ (Max Müller, Macdonell, Deussen, Radhakrishnan) ✓. Câu kết — *"không có bi ký, không có tiền đúc, không có văn bản đương thời nào định danh ông, và các Śaṅkaravijaya đều được soạn nhiều thế kỷ sau"* — ✓ đúng và là lý do chính đáng cho `Thấp`. Về Vācaspati Miśra "nửa đầu thế kỷ 9": xem §A-11, đây là một bên của tranh luận 841-vs-976.

### §B-03 · "Hai chữ 'Nhất Hạnh'"

**ĐÚNG TOÀN BỘ, và đây là khối hữu dụng nhất trong mười lăm khối.** Tôi tự truy `Q710705`: nhãn `vi` là **"Nhất Hạnh"** trần ✓, không có description `vi` ✓, và `僧一行` **có thật** trong danh sách alias trường `zh` ✓. `CH90-CE19_20-10` tồn tại và trỏ đúng **Thích Nhất Hạnh** ✓; `Q310913` cho 1926–2022 ✓. Lời cảnh báo cuối — rằng cơ chế rủi ro ở đây *chạy ngược chiều* quy tắc 8 (một vòng sau mở Wikidata ra, thấy nhãn trần, rồi "sửa" cho khớp) — là một quan sát đúng và nên được nâng lên thành quy ước chung, không chỉ để ở ghi chú một nhóm.

### §B-04 · "Wikidata khai độ chính xác, nó không khai độ tin cậy"

Luận điểm trung tâm **đúng và quan trọng**. Ba trong bốn ca dẫn chứng kiểm được; **ca thứ tư sai**.

**ĐÚNG — Padmasambhava `Q231582`.** Tôi tự truy: `P569 = 717`, `P570 = 762`, mỗi phát biểu có đúng **một** khối tham chiếu, và `P248` của khối ấy trỏ tới **`Q54919` = Virtual International Authority File** ✓ — đúng như khối ghi chú nói: một hồ sơ thư mục thư viện, không phải một mệnh đề sử học.

**ĐÚNG, và còn mạnh hơn khối ghi chú nói — Jabir `Q167852`.** `P569 = 721`, `P570 = 815`, tham chiếu duy nhất có `P248` trỏ tới **`Q18609226` = Trove** (cổng thư mục của Thư viện Quốc gia Úc). Tức con số 721 trên Wikidata cũng chỉ được chống đỡ bằng một hồ sơ thư viện, hệt như Padmasambhava. Đề nghị **bổ sung** chi tiết này vào khối: nó củng cố chính luận điểm.

**BẮT BUỘC SỬA — Charles Martel: dẫn sai số hiệu property, và mệnh đề sai.**
> *"Charles Martel: ngày sinh và ngày mất khai tới `precision 11` mà cả `P31` lẫn `P570` đều **không có tham chiếu nào**."*

Tôi tự truy `Q3301` (lần ra qua `Q3044 → P22 → Q81212 Pepin Lùn → P22 → Q3301`):
- `P569 = 688-08-23`, precision 11, **có 1 tham chiếu** (`P248 → Q24436712`);
- `P570 = 741-10-22`, precision 11, **0 tham chiếu** ✓;
- `P31 = Q5`, 0 tham chiếu ✓ — nhưng `P31` là "thực thể thuộc lớp", **không phải ngày sinh**, nên nhắc nó trong một câu về niên đại là lạc.

Hai lỗi: (a) `P31` gần như chắc chắn là lỗi gõ của `P569`; (b) nếu sửa thành `P569` thì mệnh đề **thành sai**, vì `P569` có tham chiếu. Mệnh đề đúng là: ngày **mất** không có tham chiếu, ngày **sinh** có một tham chiếu dạng "nêu trong".

Câu thay thế đề nghị: *"Charles Martel: ngày sinh và ngày mất đều khai tới `precision 11`, nhưng `P570` không có tham chiếu nào và `P569` chỉ có một tham chiếu dạng 'nêu trong' trỏ về một mục cơ sở dữ liệu — tức độ chính xác tới ngày không đi kèm chứng cứ tới ngày."*

**ĐÚNG — hai ca đối chứng.** Sibawayh `Thấp` vì hai khung chết lệch 19 năm và khác nơi chết ✓ (xem §A-05). Bêđa `Cao` vì lời tự khai ở chương cuối ✓ (xem §A-07). Cặp đối chứng này là cách trình bày tốt.

### §B-05 · "Jabir ibn Hayyan"

**ĐÚNG, và là khối được kiểm kỹ nhất.** Các mệnh đề tôi xác minh được:
- *Fihrist* của Ibn al-Nadīm, **987** ✓, là tiểu sử đầu tiên về Jabir, và chính Ibn al-Nadīm ghi lại việc có người đương thời phủ nhận Jabir từng tồn tại ✓.
- Lập luận từ im lặng qua bốn nhà viết tiểu sử Shiʿa sớm (al-Barqī, al-Kashshī, al-Najāshī, al-Ṭūsī) soạn danh sách môn đồ Jaʿfar al-Sadiq mà không ai nhắc Jabir ✓.
- **Delva 2017** ✓ — tôi xác minh được qua Crossref: Thijs Delva, *Journal of Abbasid Studies* **4(1): 35–61**, bác cách dựng niên đại của Holmyard 1927.
- **Fuat Sezgin 1971** bác Kraus và quy khối văn bản cho một nhân vật thế kỷ 8 ✓ — đây là lập trường có thật của Sezgin trong *Geschichte des arabischen Schrifttums* tập IV (1971).
- Niên đại văn bản k. 850–950 cho khối *Jābirian* ✓ là lập trường chủ đạo hiện nay (Kraus, rồi Delva).
- Hai URL hỏng: `doi.org/10.1163/22142371-12340030` và `doi.org/10.1017/S0041977X20000014`. **[KHÔNG KIỂM ĐƯỢC]** — tôi không kiểm lại hai mã HTTP cụ thể (202 với 0 byte; 429 với trang chặn Varnish) vì chúng phụ thuộc thời điểm và IP; nhưng việc khối ghi chú **xác minh thư mục qua Crossref thay vì qua URL hỏng** là cách xử lý đúng, và tôi làm lại đúng cách ấy cho Delva 2017 và ra cùng kết quả ✓.

**CÂN NHẮC — một mệnh đề tuyệt đối không kiểm được.** *"...không có công trình sau 2010 nào đứng về phía ông [Sezgin]."* Đây là mệnh đề phủ định toàn xưng về toàn bộ văn liệu sau 2010; tôi **không có cách nào xác minh** nó bằng công cụ hiện có. **[KHÔNG KIỂM ĐƯỢC].** Đề nghị hạ xuống: *"tôi không tìm được công trình sau 2010 nào đứng về phía ông"* — giữ nguyên sức nặng thực tế mà không nhận một mệnh đề không chứng minh được.

### §B-06 · "Padmasambhava bị loại bằng đúng cái thước vừa dùng cho Jabir"

**ĐÚNG TOÀN BỘ.** *Zangs gling ma* của **Nyangral Nyima Özer (1124–1192)** ✓ — hai niên đại chính xác, và nó đúng là **tiểu sử hoàn chỉnh đầu tiên** của Liên Hoa Sinh ✓, cách đời ông khoảng bốn thế kỷ ✓. Khối "tám hoá thân", hệ *terma* và *guru yoga* hình thành từ khoảng thế kỷ 12 ✓. Các bản Đôn Hoàng có nhắc một đạo sư kīlaya cùng tên nhưng không gắn với Trisong Detsen ✓. Phép so sánh với Tì-ni-đa-lưu-chi (`CH90-CE01_09-04`, tiểu sử phụ thuộc *Thiền uyển tập anh* soạn sau bảy thế kỷ) ✓ đúng và đúng chỗ — nguyên tắc "thanh chắn của atlas chính phải cao hơn phụ lục, không thấp hơn" là một quy ước nên được viết vào CONTRIBUTING.md chứ không để nằm trong ghi chú một nhóm.

### §B-07 · "Nhóm chật nhất Chapter 5: bốn người bị loại vì trần"

**Phần lớn ĐÚNG.** Harun al-Rashid trị vì **786–809** ✓. Việc *Nghìn lẻ một đêm* lấy ông làm **nhân vật** chứ không phải tư liệu về ông ✓. Việc Bayt al-Ḥikma với tư cách trung tâm dịch thuật có tổ chức gắn với **al-Maʾmun** thế kỷ 9 chứ không phải Harun ✓ — đây là lập trường của Dimitri Gutas và là một cải chính đúng, đáng khen vì nó đi ngược cách kể phổ thông. *al-Muwaṭṭaʾ* của Malik ibn Anas là bộ sưu tập luật Hồi giáo thành văn sớm nhất còn lại ✓. Nguyên tắc "trần 12 là trần, không phải định mức" ✓ khớp CONTRIBUTING.md.

**NÊN SỬA — "tiểu sử Muhammad đầu tiên" nói quá một bậc.**
> *"**Ibn Ishaq** (*Sīra*, tiểu sử Muhammad đầu tiên, nguồn mà mọi tiểu sử sau phải đi qua)"*

*Sīra* của Ibn Isḥāq là tiểu sử **còn lại** sớm nhất ở dạng tương đối đầy đủ, nhưng không phải tiểu sử **đầu tiên**: trước ông đã có các công trình *maghāzī* của ʿUrwa ibn al-Zubayr và al-Zuhrī, chỉ không còn nguyên. Thêm một điểm mà một mục CE08 về ông sẽ phải xử lý: bản của chính Ibn Isḥāq **không còn**, cái còn là bản hiệu đính của Ibn Hishām (mất k. 833) — tức nếu viết mục cho ông thì đúng thước đo mà chính các khối ghi chú này dùng cho Jabir và Padmasambhava phải được áp lại.

Câu thay thế đề nghị: *"**Ibn Ishaq** (*Sīra*, tiểu sử Muhammad sớm nhất còn lại — và chỉ còn qua bản hiệu đính của Ibn Hishām — nguồn mà mọi tiểu sử sau phải đi qua)"*.

**Quy tắc 6 — sạch.** Tôi quét toàn bộ tiêu đề mục trong `content/`: **Harun al-Rashid, Malik ibn Anas, Ibn Ishaq, An Lộc Sơn — không ai có mục riêng** ✓. Câu *"vòng CE09 phải nhặt ông lại"* cho Harun al-Rashid là một chỉ dẫn tốt cho nhóm sau, không phải vi phạm quy tắc 6.

### §B-08 · "An Lộc Sơn: bốn tiêu chí đo con người, không đo biến cố"

**ĐÚNG.** Loạn An Lộc Sơn 755–763 ✓. Lập luận "triệu chứng chứ không phải nguyên nhân" của chế độ tiết độ sứ biên trấn ✓ là cách đọc chủ đạo của sử học hiện đại, không phải quan điểm thiểu số. Hai đường biến cố vẫn vào atlas — qua Đỗ Phủ (người chứng) và Trisong Detsen (người hưởng lợi, vì chính nó mở đường cho quân Tây Tạng vào Trường An **763**) ✓ — và cả hai mục ấy quả thật có nhắc đúng những điều này, nên khối ghi chú không hứa suông. Quy tắc 6 sạch ✓.

### §B-09 · "Divashtich: bằng chứng hạng nhất vẫn không phải ảnh hưởng hạng nhất"

**ĐÚNG gần như toàn bộ.** Văn khố núi Mugh: **khoảng 80 văn kiện** Sogdian ✓; UNESCO ghi danh *Memory of the World* **năm 2025** ✓ (kỳ họp thứ 221 của Hội đồng Chấp hành, 17-4-2025); là khối tư liệu Sogdian đầy đủ nhất tìm được **trong chính Sogdiana** ✓ — lưu ý mệnh đề này được rào đúng chỗ, vì nếu bỏ chữ "trong chính Sogdiana" thì nó sẽ sai (các văn bản Sogdian ở Đôn Hoàng và Turfan nhiều hơn); nội dung gồm sổ sách buôn bán, thư từ, khế ước, trao đổi ngoại giao và báo cáo do thám ✓; thua trận **722** ✓.

**CÂN NHẮC — "tháp im lặng" không phải loại công trình được chép.** Các nguồn mô tả Ḏēwaštīč bị đóng đinh trên một **naus** — nhà quàn hài cốt Hoả giáo — chứ không phải *dakhma* (tháp im lặng). Hai thứ là hai loại kiến trúc tang lễ khác nhau. Đề nghị đổi thành "trên một nhà quàn hài cốt Hoả giáo".

**ĐÚNG và đáng giữ nguyên văn:** *"nếu lẫn 'được ghi chép nhiều' với 'có ảnh hưởng lớn', atlas sẽ dần thành bản đồ các văn khố còn sót chứ không phải bản đồ ảnh hưởng."* Đây là mệnh đề phương pháp tốt nhất trong toàn bộ 15 khối.

### §B-10 · "Ô 'Trung Á' của atlas đo một từ vựng chín ô"

Kết luận **đúng** (xem §E), nhưng **bằng chứng chính mà khối này đưa ra thì sai cả hai vế.**

**BẮT BUỘC SỬA — "cặp đối xứng" được dựng trên hai mệnh đề sai.**
> *"Phép thử tự kiểm, và nó có một cặp đối xứng ngay trong nhóm: Abu Muslim **sinh ở Kufa mà hoạt động ở Merv** → Trung Á; Abu Hanifa **có thể sinh ở Trung Á mà hoạt động ở Kufa** → Trung Đông/Bắc Phi. Cùng một quy tắc, áp cùng một chiều, đẩy hai người về hai phía ngược nhau — đó là bằng chứng nội tại rằng đây là lập luận địa lý chứ không phải thao tác thống kê."*

- **Abu Muslim không sinh ở Kufa.** Các nguồn cho nơi sinh là **Merv** hoặc vùng gần **Isfahan**; Kufa là nơi ông **lớn lên / được nuôi dạy** với tư cách *mawlā*, chứ không phải nơi sinh.
- **Abu Hanifa không "có thể sinh ở Trung Á".** Ông **sinh ở Kufa** (k. 699); cái đến từ Trung Á là **gia thế** của ông (tổ tiên gốc Kabul/Ba Tư). Chính mục `CH05-CE08-04` viết đúng là **"gốc Trung Á"** — khối ghi chú đã nâng "gốc" thành "sinh", tức khối ghi chú mâu thuẫn với mục mà nó chú giải.

Hệ quả: "cặp đối xứng" không tồn tại như mô tả. Hai người **không** đối xứng; họ đều hoạt động chủ yếu ở nơi atlas gán cho họ, chỉ khác nhau ở gốc gác. Và vì "bằng chứng nội tại rằng đây là lập luận địa lý chứ không phải thao tác thống kê" đang treo trên cặp đối xứng ấy, **lập luận phòng thủ của khối ghi chú tự hỏng** — dù, như tôi kết luận ở §E, **kết luận của nó vẫn đúng vì lý do khác**: Merv và Khurasan là nơi hoạt động chính của Abu Muslim, chấm hết, quy ước 1 áp thẳng là ra.

Câu thay thế đề nghị: *"Phép thử tự kiểm: Abu Muslim hoạt động chính ở Merv và Khurasan → Trung Á; Abu Hanifa gốc gác Trung Á nhưng sinh và hoạt động cả đời ở Kufa → Trung Đông/Bắc Phi. Cùng một quy ước — nơi hoạt động chính, không phải nơi sinh và càng không phải gốc gác — áp cho hai người có gốc gác giao nhau mà ra hai kết quả khác nhau. Đó là lập luận địa lý, không phải thao tác thống kê."*

**ĐÚNG — phần còn lại của khối.** `REGIONS` không có ô Nội Á ✓ (tôi đọc `atlaslib/common.py`); Tây Tạng và cao nguyên Mông Cổ đều bị dồn vào Đông Á ✓; `CH02-BCE06-09` = **Zarathustra** ✓ đúng người, và trường `nơi:` của mục ấy quả thật ghi *"đông Iran hoặc Trung Á"* ✓ — nên nhận xét rằng con số *Trung Á = 0,5%* trước nhóm này "đứng trên một người mà vị trí địa lý còn là câu hỏi mở" là ✓ đúng và trung thực. Kết luận *"sau Chapter 5, 'Trung Á' trong atlas thực tế chỉ còn nghĩa Transoxiana–Iran đông"* ✓.

### §B-11 · "Đông Nam Á ở lại 0,5%"

**ĐÚNG TOÀN BỘ.** Bia **Canggal năm 732** nêu Sanjaya ✓ (tiếng Phạn, quần thể Gunung Wukir, Trung Java). Bia **Kalasan năm 778** ✓ (700 Śaka) — và đúng là **bi ký đầu tiên ở Indonesia nêu tên dòng họ Śailendra** ✓, ghi việc dựng đền thờ **Tārā** và cúng một làng cho Tăng-già ✓. `Q42798` **Borobudur có `P31` không phải `Q5`** ✓ (tôi tự kiểm ở §0) — nên nó không có đường nào vào atlas ✓. `ch90.md` là phụ lục **Việt Nam**, không phải phụ lục Đông Nam Á ✓, nên lập luận "không đẩy xuống phụ lục được" đứng vững ✓. Lý do loại theo tiêu chí (c) và (d) — người bảo trợ chứ không phải người khởi tạo, và không bi ký nào cho biết điều gì thuộc quyết định riêng của họ — ✓ đúng và đúng kiểu.

Kiểm lại con số: `Đông Nam Á = 1/221 = 0,45%` ✓ làm tròn 0,5% hợp lệ. Quy tắc 6 sạch (Sanjaya và Panangkaran không có mục ở đâu) ✓.

### §B-12 · "Châu Phi hạ Sahara thế kỷ 8"

Khối này có **một lỗi niên đại nặng** và **một chỗ mô tả sai nguồn**; phần còn lại đúng.

**BẮT BUỘC SỬA (1) — Aksum ngừng đúc tiền ở thế kỷ 7, không phải thế kỷ 8.**
> *"Nhìn rộng hơn: Aksum **ngừng đúc tiền vào đầu thế kỷ 8**..."*

Tiền Aksum lưu hành từ thời Endybis (k. 270) và **suy tàn trong nửa đầu thế kỷ 7**; các đợt phát hành cuối cùng (Armah, Gersem, Hataz) được đặt ở **đầu thế kỷ 7**, với mốc thường dẫn là **k. 620**. Chênh khoảng một thế kỷ.

Đáng chú ý: sửa lại cho đúng **làm lập luận của khối ghi chú mạnh hơn**, không yếu đi — nếu nguồn tiền đúc tắt từ k. 620 thì khoảng mù tư liệu của vùng này bắt đầu **sớm hơn** một thế kỷ so với khối ghi chú tưởng, tức "con số 1,9% đo hình dạng của tư liệu" càng đúng.

Câu thay thế đề nghị: *"Nhìn rộng hơn: Aksum ngừng đúc tiền từ nửa đầu thế kỷ 7, với các đợt phát hành cuối cùng đặt quanh năm 620 — mà tiền đúc chính là nguồn đương thời atlas đã dùng cho Ezana `CH04-CE04-09` và Kaleb `CH05-CE06-09`."*

**NÊN SỬA (2) — "một biên niên soạn muộn" mô tả sai nguồn về Kyriakos.**
> *"Ông vẫn bị loại, vì nguồn duy nhất là *History of the Patriarchs of Alexandria*, **một biên niên soạn muộn**..."*

*History of the Patriarchs* với tư cách **bộ biên soạn** đúng là muộn (hợp thành và dịch sang tiếng Ả Rập ở thế kỷ 11). Nhưng phần chứa chuyện Kyriakos là **Tiểu sử giáo hoàng Michael** do **John the Deacon** viết bằng tiếng Copt, **hoàn tất khoảng 768–770** — tức khoảng **hai mươi năm** sau biến cố 748, và là **nguồn quan trọng nhất về Nubia Cơ Đốc nửa đầu thế kỷ 8**. Nói "soạn muộn" trộn tuổi của bộ sưu tập với tuổi của bản văn, và nó trộn theo hướng bất lợi cho chính Kyriakos.

Điều này **không lật kết luận loại ông** — lý do thứ hai mà khối ghi chú nêu (các hệ sử liệu không thống nhất nổi ông đứng ở đâu trong danh sách vua Makuria) vẫn nguyên, và tiêu chí (a) phạm vi vẫn loại ông. Nhưng lý do thứ nhất phải viết lại.

Câu thay thế đề nghị: *"Ông vẫn bị loại — không phải vì nguồn muộn: phần chép chuyện ông là *Tiểu sử giáo hoàng Michael* của John the Deacon, hoàn tất khoảng 768–770, tức gần như đương thời, và là nguồn tốt nhất ta có về Nubia Cơ Đốc thế kỷ 8. Ông bị loại vì các hệ sử liệu không thống nhất nổi ông đứng ở đâu trong danh sách vua Makuria — bản này xếp triều ông sau Markos, bản khác đặt giữa Merkurios và Zacharias I — nên ngay cả vị trí của ông trong triều đại cũng chưa chốt được."*

**ĐÚNG — phần còn lại.** Michael I trị vì **743–767** ✓, nên `fl. k. 748` quả thật là niên đại dựng ngược từ triều giáo hoàng ✓. Kyriakos đem quân vào Ai Cập Umayyad để buộc thả Michael I, vi phạm hiệp ước **Baqt** ✓. Nguồn viết sớm nhất về **Kanem là al-Yaʿqūbī năm 872** ✓ (ông liệt Kanem cùng Ghana và Gao trong *Bilād as-Sūdān*), thế kỷ 9 và là nguồn ngoại lai ✓. Bi ký Hồi giáo cổ nhất bờ Đông Phi là bia **Kufic ở Kizimkazi Dimbani, Zanzibar, năm 1107** ✓. Hai ID `CH04-CE04-09` (Ezana) và `CH05-CE06-09` (Kaleb) ✓ đúng người. "Bốn mục Châu Phi hạ Sahara" ✓ — tôi đếm lại từ `data/persons.json`: đúng **4**.

### §B-13 · "Châu Đại Dương 0,0%"

Kết luận **đúng và vững** (ba tầng độc lập, tầng nào cũng đủ một mình), nhưng **trích dẫn chủ lực bị sai ở hai chỗ**, và một trong hai là sai nội dung chứ không phải sai hình thức.

**BẮT BUỘC SỬA — niên đại quần đảo Society bị chép nhầm sang con số của nhóm đảo khác.**
> *"Wilmshurst, Hunt, Lipo & Anderson, *PNAS* 108(5): 1815–1820 (2010), phân tích lại 1.434 niên đại carbon phóng xạ và **đặt việc định cư quần đảo Society ở k. 1200–1290**, với toàn Đông Polynesia lan toả trong thế kỷ 13."*

Bài báo chia định cư Đông Polynesia thành **hai đợt**: (a) nhóm **Society ở trung tâm, khoảng 1025–1120 CN**; (b) sau đó, cách 70–265 năm, một đợt lan toả lớn tới **toàn bộ các đảo còn lại, khoảng 1190–1290 CN**. Khối ghi chú đã gán con số của đợt (b) cho nhóm đảo của đợt (a).

Chi tiết thư mục: tập/số/trang **108(5): 1815–1820** ✓ đúng, **1.434 niên đại carbon phóng xạ** ✓ đúng — nhưng **năm xuất bản là 2011**, không phải 2010 (bài lên mạng cuối tháng 12-2010, in ở số tháng 2-2011; dạng trích dẫn chuẩn là 2011). **NÊN SỬA.**

Lưu ý quan trọng: **kết luận không đổi.** Ngay cả mốc sớm hơn 1025 vẫn muộn hơn thế kỷ 8 hơn hai trăm năm, nên tầng (1) vẫn đứng. Nhưng một khối ghi chú tự nhận là đã kiểm thì con số phải đúng.

**[KHÔNG KIỂM ĐƯỢC] — tôi gặp đúng rào cản mà khối ghi chú gặp.** Tôi thử mở `pnas.org/doi/10.1073/pnas.1015876108` → **HTTP 403**; thử ngả PubMed → tường cookie, không ra metadata. Các con số trên tôi xác minh qua văn bản tóm tắt do công cụ tìm kiếm trả về, **không phải từ bản gốc**. Việc khối ghi chú đánh dấu các bài phản biện trên cùng tạp chí là không đọc được ✓ trung thực; tôi cũng không đọc được chúng.

**ĐÚNG — hai tầng còn lại.** Không hệ chữ viết nào ở Châu Đại Dương trước tiếp xúc châu Âu ✓; rongorongo chưa giải mã được và **tư cách chữ viết của nó vẫn là giả thiết** ✓ — cách rào này chính xác. Tây Polynesia, Melanesia, Micronesia đã có người từ lâu nhưng tên người truyền qua gia phả truyền khẩu, chỉ chép thành văn từ thế kỷ 19 ✓. Hai ca đối chiếu đều đúng: *Thiền uyển tập anh* (k. 1337) cách Tì-ni-đa-lưu-chi (580) khoảng bảy thế kỷ rưỡi ✓; *Zangs gling ma* (Nyangral Nyima Özer, 1124–1192) cách Padmasambhava khoảng bốn thế kỷ ✓. Lập luận *"phe phản biện đòi niên đại sớm hơn, mà tầng (2) và (3) độc lập hoàn toàn với tranh luận ấy"* ✓ — đây là cách đúng để xử lý một tranh luận chưa đọc được.

### §B-14 · "Ứng viên Việt Nam trong nhóm CE08"

**ĐÚNG TOÀN BỘ, và là khối xử lý quy tắc 6 chuẩn nhất.** Ba ID đều kiểm được và trỏ đúng người: `CH90-CE01_09-06` = **Mai Hắc Đế** (hoạt động k. 713–722) ✓, `CH90-CE01_09-07` = **Phùng Hưng** (hoạt động k. 766–791) ✓, `CH90-CE01_09-08` = **Khương Công Phụ** (731–805) ✓ — cả ba khớp chính xác cả tên lẫn trường `năm:` trong `data/persons.json`.

Lập luận quy tắc 6 ✓ đúng: vì cả ba **đã được chọn ở chỗ khác**, nêu tên họ như "ứng viên bị loại" sẽ là vi phạm; khối ghi chú nêu họ mà nói rõ *"không có đánh đổi nào xảy ra"*, tức dùng đúng hình thức được phép.

Hai mệnh đề về Khương Công Phụ kiểm được: ông **đỗ đầu kỳ thi nhà Đường năm 780** ✓ (khoa thi thời Đường Đức Tông, năm Canh Thân 780) và thăng tới **Đồng trung thư môn hạ bình chương sự** ✓ — chức tể tướng thực tế dưới Đường Đức Tông.

Hai cảnh báo nguồn ở cuối khối đều **đúng và đáng giữ**:
- chi tiết gia thế đến từ tộc phả họ Khương, tức nguồn muộn ✓;
- chữ **"trạng nguyên"** là thuật ngữ khoa cử Việt Nam đời sau áp ngược lên kỳ thi 780 nên phải viết "đỗ đầu kỳ thi" kèm chú ✓ — và đây là cảnh báo thực sự cần thiết, vì gần như toàn bộ nguồn tiếng Việt phổ thông về ông dùng chữ "trạng nguyên".

### §B-15 · "Hình dạng của thế kỷ, không phải thiên lệch của người chọn"

**Hai thống kê lĩnh vực ĐÚNG; một con số vùng LỆCH.**

Tôi đếm lại từ `data/persons.json`, chỉ track chính, nhóm `CH05-CE08`:
- **Chính trị/Nhà nước: 5/12** ✓ đúng như khối ghi chú nói;
- **Tôn giáo/Tâm linh: 5/12** ✓ đúng.

**NÊN SỬA — con số 33,2%.**
> *"...bốn suất cho Trung Đông/Bắc Phi giữ tỷ lệ atlas đứng nguyên ở **33,2%**..."*

Tính lại trên dữ liệu hiện tại: track chính có **221 người**, Trung Đông/Bắc Phi **73**, tức **33,0%**. Con số 33,2% đến từ bảng cơ sở của vòng cổng (`reports/ch05-ce08-gate.md` §0, lấy mốc 208 người track chính) và đã lạc hậu sau khi nhóm CE08 vào dữ liệu. Đề nghị đổi thành **33,0%**, hoặc tốt hơn là ghi kèm mẫu số: *"33,0% (73/221)"* — vì chính khối ghi chú này cảnh báo người đọc phải đọc tỷ lệ vùng kèm giới hạn, mà tỷ lệ không mẫu số thì không kiểm lại được.

Lập luận bên dưới con số thì **đúng**: cấp cho một nhóm đúng tỷ lệ bằng tỷ lệ đang có của toàn atlas thì giữ nguyên tỷ lệ ấy — 4/12 = 33,3% so với 33,0% đang có, lệch không đáng kể ✓. Vậy "cắt từ tám ứng viên xuống bốn không phải trừng phạt vùng ấy mà là giữ nguyên trạng" ✓.

**ĐÚNG — phần còn lại.** "Tính cả Abu Muslim ở ô Trung Á thì thế giới Hồi giáo vẫn chiếm **5/12** số mục của nhóm" ✓ (Abu Muslim, al-Mansur, Jaʿfar al-Sadiq, Abu Hanifa, Sibawayh). "Trung Á và Châu Mỹ lần đầu nhúc nhích, từ **1 lên 2** người mỗi ô" ✓ — tôi xác nhận: Trung Á trước nhóm này chỉ có Zarathustra, Châu Mỹ chỉ có Pakal `CH05-CE07-12`; sau nhóm này cả hai ô đều bằng **2**. Về câu "nhúc nhích bằng hai người có nguồn đương thời chứ không bằng việc hạ thanh chắn": xem §E — tôi đồng ý, nhưng với một dè dặt về mốc 766 của Yikʼin Chan Kʼawiil.

---

## §C · Nhất quán quy tắc (quy tắc 6 và quy tắc 8)

### §C-1 · Quy tắc 8 — mọi ID trong vùng CE08 đều tồn tại và trỏ đúng người

Tôi trích toàn bộ ID dạng `CHxx-…-nn` xuất hiện trong vùng CE08 của `content/ch05.md` (12 mục + 15 khối ghi chú) và đối chiếu từng cái với `data/persons.json`. **36 ID phân biệt, 0 ID không tồn tại, 0 ID trỏ sai người.**

Những ID mà quy tắc 8 cảnh báo nhiều nhất — loại "ID hợp lệ nhưng sai người", thứ lint mù hoàn toàn — đều đúng:

| ID | Trỏ tới | Dùng ở | Đúng? |
|---|---|---|---|
| `CH05-CE07-03` | Ali ibn Abi Talib | Jaʿfar al-Sadiq, `Kế thừa từ` | ✓ |
| `CH05-CE07-09` | Isiđôrô thành Seville | Bêđa, `Kế thừa từ` | ✓ |
| `CH05-CE07-10` | Pháp Xứng | Shankara, `phản bác` | ✓ |
| `CH05-CE07-11` | Tùng Tán Cán Bố | Trisong Detsen, `Kế thừa từ` | ✓ |
| `CH05-CE07-12` | Kʼinich Janaabʼ Pakal | Yikʼin Chan Kʼawiil, "đã có mục" | ✓ |
| `CH02-BCE05-08` | Pāṇini | Sibawayh, `tương đồng độc lập` | ✓ |
| `CH02-BCE06-09` | Zarathustra | ghi chú "Ô Trung Á" | ✓ |
| `CH04-CE04-09` | Ezana xứ Aksum | ghi chú Châu Phi | ✓ |
| `CH05-CE06-09` | Kaleb xứ Aksum | ghi chú Châu Phi | ✓ |
| `CH04-CE05-09` | Āryabhaṭa | ghi chú Āryabhaṭa | ✓ |
| `CH90-CE01_09-04` | Tì-ni-đa-lưu-chi | ghi chú Padmasambhava | ✓ |
| `CH90-CE01_09-06/07/08` | Mai Hắc Đế / Phùng Hưng / Khương Công Phụ | ghi chú D5 | ✓ |
| `CH90-CE19_20-01` | Nguyễn Du | Đỗ Phủ, `Ảnh hưởng tới` | ✓ |
| `CH90-CE19_20-10` | Thích Nhất Hạnh | ghi chú "Hai chữ Nhất Hạnh" | ✓ |

**Kết luận §C-1: quy tắc 8 sạch cho toàn vùng CE08.** Một điểm cần Owner quyết chứ không phải lỗi: `CH05-CE08-09` Đỗ Phủ trỏ `Ảnh hưởng tới: CH90-CE19_20-01` — một liên kết từ **track chính** sang **track phụ lục**, mà phụ lục theo thiết kế nằm ngoài thống kê toàn cục (xem §A-09).

### §C-2 · Quy tắc 6 — không ai bị nêu làm "ứng viên bị loại" mà đã có mục ở chỗ khác

Tôi gom toàn bộ tên được nêu là ứng viên bị loại hoặc bị bỏ trong 12 mục và 15 khối ghi chú, rồi quét **mọi tiêu đề mục (`^### `) trong toàn bộ `content/`**:

Charles Martel · Alcuin xứ York · Lý Bạch · Liên Hoa Sinh (Padmasambhava) · Harun al-Rashid · Malik ibn Anas · Ibn Ishaq · An Lộc Sơn · Jabir ibn Hayyan · Divashtich (Ḏēwaštīč) · Kyriakos xứ Makuria · Sanjaya · Panangkaran · Yajaw Teʼ Kʼinich II — **không một ai có mục riêng ở bất kỳ chapter nào, kể cả phụ lục.**

**Kết luận §C-2: quy tắc 6 sạch cho toàn vùng CE08.**

Hai cách xử lý **đúng** đáng ghi lại làm mẫu:
1. `CH05-CE08-12` viết *"Kʼinich Janaabʼ Pakal **có mục riêng** ở nhóm CE07"* — tức nêu đúng cách: như người đã được chọn, để tránh trùng, **không** như ứng viên bị loại.
2. Khối ghi chú D5 nêu ba nhân vật Việt Nam nhưng nói thẳng *"quy tắc 6 cấm nêu tên họ như ứng viên bị loại: không có đánh đổi nào xảy ra"* — tức tự dẫn quy tắc rồi tự tuân.

### §C-3 · Có ai bị viết như thể đã có mục trong khi không có không?

**Không.** Tôi kiểm riêng ca mà đề bài nêu: **Lý Bạch**. Ông xuất hiện hai lần ở `CH05-CE08-09` — ở `Kế thừa từ:` và ở phần "Vì sao chọn" — và **cả hai lần đều ở dạng chữ tự do, không phải ID** ✓. Đó là cách viết đúng cho một người không có mục. Tương tự với Alcuin (7 lần nhắc, 0 lần dưới dạng ID), Harun al-Rashid, Malik ibn Anas, Ibn Ishaq.

Ngược lại cũng đúng: mọi tên **có** mục đều được viết kèm ID (Pakal, Āryabhaṭa, Zarathustra, ba nhân vật Việt Nam, Thích Nhất Hạnh).

---

## §D · Hai kết luận của vòng trước, và nỗ lực bác bỏ chúng

Đề bài yêu cầu tôi **cố bác** hai kết luận, không phải xác nhận chúng. Tôi đã cố. Kết quả: **cả hai đứng vững về kết luận, nhưng một trong hai có một chân chống đỡ bị gãy.**

### §D-1 · "Charlemagne thuộc CE08 chứ không phải CE09" — ĐỨNG VỮNG, không bác được

**Các cách tôi thử bác, và vì sao chúng hỏng:**

*Thử 1 — "nhóm CE08 là 701–800, mà 800 chỉ là một năm lẻ; trọng tâm đời ông là 768–814, trung điểm 791, nhưng danh hiệu hoàng đế thì ở thế kỷ 9."* Hỏng. Tôi tự chạy `group_range('CE08')` → **`(701, 800)`** và `group_range('CE09')` → **`(801, 900)`**. Lễ đăng quang **25-12-800** rơi vào **sáu ngày cuối** của khoảng CE08, không phải CE09. Khối ghi chú nói đúng từng chữ.

*Thử 2 — "33/46 năm trị vì" có đếm đúng không?* Đúng. Trị vì 768–814 là 46 năm; phần nằm trong 701–800 là 768–800, tức **33 năm**; phần nằm trong CE09 là 801–814, **13 năm**. 33 > 13, và 33/46 = 72%.

*Thử 3 — "giai đoạn ảnh hưởng chính của ông là thời làm hoàng đế, tức 800–814."* Hỏng, và hỏng rõ. Mọi việc làm nên ảnh hưởng của ông đều ở thế kỷ 8: diệt Lombard **774**, thu phục Bavaria **788**, phá liên minh Avar **791–796**, Alcuin tới triều **782**, các *capitularia* về học thuật (*Admonitio generalis* **789**, *Epistola de litteris colendis* k. 784–785). Thế kỷ 9 chứa phần ông **giữ** một tước hiệu đã có, cộng với việc chia đế quốc (*Divisio regnorum* 806) — không phải phần tạo ra ảnh hưởng. Câu của khối ghi chú — *"thế kỷ 9 chỉ chứa phần ông **giữ** tước hiệu đã có"* — tôi không bác được.

*Thử 4 — "lint ép phải xếp CE09."* Hỏng. Đời 748–814 giao với cả `(701,800)` lẫn `(801,900)`, nên lint im lặng ở cả hai phương án ✓ đúng như khối ghi chú nói. Không có sức ép kỹ thuật nào.

*Thử 5 — tiền lệ ngược trong chính atlas.* Tôi tìm xem atlas có ca nào xếp theo năm mất không. Ngược lại: `CH04-CE05-09` **Āryabhaṭa** (476–550) được xếp nhóm **CE05** vì *Āryabhaṭīya* hoàn thành **499** — tức atlas đã từng chọn giai đoạn ảnh hưởng chống lại cả năm sinh lẫn năm mất, và khối ghi chú Āryabhaṭa ghi lại đúng việc ấy. `CH05-CE08-07` **Bêđa** (672–735) cũng vậy, xếp CE08 dù sinh ở thế kỷ 7. Tiền lệ **ủng hộ** Charlemagne-ở-CE08, không chống lại.

**Kết luận §D-1: kết luận của vòng trước đúng, lập luận của nó cũng đúng, và tôi không tìm được một kẽ nào.** Nó còn đúng theo một nghĩa mạnh hơn mức nó tự nhận: không chỉ "được phép xếp CE08" mà "xếp CE09 sẽ là lỗi", vì xếp CE09 chính là xếp theo **năm mất** — đúng cái lỗi mà §3 sinh ra để chặn.

### §D-2 · "Shankara `k. 700 – k. 750` + `Thấp`, và khung 788–820 là sản phẩm Đông phương học" — KẾT LUẬN ĐỨNG, MỘT CHÂN GÃY

**Phần đứng vững — niên đại và độ tin cậy.**

*Thử 1 — "`Thấp` là né lint."* Hỏng. `DATE_TOLERANCE["Thấp"] = None`, tức `Thấp` miễn mọi kiểm tra biên độ — nên về hình thức, đúng, `Thấp` là nấc "lint không hỏi". Nhưng nó cũng là nấc **đúng về nội dung**, và đây là ca điển hình nhất của toàn atlas: ba khung cạnh tranh là **thế kỷ 5 TCN** (truyền thống các maṭha), **700–750** và **788–820** — biên độ hơn **một nghìn ba trăm năm**. Không nấc nào khác dùng được. Và khối ghi chú tự nêu lý do thực chất (*"không có bi ký, không có tiền đúc, không có văn bản đương thời nào định danh ông"*) chứ không chỉ viện `None`.

*Thử 2 — "700–750 là lựa chọn thiểu số, chọn vì nó rơi gọn vào CE08."* Hỏng. Khung 700–750 (gắn với Hajime Nakamura) là khung mà các nguồn tham chiếu hiện hành mô tả là **được chấp nhận rộng rãi nhất hiện nay**, với 788–820 là khung "một số học giả vẫn dùng". Tôi cũng kiểm mục SEP mà atlas dẫn: **URL sống**, và nó **có** chống đỡ cả khung 700–750 lẫn việc Śaṅkara phản biện Pháp Xứng ✓. Đây không phải lựa chọn tiện lợi.

*Thử 3 — "nếu Shankara ở 700–750 thì ông trùng nhóm với chính Pháp Xứng mà ông phản bác."* Hỏng. `CH05-CE07-10` Pháp Xứng là **k. 600 – k. 660**, nhóm CE07. Không trùng.

**Phần gãy — hai chân chống đỡ, cả hai đều phải sửa.**

*(a) "Khung ấy không đến từ truyền thống Ấn Độ" — SAI ở đúng chữ then chốt.* C.P. Tiele (khối ghi chú viết nhầm là "K.P.") lấy con số 788–820 từ chuyên luận **Ấn Độ** *Āryavidyā-sudhākara* của Yajñeśvara Śāstrī, vốn dẫn lại *Śaṅkara-mandāra-saurabha* của Bhaṭṭa Nīlakaṇṭha. Giới Đông phương học **chọn và phổ biến** một niên đại Ấn Độ chứ không chế ra nó. Mệnh đề đúng — và là mệnh đề thực sự cần để bác bản nháp — là hẹp hơn: **788–820 không phải truyền thống của các maṭha**, và tuyệt đối không phải "truyền thống Śṛṅgeri". Chi tiết và câu thay thế ở §B-02.

*(b) "Vikramāditya II ủng hộ khung sớm" — SỐ HỌC KHÔNG RA.* Vikramāditya II của Cālukya trị vì **733–746**; "năm thứ mười bốn" của triều ấy rơi vào khoảng **746/747**, tức một Śaṅkara **sinh giữa thế kỷ 8** — muộn hơn khung `k. 700 – k. 750` mà mục dùng, và **gần 788–820 hơn**. Chữ "sớm" chỉ đúng khi so với 788–820; nó bị viết như một kết luận tuyệt đối và bị dùng để chống đỡ chính cái khung nó không chống đỡ. Chi tiết ở §B-02.

*(c) Thêm một chân yếu mà vòng trước không nêu:* cái **chặn đầu trên** (Vācaspati Miśra "nửa đầu thế kỷ 9") phụ thuộc vào việc đọc con số **898** trong *Nyāyasūcīnibandha* theo lịch Vikrama (**841 CN**) hay lịch Śaka (**976 CN**) — chênh **135 năm**, chưa có đồng thuận. Nếu đọc theo Śaka thì cái chặn ấy **không loại được 788–820 nữa**. Chi tiết ở §A-11.

**Kết luận §D-2:** `k. 700 – k. 750 CN` + `Thấp` **đúng và nên giữ**. Nhưng ba trong số các lý lẽ chống đỡ nó phải được viết lại: (a) đổi "truyền thống Ấn Độ" thành "truyền thống của các maṭha"; (b) bỏ mệnh đề "Vikramāditya II ủng hộ khung sớm" hoặc sửa cho đúng số học; (c) rào lại Vācaspati Miśra. Sau khi sửa, kết luận **yếu đi về mức chắc chắn** — 788–820 không bị loại dứt khoát như khối ghi chú trình bày, nó chỉ kém được ủng hộ hơn — nhưng chính vì thế mà `Thấp` càng là nấc đúng.

---

## §E · Cân bằng vùng: có mục nào được chọn, hoặc được gán `vùng:`, vì lý do thống kê không?

Đề bài hỏi thẳng, nên tôi trả lời thẳng. Phải tách **hai câu hỏi khác nhau** mà khối ghi chú §B-15 trộn làm một:

- **(i) Có `vùng:` nào bị gán sai để làm đẹp bảng không?** — Đây là điều CONTRIBUTING.md cấm tuyệt đối (quy ước vùng số 4).
- **(ii) Thống kê vùng có ảnh hưởng tới việc chọn ai vào 12 suất không?** — Đây là chuyện khác, và CONTRIBUTING.md **không** cấm nó rõ ràng.

Câu trả lời của tôi: **(i) KHÔNG. (ii) CÓ, và khối ghi chú tự thừa nhận.**

### §E-1 · Abu Muslim · `Trung Á` — gán ĐÚNG, không phải thao tác

Tôi soi kỹ vì đây là ô mỏng nhất (Trung Á trước nhóm này chỉ có 1 người) nên lợi ích thống kê của việc gán vào đây là lớn nhất.

**Dữ kiện:** trường `nơi:` ghi *"Merv và Khurasan, nay thuộc Turkmenistan và đông bắc Iran"*. Giai đoạn ảnh hưởng của ông là **745/747–755**, và toàn bộ nó diễn ra ở Khurasan: được phái **từ Iraq về Khurasan** năm 745, giương cờ đen năm 747, chiếm **Merv** cuối năm 747, rồi làm tổng đốc Khurasan cho tới khi bị al-Mansur xử tử năm 755.

**Áp quy ước 1 (nơi hoạt động chính, không phải nơi sinh):** nơi hoạt động chính là Merv/Khurasan. Merv nay thuộc Turkmenistan. Theo nghĩa còn lại của "Trung Á" trong từ vựng chín ô của atlas — Transoxiana và Iran đông — đây là **Trung Á**. Không cần viện tới thống kê để ra kết quả này.

**Phép thử ngược mà tôi tự chạy:** giả sử tôi gán ông `Trung Đông/Bắc Phi` thay vào. Lý lẽ duy nhất đỡ được là "ông là tác nhân của một cuộc cách mạng trong thế giới Hồi giáo, mà trọng tâm thế giới ấy ở Iraq–Syria". Nhưng lý lẽ ấy là lý lẽ về **chủ đề**, không phải về **địa lý**, và quy ước 1 nói rõ atlas đo địa lý. Nếu chấp nhận nó thì cũng phải chuyển Zarathustra, và mọi người Ba Tư trong atlas, về Trung Đông — tức phá chính từ vựng. Vậy **gán `Trung Á` không chỉ được phép mà là bắt buộc.**

**KẾT LUẬN §E-1: `vùng: Trung Á` của Abu Muslim là kết quả của quy ước, không phải của bảng thống kê.** Nhưng phải nói kèm hai điều:

1. **Lập luận phòng thủ mà khối ghi chú đưa ra thì hỏng** — "cặp đối xứng Abu Muslim sinh ở Kufa / Abu Hanifa có thể sinh ở Trung Á" sai cả hai vế (§B-10). Mỉa mai ở chỗ: khối ghi chú dựng một bằng chứng sai để bảo vệ một kết luận đúng. Phải sửa, vì nếu một vòng sau phát hiện bằng chứng sai, họ có thể kết luận nhầm rằng cả việc gán vùng cũng sai.
2. **Ô `Trung Á = 2` vẫn mỏng hơn con số gợi ý.** Người thứ hai là Zarathustra `CH02-BCE06-09`, mà trường `nơi:` của chính mục ấy ghi *"đông Iran **hoặc** Trung Á"*. Tức ô này gồm **một người chắc chắn và một người đang để ngỏ**. Khối ghi chú §B-10 có nói điều này ✓ — đáng khen, vì nó tự làm yếu con số của mình.

### §E-2 · Yikʼin Chan Kʼawiil · `Châu Mỹ` — `vùng:` không có đất cho thao tác; câu hỏi thật nằm ở việc CHỌN

**Về trường `vùng:`: không có lựa chọn nào để thao tác.** Tikal ở Petén, Guatemala. Trong từ vựng chín ô, không ô nào khác nhận được. Mức tự do bằng không, nên theo định nghĩa đây **không thể** là thao tác thống kê.

**Nhưng câu hỏi thật là câu hỏi chọn, và ở đó câu trả lời phức tạp hơn.** Nhóm có 12 suất và 15 ứng viên bị loại, trong đó bốn người mà khối ghi chú nói *"sẽ chắc chắn vào atlas nếu trần là 16"* — Harun al-Rashid, Malik ibn Anas, Ibn Ishaq, An Lộc Sơn. Ba trong bốn thuộc **Trung Đông/Bắc Phi**. Và khối ghi chú §B-15 nói thẳng rằng việc *"cắt từ tám ứng viên xuống bốn"* cho vùng ấy là để *"giữ tỷ lệ atlas đứng nguyên"*.

**Đó là lý luận thống kê, và nó đã tác động tới việc chọn.** Tôi không thấy lý do phải giấu điều đó — khối ghi chú cũng không giấu. Nhưng nó cần được gọi đúng tên.

**Vậy Yikʼin có đứng được một mình không?** Kiểm theo bốn tiêu chí:
- **(a) phạm vi — ông thua.** Hệ quả của ông dừng ở vùng đất thấp Maya. So với Malik ibn Anas, người mà trường phái luật trải từ Bắc Phi tới Tây Phi và còn hiệu lực hôm nay, Yikʼin thua rõ rệt theo tiêu chí (a).
- **(c) tính nguyên bản và (d) counterfactual — ông thắng.** Ông phá được thế đối đầu Tikal–Calakmul kéo dài hai thế kỷ mà những người tiền nhiệm không phá được; nếu không có ông, không hiển nhiên là Tikal sẽ trở lại vị thế ấy. Chuỗi sự kiện được chính triều đình ông khắc bằng Long Count, tức niên đại tuyệt đối tới từng ngày — chất lượng bằng chứng hiếm trong toàn nhóm.
- **Và có một khuyết tật cấu trúc mà atlas đã tự ghi nhận**: mục Pakal `CH05-CE07-12` viết thẳng *"trước 1492 không tồn tại đường vật lý nào để ảnh hưởng ra khỏi bán cầu"*. Tức tiêu chí (a) **loại trừ vĩnh viễn** toàn bộ châu Mỹ tiền Columbus theo cấu trúc, không theo công trạng.

**KẾT LUẬN §E-2 — trả lời thẳng:** việc chọn Yikʼin Chan Kʼawiil **không** thuần tuý là kết quả của bốn tiêu chí áp một cách trung lập. Nó dựa vào (c) và (d) **cộng với** một chính sách ngầm rằng khuyết tật cấu trúc của tiêu chí (a) không được phép khiến châu Mỹ tiền Columbus vĩnh viễn trống. Tôi cho rằng chính sách ấy **đúng**. Nhưng nó đang là **ngầm**, và một chính sách ngầm thì không phân biệt được với việc lấp chỉ tiêu.

**Đề nghị cụ thể (NÊN SỬA, ở CONTRIBUTING.md chứ không ở `ch05.md`):** viết hẳn một đoạn nói rằng tiêu chí (a) phạm vi được đo **trong phạm vi mạng lưới tiếp xúc tồn tại ở thời điểm ấy**, chứ không đo trên bản đồ thế giới hiện đại. Khi viết thế, Yikʼin đứng được bằng chính tiêu chí (a) — ông là thế lực mạnh nhất trong mạng lưới của ông — và atlas không còn phải dựa vào một chính sách không tên.

### §E-3 · Mười hai mục còn lại: không có mục nào bị gán `vùng:` sai

Tôi kiểm từng mục theo quy ước 1:

| Mục | `nơi:` | `vùng:` | Đúng quy ước 1? |
|---|---|---|---|
| Abu Muslim | Merv, Khurasan | Trung Á | ✓ (§E-1) |
| Al-Mansur | Baghdad, Iraq | Trung Đông/Bắc Phi | ✓ |
| Jaʿfar al-Sadiq | Medina | Trung Đông/Bắc Phi | ✓ |
| Abu Hanifa | Kufa và Baghdad | Trung Đông/Bắc Phi | ✓ — và mục **tự nêu** quy ước ra để giải trình |
| Sibawayh | Basra, Baghdad (gốc Shiraz) | Trung Đông/Bắc Phi | ✓ — gốc gác để ở `nơi:`, không kéo `vùng:` |
| Charlemagne | Aachen, vương quốc Frank | Châu Âu | ✓ |
| Bêđa | Wearmouth–Jarrow | Châu Âu | ✓ |
| Tăng Nhất Hạnh | Trường An | Đông Á | ✓ |
| Đỗ Phủ | Trường An, Thành Đô | Đông Á | ✓ |
| Trisong Detsen | Lhasa, Samye | Đông Á | ✓ — theo quy ước 3 (không có ô Nội Á), nhất quán với `CH05-CE07-11` |
| Ādi Shankara | Kerala và khắp tiểu lục địa | Nam Á | ✓ |
| Yikʼin Chan Kʼawiil | Tikal, Guatemala | Châu Mỹ | ✓ (§E-2) |

**Hai mục đáng khen riêng:** `CH05-CE08-04` Abu Hanifa và `CH05-CE08-05` Sibawayh đều có gốc gác ở một vùng khác vùng được gán, và **cả hai đều xử lý đúng** — ghi gốc gác vào trường `nơi:` và để `vùng:` theo nơi hoạt động, kèm một câu giải trình ở Abu Hanifa. Nếu có ý định làm đẹp bảng, đây chính là hai chỗ dễ làm nhất (chuyển Abu Hanifa sang Trung Á sẽ nâng ô mỏng nhất từ 2 lên 3), và **không chỗ nào bị làm.** Đó là bằng chứng thực tế mạnh hơn "cặp đối xứng" hỏng mà §B-10 đưa ra.

### §E-4 · Trả lời gọn câu hỏi của đề bài

> **"Có mục nào được chọn hoặc được gán `vùng:` vì lý do thống kê chứ không phải lý do lịch sử không?"**

- **Gán `vùng:`: không có mục nào.** Cả 12 trường `vùng:` đều ra đúng kết quả khi áp quy ước 1 một cách trung lập, và hai ca dễ thao tác nhất (Abu Hanifa, Sibawayh) đều được xử lý theo hướng **bất lợi** cho bảng thống kê.
- **Chọn ai vào 12 suất: có, một phần.** Việc giới hạn Trung Đông/Bắc Phi ở 4 suất được khối ghi chú §B-15 nói thẳng là để giữ tỷ lệ. Việc giữ một suất cho châu Mỹ dựa vào một chính sách ngầm bù cho khuyết tật cấu trúc của tiêu chí (a). Cả hai đều là quyết định tôi **tán thành về nội dung**, nhưng cả hai đều nên được viết thành quy ước ở CONTRIBUTING.md thay vì nằm trong ghi chú của một nhóm.
- **Tuyên bố cần sửa:** câu *"nhúc nhích bằng hai người có nguồn đương thời... chứ không bằng việc hạ thanh chắn"* ở §B-15 **đúng với Yikʼin** (bi ký Long Count) nhưng **không đúng với Abu Muslim** theo cách khối ghi chú ngụ ý — Abu Muslim không có nguồn đương thời; văn khố Mugh là của **Divashtich, người bị loại**, không phải của ông. Đọc nhanh rất dễ hiểu thành "Abu Muslim có văn khố Mugh đứng sau". **NÊN SỬA.** Đề nghị: *"...và nhúc nhích mà không hạ thanh chắn: Yikʼin Chan Kʼawiil có bi ký Long Count đương thời, còn Abu Muslim được chọn theo tiêu chí phạm vi — ông đổi được một triều đại, điều mà Divashtich, người có văn khố tốt hơn hẳn, không làm được."*

---

## §F · Bảng tổng kết

### F-1 · BẮT BUỘC SỬA (9)

| # | Vị trí | Vấn đề | Loại lỗi |
|---|---|---|---|
| 1 | `CE08-05` Sibawayh, "Tư tưởng" | *"bộ mô tả ngôn ngữ còn nguyên vẹn cổ nhất ngoài truyền thống Ấn Độ của Pāṇini"* — Donatus (TK 4) và Priscianus (k. 500) còn nguyên và cổ hơn | Sự kiện sai |
| 2 | `CE08-08` Yi Xing, "Tư tưởng" | *"Lịch Đại Diễn… dùng suốt phần còn lại của nhà Đường"* — thực tế 729–762, khoảng 33 năm; Đường tới 907 | Sự kiện sai |
| 3 | `CE08-12` Yikʼin, "Tư tưởng" | *"Đền IV, kim tự tháp cao nhất thế giới Maya"* — La Danta ở El Mirador (~72 m) cao hơn Đền IV (70 m) | Sự kiện sai |
| 4 | Ghi chú Shankara, tiêu đề + câu mở | *"Khung 788–820… không đến từ truyền thống Ấn Độ"* — C.P. Tiele lấy nó từ *Āryavidyā-sudhākara* của Yajñeśvara Śāstrī | Sự kiện sai |
| 5 | Ghi chú Shankara | *"Vikramāditya II… tức ủng hộ khung **sớm**"* — năm thứ 14 của triều 733–746 là k. 746, ngả về khung **muộn** | Suy luận sai |
| 6 | Ghi chú "Wikidata khai độ chính xác" | *"cả `P31` lẫn `P570` đều không có tham chiếu nào"* — `P31` là property sai; `P569` của `Q3301` **có** tham chiếu | Sự kiện sai + dẫn sai property |
| 7 | Ghi chú "Ô Trung Á" | *"Abu Muslim sinh ở Kufa"* (sai: Merv hoặc gần Isfahan) và *"Abu Hanifa có thể sinh ở Trung Á"* (sai: sinh ở Kufa) — "cặp đối xứng" không tồn tại | Hai sự kiện sai, chống đỡ một kết luận đúng |
| 8 | Ghi chú Châu Phi | *"Aksum ngừng đúc tiền vào đầu thế kỷ 8"* — thực tế nửa đầu TK 7, đợt cuối k. 620 | Sự kiện sai (sửa xong thì lập luận **mạnh hơn**) |
| 9 | Ghi chú Châu Đại Dương | *"đặt việc định cư quần đảo Society ở k. 1200–1290"* — bài báo cho Society k. **1025–1120**; 1190–1290 là các đảo **còn lại** | Chép nhầm số liệu giữa hai nhóm đảo |

### F-2 · NÊN SỬA (18)

| # | Vị trí | Vấn đề |
|---|---|---|
| 10 | `CE08-01` Abu Muslim | *"Trong ba năm"* — mốc đếm không rõ (745? 747?) |
| 11 | `CE08-02` Al-Mansur | Lý do `Trung bình` ghi *"các nguồn cho ba ngày mất khác nhau"* — sai hai lần: Wikidata chỉ có **hai** `P570`, và `DATE_TOLERANCE` đo bằng **năm** nên chênh lệch ngày không hạ được nấc. Biến số thật là năm sinh (709/713/714) |
| 12 | `CE08-02` Al-Mansur | *"Abu Hanifa chết trong ngục Baghdad năm 767"* — viết như sự kiện |
| 13 | `CE08-04` Abu Hanifa | *"bị tù… và chết trong ngục Baghdad"* — Melchert, chính nguồn thứ nhất của mục, đọc đây là truyền thuyết thánh hoá đời sau (vi phạm quy tắc 7) |
| 14 | `CE08-06` / `CE08-12` | *"năm sinh của Charlemagne… vẫn còn bốn phương án"* — `Q3044` có 5 phát biểu / **3 năm** (742, 747, 748) |
| 15 | `CE08-06` Charlemagne | *"Charles Martel… không để lại thiết chế nào"* — phủ định đúng cái sử học coi là di sản chính của ông |
| 16 | `CE08-08` Yi Xing | `năm: 683–727` thiếu "k." dù chính độ chênh 10 năm là lý do hạ xuống `Trung bình` |
| 17 | `CE08-08` Yi Xing | *"tổ tiên của mọi đồng hồ cơ"* — luận đề của Needham, chưa chứng minh đường truyền; mục tự mâu thuẫn với kỷ luật "tách hai tầng" của chính nó |
| 18 | `CE08-10` Trisong Detsen | *"sắc chỉ năm 791"* — 779 là niên đại cạnh tranh; trụ đá Samye không mang niên đại |
| 19 | `CE08-10` Trisong Detsen | *"Phía Ấn Độ thắng"* — văn bản Hán ở Đôn Hoàng chép ngược lại |
| 20 | `CE08-11` Shankara | *"Vācaspati Miśra sớ cho ông ở nửa đầu thế kỷ 9"* — 841 so với 976 tuỳ lịch Vikrama hay Śaka, chênh 135 năm; đây là **chân chịu lực** của lập luận |
| 21 | `CE08-12` Yikʼin | `trị vì 734–766` thiếu "k." dù mục tự nói *"năm mất còn để ngỏ"*; `Q2620151` có `P570 = no value` |
| 22 | Ghi chú Shankara | *"K.P. Tiele"* → **C.P. Tiele** (Cornelis Petrus Tiele, 1830–1902) |
| 23 | Ghi chú Jabir | *"không có công trình sau 2010 nào đứng về phía ông"* — mệnh đề phủ định toàn xưng; hạ xuống "tôi không tìm được…" |
| 24 | Ghi chú "Nhóm chật nhất" | *"Ibn Ishaq (Sīra, tiểu sử Muhammad **đầu tiên**)"* — là bản **sớm nhất còn lại**, và chỉ còn qua bản hiệu đính của Ibn Hishām |
| 25 | Ghi chú Châu Phi | *"nguồn duy nhất là History of the Patriarchs…, một biên niên **soạn muộn**"* — phần chép chuyện Kyriakos là *Life of Michael* của John the Deacon, k. **768–770**, gần như đương thời |
| 26 | Ghi chú Châu Đại Dương | Năm xuất bản Wilmshurst et al. là **2011**, không phải 2010 |
| 27 | Ghi chú "Hình dạng của thế kỷ" | *"33,2%"* → **33,0% (73/221)**; con số cũ lấy từ bảng cơ sở của vòng cổng, đã lạc hậu |
| 28 | Ghi chú "Hình dạng của thế kỷ" | *"nhúc nhích bằng hai người có nguồn đương thời"* — văn khố Mugh là của **Divashtich, người bị loại**, không phải của Abu Muslim |

Và một đề nghị không nằm trong `ch05.md`:

| # | Vị trí | Đề nghị |
|---|---|---|
| 29 | `CONTRIBUTING.md` | Viết rõ rằng tiêu chí (a) phạm vi được đo **trong mạng lưới tiếp xúc tồn tại ở thời điểm ấy**, không trên bản đồ thế giới hiện đại. Không có câu này, suất châu Mỹ tiền Columbus không phân biệt được với lấp chỉ tiêu (§E-2) |

### F-3 · CÂN NHẮC (11)

| # | Vị trí | Vấn đề |
|---|---|---|
| 30 | `CE08-01` | `Ảnh hưởng tới: CH05-CE08-02 · kế thừa` đọc ngược với việc al-Mansur xử tử ông |
| 31 | `CE08-02` | *"năm thế kỷ"* Baghdad giữ vị trí trung tâm |
| 32 | `CE08-03` và cả nhóm | `trực tiếp` dùng cho các cặp **không cùng thời** (Ali d. 661 → Jaʿfar b. k. 702, cách 41 năm). Ít nhất 4 cặp trong nhóm có hình dạng này. Bêđa → Isiđôrô là ca **hợp lệ** (có dấu vết văn bản). Quy ước cần được viết ra |
| 33 | `CE08-03` | Căng thẳng giữa lời rào trong phần văn xuôi và liên kết `Malik ibn Anas · trực tiếp` |
| 34 | `CE08-05` | `CH02-BCE05-08 · tương đồng độc lập` — có dòng học thuật đặt giả thuyết Sibawayh *gián tiếp* biết ngữ pháp Ấn Độ; ô `suy đoán học giả` đang gánh việc mà tên quan hệ không gánh |
| 35 | `CE08-06` | *"các bản chép **thời ông**"* — phần lớn bản chép Carolingian thuộc TK 9, sau khi ông mất |
| 36 | `CE08-09` | *"biến cố lớn nhất thế kỷ 8 ở Đông Á"* — superlative, bảo vệ được nhưng không phải dữ kiện |
| 37 | `CE08-09` | `Ảnh hưởng tới: CH90-CE19_20-01` — liên kết từ track chính sang track phụ lục; cần Owner xác nhận có được phép |
| 38 | `CE08-10` | *"người kế vị ông"* — Tride Songtsen là **con**, không phải người kế vị ngay |
| 39 | `CE08-12` | `Calakmul… · phản bác · trực tiếp` — dùng `phản bác` cho một quan hệ quân sự với một **thành bang** |
| 40 | Ghi chú Divashtich | *"tháp im lặng"* (*dakhma*) — các nguồn chép ông bị đóng đinh trên một **naus**, nhà quàn hài cốt |

### F-4 · [KHÔNG KIỂM ĐƯỢC] (9)

| Mệnh đề | Lý do |
|---|---|
| Al-Mansur: *"các nguồn cho **ba** ngày mất khác nhau"* | Wikidata chỉ có 2 `P570`; không tìm được danh sách học thuật cho 3 |
| Abu Hanifa: *"các nguồn cổ điển cho **bốn** năm sinh"* | Không tìm được danh sách 4 năm sinh cạnh tranh |
| Charlemagne: *"**bốn** phương án"* năm sinh | `Q3044` cho 3 năm phân biệt; không tìm được nguồn cho con số 4 |
| Yikʼin: mốc kết thúc triều **766** | Không có Martin & Grube 2008 để đối chiếu; nguồn mở được cho 746/755; `P570 = no value` |
| Jabir: *"không có công trình sau 2010 nào đứng về phía Sezgin"* | Mệnh đề phủ định toàn xưng, không có công cụ xác minh |
| Jabir: hai mã HTTP (202 với 0 byte; 429 Varnish) | Phụ thuộc thời điểm và IP; tôi không kiểm lại. Thư mục Delva 2017 thì tôi xác minh lại được qua Crossref ✓ |
| Wilmshurst et al.: nội dung bản gốc | `pnas.org` trả **HTTP 403**; PubMed trả tường cookie. Các con số lấy từ văn bản tóm tắt của công cụ tìm kiếm, **không phải từ bản gốc** |
| Nakamura 1983 có đặt Vācaspati Miśra ở nửa đầu TK 9 không | Không có bản sách |
| Kyriakos: vị trí trong danh sách vua Makuria (sau Markos / giữa Merkurios và Zacharias I) | Xác nhận được rằng có bất đồng, không xác nhận được chi tiết từng bản |

### F-5 · Những gì KHÔNG có lỗi

- **Cổng Q-ID: 12/12 đúng người, 12/12 `P31 = Q5`** (§0). Không mục nào trỏ nhầm sang một đồng danh hay một công trình.
- **Quy tắc 8: 36/36 ID trong vùng CE08 tồn tại và trỏ đúng người** (§C-1). Không có ca "ID hợp lệ, sai người".
- **Quy tắc 6: sạch** (§C-2). 14 tên được nêu là ứng viên bị loại, **không ai** có mục ở chỗ khác. Hai ca xử lý mẫu mực (Pakal; ba nhân vật Việt Nam).
- **Không ai bị viết như thể đã có mục** (§C-3). Lý Bạch, Alcuin và các tên tương tự đều ở dạng chữ tự do, không phải ID.
- **Từ vựng cố định: sạch.** Mọi mục ≤ 2 `lĩnh vực` nằm trong `FIELDS`, đúng 1 `vùng` trong `REGIONS`, `độ tin cậy niên đại` trong `CONFIDENCE`, số `Ảnh hưởng tới` là 2/2/3/2/2/3/3/2/3/2/3/2 — **tất cả ≤ 3**.
- **`vùng:` — không mục nào bị gán vì lý do thống kê** (§E). Hai ca dễ thao tác nhất (Abu Hanifa, Sibawayh) đều được xử lý theo hướng **bất lợi** cho bảng.
- **Charlemagne ở CE08: đúng, và tôi không bác được** (§D-1).
- **Shankara `k. 700 – k. 750` + `Thấp`: đúng, nên giữ** (§D-2) — dù ba lý lẽ chống đỡ phải viết lại.

### F-6 · Đánh giá chung

Mười hai mục và mười lăm khối ghi chú có **chất lượng trên trung bình rõ rệt**. Phần lớn các kết luận lớn đứng vững, hai kết luận mà đề bài yêu cầu tôi công kích đều sống sót, và ba trong bốn cổng hình thức (Q-ID, quy tắc 6, quy tắc 8, từ vựng) **sạch tuyệt đối** — điều hiếm.

Kiểu lỗi còn lại tập trung vào **một dạng duy nhất, lặp đi lặp lại**: một mệnh đề đúng được đẩy lên thành một **tuyệt đối** hoặc một **ưu tiên thời gian** mà nó không chịu nổi. "Cổ nhất ngoài Pāṇini", "suốt phần còn lại của nhà Đường", "cao nhất thế giới Maya", "tổ tiên của mọi đồng hồ cơ", "không để lại thiết chế nào", "không có công trình nào sau 2010", "Phía Ấn Độ thắng". Bảy trong chín lỗi BẮT BUỘC SỬA và phần lớn nhóm NÊN SỬA đều có đúng hình dạng ấy. Đề nghị cho vòng sau: **đọc lại bản thảo một lượt chỉ để săn các từ "nhất", "mọi", "duy nhất", "suốt", "không… nào"** — mỗi lần gặp, hỏi nguồn nào chống đỡ.

Dạng lỗi thứ hai, ít hơn nhưng nguy hiểm hơn, là **bằng chứng sai bảo vệ kết luận đúng** (mục #7, cặp đối xứng Abu Muslim/Abu Hanifa; và mục #5, số học Vikramāditya). Nguy hiểm vì nếu một vòng sau phát hiện bằng chứng hỏng, họ có thể lật cả kết luận — mà kết luận thì đúng.

*Hết báo cáo. Mọi truy vấn HTTP trong vòng này dùng User-Agent `history-atlas/0.1 (research)`; không có thông tin cá nhân nào xuất hiện trong header, URL, query string, payload hay trong báo cáo này.*
