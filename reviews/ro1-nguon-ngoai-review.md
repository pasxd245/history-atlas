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

---

## Ca 11 — `ch05-ce08-review-2.md:161` · CH05-CE08-01 Abu Muslim · "cuối năm ấy chiếm Merv"

**Câu trong repo** (`ideas`, 108/130 chữ):
> Năm 747 ông giương cờ đen công khai, và **cuối năm ấy** chiếm Merv, đánh bật
> tổng đốc Umayyad Nasr ibn Sayyar.

**Tra ngoài:**
- Giương cờ đen: **9 tháng 6 năm 747** (25 Ramadan 129 AH).
- Chiếm Merv: **14 tháng 2 năm 748** (Jumādā II 130 AH) — "In February 748
  (Jumada II 130), Abu Muslim established control over Merv and appointed
  Qahtaba ibn Shabib al-Taʾi to lead the army westward"; "on 14 February 748 he
  established control of Merv, expelling Nasr ibn Sayyar".

**Kết luận: BẮT BUỘC sửa** — nặng hơn mức `CÂN NHẮC` mà báo cáo cũ xếp. Đây
không phải "chọn im lặng một trong hai dòng niên đại": **cả hai dòng niên đại
mà báo cáo cũ nêu đều rơi vào năm 748**, không dòng nào đặt việc chiếm Merv vào
"cuối năm 747". Khoảng cách giữa cờ đen và Merv là **tám tháng**, bắc qua giao
thừa dương lịch. Câu hiện tại sai năm.

**Câu thay thế đề xuất, nguyên văn:**
> Năm 747 ông giương cờ đen công khai, và đầu năm 748 chiếm Merv, đánh bật tổng đốc Umayyad Nasr ibn Sayyar.

**Soi lại câu thay thế:**
- **Đếm chữ.** "cuối năm ấy" (3 chữ) → "đầu năm 748" (3 chữ): **net 0**, `ideas`
  giữ nguyên **108/130** ✔. Không phải cắt gì ở đâu.
- **"đầu năm 748" có chọn phe không?** Không — 14/02/748 nằm trong "đầu năm
  748", và cả dòng niên đại 12-747/01-748 mà báo cáo cũ nêu cũng không bị loại
  trừ hoàn toàn ở rìa. Nhưng quan trọng hơn: nó loại được cái **sai** (1747
  cuối năm).
- **Tôi không dùng câu thay thế của báo cáo cũ** ("trong vòng vài tháng"): nó
  đúng nhưng mơ hồ hơn mức cần, và tám tháng đọc thành "vài tháng" thì hơi
  rộng. Dùng một năm xác định là chặt hơn mà không tốn chữ nào.
- Vế còn lại của câu — "đánh bật tổng đốc Umayyad Nasr ibn Sayyar" — đã kiểm,
  đúng ("expelling Nasr ibn Sayyar") ✔.
- Mệnh đề kế tiếp "**Trong ba năm**, một cuộc nổi dậy ở rìa đông lật được triều
  đình" vẫn đúng sau khi sửa: 747 → trận Zab 750 ✔.

---

## Ca 12 — `ch05-ce08-review-2.md:238` · CH05-CE08-02 Al-Mansur · "giữ vai trung tâm suốt năm thế kỷ"

**Câu trong repo** (`ideas`, 95/130 chữ — dư 35 chữ):
> Baghdad lớn lên từ đó và giữ vai trung tâm của thế giới Hồi giáo **suốt năm
> thế kỷ**.

**Tra ngoài:** 762 (dựng thành) → 1258 (Mông Cổ phá thành) đúng là ~5 thế kỷ nếu
đo bằng **danh nghĩa caliph**. Nhưng quyền chính trị thật mất sớm hơn ba thế
kỷ: **nhà Buyid vào Baghdad năm 945**, caliph từ đó còn chức mà không còn
quyền; Seljuk tiếp quản 1055.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng và tự xếp "không sai, là cách đọc rộng
tay" — tôi đồng ý là **không sai**, nhưng vì mục đang dư 35 chữ, chỗ này là ca
rẻ nhất trong cả rổ: nói rõ ra không tốn gì mà gỡ được một mệnh đề dễ bị đọc
quá tay.

**Câu thay thế đề xuất, nguyên văn (câu cuối `ideas`):**
> Baghdad lớn lên từ đó và giữ vai trung tâm của thế giới Hồi giáo tới khi Mông Cổ phá thành năm 1258, dù quyền chính trị thật của caliph đã mất từ năm 945, khi nhà Buyid vào Baghdad.

**Soi lại câu thay thế:**
- **Đếm chữ.** `ideas` **95 → 116**, dưới trần 130, còn dư 14 ✔. Không cắt gì.
- **Bản thay có bỏ được "năm thế kỷ" không?** Có, và cố ý: thay một con số tổng
  bằng **hai mốc nêu tên**, nên người đọc tự thấy khoảng và tự thấy chỗ gãy.
  Tôi **không** viết "ba thế kỷ danh nghĩa" — đó sẽ lại là một con số tổng mới
  phải kiểm.
- **Hai mốc đều kiểm được:** 1258 (Mông Cổ) và 945 (Buyid) đều là mốc quy chuẩn
  ✔. Mục không có nguồn nào mâu thuẫn — trường `Nguồn` là Kennedy 1981, chuyên
  khảo chính trị Abbasid sớm, không bàn tới 945 nên không bị dẫn ngược.

---

## Ca 13 — `ch05-ce08-review-2.md:355` · CH05-CE08-05 Sibawayh · phép so sánh với ngữ pháp Hy Lạp–Latin

**Câu trong repo** (`ideas`, 127/130 chữ):
> **khác các sách ngữ pháp Hy Lạp và Latin còn lại**, al-Kitāb không bị công
> trình nào trong truyền thống của nó thay thế…

**Tra ngoài:**
- Vế được khẳng định về al-Kitāb thì **có đỡ**: sách "to this day remains the
  authoritative work on Classical Arabic grammar", "an original work of great
  genius that broke new ground, with no precedents for it in Syriac, Greek, or
  Latin".
- Vế **so sánh** thì không nguồn nào nói. Và nó đi ngược hiểu biết chuẩn về
  phía Latin: *Ars minor* / *Ars maior* của Donatus và *Institutiones
  grammaticae* của Priscianus là sách giáo khoa chuẩn của châu Âu Latin suốt
  gần một nghìn năm — tức **cũng** không bị thay thế trong truyền thống của
  chúng cho tới các ngữ pháp nhân văn chủ nghĩa.
- Carter, nguồn thứ nhất của chính mục, lập luận rằng ngữ pháp Ả Rập phát sinh
  **độc lập** với Hy Lạp (từ phương pháp luật học Islam) — tức ông chủ trương
  **không** so hai truyền thống theo kiểu này.

**Kết luận: NÊN sửa** — bỏ hẳn vế so sánh.

**Đáng ghi về quy trình, và đây là lý do mục này xứng đáng nằm trong rổ:** câu
đang sai **chính là câu thay thế của vòng 1**. Vòng 1 bắt đúng một cấp nhất sai
("bộ mô tả ngôn ngữ còn nguyên vẹn cổ nhất ngoài truyền thống Pāṇini"), nêu
đích danh Donatus, Priscianus, Dionysius Thrax để bác — rồi **dùng chính ba tác
phẩm ấy làm vế đối lập** trong câu thay thế, theo chiều ngược với dữ kiện nó
vừa trình bày. Mục đã chép nguyên câu ấy vào file. Đây là ca rõ nhất trong cả
rổ cho việc "câu thay thế phải được soi như soi bản gốc".

**Câu thay thế đề xuất, nguyên văn (câu cuối `ideas`):**
> Nó vẫn là mốc quy chiếu của ngữ pháp Ả Rập sau mười hai thế kỷ: al-Kitāb không bị công trình nào trong truyền thống của nó thay thế, mà thành văn bản mọi nhà ngữ pháp Ả Rập về sau phải chú giải hoặc phản bác.

**Soi lại câu thay thế:**
- **Đếm chữ.** Thao tác là **xoá** cụm "khác các sách ngữ pháp Hy Lạp và Latin
  còn lại," (9 chữ): `ideas` **127 → 116**... đếm lại cho chắc: trường mới ra
  **116 chữ** (xoá 9 chữ cộng việc bỏ một dấu phẩy không tính chữ, chênh so với
  phép trừ tay là do cách tách token của `s.split()`). Dưới trần 130, dư 14 ✔.
  Mục này trước khi sửa chỉ dư 3 chữ, nên việc sửa đi theo chiều **giảm** là
  một cái lợi phụ.
- **Bản thay có mệnh đề mới nào phải kiểm không?** Không một mệnh đề nào. Tôi
  chỉ **xoá**, không thêm. Đây là lựa chọn có chủ ý: mọi cách "sửa" bằng cách
  thay một so sánh này bằng một so sánh khác đều lại phải đi kiểm từ đầu, và
  vòng 1 đã vấp đúng chỗ ấy.
- Vế giữ lại ("không bị công trình nào trong truyền thống của nó thay thế") có
  nguồn ✔, và không còn phải gánh một mệnh đề về truyền thống khác.

---

## Ca 14 — `ch05-ce08-review-2.md:413` · CH05-CE08-06 Charlemagne · Einhard đứng cùng dòng Nguồn với McKitterick

**Dòng trong repo:**
> **Nguồn:** Rosamond McKitterick, Charlemagne: The Formation of a European
> Identity (Cambridge University Press, 2008); Einhard, Vita Karoli Magni,
> k. 830.

**Tra ngoài:** mô tả của nhà xuất bản cho McKitterick 2008 — sách đưa ra
*"a completely fresh and **critical examination of the contemporary sources**"*,
và chương 1 mang tên *"**Representations** of Charlemagne"*, bàn chính các
nguồn tự sự. *Vita Karoli Magni* thì là tiểu sử ca tụng do một người trong
triều viết, dựng theo khuôn Suetonius.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng, và đây đúng loại lỗi mà quy tắc 7 bắt
phải kiểm — **thể loại**, không chỉ chủ đề. Hai mục trong cùng một dòng `Nguồn`
nằm ở hai hạng khác nhau, và hạng thứ hai là **đối tượng** của hạng thứ nhất.
Dòng `Nguồn` hiện tại không nói ra điều đó, nên người đọc không thấy rằng nguồn
2 đang được nguồn 1 đọc lại.

**Dòng thay thế đề xuất, nguyên văn:**
> **Nguồn:** Rosamond McKitterick, Charlemagne: The Formation of a European Identity (Cambridge University Press, 2008) — công trình đọc lại có phê phán chính khối nguồn đương thời; Einhard, Vita Karoli Magni, k. 830 — tiểu sử ca tụng do người trong triều viết, dùng làm nguồn sơ cấp chứ không làm nguồn phán đoán.

**Soi lại dòng thay thế:**
- Trường `Nguồn` không nằm trong `WORD_TARGET`, không chạm trần nào ✔. Mẫu
  "— lưu ý/—  …" này đã được dùng ở `CH05-CE07-04`, `-12` và `CH05-CE07-11`,
  nên không phá quy ước nào ✔.
- **Chỗ tôi cố ý viết nhẹ hơn báo cáo cũ:** báo cáo cũ viết *"trong đó Einhard
  là đối tượng phê bình"*. Tôi **không** viết thế. `[KHÔNG KIỂM ĐƯỢC]`: tôi
  xác minh được McKitterick 2008 là "critical examination of the contemporary
  sources" nói chung, **không** xác minh được bà dành phần phê bình cho riêng
  Einhard, cũng không đọc được chương "Representations of Charlemagne". Viết
  "đọc lại có phê phán chính khối nguồn đương thời" là đúng mức tôi kiểm được.
- **Phần thân mục không cần đụng:** phát hiện BẮT BUỘC của vòng trước về "phần
  lớn tác phẩm Latin cổ điển còn tới nay" **đã được áp** — câu hiện tại đọc
  "còn qua phong trào chép sách ông khởi động", không còn gán các bản chép cho
  đời ông ✔.

---

## Ca 15 — `ch05-ce08-review-2.md:431` · CH05-CE08-07 Bêđa · "Thói quen ghi 'năm 2026' **bắt đầu** ở một tu viện Northumbria"

**Hai câu liền nhau trong repo** (`ideas`, 102/130 chữ — dư 28):
> Dionysius Exiguus nghĩ ra niên lịch Anno Domini từ thế kỷ 6, nhưng chính Bêđa
> … biến nó thành mặc định. Thói quen ghi "năm 2026" **bắt đầu** ở một tu viện
> Northumbria.

**Tra ngoài:**
- AD do **Dionysius Exiguus** đặt ra **năm 525** ở Rome, trong bảng Phục sinh.
- *"The system was **not widely used until the 9th century**."*
- *"Bede used AD years in his *Historia ecclesiastica gentis Anglorum* (731),
  **popularizing** the era."*
- *"On the continent of Europe, Anno Domini was introduced as the era of choice
  of the **Carolingian Renaissance by Alcuin**"*; Charlemagne và người kế vị
  phổ biến nó khắp đế quốc.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng, và vòng này thấy nó đúng ở **hai**
tầng chứ không một: chữ "bắt đầu" sai cả ở đầu **phát minh** (Rome, 525) lẫn ở
đầu **phổ dụng** (triều đình Carolingian, thế kỷ 9). Cái thật sự bắt đầu ở
Wearmouth–Jarrow là việc **dùng AD xuyên suốt một bộ sử** — tức một bước lan
truyền, không phải điểm khởi.

**Câu thay thế đề xuất, nguyên văn (câu cuối `ideas`):**
> Thói quen ghi "năm 2026" lan ra từ một tu viện Northumbria.

