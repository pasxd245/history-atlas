# Rổ 1 — bình duyệt độc lập các mục CÂN NHẮC cần nguồn ngoài repo

Ngày: 2026-11-03. Agent bình duyệt độc lập, vòng "rổ 1".
Phạm vi: ~40 mục CÂN NHẮC rút từ chín báo cáo trước, mỗi mục đều cần tra
nguồn ngoài repo mới kết luận được.

Quy ước kết luận: **BẮT BUỘC sửa** · **NÊN sửa** · **KHÔNG CẦN SỬA** ·
**[KHÔNG KIỂM ĐƯỢC]**.

Nguyên tắc tự áp: báo cáo cũ không được coi là đúng mặc định (vòng 1 của
CE08 đã ký ✓ cho ba mệnh đề sai). Mọi câu thay thế tôi đề xuất đều được
soi lại bằng chính bộ tiêu chí đã dùng để chẩn câu gốc, kèm đếm chữ.

---

## Ca 1 — `ch05-ce06-review.md:288` · "Bộ Khai Hoàng luật năm 583"

**Phát hiện cũ (nguyên văn rút gọn):** *"Niên hiệu Khai Hoàng bắt đầu 581 và bộ
luật có một bản ban **581** rồi một bản sửa **583**; ghi trần 'năm 583' bỏ mất
việc đây là bản sửa."* Đề xuất cũ: "**bản 583 của** Khai Hoàng luật".

**Câu trong repo** (`content/ch05.md:95`, mục Tùy Văn Đế):
> Bộ Khai Hoàng luật năm 583 rút hình phạt xuống năm bậc và bỏ nhiều nhục hình…

**Tra ngoài:**
- zh.wikipedia 《开皇律》: *"开皇元年（581年）… 制定《新律》。十月完成，颁布实行。
  三年（583年）… 对新律重新更定，制成《开皇律》。"* → bản 581 mang tên **《新律》**,
  chỉ bản 583 mới mang tên **《开皇律》**.
- en.wikipedia "Kaihuang Code", mục *Formulation and enactment*: bản 581 là
  "New Laws"; bản 583 "were duly proclaimed as the Kaihuang Code".
- Britannica có mục từ riêng **"New Code of 581"**, tách khỏi Kaihuang Code; mục
  "China — The Sui dynasty" viết *"In 583 his ministers compiled a revised code,
  the Kaihuang Code"*.

**Kết luận: KHÔNG CẦN SỬA.** Phát hiện cũ sai ở chỗ then chốt: không có "bản 581
của Khai Hoàng luật". 581 là 《新律》 (New Code), 583 là 《开皇律》. Câu hiện tại
gắn đúng tên với đúng năm.

**Cảnh báo về chính đề xuất cũ:** nếu áp "bản 583 của Khai Hoàng luật" thì văn
bản sẽ hàm ý Khai Hoàng luật còn bản khác — tức sửa một câu đúng thành một câu
sai. Đây đúng kiểu lỗi "câu thay thế mang lỗi mới" mà vòng trước đã vấp.

**Ghi chú còn mở, không đòi sửa:** mô tả ngắn của en.wikipedia (`581 legal code
of Sui dynasty China`) mâu thuẫn với chính thân bài của nó. Đó là lỗi của
Wikipedia, không phải của repo; hai nguồn độc lập (zh.wikipedia, Britannica)
đều đứng về phía 583. `[KHÔNG KIỂM ĐƯỢC]` ở mức sử liệu gốc: tôi không mở được
*Tùy thư* 刑法志 trong vòng này, nên kết luận dựa trên nguồn thứ cấp.

---

## Ca 2 — `ch05-ce06-review.md:496` · CH05-CE06-11 Bhavavarman I chắc hơn nguồn một bậc

**Phát hiện cũ:** (a) *"mà giới nghiên cứu thấy gắn riêng với ông"* — Heng & Lavy
viết "seems to" và "if this is true"; (b) *"vị vua **đầu tiên** ở vùng nội địa
Campuchia để lại một cụm bi ký Phạn ngữ tại chỗ đủ dựng lại một triều đại"* —
Vickery xếp ông cạnh Citrasena và cha Vīravarman. Vòng trước để `[KHÔNG KIỂM
ĐƯỢC]` cho (b) vì "không đọc được đủ Vickery".

**Tra ngoài (vòng này đọc được cả hai PDF):**

