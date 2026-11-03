# Bình duyệt độc lập — ghi chú biên tập vòng CE08, phần 2 (8 khối)
Ngày: 2026-11-02 · phạm vi: content/ch05.md, từ khối "Ô Trung Á" tới khối "Harun al-Rashid"

Phương pháp: định vị 8 khối bằng `grep -n` trên tiêu đề (hiện ở dòng 1168, 1171, 1174, 1177,
1180, 1183, 1186, 1189 — số dòng có thể xê dịch tiếp). Đọc 12 mục `CH05-CE08-01…-12`
(`content/ch05.md` dòng 412–627), `reports/stats.txt`, `CONTRIBUTING.md`, `README.md`,
`content/ch90.md`, `atlaslib/lint.py`, `atlaslib/common.py`, và ba vòng soi ghi chú trước
(`reports/ch05-ce09-review-c.md`, `-d.md`, `reports/ch05-ce10-notes-review.md`), cộng với
`reports/ch05-ce08-review.md` (vòng soi gốc của chính 8 khối này, §B-10 … §B-15).

Mọi tỉ lệ vùng được **đếm lại bằng script trên chính `content/*.md`**, không chép từ
`reports/stats.txt`, rồi mới đối chiếu với `stats.txt`. Hai mẫu số được dùng xuyên suốt:

| Mốc | Tổng mục atlas chính | Cách dựng |
|---|---:|---|
| trước nhóm CE08 | **209** | ch01 38 + ch02 39 + ch03 48 + ch04 60 + ch05 (CE06+CE07) 24 |
| sau nhóm CE08 (lúc 8 khối này được viết) | **221** | + 12 mục CE08 — khớp con số `73/221` mà chính khối 6 tự khai |
| hiện nay (sau CE09 + CE10) | **245** | khớp dòng 1 `reports/stats.txt` |

Đếm theo vùng, ba mốc:

| Vùng | 209 | 221 | 245 (nay) |
|---|---:|---:|---:|
| Trung Đông/Bắc Phi | 69 (33,0%) | 73 (33,0%) | 79 (32,2%) |
| Châu Âu | 57 (27,3%) | 59 (26,7%) | 62 (25,3%) |
| Đông Á | 51 (24,4%) | 54 (24,4%) | 60 (24,5%) |
| Nam Á | 25 (12,0%) | 26 (11,8%) | 28 (11,4%) |
| Châu Phi hạ Sahara | 4 (**1,9%**) | 4 (**1,8%**) | 5 (**2,0%**) |
| Trung Á | 1 (**0,5%**) | 2 (**0,9%**) | 4 (**1,6%**) |
| Châu Mỹ | 1 (0,5%) | 2 (0,9%) | 3 (1,2%) |
| Đông Nam Á | 1 (**0,5%**) | 1 (**0,5%**) | 4 (**1,6%**) |
| Châu Đại Dương | 0 (0,0%) | 0 (0,0%) | 0 (0,0%) |

Đính chính một tiền đề của đề bài: CE09 và CE10 thêm **ba** mục Đông Nam Á, không phải hai —
`CH05-CE09-01` Jayavarman II, `CH05-CE10-05` Khúc Thừa Dụ, `CH05-CE10-06` Mpu Sindok. Ô Đông
Nam Á đi từ 1 lên 4.

Quy ước dùng để chấm "số liệu rữa" là quy ước mà **khối tầng chapter của chính file này** đặt
ra (`content/ch05.md` dòng 1270): *"con số trong ghi chú biên tập phải tự khai nó đo ở thời
điểm nào, hoặc không nêu số."* Vòng CE10 đã áp quy ước ấy cho các khối CE09/CE10 nhưng
**không áp ngược lên bốn khối vùng của vòng CE08** — đó là nguồn gốc của phần lớn lỗi dưới đây.

---

## Khối 1 — Ô "Trung Á" của atlas đo một từ vựng chín ô, không đo lịch sử Nội Á

**Đã kiểm được (không có phát hiện)**
- `REGIONS` có đúng **9 ô** và **không có ô nào cho Nội Á / thế giới thảo nguyên**:
  `atlaslib/common.py` dòng 75. Khớp bảng "Từ vựng cố định" của `CONTRIBUTING.md` (`REGIONS` 9,
  mỗi người 1).
- Mệnh đề nền của khối là **quy tắc đã thành văn**, không phải suy diễn riêng:
  `CONTRIBUTING.md`, *Quy ước trường `vùng:`*, điểm 3 viết nguyên văn rằng cao nguyên Mông Cổ
  ghi Đông Á và *"'Trung Á' trên thực tế chỉ còn dùng cho vành đai Transoxiana–Iran đông"*.
- Phép thử tự kiểm khớp đúng hai mục nó dẫn. `CH05-CE08-01` ghi `nơi: Merv và Khurasan`,
  `vùng: Trung Á`; `CH05-CE08-04` ghi `nơi: Kufa và Baghdad`, `vùng: Trung Đông/Bắc Phi`, và
  thân mục nói đúng chữ *"gốc Trung Á"* (không phải "sinh ở Trung Á") — tức khối đã ăn khớp với
  mục sau đợt sửa của `reports/ch05-ce08-review.md` §B-10.
- Hai ca "bị dồn vào Đông Á" đều kiểm được: cao nguyên Mông Cổ — `CH03-BCE02-12 · Mặc Đốn
  thiền vu`, `nơi: … cao nguyên Mông Cổ`, `vùng: Đông Á`; Tây Tạng — `CH05-CE08-10 · Trisong
  Detsen`, `nơi: Lhasa và Samye, cao nguyên Tây Tạng`, `vùng: Đông Á`.
- `CH02-BCE06-09` đúng là **Zarathustra**, và trường `nơi:` của chính mục ấy ghi
  *"đông Iran **hoặc** Trung Á"*. Mệnh đề "vị trí địa lý còn là câu hỏi mở" đứng được.
- *"người 'Trung Á' duy nhất của atlas **trước nhóm này** là Zarathustra"* — **đúng**: ở mốc 209
  mục, ô Trung Á có đúng 1 người.
- *"Sau Chapter 5, 'Trung Á' trong atlas thực tế chỉ còn nghĩa Transoxiana–Iran đông"* — **đúng
  và vẫn đúng sau CE09/CE10**: bốn mục Trung Á hiện có là Zarathustra (đông Iran/Trung Á),
  `CH05-CE08-01` (Merv–Khurasan), `CH05-CE09-09` (Bukhara–Samarkand), `CH05-CE10-04`
  (Samanid, Bukhara). Không mục nào nằm ngoài vành đai ấy.

**BẮT BUỘC** — con số đã rữa, và nó đã sai ngay trong chính vòng viết ra nó.

Nguyên văn: *"Nghĩa là con số *Trung Á = 0,5%* đang đứng trên một người mà vị trí địa lý còn là
câu hỏi mở."*

Sai ở đâu — hai lớp:

1. **Rữa.** `0,5%` là 1/209, tức ô Trung Á **trước** khi nhóm CE08 được dựng. Ngay khi nhóm này
   vào dữ liệu, ô ấy là 2/221 = 0,9%; `reports/stats.txt` hiện ghi `Trung Á 4 1.6%`. Câu viết ở
   thì hiện tại (*"đang đứng"*) nên nó tự nhận là mô tả trạng thái hiện hành, và trạng thái ấy
   đã đổi hai lần.
2. **Mâu thuẫn nội bộ, cùng vòng, cách 15 dòng.** Khối 6 của chính vòng CE08
   (`content/ch05.md` dòng 1184) viết: *"Trung Á và Châu Mỹ lần đầu nhúc nhích, **từ 1 lên 2
   người mỗi ô**"*. Hai khối của cùng một vòng vì vậy nói ngược nhau về cùng một ô: khối 1 bảo
   ô Trung Á đứng trên **một** người, khối 6 bảo nó vừa lên **hai**. Khối 6 đúng.
   Vòng sau còn chồng thêm: khối CE09 "Độ nghiêng vùng" (dòng 1208) ghi Trung Á *"lên 1,3%"*,
   và khối CE10 "Ba ô vùng trống" nằm trong một file mà `stats.txt` nói 1,6%.

Bằng chứng: đếm lại trực tiếp trên `content/*.md` cho ô `Trung Á` — 209 mục → 1; 221 mục → 2;
245 mục → 4 (`CH02-BCE06-09`, `CH05-CE08-01`, `CH05-CE09-09`, `CH05-CE10-04`), khớp dòng
`Trung Á 4 1.6%` của `reports/stats.txt`.

Đề xuất câu thay thế nguyên văn (bỏ hẳn tỉ lệ, theo quy ước dòng 1270 — câu dưới không chứa
mẫu số nào nên không rữa lại được):
> Nghĩa là ô `Trung Á` của atlas mở ra trên một người mà vị trí địa lý còn là câu hỏi mở: trước nhóm CE08, Zarathustra là mục `Trung Á` duy nhất, và nhóm này mới thêm người thứ hai.

**NÊN** — "quy ước 1" dễ bị đọc nhầm thành "quy tắc 1".

