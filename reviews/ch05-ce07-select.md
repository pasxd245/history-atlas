# Bình duyệt độc lập — chọn 3 suất còn lại cho nhóm CE07 (Ch5)

**Người duyệt:** agent bình duyệt độc lập (không viết Ch5).
**Ngày:** 2026-10-31.
**Phạm vi:** 3 suất trống của `CH05-CE07` (9/12 đã viết, không xét lại).
**Tiêu chí:** (a) phạm vi · (b) độ bền · (c) tính nguyên bản · (d) counterfactual — `CONTRIBUTING.md`.
**Nhãn độ chắc:** [CAO] / [TRUNG BÌNH] / [THẤP] gắn cho từng phán đoán của người duyệt, tách biệt với trường `độ tin cậy niên đại:` của atlas.

---

## 0. Ba phát hiện phải đọc trước khi dùng báo cáo này

### 0.1 Q311215 KHÔNG phải Pakal — là một chi bướm

Kiểm bằng `wbgetentities`:

```
Q311215 | EN: Colias | desc: genus of insects | P31: ['Q16521']
```

`P31 = Q16521` (taxon), không phải `Q5`. Owner nghi đúng.

**Q-ID đúng: `Q371384`** — `K'inich Janaab' Pakal`, `P31: Q5`, `P569: 603-03-23`, `P570: 683-08-28`, enwiki `Kʼinich Janaabʼ Pakal`, viwiki `K'inich Janaab' Pakal`, 34 sitelinks. [CAO]

**Bẫy kề bên — đừng lấy nhầm lần nữa:** `Q641749` là **`Janaab' Pakal`** (enwiki "Janahb Pakal"), một người **khác**, mất **612**, không phải vua của Đền Bi ký. `Q4017694` là **Janaab Pakal III**. Ba người cùng tên trong một triều đại Palenque; chỉ `Q371384` là người sinh 603–mất 683. [CAO]

### 0.2 Wikidata của Dharmakīrti tự mâu thuẫn — chép vào là lint chặn build

```
Q457990 | P569: +0700-01-01 | P570: +0660-01-01
```

Năm sinh **sau** năm mất 40 năm. `CONTRIBUTING.md` liệt "năm mất trước năm sinh" là **lỗi chặn build**. Đây đúng loại ca mà ghi chú §49 cảnh báo: *"Khớp Wikidata không đồng nghĩa với đúng."* Xử lý ở §3 dưới. [CAO]

### 0.3 Phụ lục ch90 là **Việt Nam**, không phải Đông Nam Á

Đề bài mô tả ch90 là "phụ lục Đông Nam Á riêng". Đọc `content/ch90.md` dòng 1:

> `# Chapter 90 · Phụ lục · Việt Nam qua các thời kỳ`

Các mục trong đó **có** mang `vùng: Đông Nam Á` (An Dương Vương, Triệu Đà…) nhưng chỉ phủ **Việt Nam**. Thế giới Mã Lai – hải đảo, Khmer, Môn, Pyu, Java **không** được phụ lục này che. Hệ quả cho phần cân nhắc vùng ở §8: lập luận "Đông Nam Á đã có phụ lục đỡ" **yếu hơn** đề bài giả định. [CAO]

---

## 1. Harsha / Harshavardhana — `Q216895`

**Kiểm Q-ID:** ĐÚNG NGƯỜI. `P31: Q5`, EN `Harsha`, VI `Harsha`, desc "Indian king", `P569: 590`, `P570: 647`, `P39: Q39018` (monarch), 52 sitelinks. [CAO]

### Chấm điểm

| | Điểm | Giải thích |
|---|---|---|
| (a) phạm vi | **2** | Quyền lực dừng ở đồng bằng sông Hằng. Thua Pulakeshin II ở sông Narmada nên không xuống được Deccan — tức không kiểm soát nổi hết chính tiểu lục địa của mình. Ra ngoài Nam Á: vài sứ bộ Đường (Vương Huyền Sách) và việc được Huyền Trang chép lại. Đó là *được ghi chép* bởi một mạng lưới xuyên vùng, không phải *tác động lên* nó. |
| (b) độ bền | **2** | Đế quốc tan **ngay** khi ông chết năm 647 — không người kế vị, bề tôi Arjuna cướp ngôi trong vòng mấy tháng. Thứ sống dai hơn lại không phải nhà nước: *Harṣacarita* của Bāṇabhaṭṭa mở ra thể tiểu sử–lịch sử bằng văn xuôi Sanskrit, và ba vở kịch mang tên ông vẫn được đọc. Nhưng công của phần đó phần lớn thuộc về Bāṇa. |
| (c) nguyên bản | **2** | Mô hình cai trị là phục dựng khuôn Gupta, không mới. Phần nguyên bản thật — văn chương — lại là phần tác quyền đang tranh cãi (xem §1.3). |
| (d) counterfactual | **2** | Thấp. Bắc Ấn vỡ lại đúng trạng thái cũ ngay sau 647, nên 40 năm của ông là một quãng chen giữa chứ không phải một bước ngoặt. Không có Harsha thì Huyền Trang vẫn sang, Nalanda vẫn hoạt động, Pulakeshin vẫn giữ Deccan. |
| | **8/20** | |

### Bằng chứng sơ cấp

Mạnh và đa dạng — đây là điểm sáng nhất của hồ sơ Harsha. [CAO]

- **Bản khắc đồng do chính triều đình ông ban:** bản Banskhera và bản Madhuban, cả hai mang chữ ký *Śrī Harṣaḥ*; ấn Sonepat. Đây là tư liệu đương thời, không qua trung gian.
- **Niên hiệu Harsha** khởi từ 606 CN, dùng tiếp ở Nepal sau khi ông mất.
- **Huyền Trang**, *Đại Đường Tây Vực ký* — nhân chứng nước ngoài ở Ấn Độ 630–643, tức ở ngay trong triều Harsha.
- **Bāṇabhaṭṭa**, *Harṣacarita* — tụng ca cung đình, viết dở dang; là nguồn thiên vị nhưng đương thời.
- Sứ bộ Vương Huyền Sách (Đường) chép trong thư tịch Trung Hoa.

**Đề xuất `độ tin cậy niên đại:` → `Cao`.** 590–647, lên ngôi 606. Niên hiệu riêng cộng bản khắc đương thời cho một khung chặt trong dung sai ±5 năm. [CAO]

### Mệnh đề phổ thông đang bị học giới tranh luận

1. **"Harsha thống nhất Bắc Ấn / là hoàng đế lớn cuối cùng của Ấn Độ Hindu."** Đây là khung của sử học dân tộc chủ nghĩa đầu thế kỷ 20. Học giới hiện nay đọc quyền lực của ông như một **thế bá chủ lỏng (paramountcy) trên một liên minh chư hầu**, không phải một nhà nước tập quyền kiểu Gupta. Đừng in chữ "đế quốc" mà không kèm điều kiện. [TRUNG BÌNH]
2. **"Harsha cải sang đạo Phật."** Huyền Trang vẽ ông thành thí chủ Phật giáo thuần thành; nhưng **bản khắc của chính ông** dùng hiệu *paramamāheśvara* (tín đồ Shiva tối thượng), và *Harṣacarita* cho thấy thờ cả Shiva lẫn Surya. Cách đọc hiện nay: **thí chủ đa tôn giáo**, không phải người cải đạo. Chỗ này là ví dụ sách vở của việc một nguồn đương thời (Huyền Trang) vẫn có thể thiên vị theo lợi ích của chính người viết. [TRUNG BÌNH–CAO]
3. **Tác quyền ba vở kịch** *Ratnāvalī*, *Priyadarśikā*, *Nāgānanda*. Truyền thống Ấn Độ đã ghi ngờ vực từ sớm (thuyết Dhāvaka viết thuê). Không được viết "Harsha sáng tác" như một sự kiện. [TRUNG BÌNH]
4. **Đại hội Prayāga 5 năm một lần**, nơi ông bố thí sạch kho. Chỉ có **một** nguồn: Huyền Trang. Không bản khắc nào xác nhận. [CAO]