PDF Heng & Lavy tải về `200`, 205.860 byte, 11 trang, rút được 44.868 ký tự.
Nguyên văn tr. 8:
> "a form of Shiva named Gambhireshvara ("Lord of the Depths"), a god that
> **seems to have been** particularly associated with King Bhavavarman I. This
> has led **some scholars** to associate the northern group with this king's
> capital, and, **if this is true**, …"

PDF Vickery 1994 tải về `200`, 19 trang, 52.593 ký tự. Nguyên văn:
> "the princes who left short Sanskrit inscriptions north and south of the
> Dangrek mountains — **Bhavavarman, Citrasena-Mahendravarman, Vīravarman**,
> Hirayavarman, Candravarman."
> "…separate conquests by the brothers Bhavavarman and Mahendravarman …
> starting from the realm of **their father Vīravarman** which stretched from
> south of Korat to Kratie."
> "the original home area of these two kings **as well as their father
> Vīravarman** was **within Cambodia south of the Dangrek mountains**."
> "With the careers of Bhavavarman I and Citrasena, **and their father
> Vīravarman, placed firmly within Cambodia south of the Dangrek**…"

**Kết luận (a): NÊN sửa.** Phát hiện cũ đúng, nhưng đúng vì một lý do khác lý do
nó nêu. "if this is true" của nguồn rào **bước nhóm đền ↔ kinh đô**, mà mục
không hề đi bước ấy — nên phần ấy của phát hiện bắn trượt. Cái sai thật là mục
**bịa ra một chủ thể**: nguồn viết "seems to have been", không nói ai thấy; mục
viết "giới nghiên cứu thấy", vừa bỏ "seems to" vừa gán cho cả giới nghiên cứu.

**Kết luận (b): NÊN sửa.** Phát hiện cũ **đúng**, và vòng này gỡ được dấu
`[KHÔNG KIỂM ĐƯỢC]` của nó. Vickery — nguồn thứ nhất của chính mục — bốn lần
đặt cha ông **Vīravarman** trong cùng vùng nội địa Campuchia, cùng cụm người để
lại bi ký Phạn ngữ. Mục đang dẫn một nguồn **ngược** lại chữ "đầu tiên" của
chính nó (quy tắc 7). Mệnh đề "trước ông… ở **hạ lưu** Mekong" không cứu được,
vì nó khoanh sang một vùng khác, để lại ấn tượng rằng bức tranh "trước ông" đã
đầy đủ.

**Câu thay thế đề xuất cho trường `Tư tưởng / đóng góp chính`, nguyên văn:**
> Ông thuộc cụm vua sớm nhất ở vùng nội địa Campuchia để lại bi ký Phạn ngữ tại chỗ đủ dựng lại một triều đại, cùng cha ông Vīravarman và Citrasena-Mahendravarman; trước đó, bi ký tại chỗ ở hạ lưu Mekong chỉ cho tên rời rạc vài vua Phù Nam như Gunavarman, Jayavarman và Rudravarman. K.151 và K.439 ở Sambor Prei Kuk, K.53 ở Kdei Ang. K.439 cho thấy thần chính của nhóm đền phía bắc Sambor Prei Kuk là một dạng Śiva tên Gambhireśvara, vị thần dường như gắn riêng với ông. Mô hình ông để lại là mô hình tồn tại: vua Hindu hóa dùng Phạn ngữ làm ngôn ngữ bi ký và Śiva làm thần bảo trợ, chính là khuôn mà Īśānapura rồi Angkor kế tục.

**Soi lại câu thay thế (bắt buộc theo quy tắc của vòng này):**
- **Đếm chữ.** Trường gốc **126** chữ, bản thay **129** chữ, bằng chính
  `atlaslib/lint.py:12` (`len([w for w in s.split() if w])`). Ngưỡng WARN là
  `> 130`, nên 129 **không** bật WARN ✔. Dư chỉ 1 chữ, nên nếu còn muốn thêm gì
  vào trường này thì phải cắt chỗ khác; chỗ cắt rẻ nhất là bỏ
  "và Citrasena-Mahendravarman" (−3 chữ, về 126) — nó chỉ là ví dụ thứ hai,
  Vīravarman mới là phản ví dụ then chốt vì ông là **đời trước**.
- **"sớm nhất" có phải lại là một superlative không?** Có, nhưng là superlative
  về **một cụm**, không về một người, và nó nói đúng cái Vickery nói: cụm
  Vīravarman–Bhavavarman–Citrasena là phản ứng đầu tiên của giới cai trị
  Campuchia trước sự suy của Phù Nam. Tôi **không** viết "cụm vua đầu tiên" để
  khỏi tái lập đúng chữ vừa chẩn.
