# Mục mới đề xuất — CH02-BCE06-11 · Sappho xứ Lesbos

Soạn theo `prompts/atlas-prompt.md`, trả lời finding **N1** của `reports/review-ch02.md`.
**Không chỉnh sửa `content/ch02.md`.** Tài liệu này là bản nháp để Owner dán tay.

---

## 0. Chọn nhóm: BCE06, không phải BCE07 — và vì sao

Tôi giữ **CH02-BCE06-11** như Owner chỉ định. Bằng chứng niên đại không ngả hẳn về phía nào, nên cần nói rõ:

| Nguồn cổ | Nội dung | Rơi vào |
|---|---|---|
| *Suda* | bà hoạt động trong Olympiad 42 (612–608 TCN) | TK 7 TCN |
| Eusebius, *Chronicle* | bà đã nổi tiếng vào Olympiad 45 (600–599 TCN) | ranh giới |
| Parian Marble (Parian Chronicle) | bà đi đày sang Sicily khoảng giữa 604 và 595 TCN | vắt qua ranh giới |
| Wikidata Q17892 (P569/P570 hạng preferred và các giá trị phụ) | k. 630 – k. 570 TCN | phần lớn đời ở TK 6 |

Ba mốc cổ không khớp nhau, và cả ba đều cụm quanh năm 600 TCN — tức đúng đường biên giữa hai nhóm. Lý do tôi chọn BCE06:

1. **Phần lớn đời trưởng thành nằm sau 600 TCN.** Nếu sinh k. 630 và mất k. 570, bà mới ba mươi tuổi vào năm 600; toàn bộ bốn mươi năm còn lại thuộc TK 6 TCN.
2. **Các sự kiện định niên được của đời bà đều ở TK 6 TCN**: cuộc lưu đày sang Sicily (Parian Marble, sớm nhất 604, muộn nhất 595) và bối cảnh chính biến Mytilene thời Myrsilus rồi Pittacus. Pittacus sống k. 650–570 TCN và cầm quyền Mytilene mười năm, tức nhiệm kỳ của ông nằm trong TK 6 TCN và trong đời Sappho. *(Tôi không xác minh được khoảng năm cụ thể của mười năm đó, nên không ghi con số.)*
3. **Alcaeus, người cùng thành và cùng hệ khổ thơ, có niên đại k. 625–580 TCN**, tức cũng là một nhân vật TK 6 TCN về mặt hoạt động. Xếp Sappho ở BCE06 giữ hai người cùng một nhóm thế kỷ.
4. Quy tắc §5.3 của dự án xếp theo **floruit**, và floruit quy ước của bà là "k. 600 TCN" — năm 600 nằm trong khoảng BCE06 (600–501 TCN) theo `atlaslib/common.py: group_range`.

**Lập luận ngược (để Owner cân nhắc, tôi không chọn):** *Suda* đặt hoạt động của bà ở Olympiad 42 (612–608 TCN), tức TK 7; và `reports/review-ch02.md` N1 đề nghị BCE07. Nếu Owner ưu tiên chứng cứ *Suda*, đổi ID thành **CH02-BCE07-08** — phần còn lại của mục không phải sửa gì, vì `lint` chấp nhận cả hai (đời 630–570 TCN giao với cả khoảng 700–601 lẫn 600–501).

**Lưu ý một con số trong review:** N1 viết "nhóm BCE07, nhóm đang chỉ có 6/10 người". Đếm thực tế trong `content/ch02.md` là **7** mục BCE07 (CH02-BCE07-01 … -07), và BCE06 có **10**, tổng chapter **33**. Không ảnh hưởng kết luận của N1, nhưng nên sửa con số khi đóng finding.

---

## 1. Mục hoàn chỉnh — dán vào cuối nhóm BCE06

