# Bình duyệt độc lập — ghi chú biên tập vòng CE07, 10 khối
Ngày: 2026-11-02 · phạm vi: content/ch05.md dòng 1110–1142

Nhãn: **BẮT BUỘC** (sai sự thật / sai số liệu / sai mô tả repo / vi phạm quy tắc) ·
**NÊN** (đúng nhưng quá mạnh, thiếu điều kiện, sẽ rữa) · **CÂN NHẮC** (phán đoán).

Nền đã dựng trước khi soi, dùng lại cho cả mười khối:
- `reports/stats.txt` ở trạng thái hiện tại: **245 người atlas chính** + 40 phụ lục. Đông Nam Á **4 (1,6%)**, Trung Á **4 (1,6%)**, Châu Mỹ 3 (1,2%), Châu Đại Dương 0.
- `reports/ch05-ce06-slot12.md` §0.1 ghi lại trạng thái lúc các khối này được viết: **208 người atlas chính**, Đông Nam Á **1 (0,5%)**, Trung Á **1 (0,5%)**. Đây là mốc để phân biệt "sai lúc viết" với "rữa theo thời gian".
- `reports/stats.txt` **không tự khai thời điểm đo** (dòng đầu chỉ có tổng số người, không có ngày/giờ/commit). Mọi khối trích số từ nó vì vậy không có cách nào tự rào thời điểm, trừ khi tự viết ra.
- Bốn mục Đông Nam Á của atlas chính hiện nay, lấy bằng `awk` trên `content/`: `CH05-CE06-11` Bhavavarman I (Khmer), `CH05-CE09-01` Jayavarman II (Khmer), `CH05-CE10-05` Khúc Thừa Dụ (Việt Nam), `CH05-CE10-06` Mpu Sindok (**Đông Java**).

---

## Khối 1 — **Nhóm CE07 đã qua một vòng bình duyệt chọn người độc lập** (dòng 1110–1111)

**Đã kiểm được (không có phát hiện)**

- Vòng bình duyệt có thật và có hồ sơ: `reports/ch05-ce07-select.md`, đề "agent bình duyệt độc lập (không viết Ch5)", ngày 2026-10-31, phạm vi "3 suất trống của `CH05-CE07` (9/12 đã viết, không xét lại)". Khớp đúng câu "Chín mục đầu được viết trước, ba suất cuối…".
- Sáu điểm số khớp từng con số với §1–§6 và bảng xếp hạng §9 của báo cáo ấy: Pháp Xứng **18/20**, Tùng Tán Cán Bố **16/20**, Pakal **11/20**, Dapunta Hyang Sri Jayanasa **9/20**, Harsha **8/20**, Thánh Đức Thái tử **8/20**. Thang 20 = 4 tiêu chí × 5 điểm, đúng bộ (a)–(d) của `CONTRIBUTING.md`.
- Ba người được nhận đúng là ba mục hiện có: `CH05-CE07-10` Pháp Xứng, `-11` Tùng Tán Cán Bố, `-12` Pakal.
- **Quy tắc 6 sạch cho cả bảy cái tên bị loại trong khối.** `grep` toàn `content/` (gồm `content/ch90.md`): Dapunta Hyang, Harsha, Thánh Đức Thái tử / Shōtoku, Kumārila Bhaṭṭa, Gar Tongtsen, Yuknoom Chʼeen II, Pulakeshin II — **không ai** có mục ở bất kỳ chapter nào; cả bảy chỉ xuất hiện ở chính dòng 1111.

**CÂN NHẮC — khối tổng kết vòng chọn người nhưng bỏ qua cái tên duy nhất của vòng ấy đang vi phạm quy tắc 6.**

Mục `CH05-CE07-11` viết: "Ứng viên bị loại là Gar Tongtsen, đại thần điều hành phần lớn việc triều chính, và **Trisong Detsen ở thế kỷ 8**." Trisong Detsen **có mục riêng** ở `content/ch05.md` dòng 575, `CH05-CE08-10`. Đó đúng hình dạng lỗi mà quy tắc 6 sinh ra để chặn, và là loại lỗi phát sinh theo thời gian: lúc khối được viết, nhóm CE08 chưa tồn tại.

Lỗi nằm trong mục chứ không trong khối, tức **ngoài phạm vi vòng này** — ghi lại để vòng soi mục không bỏ qua. Nhưng khối 1 là chỗ duy nhất tổng kết vòng chọn người, nên nó là chỗ hợp lý để ghi thêm một câu: danh sách bị loại phải được chạy lại quy tắc 6 mỗi khi atlas thêm nhóm, không chỉ một lần lúc chấm.

*Câu có thể thêm vào cuối khối:* "Danh sách bị loại phải được chạy lại quy tắc 6 sau **mỗi** nhóm mới, không chỉ lúc chấm: một cái tên hợp lệ hôm nay có thể thành mục ở nhóm sau."

---

## Khối 2 — **Một Q-ID suýt vào atlas trỏ sang một chi bướm** (dòng 1113–1114)

**Đã kiểm được (không có phát hiện)**

Tự gọi `wbgetentities` (UA `history-atlas/0.1 (research)`), không tin con số trong file:

| Q-ID | nhãn en | desc en | P31 | P569 | P570 |
|---|---|---|---|---|---|
| `Q311215` | Colias | genus of insects | `Q16521` (taxon) | — | — |
| `Q371384` | K'inich Janaab' Pakal | Maya ruler of Palenque | `Q5` | `+0603-03-23` prec 11 | `+0683-08-28` prec 11 |
| `Q641749` | Janaab' Pakal | ajaw or lord of Palenque | `Q5` | `+0550` prec 7 | `+0612-03` prec 10 |
| `Q4017694` | Janaab Pakal III | ajaw of Palenque | `Q5` | `+0800` prec 7 | — |

Bốn mệnh đề của khối về Wikidata **đúng từng chữ**: `Q311215` là chi bướm Colias với `P31` là đơn vị phân loại; Q-ID đúng là `Q371384`; `Q641749` là một Janaabʼ Pakal khác mất năm 612; `Q4017694` là Janaab Pakal III. Mục `CH05-CE07-12` hiện ghi `wikidata: Q371384` — tức việc sửa đã thật sự vào văn bản.

**BẮT BUỘC — "Lint không bắt được loại lỗi này vì nó chỉ đọc định dạng Q-ID chứ không đọc nội dung" mô tả sai phép kiểm của lint, và cả ba Q-ID bẫy đều nằm trong tầm nó.**

Câu sai, nguyên văn: *"Lint không bắt được loại lỗi này vì nó chỉ đọc định dạng Q-ID chứ không đọc nội dung."*

`atlaslib/lint.py` có hẳn một hàm `lint_wikidata` (dòng 250–322) **tải nội dung thực thể về và đọc**. Ba phép kiểm liên quan, chạy thử trên từng Q-ID bẫy bằng chính logic trong file:

1. **So nhãn** (dòng 279–286): nếu nhãn Wikidata không giao và không là chuỗi con của tên mục → `rep.warn(... "nhãn Wikidata {q} = '{lbl}' không khớp tên ... — kiểm tra Q-ID")`. `Q311215` → nhãn `Colias` so với `Kʼinich Janaabʼ Pakal` / `Pakal Đại đế`: **nổ**.
2. **Kiểm `P31`** (dòng 287–290): `P31` không chứa `Q5` và không chứa lớp con của `Q5` → `rep.warn(... "không được xếp là người: P31 = ...")`. `Q311215` có `P31 = Q16521`: **nổ**.
3. **Đối chiếu niên đại** (dòng 291–318), với `CH05-CE07-12` ở `độ tin cậy: Cao` nên dung sai 5 năm: `Q641749` có `P570` năm 612 ở `precision` 10 → dung sai giữ nguyên 5, lệch 71 năm: **nổ**. `Q4017694` có `P569 = +0800` ở `precision` 7 → `year_in_bucket` giải thành 701–800, không chứa 603, dung sai nới lên 60, lệch 197 năm: **nổ**.

