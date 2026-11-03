# Bình duyệt độc lập · Chỗ trống số 12 của nhóm CE06 (Chapter 5)

**Ngày:** 2026-10-31 · **Người rà:** agent bình duyệt độc lập (không viết Chapter 5)
**Phạm vi:** chấm điểm và xếp hạng ứng viên cho suất cuối cùng của nhóm `CH05-CE06`.

> **Trạng thái file:** viết tăng dần, lưu ngay sau mỗi phần.
> Phần nào chưa có nghĩa là chưa làm tới, không phải đã làm mà bỏ trống.

## 0. Nền đã xác lập trước khi chấm (đọc từ repo, không phải từ web)

**Mười một suất đã chốt của CE06** — và cả mười một đã có trong `data/persons.json`
sau lần build lúc 19:36 hôm nay: Justinianus I, Biển Đức thành Norcia, Khosrow I,
Varāhamihira, Trần-na, Tùy Văn Đế, Trí Di, Bồ-đề-đạt-ma, Kaleb xứ Aksum,
Bumin Qaghan, Bhavavarman I. (`content/ch05.md` mới viết văn xuôi tới mục `-08`;
ba mục `-09/-10/-11` đã vào dữ liệu.)

### 0.1 Hai con số trong đề bài đã lạc hậu — và cả hai đều đổi kết luận

**(1) Đông Nam Á không còn 0,0%.** Đề bài ghi Đông Nam Á 0,0%. Thống kê tính lại từ
`data/persons.json` (208 người atlas chính, 40 người phụ lục CH90 tách riêng):

| Vùng | Số | % |
|---|---|---|
| Trung Đông/Bắc Phi | 69 | 33,2% |
| Châu Âu | 56 | 26,9% |
| Đông Á | 51 | 24,5% |
| Nam Á | 25 | 12,0% |
| Châu Phi hạ Sahara | 4 | 1,9% |
| Trung Á | 1 | 0,5% |
| Châu Mỹ | 1 | 0,5% |
| **Đông Nam Á** | **1** | **0,5%** |
| Châu Đại Dương | 0 | 0,0% |

`CH05-CE06-11` Bhavavarman I (Đông Nam Á) và `CH05-CE06-09` Kaleb (Châu Phi hạ Sahara,
3→4) đã mở xong hai ô mà đề bài còn ghi là trống/mỏng. **Hệ quả cho việc chấm:** sức ép
"phải lấp Đông Nam Á" ở suất 12 đã được chính nhóm CE06 giải quyết. Ô còn thật sự mỏng
nhất mà thế kỷ 6 có thể với tới là **Trung Á (1 người)**. Châu Đại Dương không có ứng
viên khả dĩ ở thế kỷ 6 — không nên giả vờ cân nhắc.