- **"dường như gắn riêng với ông"** là bản dịch sát "seems to have been
  particularly associated with", không thêm chủ thể nào ✔.
- **"Kdei Ang"** tôi kiểm lại độc lập: có trong văn bản Heng & Lavy, **không**
  có trong Vickery. Dòng `nơi:` ghi "Kdei Ang (Prey Veng)" nên đứng được ✔.
- Không chạm trường `Vì sao chọn`, nên trần 104 không liên quan ✔.

**Phần của mục vòng này kiểm lại và thấy ĐÚNG, không cần sửa:** câu
`Vì sao chọn` viết *"con số 598 mà Coedès rút từ K.151 là mốc duy nhất, và chính
Vickery cho thấy Coedès đã dùng nó sai ngữ cảnh"* khớp nguyên văn Vickery:
*"took the date 598 from inscription K151 … and inserted it into a section of
Ma Touan-lin torn out of context."* ✔

---

## Ca 3 — `ch05-ce06-review.md:545` · dòng Nguồn Boethius ghi tác giả cho bài SEP thứ nhất mà không ghi cho bài thứ hai

**Câu trong repo** (`content/ch05.md:206`):
> … Stanford Encyclopedia of Philosophy, "Anicius Manlius Severinus Boethius"
> (John Marenbon), <https://plato.stanford.edu/entries/boethius/>; Stanford
> Encyclopedia of Philosophy, "Literary Forms of Medieval Philosophy",
> <https://plato.stanford.edu/entries/medieval-literary/>.

**Tra ngoài:** `GET https://plato.stanford.edu/entries/medieval-literary/` trả
`200`; metadata trang khai `<meta name="citation_author" content="Sweeney,
Eileen">`. Vậy tác giả là **Eileen Sweeney**, đúng như báo cáo cũ nói.

**Kết luận: NÊN sửa.** Không phải lỗi sự thật, là lỗi nhất quán trong **cùng một
dòng Nguồn**: hai mục cùng một bộ bách khoa, một mục có tác giả, một mục không.

**Câu thay thế đề xuất, nguyên văn (chỉ phần cuối dòng Nguồn):**
> … Stanford Encyclopedia of Philosophy, "Literary Forms of Medieval Philosophy" (Eileen Sweeney), <https://plato.stanford.edu/entries/medieval-literary/>.

**Soi lại:** dòng `Nguồn` không nằm trong trần chữ nào (`lint.py` chỉ đếm
`ideas`/`why`/`intro`/`context`), nên thêm 2 chữ không gây hệ quả ✔. Tên lấy từ
metadata của chính trang, không từ trí nhớ ✔.

**Ghi nhận thêm, không thuộc phạm vi rổ này:** hai phát hiện BẮT BUỘC/NÊN khác
của cùng báo cáo **đã được áp** vào `content/ch05.md` rồi — dòng 186 nay ghi
"cuối thế kỷ 12" (không còn "đầu thế kỷ 13"), và dòng "Tranh luận về vấn đề phổ
quát" nay ở mức `qua trường phái`, khớp mục Porphyry.

---

## Ca 4 — `ch05-ce07-review.md:379` · CH05-CE07-03 Ali · "Madelung … nghiêng về phía Alid rõ nhất trong giới hiện đại"

**Câu trong repo** (trường `Vì sao chọn`, mục CH05-CE07-03):
> Madelung 1997, nguồn chính của mục, nghiêng về phía Alid rõ nhất trong giới hiện đại.

**Tra ngoài.** Giới điểm sách mô tả *The Succession to Muhammad* (CUP 1997) bằng
những chữ rất gần với mệnh đề của mục, nhưng **không** bằng một xếp hạng:
- "a **pro-Alid reading** of the sources", và tác giả "vigorously, and at times
  disconcertingly, **partisan**";
- Madelung "writes **against the pro-Sunni grain** of almost all of what has
  been written in the entire corpus of Western scholarship hitherto";
- sách được Cộng hoà Hồi giáo Iran trao giải Sách của năm 1997 — một chi tiết
  tiếp nhận, không phải một thước đo học thuật.