```markdown
### CH02-BCE06-11 · Sappho xứ Lesbos (Σαπφώ Sapphṓ)
`năm: k. 630–570 TCN | nơi: Mytilene (nguồn cổ cũng ghi Eresos), đảo Lesbos, nay thuộc Hy Lạp | vùng: Châu Âu | lĩnh vực: Văn học | độ tin cậy niên đại: Trung bình | wikidata: Q17892 | câu hỏi lớn: Con người`

**Tư tưởng / đóng góp chính (~100 chữ):** Thơ bà thuộc dòng melic đơn ca: bài hát ngắn bằng phương ngữ Aeolic, hát với đàn lyre trong nhóm nhỏ, khác thơ iambus ngâm đọc. Đóng góp bền nhất là biến ham muốn thành đối tượng quan sát: mảnh 31 liệt kê triệu chứng cơ thể của người nhìn người mình yêu ngồi cạnh kẻ khác; mảnh 16 đặt cái mỗi người yêu lên trên kỵ binh và hạm thuyền của sử thi. Khổ bốn dòng mang tên bà trở thành khuôn mẫu thơ Latin, dù Alcaeus cùng thời cũng dùng. Bản Alexandria ít nhất tám quyển, ước mười nghìn dòng; nay còn khoảng sáu trăm năm mươi dòng, phần lớn nhờ giấy cói Ai Cập, và chỉ mảnh 1 chắc chắn trọn vẹn.

**Vì sao chọn (~80 chữ):** Hai ứng viên cùng thời đã cân nhắc: Alcaeus (k. 625–580 TCN), cùng thành Mytilene, cùng hệ khổ thơ; và Stesichorus (k. 630–555 TCN), cũng trong kinh điển chín nhà thơ trữ tình Alexandria. Sappho vượt ở độ bền (b): thơ phe phái của Alcaeus gắn chặt bối cảnh Mytilene đã mất; hai mươi sáu quyển của Stesichorus nay gần như thất truyền; còn mảnh 31 được Catullus dịch thành bài 51, và khổ thơ mang tên bà đi tiếp qua Horace vào thánh ca Latin. Về phạm vi (a), bà là người nữ duy nhất trong kinh điển ấy.

**Kế thừa từ:**
- CH02-BCE08-01 · phản bác · suy đoán học giả
- Truyền thống ca khúc Aeolic ở Lesbos (Terpander) · kế thừa · suy đoán học giả

**Ảnh hưởng tới:**
- Catullus (Gaius Valerius Catullus) · kế thừa · trực tiếp
- Horace (Quintus Horatius Flaccus) · kế thừa · trực tiếp
- Thánh ca Latin trung cổ theo khổ Sapphic · kế thừa · qua trường phái

**Nguồn:** Eva-Maria Voigt, *Sappho et Alcaeus: Fragmenta* (Amsterdam, 1971) — bản hiệu đính chuẩn, cũng là hệ đánh số mảnh dùng ở mục này; Anton Bierl và André Lardinois (chủ biên), *The Newest Sappho: P. Sapph. Obbink and P. GC inv. 105, Frs. 1–4* (Brill, 2016).
```

---

## 2. Hai số đếm chữ

Đếm bằng chính hàm của `atlaslib/lint.py` (`len([w for w in s.split() if w])`), trên phần văn bản **sau** nhãn in đậm, đúng như `parse.py` cắt trường:

| Trường | Số chữ | Khoảng lint cho phép | Kết quả |
|---|---|---|---|
| `Tư tưởng / đóng góp chính` | **125** | 70–130 (±30% quanh 100) | đạt, dư 5 chữ |
| `Vì sao chọn` | **100** | 56–104 (±30% quanh 80) | đạt, dư 4 chữ |

---

## 3. Bảng kiểm chứng từng khẳng định