Người Trung Á duy nhất là **Zarathustra** (`CH02-BCE06-09`, nơi ghi "đông Iran hoặc
Trung Á") — ô Trung Á đang được giữ bởi một nhân vật mà chính niên đại lẫn địa bàn còn
tranh cãi (và đang nằm trong danh sách "còn treo" của Ch2). Điều đó làm một ứng viên
Sogdiana **có địa điểm xác định** đáng giá hơn, chứ không kém đi.

**(2) Nghệ thuật/Kiến trúc KHÔNG vắng mặt ở Chapter 5.** Đề bài ghi năm lĩnh vực trắng.
Kiểm lại: `CH05-CE07-12` Pakal có lĩnh vực phụ Nghệ thuật/Kiến trúc. Bốn lĩnh vực thật
sự trắng trong cả Chapter 5 là **Y học, Kỹ thuật/Công nghệ, Văn học, Sử học**.

Phân bố lĩnh vực nhóm CE06 (11 người): Chính trị/Nhà nước 6 · Tôn giáo/Tâm linh 5 ·
Luật 2 · Triết học 2 · Giáo dục 1 · Kinh tế 1 · Toán học 1 · Khoa học tự nhiên 1 ·
Quân sự 1. Nghiêng nặng về Chính trị + Tôn giáo đúng như đề bài nói.

### 0.2 Ba ràng buộc thủ tục tự áp

Không gọi sub-agent · ghi `[KHÔNG KIỂM ĐƯỢC]` kèm lý do thay vì đoán · mọi URL dẫn ra
đều tự mở bằng `curl -A 'history-atlas/0.1 (research)'`, ghi mã HTTP **kèm kích thước
và một mẩu nội dung thật** để loại trường hợp 200-mà-rỗng / 200-mà-trang-chặn-bot.
Không có thông tin cá nhân nào trong header, URL hay payload.

---

*(các phần sau đang được viết)*
## 1. Q-ID Wikidata — tra lại từ đầu, không lấy từ trí nhớ

Phương pháp: gọi `wbgetentities` qua `https://www.wikidata.org/w/api.php`
(User-Agent `history-atlas/0.1 (research)`), đọc trực tiếp P31/P569/P570 kèm **độ chính
xác** (`precision`: 11 = ngày, 9 = năm, 8 = thập niên, 7 = thế kỷ, 6 = thiên niên kỷ),
**rank**, và **số reference** của từng claim. Mọi lệnh gọi đều HTTP 200 với dung lượng
thật ghi ở cột cuối; không có trường hợp 200-mà-rỗng.

| Ứng viên | Q-ID **đã xác nhận** | P31 | P569 (sinh) | P570 (mất) | HTTP / bytes |
|---|---|---|---|---|---|
| Maniakh | **Q12552755** | Q5 (người), **REF=0** | `+0550` **prec 7 = thế kỷ**, REF=1 | **không có** | 200 / 2.919 |
| Imru' al-Qays (nhà thơ) | **Q1051776** | Q5, REF=1 | `+0501` prec 9 = năm, REF=2 | `+0544` prec 9, REF=2 | 200 / 55.246 |
| Mazdak | **Q272300** | Q5, REF=1 | `+0450` **prec 7 = thế kỷ**, REF=1 | `+0529` prec 9 REF=1 **và** `+0531` prec 9 **REF=0** (mâu thuẫn) | 200 / 21.970 |
| Gregory xứ Tours | **Q67841** | Q5, REF=1 | `+0538-11-30` **prec 11 = ngày**, REF=1 | `+0594-12-17` prec 11, REF=1 | 200 / 108.784 |
| Theodora | **Q204843** | Q5, REF=1 | `+0500` prec 9 REF=2 **và** `+0497` prec 9 REF=1 | `+0548-06-28` prec 11 **preferred** REF=1; `+0547` **deprecated** | 200 / 76.136 |
| Boethius | **Q102851** | Q5, REF=1 | `+0480` prec 9 **preferred, REF=9** | `+0524` prec 9 **preferred, REF=3** | 200 / 185.396 |
| John Philoponus | **Q317632** | Q5, **REF=4** | `+0490` prec 9, REF=5 | `+0570` prec 9, REF=3 | 200 / 113.058 |
| Anthemius xứ Tralles | **Q298226** | Q5, REF=1 | `+0474` prec 9, REF=1 | `+0534` prec 9, REF=1 | 200 / 63.861 |
| Alexander xứ Tralles | **Q708684** | Q5, REF=1 | `+0525` prec 9, REF=1 | `+0605` prec 9, REF=1 | 200 / 60.171 |
| Procopius | **Q186153** | Q5, REF=1 | `+0500` **prec 6 = thiên niên kỷ** (!) và `+0500` prec 9 | `+0506` prec 9 (!), `+0558` prec 7, và một claim **deprecated ghi `+2026-03-01`** | 200 / 103.326 |
| Tì-ni-đa-lưu-chi | **Q4111528** | Q5, **REF=0** | `+0550` **prec 7 = thế kỷ**, REF=1 | `+0594` prec 9, REF=1 | 200 / 5.111 |

### 1.1 Ba cái bẫy Q-ID đã bắt được ở vòng này

**(1) Imru' al-Qays có ba thực thể, và hai trong ba là người khác thế kỷ.** Đây đúng
kiểu bẫy Pakal/`Q311215` mà Ghi chú biên tập Chapter 5 đã ghi lại:

- `Q1051776` — **nhà thơ**, desc "Arab king and poet (501–544)". **Đây mới là người cần.**
- `Q1271038` — "Imru' al-Qays ibn 'Amr", **vua Lakhmid thứ hai**, P570 = `+0328-12-07`.
  Đây là nhân vật của **bi ký Namāra**, sống trước nhà thơ gần hai thế kỷ. 14 sitelink,
  tức dễ bị bộ tra tự động trỏ nhầm vào.
- `Q1567831` — "Imru' al-Qays II ibn 'Amr", một vua Lakhmid nữa, desc tiếng Anh ghi sai
  thành "Description of an Arab poet", **không có P569 lẫn P570**.

Ba thực thể này dùng **cùng một chuỗi tiếng Ả Rập** `امرؤ القيس بن عمرو` cho hai trong ba
nhãn. Nếu Chapter 5 viết Imru' al-Qays, Q-ID **phải** là `Q1051776` và Ghi chú biên tập
nên ghi lại hai Q-ID bẫy kia.

**(2) Procopius `Q186153` có dữ liệu rác nặng** — một claim P570 `+2026-03-01` (tức
**tháng 3 năm nay**, rõ ràng là phá hoại hoặc nhập nhầm, đang để rank deprecated), một
P570 `+0506` (ông còn viết sử tới sau 554), và một P569 ở **độ chính xác thiên niên kỷ**.
Cùng loại với ca Pháp Xứng `Q457990` đã ghi trong Ghi chú biên tập. Không được chép.

**(3) `Q12552755` (Maniakh) là một thực thể gần như trống.** P31 = Q5 **không có
reference**; P569 chỉ ở **độ chính xác thế kỷ**; **không có P570, không có P106, không có
P27**; chỉ 3 sitelink (de, kk, uz) và **không có enwiki**. Điều này không chứng minh ông
không có thật — nó phản ánh đúng việc ông chỉ tồn tại trong một nguồn. Nhưng nó có nghĩa
là trường `năm:` của mục này sẽ **không có gì để đối chiếu**, và phải viết dạng
`hoạt động ...` chứ không phải niên đại đời người.

> Ghi chú phương pháp: tôi đọc P31/P569/P570 qua `wbgetentities` chứ không qua HTML trang
> Wikidata, vì API trả về chính các claim kèm `precision`/`rank`/`references` — thứ mà
> trang HTML hiển thị đã làm tròn (prec 7 hiện ra thành "550" trông như một năm).

## 2. Maniakh — kiểm chứng chi tiết

### (a) Niên đại: KHÔNG có mốc tuyệt đối nào cho cá nhân ông

Không có bi ký, tiền đúc, hay văn bản nào do chính ông hoặc người quanh ông để lại.
Toàn bộ khung thời gian của ông là **(SL) suy luận từ một niên đại sự kiện**: sứ đoàn tới
Constantinopolis năm **568**, và chuyến sứ đáp lễ của Zemarchus năm **569**.
`Q12552755` không có P570; P569 chỉ ở **độ chính xác thế kỷ**.

→ Nếu viết, trường `năm:` **bắt buộc** là `hoạt động k. 567–569 CN` (hoặc `hoạt động
k. 560–570 CN`), **không được** viết niên đại đời người. `độ tin cậy niên đại: Thấp`.
Đây không phải thận trọng quá mức: mức Thấp **bỏ qua đối chiếu Wikidata**, mà Wikidata ở
đây không có gì để đối chiếu.

### (b) Nguồn sơ cấp định danh ông: đúng một nguồn, và đó là vấn đề

**Menander Protector**, *History*, fr. 10.1 — bản chuẩn là R. C. Blockley,
*The History of Menander the Guardsman: Introductory Essay, Text, Translation, and
Historiographical Notes* (Liverpool, 1985), **tr. 111–117**. Đoạn tơ lụa bị đốt và sứ giả
bị đầu độc nằm ở **tr. 111–113**; đoạn đối thoại với Justin II ở **tr. 114–117**.
(Chi tiết thư mục này lấy từ thư mục của một bài tạp chí bình duyệt — xem (d) — chứ không
từ trí nhớ.)

Bản thân Menander cũng chỉ còn **dạng mảnh**, bảo tồn qua các hợp tuyển Byzantine muộn.
Nghĩa là: một nhân vật → một nguồn → nguồn ấy lại là mảnh vụn truyền qua trung gian.
Đây là mức bằng chứng **mỏng hơn hẳn** Bumin Qaghan (có niên hiệu Tây Ngụy quy đổi được,
có bi ký Bugut) và Kaleb (có bi ký Geʿez định danh + tiền đúc), hai người đã vào nhóm.

**Một cái bẫy nguồn đã tự kiểm và phải cảnh báo:** PDF
`https://cpb-us-e2.wpmucdn.com/sites.uci.edu/dist/c/347/files/2020/01/Menander6-1.pdf`
(**HTTP 200, 113.536 byte, PDF 14 trang, có chữ thật**) là bản dịch Blockley của Menander
do Sasanika đăng — nguồn có thật, đúng tác giả, đúng bản dịch. Nhưng nó là **fragment
6.1–6.3**, nói về hoà ước Sasanian–La Mã năm 562. Tôi đã rút chữ và `grep`: **không có
một lần nào** các chuỗi `Maniakh`, `Maniach`, `Sogd`, `silk`, `Turk` xuất hiện trong đó.
Đây đúng kiểu lỗi quy tắc 7 — nguồn thật, đúng tác giả, đúng chủ đề chung, **không nói
điều được dẫn**. Nếu Chapter 5 muốn dẫn Menander trực tuyến thì phải tìm đúng fr. 10.1,
không phải PDF này.

### (c) Ba mệnh đề phổ thông SAI hoặc phải rào

**(c1) "Sứ đoàn 568 của Maniakh là lần tiếp xúc đầu tiên giữa Đột Quyết và Byzantium"
— đang bị tranh luận, không được viết như sự kiện.** Li Qiang & Stefanos Kordosis (2018)
lập luận rằng sứ đoàn **Đột Quyết đầu tiên tới Constantinopolis là năm 563**, theo
Theophanes Byzantios và Theophanes Confessor, và rằng "đa số công trình đã xuất bản
nghiêng về mốc 568" là một chỗ bỏ sót của học giới. Họ liệt kê đích danh những người vẫn
giữ mốc 568 (Parker; Sinor; Macartney; Kordosis). Nguyên văn:
*"The first delegation from the Western Türks to Byzantium must be dated to 563 AD."*
→ Mục nào viết "lần đầu tiên" phải rào, hoặc phải nói rõ là **sứ đoàn đầu tiên có mục
đích thương mại/liên minh**, không phải tiếp xúc đầu tiên.

**(c2) "Ba Tư đốt tơ lụa, nên Maniakh đi Constantinopolis" — đúng nhưng bị nén sai.**
Theo Menander, có **hai** sứ đoàn gửi sang Sasanian trước đó: **sứ đoàn thứ nhất** bị đốt
tơ trước mặt người Sogdiana; **sứ đoàn thứ hai** bị **đầu độc**. Gộp hai thành một là sai
chi tiết. Nguyên văn chú thích 39 của bài trên: *"the silk of the first embassy was burnt
in front of the Sogdians, and the envoys of the second embassy were poisoned"*.

**(c3) Mệnh đề hay bị kể thiếu nhất, và nó cắt thẳng vào sức nặng của ông:
chuyến đi về mặt thương mại gần như vô hiệu ngay tại chỗ.** Chính trong buổi tiếp,
Justin II cho họ thấy **Byzantium đã tự nuôi tằm và dệt tơ được rồi** — tức món hàng mà
Maniakh mang đi chào bán đã mất thế độc quyền. Bài trên gọi đó là *"the only dark spot in
the talks"*. Cái còn lại của sứ đoàn 568 là **liên minh chống Sasanian và vấn đề Avar**,
tức một kết quả **ngoại giao**, không phải một kết quả **thương mại**.
Hệ quả cho việc chấm: luận điểm hấp dẫn nhất về Maniakh ("người mở tuyến tơ lụa Bắc, nối
thảo nguyên với Địa Trung Hải") là luận điểm **yếu nhất** về mặt nguồn.

**(c4) Khả hãn sai người.** Người cử ông là **Sizaboulos/Silziboulos**, thường đồng nhất
với **Istämi**, em của Bumin — **không phải Bumin**. Mục `CH05-CE06-10` Bumin Qaghan đã có
trong nhóm; nếu viết Maniakh phải tránh để hai mục chồng nhân vật.

### (d) Nguồn thứ cấp — tự mở kiểm

1. **Li Qiang & Stefanos Kordosis, "The Geopolitics on the Silk Road: Resurveying the
   Relationship of the Western Türks with Byzantium through Their Diplomatic
   Communications", *medieval worlds* No. 8 (2018), tr. 109–125.**
   `https://medievalworlds.net/0xc1aa5572%200x003a16af.pdf` — **HTTP 200, 546.249 byte,
   PDF 17 trang, 60.053 ký tự chữ thật rút được.** Tôi đã rút toàn văn và đọc các đoạn
   nói về Maniakh (dòng 150–173 và 279–335 của bản rút chữ). Mọi trích dẫn (c1)(c2)(c3)
   ở trên lấy trực tiếp từ đây. Tạp chí truy cập mở của Viện Hàn lâm Khoa học Áo.
   **Cảnh báo dùng nguồn (quy tắc 7):** luận điểm trung tâm của bài này là các siêu cường
   định cư **thao túng** người du mục, những người *"were only treated as pieces on a
   chessboard"*. Nó **không** đỡ cho một câu kiểu "Maniakh là tác nhân chủ động định hình
   địa chính trị Á–Âu"; dẫn nó theo hướng ấy là dùng ngược.

2. **R. C. Blockley (ed./trans.), *The History of Menander the Guardsman* (Liverpool,
   1985)** — chi tiết thư mục xác nhận từ thư mục bài (1). **[KHÔNG KIỂM ĐƯỢC toàn văn]**:
   tôi không mở được bản scan hợp pháp của fr. 10.1; số trang 111–117 là lấy từ chú thích
   của bài bình duyệt (1), không phải tự đếm trang.

3. **Étienne de la Vaissière, *Sogdian Traders: A History* (Leiden: Brill, 2005)** —
   là chuyên khảo chuẩn về đề tài, có trong thư mục của (1). Bài Encyclopaedia Iranica
   "Sogdian Trade" của cùng tác giả: `https://www.iranicaonline.org/articles/sogdian-trade/`
   — **HTTP 403, 5.491 byte, nội dung trả về là trang chặn bot Cloudflare
   ("Just a moment…"), không phải bài viết.** **[KHÔNG KIỂM ĐƯỢC]** — đây đúng loại ca
   mà vòng trước gặp. **Không được dẫn URL này như đã kiểm.**

### (e) Q-ID

**`Q12552755`** — đã xác nhận ở §1: P31 = Q5 (người) **không reference**, P569 `+0550`
**độ chính xác thế kỷ**, **không có P570/P106/P27**, 3 sitelink (de/kk/uz), **không có
enwiki**. Tìm `Maniah` và `Sogdian Maniakh` trên Wikidata trả về **không có** thực thể
nào khác dễ nhầm (kết quả là một chính trị gia Indonesia và một cầu thủ bóng rổ New
Zealand) — tức ít nhất **không có bẫy trùng tên**.

### Vùng — trả lời thẳng câu hỏi của đề bài

**Xếp Trung Á được, một cách trung thực, không phải bẻ cong.** Menander gọi ông là thủ
lĩnh của người Sogdiana; Sogdiana = vành đai Transoxiana, đúng **nguyên văn** phạm vi mà
`CONTRIBUTING.md` dòng 70 nói "Trung Á" trên thực tế còn dùng cho. Không cần viện tới
ngoại lệ nào, không cần đổi nghĩa trường `nơi:`.
Đây là **điểm cộng thật** và là điểm mạnh nhất của ứng viên này.

## 3. Hai ứng viên tôi BỔ SUNG và xếp trên cả năm người trong đề bài

(Các ứng viên bổ sung còn lại — chín người nữa — ở §5.)

Đề bài nói rõ danh sách năm người là điểm xuất phát chứ không phải giới hạn. Sau khi rà
thế kỷ 6 toàn cầu, tôi thấy **hai người bị bỏ sót mà sức nặng ảnh hưởng dài hạn vượt hẳn
cả năm ứng viên được đề xuất**. Một trong hai, atlas **đã đang dựa vào** để giải thích
một mục khác mà không cho ông mục riêng.

### 3.1 Boethius — và một bằng chứng nội tại rằng ông đang bị thiếu

`grep` toàn repo: tên Boethius **đã xuất hiện ba lần** trong atlas, lần nào cũng ở vai
**cơ chế truyền** cho người khác:
- `content/ch04.md` mục Porphyry: *"Boethius dịch sang Latinh và từ đó nó thành sách vỡ
  lòng logic bắt buộc ở châu Âu lẫn thế giới Hồi giáo suốt hơn một nghìn năm."*
- cùng mục, dòng liên kết: *"Logic kinh viện Latinh và Hồi giáo **qua Boethius**"*.
- `reports/rebalance-ch04-a.md`: *"(d) 4 — **qua Boethius**, chính văn bản này quyết định
  hình dạng của logic kinh viện."*

Tức atlas đã **ba lần** dùng ông làm bản lề nhân quả, và **chưa lần nào** cho ông một
mục. Ông cũng **chưa từng** bị nêu là ứng viên bị loại ở bất kỳ đâu — nên đây là một
khoảng trống chưa được quyết, không phải một quyết định đã có.

**(a) Niên đại — và mệnh đề phổ thông đầu tiên bị bác.**
Không có mốc tuyệt đối theo nghĩa bi ký. Khung đời ông neo vào **chức vụ** (consul 510,
magister officiorum đầu những năm 520) và vào vụ xử tử dưới Theodoric. SEP (bản sửa
**14-10-2026**) ghi: *"born: circa 475–7 C.E., died: 526? C.E."* và *"imprisoned and
(probably in 526) executed"*.
→ **Niên đại "480–524" rất phổ biến là niên đại quy ước, không chắc.** Wikidata
`Q102851` để P569 `+0480` (preferred, **9 reference**) và P570 `+0524` (preferred, 3 ref),
**lệch với SEP cả hai đầu**. Đây đúng ca mà `CONTRIBUTING.md` quy tắc 4 cảnh báo: khớp
Wikidata không đồng nghĩa với đúng.
→ Khuyến nghị: `năm: k. 477 – k. 526 CN`, `độ tin cậy niên đại: Trung bình` (dung sai
±25 năm, nuốt được cả 480/524 lẫn 477/526, nên lint sẽ sạch mà không phải chọn phe).

**(b) Nguồn sơ cấp định danh.** Mạnh khác thường so với mọi ứng viên còn lại ở đây:
**chính các tác phẩm của ông còn nguyên** — hai bình luận *Isagoge*, bình luận
*Categoriae*, hai bình luận *De interpretatione*, các chuyên luận về tam đoạn luận giả
thiết và về *De topicis differentiis*, bốn *Opuscula sacra*, *De institutione arithmetica*,
*De institutione musica*, và *De consolatione philosophiae*. Thêm *Variae* của Cassiodorus
(đương thời, cùng triều) và *Anonymus Valesianus* cho vụ án.
Đây là **loại bằng chứng mà nhóm CE06 đang thiếu**: tám trong mười một người hiện có đều
phải rào niên đại hoặc rào quy thuộc; Boethius thì không.

**(c) Mệnh đề phải rào.**
- "480–524" — xem (a).
- "Boethius dịch toàn bộ Aristotle sang Latinh" — **sai**. Ông dịch *Organon*; SEP ghi
  rõ bản dịch *Posterior Analytics* của ông **đã mất**, và kế hoạch dịch toàn bộ
  Plato + Aristotle thì không hoàn thành.
- "Consolatio là tác phẩm Kitô giáo" — phải rào: SEP ghi treatise III của *Opuscula* là
  *"a brief, not specifically Christian philosophical treatise"*, và chính *Consolatio*
  nổi tiếng vì **không** viện dẫn giáo lý Kitô. Đây là tranh luận học thuật thật, không
  nên khép.
- "Ông bị giết vì đức tin Công giáo chống Arian" — là cách đọc hagiographic muộn; SEP ghi
  nguyên nhân là **cáo buộc phản nghịch và hành nghề ma thuật**, có thể vì ông đụng vào
  tham nhũng trong triều.

**(d) Nguồn thứ cấp — tự mở kiểm.**
1. **SEP, "Anicius Manlius Severinus Boethius"** (John Marenbon), bản sửa 14-10-2026 —
   `https://plato.stanford.edu/entries/boethius/` — **HTTP 200, 90.315 byte, rút được
   70.352 ký tự chữ thật**, `<title>` = "Anicius Manlius Severinus Boethius (Stanford
   Encyclopedia of Philosophy)". Tôi đã đọc §1 (Life and Works) và §8 (Influence and
   Importance). Trích nguyên văn §8: *"Along with Augustine and Aristotle, he is the
   fundamental philosophical and theological author in the Latin tradition."* và
   *"In logic, Boethius's translations of Aristotle and Porphyry (except for that of the
   Posterior Analytics, which was lost) remained standard throughout the Middle Ages."*
   và, về *Consolatio*: *"translations, not merely into almost every medieval vernacular,
   but also into Greek and even Hebrew"* — trong đó có **Jean de Meun** và **Chaucer**.