### Rủi ro trùng lặp trong nhóm

CE07 đã có **Brahmagupta** ở Nam Á. Thêm Harsha → Nam Á 2/12, không mở vùng mới nào.

---

## 2. Thánh Đức Thái tử / Shōtoku — `Q263972`

**Kiểm Q-ID:** ĐÚNG NGƯỜI. `P31: Q5`, EN `Prince Shōtoku`, VI `Thánh Đức Thái tử`, `P569: 574-02-07`, `P570: 622-04-08`, `P27: Q17` (Nhật Bản), 43 sitelinks.
**Chú ý:** chính mô tả Wikidata đã tự gắn cảnh báo — *"semi-legendary Japanese prince"*. [CAO]

### Chấm điểm

| | Điểm | Giải thích |
|---|---|---|
| (a) phạm vi | **1** | Quần đảo Nhật Bản, không hơn. Chiều tác động chủ yếu là **vào** — Nhật tiếp nhận mô hình Tùy–Bách Tế; không có dòng chảy ngược ra lục địa. Thư "Thiên tử xứ mặt trời mọc" gửi Tùy Dạng Đế là một cử chỉ ngoại giao đáng nhớ, nhưng *Tùy thư* ghi người gửi là **quân chủ nước Oa** (tức Suiko), không đích danh ông. |
| (b) độ bền | **3** | Rất cao — **nhưng là độ bền của tín ngưỡng, không phải của con người**. Giáo phái Thái tử kéo 1400 năm, Hōryū-ji còn đứng, mặt ông in trên tiền giấy Nhật tới tận 1984. Chấm 3 là chấm cho sự vật tồn tại thật ấy, đồng thời từ chối tính nó thành thành tựu của người thế kỷ 7. |
| (c) nguyên bản | **2** | Đúng cái phần được coi là nguyên bản — Hiến pháp 17 điều, *Tam kinh nghĩa sớ* — lại đúng cái phần tác quyền đang bị bác (§2.3). Phần ít bị ngờ nhất là mười hai cấp mũ (603) và các sứ bộ sang Tùy, mà cả hai đều là nhập khẩu thể chế lục địa. |
| (d) counterfactual | **2** | Thấp. Động lực Hán hoá của Nhật là cấu trúc, do thị tộc Soga và nữ hoàng Suiko đẩy; Soga no Umako mới là người nắm thực quyền. Bỏ Umayado ra khỏi thế kỷ 7, quỹ đạo gần như không đổi. |
| | **8/20** | |

### Bằng chứng sơ cấp

Đây là chỗ hồ sơ thủng. [CAO]

- **Không có văn bản đương thời nào do ông hoặc triều đình ông để lại.**
- *Nihon shoki* (720) — nguồn chính, soạn **gần 100 năm** sau khi ông mất, và chính là nguồn mà học giới cho rằng đã **tạo ra** nhân vật.
- **Bi ký tượng Thích Ca tam tôn chùa Hōryū-ji (623)** — gần như là mảnh vật chứng gần đương thời duy nhất; nhưng niên đại và tính nguyên gốc của chính bản khắc này cũng từng bị đặt vấn đề, và Hōryū-ji đã cháy rồi dựng lại (670).
- *Tùy thư* ghi các sứ bộ 600 và 607 — xác nhận **sự kiện**, không xác nhận **người**.

**Đề xuất `độ tin cậy niên đại:` → `Trung bình`.** Hai năm 574 và 622 chỉ có ở *Nihon shoki*; chúng nhất quán nội bộ và khớp bi ký Hōryū-ji, nên không phải hạng `Thấp`, nhưng một nguồn muộn một thế kỷ thì không đủ cho `Cao` (dung sai ±5). [TRUNG BÌNH]

### Mệnh đề phổ thông đang bị học giới tranh luận

Đây là ca tranh luận **nặng nhất** trong cả sáu ứng viên. Người viết phải biết trước, nếu không sẽ in thẳng truyền thuyết thế kỷ 8 thành sự kiện thế kỷ 7.

1. **Chính sự tồn tại của "Thánh Đức Thái tử".** Ōyama Seiichi (大山誠一), *〈聖徳太子〉の誕生* (1999), lập luận rằng một hoàng tử tên **Umayado (厩戸)** có thật, nhưng hình tượng "Thánh Đức Thái tử" là **kiến tạo của nhóm soạn *Nihon shoki***, mà người chủ xướng là Fujiwara no Fuhito. Luận điểm này không được chấp nhận toàn bộ nhưng đã đổi hẳn mặt bằng tranh luận: sách giáo khoa Nhật nay thường in 厩戸王（聖徳太子）. [CAO]
2. **Hiến pháp 17 điều (604).** Văn bản chứa từ ngữ hành chính **lỗi thời so với năm 604** — đáng chú ý là 国司 (*kokushi*), chức danh chỉ có sau cải cách Taika. Hoặc soạn muộn hơn, hoặc đã bị biên tập lại khi đưa vào *Nihon shoki*. [CAO]
3. **Tam kinh nghĩa sớ** (sớ ba bộ kinh Pháp Hoa, Thắng Man, Duy Ma). Tác quyền bị ngờ mạnh; nhiều ý kiến cho là soạn phẩm lục địa được gán cho ông về sau. [TRUNG BÌNH]
4. **Chức "nhiếp chính".** Việc ông có thật sự nhiếp chính hay chỉ là một hoàng thân bên cạnh Soga no Umako đang nắm quyền, là câu hỏi mở. [TRUNG BÌNH]

### Rủi ro trùng lặp trong nhóm

CE07 đã có **4 người Đông Á** (Đường Thái Tông, Võ Tắc Thiên, Huyền Trang, Huệ Năng). Thêm Shōtoku → 5/12 Đông Á.

---

## 3. Dharmakīrti / Pháp Xứng — `Q457990`

**Kiểm Q-ID:** ĐÚNG NGƯỜI. `P31: Q5`, EN `Dharmakirti`, **VI `Pháp Xứng`**, desc "Indian Buddhist philosopher (fl.c.600–670)", enwiki `Dharmakirti`, viwiki `Pháp Xứng`, 32 sitelinks. [CAO]

> **CẢNH BÁO DỮ LIỆU (xem §0.2):** `P569: +0700` / `P570: +0660` — sinh sau khi mất. **Không chép hai số này.** Ghi `năm: hoạt động k. 600–660 CN` theo quy ước "chỉ biết khoảng hoạt động" của `CONTRIBUTING.md`. Với `độ tin cậy niên đại: Thấp`, `DATE_TOLERANCE["Thấp"] = None` nên lint bỏ qua đối chiếu — đó là cách xử lý đúng, không phải cách né.

### Chấm điểm