| # | Khẳng định trong mục | Nguồn | Đã làm gì để xác nhận |
|---|---|---|---|
| 1 | Q-ID là **Q17892** | Wikidata API | Gọi `wbgetentities&ids=Q17892`. Nhãn en/vi = "Sappho"; description en = "ancient Greek poet from Lesbos (c. 630-c. 570 BC)"; **P31 = Q5** (là người, nên không cần nhãn [Truyền thuyết]); P21 = Q6581072 (nữ); P106 gồm Q49757 (nhà thơ). Đúng người. |
| 2 | `năm: k. 630–570 TCN` | Wikidata P569/P570 | P569 có giá trị **−0630** (precision 9) và hạng preferred **−0650** (precision 7, tức chỉ chính xác tới thế kỷ); P570 hạng **preferred = −0570** (precision 9). Lint lấy giá trị *gần nhất*: lệch **0 năm** cho cả năm sinh lẫn năm mất. Với `độ tin cậy: Trung bình` (dung sai ±25 theo `DATE_TOLERANCE`), vượt qua thoải mái. |
| 3 | `nơi:` Mytilene, nguồn cổ cũng ghi Eresos, đảo Lesbos | Wikidata P19 | P19 có ba giá trị: **Q42295059 = Mytilene**, **Q1018197 = Eresos**, **Q128087 = Lesbos** (hạng preferred). Tôi tra nhãn từng Q-ID qua API. Cách ghi trong mục phản ánh đúng việc nguồn cổ chia rẽ giữa hai thành. |
| 4 | `lĩnh vực: Văn học`, `vùng: Châu Âu` | `atlaslib/common.py` | Đối chiếu trực tiếp `FIELDS` và `REGIONS`. 1 lĩnh vực (≤2), 1 vùng (đúng 1). Giữ một lĩnh vực cho nhất quán với Homer, Hesiod, Archilochus — cả bốn đều chỉ ghi "Văn học", dù thơ melic là thơ **hát** nên về lý có thể thêm "Nghệ thuật/Kiến trúc". |
| 5 | `câu hỏi lớn: Con người` | `BIG_QUESTIONS` | Trong từ vựng; cùng lựa chọn với Homer và Archilochus. |
| 6 | Thơ melic đơn ca, phương ngữ Aeolic, hát với đàn lyre, **khác thơ iambus ngâm đọc** | Wikipedia "Nine Lyric Poets"; "Iambus (genre)" | Trang kinh điển chín nhà thơ nói rõ kinh điển này **loại trừ** "the elegy and iambus"; trang *Iambus* xác nhận bộ ba iambographer kinh điển là **Archilochus, Semonides, Hipponax**, một thể loại riêng. Đây là cơ sở để gỡ va chạm "người đầu tiên" với Archilochus (mục 5 bên dưới). |
| 7 | Mảnh 31: liệt kê triệu chứng cơ thể | Wikipedia "Sappho 31" | Bài nêu nguyên chuỗi triệu chứng: tim đập dồn, không nói được, lưỡi gãy/cứng, lửa mỏng chạy dưới da, mắt không thấy, tai ù, mồ hôi lạnh, run, tái hơn cỏ. Còn **bốn khổ trọn vẹn cộng vài chữ của khổ thứ năm**. Tôi cố ý **không** gọi cảm xúc trong bài là "ghen tuông": cách đọc đó là do bản phóng tác của Catullus áp vào, và còn tranh luận. |
| 8 | Mảnh 16: đặt cái mỗi người yêu lên trên kỵ binh và hạm thuyền của sử thi | Wikipedia "Sappho 16" | Bài mô tả đúng cấu trúc priamel: "some say an army of horsemen, others say foot soldiers, still others say a fleet" rồi đặt "whatever one loves" lên trên. Lưu ý đã rào: giới nghiên cứu **còn tranh luận** đây có phải là bác bỏ thang giá trị quân sự của sử thi hay không — nên trong mục tôi chỉ mô tả thao tác của bài thơ, không gán cho bà một tuyên ngôn. |
| 9 | Mảnh 16 truyền qua giấy cói | Wikipedia "Sappho 16" | **P.Oxy. 1231** (bản chép TK 2, công bố 1914), được bổ sung thêm chữ nhờ **P.GC inv. 105** do Burris, Fish và Obbink công bố 2014. |
| 10 | Khổ Sapphic: bốn dòng, ba dòng mười một âm tiết + một dòng adonean | Wikipedia "Sapphic stanza" | "3 lesser Sapphic lines followed by an adonic"; dòng Sappho nhỏ có 11 âm tiết. |
| 11 | **"dù Alcaeus cùng thời cũng dùng"** | Wikipedia "Sapphic stanza" | Nguyên văn: Alcaeus "composed in, and **may have invented**, the Sapphic stanza". Đây là lý do tôi **không** viết rằng Sappho sáng tạo ra khổ thơ này — tên gọi là do đời sau gán. |
| 12 | Khổ thơ "trở thành khuôn mẫu thơ Latin" | Wikipedia "Sapphic stanza" | Horace dùng khổ Sapphic cho **25 bài Odes** cộng *Carmen Saeculare*, và chuẩn hoá vị trí ngắt nhịp. |
| 13 | Đi tiếp "vào thánh ca Latin" | Wikipedia "Sapphic stanza" | Thể thơ sống qua trung cổ dù hệ nhịp chuyển từ lượng sang trọng âm; ví dụ tiêu biểu là thánh ca **"Ut queant laxis"**, chính bài cho ra tên các nốt sol-fa. |
| 14 | Bản Alexandria "ít nhất tám quyển" | Wikipedia "Sappho" | Nguyên văn: bản hiệu đính "was divided into at least eight books". Tôi dùng "ít nhất tám" chứ không dùng con số chín thường gặp, vì chín là con số còn tranh luận. |
| 15 | "ước mười nghìn dòng; nay còn khoảng sáu trăm năm mươi dòng" | Wikipedia "Sappho" | Nguyên văn: "Sappho probably wrote around 10,000 lines of poetry; today, only about 650 survive". Giữ nguyên dạng ước lượng, **không làm tròn lên**. |
| 16 | "chỉ mảnh 1 chắc chắn trọn vẹn" | Wikipedia "Sappho"; "Ode to Aphrodite" | Nguyên văn trang Sappho: "only the Ode to Aphrodite is certainly complete". Trang *Ode to Aphrodite* xác nhận bài được **Dionysius xứ Halicarnassus** chép **trọn vẹn** trong khảo luận *On Literary Composition*, và còn một phần trên **P.Oxy. 2288**. Có hai chỗ đọc còn ngờ (chữ đầu bài và dòng 19) — đó là lý do tôi viết "chắc chắn trọn vẹn" chứ không viết "nguyên vẹn". |
| 17 | Mảnh 31 do Longinus chép | Wikipedia "Sappho 31" | Được giữ trong *On the Sublime* (khảo luận TK 1 CN gán cho Longinus), dẫn ra làm ví dụ về cường độ cảm xúc. |
| 18 | **Alcaeus k. 625–580 TCN, cùng thành Mytilene, đồng thời** | Wikipedia "Alcaeus of Mytilene" | "c. 625/620 – c. 580 BC"; được mô tả là "a contemporary and a countryman of Sappho", sống ở Mytilene trên đảo Lesbos. **Đã kiểm tra đúng là người cùng thời** (yêu cầu bắt buộc sau lỗi lệch 123 năm của mục trước). |
| 19 | Thơ Alcaeus là thơ phe phái gắn bối cảnh Mytilene | Wikipedia "Alcaeus of Mytilene" | Ông làm thơ về các cuộc tranh quyền ở Mytilene, về Myrsilus và Pittacus, từng dự âm mưu thất bại và đi đày. |
| 20 | **Stesichorus k. 630–555 TCN**, trong kinh điển chín người | Wikipedia "Stesichorus" | "c. 630–555 BC"; thuộc "the nine lyric poets esteemed by the scholars of Hellenistic Alexandria". **Đã kiểm tra đúng là người cùng thời với Sappho.** |
| 21 | "hai mươi sáu quyển của Stesichorus nay gần như thất truyền" | Wikipedia "Stesichorus" | Bản Alexandria gồm **26 quyển**, nay chỉ còn mảnh vụn; một nhà nghiên cứu được dẫn: "Time has dealt more harshly with Stesichorus than with any other major lyric poet." |
| 22 | Sappho là **người nữ duy nhất** trong kinh điển chín nhà thơ trữ tình | Wikipedia "Nine Lyric Poets" | Danh sách chín người: Alcman, Sappho, Alcaeus, Anacreon, Stesichorus, Ibycus, Simonides, Bacchylides, Pindar — tám người còn lại đều là nam. (Rào riêng: Antipater xứ Thessalonica về sau đề một danh sách **khác**, gồm chín nữ thi sĩ; câu trong mục chỉ nói về kinh điển chín nhà thơ trữ tình, nên vẫn đúng.) |
| 23 | Catullus dịch mảnh 31 thành bài 51 | Wikipedia "Sappho 31" | Catullus phóng tác trực tiếp mảnh 31 thành bài 51, đặt Lesbia vào vai người được yêu trong bài của Sappho. Đây là cơ sở cho mức bằng chứng **trực tiếp** ở liên kết Catullus. |
| 24 | Liên kết Horace ở mức **trực tiếp** | Wikipedia "Sapphic stanza"; "Alcaeus of Mytilene" | Horace dùng khổ Sapphic cho 25 bài Odes và tự nhận công đưa thể thơ Aeolic vào Latin (*Odes* 3.30). Quan hệ có văn bản chứng minh, không phải suy đoán. |
| 25 | Nguồn 1 — Voigt, *Sappho et Alcaeus: Fragmenta* (1971) | Open Library API | Tra `openlibrary.org/search.json`: có bản ghi "Sappho et Alceus, fragmenta edidit Eva-Marie Voigt", năm 1971. **Sách có thật.** Đây là bản hiệu đính chuẩn và là hệ đánh số mảnh (1, 16, 31) dùng trong mục. |
| 26 | Nguồn 2 — Bierl & Lardinois (ch.b.), *The Newest Sappho* (Brill, 2016) | Open Library API | Tra được hai bản ghi khớp: "The Newest Sappho : P. Sapph. Obbink and P. GC inv. 105, Frs. 1-4", tác giả/chủ biên **Anton Bierl** và **A. P. M. H. Lardinois**, nhà xuất bản **Brill**, năm **2016**, khoảng 543–560 trang. **Sách có thật và đúng là nói về Sappho** — toàn bộ tập bàn về chính hai giấy cói mới. |

