# Bình duyệt độc lập — ghi chú biên tập CE10, 12 khối
Ngày: 2026-11-02 · phạm vi: content/ch05.md dòng 1229–1270

Phương pháp: đọc toàn bộ nhóm CE10 (`content/ch05.md` dòng 846–1055), `reports/stats.txt`,
`reports/ch05-ce10-wikidata.md`, `reports/ch05-ce10-review.md`, `reports/ch05-ce09-review-c.md`,
`reports/ch05-ce09-review-d.md`, `CONTRIBUTING.md`, `README.md`, `HANDOFF-ce09-ce10.md`,
`content/ch90.md`, `atlaslib/lint.py`, `atlaslib/common.py`.
Mọi QID được tra lại trực tiếp bằng `wbgetentities` trong vòng này (User-Agent trung lập),
không tin con số chép lại trong hồ sơ cổng.

---

## Khối 1 — Sáu người cai trị trong mười hai, và vì sao nguyên tắc của nhóm CE09 không áp được ở đây

**Đã kiểm được (không có phát hiện)**
- `Chính trị/Nhà nước` **3/24 ô ở CE09**: đếm tay 12 mục CE09, mỗi mục 2 lĩnh vực = 24 ô; mang nhãn
  `Chính trị/Nhà nước` là `CH05-CE09-01`, `-08`, `-12` = 3. Đúng, và khớp chính khối lĩnh vực CE09
  (`content/ch05.md:1213`).
- **7 trong 22 ô, tức 31,8%** ở CE10: đếm tay lĩnh vực 12 mục CE10 = 2+2+2+2+**1**+2+**1**+2+2+2+2+2 = 22 ô
  (`-05` và `-07` chỉ có một lĩnh vực). Mang nhãn `Chính trị/Nhà nước`: `-03`, `-04`, `-05`, `-06`, `-08`,
  `-09`, `-11` = 7. 7/22 = 31,818…% → 31,8%. Đúng.
- **23,8% của toàn atlas**: khớp `reports/stats.txt` (`Chính trị/Nhà nước 97 23.8%`). Giá trị đúng
  *tại thời điểm đo* — xem BẮT BUỘC thứ ba.
- Sáu ID được liệt kê (`-08`, `-09`, `-11`, `-05`, `-06`, `-04`) đều tồn tại và đều là người cai trị. Số
  đếm "sáu người cai trị trong mười hai" đúng.

**BẮT BUỘC** — câu sai, nguyên văn: *"và nhà nước Transoxiana độc lập khỏi Baghdad (`CH05-CE10-04`)."*

Sai ở đâu: mệnh đề "độc lập khỏi Baghdad" đã bị chính vòng bình duyệt CE10 bác và đã được gỡ khỏi
thân mục, nhưng khối ghi chú này vẫn giữ. Bằng chứng ba lớp, đều trong repo:
(1) thân mục `CH05-CE10-04` hiện viết *"nhưng vẫn nhận sắc phong của caliph al-Muʿtaḍid và vẫn gửi cống
về Baghdad"*; (2) **khối 2 của chính Ghi chú biên tập** (dòng 1234) viết rằng vế "không qua Baghdad" là
sai và đã bị sửa; (3) `reports/ch05-ce10-review.md:114` ghi caliph al-Muʿtaḍid là người thúc Ismāʿīl đánh
ʿAmr rồi **sắc phong** Khorasan, Ṭabaristān, Rayy và Isfahan cho ông. Khối 1 và khối 2 vì vậy đang nói
ngược nhau về cùng một mục, cách nhau ba dòng.

Đề xuất câu thay thế nguyên văn:
> và một triều đình Transoxiana cai trị Khorasan bằng bộ máy riêng trong khi vẫn nhận sắc phong Baghdad (`CH05-CE10-04`).

**BẮT BUỘC** — câu sai, nguyên văn: *"Sáu mục vua của nhóm này đều được chỉ mục vì **thể chế chính họ lập**"*
(kèm hai mục trong danh sách liền sau).

Sai ở đâu: mệnh đề "đều … thể chế chính họ lập" không đúng cho ít nhất hai trong sáu mục, và phản ví dụ
nằm ngay trong danh sách mà chính câu ấy đưa ra.
- `CH05-CE10-05` được gắn với *"chức tiết độ sứ do người bản địa giữ"*. Chức tiết độ sứ là **thể chế của
  nhà Đường**, không phải thể chế Khúc Thừa Dụ lập: thân mục viết *"tự nhận chức Tĩnh Hải quân tiết độ sứ"*
  và ghi `Kế thừa từ: Thể chế tiết độ sứ của nhà Đường · kế thừa · trực tiếp`. Cái mới ở đây là **ai giữ
  chức**, không phải chức.
- `CH05-CE10-06` được gắn với *"chỗ rẽ của trung tâm Java"*. Dời trung tâm chính trị là một sự kiện địa lý,
  không phải một thể chế; thân mục còn ghi rõ *"Vì sao dời thì chưa ai chứng minh được"*. Thể chế mà mục
  thật sự chỉ mục là **sắc lập sima**, và khối 1 không nhắc tới nó.

Đề xuất câu thay thế nguyên văn:
> Bốn trong sáu mục vua được chỉ mục vì **thể chế chính họ lập**: ngôi vua cha truyền con nối và hai hệ quan chế bắc–nam (`CH05-CE10-08`), lối thống nhất bằng hôn nhân giữa các dòng họ (`CH05-CE10-09`), danh hiệu caliph thứ ba (`CH05-CE10-11`), và sắc lập sima gắn làng vào nhà nước bằng nghĩa vụ (`CH05-CE10-06`). Hai mục còn lại được chỉ mục vì một lý do khác và phải nói đúng tên nó: `CH05-CE10-05` không lập ra chức tiết độ sứ mà là người bản địa đầu tiên giữ nó, còn `CH05-CE10-04` giữ được một triều đình Transoxiana vận hành bằng bộ máy riêng trong khi vẫn nhận sắc phong Baghdad.

**BẮT BUỘC** — câu sai, nguyên văn: *"Nhóm này đi ngược: 7 trong 22 ô, tức 31,8%, so với 23,8% của toàn atlas."*

Sai ở đâu: con số **23,8%** là một tỉ lệ toàn cục viết ở thì hiện tại, không tự khai thời điểm đo — tức vi
phạm đúng quy ước mà **khối 13 của chính vòng này vừa đặt ra** ba mươi chín dòng bên dưới: *"con số trong
ghi chú biên tập phải tự khai nó đo ở thời điểm nào, hoặc không nêu số"* (dòng 1270). Khối 13 còn nêu đích
danh ca đã được chữa theo quy ước ấy — `23,4%` ở khối lĩnh vực CE09 nay ghi *"toàn atlas **khi ấy**"*
(kiểm được ở dòng 1213). Khối 1 là ca mới sinh ra ngay trong vòng đặt quy ước. Mẫu số sẽ đổi ở CE11, và
`reports/stats.txt` hiện đo trên 245 nhân vật; 23,8% sẽ sai sau vòng sau mà không lint nào bắt được
(`atlaslib/lint.py` không đọc văn bản Ghi chú biên tập ngoài phép kiểm chữ "Việt Nam").

Đề xuất câu thay thế nguyên văn:
> Nhóm này đi ngược: 7 trong 22 ô, tức 31,8% — so với 23,8% của toàn atlas **đo sau khi dựng nhóm này**.

**NÊN** — *"ở Trung Á, Đông Nam Á và vùng Đông Á ngoài Trung Hoa, người thế kỷ 10 để lại đủ tư liệu để chấm
theo bốn tiêu chí **gần như chỉ có người lập nhà nước**."*

Mệnh đề có hedge "gần như", nên không sai; nhưng phản ví dụ nằm trong chính nhóm và khối không nêu:
`CH05-CE10-10 · Ki no Tsurayuki` thuộc đúng "Đông Á ngoài Trung Hoa", không phải người lập nhà nước, và
được chấm bằng (c) và (d) trên một văn bản còn nguyên. Tỉ lệ thật trong nhóm là 5/6 cho ba vùng ấy
(`-04`, `-05`, `-06`, `-08`, `-09` là vua; `-10` thì không). Một khối tự nhận là khai chỗ yếu thì nên khai
luôn ca làm yếu lập luận của mình.

**CÂN NHẮC** — khối mở bằng 7 ô `Chính trị/Nhà nước` rồi giải thích 6 mục vua. Ô thứ bảy là `CH05-CE10-03 ·
al-Fārābī` (`Triết học, Chính trị/Nhà nước`), người không cai trị gì cả. Một mệnh đề phụ nửa dòng
("ô thứ bảy là nhãn lĩnh vực của một nhà triết học chính trị, không phải một người cai trị") sẽ chặn
được chỗ người đọc tự trừ 7 − 6 = 1 rồi đoán sai.

> **Lưu ý về trạng thái file trong lúc soi.** Giữa lúc vòng này chạy, `content/ch05.md` được sửa
> (các mục CE10 được áp bình duyệt: `-02` đổi năm sinh 854→865, `-06`/`-08`/`-09` thêm ứng viên bị cắt,
> `-05` **nâng hai đích tự do thành ID** `CH90-CE01_09-07` và `CH90-CE10_14-01`, `-10` hạ một dòng
> `trực tiếp` xuống `qua trường phái`). **Mười ba khối ghi chú biên tập thì không đổi một chữ.**
> Phạm vi soi vì vậy dịch xuống một dòng: nay là **1231–1271**. Mọi trích dẫn dưới đây đã kiểm lại
> là còn nguyên văn trong file sau khi sửa. Một số khối nay mô tả một trạng thái repo không còn tồn tại —
> đánh dấu rõ ở từng chỗ.

---

## Khối 2 — Mục sát ranh giới nhất của nhóm, và nó tự khai: Ismāʿīl Samānī

**Đã kiểm được (không có phát hiện)**
- *"bản đầu viết rằng đây là **lần đầu** … **không qua Baghdad** — cả hai vế đều sai"*: khớp đúng
  `reports/ch05-ce10-review.md:112–114`, và thân mục hiện tại đã mang câu thay thế mà vòng ấy đề nghị
  (`:116`), nguyên văn trùng khớp.