| | Điểm | Giải thích |
|---|---|---|
| (a) phạm vi | **4** | Vượt xa Nam Á: hệ *pramāṇa* của ông thành **xương sống chương trình học viện Tây Tạng** (môn *tshad ma*) rồi theo đó sang Mông Cổ, và vẫn đang được dạy. Trong chính Ấn Độ, ông buộc **phía đối lập** phải tái cấu trúc — Nyāya (Vācaspati, Jayanta, Udayana), Mīmāṃsā, Kỳ Na giáo và Vedānta đều phải trả lời ông trong 700 năm sau. Không 5 vì ảnh hưởng sang Đông Á mỏng: Trung Hoa đã nhận nhánh nhân minh qua Huyền Trang **trước** ông. |
| (b) độ bền | **5** | ~1300 năm và **chưa dứt**: vẫn là giáo trình sống của các học viện Geluk và Sakya, đồng thời là một ngành nghiên cứu đang hoạt động trong triết học so sánh đương đại. Ít ứng viên nào trong cả Ch5 có chuỗi liên tục như vậy. |
| (c) nguyên bản | **5** | *Apoha* (nghĩa do loại trừ), *svalakṣaṇa* đối lập *sāmānyalakṣaṇa*, **arthakriyā** — lấy hiệu lực nhân quả làm tiêu chuẩn của cái thật, các chứng minh *kṣaṇabhaṅga* (sát-na diệt), *svasaṃvedana* (tự chứng). Ông đứng trên Trần-na nhưng **biến đổi** chứ không nối dài: Trần-na đặt bộ công cụ, Dharmakīrti dựng từ đó một siêu hình học hoàn chỉnh. |
| (d) counterfactual | **4** | Cao. Không có ông, chương trình của Trần-na nhiều khả năng dừng ở mức phương pháp luận. Toàn bộ cuộc tranh luận nhận thức luận Ấn Độ từ thế kỷ 7 tới 14 được tổ chức quanh **cách đặt vấn đề của ông** — kể cả bởi những người bác ông. Không 5 vì nền tảng Trần-na đã có sẵn. |
| | **18/20 — cao nhất trong sáu ứng viên** | |

### Bằng chứng sơ cấp

Rất mạnh về **tác phẩm**, rất yếu về **tiểu sử** — một sự bất đối xứng đáng viết thành câu. [CAO]

- **Bảy bộ luận còn nguyên**, phần lớn qua bản Tây Tạng, một phần có Sanskrit: *Pramāṇavārttika*, *Pramāṇaviniścaya*, *Nyāyabindu*, *Hetubindu*, *Vādanyāya*, *Sambandhaparīkṣā*, *Saṃtānāntarasiddhi*. Đây là bằng chứng sơ cấp **do chính ông viết** — hạng mà Harsha, Songtsen và Pakal đều không có.
- Chuỗi sớ giải Ấn Độ nối ngay sau (Devendrabuddhi, Śākyabuddhi, Prajñākaragupta…) đặt cận trên cho niên đại.
- **Tiểu sử thì gần như trống:** mọi chi tiết đời ông đến từ truyền thống Tây Tạng muộn (Tāranātha, thế kỷ 17) — cùng loại nguồn mà mục Trần-na `CH05-CE06-05` đã đúng khi để `Thấp`.

**Đề xuất `độ tin cậy niên đại:` → `Thấp`.** Xem §3.3 dưới: sai số giữa các phương án đang là **~50 năm**, vượt xa dung sai `Trung bình` (±25). [CAO]

### Mệnh đề phổ thông đang bị học giới tranh luận

1. **"Dharmakīrti sống 600–660 CN."** Đây là **quy ước**, không phải kết quả đo. SEP ghi Frauwallner "came out strongly for 600–660" nhưng gọi chứng cứ là **inconclusive**, và liệt hai phương án sớm hơn hẳn:
   - **Krasser (2012)** dùng quan hệ Dharmakīrti–Bhāviveka–Kumārila để đẩy hoạt động của ông về **giữa thế kỷ 6**;
   - **Balcerowicz (2016)** đề xuất **550–610** dựa trên ảnh hưởng lên nhà Kỳ Na giáo Samantabhadra.
   SEP kết luận rằng "caution or even agnosticism" vẫn là thái độ hợp lý.
   **Hệ quả trực tiếp cho atlas:** nếu Krasser hoặc Balcerowicz đúng, ông thuộc **CE06**, không phải CE07 — và CE06 đã có Trần-na. Xếp ông vào CE07 là theo **đa số hiện hành**, và điều đó phải được nói ra trong "Vì sao chọn", không được giấu. [CAO]
   *Nguồn đã kiểm, URL tồn tại và đúng chủ đề:* `https://plato.stanford.edu/entries/dharmakiirti/`.
2. **Một mảnh chứng cứ cụ thể người viết nên biết:** **Huyền Trang ở Ấn Độ 630–643, học nhân minh rất sâu, mà không hề nhắc Dharmakīrti**; **Nghĩa Tịnh** (ở Ấn Độ 671–695) thì có nhắc. Đây là lập luận quen thuộc ủng hộ niên đại **muộn** — và nó là một chi tiết đắt, vì nó nối thẳng sang mục Huyền Trang `CH05-CE07-06` đã có trong nhóm. [CAO]
3. **"Học trò trực tiếp của Trần-na."** Truyền thống chép ông học với **Īśvarasena**, học trò của Trần-na — tức cách một đời. Nhiều bản phổ thông rút gọn thành "học trò Trần-na". Đừng rút gọn. [TRUNG BÌNH–CAO]
4. **Quy tắc §6 của `CONTRIBUTING.md` áp dụng ở đây:** **Trần-na đã có mục riêng (`CH05-CE06-05`)**, nên **không được** nêu ông làm "ứng viên bị loại". Nếu muốn nhắc để định vị, phải viết rõ *"có mục riêng ở nhóm CE06"*.

### Ứng viên bị loại dùng được (đã đối chiếu `data/persons.json`, 242 mục — **không ai trong số này đã có mục**)

- **Kumārila Bhaṭṭa** — `Q774847`, Mīmāṃsā, đối thủ cùng thời, chính là người mà lập luận niên đại của Krasser xoay quanh. ⚠️ Mô tả tiếng Anh trên Wikidata của mục này đang **sai** ("Master alchemist who documented rasayana…") — lại một ca §49: khớp Q-ID vẫn phải đọc lại bằng mắt.
- **Pulakeshin II** — `Q708370` (dùng cho mục Harsha nếu cần).


---

## 4. Tùng Tán Cán Bố / Songtsen Gampo — `Q320122`

**Kiểm Q-ID:** ĐÚNG NGƯỜI. `P31: Q5`, EN `Songtsän Gampo`, **VI `Tùng Tán Cán Bố`**, desc "Tibetan emperor (604-650)", enwiki `Songtsen Gampo`, viwiki `Songtsen Gampo`, 45 sitelinks. [CAO]

> **Chú ý dữ liệu:** `P569` có **hai** giá trị mâu thuẫn — `604` và `617`. `P570: 650`. Tức Wikidata tự nó không quyết được năm sinh (chênh 13 năm). Xem đề xuất độ tin cậy dưới.

### Chấm điểm

| | Điểm | Giải thích |
|---|---|---|
| (a) phạm vi | **4** | Nhà nước ông lập thành **cường quốc thứ ba của Á châu nội địa** suốt 200 năm: giằng co với nhà Đường quanh lòng chảo Tarim, ép được Nepal và bắc Ấn, và năm 763 **chiếm Trường An**. Chữ viết xuất hiện trong triều ông về sau thành **vật chứa** cho khối văn bản Phật giáo Ấn Độ lớn nhất còn sót lại — gồm chính bảy bộ luận của Dharmakīrti ở §3. Đó là phạm vi vượt vùng theo nghĩa chặt nhất. |
| (b) độ bền | **5** | Chữ Tạng vẫn dùng sau 1400 năm. Lhasa vẫn là thủ phủ vì ông dời đô về đó. Chùa Jokhang vẫn là nơi thiêng nhất của Phật giáo Tạng truyền. Rất ít quyết định thế kỷ 7 nào còn giữ nguyên hiệu lực vật chất như vậy. |
| (c) nguyên bản | **3** | Hạ điểm một cách có chủ ý. Chữ Tạng là **phái sinh** từ hệ Brahmi–Gupta, không phải phát minh; và phần lớn cái được gán cho ông (xem §4.3) là truyền thuyết muộn. Phần nguyên bản vững là bộ khung hành chính–quân sự và luật lệ của đế quốc Yarlung. |
| (d) counterfactual | **4** | Cao. Không có bước thống nhất cao nguyên và việc đưa chữ viết vào triều đình, rất khó có đế quốc Tạng, và càng khó có cái kho kinh điển Tạng ngữ mà ngày nay là đường duy nhất tiếp cận nhiều tác phẩm Phật giáo Ấn Độ đã mất bản Sanskrit. Không cho 5 vì **cha ông, Namri Songtsen, đã khởi việc thống nhất** — ông thừa hưởng một đà đang chạy. |
| | **16/20 — hạng nhì** | |