2. **John Marenbon, *Boethius* (Oxford University Press, 2003)** và **John Magee (2024)** —
   cả hai nằm trong thư mục bài SEP trên. **[KHÔNG KIỂM ĐƯỢC toàn văn]**: tôi không mở
   được bản sách; chỉ xác nhận chúng được SEP dẫn, không xác nhận nội dung cụ thể.
3. SEP có bài riêng `https://plato.stanford.edu/entries/philoponus/` — **HTTP 200,
   75.276 byte** (xem §3.2). Đối chiếu: `https://plato.stanford.edu/entries/gregory-tours/`
   — **HTTP 404, 9.908 byte, `<title>` = "Document Not Found"**. Ghi lại để chứng minh
   rằng hai mã 200 ở trên là 200 thật, không phải 200-trả-trang-rỗng.

**(e) Q-ID: `Q102851`** — đã xác nhận ở §1 (P31 = Q5; P569/P570 preferred, nhiều
reference nhất trong cả bảng). Không có thực thể trùng tên gây nhầm.

**Vùng / lĩnh vực.** `vùng: Châu Âu` (Rome và Pavia — không cần ngoại lệ nào).
`lĩnh vực: Triết học, Văn học` — **Văn học là một trong bốn lĩnh vực đang trắng trong cả
Chapter 5**, và *Consolatio* là prosimetrum, tức lựa chọn này không phải nhét cho đủ ô.

### 3.2 John Philoponus — mạnh về (a)(b)(c)(d), yếu đúng ở hai tiêu chí phụ

**(a)** `k. 490 – k. 570 CN`; mốc neo chắc nhất là **năm 517**, niên đại ông ghi trong
bình luận *Physica* (mốc nội tại của văn bản, không phải quy ước) — *tôi lấy mốc này từ
hiểu biết chung và* **[KHÔNG KIỂM ĐƯỢC]** *trong trang SEP đã mở; nếu viết mục phải kiểm
lại*. Wikidata `Q317632` ghi 490–570 với **REF=5 / REF=3**, và P31 có **4 reference** —
thực thể sạch nhất trong cả bảng §1.

**(b)** Chính các bình luận của ông còn (Physica, De anima, Meteorologica, Analytica…),
cộng *De aeternitate mundi contra Proclum* (529) và *contra Aristotelem*. Một phần chỉ
còn qua **bản Syriac và Ả Rập** — chi tiết này tự nó là luận điểm.

**(c)** Mệnh đề phải rào: "Philoponus phát minh thuyết impetus" — SEP nói ông
*"initiated and in fact anticipated the eventual liberation of natural philosophy from
the straitjacket of Aristotelianism"*, chứ không trao cho ông một phát minh trọn gói.
Mệnh đề hay bị bỏ: ông bị **kết án dị giáo sau khi chết, năm 680–81**, vì cách hiểu
tam vị nhất thể theo lối Aristotle (bị đọc thành "ba thần"). Chính án đó là lý do tên ông
bị xoá ở phía Hy Lạp mà **còn nguyên ở phía Syriac và Ả Rập**.

**(d)** SEP, "John Philoponus" — `https://plato.stanford.edu/entries/philoponus/` —
**HTTP 200, 75.276 byte, rút được 55.340 ký tự chữ thật**, `<title>` = "John Philoponus
(Stanford Encyclopedia of Philosophy)". Nguyên văn: *"Philoponus' works were translated
into Arabic, Latin, and Syriac, and he influenced later thinkers such as Bonaventure,
Gersonides, Buridan, Oresme, and Galileo."*

**(e) Q-ID `Q317632`** — đã xác nhận ở §1.

**Vì sao ông vẫn không phải khuyến nghị của tôi:** `vùng:` của ông là
**Trung Đông/Bắc Phi** (Alexandria — theo đúng tiền lệ Diophantus đã khai báo ở
`CONTRIBUTING.md` quy tắc vùng mục 2, Alexandria **không** hưởng ngoại lệ Tiểu Á).
Đó là vùng **đang nặng nhất atlas (33,2%)**. Và `lĩnh vực:` của ông (Triết học +
Khoa học tự nhiên) **không lấp ô trống nào** của Chapter 5. Ông thua Boethius ở tiêu chí
3 và 4 trong khi tiêu chí 1 thì ngang ngửa chứ không vượt.

## 4. Bốn ứng viên còn lại trong đề bài

### 4.0 Năm cái bẫy URL mới bắt được trong vòng này

Đề bài nói vòng trước gặp bốn URL "200 mà rỗng hoặc là trang chặn bot". Vòng này tôi gặp
thêm **năm** kiểu, ghi lại để lần sau khỏi mất công:

| URL | Mã | Kích thước | Thực tế |
|---|---|---|---|
| `https://ctext.org/wen-xuan` | **200** | 2.781 B | *"Checking the security of your connection…"* — **chặn bot trả 200** |
| `https://www.jstor.org/stable/596183` | **200** | 3.038 B | `<title>` = **"Client Challenge"** — chặn bot trả 200 |
| `https://referenceworks.brill.com/display/entries/EI2O/COM-23497.xml` | **202** | **0 B** | thân trả về rỗng tuyệt đối |
| `https://en.wikisource.org/wiki/The_Moallakat/Poem_of_Imriu-l-Quais` | **404** | 42.553 B | 404 **nhưng `<title>` trông như trang thật** — nếu chỉ nhìn title thì tưởng đã kiểm |
| `https://www.britannica.com/biography/Saint-Gregory-of-Tours`, `https://www.iranicaonline.org/articles/mazdak` | **403** | 5.536 / 5.467 B | Cloudflare *"Just a moment…"* |

