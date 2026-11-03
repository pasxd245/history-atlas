# Bình duyệt độc lập — ghi chú biên tập vòng CE08, phần 1 (8 khối)
Ngày: 2026-11-02 · phạm vi: content/ch05.md, từ khối "Khung 788–820 của Shankara" tới khối "Divashtich"

Phương pháp: định vị 8 khối bằng `grep -n` trên tiêu đề (không bằng số dòng). Đọc trước khi soi:
12 mục `CH05-CE08-01` … `-12`, `reports/stats.txt`, `CONTRIBUTING.md`, `README.md`,
`content/ch90.md`, `atlaslib/lint.py`, `reports/ch05-ce08-gate.md`, `reports/ch05-ce09-review-c.md`,
`reports/ch05-ce09-review-d.md`, `reports/ch05-ce10-notes-review.md`.
Mọi Q-ID được tra lại trực tiếp bằng `wbgetentities` trong vòng này (User-Agent trung lập
`history-atlas/0.1 (research)`), không tin con số chép trong file hay trong hồ sơ cổng.
Báo cáo được ghi **tăng dần**: soi xong khối nào ghi ngay khối đó.

**Nền thống kê dùng cho mọi phép tính lại:** `reports/stats.txt` hiện ghi **245 nhân vật (atlas chính)
+ 40 phụ lục**. Hồ sơ cổng CE08 (`reports/ch05-ce08-gate.md:§0`) ghi nền **208 người** lúc viết.
Mọi tỉ lệ trong tám khối này vì vậy phải được đọc như số đo của một atlas nhỏ hơn 37 người.

---

## Khối 1 — Khung 788–820 của Shankara không phải truyền thống của các maṭha

**Đã kiểm được (không có phát hiện)**
- **Ba niên đại maṭha**: Śṛṅgeri **483 TCN**, Kanchipuram **509 TCN**, Dvārakā **491 TCN** — cả ba khớp
  nguồn tham khảo phổ thông (en.wikipedia "Adi Shankara", mục *Matha datings*, HTTP 200, 59.922 B, tra
  trong vòng này). Mệnh đề "truyền thống của chính các maṭha đặt ông ở thế kỷ 5 TCN" đúng.
- **Bản ghi Śṛṅgeri**: đúng là chỉ nói ông sinh vào **năm thứ mười bốn** đời một vua tên "Vikramāditya"
  mà không cho biết là Vikramāditya nào. Đúng.
- **Vikramāditya II của triều Cālukya (733–746)**: khung trị vì khớp. Số học trong khối cũng khớp —
  733 là năm thứ nhất thì năm thứ mười bốn là 746, và 733–746 đúng là mười bốn năm, nên câu "năm thứ
  mười bốn rơi đúng vào cuối triều" tự nhất quán.
- **Danh sách người phổ biến khung 788–820**: Max Müller, Macdonell, Deussen, Radhakrishnan — khớp.
  Tên "**C.P.** Tiele" trong khối **đúng hơn** nguồn phổ thông (viết "K.P. Tiele"): Cornelis Petrus
  Tiele, 1830–1902. Hai năm đời cũng đúng. Không sửa.
- **Mục khớp với khối ở ba điểm**: `CH05-CE08-11` ghi `k. 700 – k. 750 CN`, `độ tin cậy niên đại: Thấp`,
  và có dòng `Kế thừa từ: CH05-CE07-10 · phản bác · trực tiếp` (Pháp Xứng). Khối không nêu tỉ lệ nào,
  nên không có số liệu rữa ở đây.
- **Câu "không phải mẹo né lint"**: kiểm được và đúng theo nghĩa khối nói. `atlaslib/lint.py`
  (`lint_wikidata`) lấy `tol = C.DATE_TOLERANCE.get(p["confidence"])`; `Thấp` trả `None` nên hàm ghi
  INFO *"độ tin cậy Thấp — bỏ qua đối chiếu niên đại"* rồi `continue`. Tức mức `Thấp` **thật sự** làm
  lint im lặng trước khoảng lệch 88 năm giữa mục (k. 700–750) và Wikidata (`Q180967` P569 = +0788,
  P570 = +0820, cả hai precision 9) — khối tự khai điều đó thay vì giấu, đúng tinh thần quy tắc 4.

**BẮT BUỘC** — câu sai, nguyên văn: *"Học giới hiện nay chặn hai đầu bằng văn bản — Śaṅkara trích nguyên
văn Pháp Xứng, và Vācaspati Miśra sớ cho ông ở nửa đầu thế kỷ 9 — nên mục ghi `k. 700 – k. 750 CN` với
độ tin cậy `Thấp`."*

Sai ở đâu: vế **Vācaspati Miśra** được viết như một mốc chắc, trong khi vòng CE10 đã bác đúng vế ấy và
đã gỡ nó khỏi thân mục. Khối và mục nay nói ngược nhau về cùng một mỏ neo. Bằng chứng ba lớp, đều trong repo:

1. Thân mục `CH05-CE08-11` hiện viết: *"còn mỏ neo Vācaspati Miśra (`CH05-CE10-07`) thì **lỏng hơn vẻ
   ngoài**, vì niên đại của chính Vācaspati có hai cách đọc cách nhau 135 năm."*
2. Khối *"Vācaspati Miśra có thể không thuộc thế kỷ này…"* của chính `## Ghi chú biên tập`
   (`content/ch05.md:1251`) ghi: *"mục `CH05-CE08-11 · Ādi Shankara` trước đây dùng Vācaspati làm mốc
   chặn trên và ghi ông 'sớ cho ông ở nửa đầu thế kỷ 9' — câu ấy **chỉ đúng nếu nhận cách đọc 841**, tức
   mâu thuẫn với chính mục mới."* `CH05-CE10-07` chọn cách đọc Śaka (976) và ghi `độ tin cậy: Thấp`.
3. Cụm *"sớ cho ông ở nửa đầu thế kỷ 9"* mà khối 1 còn giữ là **đúng nguyên văn** câu đã bị gỡ khỏi mục.
   (Vòng CE10 ghi nhận là không truy được nguyên văn bản nháp — `reports/ch05-ce10-notes-review.md`,
   mục `[KHÔNG KIỂM ĐƯỢC]` số 2; câu ấy vẫn còn **trong khối 1**, nên vòng này truy được.)

Ghi thêm cho đầy đủ: mốc Vācaspati "nửa đầu thế kỷ 9 → chặn trên k. 800" đúng là lập luận chuẩn trong tài
liệu tham khảo ngoài repo. Vấn đề không phải nó lạ, mà là **atlas này đã quyết khác** và khối chưa theo.

Đề xuất câu thay thế nguyên văn:
> Học giới hiện nay chặn đầu dưới bằng văn bản — Śaṅkara trích nguyên văn Pháp Xứng, nên không sớm hơn giữa thế kỷ 7 — còn đầu trên thì lỏng hơn vẻ ngoài: mốc quen dùng là bản sớ của Vācaspati Miśra, mà niên đại của chính Vācaspati (`CH05-CE10-07`) có hai cách đọc cách nhau 135 năm. Mục vì vậy ghi `k. 700 – k. 750 CN` với độ tin cậy `Thấp`, và không treo kết luận vào mốc ấy.

**NÊN** — khối và mục mô tả vai của giới Đông phương học **khác nhau**, và khối tự mâu thuẫn trong ba câu.

Khối viết: *"đóng góp của giới Đông phương học là **chọn và phổ biến** một niên đại vốn có nguồn Ấn Độ,
không phải chế ra nó"*. Thân mục `CH05-CE08-11` lại viết: *"khung 788–820 … là **đề xuất** của Đông
phương học châu Âu cuối thế kỷ 19"*. "Đề xuất" là đúng cái nghĩa mà khối vừa loại trừ. Một vòng sau đọc
hai câu này sẽ không biết câu nào là phán quyết.

Đề xuất câu thay thế nguyên văn (cho **thân mục**, giữ khối như nó đang viết):
> Niên đại của ông là tranh luận mở, và khung 788–820 hay được chép lại không phải truyền thống của các maṭha mà là khung được giới Đông phương học châu Âu cuối thế kỷ 19 chọn và phổ biến; các maṭha đặt ông ở thế kỷ 5 trước Công nguyên.

**CÂN NHẮC** — chuỗi truyền của khung 788–820 chưa kiểm được.

Khối viết chuỗi: Tiele lấy từ *Āryavidyā-sudhākara* của **Yajñeśvara Śāstrī**, vốn dẫn lại
*Śaṅkara-mandāra-saurabha* của **Bhaṭṭa Nīlakaṇṭha*. `[KHÔNG KIỂM ĐƯỢC]` — tài liệu tham khảo phổ thông
tôi mở được chỉ nói khung ấy *"được các học giả cuối TK 19 – đầu TK 20 đề xuất, theo sau Tiele"* và
**không** chứa hai nhan đề lẫn hai tên người ấy; tôi không mở được công trình chuyên ngành nào nêu chuỗi
truyền này. Chuỗi ấy là thứ làm cho vế "không phải chế ra nó" đứng được, nên nếu vòng sau không xác minh
được nó từ một nguồn chuyên ngành, phải hoặc bỏ chuỗi, hoặc gắn nhãn là chưa kiểm — đúng quy ước
`[KHÔNG KIỂM ĐƯỢC]` mà hồ sơ cổng CE08 đã đặt.