`README.md` dòng 77 liệt đúng hai cảnh báo ấy: "nhãn Wikidata không khớp tên" và "niên đại lệch Wikidata (P569/P570)". Vậy mệnh đề "chỉ đọc định dạng" đúng cho **`build.py --offline`**, và chỉ cho nó. Chỗ lint thật sự yếu là **mức**, không phải **tầm nhìn**: cả ba là `WARN` chứ không phải lỗi chặn build, nên một vòng vội vẫn có thể commit qua.

Viết sai chỗ này nguy hiểm vì nó dạy vòng sau rằng không có lưới nào — trong khi lưới có, chỉ là lưới mềm.

*Câu thay thế đề nghị:* "Lint **có** nhìn thấy loại lỗi này, nhưng chỉ ở chế độ online và chỉ ở mức cảnh báo: `lint_wikidata` so nhãn Wikidata với tên mục và cảnh báo khi `P31` không phải `Q5`, nên `Q311215` sẽ nổ cả hai; còn `Q641749` và `Q4017694` nổ ở phép đối chiếu `P569`/`P570` vì mục này để `độ tin cậy: Cao`, dung sai 5 năm. Cái lint **không** làm là chặn: cả ba chỉ là `WARN`, và `build.py --offline` bỏ qua trọn vòng Wikidata. Lưới có thật nhưng mềm — đừng dựa vào nó thay cho việc tự tra."

**BẮT BUỘC — "lần trước là mười hai Q-ID nhớ sai của nhóm CE08" không có trong hồ sơ, và thứ tự thời gian thì ngược lại.**

Câu sai, nguyên văn: *"Đây là lần thứ hai trong Chapter 5 cổng tra Q-ID chặn được một mục sai người — lần trước là mười hai Q-ID nhớ sai của nhóm CE08."*

Ba chỗ hỏng, cả ba kiểm được mà không ra khỏi repo:

1. **Hồ sơ CE08 nói ngược.** `reports/ch05-ce08-gate.md` §1 kết luận: "Tất cả 20 đều P31 = Q5. Cổng Q-ID của vòng trước đứng vững; **không có ca 'chi bướm Colias' nào ở đây**." Và `reports/ch05-ce08-review.md` dòng 35: "cả 12 Q-ID trỏ đúng người, cả 12 đều `P31 = Q5`. Không có ca 'chi bướm'." Tức vòng CE08 bắt được **không** Q-ID sai nào, chứ không phải mười hai.
2. **Thứ tự ngược.** `reports/ch05-ce08-gate.md` dòng 370 viết vòng CE08 tra Q-ID "không lấy từ trí nhớ (**tiền lệ con bướm Colias ở Ghi chú biên tập CE07**)". CE08 viện CE07 làm tiền lệ, nên CE08 không thể là "lần trước".
3. **`grep` toàn repo** cho "mười hai Q-ID", "12 Q-ID", "Q-ID nhớ sai": không báo cáo nào ghi một ca mười hai Q-ID sai. Ca nhiều Q-ID bẫy duy nhất có hồ sơ là `reports/ch05-ce06-slot12.md` §1.1 — **ba** bẫy (Imru' al-Qays ba thực thể, Procopius dữ liệu rác, Maniakh thực thể gần trống) — và chính nó cũng viện ca Pakal làm tiền lệ, tức cũng đến **sau**.

*Câu thay thế đề nghị:* "Đây là ca Q-ID trỏ sai người **sớm nhất mà hồ sơ trong `reports/` ghi lại** cho Chapter 5, và hai vòng sau đều viện nó làm tiền lệ: `reports/ch05-ce06-slot12.md` §1.1 bắt thêm ba bẫy cùng họ (ba thực thể Imru' al-Qays, dữ liệu rác của Procopius, thực thể gần trống của Maniakh), còn `reports/ch05-ce08-gate.md` §1 chạy cổng trên 20 ứng viên và **không bắt được ca nào** — cổng đứng vững chứ không phải bắt thêm."

---

## Khối 3 — **Niên đại Pháp Xứng: Wikidata tự mâu thuẫn, đừng chép** (dòng 1116–1117)

**Đã kiểm được (không có phát hiện)**

- Hai giá trị thô **đúng y như khối ghi**. `wbgetentities` cho `Q457990`: `P569 = +0700-01-01` ở `precision 7`, `P570 = +0660-01-01` ở `precision 9`. Nhãn `vi` là `Pháp Xứng`, `P31 = Q5` — Q-ID trỏ đúng người.
- Mục `CH05-CE07-10` hiện ghi `năm: k. 600 – k. 660 CN` và `độ tin cậy niên đại: Thấp` — khớp đúng điều khối nói mục đã làm.
- Quy niên đại 600–660 cho **Frauwallner** là đúng: `reports/ch05-ce07-select.md` §3.3 dẫn SEP "Dharmakīrti" (URL đã mở, đúng chủ đề) ghi Frauwallner "came out strongly for 600–660".
- "Một mạch gần đây đẩy ông sớm hơn nửa thế kỷ" khớp: Krasser (2012) đẩy về giữa thế kỷ 6; Balcerowicz (2016) đề xuất 550–610.
- Khối **không** lặp lại một mệnh đề sai có trong hồ sơ nguồn của nó: `reports/ch05-ce07-select.md` §0.2 viết "chép vào là lint chặn build", nhưng lỗi chặn build "năm mất trước năm sinh" chỉ áp cho trường `năm:` của chính atlas (`atlaslib/lint.py` dòng 120–121), không áp cho giá trị Wikidata. Khối đã bỏ mệnh đề ấy — đúng.

**BẮT BUỘC — "tức sinh sau khi mất bốn mươi năm" là cách đọc điểm cho một giá trị mà chính khối vừa khai là ở độ chính xác thế kỷ, và quy ước của dự án đọc ngược lại.**

Câu sai, nguyên văn: *"`Q457990` ghi P569 = +0700 (độ chính xác thế kỷ) và P570 = +0660, tức **sinh sau khi mất bốn mươi năm**."*

`atlaslib/common.py` dòng 136–147 định nghĩa `year_in_bucket` với docstring nói thẳng: *"Giá trị Wikidata ở mức thế kỷ (p7) hoặc thiên niên kỷ (p6) là một KHOẢNG… `+0300/p7` → thế kỷ 3 CN → 201..300."* Áp đúng công thức ấy, `+0700/p7` = **601–700**, không phải điểm 700. Khoảng 601–700 **chứa** năm mất 660, và chứa cả `k. 600` mà mục đang dùng. Tức khi tôn trọng chính độ chính xác mà khối vừa khai, **không có nghịch lý sinh-sau-mất nào**; nghịch lý chỉ xuất hiện khi đọc `+0700` như một năm.

`atlaslib/lint.py` dòng 305–309 còn có cả một chú thích cảnh báo đúng cái bẫy này ("So bằng khoảng cách tới điểm sẽ báo sai đúng ở đầu khoảng — Galen mất k. 216 bị kêu lệch 84 năm so với 'thế kỷ 3' chứa nó"). Và khối ở dòng 1150 của cùng mục Ghi chú biên tập này mang tiêu đề **"Wikidata khai độ chính xác, nó không khai độ tin cậy"** — tức cùng một mục Ghi chú biên tập đang dạy quy tắc ở một chỗ và phá nó ở chỗ khác.

Hệ quả thực tế: vòng sau đọc khối này sẽ đi tìm một "mâu thuẫn Wikidata" không tồn tại, và có thể báo lỗi lên Wikidata nhầm. Điều đáng ghi lại thì vẫn còn nguyên, chỉ là nó khác: `P569` ở độ chính xác thế kỷ **không pin được gì**, nên không dùng để chỉnh mục.

*Câu thay thế đề nghị:* "`Q457990` ghi `P570 = +0660` ở độ chính xác **năm**, còn `P569 = +0700` ở độ chính xác **thế kỷ** — mà theo đúng quy ước `year_in_bucket` của `atlaslib/common.py`, một giá trị `p7` là **khoảng 601–700**, không phải năm 700. Đọc đúng thì không có nghịch lý sinh-sau-mất; đọc như một điểm thì có, và đó là cái bẫy. Điều rút ra là `P569` ở đây **không pin được gì**: nó chỉ nói "thế kỷ 7", trùm cả `k. 600` lẫn `k. 660`."

**NÊN — khối lo vòng sau "sửa mục theo Wikidata" nhưng bỏ sót dữ kiện làm nỗi lo ấy nhẹ hẳn: ở mức `Thấp`, lint không đối chiếu niên đại.**

`atlaslib/common.py` dòng 82 đặt `DATE_TOLERANCE = {"Cao": 5, "Trung bình": 25, "Thấp": None}`, và `lint.py` dòng 291–293 thấy `None` thì ghi `INFO "độ tin cậy Thấp — bỏ qua đối chiếu niên đại"` rồi `continue`. Vì mục này để `Thấp`, **không có cảnh báo nào** sẽ nổ để thúc một vòng sau chỉnh `năm:` theo Wikidata. Nói ra điều đó làm khối mạnh lên: sức ép duy nhất còn lại là sức ép của người đọc, không phải của công cụ.

*Câu có thể thêm:* "Thêm một điểm tựa: vì mục để `Thấp`, `DATE_TOLERANCE` là `None` nên lint **bỏ qua hẳn** phép đối chiếu niên đại Wikidata cho mục này (`atlaslib/lint.py`, nhánh `tol is None`). Không có cảnh báo nào sẽ thúc vòng sau sửa — nếu ai đó sửa thì đó là quyết định của người, không phải của công cụ."

---

## Khối 4 — **Tuổi thọ Pakal: bi ký nói 80, bộ xương từng nói 40–50** (dòng 1119–1121)

**Đã kiểm được (không có phát hiện)**

- "Trị vì 68 năm" ✓ — khớp `Q371384` (603→683), khớp mục `CH05-CE07-12` ("Lên ngôi năm 615 lúc mười hai tuổi và trị vì sáu mươi tám năm"), và khớp tóm tắt enwiki ("reigned 68 years… took the throne at age 12").
- `độ tin cậy niên đại: Cao` ✓ đúng như khối nói.
- Mạch giám định: khối mô tả khớp `reports/ch05-ce07-select.md` §5 — giám định 1952 sau khi Ruz Lhuillier mở mộ cho 40–50 tuổi; hai lối giải thích (hai người khác nhau — chính Ruz nêu; hoặc phương pháp lệch); Tiesler & Cucina (2006) giám định lại bằng transition analysis và histomorphometry, kết luận người trong mộ **không thể dưới 50**.
- "Tên hai nhà nhân học giám định năm 1952 không kiểm được tới nguồn gốc nên cố ý không ghi" ✓ — `grep` mục `CH05-CE07-12`: không có tên nào như vậy.
- Von Däniken (1968) và cách bác nó: khớp `reports/ch05-ce07-select.md` §5 khoản 7. Khối không tuyên bố mệnh đề này đã vào mục, nên không có gì để đối chiếu.

**BẮT BUỘC — khối tự khai mục đã viết "nghiêng về phía bi ký", nhưng mục không viết câu ấy và không hề nhắc tới tranh luận tuổi thọ.**

Câu sai, nguyên văn: *"Mục viết "nghiêng về phía bi ký", **không viết "đã chứng minh"**, vì vẫn còn một mạch thận trọng."*

Đọc hết mục `CH05-CE07-12` (dòng 395–411): **không có** chuỗi "nghiêng về phía bi ký", không có "bộ xương", không có "Ruz", không có "40–50". `grep` ba chuỗi ấy trên toàn `content/ch05.md` chỉ trả về chính khối 4. Tên Tiesler & Cucina xuất hiện đúng một lần ở dòng 410, trong trường `Nguồn`, như nhan đề sách — không kèm mệnh đề nào.

Tức mục **không** chọn một phía thận trọng hơn; mục **im lặng hoàn toàn** về tranh luận này. Hai trạng thái ấy khác nhau, và sự khác biệt quan trọng đúng theo lý do khối tồn tại: một vòng sau đọc khối, tin rằng mục đã rào, sẽ không đi thêm bước nào — trong khi mục vẫn đang để độ tin cậy `Cao` mà không nói vì sao `Cao` chịu được một giám định xương từng cho 40–50 tuổi.

*Câu thay thế đề nghị (mô tả đúng trạng thái hiện tại):* "Mục hiện **không** nhắc tranh luận này: nó để `độ tin cậy: Cao` theo bi ký và dừng ở đó, còn Tiesler & Cucina 2006 chỉ xuất hiện trong trường `Nguồn` như nhan đề sách. Nếu vòng sau muốn đưa tranh luận vào mục thì công thức đúng là **"nghiêng về phía bi ký"**, không phải "đã chứng minh", vì vẫn còn một mạch thận trọng."

**BẮT BUỘC — hai ngày tháng đều lệch đúng +1 so với Wikidata và so với chính báo cáo mà khối dựa vào.**

Câu sai, nguyên văn: *"Bi ký Palenque cho niên đại tới từng ngày (sinh **24-3-603**, mất **29-8-683**, trị vì 68 năm)…"*

| Nguồn | sinh | mất |
|---|---|---|
| Khối 4 | 24-3-603 | 29-8-683 |
| `Q371384`, tự tra `wbgetentities` | `+0603-**03-23**` (precision 11 = ngày) | `+0683-**08-28**` (precision 11) |
| `reports/ch05-ce07-select.md` §0.1 và §5 | `603-03-23` | `683-08-28` |

Cả hai lệch **đúng +1 ngày**. `CONTRIBUTING.md` quy tắc 3 mô tả chính hình dạng này: *"5/6 số chương Keith Taylor sai — và cả 5 lệch đúng +1. Hình dạng đó nghĩa là con số đã được sinh ra chứ không tra cứu."*

**[KHÔNG KIỂM ĐƯỢC]** — tôi **không** mở được Tiesler & Cucina 2006 hay một bộ chuyển Long Count để loại trừ khả năng +1 đến từ quy ước lịch (Julian so với proleptic Gregorian) chứ từ lỗi chép. Vì vậy đề xuất dưới đây bám vào hai nguồn đã kiểm được trong repo và trên Wikidata, và nói thẳng chỗ chưa khép.

*Câu thay thế đề nghị:* "Bi ký Palenque cho niên đại tới từng ngày — `Q371384` khai `P569 = 603-03-23` và `P570 = 683-08-28` ở độ chính xác ngày, khớp `reports/ch05-ce07-select.md` §0.1 — và nhất quán nội tại với 68 năm trị vì; đó là lý do độ tin cậy để **Cao**. (Nếu một vòng sau gặp bản ghi lệch một ngày, kiểm quy ước lịch trước khi sửa: chênh lệch Julian/Gregorian là lời giải thích thường gặp cho loại lệch ±1 này, và chỗ đó **chưa được đối chiếu tới bản gốc**.)"

---

## Khối 5 — **Một đính chính về phạm vi phụ lục, vì nó đã làm lệch lập luận chọn người** (dòng 1123–1125)

**Đã kiểm được (không có phát hiện)**

- **Đính chính cốt lõi đúng, và đã vào văn bản.** `content/ch90.md` dòng 1: `# Chapter 90 · Phụ lục · Việt Nam qua các thời kỳ`. Cả **40/40** mục của ch90 là nhân vật hoạt động trong phạm vi Việt Nam (từ `CH90-BCE03_01-01` An Dương Vương tới `CH90-CE19_20-10` Thích Nhất Hạnh); không có mục Khmer, Java, Mã Lai hay Pyu nào. Lập luận "đã có phụ lục ch90 đỡ" cho Đông Nam Á đúng là sai, như khối nói.
- Đính chính này khớp `reports/ch05-ce07-select.md` §0.3, nơi vòng bình duyệt bác đúng tiền đề ấy của đề bài.
- **Jayavarman II: cả ba mệnh đề đều đúng và đã thành hiện thực.** Bia Sdok Kak Thom khắc năm 1052, tức 250 năm sau lễ 802 ✓ (mục `CH05-CE09-01` viết đúng như vậy). "Khi viết, ông phải để độ tin cậy **Thấp**" ✓ — mục hiện ghi `độ tin cậy niên đại: Thấp`. "P569/P570 của ông trên Wikidata (800/900) là giá trị độn" ✓ — tự tra `Q379239`: `P569 = +0800` và `P570 = +0900`, **cả hai ở `precision 7`**, tức khoảng thế kỷ chứ không phải năm; mục để `năm: trị vì k. 802–850 CN` và không chép hai con số ấy.

**BẮT BUỘC — con số Đông Nam Á đã rữa: đúng lúc viết, sai bây giờ, và câu lại viết ở thì hiện tại.**

Câu sai, nguyên văn: *"Hệ quả phải ghi thẳng: sau Chapter 5, **Đông Nam Á vẫn chỉ có đúng một người trong atlas chính (0,5%)** — và người ấy, Bhavavarman I, là một mục Khmer, nên Java, Mã Lai–hải đảo và Pyu vẫn trống hoàn toàn."*

| | Lúc khối được viết | Bây giờ |
|---|---|---|
| Nguồn | `reports/ch05-ce06-slot12.md` §0.1 (208 người atlas chính) | `reports/stats.txt` (245 người atlas chính) |
| Đông Nam Á | **1 — 0,5%** | **4 — 1,6%** |

Bốn mục Đông Nam Á hiện nay, lấy bằng `awk` trên `content/`: `CH05-CE06-11` Bhavavarman I (Khmer) · `CH05-CE09-01` Jayavarman II (Khmer) · `CH05-CE10-05` Khúc Thừa Dụ (Việt Nam) · `CH05-CE10-06` Mpu Sindok (**lưu vực sông Brantas, Đông Java**).

Hai vế của câu đều hỏng chứ không chỉ con số:
1. "chỉ có đúng một người… (0,5%)" → thực tế **bốn người, 1,6%**.
2. "Java… vẫn trống hoàn toàn" → **`CH05-CE10-06` Mpu Sindok đã lấp Java**. Chỉ **Mã Lai–hải đảo và Pyu** còn trống thật.

Chỗ này nguy hiểm hơn một con số lệch, vì cả khối tồn tại để sửa một lập luận chọn người sai — mà bản thân nó lại dựng lập luận mới trên một con số không tự rào thời điểm. `reports/stats.txt` cũng không khai thời điểm đo (dòng đầu chỉ có tổng số người, không ngày, không commit), nên khối phải tự rào.

*Câu thay thế đề nghị (viết để không rữa lại — bỏ tỉ lệ, ghi mốc đo, và chỉ giữ phần còn đúng):* "Hệ quả phải ghi thẳng: tại thời điểm viết khối này (atlas chính 208 người, theo `reports/ch05-ce06-slot12.md` §0.1), Đông Nam Á **chỉ có đúng một người** trong atlas chính, và người ấy — Bhavavarman I — là một mục Khmer. Khoảng trống thật vì vậy không phải "Đông Nam Á" nói chung mà là **thế giới hải đảo và Pyu**: đó là một khoảng trống thật chứ không phải một ô đã có chỗ khác bù. Con số cập nhật phải đọc từ `reports/stats.txt` chứ đừng đọc ở đây."

**NÊN — câu cuối ("Đông Nam Á hải đảo vẫn trống sau CE09") đúng theo nghĩa hẹp nhưng nay dễ bị đọc nhầm thành trạng thái hiện tại.**

Nguyên văn: *"Ông cũng chỉ phủ Khmer lục địa, nên Đông Nam Á **hải đảo** vẫn trống sau CE09."* Mệnh đề này được khoanh bằng chữ "sau CE09" nên về kỹ thuật vẫn đúng. Nhưng nhóm CE10 ngay sau đó đã đưa Mpu Sindok vào, nên một người đọc lướt sẽ mang câu này ra làm hiện trạng. Thêm bốn chữ là đủ.

*Câu thay thế đề nghị:* "Ông cũng chỉ phủ Khmer lục địa, nên Đông Nam Á **hải đảo** vẫn trống sau CE09 — ô ấy về sau được `CH05-CE10-06` Mpu Sindok (Đông Java) lấp, còn Mã Lai–hải đảo và Pyu thì chưa."

**CÂN NHẮC — "dòng đầu của `content/ch90.md` nói rõ" đúng với dòng tiêu đề, nhưng dòng kế ngay sau đó thì không rõ bằng.**

`content/ch90.md` dòng 3 viết: "ảnh hưởng được đo trong phạm vi **Việt Nam và Đông Nam Á**, không phải toàn nhân loại." Tức chính phụ lục có một câu mô tả phạm vi rộng hơn cái mà khối đang viện. Nội dung thực tế thì đứng về phía khối (40/40 mục là Việt Nam), nhưng nếu muốn đính chính này cầm cự được qua nhiều vòng, nên sửa luôn câu gây nhập nhằng ở `content/ch90.md` chứ không chỉ ghi vào ghi chú của Chapter 5.

---

## Khối 6 — **Vùng của Tùng Tán Cán Bố, và một cám dỗ bị từ chối** (dòng 1127–1128)

**Đã kiểm được (không có phát hiện)**

- **Tiền lệ đúng người, đúng ID, đúng vùng.** `content/ch03.md` dòng 607–608: `CH03-BCE02-12 · Mặc Đốn thiền vu`, `nơi: … cao nguyên Mông Cổ`, `vùng: **Đông Á**`. Đúng như khối viện.
- **"Danh sách chín vùng không có ô nào cho Nội Á"** ✓ — `atlaslib/common.py` dòng 75: `REGIONS` có đúng 9 giá trị, không có Nội Á / thế giới thảo nguyên. `CONTRIBUTING.md` quy ước `vùng:` khoản 3 viết ra chính hệ quả ấy.
- **"Atlas đã bác cách làm này một lần với Kanishka"** ✓ — `CONTRIBUTING.md` quy ước `vùng:` khoản 4: "Vòng rà soát vùng đã **bác** đề xuất chuyển Kanishka từ Nam Á sang Trung Á".
- **"`CONTRIBUTING.md` cấm đổi vùng của một người để cải thiện thống kê"** ✓ — cùng khoản 4, nguyên văn: "Đừng đổi `vùng:` của một người để cải thiện thống kê."
- **"Đông Á thành 5/12 của nhóm"** ✓ — đếm tay trong nhóm CE07: `-04` Đường Thái Tông, `-05` Võ Tắc Thiên, `-06` Huyền Trang, `-07` Huệ Năng, `-11` Tùng Tán Cán Bố = **5**. Khớp cả `reports/ch05-ce07-select.md` §8.2.
- **"Không vùng mới nào được mở ra"** ✓ — Đông Á đã có mặt trong nhóm từ `-04`.
- Mục `CH05-CE07-11` hiện ghi `vùng: Đông Á` — quyết định đã vào văn bản.

**BẮT BUỘC — hai con số Trung Á đã rữa, và cả hai viết ở thì hiện tại.**

Câu sai, nguyên văn: *"Ghi "Trung Á" sẽ nâng con số Trung Á **từ 0,5% lên khoảng 1%**, và đó chính là lý do không được làm…"*

| | Lúc khối được viết | Bây giờ |
|---|---|---|
| Nguồn | `reports/ch05-ce06-slot12.md` §0.1 (208 người) | `reports/stats.txt` (245 người) |
| Trung Á | 1 — **0,5%** | 4 — **1,6%** |
| Nếu đổi vùng Tùng Tán Cán Bố | 2 — **≈1,0%** | 5 — **≈2,0%** |

Bốn mục Trung Á hiện nay, lấy bằng `awk` trên `content/`: `CH02-BCE06-09` Zarathustra · `CH05-CE08-01` Abu Muslim al-Khurasani · `CH05-CE09-09` Al-Bukhari · `CH05-CE10-04` Ismāʿīl Samānī. Ba trong bốn là mục mới của chính Chapter 5, tức con số rữa **do chính chapter này** chứ không do nơi khác.

Lập luận của khối **không** phụ thuộc vào hai con số ấy — nó đứng trên `CONTRIBUTING.md` khoản 4, vốn cấm đổi vùng vì thống kê bất kể thống kê đang là bao nhiêu. Giữ con số ở đây chỉ gắn một lập luận đúng vào hai số sẽ sai lại sau mỗi vòng.

*Câu thay thế đề nghị (bỏ hẳn tỉ lệ, giữ nguyên sức nặng):* "Ghi "Trung Á" sẽ **nhích con số Trung Á lên một bậc**, và đó chính là lý do không được làm — `CONTRIBUTING.md` quy ước `vùng:` khoản 4 cấm đổi `vùng:` của một người để cải thiện thống kê, và vòng rà soát vùng đã bác đúng đề xuất ấy một lần với Kanishka. Con số Trung Á hiện hành đọc ở `reports/stats.txt`, đừng đọc ở đây."

---

## Khối 7 — **Bốn mệnh đề bị vòng kiểm sự kiện bác, và đã sửa trong mục** (dòng 1130–1133)

**Đã kiểm được (không có phát hiện)**

Mở từng mục ra đối chiếu. **Cả bốn mệnh đề "đã sửa" đều thật sự nằm trong văn bản hiện tại:**

| # | Khối nói đã sửa | Văn bản mục hiện tại |
|---|---|---|
| 1 | Đường luật sớ nghị không do Thái Tông ban; của ông là Trinh Quán luật 637; Đường luật sớ nghị ban 653 dưới Cao Tông | `CH05-CE07-04`: "cho biên **Trinh Quán luật năm 637** — bộ Đường luật sớ nghị quen thuộc hơn thì **phải tới năm 653, dưới triều con ông**, mới ban" ✓ |
| 2 | Thứ lưu hành 690 là **bản sớ**, không phải kinh nguỵ tạo | `CH05-CE07-05`: "năm 690 **một bản sớ**, Đại Vân kinh Thần Hoàng thụ ký nghĩa sớ, được lưu hành khắp các châu, **đọc một kinh Ấn Độ có thật** thành lời sấm" ✓ |
| 3 | Nālandā khoảng năm năm, không phải hơn mười | `CH05-CE07-06`: "ở lại **hơn mười năm** mà **riêng Nālandā chừng năm năm**" ✓ |
| 4 | Sasanian sụp 651, sau khi Umar đã chết | `CH05-CE07-02`: "Sasanian bị đánh gãy xương sống rồi **sụp hẳn năm 651, sau khi ông đã chết**" ✓ |

- "Bản thảo đầu còn tự mâu thuẫn với `CH05-CE06-03` trong cùng file, vốn đã ghi đúng 651" ✓ — `CH05-CE06-03` Khosrow I dòng 46 ghi "sau năm **651**". Mâu thuẫn nội bộ nay đã hết.
- **Ba chỗ "phải rào mà nay đã rào" cũng đều đã rào thật:** lịch Hijri — `CH05-CE07-02` "là do truyền thống quy cho ông, **không phải do chứng cứ đương thời**" ✓; dīwān — "xếp theo thâm niên theo đạo và quan hệ với nhà tiên tri **chứ không theo công trạng chiến trận**" ✓; Brāhmasphuṭasiddhānta tới Baghdad — `CH05-CE07-08` "chỉ được chép **rất muộn**, qua Ibn al-Adamī rồi al-Qifṭī, nên **đọc như giai thoại**" ✓.
- Hai trong ba chi tiết "không được viết vào mục" đúng là không có: `CH05-CE07-09` ghi "**Gần một nghìn** bản chép tay" và "việc chia thành hai mươi quyển là do **Braulio**, học trò ông, làm sau" ✓; `grep "Forte"` trên toàn `content/` chỉ trả về chính dòng 1133 — tên Forte không vào trường `Nguồn` của mục nào ✓.

**BẮT BUỘC — khối khai "chiếu chỉ cấm xuất cảnh năm 629 … không được viết vào mục", nhưng mục có viết.**

Câu sai, nguyên văn: *"Ba chi tiết **không kiểm được tới nguồn gốc** nên không được viết vào mục: **chiếu chỉ cấm xuất cảnh năm 629**; …"*

`CH05-CE07-06` dòng 297 viết: *"Năm 629 ông rời Trung Hoa — **tiểu sử môn đồ soạn sau khi ông mất nói là trái lệnh cấm**, còn chính Tây Vực ký không kể…"*. Lệnh cấm **có** trong mục, chỉ là được quy nguồn và được đặt cạnh phản chứng.

Cách xử lý trong mục thật ra tốt hơn cách khối mô tả — nêu kèm nguồn và kèm chỗ nguồn im lặng, đúng tinh thần quy tắc 3 và 7. Vấn đề là khối mô tả **sai trạng thái văn bản**, mà một mục Ghi chú biên tập tồn tại chính để vòng sau khỏi phải mở lại từng mục. Một vòng sau tin khối sẽ đi tìm xem ai đã "lén" thêm chi tiết bị cấm, hoặc tệ hơn, xoá một câu đang rào đúng.

*Câu thay thế đề nghị:* "Hai chi tiết **không kiểm được tới nguồn gốc** nên không được viết vào mục: bản đếm gốc số bản chép tay Etymologiae (nay ghi "gần một nghìn", và việc chia hai mươi quyển là do Braulio làm sau chứ không phải Isiđôrô); nhà xuất bản và lần in của Forte 1976. Chi tiết thứ ba — **chiếu chỉ cấm xuất cảnh năm 629** — cũng không truy được tới nguồn gốc, nên mục **không khẳng định** nó mà quy cho nguồn và nêu luôn chỗ nguồn im lặng: "tiểu sử môn đồ soạn sau khi ông mất nói là trái lệnh cấm, còn chính Tây Vực ký không kể". Giữ nguyên công thức ấy, đừng rút gọn thành một khẳng định."

**CÂN NHẮC — niên đại "k. 424–430" cho bản dịch của Đàm Vô Sấm chỉ truy được tới một vòng nội bộ, không tới nguồn.**

Khối viết Đại Vân kinh "do Đàm Vô Sấm dịch **k. 424–430**". Con số này xuất hiện trong `reports/ch05-ce07-facts.md` dòng 320 và 349 nhưng ở đó cũng **không kèm nguồn nào mở được**. **[KHÔNG KIỂM ĐƯỢC]** — tôi không mở được một mục lục hay danh mục kinh lục nào để xác nhận khoảng 424–430 (Đàm Vô Sấm hoạt động ở Lương Châu từ k. 412 tới khi mất năm 433, nên khoảng ấy khả dĩ, nhưng "khả dĩ" không phải "đã kiểm").

Điểm quan trọng là mệnh đề này **không** vào mục — `CH05-CE07-05` chỉ viết "một kinh Ấn Độ có thật", không ghi dịch giả và không ghi năm — nên rủi ro hiện chỉ nằm trong ghi chú. Nếu muốn giữ con số thì nên gắn nó vào một kinh lục cụ thể; nếu không, bỏ khoảng năm và viết "do Đàm Vô Sấm dịch sang Hán văn ở thế kỷ 5" là đủ cho mục đích của khối.

---

## Khối 8 — **Bốn nguồn phải đọc kèm cảnh báo (quy tắc 7)** (dòng 1135–1136)

**Đã kiểm được (không có phát hiện)**

- **Ba trong bốn cảnh báo đã thật sự nằm trong văn bản mục**, đúng như khối tự khai:
  - **Madelung 1997** — `CH05-CE07-03` viết "Mục này cố ý không chọn phía trong tranh luận ấy. … **Madelung 1997, nguồn chính của mục, nghiêng về phía Alid rõ nhất trong giới hiện đại.**" ✓ Đúng cả hai vế khối nói.
  - **Wechsler 1974** — `CH05-CE07-04` trường `Nguồn` viết "Howard J. Wechsler, *Mirror to the Son of Heaven* (Yale University Press, 1974) — **lưu ý đây là chuyên khảo về Ngụy Trưng và chế độ gián quan, dùng cho vế ấy chứ không dùng cho vế bộ luật**; về luật xem **Wallace Johnson, *The T'ang Code* (Princeton University Press, 1979)**." ✓ Cả cảnh báo lẫn nguồn bù đều có.
  - **McRae** — `CH05-CE07-07` viết "**McRae tuy nhận phần sử liệu vẫn phản đối cách Hồ Thích quy giản Thiền tông thành chuyện tranh quyền**" ✓.
- **Cảnh báo Plofker kiểm được tới nguồn và đúng.** Bodleian/Oxford công bố lại niên đại bản thảo Bakhshali **ngày 14-10-2024** thành **799–1102 CE** (folio 16 lùi về 931–1032), sau một lượt carbon lại năm 2018 — khớp "tháng 10/2024" và "799–1102" của khối. Và Plofker đúng là người đứng đầu nhóm phản đối công bố 2017: *"The Bakhshālī Manuscript: A Response to the Bodleian Library's Radiocarbon Dating"*, **History of Science in South Asia** 5.1 (2017), tr. 134–150, doi `10.18732/H2XT07`. Hệ quả khối rút ra cũng đúng: trước tháng 9/2024 bản thảo ấy được coi là văn bản Ấn Độ sớm nhất mang ký hiệu số không, nên việc lùi niên đại làm mệnh đề "văn bản sớm nhất còn lại" của `CH05-CE07-08` vững hơn chứ không yếu đi.
- **Không nguồn nào trong bốn nguồn này mang URL** (cả bốn là sách in), nên không có URL để trỏ nhầm người. URL duy nhất của cả nhóm CE07 nằm ở `CH05-CE07-10`: Stanford Encyclopedia of Philosophy, mục "Dharmakīrti". Tôi tự mở `https://plato.stanford.edu/entries/dharmakiirti/` (UA `history-atlas/0.1 (research)`): **HTTP 200, 145.892 byte**, `<title>` = "Dharmakīrti (Stanford Encyclopedia of Philosophy)", có tên **Tillemans** trong trang. Đúng người, đúng tiết, đúng tác giả.

**NÊN — cảnh báo thứ tư là cái duy nhất chưa vào mục, và khối không nói ra sự bất đối xứng ấy.**

Với ba nguồn đầu, khối ghi rõ mục đã làm gì ("mục đã ghi thẳng điều đó", "mục đã bổ sung Wallace Johnson"). Với Plofker, khối chỉ mô tả tình trạng học thuật rồi dừng. Đối chiếu `CH05-CE07-08`: trường `Nguồn` ghi "Kim Plofker, *Mathematics in India* (Princeton University Press, 2009)" **không kèm cảnh báo nào**, và phần văn xuôi không nhắc Bakhshali. Tức ba cảnh báo đã vào văn bản, một thì chưa — và đó lại là cảnh báo duy nhất gắn với một kết luận "vừa mới đảo chiều", tức dễ rữa nhất.

Không phải lỗi sự thật, nên không xếp BẮT BUỘC. Nhưng một khối mang tên "bốn nguồn **phải đọc kèm cảnh báo**" mà để người đọc tưởng cả bốn đã được xử lý như nhau thì đang che mất việc còn phải làm.

*Câu thay thế đề nghị:* "Plofker là người đứng đầu nhóm phản đối cách công bố niên đại Bakhshali năm 2017 (*History of Science in South Asia* 5.1, tr. 134–150) — liên quan vì **14-10-2024** Bodleian đã lùi niên đại bản thảo ấy về **799–1102**, tức mệnh đề "văn bản sớm nhất còn lại" của mục Brahmagupta vững hơn trước. **Khác ba nguồn trên, cảnh báo này chưa vào mục**: `CH05-CE07-08` dẫn Plofker không kèm ghi chú và không nhắc Bakhshali. Để nguyên cũng được, vì mệnh đề của mục đang được củng cố chứ không bị đe doạ — nhưng nếu niên đại đảo chiều lần nữa thì đây là mục phải mở lại đầu tiên."

**CÂN NHẮC — "Plofker là người phản đối" gán cho một người cái của năm người.**

Bài phản hồi 2017 có năm đồng tác giả: Kim Plofker, Agathe Keller, Takao Hayashi, Clemency Montelle, Dominik Wujastyk. Viết "Plofker là người phản đối" không sai về thực chất (bà đứng tên đầu, và bà là tác giả của chính cuốn sách mục đang dẫn), nhưng với một dự án mà quy tắc 7 đòi biết nguồn **lập luận gì**, ghi "Plofker và cộng sự (2017)" chính xác hơn và cũng dễ tra hơn.

---

## Khối 9 — **Ứng viên Việt Nam trong nhóm CE07 (yêu cầu D5)** (dòng 1138–1139)

**Đã kiểm được (không có phát hiện)**

- **Yêu cầu D5 được thoả về mặt cơ chế.** `atlaslib/lint.py` dòng 46–48 cảnh báo khi `## Ghi chú biên tập` không chứa chuỗi chuẩn hoá "viet"/"vietnam"; khối này có mặt và nêu đích danh người, nên cảnh báo không nổ.
- **Mai Thúc Loan có mục thật:** `content/ch90.md` dòng 122, `CH90-CE01_09-06 · Mai Hắc Đế (Mai Thúc Loan)`. Và "722, thuộc thế kỷ 8" ✓ — `group_range('CE08') = (701, 800)` chứa 722, nên ông đúng là nằm ngoài nhóm CE07.
- **Tì-ni-đa-lưu-chi:** mất **594** ✓ (`Q4111528`, `P570 = +0594`, ghi trong `reports/ch05-ce06-slot12.md` §1); `group_range('CE06') = (501, 600)` chứa 594, nên "thuộc nhóm CE06" đúng. Mục của ông là `CH90-CE01_09-04` ✓, và việc để P4 quyết có nên chuyển ông lên atlas chính khớp đúng khối ở dòng 1103–1105 — **không mâu thuẫn nội bộ**.
- An Nam đô hộ phủ từ **679** và khởi nghĩa **687** khớp chính sử phổ thông. **[KHÔNG KIỂM ĐƯỢC]** tới nguồn sơ cấp: tôi không mở ĐVSKTT hay Cựu/Tân Đường thư để đối chiếu hai mốc này.

**BẮT BUỘC — "đều đã có chỗ trong phụ lục `ch90`" sai với hai trong ba cái tên: Lý Tự Tiên và Đinh Kiến không có mục ở bất kỳ đâu trong atlas.**

Câu sai, nguyên văn: *"Các nhân vật được định danh trong giai đoạn này — **Lý Tự Tiên và Đinh Kiến (khởi nghĩa 687)**, Mai Thúc Loan (722, thuộc thế kỷ 8) — **đều đã có chỗ trong phụ lục `ch90`** và được đo bằng hệ quy chiếu của phụ lục."*

Bằng chứng: `grep -rn "Tự Tiên" content/ data/ reports/` và `grep -rn "Đinh Kiến" content/ data/ reports/` mỗi lệnh trả về **đúng hai dòng, và cả hai là chính câu này** (`content/ch05.md` dòng 1139 và bản sao của nó trong `data/persons.json` dòng 673). Không có mục nào mang tên họ.

Nhóm `CH90-CE01_09` hiện có **tám** mục: Trưng Trắc, Bà Triệu, Sĩ Nhiếp, Tì-ni-đa-lưu-chi, Lý Nam Đế, Mai Hắc Đế, Phùng Hưng, Khương Công Phụ. Hai cái tên của năm 687 không nằm trong đó.

Đây là lỗi hai chiều. Thứ nhất, nó sai sự thật về repo. Thứ hai, nó **làm hỏng chính lập luận của khối**: câu đang nói "họ đã được đo ở thang phụ lục rồi, nên không cần xét ở thang toàn nhân loại" — nhưng nếu họ chưa từng có mục thì chưa ai đo họ ở thang nào cả, và khoảng trống ấy chỉ đang được giấu đi. Ngược với ca quy tắc 6 thông thường (nêu ứng viên bị loại cho một người **đã có** mục), đây là ca gán mục cho người **chưa có** — nhưng hệ quả vẫn vậy: câu văn tự mâu thuẫn, và không có đánh đổi nào thật sự xảy ra.

*Câu thay thế đề nghị:* "Các nhân vật được định danh trong giai đoạn này là **Lý Tự Tiên và Đinh Kiến** (khởi nghĩa 687). **Cả hai hiện không có mục ở bất kỳ chapter nào, kể cả phụ lục `ch90`** — nhóm `CH90-CE01_09` đang có tám mục và không ai trong số đó là họ — nên theo quy tắc 6 họ là ứng viên bị loại hợp lệ, và không ai trong hai người vượt được bốn tiêu chí ở thang toàn nhân loại; vì vậy nhóm CE07 không có mục Việt Nam nào ở atlas chính. **Việc có nên bổ sung họ vào phụ lục hay không là một câu hỏi để ngỏ, không phải một việc đã làm.** Mai Thúc Loan (khởi nghĩa 722) **có** mục ở phụ lục — `CH90-CE01_09-06` — nhưng thuộc thế kỷ 8 nên nằm ngoài nhóm này."

---

## Khối 10 — **Charlemagne ở nhóm thế kỷ 8, và vòng duyệt đã bác tiền đề của người ra đề** (dòng 1141–1142)

**Đã kiểm được (không có phát hiện)**

- **Vòng duyệt có thật và đúng như khối kể.** `reports/ch05-ce08-gate.md` §2.3 mang tiêu đề "[ĐÃ QUYẾT] Charlemagne — **CE08**, không phải CE09 (tôi không đồng ý với tiền đề của đề bài)" và mở đầu: "Đề bài viết 'Theo §3 thì CE09 có lý hơn CE08'… **tôi kết luận ngược lại**".
- **`group_range('CE08')` trả về `(701, 800)`** ✓ — tôi tính lại từ `atlaslib/common.py` dòng 91–102: với `era == "CE"`, `((8-1)*100+1, 8*100)` = `(701, 800)`. Nhóm **bao gồm cả năm 800**, đúng như khối nói.
- **Lễ đăng quang 25-12-800** ✓ — `reports/ch05-ce08-gate.md` dẫn nguyên văn "on **Christmas Day 800**".
- **Chuỗi sự kiện thế kỷ 8** ✓ — diệt vương quốc Lombard **774**, thu phục Bavaria **788**, chiến dịch Avar **791–796**, Alcuin tới triều đình **782**, sứ bộ Harun al-Rashid **thập niên 790**: khớp từng mốc với bảng §2.3.
- **"Lint im lặng ở cả hai phương án (đời 748–814 giao với cả hai khoảng nhóm)"** ✓ — tôi chạy lại logic `atlaslib/lint.py` dòng 122–125 bằng tay: cảnh báo chỉ nổ khi `d < rng[0] or b > rng[1]`. Với CE08 `(701,800)`: `814 < 701`? không; `748 > 800`? không → im. Với CE09 `(801,900)`: `814 < 801`? không; `748 > 900`? không → im. Mục `CH05-CE08-06` ghi `năm: k. 748–814 CN`, đúng cặp số khối dùng.
- **Tiền lệ Āryabhaṭa có thật và nhất quán** ✓ — `content/ch05.md` dòng 1059–1061, khối "**Āryabhaṭa không ở chapter này, và vì sao**", viết đúng nguyên tắc ấy và đúng chiều.

**BẮT BUỘC — "33 trong 46 năm trị vì" không khớp chính bảng mà nó rút gọn: 33 + 14 = 47.**

Câu sai, nguyên văn: *"Đếm theo giai đoạn ảnh hưởng: **33 trong 46 năm trị vì**, việc diệt vương quốc Lombard…"*

Bảng ở `reports/ch05-ce08-gate.md` §2.3, Lập luận 2, chia rành mạch:

| | thuộc CE08 (701–800) | thuộc CE09 (801–900) |
|---|---|---|
| Số năm trị vì | **33 năm** (768–800) | **14 năm** (801–814) |

33 + 14 = **47**, không phải 46. Hai con số đếm năm dương lịch mà triều ông chạm tới (768…800 là 33 năm; 801…814 là 14 năm), và tổng của cách đếm ấy là 47. Viết "33 trong 46" là trộn hai quy ước: 46 là **độ dài** triều đại (768→814), còn 33 là **số năm dương lịch**. Trong cùng một câu thì phải cùng một thước.

Chỗ này nhỏ nhưng đúng loại lỗi mà các vòng trước đã phải sửa (CE10 từng viết 15/20 trong khi thực tế là 17/20), và nó nằm ngay ở mệnh đề định lượng duy nhất chống đỡ cả kết luận.

*Câu thay thế đề nghị:* "Đếm theo giai đoạn ảnh hưởng: **33 trong 47 năm dương lịch mà triều ông chạm tới — 768–800 thuộc thế kỷ 8, chỉ còn 801–814 là mười bốn năm thuộc thế kỷ 9** — và việc diệt vương quốc Lombard, thu phục Bavaria, các chiến dịch Avar, việc Alcuin tới triều đình cùng sứ bộ với Harun al-Rashid đều thuộc thế kỷ 8."

**NÊN — "rơi vào sáu ngày cuối" đảo nghĩa câu gốc và sai một ngày.**

Nguyên văn: *"…nên lễ đăng quang ngày 25-12-800 **rơi vào sáu ngày cuối** của chính nhóm ấy chứ không nằm ngoài."*

Câu gốc ở `reports/ch05-ce08-gate.md` §2.3 viết: "rơi vào **tuần cuối cùng** của nhóm CE08 — **sớm hơn ranh giới đúng sáu ngày**." Đó là "cách ranh giới sáu ngày", không phải "nằm trong sáu ngày cuối". Sáu ngày cuối của năm 800 là 26–31/12, **không chứa** 25/12; 25/12 là ngày thứ bảy tính từ cuối.

*Câu thay thế đề nghị:* "…nên lễ đăng quang ngày 25-12-800 rơi vào **tuần cuối cùng** của chính nhóm ấy — **cách ranh giới đúng sáu ngày** — chứ không nằm ngoài."

**CÂN NHẮC — "quy tắc §3" trỏ tới một chỗ mà `§3` không phải số hiệu của nó, và câu chữ của quy tắc nói "năm sinh" chứ không nói "năm mất".**

Quy tắc thật nằm ở `prompts/atlas-prompt.md` dòng 19, **khoản 3** của danh sách trong **§5**: "Xếp nhân vật vào thế kỷ của giai đoạn ảnh hưởng chính (floruit / tác phẩm hoặc hành động quan trọng nhất), **không theo năm sinh**." Hai chỗ đáng chỉnh: (i) gọi nó là "§3" dễ khiến vòng sau đi tìm một mục §3 không tồn tại — `CONTRIBUTING.md` chỉ dẫn "`prompts/atlas-prompt.md` (§5)"; (ii) văn bản quy tắc chặn việc xếp theo **năm sinh**, còn lập luận ở đây chặn việc xếp theo **năm mất**. Tinh thần thì phủ cả hai đầu và lập luận vẫn đứng, nhưng nếu muốn khối chịu được soi thì nên viết "khoản 3 của `prompts/atlas-prompt.md` §5 — xếp theo giai đoạn ảnh hưởng chính chứ không theo mốc sinh hay mốc mất".

**CÂN NHẮC — "sứ bộ với Harun al-Rashid đều thuộc thế kỷ 8" đúng với phần trao đổi, nhưng repo có một mốc 802 ở chỗ khác.**

`reports/ch05-ce09-gate.md` dòng 114 ghi "con voi Abul-Abbas, **802**", tức chi tiết nổi tiếng nhất của quan hệ ấy rơi vào thế kỷ 9, trong khi `reports/ch05-ce08-gate.md` ghi việc trao đổi sứ giả ở "**thập niên 790**". Cả hai đều đúng về phần mình, nhưng một vòng sau đọc khối 10 rồi gặp mốc 802 sẽ tưởng có mâu thuẫn. Thêm bốn chữ là chặn được: "sứ bộ với Harun al-Rashid **khởi từ thập niên 790**".

---

## Tổng kết

### Bảng đếm theo khối

| Khối | Dòng | Tên rút gọn | BẮT BUỘC | NÊN | CÂN NHẮC |
|---|---|---|---|---|---|
| 1 | 1110 | Nhóm CE07 đã qua một vòng bình duyệt chọn người độc lập | 0 | 0 | 1 |
| 2 | 1113 | Một Q-ID suýt vào atlas trỏ sang một chi bướm | **2** | 0 | 0 |
| 3 | 1116 | Niên đại Pháp Xứng: Wikidata tự mâu thuẫn | **1** | 1 | 0 |
| 4 | 1119 | Tuổi thọ Pakal: bi ký nói 80, bộ xương nói 40–50 | **2** | 0 | 0 |
| 5 | 1123 | Một đính chính về phạm vi phụ lục | **1** | 1 | 1 |
| 6 | 1127 | Vùng của Tùng Tán Cán Bố | **1** | 0 | 0 |
| 7 | 1130 | Bốn mệnh đề bị vòng kiểm sự kiện bác | **1** | 0 | 1 |
| 8 | 1135 | Bốn nguồn phải đọc kèm cảnh báo (quy tắc 7) | 0 | 1 | 1 |
| 9 | 1138 | Ứng viên Việt Nam trong nhóm CE07 (D5) | **1** | 0 | 0 |
| 10 | 1141 | Charlemagne ở nhóm thế kỷ 8 | **1** | 1 | 2 |
| **Tổng** | | | **10** | **4** | **6** |

### Mười lỗi BẮT BUỘC, gom theo loại

**A. Tự khai sai về trạng thái văn bản (3 lỗi) — loại nặng nhất, vì mục Ghi chú biên tập tồn tại để vòng sau khỏi mở lại từng mục.**
1. **Khối 4:** khai mục "viết 'nghiêng về phía bi ký'" — `CH05-CE07-12` **không có câu ấy và không nhắc tranh luận tuổi thọ ở bất kỳ dạng nào**.
2. **Khối 7:** khai "chiếu chỉ cấm xuất cảnh năm 629 … không được viết vào mục" — `CH05-CE07-06` **có viết**, dạng quy nguồn kèm phản chứng.
3. **Khối 9:** khai Lý Tự Tiên và Đinh Kiến "đều đã có chỗ trong phụ lục `ch90`" — **cả hai không có mục ở bất kỳ chapter nào**; `grep` chỉ trả về chính câu ấy.

**B. Mô tả sai phép kiểm của repo (1 lỗi) — đúng loại mà vòng CE09 đã bắt một lần.**
4. **Khối 2:** "Lint không bắt được loại lỗi này vì nó chỉ đọc định dạng Q-ID chứ không đọc nội dung" — `lint_wikidata` đọc nhãn, đọc `P31`, đối chiếu `P569`/`P570`; cả ba Q-ID bẫy đều nổ cảnh báo ở chế độ online. Cái lint thiếu là **mức** (WARN, không chặn build), không phải tầm nhìn.

**C. Số liệu rữa — đúng lúc viết, sai bây giờ, lại viết ở thì hiện tại (2 lỗi).**
5. **Khối 5:** "Đông Nam Á vẫn chỉ có đúng một người trong atlas chính (0,5%)" và "Java … vẫn trống hoàn toàn" → nay **4 người, 1,6%**, và Java đã được `CH05-CE10-06` Mpu Sindok lấp.
6. **Khối 6:** "nâng con số Trung Á từ 0,5% lên khoảng 1%" → nay Trung Á **1,6%**, đổi vùng sẽ thành **2,0%**.

**D. Sai số học / sai con số so với chính nguồn của khối (3 lỗi).**
7. **Khối 4:** ngày sinh–mất Pakal ghi 24-3-603 / 29-8-683, trong khi `Q371384` và `reports/ch05-ce07-select.md` đều ghi **23-3-603 / 28-8-683** — lệch đúng +1, đúng hình dạng mà `CONTRIBUTING.md` quy tắc 3 mô tả.
8. **Khối 10:** "33 trong 46 năm trị vì" — bảng nguồn cho 33 + 14, tổng **47**.
9. (cùng loại, ở khối 2) "**mười hai** Q-ID nhớ sai của nhóm CE08" — không báo cáo nào ghi con số ấy; CE08 bắt được **không** Q-ID sai nào.

**E. Sai thứ tự / sai quy kết sự kiện trong chính repo (1 lỗi).**
10. **Khối 2:** "lần thứ hai trong Chapter 5 … lần trước là … nhóm CE08" — `reports/ch05-ce08-gate.md` dòng 370 viện chính ca CE07 này làm **tiền lệ**, nên CE08 đến **sau**, không phải trước.

**Nhận xét chung.** Phần Wikidata của cụm này rất vững: tôi tự tra lại `Q311215`, `Q371384`, `Q641749`, `Q4017694`, `Q457990`, `Q379239` và **mọi giá trị thô mà khối ghi đều đúng**. Điểm yếu lặp lại nằm ở ba chỗ khác, và cả ba đều kiểm được mà không ra khỏi repo: (i) khối **tự khai việc đã làm** mà không mở lại mục để xác nhận — 3/10 lỗi; (ii) khối **rút gọn một bảng trong báo cáo nguồn** rồi làm hỏng số hoặc đảo nghĩa — khối 10 hỏng cả hai cách, khối 2 hỏng theo cách thứ nhất; (iii) khối **gắn lập luận đúng vào một tỉ lệ không tự rào thời điểm**, mà `reports/stats.txt` lại không khai thời điểm đo, nên con số rữa mà không ai thấy. Hai khối 5 và 6 đều thuộc loại (iii) và lập luận của cả hai **vẫn đứng sau khi bỏ hẳn tỉ lệ** — đó là cách chữa rẻ nhất.

### Mọi chỗ `[KHÔNG KIỂM ĐƯỢC]`

1. **Khối 4** — không mở được Tiesler & Cucina 2006 hay một bộ chuyển Long Count, nên **không loại trừ được** khả năng chênh +1 ngày của ngày sinh/mất Pakal đến từ quy ước lịch (Julian so với proleptic Gregorian) chứ không từ lỗi chép. Đề xuất thay thế ở khối 4 đã ghi thẳng điều này vào trong câu.
2. **Khối 7** — niên đại "k. 424–430" cho bản dịch Đại Vân kinh của Đàm Vô Sấm chỉ truy được tới `reports/ch05-ce07-facts.md`, nơi cũng không kèm nguồn mở được. Không xác nhận được bằng kinh lục. (Mệnh đề này **không** nằm trong mục nào, nên rủi ro chỉ ở ghi chú.)
3. **Khối 9** — hai mốc "An Nam đô hộ phủ từ 679" và "khởi nghĩa 687" khớp chính sử phổ thông nhưng **không đối chiếu tới nguồn sơ cấp** (ĐVSKTT, Cựu/Tân Đường thư) trong vòng này.

Ngoài ba chỗ trên, mọi mệnh đề được nêu trong báo cáo này đều đã kiểm tới `content/`, `reports/`, `atlaslib/`, `prompts/`, hoặc tới một lệnh gọi `wbgetentities` / HTTP do chính vòng này thực hiện với User-Agent `history-atlas/0.1 (research)`.