**Kết luận: NÊN sửa.** Nội dung của mệnh đề đứng vững; chỗ hỏng là **hình thức
xếp hạng**: "rõ nhất trong giới hiện đại" đòi một phép so sánh toàn giới mà
không nguồn nào thực hiện. Điều các nguồn nói được là *chiều* (thiên Alid) và
*vị thế so với mặt bằng* (ngược chiều phần lớn học thuật phương Tây) — cả hai
đều kiểm được, và nói đủ mạnh cho mục đích của mục là cảnh báo người đọc về
thiên hướng của nguồn.

**Câu thay thế đề xuất, nguyên văn (câu cuối trường `Vì sao chọn`):**
> Madelung 1997, nguồn chính của mục, đọc thiên Alid, ngược chiều phần lớn học thuật phương Tây.

**Soi lại câu thay thế:**
- **Đếm chữ.** `why` gốc **103**, bản thay **104**. Ngưỡng WARN cho `why` là
  `abs(n − 80) > 0.3×80`, tức `n > 104`; vậy 104 **không** bật WARN ✔ — nhưng
  đây là **đúng mép**. Nếu vòng sau còn muốn thêm chữ nào vào trường này thì
  phải cắt trước; chỗ cắt rẻ nhất là "phần lớn" (−2 chữ).
- **Bản thay có còn là so sánh cấp nhất không?** Không. "ngược chiều phần lớn"
  là mệnh đề về đa số, không phải về hạng nhất — tôi kiểm riêng điểm này vì nó
  chính là lỗi đang chẩn.
- Giữ nguyên "Madelung 1997": xem Ca 11 về việc năm in có hai giá trị.

---

## Ca 5 — `ch05-ce07-review.md:488` · CH05-CE07-04 Đường Thái Tông · "sử do chính triều ông soạn"

**Câu trong repo** (trường `Vì sao chọn`):
> Nguồn chính về ông là sử do chính triều ông soạn, và việc ông can thiệp vào
> khởi cư chú được chép lại.

**Trường `Nguồn`** của mục liệt kê: *Cựu Đường thư* (945); *Trinh Quán chính
yếu* (Ngô Căng); Wechsler 1974; Wallace Johnson 1979.

**Tra ngoài:**
- *Cựu Đường thư*: "Originally compiled during the **Five Dynasties and Ten
  Kingdoms** period (10th century AD)", chủ biên ghi danh Lưu Hú. Soạn dưới
  **Hậu Tấn**, gần ba thế kỷ sau khi Thái Tông mất (649) — **không** phải triều
  ông.
- *Trinh Quán chính yếu*: zh.wikipedia 《貞觀政要》 — "為唐代史學家**吳兢**所撰",
  và "吳兢完成此书之后曾经上呈给当时的皇帝**唐玄宗**". Tức soạn đời Đường nhưng
  dưới **Huyền Tông**, khoảng bảy tám chục năm sau khi Thái Tông mất.

**Kết luận: NÊN sửa.** Phát hiện cũ **đúng**. Không nguồn nào trong trường
`Nguồn` là "sử do chính triều ông soạn". Ý mà câu muốn nói — lớp thực lục soạn
đương triều — có thật, nhưng lớp ấy **không** nằm trong trường `Nguồn`, nên câu
đang mô tả sai chính cái nó trỏ tới.

**Vế thứ hai của câu thì ĐÚNG, giữ nguyên:** việc Thái Tông can thiệp vào ghi
chép là có thật và được chép lại — năm **642** ông đòi xem khởi cư chú do **Chử
Toại Lương** giữ và bị từ chối; sau đó **Phòng Huyền Linh** cho xem, và ông yêu
cầu chép vụ Huyền Vũ môn "thẳng" thay vì xoá.

**Câu thay thế đề xuất, nguyên văn (câu cuối trường `Vì sao chọn`):**
> Hai nguồn chính về ông đều soạn sau khi ông mất: Trinh Quán chính yếu đời Huyền Tông, Cựu Đường thư năm 945; việc ông can thiệp vào khởi cư chú vẫn được chép.

**Soi lại câu thay thế:**
- **Đếm chữ.** `why` gốc **93**, bản thay **104** — đúng mép, không bật WARN ✔.
  Mức tăng +11 là đáng kể; nếu Chủ dự án muốn giữ biên an toàn thì cắt
  "đời Huyền Tông" (−3, về 101), đổi lại mất chính cái chi tiết chứng minh
  *Trinh Quán chính yếu* không phải sử đương triều.
- **Mệnh đề mới có kiểm được từng cái không?** "đời Huyền Tông": zh.wikipedia ✔.
  "năm 945": khớp cả trường `Nguồn` hiện có lẫn mô tả "10th century" ✔.
  "vẫn được chép": giữ nguyên vế đã kiểm ✔.