**CÂN NHẮC** — khối bỏ mất cách đọc "Vikramāditya" thứ hai.

Khối chỉ nêu một cách đọc (Vikramāditya II Cālukya). Tài liệu tham khảo phổ thông nêu thêm một cách đọc
quy về **Chandragupta II (thế kỷ 4 CN)**, và chính cách đọc ấy mới làm rõ vì sao bản ghi Śṛṅgeri "không
chốt được gì". Thêm nửa câu sẽ làm luận điểm của khối mạnh hơn chứ không yếu đi.

---

## Khối 2 — Hai chữ "Nhất Hạnh", và một va chạm cách nhau 1.200 năm

**Đã kiểm được (không có phát hiện)**
- **Nhãn vi của `Q710705` đúng là "Nhất Hạnh" trần**, và **không có description tiếng Việt**. Tra lại
  trực tiếp trong vòng này: `labels.vi = "Nhất Hạnh"`, `descriptions.vi` không tồn tại. Cả hai mệnh đề đúng.
- **`僧一行` là alias có thật trong trường `zh` của chính `Q710705`**, không phải tên atlas tự đặt. Đúng.
  Bốn alias zh hiện có: `僧一行`, `唐一行`, `张遂`, `一行禅师`. Trường `aliases.vi` còn có `Trương Toại`,
  tức cả cụm `tục danh Trương Toại 張遂` trong tên mục cũng có chỗ dựa trên Wikidata.
- **`CH90-CE19_20-10 · Thích Nhất Hạnh (釋一行)` có thật ở phụ lục** (`content/ch90.md:657`), Q-ID
  `Q310913` — **khác** `Q710705`. Hai người, hai Q-ID, không phải một mục trùng.
- **"Cách nhau mười hai thế kỷ" / "1.200 năm"**: `k. 683–727` so với `1926–2022`, chênh 1.243 năm ở năm
  sinh. Cả tiêu đề lẫn thân khối đều ở trong sai số của cách nói ấy. Nhất quán.
- **Tên mục giữ lint im lặng, và đó là một lý do kỹ thuật thật.** `atlaslib/common.py:358 wd_names()`
  gộp cả `labels` lẫn `aliases`, nên `僧一行` trong `name_orig` khớp một alias và phép kiểm "nhãn Wikidata
  không khớp tên" không nổ. `reports/lint-ch05.txt` xác nhận: **ERROR 0 · WARN 0**, không có mục nào cho
  `CH05-CE08-08`. Tên mục vừa tránh va chạm vừa qua được cổng — khối không phải sửa gì ở đây.
- **Thân mục khớp khối**: `CH05-CE08-08` viết *"Ông không liên quan gì tới Thích Nhất Hạnh (1926–2022),
  người có mục riêng ở phụ lục."* Không có mâu thuẫn giữa khối và mục.

Không có phát hiện mức **BẮT BUỘC** hay **NÊN** ở khối này.

**CÂN NHẮC** — khối nên nói thẳng rằng **lint không có phép kiểm nào đỡ cho chỗ này**, vì đó mới là lý do
câu "Đừng sửa" phải tồn tại.

Tôi kiểm `atlaslib/lint.py:lint_global`: vòng `by_name` so bằng `C.norm_name(p["name_vi"])` và vòng
`by_q` so bằng Q-ID. Ở đây `name_vi` là `Tăng Nhất Hạnh` so với `Thích Nhất Hạnh` (khác chuỗi), còn Q-ID
là `Q710705` so với `Q310913` (khác). Cả hai vòng đều im. Quan trọng hơn: **nếu một vòng sau "sửa" tên
mục thành `Nhất Hạnh` trần đúng như khối lo, lint vẫn im** — `Nhất Hạnh` vẫn khác chuỗi `Thích Nhất Hạnh`
và Q-ID vẫn khác. Tức không có cổng tự động nào bắt được cú sửa ấy; khối ghi chú này là lớp bảo vệ duy
nhất. Thêm một câu nói rõ điều đó làm khối mạnh hơn hẳn.

Đề xuất câu thêm nguyên văn (đặt ngay trước câu cuối "Đừng sửa."):
> Không cổng tự động nào đỡ chỗ này: lint chỉ đối chiếu `name_vi` theo chuỗi và Q-ID theo Q-ID, mà hai mục khác nhau ở cả hai, nên nếu tên bị sửa thành "Nhất Hạnh" trần thì `build.py` vẫn báo sạch.

---

## Khối 3 — Wikidata khai độ chính xác, nó không khai độ tin cậy

**Đã kiểm được (không có phát hiện)** — tất cả tra lại trực tiếp bằng `wbgetentities` trong vòng này:
- **Shankara `Q180967`**: P569 = `+0788`, P570 = `+0820`, cả hai precision 9. Khớp "788–820".
- **Jabir `Q167852`**: P569 = `+0721`, P570 = `+0815`, mỗi claim **đúng một** tham chiếu, và nguồn của
  tham chiếu ấy là `P248 = Q18609226`, nhãn en đúng là **"Trove"**, kèm `P1315` (People Australia ID).
  Mệnh đề *"chỉ có một tham chiếu trỏ về Trove, cổng thư mục của Thư viện Quốc gia Úc"* **đúng từng chữ**.
- **Padmasambhava `Q231582`**: P569 = `+0717`, P570 = `+0762`, mỗi claim một tham chiếu, và tham chiếu ấy
  mang `P214` (VIAF). Mệnh đề *"tham chiếu duy nhất là P214 VIAF"* đúng.
- **Charles Martel `Q3301`**: P569 = `+0688-08-23` **precision 11**, P570 = `+0741-10-22` **precision 11**;
  P570 có **0 tham chiếu**; P569 có **1** tham chiếu, chỉ gồm `P248`. Ba mệnh đề đều đúng.
- **Cặp đối chứng Sibawayh / Bêđa**: `CH05-CE08-05` ghi `Thấp`, `CH05-CE08-07` ghi `Cao` — khớp mục.
  `Q983355` P569 = `+0760` precision 9 với tham chiếu **duy nhất là `P143`** (import từ Wikipedia), tức
  "một con số gọn" mà chỗ dựa gần bằng không — đúng như khối nói. Khung chết lệch 19 năm và khác nơi
  chết: `reports/ch05-ce08-review.md:391` đã xác nhận ✓ ở vòng trước; tôi không mở lại nguồn cổ điển, nên
  phần "19 năm" là **kiểm được trong repo, không kiểm lại ngoài repo**.
- Nguyên tắc khối đặt ra — chấm `độ tin cậy niên đại:` theo biên độ giữa các giá trị cạnh tranh chứ
  không theo `precision` — **không** va với `CONTRIBUTING.md`: ở đó `độ tin cậy` chỉ điều khiển dung sai
  đối chiếu (Cao ±5 · Trung bình ±25 · Thấp bỏ qua), không được định nghĩa theo `precision`.

**BẮT BUỘC** — câu sai, nguyên văn: *"Nói cách khác: trong nhóm CE08, bốn niên đại được khai ở độ chính
xác cao nhất lại là bốn niên đại yếu nhất."*

Sai ở đâu: câu tổng kết này mâu thuẫn với **chính bốn dữ kiện mà khối vừa liệt kê ba dòng trên**, và còn
sai cả phạm vi.