**Soi lại câu thay thế:**
- **Đếm chữ.** "bắt đầu ở" (3 chữ) → "lan ra từ" (3 chữ): **net 0**, `ideas`
  giữ nguyên **102/130** ✔.
- **"lan ra từ" có còn quá mạnh không?** Tôi kiểm riêng điểm này, vì lối lan
  thật sự đi qua triều đình Carolingian chứ không đi thẳng từ Jarrow ra châu
  Âu. "Lan ra từ" chịu được cách đọc ấy (Bêđa là điểm xuất phát của đợt lan,
  Alcuin và triều đình là chặng tiếp), trong khi "bắt đầu" thì không. Nếu Chủ
  dự án muốn chặt hơn nữa, bản an toàn tuyệt đối là *"Thói quen ghi 'năm 2026'
  đi ra thế giới từ một tu viện Northumbria"* — nhưng tôi **không** khuyến nghị
  nó, vì nó dài hơn 1 chữ mà không chặt hơn bao nhiêu.
- Câu ngay trên giữ nguyên, và sau khi sửa thì **hai câu nói cùng một điều**
  thay vì câu sau đè lên câu trước ✔.

---

## Ca 16 — `ch05-ce08-review-2.md:434` · CH05-CE08-07 Bêđa · Bêđa và Alcuin không cùng thời

**Dòng trong repo:**
> **Ảnh hưởng tới:** … Alcuin xứ York và trường học York · kế thừa · **trực tiếp**

và trong `Vì sao chọn`: *"Ứng viên bị loại **cùng vùng** là Alcuin xứ York."*

**Tra Wikidata trực tiếp** (`Q154332`, Alcuin):

| P569 | rank | tham chiếu |
|---|---|---|
| +0724 | normal | 3 |
| +0735 | normal | 4 |
| +0740 | **preferred** | 2 |

(P570 = 19/05/0804, preferred, 3 tham chiếu.) Lưu ý: giá trị **preferred** (740)
lại **không** phải giá trị nhiều tham chiếu nhất (735 có 4) — thêm một ca cho
thấy rank của Wikidata không nói gì về độ tin cậy.

**Tra ngoài repo:** en.wikipedia "Alcuin" — *"Alcuin of York (**c. 735** –
19 May 804) … He was born around 735 and became **the student of Archbishop
Ecgbert at York**."* Bêđa mất **735**.

**Kết luận: NÊN sửa mức bằng chứng.** Phát hiện cũ đúng. Ở cả ba giá trị
Wikidata lẫn ở niên đại quy chuẩn (k. 735), hai người **không có tiếp xúc nào
nói được bằng nguồn**: ở phương án phổ biến nhất Alcuin sinh đúng năm Bêđa
mất, ở phương án preferred thì sinh sau năm năm. `CONTRIBUTING.md` quy tắc 9
nói thẳng: *"đời hai người phải chồng lấn, **và** phải có tiếp xúc nói được
bằng nguồn. Không chồng đời thì viết `qua trường phái`."*

Đường truyền thật thì có và kiểm được: Alcuin học với **Ecgbert** ở York, và
Ecgbert là học trò của Bêđa — tức đúng hình dạng `qua trường phái`.

**Dòng thay thế đề xuất, nguyên văn:**
> - Alcuin xứ York và trường học York · kế thừa · qua trường phái

**Soi lại dòng thay thế:**
- `qua trường phái` ∈ `EVIDENCE_LEVELS` ✔. Dòng **thay** dòng cũ chứ không
  thêm, nên vẫn trong trần 3 mục của `Ảnh hưởng tới` ✔. Dòng quan hệ không nằm
  trong `WORD_TARGET` ✔.
- **Sửa này có tái lập lỗi nào không?** Tôi kiểm riêng: đích là **chuỗi tự do**
  ("Alcuin xứ York và trường học York"), không phải ID, nên không có mục đích
  nào để "mở ra đọc tên" theo quy tắc 8; và việc hạ mức không tạo ra mệnh đề
  mới nào cần nguồn ✔.

**Phần KHÔNG cần sửa trong cùng ca:** chữ "ứng viên bị loại **cùng vùng**" —
mục cố ý viết "cùng vùng" chứ không "cùng thời", nên nó **không** vi phạm quy
tắc 5 bằng cách khẳng định một điều sai. Nó chỉ lệch với chữ của template §5
("cùng lĩnh vực, cùng thời"). Đó là câu hỏi về template, thuộc về Chủ dự án,
không phải một lỗi sự thật — tôi để nguyên.

---

## Ca 17 — `ch05-ce08-review-2.md:479` · CH05-CE08-09 Đỗ Phủ · "biến cố lớn nhất thế kỷ 8 ở Đông Á"

**Câu trong repo** (`ideas`, 108/130 chữ — dư 22):
> loạn An Lộc Sơn từ năm 755 — **biến cố lớn nhất thế kỷ 8 ở Đông Á** — đến với
> hậu thế một phần qua mắt một viên quan nhỏ…

**Khối ghi chú biên tập của chính file** viết cùng mệnh đề ấy **có rào**:
*"**có lẽ** là biến cố đơn lẻ có hệ quả lớn nhất thế kỷ 8 ở lục địa Á–Âu"*.

**Kết luận: NÊN sửa.** Đây là ca hiếm mà phép kiểm mạnh nhất nằm **trong chính
repo**: hai chỗ nói cùng một điều, một chỗ rào, một chỗ không. Mệnh đề bảo vệ
được (loạn An Lộc Sơn làm sụp quân điền và phủ binh, đổi cơ cấu thuế khoá, và
sử học Trung Quốc coi là mốc chia đôi nhà Đường), nhưng nó vẫn là một phán
đoán về tầm vóc, không phải một dữ kiện — và bản thân mục đã biết thế ở chỗ
khác.

**Câu thay thế đề xuất, nguyên văn:**
> Về nội dung, loạn An Lộc Sơn từ năm 755 — có lẽ là biến cố lớn nhất thế kỷ 8 ở Đông Á — đến với hậu thế một phần qua mắt một viên quan nhỏ bị nó đẩy đi lưu lạc.

**Soi lại câu thay thế:**
- **Đếm chữ.** `ideas` **108 → 111**, dưới trần 130, còn dư 19 ✔.
- **Tôi cố ý KHÔNG đồng bộ phạm vi.** Khối ghi chú ghi "lục địa Á–Âu", thân mục
  ghi "Đông Á". Giữ "Đông Á" ở thân mục là **đúng hơn**: nó là phạm vi hẹp hơn,
  dễ bảo vệ hơn, và nằm trong phạm vi nguồn của mục. Nếu đồng bộ theo chiều
  ngược — nới thân mục ra thành "Á–Âu" — thì sẽ là nhân một superlative lên
  thay vì rào nó. Chênh phạm vi còn lại giữa hai chỗ là chuyện Chủ dự án quyết,
  không phải chuyện tôi sửa.

---

## Ca 18 — `ch05-ce08-review-2.md:504` · CH05-CE08-10 Trisong Detsen · `Q366661` có bốn `P570`

**Dòng trong repo:**
> `năm: trị vì 755–797 CN | … | độ tin cậy niên đại: Trung bình | wikidata: Q366661 | …`

**Tra Wikidata trực tiếp** (`Q366661`, `200`):

| thuộc tính | giá trị | rank | tham chiếu |
|---|---|---|---|
| P569 | +0742 | normal | 1 |
| P569 | +0742 (bản Julian) | normal | 1 |
| P570 | +0798 | normal | 1 |
| P570 | **+0797** | **preferred** | **0** |
| P570 | +0800 | normal | 1 |
| P570 | +0797 (bản Julian) | normal | 1 |

Xác nhận đúng như báo cáo cũ mô tả: **bốn** phát biểu `P570`, và giá trị
**preferred lại là giá trị duy nhất không có tham chiếu nào**. Theo nguyên tắc
của vòng này, một claim không tham chiếu chưa phải bằng chứng — nên rank
preferred ở đây **không** là lý do để chọn 797.

**Tra ngoài repo:** en.wikipedia "Trisong Detsen" — *"was the 38th King (Tsenpo)
of Tibet **from 755 to 797**"*. Tức khung `trị vì 755–797` của mục **khớp**
nguồn ngoài, độc lập với mớ `P570` lộn xộn.

**Kết luận: KHÔNG CẦN SỬA** cho con số. Khung trị vì mục ghi đứng được, và nó
đứng được **không phải nhờ** giá trị preferred không tham chiếu mà nhờ một
nguồn ngoài nói cùng con số.

**Nhưng phần quy trình của phát hiện cũ thì đúng, và là việc của Chủ dự án:**
vì trường `năm:` dùng dạng `trị vì`, `NON_BIO_YEARS_RE` làm lint **bỏ qua hoàn
toàn** phép đối chiếu Wikidata — tức mục khai `độ tin cậy niên đại: Trung bình`
mà không phép kiểm tự động nào chạm vào nó. Quy ước `CONTRIBUTING.md` cho phép
dạng `trị vì` với "vua không có năm sinh"; ở đây Wikidata **có** năm sinh
(742, hai phát biểu). Đây là quyết định quy ước cho **mọi mục vua**, không
phải một lỗi của riêng mục này — tôi không đề xuất sửa một mục lẻ.

**Ghi chú đối chiếu, vì hai mục Tây Tạng đang không cùng cách:**
`CH05-CE07-11` (Tùng Tán Cán Bố) dùng dạng `k. 617–650` nên **có** bị lint đối
chiếu, còn `CH05-CE08-10` dùng `trị vì 755–797` nên **không**. Hai mục cùng
vùng, cùng loại nhân vật, hai chế độ kiểm khác nhau. Xem thêm Ca 8.

---

## Ca 19 — `ch05-ce06-notes-review.md:202` · khối ghi chú Kaleb · nhan đề chuyên khảo Robin khoanh triều Joseph, không khoanh chiến dịch Kaleb

**Câu trong repo** (`content/ch05.md:1087`, khối Ghi chú biên tập):
> Chiến dịch của Kaleb thì không có mốc như vậy: Robin đặt nó sau Lễ Ngũ Tuần
> 525 **và tự đặt tên chuyên khảo của mình là** "de 522 à 525, ou une des années
> suivantes"

**Nhan đề đầy đủ, như chính trường `Nguồn` của mục ghi** (`ch05.md:157`):
> Christian Julien Robin, "**Joseph, dernier roi de Ḥimyar** (de 522 à 525, ou
> une des années suivantes)", *Jerusalem Studies in Arabic and Islam* 34 (2008),
> tr. 1–124.

**Tra ngoài:** bản ghi thư mục xác nhận nhan đề, tạp chí, số, năm và khoảng
trang (tr. 1–124) đúng từng phần. Và nhan đề nói rõ chủ đề: **Joseph — tức
Yūsuf, vua Ḥimyar cuối cùng** — nên ngoặc đơn niên đại khoanh **triều đại của
Yūsuf**, không khoanh chiến dịch Aksum của Kaleb.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng. Suy luận của khối vẫn đi được (chiến
dịch kết thúc triều ấy, nên hai khung chồng nhau trên thực tế), nhưng câu như
đang viết đọc ra thành "Robin đặt tên sách theo niên đại chiến dịch Kaleb" —
sai về chính nguồn mà khối đang trưng ra làm bằng.

**Câu thay thế đề xuất, nguyên văn:**
> Chiến dịch của Kaleb thì không có mốc như vậy: Robin đặt nó sau Lễ Ngũ Tuần 525, và chính nhan đề chuyên khảo của ông về vị vua Ḥimyar bị Kaleb lật đã phải mở ngoặc "de 522 à 525, ou une des années suivantes"

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập **không** nằm trong `WORD_TARGET` của `atlaslib/lint.py`
  (lint chỉ kiểm khối này có nhắc ứng viên Việt Nam hay không), nên không có
  trần chữ nào áp vào ✔.
- **Bản thay có đưa vào mệnh đề mới nào không?** Một: "vị vua Ḥimyar bị Kaleb
  lật". Nó được chính mục đỡ ở hai chỗ (`ch05.md:1087` đã nêu Yūsuf ʾAsʾar
  Yathʾar là đối thủ; nhan đề Robin gọi Joseph là "dernier roi de Ḥimyar") ✔.
  Tôi **không** viết "Joseph = Yūsuf" thành một mệnh đề riêng trong câu, vì đó
  là một phép đồng nhất tên gọi mà khối chưa giải thích ở đâu — thêm vào đây sẽ
  là một mệnh đề mới phải kiểm.
- **Tôi dùng "bị Kaleb lật" chứ không "bị ông lật"** như đề xuất cũ: trong câu
  này chủ ngữ gần nhất là Robin, nên "ông" của đề xuất cũ trỏ nhập nhằng sang
  Robin. Đây là một lỗi nhỏ nhưng có thật trong câu thay thế của vòng trước.

---

## Ca 20 — `ch05-ce06-notes-review.md:204` · "hagiography soạn khoảng ba mươi lăm năm sau"

**Câu trong repo** (`content/ch05.md:1087`):
> Chuyện Kaleb thoái vị đi tu đến từ *Martyrium Arethae* (Hy Lạp, **k. 560**),
> tức hagiography soạn **khoảng ba mươi lăm năm** sau