Bài học thao tác: **mã HTTP một mình vô dụng, `<title>` một mình cũng vô dụng.** Phải có
cả ba — mã, số byte, và số ký tự chữ rút được sau khi bỏ thẻ.

### 4.1 Imru' al-Qays — hấp dẫn về lĩnh vực, nhưng hỏng ở tiêu chí 2

**(a) Niên đại.** Wikidata `Q1051776` ghi sinh `+0501`, mất `+0544`, cả hai prec 9, REF=2.
**Không có mốc tuyệt đối nào cho nhà thơ này.** Toàn bộ khung niên đại đến từ *akhbār* Ả
Rập thế kỷ 8–10, tức sau 200–400 năm → **(QƯ) quy ước**, không phải (BK).
Mốc tuyệt đối duy nhất mang tên "Imru' al-Qays" trong thế giới Ả Rập tiền Hồi giáo là
**bi ký Namāra, 328 CN** — và đó là **người khác, sớm hơn gần hai thế kỷ**. Xem §1.1 bẫy
số 1: ba thực thể Wikidata khác nhau cùng tên.

**(b) Nguồn sơ cấp.** Không có nguồn đương thời. Thơ ông đến qua *Muʿallaqāt* và
*Mufaḍḍaliyyāt*, do các *rāwī* thế kỷ 8 truyền; tiểu sử đến qua Ibn Qutayba và
*Kitāb al-Aghānī* (thế kỷ 9–10). **[KHÔNG KIỂM ĐƯỢC]** — tôi không mở được bản văn nào
trong số này trong vòng kiểm này.

**(c) Mệnh đề phải bác.** Hai cái, và cái thứ hai là chí mạng:
1. Đồng nhất ông với vua Imru' al-Qays của bi ký Namāra — **sai**, lệch ~175 năm.
2. "Thơ tiền Hồi giáo là bằng chứng đương thời về Ả Rập thế kỷ 6" — **phải rào nặng**.
   Tính xác thực của toàn bộ kho thơ *jāhilī* đã bị D. S. Margoliouth (1925) và
   Ṭāhā Ḥusayn (*Fī al-Shiʿr al-Jāhilī*, 1926) công kích tận gốc, và tranh luận đó
   **chưa khép**. Đây đúng là tình huống mà đề bài bảo phải phạt nặng: mệnh đề trung tâm
   đang bị chuyên gia hàng đầu bác.

**(d) Nguồn thứ cấp.** **[KHÔNG KIỂM ĐƯỢC]** — tôi đã thử và **thất bại cả bốn lần**:
Wikisource 404; JSTOR 200-giả (Client Challenge); Brill *Encyclopaedia of Islam* HTTP 202
rỗng 0 byte; Britannica 403. **Không được dẫn bất kỳ URL nào trong số này như đã kiểm.**
Việc không kiểm được nguồn thứ cấp tự nó là một điểm trừ: mục viết ra sẽ không có chân.

**(e) Q-ID `Q1051776`** — đã xác nhận ở §1, kèm cảnh báo ba-thực-thể.

### 4.2 Mazdak — vướng cả tiêu chí 2 lẫn tiêu chí 5

**(a)** `Q272300`: sinh `+0450` **prec 7 = thế kỷ** (tức Wikidata chỉ biết "thế kỷ 5"),
REF=1. Mất: **hai claim mâu thuẫn** — `+0529` REF=1 và `+0531` **REF=0**. Niên đại tử
hình Mazdak là một trong những điểm tranh cãi dai nhất của sử Sasanid.
**Độ tin cậy niên đại tốt nhất có thể viết: Thấp.**

**(b)** Không nguồn đương thời Ba Tư. Thông tin đến qua Procopius (Hy Lạp, đương thời
nhưng không nêu tên Mazdak ở đoạn liên quan), các sử gia Ả Rập–Ba Tư muộn (Ṭabarī,
*Shāhnāma*, *Siyāsatnāma* của Niẓām al-Mulk thế kỷ 11), và nguồn Syriac. Toàn bộ là
nguồn **thù địch**: không có một dòng nào do phía Mazdak viết ra còn lại.

**(c)** Mệnh đề phổ thông "Mazdak chủ trương cộng sản nguyên thuỷ, chia chung của cải và
vợ" là **mệnh đề của kẻ thù ông**, lặp lại từ *Siyāsatnāma* — một tác phẩm viết 500 năm
sau nhằm bôi nhọ phái Ismāʿīlī đương thời bằng cách gán cho họ tổ tiên Mazdak. Nghiên cứu
hiện đại (Crone, "Kavād's Heresy and Mazdak's Revolt", *Iran* 29, 1991) đọc lại phong
trào theo hướng khác hẳn. **[KHÔNG KIỂM ĐƯỢC]**: tôi *không* mở được bài Crone trong vòng
này (JSTOR chặn bot, xem §4.0); tôi chỉ nêu nó như một hướng cần kiểm, **không** dẫn nó
như đã kiểm.

**(d)** **[KHÔNG KIỂM ĐƯỢC]** — Encyclopaedia Iranica `articles/mazdak` trả **HTTP 403,
5.467 byte, Cloudflare "Just a moment…"**. Không có nguồn thứ cấp nào được mở thành công.

**(e)** `Q272300` — xác nhận ở §1.

**Tiêu chí 5 (chồng lấn).** Mazdak đã được nêu đích danh **ngay trong mục Khosrow I hiện
có** như đối thủ bị đàn áp. Thêm mục riêng cho ông **không mang lại ý mới**, chỉ thêm một
nhân vật trong cùng một cảnh — trừ khi ý mới là "phong trào tôn giáo–xã hội bình dân",
mà muốn viết ý đó thì phải viết trên một nền bằng chứng mà §(b) vừa cho thấy là không có.

### 4.3 Gregory xứ Tours — ứng viên MẠNH NHẤT trong bốn người này, và lý do thật sự đáng kể

Đây là ứng viên duy nhất trong đề bài **lấp đúng một trong bốn ô trống thật của Chapter 5**.

**(a) Niên đại — tốt bất thường.** `Q67841`: sinh `+0538-11-30` **prec 11 = ngày**, REF=1;
mất `+0594-12-17` **prec 11 = ngày**, REF=1. Độ chính xác ngày ở thế kỷ 6 là hiếm, và ở
đây nó có cơ sở: ông **tự ghi niên đại trong chính tác phẩm của mình** (Book X kết ở năm
thứ 21 giám mục của ông). Lưu ý một lệch nhỏ cần rào: bản Fordham ghi tiêu đề
**"Gregory of Tours (539-594)"**, lệch một năm với Wikidata ở đầu sinh.
→ `năm: 538–594 CN` hoặc `k. 539–594`, `độ tin cậy niên đại: Cao` (dung sai ±5 nuốt được
lệch 538/539).

**(b) Nguồn sơ cấp — ông CHÍNH LÀ nguồn sơ cấp.** *Decem Libri Historiarum* còn nguyên
mười quyển, cộng *Liber in gloria martyrum*, *Liber vitae patrum*, *De virtutibus sancti
Martini*. Đây là thế mạnh gần như độc nhất: với hầu hết ứng viên khác ta phải hỏi "ai
nhắc đến người này?", còn ở đây câu hỏi đảo lại — **phần lớn những gì ta biết về Gaul thế
kỷ 6 là biết qua ông.**

**(c) Mệnh đề phải bác / rào.**
- "Ông chép sử trung lập" — **sai**. *Historiae* là tác phẩm luận chiến thần học: ông mở
  bằng tuyên xưng đức tin Nicaea và dựng toàn bộ trần thuật quanh tương phản
  Công giáo / Arian. Đọc nó như biên niên khách quan là lỗi.
- Tên quen "History of the Franks" là **tên do người sau đặt**; nhan đề của chính ông là
  *Decem Libri Historiarum* ("Mười quyển Sử"), và chủ đề không chỉ là người Frank. Đây là
  đúng kiểu lỗi mà quy tắc 7 nói tới: dẫn đúng sách, sai luận đề của sách.
- Chuyện Clovis rửa tội "năm 496" là **suy luận hiện đại (SL)** dựng từ trần thuật của
  chính Gregory, không phải mốc tuyệt đối; niên đại này vẫn đang tranh luận (496 / 499 /
  508).

**(d) Nguồn — tự mở kiểm.**
1. **Internet Medieval Sourcebook, Gregory of Tours, *History of the Franks*, Books I–X**
   (bản dịch Ernest Brehaut) — `https://sourcebooks.fordham.edu/basis/gregory-hist.asp` —
   **HTTP 200, 783.737 byte, rút được 578.087 ký tự chữ thật**; đếm trong thân bài:
   "Gregory" 132 lần, "Tours" 135, "Clovis" 85, "Franks" 90; có mục lục Book I–X.
   Đây là **nguồn sơ cấp (bản dịch)**, tôi ghi đúng như vậy, không nâng nó thành nguồn
   thứ cấp.
2. **[KHÔNG KIỂM ĐƯỢC] — không có bài SEP.** `https://plato.stanford.edu/entries/gregory-tours/`
   trả **HTTP 404, 9.908 byte, `<title>` = "Document Not Found"**. Britannica trả
   **403**. Tức: ứng viên này **chưa có nguồn thứ cấp nào được tôi mở và xác nhận**.
   Muốn đưa ông vào atlas thì phải làm thêm một vòng tìm nguồn thứ cấp mở được.

**(e) Q-ID `Q67841`** — xác nhận ở §1. Không trùng tên nguy hiểm (Gregory I là `Q42827`,
Gregory Nazianzen và Gregory xứ Nyssa đều là thực thể khác; đây đúng là một họ tên mà
quy tắc 8 cảnh báo, nên tôi ghi rõ: **Q67841 ≠ Q42827**).

**Vùng / lĩnh vực.** `vùng: Châu Âu` (Tours, Gaul). `lĩnh vực: Sử học, Tôn giáo` —
**Sử học là một trong bốn ô trống thật của Chapter 5.**

### 4.4 Theodora — bị tiêu chí 5 chặn, không phải tiêu chí 1

**(a)** `Q204843`: sinh **hai claim mâu thuẫn** `+0500` (REF=2) và `+0497` (REF=1);
mất `+0548-06-28` prec 11 **preferred** REF=1, cộng một claim `+0547` **deprecated**.
Mốc mất 28-6-548 là mốc tốt (được chép đương thời). → `độ tin cậy niên đại: Trung bình`.