---

## 4. Những chỗ tôi cố ý **không** viết, và lý do

Owner dặn riêng mấy điểm; đây là kết quả kiểm tra.

### 4.1 Epigram "Nàng Thơ thứ mười" gán cho Plato — **đã kiểm tra, và đã loại khỏi mục**

`reports/review-ch02.md` N1 dùng câu "Plato gọi là 'Nàng Thơ thứ mười'" làm một trong các bằng chứng cho tiêu chí (a). Tôi **không đưa câu này vào mục**, vì hai lý do:

1. **Nguồn sớm nhất gọi bà là Nàng Thơ thứ mười không phải Plato.** Theo Wikipedia "Sappho", văn bản còn lại sớm nhất làm việc đó là **một epigram TK 3 TCN của Dioscorides**; các bài cùng chủ đề trong *Greek Anthology* thì của **Antipater xứ Sidon**, và *một bài được gán cho Plato*.
2. Cách diễn đạt "attributed to Plato" chính là vấn đề: các epigram gán cho Plato trong *Greek Anthology* là một khối văn bản mà giới nghiên cứu từ lâu phần lớn coi là **nguỵ tác thời Hy Lạp hoá**, không phải tác phẩm Plato.

Thay vào đó mục dùng **kinh điển chín nhà thơ trữ tình Alexandria** làm chứng cứ cho tiêu chí (a) — đây là sự kiện văn bản học vững, không phụ thuộc vào một quy gán đang tranh cãi.