### Bằng chứng sơ cấp

Tốt một cách bất ngờ, **với điều kiện chỉ dùng tầng sớm**. [CAO]

- **Biên niên Tạng cổ (Old Tibetan Annals)** và **Ký sự Tạng cổ (Old Tibetan Chronicle)** — thủ bản Đôn Hoàng, soạn khoảng thế kỷ 8–9. Được mô tả là tư liệu quan trọng nhất hiện có về lịch sử Tạng sơ kỳ. *Biên niên* ghi ông mất **649/650**.
- **Thư tịch Đường** — *Cựu Đường thư* và *Tân Đường thư*, phần Thổ Phồn: nguồn ngoại vi độc lập, xác nhận cuộc hôn nhân với công chúa Văn Thành.
- **Trụ đá Zhol** ở Lhasa — nhưng dựng khoảng **764**, tức hơn một thế kỷ sau; không phải chứng cứ đương thời về ông.

**Đề xuất `độ tin cậy niên đại:` → `Trung bình`.**
Năm mất 649/650 vững (Biên niên Tạng cổ + thư tịch Đường). Năm sinh thì không: 604 hay 617 đều đang được chép, chênh 13 năm — nằm trong dung sai `Trung bình` (±25) nhưng vượt `Cao` (±5). Khuyến nghị ghi `năm: k. 604–650 CN` (hoặc `trị vì k. 618–650 CN`) và **nói rõ trong văn xuôi rằng năm sinh có hai phương án**. [CAO]

### Mệnh đề phổ thông đang bị học giới tranh luận

Hồ sơ này có một đặc điểm phải nắm: **gần như toàn bộ hình ảnh phổ thông về ông đến từ nguồn thế kỷ 11–12, không phải từ tầng Đôn Hoàng.** Nếu người viết lấy từ sách phổ thông, họ sẽ chép lại bản dựng của Phật giáo hậu kỳ.

1. **"Thonmi Sambhota được cử sang Ấn Độ và sáng chế chữ Tạng."** **Các nguồn Tạng sớm nhất, gồm *Ký sự Tạng cổ*, không hề nhắc tới Thonmi Sambhota.** Ông xuất hiện trong nguồn muộn hơn nhiều, và các luận thư mang tên ông nhiều khả năng được gom lại trong những thập niên **sau** triều Songtsen. Chữ viết thì có thật và xuất hiện trong triều ông; **người** được gán công thì đáng ngờ. Viết "chữ Tạng được định hình dưới triều ông" là an toàn; viết "Thonmi Sambhota sáng chế" là chép truyền thuyết. [CAO]
   *Nguồn đã kiểm:* Sam van Schaik, "A New Look at the Tibetan Invention of Writing" (bản PDF công khai tại `earlytibet.com`) — chuyên khảo đúng chủ đề này.
2. **"Công chúa Nepal Bhrikuti."** **Không tìm thấy một dẫn chiếu nào tới bà trong khối văn thư Đôn Hoàng**, và nguồn Nepal cũng không có. Nhiều khả năng là nhân vật được thêm vào về sau để làm cân xứng với công chúa Văn Thành (người thì **có** trong thư tịch Đường). Đừng kể hai bà như hai sự kiện ngang nhau. [CAO]
3. **"Songtsen Gampo đưa Phật giáo vào Tây Tạng / là pháp vương."** Khối văn thư Đôn Hoàng cho thấy rất ít dấu vết Phật giáo trong triều ông. Chân dung "pháp vương" là sản phẩm của văn học *terma* thế kỷ 11–12 (*Maṇi bka' 'bum*). Việc thiết lập Phật giáo thật sự diễn ra dưới **Trisong Detsen**, thế kỷ 8. [CAO]
4. **`vùng:` — vấn đề riêng của mục này, xem §8.2.** `REGIONS` không có ô nào cho Tây Tạng.

### Ứng viên bị loại dùng được

- **Gar Tongtsen Yulsung** (mgar stong rtsan yul zung) — `Q843378`, "Tibetan general (590-667)", **đã kiểm: không có mục nào trong `data/persons.json`**. Đây là ứng viên bị loại *tốt*, vì ông là đại thần điều hành thực tế nhà nước và gia tộc Gar khống chế triều đình 650–698; nêu ông làm cho lập luận chọn Songtsen mạnh lên chứ không yếu đi.
- **Không** dùng Thonmi Sambhota làm ứng viên bị loại — tính lịch sử của chính ông đang bị ngờ, nêu ra sẽ thành một khẳng định ngầm rằng ông có thật.

---

## 5. Kʼinich Janaabʼ Pakal của Palenque — ~~`Q311215`~~ → **`Q371384`**

**Kiểm Q-ID:** Q-ID đề bài đưa **SAI** — xem §0.1. Q-ID đúng là `Q371384`: `P31: Q5`, EN/VI `K'inich Janaab' Pakal`, desc "Maya ruler of Palenque", `P569: 603-03-23`, `P570: 683-08-28`, `P106: Q412185`, 34 sitelinks. [CAO]

### Chấm điểm

| | Điểm | Giải thích |
|---|---|---|
| (a) phạm vi | **2** | Yếu, và cần nói thẳng tại sao. Palenque bá chủ vùng tây đồng bằng Maya; phong cách bi ký và điêu khắc của nó được bắt chước ở các trung tâm lân cận. Ngoài Trung Mỹ thì **bằng không** — nhưng đó là **sự thật về địa lý hành tinh, không phải về ông** (xem §8.1: tiêu chí (a) phạt có hệ thống mọi nhân vật tiền-Columbus). |
| (b) độ bền | **3** | Triều đại Palenque tắt trong vòng khoảng một thế kỷ sau ông. Nhưng có một độ bền thật, dù ngoài ý định: **khối văn bản Palenque là xương sống của công cuộc giải mã chữ Maya hiện đại** — lịch sử triều đại đầy đủ nhất trong toàn bộ ngữ liệu Maya, và là nơi các bước đột phá giải mã được thử. Chữ ông cho khắc vẫn đang làm việc. |
| (c) nguyên bản | **4** | Cao, và đây là trụ chính của hồ sơ. Đền Bi ký là một **kim tự tháp tang lễ có hầm mộ và ống dẫn hồn (psychoduct)** — một hình thức kiến trúc hiếm trong thế giới Maya. Nắp quách với hình ông rơi vào thế giới dưới dọc theo cây vũ trụ, và chương trình văn bản nối phả hệ của ông vào thời thần thoại (nhóm Thập Tự, phép đếm 819 ngày) là một công trình **ý thức hệ** được thiết kế trọn gói, không phải một đống bia rời. |
| (d) counterfactual | **2** | Thấp, và không nên thổi. Không có Pakal, quỹ đạo của văn minh Maya gần như không đổi. Counterfactual thật sự của ông là **đối với tư liệu**, không đối với lịch sử: thiếu khối văn bản Palenque, lịch sử giải mã chữ Maya đã khác. Phải viết đúng như vậy, đừng đánh tráo hai thứ. |
| | **11/20 — hạng ba** | |

### Bằng chứng sơ cấp

Thuộc hạng **tốt nhất** trong sáu ứng viên về mặt vật chất, và hoàn toàn **nội sinh** — không ai kể hộ ông. [CAO]