1. **Chỉ một trong bốn được khai ở "độ chính xác cao nhất".** Tra lại: Shankara `+0788` **precision 9**,
   Jabir `+0721` **precision 9**, Padmasambhava `+0717` **precision 9** — cả ba là **năm trần**. Chỉ
   Charles Martel đạt `precision 11`. Chính khối cũng viết tách bạch điều đó (*"Charles Martel: ngày sinh
   và ngày mất **đều** khai tới `precision 11`"*), tức câu tổng kết đang phóng đại đặc điểm của một ca
   lên cả bốn.
2. **Chiều ngược lại là phản ví dụ, và nó nằm ngay trong nhóm.** `Q154938` (Bêđa) có P570 =
   `+0735-05-25`, **precision 11**, rank `preferred`, **2 tham chiếu** — và Bêđa chính là mục mà khối
   chấm `Cao`. `Q190896` (Abu Hanifa) có P569 = `+0699-09-05`, precision 11, rank `preferred`, 2 tham
   chiếu. Tức trong nhóm CE08, `precision 11` xuất hiện ở cả hồ sơ mạnh nhất lẫn hồ sơ rỗng nhất — đúng
   luận điểm của khối, nhưng không phải theo cách câu này phát biểu.
3. **Ba trong bốn người không thuộc "nhóm CE08".** Chỉ Shankara có mục (`CH05-CE08-11`). Jabir,
   Padmasambhava và Charles Martel là **ứng viên bị loại**, không phải mục của nhóm.

Đề xuất câu thay thế nguyên văn:
> Nói cách khác: bốn niên đại yếu nhất mà nhóm này phải xử — một mục (Shankara) và ba ứng viên bị loại — đều **không** yếu vì Wikidata ghi mơ hồ. Ba trong bốn được khai gọn tới năm, ca thứ tư (Charles Martel) khai tới tận ngày, mà chỗ dựa phía sau là một hồ sơ thư mục hoặc không có gì. Chiều ngược cũng đúng và phải nói ra: giá trị khai tới ngày ở `Q154938` (Bêđa, P570 = 735-05-25, rank `preferred`, có tham chiếu) lại thuộc về đúng mục được chấm `Cao`. Trường `precision` vì thế không nói gì về độ tin cậy theo **cả hai** chiều.

**NÊN** — tả sai loại nguồn đỡ cho P569 của Charles Martel.

Khối viết: *"`P569` chỉ có một tham chiếu dạng 'nêu trong' trỏ về **một mục cơ sở dữ liệu**"*. Tham chiếu
ấy là `P248 = Q24436712`, mà `Q24436712` được Wikidata mô tả là **"encyclopedic article"** — mục *Карл
Мартелл* trong **Từ điển bách khoa Brockhaus–Efron (ЭСБЕ)**, bộ từ điển Nga 1890–1907. Đó là một mục từ
điển bách khoa cuối thế kỷ 19, không phải một bản ghi cơ sở dữ liệu. Khác biệt này quan trọng vì nó làm
luận điểm của khối **mạnh hơn**: một ngày tháng chính xác tới 23-8-688 đang dựa vào một bộ bách khoa
cùng thời với chính cái khung 788–820 mà khối vừa hạ cấp ở ca Shankara.

Đề xuất câu thay thế nguyên văn:
> Charles Martel: ngày sinh và ngày mất đều khai tới `precision 11`, nhưng `P570` **không có tham chiếu nào** và `P569` chỉ có một tham chiếu dạng "nêu trong" trỏ về một mục từ điển bách khoa Nga cuối thế kỷ 19 (Brockhaus–Efron) — độ chính xác tới ngày không đi kèm chứng cứ tới ngày.

**CÂN NHẮC** — chuỗi sử học của ca Jabir chưa kiểm lại ở vòng này.

*"con số 721 truy ngược về giả thuyết Holmyard 1927 mà Delva 2017 đã tháo rời"* — `[KHÔNG KIỂM ĐƯỢC]`
ở vòng này. Kiểm được phần yếu hơn: `reports/ch05-ce08-gate.md:§5.1` ghi Delva 2017 đã được mở qua
Crossref (HTTP 200, 28.897 B), và cái **tham chiếu Trove** thì tôi xác minh trực tiếp. Mối nối
"Trove → Holmyard 1927" thì không nguồn nào trong repo chứng, và tôi không mở được nó.

---

## Khối 4 — Jabir ibn Hayyan: một ứng viên mà câu hỏi không phải "ông làm gì" mà "ông có ở thế kỷ 8 không"

**Đã kiểm được (không có phát hiện)**
- **Quy tắc 6 sạch.** `grep -n "^### "` trên `content/ch01.md`…`ch05.md` và `content/ch90.md`: **không có mục
  nào** cho Jabir ibn Hayyan ở bất kỳ chapter nào, kể cả phụ lục. `CH05-CE09-06 · Hunayn ibn Ishaq`
  (`Q503130`) là **người khác**, không phải Jabir (`Q167852`) — một bẫy đọc lướt, nhưng mục không mắc.
- **"Không được nhắc trong bất kỳ nguồn sử nào trước khoảng năm 900"** — khớp tài liệu tham khảo phổ thông
  (en.wikipedia "Jabir ibn Hayyan", HTTP 200, 53.037 B, tra trong vòng này).
- **"Ibn al-Nadīm trong *Fihrist* năm 987"** ✓, và **"ngay thời Ibn al-Nadīm đã có người khẳng định ông
  chưa từng tồn tại"** ✓ — cả hai khớp nguồn trên.
- **"k. 850–950"** cho khối *Jābirian* ✓ — nguồn trên ghi khung ấy là cách định niên "được chấp nhận rộng
  rãi trong học thuật hiện đại". Ba chỗ dựa khối nêu (thuật ngữ triết học giữa TK 9; bản dịch Hy Lạp cuối
  TK 9; triết học Shiʿa sơ kỳ chỉ thấy ở nguồn cuối TK 9 – đầu TK 10) cũng khớp.
- **"Fuat Sezgin 1971 bác Kraus"** ✓ — Sezgin, *Geschichte des arabischen Schrifttums* IV (Brill, 1971),
  được mô tả đúng là một phê phán luận đề định niên muộn của Kraus.
- **Hai URL hỏng — kiểm lại trực tiếp trong vòng này, cả hai đúng từng chi tiết:**
  - `doi.org/10.1163/22142371-12340030` → chuyển tới `brill.com/view/journals/jas/4/1/article-p35_2.xml`,
    **HTTP 202, 0 byte**. Đúng.
  - `doi.org/10.1017/S0041977X20000014` → chuyển tới `cambridge.org/core/product/identifier/…`,
    **HTTP 429, 1.478 byte**, nội dung là trang *"429 Too many automated requests from this network"*, và
    chuỗi **`Varnish`** có mặt trong thân trang. Đúng cả mã, cả kích thước, cả định danh Varnish.
- **"Thư mục hai bài được xác minh qua Crossref, không qua hai URL ấy"** ✓ — tôi làm lại đúng thế:
  `api.crossref.org` trả `10.1163/22142371-12340030` = **Delva, "The Abbasid Activist Ḥayyān al-ʿAṭṭār as
  the Father of Jābir b. Ḥayyān: An Influential Hypothesis Revisited", *Journal of Abbasid Studies* 4(1),
  2017**; và `10.1017/S0041977X20000014` = **Capezzone, "The solitude of the Orphan: Ǧābir b. Ḥayyān and
  the Shiite heterodox milieu of the third/ninth–fourth/tenth centuries", *BSOAS*, 2020**.
- **Phụ chú cho khối 3:** nhan đề Delva 2017 ở trên, cộng với chú thư mục của nguồn tham khảo
  ("bác giả thuyết của Holmyard 1927 rằng Jabir là con một dược sĩ proto-Shiʿa tên Ḥayyān al-ʿAṭṭār"),
  **củng cố** mệnh đề "Delva 2017 tháo rời giả thuyết Holmyard 1927" mà khối 3 dùng. Phần vẫn chưa kiểm
  được là mắt nối "tham chiếu Trove → Holmyard 1927".
- **"Quy tắc §3 tự nó đã loại"** — kiểm được về nội dung: `prompts/atlas-prompt.md`, mục *Quy tắc chọn
  nhân vật*, **điều 3** đúng là *"Xếp nhân vật vào thế kỷ của giai đoạn ảnh hưởng chính (floruit / tác
  phẩm hoặc hành động quan trọng nhất), không theo năm sinh."* Lập luận của khối áp đúng điều ấy.

**BẮT BUỘC** — câu sai, nguyên văn: *"các nhà viết tiểu sử Shiʿa **sớm** — al-Barqī, al-Kashshī,
al-Najāshī, al-Ṭūsī — soạn những bộ dày về **môn đồ của Jaʿfar al-Sadiq** mà không ai nhắc tới Jabir."*

Sai ở đâu: chữ **"sớm"** không đúng với hai trong bốn người, và nó đang gánh toàn bộ sức nặng của lập
luận. Tra lại trong vòng này:
- **al-Kashshī** — mất khoảng **951–952**.
- **al-Najāshī** (Aḥmad ibn ʿAlī) — khoảng **982–1058**.
- **al-Ṭūsī** (Muḥammad ibn al-Ḥasan, Shaykh al-Ṭāʾifa) — khoảng **995–1067**, tức AH 385–460.

Hai người cuối viết ở **thế kỷ 11**, tức **sau** *Fihrist* (987) mà chính khối vừa đặt làm mốc, có người
sau tới gần một thế kỷ. Đặt họ dưới nhãn "sớm" ngay sau câu "không được nhắc trước khoảng năm 900" sẽ làm
người đọc tưởng khối đang đưa ra **bốn** chứng im lặng trước năm 900 — trong khi chỉ một (al-Barqī, thế
kỷ 9) có thể nằm ở đó. Nghịch lý là lập luận **vẫn mạnh** khi nói đúng mốc, chỉ là mạnh theo một cách khác.