*Có thật là Plato nhắc Sappho*, nhưng ở chỗ khác: trong *Phaedrus* (bài diễn từ thứ hai của Socrates về tình yêu), và chỗ đó cũng chỉ là nhắc tên cùng một tiếng vọng của mảnh 31, không phải lời tôn xưng. Tôi không dùng vì quá mỏng cho một mục 125 chữ.

**Đề nghị với Owner:** khi đóng finding N1, nên ghi lại rằng luận cứ "Plato gọi là Nàng Thơ thứ mười" trong chính bản review là **một quy gán không đứng vững** — nếu không, lỗi này sẽ đi vào chapter qua đường review.

### 4.2 Tiểu sử — không viết gì như thể là sự thật đã xác lập

Mục này **không** nhắc: Phaon, cú nhảy từ mỏm Leucas, chồng "Kerkylas xứ Andros" (một cái tên mà *Suda* chép và nhiều nhà nghiên cứu đọc là trò đùa tục của hài kịch Attica), trường nữ sinh, hay bất cứ chuyện tình nào. Lý do: gần như toàn bộ "tiểu sử" Sappho là **suy diễn ngược từ chính thơ bà, cộng với biếm hoạ của hài kịch Attica và văn chương La Mã** (Ovid, *Heroides* 15 — bản thân bài này cũng có tranh cãi về tác quyền). Mục chỉ khẳng định những gì có chỗ dựa văn bản: thể loại, nội dung hai mảnh thơ, khổ thơ, tình trạng văn bản, và tiếp nhận.

Hệ quả hình thức: **không gắn nhãn `[Tranh cãi lịch sử]`**. Nhãn đó dành cho người mà *sự tồn tại* bị nghi ngờ (Homer, Lão Tử, Zarathustra). Sự tồn tại của Sappho không bị nghi ngờ — chỉ tiểu sử của bà là không đáng tin. Hai chuyện khác nhau, và trộn lẫn sẽ làm nhãn mất nghĩa.

### 4.3 Giấy cói mới và câu hỏi về tính xác thực

Mục chỉ viết "phần lớn nhờ giấy cói Ai Cập" — một khẳng định không thể sai. Tôi **không** đưa vụ **P.Sapph.Obbink** (Brothers Poem và Kypris Poem, Dirk Obbink công bố 2014) vào thân mục, vì trong 125 chữ không có cách nào rào cho đúng. Nhưng đây là thứ Owner cần biết khi đọc nguồn thứ hai tôi dẫn:

- Tranh cãi chủ yếu là về **xuất xứ (provenance) và tính hợp pháp** của mảnh giấy cói, không phải về việc bài thơ có phải thơ cổ hay không.
- Chính vì thế tôi dẫn **Bierl & Lardinois 2016** chứ không dẫn riêng bài công bố của Obbink: tập Brill là nơi tập hợp cả văn bản lẫn tranh luận quanh nó.
- Chi tiết của vụ này nằm ngoài phạm vi những gì tôi tự xác minh được trong lần chạy này — xem mục 7.

---

## 5. Va chạm "người đầu tiên" với Archilochus — có thật, và cách gỡ

### Vấn đề