- *"Nhà Ṭāhir đã làm thế từ 821"*: khớp vòng bình duyệt (nhà Ṭāhir 821–873).
- *"chính caliph al-Muʿtaḍid là người thúc ông đánh ʿAmr rồi sắc phong cho ông"*: khớp vòng bình duyệt
  (`:114`, kèm danh sách Khorasan, Ṭabaristān, Rayy, Isfahan).
- *"tụt từ một bước ngoặt xuống mắt thứ ba của một chuỗi đã chạy từ 821"*: khớp `:132` gần như nguyên văn.
- *"phục hưng văn học Ba Tư ở Bukhara thì thuộc thế hệ sau ông"* và *"được ghi ở mức `suy đoán học giả`"*:
  thân mục ghi `- Phục hưng văn học Ba Tư mới ở Bukhara thế kỷ 10 · kế thừa · suy đoán học giả`. Đúng.
- `al-Tirmidhī` `Q293578` **có** được nêu ở ghi chú nhóm CE09 (dòng 1208). Đúng.
- Tra lại `Q293578` bằng `wbgetentities`: `P569 = +0825` (p9), `P570 = +0892` (p9). Năm mất 892 xác nhận.

**BẮT BUỘC** — câu sai, nguyên văn: *"thì đây là mục đầu tiên nên cắt, và ứng viên thay thế trong cùng ô
vùng là al-Tirmidhī `Q293578` — đã nêu ở ghi chú nhóm CE09."*

Sai ở đâu: al-Tirmidhī **không đủ tư cách làm ứng viên thay thế cho một suất CE10**, và chính thân mục
`CH05-CE10-04` nói thế, cách khối này mười chín dòng: *"Hồ sơ cổng không tìm được ứng viên Trung Á nào khác
cho khung 901–1000: al-Tirmidhī mất năm 892, thuộc nhóm trước."* Tôi tra lại `Q293578` trực tiếp: `P570 =
892`, nằm ngoài khung 901–1000 của nhóm. Cắt `CH05-CE10-04` rồi thay bằng ông thì ô Trung Á của nhóm CE10
vẫn bằng 0 — và lint sẽ cảnh báo đời sống không giao với khung nhóm (`atlaslib/lint.py`, phép kiểm
`rng`/`years_ok`). Đây đúng loại lỗi `CONTRIBUTING.md` điểm 5 cấm: *"'Ứng viên cùng thời' phải thật sự
cùng thời."*

Đề xuất câu thay thế nguyên văn:
> thì đây là mục đầu tiên nên cắt — và phải nói thẳng rằng **không có ai thay được**: hồ sơ cổng không tìm được ứng viên Trung Á nào khác trong khung 901–1000, còn al-Tirmidhī `Q293578` (mất 892, đã nêu ở ghi chú nhóm CE09) thuộc nhóm trước. Cắt mục này là chấp nhận ô Trung Á của nhóm bằng 0, không phải đổi người.

**NÊN** — *"Hai mệnh đề mạnh nhất trong mục — dirham Samanid thành bạc của đường thương mại Bắc Âu, và
tiếng Ba Tư trở lại làm ngôn ngữ hành chính — đều là mệnh đề về **nhà nước**, không phải về cá nhân ông"*.

Khối tự nhận đang khai chỗ yếu, nhưng khai thiếu một tầng mà vòng bình duyệt đã ghi: mệnh đề dirham
không chỉ "về nhà nước" — nguồn mà mục dẫn (Kovalev 2002, *Histoire & Mesure*) đo **sản lượng xưởng đúc
Samarqand**, tức một chuỗi suy luận từ sản lượng tiền sang ảnh hưởng thương mại Baltic, chứ không phải
một mệnh đề về việc Ismāʿīl làm. Nói "về nhà nước" làm chỗ yếu nhẹ đi một bậc so với thực tế.
Ghi thêm nửa câu — rằng mệnh đề ấy là suy luận từ dữ liệu đúc tiền, không phải từ hành vi của ông —
sẽ làm lời tự khai khớp với bằng chứng.

**CÂN NHẮC** — khối kết bằng *"Nếu vòng bình duyệt thấy đây vẫn là chỉ mục một người bảo trợ…"* ở thì
tương lai. Vòng bình duyệt CE10 **đã chạy xong** và đã kết luận: `reports/ch05-ce10-review.md` giữ mục
này, chỉ bắt hai tính từ. Câu điều kiện nên đổi sang thì hoàn thành, nếu không vòng CE11 sẽ tưởng việc
này còn treo.

---

## Khối 3 — Sáu bẫy niên đại Wikidata của thế kỷ 10, và cách mỗi mục xử

Tôi tra lại **cả sáu** QID trực tiếp bằng `wbgetentities` trong vòng này, không tin con số chép trong
hồ sơ cổng. Kết quả từng bẫy:

**Đã kiểm được (không có phát hiện)**
- (1) `Q192124` — `P570 = +0922-00-00` p9. Đúng là 922. Mục ghi 923. `DATE_TOLERANCE["Cao"] = 5`
  (`atlaslib/common.py:82`), nên lệch 1 năm thật sự nằm trong dung sai `Cao`. **Mệnh đề đúng trọn vẹn.**
- (2) `Q1292812` — `P569 = +0900` p9, `P570 = +0980` p9. Độ chính xác năm, đúng. Biên độ học thuật
  841–976 = 135 năm, khớp. Mục ghi `hoạt động k. 950–1000` + `Thấp`. **Đúng.**
- (3) `Q1001807` — `P569 = +0801-01-01` **p7**. Đúng là đệm thế kỷ. Mục ghi `hoạt động 905–907`. **Đúng.**
- (5) `Q172383` — có `P569 = +0938` p9. Mục ghi `k. 945`. **Đúng.**
- (6) `Q47684` — **không có `P569`**; chỉ `P570 = +0947` p9. Mục ghi `trị vì k. 929–947` + `Thấp`. **Đúng.**
- Phép kiểm `NON_BIO_YEARS_RE` mà hồ sơ cổng cảnh báo (trường `năm:` phải **mở đầu** bằng "trị vì"/"hoạt
  động") được `-05`, `-06`, `-07` tuân đúng. Không có mục CE10 nào kích hoạt đối chiếu sinh–mất sai loại.

**BẮT BUỘC** — câu sai, nguyên văn: *"Hồ sơ cổng CE10 kiểm trước khi viết, và cả sáu bẫy đều xác nhận lại
được ở vòng viết này."*

Sai ở đâu: **"sáu bẫy" của khối không phải "sáu bẫy" của hồ sơ cổng.** Bảng *"1. Bẫy niên đại phải xử
trước khi viết"* trong `reports/ch05-ce10-wikidata.md` liệt kê sáu dòng, và đó là: `Q169234` al-Rāzī ·
`Q1292812` Vācaspati · `Q192124` al-Ṭabarī · **`Q316349` al-Ashʿarī** · `Q172383` Gerbert ·
**`Q170248` Hrotsvitha`**. Khối 3 bỏ hai ca cuối (cả hai người đều bị cắt khỏi nhóm) và thay bằng
`Q1001807` Khúc Thừa Dụ — vốn nằm ở **mục 3** của hồ sơ cổng — và `Q47684` Mpu Sindok — vốn nằm ở
**mục 2**. Hệ quả thực tế: câu như đang viết hàm ý hồ sơ cổng đã được rà hết, trong khi hai bẫy gốc
(al-Ashʿarī lệch 1 năm ở **cả hai đầu**; Hrotsvitha có `P570 = 968` mà bà còn viết sau 973) **chưa được
xác nhận lại ở vòng nào**, và cả hai người vẫn được khối 12 nêu tên kèm niên đại.

Đề xuất câu thay thế nguyên văn:
> Hồ sơ cổng CE10 kiểm trước khi viết; sáu bẫy chạm vào mười hai mục thật sự được viết đều xác nhận lại được ở vòng này — ba từ bảng bẫy của hồ sơ cổng (`Q192124`, `Q1292812`, `Q169234`), hai từ mục "không có niên đại sinh" (`Q47684`, `Q1270024`) và một từ mục xác nhận lại cảnh báo CE09 (`Q1001807`). Hai bẫy còn lại của bảng ấy, `Q316349` al-Ashʿarī và `Q170248` Hrotsvitha, thuộc về người bị cắt nên **chưa được xác nhận lại**; niên đại của họ nêu ở khối "Những người bị cắt" vì thế lấy từ học giới, không từ Wikidata.

**NÊN** — *"(4) `Q169234` khai **năm** năm sinh khác nhau cho al-Rāzī, biên độ 12 năm"*.

Tra lại: `Q169234` có **năm phát biểu** `P569` — 866 (rank `preferred`), 854, 854, 864, 865 — tức chỉ
**bốn giá trị khác nhau**, vì 854 lặp hai lần. Biên độ 866 − 854 = 12 năm thì đúng. Thân mục `CH05-CE10-02`
viết chính xác hơn khối ghi chú (*"năm năm sinh khác nhau — 854 hai lần, 864, 865, 866"* — có liệt kê nên
người đọc tự thấy), còn khối 3 bỏ phần liệt kê nên chữ "khác nhau" thành sai. Đề nghị:
> (4) `Q169234` khai **năm phát biểu** `P569` cho al-Rāzī — 866, 854, 854, 864, 865, tức bốn giá trị khác nhau, biên độ 12 năm — nên mục ghi `Trung bình`.

**NÊN** — câu sai, nguyên văn: *"Không mục nào trong nhóm này chép thẳng một trường Wikidata mà không nói
rõ nó đáng tin tới đâu."*