Đề xuất câu thay thế nguyên văn:
> Lập luận từ im lặng ở đây rất mạnh, nhưng phải nói đúng mốc của từng người: bốn bộ rijāl Shiʿa — al-Barqī, al-Kashshī (mất k. 951), al-Najāshī (k. 982–1058) và al-Ṭūsī (k. 995–1067) — đều soạn những bộ dày về **môn đồ của Jaʿfar al-Sadiq** mà không ai nhắc tới Jabir. Hai trong bốn người, al-Najāshī và al-Ṭūsī, viết ở thế kỷ 11, tức **sau** *Fihrist*; nên cái họ chứng không phải "chưa ai biết tới Jabir", mà là điều nặng không kém: ngay khi tên ông đã lưu hành rộng, truyền thống rijāl Shiʿa vẫn không xếp ông vào danh sách môn đồ của chính vị Imam mà truyền thuyết gắn ông vào.

Ghi rõ trong chính đề xuất: niên đại **al-Barqī** là `[KHÔNG KIỂM ĐƯỢC]` ở vòng này (không tìm được mục
tham khảo tiếng Anh riêng cho ông), nên câu thay thế **không** gán năm cho ông và chỉ nói "thế kỷ 9" ở
phần diễn giải, không nói trong câu được đề xuất.

**NÊN** — khối để ngỏ một câu hỏi mà **một khối sau trong cùng file đã đóng**, và không có con trỏ nào
nối hai chỗ.

Khối 4 kết: *"Nếu atlas muốn khối ấy có mặt, chỗ đúng là CE09 hoặc CE10 kèm nhãn `[Tranh cãi lịch sử]`,
và đó là quyết định của nhóm sau."* Khối *"Jabir ibn Hayyan: ghi chú CE08 để ngỏ, vòng này đóng lại"*
(`content/ch05.md:1192`) trả lời: **không**, và nói thẳng rằng dán `[Tranh cãi lịch sử]` ở đây sẽ **vi
phạm quy tắc 7** vì nhãn ấy dùng cho một con người mà sự tồn tại gây tranh cãi, không dùng cho một tập
văn bản ẩn danh. Hai khối cách nhau 39 dòng, và khối sau có nêu khối trước còn khối trước thì không nêu
khối sau. Đây đúng hình dạng đã sinh ra lỗi ở khối 6 (ca Harun al-Rashid, xem dưới): một chỉ dẫn CE08 đã
bị bác nhưng vẫn đứng nguyên văn.

Đề xuất câu thay thế nguyên văn:
> Nếu atlas muốn khối ấy có mặt, chỗ đúng là CE09 hoặc CE10 kèm nhãn `[Tranh cãi lịch sử]`, và đó là quyết định của nhóm sau. *(Đã quyết: vòng CE10 từ chối — xem khối "Jabir ibn Hayyan: ghi chú CE08 để ngỏ, vòng này đóng lại" bên dưới. Lý do không phải niên đại mà là sai đơn vị phân tích, và nhãn `[Tranh cãi lịch sử]` đặt ở đây sẽ vi phạm quy tắc 7.)*

**NÊN** — hai DOI được nêu mà không nói bài nào là bài nào, và bài quan trọng nhất của lập luận thì
không được gọi tên.

Khối viết *"Hai URL phải đánh dấu"* rồi liệt kê hai DOI trần. Một vòng sau mở ghi chú này sẽ không biết
DOI nào thuộc Delva 2017 và DOI nào thuộc bài còn lại — mà bài còn lại, **Capezzone 2020 (BSOAS)**, chính
là một công trình **sau 2010** đặt Jabir vào môi trường Shiʿa thế kỷ 9–10, tức là chứng cứ trực tiếp cho
câu *"hai vòng kiểm độc lập đều không tìm được công trình nào sau 2010 đứng về phía [Sezgin]"* ngay trên.
Gọi tên nó làm khối mạnh hơn mà không thêm rủi ro.

Đề xuất câu thay thế nguyên văn:
> Hai URL phải đánh dấu: `doi.org/10.1163/22142371-12340030` (Delva 2017, *Journal of Abbasid Studies*) trả **HTTP 202 với 0 byte**, và `doi.org/10.1017/S0041977X20000014` (Capezzone 2020, *BSOAS*, bài đặt Jabir vào môi trường Shiʿa thế kỷ 9–10) trả **HTTP 429** với trang chặn bot của Varnish — cùng loại bẫy mà các khối URL ở trên đã ghi. Thư mục hai bài được xác minh qua Crossref, không qua hai URL ấy.

**CÂN NHẮC** — ký hiệu `§3` không giải ra được chỗ nào trong repo, và nó va với một quy tắc khác.

Nội dung thì đúng (xem phần "Đã kiểm được"), nhưng trong repo **không có mục nào đánh số `§3`**:
`prompts/atlas-prompt.md` dùng tiêu đề chữ rồi danh sách số, `CONTRIBUTING.md` cũng vậy. Nguy hiểm là
`CONTRIBUTING.md` **có** một "quy tắc 3" khác hẳn (*"Không ghi số chương / quyển / tập nếu chưa mở mục
lục"*), nên "quy tắc §3" rất dễ bị đọc nhầm. Ghi thành `điều 3 của "Quy tắc chọn nhân vật" trong
prompts/atlas-prompt.md` sẽ dứt điểm — và nếu sửa thì nên sửa cả khối Charlemagne ngay trên, nơi dùng
cùng ký hiệu.

**CÂN NHẮC** — bẫy `429 / Varnish` là loại mới, chưa có trong danh sách URL chạy xuyên chapter.

Khối viết *"cùng loại bẫy mà ghi chú CE06 đã ghi"*. Kiểm: danh sách ở `content/ch05.md:1093` có
`202`, `405`, `406`, `200`-kèm-trang-chặn; danh sách ở `content/ch05.md:1107` có thêm `Brill trả 202 / 0
byte`, `403` qua Cloudflare, `404` với `<title>` giống trang thật. **Không danh sách nào có `429`.** Vậy
nửa đầu câu (202/0 byte) đúng là ca đã ghi, nửa sau là ca **mới**. Nên nối nó vào danh sách đang tích luỹ
thay vì để nằm riêng trong khối Jabir.

---

## Khối 5 — Padmasambhava bị loại bằng đúng cái thước vừa dùng cho Jabir

**Đã kiểm được (không có phát hiện)**
- **Quy tắc 6 sạch, và sạch ở cả ca khó.** Padmasambhava / Liên Hoa Sinh (`Q231582`) **không có mục** ở
  `ch01`–`ch05` lẫn `ch90`. Còn **Tì-ni-đa-lưu-chi** thì khối nhắc đúng cách mà `CONTRIBUTING.md` quy
  tắc 6 yêu cầu: gọi ông là *"người atlas giữ ở phụ lục"*, **không** gọi là ứng viên bị loại — khớp phán
  quyết ở khối *"Một câu hỏi thủ tục đã được quyết…"* của chính Ghi chú biên tập.
- **Mọi mốc trong khối khớp tài liệu tham khảo phổ thông** (en.wikipedia "Padmasambhava", HTTP 200,
  39.512 B, tra trong vòng này):
  - *Zangling-ma* là **tiểu sử đầu tiên** của Padmasambhava, tác giả **Nyangral Nyima Özer (1124–1192)** ✓
    — cả hai năm đời đúng từng chữ.
  - "khoảng **bốn thế kỷ** sau đời ông" ✓ (thế kỷ 8 → thế kỷ 12).
  - "khối *tám hoá thân*, hệ **terma** và **guru yoga** đều hình thành từ khoảng **thế kỷ 12**" ✓ — nguồn
    ghi các hagiography bắt đầu "từ khoảng thế kỷ 12", tám hoá thân thuộc truyền thống terma, và hình
    Padmasambhava được quán trong guru yoga.
  - "Các bản chép Đôn Hoàng có nhắc một đạo sư **kīlaya** cùng tên **nhưng không gắn ông với Trisong
    Detsen**" ✓ — khớp gần như từng chữ.
- **Khối khớp thân mục.** `CH05-CE08-10 · Trisong Detsen` viết đúng cùng hai dữ kiện ấy trong phần
  "Vì sao chọn". Không có mâu thuẫn khối–mục.
- "Tiểu sử phụ thuộc một bộ soạn sau **bảy thế kỷ**" cho Tì-ni-đa-lưu-chi ✓ nhất quán với khối Châu Đại
  Dương của chính chapter (*Thiền uyển tập anh* cách ông bảy thế kỷ).

**NÊN** — tiêu đề hứa "đúng cái thước vừa dùng cho Jabir", nhưng khối **không** áp bước quyết định của cái
thước ấy, và cũng không xét phương án khắc phục mà khối 4 đưa ra.

Khối 4 nói thẳng bước nào là bước loại: *"**Quy tắc §3 tự nó đã loại**: … **giai đoạn ảnh hưởng** của
khối văn bản mang tên ông là thế kỷ 9–10"*, rồi đưa phương án — chuyển sang CE09/CE10 kèm nhãn. Khối 5
dừng ở nửa trước của thước (nguồn muộn, bằng chứng sớm không đỡ mệnh đề cần) rồi chuyển sang một lập
luận **khác loại**: *"Suất Tây Tạng vì vậy là một, không phải hai"* — đó là lập luận **tranh suất trong
nhóm**, không phải lập luận giai đoạn ảnh hưởng. Trớ trêu là dữ kiện để hoàn tất bước §3 nằm sẵn trong
chính khối: nếu tám hoá thân, terma và guru yoga hình thành từ thế kỷ 12, thì giai đoạn ảnh hưởng của
nhân vật "Padmasambhava" là thế kỷ 12 chứ không phải thế kỷ 8 — y hệt hình dạng của ca Jabir.
`reports/ch05-ce08-gate.md` còn xếp ông vào đúng mục **§5.1 "Bị loại vì giai đoạn ảnh hưởng không thuộc
thế kỷ 8 (quy tắc §3)"**, tức hồ sơ cổng cũng nghĩ thước ấy đã được áp — nhưng câu văn trong ghi chú thì
chưa áp.

Đề xuất câu thay thế nguyên văn (thay câu cuối của khối):
> Áp nốt bước còn lại của cùng cái thước: nếu tám hoá thân, hệ terma và guru yoga đều hình thành từ khoảng thế kỷ 12, thì **giai đoạn ảnh hưởng** của nhân vật Padmasambhava là thế kỷ 12, không phải thế kỷ 8 — nên theo điều 3 của *Quy tắc chọn nhân vật*, CE08 là nhóm sai chứ không chỉ là suất chật. Suất Tây Tạng của nhóm này vì vậy là một, không phải hai; và nếu một chapter sau muốn chỉ mục hiện tượng Padmasambhava, chỗ đúng là thế kỷ 12, nơi khối văn bản về ông thật sự hình thành.

**NÊN** — "bằng chứng sớm nhất" bỏ sót một nguồn mà chính tài liệu tham khảo xếp ngang hàng.

Khối viết: *"tức **bằng chứng sớm nhất** không chống đỡ cho chính mệnh đề mà một mục CE08 sẽ cần."*
Nguồn tôi mở nêu — cạnh các bản Đôn Hoàng — **`Dba' bzhed` (*Testament of Ba*, k. thế kỷ 9–12)** là *"một
trong những nguồn biên niên sớm nhất về Padmasambhava như một nhân vật lịch sử"*, và chính nó chép việc
lập tu viện Samye dưới triều Trisong Detsen. Khối không nhắc nguồn này. Nó **không** cứu được ca
Padmasambhava — khung niên đại của chính `Dba' bzhed` kéo tới tận thế kỷ 12, tức không chắc chắn sớm hơn
lớp hagiography — nhưng một vòng sau mở cùng trang tham khảo sẽ thấy ngay chỗ hổng và mất tin vào cả khối.
Nêu nó ra rồi loại nó bằng chính niên đại của nó thì chặt hơn là im lặng.

Đề xuất câu thay thế nguyên văn:
> Các bản chép Đôn Hoàng có nhắc một đạo sư kīlaya cùng tên **nhưng không gắn ông với Trisong Detsen**; còn nguồn biên niên sớm thứ hai hay được viện tới, *Testament of Ba* (`Dba' bzhed`), thì chính nó được định niên trong khoảng thế kỷ 9–12, nên không đứng chắc hơn lớp hagiography mà nó phải đỡ. Tức bằng chứng sớm nhất không chống đỡ cho chính mệnh đề mà một mục CE08 sẽ cần.

**CÂN NHẮC** — lập luận "thanh chắn atlas chính cao hơn phụ lục" đang tựa vào một câu hỏi còn treo.

Khối dùng Tì-ni-đa-lưu-chi làm mốc so sánh và kết luận *"thanh chắn của atlas chính phải **cao hơn** phụ
lục"*. Nguyên tắc ấy có chỗ dựa thành văn (`README.md`: phụ lục dùng hệ quy chiếu Việt Nam/Đông Nam Á,
không phải nhân loại) nên không phải mệnh đề bịa. Nhưng khối *"Một câu hỏi thủ tục đã được quyết…"* của
cùng Ghi chú biên tập để ngỏ việc **chuyển Tì-ni-đa-lưu-chi từ phụ lục lên atlas chính cho P4 quyết**.
Nếu P4 chuyển, mốc so sánh của khối 5 biến mất. Nên ghi một nửa câu phòng hờ, hoặc đổi mốc so sánh sang
một tiêu chí không phụ thuộc vị trí của một mục cụ thể.