- **Bi ký đương thời do chính triều đình ông đặt:** các bảng chữ Đền Bi ký, nhóm Thập Tự (Đền Thập Tự, Thập Tự Lá, Mặt Trời), các bảng Cung điện. Niên đại ghi bằng **Trường kỳ (Long Count)**, tương quan GMT cho ngày dương lịch chính xác tới **ngày**.
- **Ngôi mộ còn nguyên**, do **Alberto Ruz Lhuillier** mở năm **1952** sau bốn năm dọn bậc thang lấp: quách đá, nắp chạm, mặt nạ ngọc, và bộ hài cốt.
- Ngày sinh **24/3/603**, lên ngôi **27/7/615** (12 tuổi, sau nhiếp chính của mẹ là **Sak Kʼukʼ**), mất **29/8/683** — trị vì **68 năm**, một trong những triều dài nhất được xác minh trong lịch sử quân chủ thế giới.

**Đề xuất `độ tin cậy niên đại:` → `Cao`.** Nghịch lý dễ chịu: ứng viên "xa xôi" nhất lại có niên đại **chặt nhất** trong cả sáu, vì Trường kỳ là lịch đếm ngày tuyệt đối. Sai số nằm ở hằng số tương quan GMT, cỡ vài ngày — thừa sức trong dung sai ±5 năm. [CAO]

### Mệnh đề phổ thông đang bị học giới tranh luận

#### 5.4.1 Tuổi 80 và bộ xương trong mộ — tranh luận đã tới đâu (phần đề bài hỏi riêng)

Trình tự, viết gọn để người soạn khỏi dựng lại sai:

1. **Bi ký nói 80.** Trường kỳ cho sinh 603, mất 683 → 80 tuổi, 68 năm trị vì.
2. **Xương nói 40–50.** Sau khi Ruz mở mộ năm 1952, các nhà nhân học hình thể Mexico giám định bộ hài cốt và ra khoảng **40–50 tuổi**, chủ yếu dựa trên **mức mòn răng**. Chênh lệch khoảng **30–40 năm** — gọi là "vấn đề Palenque".
3. **Hai lối thoát được đề xuất.** Hoặc (i) bi ký nói về **hai người khác nhau** / người trong quách không phải Pakal — **chính Ruz Lhuillier** đã nêu khả năng này; hoặc (ii) **phương pháp giám định tuổi bị lệch** với một quý tộc Maya.
4. **Trọng tâm tranh luận đã chuyển sang (ii).** Lập luận: thước đo mòn răng giả định một khẩu phần nhiều hạt nghiền trên đá, tức lẫn cát; một người thuộc tầng trên cùng ăn chế độ mềm hơn sẽ **mòn răng ít hơn**, và phương pháp vì vậy **hệ thống hạ thấp tuổi**.
5. **Vera Tiesler & Andrea Cucina (chủ biên), *Janaab' Pakal of Palenque: Reconstructing the Life and Death of a Maya Ruler*, University of Arizona Press, 2006** — giám định lại bằng **transition analysis** (một phương pháp định tuổi vĩ mô mới), **histomorphometry** (đo vi cấu trúc xương) và phân tích ảnh taphonomy. Kết quả nghiêng về phía bi ký: người trong mộ **không thể dưới 50 tuổi** và nhiều khả năng mất ở **thập niên thứ tám hoặc thứ chín** của đời.
6. **Trạng thái hiện nay.** Phần lớn giới nghiên cứu coi mâu thuẫn là **đã giải quyết theo hướng bi ký đúng**, và quy phần chênh cho **giới hạn của phương pháp cổ nhân học**. Nhưng **vẫn tồn tại mạch thận trọng** cho rằng độ bất định của định tuổi bộ xương này còn rộng, nên dải 40–50 chưa bị loại hẳn về mặt kỹ thuật. [TRUNG BÌNH–CAO]

**Cách viết an toàn:** "bi ký cho tuổi 80; giám định xương năm 1952 cho 40–50; khảo sát lại năm 2006 bằng phương pháp mới nghiêng về phía bi ký và quy phần lệch cho giới hạn của cách định tuổi qua mòn răng." **Không** viết "đã được chứng minh ông thọ 80 tuổi", cũng **không** viết "bộ xương không phải của ông" — cả hai đều là một phía của tranh luận in thành sự kiện.
*Tài liệu nền:* Tiesler & Cucina (chủ biên) 2006, Univ. of Arizona Press — bản ghi JSTOR `j.ctv1qwwk7s`. **Người viết phải tự mở mục lục trước khi ghi bất kỳ số chương nào** (`CONTRIBUTING.md` §48).

#### 5.4.2 Những mệnh đề khác

7. **Nắp quách vẽ "phi hành gia".** Erich von Däniken, *Chariots of the Gods?* (1968), so tư thế Pakal với phi hành gia Project Mercury và đọc hoạ tiết thành tên lửa. Giới khảo cổ **bác gần như tuyệt đối**: hình là Pakal rơi xuống thế giới dưới dọc cây vũ trụ, theo đúng bộ hình tượng vũ trụ luận Maya đã biết. Đây **không phải** một tranh luận học thuật — nhưng nó phổ biến tới mức **nên nhắc một câu để chặn**, vì độc giả tiếng Việt rất dễ gặp nó trước khi gặp atlas. [CAO]
8. **Tên gọi.** Dạng cũ "Pacal" vẫn còn trong tài liệu tiếng Việt; dạng chuẩn hiện nay là **Kʼinich Janaabʼ Pakal**. Và nhớ §0.1: trong cùng triều đại có ít nhất ba người tên Janaabʼ Pakal.
9. **"Nữ hoàng Đỏ" ở Đền XIII** thường được giới thiệu là vợ ông, **Tzʼakbu Ajaw**. Đồng nhất này là **suy luận**, chưa được xác nhận: nỗ lực lấy DNA không thành. Nếu nhắc, phải ghi là giả thuyết. [TRUNG BÌNH]

### Ứng viên bị loại dùng được

- **Yuknoom Chʼeen II** của Calakmul (trị vì 636–686) — `Q3083253`, **đã kiểm: không có mục nào trong `data/persons.json`**, nên hợp lệ làm ứng viên bị loại theo `CONTRIBUTING.md` §51.
  Đây là **đối thủ nặng ký thật**, không phải bù nhìn: ông dựng mạng bá quyền Kaan rộng nhất lịch sử Maya, hạ Tikal, dựng chư hầu ở Dos Pilas, Cancuén, Naranjo. Theo (a) và (d) ông **ăn điểm Pakal**.
  **Vì sao vẫn chọn Pakal:** (i) bá quyền Kaan sụp trong vòng mười năm sau khi Yuknoom mất — (b) thấp; (ii) bia Calakmul **xói mòn nặng**, phần lớn câu chuyện Kaan phải dựng lại từ văn bản ở các địa điểm khác và là một lĩnh vực **đang biến động nhanh** — với một dự án mà điểm hỏng đặc trưng là trích dẫn bịa, chất lượng tư liệu phải được tính thành một tiêu chí thực; (iii) Palenque hơn hẳn về (c).
  ⚠️ **Bẫy Q-ID:** có cả `Q8060771` **Yuknoom Chʼeen I**. Lấy nhầm là lặp lại đúng lỗi §0.1.


---

## 6. Dapunta Hyang Sri Jayanasa — `Q12480888`

**Kiểm Q-ID:** ĐÚNG NGƯỜI. `P31: Q5`, EN `Dapunta Hyang Sri Jayanasa`, desc "emperor of Srivijaya empire", enwiki `Sri Jayanasa of Srivijaya`.
**Nhưng hồ sơ rất mỏng:** **không có `P569`, không có `P570`, không có `P106`, không có `P39`**, chỉ **10 sitelinks**, và **không có nhãn tiếng Việt, không có viwiki**. Người viết sẽ phải tự đặt tên tiếng Việt và sẽ không có mục Wikipedia tiếng Việt để dẫn. [CAO]

### Chấm điểm