Sai ở đâu: hai mục chép niên đại trùng khít Wikidata và **không** nói gì về độ tin cậy của trường ấy.
`CH05-CE10-08` ghi `872–926` + `Cao`; tra `Q4989`: `P569 = +0872` p9, `P570 = +0926-09-06` p11 — trùng
khít, và cả mục không có một câu nào về Wikidata. `CH05-CE10-09` ghi `877–943` + `Cao`; `Q334312`:
`P569 = +0877-01-31` p11, `P570 = +0943-07-04` p11 — cũng trùng khít, cũng không có câu nào. Mệnh đề
tuyệt đối "không mục nào" vì thế không đứng. Đề nghị:
> Mười mục trong nhóm nói rõ trường Wikidata nào đáng tin tới đâu; hai mục còn lại, `-08` và `-09`, chép niên đại trùng khít `Q4989` và `Q334312` ở độ chính xác ngày hoặc năm và không cần bàn thêm.

**CÂN NHẮC** — bẫy (5) bỏ mất một dữ kiện có lợi cho chính lập luận của nó: `Q172383` còn mang **một phát
biểu `P569` thứ hai ở dạng `somevalue`** (biết là có năm sinh, không biết năm nào). Tức Wikidata tự nó
không nhất quán về năm sinh Gerbert, chứ không chỉ "mạnh hơn mức nguồn cho phép". Nêu ra sẽ làm căn cứ
chọn `k. 945` chắc hơn.

---

## Khối 4 — Quy tắc 6 đảo chiều: Khúc Thừa Dụ thôi là "ứng viên bị loại", và bốn chỗ phải sửa theo

**Đã kiểm được (không có phát hiện)**
- Đếm lại **bốn chỗ**: (i) khối ứng viên Việt Nam của CE09, `content/ch05.md:1223`; (ii)
  `CH90-CE01_09-07`, `content/ch90.md:142`; (iii) `CH90-CE10_14-01`, `content/ch90.md:176`;
  (iv) danh sách bị loại cuối phụ lục, `content/ch90.md:687`. Đúng bốn, không thừa không thiếu.
- **Cả bốn chỗ đều đã mang chuỗi `CH05-CE10-05`**. `grep "Khúc Thừa Dụ" content/ch90.md` trả về đúng
  ba dòng trên cộng dòng quan hệ ở `:148`; không còn chỗ nào nêu ông mà thiếu liên kết.
- Chỗ (iv) còn ghi thẳng mục đích: *"Giữ dòng này để ghi lại quyết định, không phải để nêu ông làm người
  bị loại."* Đó đúng cách `CONTRIBUTING.md` quy tắc 6 yêu cầu xử lý.
- *"vì lint mù với nó"*: đọc hết `atlaslib/lint.py` (364 dòng). Lint **không** đọc nội dung
  `Vì sao chọn` ngoài phép đếm chữ, và phép kiểm duy nhất chạm tới Ghi chú biên tập là tìm chuỗi
  "viet"/"vietnam" cho D5 (`lint_chapter`). Không có phép kiểm nào đối chiếu tên người trong văn xuôi với
  danh sách mục. **Mệnh đề đúng.**

**BẮT BUỘC** — câu sai, nguyên văn: *"Khi ông có mục riêng thì cả bốn chỗ ấy vi phạm quy tắc 6, và vòng
này đã sửa cả bốn thành liên kết tới `CH05-CE10-05`."*

Sai ở đâu: câu tuyên bố một việc đã làm xong, trong khi **một trong bốn chỗ vẫn vi phạm sau khi sửa**, và
chính khối 6 của cùng Ghi chú biên tập nói vậy. `content/ch90.md:176` hiện đọc: *"**Ứng viên cạnh tranh**
là Dương Đình Nghệ, và Khúc Thừa Dụ — … nay có mục riêng ở `CH05-CE10-05`. Ngô Quyền được chọn theo
counterfactual (d): họ Khúc vẫn nhận danh nghĩa nhà Đường…"* Thêm liên kết **không** gỡ được việc ông
vẫn bị liệt kê là ứng viên cạnh tranh rồi bị xếp dưới bằng tiêu chí (d) — đúng cái quy tắc 6 cấm, và đúng
cái khối 6 gọi là *"Trạng thái ấy không được giữ nguyên"* (dòng 1248). `CONTRIBUTING.md:51` còn cho sẵn
câu mẫu phải dùng: *"có mục riêng ở nhóm X nên không phải ứng viên bị loại"* — chỗ (iv) dùng đúng mẫu ấy,
chỗ (iii) thì không.

Đề xuất câu thay thế nguyên văn:
> Khi ông có mục riêng thì cả bốn chỗ ấy vi phạm quy tắc 6. Vòng này đã thêm liên kết `CH05-CE10-05` vào cả bốn, nhưng **chỉ ba chỗ hết vi phạm**: `CH90-CE10_14-01` vẫn liệt ông là "ứng viên cạnh tranh" rồi xếp ông dưới Ngô Quyền bằng tiêu chí (d), nên nó còn mang đúng hình dạng mà quy tắc 6 cấm. Chỗ ấy phải sửa cùng với mâu thuẫn hai track bàn ở khối dưới, không sửa riêng được.

**NÊN** — *"Đây là lần đầu atlas gặp quy tắc 6 theo chiều ngược"*.

`[KHÔNG KIỂM ĐƯỢC]` theo nghĩa tuyệt đối — tôi không rà được toàn bộ lịch sử biên tập của ch01–ch04 để
loại trừ một ca tương tự đã xảy ra. Cái kiểm được: `reports/ch05-ce09-review-c.md` và `-d.md` không ghi ca
nào thuộc loại này, và `CONTRIBUTING.md:51` chỉ mô tả chiều xuôi (11 ca ở Ch3). Nên viết là *"lần đầu
được ghi lại"* thay vì *"lần đầu atlas gặp"*, để mệnh đề khớp đúng cái đã kiểm.

**CÂN NHẮC** — *"Quy trình ấy nên được ghi vào `CONTRIBUTING.md`"*. `CONTRIBUTING.md:51` **đã** gợi ý nửa
quy trình: *"Dò bằng script đối chiếu mọi tên trong 'Vì sao chọn' với `data/persons.json`."* Cái còn thiếu
đúng là chiều ngược — chạy phép dò ấy **sau** khi thêm mục mới, không chỉ trước. Nêu rõ phần đã có sẽ
biến kiến nghị thành một dòng sửa thay vì một mục viết mới.

---

## Khối 5 — Một đích tự do nay giải được, nhưng vòng này cố ý không nâng nó

**Đã kiểm được (không có phát hiện)**
- `CH90-CE01_09-07 · Phùng Hưng` **vẫn** có dòng `- Khúc Thừa Dụ · kế thừa · qua trường phái`
  (`content/ch90.md:148`), còn nguyên dạng văn bản tự do. Mô tả đúng.
- Chuỗi ấy quả thật nay giải được về `CH05-CE10-05`.
- Nâng nó sẽ tạo ra liên kết **phụ lục → mạch chính**, chiều hiện chưa có ví dụ nào trong repo:
  `grep "^- CH0[1-5]-" content/ch90.md` trả về **rỗng**.

**BẮT BUỘC** — câu sai, nguyên văn: *"vì nâng sẽ tạo ra một liên kết từ **phụ lục sang mạch chính** — tức
quyết định thay chủ dự án câu hỏi còn treo số 2."*