---

## Khối 6 — Nhóm chật nhất Chapter 5: bốn người bị loại vì trần, không vì chất lượng

**Đã kiểm được (không có phát hiện)**
- **"Trần 12 người là trần, không phải định mức"** ✓ — `prompts/atlas-prompt.md`, *Quy tắc chọn nhân vật*
  điều 2: *"Tối đa 12 nhân vật mỗi nhóm. KHÔNG cố cho đủ 12: nếu thiếu ứng viên xứng đáng, chọn ít hơn và
  ghi lý do."* `atlaslib/lint.py` cũng chỉ báo ERROR khi **vượt** 12 (`len(g["persons"]) >
  C.PROJECT["max_per_group"]`), không có phép kiểm nào đòi đủ 12.
- **Con số "mười lăm" đúng vào lúc viết** ✓ — `reports/ch05-ce08-gate.md §5` liệt kê đúng 15 người:
  §5.1 (3) Jabir · Padmasambhava · Harun al-Rashid; §5.2 (4) Alcuin · Malik ibn Anas · Ibn Ishaq · Lý Bạch;
  §5.3 (8) An Lộc Sơn · Shōmu · Charles Martel · Divashtich · Sanjaya · Panangkaran · Kyriakos ·
  Jayavarman II.
- **Ba trong bốn người được nêu đích danh vẫn sạch quy tắc 6** — đối chiếu bằng Q-ID trên toàn `content/`:
  Harun `Q131002`, Malik `Q312299`, Ibn Ishaq `Q334847`, An Lộc Sơn `Q360559` — **không ai có mục**.
  Đặc biệt `CH05-CE09-06 · Hunayn ibn Ishaq` (`Q503130`) là người khác, không va với Ibn Ishaq.
- **"Tikal cuối Cổ điển"** ✓ đúng, và đúng hơn hồ sơ cổng: `reports/ch05-ce08-gate.md:715` viết "Tikal ở
  đỉnh **Hậu** Cổ điển" (Postclassic), còn khối viết "cuối Cổ điển" (Late Classic), khớp thân mục
  `CH05-CE08-12` ("thế giới Maya thời Cổ điển"). Khối đã sửa lỗi của hồ sơ cổng; không đụng vào.
- Khối **không nêu tỉ lệ phần trăm nào**, nên không có số liệu rữa theo kiểu ô vùng.

**BẮT BUỘC** — câu sai, nguyên văn: *"Mười lăm ứng viên bị loại, trong đó bốn người sẽ chắc chắn vào atlas
nếu trần là 16"*.

Sai ở đâu: **một trong mười lăm người ấy nay đã có mục riêng trong atlas**, nên con số 15 đang vi phạm
quy tắc 6 theo đúng kiểu phát sinh theo thời gian mà vòng CE10 vừa gặp với Khúc Thừa Dụ.

Bằng chứng: `reports/ch05-ce08-gate.md §5.3` xếp **Jayavarman II** vào danh sách 15 (kèm ghi chú
*"ông là ứng viên Đông Nam Á của nhóm ấy"* gửi sang CE09). Đối chiếu Q-ID trên toàn `content/`:
`Q379239` nay nằm ở **`CH05-CE09-01 · Jayavarman II`**. Mười bốn người còn lại vẫn không có mục ở đâu —
tôi kiểm từng Q-ID một: `Q167852`, `Q231582`, `Q131002`, `Q154332`, `Q312299`, `Q334847`, `Q7071`,
`Q360559`, `Q349263`, `Q3301`, `Q753663`, `Q3107477`, `Q7130030`, `Q1148493` đều trả **none**. Vậy con số
đúng hôm nay là **mười bốn**, và chỗ hụt một người phải được nói rõ chứ không được lặng lẽ trừ đi.

**BẮT BUỘC** — câu sai, nguyên văn: *"**Harun al-Rashid** (trị vì 786–809; danh tiếng ông lại đến từ hai
thứ không thuộc về ông — *Nghìn lẻ một đêm* lấy ông làm nhân vật chứ không phải tư liệu về ông, và Bayt
al-Ḥikma với tư cách trung tâm dịch thuật có tổ chức gắn với al-Maʾmun thế kỷ 9; **vòng CE09 phải nhặt
ông lại**)"*.

Sai ở hai chỗ, cả hai đều bị bác ngay trong cùng file:

1. **"vòng CE09 phải nhặt ông lại"** mô tả một trạng thái repo **không còn tồn tại**. Khối *"Tiền đề bị
   bác bỏ: Harun al-Rashid và cái gọi là 'Nhà Trí tuệ'"* (`content/ch05.md:1186`) ghi: *"Ghi chú CE08 dặn
   vòng CE09 nhặt lại Harun al-Rashid. Vòng này đã đánh giá lại độc lập và **từ chối**, và **lý do không
   phải trần 12**."* Thân mục `CH05-CE09-06` cũng viết: *"Hai ứng viên bảo trợ, Harun al-Rashid và
   al-Maʾmun, **bị loại vì lý do ấy**."* Tức mệnh lệnh của khối 6 đã được thi hành và đã bị bác, mà khối 6
   không đổi một chữ.
2. **"Bayt al-Ḥikma với tư cách trung tâm dịch thuật có tổ chức gắn với al-Maʾmun thế kỷ 9"** khẳng định
   đúng cái mệnh đề mà chapter này ở chỗ khác nói là **đang bị tháo dỡ** — khối 6 chỉ chuyển nó từ Harun
   sang al-Maʾmun. `content/ch05.md:1186` dẫn İhsanoğlu (Routledge, 2023) rằng Bayt al-Ḥikma *"như một
   học viện có khoa, có ban, có chương trình dịch thuật"* là sản phẩm dựng lên bởi Đông phương học thế kỷ
   19 – đầu 20, và nói thẳng: *"Nếu mệnh đề ấy đổ thì nó không cứu được Harun **mà cũng không cứu được
   al-Maʾmun**."* Thân mục `CH05-CE09-06` lặp lại y vậy.

Đề xuất câu thay thế nguyên văn (thay cả cụm Harun trong danh sách):
> **Harun al-Rashid** (trị vì 786–809; danh tiếng ông đến từ hai thứ không thuộc về ông — *Nghìn lẻ một đêm* lấy ông làm nhân vật chứ không phải tư liệu về ông, còn Bayt al-Ḥikma như một trung tâm dịch thuật có tổ chức là mệnh đề đang bị học thuật tháo dỡ, nên nó không đỡ được ông mà cũng không đỡ được al-Maʾmun; ghi chú này từng dặn vòng CE09 nhặt ông lại, **vòng CE09 đã đánh giá lại và từ chối vì lý do nội dung** — xem khối "Tiền đề bị bác bỏ: Harun al-Rashid và cái gọi là 'Nhà Trí tuệ'")

**BẮT BUỘC** — câu sai, nguyên văn (tiêu đề khối): *"Nhóm chật nhất Chapter 5: bốn người bị loại **vì
trần, không vì chất lượng**"*.

Sai ở đâu: hai trong bốn người ấy bị loại vì **lý do chất lượng**, và cả hai phản ví dụ nằm trong chính
Ghi chú biên tập này — một ở ngay khối kế tiếp.

- **An Lộc Sơn**: khối 7, liền ngay dưới, viết *"theo tiêu chí (c) tính nguyên bản và (d) counterfactual,
  An Lộc Sơn là **triệu chứng** … chứ không phải người tạo ra nó"*. Đó là một phán quyết về **con người**,
  không phải về số suất. `reports/ch05-ce08-gate.md` cũng xếp ông ở **§5.3 "Bị loại vì bốn tiêu chí"**,
  không ở mục nào nói về trần.
- **Harun al-Rashid**: xem lỗi BẮT BUỘC ngay trên — khối ở dòng 1186 nói **"lý do không phải trần 12"**.

Chỉ **Malik ibn Anas** và **Ibn Ishaq** thật sự là nạn nhân của số suất: hồ sơ cổng xếp hai ông ở
**§5.2 "Bị loại vì có người cùng vai mạnh hơn trong nhóm"** và giải thích bằng hạn ngạch bốn suất Trung
Đông, không bằng chất lượng hồ sơ.

Đề xuất tiêu đề và câu thay thế nguyên văn:
> **Nhóm chật nhất Chapter 5: hai người bị loại vì trần, và hai ca hay bị xếp nhầm vào đó**
>
> … Mười lăm ứng viên bị loại khi ấy, nay còn **mười bốn** đúng nghĩa: Jayavarman II từ đó đã có mục riêng ở `CH05-CE09-01`, nên quy tắc 6 cấm còn gọi ông là ứng viên bị loại. Trong mười bốn người, **hai người** bị loại thuần tuý vì hết suất chứ không vì chất lượng: **Malik ibn Anas** (*al-Muwaṭṭaʾ*, bộ luật thành văn sớm nhất còn lại của Hồi giáo) và **Ibn Ishaq** (*Sīra*, tiểu sử Muhammad sớm nhất còn lại — và chỉ còn qua bản hiệu đính của Ibn Hishām — nguồn mà mọi tiểu sử sau phải đi qua); cả hai bị gạt vì bốn suất Trung Đông đã đầy. Hai ca còn lại phải tách ra vì lý do loại của chúng là lý do nội dung: **Harun al-Rashid** (xem cụm sửa ở trên) và **An Lộc Sơn** (xem khối ngay dưới). Nới trần lên 16 vì vậy chỉ cứu được hai người, không phải bốn.

**CÂN NHẮC** — câu cuối khối vẫn đứng, và nên giữ nguyên.

*"Trần không được nới cho riêng một nhóm: chính các bảng phân bố vùng và lĩnh vực là thứ atlas dùng để tự
phê bình, và chúng chỉ đọc được khi các nhóm so sánh được với nhau."* Lập luận này độc lập với ba lỗi
trên và không bị chúng kéo theo. Khi sửa, đừng sửa lây câu này.

---

## Khối 7 — An Lộc Sơn: bốn tiêu chí đo con người, không đo biến cố

**Đã kiểm được (không có phát hiện)**
- **Quy tắc 6 sạch.** `Q360559` (An Lộc Sơn) **không có mục** ở bất kỳ chapter nào, kể cả `ch90` — kiểm
  bằng đối chiếu Q-ID trên toàn `content/`.
- **Nhãn tiêu chí đúng.** `(c) tính nguyên bản` và `(d) counterfactual` khớp đúng danh sách ở
  `prompts/atlas-prompt.md` điều 4 và `README.md` ((a) phạm vi · (b) độ bền · (c) tính nguyên bản ·
  (d) counterfactual). Không có chuyện gọi nhầm chữ cái — một lỗi dễ mắc mà khối này không mắc.
- **"Loạn An Lộc Sơn (755–763)"** ✓ khung quy ước chuẩn, và nhất quán với `CH05-CE08-09` ("loạn An Lộc Sơn
  từ năm 755") cùng dòng `Bối cảnh` của nhóm.
- **Mốc 763** ✓ — `CH05-CE08-10` ghi *"năm 763 quân Tây Tạng vào Trường An và lập một hoàng đế của riêng
  họ"*, khớp năm trong khối.
- **Khối không nêu tỉ lệ nào**, không có số liệu rữa.
- **Lập luận của khối đứng vững và không bị lỗi của khối 6 kéo theo.** Ngược lại: khối 7 chính là phản ví
  dụ làm lộ lỗi ở khối 6 (xem BẮT BUỘC thứ ba của khối 6). Khi sửa khối 6, **không** được sửa khối 7 theo
  hướng ngược lại — hồ sơ cổng (`reports/ch05-ce08-gate.md §5.3`) xếp An Lộc Sơn đúng vào mục "bị loại vì
  bốn tiêu chí", nên khối 7 mới là bản đúng.

**NÊN** — câu *"Biến cố vẫn vào atlas qua hai góc"* hứa nhiều hơn những gì hai mục thật sự chở.

Góc thứ nhất có thật: `CH05-CE08-09 · Đỗ Phủ` gọi đích danh *"loạn An Lộc Sơn từ năm 755"* trong phần
"Tư tưởng", nên người đọc mục ấy gặp được biến cố. Góc thứ hai thì **không**: `grep -n "An Lộc Sơn"
content/ch05.md` trả về đúng bốn dòng — `413` (Bối cảnh nhóm), `560` (Đỗ Phủ), `1160` (khối 6) và `1163`
(chính khối 7). **Mục Trisong Detsen `CH05-CE08-10` không nhắc An Lộc Sơn một chữ nào.** Mục ấy chỉ chép
*"năm 763 quân Tây Tạng vào Trường An"* như một sự kiện trần, không nói vì sao Trường An để lọt. Tức mệnh
đề nhân quả mà khối dựa vào — "chính nó mở đường cho quân Tây Tạng vào Trường An" — chỉ tồn tại **trong
ghi chú biên tập**, không tồn tại trong atlas. Người đọc atlas (không đọc ghi chú) sẽ không gặp góc thứ hai.

Có hai cách sửa, và nên chọn cách thứ nhất vì nó làm atlas tốt lên chứ không chỉ làm câu văn đúng lên:

Đề xuất (a) — thêm vào `CH05-CE08-10`, phần "Tư tưởng / đóng góp chính", thay cụm mở đầu:
> Dưới triều ông, Thổ Phồn đạt tầm xa nhất: khi nhà Đường còn chưa gượng lại sau loạn An Lộc Sơn, năm 763 quân Tây Tạng vào Trường An và lập một hoàng đế của riêng họ; năm 783 buộc nhà Đường ký lại đường biên.

Đề xuất (b) — nếu không muốn đụng thân mục, sửa chính câu trong khối 7:
> Biến cố vẫn vào atlas qua mục Đỗ Phủ (người chứng), và gián tiếp qua mục Trisong Detsen: mục ấy chép việc quân Tây Tạng vào Trường An năm 763 mà không nêu nguyên nhân, nên mối nối với loạn An Lộc Sơn hiện chỉ nằm ở ghi chú này.

**CÂN NHẮC** — hai mệnh đề "lớn nhất" trong cùng chapter không cùng phạm vi.

Khối 7 viết *"có lẽ là biến cố đơn lẻ có hệ quả lớn nhất thế kỷ 8 ở **lục địa Á–Âu**"*, còn thân mục
`CH05-CE08-09` viết *"biến cố lớn nhất thế kỷ 8 ở **Đông Á**"*. Hai câu không mâu thuẫn (một bao trùm
cái kia) và khối có hedge "có lẽ", nên không phải lỗi. Chỉ lưu ý: mệnh đề rộng hơn nằm ở chỗ **không có
nguồn**, còn mệnh đề hẹp hơn nằm trong mục **có nguồn**. Nếu một vòng sau muốn thống nhất, hãy kéo mục
lên theo khối chứ đừng kéo khối xuống — hoặc giữ nguyên cả hai, cách hiện tại cũng chấp nhận được.

---

## Khối 8 — Divashtich: bằng chứng hạng nhất vẫn không phải ảnh hưởng hạng nhất

**Đã kiểm được (không có phát hiện)**
- **Quy tắc 6 sạch.** `Q753663` (Divashtich) **không có mục** ở bất kỳ chapter nào, kể cả `ch90`.
- **"Thua trận năm 722"** ✓ — tài liệu tham khảo phổ thông (en.wikipedia "Divashtich", HTTP 200) chép
  trận gần Zarafshan năm **722** do al-Harashī thắng, rồi ông chạy lên pháo đài Kalʼai Mug.
- **"Bị đóng đinh trên một *naus*, nhà quàn hài cốt Hoả giáo"** ✓ — nguồn trên ghi al-Harashī *"had
  Divashtich crucified on a Zoroastrian burial building"*. Cả hành vi, cả loại công trình đều đúng; chú
  giải "nhà quàn hài cốt Hoả giáo" cho chữ *naus* là chính xác.
- **"Triều đại ông chấm dứt"** ✓ — nguồn trên ghi ông là **người cuối cùng** trong năm người của dòng họ
  mang tước *sur*.
- **Văn khố núi Mugh là của Divashtich, không phải của Abu Muslim** ✓ — nhất quán với khối *"Hình dạng
  của thế kỷ…"* (`content/ch05.md:1184`), vốn nói đúng điều ấy, và với `CH05-CE08-01`.
- **Câu kết của khối** (*"nếu lẫn 'được ghi chép nhiều' với 'có ảnh hưởng lớn'…"*) khớp nguyên văn
  khuyến nghị ở `reports/ch05-ce08-gate.md §5.3`. Đây là câu khối được giao phải giữ, và nó được giữ đúng.
- **Khối không nêu tỉ lệ nào.**

**NÊN** — thân mục `CH05-CE08-01` nói một mệnh đề **rộng hơn** khối, và chính cái rộng hơn ấy là chỗ hở.

Khối 8 viết cẩn thận: *"khối tư liệu Sogdian đầy đủ nhất từng tìm được **trong chính Sogdiana**"*. Thân
mục `CH05-CE08-01` bỏ mất mệnh đề giới hạn: *"người để lại văn khố núi Mugh, **khối văn kiện Sogdian đầy
đủ nhất từng tìm được**"* — không có "trong chính Sogdiana". Ở dạng trần ấy nó là một mệnh đề "nhất" dễ
có phản ví dụ, vì khối tư liệu tiếng Sogdian lớn nhất được biết đến lại nằm **ngoài** Sogdiana (các thư
tịch Sogdian ở Đôn Hoàng và Turfan). Khối đúng, mục sai; sửa mục theo khối.

Đề xuất câu thay thế nguyên văn (cho **thân mục** `CH05-CE08-01`, phần "Vì sao chọn"):
> Ứng viên bị loại là Divashtich xứ Panjikant, người để lại văn khố núi Mugh, khối văn kiện Sogdian đầy đủ nhất từng tìm được trong chính Sogdiana.

**NÊN** — "khoảng 80 văn kiện **Sogdian**" gán cho một văn khố mà chính nó có bốn thứ tiếng.

Nguồn tôi mở (en.wikipedia "Kalʼai Mug", HTTP 200) ghi đoàn khảo sát của Freiman năm 1933 tìm được
*"documents in Sogdian, Arabic, Turkic and Chinese"*. Nếu tổng văn khố vào khoảng 80 đơn vị thì phần
tiếng Sogdian phải **ít hơn** 80; nếu phần Sogdian đúng là khoảng 80 thì tổng phải lớn hơn. Khối hiện
viết như thể cả hai bằng nhau. Đây không phải lỗi lớn, nhưng nó nằm đúng trong câu mà khối dùng để
chứng "ông đứng cao hơn gần như mọi người trong nhóm về bằng chứng", nên nên nói chặt.

Đề xuất câu thay thế nguyên văn:
> Văn khố núi Mugh — khoảng 80 văn kiện từ kho riêng của Ḏēwaštīč, phần lớn bằng tiếng Sogdian, kèm một số bản tiếng Ả Rập, Turkic và Hán — là khối tư liệu Sogdian đầy đủ nhất từng tìm được trong chính Sogdiana, gồm sổ sách buôn bán, thư từ, khế ước, trao đổi ngoại giao và báo cáo do thám.

**CÂN NHẮC** — hai con số/mốc của khối không kiểm được ở vòng này.

1. **"UNESCO ghi danh *Memory of the World* năm 2025"** — `[KHÔNG KIỂM ĐƯỢC]`. Tôi đã thử ba đường và
   không đường nào xác nhận: tìm kiếm trong UNESCO MoW Register (`unesco.org/en/memory-world/register`,
   HTTP 200, 251.365 B — trang dựng động, chuỗi "Mugh" chỉ xuất hiện trong tham số truy vấn, không trong
   kết quả), trang *country overview* cho Tajikistan (HTTP 200, 81.113 B — cũng dựng động), và tìm kiếm
   toàn site (`unesco.org/en/search?text=Mugh`, HTTP 200, 452.594 B — **không** có chuỗi "Mugh" trong
   phần văn bản đã render). Hai mục tham khảo phổ thông về Divashtich và Kalʼai Mug cũng **không** nhắc
   tới việc ghi danh. Mốc này do đó phải được xác minh lại từ chính danh mục MoW trước khi giữ, hoặc
   gắn nhãn chưa kiểm.
2. **"khoảng 80 văn kiện"** — `[KHÔNG KIỂM ĐƯỢC]` về con số. Tôi không mở được nguồn nào cho một con số
   cụ thể. Chữ "khoảng" đã là cách viết phòng hờ đúng, nên nếu không xác minh được thì **giữ nguyên chữ
   "khoảng"**, đừng thay bằng một con số tròn trông chắc chắn hơn.

---

## Phụ chú cho Khối 1 — một mệnh đề trong câu thay thế của chính tôi phải được đánh dấu

Câu thay thế tôi đề xuất ở khối 1 giữ lại vế *"Śaṅkara trích nguyên văn Pháp Xứng, nên không sớm hơn giữa
thế kỷ 7"*. Phải nói rõ: chữ **"nguyên văn"** là `[KHÔNG KIỂM ĐƯỢC]` ở vòng này. Tài liệu tham khảo tôi mở
được chỉ nói mốc chặn dưới k. 650 đến từ việc tác phẩm của ông *"mang dấu vết tranh luận với các tác giả
Phật giáo và Mīmāṃsā thế kỷ 5–7"* — tức một mệnh đề yếu hơn "trích nguyên văn". Mệnh đề này có sẵn trong
bản gốc và tôi không đề nghị bỏ nó, nhưng nếu vòng sau không xác minh được bằng một công trình chuyên
ngành thì nên hạ xuống *"Śaṅkara tranh luận với Pháp Xứng"* — đủ để chặn đầu dưới mà không vượt quá
chứng cứ. Thân mục `CH05-CE08-11` hiện cũng viết *"ông trích Pháp Xứng"*, nên nếu sửa thì sửa cả hai chỗ.

---

## Tổng kết

### Bảng đếm theo khối

| # | Khối | BẮT BUỘC | NÊN | CÂN NHẮC |
|---|---|---|---|---|
| 1 | Khung 788–820 của Shankara không phải truyền thống của các maṭha | 1 | 1 | 2 |
| 2 | Hai chữ "Nhất Hạnh", và một va chạm cách nhau 1.200 năm | 0 | 0 | 1 |
| 3 | Wikidata khai độ chính xác, nó không khai độ tin cậy | 1 | 1 | 1 |
| 4 | Jabir ibn Hayyan: … "ông có ở thế kỷ 8 không" | 1 | 2 | 2 |
| 5 | Padmasambhava bị loại bằng đúng cái thước vừa dùng cho Jabir | 0 | 2 | 1 |
| 6 | Nhóm chật nhất Chapter 5: bốn người bị loại vì trần | 3 | 0 | 1 |
| 7 | An Lộc Sơn: bốn tiêu chí đo con người, không đo biến cố | 0 | 1 | 1 |
| 8 | Divashtich: bằng chứng hạng nhất vẫn không phải ảnh hưởng hạng nhất | 0 | 2 | 1 |
| | **Tổng** | **6** | **9** | **10** |

Khối sạch nhất: **khối 2** (không có BẮT BUỘC lẫn NÊN; mọi mệnh đề Wikidata đều tra lại và đúng từng chữ).
Khối nặng nhất: **khối 6** (ba lỗi BẮT BUỘC, cả ba đều thấy được mà không cần ra khỏi `content/ch05.md`).

### Sáu lỗi BẮT BUỘC, gom theo loại

**A. Khối mô tả một trạng thái repo không còn tồn tại — 3 lỗi.** Đây là hình dạng áp đảo của vòng này,
giống hệt kết luận của `reports/ch05-ce10-notes-review.md`. Không lỗi nào cần tra cứu bên ngoài để thấy.
- **Khối 1**: *"Vācaspati Miśra sớ cho ông ở nửa đầu thế kỷ 9"* — vòng CE10 đã bác mỏ neo này và đã gỡ
  câu khỏi `CH05-CE08-11`; khối còn giữ nguyên văn câu cũ.
- **Khối 6**: *"vòng CE09 phải nhặt ông lại"* (Harun al-Rashid) — vòng CE09 đã từ chối, và khối ở
  `content/ch05.md:1186` ghi lại việc từ chối ấy cùng lý do.
- **Khối 6**: *"Mười lăm ứng viên bị loại"* — một trong mười lăm (Jayavarman II) nay có mục ở
  `CH05-CE09-01`, nên con số vi phạm quy tắc 6. Đúng ca mà vòng CE10 gặp với Khúc Thừa Dụ.

**B. Mệnh đề quá rộng mà phản ví dụ nằm trong chính dữ kiện của khối — 2 lỗi.**
- **Khối 3**: *"bốn niên đại được khai ở độ chính xác cao nhất"* — ba trong bốn là `precision 9` (năm
  trần), và chính khối đã liệt kê như thế ba dòng trên. Phản ví dụ chiều ngược: `Q154938` (Bêđa) khai tới
  ngày với tham chiếu, mà Bêđa là mục được chấm `Cao`.
- **Khối 6**: tiêu đề *"bốn người bị loại vì trần, không vì chất lượng"* — An Lộc Sơn bị loại theo tiêu
  chí (c)/(d) (khối 7 nói thế, hồ sơ cổng xếp ở §5.3), Harun bị từ chối vì lý do nội dung
  (`content/ch05.md:1186` nói thẳng *"lý do không phải trần 12"*). Chỉ hai trong bốn là nạn nhân của trần.

**C. Mệnh đề sử học sai mốc — 1 lỗi.**
- **Khối 4**: gọi al-Najāshī (k. 982–1058) và al-Ṭūsī (k. 995–1067) là *"các nhà viết tiểu sử Shiʿa
  **sớm**"* ngay sau câu lấy năm 900 và *Fihrist* 987 làm mốc. Hai người này viết ở **thế kỷ 11**.

**Ghi riêng — một lỗi loại "mô tả sai chính repo" mà vòng này KHÔNG tìm thấy.** Hai vòng trước đều bắt
được một khối tả sai phép kiểm của lint. Tôi đọc lại `atlaslib/lint.py` cho mọi mệnh đề kỹ thuật trong
tám khối: khối 1 (mức `Thấp` làm lint bỏ qua đối chiếu niên đại), khối 2 (tên mục không gây cảnh báo
nhãn), khối 6 (trần 12 là trần, không phải định mức) — **cả ba đều đúng**. `reports/lint-ch05.txt` xác
nhận ERROR 0 · WARN 0.

### Mọi chỗ `[KHÔNG KIỂM ĐƯỢC]`

1. **Khối 1** — chuỗi truyền của khung 788–820: Tiele lấy từ *Āryavidyā-sudhākara* của Yajñeśvara Śāstrī,
   vốn dẫn lại *Śaṅkara-mandāra-saurabha* của Bhaṭṭa Nīlakaṇṭha. Tài liệu tham khảo tôi mở được chỉ nói
   khung ấy do các học giả cuối TK 19 – đầu TK 20 đề xuất "theo sau Tiele", **không** có hai nhan đề lẫn
   hai tên người. Đây là mắt xích giữ cho vế "không phải chế ra nó" đứng được.
2. **Khối 1 (và câu thay thế của chính tôi)** — chữ *"trích **nguyên văn** Pháp Xứng"*. Nguồn mở được chỉ
   nói "mang dấu vết tranh luận với các tác giả Phật giáo và Mīmāṃsā thế kỷ 5–7". Xem Phụ chú cho Khối 1.
3. **Khối 3** — mắt nối *"tham chiếu Trove → giả thuyết Holmyard 1927"*. Nửa sau của chuỗi thì **đã kiểm
   được** ở khối 4 (Crossref + chú thư mục xác nhận Delva 2017 bác giả thuyết Holmyard 1927); mắt nối
   Trove thì không nguồn nào chứng.
4. **Khối 3** — *"hai khung chết [của Sibawayh] loại trừ nhau, lệch mười chín năm và khác cả nơi chết"*.
   Kiểm được **trong repo** (`reports/ch05-ce08-review.md:391` xác nhận ✓ ở vòng trước); tôi không mở lại
   nguồn cổ điển nào ở vòng này.
5. **Khối 4** — niên đại **al-Barqī**. Không tìm được mục tham khảo tiếng Anh riêng cho ông; câu thay thế
   tôi đề xuất vì vậy cố ý **không** gán năm cho ông. Ba người còn lại đã tra và ghi năm trong báo cáo.
6. **Khối 4** — *"hai vòng kiểm độc lập đều không tìm được công trình nào sau 2010 đứng về phía
   [Sezgin]"*. Tôi xác nhận được chiều thuận (Capezzone 2020, *BSOAS*, đặt khối Jābirian vào môi trường
   Shiʿa thế kỷ 9–10) nhưng **không** rà vét được văn liệu sau 2010 để chứng mệnh đề phủ định.
7. **Khối 8** — *"UNESCO ghi danh Memory of the World năm 2025"*. Ba đường tra đều không xác nhận (chi
   tiết mã HTTP và kích thước ghi trong khối 8).
8. **Khối 8** — con số *"khoảng 80 văn kiện"*. Không mở được nguồn cho một con số cụ thể; khuyến nghị
   **giữ nguyên chữ "khoảng"**.

### Ba việc nên làm trước khi vòng CE08 phần 2 bắt đầu

1. **Đọc chéo tám khối này với bốn khối CE09/CE10 nói về cùng người.** Ba trong sáu lỗi BẮT BUỘC là ghi
   chú CE08 mô tả một trạng thái mà một khối sau trong **cùng file** đã lật. Cặp nguy hiểm nhất là
   Harun al-Rashid (khối 6 ↔ `content/ch05.md:1186`), rồi Jabir (khối 4 ↔ `:1192`), rồi Śaṅkara
   (khối 1 ↔ `:1251`). Quy ước nên đặt: **khối cũ phải mang con trỏ tới khối đã lật nó**, không chỉ khối
   mới nhắc khối cũ — hiện quan hệ đang một chiều ở cả ba cặp.
2. **Mở rộng quy ước số liệu của vòng CE10 từ "tỉ lệ phần trăm" sang "mọi số đếm phụ thuộc trạng thái
   atlas".** `content/ch05.md:1270` đặt quy ước *"con số trong ghi chú biên tập phải tự khai nó đo ở thời
   điểm nào, hoặc không nêu số"* — nhưng chỉ nói về **tỉ lệ**. Lỗi của vòng này là một **số đếm**
   ("mười lăm ứng viên bị loại"), và nó rữa theo đúng cơ chế ấy. Không khối nào trong tám khối này nêu
   tỉ lệ phần trăm, nên quy ước hiện hành sẽ không bắt được lỗi duy nhất thuộc loại ấy.
3. **Gắn mốc thời gian vào `reports/stats.txt`.** File này là nguồn của mọi con số trong ghi chú biên
   tập, nhưng bản thân nó **không tự khai thời điểm đo**: tôi `grep` cả file, **không có chuỗi năm nào**
   (`grep -c "202[0-9]" reports/stats.txt` → `0`). Dòng đầu chỉ ghi "245 nhân vật (atlas chính) + 40 ở
   phụ lục". Hệ quả: một vòng sau chép số từ đây không có cách nào biết số ấy đo khi nào, nên quy ước ở
   điểm 2 không thể thi hành được từ nguồn. Thêm một dòng ngày tháng (và lý tưởng là số chapter/nhóm đã
   có) vào đầu `stats.txt` là việc rẻ nhất trong ba việc này.