| | Điểm | Giải thích |
|---|---|---|
| (a) phạm vi | **2** | Ở thời điểm các bia của **chính ông** (682–686), tầm với là Palembang, Jambi, đảo Bangka, Lampung, cộng một cuộc viễn chinh đường biển nhắm sang Java. Srivijaya **về sau** mới khống chế eo Malacca và eo Sunda và thành trung tâm Phật học quốc tế — Nghĩa Tịnh dừng lại đó học Sanskrit năm 671. Phần lớn "phạm vi" thường gán cho ông thực ra là thành tựu của các đời sau. |
| (b) độ bền | **3** | Nhà nước kéo khoảng sáu thế kỷ. Và có một di sản sắc hơn, thường bị bỏ sót: **các bia của ông là văn bản tiếng Mã Lai có niên đại sớm nhất còn biết** — tức điểm khởi của mạch văn tự dẫn thẳng tới tiếng Mã Lai và tiếng Indonesia ngày nay, ngôn ngữ của hơn 250 triệu người. Đó mới là lập luận (b) mạnh nhất của hồ sơ này, không phải tuổi thọ của vương quốc. |
| (c) nguyên bản | **2** | Dạng nhà nước cảng-triều cống và việc dùng tiếng Mã Lai kèm lời nguyền Sanskrit làm **công cụ ràng buộc trung thành** (bia Telaga Batu) là đáng chú ý. Nhưng quy được bao nhiêu phần cho **cá nhân** ông thì không ai biết — đó là vấn đề chung của mọi vua chỉ tồn tại trong vài tấm bia. |
| (d) counterfactual | **2** | Thấp–trung bình. Vị trí địa lý của eo biển gần như bảo đảm sẽ có **một** trung tâm trung chuyển trỗi dậy ở đó. Rằng nó mang tên Srivijaya và đóng ở Palembang thì có phần của ông; rằng nó tồn tại thì không. |
| | **9/20** | |

### Bằng chứng sơ cấp

**Mạnh hơn danh tiếng của ông rất nhiều — và đây là phát hiện đáng chú ý nhất của mục này.** [CAO]

Khác Harsha (được người khác kể), khác Shōtoku (được kể muộn một thế kỷ), khác Songtsen (tầng truyền thuyết dày), Dapunta Hyang **chỉ** tồn tại trong **bia khắc đương thời, có niên đại chính xác, nêu đích danh ông**:

- **Bia Kedukan Bukit** — 605 Śaka = **16/6/682**, tìm được gần Palembang năm 1920. Chép một *siddhayātra* (cuộc hành trình thiêng) bằng thuyền, một đạo quân, và việc lập một khu định cư sau khi thắng trận.
- **Bia Talang Tuwo** — 606 Śaka = **684**: lập vườn *Śrīkṣetra* và một lời cầu phúc Phật giáo Đại thừa.
- **Bia Kota Kapur** (đảo Bangka) — 608 Śaka = **686**: lời nguyền nhắm vào kẻ phản, nhắc một cuộc viễn chinh chống Java.
- **Bia Telaga Batu**, **Karang Brahi**, **Palas Pasemah** — cùng nhóm *siddhayātra*.

**Đề xuất `độ tin cậy niên đại:` → `Trung bình`.**
Lý do tách bạch: **niên đại các văn bản thì chắc tới từng ngày**; nhưng (i) **không có năm sinh và năm mất** của con người, và (ii) việc **"Dapunta Hyang" của bia Kedukan Bukit và "Sri Jayanasa" của bia Talang Tuwo là cùng một người** là một **quy ước học thuật**, không phải điều bia nói ra. Ghi theo mẫu "chỉ biết khoảng hoạt động" của `CONTRIBUTING.md`: `năm: hoạt động 682–686 CN`. **Không** để `Cao`, vì `Cao` sẽ ngụ ý một độ chắc về *con người* mà tư liệu không cấp. [CAO]

### Mệnh đề phổ thông đang bị học giới tranh luận

1. **"Dapunta Hyang chính là Sri Jayanasa."** Hai danh xưng ở hai bia khác nhau. Gộp lại là quy ước tiện dụng, được dùng rộng rãi (kể cả Wikidata đã gộp sẵn trong nhãn), nhưng **không phải điều được chứng minh**. [TRUNG BÌNH–CAO]
2. **"Srivijaya là một đế quốc hàng hải."** Chữ "đế quốc" đang bị đẩy lùi. Các mô hình cạnh tranh — mạng lưới cảng kiểu "dendritic" của Bennet Bronson, *mandala* của O. W. Wolters — đọc Srivijaya như một **liên minh cảng lỏng lẻo dựa trên uy tín và phân phối lại**, không phải một nhà nước lãnh thổ. Đây là tranh luận sống, và nó đánh thẳng vào điểm (a). [TRUNG BÌNH–CAO]
3. **Kinh đô ở Palembang.** Từng bị tranh luận dài (Soekmono đề xuất Jambi–Muara Jambi); nay Palembang chiếm ưu thế nhờ khảo cổ, nhưng đừng viết như chưa từng có tranh luận. [TRUNG BÌNH]
4. **Chữ "śrīvijaya" trong bia Kedukan Bukit là tên nước hay là cụm "thắng lợi rực rỡ"?** Việc đọc nó thành tên một vương quốc là **thành quả của Georges Cœdès năm 1918** — trước đó không ai biết Srivijaya tồn tại. Một chi tiết hay cho phần văn xuôi, và cũng là một lời nhắc rằng toàn bộ nhân vật này đứng trên một phép đọc ngữ văn. [TRUNG BÌNH–CAO]

---

## 7. Jayavarman II (`Q379239`) — kiểm chéo giả định của đề bài về CE09

Đề bài giả định: *Đông Nam Á "đằng nào cũng được bảo đảm" ở CE09 bằng một người mạnh hơn hẳn.* Tôi kiểm giả định này vì nó đang gánh phần lớn sức nặng của quyết định.

**Q-ID:** ĐÚNG NGƯỜI. `P31: Q5`, VI `Jayavarman II`, desc "9th-century king of Cambodia", `P27: Q424` (Campuchia), 31 sitelinks.
⚠️ Nhãn tiếng Anh trên Wikidata đang **gõ sai**: `Jayavaraman II`. `P569: 800` / `P570: 900` rõ ràng là **giá trị độn** (hai mốc tròn trăm), không phải niên đại thật — **đừng chép**. [CAO]

**Giả định đúng ở phần (a)(b)(d), sai ở phần bằng chứng.**

- **Về sức nặng: đúng.** Lễ hiến tế năm **802** trên núi Mahendraparvata (Phnom Kulen) tấn phong ông làm *chakravartin* được coi là điểm khởi của Đế quốc Khmer — một nhà nước kéo sáu thế kỷ, để lại Angkor. Theo (a)(b)(d) ông trội hơn Dapunta Hyang rõ rệt. ✔
- **Về bằng chứng: ngược lại với điều người ta tưởng.** Phần lớn những gì biết về Jayavarman II đến từ **bia Sdok Kak Thom, khắc năm 1052** — **250 năm sau** sự kiện, dưới triều Udayādityavarman. **Michael Vickery**, "A legend concerning Jayavarman II", đặt vấn đề đúng chỗ này. Tức: **Dapunta Hyang có bằng chứng sơ cấp đương thời; Jayavarman II thì không.** [CAO]
- **Khuyến nghị khi tới CE09:** `độ tin cậy niên đại: Thấp`, và phần văn xuôi phải nói rằng năm 802 là **niên đại do một bản bia thế kỷ 11 đặt lại**, không phải một mốc đương thời.
- **Một giới hạn nữa đề bài chưa tính:** Jayavarman II phủ **Đông Nam Á lục địa** (Khmer). Ông **không** phủ **thế giới hải đảo/Mã Lai** — mà đó mới đúng là phần Dapunta Hyang đại diện. Cộng với §0.3 (ch90 chỉ là Việt Nam), nghĩa là **sau CE09, Đông Nam Á hải đảo vẫn ở 0 trong atlas chính.**
- **Nhưng không bị khoá vĩnh viễn:** Sailendra và Borobudur (CE08–CE09), các vua Srivijaya đời sau, rồi Gajah Mada / Hayam Wuruk của Majapahit (CE14) đều là cửa còn mở cho Đông Nam Á hải đảo, và vài người trong số đó mạnh hơn Dapunta Hyang. [TRUNG BÌNH]