Nguyên văn: *"đúng quy ước 1 và đúng phần nghĩa còn lại của 'Trung Á'…"*. `CONTRIBUTING.md` có
hai danh sách đánh số chạy song song: *Quy tắc nội dung* 1–8 (quy tắc 1 = "Tra Wikidata Q-ID
bằng API") và *Quy ước trường `vùng:`* 1–4 (điểm 1 = "nơi hoạt động chính"). Chính khối này
dẫn "quy tắc 6" và "quy tắc 7" ở các khối lân cận theo danh sách thứ nhất, nên "quy ước 1"
đứng một mình là chỗ va chạm thật.
> …đúng *Quy ước trường `vùng:`* điểm 1 của `CONTRIBUTING.md` và đúng phần nghĩa còn lại của "Trung Á"…

**CÂN NHẮC** — khối nên trỏ thẳng vào chỗ quy ước đã được ghi thành văn.

Khi khối này được viết, *Quy ước trường `vùng:`* điểm 3 của `CONTRIBUTING.md` đã tồn tại và nói
gần như cùng một câu ("Mọi con số Trung Á phải đọc kèm giới hạn từ vựng này"). Câu kết của khối
— *"Mọi so sánh tỷ lệ vùng phải đọc kèm giới hạn này"* — vì vậy đang lặp lại một quy tắc đã có
chỗ đứng mà không trỏ tới nó. Thêm một tham chiếu sẽ làm khối ngắn hơn và khó rữa hơn.

---

## Khối 2 — Đông Nam Á ở lại 0,5%, và lý do không phải là không tìm

**Đã kiểm được (không có phát hiện)**
- **Bia Canggal 732 / Sanjaya** — xác nhận lại trực tiếp (en.wikipedia REST summary, User-Agent
  trung lập): bi ký Phạn ngữ niên đại 732, quần thể đền Gunung Wukir, Trung Java, chép sắc dụ
  của Sanjaya.
- **Bia Kalasan 778 / Śailendra** — xác nhận lại trực tiếp: niên đại **700 Śaka** (= 778 CN),
  và đúng là *"the first inscription discovered in Indonesia that mentioned the dynastic name of
  Sailendra"*. Mệnh đề "bi ký đầu tiên ở Indonesia nêu tên dòng họ Śailendra" **đúng nguyên văn**.
- **`Q42798` không phải người** — tôi tra lại `wbgetentities`: nhãn en *"Borobudur Temple"*,
  `P31` = `Q5393308`, `Q839954`, `Q2736554`; **không có `Q5`**. Mệnh đề của khối đúng.
- **Quy tắc 6 sạch, và vẫn sạch sau CE09/CE10.** `grep` "Sanjaya" và "Panangkaran" trên toàn
  `content/`: hai cái tên chỉ xuất hiện **trong chính khối này**, không có mục ở ch01–ch05 hay
  ch90. Không ai trong hai người được viết dưới dạng ID.
- **`ch90.md` không chứa nhân vật Java.** 40 mục của phụ lục đều là nhân vật lịch sử Việt Nam,
  nên kết luận "không đẩy xuống phụ lục được" đứng vững về mặt thực tế.
- Lý do loại theo tiêu chí (c) và (d) — người bảo trợ chứ không phải người khởi tạo — nhất quán
  với nguyên tắc mà khối lĩnh vực CE09 (`content/ch05.md` dòng 1214) gọi tên là *"loại người bảo
  trợ, giữ người làm ra tri thức"*.

**BẮT BUỘC** — tỉ lệ trong **tiêu đề khối** đã rữa.

Nguyên văn (tiêu đề): *"**Đông Nam Á ở lại 0,5%**, và lý do không phải là không tìm"*

Sai ở đâu: `0,5%` = 1/221, đúng vào lúc viết. `reports/stats.txt` hiện ghi
`Đông Nam Á 4 1.6%`. Ô này đã **gấp bốn** kể từ khi khối được viết, nên một tiêu đề viết ở thể
khẳng định hiện tại đang nói sai với người đọc trước cả khi họ đọc thân khối. Đây cũng là chỗ
quy ước dòng 1270 áp thẳng: tiêu đề không tự khai thời điểm đo.

Bằng chứng: đếm lại trên `content/*.md` — ô `Đông Nam Á` ở mốc 221 có đúng 1 mục
(`CH05-CE06-11 · Bhavavarman I`); ở mốc 245 có 4 (`CH05-CE06-11`, `CH05-CE09-01 · Jayavarman
II`, `CH05-CE10-05 · Khúc Thừa Dụ`, `CH05-CE10-06 · Mpu Sindok`). Khối CE09 "Độ nghiêng vùng"
(dòng 1208) đã tự ghi *"Đông Nam Á lên 0,9%"*, tức bản thân file đã mâu thuẫn với tiêu đề này
từ vòng CE09.

Đề xuất tiêu đề thay thế nguyên văn (không chứa tỉ lệ nên không rữa lại được):
> **Đông Nam Á ở lại một mục sau nhóm CE08, và lý do không phải là không tìm**

**BẮT BUỘC** — câu kết của thân khối đã rữa theo cùng một cách.

Nguyên văn: *"Con số 1 người Đông Nam Á trong thống kê là con số thật, không phải con số thiếu
sót kỹ thuật."*

Sai ở đâu: "con số 1 người… trong thống kê" mô tả `reports/stats.txt`, mà `stats.txt` **không
còn ghi 1**. Đáng chú ý là `stats.txt` tự khai mẫu số ngay ở dòng đầu (*"245 nhân vật (atlas
chính) + 40 ở phụ lục"*) trong khi câu này thì không — nên người đọc đối chiếu hai file sẽ thấy
một mâu thuẫn mà không có chỗ nào giải thích. Lập luận bên dưới câu (không phải thiếu sót kỹ
thuật) vẫn đúng; chỉ con số hỏng.

Đề xuất câu thay thế nguyên văn:
> Việc atlas khi ấy chỉ có một mục Đông Nam Á (`CH05-CE06-11`) là kết quả thật của bốn tiêu chí, không phải một thiếu sót kỹ thuật — và các vòng sau cho thấy nó không phải trần: CE09 và CE10 thêm `CH05-CE09-01`, `CH05-CE10-05` và `CH05-CE10-06`.

**NÊN** — *"`ch90.md` là phụ lục **Việt Nam**, không phải phụ lục Đông Nam Á"* nói chặt hơn hai
văn bản định nghĩa phụ lục.

`content/ch90.md` dòng 3 viết: *"ảnh hưởng được đo trong phạm vi **Việt Nam và Đông Nam Á**"*,
và `README.md` dòng 15 viết: *"Phụ lục Việt Nam dùng hệ quy chiếu **Việt Nam / Đông Nam Á**"*.
Hai câu ấy mô tả **hệ quy chiếu**, không phải phạm vi tuyển người — nhưng chúng khiến câu phủ
định của khối trông như bị chính repo bác. Chỗ dựa chắc là tiêu đề chapter (*"Phụ lục · Việt
Nam qua các thời kỳ"*) cộng với việc cả 40 mục đều là nhân vật lịch sử Việt Nam. Vòng
`reports/ch05-ce09-review-d.md` đã bắt một ca cùng loại ở khối 12 (dòng 3 của `ch90.md` bác một
mệnh đề về "định nghĩa của phụ lục"), nên đây là chỗ tái phát.
> Thứ hai, phụ lục `ch90.md` tuyển **nhân vật lịch sử Việt Nam** — cả 40 mục hiện có đều thế, dù hệ quy chiếu của nó được khai là "Việt Nam và Đông Nam Á" — nên Sanjaya và Panangkaran không thể "đẩy xuống phụ lục": nếu không vào track chính thì họ không vào đâu cả.

**CÂN NHẮC** — khối nên trỏ tới `CH05-CE10-06`.

Luận điểm của khối là "lý do không phải là không tìm". Vòng CE10 về sau **đã** đưa một người
cai trị Java vào track chính (`CH05-CE10-06 · Mpu Sindok`), và mục ấy còn nhắc chính các triều
đại Śailendra–Mataram mà khối này bàn. Một câu trỏ sang đó biến khối từ một lời biện hộ thành
một mắt xích kiểm chứng được.

---

## Khối 3 — Châu Phi hạ Sahara thế kỷ 8: ba hệ chữ viết, không hệ nào phục vụ được

**Đã kiểm được (không có phát hiện)**
- **Kyriakos / Michael I / Baqt.** Michael I làm giáo hoàng Alexandria 743–767, nên khung
  `fl. k. 748` quả thật là niên đại **dựng ngược từ triều giáo hoàng**, đúng như khối tự khai.
- **Nguồn về Kyriakos được mô tả đúng sau đợt sửa của vòng CE08.** Câu hiện tại
  (*"phần chép chuyện ông là *Life of Michael* của John the Deacon, k. 768–770, tức gần như
  đương thời, nên vấn đề không phải nguồn muộn mà là nguồn **đơn độc và ngoại lai**"*) là bản đã
  áp khuyến nghị "NÊN SỬA (2)" của `reports/ch05-ce08-review.md` §B-12 — tức khối không còn trộn
  tuổi bộ biên soạn thế kỷ 11 với tuổi bản văn.
- **Aksum ngừng đúc tiền nửa đầu thế kỷ 7, đợt cuối quanh 620** — bản hiện tại là bản đã sửa
  theo "BẮT BUỘC SỬA (1)" của cùng báo cáo; bản nháp cũ ghi "đầu thế kỷ 8".
- **`CH04-CE04-09` = Ezana xứ Aksum** và **`CH05-CE06-09` = Kaleb xứ Aksum** — hai ID trỏ đúng
  người (đọc trực tiếp tiêu đề mục).
- **al-Yaʿqūbī 872 là nguồn viết sớm nhất về Kanem** — nhất quán với `CH05-CE09-08` ("Vì sao
  chọn"), nơi chính mốc ấy được dùng lại: *"al-Yaʿqūbī k. 872 chép tên vua Zaghawa"*.
- **Luận điểm nền vẫn đứng sau khi thêm mục thứ năm.** Tôi kiểm từng mục Châu Phi hạ Sahara
  theo tiêu chí "tiền đúc hoặc bi ký còn hoạt động": `CH02-BCE08-06` Piye và `CH02-BCE07-09`
  Taharqa (Kush, bi ký vương triều), `CH04-CE04-09` Ezana và `CH05-CE06-09` Kaleb (tiền đúc
  Aksum), và mục mới `CH05-CE09-08` Georgios I — mà `Nguồn:` của chính mục ấy neo vào **mộ chí
  Hy ngữ ngày 5-6-887** (DBMNT số 12). Mục thứ năm **không** phá khái quát; nó củng cố.

**BẮT BUỘC** — "Bốn mục" đã rữa.

Nguyên văn: *"**Bốn mục** Châu Phi hạ Sahara hiện có của atlas đều rơi vào các thế kỷ mà tiền
đúc hoặc bi ký còn hoạt động."*

Sai ở đâu: chữ *"hiện có"* khoá câu vào trạng thái hiện hành, và trạng thái ấy là **năm**, không
phải bốn — vòng CE09 thêm `CH05-CE09-08 · Georgios I của Makuria`. `reports/stats.txt` ghi
`Châu Phi hạ Sahara 5 2.0%`; đếm lại trên `content/*.md` cho đúng 5 mục đã liệt ở trên.

**BẮT BUỘC** — `1,9%` không khớp mẫu số nào của vòng viết ra nó.

Nguyên văn: *"Đó không phải trùng hợp: con số **1,9%** đo hình dạng của tư liệu."*

Sai ở đâu, và đây là ca nặng hơn ca trên vì nó **đã lệch ngay lúc viết**:
- `1,9%` = 4/209, tức ô Châu Phi hạ Sahara **trước** khi nhóm CE08 được dựng.
- Ở mốc mà chính vòng này tự khai trong khối 6 (*"73/221"*), con số đúng là 4/221 = **1,8%**.
  Nhóm CE08 không thêm mục Châu Phi hạ Sahara nào, nên chỉ mẫu số tăng và tỉ lệ **tụt**.
- Hiện nay là 5/245 = **2,0%**.

Nghĩa là cùng một vòng CE08 dùng hai mẫu số khác nhau ở hai khối cách nhau chín dòng: khối 6
dùng 221, khối 3 dùng 209. Vòng soi gốc (`reports/ch05-ce08-review.md` §B-12) xác nhận "Bốn
mục ✓" nhưng **không** kiểm lại con số 1,9%, nên lỗi này lọt qua.

Đề xuất câu thay thế nguyên văn cho **cả hai câu** (bỏ tỉ lệ, liệt kê mục để người sau kiểm
được, và tự khai mốc đo):
> Tính tới hết Chapter 5, mọi mục Châu Phi hạ Sahara của atlas — Piye và Taharqa ở Kush, Ezana và Kaleb ở Aksum, Georgios I `CH05-CE09-08` ở Makuria — đều rơi vào các thế kỷ mà tiền đúc hoặc bi ký còn hoạt động. Đó không phải trùng hợp: ô này đo hình dạng của tư liệu.

**BẮT BUỘC** — *"có đúng một cá nhân có tên và có niên đại"* bị bác bởi chính mệnh đề liền sau nó.

Nguyên văn: *"Vùng này có **đúng một cá nhân có tên và có niên đại** — **Kyriakos xứ Makuria**,
`fl. k. 748`…"*

Sai ở đâu: hai câu sau, chính khối nêu tên hai vua Makuria khác — *"bản này xếp triều ông sau
Markos, bản khác đặt giữa **Merkurios** và **Zacharias I**"*. Merkurios là một cá nhân **có tên
và có niên đại thế kỷ 8**: en.wikipedia ghi *"reigned 697 – c. 722"* (tra lại trực tiếp qua API
MediaWiki, User-Agent trung lập), tức phần lớn triều ông nằm trong khung 701–800 của nhóm CE08.
Zacharias I cũng là một mục riêng có thật. Vậy tiêu chí thật mà khối đang dùng không phải "có
tên và có niên đại" — Kyriakos cũng không có niên đại riêng, khung của ông là dựng ngược — mà
là **"có một việc làm cụ thể được một nguồn gần đương thời thuật lại"**. Khối đang nêu một tiêu
chí dễ bác thay cho tiêu chí thật của nó, và phản ví dụ nằm trong chính câu của nó.

Đề xuất câu thay thế nguyên văn:
> Vùng này có đúng một cá nhân thế kỷ 8 mà một nguồn gần đương thời thuật lại được **một việc làm cụ thể** — **Kyriakos xứ Makuria**, `fl. k. 748`, người đem quân vào Ai Cập Umayyad tới tận Fustat để buộc thả giáo hoàng Alexandria Michael I, vi phạm hiệp ước Baqt. Danh sách vua Makuria còn nêu **Merkurios** (trị vì 697 – k. 722) và **Zacharias I**, nhưng những gì quy cho hai người ấy được rút ra từ chính các danh sách vua, không từ một bản thuật sự kiện.

`[KHÔNG KIỂM ĐƯỢC]` trong đề xuất trên: mệnh đề cuối (*"được rút ra từ chính các danh sách vua,
không từ một bản thuật sự kiện"*) tôi chỉ kiểm được tới mức en.wikipedia — bài Merkurios quy
việc sáp nhập Nobatia cho triều ông bằng công thức *"Authorities believe"*, tức là suy luận của
giới nghiên cứu chứ không phải trích một nguồn thuật sự. Tôi **không** mở được nghiên cứu
chuyên ngành về danh sách vua Makuria để loại trừ một bản thuật sự kiện nào đó về Merkurios.
Nếu vòng sau không muốn mang mệnh đề chưa kiểm hết, cắt câu thứ hai và chỉ giữ câu thứ nhất là
đủ — câu thứ nhất đã đúng một mình.

---

## Khối 4 — Châu Đại Dương 0,0%: ô trống duy nhất còn lại, và nó có lý do

**Đã kiểm được (không có phát hiện)**
- **`0,0%` chưa rữa và không rữa được trong im lặng.** Đếm lại trên `content/*.md`: ô Châu Đại
  Dương = 0 ở cả ba mốc 209 / 221 / 245. Khớp `reports/stats.txt` (`Châu Đại Dương 0 0.0%`).
- **"ô trống duy nhất còn lại" vẫn đúng, và thật ra còn đúng mạnh hơn khối tự nhận.** Trong 9 ô
  `REGIONS`, tám ô còn lại đều ≥ 1. Mở rộng ra toàn bộ từ vựng cố định: 16 ô `FIELDS` đều ≥ 1
  (ô mỏng nhất `Y học` = 6), 4 ô `BIG_QUESTIONS` đều ≥ 1, 4 ô `RELATION_TYPES` và 3 ô
  `EVIDENCE_LEVELS` đều ≥ 1. Châu Đại Dương là **ô trống duy nhất trong toàn bộ từ vựng của
  atlas**, không chỉ trong bảng vùng.
- **Chữ "còn lại" có chỗ dựa.** Trước Chapter 5, Châu Mỹ và Đông Nam Á cũng bằng 0 — chính
  comment ở `atlaslib/lint.py` (quanh dòng 194) ghi *"Ch4 từng qua cổng lint sạch trong khi Châu
  Mỹ, Đông Nam Á và Châu Đại Dương bằng 0 trên toàn atlas"*. Hai ô kia đã được lấp trong
  Chapter 5; ô này thì chưa.
- **Trích dẫn PNAS: tôi mở được và nó đúng từng chữ.** Qua Crossref (`10.1073/pnas.1015876108`):
  tác giả Wilmshurst, Hunt, Lipo, Anderson ✓; *PNAS* **108(5): 1815–1820** ✓; in tháng 2-2011
  (lên mạng 27-12-2010), nên ghi **(2011)** là dạng trích chuẩn ✓ — khối đã sửa đúng theo
  khuyến nghị của `reports/ch05-ce08-review.md` §B-13. Qua Europe PMC tôi lấy được **toàn văn
  tóm tắt**, và bốn con số của khối khớp nguyên văn: *"1,434 radiocarbon dates"* ✓;
  *"earliest in the Society Islands A.D. ∼1025-1120"* ✓; *"after 70-265 y"* ✓; *"dispersal
  continued in one major pulse to all remaining islands A.D. ∼1190-1290"* ✓.
- **`pnas.org` vẫn trả HTTP 403** — tôi thử lại, đúng như khối ghi.
- **Ba tầng lý do được hai vòng sau dẫn lại và không vòng nào sửa tầng nào.** Khối CE09 về
  ʻAhoʻeitu (dòng 1220) viết *"vòng CE09 không sửa tầng nào"* và áp **tầng (3)** nguyên vẹn lên
  Tonga; khối CE10 "Ba ô vùng trống" (dòng 1260) viết *"ba tầng lý do của khối CE08 vẫn nguyên"*.
  Ba khối nói cùng một chuyện, không có chỗ nào lệch.
- **Hai ca đối chiếu khớp repo.** *Zangs gling ma* cách Padmasambhava bốn thế kỷ — nhất quán với
  `CH05-CE08-10` ("Vì sao chọn": *"tiểu sử đầu tiên ra đời khoảng bốn thế kỷ sau"*).
  Tì-ni-đa-lưu-chi: `CH90-CE01_09-04` ghi `hoạt động 580–594` và *"Thiền uyển tập anh soạn rất
  muộn"* — xem CÂN NHẮC dưới về con số "bảy thế kỷ".
- **Rongorongo**: cách rào *"ngay tư cách chữ viết của nó vẫn còn là giả thiết"* là cách rào
  đúng, không nói quá về phía "đã biết".

**BẮT BUỘC** — khối tuyên bố một giới hạn rồi vượt qua chính giới hạn ấy ở mệnh đề liền sau.

Nguyên văn: *"…và nội dung các bài phản biện thì đánh dấu là **không kiểm được**. Điều đó không
đổi kết luận: **phe phản biện đòi niên đại sớm hơn**, mà tầng (2) và (3) độc lập hoàn toàn với
tranh luận ấy."*

Sai ở đâu: hai mệnh đề này không đứng chung được. Khối vừa khai rằng nội dung các bài phản biện
**không kiểm được**, rồi ngay câu sau phát biểu **nội dung ấy** ("đòi niên đại sớm hơn") và dùng
nó làm bản lề để trấn an người đọc. Đây đúng loại lỗi mà `CONTRIBUTING.md` quy tắc 7 và
`README.md` (*"model thì tự tin kể cả khi sai"*) tồn tại để chặn, và nó nặng hơn ở đây vì khối
này tự đặt mình làm khuôn mẫu khai giới hạn cho các vòng sau.

Bằng chứng tôi thu được, và nó **đổi được một phần**: bài phản biện **có thật và tra ra được** —
Mulrooney, Bickler, Allen & Ladefoged, *"High-precision dating of colonization and settlement in
East Polynesia"*, *PNAS* **108: E192–E194** (2011), `10.1073/pnas.1100447108`, có kèm thư trả
lời của nhóm tác giả ở **E195** (Europe PMC xếp loại `letter; comment`). Nhưng bản ghi **không
có tóm tắt**, nên tôi xác nhận được **sự tồn tại và thể loại**, không xác nhận được **lập
trường** của nó. Mệnh đề "đòi niên đại sớm hơn" vì vậy vẫn chưa ai kiểm — `[KHÔNG KIỂM ĐƯỢC]`, và câu thay thế dưới đây được viết sao cho không cần tới nó.

Đề xuất câu thay thế nguyên văn:
> Phải ghi rằng niên đại rút ngắn của Wilmshurst **bị phản biện ngay trên cùng tạp chí**: Mulrooney, Bickler, Allen & Ladefoged, *PNAS* 108: E192–E194 (2011), kèm thư trả lời của nhóm tác giả ở E195. Bản gốc bài chính không mở được qua `pnas.org` (HTTP 403), nhưng toàn văn tóm tắt lấy được qua Europe PMC và bốn con số trên khớp nguyên văn; **lập trường của bài phản biện thì vòng này không đọc được** — chỉ xác nhận được nó tồn tại. Kết luận ở đây vì vậy không treo vào tầng (1): nếu phản biện thắng theo hướng niên đại sớm hơn thì tầng (1) lung lay, còn tầng (2) và (3) độc lập hoàn toàn với tranh luận niên đại.

**NÊN** — *"Theo quy tắc 7"* viện sai điều khoản.

Nguyên văn: *"**Theo quy tắc 7**, phải ghi rằng niên đại rút ngắn của Wilmshurst bị phản biện…"*
Quy tắc 7 của `CONTRIBUTING.md` nói về việc một nguồn **bị dùng ngược với lập luận của chính
nó** (ca Hansen, ca Fried & Unguru bị ghi sai thể loại). Ở đây Wilmshurst không bị dùng ngược —
khối dùng đúng kết luận của bài báo. Việc phải công bố rằng một niên đại còn tranh chấp có chỗ
dựa khác và đúng hơn: mục *Về những giai đoạn còn tranh luận* trên trang Overview, được
`CONTRIBUTING.md` trỏ tới ở phần "Phản hồi mà không cần viết code". `reports/ch05-ce09-review-c.md`
đã bắt đúng một ca cùng hình dạng ở khối Jabir (*"viện quy tắc nội bộ làm chỗ dựa giả"*), nên
đây là chỗ tái phát.
> Theo nguyên tắc công bố ở mục *Về những giai đoạn còn tranh luận*, phải ghi rằng…

**CÂN NHẮC** — *"bảy thế kỷ"* cho khoảng cách *Thiền uyển tập anh* – Tì-ni-đa-lưu-chi là con số
nói nhẹ, và nói nhẹ theo hướng làm yếu lập luận của chính khối.

`CH90-CE01_09-04` ghi Tì-ni-đa-lưu-chi `hoạt động 580–594`; `reports/ch05-ce08-review.md` §B-13
đặt *Thiền uyển tập anh* ở k. 1337 và tính ra **khoảng bảy thế kỷ rưỡi**. Vì khối dùng con số
này làm **thước so sánh dưới** cho khoảng cách hơn một nghìn năm của Châu Đại Dương, ghi nhẹ đi
nửa thế kỷ chỉ làm thước ngắn lại. Đề nghị ghi "bảy thế kỷ rưỡi" kèm mốc k. 1337 — con số ấy
không rữa vì cả hai đầu đều cố định.

**CÂN NHẮC** — `0,0%` trong tiêu đề không tự khai mốc đo.

Theo chữ của quy ước dòng 1270, mọi con số trong ghi chú biên tập phải tự khai thời điểm đo.
`0,0%` là ngoại lệ thực tế duy nhất đáng bàn: nó không thể rữa trong im lặng, vì ngày ô này có
người thì toàn bộ khối phải viết lại chứ không chỉ con số. Ghi ra để vòng P4 quyết dứt điểm là
quy ước có ngoại lệ "số 0" hay không, thay vì để mỗi vòng tự xử.

---

## Khối 5 — Ứng viên Việt Nam trong nhóm CE08 (yêu cầu D5)

**Đã kiểm được (không có phát hiện)**
- **Ba ID trỏ đúng người, và trường `năm:` khớp từng chữ** (đọc trực tiếp `content/ch90.md`):
  `CH90-CE01_09-06` = Mai Hắc Đế, `năm: hoạt động k. 713–722` ✓;
  `CH90-CE01_09-07` = Phùng Hưng, `năm: hoạt động k. 766–791` ✓;
  `CH90-CE01_09-08` = Khương Công Phụ, `năm: 731–805` ✓.
- **Quy tắc 6 — sạch, và vẫn sạch sau CE09/CE10.** Đây là chiều "người đã có mục ở chỗ khác",
  và khối dùng **đúng hình thức được phép** của `CONTRIBUTING.md` quy tắc 6 (*"nói rõ 'có mục
  riêng ở nhóm X nên không phải ứng viên bị loại'"*): nó nêu tên ba người, nói thẳng *"quy tắc 6
  **cấm** nêu tên họ như ứng viên bị loại"* và kết *"không có đánh đổi nào xảy ra"*. Không ai
  trong ba người được viết dưới dạng ID trong phần "Vì sao chọn" của bất kỳ mục CE08 nào.
- **Không có trôi dạt sau hai vòng mới.** Mục duy nhất Việt Nam được CE09/CE10 thêm vào mạch
  chính là `CH05-CE10-05 · Khúc Thừa Dụ`, thế kỷ 10 — ngoài khung 701–800, nên không chạm vào
  khối này. Ca Khúc Thừa Dụ mà vòng CE10 gặp (`reports/ch05-ce10-notes-review.md` khối 4 và 6)
  **không** lặp lại ở đây.
- **`731–805` khớp Wikidata.** `Q6191512` (nhãn vi *Khương Công Phụ*, zh *姜公輔*, `P31 = Q5`):
  `P569 = +0731`, `P570 = +0805` — tra lại trực tiếp bằng `wbgetentities`.
- **Chức "Đồng trung thư môn hạ bình chương sự" đúng, và kiểm được tới nguồn sơ cấp.**
  *Tân Đường thư* quyển 152 (đọc toàn văn trên zh.wikisource) chép: 「乃擢公輔**諫議大夫、同中書
  門下平章事**」. Cũng xác nhận luôn hai chi tiết của `CH90-CE01_09-08`: việc can gián về đám
  tang **Đường An công chúa** (「唐安公主道薨… 公輔諫曰」) và việc ông mất vào lúc Thuận Tông lên
  ngôi, tức 805 (「順宗立，拜吉州刺史，未就官卒」).
- **Cảnh báo "tộc phả họ Khương ở Thạch Thất" là cảnh báo hướng tới tương lai, không mô tả sai
  hiện trạng.** Mục `CH90-CE01_09-08` hiện **không** có chi tiết gia thế nào và `Nguồn:` chỉ ghi
  *Tân Đường thư* quyển 152 và *Toàn Đường văn* quyển 446 — không có tộc phả. Khối nói rõ đây là
  cảnh báo *"cho vòng nào viết lại mục ấy"*, nên đúng phạm vi.

**BẮT BUỘC** — *"đỗ đầu kỳ thi nhà Đường năm 780"* không có chỗ dựa trong chính nguồn mà mục
Khương Công Phụ dẫn, và nó là **cùng một mệnh đề** mà khối tự cấm ở câu cuối.

Nguyên văn: *"Khương Công Phụ có hồ sơ tốt nhất trong ba người — **ông đỗ đầu kỳ thi nhà Đường
năm 780** và thăng tới Đồng trung thư môn hạ bình chương sự dưới Đường Đức Tông…"*

Sai ở hai chỗ, và hai chỗ độc lập nhau:

1. **Thứ hạng "đỗ đầu" không có trong nguồn.** *Tân Đường thư* quyển 152 — nguồn mà
   `CH90-CE01_09-08` dẫn đích danh — chép đúng chín chữ: 「姜公輔，愛州日南人。**第進士**，補校
   書郎，**以制策異等**授右拾遺，為翰林學士。」 Tức: ông **đỗ tiến sĩ**, rồi **chế sách "dị
   đẳng"** (một bậc xếp loại của khoa chế, không phải một thứ hạng nhất được nêu tên) thì được
   trao chức Hữu thập di. Không có chữ nào về việc đứng đầu kỳ thi.
2. **Năm 780 bị gắn vào sai kỳ thi.** *Tân Đường thư* quyển 152 **không nêu năm nào** cho cả hai
   kỳ. Theo zh.wikipedia (nguồn cấp ba, dẫn lại *Tân Đường thư* và các khảo cứu hiện đại), ông
   đỗ **tiến sĩ năm 764** (Quảng Đức năm thứ hai), còn **780** (Kiến Trung nguyên niên) là năm
   Đường Đức Tông mở khoa chế *"Hiền lương phương chính năng trực ngôn cực gián khoa"* mà ông
   「登榜」. Gộp hai kỳ thành một câu "đỗ đầu kỳ thi nhà Đường năm 780" là trộn kỳ thi tiến sĩ
   với khoa chế, rồi gán cho nó một thứ hạng không nguồn nào chép.

Vì sao đây là lỗi nặng chứ không phải lỗi chữ: **câu cuối của chính khối này** viết *"chữ 'trạng
nguyên' là thuật ngữ khoa cử Việt Nam đời sau áp ngược lên kỳ thi năm 780, nên phải viết là 'đỗ
đầu kỳ thi' kèm chú"*. Nhưng "trạng nguyên" và "đỗ đầu kỳ thi" khẳng định **cùng một thứ hạng**;
khối mới chỉ đổi từ vựng, trong khi vấn đề thật là **không có bằng chứng về thứ hạng**. Và mục
mà khối đang chú giải thì viết đúng hơn khối: `CH90-CE01_09-08` chỉ ghi *"ông **đỗ tiến sĩ** nhà
Đường"*, không nêu thứ hạng, không nêu năm. Khối ghi chú đang mạnh hơn mục nó bảo vệ.

Ghi thêm cho vòng sau: `reports/ch05-ce08-review.md` §B-14 đã duyệt câu này là *"✓ (khoa thi
thời Đường Đức Tông, năm Canh Thân 780)"* — tức một vòng bình duyệt đã ký nhận nó. Đây là ca cho
thấy "đã qua một vòng duyệt" không miễn cho việc mở nguồn sơ cấp.

Đề xuất câu thay thế nguyên văn (cho **cả câu giữa lẫn cảnh báo cuối**):
> Khương Công Phụ có hồ sơ tốt nhất trong ba người — *Tân Đường thư* quyển 152 chép ông **đỗ tiến sĩ**, rồi **chế sách "dị đẳng"** được trao chức Hữu thập di và vào Hàn lâm viện, và sau binh biến Kinh Nguyên năm 783 thăng tới **Gián nghị đại phu, Đồng trung thư môn hạ bình chương sự** dưới Đường Đức Tông, tức xuất hiện trong bộ máy quan chức chứ không chỉ trong truyền thuyết khởi nghĩa — nhưng ông thành công **bên trong** một hệ thống do người khác dựng.

> …và chữ "trạng nguyên" là thuật ngữ khoa cử Việt Nam đời sau áp ngược lên kỳ thi của ông. Không được thay nó bằng "đỗ đầu kỳ thi" — đó là cùng một mệnh đề thứ hạng, chỉ đổi chữ: *Tân Đường thư* quyển 152 chỉ chép "đệ tiến sĩ" và "chế sách dị đẳng", **không chép thứ hạng và không chép năm nào**.

`[KHÔNG KIỂM ĐƯỢC]` trong đề xuất trên: hai mốc **764** (tiến sĩ) và **780** (khoa chế) tôi chỉ
lấy được từ zh.wikipedia, không từ nguồn sơ cấp — vì vậy tôi **không** đưa hai mốc ấy vào câu
thay thế, chỉ dùng chúng để chứng minh rằng mốc 780 gắn với khoa chế chứ không gắn với kỳ thi
tiến sĩ. Mốc **783** (binh biến Kinh Nguyên) thì kiểm được: *Tân Đường thư* quyển 152 chép
「俄而涇師亂」 ngay trước đoạn thăng chức, và niên đại 783 của binh biến Kinh Nguyên là mốc phổ
thông — nếu vòng sau không muốn mang con số, bỏ hai chữ "năm 783" là đủ.

**NÊN** — *"các bộ sử Đường"* đặt sai thời của nguồn.

Nguyên văn: *"hai cuộc khởi nghĩa đầu đến qua *Đại Việt sử ký toàn thư* (thế kỷ 15) và **các bộ
sử Đường**, đều sau sự kiện nhiều thế kỷ"*. Hai bộ mà `CH90-CE01_09-06` thật sự dẫn là *Tân
Đường thư* và *Tư trị thông giám* — cả hai soạn **đời Tống, thế kỷ 11**, tức sử **về** nhà Đường
chứ không phải sử **của** nhà Đường. Kết luận ("sau sự kiện nhiều thế kỷ") không đổi, nhưng chữ
"sử Đường" làm người đọc hiểu ngược: nó gợi nguồn đương thời, trong khi lập luận của khối cần
đúng điều ngược lại.
> …hai cuộc khởi nghĩa đầu đến qua *Đại Việt sử ký toàn thư* (thế kỷ 15) và các bộ sử Trung Hoa chép về nhà Đường (*Tân Đường thư*, *Tư trị thông giám*, đều thế kỷ 11), đều sau sự kiện nhiều thế kỷ…

**CÂN NHẮC** — nhãn "(yêu cầu D5)" gợi một phép kiểm tự động mạnh hơn thực tế.

`atlaslib/lint.py` (dòng 46–48) kiểm D5 bằng một phép tìm chuỗi `"viet"`/`"vietnam"` trên **toàn
bộ** `## Ghi chú biên tập` của chapter, và chỉ cảnh báo **một lần cho cả chapter**. Nghĩa là năm
khối D5 của Chapter 5 (CE06…CE10) được giữ bằng **quy ước biên tập**, không bằng cổng lint: xoá
bốn trong năm khối thì lint vẫn im. Đáng ghi để vòng P4 biết chỗ này không có lưới an toàn.

---

## Khối 6 — Hình dạng của thế kỷ, không phải thiên lệch của người chọn

**Đã kiểm được (không có phát hiện)**
- **5/12 `Chính trị/Nhà nước`** — đếm tay 12 mục CE08: `-01` Abu Muslim, `-02` Al-Mansur, `-06`
  Charlemagne, `-10` Trisong Detsen, `-12` Yikʼin. Đúng 5.
- **5/12 `Tôn giáo/Tâm linh`** — `-03` Jaʿfar al-Sadiq, `-04` Abu Hanifa, `-07` Bêđa, `-10`
  Trisong Detsen, `-11` Ādi Shankara. Đúng 5.
- **`33,0% (73/221)`** — tính lại: ở mốc 221 mục, Trung Đông/Bắc Phi = 73, tức 33,03%. Đúng, và
  đây là **con số duy nhất trong tám khối có mẫu số đi kèm**, tức đã làm sẵn đúng việc mà quy
  ước dòng 1270 về sau mới đặt tên. Bản hiện tại là bản đã sửa theo "NÊN SỬA" của
  `reports/ch05-ce08-review.md` §B-15 (bản nháp ghi 33,2%).
- **Bốn suất Trung Đông/Bắc Phi trong nhóm** — `-02`, `-03`, `-04`, `-05`. Đúng 4; 4/12 = 33,3%
  so với 33,0% đang có, nên lập luận "giữ nguyên trạng, không phải trừng phạt vùng" đứng được.
- **"Tính cả Abu Muslim ở ô Trung Á thì thế giới Hồi giáo vẫn chiếm 5/12"** — đúng 5 mục.
- **"Trung Á và Châu Mỹ lần đầu nhúc nhích, từ 1 lên 2 người mỗi ô"** — đếm lại: ở mốc 209 cả
  hai ô đều = 1 (Zarathustra; `CH05-CE07-12` Pakal); ở mốc 221 cả hai = 2. Đúng, và vì câu được
  neo vào **tác động của chính nhóm này** nên nó không rữa khi mẫu số đổi.
- **"văn khố núi Mugh là của Divashtich, người bị loại"** — khớp `CH05-CE08-01` ("Vì sao chọn":
  *"Ứng viên bị loại là Divashtich xứ Panjikant, người để lại văn khố núi Mugh"*). Bản hiện tại
  là bản đã sửa theo mục 28 của bảng sửa trong `reports/ch05-ce08-review.md`.
- **"Yikʼin có bi ký Long Count do chính triều đình ông khắc"** — khớp `CH05-CE08-12` ("Vì sao
  chọn": *"nó được chính triều đình ông khắc bằng Long Count"*).

**BẮT BUỘC** — *"bốn trường phái luật Sunni"* đặt vào thế kỷ 8 cả hai trường phái của thế kỷ 9,
và nó bị bác bởi chính **nguồn mà mục Abu Hanifa dẫn**.

Nguyên văn: *"thế kỷ 8 đúng là thế kỷ của nhà nước mới (Abbasid, Carolingian, Thổ Phồn) và của
tôn giáo được thể chế hoá (**bốn trường phái luật Sunni**, quốc giáo Tây Tạng, Advaita)."*

Sai ở đâu — ba lớp bằng chứng, hai trong ba nằm trong repo:

1. **Niên đại của chính bốn người được lấy tên đặt cho bốn trường phái.** Tra Wikidata trực
   tiếp: Abu Hanifa `Q190896` mất **767**; Malik ibn Anas `Q312299` **711–795**; al-Shāfiʿī
   `Q294281` **767–820**; Ahmad ibn Hanbal `Q194442` **780–855**. Hai trong bốn người mất ở
   **thế kỷ 9**, không phải thế kỷ 8.
2. **Atlas tự xếp một trong hai người ấy sang nhóm sau.** `CH05-CE09-07 · Ahmad ibn Hanbal` nằm
   trong nhóm CE09 (801–900), và khối lĩnh vực CE09 (dòng 1214) kể ông là bằng chứng cho việc
   *"thế kỷ 9 đúng là lúc các truyền thống lớn cùng đóng khung chính điển của mình"*. Hai khối
   của cùng một file vì vậy dùng cùng một hiện tượng để giải thích **hai thế kỷ khác nhau**.
3. **Quy tắc 7 — nguồn bị dùng ngược.** `CH05-CE08-04` dẫn **Christopher Melchert, *The
   Formation of the Sunni Schools of Law, 9th–10th Centuries C.E.* (Brill, 1997)**. Nhan đề của
   chính quyển sách đặt việc **hình thành** các trường phái ở **thế kỷ 9–10**. Dùng nó để đỡ cho
   một mục rồi, ở khối ghi chú, lại viết rằng bốn trường phái là đặc trưng của thế kỷ 8 là đúng
   hình dạng lỗi mà `CONTRIBUTING.md` quy tắc 7 mô tả (ca Hansen).

Đề xuất câu thay thế nguyên văn:
> …thế kỷ 8 đúng là thế kỷ của nhà nước mới (Abbasid, Carolingian, Thổ Phồn) và của tôn giáo được thể chế hoá — hai trong bốn người được lấy tên đặt cho các trường phái luật Sunni sống và dạy ở thế kỷ này (Abu Hanifa mất 767, Malik ibn Anas mất 795; al-Shāfiʿī và Ibn Hanbal thì thuộc thế kỷ 9, và atlas xếp Ibn Hanbal ở `CH05-CE09-07`), Phật giáo thành quốc giáo Tây Tạng, và Advaita Vedānta thành hệ thống. Bản thân các **trường phái** thì Melchert — nguồn mà `CH05-CE08-04` dẫn — đặt ở thế kỷ 9–10.

Ghi kèm, ngoài phạm vi tám khối nhưng cùng một lỗi: câu *"Bốn trường phái luật Sunni và ngữ
pháp Ả Rập thành hình"* ở **Bối cảnh nhóm CE08** (dòng 413) và cụm *"sự kết tinh của bốn trường
phái luật"* ở khối trần-12 (dòng 1160) mang đúng mệnh đề này. Sửa một chỗ mà bỏ hai chỗ kia sẽ
tạo ra mâu thuẫn mới.

**NÊN** — *"cao hơn mức nền của atlas"* gộp một chênh lệch 13,6 điểm với một chênh lệch 2,3 điểm.

Tôi tính tỉ lệ **theo mục mang nhãn** (cùng đơn vị với "5/12") ở mốc 221:
`Tôn giáo/Tâm linh` 62/221 = **28,1%**, so với 5/12 = 41,7% → lệch **+13,6 điểm**;
`Chính trị/Nhà nước` 87/221 = **39,4%**, so với 5/12 = 41,7% → lệch **+2,3 điểm**.
Với n = 12, một mục đổi tay là 8,3 điểm — tức độ lệch của `Chính trị/Nhà nước` nhỏ hơn **một
phần ba** một mục. Nói nhóm này cao hơn mức nền ở cả hai ô rồi dựng một lời giải thích lịch sử
cho cả hai là đọc nhiễu thành tín hiệu ở ô thứ hai. (Lưu ý đơn vị: nếu đếm **theo ô lĩnh vực**
như các khối CE09/CE10 làm thì mức nền là 24,1% và 17,2%, còn nhóm này là 5/21 ô (đếm lại: 12 mục CE08 mang tổng cộng **21** ô lĩnh vực, vì `-02`, `-05`, `-09` chỉ có một lĩnh vực) — hai cách đếm
cho hai bức tranh khác nhau, nên khối phải nói nó đếm theo cách nào.)
> `Tôn giáo/Tâm linh` 5/12 là **cao rõ rệt** so với mức nền của atlas khi ấy (62/221 mục); `Chính trị/Nhà nước` 5/12 thì **đúng bằng mức nền** (87/221 mục), nên ô ấy không cần lời giải thích nào. Chỉ ô tôn giáo cần, và nó có: thế kỷ 8 là thế kỷ…

**NÊN** — *"khối tư liệu Sogdian cùng thời soi sáng bối cảnh Khurasan của ông"* đặt văn khố sai
chỗ và sai thì.

Văn khố núi Mugh là của Divashtich xứ **Panjikant**, tức **Sogdiana / Transoxiana**, không phải
Khurasan — và chính khối 1 ở trên phân biệt hai thứ ấy khi nói "Transoxiana–Iran đông". Về
thời: khối CE08 ngay trên (dòng 1167) ghi Divashtich **thua trận năm 722**, trong khi Abu Muslim
được phái về Khurasan **năm 745**; hai mươi ba năm chênh nhau thì "cùng thời" là cách nói rộng.
Câu vẫn đúng ở ý chính (tư liệu chứng cho bối cảnh, không chứng cho người — khối tự nói thế ở
câu kết), chỉ cần đặt đúng chỗ.
> …Abu Muslim có truyền thống sử Abbasid, và bối cảnh Khurasan–Transoxiana mà ông khai thác thì có khối tư liệu Sogdian của thế hệ ngay trước (văn khố núi Mugh, khép lại năm 722) soi sáng…

**CÂN NHẮC** — thêm hai chữ "khi ấy" vào câu 33,0%.

`(73/221)` đã ghim được thời điểm đo, nên câu này **không** thuộc loại số liệu rữa. Nhưng vòng
CE10 khi áp quy ước dòng 1270 đã chọn cách viết *"toàn atlas **khi ấy**"* và *"245 mục atlas
chính sau vòng CE10"*. Để ba vòng dùng cùng một thể thức, đề nghị: *"giữ tỷ lệ atlas **khi ấy**
đứng nguyên ở 33,0% (73/221); sau CE09 và CE10 tỉ lệ này còn 32,2%"*.

---

## Khối 7 — Alcuin: người lẽ ra phải ở nhóm này

**Đã kiểm được (không có phát hiện)**
- **`Q154332` đúng là Alcuin, và mệnh đề `P569` đúng từng chữ.** Tôi tra lại trực tiếp bằng
  `wbgetentities` (User-Agent trung lập): nhãn en = *Alcuin*, `P31 = Q5`, và `P569` có **đúng ba
  giá trị** — `+0724` (normal), `+0735` (normal), `+0740` (**preferred**). Biên độ 740 − 724 =
  **16 năm**, khớp "ba giá trị lệch nhau mười sáu năm" và khớp cả thứ tự "740 preferred / 735 /
  724" mà khối viết. `reports/ch05-ce08-review.md` dòng 38 đã kiểm một lần; tôi kiểm lại độc lập
  và ra cùng kết quả.
- **Năm mất 804 đúng.** `P570` hạng preferred = `+0804-05-19`.
- **Quy tắc 6 — sạch.** `grep "Alcuin"` trên `content/ch05.md` cho 5 lần, `content/ch90.md` cho 0
  lần; cả 5 lần ở ch05 đều là **văn bản tự do** (hai dòng `Ảnh hưởng tới` của `CH05-CE08-06` và
  `CH05-CE08-07`, phần "Vì sao chọn" của `-07`, khối Charlemagne dòng 1142, và khối này).
  Alcuin **không có mục riêng ở bất kỳ chapter nào, kể cả `ch90`** — nên nêu ông làm ứng viên bị
  loại là hợp lệ, và vẫn hợp lệ sau CE09/CE10.
- **"trùng vai với Charlemagne ở ô `Giáo dục`"** — `CH05-CE08-06` quả thật mang
  `lĩnh vực: Chính trị/Nhà nước, **Giáo dục**`, và `Ảnh hưởng tới` của nó có dòng *"Alcuin xứ
  York và cải cách học thuật Carolingian"*. Lý do loại khớp với "Vì sao chọn" của
  `CH05-CE08-07`.
- **"ở Tours 796–804"** — khớp en.wikipedia (*"In 796, he was made abbot of … Tours … He remained
  there until his death"*).
- **Khối ăn khớp với hai khối khác của file.** Khối Charlemagne (dòng 1142) dùng cùng quy tắc
  "giai đoạn ảnh hưởng chính" theo cùng hướng; và `reports/ch05-ce09-review-d.md` ghi rằng lập
  luận "ô `Giáo dục` của CE09 trống" treo vào đúng kết luận của khối này (Alcuin thuộc CE08).
  Ba chỗ nhất quán.

**BẮT BUỘC** — *"ra hai chapter"* mô tả sai cấu trúc của chính repo.

Nguyên văn: *"…nếu được viết thì hai mục **phải cùng nhóm**, không được tách một cặp thầy–trò
của cùng một chương trình cải cách **ra hai chapter**."*

Sai ở đâu: CE08 và CE09 **đều là nhóm của Chapter 5**. `content/ch05.md` chứa năm nhóm —
`## Nhóm CE06` (dòng 4), `CE07` (209), `CE08` (412), `CE09` (628), `CE10` (846). Đặt Alcuin vào
CE09 sẽ tách cặp thầy–trò ra **hai nhóm trong cùng một chapter**, không phải hai chapter. Cái
giá thật vì vậy nhỏ hơn cái giá khối nêu, và vì toàn bộ sức nặng của câu nằm ở chữ "hai
chapter", nó đang mượn một hậu quả không có thật.

Đề xuất câu thay thế nguyên văn:
> …nếu được viết thì hai mục **phải cùng nhóm**, không được tách một cặp thầy–trò của cùng một chương trình cải cách ra hai nhóm thế kỷ — và lần này không phải vì ranh giới chapter (CE08 và CE09 đều thuộc Chapter 5) mà vì bảng phân bố theo nhóm là thứ atlas dùng để tự đọc.

**NÊN** — `độ tin cậy niên đại: Thấp` chặt hơn thang mà chính nhóm CE08 đang dùng.

Khối kê đơn `Thấp` cho một hồ sơ gồm **ba năm sinh cạnh tranh trong 16 năm + một năm mất xác
định tới từng ngày**. Đối chiếu trong cùng nhóm:
- `CH05-CE08-02 · Al-Mansur` — *"Niên đại ghi **Trung bình** vì các nguồn cho ba năm sinh khác
  nhau: 709, 713 và 714"*;
- `CH05-CE08-06 · Charlemagne` — **Trung bình**, và `CH05-CE08-12` mô tả ông là người *"năm sinh
  … vẫn còn ba phương án cạnh tranh là 742, 747 và 748"*;
- `CH05-CE08-05 · Sibawayh` — **Thấp**, vì *"nguồn cho hai khung chết **loại trừ nhau**, khác cả
  nơi chết"*; `CH05-CE08-11 · Shankara` — **Thấp**, vì niên đại là tranh luận mở hàng thế kỷ.

Tức thang thực tế của nhóm: ba năm sinh cạnh tranh → `Trung bình`; năm mất không chốt được hoặc
niên đại tranh chấp cả thế kỷ → `Thấp`. Alcuin thuộc nhóm thứ nhất, và còn **tốt hơn** al-Mansur
ở chỗ có ngày mất chính xác. Dung sai `Trung bình` của `CONTRIBUTING.md` là ±25 năm, rộng hơn
biên độ 16 năm ở đây.
> …nên mục ấy phải ghi `độ tin cậy niên đại: Trung bình` kèm một câu nêu cả ba giá trị — cùng cách `CH05-CE08-02` xử ba năm sinh của al-Mansur. (`Thấp` để dành cho ca như `CH05-CE08-05`, nơi hai khung chết loại trừ nhau.)

**NÊN** — "người được đề nghị nhường là Sibawayh" là một đánh đổi chưa được tính giá, và khối 6
đã tính giá ngược lại.

Khối 6 (dòng 1184) biện minh **đúng bốn** suất Trung Đông/Bắc Phi bằng lập luận "giữ tỷ lệ atlas
đứng nguyên ở 33,0% (73/221)". Rút Sibawayh để nhận Alcuin sẽ:
- hạ Trung Đông/Bắc Phi của nhóm từ 4/12 (33,3%) xuống 3/12 (25,0%) — tức phá chính lập luận
  "giữ nguyên trạng" của khối 6, và hạ "thế giới Hồi giáo 5/12" xuống 4/12;
- nâng Châu Âu từ 2/12 lên 3/12, trong khi Châu Âu khi ấy đang ở 26,7% toàn atlas;
- **xoá ô `Ngôn ngữ học` khỏi nhóm** — Sibawayh là mục `Ngôn ngữ học` duy nhất của CE08 (đếm 21
  ô lĩnh vực của nhóm), để nhận thêm một ô `Giáo dục` thứ hai của châu Âu.

Thêm nữa, `CH05-CE08-07` khung cùng việc ấy khác đi: ở đó Alcuin là *"ứng viên bị loại **cùng
vùng**"* của Bêđa, tức một suất **Châu Âu**, không phải một suất Trung Đông. Hai chỗ trong cùng
chapter đang đề nghị lấy chỗ từ hai vùng khác nhau cho cùng một người.
> Và nếu cần một suất, hai phương án phải được nêu kèm giá: lấy suất Châu Âu (đổi với `CH05-CE08-07`, đúng khung mà mục ấy đang dùng), hoặc lấy suất Trung Đông của Sibawayh — phương án sau làm mất ô `Ngôn ngữ học` duy nhất của nhóm và phá lập luận "giữ tỷ lệ đứng nguyên" của khối về hình dạng thế kỷ.

**CÂN NHẮC** — *"triều Aachen 782–796"* đặt tên một nơi trước khi nơi ấy thành triều đình.

Phần lớn cung Aachen được dựng **trong thập niên 790** (en.wikipedia, *Palace of Aachen*:
*"Most of the Carolingian palace was built in the 790s"*), còn triều đình Carolingian trước đó
di động. en.wikipedia mô tả Alcuin là người ở *"the Carolingian court"* trong thập niên 780–790,
không gắn ông với Aachen cho giai đoạn đầu. Mốc 782–796 thì đúng; chỉ cái tên nơi là đặt sớm.
Đề nghị viết "ở triều đình Charlemagne 782–796".
`[KHÔNG KIỂM ĐƯỢC]`: năm chính xác mà triều đình chuyển hẳn về Aachen — tôi chỉ có mốc "thập
niên 790" từ en.wikipedia, không mở được nghiên cứu chuyên ngành. Vì vậy đề nghị trên là **bỏ
tên nơi**, không phải thay bằng một mốc khác.

---

## Khối 8 — Tiền đề bị bác bỏ: Harun al-Rashid và cái gọi là "Nhà Trí tuệ"

**Ghi chú phạm vi trước khi vào nội dung.** Khối này **tự khai là khối của vòng CE09**, không
phải CE08: câu mở là *"Ghi chú CE08 dặn vòng CE09 nhặt lại Harun al-Rashid. **Vòng này** đã
đánh giá lại độc lập và từ chối"*. Nó cũng đã được soi một lần với tư cách ấy —
`reports/ch05-ce09-review-c.md` mở đầu bằng *"Phạm vi: … từ khối `**Tiền đề bị bác bỏ: Harun
al-Rashid và cái gọi là "Nhà Trí tuệ"**` tới hết file"* và đặt nó làm mục **§1**. Tôi vẫn rà
theo yêu cầu, nhưng ghi ra để vòng P4 không đếm nó hai lần vào hai vòng khác nhau, và để biết
rằng **hai phát hiện của vòng CE09 với khối này chưa được áp** (xem mục cuối).

**Đã kiểm được (không có phát hiện)**
- **Nhan đề sách đúng từng chữ.** Trang Routledge (HTTP 200) trả về tiêu đề
  *"The Abbasid House of Wisdom: Between Myth and Reality - 1st Edition"*. Crossref xác nhận
  đây là một `monograph` của **Routledge**, ISBN `9781003323679`, tác giả Ekmeleddin İhsanoğlu.
- **Luận điểm của sách đúng như khối mô tả, và mục lục chứng cho điều đó.** Crossref liệt kê các
  chương: *"Baghdad and the Rise of Interest in Foreign Sciences"* (tr. 1–13), **"Creating a
  Myth"** (14–24), **"Dissecting the Myth"** (25–33), *"What to Call a Library in Arabic?"*
  (34–38), *"What Was the Abbasid Caliph's Library Called?"* (39–49), *"Was the House of Science
  an Arena for Debates?"* (50–55), *"What Was the Reality?"* (56–67), *"What Happened to the
  House of Wisdom?"* (68–71), *"The Impact"* (72–77), *"Concluding Remarks"* (78–80). Mệnh đề
  "Bayt al-Ḥikma như một học viện có khoa, có ban, có chương trình dịch thuật là sản phẩm được
  dựng lên" khớp với cấu trúc "tạo huyền thoại → mổ xẻ huyền thoại → thực tế là gì".
- **Cảnh báo MacTutor đúng nguyên văn, và tôi tự mở trang để xác nhận.**
  `https://mathshistory.st-andrews.ac.uk/Biographies/Hunayn/` trả HTTP 200 và chứa đúng cụm
  *"leading translator in the **House of Wisdom** at one of the most remarkable periods of
  mathematical revival"*. Đây không phải mệnh đề dựng ra.
- **Và cảnh báo ấy đã được thi hành trong mục.** `Nguồn:` của `CH05-CE09-06` ghi đích danh:
  *"MacTutor … — **dùng cho niên đại và địa vị, không dùng cho mệnh đề thiết chế**"*. Khối mô tả
  đúng trạng thái repo, không nói khống.
- **"chapter có `CH05-CE09-06 · Hunayn ibn Ishaq` chứ không có người chi tiền"** — đúng, và
  "Vì sao chọn" của chính mục ấy nói cùng một câu: *"Hai ứng viên bảo trợ, Harun al-Rashid và
  al-Maʾmun, bị loại vì lý do ấy."*
- **Quy tắc 6 — sạch.** `grep "Harun"` trên `content/ch05.md` cho 5 lần, `content/ch90.md` cho 0
  lần; không lần nào là một mục, và dòng `Ảnh hưởng tới` của `CH05-CE08-02` (*"Harun al-Rashid
  và triều đình Baghdad thế kỷ 9"*) là **văn bản tự do**, đúng dạng cho người không có mục.
- **Nội chiến 811–813** — Fitna thứ tư, do dàn xếp kế vị của Harun gây ra; đã được
  `reports/ch05-ce09-review-c.md` §1 kiểm và tôi không bác được.

**BẮT BUỘC** — năm xuất bản của quyển sách chủ lực sai một năm.

Nguyên văn: *"İhsanoğlu, *The Abbasid House of Wisdom: Between Myth and Reality* (Routledge,
**2023**)…"*

Sai ở đâu: hai cơ sở dữ liệu thư mục độc lập đều cho **2022**.
- **Crossref** (sổ đăng ký DOI, nguồn do chính nhà xuất bản nộp): bản ghi `monograph` của ISBN
  `9781003323679` có `issued = 2022-07-21`, và cả mười bản ghi chương con đều mang cùng ngày.
- **OpenLibrary**: `first_publish_year = 2022` cho **cả hai** ISBN mà vòng CE09 đã dẫn —
  `9781032347455` (bìa cứng) và `9781032347486` — với publisher Routledge / Taylor & Francis.

Đây là loại lỗi mà `CONTRIBUTING.md` nhắm tới ở quy tắc 3 và quy tắc 7: một chi tiết thư mục
được ghi mà không mở bản ghi gốc. Nó nhỏ, nhưng khối này là khối **dạy các vòng sau cách xử lý
một tiền đề sai**, nên trích dẫn của nó bị soi kỹ hơn mức thường.

Đề xuất câu thay thế nguyên văn:
> İhsanoğlu, *The Abbasid House of Wisdom: Between Myth and Reality* (Routledge, 2022), lập luận rằng…

`[KHÔNG KIỂM ĐƯỢC]` trong đề xuất trên: trang Routledge dựng bằng JavaScript nên tôi **không**
đọc được trường ngày xuất bản trên chính trang ấy — chỉ đọc được nhan đề và "1st Edition". Nếu
tồn tại một lần in bìa mềm năm 2023 thì cả hai năm đều có thể bảo vệ được; nhưng OpenLibrary ghi
2022 cho cả ISBN bìa mềm, và không có bản ghi 2023 nào trong Crossref.

**BẮT BUỘC** — khối bác một kết luận của vòng CE08 mà không ghi rằng nó bác, nên file hiện mang
hai lý do loại trừ nhau cho cùng một người.

Nguyên văn: *"Vòng này đã đánh giá lại độc lập và từ chối, và **lý do không phải trần 12**."*

Sai ở đâu: khối CE08 mà chính câu đầu của khối này trích (`content/ch05.md` dòng 1160) viết:
*"Mười lăm ứng viên bị loại, trong đó **bốn người sẽ chắc chắn vào atlas nếu trần là 16**:
**Harun al-Rashid** …"*. Hai mệnh đề không đứng chung được: nếu Harun bị loại vì tiêu chí chứ
không vì trần, thì nâng trần lên 16 **không** đưa ông vào. Khối 8 có khối 1160 trong tay (nó
trích chính khối ấy ở câu mở) nhưng không nói rằng kết luận của mình **thay thế** kết luận kia,
nên người đọc file từ trên xuống gặp hai câu phủ định nhau cách nhau 30 dòng. Đây đúng hình
dạng lỗi mà `reports/ch05-ce10-notes-review.md` xếp loại **A** ("khối này mâu thuẫn với khối kia
trong cùng Ghi chú biên tập") và gọi là hình dạng áp đảo của vòng trước.

Đề xuất câu thay thế nguyên văn (một câu, đặt ngay sau câu mở):
> Vòng này đã đánh giá lại độc lập và từ chối, và lý do **không** phải trần 12 — tức kết luận này **thay thế** câu ở khối trần-12 phía trên, nơi Harun được kể vào nhóm "chắc chắn vào atlas nếu trần là 16"; nâng trần cũng không đưa ông vào, và khối ấy cần được sửa theo.

**NÊN** — *"Gutas (1998)"* là một trích dẫn trống tên tác phẩm.

Khối dẫn İhsanoğlu đầy đủ (tên sách, nhà xuất bản, năm) rồi dẫn Gutas bằng mỗi họ và năm.
`CONTRIBUTING.md` quy tắc 7 đòi người viết biết **nguồn lập luận gì**, mà một trích dẫn không
tên sách thì người sau không lần được. Tác phẩm là *Greek Thought, Arabic Culture: The
Graeco-Arabic Translation Movement in Baghdad and Early ʿAbbāsid Society* (Routledge, 1998) —
`reports/ch05-ce09-review-c.md` §1 đã tra và xác nhận nội dung khớp.
> …; Dimitri Gutas, *Greek Thought, Arabic Culture* (Routledge, 1998), từ lâu đã mô tả phong trào dịch thuật như một hiện tượng xã hội rộng, không phải sản phẩm của một toà nhà.

**NÊN** — hai phát hiện của vòng CE09 với chính khối này **chưa được áp**, và cả hai vẫn đúng.

`reports/ch05-ce09-review-c.md` §1 nêu hai điểm; đọc lại văn bản hiện tại thì không điểm nào
được sửa:
1. *"sản phẩm được dựng lên trong **thế kỷ 19 – đầu 20** bởi học giả Đông phương học"* — khung
   thế kỷ ấy là suy luận của người viết khối, không phải câu của İhsanoğlu. Tôi đọc được mục lục
   sách qua Crossref và nó **không** chứa mốc thế kỷ nào; nội dung sách thì tôi không mở được
   — `[KHÔNG KIỂM ĐƯỢC]`.
   Vì khối này tồn tại để dạy "đừng nói chặt hơn nguồn", nó nên tự áp quy tắc ấy trước.
2. *"hai thứ làm Harun nổi tiếng đều không phải của ông"* — chọn mẫu có lợi: Harun còn được biết
   qua chiến dịch Byzantium, sứ bộ với Charlemagne (chính `content/ch05.md` dòng 1142 nhắc sứ bộ
   ấy), và nền thuế vụ al-Maʾmun thừa hưởng.

Câu thay thế cho cả hai điểm đã có sẵn trong `reports/ch05-ce09-review-c.md` §1 và tôi không đề
xuất khác; việc cần làm là **áp**, không phải viết lại.

**CÂN NHẮC** — *"hệ quả chính trị trực tiếp nhất của ông"* là một so sánh hạng nhất không kiểm
được.

Mệnh đề nhân quả (dàn xếp kế vị → Fitna thứ tư) thì vững; chữ **"trực tiếp nhất"** thì đòi một
phép xếp hạng mọi hệ quả chính trị của Harun mà không ai trong các vòng duyệt làm. Bỏ hai chữ
ấy, câu không yếu đi: *"và một hệ quả chính trị trực tiếp của ông là cuộc nội chiến 811–813 do
chính sắp xếp kế vị của ông gây ra"*.

---

## Tổng kết

| Khối | Tên rút gọn | BẮT BUỘC | NÊN | CÂN NHẮC |
|---|---|---:|---:|---:|
| 1 | Ô "Trung Á" đo một từ vựng chín ô | 1 | 1 | 1 |
| 2 | Đông Nam Á ở lại 0,5% | 2 | 1 | 1 |
| 3 | Châu Phi hạ Sahara thế kỷ 8 | 3 | 0 | 0 |
| 4 | Châu Đại Dương 0,0% | 1 | 1 | 2 |
| 5 | Ứng viên Việt Nam trong nhóm CE08 (D5) | 1 | 1 | 1 |
| 6 | Hình dạng của thế kỷ | 1 | 2 | 1 |
| 7 | Alcuin: người lẽ ra phải ở nhóm này | 1 | 2 | 1 |
| 8 | Tiền đề bị bác bỏ: Harun al-Rashid | 2 | 2 | 1 |
| **Tổng** | | **12** | **10** | **8** |

### Gom 12 lỗi BẮT BUỘC theo loại

**A. Tỉ lệ vùng đã rữa, hoặc chưa bao giờ khớp mẫu số — 4 lỗi.**
Đúng như dự đoán, đây là nhóm lỗi lớn nhất, và nó tập trung ở ba khối vùng liền nhau.
- Khối 1: *"Trung Á = 0,5% đang đứng trên một người"* — 0,5% là 1/209 (trước CE08); ở mốc viết
  đã là 2/221 = 0,9%; nay 4/245 = 1,6%. **Khối 6 của cùng vòng** đã nói ngược ("từ 1 lên 2").
- Khối 2, **tiêu đề**: *"Đông Nam Á ở lại 0,5%"* — nay 1,6%; khối CE09 (dòng 1208) đã ghi 0,9%
  từ một vòng trước.
- Khối 2, thân: *"Con số 1 người Đông Nam Á trong thống kê"* — `stats.txt` ghi 4.
- Khối 3: *"con số 1,9%"* — không khớp mẫu số nào của vòng viết ra nó (4/209 = 1,9% là trạng
  thái **trước** CE08; ở mốc 221 là 1,8%; nay 2,0%). Ca duy nhất **đã sai ngay lúc viết**.

**B. Khối này mâu thuẫn với khối kia trong cùng `## Ghi chú biên tập` — 3 lỗi.**
Hình dạng áp đảo của vòng CE10 vẫn còn nguyên ở đây.
- Khối 1 ↔ khối 6 về số người trong ô Trung Á (xem A).
- Khối 6 ↔ khối lĩnh vực CE09 (dòng 1214) về việc "bốn trường phái luật Sunni" thuộc thế kỷ nào;
  atlas tự xếp Ibn Hanbal ở `CH05-CE09-07`.
- Khối 8 ↔ khối trần-12 (dòng 1160): một bên nói Harun bị loại **không** vì trần 12, bên kia nói
  ông **chắc chắn vào atlas nếu trần là 16**.

**C. Mệnh đề quá rộng mà phản ví dụ nằm trong chính câu hoặc chính nguồn của nó — 3 lỗi.**
- Khối 3: *"có đúng một cá nhân có tên và có niên đại"* — hai câu sau khối tự nêu Merkurios
  (trị vì 697 – k. 722) và Zacharias I.
- Khối 3: *"Bốn mục Châu Phi hạ Sahara **hiện có**"* — nay năm.
- Khối 6: *"bốn trường phái luật Sunni"* đặt ở thế kỷ 8, trong khi **nguồn mà `CH05-CE08-04` dẫn**
  (Melchert, *The Formation of the Sunni Schools of Law, **9th–10th Centuries C.E.***) đặt việc
  hình thành ở thế kỷ 9–10. Đây là ca quy tắc 7 rõ nhất của cả tám khối.

**D. Mệnh đề lịch sử không có chỗ dựa trong nguồn mà chính repo dẫn — 1 lỗi.**
- Khối 5: *"đỗ đầu kỳ thi nhà Đường năm 780"*. *Tân Đường thư* quyển 152 (nguồn của
  `CH90-CE01_09-08`, đọc toàn văn trên zh.wikisource) chỉ chép 「第進士」 và 「以制策異等」 — không
  thứ hạng, không năm. Và nó là **cùng một mệnh đề thứ hạng** mà câu cuối của chính khối tuyên
  bố phải loại bỏ ("trạng nguyên"). Một vòng bình duyệt trước đã ký nhận câu này là đúng.

**E. Mô tả sai cấu trúc của chính repo — 1 lỗi.**
- Khối 7: *"không được tách … **ra hai chapter**"*. CE08 và CE09 đều là nhóm của Chapter 5.

**F. Khối tuyên bố một giới hạn rồi vượt qua chính nó — 1 lỗi.**
- Khối 4: khai *"nội dung các bài phản biện … không kiểm được"*, rồi câu sau phát biểu nội dung
  ấy (*"phe phản biện đòi niên đại sớm hơn"*) và dùng nó làm bản lề cho kết luận.

**G. Lỗi thư mục — 1 lỗi.**
- Khối 8: İhsanoğlu, *The Abbasid House of Wisdom* — Routledge **2022**, không phải 2023
  (Crossref `issued 2022-07-21`; OpenLibrary `first_publish_year 2022` cho cả hai ISBN).

### Ba chỗ đã **được** sửa đúng và không nên động vào

Ghi lại để vòng sau khỏi "sửa" ngược:
1. Khối 3, mốc Aksum ngừng đúc tiền **nửa đầu thế kỷ 7 / quanh 620** — bản nháp ghi "đầu thế kỷ
   8" và đã được `reports/ch05-ce08-review.md` §B-12 sửa.
2. Khối 4, **(2011)** và cặp niên đại **1025–1120 / 1190–1290** — tôi xác minh lại từ Crossref và
   toàn văn tóm tắt Europe PMC, cả bốn con số khớp nguyên văn bài báo. Mục `[KHÔNG KIỂM ĐƯỢC]`
   mà vòng CE08 đặt ở đây **nay gỡ được**.
3. Khối 6, **33,0% (73/221)** và **"văn khố núi Mugh là của Divashtich"** — cả hai là bản đã sửa,
   và `(73/221)` là con số duy nhất trong tám khối đã tự khai mốc đo.

### Mọi chỗ `[KHÔNG KIỂM ĐƯỢC]`

1. **Khối 3** — *"những gì quy cho Merkurios và Zacharias I được rút ra từ danh sách vua, không
   từ một bản thuật sự kiện"* (nằm trong câu tôi đề xuất). Tôi chỉ kiểm tới en.wikipedia, nơi
   việc Makuria sáp nhập Nobatia được gán cho triều Merkurios bằng công thức *"Authorities
   believe"*. Không mở được nghiên cứu chuyên ngành về danh sách vua Makuria. Mốc **trị vì
   697 – k. 722** thì kiểm được (en.wikipedia, API MediaWiki).
2. **Khối 4** — **lập trường** của bài phản biện trên PNAS. Tôi xác nhận được **sự tồn tại và
   thể loại**: Mulrooney, Bickler, Allen & Ladefoged, *PNAS* 108: E192–E194 (2011),
   `10.1073/pnas.1100447108`, `letter; comment`, có thư trả lời ở E195 (Europe PMC). Bản ghi
   **không có tóm tắt**, nên mệnh đề "đòi niên đại sớm hơn" vẫn chưa ai kiểm — câu thay thế của
   tôi được viết sao cho không cần tới nó.
3. **Khối 4** — năm soạn *Thiền uyển tập anh*. Tôi dùng mốc k. 1337 của
   `reports/ch05-ce08-review.md` §B-13; `content/ch90.md` chỉ ghi "soạn rất muộn", không có năm.
4. **Khối 5** — hai mốc **764** (tiến sĩ) và **780** (khoa chế "Hiền lương phương chính năng
   trực ngôn cực gián"). Chỉ có ở zh.wikipedia, không có trong *Tân Đường thư* quyển 152. Tôi
   **không** đưa hai mốc này vào câu thay thế; chúng chỉ dùng để chứng minh rằng mốc 780 không
   gắn với kỳ thi tiến sĩ. (Kiểm được từ nguồn sơ cấp: 「第進士」, 「以制策異等」,
   「諫議大夫、同中書門下平章事」, 「唐安公主道薨」, 「順宗立…未就官卒」.)
5. **Khối 7** — năm triều đình Carolingian chuyển hẳn về Aachen. Chỉ có mốc "thập niên 790"
   (en.wikipedia, *Palace of Aachen*). Vì vậy đề xuất của tôi là **bỏ tên nơi**, không thay bằng
   một mốc khác.
6. **Khối 8** — việc İhsanoğlu có khoanh huyền thoại Bayt al-Ḥikma vào **thế kỷ 19 – đầu 20** hay
   không. Tôi đọc được mục lục đầy đủ qua Crossref (mười chương, kèm số trang) và nó không chứa
   mốc thế kỷ nào; nội dung sách thì không mở được. Phát hiện NÊN của
   `reports/ch05-ce09-review-c.md` §1 ở điểm này **vẫn đứng**.
7. **Khối 8** — năm xuất bản: xem `[KHÔNG KIỂM ĐƯỢC]` ở mục G phía trên. Trang Routledge dựng
   bằng JavaScript nên không đọc được trường ngày trên chính trang ấy; kết luận **2022** dựa vào
   Crossref và OpenLibrary.

### Ba việc nên làm trước khi áp báo cáo này

1. **Sửa bốn con số vùng cùng một lúc, không sửa lẻ.** Khối 1, tiêu đề + thân khối 2, và khối 3
   phải được viết lại theo cùng một thể thức (bỏ tỉ lệ, hoặc ghi kèm mẫu số), vì chúng được đọc
   cạnh nhau và một nửa sửa sẽ tạo ra mâu thuẫn mới. Quy ước đã có ở dòng 1270; vòng CE10 chỉ áp
   nó cho các khối CE09/CE10 và bỏ sót đúng ba khối này.
2. **Sửa "bốn trường phái luật Sunni" ở cả ba chỗ.** Ngoài khối 6, cụm này còn ở **Bối cảnh nhóm
   CE08** (dòng 413) và khối trần-12 (dòng 1160).
3. **Đóng hai việc còn treo từ vòng CE09.** Hai phát hiện của `reports/ch05-ce09-review-c.md` §1
   với khối Harun chưa được áp sau hai vòng; và khối trần-12 (dòng 1160) vẫn kể Harun là người
   "chắc chắn vào atlas nếu trần là 16" trong khi khối 8 đã bác chính điều đó.