`CH02-BCE07-04` (Archilochus) hiện viết, trong **Vì sao chọn**:

> Archilochus vượt trội ở tính nguyên bản (c): ông là **người đầu tiên đặt kinh nghiệm cá nhân, kể cả kinh nghiệm đáng xấu hổ, làm đề tài hợp lệ của thơ trữ tình đơn ca** — Hesiod đã nói ở ngôi thứ nhất nhưng trong khuôn sử thi giáo huấn, và ở độ bền (b): Horace, Catullus rồi cả truyền thống thơ trữ tình châu Âu đều nhận ảnh hưởng, trong khi Tyrtaeus chỉ sống trong giáo dục Sparta.

Thêm Sappho tạo ra va chạm — nhưng **không phải va chạm về niên đại**. Archilochus (k. 680–645 TCN) có trước Sappho (k. 630–570 TCN), nên chữ "đầu tiên" không sai về thời gian. Va chạm nằm ở **thuật ngữ thể loại**:

- Cụm "**thơ trữ tình đơn ca**" (monodic lyric) trong nghĩa cổ điển chỉ **thơ melic**: bài hát với đàn lyre. Đó chính xác là thể loại của Sappho và Alcaeus — và **không** phải thể loại của Archilochus.
- Archilochus làm **iambus và elegy**. Kinh điển Alexandria phân biệt rạch ròi: danh sách **chín nhà thơ trữ tình** (có Sappho) **loại trừ** elegy và iambus; Archilochus đứng ở một kinh điển khác, bộ ba **iambographer** cùng Semonides và Hipponax.

Nói cách khác, mục Archilochus đang dùng đúng cái nhãn thể loại mà kinh điển cổ dành cho Sappho, để trao cho Archilochus danh hiệu "người đầu tiên". Giữ nguyên hai mục cạnh nhau sẽ khiến người đọc thấy mâu thuẫn.

### Cách gỡ — đúng mô hình Owner đã dùng cho va chạm Hesiod/Archilochus: **phân biệt bằng thể loại**

Sửa **một cụm từ** trong mục Archilochus. Dòng hiện tại:

```
Archilochus vượt trội ở tính nguyên bản (c): ông là người đầu tiên đặt kinh nghiệm cá nhân, kể cả kinh nghiệm đáng xấu hổ, làm đề tài hợp lệ của thơ trữ tình đơn ca — Hesiod đã nói ở ngôi thứ nhất nhưng trong khuôn sử thi giáo huấn, và ở độ bền (b):
```

Đề nghị thay thành:

```
Archilochus vượt trội ở tính nguyên bản (c): ông là người đầu tiên đặt kinh nghiệm cá nhân, kể cả kinh nghiệm đáng xấu hổ, làm đề tài hợp lệ của thơ iambus và elegy — Hesiod đã nói ở ngôi thứ nhất nhưng trong khuôn sử thi giáo huấn, và ở độ bền (b):
```

Đổi **bốn chữ** ("thơ trữ tình đơn ca" → "thơ iambus và elegy"). Sau khi sửa:

- Archilochus giữ nguyên danh hiệu "người đầu tiên", chỉ được khoanh đúng vào thể loại của ông — thể loại mà kinh điển cổ xếp riêng.
- Sappho giữ "melic đơn ca" làm địa hạt của mình, đúng như cách Alexandria phân loại.
- Mục Sappho đã chủ động đỡ sẵn: câu mở đầu viết "**khác thơ iambus ngâm đọc**" chính là để bắt tay với chỗ sửa này.
- Mục Sappho **không** dùng chữ "người đầu tiên" ở bất cứ đâu, nên không tạo va chạm mới.

**Số chữ sau khi sửa:** cụm thay thế dài **4 chữ**, cụm bị thay dài **4 chữ** — tổng số chữ của trường `Vì sao chọn` ở mục Archilochus **không đổi**, nên lint không đổi trạng thái.

---

## 6. Đề nghị sửa liên kết đối ứng ở các mục đã có

Giữ ở mức tối thiểu. Tôi chỉ đề nghị những chỗ mà **không sửa thì sai hoặc thiếu nhất quán**, chứ không rải liên kết cho đẹp.

### 6.1 BẮT BUỘC — `CH02-BCE07-04` Archilochus, trường `Vì sao chọn`

Đã trình bày ở mục 5. Đây là sửa chữ, không phải sửa liên kết, nhưng là hệ quả trực tiếp của việc thêm Sappho nên phải làm cùng lúc.

### 6.2 BẮT BUỘC — phần `**Giới thiệu chapter**`, con số nhân vật

Dòng hiện tại:

> Bốn nhóm thế kỷ gồm **33 nhân vật**, từ vua Assyria và ngôn sứ Do Thái tới Khổng Tử, Đức Phật, Thales và Socrates, chọn theo phạm vi, độ bền, tính nguyên bản và counterfactual.

Đề nghị:

> Bốn nhóm thế kỷ gồm **34 nhân vật**, từ vua Assyria và ngôn sứ Do Thái tới Khổng Tử, Đức Phật, Thales và Socrates, chọn theo phạm vi, độ bền, tính nguyên bản và counterfactual.

(Chỉ đổi con số. Giới thiệu chapter đang ở dưới trần 130 chữ nên không ảnh hưởng lint.)

### 6.3 BẮT BUỘC — `## Ghi chú biên tập`, nói ra việc chapter trước đó không có người nữ nào

N1 nhấn mạnh đây là **vấn đề riêng**, độc lập với việc có thêm Sappho: "số lượng ứng viên nữ có nguồn quả thật rất ít — nhưng đó là một **phát hiện phải viết ra**, không phải một khoảng lặng." Đề nghị thêm một mục mới vào `Ghi chú biên tập`:

```markdown
**Về độ phủ giới**
Bản thảo đầu của chapter này có 33 nhân vật và không có người nữ nào, mà không nói gì về điều đó. Sappho (CH02-BCE06-11) được bổ sung sau bình duyệt. Sau khi bổ sung, tỉ lệ là 1/34 — con số này phản ánh hai thứ chồng lên nhau, và không nên đọc lẫn: trong cửa sổ 800–401 TCN, rất ít phụ nữ để lại tác phẩm hoặc hành động được nguồn đương thời định danh; và chính việc chọn lọc, sao chép, lưu truyền của đời sau cũng đã lọc bớt. Sappho là trường hợp hiếm còn văn bản để đọc, và ngay cả văn bản của bà cũng chỉ còn khoảng 650 trên ước chừng 10.000 dòng. Các ứng viên nữ đã rà và không chọn được vì không đủ tư liệu cá nhân: Enheduanna (thuộc Chapter 1 về niên đại), Telesilla xứ Argos và Korinna (niên đại tranh cãi, nhiều khả năng muộn hơn cửa sổ này), Gargī Vācaknavī và Maitreyī (nhân vật trong Bṛhadāraṇyaka Upaniṣad, không có tiểu sử độc lập — cùng vấn đề với Yajnavalkya).
```

> **Rào:** mục đề nghị này nêu đích danh bốn ứng viên nữ. Lý do loại của Enheduanna (niên đại ~TK 23 TCN, thuộc Chapter 1) là chắc chắn. Ba trường hợp còn lại tôi nêu theo hiểu biết chung và **chưa xác minh từng cái trong lần chạy này** — xem mục 7. Nếu Owner muốn đưa đoạn này vào chapter, nên kiểm lại niên đại Telesilla và Korinna trước, hoặc rút gọn đoạn còn phần không cần kiểm.

### 6.4 ĐÃ CÂN NHẮC VÀ **KHÔNG** ĐỀ NGHỊ — thêm Sappho vào `Ảnh hưởng tới` của Homer

Mục Sappho có `Kế thừa từ: CH02-BCE08-01 · phản bác · suy đoán học giả` (mảnh 16 đặt lựa chọn riêng tư cạnh thang giá trị sử thi). Về đối ứng, lẽ ra Homer nên có dòng trỏ ngược lại. Nhưng `Ảnh hưởng tới` của Homer **đã đủ ba mục** (CH02-BCE08-02, CH02-BCE05-06, Virgil), tức đã chạm trần của template. Thêm mục thứ tư sẽ bật cảnh báo lint.

Chapter đã chấp nhận liên kết **không đối xứng** ở nhiều chỗ (ví dụ `Kế thừa từ` của Hesiod trỏ tới vũ trụ luận Cận Đông mà không có chiều ngược lại), nên để nguyên là nhất quán. **Đề nghị: không sửa mục Homer.**

### 6.5 ĐÃ CÂN NHẮC VÀ **KHÔNG** ĐỀ NGHỊ — liên kết Archilochus ↔ Sappho

Không có bằng chứng Sappho đọc Archilochus, cũng không có chiều ngược lại. Theo đúng quy ước cuối `prompts/atlas-prompt.md` ("không suy diễn quan hệ kế thừa khi thiếu bằng chứng"), **không thêm liên kết nào giữa hai mục**. Quan hệ thật giữa họ là quan hệ **thể loại**, và đã được xử lý bằng cách sửa chữ ở mục 5.