---

## 8. Cân sức ép vùng — nói rõ tôi đánh đổi thế nào

### 8.1 Tiêu chí (a) phạt có hệ thống hai vùng đang trống

Đây là điều phải nói trước mọi thứ khác, vì nếu không nói thì phần chấm điểm ở trên sẽ bị đọc sai.

Tiêu chí (a) đo **"ảnh hưởng vượt ra ngoài vùng của chính mình bao xa"**. Trước năm 1492, châu Mỹ **không có đường vật lý** nào để ảnh hưởng ra ngoài châu Mỹ. Nghĩa là (a) ở đây **không đo tầm vóc, nó đo mức kết nối của bán cầu** — và áp (a) nguyên xi sẽ **bảo đảm về mặt toán học** rằng Châu Mỹ đứng ở 0% mãi mãi, bất kể ta chọn ai. Cùng một hiệu ứng, nhẹ hơn, áp lên Châu Đại Dương và Châu Phi hạ Sahara.

Đây **không phải** lý do để hạ chuẩn. Nó là lý do để **đọc điểm (a) của Pakal 2/5 cho đúng nghĩa**: con số ấy nói về địa lý hành tinh, không nói rằng Pakal là một nhân vật hạng hai. Ba điểm còn lại của ông — đặc biệt (c) = 4 — mới là chỗ đo chính ông, và chúng đứng vững.

**Khuyến nghị:** ghi đúng nhận định này vào `## Ghi chú biên tập` của Ch5. Nó thuộc loại hạn chế-của-thước-đo mà `CONTRIBUTING.md` quy ước `vùng:` §3 đã có tiền lệ (khai báo rằng "Trung Á" chỉ còn là vành đai Transoxiana và thế giới du mục không tồn tại như một hạng mục).

### 8.2 `vùng:` của Songtsen Gampo — và một cám dỗ phải từ chối

`REGIONS` có 9 ô, **không ô nào cho Tây Tạng**.

Cám dỗ rõ ràng: ghi **Trung Á** để kéo 0.5% lên 1%. **Phải từ chối.** `CONTRIBUTING.md` quy ước `vùng:` §3 đã ghi thành văn rằng "Trung Á" trên thực tế chỉ dùng cho **vành đai Transoxiana–Iran đông**; và §4 cấm đổi `vùng:` để làm đẹp thống kê, với tiền lệ đã **bác** đề xuất chuyển Kanishka sang Trung Á. Ghi Lhasa là Trung Á sẽ là **đúng cùng một lỗi**, chỉ đổi tên người.

**Khuyến nghị: `vùng: Đông Á`**, theo quy tắc §1 (nơi hoạt động chính = Lhasa) và theo tiền lệ đã khai báo ở §3 (cao nguyên Mông Cổ → Đông Á, Mặc Đốn thiền vu `CH03-BCE02-12`). Đây là **lựa chọn tốt nhất trong các lựa chọn dở**, và nó phải được khai báo trong `## Ghi chú biên tập` như ngoại lệ thứ hai được ghi thành văn — y như cách các thành bang Hy Lạp ở Tiểu Á đã được khai báo.

**Chi phí phải thừa nhận:** chọn Songtsen đẩy Đông Á lên **5/12** trong nhóm CE07 và **không mở được vùng nào**. Tôi vẫn chọn ông, vì 16/20 bỏ xa mọi ứng viên còn lại ngoài Dharmakīrti, và `CONTRIBUTING.md` nói rõ cân bằng vùng **không được hạ chuẩn chất lượng**. Đổi lại cho sự thừa nhận đó: văn xuôi nên nói rõ Tây Tạng là một **thế giới riêng** bị nhãn "Đông Á" làm mờ — đúng tinh thần đã dùng cho thế giới thảo nguyên.

### 8.3 Đổi Dapunta Hyang lấy Pakal — đánh đổi thật, nói thẳng

**Điều tôi KHÔNG dựa vào:** không cần tới lập luận vùng để xếp Pakal trên Dapunta Hyang. **11/20 so với 9/20 đã quyết trên thuần chuyên môn** — Pakal hơn rõ ở (c) (4 so với 2) và hơn ở (b). Lập luận vùng chỉ **xác nhận**, không **gánh**, kết luận. Tôi nêu điều này ra vì đó chính là chỗ một bản bình duyệt dễ tự lừa mình nhất.

**Điều tôi thừa nhận là mất:** Đông Nam Á đứng ở **0,0%** sau Ch5 và — theo §7 — Đông Nam Á **hải đảo** sẽ vẫn ở 0 cả sau khi Jayavarman II vào CE09. Đó là một lỗ thật, và tôi không giả vờ rằng phụ lục ch90 vá được nó (§0.3: ch90 là Việt Nam).

**Vì sao vẫn chấp nhận mất:**
1. Dapunta Hyang 9/20 là **ứng viên yếu nhất trừ hai người 8/20**; ép ông vào để lấp ô vùng chính là "hạ chuẩn chất lượng xuống dưới ngưỡng" mà `CONTRIBUTING.md` cấm.
2. Đông Nam Á **có** đường vào qua CE09 (Jayavarman II, lục địa) và **còn** cửa cho hải đảo ở CE08–CE09 (Sailendra) và CE14 (Majapahit) — bằng những người **mạnh hơn** ông.
3. Châu Mỹ **không có** chỗ nào khác trong Ch5, và theo §8.1 thì nếu đã có một ứng viên châu Mỹ qua ngưỡng mà vẫn bỏ, ta đang để một khuyết tật của **thước đo** tự kéo dài thành một khuyết tật của **atlas**.

**Khuyến nghị kèm theo:** ghi vào `## Ghi chú biên tập` Ch5 rằng Đông Nam Á còn trống ở Ch5 **và vì sao** — đây đúng là phương án thứ hai mà quy ước `vùng:` §4 cho phép ("ghi vào Ghi chú biên tập rằng vùng ấy trống và vì sao").

### 8.4 Những vùng trống khác: đã tìm, không có ai qua ngưỡng

- **Trung Á (0,5%).** Đã cân nhắc Thống Diệp Hộ khả hãn (Tong Yabghu) của Tây Đột Quyết, trị vì ~618–630. Không đề xuất: theo quy ước `vùng:` §3, thế giới thảo nguyên **không có ô** trong `REGIONS`, nên ông cũng không lấp được Trung Á; và hồ sơ (b)(c) không đủ. **Không có ứng viên Trung Á nào qua ngưỡng trong thế kỷ 7.** [TRUNG BÌNH]
- **Châu Phi hạ Sahara (1,5%).** Đã cân nhắc **Armah của Aksum** (~614–631), thường được đồng nhất với Najāshī Aṣḥama — vị vua che chở nhóm Muslim di cư năm 615, biến cố mà truyền thống Hồi giáo gọi là cuộc Hijra thứ nhất. **Điểm mạnh:** có **tiền đúc mang tên Armah**, tức bằng chứng sơ cấp vật chất. **Lý do loại:** việc đồng nhất Armah với Najāshī đang bị tranh luận; và theo (a)(c)(d) ông dưới ngưỡng — ông là **người nhận** một biến cố do người khác khởi, và Aksum thời ông đang suy. Ghi lại ở đây để lần rà sau không phải tìm lại. [TRUNG BÌNH]
- **Châu Âu (hiện 1/12 trong nhóm).** Đã cân nhắc **Heraclius** (trị vì 610–641). Không đề xuất: Châu Âu đã ở **27,7%** toàn atlas, nên thêm vào là đi ngược chiều cần đi; và dù counterfactual của ông cao, ông mất gần hết những gì ông thắng. [TRUNG BÌNH]