**(b)** Rất mạnh: **bi ký và hình ảnh đương thời định danh bà** — khảm San Vitale
(Ravenna, k. 547) có tên bà; luật của Justinianus nêu tên bà (*Novellae*); Procopius nêu
tên bà ở cả ba tác phẩm; John xứ Ephesus (Syriac, đương thời, phía Miaphysite) nêu tên bà
và quan trọng là nêu **thiện cảm**, đối trọng với Procopius.

**(c) Mệnh đề phải bác.** Gần như toàn bộ chân dung phổ thông về bà — xuất thân kỹ nữ,
các giai thoại tình dục — đến từ **một nguồn duy nhất**, *Anekdota* (*Secret History*)
của Procopius, một tác phẩm bôi nhọ. Tôi đã mở và xác nhận văn bản:
`https://sourcebooks.fordham.edu/basis/procop-anec.asp` — **HTTP 200, 305.464 byte,
226.445 ký tự chữ thật**, trong đó "Theodora" xuất hiện **110 lần**, "Justinian" 117.
Tức nguồn có thật, đúng người, đúng chủ đề — **nhưng chính vì nó là nguồn duy nhất nên
không được dùng nó làm bằng chứng cho những điều chỉ nó nói.** Câu nổi tiếng
"Hoàng bào là tấm vải liệm đẹp" trong bạo loạn Nika cũng là **Procopius thuật lại
(*Wars* I.24)**, không phải biên bản.

**(d)** Fordham *Anekdota* (xác nhận trên) là **nguồn sơ cấp**. Nguồn thứ cấp:
**[KHÔNG KIỂM ĐƯỢC]** trong vòng này.

**(e) Q-ID `Q204843`** — xác nhận ở §1.

**Tiêu chí 5 — chỗ bà gãy.** Theodora đã được nêu đích danh **trong chính mục
Justinianus I** hiện có. Toàn bộ sân khấu của bà — Nika 532, San Vitale, chính sách
Miaphysite — **là sân khấu của mục đã có**. Ý mới khả dĩ duy nhất là "quyền lực nữ giới
trong triều đình Byzantine", một ý thật; nhưng để viết nó phải dựa vào Procopius, tức
dựa vào đúng nguồn mà §(c) vừa nói là không dùng được cho việc đó. **Đây là thế kẹt
thật, không phải tôi dựng ra để loại bà.**

## 5. Các ứng viên khác tôi đã rà và loại — kèm lý do kiểm được

Tất cả Q-ID dưới đây đều do tôi tự tra bằng `wbsearchentities` + `wbgetentities` trong
vòng này, **không lấy từ trí nhớ**. Hai tra cứu bị mất vì HTTP 429 ở vòng trước
(Gregory I và Li Chun) đã được **chạy lại thành công**, kết quả ở đây.

### 5.1 Grêgôriô I (Gregory Cả) — `Q42827`

| | |
|---|---|
| P31 | Q5, **REF=3** (P1047 Catholic-Hierarchy, P5587, P7796, P248) |
| P569 | **hai claim**: `+0540-11-30` **prec 9** (chuỗi có ngày nhưng độ chính xác chỉ là NĂM — bẫy đọc) và `+0540` prec 9 |
| P570 | `+0604-03-12` **prec 11 = ngày, REF=3** |

Dữ liệu sạch, niên đại chắc. **Nhưng ông bị loại vì hai lý do, cả hai đều về quy tắc
sắp xếp của chính atlas:**
1. **§3/§5.3 bảo xếp theo giai đoạn ảnh hưởng chính, không theo năm sinh/mất.** Giai đoạn
   ảnh hưởng của ông là **giáo hoàng 590–604**, và sức nặng lịch sử (truyền giáo Anh 597,
   *Regula pastoralis*, cải tổ hành chính toà thánh) **nằm gần như trọn ở bản lề sang thế
   kỷ 7**. Theo đúng tiền lệ Āryabhaṭa mà atlas đã dùng, ông thuộc về **CE07**, không
   phải CE06. Đặt ông vào CE06 là lách luật.
2. Tiêu chí 5: ông là **nguồn chính** cho tiểu sử Biển Đức thành Norcia (*Dialogi* II) —
   mà Biển Đức đã có mục `CH05-CE06-02`. Và lĩnh vực của ông (Tôn giáo + Chính trị) là
   **đúng hai ô đã nặng nhất CE06** (Tôn giáo 5, Chính trị 6).

**Khuyến nghị riêng: nên xét ông nghiêm túc cho nhóm CE07 ở vòng sau**, nếu CE07 còn chỗ.

### 5.2 Tiêu Thống (Xiao Tong) — `Q1039198`

Bẫy đã bắt: `wbsearchentities "Xiao Tong"` trả về **sáu** kết quả, trong đó **hai nhà
nghiên cứu đương đại có ORCID** (`Q101225322`, `Q89008969`) và hai nhân vật CBDB khác.
Người đúng là **`Q1039198`** — "Xiao Tong, Crown Prince of Liang Dynasty" / vi "Tiêu Thống".

| | |
|---|---|
| P31 | Q5, REF=1 |
| P569 | `+0501` prec 9, REF=1 |
| P570 | `+0531-05-30` prec 11, **REF=1 nhưng reference chỉ là P143 = "nhập từ Wikipedia"** → không phải reference thật |

**Điểm mạnh thật:** *Văn tuyển* (文選, *Wen xuan*) là **tuyển tập văn học có ảnh hưởng dài
nhất Đông Á** — nền của chương trình khoa cử, và là sách giáo khoa văn học ở Nhật Bản và
Triều Tiên hàng thế kỷ. Lấp ô **Văn học** (một trong bốn ô trống), vùng Đông Á, niên đại
501–531 **nằm trọn trong CE06**. Trên giấy đây là ứng viên tốt.

**Vì sao vẫn xếp dưới Boethius:**
- Tiêu chí 1: ảnh hưởng của *Văn tuyển* rất sâu nhưng **giới hạn trong một vùng văn hoá**;
  ảnh hưởng của Boethius trải qua Latinh, Hy Lạp, Hebrew và mọi ngôn ngữ bản địa châu Âu.
- Tiêu chí 3 (tính nguyên bản): ông là **người biên tuyển**, không phải tác giả của phần
  lớn nội dung. Counterfactual yếu hơn: nếu không có Tiêu Thống, một tuyển tập tương
  đương nhiều khả năng vẫn ra đời ở triều Lương.
- Tiêu chí 3 (vùng): Đông Á đã có **3/11** người trong CE06.
- **[KHÔNG KIỂM ĐƯỢC] nguồn thứ cấp**: `https://ctext.org/wen-xuan` trả **HTTP 200 nhưng
  chỉ 2.781 byte và là trang chặn bot** (§4.0). Không mở được nguồn nào khác.

### 5.3 Dionysius Exiguus — `Q274091`

Ảnh hưởng dài hạn có lẽ là **lớn nhất trong toàn bộ danh sách này**: hệ đếm năm
*Anno Domini* ông dựng năm 525 hiện là cách đánh số năm mặc định của gần như cả hành
tinh. Nhưng dữ liệu không đỡ nổi:

| | |
|---|---|
| P31 | Q5, **REF=1 và reference là P143 = nhập từ Wikipedia** → thực tế **không có reference** |
| P569 | `+0475` prec 9, REF=1 (cũng P143) |
| P570 | `+0550` **rank = deprecated**; `+0544` prec 9 REF=1 |