- **Chỗ tôi cố ý không viết:** tôi **không** đưa chữ "thực lục" vào câu thay
  thế, dù đó là ý thật mà báo cáo cũ suy ra. Thực lục Thái Tông **không** nằm
  trong trường `Nguồn`; viết nó vào `Vì sao chọn` sẽ tái lập đúng lỗi đang
  chẩn — mô tả một nguồn mà mục không dẫn. `[KHÔNG KIỂM ĐƯỢC]` ở mức chi tiết:
  tôi không xác minh được niên đại soạn chính xác của *Trinh Quán chính yếu*
  (các mốc 707–709 và đời Huyền Tông đều được đề nghị trong tài liệu); chữ
  "đời Huyền Tông" dựa trên việc Ngô Căng dâng sách cho Huyền Tông, là điều
  zh.wikipedia nói rõ, chứ không dựa trên một niên đại soạn xác định.

---

## Ca 6 — `ch05-ce07-review.md:993` · CH05-CE07-09 Isiđôrô · "Braulio, học trò ông"

**Câu trong repo** (trường `Tư tưởng / đóng góp chính`):
> việc chia thành hai mươi quyển là do Braulio, **học trò ông**, làm sau

**Phát hiện cũ:** "học trò" hẹp hơn hồ sơ; mô tả quy chuẩn gọi Braulio là **bạn**
và người trao đổi thư từ.

**Tra ngoài — tôi mở chính nguồn mà mục dẫn** (Barney et al., *The Etymologies
of Isidore of Seville*, CUP 2006; PDF `200`, 6.830.698 byte, trích được phần
Introduction):