---

## 9. KHUYẾN NGHỊ CUỐI

### Chọn — theo thứ tự ưu tiên

| # | Người | Q-ID | Tổng | `vùng:` | `độ tin cậy niên đại:` |
|---|---|---|---|---|---|
| **1** | **Dharmakīrti (Pháp Xứng)** | `Q457990` | **18/20** | Nam Á | **Thấp** |
| **2** | **Tùng Tán Cán Bố (Songtsen Gampo)** | `Q320122` | **16/20** | **Đông Á** (xem §8.2) | **Trung bình** |
| **3** | **Kʼinich Janaabʼ Pakal** | **`Q371384`** ⚠️ không phải Q311215 | **11/20** | **Châu Mỹ** | **Cao** |

**Lấy đủ 12, không dừng ở 11.** Đề bài hỏi thẳng, nên tôi trả lời thẳng: cả ba người trên đều **trên** ngưỡng chất lượng, nên không có lý do gì để bỏ trống một suất. Người yếu nhất trong ba là Pakal ở 11/20, nhưng (c) = 4 của ông đứng độc lập được, niên đại của ông là **chắc nhất trong cả sáu**, và bằng chứng sơ cấp của ông là **vật chất và nội sinh**. Nếu ngưỡng đặt cao tới mức loại Pakal thì nó cũng loại mất vài mục **đã viết** ở các chapter trước — nghĩa là ngưỡng đó không phải ngưỡng thật của atlas này.

Nhóm sau khi chọn: **Trung Đông/Bắc Phi 3 · Đông Á 5 · Nam Á 2 · Châu Âu 1 · Châu Mỹ 1** — và lần đầu tiên trong 202 mục, **Châu Mỹ thoát 0%**.

### Loại — mỗi người một câu

- **Harsha `Q216895` (8/20)** — đế quốc tan ngay trong năm ông chết nên (b) và (d) đều sụp, và Nam Á trong nhóm này đã có Brahmagupta, sắp có Dharmakīrti.
- **Thánh Đức Thái tử `Q263972` (8/20)** — phần làm ông nổi tiếng (Hiến pháp 17 điều, *Tam kinh nghĩa sớ*, chức nhiếp chính) chính là phần học giới đang coi là kiến tạo thế kỷ 8, và Đông Á trong nhóm đã quá tải.
- **Dapunta Hyang Sri Jayanasa `Q12480888` (9/20)** — bằng chứng sơ cấp của ông **tốt hơn** tiếng tăm, nhưng (a)(c)(d) đều mỏng, và Đông Nam Á có đường vào ở CE09 bằng một người mạnh hơn; loại ông là một **mất mát thật**, đã ghi rõ ở §8.3 thay vì giấu đi.
- **Yuknoom Chʼeen II `Q3083253` (đề xuất thêm của tôi, đã loại)** — hơn Pakal ở (a)(d) nhưng thua ở (b)(c), và bia Calakmul xói mòn tới mức tư liệu không đủ vững cho một dự án mà điểm hỏng đặc trưng là trích dẫn bịa.
- **Armah của Aksum / Tong Yabghu / Heraclius (đề xuất thêm, đã loại)** — xem §8.4.

### Việc bắt buộc cho người viết — bảy điểm

1. **`Q371384`, không phải `Q311215`.** Và tránh `Q641749` (Janaabʼ Pakal mất 612), `Q4017694` (Janaab Pakal III), `Q8060771` (Yuknoom Chʼeen **I**).
2. **Đừng chép `P569`/`P570` của Dharmakīrti** (700/660 — sinh sau khi mất). Ghi `năm: hoạt động k. 600–660 CN`, `độ tin cậy niên đại: Thấp`.
3. **Trần-na có mục riêng `CH05-CE06-05`** → theo `CONTRIBUTING.md` §51, **không** được nêu ông làm "ứng viên bị loại". Dùng **Kumārila Bhaṭṭa `Q774847`** (đã kiểm: chưa có mục; nhưng mô tả tiếng Anh trên Wikidata của mục này đang sai, đừng dịch lại nó).
4. **Ứng viên bị loại đã kiểm sạch, đều không có mục trong `data/persons.json` (242 mục):** Kumārila `Q774847`, Gar Tongtsen Yulsung `Q843378`, Yuknoom Chʼeen II `Q3083253`, Pulakeshin II `Q708370`.
5. **Kiểm "cùng thời" theo `CONTRIBUTING.md` §50 trước khi viết đoạn so sánh.** Ba người được chọn **thật sự** cùng thời với nhau và với nhóm — Songtsen mất 650, Dharmakīrti hoạt động ~600–660, Pakal 603–683, Huyền Trang ở Ấn Độ 630–643. Có một mạch nối đẹp và **có thật**: Huyền Trang (`CH05-CE07-06`) ở Ấn Độ đúng khoảng Dharmakīrti hoạt động mà **không nhắc tới ông**, trong khi Nghĩa Tịnh (ở Ấn Độ 671–695) thì có — chính chi tiết đó là một trong các lập luận về niên đại ở §3.3.
6. **Hai mục phải viết vào `## Ghi chú biên tập`:** (i) giới hạn của tiêu chí (a) với châu Mỹ tiền-Columbus (§8.1); (ii) Tây Tạng ghi `Đông Á` như ngoại lệ thứ hai được khai báo, **không** ghi Trung Á (§8.2). Và nên thêm (iii): Đông Nam Á còn trống ở Ch5 và vì sao (§8.3).
7. **Không ghi số chương/trang của Tiesler & Cucina 2006 nếu chưa mở mục lục** (`CONTRIBUTING.md` §48 — bài học 5/6 số chương Keith Taylor sai, và cả 5 đều lệch +1).

### Nguồn người duyệt đã mở và kiểm

- Wikidata API `wbgetentities` / `wbsearchentities` / `Special:EntityData` — mọi Q-ID ở trên.
- Stanford Encyclopedia of Philosophy, mục **"Dharmakīrti"** — `https://plato.stanford.edu/entries/dharmakiirti/` — **đã mở, tồn tại, đúng chủ đề**, và có đúng đoạn về tranh luận niên đại (Frauwallner / Krasser 2012 / Balcerowicz 2016).
- Sam van Schaik, "A New Look at the Tibetan Invention of Writing" — PDF công khai tại `earlytibet.com`.
- Michael Vickery, "A legend concerning Jayavarman II" — PDF tại `michaelvickery.org`.
- Vera Tiesler & Andrea Cucina (chủ biên), *Janaab' Pakal of Palenque*, University of Arizona Press, 2006 — bản ghi JSTOR `j.ctv1qwwk7s`.

### KHÔNG KIỂM ĐƯỢC

- **Bản PDF "The Bones of Kʼinich Janaab Pakal" trên mesoweb.com.** Tệp tải về được nhưng không giải được nội dung văn bản. Phần §5.4.1 vì vậy dựng từ các nguồn khác đã liệt ở trên; **các tên riêng của hai nhà nhân học hình thể giám định bộ hài cốt năm 1952 tôi cố ý KHÔNG ghi**, vì tôi không mở được nguồn xác nhận chính tả. Người viết nếu muốn nêu đích danh thì phải tự kiểm.
- **Nội dung đầy đủ của Tiesler & Cucina 2006** — chỉ đọc được phần mô tả phương pháp qua nguồn thứ cấp, **không mở được chính sách**. Vì vậy §5.4.1 ghi "nghiêng về phía bi ký" chứ không ghi "đã chứng minh".
- **Niên đại chính xác và tính nguyên gốc của bi ký tượng Thích Ca Hōryū-ji (623)** — biết là có tranh luận, **không** truy được tới một công trình cụ thể trong lượt rà này.