**Kết luận: NÊN sửa.** Phát hiện cũ đúng, và lý do nó đúng nằm **ngay trong
cùng đoạn văn**: ba câu phía trên, khối vừa lập luận rằng chiến dịch Kaleb
**không chốt được năm** (Robin: 525 "hoặc một trong những năm tiếp theo";
Hatke: mùa xuân 529), và kết luận *"Mục vì vậy viết 'thập niên 520', không viết
'năm 525'"*. Rồi câu cuối lại trừ một hiệu số chính xác — 560 − 525 = 35 — tức
lặng lẽ chốt đúng cái mốc vừa từ chối chốt. Theo chuỗi Hatke thì khoảng cách là
~31 năm; mà bản thân mốc soạn *Martyrium* cũng chỉ ghi "**k.** 560", nên con số
35 được trừ từ hai đầu đều không chắc.

**Câu thay thế đề xuất, nguyên văn:**
> Chuyện Kaleb thoái vị đi tu đến từ *Martyrium Arethae* (Hy Lạp, k. 560), tức hagiography soạn khoảng ba bốn mươi năm sau

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **"ba bốn mươi năm" có đủ bao cả hai chuỗi không?** Có: 560 − 525 = 35 và
  560 − 529 = 31, cả hai nằm trong "ba bốn mươi năm" ✔. Tôi kiểm riêng điểm
  này vì một bản sửa bao không đủ sẽ chỉ là đổi một con số chốt này lấy một con
  số chốt khác.
- **Chỗ tôi không đụng:** mốc "k. 560" của *Martyrium Arethae* giữ nguyên.
  `[KHÔNG KIỂM ĐƯỢC]`: tôi không xác minh được niên đại soạn *Martyrium
  Arethae* ở vòng này; nó đã mang chữ "k." nên không tự nhận quá chắc, và việc
  sửa nó là một ca riêng cần mở văn bản học về *Martyrium*.

---

## Ca 21 — `ch05-ce06-notes-review.md:222` · Vickery quy mệnh đề cho Claude Jacques

**Phát hiện cũ:** trong Vickery 1994, mệnh đề "'Funan' và 'Chenla' là thuật ngữ
Trung Hoa mơ hồ" được quy cho **Claude Jacques**, không phát biểu ở ngôi thứ
nhất.

**Tra ngoài — tôi mở chính PDF Vickery 1994 và đọc đoạn ấy.** Nguyên văn:
> "**Claude Jacques emphasized** the very vague character of the Chinese terms
> 'Funan' and 'Chenla', and the circumstance that many inscriptions make no
> reference to supralocal authority, which Jacques at least on occasion has
> considered to mean that those locations were independent of any king
> (**Jacques, 1986b: 90**)."

Vickery có dẫn nguồn cấp hai rõ ràng, có số trang, và câu kế của ông là một câu
hỏi ("If that were always true, should they all be called states…"), tức ông
**tiếp nhận và xây tiếp**, không phát biểu.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng. Đây đúng hình dạng mà quy tắc 7 nhắm
tới: nguồn tồn tại, đúng chủ đề, nhưng **lớp quy thuộc** bị bỏ — khối đang gán
cho Vickery một mệnh đề mà chính Vickery gán cho người khác. Đáng để sửa, vì
khối ấy tồn tại chính là để dạy cách đọc nguồn cho đúng.

**Câu thay thế đề xuất, nguyên văn:**
> Vickery 1994 tháo rời mệnh đề ấy từ chính nguồn sơ cấp, và — nối tiếp Claude Jacques — chỉ ra rằng "Chân Lạp" với "Phù Nam" phần lớn là phạm trù của thư tịch Trung Hoa

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **"nối tiếp Claude Jacques" có đúng mức không?** Có. Tôi cân nhắc "theo Claude
  Jacques" nhưng bỏ: Vickery không chỉ chép lại, ông dựng tiếp một lập luận
  riêng trên đó, nên "nối tiếp" đúng hơn "theo" ✔. Tôi **không** viết "Jacques
  1986b: 90" vào thân khối — thêm một trích dẫn cấp ba vào một khối ghi chú sẽ
  tạo một dòng mới phải bảo trì mà không thêm gì cho lập luận.
- **Hai mệnh đề khác của cùng khối tôi kiểm lại và thấy ĐÚNG, không cần sửa:**
  (a) cảnh báo quy tắc 7 về "Phù Nam là đế quốc hàng hải bị Chân Lạp đánh bại"
  được chính Vickery 1994 chặn nguyên văn — *"Funan was in decline, and no
  longer an attractive object for conquest"* ✔; (b) chiều quan hệ anh em trong
  K.1150 — *"Īśānavarman was also father of Bhavavarman II, called younger
  brother of Śivadatta in K1150"* ✔, khối không đảo chiều.

---

## Ca 22 — `ch05-ce06-notes-review.md:272` · `csla.history.ox.ac.uk` E06616 bị xếp "chết hoặc chặn"

**Tra lại hôm nay, hai lần gọi độc lập:**
- `GET https://csla.history.ox.ac.uk/record.php?recid=E06616` → **503**,
  1.113 byte, thân trang `<title>CSLA — Temporarily Unavailable</title>`.
- `GET https://csla.history.ox.ac.uk/` (gốc site) → **503**, **cũng 1.113 byte**
  — tức **cả site** đang trả một trang bảo trì duy nhất, không phải riêng bản
  ghi E06616 bị gỡ.

**Kết luận: NÊN sửa** cách phân loại trong khối ghi chú URL.

Hai dữ kiện mới của vòng này, so với báo cáo cũ: (a) 503 kèm đúng chữ
"Temporarily Unavailable" là **mã của một sự cố tạm thời** theo đúng nghĩa
HTTP — khác hẳn 404 (gỡ) hay 403 (chặn); (b) vì gốc site và bản ghi trả **cùng
một trang cùng kích thước**, đây là bảo trì toàn site, nên không có căn cứ nào
để kết luận riêng E06616 không tồn tại.

Xếp nó cùng rổ với `bitig.kz` (chết hẳn) là một **bẫy bảo trì ngược**: một
nguồn dùng được bị loại vĩnh viễn vì một lần máy chủ nghỉ, và không ai sẽ kiểm
lại vì danh sách đã nói là "đã kiểm".

**Sửa đề xuất:** tách danh sách URL xuyên chapter làm **hai** mục, và chuyển
CSLA sang mục thứ hai:
> - **Chết hẳn, không dẫn:** `bitig.kz`.
> - **Tạm không truy cập được, kiểm lại trước khi dùng:** `csla.history.ox.ac.uk` (đo 2026-11-03: 503, trang "Temporarily Unavailable" trên toàn site).

**Soi lại đề xuất:** (a) tôi ghi **ngày đo** vào chính dòng — đó là cách duy
nhất để một dòng về trạng thái máy chủ không rữa âm thầm, và là thiếu sót chung
của danh sách hiện tại ✔. (b) `[KHÔNG KIỂM ĐƯỢC]`: tôi **không** kiểm lại
`bitig.kz` ở vòng này, nên giữ nguyên phân loại cũ của nó chứ không xác nhận ✔.
(c) Mục ghi chú URL không nằm trong `WORD_TARGET` ✔.

---

## Ca 23 — `ch05-ce06-notes-review.md:349` · "kế hoạch dịch trọn Plato lẫn Aristotle không hoàn thành" bị cho là không có trên trang SEP