Sai ở đâu: câu hỏi còn treo số 2 hỏi **chiều ngược lại**. Nguyên văn
`HANDOFF-ce09-ce10.md:46`: *"2. Liên kết từ **mạch chính sang phụ lục** (vd `CH05-CE08-09 →
CH90-CE19_20-01`) có được phép không."* Đó là chỗ duy nhất trong repo có cụm "câu hỏi còn treo"
(`grep -n "treo"` trên `CONTRIBUTING.md`, `README.md`, `content/*.md`, `HANDOFF-ce09-ce10.md`). Hệ quả
thật: việc không nâng dòng Phùng Hưng **không** bị câu hỏi số 2 chặn, vì nó không thuộc câu hỏi ấy; và
chiều mà câu hỏi số 2 thật sự hỏi thì **đã có tiền lệ đang chạy** — `CH05-CE08-09 · Đỗ Phủ` trỏ sang
`CH90-CE19_20-01`, được lint chấp nhận (`reports/lint-ch05.txt:32`, mức INFO).

Đề xuất câu thay thế nguyên văn:
> vì nâng sẽ tạo ra liên kết đầu tiên theo chiều **phụ lục → mạch chính** — một chiều mà repo chưa có ví dụ nào, và mà câu hỏi còn treo số 2 của `HANDOFF-ce09-ce10.md` **chưa hỏi tới**: câu ấy chỉ hỏi chiều mạch chính → phụ lục, vốn đã có tiền lệ `CH05-CE08-09 → CH90-CE19_20-01` được lint chấp nhận. Vòng này hoãn vì chiều mới cũng là quyết định của chủ dự án, nên câu hỏi số 2 cần được mở rộng cho cả hai chiều trước khi ai sửa dòng ấy.

**BẮT BUỘC** — câu sai, nguyên văn (tiêu đề khối): *"**Một đích tự do nay giải được, nhưng vòng này cố ý
không nâng nó**"*.

Sai ở đâu: số đếm sai, và phần bị bỏ sót nằm ở chiều **không** bị treo. Vòng bình duyệt CE10 đã liệt kê
**ba** đích tự do giải được, không phải một (`reports/ch05-ce10-review.md:461`): dòng Phùng Hưng ở
`ch90`, cộng **hai đích ngay trong `CH05-CE10-05`** — Ngô Quyền → `CH90-CE10_14-01` và Phùng Hưng →
`CH90-CE01_09-07`. Hai đích sau chạy theo chiều mạch chính → phụ lục, tức chiều đã có tiền lệ, nên lý do
hoãn mà khối nêu không áp được cho chúng. Và việc ấy nay đã xảy ra: `content/ch05.md:928` và `:933` hiện
là `- CH90-CE01_09-07 · kế thừa · suy đoán học giả` và `- CH90-CE10_14-01 · kế thừa · qua trường phái`.
**Khối 5 đang mô tả một trạng thái repo không còn tồn tại.**

Đề xuất câu thay thế nguyên văn (tiêu đề + câu mở):
> **Ba đích tự do nay giải được; hai đã nâng, một thì hoãn — và lý do hoãn chỉ áp cho một**
> Vòng này giải được ba đích tự do về ID. Hai đích trong `CH05-CE10-05` chạy theo chiều mạch chính → phụ lục, chiều đã có tiền lệ `CH05-CE08-09 → CH90-CE19_20-01`, nên đã nâng: Ngô Quyền thành `CH90-CE10_14-01`, Phùng Hưng thành `CH90-CE01_09-07`. Đích thứ ba đi chiều ngược — dòng `- Khúc Thừa Dụ · kế thừa · qua trường phái` ở `CH90-CE01_09-07` (`content/ch90.md:148`) — và vòng này **không** nâng, vì chiều phụ lục → mạch chính chưa có tiền lệ nào trong repo.

**NÊN** — *"nếu câu hỏi ấy được trả lời 'có', sửa một dòng là xong."* Sau khi hai đích kia đã được nâng,
câu này còn đúng về số dòng nhưng sai về hệ quả: nâng dòng ấy sẽ làm `CH90-CE01_09-07` và `CH05-CE10-05`
trỏ vào nhau, tức sinh ra cặp quan hệ hai chiều **xuyên track** đầu tiên của atlas, và phép kiểm đối xứng
trong `lint_global` (`atlaslib/lint.py`) sẽ bắt đầu sinh INFO cho cả hai phía. Nên ghi kèm hệ quả ấy, vì
đó mới là cái chủ dự án phải quyết, chứ không phải công sức sửa.

---

## Khối 6 — Khúc Thừa Dụ ở mạch chính hay ở phụ lục: một câu hỏi về thang đo, không phải về con người

**Đã kiểm được (không có phát hiện)**
- Trích dẫn *"họ Khúc vẫn nhận danh nghĩa nhà Đường"* và *"938 là mốc mở đầu kỷ nguyên độc lập trong mọi
  cách phân kỳ sử Việt"*: **đúng nguyên văn** `content/ch90.md:176`.
- Mâu thuẫn hai track đo bằng cùng tiêu chí (d): khớp `reports/ch05-ce10-review.md:178`, kể cả cách diễn
  đạt *"không phải chuyện thang đo mà là chuyện nhất quán nội bộ"* và *"không được giữ nguyên"* (`:182`).
  Khối mô tả đúng cái vòng bình duyệt đã làm.
- **Số học của lối ra (b)**: `reports/stats.txt` ghi `Đông Nam Á 4 1.6%` trên 245 nhân vật atlas chính.
  Chuyển một người sang phụ lục → 3/244 = 1,229…% → **1,2%**. Tính tay lại: đúng cả hai con số.
- *"40 mục `ch90`"*: `reports/stats.txt` ghi `ch90 (40 nhân vật)`. Đúng.
- *"Việt Nam là vùng duy nhất có track song song"*: `content/ch90.md` là file phụ lục duy nhất, và
  `[ch90] Vùng — Đông Nam Á 40 100.0%`. Đúng.

**BẮT BUỘC** — câu sai, nguyên văn: *"con số Đông Nam Á toàn cục hiện **phụ thuộc vào một quyết định track
mà tiêu chí chưa được viết ra ở đâu** — không ở `CONTRIBUTING.md`, không ở `README.md`."*

Sai ở đâu: tiêu chí **có** ở `README.md`. Nguyên văn `README.md:15`: *"**Phụ lục Việt Nam dùng hệ quy chiếu
Việt Nam / Đông Nam Á**, không phải nhân loại, nên bị loại khỏi mọi thống kê toàn cục."* Nặng hơn: chính
khối này mở đầu bằng cùng một tiêu chí, viết lại gần như nguyên văn (*"ảnh hưởng của nhân vật Việt Nam
được đo trong phạm vi Việt Nam và Đông Nam Á, không phải toàn nhân loại"*), rồi ba câu sau tuyên bố nó
chưa được viết ở đâu. Cái **thật sự** thiếu là hẹp hơn nhiều: không có quy tắc nói một nhân vật Việt Nam
đạt thang đo toàn cầu thì vào track nào, và có được xuất hiện ở cả hai track không.

Đề xuất câu thay thế nguyên văn:
> Một hệ quả nữa phải đọc kèm: `README.md` có nêu tiêu chí track — phụ lục dùng hệ quy chiếu Việt Nam / Đông Nam Á, không phải nhân loại — nhưng **không** nói một nhân vật Việt Nam đạt thang đo toàn cầu thì thuộc track nào, và `CONTRIBUTING.md` cũng không. Con số Đông Nam Á toàn cục vì thế phụ thuộc vào đúng khoảng trống ấy. Việt Nam là vùng duy nhất có track song song, nên từ vòng này mỗi mục trong 40 mục `ch90` đều có một lập luận để đòi chuyển lên.

**BẮT BUỘC** — câu sai, nguyên văn: *"chuyển ông về `ch90`, và khi đó `Đông Nam Á` toàn cục tụt từ 4 người
(1,6%) xuống 3 (1,2%)."*

Sai ở đâu: hai tỉ lệ toàn cục viết ở thì hiện tại, không tự khai thời điểm đo — cùng loại vi phạm với
khối 1, và vi phạm đúng quy ước mà khối 13 đặt ra ở dòng 1271. Cả 1,6% và 1,2% đều đúng **hôm nay**
(mẫu số 245, rồi 244), nhưng CE11 sẽ đổi mẫu số và cả hai con số sẽ rữa cùng lúc mà không lint nào bắt
được. Số đếm người (4 → 3) thì không rữa; chỉ phần trăm rữa.

Đề xuất câu thay thế nguyên văn:
> hoặc (b) chuyển ông về `ch90`, và khi đó `Đông Nam Á` toàn cục tụt từ 4 người xuống 3 — **đo trên 245 mục atlas chính sau vòng CE10**, tức từ 1,6% xuống 1,2%.

**NÊN** — lối ra (a) của khối — *"giữ ông ở mạch chính và chuyển lập luận của `CH90-CE10_14-01` sang tiêu
chí (b)"* — khai thiếu một việc phải làm kèm. Sửa tiêu chí thôi chưa đủ: câu ở `content/ch90.md:176` còn
liệt Khúc Thừa Dụ vào cụm *"Ứng viên cạnh tranh"*, và đó là một vi phạm quy tắc 6 độc lập với chuyện tiêu
chí nào (xem khối 4). Lối ra (a) nên ghi là **hai sửa**, không phải một.

---

## Khối 7 — Vācaspati Miśra có thể không thuộc thế kỷ này, và chapter này có một chỗ nữa phải chỉnh theo

**Đã kiểm được (không có phát hiện)**
- *"đứng trên một niên hiệu duy nhất, trong *Nyāyasūcīnibandha*"* và hai cách đọc **841** / **976**:
  khớp thân mục `CH05-CE10-07` và khớp `reports/ch05-ce10-wikidata.md` (biên độ ~135 năm). Số học cũng
  khớp: 976 − 841 = 135, và chênh lịch Vikrama/Śaka đúng bằng 135 năm.
- *"nếu cách đọc kia đúng thì ông thuộc nhóm CE09"*: 841 nằm trong khung `CE09 · TK 9 (801 – 900)`. Đúng.
- *"Vòng này sửa câu ở mục Śaṅkara thành nói rõ mỏ neo ấy lỏng"*: **đã xảy ra**. `CH05-CE08-11` hiện đọc
  *"mỏ neo Vācaspati Miśra (`CH05-CE10-07`) thì lỏng hơn vẻ ngoài, vì niên đại của chính Vācaspati có hai
  cách đọc cách nhau 135 năm"* (`content/ch05.md:597`).
- *"chapter này có **một** chỗ nữa phải chỉnh theo"*: đếm lại toàn bộ `Vācaspati` trong `content/ch05.md`
  — dòng 597 (mục Śaṅkara), 954 (mục của chính ông), 1238 (khối 3), 1251 (khối này). Không có chỗ thứ hai
  dùng ông làm mỏ neo. **Số đếm đúng.**

**NÊN** — khối tự nhận là khai chỗ yếu niên đại nhưng dừng sớm hơn chính thân mục. `CH05-CE10-07` nay
viết thêm: *"cách đọc Śaka chỉ cho **một** con số — 976, niên đại soạn sách — nên khung 950–1000 là suy
ra, không phải đọc thẳng."* Tức ngay cả khi nhận cách đọc Śaka, khung `hoạt động k. 950–1000` vẫn là suy
diễn từ một mốc soạn sách duy nhất. Khối nên nêu tầng ấy, vì nó là lý do thật khiến `độ tin cậy niên đại`
phải là `Thấp` chứ không chỉ chuyện hai lịch.

**CÂN NHẮC** — *"mục `CH05-CE08-11 · Ādi Shankara` **trước đây** … ghi ông 'sớ cho ông ở nửa đầu thế kỷ 9'"*.
`[KHÔNG KIỂM ĐƯỢC]` — câu cũ không còn trong file và cũng không có trong `git show HEAD:content/ch05.md`
(bản commit đã mang câu đã sửa). Tôi xác minh được **kết quả** của việc sửa, không xác minh được **nguyên
văn bản nháp**. Nếu giữ câu này thì nên bỏ dấu ngoặc kép, vì nó đang trình bày một trích dẫn mà repo
không còn chứng cứ.

---

## Khối 8 — Atlas đã dựa vào al-Ṭabarī ba lần trước khi xét ông là một nhân vật

**Đã kiểm được (không có phát hiện)**
- **Ba mục, đúng ba**: `CH05-CE06-03` (`Ṭabarī, Tārīkh, quyển V, bản dịch C.E. Bosworth, SUNY Press, 1999`),
  `CH05-CE07-02` (`các quyển XII–XIV, bản dịch SUNY Press`), `CH05-CE07-03` (`các quyển XVI–XVII, bản dịch
  SUNY Press`). Quét toàn bộ trường `**Nguồn:**` của `content/ch05.md` không thấy mục thứ tư. Khớp cả
  `reports/ch05-ce10-wikidata.md` mục 6.3 và `CH05-CE10-01` (*"chính bộ dịch mà … đã dẫn"*).
- *"ba vòng liên tiếp"*: CE06 rồi CE07 (hai mục) — tức hai nhóm, ba mục. Cách viết *"ba vòng liên tiếp"*
  đếm theo vòng thì không khớp; xem CÂN NHẮC.
- Phép rà đề xuất (*"đếm tần suất tên người trong các trường `Nguồn`"*) hiện **không** tồn tại ở đâu trong
  repo: `atlaslib/lint.py` chỉ kiểm `Nguồn` có mặt hay không (`if not p["sources"]`). Kiến nghị là mới.

**BẮT BUỘC** — câu sai, nguyên văn: *"Đó là một điểm mù cùng họ với quy tắc 8: lint kiểm được ID trỏ sai,
nhưng không kiểm được rằng một cái tên xuất hiện nhiều lần ở trường `Nguồn` có thể đang đòi một mục."*

Sai ở đâu: **lint không kiểm được ID trỏ sai**, và quy tắc 8 nói đúng điều ngược lại với vế đầu câu này.
`HANDOFF-ce09-ce10.md:40` định nghĩa quy tắc 8: *"lint **mù** với liên kết trỏ đúng ID sai người, và mù
với việc nâng mức bằng chứng."* Đọc `atlaslib/lint.py`: phép kiểm duy nhất về đích liên kết là
`if C.ID_RE.match(t) and t not in all_persons: rep.warn(…, "liên kết tới ID chưa tồn tại")` — tức chỉ
kiểm ID **có tồn tại** hay không, cộng một phép kiểm tự trỏ (`t == p["id"]`), một vòng đối xứng hai chiều
ở mức INFO, và một phép kiểm nghịch niên đại. Không có phép nào biết ID trỏ **đúng người** hay không.
Đây đúng loại lỗi vòng CE09 đã bắt một lần: một khối mô tả sai phép kiểm của lint.

Đề xuất câu thay thế nguyên văn:
> Đó là một điểm mù cùng họ với quy tắc 8: lint chỉ kiểm được một ID liên kết **có tồn tại** hay không, chứ không kiểm được nó trỏ đúng người — và lại càng không kiểm được rằng một cái tên xuất hiện nhiều lần ở trường `Nguồn` có thể đang đòi một mục.

**CÂN NHẮC** — *"trong **ba vòng liên tiếp**, atlas dùng công trình của một người làm hạ tầng"*. Ba mục
nằm ở **hai** nhóm (CE06 một mục, CE07 hai mục), không phải ba vòng. Viết *"qua hai nhóm liên tiếp, ở ba
mục"* sẽ khớp bằng chứng mà không mất sức nặng của lập luận.

---

## Khối 9 — Ứng viên Việt Nam trong nhóm CE10 (yêu cầu D5)

**Đã kiểm được (không có phát hiện)**
- *"Lần đầu từ đầu Chapter 5, câu trả lời không phải 'không có ai'"*: đọc lại cả năm khối D5 của chapter —
  CE06 (`:1065`), CE07 (`:1138`), CE08 (`:1180`), CE09 (`:1222`), CE10 (`:1256`). Bốn khối đầu đều kết
  luận không có nhân vật Việt Nam nào vào **atlas chính** (CE08 kết bằng "cả ba đều đã có mục riêng trong
  phụ lục", vẫn là không có ai ở mạch chính). **Mệnh đề đúng.**
- **Quy tắc 6 cho hai cái tên bị loại**: `grep` "Khúc Hạo" và "Dương Đình Nghệ" trên `data/persons.json`
  và `content/` — **không ai trong hai người có mục ở bất kỳ chapter nào, kể cả `ch90`**. Danh sách
  `### ` của cả sáu file content không có dòng nào mang tên họ. Quy tắc 6 sạch.
- `CH90-CE10_14-01` tồn tại và là Ngô Quyền. Đúng.
- Yêu cầu D5 được thoả về mặt máy: `atlaslib/lint.py` kiểm Ghi chú biên tập có chứa chuỗi "viet"/"vietnam";
  khối này cung cấp.
- Niên đại nêu trong khối — Khúc Hạo cải cách k. 907–917, Dương Đình Nghệ khôi phục tự chủ 931 — khớp
  thân mục `CH05-CE10-05` (`- Khúc Hạo và cuộc cải cách hộ tịch – thuế khoá k. 907–917`) và khớp
  `content/ch90.md:176`. Về bản thân sự kiện lịch sử: `[KHÔNG KIỂM ĐƯỢC]` ở vòng này — tôi không mở được
  nguồn sơ cấp cho hai mốc ấy, chỉ xác nhận chúng nhất quán trong toàn repo.

**NÊN** — *"bị loại vì tiêu chí (d) — cải cách ấy chỉ thực hiện được trên nền quyền tự chủ cha ông đã
giành, nên chuỗi nhân quả quy về một mục là đủ, và **atlas ghi người mở chuỗi**."*

Nguyên tắc "atlas ghi người mở chuỗi" bị chính đoạn sau của khối phản bác: *"Điểm cuối thì đã có mục ở
phụ lục, `CH90-CE10_14-01`."* Tức cùng một chuỗi nhân quả đang có **hai** mục trong atlas — điểm mở ở
mạch chính và điểm cuối ở phụ lục — còn mắt giữa thì bị loại bằng lý lẽ "chỉ ghi người mở chuỗi".
Nguyên tắc như đang phát biểu không giải thích được tại sao Ngô Quyền vào được. Lý do thật là **hai track
đo bằng hai hệ quy chiếu**, và đó đúng là chỗ khối 6 đang treo. Nên viết nguyên tắc cho đúng phạm vi:
> bị loại vì tiêu chí (d) — cải cách ấy chỉ thực hiện được trên nền quyền tự chủ cha ông đã giành, nên ở **thang đo toàn cầu** chuỗi nhân quả quy về một mục là đủ, và mạch chính ghi người mở chuỗi. Điểm cuối của chuỗi có mục riêng ở phụ lục, `CH90-CE10_14-01`, vì phụ lục đo bằng hệ quy chiếu khác.

**CÂN NHẮC** — khối không nhắc rằng **Dương Đình Nghệ cũng đang bị nêu làm "ứng viên cạnh tranh" ở
`content/ch90.md:176`**. Ông không vi phạm quy tắc 6 (không có mục ở đâu cả — tôi đã kiểm), nhưng việc
cùng một người bị loại ở cả hai track vì hai lý do khác nhau là dữ kiện đáng ghi nửa dòng, đúng tinh thần
khối 6.

---

## Khối 10 — Ba ô vùng trống của nhóm này, và một ứng viên bị loại vì niên đại chứ không vì chất lượng

**Đã kiểm được (không có phát hiện)**
- **Ba ô thật sự bằng 0 ở nhóm CE10**: đọc 12 trường `vùng:` — Trung Đông/Bắc Phi ×3, Trung Á ×1,
  Đông Nam Á ×2, Nam Á ×1, Đông Á ×3, Châu Âu ×2. `Châu Mỹ`, `Châu Phi hạ Sahara`, `Châu Đại Dương` = 0.
  Đúng.
- **Gudit là ứng viên Châu Phi hạ Sahara duy nhất của hồ sơ cổng**: rà cả 14 ứng viên trong
  `reports/ch05-ce10-wikidata.md` — không có tên nào khác thuộc vùng ấy. Đúng.
- `Q1270024` `P569 = +0950` ở **`precision` 7**: tôi tra lại trực tiếp, **đúng**. Và đúng là cùng dạng bẫy
  với `Q1001807` (`+0801` p7).
- Ba tầng lý do Châu Đại Dương của khối CE08 (`content/ch05.md:1177`) còn nguyên văn, không bị sửa ở
  vòng này.
- ʻAhoʻeitu *"thuộc đúng thế kỷ này"*: khối CE09 (`:1219`) viết *"Niên đại truyền thống đặt ông ở **thế kỷ
  10**, tức thuộc CE10 chứ không thuộc nhóm này."* Khớp. Và đúng là ở CE10 chỉ còn tầng (3) chặn, vì lý do
  thứ nhất của khối CE09 là sai thế kỷ, nay tự tiêu. Suy luận của khối đứng vững.

**NÊN** — câu sai (thiếu chính xác), nguyên văn: *"và không có `P570` nào cả"*.

`Q1270024` **có** một phát biểu `P570`, nhưng ở dạng `somevalue` — tức Wikidata khẳng định bà đã chết mà
không khai năm nào. Khác với `Q47684` (Mpu Sindok), nơi `P569` **vắng mặt hoàn toàn` — và khối 3 dùng đúng
chữ "không có `P569` nào" cho ca ấy. Hai ca khác loại mà khối dùng cùng một cách diễn đạt. Hệ quả thực:
`somevalue` vẫn đi qua `atlaslib/lint.py` như không có giá trị (`if it["year"] is None: continue`), nên kết
luận không đổi — nhưng câu thì nên đúng:
> `P569` của bà là `+0950` ở `precision` **7**, tức đệm thế kỷ như ca Khúc Thừa Dụ, còn `P570` chỉ có một phát biểu `somevalue` — khẳng định bà đã chết mà không khai năm nào

**NÊN** — câu sai (thiếu một dữ kiện làm đổi kết luận), nguyên văn: *"Với Châu Mỹ, hồ sơ cổng không đưa ra
được ứng viên nào có niên đại neo được."*

Hồ sơ cổng **có** đưa ra một tên cho Châu Mỹ và tự đánh dấu là **chưa xong**:
`reports/ch05-ce10-wikidata.md` mục 4 ghi `Topiltzin Quetzalcoatl` trong số bốn ứng viên *"không resolve
được bằng tiêu đề Wikipedia tiếng Anh đã thử"*, kèm nguyên văn *"Chưa kết luận là không có — phải tra lại
bằng dạng tên khác trước khi loại. **[CHƯA KẾT LUẬN]**"*. Câu của khối biến một việc **chưa làm** thành một
kết quả rà. Vòng CE11 đọc câu này sẽ tưởng Châu Mỹ đã được quét sạch.

Đề xuất câu thay thế nguyên văn:
> Với Châu Mỹ, hồ sơ cổng để lại một việc chưa xong chứ không một kết luận: `Topiltzin Quetzalcoatl` không resolve được về thực thể Wikidata nào bằng các dạng tên đã thử, và hồ sơ ghi rõ `[CHƯA KẾT LUẬN]` — phải tra lại bằng dạng tên khác trước khi loại. Nhóm này không làm việc ấy, nên ô Châu Mỹ bằng 0 là một ô **chưa rà**, không phải một ô đã rà và trống. Nền cảnh thì đúng: giai đoạn hậu Chichén ở vùng đất thấp Maya là giai đoạn bi ký thưa dần.

**CÂN NHẮC** — khối rút gọn ca ʻAhoʻeitu xuống còn tầng (3), nhưng khối CE09 còn ghi một trở ngại thao tác
mà khối này bỏ: `Q1245849` khai `P31 = Q6949213` ("mythological king"), không phải `Q5`, nên ông vào atlas
thì **bắt buộc mang nhãn** và sẽ kích hoạt cảnh báo `P31` trong `lint_wikidata`. Đó không phải lý do loại
(atlas nhận nhân vật truyền thuyết), nhưng là việc phải làm kèm, và nó sẽ bị quên nếu khối CE10 là chỗ
cuối cùng ai đọc.

---

## Khối 11 — `Khoa học tự nhiên` bằng 0 hai nhóm liên tiếp, và lần này không đổ cho thế kỷ được

**Đã kiểm được (không có phát hiện)**
- **CE10 đúng là 0 ô `Khoa học tự nhiên`**: đọc 12 trường `lĩnh vực:`, không mục nào mang nhãn ấy
  (`-02` là `Y học, Triết học`). Đúng.
- **CE09 đã khai ô này trống và quy cho người chọn**: `content/ch05.md:1214` viết *"`Khoa học tự nhiên` và
  `Giáo dục` **bằng 0**, và ở đây không có biện hộ"*, kèm hai cái tên bị loại (al-Kindī, al-Farghānī) và
  lý do (trần 12, cân vùng). Khớp đúng.
- Lập luận *"cả hai lần đều có ứng viên"* vì thế đứng được: CE09 nêu đích danh hai người, CE10 nêu
  al-Masʿūdī.
- al-Masʿūdī **mất 957**: khớp `reports/ch05-ce10-wikidata.md` mục 5 (`Q168705` 896 → 957).
- *"Mục `CH05-CE10-01` nêu al-Masʿūdī làm ứng viên cùng ô bị cắt"*: đúng nguyên văn.
- Khối không chứa tỉ lệ phần trăm nào, nên **không vi phạm quy ước của khối 13**. Đây là khối duy nhất
  nêu số liệu mà tự tránh được chỗ rữa — bằng cách chỉ dùng số đếm 0.

**NÊN** — *"ông bị cắt **hai lần** — một lần ở ô `Sử học` vì al-Ṭabarī, một lần ở ô `Khoa học tự nhiên` vì
không ai trong nhóm này chịu nhường suất."*

"Lần cắt thứ hai" chưa có chỗ dựa trong repo. `CH05-CE10-01` chỉ nêu ông là ứng viên bị cắt **cùng ô**
với al-Ṭabarī, tức ô `Sử học`; không mục nào, và không hồ sơ nào, từng xét ông cho ô `Khoa học tự nhiên`.
Hồ sơ cổng xếp ông ở mục "ứng viên sạch" mà không gán lĩnh vực. Mô tả của chính khối — *"vừa chép sử vừa
ghi chép địa lý và vật lý tự nhiên"* — trỏ mạnh hơn về `Khám phá/Địa lý` (cũng đang mỏng, 8 mục) chứ không
về `Khoa học tự nhiên`. Nói "bị cắt hai lần" làm một suy diễn thành một sự việc.

Đề xuất câu thay thế nguyên văn:
> Mục `CH05-CE10-01` nêu al-Masʿūdī làm ứng viên bị cắt ở ô `Sử học`, nhưng nói cho đủ thì ông còn là ứng viên **khả dĩ** cho một ô khác mà không vòng nào xét tới: phần địa lý và ghi chép tự nhiên của *Murūj al-dhahab* đáng được cân cho `Khám phá/Địa lý` hoặc `Khoa học tự nhiên`, và nhóm này không cân.

**NÊN** — *"và có cả lớp thiên văn Buyid ở Baghdad"*: khối khuyến nghị CE11 coi đây là ràng buộc nhưng
không để lại một cái tên nào tra được, trong khi hồ sơ cổng **có sẵn một tên đúng ô và đang treo**:
`Abu al-Wafa' Buzjani` nằm trong bốn ứng viên `[CHƯA KẾT LUẬN]` ở mục 4 của
`reports/ch05-ce10-wikidata.md`, chưa resolve được về QID. Nêu đích danh sẽ biến lời khuyên thành một việc
làm được, và `al-Muqaddasi` ở cùng danh sách cũng là một tên cho ô `Khám phá/Địa lý`.

**CÂN NHẮC** — *"Nhóm CE09 đã khai ô này trống"* đúng, nhưng CE09 khai **hai** ô trống, `Khoa học tự
nhiên` **và** `Giáo dục`. CE10 đã lấp `Giáo dục` (`CH05-CE10-12 · Gerbert`). Nói ra một câu sẽ cho thấy
khuôn này là khuôn của **một** ô cụ thể, không phải một thói quen bỏ ô — tức làm lập luận "đây là một
khuôn, không phải một sự cố" chặt hơn chứ không lỏng đi.

---

## Khối 12 — Những người bị cắt, và lý do của từng người

**Đã kiểm được (không có phát hiện)**
- **Số tên: chín, không phải tám** — al-Ashʿarī, Saadia Gaon, al-Masʿūdī, Ḥasdai ibn Shaprut, Dunash ben
  Labrat, Rajaraja I, Sei Shōnagon, Abhinavagupta, Hrotsvitha. (Khối không tự nêu con số nào, nên đây
  không phải lỗi của khối; ghi lại vì đề bài vòng này giả định tám.)
- **Quy tắc 6 cho cả chín người**: `grep` từng tên trên `data/persons.json` và trên mọi dòng `### ` của
  sáu file `content/*.md`. **Không ai trong chín người có mục ở bất kỳ chapter nào, kể cả `ch90`.**
  Những chỗ tên họ xuất hiện đều là văn xuôi hoặc dòng quan hệ tự do, không phải mục. Quy tắc 6 sạch.
- *"ô `Tôn giáo/Tâm linh` của nhóm đã có bốn mục"*: đếm tay — `-01`, `-06`, `-09`, `-11`. Đúng bốn.
- *"Trung Đông đã giữ ba suất"*: `-01`, `-02`, `-03`. Đúng ba.
- *"nhóm đã có một suất Córdoba"*: `-11 · ʿAbd al-Raḥmān III`, nơi ghi *"Córdoba và Madīnat al-Zahrāʾ"*.
  Đúng một.
- *"dòng `Ảnh hưởng tới` tự do mang tên ông ở `CH05-CE09-11` vì vậy **vẫn giữ nguyên dạng văn bản tự do**"*:
  **kiểm được và đúng** — `CH05-CE09-11` hiện còn `- Abhinavagupta và bình chú Locana · kế thừa · trực tiếp`.
  Đây là một trong ít mệnh đề "đã/chưa làm" của cả 13 khối mà trạng thái file khớp chính xác.
- Niên đại của bốn người có ghi năm đều khớp `reports/ch05-ce10-wikidata.md`: Saadia Gaon 882–942
  (`Q328748`), Rajaraja I 947–1014 (`Q2128757`), Sei Shōnagon 966–1025 (`Q231603`), Abhinavagupta
  k. 950–1016 (khớp cách ghi ở `CH05-CE09-11`; `Q320619` ghi 950–1020).
- *"Atlas không có trường giới tính nên không thống kê được tỉ lệ"*: đúng — dòng metadata chỉ có
  `năm / nơi / vùng / lĩnh vực / độ tin cậy niên đại / wikidata / câu hỏi lớn`, và `reports/stats.txt`
  không có mục nào theo giới.

**NÊN** — câu sai, nguyên văn: *"nhưng tác phẩm của bà thất truyền cho tới khi Conrad Celtis tìm lại năm
1501"*.

Năm 1501 là năm **bản in đầu tiên** (Nuremberg, có minh hoạ của Dürer), không phải năm tìm lại. Bản chép
tay Emmeram được Celtis tìm thấy ở tu viện St. Emmeram, Regensburg, khoảng **1493–1494**. Nguồn tham chiếu
phổ thông cũng ghi cả hai mốc cạnh nhau — tôi không mở được nghiên cứu chuyên ngành về truyền bản
Hrotsvitha, nên mốc 1493–1494 ở đây là `[KHÔNG KIỂM ĐƯỢC]` ở mức nguồn sơ cấp — nên 1501 không phải bịa — nhưng gộp hai mốc thành một làm hỏng
đúng cái lập luận mà khối đang dựng: khoảng cách truyền bản. Đề nghị:
> nhưng tác phẩm của bà thất truyền cho tới khi Conrad Celtis tìm được bản chép tay ở St. Emmeram khoảng 1493–1494 và cho in năm 1501

**NÊN** — tiêu đề khối hứa *"lý do của **từng người**"* và câu mở hứa *"để vòng duyệt khỏi phải đoán"*,
nhưng bốn ứng viên của hồ sơ cổng **không có lý do nào được ghi ở đâu**: `Topiltzin Quetzalcoatl`,
`Ibn Fadlan`, `Abu al-Wafa' Buzjani` và `al-Muqaddasi` nằm ở mục 4 của
`reports/ch05-ce10-wikidata.md` với trạng thái `[CHƯA KẾT LUẬN]` và lời dặn *"phải tra lại bằng dạng tên
khác trước khi loại"*. Họ không vào nhóm, và không khối nào nói vì sao. Hai trong bốn người ấy lại đúng
vào hai ô mà khối 10 và khối 11 đang than trống (`Châu Mỹ`, `Khoa học tự nhiên`). Đề nghị thêm một câu
cuối khối:
> Và bốn cái tên nữa phải ghi là **chưa xử xong**, không phải đã cắt: `Topiltzin Quetzalcoatl`, `Ibn Fadlan`, `Abu al-Wafa' Buzjani`, `al-Muqaddasi` — hồ sơ cổng không resolve được QID cho họ và đánh dấu `[CHƯA KẾT LUẬN]`, vòng này không tra lại, nên lý do họ vắng mặt là một việc bỏ dở chứ không phải một phán đoán.

**CÂN NHẮC** — *"**al-Ashʿarī** (874–936)"*: hồ sơ cổng ghi `Q316349` khai **873–935**, tức lệch một năm ở
cả hai đầu, và chính hồ sơ gọi đó là *"dấu hiệu điển hình của quy đổi AH→CE bằng công thức"*. Khối dùng
cặp số của học giới (đúng), nhưng không ghi rằng Wikidata nói khác. Nếu CE11 nhặt ông lên, người viết sẽ
gặp lại đúng bẫy ấy mà không được cảnh báo. Với **Hrotsvitha** thì ngược lại: hồ sơ cổng cảnh báo
`P570 = 968` nhiều khả năng sai (bà còn viết sau 973) và đề nghị ghi `hoạt động k. 960–975`; khối cho bốn
người khác có niên đại mà không cho bà, nên cảnh báo ấy rơi mất.

---

## Khối 13 — Hai việc ở tầng chapter mà vòng bình duyệt CE10 chỉ ra, ghi lại cho P4

**Đã kiểm được (không có phát hiện)**
- Ý *Một* (thể thức ứng viên bị loại) và ý *Hai* (`trực tiếp` hai nghĩa) đúng là hai phát hiện tầng nhóm
  của `reports/ch05-ce10-review.md` (`:458` và `:459`), diễn đạt lại trung thực phần lõi.
- *"Lint không phân biệt được"* mức bằng chứng: đúng. `atlaslib/lint.py` chỉ kiểm
  `l["evidence"] not in C.EVIDENCE_LEVELS`, tức có trong từ vựng hay không. Không có phép kiểm ngữ nghĩa.
  Khớp quy tắc 8 ở `HANDOFF-ce09-ce10.md:40` (*"mù với việc nâng mức bằng chứng"*).
- *"một con số viết ở thì hiện tại sẽ sai sau vòng sau mà không lint nào bắt được"*: đúng; lint không đọc
  văn xuôi Ghi chú biên tập ngoài phép tìm chuỗi "viet"/"vietnam".
- **Hai ca đã sửa, kiểm được cả hai**: (a) khối Châu Mỹ (`content/ch05.md:1201–1202`) nay không còn một
  con số nào — *"Con số ở ô Châu Mỹ vì thế không đo lịch sử châu Mỹ"* là câu duy nhất nhắc tới con số, và
  nó không nêu giá trị; (b) khối lĩnh vực CE09 (`:1214`) nay đọc *"trong khi toàn atlas **khi ấy** ở
  23,4%"*. Cả hai mệnh đề của khối đều đúng.
- *"hơn bốn trăm hai mươi năm"*: `CH05-CE06-12 · Boethius` ghi `k. 477 – k. 526`, `CH05-CE10-12 · Gerbert`
  ghi `k. 945–1003`. Khoảng cách theo số liệu của chính atlas là ~419 năm; vòng bình duyệt dùng 524 nên ra
  421. Xem CÂN NHẮC.

**BẮT BUỘC** — câu sai, nguyên văn (tiêu đề khối): *"**Hai việc ở tầng chapter mà vòng bình duyệt CE10 chỉ
ra, ghi lại cho P4**"*.

Sai ở đâu: thân khối có **ba** việc, đánh số rành mạch *"Một,"* (dòng 1269), *"Hai,"* (1270), *"Ba,"*
(1271). Tiêu đề đếm sai chính nội dung nằm dưới nó. Việc thứ ba không phải phần phụ — nó là chỗ đặt ra
quy ước mà bốn khối khác phải tuân.

Đề xuất câu thay thế nguyên văn:
> **Ba việc ở tầng chapter mà vòng bình duyệt CE10 chỉ ra, ghi lại cho P4**

**BẮT BUỘC** — câu sai, nguyên văn: *"tỉ lệ làm được trong Chapter 5 là CE07 12/12, CE09 4/12, CE10 3/12.
Đây không phải lỗi của một nhóm mà là một **đường dốc qua ba vòng**"*, cùng với tiêu đề ý *Một*:
*"thể thức nêu ứng viên bị loại đang **trượt dốc đều**"*.

Sai ở đâu: dãy số bị cắt mất hai điểm, và hai điểm bị cắt là hai điểm phá hình dạng "dốc đều". Nguồn mà
khối dẫn ghi đủ năm điểm — `reports/ch05-ce10-review.md:458`: *"CE07 đạt 12/12, CE06 8/12, CE08 6/12,
CE09 4/12, CE10 3/12."* Xếp theo thời gian: **CE06 8/12 → CE07 12/12 → CE08 6/12 → CE09 4/12 → CE10 3/12**.
Đó là một đỉnh ở CE07 rồi mới xuống, không phải một dốc đều, và CE07 không phải điểm khởi đầu của bất kỳ
dốc nào. Thêm nữa: con số **3/12 nay đã rữa**. Sau khi các mục CE10 được áp bình duyệt trong hôm nay,
`CH05-CE10-06` nêu Rajendravarman II và `CH05-CE10-09` nêu Cung Duệ với Chân Huyên, nên số mục có nêu
đích danh ứng viên cùng ô đã lên **ít nhất 5/12**. Đây là ca minh hoạ sống cho chính quy ước mà ý *Ba*
của khối đặt ra ba dòng bên dưới.

Đề xuất câu thay thế nguyên văn:
> Một, **thể thức nêu ứng viên bị loại không ổn định và đang ở mức thấp**. Template §5 yêu cầu mỗi mục nêu đích danh ứng viên bị loại cùng ô; đo trên Chapter 5 **trước khi áp bình duyệt CE10**, tỉ lệ là CE06 8/12, CE07 12/12, CE08 6/12, CE09 4/12, CE10 3/12 — một đỉnh ở CE07 rồi bốn vòng dưới mức ấy, chứ không phải một dốc đều. Đây không phải lỗi của một nhóm, nên phải xử ở tầng chapter chứ không vá từng mục. Nhóm CE10 bù bằng một khối riêng liệt kê người bị cắt ở Ghi chú biên tập, nhưng đó là bù chứ không phải thay.

**BẮT BUỘC** — câu sai, nguyên văn: *"`CH05-CE10-12 · Gerbert` kế thừa `CH05-CE06-12 · Boethius` ở mức
`trực tiếp` qua một khoảng cách **hơn bốn trăm hai mươi năm**, trong khi **các dòng `trực tiếp` khác chỉ
người thật sự gặp nhau**."*

Sai ở đâu: vế sau sai, và nguồn mà khối đang dẫn nói ngược. `reports/ch05-ce10-review.md:459` ghi rõ
**năm dòng** trong chính nhóm CE10 dùng `trực tiếp` cho quan hệ văn bản xuyên thế kỷ, và Gerbert chỉ là
một trong năm. Tôi đếm lại toàn bộ nhóm: **19 dòng `trực tiếp`**, trong đó phần lớn không thể là người
gặp nhau — `CH05-CE10-01` kế thừa *"Ibn Isḥāq và al-Wāqidī, hai người soạn sīra và maghāzī thế kỷ 8"*
(Ibn Isḥāq mất 767, al-Ṭabarī sinh 839); `CH05-CE10-01` ảnh hưởng tới *"Balʿamī và bản rút gọn tiếng Ba
Tư k. 963"* (ông mất 923); `CH05-CE10-02` ảnh hưởng tới *"Bản dịch Latin *Continens* (1279)"*;
`CH05-CE10-03` ảnh hưởng tới Ibn Sīnā (sinh 980, al-Fārābī mất 950); `CH05-CE10-07` kế thừa Uddyotakara
(cách khoảng ba thế kỷ). Và một loạt dòng `trực tiếp` khác trỏ vào **thể chế hoặc truyền thống**, không
trỏ vào người: *"Thể chế tiết độ sứ của nhà Đường"*, *"Truyền thống *Vạn diệp tập*"*, *"Nhánh Umayyad
lưu vong lập tiểu quốc Córdoba năm 756"*. Chỉ khoảng ba dòng trong nhóm là người thật sự gặp nhau
(`-04` phản bác ʿAmr ibn al-Layth, `-05` ảnh hưởng tới Khúc Hạo, `-11` phản bác nhà Fatimid).

Đề xuất câu thay thế nguyên văn:
> Hai nghĩa ấy nằm cạnh nhau trong cùng một nhóm, và nghĩa văn bản mới là nghĩa chiếm đa số: trong 19 dòng `trực tiếp` của nhóm CE10, chỉ khoảng ba dòng chỉ người thật sự gặp nhau, còn lại là quan hệ văn bản hoặc là đích không phải người. Ca xa nhất là `CH05-CE10-12 · Gerbert` kế thừa `CH05-CE06-12 · Boethius` qua khoảng **bốn trăm hai mươi năm**. Lint không phân biệt được, nên `CONTRIBUTING.md` cần một định nghĩa, và nếu định nghĩa chọn nghĩa người–người thì một loạt dòng trong Chapter 5 phải hạ xuống `qua trường phái`.

**BẮT BUỘC** — ý *Ba* đặt ra quy ước *"con số trong ghi chú biên tập phải tự khai nó đo ở thời điểm nào,
hoặc không nêu số"* nhưng **chính vòng đặt quy ước đã vi phạm nó hai lần**, và cả hai nằm trong mười hai
khối CE10: khối 1 nêu *"23,8% của toàn atlas"* ở thì hiện tại (dòng 1232), khối 6 nêu *"4 người (1,6%)
xuống 3 (1,2%)"* ở thì hiện tại (dòng 1248). Cả ba con số hiện đúng theo `reports/stats.txt` (mẫu số 245),
và cả ba sẽ sai sau CE11. Một quy ước được công bố cùng lúc với hai ca vi phạm chưa sửa thì vòng sau sẽ
đọc nó như một lời khuyên.

Đề xuất câu thêm vào cuối ý *Ba*:
> Quy ước nên giữ từ đây: con số trong ghi chú biên tập phải tự khai nó đo ở thời điểm nào, hoặc không nêu số. Và phải áp ngược lại ngay trong vòng này: hai con số toàn cục còn ở thì hiện tại — `23,8%` ở khối người cai trị và `1,6% → 1,2%` ở khối thang đo Khúc Thừa Dụ — cùng đo trên 245 mục atlas chính sau vòng CE10, nên phải ghi kèm mốc ấy.

**NÊN** — *"hơn bốn trăm hai mươi năm"*. Theo số liệu của chính atlas — Boethius `k. 477 – k. 526`,
Gerbert `k. 945–1003` — khoảng cách là **~419 năm**, tức chưa "hơn bốn trăm hai mươi". Vòng bình duyệt ra
421 vì dùng năm mất 524, vốn khác năm mà mục Boethius ghi. Một ghi chú biên tập không nên mâu thuẫn với
trường `năm:` của chính atlas; viết *"khoảng bốn trăm hai mươi năm"* là khớp cả hai cách tính.

**CÂN NHẮC** — khối tự giới thiệu là *"vòng bình duyệt CE10 chỉ ra"*, nhưng ý *Ba* (tỉ lệ phần trăm rữa)
không có trong `reports/ch05-ce10-review.md` — tôi không tìm thấy mục nào của báo cáo ấy nêu nó. Đó có vẻ
là phát hiện của chính vòng viết, và ghi công cho vòng bình duyệt làm sai đường truy vết. Nên tách:
hai việc từ vòng bình duyệt, một việc tự tìm.

---

## Tổng kết

### Bảng đếm theo từng khối

| Khối | Tên rút gọn | BẮT BUỘC | NÊN | CÂN NHẮC |
|---|---|---:|---:|---:|
| 1 | Sáu người cai trị trong mười hai | 3 | 1 | 1 |
| 2 | Mục sát ranh giới nhất: Ismāʿīl Samānī | 1 | 1 | 1 |
| 3 | Sáu bẫy niên đại Wikidata | 1 | 2 | 1 |
| 4 | Quy tắc 6 đảo chiều | 1 | 1 | 1 |
| 5 | Một đích tự do nay giải được | 2 | 1 | 0 |
| 6 | Khúc Thừa Dụ ở mạch chính hay phụ lục | 2 | 1 | 0 |
| 7 | Vācaspati Miśra có thể không thuộc thế kỷ này | 0 | 1 | 1 |
| 8 | Atlas đã dựa vào al-Ṭabarī ba lần | 1 | 0 | 1 |
| 9 | Ứng viên Việt Nam trong nhóm CE10 (D5) | 0 | 1 | 1 |
| 10 | Ba ô vùng trống của nhóm này | 0 | 2 | 1 |
| 11 | `Khoa học tự nhiên` bằng 0 hai nhóm liên tiếp | 0 | 2 | 1 |
| 12 | Những người bị cắt | 0 | 2 | 1 |
| 13 | Hai việc ở tầng chapter | 4 | 1 | 1 |
| **Tổng** | | **15** | **16** | **11** |

### Gom lỗi BẮT BUỘC theo loại

**A. Khối này mâu thuẫn với khối kia trong cùng Ghi chú biên tập — 4 lỗi.**
Đây là hình dạng áp đảo của vòng này, và nó khác hẳn vòng soi 12 mục (nơi lỗi chính là "lần đầu / sớm
nhất" có phản ví dụ). Ở đây các khối được viết ở các thời điểm khác nhau rồi đặt cạnh nhau mà không ai
đọc chéo.
- Khối 1 nói `CH05-CE10-04` lập *"nhà nước Transoxiana **độc lập khỏi Baghdad**"*; khối 2 và thân mục nói
  ông vẫn nhận sắc phong và gửi cống về Baghdad.
- Khối 4 tuyên bố **đã sửa xong** cả bốn chỗ vi phạm quy tắc 6; khối 6 nói chỗ thứ ba vẫn ở trạng thái
  *"không được giữ nguyên"*.
- Khối 6 nói tiêu chí track *"chưa được viết ra ở đâu cả"*; câu mở của **chính khối 6** phát biểu tiêu chí
  ấy, và `README.md:15` có nó.
- Khối 1 và khối 6 nêu tỉ lệ toàn cục ở thì hiện tại; khối 13 cấm đúng việc đó.

**B. Mô tả sai một tài liệu trong repo — 4 lỗi.**
- Khối 3: "sáu bẫy" của khối không trùng "sáu bẫy" của `reports/ch05-ce10-wikidata.md`; hai bẫy gốc
  (`Q316349`, `Q170248`) chưa được xác nhận lại ở vòng nào.
- Khối 5: *"câu hỏi còn treo số 2"* ở `HANDOFF-ce09-ce10.md:46` hỏi chiều **mạch chính → phụ lục**, không
  phải chiều mà khối đang bàn — và chiều nó hỏi thì đã có tiền lệ đang chạy.
- Khối 13 ý *Một*: dãy `CE07 12/12, CE09 4/12, CE10 3/12` cắt mất hai điểm của nguồn nó dẫn
  (`reports/ch05-ce10-review.md:458`), và hai điểm bị cắt là hai điểm phá hình dạng "dốc đều".
- Khối 13 ý *Hai*: *"các dòng `trực tiếp` khác chỉ người thật sự gặp nhau"* — nguồn nó dẫn nêu năm dòng
  ngược lại ngay trong cùng nhóm; đếm lại được 19 dòng `trực tiếp`, chỉ khoảng ba là người gặp nhau.

**C. Mô tả sai phép kiểm của lint — 1 lỗi (lỗi tái phát, vòng CE09 đã bắt một ca cùng loại).**
- Khối 8: *"lint kiểm được ID trỏ sai"*. `atlaslib/lint.py` chỉ kiểm ID **có tồn tại**; quy tắc 8 ở
  `HANDOFF-ce09-ce10.md:40` nói thẳng lint **mù** với liên kết trỏ đúng ID sai người.

**D. Mệnh đề quá rộng mà phản ví dụ nằm trong chính danh sách của nó — 2 lỗi.**
- Khối 1: *"Sáu mục vua … đều được chỉ mục vì **thể chế chính họ lập**"*, trong khi `-05` nhận một chức
  của nhà Đường và `-06` được gắn với một sự kiện dời đô.
- Khối 2: al-Tirmidhī (mất 892) không thể làm ứng viên thay thế cho một suất khung 901–1000, và thân mục
  `CH05-CE10-04` nói đúng điều đó.

**E. Số đếm / tiêu đề sai — 2 lỗi.**
- Khối 13: tiêu đề *"Hai việc"*, thân khối có ba.
- Khối 5: tiêu đề *"Một đích tự do"*, thực tế ba — và hai trong ba **đã được nâng** trong lúc vòng này
  chạy, nên khối đang mô tả một trạng thái repo không còn tồn tại.

### Mọi chỗ `[KHÔNG KIỂM ĐƯỢC]`

1. **Khối 4** — *"Đây là lần đầu atlas gặp quy tắc 6 theo chiều ngược."* Tôi không rà được lịch sử biên
   tập của ch01–ch04 để loại trừ một ca tương tự. Kiểm được phần yếu hơn: không báo cáo bình duyệt nào
   trên đĩa ghi ca cùng loại, và `CONTRIBUTING.md:51` chỉ mô tả chiều xuôi.
2. **Khối 7** — nguyên văn câu cũ ở `CH05-CE08-11` (*"sớ cho ông ở nửa đầu thế kỷ 9"*). Câu đã bị thay
   trước commit hiện tại; `git show HEAD:content/ch05.md` đã mang bản đã sửa. Kiểm được **kết quả** sửa,
   không kiểm được **nguyên văn bản nháp**.
3. **Khối 9** — hai mốc lịch sử: cải cách hộ tịch – thuế khoá của Khúc Hạo k. 907–917, và việc Dương Đình
   Nghệ khôi phục quyền tự chủ năm 931. Tôi không mở nguồn sơ cấp nào ở vòng này; chỉ xác nhận hai mốc
   nhất quán giữa `content/ch05.md` và `content/ch90.md`.
4. **Khối 12** — mốc Conrad Celtis: tôi đối chiếu được hai mốc 1493/94 (tìm bản chép tay) và 1501 (bản in)
   trong tài liệu tham khảo phổ thông, nhưng **không** mở được nghiên cứu chuyên ngành về truyền bản
   Hrotsvitha. Kết luận "1501 là năm in, không phải năm tìm lại" ở mức NÊN chứ không BẮT BUỘC vì vậy.

### Ba việc nên làm trước khi vòng CE11 bắt đầu

1. **Đọc chéo mười ba khối một lượt.** Bốn trong mười lăm lỗi BẮT BUỘC là mâu thuẫn giữa khối với khối,
   và không lỗi nào trong số đó cần tra cứu bên ngoài để thấy.
2. **Cập nhật ghi chú biên tập cho khớp các mục vừa sửa.** Mười hai mục CE10 đã được áp bình duyệt hôm
   nay; mười ba khối thì không đổi một chữ. Ít nhất khối 5 (hai đích đã nâng) và khối 13 ý *Một* (3/12 nay
   đã lên ít nhất 5/12) đang mô tả trạng thái cũ.
3. **Áp quy ước của khối 13 ngược lại lên chính vòng CE10** — hai con số ở khối 1 và khối 6 — rồi mới ghi
   quy ước ấy vào `CONTRIBUTING.md`.