1. Barney gọi thẳng Braulio là **"his disciple Braulio"** ("As his disciple
   Braulio remarked in his *Renotatio*…"). en.wikipedia "Braulio of Zaragoza"
   cũng chép: "In 610 Braulio took the habit of a monk, and was later to
   **study at Isidore's school in Seville**… Braulio was **ordained by Isidore**
   in 624."

2. **Nhưng cùng đoạn ấy lại lật một mệnh đề khác của mục.** Chú thích 56 của
   Barney, nguyên văn:
   > "Furthermore, it seems that Braulio divided the work into **fifteen**
   > books; the division into **twenty** books developed during the course of
   > the **manuscript diffusion** (see Reydellet 1966:435)."

   Và chính bản dịch *Renotatio* in trong sách ấy đọc: *"I divided it into
   twenty (or, '**fifteen**,' in some manuscripts) books"* — tức con số đã vênh
   ngay trong truyền bản của lời Braulio tự khai.

**Kết luận về phát hiện cũ: KHÔNG CẦN SỬA.** Phát hiện 09-4 **sai**. "học trò"
không hẹp hơn hồ sơ — nó là đúng chữ mà nguồn thứ nhất của mục dùng
("his disciple"), và được tiểu sử độc lập chống lưng. Nếu áp phát hiện cũ, mục
sẽ bị sửa **rời xa** nguồn nó dẫn. Đây là ca thứ hai trong vòng này mà một đề
xuất cũ sẽ làm hỏng một câu đang đúng.

**Nhưng cùng câu ấy có một lỗi khác, nặng hơn, mà chín báo cáo trước đều bỏ
sót — BẮT BUỘC sửa.** Mục khẳng định trần rằng Braulio chia sách thành **hai
mươi** quyển. Nguồn thứ nhất của chính mục nói ngược: Braulio có lẽ chia thành
**mười lăm**, và con số hai mươi hình thành trong quá trình sao chép. Đây đúng
dạng quy tắc 7 — nguồn tồn tại, đúng chủ đề, và bị dẫn ngược lại luận điểm của
chính nó.

**Câu thay thế đề xuất cho cả trường `Tư tưởng / đóng góp chính`, nguyên văn:**
> Etymologiae gom phần học thuật cổ điển ông với tới được thành một bộ sắp theo chủ đề, lối giải thích xuyên suốt là truy nguyên từ — việc chia thành quyển là do Braulio, học trò ông, làm sau, còn con số hai mươi có lẽ của khâu sao chép: ông tin rằng biết gốc một từ là biết bản chất của vật mà từ ấy gọi tên. Phương pháp đó sai, nhưng kết quả là một bộ bách khoa bao trùm ngữ pháp, y học, luật, địa lý và nông nghiệp — và với phần lớn Tây Âu năm thế kỷ sau, nó là chỗ gần nhất với một thư viện. Gần một nghìn bản chép tay còn lại, rất lớn với văn bản trung cổ sớm.

**Soi lại câu thay thế — đây là ca căng nhất về trần chữ trong rổ này:**
- **Trường gốc đã ở đúng 130 chữ**, tức sát mép WARN (`> 130`). Mệnh đề đính
  chính tự nó tốn thêm chữ, nên **bắt buộc phải cắt chỗ khác**. Bốn chỗ tôi
  cắt, nói rõ cắt gì ở đâu:
  1. "gom những gì ông còn với tới được của học thuật cổ điển" → "gom phần học
     thuật cổ điển ông với tới được" (**−3**);
  2. "mà lối giải thích" → "lối giải thích" (**−1**);
  3. "một bộ bách khoa **duy nhất** bao trùm" → "một bộ bách khoa bao trùm"
     (**−2**) — cắt này còn là một cái lợi phụ: "duy nhất" tự nó là một cấp
     nhất không đỡ được, vì Tây Âu thời ấy còn Cassiodorus và Pliny;
  4. "trong năm thế kỷ sau" → "năm thế kỷ sau" (**−1**); "con số rất lớn với
     một văn bản trung cổ sớm" → "rất lớn với văn bản trung cổ sớm" (**−2**).
  Tổng cắt **−9**, mệnh đề mới **+8** → trường thành **129 chữ**, dưới 130 ✔
  (đếm bằng `atlaslib/lint.py:12`; lưu ý dấu "—" được hàm ấy tính là một chữ,
  tôi giữ nguyên hai dấu "—" cũ nên không làm lệch phép đếm).
- **Bản thay có mang lỗi mới không?** Tôi viết "**có lẽ** của khâu sao chép",
  không viết "là của khâu sao chép". Lý do: Barney nói "it **seems** that", và
  chính lời Braulio trong truyền bản vẫn đọc "twenty" ở phần lớn thủ bản. Viết
  trần "là" sẽ chỉ là đổi một khẳng định quá chắc này lấy một khẳng định quá
  chắc khác — đúng cái lỗi tôi vừa chẩn.
- Giữ "học trò ông" vì đó là chữ của nguồn, theo kết luận ở trên ✔.

---

## Ca 7 — `ch05-ce07-review.md:1126` · CH05-CE07-10 Pháp Xứng · nguồn SEP không có URL

**Câu trong repo** (trường `Nguồn`, mục CH05-CE07-10):
> Tom J.F. Tillemans, "Dharmakīrti", Stanford Encyclopedia of Philosophy; …

**Tra ngoài:** `GET https://plato.stanford.edu/entries/dharmakiirti/` →
`200`, 145.892 byte. Slug đúng là **`dharmakiirti`** với **hai chữ `i`** — đây
chính là dạng slug mà báo cáo cũ cảnh báo là dễ viết sai, và lần tra này xác
nhận cảnh báo ấy có cơ sở (`dharmakirti` một `i` không phải slug của SEP).

**Kết luận: NÊN sửa.** Không phải lỗi theo §5 của `prompts/atlas-prompt.md`
("kèm link nếu có"), nhưng là lệch nhất quán: `CH05-CE06-12` trong cùng chapter
dẫn SEP kèm URL đầy đủ. Thêm URL cũng khoá luôn slug lại để vòng sau khỏi đoán.

**Câu thay thế đề xuất, nguyên văn (phần đầu trường `Nguồn`):**
> Tom J.F. Tillemans, "Dharmakīrti", Stanford Encyclopedia of Philosophy, <https://plato.stanford.edu/entries/dharmakiirti/>; …

**Soi lại:** trường `Nguồn` không nằm trong `WORD_TARGET`, không chạm trần ✔.
URL đã tự tay gọi và nhận `200` trong vòng này, không chép lại từ báo cáo cũ ✔.
Tên tác giả Tillemans tôi **không** kiểm lại ở vòng này — `[KHÔNG KIỂM ĐƯỢC]`
cho riêng điểm đó.

---

## Ca 8 — `ch05-ce07-review.md:1261` · CH05-CE07-11 Tùng Tán Cán Bố · `Trung bình` cho một năm sinh tán rất rộng

**Dòng trong repo:**
> `năm: k. 617–650 CN | … | độ tin cậy niên đại: Trung bình | wikidata: Q320122 | …`

**Tra Wikidata trực tiếp** (`Special:EntityData/Q320122.json`, `200`, 49.171 byte):

| thuộc tính | giá trị | rank | tham chiếu | precision |
|---|---|---|---|---|
| P569 | +0604 | normal | 1 | 9 (năm) |
| P569 | +0617 | normal | 1 | 9 (năm) |
| P570 | +0650 | normal | 1 | 9 (năm) |

Hai `P569` **cùng rank normal**, không cái nào preferred — Wikidata ở đây không
chọn phe, và theo nguyên tắc của vòng này, `precision 9` nói về độ chính xác
khai báo chứ không nói gì về độ tin cậy.

**Tra ngoài repo:** en.wikipedia "Songtsen Gampo" — *"it is generally accepted
that he was born in an **Ox year** of the Tibetan calendar"*, và các năm Sửu
ứng viên là **557, 569, 581, 593, 605, 617**; thân bài còn nghiêng về **605**
(*"he was probably born in the Ox year 605 CE"*), trong khi Wikidata nghiêng
604/617. Tức biên độ thật của năm sinh là **sáu mươi năm**, không phải ±25.

**Kết luận: NÊN sửa.** Phát hiện cũ **đúng**, và vòng này đo được biên độ mà nó
mới chỉ ước lượng. Theo thang ở `CONTRIBUTING.md:51` (Cao ±5, Trung bình ±25,
Thấp bỏ qua đối chiếu), một năm sinh tán sáu mươi năm **không** nằm trong ±25.
Giữ `Trung bình` cũng không nhất quán nội bộ: `CH05-CE06-11` Bhavavarman được
để `Thấp` cho một khung **hẹp hơn**.

**Sửa đề xuất, nguyên văn (chỉ một trường của dòng metadata):**
> `độ tin cậy niên đại: Thấp`

**Soi lại:** (a) `Thấp` nghĩa là "bỏ qua đối chiếu Wikidata", nên đổi sang
`Thấp` **không** tạo cảnh báo lint mới, chỉ gỡ một khẳng định quá chắc ✔.
(b) Tôi **không** đề xuất đổi chính con số `k. 617` — 617 là một trong các năm
Sửu ứng viên, là giá trị Wikidata, và chữ "k." đã rào sẵn; thay nó bằng 605
chỉ là đổi phe chứ không thêm độ chắc ✔. (c) Trường metadata không nằm trong
`WORD_TARGET` nên không chạm trần nào ✔.

**Một phát hiện mới, không nằm trong rổ, cần vòng sau quyết — về năm MẤT:**
Trường `Nguồn` của mục tự ghi *"bản chép này bắt đầu ở năm 650, **tức năm ông
mất**"*. Nhưng en.wikipedia chép: *"According to the **Tibetan Annals**,
Songtsen Gampo must have died in **649**, and, in 650, the Tang emperor sent an
envoy with a 'letter of mourning and condolences'."* Nếu đúng, thì mốc 650
không phải năm ông mất mà là năm **Đường cử sứ viếng**, và chính câu rào trong
trường `Nguồn` đang nói sai về nguồn nó rào. `[KHÔNG KIỂM ĐƯỢC]` ở vòng này:
tôi không mở được Dotson, *The Old Tibetan Annals* (2009) để đọc trực tiếp
mục năm 649–650, nên **không** đề xuất sửa. Ghi lại để vòng sau mở Dotson ra
đọc, chứ đừng sửa theo Wikipedia.

---

## Ca 9 — `ch05-ce07-review.md:1368` · CH05-CE07-12 Pakal · "cá nhân châu Mỹ tiền Columbus mà ngày nay biết rõ nhất"

**Câu trong repo** (trường `Vì sao chọn`):
> hồ sơ văn bản và kiến trúc Palenque chi tiết hơn bất cứ nơi nào khác ở vùng
> Maya, khiến ông là **cá nhân châu Mỹ tiền Columbus mà ngày nay biết rõ nhất**.

**Tra ngoài:**
- en.wikipedia "Kʼinich Janaabʼ Pakal" **không** đưa ra mệnh đề ấy; chỗ gần
  nhất là *"He is **perhaps best known in popular culture** for his depiction
  on the carved lid of his sarcophagus"* — một mệnh đề về văn hoá đại chúng,
  đã rào bằng "perhaps", và về **một cổ vật**, không về một con người.
- Mệnh đề nền cũng chỉ đúng ở dạng đã rào: Đền Bi ký mang **văn bản Maya liên
  tục dài thứ hai** (617 ký hiệu), dài nhất là Cầu thang Chữ tượng hình ở
  **Copán** (~2.200 ký hiệu). Về hồ sơ triều đại, cách nói quy chuẩn là
  "một trong những nguồn ký tự dồi dào nhất của thế giới Maya", không phải
  "hơn bất cứ nơi nào khác".

**Kết luận: NÊN sửa.** Phát hiện cũ đúng về mệnh đề dẫn xuất, và vòng này thấy
thêm rằng **mệnh đề nền cũng là một cấp nhất không đỡ được** — báo cáo cũ đã
cho nó qua ("đo được và nhiều khả năng đúng"), tôi không cho qua.

**Câu thay thế đề xuất cho cả trường `Vì sao chọn`, nguyên văn:**
> Ứng viên bị loại là Yuknoom Chʼeen II của Calakmul, vua của thế lực thật sự mạnh hơn đương thời. Pakal được chọn theo tính nguyên bản (c): hồ sơ văn bản và kiến trúc Palenque thuộc loại dày nhất vùng Maya, khiến đời ông được ghi chép kỹ hơn hẳn phần lớn người cai trị Maya cổ điển. Phải nói thẳng một khuyết tật của tiêu chí phạm vi (a): trước 1492 không tồn tại đường vật lý nào để ảnh hưởng ra khỏi bán cầu.

**Soi lại câu thay thế:**
- **Đếm chữ.** `why` gốc **90**, bản thay **87** — ngắn hơn, dưới trần 104 ✔.
  Không phải cắt gì ở đâu khác.
- **Bản thay còn cấp nhất nào không?** Còn một, cố ý: "**thuộc loại** dày nhất"
  — dạng "among the …", vốn đúng với Palenque kể cả khi Copán dài hơn. Vế dẫn
  xuất đổi từ phạm vi **hai lục địa** ("cá nhân châu Mỹ tiền Columbus") xuống
  phạm vi **so được** ("phần lớn người cai trị Maya cổ điển"), và đổi từ một
  mệnh đề về *trạng thái tri thức hiện nay* (không đo được) sang một mệnh đề về
  *khối tư liệu* (đo được).
- **Tôi không dùng câu thay thế của báo cáo cũ** ("được ghi chép **dày nhất**"):
  nó giữ nguyên hình thức cấp nhất mà chính báo cáo ấy đang chẩn, và báo cáo ấy
  tự thú `[KHÔNG KIỂM ĐƯỢC]` cho nó ngay dòng sau. Đây là ca thứ ba trong vòng
  này mà đề xuất cũ mang đúng cái lỗi nó vừa chẩn.
- **Trường `ideas` không cần đụng:** "khối văn bản tượng hình **thuộc loại dài
  nhất** châu Mỹ tiền Columbus" đã ở dạng "among the"; với vị trí thứ hai sau
  Copán, câu ấy **đúng** ✔.

---

## Ca 10 — `ch05-ce07-review.md:1390` · năm in của Tiesler & Cucina

**Dòng trong repo:** Tiesler và Cucina (chủ biên), *Janaab' Pakal of Palenque*
(University of Arizona Press, **2006**).

**Tra ngoài** (OpenLibrary API, hai bản ghi khớp):
- *Janaab' Pakal of Palenque*, University of Arizona Press —
  `first_publish_year: 2005`, `publish_year: [2017, 2005, 2006]`,
  ISBN 0816525102 / 0816537313 / 0816545898 (bản cứng, bản mềm, bản điện tử).
- *Janaab' Pakal de Palenque*, Universidad Autónoma de Yucatán / UNAM —
  `first_publish_year: 2004`, ISBN 9703214894.

Tra web: các bản ghi thư mục phổ thông và trang nhà xuất bản đều dẫn **2006**
cho bản University of Arizona Press.

**Kết luận: KHÔNG CẦN SỬA.** Báo cáo cũ mô tả đúng hiện trạng và đã tự kết luận
không sửa; vòng này xác nhận lại bằng một nguồn thư mục có cấu trúc. 2006 là
năm thường được dẫn và nằm trong vùng hợp lý; **2005 và 2004 là hai ấn bản
khác**, không phải hai giá trị tranh nhau cho cùng một ấn bản.

`[KHÔNG KIỂM ĐƯỢC]`: tôi không mở được trang bản quyền để phân biệt năm
copyright với năm phát hành. Ghi lại đúng như báo cáo cũ dặn, để vòng sau khỏi
"đính chính" 2006 thành 2005.