**Câu trong repo** (`content/ch05.md:1100`, khối "Bốn điều không được viết về
Boethius", ý (2)):
> ông dịch *Organon*, bản *Phân tích hậu* đã mất, và kế hoạch dịch trọn Plato
> lẫn Aristotle không hoàn thành.

**Phát hiện cũ:** mệnh đề này *"không tìm thấy trên trang SEP mà mục dẫn"*; báo
cáo cũ đã thử các chuỗi "translate all", "all the works of Plato", "every work"
và đều ra 0 kết quả, rồi kết luận *"nguồn đang được dẫn không đỡ cho nó"*.

**Tra ngoài — tôi tải nguyên trang SEP "boethius" (`200`, 90.315 byte), lọc thẻ
rồi đọc.** Mệnh đề **có trên trang**, mục 2 *The Logical Project*:
> "Boethius's work as a translator and commentator of Aristotelian logic is
> usually regarded by historians to be just the beginning of a wider project —
> announced in the second commentary on *On Interpretation* (c. 516), and
> **cut short by his execution** — **to translate and comment on all the
> writings of Plato and Aristotle**."

Trang còn nói thêm Boethius mải chú giải logic đến mức *"it is hard not to see
it as having diverted him from his more grandiose and hardly practicable
scheme"* — tức đỡ cả vế "không hoàn thành".

**Kết luận: KHÔNG CẦN SỬA.** Phát hiện cũ **sai**, và sai vì một lý do đáng ghi
riêng: nó là một **lỗi chuỗi tìm kiếm**, không phải một lỗi đọc. Trang viết
"all **the writings of** Plato and Aristotle"; ba chuỗi mà báo cáo cũ thử đều
không khớp dạng ấy. Nếu áp phát hiện này, mục sẽ bị gỡ một câu **có nguồn**, và
dòng `Nguồn` sẽ bị thêm một nguồn thừa để đỡ cho thứ đã được đỡ.

**Bài học quy trình, vì nó lặp lại:** đây là ca thứ tư trong rổ này mà báo cáo
cũ kết luận ngược. Ba ca trước là đề xuất mang lỗi mới; ca này là `[KHÔNG KIỂM
ĐƯỢC]` **tuyên quá mạnh** — "không có trên trang" là một mệnh đề phủ định toàn
xưng, mà bằng chứng chỉ là ba lần `grep` trượt.

**Ghi nhận thêm:** trang SEP mở đầu bằng *"born: circa 475–7 C.E., died: 526?
C.E."* — đỡ đúng cho cả `năm: k. 477 – k. 526` của mục lẫn ý (1) của khối
("nguồn… đặt dấu hỏi sau năm mất 526") ✔. Và ý (1) ấy **đã được áp** bản sửa
của vòng trước ("không phải để lách lint — với lệch 2 năm thì cả mức Cao cũng
qua").

---

## Ca 24 — `ch05-ce06-notes-review.md:351` · "chính việc nó không viện giáo lý Kitô mới là điều làm nó nổi tiếng"

**Câu trong repo** (`content/ch05.md:1100`, ý (4)):
> Không khép tranh luận *Consolatio* có phải tác phẩm Kitô giáo hay không;
> **chính việc nó không viện giáo lý Kitô mới là điều làm nó nổi tiếng**.

**Tra ngoài — nguyên văn SEP "boethius"** (trang tôi đã tải, `200`):
> "…the **absence of any explicit reference to Christianity** in the
> *Consolation* **poses a special problem**, when it is recalled that it is the
> work of a man about to face death and so very literally composing his
> philosophical and literary testament."

**Kết luận: NÊN sửa.** Phát hiện cũ đúng. SEP xếp sự vắng mặt ấy là một **bài
toán** của giới nghiên cứu — và nêu rõ *vì sao* nó là bài toán (người viết đang
chờ án tử, nên đây là di chúc tư tưởng của ông). Mục biến nó thành **lý do nổi
tiếng**, một phán đoán về tiếp nhận mà không nguồn nào trong mục đỡ. Lỗi này
nằm ngay trong một khối có nhiệm vụ dạy cách không nói quá nguồn, nên đáng sửa
hơn nếu nó nằm chỗ khác.

**Câu thay thế đề xuất, nguyên văn:**
> Không khép tranh luận *Consolatio* có phải tác phẩm Kitô giáo hay không; chính sự vắng mặt ấy là điều làm nó thành một bài toán của giới nghiên cứu.

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **"bài toán của giới nghiên cứu" có phải lại là một mệnh đề về giới nghiên
  cứu không?** Có — và tôi kiểm riêng điểm này, vì Ca 4 của chính báo cáo này
  vừa chẩn một mệnh đề dạng ấy. Khác biệt: ở Ca 4 mục **xếp hạng** giới nghiên
  cứu ("rõ nhất trong giới hiện đại"), không nguồn nào xếp; ở đây SEP **tự**
  gọi nó là "a special problem", nên câu thay thế chỉ dịch lại chữ của nguồn,
  không thêm một phép đo nào ✔.
- **Chỗ tôi cố ý giữ:** nửa đầu câu ("Không khép tranh luận…") giữ nguyên — đó
  là chỉ dẫn biên tập đúng, và chính SEP cũng để ngỏ ("These questions will
  appear in sharper focus … when the argument of the *Consolation* has been
  examined") ✔.

---

## Ca 25 — `ch05-ce07-notes-review.md:180` · "dòng đầu của `content/ch90.md` nói rõ"

**Câu trong repo** (`content/ch05.md:1124`):
> ch90 là phụ lục **Việt Nam**, không phải Đông Nam Á — **dòng đầu của
> `content/ch90.md` nói rõ**.

**Đối chiếu `content/ch90.md`:**
- Dòng 1: `# Chapter 90 · Phụ lục · **Việt Nam** qua các thời kỳ` — đúng như
  khối viện.
- Dòng 3 (`Giới thiệu chapter`): *"ảnh hưởng được đo trong phạm vi **Việt Nam
  và Đông Nam Á**, không phải toàn nhân loại."*

**Kết luận: NÊN sửa — nhưng KHÔNG sửa theo cách báo cáo cũ đề nghị.**

Báo cáo cũ đề nghị *"nên sửa luôn câu gây nhập nhằng ở `content/ch90.md`"*. Tôi
**phản đối** đề nghị ấy, và đây là phần đóng góp riêng của vòng này. Lý do: câu
ở `ch90.md:3` **đang được hai khối khác trong `ch05.md` dùng làm bằng**, và sửa
nó sẽ làm cả hai chỗ ấy nói sai về một văn bản đã đổi:
- `ch05.md:1172` trích thẳng nó: *"dù hệ quy chiếu của nó được khai là **'Việt
  Nam và Đông Nam Á'**"* — một trích dẫn nguyên văn sẽ thành trích sai.
- `ch05.md:1223` dựng lập luận loại Cao Biền trên chính câu ấy: *"hệ quy chiếu
  của `content/ch90.md` là ảnh hưởng đo trong phạm vi Việt Nam chứ không phải
  nguồn gốc nhân vật"*.

Sửa một dòng để chữa một chỗ rồi làm hỏng hai chỗ khác là đúng hình dạng lỗi mà
vòng này được lập ra để chặn. **Chỗ rẻ và an toàn là sửa chính câu đang viện
sai**, trong `ch05.md:1124`.

**Câu thay thế đề xuất, nguyên văn:**
> ch90 là phụ lục **Việt Nam**, không phải Đông Nam Á — nhan đề của `content/ch90.md` nói rõ, và cả 40 mục hiện có đều là nhân vật Việt Nam, dù dòng `Giới thiệu chapter` của nó khai hệ quy chiếu rộng hơn là "Việt Nam và Đông Nam Á".

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không nằm trong `WORD_TARGET` ✔.
- **Bản thay có mệnh đề nào phải kiểm không?** Hai, cả hai kiểm được **trong
  repo**: "nhan đề" (dòng 1 của `ch90.md`) ✔ và "40 mục đều là nhân vật Việt
  Nam" — con số 40 lấy từ chính `ch05.md:1172`, vốn đã khẳng định nó. Nếu Chủ
  dự án muốn một câu không rữa theo số mục thì bỏ "40" và viết "mọi mục hiện
  có"; tôi giữ 40 vì nó đã có sẵn trong file và việc bỏ nó sẽ làm hai chỗ lệch
  nhau.
- **Bản thay nói ra chỗ nhập nhằng thay vì giấu nó**, nên vòng sau đọc
  `ch90.md:3` sẽ không tưởng là bắt được mâu thuẫn mới ✔.

---

## Ca 26 — `ch05-ce07-notes-review.md:243` · niên đại "k. 424–430" của bản dịch Đại Vân kinh

**Câu trong repo** (`content/ch05.md:1131`, ý (2)):
> Đại Vân kinh **không** phải nguỵ tạo của triều Võ Tắc Thiên — đó là kinh Ấn
> Độ có thật do Đàm Vô Sấm dịch **k. 424–430**

**Tra ngoài:**
- en.wikipedia "Mahāmegha Sūtra": *"The Mahāmegha Sūtra was translated into
  Chinese **in the fifth century** by **Dharmakṣema (385–433)** as *Great
  Vaipulya Great Cloud Sutra* (大方等大雲經, **T. 387**)."* — xác nhận dịch giả,
  xác nhận thế kỷ, **không** cho khoảng năm.
- Các nguồn khác tôi tra được chỉ khoanh bằng chính đời hoạt động của Đàm Vô
  Sấm (k. 421–433 ở Lương Châu), tức **rộng hơn nhiều** so với 424–430.

**Kết luận: NÊN sửa.** Hai lớp:
1. Mệnh đề **chính** của ý (2) — Đại Vân kinh là kinh Ấn Độ có thật, do Đàm Vô
   Sấm dịch, và thứ được soạn năm 690 là **bản sớ** — **đúng và nay có nguồn
   ngoài đỡ** ✔. Phần này giữ nguyên.
2. Riêng khoảng **"k. 424–430"** thì không nguồn nào tôi mở được đỡ. Nó hẹp hơn
   cả khoảng mà nguồn cho phép, tức là một con số **chặt hơn hiểu biết** — đúng
   hình dạng mà `CONTRIBUTING.md` quy tắc 3 cấm ("thà bỏ số… còn hơn ghi đoán").

**Câu thay thế đề xuất, nguyên văn (chỉ cụm niên đại):**
> đó là kinh Ấn Độ có thật do Đàm Vô Sấm (385–433) dịch sang Hán văn ở thế kỷ 5

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **"thế kỷ 5" có đủ cho mục đích của khối không?** Có — mục đích của ý (2) là
  chứng minh kinh **có trước** năm 690 hàng mấy thế kỷ, chứ không phải định
  niên đại bản dịch. Thế kỷ 5 làm trọn việc ấy, và làm bằng một mệnh đề có
  nguồn.
- **Tôi thêm "(385–433)"** vì đó là niên đại Đàm Vô Sấm trong chính nguồn ngoài
  tôi mở, và nó khoá luôn trần trên: không bản dịch nào của ông muộn hơn 433 ✔.
- **Chỗ tôi cố ý không làm:** không thay "k. 424–430" bằng "k. 421–433". Khoảng
  ấy là **đời hoạt động của người dịch**, không phải niên đại của bản dịch này;
  chuyển một khoảng đời thành một khoảng dịch là tạo ra đúng loại con số mà tôi
  vừa gỡ.
- `[KHÔNG KIỂM ĐƯỢC]`: tôi không mở được kinh lục Hán văn (`出三藏記集`,
  `開元釋教錄`) để truy niên đại chính xác của T. 387. Nếu Chủ dự án muốn giữ
  một khoảng năm, nó phải được gắn vào một kinh lục nêu đích danh.

---

## Ca 27 — `ch05-ce07-notes-review.md:270` · "Plofker là người phản đối" gán cho một người cái của năm người

**Câu trong repo** (`content/ch05.md:1136`):
> **Plofker là người phản đối** niên đại Bakhshali công bố năm 2017 — … Và bài
> phản hồi 2017 có năm đồng tác giả, nên gọi đúng là Plofker và cộng sự.

**Tra ngoài:** bài phản hồi là **Plofker, Keller, Hayashi, Montelle,
Wujastyk**, "The Bakhshālī Manuscript: A Response to the Bodleian Library's
Radiocarbon Dating", *History of Science in South Asia* **5.1 (2017),
tr. 134–150** — năm đồng tác giả, đúng tạp chí, đúng tập/số, đúng khoảng trang,
truy cập mở (bản HAL-SHS đặt tên tệp là "Plofker **et al.**").

**Kết luận: NÊN sửa** — nhưng phát hiện cũ đã **được áp một nửa**, và nửa ấy
làm khối tự mâu thuẫn trong cùng một đoạn.

Đây là điều vòng này thấy mà báo cáo cũ chưa thấy: câu đính chính *"Và bài phản
hồi 2017 có năm đồng tác giả, nên gọi đúng là Plofker và cộng sự"* **đã được
thêm vào cuối đoạn**, nhưng câu mở đầu vẫn nguyên "Plofker là người phản đối".
Kết quả là một đoạn vừa nói sai vừa tự đính chính, cách nhau bốn câu. Với một
khối tồn tại để vòng sau **khỏi phải mở lại từng mục**, hình dạng ấy tệ hơn lỗi
gốc: người đọc nhanh lấy câu đầu, người đọc kỹ lấy câu cuối.

**Sửa đề xuất:** đưa đính chính vào chính câu, rồi **bỏ** câu đính chính ở
cuối. Nguyên văn câu mở:
> Plofker và cộng sự (2017) là nhóm phản đối niên đại Bakhshali công bố năm 2017 — liên quan vì tháng 10/2024 Bodleian đã lùi niên đại bản thảo ấy về 799–1102, …

và xoá câu cuối *"Và bài phản hồi 2017 có năm đồng tác giả, nên gọi đúng là
Plofker và cộng sự."*

**Soi lại đề xuất:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **"nhóm phản đối" có đúng không?** Bài mang nhan đề "A **Response** to the
  Bodleian Library's Radiocarbon Dating" và phản bác cách công bố, nên "phản
  đối" đúng; tôi đổi "người" → "nhóm" cho khớp năm tác giả ✔.
- **Tôi không thêm bốn tên còn lại vào khối.** Khối này là ghi chú cảnh báo
  nguồn, không phải thư mục; "và cộng sự" đủ để tra lại, và thêm bốn tên sẽ tạo
  bốn chuỗi nữa phải bảo trì ✔.
- **Phần còn lại của đoạn tôi kiểm và thấy ĐÚNG:** `CH05-CE07-08` quả thật dẫn
  "Kim Plofker, *Mathematics in India* (Princeton University Press, 2009)"
  **không kèm cảnh báo nào** và không nhắc Bakhshali (`ch05.md:341`) ✔ — nên
  câu "cảnh báo này chưa vào mục" vẫn đúng và phải giữ.
- `[KHÔNG KIỂM ĐƯỢC]`: tôi **không** xác minh lại mốc "tháng 10/2024 Bodleian
  lùi niên đại về 799–1102" ở vòng này.

---

## Ca 28 — `ch05-ce07-notes-review.md:338` · "sứ bộ với Harun al-Rashid đều thuộc thế kỷ 8"

**Câu trong repo** (`content/ch05.md:1142`, khối lý giải vì sao Charlemagne ở
nhóm CE08):
> việc diệt vương quốc Lombard, thu phục Bavaria, các chiến dịch Avar, việc
> Alcuin tới triều đình và cả **sứ bộ với Harun al-Rashid đều thuộc thế kỷ 8**

**Tra ngoài:**
- *"Numerous embassies were exchanged between Charlemagne and the Abbasid
  caliph Harun al-Rashid **from 797**."* Sứ bộ đầu của Charlemagne (797) gồm
  Isaac người Do Thái, Lantfrid và Sigimund.
- Nhưng trao đổi **không dừng ở thế kỷ 8**: con voi **Abul-Abbas** tới Aachen
  năm **801** (có nguồn ghi **802**), kèm các tặng vật khác (hương liệu, vải,
  một chiếc đồng hồ, bàn cờ). Tổng cộng ba sứ bộ Charlemagne gửi đi và ít nhất
  hai sứ bộ Harun gửi lại.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng, và vòng này gỡ được dấu hỏi của nó:
mốc 802 mà báo cáo cũ thấy trong `reports/ch05-ce09-gate.md` **không** mâu
thuẫn với repo — nó là mốc thật, và chính nó chứng minh chữ "**đều**" là sai.
Chuỗi sứ bộ **khởi** ở thập niên 790 nhưng **vắt qua** mốc 800.

**Câu thay thế đề xuất, nguyên văn:**
> việc diệt vương quốc Lombard, thu phục Bavaria, các chiến dịch Avar, việc Alcuin tới triều đình và cả sứ bộ với Harun al-Rashid khởi từ thập niên 790 đều thuộc thế kỷ 8

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **Bản thay có làm yếu lập luận của khối không?** Không, và tôi kiểm riêng
  điểm này vì đó là rủi ro thật của mọi bản rào. Lập luận của khối là "33 trong
  47 năm dương lịch mà triều ông chạm tới thuộc thế kỷ 8"; việc sứ bộ **khởi**
  ở 797 vẫn nằm trọn trong vế ấy, và việc đuôi của nó rơi sang 801–802 còn
  **khớp** với câu kế của khối ("thế kỷ 9 chỉ chứa phần ông giữ tước hiệu đã
  có") — tiếp nhận một con voi là đúng dạng "giữ" chứ không phải "dựng".
- **"khởi từ thập niên 790" chịu được cả hai mốc** 797 (sứ bộ đầu) và 801/802
  (voi), nên không phải chọn phe giữa 801 và 802 ✔ — một chi tiết đáng giữ, vì
  chính hai mốc ấy còn đang vênh trong các nguồn.

---

## Ca 29 — `ch05-ce08-notes-review-1.md:74` · chuỗi truyền của khung 788–820

**Câu trong repo** (`content/ch05.md:1145`):
> C.P. Tiele (Cornelis Petrus Tiele, 1830–1902) lấy nó từ chuyên luận
> *Āryavidyā-sudhākara* của **Yajñeśvara Śāstrī**, vốn dẫn lại
> *Śaṅkara-mandāra-saurabha* của **Bhaṭṭa Nīlakaṇṭha* — rồi Max Müller,
> Macdonell, Deussen và Radhakrishnan chấp nhận theo lệ.

**Phát hiện cũ:** `[KHÔNG KIỂM ĐƯỢC]` — *"tài liệu tham khảo phổ thông tôi mở
được… **không** chứa hai nhan đề lẫn hai tên người ấy"*, và cảnh báo rằng nếu
vòng sau không xác minh được thì **phải bỏ chuỗi hoặc gắn nhãn chưa kiểm**.

**Tra ngoài — vòng này tìm được nguồn, và nó khớp từng mắt xích.** Natalia
Isayeva, *Shankara and Indian Philosophy* (1993), chương tiểu sử:
> "Tiele… suggested as a probable date of Sankara's life an interval
> **between 788 and 820**. He based his estimate on the evidence of a later
> Vedantin, **Yajnesvara Sastri**, who cites in his treatise
> ***Aryavidya-sudhakar*** … an earlier work by **Bhatta Nilakantha**, entitled
> ***Sankara-mandara-saurabha***."

Thêm một mắt xích nữa, cùng chiều: Nīlakaṇṭha đặt năm sinh Śaṅkara là **Kali
3889 = 788 CN**. Và danh sách người chấp nhận theo lệ cũng khớp: en.wikipedia
"Adi Shankara" chép *"following **K.P. Tiele**, and was customarily accepted by
scholars such as **Max Müller, Macdonnel**, Pathok, **Deussen and
Radhakrishna**"*.

**Kết luận: KHÔNG CẦN SỬA, và dấu `[KHÔNG KIỂM ĐƯỢC]` của vòng trước được GỠ.**
Chuỗi truyền trong khối đúng cả ba mắt xích, đúng cả bốn tên người chấp nhận
theo lệ. Vế "đóng góp của giới Đông phương học là **chọn và phổ biến** một niên
đại vốn có nguồn Ấn Độ, không phải chế ra nó" vì vậy đứng vững — đúng cái vế mà
báo cáo cũ cảnh báo có thể phải bỏ.

**Hai ghi chú thêm, đều nghiêng về phía repo:**
1. Repo viết "**C.P.** Tiele (Cornelis Petrus Tiele, 1830–1902)", trong khi cả
   Isayeva lẫn en.wikipedia viết "**K.P.** Tiele". Repo **đúng hơn**: tên thật
   là Cornelis Petrus. "K.P." gần như chắc chắn là vết chuyển tự qua tiếng Nga
   (Корнелис → K). Repo đã làm đúng việc ghi kèm tên đầy đủ, nên không cần sửa.
2. `k. 700 – k. 750` mà mục dùng khớp nguồn ngoài: *"c. 700 – c. 750 CE:
   Late 20th-century and early 21st-century scholarship tends to place
   Shankara's life…"* ✔

---

## Ca 30 — `ch05-ce08-notes-review-1.md:84` · khối bỏ mất cách đọc "Vikramāditya" thứ hai

**Câu trong repo** (`content/ch05.md:1145`):
> Bản ghi Śṛṅgeri thật sự chỉ nói ông sinh vào năm thứ mười bốn đời một vua tên
> Vikramāditya mà **không cho biết là Vikramāditya nào**. **Một cách đọc** quy
> về Vikramāditya II của triều Cālukya (733–746) — nhưng…

**Tra ngoài** — en.wikipedia "Adi Shankara", nguyên văn:
> "The records of the Sringeri Matha state that Shankara was born in the 14th
> year of the reign of 'Vikramaditya', but **it is unclear to which king this
> name refers**. Though **some researchers identify the name with Chandragupta
> II (4th century CE)**, **modern scholarship accepts** the Vikramaditya as
> being from the Chalukya dynasty of Badami, most likely **Vikramaditya II
> (733–746 CE)**."

**Kết luận: NÊN sửa.** Phát hiện cũ đúng. Khối viết "Một cách đọc" ở số ít rồi
chỉ trình bày một cách đọc, nên người đọc không thấy rằng chính sự **phân tán**
của tên ấy — từ thế kỷ 4 tới thế kỷ 8 — mới là lý do bản ghi "không chốt được
gì". Thêm cách đọc thứ hai làm luận điểm của khối **mạnh hơn**, không yếu đi.

**Câu thay thế đề xuất, nguyên văn:**
> Bản ghi Śṛṅgeri thật sự chỉ nói ông sinh vào năm thứ mười bốn đời một vua tên Vikramāditya mà không cho biết là Vikramāditya nào. Một số nhà nghiên cứu đọc tên ấy là Chandragupta II (thế kỷ 4 CN), tức một Śaṅkara sớm hơn bốn thế kỷ; cách đọc được học giới hiện nay chấp nhận thì quy về Vikramāditya II của triều Cālukya (733–746) — nhưng năm thứ mười bốn của triều ấy rơi vào khoảng 746, tức một Śaṅkara muộn hơn khung mục này dùng, chứ không sớm hơn

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không nằm trong `WORD_TARGET` ✔.
- **Tôi giữ đúng trọng số của nguồn:** "một số nhà nghiên cứu" cho Chandragupta
  II (nguồn: "some researchers") và "được học giới hiện nay chấp nhận" cho
  Vikramāditya II (nguồn: "modern scholarship accepts"). Đây là điểm tôi soi
  kỹ, vì nêu hai cách đọc **ngang hàng** sẽ là một lỗi mới: nguồn nói rõ chúng
  không ngang hàng.
- **Bản thay có đụng tới lập luận kế tiếp của khối không?** Không — câu về
  "triều ấy chỉ dài mười ba tới mười bốn năm, nên 'năm thứ mười bốn' rơi đúng
  vào cuối triều, một trùng hợp đáng ngờ" giữ nguyên và vẫn nối liền ✔.
- **Và nó củng cố kết luận của chính khối** ("Bản ghi ấy vì vậy không chốt được
  gì: nó chỉ loại thế kỷ 5 TCN"): với hai cách đọc cách nhau bốn thế kỷ, câu
  kết luận ấy nay có hai chân thay vì một ✔.

---

## Ca 31 — `ch05-ce08-notes-review-1.md:182` · chuỗi sử học của ca Jabir

**Câu trong repo** (`content/ch05.md:1151`):
> Jabir ibn Hayyan: 721–815, con số **721** truy ngược về giả thuyết **Holmyard
> 1927** mà **Delva 2017** đã tháo rời

**Phát hiện cũ:** `[KHÔNG KIỂM ĐƯỢC]` ở vòng ấy — *"Mối nối 'Trove → Holmyard
1927' thì không nguồn nào trong repo chứng, và tôi không mở được nó."*

**Tra ngoài — vòng này mở được, và cả ba mắt xích đều khớp.** en.wikipedia
"Jabir ibn Hayyan":
1. **Giả thuyết là của Holmyard 1927**, nguyên văn mục thư mục: *"Holmyard,
   Eric J. (1927). 'An Essay on Jābir ibn Ḥayyān'… (**seminal paper first
   presenting the hypothesis** that Jabir was the son of a proto-Shi'ite
   pharmacist called Ḥayyān al-ʿAṭṭār)"*.
2. **Con số 721 đến từ chính giả thuyết ấy**: *"Because Ḥayyān al-ʿAṭṭār was
   supposedly executed not long after **721**, the hypothesis even made it
   possible to **estimate Jabir's date of birth at c. 721**."*
3. **Delva 2017 tháo rời nó**: *"Delva, Thijs (2017). 'The Abbasid Activist
   Ḥayyān al-ʿAṭṭār as the Father of Jābir b. Ḥayyān: An Influential Hypothesis
   Revisited'. *Journal of Abbasid Studies* 4(1): 35–61. (**rejects Holmyard
   1927's hypothesis** … on the basis of newly available evidence)"*, và lý do:
   Ḥayyān al-ʿAṭṭār *"probably lived at least until c. 744"* và thuộc bộ lạc
   Nakhaʿ chứ không phải Azd.

**Kết luận: KHÔNG CẦN SỬA, và dấu `[KHÔNG KIỂM ĐƯỢC]` của vòng trước được GỠ.**
Câu trong repo đúng từng mắt xích, và đúng cả ở chỗ tinh tế nhất: 721 **không**
là một niên đại được chứng, nó là một **hệ quả số học** của một giả thuyết về
cha ông — đúng như khối lập luận.

**Phần kiểm lại và thấy ĐÚNG trong cùng khối:** mệnh đề *"ngay thời Ibn
al-Nadīm đã có người khẳng định ông chưa từng tồn tại"* khớp nguyên văn nguồn
ngoài (*"already in Ibn al-Nadīm's time, there were some people who explicitly
asserted that Jabir had never existed"*) ✔; mốc *Fihrist* **987** ✔.

---

## Ca 32 — `ch05-ce08-notes-review-1.md:281` · bẫy `429 / Varnish` chưa có trong danh sách URL xuyên chapter

**Câu trong repo** (`content/ch05.md:1154`):
> `doi.org/10.1163/22142371-12340030` (Delva 2017) trả **HTTP 202 với 0 byte**,
> và `doi.org/10.1017/S0041977X20000014` (Capezzone 2020) trả **HTTP 429** với
> trang chặn bot của Varnish — **cùng loại bẫy mà ghi chú CE06 đã ghi**.

**Tôi gọi lại cả hai URL hôm nay:**

| URL | mã | kích thước | đích cuối |
|---|---|---|---|
| `doi.org/10.1163/22142371-12340030` | **202** | **0 byte** | brill.com/…/article-p35_2.xml |
| `doi.org/10.1017/S0041977X20000014` | **429** | 1.478 byte | cambridge.org/core/product/… |

Thân trang thứ hai: `<title>429 Too many automated requests from this
network.</title>`, và chuỗi `Varnish` có trong trang. **Cả hai mô tả trong repo
đều tái lập được nguyên vẹn** — điều đáng ghi riêng, vì trạng thái máy chủ là
thứ hay rữa nhất trong mọi ghi chú.

**Đối chiếu hai danh sách bẫy đang tích luỹ:**
- `ch05.md:1093`: `202`, `405`, `406`, `200`-kèm-trang-chặn, `200`/0-byte không
  ổn định, JSTOR landing page 3 KB.
- `ch05.md:1107`: `ctext.org` 200/2.781 byte, JSTOR 200/3.038 byte "Client
  Challenge", Brill **202 / 0 byte**, Wikisource `404` với `<title>` giống
  trang thật, Britannica và Iranica `403` qua Cloudflare.

**Không danh sách nào chứa `429`.**

**Kết luận: NÊN sửa.** Phát hiện cũ đúng: nửa đầu câu (202/0 byte của Brill) là
ca **đã ghi**, nửa sau (429/Varnish của Cambridge) là ca **mới**, nhưng câu
viết gộp "cùng loại bẫy mà ghi chú CE06 đã ghi" khiến nó không được nhặt vào
danh sách. Hệ quả cụ thể: một vòng sau gặp `429` sẽ không tìm thấy nó trong
danh sách và sẽ mất công chẩn lại từ đầu.

**Sửa đề xuất — thêm vào danh sách ở `ch05.md:1107`, nguyên văn dòng thêm:**
> Cambridge Core trả **429** với trang chặn bot của Varnish (`<title>429 Too many automated requests from this network.</title>`, 1.478 byte) — mã này khác mọi ca trên ở chỗ nó **phụ thuộc tần suất**, nên một lần gọi lại sau đó có thể qua; đừng xếp nó vào "chết hoặc chặn".

**Soi lại đề xuất:**
- Danh sách URL nằm trong khối Ghi chú biên tập, không có trần chữ ✔.
- **Tôi thêm một mệnh đề mà báo cáo cũ không có:** `429` **phụ thuộc tần suất**.
  Đó là điều phân biệt nó với `403`/`404`/`202` trong cùng danh sách, và nếu
  không nói ra thì dòng mới sẽ sinh đúng cái bẫy bảo trì ngược đã chẩn ở Ca 22
  (một nguồn dùng được bị loại vĩnh viễn vì một lần gặp 429).
- Dòng ghi kèm `<title>` và kích thước, tức **kiểm lại được** ✔.

---

## Ca 33 — `ch05-ce08-notes-review-1.md:474` · hai mệnh đề "lớn nhất" trong cùng chapter không cùng phạm vi

**Hai chỗ trong repo:**
- Khối 7 (Ghi chú biên tập): *"**có lẽ** là biến cố đơn lẻ có hệ quả lớn nhất
  thế kỷ 8 ở **lục địa Á–Âu**"*.
- Thân mục `CH05-CE08-09` (`ideas`): *"biến cố lớn nhất thế kỷ 8 ở **Đông Á**"*
  — không rào.

**Kết luận: NÊN sửa — và cách sửa đã nêu ở Ca 17, không mở thêm phiếu.**

Báo cáo cũ xếp ca này là "không phải lỗi" vì hai câu không mâu thuẫn (một bao
trùm cái kia) và câu rộng có hedge. Tôi **không đồng ý** ở một điểm, và điểm ấy
là lý do ca này đáng kết luận chứ không đáng xếp lại vào "chỉ lưu ý": hai câu
lệch nhau **ở chỗ rào**, không ở chỗ phạm vi. Câu có nguồn đỡ (thân mục, có
trường `Nguồn`) là câu **không rào**; câu không có nguồn nào đỡ (khối ghi chú)
lại là câu **có rào**. Đó là hình dạng ngược, và nó nói rằng chữ "có lẽ" đang
được dùng theo cảm giác từng chỗ chứ không theo tình trạng bằng chứng.

**Việc phải làm vì vậy chỉ có một:** thêm "có lẽ" vào thân mục
`CH05-CE08-09` — câu thay thế đầy đủ, phép đếm chữ (108 → 111/130) và phần soi
lại đã viết ở **Ca 17**.

**Chỗ tôi KHÔNG đề xuất, và nói rõ vì sao:** không nới phạm vi thân mục từ
"Đông Á" lên "Á–Âu" để khớp khối ghi chú. Làm thế là nhân một cấp nhất lên thay
vì rào nó, và sẽ kéo mệnh đề ra ngoài phạm vi hai nguồn của mục (Owen 2016 và
Hung 1952, đều là công trình về Đỗ Phủ chứ không phải về lịch sử Á–Âu).

---

## Ca 34 — `ch05-ce08-notes-review-1.md:523` · hai con số/mốc của khối văn khố núi Mugh

**Câu trong repo** (`content/ch05.md:1166`):
> Văn khố núi Mugh — **khoảng 80 văn kiện** từ kho riêng của Ḏēwaštīč, phần lớn
> bằng tiếng Sogdian kèm một số bản Ả Rập, Turkic và Hán, **UNESCO ghi danh
> *Memory of the World* năm 2025** — … gồm sổ sách buôn bán, thư từ, khế ước,
> trao đổi ngoại giao và báo cáo do thám.

**Phát hiện cũ:** `[KHÔNG KIỂM ĐƯỢC]` cho mốc UNESCO 2025 — báo cáo cũ đã thử
ba đường (MoW Register, country overview Tajikistan, tìm kiếm) và không đường
nào xác nhận, vì các trang ấy dựng động nên `curl` không đọc được kết quả.

**Tra ngoài — vòng này xác nhận được, và xác nhận tới từng chi tiết:**
- UNESCO có trang riêng cho bộ sưu tập: *Collection of documents from Mount
  Mugh*, mục Memory of the World; Wikidata có thực thể `Q136768442` cho nó.
- **Ghi danh năm 2025**: được đưa vào Memory of the World International
  Register tại **kỳ họp thứ 221 của Hội đồng Chấp hành UNESCO, ngày
  17-4-2025**, do IICAS và ICDH đề cử.
- **"khoảng 80 văn kiện"**: *"The collection comprises **approximately 80
  manuscripts** discovered in the 1930s near present day Panjakent in
  Tajikistan."* ✔
- **Danh mục thể loại khớp gần như từng chữ**: *"everyday **business records,
  letters, contracts, diplomatic exchange and spy reports**"* ✔
- **Các ngôn ngữ khác**: *"The ethnic diversity of Sogdiana is reflected in
  **Arabic, Chinese and Old Turkic** texts found in the collection"* ✔
- **Ḏēwaštīč và năm 722**: *"The documents show the life of **Dewashtich**, the
  ruler of Penjikent principality, until his **defeat by Arab forces in
  722**"* ✔ — khớp cả `ch05.md:419` ("Divashtich thua trận năm 722").

**Kết luận: KHÔNG CẦN SỬA, và dấu `[KHÔNG KIỂM ĐƯỢC]` của vòng trước được GỠ.**

Phần số học mà báo cáo cũ chẩn — tổng ~80 và phần Sogdian không thể bằng nhau —
**đã được áp**: câu hiện tại đọc "khoảng 80 văn kiện…, **phần lớn** bằng tiếng
Sogdian **kèm một số** bản Ả Rập, Turkic và Hán", đúng cấu trúc mà nguồn UNESCO
mô tả ✔.

**Một chỗ đáng chỉnh nhỏ, không bắt buộc:** nguồn UNESCO viết "approximately 80
**manuscripts**" (bản thảo), repo viết "văn kiện". Với một văn khố hành chính
thì hai chữ gần như trùng nhau và "văn kiện" hợp ngữ cảnh tiếng Việt hơn, nên
tôi **không** đề xuất đổi. Ghi lại để vòng sau khỏi tưởng đã bắt được lệch.

---

## Ca 35 — `ch05-ce09-review-d.md:92` · "(850)" cho *Gaṇitasārasaṅgraha*

**Câu trong repo** (`content/ch05.md:1211`, khối Ghi chú biên tập):
> **Mahāvīrācārya**, tác giả *Gaṇitasārasaṅgraha* **(850)**, văn bản Ấn Độ sớm
> nhất dành riêng hoàn toàn cho toán học, bị cắt vì là người thứ mười ba

**Tra ngoài:** mọi nguồn tôi mở được đều rào — *"written by the Indian
mathematician Mahavira **around 850 CE**"*; *"Mahavira wrote
Gaṇitasārasaṅgraha … **during the reign of Amoghavarsha (c. 814–878)** of the
Rashtrakuta dynasty"*. Không nguồn nào cho một năm trần.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng, và lý do nó đúng có hai chân, không
một: (a) nguồn ngoài chỉ cho "around 850"; (b) hồ sơ cổng của chính dự án
(`reports/ch05-ce09-gate.md:88`) xếp Mahāvīrācārya `độ tin cậy niên đại: Thấp`
với lý do "Không có niên đại độc lập; khung duy nhất là triều Amoghavarsha I" —
tức dự án **tự biết** con số này lỏng, rồi viết nó trần ở chỗ khác. Chính
chapter này viết "k. 850", "k. 870" cho các tác phẩm khác, nên đây còn là lệch
nội bộ.

**Gộp với Ca 36 vì cùng một câu — câu thay thế đề xuất, nguyên văn:**
> **Mahāvīrācārya**, tác giả *Gaṇitasārasaṅgraha* (k. 850, soạn dưới triều Amoghavarsha I), văn bản Ấn Độ sớm nhất dành riêng hoàn toàn cho toán học, bị cắt vì là người thứ mười ba; ghi luôn chỗ ông sai để không ai phải phát hiện lại: ông khẳng định một số chia cho **không** thì không đổi (24 ÷ 0 = 24). So với `CH05-CE07-08` thì đó là bước lùi ở đúng phép tính ấy — Brahmagupta để `n ÷ 0` nguyên dạng phân số có mẫu bằng không, không gán giá trị — nhưng Brahmagupta cũng sai, chỉ sai chỗ khác: ông khẳng định 0 ÷ 0 = 0.

---

## Ca 36 — `ch05-ce09-review-d.md:96` · "một bước lùi so với `CH05-CE07-08`"

**Tra ngoài:**
- Mahāvīrācārya: *"at around 850 CE, Mahavira argued that **any number divided
  by zero leaves that number unchanged**, so then, for example, **24 ÷ 0 =
  24**."*
- Brahmagupta: *"**Brahmagupta asserted that zero divided by zero is zero**…
  allows division by zero resulting in a **fraction with a 0 in the
  denominator**, and defines 0/0 = 0."*

**Kết luận: NÊN sửa.** Phát hiện cũ đúng. Mệnh đề "một bước lùi" đúng ở **đúng
một phép tính** — `n ÷ 0` với `n ≠ 0`, nơi Brahmagupta để nguyên dạng phân số
còn Mahāvīrācārya gán một giá trị sai. Nhưng câu như đang viết để người đọc
hiểu Brahmagupta đã làm đúng cả bài, trong khi ông sai ở `0 ÷ 0`. Với một khối
có nhiệm vụ "**ghi luôn chỗ ông sai để không ai phải phát hiện lại**", bỏ sót
chỗ sai của người kia là một mâu thuẫn tự thân.

**Câu thay thế: xem Ca 35** (cùng một câu, một bản sửa).

**Soi lại câu thay thế của Ca 35 + 36:**
- Khối Ghi chú biên tập không nằm trong `WORD_TARGET` ✔ — không trần chữ.
- **Mọi mệnh đề mới đều có nguồn ngoài, không một mệnh đề nào từ trí nhớ:**
  "k. 850" (around 850 CE) ✔; "dưới triều Amoghavarsha I" ✔; "24 ÷ 0 = 24" là
  **chính ví dụ của nguồn**, nên nó không phải tôi tự dựng ✔; "phân số có mẫu
  bằng không" và "0 ÷ 0 = 0" ✔.
- **Tôi giữ "bước lùi" chứ không bỏ**, vì nó đúng ở phép tính được nêu; cái
  được thêm là **phạm vi** của nó. Bỏ hẳn sẽ mất một nhận định đúng.
- **Chỗ tôi cố ý không đụng:** "văn bản Ấn Độ sớm nhất dành riêng hoàn toàn cho
  toán học" — một cấp nhất. `[KHÔNG KIỂM ĐƯỢC]` ở vòng này: tôi không đối chiếu
  được nó với *Bakhshālī* hay *Pāṭīgaṇita* của Śrīdhara. Ghi lại để vòng sau
  biết đây là mệnh đề **chưa** được kiểm, chứ không phải đã qua.

---

## Ca 37 — `ch05-ce09-review-d.md:173` · chỉ một trong ba mục tự khai "có thể bị bác"

**Ba mục, đọc thẳng từ `content/ch05.md`:**

| mục | câu về lựa chọn lĩnh vực thứ hai | tự khai "có thể bị bác"? | `why` |
|---|---|---|---|
| `CH05-CE09-08` | "Lĩnh vực thứ hai ghi Kinh tế: việc ông làm là đàm phán lại một nghĩa vụ cống nạp – thương mại." | **không** | 104/104 |
| `CH05-CE09-09` | "…không ghi Luật, vì *al-Tārīkh al-kabīr* là phê phán tiểu sử người truyền… **đó là một lựa chọn có thể bị bác**." | **có** | 81 |
| `CH05-CE09-12` | "Lĩnh vực thứ hai ghi Quân sự vì Voss và Kremer rút vai chỉ huy quân sự của ông từ chính bi ký…" | **không** | 94 |

**Kết luận: NÊN sửa — và sửa ở khối ghi chú, KHÔNG ở thân ba mục.**

Phát hiện cũ đúng về hiện trạng. Nhưng bản sửa hiển nhiên (thêm câu tự khai vào
`-08` và `-12`) **không chạy được**: `CH05-CE09-08` đang ở **đúng 104/104 chữ**,
tức không còn một chữ nào. Thêm một mệnh đề vào đó buộc phải cắt chỗ khác trong
một trường vốn đang làm việc nặng — nó là chỗ duy nhất giải thích vì sao cả
Châu Phi hạ Sahara thế kỷ 9 chỉ có một người.

Và có một lý do nội dung mạnh hơn lý do kỹ thuật: ba quyết định **không cùng độ
chắc**. `-12` dẫn hai tác giả rút vai trò ấy **từ chính bi ký** (Voss và
Kremer), tức có bằng chứng trực tiếp; `-09` tự nhận lỏng vì nó là một phép phân
loại thao tác học thuật. Ép cả ba mang cùng một câu tự khai sẽ làm **sai lệch**
chứ không làm nhất quán.

**Câu thêm đề xuất cho khối ghi chú tương ứng, nguyên văn:**
> Ba quyết định lĩnh vực thứ hai của nhóm không cùng độ chắc, và chỉ một mục nói ra: `CH05-CE09-12` rút vai Quân sự từ chính bi ký, `CH05-CE09-08` rút vai Kinh tế từ nội dung việc làm, còn `CH05-CE09-09` tự ghi "có thể bị bác" vì đó là một phép phân loại thao tác học thuật chứ không phải một dữ kiện. Ai đọc ba mục liền nhau mà không đọc khối này sẽ thấy ba mức tự tin như nhau.

**Soi lại câu thêm:**
- Khối Ghi chú biên tập không có trần chữ ✔; ba trường `why` **không bị đụng**,
  nên không ca nào vượt trần ✔ — đây chính là lý do tôi chọn chỗ sửa này.
- **Câu thêm có tự mâu thuẫn không?** Tôi kiểm riêng: nó không khẳng định mục
  nào đúng mục nào sai, chỉ mô tả **loại bằng chứng** của từng quyết định, và cả
  ba mô tả ấy đều đọc thẳng được từ chính ba mục ✔.

---

## Ca 38 — `ch05-ce09-review-d.md:206` · con số "khoảng 950" cho ʻAhoʻeitu

**Phát hiện cũ:** `[KHÔNG KIỂM ĐƯỢC]` — *"tôi không tìm được nguồn nào trong
tầm tra của vòng này nói đúng 950"*; đề nghị viết "thế kỷ 10" thay vì "khoảng
950".

**Tra ngoài — vòng này tìm được, và 950 là một con số có xuất xứ:**
- en.wikipedia "Tuʻi Tonga Empire": *"Tongan expansionism and projected
  hegemony in Oceania which **began around 950 CE**, reaching its peak during
  the period 1200–1500."*
- en.wikipedia "Tuʻi Tonga": *"a line of Tongan kings, which **originated in
  the tenth century with the mythical ʻAhoʻeitu**"*.

**Kết luận: KHÔNG CẦN SỬA, và dấu `[KHÔNG KIỂM ĐƯỢC]` của vòng trước được GỠ.**
"Khoảng 950" là mốc quy ước cho khởi điểm bành trướng Tonga, và dòng Tuʻi Tonga
được quy khởi từ ʻAhoʻeitu — nên con số không phải vô căn cứ. Nó đã mang chữ
"khoảng", tức không tự nhận chắc hơn nguồn.

**Một chỗ phải nói cho chính xác, nhưng không đòi sửa:** 950 là mốc của **sự
bành trướng**, không phải một niên đại tiểu sử của ʻAhoʻeitu — người mà
`Q1245849` thậm chí **không có `P569` lẫn `P570` nào**. Kết luận của khối
("thuộc CE10, không thuộc nhóm này") đứng vững ở cả hai cách đọc, vì cả 950 lẫn
"early 10th century" đều rơi trong 901–1000.

---

## Ca 39 — `ch05-ce09-review-d.md:323` · "lint không nhắc được"

**Câu trong repo** (`content/ch05.md:1229`):
> Đây là một thao tác bảo trì mà lint chỉ nhắc được **một nửa**: vòng đối xứng
> (`atlaslib/lint.py:224-232`) in INFO khi đầu kia đã dùng ID, nhưng khi **cả
> hai** đầu còn là văn bản tự do thì không có dòng nào — **lint không biết** một
> chuỗi văn bản tự do nào đó vừa trở thành một mục có thật.

**Kiểm trong mã nguồn** (phần kiểm được của ca này; kết luận về khả thi là một
mệnh đề kỹ thuật, không phải một mệnh đề sử học):
- Mô tả hiện trạng **đúng**: `atlaslib/lint.py:150-151` chỉ kiểm đích khi
  `C.ID_RE.match(t)`; mọi đích tự do đi thẳng qua. Vòng đối xứng ở dòng 226–231
  cũng chỉ chạy khi `t in all_persons`.
- Nhưng phép kiểm ngược **làm được**: `atlaslib/parse.py:122` cho mỗi mục cả
  `name_vi` lẫn `name_orig`, và `all_persons` đã có sẵn trong `lint_chapter`.
  Đối chiếu tập đích tự do với chỉ mục hai trường tên ấy là một phép so chuỗi
  cơ học — không có gì trong lint chặn nó.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng ở cả hai vế: (a) câu đang đóng cửa một
việc **làm được**, và (b) quy trình thủ công mà khối kê — mỗi vòng `grep` tên
người mới trên toàn `content/` — **không co giãn**: nó quét theo chiều
người-mới → văn-bản-cũ, nên bỏ sót mọi đích tự do đã hở từ các vòng trước mà
không nhóm mới nào gợi ra.

**Câu thay thế đề xuất, nguyên văn (vế cuối của câu):**
> …nhưng khi **cả hai** đầu còn là văn bản tự do thì không có dòng nào — lint **hiện chưa** biết một chuỗi văn bản tự do nào đó vừa trở thành một mục có thật. Phép kiểm ngược thì làm được và rẻ hơn phép `grep` theo chiều người-mới: rút tập đích tự do rồi đối chiếu một lượt với chỉ mục `name_vi`/`name_orig` của mọi mục (`atlaslib/parse.py:122`), dưới dạng **cảnh báo** chứ không phải lỗi chặn — vì đích tự do hợp lệ như "Trường phái luật Hanbalī" phải được phép tồn tại.

**Soi lại câu thay thế:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **"cảnh báo chứ không phải lỗi chặn" là mệnh đề tôi thêm và nó bắt buộc phải
  có:** nếu không nói, một vòng sau sẽ cài phép kiểm ở mức ERROR và chặn build
  trên hàng trăm đích tự do hợp lệ. Ví dụ "Trường phái luật Hanbalī" lấy từ
  chính `content/ch05.md` ✔.
- **Tôi không viết con số "141 dòng"** như báo cáo cũ nêu: đó là một con số đếm
  trạng thái file, đúng loại số sẽ rữa ở vòng sau — và chính chapter này vừa
  đặt ra quy ước "con số trong ghi chú biên tập phải tự khai nó đo ở thời điểm
  nào, hoặc không nêu số" (`ch05.md:1271`, ý *Ba*). Viết nó vào sẽ là vi phạm
  quy ước ngay trong tệp đặt ra quy ước.

---

## Ca 40 — `ch05-ce10-notes-review.md:188` · `Q172383` còn một `P569` dạng `somevalue`

**Tra Wikidata trực tiếp** (`Q172383` = Sylvester II / Gerbert, `200`):

| thuộc tính | giá trị | rank | tham chiếu |
|---|---|---|---|
| P569 | **`somevalue`** (biết có, không biết năm nào) | **preferred** | 1 |
| P569 | +0938 | normal | 1 |
| P570 | +1003-05-12 (`precision 11`) | normal | 3 |

**Kết luận: NÊN sửa**, và phát hiện cũ đúng — **nhưng nó mô tả sai vị trí của
giá trị ấy**, và chỗ sai lại nghiêng về phía làm lập luận yếu đi.

Báo cáo cũ gọi đó là *"một phát biểu `P569` **thứ hai** ở dạng `somevalue`"*,
như thể nó là một giá trị phụ. Thực tế `somevalue` chính là giá trị **rank
preferred** — tức Wikidata, ở phát biểu nó tự đánh dấu là tốt nhất, nói thẳng
**"không biết năm sinh"**, còn con số 938 mới là giá trị hạng thường. Đó là
chứng cứ mạnh hơn hẳn cho việc mục chọn `k. 945` theo nguồn ngoài thay vì theo
Wikidata.

**Câu thêm đề xuất cho bẫy (5) của khối, nguyên văn:**
> Và chính Wikidata nói ra chỗ nó không biết: `P569` của `Q172383` có hai phát biểu, và phát biểu ở rank **preferred** là `somevalue` — "có năm sinh, không rõ năm nào" — còn con số 938 chỉ ở rank thường. Tức mốc 938 không phải một giá trị Wikidata đề cử; chọn `k. 945` theo nguồn ngoài vì vậy không đi ngược Wikidata, nó đi vào đúng chỗ Wikidata để trống.

**Soi lại câu thêm:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **Mọi con số trong câu đều lấy từ lần gọi API của chính vòng này**, không chép
  lại từ báo cáo cũ ✔ — và đó là lý do bắt được chỗ báo cáo cũ đặt sai vị trí
  `somevalue`.
- Câu **không** khẳng định `k. 945` là đúng; nó chỉ nói việc chọn ấy không mâu
  thuẫn Wikidata. Tôi kiểm riêng điểm này vì nói quá lên ở đây sẽ là đúng lỗi
  đang chẩn ✔.

---

## Ca 41 — `ch05-ce10-notes-review.md:350` · "mục CH05-CE08-11 trước đây ghi…" bị cho là không có trong git

**Câu trong repo** (`content/ch05.md:1252`):
> mục `CH05-CE08-11 · Ādi Shankara` **trước đây** dùng Vācaspati làm mốc chặn
> trên và ghi ông **"sớ cho ông ở nửa đầu thế kỷ 9"** — câu ấy **chỉ đúng nếu
> nhận cách đọc 841**…

**Phát hiện cũ:** `[KHÔNG KIỂM ĐƯỢC]` — *"câu cũ không còn trong file và cũng
không có trong `git show HEAD:content/ch05.md`"*; đề nghị **bỏ dấu ngoặc kép**
vì repo "không còn chứng cứ".

**Tra trong git — vòng này tìm được, và tìm thấy ngay.** `git log --all -S "nửa
đầu thế kỷ 9" -- content/ch05.md` trả về hai commit. Mở commit sớm hơn:
> `git show 3157f64:content/ch05.md` — dòng 597 (thân mục `CH05-CE08-11`):
> *"…ông trích Pháp Xứng, nên sau giữa thế kỷ 7; **Vācaspati Miśra sớ cho ông ở
> nửa đầu thế kỷ 9**."*
> và dòng 716 (khối ghi chú): *"…Śaṅkara trích nguyên văn Pháp Xứng, và
> **Vācaspati Miśra sớ cho ông ở nửa đầu thế kỷ 9** — nên mục ghi `k. 700 –
> k. 750 CN`…"*

Trích dẫn trong dấu ngoặc kép khớp **từng chữ**.

**Kết luận: KHÔNG CẦN SỬA, và dấu `[KHÔNG KIỂM ĐƯỢC]` của vòng trước được GỠ.**
Phát hiện cũ **sai**, và sai vì một lý do có thể nói thành quy trình: nó chỉ tra
`git show HEAD:…`, tức **một** bản chụp, trong khi câu được trích tường minh là
một câu **đã bị sửa** — chỗ duy nhất nó còn tồn tại là lịch sử. Một phép
`git log -S` là đủ.

Nếu áp phát hiện cũ (bỏ dấu ngoặc kép), repo sẽ **mất** một trích dẫn có thật và
tra lại được, để đổi lấy một lời diễn giải không tra lại được. Đây là ca thứ năm
trong rổ này mà đề xuất cũ làm hỏng một chỗ đang đúng.

**Gợi ý nhỏ, không bắt buộc:** nếu Chủ dự án muốn vòng sau khỏi phải đi tìm,
thêm `(xem `3157f64:content/ch05.md`)` vào sau trích dẫn. Lưu ý điều kiện kèm:
`reviews/README.md` ghi rõ lịch sử git **đã được viết lại ngày 2026-11-03** nên
mọi hash trước đó không còn giải ra được; hash tôi nêu là hash **sau** lần viết
lại ấy, và sẽ chết nếu lịch sử bị viết lại lần nữa. Vì vậy tôi **không** khuyến
nghị mạnh việc ghi hash vào văn bản — chuỗi `git log -S "nửa đầu thế kỷ 9"` thì
không rữa.

---

## Ca 42 — `ch05-ce10-notes-review.md:462` · ca ʻAhoʻeitu và `P31 = Q6949213`

**Tra Wikidata trực tiếp** (`Q1245849`, `200`):

| thuộc tính | giá trị | rank | tham chiếu |
|---|---|---|---|
| P31 | **`Q6949213`** (mythological king) | normal | **0** |
| P39 | `Q42298576` | normal | **0** |
| P569 / P570 | **không có phát biểu nào** | — | — |

Nhãn tiếng Anh: `'Aho'eitu`; mô tả: *"son of the god Tangaloa ʻEitumātupuʻa and
a mortal woman"*; **không có nhãn tiếng Việt**.

**Kết luận: NÊN sửa.** Phát hiện cũ đúng: khối CE10 rút gọn ca ʻAhoʻeitu xuống
còn tầng (3) và **bỏ mất** trở ngại thao tác mà khối CE09 đã ghi. Vòng này xác
nhận trở ngại ấy và tìm thêm **ba** dữ kiện khối chưa có, tất cả đều nặng hơn:
1. `P31 = Q6949213` **không có tham chiếu nào** — nên ngay cả phép phân loại
   "mythological king" cũng chưa phải bằng chứng theo nguyên tắc của dự án.
2. Thực thể **không có `P569` lẫn `P570`** — tức nếu ông vào atlas, trường
   `năm:` sẽ không có gì để đối chiếu, cộng dồn với cảnh báo `P31`.
3. **Không có nhãn tiếng Việt**, nên tên mục sẽ phải tự đặt.

**Câu thêm đề xuất cho khối CE10, nguyên văn:**
> Và trở ngại thao tác mà khối CE09 ghi vẫn còn nguyên, đừng để nó rơi ở đây: `Q1245849` khai `P31 = Q6949213` ("mythological king") chứ không phải `Q5` — không kèm tham chiếu nào — và thực thể ấy **không có `P569` lẫn `P570`**, cũng không có nhãn tiếng Việt. Tính truyền thuyết **không** phải lý do loại (atlas có nhãn `[Truyền thuyết]` và đã dùng), nhưng ba điều trên là việc phải làm kèm nếu ông vào atlas, và sẽ kích hoạt cảnh báo `P31` trong `lint_wikidata`.

**Soi lại câu thêm:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **Tôi nhắc lại mệnh đề "tính truyền thuyết không phải lý do loại"** dù nó dài
  thêm, vì bỏ nó đi là mở đúng cái cửa mà khối CE09 đã đóng — một vòng sau sẽ
  dùng `Q6949213` làm lý do loại ✔.
- Ba dữ kiện mới đều từ lần gọi API của chính vòng này ✔.

---

## Ca 43 — `ch05-ce10-notes-review.md:552` · al-Ashʿarī (874–936) so với `Q316349` khai 873–935

**Câu trong repo** (`content/ch05.md:1267`, khối "Những người bị cắt"):
> **al-Ashʿarī** (**874–936**) — mạnh ngang bất kỳ ai trong nhóm; bị cắt vì ô
> `Tôn giáo/Tâm linh` của nhóm đã có bốn mục…

**Tra Wikidata trực tiếp** (`Q316349`, `200`):

| thuộc tính | giá trị | rank | tham chiếu |
|---|---|---|---|
| P569 | +0873 | **preferred** | **7** |
| P569 | +0873 | normal | 1 |
| P570 | +0935 | normal | 1 |

**Tra ngoài repo:** AH thì **không ai cãi** — sinh **260 AH**, mất **324 AH**.
Cách ghi CE thì có hai: en.wikipedia dùng **874–936**; các tài liệu chuyên
ngành thường viết **260/873-4** và **324/935-6**.

**Kết luận: KHÔNG CẦN SỬA con số — nhưng phần CHẨN ĐOÁN của hồ sơ cổng thì SAI,
và đó mới là thứ cần sửa.**

Hồ sơ cổng gọi cặp lệch-một-năm-cả-hai-đầu này là *"dấu hiệu điển hình của quy
đổi AH→CE bằng công thức"*. Tôi kiểm lại phép quy đổi và kết luận **ngược**:
- **260 AH bắt đầu khoảng 28-10-873** và kết thúc khoảng 16-10-**874**;
  **324 AH bắt đầu khoảng 01-12-935**, kết thúc khoảng 19-11-**936**. Một năm
  AH **vắt qua hai năm CE**, nên ±1 ở cả hai đầu là **cấu trúc của lịch**, không
  phải vết của một công thức.
- Hơn nữa, công thức tuyến tính quen dùng (`CE ≈ AH + 622 − AH/33`) cho
  260 → **874,1** và 324 → **936,2** — tức công thức ra **đúng cặp số mà repo
  đang dùng**, còn 873/935 của Wikidata là **năm CE mà năm AH bắt đầu**. Chẩn
  đoán của hồ sơ cổng vì vậy chỉ nhầm phe, mà là nhầm đúng phe quan trọng.

**Vậy việc phải làm:** giữ **874–936** (cặp số của học giới, và của
en.wikipedia), và **sửa lời chẩn** ở hồ sơ cổng / khối ghi chú thành:

> `Q316349` khai 873–935, lệch một năm ở cả hai đầu so với cặp 874–936 mà khối này dùng. Đó **không** phải dấu hiệu quy đổi bằng công thức: ông sinh **260 AH** và mất **324 AH**, mà 260 AH chạy từ cuối 873 sang cuối 874 và 324 AH từ cuối 935 sang cuối 936 — hai cách ghi CE chỉ khác nhau ở chỗ lấy năm AH **bắt đầu** hay năm nó **phần lớn rơi vào**. Nếu CE11 nhặt ông lên thì viết cặp AH kèm theo là cách duy nhất không phải chọn phe.

**Soi lại đề xuất:**
- Khối Ghi chú biên tập không có trần chữ ✔.
- **Tôi tự kiểm phép tính lịch của chính mình** thay vì chép lại: năm Hồi lịch
  ≈ 354,367 ngày; 259 năm kể từ 16-07-622 cho cuối 873, 323 năm cho cuối 935 —
  khớp với các mốc quy chuẩn ✔. Đây là chỗ dễ sai nhất trong cả ca, nên tôi ghi
  cả phép tính ra để vòng sau kiểm lại được chứ không phải tin tôi.
- **Tôi không đề nghị đổi 874–936 sang 873–935 theo Wikidata**: 7 tham chiếu ở
  rank preferred nghe thì mạnh, nhưng cả hai phát biểu `P569` của `Q316349` đều
  là **cùng một con số 873**, nên "7 tham chiếu" chỉ chứng rằng nhiều nơi chép
  873 — không chứng rằng 874 sai ✔.

---

## Ca 44 — `ch05-ce10-notes-review.md:639` · ý *Ba* không có trong `reviews/ch05-ce10-review.md`

**Phát hiện cũ:** khối tự giới thiệu là *"vòng bình duyệt CE10 chỉ ra"*, nhưng ý
*Ba* (tỉ lệ phần trăm rữa) không có trong báo cáo ấy; đề nghị tách "hai việc từ
vòng bình duyệt, một việc tự tìm".

**Đọc lại văn bản hiện tại:**
- Tiêu đề khối (`content/ch05.md:1268`) là **"Ba việc ở tầng chapter, ghi lại
  cho P4"** — **không** có cụm "vòng bình duyệt CE10 chỉ ra", tức mệnh đề quy
  công mà phát hiện cũ nhắm vào **không còn trong file**.
- Ý *Ba* tự ghi công đúng chỗ: *"**Vòng này** tìm thấy hai ca đã rữa và sửa
  theo cách không rữa lại được"* — "vòng này" là vòng viết, không phải vòng bình
  duyệt.
- Và trong `reviews/ch05-ce10-review.md` thì **có** ca cụ thể của đúng hiện
  tượng ấy: dòng 60 — *"Con số 1,3% là **tỉ lệ trước khi thêm chính mục
  này**"*; dòng 446 — *"`CE10-02` — '`Y học`… 1,3%'; `reports/stats.txt` ghi
  **1.5%**"*.

**Kết luận: KHÔNG CẦN SỬA.** Phát hiện cũ **không còn áp dụng được**: cụm quy
công mà nó phản đối đã không có trong văn bản hiện tại, và ý *Ba* đã tự ghi
công cho vòng viết. Ngoài ra, ngay cả nếu có quy công thì nó cũng không phải vô
căn cứ — báo cáo CE10 bắt được **ca cụ thể** (1,3% đã rữa thành 1,5%); cái vòng
viết tự thêm là **sự khái quát** từ ca ấy thành một quy ước. Phân biệt
"ca cụ thể" với "khái quát" là một ranh giới tinh hơn mức mà một dòng ghi công
cần phải phân giải.

`[KHÔNG KIỂM ĐƯỢC]`: tôi **không** dựng lại được bản nháp mà báo cáo cũ đã đọc,
nên không xác định được cụm "vòng bình duyệt CE10 chỉ ra" từng tồn tại rồi bị
gỡ, hay báo cáo cũ diễn giải tiêu đề khối. Kết luận không đổi theo cả hai
đường, vì văn bản hiện tại đã đúng.

---
---

# Tổng kết

## Bảng theo bốn hạng kết luận

| Ca | Mục / khối | Kết luận |
|---|---|---|
| 11 | `CH05-CE08-01` Abu Muslim — "cuối năm ấy chiếm Merv" | **BẮT BUỘC sửa** |
| 6b | `CH05-CE07-09` Isiđôrô — "chia thành **hai mươi quyển** là do Braulio" (**lỗi mới, chín báo cáo trước đều bỏ sót**) | **BẮT BUỘC sửa** |
| 2 | `CH05-CE06-11` Bhavavarman — "giới nghiên cứu thấy" + "vị vua **đầu tiên**" | NÊN sửa |
| 3 | `CH05-CE06-12` Boethius — dòng Nguồn thiếu tác giả bài SEP thứ hai | NÊN sửa |
| 4 | `CH05-CE07-03` Ali — Madelung "rõ nhất trong giới hiện đại" | NÊN sửa |
| 5 | `CH05-CE07-04` Thái Tông — "sử do chính triều ông soạn" | NÊN sửa |
| 7 | `CH05-CE07-10` Pháp Xứng — nguồn SEP không có URL | NÊN sửa |
| 8 | `CH05-CE07-11` Tùng Tán Cán Bố — `Trung bình` → `Thấp` | NÊN sửa |
| 9 | `CH05-CE07-12` Pakal — "cá nhân châu Mỹ tiền Columbus biết rõ nhất" | NÊN sửa |
| 12 | `CH05-CE08-02` Al-Mansur — "trung tâm suốt năm thế kỷ" | NÊN sửa |
| 13 | `CH05-CE08-05` Sibawayh — so sánh với ngữ pháp Hy Lạp–Latin | NÊN sửa |
| 14 | `CH05-CE08-06` Charlemagne — Einhard cùng dòng Nguồn với McKitterick | NÊN sửa |
| 15 | `CH05-CE08-07` Bêđa — "bắt đầu ở một tu viện Northumbria" | NÊN sửa |
| 16 | `CH05-CE08-07` Bêđa — Alcuin `trực tiếp` → `qua trường phái` | NÊN sửa |
| 17 | `CH05-CE08-09` Đỗ Phủ — "biến cố lớn nhất thế kỷ 8 ở Đông Á" | NÊN sửa |
| 19 | Khối Kaleb — nhan đề chuyên khảo Robin | NÊN sửa |
| 20 | Khối Kaleb — "ba mươi lăm năm" | NÊN sửa |
| 21 | Khối Chân Lạp — Vickery quy mệnh đề cho Claude Jacques | NÊN sửa |
| 22 | Khối URL — CSLA xếp nhầm vào "chết hoặc chặn" | NÊN sửa |
| 24 | Khối Boethius ý (4) — "làm nó nổi tiếng" → "một bài toán" | NÊN sửa |
| 25 | Khối Đông Nam Á — "dòng đầu của `ch90.md` nói rõ" | NÊN sửa |
| 26 | Khối Võ Tắc Thiên ý (2) — "k. 424–430" | NÊN sửa |
| 27 | Khối bốn nguồn — "Plofker là người phản đối" | NÊN sửa |
| 28 | Khối Charlemagne/CE08 — "sứ bộ … **đều** thuộc thế kỷ 8" | NÊN sửa |
| 30 | Khối Shankara — bỏ mất cách đọc Vikramāditya thứ hai | NÊN sửa |
| 32 | Khối URL — bẫy `429 / Varnish` chưa vào danh sách | NÊN sửa |
| 33 | Hai "lớn nhất" lệch chỗ rào (**gộp vào Ca 17, không mở phiếu riêng**) | NÊN sửa |
| 35 | Khối người bị cắt CE09 — "*Gaṇitasārasaṅgraha* (850)" | NÊN sửa |
| 36 | Khối người bị cắt CE09 — "một bước lùi so với `CH05-CE07-08`" | NÊN sửa |
| 37 | Ba mục CE09 — chỉ một tự khai "có thể bị bác" | NÊN sửa |
| 39 | Khối đích tự do — "lint không biết" → "lint hiện chưa" | NÊN sửa |
| 40 | Khối bẫy CE10 (5) — `Q172383` có `P569` **preferred** là `somevalue` | NÊN sửa |
| 42 | Khối CE10 — ca ʻAhoʻeitu, `P31 = Q6949213` | NÊN sửa |
| 43b | Khối người bị cắt CE10 — **lời chẩn** "quy đổi AH→CE bằng công thức" sai | NÊN sửa |
| 1 | `CH05-CE06-06` Tùy Văn Đế — "Khai Hoàng luật năm 583" (**phát hiện cũ sai**) | **KHÔNG CẦN SỬA** |
| 6a | `CH05-CE07-09` — "Braulio, **học trò ông**" (**phát hiện cũ sai**) | **KHÔNG CẦN SỬA** |
| 10 | `CH05-CE07-12` — năm in Tiesler & Cucina 2006 | **KHÔNG CẦN SỬA** |
| 18 | `CH05-CE08-10` — `trị vì 755–797` so với bốn `P570` | **KHÔNG CẦN SỬA** |
| 23 | Khối Boethius ý (2) — "dịch trọn Plato lẫn Aristotle" (**phát hiện cũ sai**) | **KHÔNG CẦN SỬA** |
| 29 | Khối Shankara — chuỗi truyền Tiele ← Yajñeśvara ← Nīlakaṇṭha | **KHÔNG CẦN SỬA** |
| 31 | Khối niên đại yếu — Jabir 721 ← Holmyard 1927, Delva 2017 | **KHÔNG CẦN SỬA** |
| 34 | Khối Divashtich — văn khố Mugh, UNESCO 2025, ~80 văn kiện | **KHÔNG CẦN SỬA** |
| 38 | Khối Châu Đại Dương — "khoảng 950" cho ʻAhoʻeitu | **KHÔNG CẦN SỬA** |
| 41 | Khối Vācaspati — trích dẫn "nửa đầu thế kỷ 9" (**phát hiện cũ sai**) | **KHÔNG CẦN SỬA** |
| 43a | Khối CE10 — **con số** al-Ashʿarī 874–936 | **KHÔNG CẦN SỬA** |
| 44 | Khối "Ba việc ở tầng chapter" — ý *Ba* (**phát hiện cũ không còn áp dụng**) | **KHÔNG CẦN SỬA** |

**Cộng: 44 ca** — 2 BẮT BUỘC · 32 NÊN · 12 KHÔNG CẦN SỬA (Ca 6 và Ca 43 mỗi ca
tách làm hai nửa khác hạng).

## `[KHÔNG KIỂM ĐƯỢC]` — những chỗ vòng này KHÔNG xác minh được

Liệt kê riêng, vì đây là phần dễ bị đọc nhầm thành "đã kiểm, không sao".

| # | Mệnh đề | Thuộc ca |
|---|---|---|
| 1 | *Tùy thư* 刑法志 — không mở được sử liệu gốc cho hai bản 581/583 | Ca 1 |
| 2 | Niên đại soạn chính xác của *Trinh Quán chính yếu* (707–709 hay đời Huyền Tông) | Ca 5 |
| 3 | Tác giả bài SEP "Dharmakīrti" — không kiểm lại Tillemans ở lần ghi đầu (sau đó kiểm riêng: `citation_author = Tillemans, Tom` ✔) | Ca 7 |
| 4 | Năm mất Tùng Tán Cán Bố: 649 (Tibetan Annals) hay 650 — **cần mở Dotson 2009**, đừng sửa theo Wikipedia | Ca 8 |
| 5 | Trang bản quyền Tiesler & Cucina — không phân biệt được năm copyright với năm phát hành | Ca 10 |
| 6 | McKitterick 2008 có dành phần phê bình cho **riêng** Einhard hay không | Ca 14 |
| 7 | Niên đại soạn *Martyrium Arethae* ("k. 560") | Ca 20 |
| 8 | Trạng thái `bitig.kz` — vòng này **không** kiểm lại | Ca 22 |
| 9 | Niên đại chính xác của T. 387 trong kinh lục Hán văn | Ca 26 |
| 10 | Mốc "tháng 10/2024 Bodleian lùi niên đại Bakhshali về 799–1102" | Ca 27 |
| 11 | "*Gaṇitasārasaṅgraha* là văn bản Ấn Độ **sớm nhất** dành riêng cho toán học" — chưa đối chiếu *Bakhshālī*, *Pāṭīgaṇita* | Ca 36 |
| 12 | Bản nháp mà `ch05-ce10-notes-review.md` đã đọc khi viết phát hiện về ý *Ba* | Ca 44 |

## Ba việc vòng này thấy mà rổ không hỏi tới

1. **Năm báo cáo cũ kết luận ngược** (Ca 1, 6a, 23, 41, 44), và chúng **không
   cùng một kiểu hỏng**:
   - Ca 1 và Ca 6a: đề xuất sửa sẽ **biến một câu đúng thành câu sai**.
   - Ca 23: `[KHÔNG KIỂM ĐƯỢC]` tuyên dạng **phủ định toàn xưng** ("không có
     trên trang") dựa trên ba lần `grep` trượt chuỗi.
   - Ca 41: tra `git show HEAD:` thay vì `git log -S`, tức tra **một bản chụp**
     để kết luận về một câu **đã bị sửa**.
   - Ca 44: phản đối một cụm chữ **không còn trong văn bản**.
   Bốn kiểu này cần bốn phép phòng khác nhau; gộp chúng thành "báo cáo cũ có
   thể sai" là mất thông tin.

2. **Bốn dấu `[KHÔNG KIỂM ĐƯỢC]` của vòng trước nay GỠ được** (Ca 29 chuỗi
   Tiele, Ca 31 chuỗi Jabir, Ca 34 UNESCO 2025, Ca 38 mốc 950). Cả bốn đều gỡ
   được bằng **cùng một thao tác**: tra lại bằng một dạng chuỗi khác, hoặc tra
   một trang **lân cận** thay vì trang chính (Tuʻi Tonga Empire thay vì
   ʻAhoʻeitu; mục thư mục của bài thay vì bài). Đáng đưa vào `CONTRIBUTING.md`:
   `[KHÔNG KIỂM ĐƯỢC]` nên ghi kèm **chuỗi đã thử**, để vòng sau biết thử gì
   khác.

3. **Một hình dạng lỗi lặp đủ nhiều để thành quy tắc: câu thay thế mang đúng
   lỗi nó vừa chẩn.** Ba ca trong rổ này:
   - Ca 13 (Sibawayh): vòng 1 bác một cấp nhất bằng Donatus/Priscianus/Dionysius
     Thrax, rồi dùng chính ba tác phẩm ấy làm vế đối lập trong câu thay thế —
     và câu ấy **đã được chép vào file**.
   - Ca 9 (Pakal): báo cáo cũ chẩn một cấp nhất rồi đề xuất một cấp nhất khác
     ("dày nhất"), và tự thú `[KHÔNG KIỂM ĐƯỢC]` cho nó ngay dòng sau.
   - Ca 19 (Robin): câu thay thế dùng đại từ "ông" ở chỗ chủ ngữ gần nhất là
     Robin, nên nó trỏ sai đúng người mà nó đang đi sửa.
   Phép phòng rẻ nhất: **đọc câu thay thế như thể nó là câu gốc, bằng đúng tiêu
   chí vừa dùng để chẩn** — và viết ra kết quả phép đọc ấy, như mọi ca trong
   báo cáo này đã làm ở phần "Soi lại".