Thêm bẫy: `wbsearchentities "Dionysius Exiguus"` trả **`Q103850224` ("encyclopedia
article")** và **`Q136765646` / `Q115468674`** (các ấn bản sách) — ba thực thể **không
phải người** nằm ngay cạnh. Lấy nhầm là chuyện rất dễ.

**Loại vì:** `độ tin cậy niên đại` chỉ có thể là **Thấp**; mệnh đề trung tâm phải rào
nặng (tính toán của ông **sai** — Chúa Giê-su gần như chắc chắn sinh trước năm 1 CN vài
năm; và *Anno Domini* chỉ phổ biến sau khi **Bede** dùng nó hai thế kỷ sau, nên
counterfactual thật sự thuộc về Bede nhiều hơn). Đây là ứng viên tôi **tiếc nhất**, và
tôi ghi rõ ở đây để vòng sau có người tìm được nguồn tốt thì xét lại.

### 5.4 Lý Xuân (Li Chun), người dựng cầu An Tế — **LOẠI DỨT KHOÁT: không tồn tại Q-ID**

Đây là phát hiện đáng kể nhất của mục 5. Tôi tra `wbsearchentities`:
- `"Li Chun engineer"` → **HTTP 200, 68 byte, 0 kết quả**.
- `"Li Chun"` → 6 kết quả: một hoàng đế Đường (`Q9761`), một quan nhà Minh (`Q11178813`),
  và ba mục CBDB — **không có người kỹ sư nào**.
- `"Anji Bridge"` / `"Zhaozhou Bridge"` → chỉ có **`Q551446`**, là **cây cầu**, không
  phải người.
- Tôi đọc tiếp claim của `Q551446`: **không có P84 (kiến trúc sư), không có P170
  (người tạo)**. Trường duy nhất liên quan là **P571 (khởi dựng) = `+0606`, REF=0**.

Hai hệ quả: (1) `CONTRIBUTING.md` quy tắc 1 đòi Q-ID — **không có Q-ID thì không viết
được mục**; (2) kể cả nếu có, niên đại Wikidata **606** đẩy cầu sang **thế kỷ 7**, ngoài
CE06. Ô **Kỹ thuật/Công nghệ** của Chapter 5 vẫn trống, nhưng **không lấp được bằng
người này**.

### 5.5 Anthemius xứ Tralles `Q298226` / Alexander xứ Tralles `Q708684`

Hai anh em, hai ô trống hấp dẫn: Anthemius lấp **Kỹ thuật/Công nghệ** +
**Nghệ thuật/Kiến trúc** (Hagia Sophia, 532–537), Alexander lấp **Y học**
(*Therapeutica*, được dịch sang Latinh, Ả Rập và Hebrew).

Cả hai đều **Q5, REF=1, prec 9** — dữ liệu mỏng nhưng không mâu thuẫn.

**Loại vì tiêu chí 5 và 3:**
- Anthemius **nằm trọn trong cảnh của Justinianus** (ông được Justinianus bổ nhiệm; công
  trình là công trình của Justinianus). Mục Justinianus hiện có đã nói về Hagia Sophia.
  Đây đúng là "thêm một nhân vật trong cùng một cảnh".
- Alexander thoát được chồng lấn và **thật sự lấp ô Y học**, nên ông là ứng viên
  nghiêm túc. Nhưng: `vùng:` của ông là **Trung Đông/Bắc Phi hoặc Châu Âu tuỳ cách đọc**
  (sinh ở Tralles — Tiểu Á nói tiếng Hy Lạp, tức **ngoại lệ đã khai báo → Châu Âu**;
  hoạt động chủ yếu ở **Rome** → cũng Châu Âu). Và tiêu chí 1 của ông yếu hơn hẳn: ông là
  một thầy thuốc giỏi có sách được dùng lâu, không phải người đổi hình dạng một ngành.
  **[KHÔNG KIỂM ĐƯỢC] nguồn thứ cấp** cho cả hai.
- Nếu ban biên tập muốn **ưu tiên lấp ô Y học hơn ô Văn học**, Alexander xứ Tralles là
  lựa chọn đúng, và tôi xếp ông **hạng 4** trong bảng §6 chứ không gạt đi.

### 5.6 Procopius `Q186153` — loại vì dữ liệu rác và chồng lấn

Lấp ô **Sử học**, nhưng: Wikidata có `+0500` **prec 6 = thiên niên kỷ**, một P570 `+0506`
(vô lý), một P570 `+0558` prec 7, **và một claim deprecated ghi `+2026-03-01`** (xem
§1.1 bẫy số 2). Thêm vào đó ông nằm trọn trong cảnh Justinianus. **Gregory xứ Tours lấp
cùng ô Sử học với dữ liệu tốt hơn nhiều và không chồng lấn** → Procopius bị chính
Gregory loại.

### 5.7 Bhartṛhari `Q335161` — loại vì niên đại đẩy sang thế kỷ 7

P569 `+0570`, P570 `+0651` — **theo chính Wikidata thì ông chủ yếu thuộc CE07**, và
reference là P143/P1417 (nhập từ Wikipedia / Britannica ID), không phải nguồn học thuật.
Niên đại thật của ông là một tranh luận lớn (có hướng đặt ông **k. 450–510**, tức sớm
hơn một thế kỷ rưỡi). Biên độ bất định **~150 năm** → `độ tin cậy niên đại: Thấp`, và
không xác định nổi ông thuộc nhóm nào. Loại.

### 5.8 Tì-ni-đa-lưu-chi `Q4111528` — vướng quy tắc 6, cần ban biên tập ra phán quyết

`Q4111528`: **P31 REF=0**, P569 `+0550` **prec 7 = thế kỷ**, P570 `+0594` REF=1; toàn bộ
thực thể chỉ **5.111 byte** — gần rỗng.

Vấn đề thủ tục quan trọng hơn vấn đề dữ liệu: ông **đã có mục** trong phụ lục
`CH90-CE01_09-04`, và ghi chú biên tập của `ch05.md` đã đánh dấu ông là người
"cân nhắc nâng lên ở P4". Theo **quy tắc 6**, người đã có mục ở chỗ khác **không được nêu
như ứng viên bị loại** trong ghi chú biên tập. Nhưng quy tắc 6 được viết cho các mục
chính; phụ lục CH90 vốn **được thiết kế để cô lập khỏi thống kê chính**.
→ **Tôi không tự quyết chuyện này.** Phán quyết cần có: *"mục phụ lục CH90 có tính là
'đã có mục' theo nghĩa quy tắc 6 hay không?"* Tôi để ông **ngoài** danh sách ứng viên bị
loại ở §8 cho an toàn, và nêu câu hỏi ở §8.1.

Về nội dung: kể cả khi được xét, dữ liệu niên đại prec-thế-kỷ và thực thể Wikidata gần
rỗng khiến `độ tin cậy niên đại` tối đa là **Thấp**.

## 6. Bảng xếp hạng có điểm số

### 6.1 Thang điểm tôi dùng và vì sao

Đề bài cho năm tiêu chí kèm trọng số bằng lời ("nặng nhất", "có trọng số thật"…).
Tôi quy ra số theo đúng thứ tự nặng–nhẹ đó, **tổng 20 điểm** để khớp thang mà ghi chú
biên tập CE07 đã dùng (Pháp Xứng 18/20, Tùng Tán Cán Bố 16/20, Pakal 11/20) — nhờ vậy
điểm ở đây so sánh được trực tiếp với điểm đã có trong repo.

| Tiêu chí | Thang | Căn cứ |
|---|---|---|
| **C1 Ảnh hưởng dài hạn** (gồm counterfactual) | **0–7** | đề bài: "nặng nhất" |
| **C2 Độ vững bằng chứng** | **0–5** | đề bài: phạt nặng nếu mệnh đề trung tâm đang bị chuyên gia bác |
| **C3 Cân đối vùng** | **0–3** | "có trọng số thật" nhưng không được bẻ cong |
| **C4 Cân đối lĩnh vực** | **0–3** | ngang C3 |
| **C5 Ý mới / không chồng lấn** | **0–2** | tiêu chí sàng, không phải tiêu chí nâng |

**Số liệu nền để chấm C3 và C4** (tính lại từ `data/persons.json`, 208 mục chính / 23 mục
Chapter 5 — xem §0.1):

- **Vùng, trong Chapter 5**: Đông Á **9/23 (39%)**, Trung Đông/Bắc Phi 4, Nam Á 4,
  **Châu Âu 3 (13%)**, Châu Phi hạ Sahara 1, Đông Nam Á 1, Châu Mỹ 1, **Trung Á 0**.
  Toàn atlas: MENA 33,2% · Châu Âu 26,9% · Đông Á 24,5% · Nam Á 12,0% · **Trung Á 0,5%**.
  → Đông Á là vùng **nặng nhất** trong Chapter 5, không phải Châu Âu. Trung Á trống hẳn.
- **Lĩnh vực, bốn ô TRỐNG trong cả Chapter 5** (xác nhận lại bằng script):
  **Y học 0 · Kỹ thuật/Công nghệ 0 · Văn học 0 · Sử học 0**.
  (Nhắc lại: Nghệ thuật/Kiến trúc **không** trống — Pakal `CH05-CE07-12` có, tổng 1.)

### 6.2 Bảng

| # | Ứng viên | Q-ID | C1 /7 | C2 /5 | C3 /3 | C4 /3 | C5 /2 | **Tổng /20** |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **1** | **Boethius** | `Q102851` | **7** | **5** | 1 | **3** | **2** | **18** |
| **2** | Gregory xứ Tours | `Q67841` | 5 | **5** | 1 | **3** | **2** | **16** |
| 3 | John Philoponus | `Q317632` | 6 | **5** | 1 | 0 | **2** | 14 |
| — | *(Grêgôriô I — loại vì sai nhóm)* | `Q42827` | 6 | 5 | 1 | 0 | 1 | *(13)* |
| 4 | Tiêu Thống | `Q1039198` | 4 | 4 | **0** | **3** | **2** | 13 |
| 5 | Alexander xứ Tralles | `Q708684` | 3 | 3 | 1 | **3** | **2** | 12 |
| 6 | Imru' al-Qays | `Q1051776` | 5 | **1** | 1 | **3** | **2** | 12 |
| 7 | Maniakh | `Q12552755` | 3 | 2 | **3** | 1 | **2** | 11 |
| 8 | Anthemius xứ Tralles | `Q298226` | 4 | 3 | 1 | **3** | **0** | 11 |
| 9 | Dionysius Exiguus | `Q274091` | 6 | **1** | 1 | 1 | **2** | 11 |
| 10 | Procopius | `Q186153` | 5 | 2 | 1 | **3** | **0** | 11 |
| 11 | Theodora | `Q204843` | 4 | 3 | 1 | 0 | **0** | 8 |
| 12 | Mazdak | `Q272300` | 3 | **1** | 1 | 1 | **0** | 6 |
| — | *Lý Xuân (cầu An Tế)* | **không có** | — | — | — | — | — | **không chấm được** |
| — | *Bhartṛhari* | `Q335161` | — | — | — | — | — | **sai thế kỷ** |
| — | *Tì-ni-đa-lưu-chi* | `Q4111528` | — | — | — | — | — | **chờ phán quyết quy tắc 6** |

### 6.3 Giải trình từng điểm cho ba hạng đầu

**Boethius 7/5/1/3/2 = 18.**
- **C1 = 7** (kịch khung). Căn cứ không phải cảm tính mà là một câu tôi đã tự mở và đọc
  trong SEP: *"Along with Augustine and Aristotle, he is the fundamental philosophical and
  theological author in the Latin tradition."* Counterfactual rõ và dài: nếu không có bản
  dịch của ông, Tây Âu **không có Aristotle logic** cho đến làn sóng dịch từ tiếng Ả Rập
  thế kỷ 12 — tức **mất khoảng 600 năm**. Toàn bộ logic kinh viện, cái khung mà đại học
  châu Âu được dựng lên trên đó, đi qua ông.
- **C2 = 5.** Đây là hồ sơ bằng chứng **vững nhất trong cả bảng**: tác phẩm của ông còn
  nguyên, không phải đoán ai nói về ai. Mệnh đề trung tâm (ông là kênh truyền Aristotle
  vào Latinh) **không bị ai bác** — ngược lại, SEP còn làm nó sắc hơn. Trừ 0 cho vênh
  niên đại 524/526 vì vênh hai năm không đụng tới mệnh đề trung tâm.
- **C3 = 1.** Trung thực mà nói, đây là **điểm yếu duy nhất**: Châu Âu là vùng nặng thứ
  hai toàn atlas (26,9%). Tôi **không** nâng điểm này bằng lý lẽ "nhưng trong Chapter 5
  Châu Âu chỉ có 13%" — lý lẽ đó đúng nhưng là cách chọn mẫu có lợi cho kết luận, nên tôi
  nêu nó như thông tin, không tính thành điểm.
- **C4 = 3.** Lấp **Văn học**, một trong bốn ô trống thật. Và không phải nhét cho đủ ô:
  *Consolatio* là prosimetrum, SEP ghi nó được dịch *"not merely into almost every
  medieval vernacular, but also into Greek and even Hebrew"*, người dịch gồm
  **Jean de Meun và Chaucer**.
- **C5 = 2.** Không chồng lấn với bất kỳ ai trong 11 người CE06. Mạnh hơn thế: atlas
  **đã ba lần dựa vào ông** làm cơ chế truyền cho Porphyry mà chưa cho ông mục nào (§3.1).

**Gregory xứ Tours 5/5/1/3/2 = 16.**
- **C1 = 5** chứ không hơn: ảnh hưởng của ông chủ yếu là **ảnh hưởng của một nguồn** —
  ta biết Gaul thế kỷ 6 qua ông. Đó là ảnh hưởng thật và bền, nhưng khác loại với
  ảnh hưởng "đổi hình dạng một ngành" của Boethius.
- **C2 = 5**: niên đại prec-ngày hai đầu, tác phẩm còn nguyên mười quyển.
  *Lưu ý thủ tục:* tôi **chưa mở được nguồn thứ cấp nào** cho ông (SEP 404, Britannica
  403). Tôi **không** trừ C2 vì chuyện đó — C2 chấm độ vững của bằng chứng lịch sử, không
  chấm độ may mắn của tôi khi tải trang — nhưng nó là việc **bắt buộc phải làm xong trước
  khi viết mục**, ghi rõ ở §8.2.
- **C4 = 3**: lấp **Sử học**, ô trống thật, và lấp bằng người sáng lập thực tế của
  sử học Latinh hậu La Mã.

**John Philoponus 6/5/1/0/2 = 14.** C1 cao (SEP: ảnh hưởng tới
*"Bonaventure, Gersonides, Buridan, Oresme, and Galileo"*), C2 cao (thực thể Wikidata
sạch nhất bảng: P31 REF=4). Gãy ở **C4 = 0**: Triết học và Khoa học tự nhiên **đều đã có
trong CE06**, nên ông không lấp gì. Kém Boethius đúng ở hai chỗ C1 và C4.

## 7. KHUYẾN NGHỊ DUY NHẤT

> ### Lấp chỗ thứ 12 của CE06 bằng **Boethius**.

Không phải "không ai xứng đáng". Có người xứng đáng, và theo tôi là xứng đáng khá rõ:
**18/20**, bằng điểm Pháp Xứng — người được xếp cao nhất CE07 — và cách người hạng hai
2 điểm.

### 7.1 Các trường cần điền

```
### CH05-CE06-12 · Boethius (Anicius Manlius Severinus Boethius)

năm: k. 477–526 CN
vùng: Châu Âu
lĩnh vực: Triết học, Văn học
độ tin cậy niên đại: Trung bình
wikidata: Q102851
câu hỏi lớn: Thực tại
```

Giải trình từng trường:

- **`năm: k. 477–526 CN`.** Tôi **không** dùng "480–524" dù đó là con số phổ biến và là
  con số Wikidata để ở rank *preferred*. Lý do: SEP (bản sửa 14-10-2026) ghi
  *"born: circa 475–7"* và *"died: 526?"*, *"imprisoned and (probably in 526) executed"*.
  Đây đúng tình huống `CONTRIBUTING.md` **quy tắc 4** cảnh báo — khớp Wikidata không đồng
  nghĩa với đúng. Tiền tố `k.` giữ cho câu không nói dối.
- **`độ tin cậy niên đại: Trung bình`.** Dung sai lint là **±25 năm**
  (`DATE_TOLERANCE` trong `atlaslib/common.py`), nuốt trọn cả cặp 480/524 lẫn 477/526, nên
  đối chiếu Wikidata sẽ **sạch mà không phải chọn phe** trong một tranh luận chưa khép.
  Đặt `Cao` (±5) cũng qua được lint ở đầu mất (524 vs 526) nhưng sẽ là một tuyên bố chắc
  chắn mà nguồn không cho phép. **Không đặt `Cao`.**
- **`vùng: Châu Âu`.** Rome và Pavia. **Không cần viện tới ngoại lệ nào**, không có chỗ
  nào để bẻ cong. Tôi nói thẳng: lựa chọn này **không có lợi** cho thống kê vùng
  (Châu Âu 26,9% toàn atlas) — tôi vẫn khuyến nghị ông vì C1/C2/C4 áp đảo, chứ không
  phải vì vùng.
- **`lĩnh vực: Triết học, Văn học`** — tối đa 2 trường theo §5. **Văn học** là một trong
  bốn ô trống thật của Chapter 5, và nó đúng với *Consolatio* (prosimetrum, vào hầu hết
  ngôn ngữ bản địa trung cổ, Jean de Meun và Chaucer dịch).
- **`wikidata: Q102851`** — tôi tự tra qua `wbsearchentities` rồi `wbgetentities`, đọc
  claim thô: **P31 = Q5** (người); **P569 `+0480` prec 9, rank preferred, 9 reference** —
  nhiều reference nhất trong cả bảng §1; **P570 `+0524` prec 9, rank preferred,
  3 reference**. Không có thực thể trùng tên gây nhầm (khác hẳn ca Imru' al-Qays ba thực
  thể và ca Dionysius Exiguus có cả "bài bách khoa" lẫn "ấn bản sách" đứng cạnh).

**Vị trí hiển thị:** không cần lo chỉ số `-12`. `atlaslib/render.py` sắp người trong nhóm
theo `(born, id)`, nên với `born = 477` ông sẽ tự động hiện **đầu nhóm CE06**, đúng với
giai đoạn ảnh hưởng chính (viết k. 505–524) theo tinh thần §3/§5.3.

### 7.2 Luận đề trung tâm — viết được, không cần rào quá tay

> Boethius chọn **không** viết triết học của riêng mình. Ông bỏ cả đời vào việc dịch và
> chú giải bộ *Organon* của Aristotle sang tiếng Latinh, và chính lựa chọn đó quyết định
> **Tây Âu có thể nghĩ bằng cái gì trong sáu trăm năm sau đó**: cho đến làn sóng dịch từ
> tiếng Ả Rập ở thế kỷ 12, Aristotle của Boethius **chính là** Aristotle ở phương Tây.
> Câu hỏi mà Porphyry cố tình gác lại trong *Isagoge* — giống và loài tồn tại thật hay chỉ
> trong tư tưởng — đến tay các nhà kinh viện là **qua bản dịch và chú giải của ông**, và
> trở thành tranh luận trung tâm của cả một thời kỳ.

Một sắc thái **nên viết vào, vì nó làm luận đề mạnh hơn chứ không yếu đi** (và vì quy
tắc 7): cái ông truyền không phải Aristotle trung tính. SEP *"Literary Forms of Medieval
Philosophy"* — tôi đã mở và đọc — nói rõ ông mang sang cho thời trung cổ
*"both the obvious and more subtle Neoplatonic distortions of the Aristotelian corpus"*,
và chính ông lặp lại tham vọng của Porphyry là **chứng minh Plato và Aristotle hoà hợp**.
Tức: châu Âu trung cổ đọc Aristotle **qua lăng kính Tân Plato**, và lăng kính đó là
của Boethius.

### 7.3 Quan hệ nên nối

- **`CH04-CE03-03` Porphyry xứ Tyre · kế thừa · trực tiếp** — Boethius dịch chính
  *Isagoge* của Porphyry và chú giải nó hai lần.
  **Nên sửa luôn dòng quan hệ hiện có trong mục Porphyry** (`content/ch04.md` dòng 455):
  hiện nó là *"Logic kinh viện Latinh và Hồi giáo qua Boethius · kế thừa · qua trường phái"*
  — một quan hệ trỏ vào **một khái niệm**, với **tên Boethius nằm trong chuỗi mô tả**.
  Khi Boethius có mục riêng, dòng này nối được vào **một người thật**.
- **`CH05-CE06-01` Justinianus I · tương đồng độc lập · suy đoán học giả** — hai dự án
  cùng thế hệ nhằm giữ lại di sản cổ điển bằng hai cách khác nhau (hệ thống hoá luật
  La Mã / hệ thống hoá logic Hy Lạp). **Đây là một quan hệ yếu — nếu ban biên tập thấy
  gượng thì bỏ.** Tôi nêu ra chứ không đẩy.

### 7.4 Những gì BẮT BUỘC phải làm trước khi viết mục

1. **Mở thêm ít nhất một nguồn thứ cấp nữa và xác nhận bằng mã + byte + ký tự.** Hiện tôi
   có **hai** nguồn đã kiểm, cả hai đều là SEP:
   `https://plato.stanford.edu/entries/boethius/` (**200 / 90.315 B / 70.352 ký tự**) và
   `https://plato.stanford.edu/entries/medieval-literary/` (**200 / 144.744 B /
   117.957 ký tự**, "Boethius" xuất hiện **35 lần**). Marenbon 2003 và Magee 2024 tôi
   **chỉ xác nhận là có trong thư mục SEP**, **[KHÔNG KIỂM ĐƯỢC]** nội dung — **không
   được dẫn chúng như đã kiểm**.
2. **Không viết "480–524"** ở bất kỳ đâu trong mục mà không có chữ `k.` hoặc một câu rào.
3. **Không viết "Boethius dịch toàn bộ Aristotle"** — SEP ghi rõ bản
   *Posterior Analytics* của ông **đã mất** và kế hoạch dịch trọn Plato + Aristotle
   **không hoàn thành**.
4. **Không viết ông tử đạo vì đức tin.** Cáo buộc trong hồ sơ là **phản nghịch và hành
   nghề ma thuật**; cách đọc "tử đạo chống Arian" là hagiography đời sau.
5. **Không khép tranh luận "Consolatio có phải tác phẩm Kitô giáo không."**

## 8. Danh sách ứng viên bị loại, dùng được cho ghi chú biên tập

### 8.1 Kiểm quy tắc 6 bằng script, không bằng trí nhớ

Quy tắc 6 cấm nêu một người là "ứng viên bị loại" nếu người đó **đã có mục riêng ở chỗ
khác**. Tôi kiểm bằng cách đối chiếu **Q-ID** (không đối chiếu tên — tên tiếng Việt
phiên âm rất dễ trượt) của toàn bộ 15 ứng viên với trường `wikidata` của cả 248 mục trong
`data/persons.json`:

| Kết quả | |
|---|---|
| **14/15 ứng viên: KHÔNG có mục ở bất kỳ đâu** | → nêu được, hợp quy tắc 6 |
| **`Q4111528` Tì-ni-đa-lưu-chi: ĐÃ CÓ mục `CH90-CE01_09-04`** | → **không nêu**, xem dưới |

**Câu hỏi cần ban biên tập phán quyết (tôi không tự quyết):** phụ lục CH90 được thiết kế
để **cô lập khỏi thống kê chính**. Vậy một mục trong CH90 có tính là "đã có mục" theo
nghĩa quy tắc 6 không? Trong lúc chưa có phán quyết, tôi **loại Tì-ni-đa-lưu-chi ra khỏi
danh sách dưới đây** — phương án an toàn, vì nêu nhầm thì vi phạm quy tắc, còn không nêu
thì chỉ là thiếu sót nhỏ.

### 8.2 Văn bản đề nghị cho mục `## Ghi chú biên tập` của `content/ch05.md`

> **Chỗ thứ 12 của nhóm CE06 — điểm chấm và các ứng viên bị loại.**
> Thang 20 điểm, cùng thang đã dùng cho CE07: ảnh hưởng dài hạn 7 · độ vững bằng chứng 5 ·
> cân đối vùng 3 · cân đối lĩnh vực 3 · ý mới 2.
>
> **Chọn: Boethius `Q102851` — 18/20.** Lấp ô **Văn học**, một trong bốn lĩnh vực trống
> của cả Chapter 5 (ba ô còn lại: Y học, Kỹ thuật/Công nghệ, Sử học). Lý do chính không
> phải lấp ô mà là counterfactual: không có bản dịch *Organon* của ông, Tây Âu không có
> Aristotle logic cho tới làn sóng dịch từ tiếng Ả Rập thế kỷ 12. Niên đại để
> `k. 477–526 CN` / `Trung bình` chứ không để "480–524" / `Cao`, vì SEP ghi "circa 475–7"
> và "526?" trong khi Wikidata để 480/524 ở rank preferred — hai nguồn vênh nhau và
> tranh luận chưa khép.
>
> **Xếp sau và bị loại:**
> - **Gregory xứ Tours `Q67841` — 16/20.** Ứng viên mạnh thật, lấp ô **Sử học** với niên
>   đại prec-ngày hai đầu và mười quyển *Decem Libri Historiarum* còn nguyên. Loại vì
>   thua Boethius ở ảnh hưởng dài hạn (ảnh hưởng của ông chủ yếu là ảnh hưởng của một
>   **nguồn**), và vì vòng kiểm này **chưa mở được nguồn thứ cấp nào** cho ông
>   (SEP không có bài — 404; Britannica chặn bot — 403). **Nên xét lại ở vòng sau.**
> - **John Philoponus `Q317632` — 14/20.** Hồ sơ bằng chứng rất tốt, ảnh hưởng tới tận
>   Buridan, Oresme và Galileo. Loại vì không lấp ô nào (Triết học và Khoa học tự nhiên
>   đều đã có trong CE06) và vì vùng Trung Đông/Bắc Phi đang nặng nhất atlas (33,2%);
>   Alexandria **không** hưởng ngoại lệ Tiểu Á, theo đúng tiền lệ Diophantus.
> - **Grêgôriô I `Q42827` — không chấm vào CE06.** Dữ liệu niên đại tốt (mất 12-3-604,
>   độ chính xác ngày, 3 reference), nhưng giai đoạn ảnh hưởng chính của ông là
>   **giáo hoàng 590–604**, nằm ở bản lề sang thế kỷ 7. Theo §3/§5.3 (xếp theo giai đoạn
>   ảnh hưởng, không theo năm sinh), **ông thuộc về CE07** — đề nghị xét ở đó.
> - **Tiêu Thống `Q1039198` — 13/20.** *Văn tuyển* là tuyển tập văn học ảnh hưởng dài nhất
>   Đông Á. Loại vì ông là người **biên tuyển** nên counterfactual yếu, và vì Đông Á đã
>   chiếm **9/23 (39%)** Chapter 5 — vùng nặng nhất chương.
> - **Alexander xứ Tralles `Q708684` — 12/20.** Lấp ô **Y học**. Loại vì ảnh hưởng dài
>   hạn ở tầm "sách thuốc được dùng lâu", không phải tầm đổi hình dạng một ngành.
>   **Nếu ưu tiên lấp Y học hơn Văn học thì đây là lựa chọn đúng.**
> - **Imru' al-Qays `Q1051776` — 12/20.** Loại vì **độ vững bằng chứng 1/5**: không có
>   nguồn đương thời; niên đại 501–544 là quy ước dựng từ *akhbār* thế kỷ 8–10; và tính
>   xác thực của toàn bộ kho thơ tiền Hồi giáo vẫn đang bị tranh cãi từ gốc
>   (Margoliouth 1925, Ṭāhā Ḥusayn 1926). Thêm: **có ba thực thể Wikidata cùng tên**, và
>   mốc tuyệt đối duy nhất mang tên này — bi ký Namāra **328 CN** — là **người khác**.
> - **Maniakh `Q12552755` — 11/20.** Ứng viên duy nhất xếp được **Trung Á** một cách
>   trung thực (Sogdiana = Transoxiana, đúng vành đai mà quy ước `vùng:` vẫn gọi là
>   Trung Á), và Trung Á đang **trống hoàn toàn trong Chapter 5**, toàn atlas chỉ 1 người.
>   Đó là điểm cộng thật, **không phải bẻ cong**. Loại vì ảnh hưởng dài hạn mỏng (một
>   sứ đoàn, mà mục đích thương mại của nó bị vô hiệu ngay tại chỗ) và vì thực thể
>   Wikidata gần rỗng: P31 **REF=0**, P569 `+0550` **độ chính xác chỉ tới thế kỷ**.
> - **Anthemius xứ Tralles `Q298226` — 11/20.** Lấp hai ô (Kỹ thuật/Công nghệ,
>   Nghệ thuật/Kiến trúc) nhưng **ý mới 0/2**: ông do Justinianus bổ nhiệm, công trình là
>   công trình của Justinianus, và mục Justinianus đã nói về Hagia Sophia.
> - **Dionysius Exiguus `Q274091` — 11/20.** Ảnh hưởng có lẽ lớn nhất danh sách (hệ
>   *Anno Domini*), nhưng **bằng chứng 1/5**: thực thể Wikidata không có reference thật
>   (chỉ "nhập từ Wikipedia"), năm mất có một claim bị **deprecated**; và công bằng mà
>   nói, công lớn phổ biến hoá *Anno Domini* thuộc về **Bede**, hai thế kỷ sau.
> - **Procopius `Q186153` — 11/20.** Lấp ô Sử học nhưng nằm trọn trong cảnh Justinianus,
>   và thực thể Wikidata hỏng nặng: một P569 độ chính xác **thiên niên kỷ**, một P570
>   `+0506` vô lý, và một claim bị deprecated ghi **`+2026-03-01`**.
> - **Theodora `Q204843` — 8/20.** Bằng chứng định danh thì tốt (khảm San Vitale,
>   *Novellae*, John xứ Ephesus). Loại vì **ý mới 0/2**: toàn bộ sân khấu của bà là sân
>   khấu của mục Justinianus đã có; và vì chân dung phổ thông về bà hầu như chỉ dựa vào
>   **một nguồn bôi nhọ duy nhất**, *Anekdota* của Procopius — tức ý mới khả dĩ duy nhất
>   ("quyền lực nữ giới trong triều Byzantine") lại phải dựng trên đúng cái nguồn không
>   dùng được cho việc đó.
> - **Mazdak `Q272300` — 6/20.** Loại vì **ý mới 0/2** (đã được nêu đích danh trong mục
>   Khosrow I) và **bằng chứng 1/5**: không một dòng nào từ phía ông còn lại; hình ảnh
>   "chia chung của cải và vợ" đến từ *Siyāsatnāma*, viết 500 năm sau nhằm bôi nhọ phái
>   Ismāʿīlī đương thời.
> - **Bhartṛhari `Q335161` — không chấm.** Wikidata ghi 570–651, tức chủ yếu thuộc thế
>   kỷ 7, trong khi một hướng nghiên cứu khác đặt ông **k. 450–510**. Biên độ bất định
>   ~150 năm thì không xác định nổi ông thuộc nhóm nào.
> - **Lý Xuân, người dựng cầu An Tế — không chấm được: không tồn tại Q-ID.**
>   `wbsearchentities` không trả về thực thể người nào ứng với kỹ sư này; chỉ có **cây
>   cầu** `Q551446`, và cây cầu đó **không có trường P84 (kiến trúc sư) lẫn P170 (người
>   tạo)**, còn P571 (khởi dựng) ghi **606**, tức đã sang thế kỷ 7. Ô
>   **Kỹ thuật/Công nghệ** của Chapter 5 vẫn trống và **không lấp được bằng người này**.

### 8.3 Ba việc còn treo, ghi lại để không rơi

1. **Gregory xứ Tours chưa có nguồn thứ cấp nào được mở và xác nhận.** Nếu vòng sau định
   xét lại ông (16/20, ứng viên hạng hai), việc đầu tiên là tìm một nguồn thứ cấp **mở
   được bằng curl** — SEP không có bài về ông, Britannica chặn bot.
2. **Phán quyết quy tắc 6 cho phụ lục CH90** (§8.1) — ảnh hưởng tới Tì-ni-đa-lưu-chi và
   tới cả bảy nhân vật Việt Nam khác trong CH90 ở các vòng sau.
3. **Ô Y học, Kỹ thuật/Công nghệ và Sử học của Chapter 5 vẫn trống sau vòng này.**
   Boethius chỉ lấp được **Văn học**. Alexander xứ Tralles (Y học, 12/20) và Gregory xứ
   Tours (Sử học, 16/20) là hai lối ra sẵn có nếu CE07 hoặc một nhóm khác còn chỗ;
   Kỹ thuật/Công nghệ thì **chưa có lối ra nào** sau khi Lý Xuân bị loại vì không có Q-ID.

---

*Hết báo cáo. Mọi Q-ID trong văn bản này đều do tôi tự tra bằng `wbsearchentities` +
`wbgetentities` trong vòng kiểm này và đọc claim thô (P31/P569/P570 kèm `precision`,
`rank`, số `references`); không có Q-ID nào lấy từ trí nhớ. Mọi URL được dẫn như "đã
kiểm" đều kèm mã HTTP, số byte và số ký tự chữ rút được sau khi bỏ thẻ. Mọi chỗ không
kiểm được đều mang nhãn `[KHÔNG KIỂM ĐƯỢC]` kèm lý do.*