### 6.6 TUỲ Owner — mục `Ứng viên mạnh đã bị loại`

Nếu Owner chọn **BCE06** như bản này, không cần làm gì. Nếu Owner quyết định **không** đưa Sappho vào chapter, thì theo N1 bà **bắt buộc** phải xuất hiện trong danh sách ứng viên bị loại kèm lý do thật — và lý do "không đủ chỗ" không đứng được, vì BCE06 đã nâng trần lên 12 và đang có 10.

---

## 7. Những gì tôi **không** xác minh được trong lần chạy này

Nói thẳng, không giấu:

1. **Ngân sách tìm kiếm web của phiên đã hết** (200/200 lượt WebSearch) ngay sau truy vấn Wikidata. Toàn bộ phần còn lại tôi làm bằng **WebFetch tới URL đã biết** và **API công khai** (Wikidata, Open Library). Nghĩa là tôi xác minh được *những gì tôi biết địa chỉ để tới*, nhưng không quét rộng được.

2. **Britannica không kiểm tra được.** `https://www.britannica.com/biography/Sappho-Greek-poet` trả **HTTP 403** cho cả WebFetch lẫn curl. Vì `reports/review-ch02.md` đã bắt được ba lỗi Britannica (S2, S3, S4 — mục không tồn tại hoặc sai tên), tôi **chủ động không dẫn Britannica**, và dùng hai chuyên khảo đã xác minh được qua Open Library thay thế. Điều này cũng hợp với yêu cầu "ưu tiên chuyên khảo hoặc văn bản gốc hơn bách khoa toàn thư".

3. **Oxford Classical Dictionary: không xác minh được.** OCD nằm sau tường phí, tôi không mở được để xác nhận có mục "Sappho" và ai viết. Vì vậy **không dẫn OCD**, dù ba mục Hy Lạp khác trong chapter (Homer, Hesiod, Archilochus) đều dẫn.

4. **Phần lớn kiểm chứng sự kiện dựa trên Wikipedia tiếng Anh**, không phải trên bản in của chuyên khảo. Hai nguồn tôi dẫn trong mục (Voigt 1971; Bierl & Lardinois 2016) tôi đã xác minh là **có thật và đúng chủ đề** qua Open Library, nhưng **tôi chưa đọc nội dung bên trong** để đối chiếu từng câu. Đây đúng là giới hạn mà khối minh bạch của chapter đã tự nhận ("Mục Nguồn là điểm khởi đầu để tự kiểm tra, chưa được đối chiếu từng câu") — nhưng cần nói ra ở đây chứ không để ngầm.

5. **Vụ P.Sapph.Obbink: tôi chưa tự xác minh.** Tôi biết đủ để **không** đưa nó vào thân mục, và dẫn một nguồn (Bierl & Lardinois 2016) chuyên bàn về nó. Nhưng các chi tiết cụ thể — ai nêu phản đối, kết luận ra sao, mảnh giấy cói hiện ở đâu, chuyện gì xảy ra với Dirk Obbink — tôi **không xác nhận được trong lần chạy này** và do đó **không khẳng định điều gì** về chúng, kể cả trong báo cáo này. Nếu Owner muốn đưa chuyện này vào chapter, cần một lần kiểm riêng.

6. **Bốn ứng viên nữ nêu ở đoạn đề nghị 6.3** (Enheduanna, Telesilla, Korinna, Gargī/Maitreyī): chỉ Enheduanna là chắc. Ba trường hợp kia chưa kiểm niên đại. Đã rào ngay tại chỗ.

7. **Dioscorides và epigram "Nàng Thơ thứ mười":** tôi xác nhận được *qua trang Wikipedia "Sappho"* rằng văn bản sớm nhất gọi bà như vậy là epigram TK 3 TCN của Dioscorides, và rằng bài cùng chủ đề trong *Greek Anthology* chỉ **được gán** cho Plato. Tôi **không** truy được số hiệu chính xác trong *Palatine Anthology*, cũng không truy được tới công trình chuyên môn bác bỏ tác quyền Plato. Vì vậy kết luận hành động của tôi là **không dùng chi tiết này trong mục** — mức chắc chắn hiện có đủ để loại bỏ, không đủ để khẳng định.

8. **Niên đại nhóm:** như mục 0, bằng chứng cổ không ngả hẳn về BCE06 hay BCE07. Tôi chọn BCE06 theo chỉ định của Owner và theo lập luận "phần lớn đời trưởng thành sau 600 TCN", nhưng đây là một **phán đoán**, không phải một kết quả. *Suda* đứng về phía BCE07.
