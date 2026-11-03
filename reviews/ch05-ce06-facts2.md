# Kiểm chứng sự kiện độc lập — Chapter 5, nhóm CE06 (vòng 2)

Phạm vi: `CH05-CE06-09` Kaleb · `CH05-CE06-10` Bumin Qaghan · `CH05-CE06-11` Bhavavarman I · `CH05-CE06-12` Boethius, cộng các khối nói về nhóm CE06 trong `## Ghi chú biên tập` của `content/ch05.md`.

Người kiểm: agent độc lập, không viết chapter này. Ngày: 2026-10-31.
Quy ước: mọi URL dẫn trong báo cáo này đều **đã tự mở kiểm**, và ghi kèm mã HTTP + số byte + dấu hiệu nội dung chữ thật. Chỗ không kiểm được ghi `[KHÔNG KIỂM ĐƯỢC]` kèm lý do.

Trạng thái: **đang viết tăng dần** — mục nào đã có đề mục `### Kết luận` là đã kiểm xong.

---

## URL đã mở kiểm (bảng chung)

| URL | HTTP | Kích thước tải | Chữ thật sau khi bóc thẻ | Đánh giá |
|---|---|---|---|---|
| `https://plato.stanford.edu/entries/boethius/` | 200 | 90.315 B | **70.352 ký tự** | Thật, đọc được. Tác giả `DC.creator = Marenbon, John` ✓. Bản sửa lớn gần nhất: Wed Oct 14, 2026. |
| `https://plato.stanford.edu/entries/medieval-literary/` | 200 | 144.744 B | **117.959 ký tự** | Thật, đọc được. Tác giả `DC.creator = Sweeney, Eileen` (mục không ghi tên tác giả — không sai, chỉ là thiếu). |
| `https://plato.stanford.edu/entries/porphyry/` | 200 | 64.928 B | 50k+ ký tự | Thật (kiểm để đối chiếu mục `CH04-CE03-03`). |
| `https://plato.stanford.edu/entries/medieval-philosophy/` | 200 | 161.099 B | **121.961 ký tự** | Thật. Dùng làm nguồn đối chứng cho đường truyền Aristotle thế kỷ 12. Không được dẫn trong mục — đây là nguồn của **người kiểm**. |
| Wikidata `wbgetentities` Q705378 / Q29001 / Q854920 / Q102851 | 200 | 17.042 / 16.466 / 8.556 / 185.276 B | JSON hợp lệ, có `entities` | Thật. Kết quả ghi ở từng mục. |

---

## `CH05-CE06-12` · Boethius

### (0) Q-ID và nhãn

`Q102851` → nhãn en/vi = **"Boethius"** ✓ đúng người, `P31 = Q5`.
P569 có ba giá trị: `+0480` (độ chính xác **năm**, rank **preferred**, 9 reference) và hai lần `+0475` (độ chính xác **thập niên**). P570 có ba giá trị: `+0525` (thập niên), `+0524-10-25` (ngày), `+0524` (năm, rank **preferred**, 3 reference).
→ Ghi chú biên tập khối **"Bốn điều không được viết về Boethius"** điểm (1) nói "480–524 ... là cặp số Wikidata để ở rank preferred" — **kiểm đúng, không sửa gì**. Đây là một trong số rất ít chỗ trong ghi chú khớp chính xác với dữ liệu.
SEP Marenbon mở bài đúng nguyên văn: *"(born: circa 475–7 C.E., died: 526? C.E.)"* — tức "nguồn chuyên ngành ghi sinh khoảng 475–477 và đặt dấu hỏi sau năm mất 526" **kiểm đúng từng chữ**. Trường `năm: k. 477 – k. 526 CN` hợp lệ.

### (1) Mệnh đề sai

**BẮT BUỘC — 1 lỗi. Đây là lỗi nặng nhất của cả bốn mục.**

> **Câu nguyên văn hiện tại:** "Lựa chọn ấy quyết định Tây Âu có thể nghĩ bằng cái gì trong sáu trăm năm sau đó: cho tới làn sóng dịch từ tiếng Ả Rập thế kỷ 12, Aristotle của Boethius chính là Aristotle ở phương Tây."

**Sai ở đâu — hai lớp:**

**Lớp 1 — sai đường truyền.** Cái chấm dứt thế độc quyền của Boethius trong logic **không phải** làn sóng dịch từ tiếng Ả Rập. Phần còn lại của bộ *Organon* (*logica nova*) đến với phương Tây qua **chính các bản dịch Latinh của Boethius được tìm lại**, cộng bản dịch thẳng từ Hy Lạp. SEP "Medieval Philosophy" (Marenbon) tách bạch hai dòng ở hai tiểu mục riêng — §1.3.2 *Greek to Latin* và §1.3.3 *Arabic to Latin* — và viết về logic: *"...supplemented by Porphyry and Boethius (the* logica vetus *) by the eleventh century, and once the rest of the* Organon *(the* logica nova *) became available, by the early thirteenth century..."* (121.961 ký tự, đã mở kiểm). Cái **thật sự** đến qua tiếng Ả Rập là triết học tự nhiên, siêu hình học và các nhà bình giải — không phải Organon.

**Lớp 2 — sai cả mốc "cho tới".** SEP Boethius nói ngược hẳn: *"In logic, Boethius's translations of Aristotle and Porphyry (except for that of the* Posterior Analytics *, which was lost) **remained standard throughout the Middle Ages**."* Tức bản dịch của ông không bị thay ở thế kỷ 12 mà **giữ vị trí chuẩn suốt thời trung cổ**. Câu "cho tới thế kỷ 12" biến một sự kiện kéo dài thành một sự kiện bị cắt.

**Lớp 3 — và đây là chỗ chạm quy tắc 7/8 của dự án: mệnh đề này được gán cho SEP mà SEP không nói.** Đếm máy trên toàn văn bản SEP "Boethius" đã bóc thẻ (70.352 ký tự): chuỗi **`Arabic` xuất hiện 0 lần**. Không có một chữ nào về tiếng Ả Rập trong bài được dẫn để đỡ cho câu này.

**Câu thay thế viết sẵn (dán thẳng vào mục):**

> "Lựa chọn ấy quyết định Tây Âu có thể nghĩ bằng cái gì trong hơn sáu thế kỷ sau đó: tới thế kỷ 11 chương trình logic Latinh gồm đúng hai tác phẩm Aristotle cộng Porphyry và chính Boethius — bộ *logica vetus* — và phải tới đầu thế kỷ 13 phần còn lại của *Organon* mới lưu hành rộng, phần lớn vẫn qua chính các bản dịch Latinh của ông được tìm lại."

(Nếu muốn ngắn hơn và vẫn an toàn: *"...cho tới khi phần còn lại của Organon lưu hành rộng ở đầu thế kỷ 13, Aristotle của Boethius chính là Aristotle ở phương Tây."* — chỉ cần bỏ hẳn cụm "dịch từ tiếng Ả Rập".)

**NÊN — 1 chỗ rào.**

> **Câu nguyên văn hiện tại:** "Ông chọn không viết triết học của riêng mình mà đổ gần cả đời vào việc dịch và **chú giải bộ Organon** của Aristotle sang Latinh."

**Sai ở đâu:** vế *dịch* đúng — ông dịch cả bộ Organon. Vế *chú giải* thì không: theo SEP, ông chỉ viết bình luận cho **Phạm trù** (một bản) và **Về mệnh đề** (hai bản), cộng hai bản cho *Isagoge* của Porphyry và một bản cho *Topica* của Cicero. Bốn tác phẩm còn lại của Organon ông dịch mà **không** chú giải. Cùng lỗi này lặp ở dòng `**Nguồn:**`, nơi ghi "các bình luận *Organon*" số nhiều.

**Câu thay thế viết sẵn:**

> "Ông chọn không viết triết học của riêng mình mà đổ gần cả đời vào việc dịch trọn bộ *Organon* của Aristotle sang Latinh và chú giải phần đầu của nó — *Phạm trù* một lần, *Về mệnh đề* hai lần."

và sửa dòng Nguồn: "hai bình luận *Isagoge*; bình luận *Phạm trù* và hai bình luận *Về mệnh đề*" (thay cho "các bình luận *Organon*").

**Không có lỗi ở ba mệnh đề còn lại:** "bản *Phân tích hậu* đã mất" ✓ (SEP: *"except for that of the Posterior Analytics, which was lost"*); "Kế hoạch dịch trọn cả Plato lẫn Aristotle thì không xong" ✓ (SEP: kế hoạch *"announced in the second commentary on On Interpretation (c. 516), and cut short by his execution — to translate and comment on all the writings of Plato and Aristotle"*); "Viết trong tù chờ án tử" ✓ (SEP: *"he was imprisoned and (probably in 526) executed, but not before he had the chance to write his literary masterpiece"*).

### (2) Nguồn bị dẫn ngược (quy tắc 7)

Hai bài SEP **có thật, mở được, đúng chủ đề** (bảng URL ở trên). Không có nguồn nào bị dẫn ngược **trong phần thân mục**. Nhưng có hai vấn đề quy thuộc:

1. **Mệnh đề "dịch từ tiếng Ả Rập" được gán cho SEP mà SEP không có một chữ nào** — đã nêu ở (1). Đây đúng hình dạng lỗi mà quy tắc 7 mô tả, chỉ khác chiều: không phải nguồn phản đối, mà nguồn **im lặng** trong khi mục nói như thể nó đỡ.
2. **Bài SEP thứ hai gần như không đỡ gì cả.** "Literary Forms of Medieval Philosophy" (Sweeney) có 35 lần nhắc Boethius và **có** đoạn đỡ được đúng một mệnh đề của mục — *"...allegorical figures, like Boethius's Lady Philosophy in the* Consolatio..." và *"the prosimetrum of Boethius's Consolation combining prose dialogue with poetry"* — tức nó đỡ cho "dựng một cuộc đối thoại với Triết học nhân cách hoá". Nhưng phần lớn chỗ nó nhắc Boethius là về *De Hebdomadibus* và hình thức tiên đề, thứ mục không hề nói tới. Đếm máy: **`Chaucer` 0 lần, `Jean de Meun` 0 lần** trong bài này.
   → Hệ quả cho dòng `**Ảnh hưởng tới:**`: cặp Chaucer / Jean de Meun **được đỡ bởi bài SEP thứ nhất, không phải bài thứ hai**. SEP Boethius §8 viết đúng chuyện ấy: *"Jean de Meun, who put the Consolation into Old French in the later thirteenth century, and Chaucer, who translated it into Middle English about a century later."* ✓ Dòng quan hệ **đúng, giữ nguyên** — chỉ cần biết nó tựa vào bài nào.

**CÂN NHẮC:** dòng Nguồn nên ghi tên tác giả cho bài thứ hai như đã làm với bài thứ nhất: `Stanford Encyclopedia of Philosophy, "Literary Forms of Medieval Philosophy" (Eileen Sweeney)`.

### (3) Liên kết sai người (quy tắc 8)

| Dòng | Đích thật | Đúng người? | Mức hiện tại | Phán quyết |
|---|---|---|---|---|
| `CH04-CE03-03` (Kế thừa từ) | **Porphyry xứ Tyre**, `k. 234–305 CN`, Q203445 | ✓ đúng người | `trực tiếp` | **xem dưới** |
| `CH03-BCE04-02` (Kế thừa từ) | **Aristotle**, Q868 | ✓ đúng người | `qua trường phái` | mâu thuẫn nội tại — xem dưới |
| Tranh luận phổ quát kinh viện | — | ✓ | `trực tiếp` | đúng |
| Chaucer / Jean de Meun | — | ✓ (SEP xác nhận) | `qua trường phái` | đúng |

**Vấn đề chính — và nó là một ca quy tắc 8 thật, không phải bắt bẻ.**

Porphyry mất **k. 305**; Boethius sinh **k. 477**. Khoảng cách **~172 năm**, lớn hơn cả ca 130 năm mà `CONTRIBUTING.md` quy tắc 8 nêu đích danh là thứ lint **không** bắt được. Hai người không thể gặp nhau; không có chuỗi thầy–trò nào nối họ.

Nhưng chi tiết quyết định không nằm ở con số năm, mà ở **lịch sử sửa đổi của chính dự án**. Tra `git log -S`: commit `045c86d` ("ch05: CH05-CE06-12 Boethius") đã thay dòng cũ trong mục Porphyry

```
- Logic kinh viện Latinh và Hồi giáo qua Boethius · kế thừa · qua trường phái
```
bằng
```
+ CH05-CE06-12 · kế thừa · trực tiếp
+ Logic Hồi giáo qua bản dịch Ả Rập của Isagoge · kế thừa · qua trường phái
```

Tức: **cùng một quan hệ, cùng hai con người, mức bằng chứng bị nâng từ `qua trường phái` lên `trực tiếp` ngay trong thao tác nối ID.** Không có bằng chứng mới nào được thêm; chỉ cái tên chuyển từ văn xuôi sang ID. Đánh giá cũ của chính dự án — `qua trường phái` — là đánh giá đúng.

Lập luận "nhưng Boethius dịch và chú giải thẳng văn bản Porphyry, thế là trực tiếp" **không cứu được mức này**, vì chính file đang tự bác nó: Boethius dịch và chú giải văn bản Aristotle theo đúng kiểu ấy, mà dòng `CH03-BCE04-02` lại ghi **`qua trường phái`**. Một mục không thể dùng hai thước cho cùng một loại quan hệ. Nếu "dịch văn bản = trực tiếp" thì Aristotle cũng phải lên `trực tiếp`; nếu không thì Porphyry phải xuống.

**Sửa viết sẵn — phải sửa ở CẢ HAI file (vòng đối xứng sẽ bắt nếu chỉ sửa một):**

Trong `content/ch05.md`, mục `CH05-CE06-12`, khối **Kế thừa từ**:
```
- CH04-CE03-03 · kế thừa · qua trường phái
```
Trong `content/ch04.md`, mục `CH04-CE03-03`, khối **Ảnh hưởng tới**:
```
- CH05-CE06-12 · kế thừa · qua trường phái
```

(Phương án thay thế, nếu Owner muốn giữ sắc thái "qua văn bản chứ không qua trường phái": vẫn hạ xuống `qua trường phái` ở cả hai chỗ, rồi ghi một dòng vào Ghi chú biên tập rằng từ vựng ba mức hiện **không có ô cho truyền thừa qua văn bản cách thế kỷ** — đúng hình dạng vấn đề mà quy ước `vùng:` đã phải ghi thành văn. Không được tự ý thêm giá trị mới vào `EVIDENCE_LEVELS` nếu không sửa cả `atlaslib/common.py` lẫn `prompts/atlas-prompt.md`.)

### (4) Chi tiết không truy được tới nguồn gốc

1. **"nơi: Rome và **Pavia**"** — đếm máy: chuỗi `Pavia` xuất hiện **0 lần** trong cả hai bài SEP được dẫn. SEP chỉ viết ông sống phần lớn đời dưới Theoderic, "unlikely that he travelled to Athens or Alexandria", và bị cầm tù rồi hành quyết — **không nêu địa điểm**. Pavia/Ticinum là truyền thống (mộ ở San Pietro in Ciel d'Oro), nhưng nơi hành quyết thực tế còn tranh luận (*ager Calventianus*). Đề nghị: đổi `nơi:` thành **"Rome và Ravenna, vương quốc Ostrogoth ở Ý"** (Ravenna là triều đình Theoderic, SEP có nói), hoặc giữ Pavia nhưng rào trong văn xuôi. Không để nguyên như sự kiện.
2. **"sáu trăm năm"** — con số tròn tự suy ra từ k. 526 → k. 1125. Sau khi sửa theo (1) ở trên thì mốc đúng là "đầu thế kỷ 13", nên con số cũng phải đổi; câu thay thế đã dùng "hơn sáu thế kỷ".
3. **"tên ông đã hai lần xuất hiện trong atlas như cơ chế truyền cho Porphyry ở `CH04-CE03-03`, một lần ngay trong dòng quan hệ"** — `grep` hiện tại toàn `content/` cho **đúng một** lần còn lại (văn xuôi mục Porphyry, `ch04.md:446`). Dòng quan hệ kia **đã bị chính commit này xoá** (xem (3)). Mệnh đề đúng về quá khứ, sai về hiện tại, và độc giả không có cách nào biết. **CÂN NHẮC** sửa thành: *"...tên ông đã hai lần xuất hiện trong atlas như cơ chế truyền cho Porphyry ở `CH04-CE03-03` — một lần trong văn xuôi, một lần trong dòng quan hệ mà mục này vừa thay bằng một liên kết thật — mà chưa bao giờ có mục riêng."*
4. **"Phần lớn mười một mục còn lại của nhóm CE06 phải rào niên đại hoặc rào quy thuộc"** — kiểm được bằng script trên `data/persons.json` và **đúng**: trong 12 mục CE06, độ tin cậy niên đại là **Cao 5 / Trung bình 3 / Thấp 4**, tức 7/12 phải rào niên đại — đã trừ chính Boethius (Trung bình) thì là 7/11. "Phần lớn mười một mục còn lại" đứng vững. Giữ nguyên.
5. **"Boethius thì tác phẩm còn nguyên vẹn"** — không đúng tuyệt đối: bản dịch *Phân tích hậu* **đã mất**, chính mục nói thế ở đoạn trên. **CÂN NHẮC** đổi thành "tác phẩm chính còn nguyên vẹn" để mục không tự mâu thuẫn trong vòng hai đoạn.


---

## `CH05-CE06-10` · Bumin Qaghan

### URL / nguồn đã mở kiểm cho mục này

| Nguồn | Cách mở | HTTP | Kích thước tải | Chữ thật | Đánh giá |
|---|---|---|---|---|---|
| `周書/卷50` | zh.wikisource **MediaWiki API** (`action=query&prop=revisions&rvslots=main&formatversion=2`) | 200 | 34.092 B | **12.104 ký tự wikitext** | Thật. `title` trả về đúng `周書/卷50`, có `revisions`. Tiêu đề mục: 卷五十 列傳第四十二 **異域下**, tác giả 唐 **令狐德棻**. |
| `北史/卷099` | cùng API | 200 | 34.106 B | **11.535 ký tự** | Thật. 卷九十九 列傳第八十七 **突厥 鐵勒**, tác giả **李延壽**. |
| `隋書/卷84` | cùng API | 200 | 37.162 B | **12.646 ký tự** | Thật. 列傳第四十九 **北狄**, 唐 **魏徵** 等. |
| HCCA vol. III (UNESCO), bản PDF gương almuslih.org | `curl` với UA `history-atlas/0.1 (research)` | 200 | **10.773.125 B** | PDF **558 trang** (đọc `/Count` từ byte thô; `file` báo nhầm "32 pages" — ghi lại như một cái bẫy mới) | Thật, trích được text bằng pypdf. |
| Wikidata `wbgetentities` `Q29001` | API | 200 | 16.466 B | JSON hợp lệ | Thật. |
| `https://doi.org/10.2143/JA.307.1.3286342` (Yoshida 2019) | `curl -sL` + `Accept: application/vnd.citationstyles.csl+json` | 302 → **200** | **421 B** CSL-JSON | **Thật, đọc được.** Xem (5) — ghi chú biên tập nói DOI này trả 406, nay **không còn đúng**. |
| `https://poj.peeters-leuven.be/content.php?url=article&id=3286342&journal_code=JA` | `curl -sL` + UA chung | 200 | 20.283 B | có abstract chữ thật (~900 ký tự) | Thật. |

**Lưu ý quy trình (đúng loại bẫy mà ghi chú biên tập đang cảnh báo):** tiêu đề trang Wikisource của Bắc sử là `北史/卷099` — **có số 0 đệm**. Gọi `北史/卷99` thì API trả `missing: true`. Dùng API JSON nên phát hiện ngay; nếu fetch HTML thì sẽ nhận một trang 404 có `<title>` trông như trang thật. Số quyển mà mục ghi (**quyển 99**) là **đúng**; chỉ là quy ước đặt tên của Wikisource.

### (0) Q-ID và nhãn

`Q29001` → nhãn en = **"Bumin Qaghan"** ✓ đúng người, `P31 = Q5` (1 reference).
`P569 = +0490`, **precision 9 (năm)**, rank normal, **0 reference** — khớp chính xác ghi chú biên tập.
`P570 = +0552`, precision 9, rank normal, 1 reference.

### (1) Mệnh đề sai

**BẮT BUỘC — 1 lỗi.**

> **Câu nguyên văn hiện tại:** "Ông làm khả hãn nhiều nhất một năm, và mọi chinh phục thường bị gán cho ông — diệt Nhu Nhiên, phá Hiệt Đát, mở đường tới Byzantium — chính văn đều chép dưới tên Mộc Hãn khả hãn hoặc sau khi ông chết."

**Sai ở đâu:** vế "chính văn đều chép dưới tên Mộc Hãn khả hãn" **không đúng với cả ba hạng mục**, và sai nặng nhất ở hạng mục thứ ba.

1. **"mở đường tới Byzantium"**: chính sử Trung Hoa **không chép một dòng nào** về việc này. Đếm máy trên toàn văn ba quyển: 「拂菻」 xuất hiện **1 lần** trong 北史卷099 và **1 lần** trong 隋書卷84, cả hai đều nằm trong **danh sách địa lý các bộ lạc Thiết Lặc** (「拂菻東，則有恩屈、阿蘭…」), không liên quan gì đến sứ đoàn; 「大秦」 2 lần trong 周書卷50, đều trong mục Ba Tư/Tây Vực. Không có sứ đoàn, không có Mộc Hãn. Nguồn duy nhất là **Menander Protector** (Hy Lạp), và chính nguồn mà mục đang dẫn — Sinor, tr. 328 — gán sứ đoàn đầu (563) cho **Askel**, thủ lĩnh bộ thứ nhất của liên minh Nỗ Thất Tất thuộc Tây Đột Quyết, và sứ đoàn 568 của **Maniakh** cho **Silziboulos**, "*who is usually wrongly identified with Ishtemi*". Không ai trong số này là Mộc Hãn.
2. **"phá Hiệt Đát"**: chính văn Trung Hoa **có** chép dưới tên Mộc Hãn ✓ (北史卷099: 「俟斤又西破嚈噠，東走契丹，北並契骨」). Nhưng **chính nguồn được dẫn thì không**: Sinor tr. 327 viết cuộc diệt Hiệt Đát 557–561 là "*through a joint action of the Türks (**probably led by Ishtemi**) and the Sasanian king, Khusrau I Anushirvan*".
3. **"diệt Nhu Nhiên"**: mâu thuẫn nội bộ ngay trong cùng đoạn — câu trước đó của chính mục viết "đầu 552 ông đánh bại Nhu Nhiên", và chính văn xác nhận (周書卷50: 「魏廢帝元年正月，土門發兵擊茹茹，大破之於懷荒北。阿那瓌自殺」). Cái được chép dưới tên Mộc Hãn là việc **diệt nốt tàn dư** (鄧叔子), về sau.

**Câu thay thế (viết sẵn, dán được):**

> "Ông làm khả hãn nhiều nhất một năm, nên hầu hết những gì thường được gán cho ông thì chính văn lại chép dưới tên người khác: Chu thư và Bắc sử đặt việc diệt nốt tàn dư Nhu Nhiên (鄧叔子) và phá Hiệt Đát dưới tên Mộc Hãn khả hãn, sau khi ông chết; còn việc mở đường tới Byzantium thì chính sử Trung Hoa không chép một dòng nào — hai sứ đoàn 563 và 568 chỉ được biết qua Menander Protector, và đều thuộc cánh Tây chứ không thuộc ông."

### (2) Nguồn bị dẫn ngược (quy tắc 7)

**Dòng `**Nguồn:**` hiện tại:** "周書 quyển 50, liệt truyện 42, Dị vực hạ (Lệnh Hồ Đức Phân, hoàn thành 636); 北史 quyển 99; Denis Sinor, chương 14 trong *History of Civilizations of Central Asia*, tập III (UNESCO), tr. 328."

**a) 周書 quyển 50 — đúng từng chi tiết.** Mở API: mục đúng là 「卷五十 列傳第四十二 **異域下**」 ✓ (quyển 50 ✓, liệt truyện 42 ✓, Dị vực **hạ** ✓), tác giả 「唐 令狐德棻」 ✓. Toàn bộ chuỗi niên đại của mục kiểm khớp nguyên văn:
- 「大統十一年，太祖遣酒泉胡安諾槃陀使焉」 = **545**, sứ bộ Tây Ngụy tới ✓
- 「十二年，土門遂遣使獻方物」 = **546** ✓
- 「十七年六月，以魏長樂公主妻之」 = **551/6** ✓
- 「魏廢帝元年正月，土門發兵擊茹茹，大破之於懷荒北…土門遂自號伊利可汗」 = **552/1** ✓
- 「爾是我鍛奴，何敢發是言也？」 ✓ nguyên văn, đúng người nói (阿那瓌), đúng thứ tự (sau 546, trước 551) ✓
- 「土門死，子科羅立」 ✓

**b) 北史 quyển 99 — số quyển đúng** (卷九十九 列傳第八十七 突厥 鐵勒, 李延壽) ✓. Nhưng xem (5): ghi chú biên tập mô tả sai nội dung quyển này.

**c) Sinor, chương 14, tập III — bibliografi đúng, nhưng thiếu một đồng tác giả và trích hơi lệch trang.**
Mở PDF toàn tập (200 / 10.773.125 B / 558 trang), trang tiêu đề chương (pdfindex 320 = **trang in 321**) ghi nguyên văn: **"14 — THE TÜRK EMPIRE * — D. Sinor and S. G. Klyashtorny"**; mục lục chương có "Political history ... 327".
→ **Chương 14 ✓, tập III ✓, tr. 328 có thật và đúng chủ đề ✓.**
→ Hai điểm phải sửa, mức **NÊN**: (i) chương **đồng tác giả với S. G. Klyashtorny**, dẫn trống một mình "Denis Sinor" là thiếu; (ii) phần nói về **chính Bumin** nằm ở **tr. 327** ("*Bumin died shortly after he had deposed A-na-kui*"), tr. 328 đã sang đời Mộc Hãn/Tháp Bát/Nivar. Nên dẫn **tr. 327–328**.

**Câu thay thế cho dòng Nguồn (viết sẵn):**

> **Nguồn:** 周書 quyển 50, liệt truyện 42, Dị vực hạ (Lệnh Hồ Đức Phân, hoàn thành 636); 北史 quyển 99, liệt truyện 87, Đột Quyết – Thiết Lặc (Lý Diên Thọ); D. Sinor và S. G. Klyashtorny, chương 14 "The Türk Empire", trong *History of Civilizations of Central Asia*, tập III (UNESCO), tr. 327–328.

**d) Có bị dẫn ngược không?** Có, mức nhẹ ở mục và **mức nặng ở ghi chú biên tập** (xem (5)). Ở mục: Sinor được dẫn để đỡ cho câu "chính văn đều chép dưới tên Mộc Hãn khả hãn", trong khi Sinor gán Hiệt Đát cho **Ishtemi** và Byzantium cho **Askel/Silziboulos**. Sửa theo câu thay thế ở (1) là hết.

### (3) Liên kết sai người / sai mức bằng chứng (quy tắc 8)

| Dòng | Kiểm | Kết luận |
|---|---|---|
| `CH03-BCE02-12 · tương đồng độc lập · suy đoán học giả` (Kế thừa từ) | `CH03-BCE02-12` = **Mặc Đốn thiền vu** (`content/ch03.md:607`) ✓ đúng người. Cách nhau ~660 năm nên `trực tiếp` là bất khả; `suy đoán học giả` ✓ đúng mức. | **Không lỗi.** Ghi thêm một sắc thái: chính 周書卷50 tự nối hai người — 「土門遂自號伊利可汗，**猶古之單于也**。號其妻為可賀敦，**亦猶古之閼氏也**」. Nhưng đó là phép loại suy của **sử quan Đường năm 636**, không phải bằng chứng Bumin vay mượn, nên `tương đồng độc lập · suy đoán học giả` là cách ghi **thận trọng đúng mức**. Giữ nguyên. |
| `Nhu Nhiên hãn quốc · phản bác · trực tiếp` | Nút văn bản tự do, không phải ID. Đương thời ✓ (A Na Quỳ chết 552, do chính Bumin đánh). | **Không lỗi.** |
| `Mộc Hãn khả hãn và Đột Quyết hãn quốc 553–572 · kế thừa · trực tiếp` (Ảnh hưởng tới) | 周書卷50 和 北史卷099 đều chép Mộc Hãn (俟斤/燕都) là **con Bumin**, lên ngôi sau anh là 科羅. Sinor tr. 327 độc lập xác nhận "*Bumin's other son Muhan (553–572)*" — **khớp cả quan hệ lẫn hai mốc 553–572** ✓. | **Không lỗi.** `trực tiếp` chính đáng (cha–con, kế vị cách nhau vài tháng). |
| `Bi ký Orkhon thế kỷ 8 · kế thừa · qua trường phái` | Nút văn bản tự do. Cách ~2 thế kỷ nên `trực tiếp` sẽ sai; `qua trường phái` ✓. Sinor tập III có hẳn tiểu mục "Epigraphic memorials of the Türks" tr. 337. | **Không lỗi.** |

**Kết luận (3): không có lỗi quy tắc 8 ở mục này.** Không có liên kết nào trỏ nhầm người, không có mức bằng chứng nào bị nâng quá bằng chứng. Nói thẳng để đối chiếu: đây là mục **sạch nhất về quy tắc 8** trong bốn mục — ngược hẳn với `CH05-CE06-12`.

### (4) Chi tiết viết như sự kiện mà không truy được tới nguồn gốc

1. **Trường `nơi:` — "cao nguyên Mông Cổ, núi Ötükän (都斤山) và lưu vực Orkhon".** Không nguồn nào đặt **chính Bumin** ở Ötükän hay Orkhon.
   - 周書卷50 có 「可汗恆處於都斤山，牙帳東開」, nhưng câu này nằm trong **phần phong tục chung** của truyện Đột Quyết (giữa đoạn tang lễ và đoạn 「其書字類胡，而不知年曆」), mô tả hãn quốc **tại thời điểm biên soạn năm 636**, không nằm trong mạch kể về Bumin.
   - Mạch kể về chính Bumin đặt ông ở: 「始至塞上市繒絮」 (biên giới Tây Ngụy) và 「大破之於懷荒北」 (bắc Hoài Hoang).
   - Gốc A Sử Na thì chính văn đặt ở **金山** (Kim Sơn = Altai): 「居金山之陽，為茹茹鐵工」 (周書卷50), 「世居金山，工於鐵作」 (隋書卷84).
   - Sinor tr. 327 có nhắc Ötükän nhưng là khi mô tả **phần phía đông của đế quốc dưới thời Mộc Hãn (553–572)**, sau khi Bumin đã chết.
   - 「**lưu vực Orkhon**」 **không xuất hiện trong bất kỳ nguồn nào mục đang dẫn** — đây là suy diễn từ vị trí bi ký Orkhon thế kỷ 8, tức muộn hơn hai thế kỷ.
   → **NÊN sửa.** Câu thay thế cho trường: `nơi: biên giới bắc Tây Ngụy và thảo nguyên Mông Cổ; gốc A Sử Na ở Kim Sơn (金山, dãy Altai)`.
2. **"伊利可汗" phiên là "Y Lợi khả hãn"** ✓ có trong chính văn (周書卷50, 1 lần). Nếu ở đâu đó trong dự án phiên thành **"Illig Qaghan"** thì đó là **tái dựng của giới nghiên cứu**, không phải chữ của nguồn; Sinor không dùng dạng này. **CÂN NHẮC** rào nếu có dùng.
3. **"hoạt động 545–552 CN"** — truy được tới gốc ✓: 545 là 大統十一年 (lần đầu chính văn chép tới ông), 552 là 魏廢帝元年正月. Xem thêm (5) mục K.

### (5) Khối ghi chú biên tập về Bumin

Khối **"Ba mệnh đề phổ thông về Bumin bị chính văn bác"** và đoạn **"Một ghi chú về trường `năm:`"**. Kiểm từng mệnh đề:

| # | Mệnh đề trong ghi chú | Kết quả |
|---|---|---|
| A | 「隋書卷84 không hề có hai chữ 土門 (đếm máy: 0 lần)」 | **ĐÚNG** ✓ — đếm máy trên 12.646 ký tự wikitext: `土門` = **0**. |
| B | 「chỉ có vương hiệu 伊利可汗 và không một niên đại nào」 | **ĐÚNG** ✓ — `伊利可汗` = 1; `大統` = 0, `廢帝` = 0. |
| C | 「隋書卷84 mở mục Tây Đột Quyết bằng câu cho Tây Đột Quyết xuất từ con của Mộc Hãn khả hãn」 | **ĐÚNG từng chữ** ✓ — 「==西突厥== 西突厥者，木杆可汗之子大邏便也」. |
| D | 「việc tách Đông/Tây xảy ra dưới thời Nivar (581–587)」 | **ĐÚNG từng chữ** ✓ — Sinor tr. in **328**: "*It was at the time of Nivar that the rift separating Eastern and Western Türks occurred*", và "*Taghpar's brother, Nivar (581–587)*". Số trang 328 ở đây **chính xác**. |
| E | 「Denis Sinor nêu đích danh và **bác** cách hiểu 'chia đôi hãn quốc cho em là Istämi'」 | **SAI — BẮT BUỘC sửa.** Xem dưới. |
| F | 「chỉ 周書卷50 mới chép đủ chuỗi 545/546/551/552 và gọi tên ông」 | **SAI — BẮT BUỘC sửa.** Xem dưới. |
| G | 「北史卷99 ghép hai bản cạnh nhau mà không hòa giải」 | **SAI — BẮT BUỘC sửa.** Xem dưới. |
| H | 「chính sử Trung Hoa **không thống nhất** cả về việc người kế vị ông là con (科羅) hay em」 | **ĐÚNG về kết luận**, sai về chỗ đặt. Xem G. |
| I | 「Yoshida Yutaka (2019, *Journal Asiatique* 307/1) … kết luận rằng người được bia đề tặng theo cách đọc cũ 'không còn tồn tại trong bi ký'」 | **ĐÚNG**, nhưng cần nói rõ **là ai**. Xem dưới. |
| J | 「Năm sinh 490 trên Wikidata ở độ chính xác năm và không có reference nào」 | **ĐÚNG từng chi tiết** ✓ — `P569 = +0490`, `precision = 9`, `references = []`. |
| K | 「không bộ sử nào chép năm mất của ông — chỉ có hai chữ 「土門死」, và 552 là chọn một đầu của khoảng tháng 2/552 – tháng 3/553」 | **ĐÚNG** ✓ — 周書卷50 chỉ có 「土門死，子科羅立」, không niên đại; mốc dưới là 魏廢帝元年正月 (552), mốc trên là 「二年三月，科羅遣使獻馬五萬匹」 (553/3). Khoảng đúng như ghi chú mô tả. |
| L | 「DOI 10.2143/JA.307.1.3286342 trả **406** với content negotiation nên phải dẫn URL Peeters」 | **KHÔNG CÒN ĐÚNG.** Xem dưới. |

---

**E — BẮT BUỘC. Sinor bị dẫn ngược (đúng hình dạng quy tắc 7).**

> **Câu nguyên văn hiện tại:** "Thứ nhất, "chia đôi hãn quốc cho em là Istämi": Denis Sinor nêu đích danh và bác cách hiểu này — việc tách Đông/Tây xảy ra dưới thời Nivar (581–587) — và 隋書卷84 mở mục Tây Đột Quyết bằng câu cho Tây Đột Quyết xuất từ con của Mộc Hãn khả hãn, không phải từ Istämi."

**Sai ở đâu — Sinor không bác, ông khẳng định.** Nguyên văn tr. in **327** (pdfindex 326, trích bằng pypdf từ bản PDF 558 trang):

> "*On his death, the government of the newly created Türk Empire was divided between Bumin's other son Muhan (553–572) and **Ishtemi (553– ?), Muhan's uncle, and brother of the late Bumin**. Muhan ruled over the eastern part of the empire, centred on Mongolia, while Ishtemi was in charge of the western areas. … Thus it can be said that **almost from the moment of its inception, the Türk Empire was bicephalous**.*"

Tức Sinor **xác nhận cả hai vế** mà ghi chú nói ông bác: (i) Istämi **đúng là em Bumin**, (ii) hãn quốc **đúng là bị chia đôi Đông/Tây ngay từ 553**. Cái ông đính chính là chuyện khác và hẹp hơn: việc chia đôi không do **Bumin** làm cho em, mà xảy ra sau khi con ông là 科羅 chết, và giữa **con Bumin (Mộc Hãn)** với em Bumin; còn cái xảy ra dưới thời Nivar là **"the rift"** — sự **đứt gãy thành hai nhà nước đối địch**, không phải cấu trúc hai đầu.

Vế thứ hai cũng không đứng: ghi chú dùng 隋書卷84 để nói Tây Đột Quyết "không phải từ Istämi", nhưng chính Sinor tr. 328 viết "*the principal ruler of the Western Frontier Region of the Türk Empire was **Tardu, a son of Ishtemi***". Hai mệnh đề này nói về hai thứ khác nhau (dòng dõi nhà nước Tây Đột Quyết hậu-581 vs. người cầm cánh Tây trước đó), và ghép chúng thành một lời bác là ép nguồn.

**Câu thay thế (viết sẵn, dán được):**

> "Thứ nhất, "Bumin chia đôi hãn quốc cho em là Istämi": phải tách làm hai mệnh đề. Sinor và Klyashtorny (tr. 327) **xác nhận** Istämi là em Bumin và hãn quốc có hai đầu "gần như ngay từ lúc khai sinh" — nhưng việc chia ấy xảy ra **sau khi Bumin và con cả ông là 科羅 đã chết**, và là giữa con ông là Mộc Hãn với em ông, chứ không phải một sự phân phong do chính Bumin thực hiện. Còn sự **đứt gãy** thành hai nhà nước Đông/Tây đối địch thì hai ông đặt ở thời Nivar (581–587), tr. 328. Mục vì vậy không ghi bất kỳ hành vi phân phong nào cho Bumin."

---

**F — BẮT BUỘC. "Chỉ 周書卷50" là sai; 北史卷099 chép y hệt.**

> **Câu nguyên văn hiện tại:** "chỉ 周書卷50 mới chép đủ chuỗi 545/546/551/552 và gọi tên ông."

**Sai ở đâu:** 北史卷099 chép **đúng cùng một chuỗi, cùng chữ, và gọi tên 土門 tám lần** (đếm máy: `土門` = **8**). Nguyên văn:

> 「其後曰土門，部落稍盛，始至塞上市繒絮，願通中國。**西魏大統十一年**，周文帝遣酒泉胡安諾槃陀使焉。… **十二年**，土門遂遣使獻方物。… 周文帝許之，**十七年六月**，以魏長樂公主妻之。… **廢帝元年正月**，土門發兵擊蠕蠕，大破之於懷荒北。」

(Chú ý một cái bẫy đếm máy mà vòng trước đã mắc: cả hai bộ đều viết năm 546 là 「十二年」 **không lặp lại niên hiệu 大統**, nên `grep "大統十二年"` ra 0 lần ở Bắc sử — và ở Chu thư thì 1 lần đó lại nằm trong truyện **Hiệt Đát**, không phải truyện Đột Quyết. Phải đọc câu, không chỉ đếm chuỗi.)

**G — BẮT BUỘC. 北史卷099 không "ghép hai bản cạnh nhau"; chỗ bất nhất nằm ở 隋書卷84.**

> **Câu nguyên văn hiện tại:** "北史卷99 ghép hai bản cạnh nhau mà không hòa giải, nên chính sử Trung Hoa **không thống nhất** cả về việc người kế vị ông là con (科羅) hay em."

**Sai ở đâu:** 北史卷099 cho **đúng một** bản, liền mạch, trùng Chu thư: 「**土門死，子科羅立**。科羅號乙息記可汗，又破叔子于沃野北賴山。且死，舍其子攝圖，立其弟俟斤，是為木杆可汗。」 Không có chỗ nào ghép hai bản.
Chỗ bất nhất nằm ở **隋書卷84**: 「卒，**弟**逸可汗立」. Chính 校勘記 in kèm Chu thư nói đúng điều đó: 「隋書卷八四突厥傳云伊利『卒，弟逸可汗立』。伊利即土門，逸可汗即科羅或乙息記可汗，作『子』作『弟』不同。」
→ **Kết luận "chính sử Trung Hoa không thống nhất" là ĐÚNG; chỉ gán nhầm chỗ.** Sửa chỗ gán là xong.

**Câu thay thế cho cả F và G (viết sẵn, dán được, thay nguyên hai câu):**

> "chỉ 周書卷50 và 北史卷099 mới chép đủ chuỗi 545/546/551/552 và gọi đích danh 土門 (Bắc sử 8 lần, gần như trùng chữ với Chu thư). Chỗ chính sử Trung Hoa **không thống nhất** là người kế vị: Chu thư và Bắc sử đều chép 「土門死，**子**科羅立」, còn 隋書卷84 chép 「卒，**弟**逸可汗立」 — và 校勘記 in kèm Chu thư nêu thẳng sự khác biệt 「作『子』作『弟』不同」."

---

**I — NÊN. Phát hiện của Yoshida là về Mahan Tegin, không phải về Bumin.**

> **Câu nguyên văn hiện tại:** "Thứ ba, "bi ký Bugut nhắc tên ông": bản dịch Kljaštornyj & Livšic 1972 đang được trích lại trên web **từ một thread diễn đàn**, trong khi Yoshida Yutaka (2019, *Journal Asiatique* 307/1) đã hiệu đính lại bằng ảnh 3D và kết luận rằng người được bia đề tặng theo cách đọc cũ "không còn tồn tại trong bi ký"."

Dữ liệu thư mục **kiểm đúng hết** qua content negotiation DOI (200 / 421 B CSL-JSON): tác giả `YOSHIDA, Yutaka`; năm `2019`; tạp chí `Journal Asiatique`; `issue: 1`; **trang `97–108`**; nhan đề **"Sogdian Version of the Bugut Inscription Revisited"**. Abstract trên Peeters (200 / 20.283 B) nói nguyên văn: "*The most important is the discovery that **Mahan Tegin**, to whom the inscription was believed to be dedicated, **no longer exists in the inscription**.*"
**Vấn đề:** ghi chú đặt câu này ngay sau mệnh đề "bi ký Bugut nhắc tên **ông** [Bumin]", khiến người đọc hiểu rằng cái bị Yoshida xoá là tên **Bumin**. Thực tế cái bị xoá là **Mahan Tegin**; còn bia, theo bản mới, nói về tính chính danh của **Tatpar** và con là **Umna**. Lập luận "mục không dẫn Bugut" vẫn đứng, chỉ cần nói đúng tên.

**Câu thay thế (viết sẵn):**

> "Thứ ba, "bi ký Bugut nhắc tên ông": bản dịch Kljaštornyj & Livšic 1972 đang được trích lại trên web **từ một thread diễn đàn**, trong khi Yoshida Yutaka, "Sogdian Version of the Bugut Inscription Revisited", *Journal Asiatique* 307/1 (2019), tr. 97–108, đã hiệu đính lại bằng ảnh 3D và kết luận rằng **Mahan Tegin** — người mà cách đọc cũ cho là bia đề tặng — "không còn tồn tại trong bi ký"; theo bản mới, bia nói về tính chính danh của Tatpar khả hãn và con là Umna. Toàn bộ nền văn bản của bia vì vậy vừa đảo, nên mục không dẫn Bugut."

**L — CÂN NHẮC. Mẹo URL đã lạc hậu.**

> **Câu nguyên văn hiện tại:** "DOI 10.2143/JA.307.1.3286342 trả **406** với content negotiation nên phải dẫn URL Peeters."

Kiểm lại hôm nay (2026-10-31) với UA chung: `curl -sL -H 'Accept: application/vnd.citationstyles.csl+json'` → **302 → 200, 421 byte CSL-JSON hợp lệ**, qua `data.medra.org`. Không còn 406.
**Câu thay thế:** "DOI 10.2143/JA.307.1.3286342 từng trả **406** với content negotiation (kiểm lại 31-10-2026: nay trả 200 qua `data.medra.org`, 421 byte CSL-JSON); URL Peeters `poj.peeters-leuven.be/content.php?url=article&id=3286342&journal_code=JA` trả 200 / 20.283 byte có abstract chữ thật, dẫn được."

### Kết luận `CH05-CE06-10`

Thân mục là **mục chắc nhất về nguồn sơ cấp trong cả bốn mục**: mọi mốc niên đại, câu chửi 「爾是我鍛奴」, vương hiệu 伊利可汗 và quan hệ cha–con với Mộc Hãn đều khớp nguyên văn 周書卷50 và 北史卷099, và số quyển của cả hai đều **đúng** khi mở mục lục thật. Không có lỗi quy tắc 8.
Lỗi nằm ở **một câu trong thân mục** (Byzantium/Mộc Hãn) và ở **ba mệnh đề trong ghi chú biên tập** (E, F, G) — trong đó E là một ca dẫn nguồn ngược đúng hình dạng quy tắc 7: một chuyên gia được nêu đích danh là "bác" điều mà trang 327 của chính ông khẳng định.

---

## CH05-CE06-09 · Kaleb xứ Aksum

### URL đã mở kiểm cho mục này

| URL | HTTP | byte | ký tự chữ thật | ghi chú |
|---|---|---|---|---|
| `ancientarabia.huma-num.fr/dictionary/definition/aksum-arabia-and` | 200 | 49.022 | **17.523** | Hatke, "Aksum [and South Arabia]" — đọc được, đủ chữ |
| `ancientarabia.huma-num.fr/dictionary/definition/kaleb` | 200 | 31.741 | **6.135** | Hatke, "Kālēb" — **mục riêng, atlas không dẫn** |
| `doi.org/10.60667/tdaa-0005` (CSL-JSON) | 200 | 611 | 611 | xác nhận Hatke 2023, chapter, *Thematic Dictionary of Ancient Arabia* |
| `doi.org/10.60667/tdaa-0059` (CSL-JSON) | 200 | 608 | 608 | xác nhận mục "Kālēb" cùng bộ |
| Hatke, *PAN* 2023 (PDF đã tải, `pan.pdf`) | 200 | 884.215 | 183.343 (pypdf) | 58 trang; mục 3.5 bàn riêng RIÉth 191 |
| `api.openalex.org/works?search=Joseph dernier roi de Himyar` | 200 | 316.179 | — | xác nhận thư mục Robin 2008 |
| `en.wikipedia.org/api/rest_v1/page/html/Ja_1028` | 200 | 32.887 | **5.437** | bản dịch Ja 1028 theo CSAI (nguồn hạng ba, chỉ dùng đối chiếu) |
| `dasi.cnr.it/csai-epi-2416` và `dasi.cnr.it/` | **000** | **0** | 0 | **không nối được** (cả http lẫn https, cả hai lần thử) |
| `repositories.lib.utexas.edu/.../content` (luận án Kjær) | **403** | 919 | ~0 | HTML chặn, không phải PDF |
| `academia.edu/.../Religious_Ideology_in_the_Gəʿəz_Epigraphic_Corpus_from_Yemen` | **403** | 5.754 | **58** | Cloudflare "Just a moment…" |
| `dialnet.unirioja.es` (bản ghi Robin JSAI 34) | **000** | 0 | 0 | curl 000; WebFetch `ECONNREFUSED 193.144.2.34:443` |
| `books.openbookpublishers.com/10.11647/obp.0219/ch7.xhtml` | **405** | 2.145 | — | đúng như bẫy đã ghi trong ghi chú biên tập (UA chung bị từ chối) |

Mọi lệnh gọi mạng dùng `User-Agent: history-atlas/0.1 (research)`, không có thông tin cá nhân trong header/URL/payload.

### (0) Q-ID và siêu dữ liệu

`wikidata: Q705378` → đúng người (Kaleb of Axum), `P31 = Q5`. ✓

`năm: trị vì k. 510 – k. 540 CN` khớp **nguyên văn** Hatke: "Kālēb (r. ca. 510–540 CE)" (mục "Kālēb"; cùng con số lặp lại trong mục "Aksum" và trong PAN tr. 355). ✓
`nơi: Aksum, nay thuộc Ethiopia, và Ḥimyar ở Yemen` ✓ — Hatke: "Kālēb spent seven months in South Arabia".
`vùng: Châu Phi hạ Sahara` ✓ theo quy ước nơi hoạt động chính.
`độ tin cậy niên đại: Trung bình` ✓ hợp lý (dung sai ±25 năm, tránh phải chọn phe 525/529).

### (1) Mệnh đề sai hoặc không đỡ được

#### 1a. BẮT BUỘC — "tiền đúc mang tên ông" làm bằng chứng quân Aksum có mặt ở Nam Arabia

**Câu hiện tại (dòng 145):**
> "Các bi ký Geʿez tìm thấy ngay tại Yemen và tiền đúc mang tên ông là bằng chứng vật chất rằng quân Aksum có mặt thật ở Nam Arabia, độc lập với mọi nguồn Kitô giáo."

**Hai lỗi chồng nhau:**

1. **Tiền đúc không chứng minh được điều đó, và không nguồn nào được dẫn nói thế.** Đếm trong hai nguồn đã mở: mục "Kālēb" chứa chữ `coin` **0 lần**; mục "Aksum [and South Arabia]" chứa `coin` **1 lần** và lần ấy nói về dạng Hy Lạp hoá `ABACCIN` trên một đồng tiền Aksum khoảng năm 400 — không liên quan Kaleb. Tiền Aksum được đúc **tại Aksum**; nó chứng minh có ông vua, không chứng minh có đạo quân ở bên kia Biển Đỏ.
2. **"độc lập với mọi nguồn Kitô giáo" sai với chính loại bằng chứng vừa nêu.** Bi ký Geʿez ở Yemen là văn bản Kitô giáo công khai: Hatke viết chúng "quote from scripture, including Isaiah and the Book of Psalms" và "give a decidedly Biblical cast to the invasion". Chúng độc lập với **hagiography Hy Lạp–Syriac**, không độc lập với nguồn Kitô giáo.

**Bằng chứng vật chất mà Hatke thật sự nêu** cho sự hiện diện Aksum ở Nam Arabia là hai thứ khác: (a) nhóm bi ký Geʿez rời rạc ở Maʾrib và Ẓafār (RIÉth 195, 263, 264, Ẓafar 08-077, 265, 266) — và Hatke rào là chúng "**appear to** document the Aksumite invasion of 529"; (b) hai văn bản Sabaic `Ist 7608 bis` và `Wellcome A 103664` thời Sumūyafaʿ Ashwaʿ, trong đó người dâng cúng gọi "**their lords, the kings of the Aksumites**" (ʾmrʾ-hmw ngs²t ʾks¹m n) và nhắc "governors for the kings of the Aksumites" (ʿqbt m l-ngs²t ʾks¹m n). Đây mới là bằng chứng do **người bản địa Nam Arabia** khắc, nên thật sự độc lập với nguồn Kitô giáo Hy Lạp–Syriac.

**Câu thay thế (viết sẵn):**
> "Các bi ký Geʿez tìm thấy ngay tại Yemen — ở Maʾrib và Ẓafār — cùng hai văn bản Sabaic thời Sumūyafaʿ Ashwaʿ gọi thẳng "các chúa của chúng tôi, những vua Aksum" là bằng chứng vật chất tại chỗ rằng quân Aksum có mặt thật ở Nam Arabia, không phải chỉ có hagiography Hy Lạp và Syriac nói vậy."

#### 1b. NÊN — chuỗi chữ `klb ʾl ʾṣbḥ wld tzn` không truy được về nguồn nào đã mở

**Câu hiện tại (dòng 145):**
> "Bi ký RIÉth 191 nêu đích danh ông — `klb ʾl ʾṣbḥ wld tzn`, Kālēb ʾElla ʾAṣbəḥā con của Tāzēnā — kèm một vương hiệu dài mô phỏng đúng lối xưng của vua Ḥimyar."

- **Nửa sau ĐÚNG, và đúng mạnh.** Hatke, mục "Kālēb": RIÉth 191 "presents a title that is inspired in part by the so-called **Very Long Royal Title** borne by Himyarite kings since the fifth century, the chief difference being the addition of names of African vassals", kèm nguyên văn RIÉth 191/7–10: "King of Aksum and Ḥimyar and Dhū-Raydān and Sabaʾ and Salḥīn and Ṭawdum and Yamanāt and Tihāma and Ḥaḍramawt and all of their Arabs, and of the Beja and the Nubians and the Kushites and Ṣəyāmō and the DRBT". Không có lỗi ở đây.
- **Chuỗi phiên âm `klb ʾl ʾṣbḥ wld tzn`: [KHÔNG KIỂM ĐƯỢC].** Lý do cụ thể: tìm trong toàn bộ `pan.pdf` (58 trang, 183.343 ký tự — mục 3.5 bàn riêng RIÉth 191) **0 lần** xuất hiện `klb`, `ʾṣbḥ`, `tzn`, `ʾElla`, `Tāzēnā`; tìm trong hai mục từ điển cũng không có chuỗi phụ âm nào như vậy. Hatke chỉ viết dạng chuẩn hoá "Kālēb… son of his immediate predecessor, Tāzēnā, and bore as an alternative name ʾƎlla ʾAṣbəḥā". Phần vương hiệu ông trích nguyên văn (RIÉth 191/7–10) **bắt đầu bằng "King of Aksum"**, không kèm tên riêng. Ấn bản có thể kiểm được chuỗi này là Drewes & Schneider 1991: 271–274 và Drewes 2019: 248–255 — **không có bản số hoá mở**; DASI trả `000`.
- Lưu ý thêm: atlas viết `ʾElla`, Hatke viết `ʾƎlla` (chữ ə, không phải e). Khác biệt chuyển tự, CÂN NHẮC.

**Câu thay thế (viết sẵn) — giữ cái kiểm được, bỏ cái không:**
> "Bi ký RIÉth 191 ở Aksum, khắc bằng chữ musnad Nam Arabia, xưng ông bằng một vương hiệu dài phỏng theo "Vương hiệu Rất Dài" mà vua Ḥimyar dùng từ thế kỷ 5, chỉ thêm vào đó tên các chư hầu châu Phi: "vua của Aksum và Ḥimyar và Dhū-Raydān và Sabaʾ và Salḥīn và Ṭawdum và Yamanāt và Tihāma và Ḥaḍramawt và toàn thể người Ả Rập của họ, và của người Beja, người Nubia, người Kush, Ṣəyāmō và DRBT"."

#### 1c. KHÔNG CÓ LỖI — "chữ musnad" của RIÉth 191

Vòng trước từng nghi ngờ chi tiết này. **Nghi ngờ đó sai, mục viết đúng.** Hatke, PAN 2023, mục 3.5: "This forty-line Gəʿəz inscription is, like RIÉth 185 I and RIÉth 185 bis I from the reign of ʿEzānā, **written in the consonantal musnad script of South Arabia**." Mục "Kālēb" lặp lại: "written in the consonantal musnad script of pre-Islamic South Arabia". Cả `**Nguồn:**` ("Bi ký RIÉth 191 (Aksum, chữ musnad)") lẫn thân mục đều chính xác. **Không sửa gì.**

#### 1d. KHÔNG CÓ LỖI — câu cuối về Abraha

> "Hệ thống ấy sụp ngay trong đời ông: Abraha lật Sumūyafaʿ Ashwaʿ và đánh bại hai chiến dịch trừng phạt."

Khớp gần như từng chữ với Hatke, mục "Kālēb": Abraha "thwarted **two punitive campaigns** launched by Kālēb to remove him from power"; và mục "Aksum": "After two punitive campaigns sent by Kālēb failed to remove him from power, Abraha was left in place as king of Ḥimyar." ✓ **Không sửa.**

#### 1e. KHÔNG CÓ LỖI — "Thập niên 520 ông vượt Biển Đỏ"

Hatke, mục "Aksum": "Kālēb invaded Ḥimyar once again in the spring of 529, **this time leading the Aksumite army in person**"; mục "Kālēb": "four invasions… **one of which he led in person**". Việc đích thân vượt biển được nguồn đỡ ✓, và cách viết "thập niên 520" bao được cả 525 lẫn 529 nên tránh đúng chỗ tranh cãi. **Không sửa.**

#### 1f. CÂN NHẮC — "lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia"

**Câu hiện tại (dòng 147):** "Đây là lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia…"

Mệnh đề *lần cuối* không sai, nhưng mốc kết thúc không nằm ở Kaleb: theo Hatke, Abraha "was effectively an **autonomous** Ḥimyarite king" và "The dynasty founded by Abraha declined under his sons Yaksūm and Masrūq and **was toppled ca. 570**"; Gajda (cùng bộ từ điển) viết "The Ethiopian occupation of Ḥimyar lasted for about forty years, **between 530 and 570**". Tức giai đoạn Ethiopia cai trị Yemen kết thúc khoảng ba mươi năm **sau** khi Kaleb thoái vị, và phần lớn thời gian ấy nằm ngoài quyền kiểm soát của Aksum.

**Câu thay thế (viết sẵn):**
> "Đây là lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia — giai đoạn ấy kéo tới khoảng năm 570, nhưng phần lớn nằm trong tay Abraha, người đã tự trị khỏi Aksum — và cái thất bại của nó mới là phần có hệ quả dài:"

### (2) Quy tắc 7 — nguồn bị dẫn ngược chính nó

**Dòng `**Nguồn:**` hiện tại:**
> "Bi ký RIÉth 191 (Aksum, chữ musnad); George Hatke, mục "Aksum", trong *A Thematic Dictionary of Ancient Arabia*; Christian Julien Robin, "Joseph, dernier roi de Ḥimyar (de 522 à 525, ou une des années suivantes)", *Jerusalem Studies in Arabic and Islam* 34 (2008), tr. 1–124."

**Không có ca dẫn ngược kiểu quy tắc 7 ở mục này** — khác với `CH05-CE06-10`, nơi Sinor bị nêu đích danh là "bác" điều chính ông khẳng định. Nói thẳng: mục này **sạch** ở quy tắc 7. Nhưng có ba vấn đề nguồn khác, xếp thấp hơn:

**2a. NÊN — dẫn sai mục từ điển.** Mệnh đề về vương hiệu (xem 1b) nằm ở mục **"Kālēb"** (doi 10.60667/tdaa-0059), không nằm ở mục "Aksum [and South Arabia]" (doi 10.60667/tdaa-0005) mà atlas dẫn. Mục "Aksum" có bàn Kaleb thật (518, mùa xuân 529, Yūsuf, Sumūyafaʿ Ashwaʿ, Abraha, hai chiến dịch trừng phạt — tất cả đều kiểm được ở đó), nên dẫn mục "Aksum" không phải sai hoàn toàn; chỉ là **chi tiết đặc trưng nhất của thân mục lại ở mục kia**.

**2b. NÊN — dạng thư mục sai ba chỗ.** Nhan đề bộ sách không có mạo từ "A": tự trang dẫn là **"Thematic Dictionary of Ancient Arabia"**. Tên mục bị cắt: thật là **"Aksum [and South Arabia]"**. Thiếu năm và DOI. Dạng tự trang yêu cầu, đã kiểm qua DOI:

**Dòng `**Nguồn:**` thay thế (viết sẵn):**
> "**Nguồn:** Bi ký RIÉth 191 (Aksum, chữ musnad; ấn bản Drewes & Schneider 1991, tr. 271–274); George Hatke, "Aksum [and South Arabia]" và "Kālēb", trong *Thematic Dictionary of Ancient Arabia* (ấn bản trực tuyến 2023), doi 10.60667/tdaa-0005 và 10.60667/tdaa-0059; Christian Julien Robin, "Joseph, dernier roi de Ḥimyar (de 522 à 525, ou une des années suivantes)", *Jerusalem Studies in Arabic and Islam* 34 (2008), tr. 1–124."

**2c. Robin 2008: thư mục ĐÚNG, nội dung [KHÔNG KIỂM ĐƯỢC].**
Đã xác nhận qua OpenAlex `W951226220` (200 / 316.179 byte): tác giả **Christian Julien Robin**, nhan đề khớp từng chữ kể cả ngoặc đơn, *Jerusalem Studies in Arabic and Islam*, số **34**, trang **1–124**, năm **2008**. Atlas chép đúng hoàn toàn. ✓
Nhưng `open_access: {is_oa: false, oa_status: "closed", any_repository_has_fulltext: false}` — **không có bản toàn văn ở bất kỳ kho nào**, và Dialnet trả `000`/`ECONNREFUSED`. Vì vậy câu "Robin đặt sau **Lễ Ngũ Tuần 525**" là **[KHÔNG KIỂM ĐƯỢC]**: không mở được trang nào của bài để xác nhận chữ "Lễ Ngũ Tuần" (Pentecôte). Chỉ phần trong ngoặc kép — "ou une des années suivantes" — là kiểm được, vì nó nằm trong **chính nhan đề**.

**2d. CÂN NHẮC — câu trích bị gán cho một đối tượng khác với trong nguồn.** Nhan đề Robin nói về **niên đại trị vì của Yūsuf** ("Joseph, dernier roi de Ḥimyar, **de 522 à 525**, ou une des années suivantes"), còn atlas dùng câu ấy để nói **niên đại chiến dịch của Kaleb**. Hai thứ trùng nhau về thực chất (Yūsuf chết trong chiến dịch ấy) nên không phải lỗi sự kiện, nhưng câu trích đang được đặt vào một chủ ngữ khác với nguồn. Nếu muốn chặt, viết: "Robin đặt dấu chấm hết cho Yūsuf vào 525 'hoặc một trong những năm tiếp theo', Hatke đặt chiến dịch ở mùa xuân 529."

**2e. Một sắc thái đáng ghi, không phải lỗi của atlas:** Hatke **không nhất quán với chính mình** giữa hai ấn phẩm. Trong PAN 2023 (tr. 1220–1223 của bản trích chữ) ông viết bi ký Geʿez ở Yemen thuộc "the aftermath of his **second invasion** of South Arabia in **525**" — và chuỗi "529" xuất hiện **0 lần trong toàn bộ 58 trang**. Trong từ điển 2023 ông viết "the spring of **529**". Thêm nữa, ngay trong mục "Aksum" ông ghi Yūsuf "r. ca. **522–525**" nhưng lại cho Kaleb giết Yūsuf năm **529**. Câu của atlas ("Hatke đặt ở mùa xuân 529") vì vậy **đúng với một trong hai ấn phẩm**, và nên biết rằng khung "Robin 525 / Hatke 529" không phải một cuộc tranh luận hai người gọn gàng.

### (3) Quy tắc 8 — liên kết và mức bằng chứng

| Dòng | Đích | Người đúng? | Mức | Đánh giá |
|---|---|---|---|---|
| `Kế thừa từ: CH04-CE04-09 · kế thừa · qua trường phái` | Ezana xứ Aksum (ch04 dòng 747) | ✓ đúng người | `qua trường phái` | **Đúng.** Cách nhau ~145 năm (Ezana r. ca. 330–365 vs Kaleb r. ca. 510–540) nên `trực tiếp` sẽ sai; `qua trường phái` vừa đúng. Nội dung cũng có nguồn đỡ: Hatke ghi Ousanas và Ezana đã "lay claim to Sabaʾ and Ḥimyar, along with their respective royal palaces of Salḥīn and Raydān, in their titl[es]" — tức đúng cái truyền thống xưng hiệu mà Kaleb nối. |
| `Kế thừa từ: Truyền thống vương quyền Ḥimyar và lối xưng hiệu Nam Arabia · kế thừa · trực tiếp` | mô tả, không phải ID | — | `trực tiếp` | **Đúng, và đỡ được bằng nguyên văn**: vương hiệu RIÉth 191 "inspired in part by the so-called Very Long Royal Title borne by Himyarite kings since the fifth century". |
| `Ảnh hưởng tới: Abraha và Yemen tiền Hồi giáo · kế thừa · trực tiếp` | mô tả | — | `trực tiếp` | Mức `trực tiếp` **đúng** (Abraha là sĩ quan trong chính đạo quân Kaleb phái sang). Loại quan hệ `kế thừa` thì **CÂN NHẮC**: Abraha lật vua bù nhìn của Kaleb và đánh bại hai chiến dịch trừng phạt của ông, nên `phản bác` cũng đỡ được không kém. Giữ `kế thừa` thì nên hiểu là kế thừa thể chế vương quyền Kitô giáo ở Ḥimyar, không phải kế thừa ý chí Kaleb. |
| `Ảnh hưởng tới: Truyền thống "Năm Con Voi" trong sử liệu Hồi giáo · kế thừa · suy đoán học giả` | mô tả | — | `suy đoán học giả` | **Đúng mức.** Đây là chỗ dễ viết quá tay nhất và mục đã rào đúng. |

**Không có lỗi trỏ nhầm người ở mục này.** Hai liên kết có ID đều trỏ đúng, và không liên kết nào bị đặt mức bằng chứng cao hơn nguồn cho phép.

### (4) Chi tiết viết như sự kiện mà không truy được về nguồn

1. **`klb ʾl ʾṣbḥ wld tzn`** — xem 1b. [KHÔNG KIỂM ĐƯỢC]: 0 lần trong PAN (58 tr.), 0 lần trong hai mục từ điển; ấn bản gốc (Drewes & Schneider 1991; Drewes 2019) không có bản số hoá mở, DASI trả `000`.
2. **"tiền đúc mang tên ông"** — xem 1a. Không nguồn nào được dẫn nhắc tới tiền của Kaleb.
3. **"Lễ Ngũ Tuần 525"** — xem 2c. [KHÔNG KIỂM ĐƯỢC]: Robin JSAI 34 đóng truy cập, không kho nào có toàn văn.
4. **"dựng vua bù nhìn"** (số ít) — đúng nhưng thiếu: Hatke ghi **hai** vua bù nhìn, Maʿdīkarib Yaʿfur (518) và Sumūyafaʿ Ashwaʿ (529). Vì câu sau của mục nói Abraha lật Sumūyafaʿ Ashwaʿ, người đọc sẽ tự suy ra đúng, nên chỉ CÂN NHẮC.

### (5) Rà khối ghi chú biên tập "Năm 525 của Kaleb"

| | Mệnh đề trong ghi chú | Kết quả |
|---|---|---|
| **A** | "Ry 508, Ja 1028, Ry 507, Ry 513, Ry 515 — ghi niên đại năm 633 lịch Ḥimyar" | **ĐÚNG** cho Ja 1028: bản dịch theo CSAI ghi "The month of Mḏrʾn of the six hundred thirty-three". Ry 507/508 cùng năm 633 HE theo cùng nguồn. Ry 513/Ry 515 **[KHÔNG KIỂM ĐƯỢC]** (DASI `000`). |
| **B** | "tức tháng 6–7 năm 523 CN" | **NÊN rào.** Bản CSAI quy đổi 633 HE → **523 CE** ✓, nhưng phép quy đổi phụ thuộc kỷ nguyên Ḥimyar và một phần tài liệu chuyên ngành quy đổi cùng năm 633 thành **524**. Không mở được DASI để chốt, nên đừng viết dấu bằng trần trụi. |
| **C** | "nêu đích danh vua Yūsuf ʾAsʾar Yathʾar" | **ĐÚNG**, nguyên văn Ja 1028 dòng 1: "bless the king Yusuf ʾs¹ʾr Yṯʾr, the king of all the tribes". ✓ |
| **D** | "bi ký Sabaic **quanh Najrān**… do chính bên gây ra sự kiện khắc" | **NÊN sửa — và đây là chỗ đáng kể nhất trong khối.** Vị trí thì đúng (Ja 1028 ở Bir Ḥimā, cách Najrān 85 km đông bắc) và "do bên gây ra khắc" cũng đúng (người đặt khắc là viên tướng S²rḥʾl Yqbl của Yūsuf). **Nhưng** chính nguồn mà mục dẫn nói ngược: Hatke gán Ja 1028 / Ry 507 / Ry 508 cho việc Yūsuf **tàn sát đồn trú Aksum ở Ẓafār, đốt nhà thờ và phong toả bờ Biển Đỏ**, rồi viết thẳng về cuộc tấn công Najrān mùa thu 523: "**Although no Sabaic inscriptions refer directly to this campaign**, it is recorded in detail in sixth-century Greek and Syriac hagiographies." Tức theo Hatke, biến cố Najrān **không** có bi ký Sabaic nào chép trực tiếp — đúng điều ghi chú đang dựa vào. (Bản thân Ja 1028 có nhắc Nagrān, nhưng ở tư cách chiến dịch quân sự và canh phòng, không ở tư cách cuộc tàn sát.) |
| **E** | "Đó là bi ký đương thời… **độc lập với mọi nguồn Kitô giáo**" | **ĐÚNG** cho nhóm bi ký Sabaic này (do phía Do Thái giáo Ḥimyar khắc). Lưu ý: cùng cụm từ ấy ở **thân mục** lại gán cho bi ký Geʿez, và ở đó thì **sai** — xem 1a. |
| **F** | "Robin… tự đặt tên chuyên khảo của mình là 'de 522 à 525, ou une des années suivantes'" | **ĐÚNG**, xác nhận qua OpenAlex. ✓ Phần "sau Lễ Ngũ Tuần 525" thì [KHÔNG KIỂM ĐƯỢC]. |
| **G** | "Hatke dựng một chuỗi khác hẳn với **bốn lần** Aksum xâm nhập Nam Arabia, trong đó Kaleb **chỉ đích thân cầm quân một lần**, mùa xuân 529" | **ĐÚNG từng chi tiết**, nguyên văn mục "Kālēb": "launched **no fewer than four invasions** of South Arabia… **one of which he led in person**", và mục "Aksum": "in the spring of 529, this time **leading the Aksumite army in person**". ✓ Đây là mệnh đề được kiểm kỹ nhất và sạch nhất trong khối. |
| **H** | "Mục vì vậy viết 'thập niên 520', không viết 'năm 525'" | **ĐÚNG**, thân mục đúng là viết vậy. ✓ Quyết định này hợp lý và nên giữ. |
| **I** | "bi ký CIH 621 ghi 640 HE = tháng 2 năm 530" | **[KHÔNG KIỂM ĐƯỢC]** — DASI `000`, academia.edu 403, OBP 405. Kiểm được phần liên quan: Hatke xác nhận CIH 621 có dính tới cái chết của Yūsuf ("an event alluded to **obliquely** in CIH 621") nhưng **không cho niên đại**. Lời khuyên "đừng dẫn CIH 621 cho năm 525" vẫn đứng vững, vì nếu CIH 621 chỉ *ám chỉ xa* cái chết của Yūsuf thì nó không chốt được năm nào cả. |
| **J** | "Chuyện Kaleb thoái vị đi tu đến từ *Martyrium Arethae* (Hy Lạp, k. 560)… **không có nguồn Geʿez đương thời xác nhận**" | Phần "không có nguồn Geʿez đương thời" **đúng**: RIÉth 191 là bi ký duy nhất của triều Kaleb tìm được ở Ethiopia (Hatke, PAN mục 3.5) và nó không nói gì về thoái vị. Niên đại k. 560 của *Martyrium Arethae* **[KHÔNG KIỂM ĐƯỢC]** (không mở được ấn bản nào). Lưu ý Hatke lại chép việc thoái vị **như sự kiện**, không kèm cảnh báo: "Kālēb himself abdicated the throne ca. 540 and spent the remainder of his life as a monk". |
| **K** | "tức hagiography soạn khoảng **ba mươi lăm năm sau**" | **CÂN NHẮC — số không khớp với tiền đề liền trước.** 560 − 525 = 35 ✓ nếu đếm từ chiến dịch; nhưng câu đang nói về **việc thoái vị**, mà Hatke đặt thoái vị ở **k. 540**, tức cách *Martyrium Arethae* khoảng **hai mươi** năm. Nên viết rõ đếm từ mốc nào. |

**Câu thay thế cho D (viết sẵn):**
> "Mốc chắc nhất của toàn bộ câu chuyện lại không thuộc về Kaleb mà thuộc về đối thủ: nhóm bi ký Sabaic ở Bir Ḥimā gần Najrān — Ry 508, Ja 1028, Ry 507, Ry 513, Ry 515 — ghi niên đại năm 633 lịch Ḥimyar (quy đổi thường là tháng 6–7 năm 523 CN, có bản quy đổi ra 524) và nêu đích danh vua Yūsuf ʾAsʾar Yathʾar. Chúng do chính viên tướng của Yūsuf đặt khắc, nên độc lập với mọi nguồn Kitô giáo. Cần chính xác một chỗ: Hatke gán chúng cho việc Yūsuf tàn sát đồn trú Aksum ở Ẓafār và phong toả bờ Biển Đỏ, và nói thẳng rằng **không bi ký Sabaic nào chép trực tiếp** cuộc tấn công Najrān mùa thu 523 — biến cố ấy chỉ có trong hagiography Hy Lạp và Syriac."

**Câu thay thế cho K (viết sẵn):**
> "…tức hagiography soạn khoảng hai mươi năm sau lần thoái vị (Hatke đặt thoái vị ở khoảng năm 540), **không có nguồn Geʿez đương thời xác nhận**; mục không viết chi tiết này như sự kiện."

### Kết luận `CH05-CE06-09`

Mục Kaleb **không có ca dẫn nguồn ngược kiểu quy tắc 7 và không có lỗi quy tắc 8** — cả hai liên kết có ID đều trỏ đúng người và cả bốn mức bằng chứng đều đặt đúng, kể cả chỗ dễ viết quá tay nhất ("Năm Con Voi" được rào `suy đoán học giả`).
Lỗi thật nằm ở **một câu trong thân mục**: "tiền đúc mang tên ông" không được nguồn nào đỡ và không chứng minh được điều câu ấy nói, còn "độc lập với mọi nguồn Kitô giáo" thì sai với chính loại bằng chứng vừa nêu (bi ký Geʿez ở Yemen trích Isaiah và Thi thiên). Trong ghi chú biên tập, mệnh đề **D** cần sửa vì nguồn được mục dẫn nói ngược lại về chuyện bi ký Sabaic có chép biến cố Najrān hay không.
Ba chi tiết phải đánh dấu **[KHÔNG KIỂM ĐƯỢC]**, không được viết như sự kiện cho tới khi mở được ấn bản: chuỗi phiên âm `klb ʾl ʾṣbḥ wld tzn`, "Lễ Ngũ Tuần 525" của Robin, và niên đại 640 HE của CIH 621.
Một điểm vòng trước nghi sai mà **thực ra đúng**: RIÉth 191 **đúng là** khắc bằng chữ musnad — đừng "sửa" nó.

---

## CH05-CE06-11 · Bhavavarman I

### URL đã mở kiểm cho mục này

| URL | HTTP | byte | ký tự chữ thật | ghi chú |
|---|---|---|---|---|
| `michaelvickery.org/vickery1994what.pdf` | 200 | 205.860 | **52.593** (19 tr., pypdf) | URL trong `**Nguồn:**` — **sống, đọc được** |
| `angkordatabase.asia/.../Pre_Angkorian_cities_Ishanapura_and_Mahe.pdf` | 200 | 998.294 | **44.868** (11 tr.) | URL trong `**Nguồn:**` — **sống, đọc được** |
| Vickery 2003, "Funan Reviewed" (PDF đã tải) | 200 | — | **171.269** (45 tr.) | nguồn đối chứng, không nằm trong `**Nguồn:**` |
| `api.openalex.org/works?search=East and West New Inscriptions from Funan Zhenla and Dvāravatī` | 200 | 328.257 | — | xác nhận thư mục Goodall & Revire |
| `hal.science/halshs-04142364v1/document` | **200** | 2.549.302 | PDF 50 tr. | **đính chính một mục trong ghi chú biên tập: HAL nay mở được bằng UA chung, không trả trang chặn bot** |

### (0) Q-ID và siêu dữ liệu

`wikidata: Q854920` → đúng người (Bhavavarman I). Lưu ý đã ghi ở khối ghi chú: Q854920 khai **sinh 600 và mất 600**, vô nghĩa — nhưng `độ tin cậy niên đại: Thấp` bỏ qua đối chiếu Wikidata nên không gây hại. ✓

`năm: trị vì k. 550 – k. 600 CN` — **khớp nguyên văn nguồn được dẫn**: Heng & Lavy viết "Bhavavarman I (reigned around 550–600)". ✓ Vickery 1994 cũng đặt cái chết của ông "probably around 600". ✓

`vùng: Đông Nam Á` ✓. `lĩnh vực`, `câu hỏi lớn` ✓.

**`nơi:` thì có vấn đề — xem 1c.**

### (1) Mệnh đề sai

#### 1a. BẮT BUỘC — mệnh đề trung tâm của mục sai, và sai theo đúng nguồn mà mục dẫn

**Câu hiện tại (dòng 179), câu mở đầu của mục:**
> "Ông là vị vua sớm nhất ở lưu vực Mekong được chính bi ký Phạn ngữ tại chỗ định danh…"

**Sai.** Ba lớp bằng chứng, lớp nào cũng đến từ chính Michael Vickery — tác giả mà `**Nguồn:**` dẫn:

1. **Vickery 1994** (tr. 197–212, bài mà mục dẫn), nói về chính vấn đề này: "…given the distance between Funan, with the **Jayavarman-Rudravarman inscriptions in southern Cambodia and Vietnam**, and the Bhavavarman-Citrasena inscriptions in the north". Tức Vickery coi là hiển nhiên rằng có bi ký tại chỗ nêu tên hai vua Phù Nam **Jayavarman và Rudravarman** ở nam Campuchia và Việt Nam — tức ở lưu vực Mekong, và sớm hơn Bhavavarman I.
2. **Chính K.53 — một trong ba bi ký mà mục nêu đích danh — mở đầu danh sách vua bằng Rudravarman, không bằng Bhavavarman.** Vickery 1994: "K53 from Ba Phnom, dated AD 667… It lists four generations of a family which provided ministers to five kings, **Rudravarman**, Bhavavarman [I], Mahendravarman [Citrasena], Īśānavarman, and Jayavarman [I], the first and third of whom figure in the Chinese histories as respectively **last king of Funan** and the first conqueror from Chenla."
3. **Vickery 2003, "Funan Reviewed"** (BEFEO 90–91, tr. 101–143) cho số hiệu và niên đại cụ thể: "**K. 40**, written in mid-6th-century script, and found at **Tonle Bati, some 30 km southwest of Phnom Penh**… **names a King Rudravarman, son of a King Jayavarman**. Both these inscriptions are in **Sanskrit**"; và "A certain **Gunavarman**… whose record is at least **local contemporary evidence** (inscription **K. 5, early 5th century**)". Thêm **K. 875** của hoàng hậu Kulaprabhāvatī. Vickery gọi K.5, K.875, K.40 là "the three 5th-century inscriptions" / "the three inscriptions which may with some certainty be attributed to Funan".

Tức: bi ký Phạn ngữ tại chỗ ở lưu vực Mekong định danh người cai trị **sớm hơn Bhavavarman I ít nhất một thế kỷ rưỡi**.

Mức nghiêm trọng bị nhân đôi bởi `**Vì sao chọn**`, vốn viết: "Đổi lại, **mệnh đề trung tâm thì không cần rào**." Mệnh đề trung tâm chính là mệnh đề sai.

**Câu thay thế (viết sẵn) — giữ được cái thật sự đặc biệt ở ông:**
> "Ông là vị vua đầu tiên của vùng nội địa Campuchia để lại một cụm bi ký Phạn ngữ tại chỗ đủ để dựng lại một triều đại — trước ông, bi ký tại chỗ ở hạ lưu Mekong chỉ cho tên rời rạc của vài vua Phù Nam như Gunavarman, Jayavarman và Rudravarman."

Nếu muốn giữ hình thức một kỷ lục, phải đổi mốc so sánh chứ không đổi chữ: *sớm nhất* thì sai, *đầu tiên ở nội địa* hoặc *đầu tiên có cụm bi ký liên hoàn* thì đúng.

#### 1b. BẮT BUỘC — "không bi ký nào gắn với ông ghi niên đại Śaka"

**Câu hiện tại (dòng 181):**
> "…không bi ký nào gắn với ông ghi niên đại Śaka, nên niên đại để Thấp và toàn bộ khung trị vì là cổ tự học cộng đếm ngược từ Īśānavarman I."

Vickery 1994 nói ngược, và nói về đúng một trong ba bi ký mục nêu: Coedès "**took the date 598 from inscription K151** which seems to associate Bhavavarman with that region". Tức K.151 **có** một niên đại đọc ra được 598 CN. (Vickery phản đối cách Coedès *dùng* con số ấy — nhét nó vào một đoạn Mã Đoan Lâm bị cắt khỏi ngữ cảnh — chứ không phản đối việc bi ký có niên đại.)

Hệ quả: lý do giải thích cho mức `Thấp` là **sai**, dù bản thân mức `Thấp` vẫn nên giữ (Heng & Lavy chỉ dám viết "around 550–600"; Vickery chỉ dám viết "probably around 600").

**Câu thay thế (viết sẵn):**
> "…niên đại để Thấp vì khung trị vì phần lớn là cổ tự học cộng đếm ngược từ Īśānavarman I: con số 598 mà Coedès rút từ K.151 là mốc duy nhất, và chính Vickery cho thấy Coedès đã dùng nó sai ngữ cảnh."

#### 1c. BẮT BUỘC — địa lý của ba bi ký được nêu

**Câu hiện tại (dòng 179) và trường `nơi:`:**
> "…trong một nhóm văn bản ngắn rải từ bắc Campuchia qua đông bắc Thái Lan tới nam Lào — K.151 ở Robaṅ Romãs nêu ông…, K.439 gắn ông với thần Gambhireśvara, K.53 nhắc lại ông trong một văn bản hồi cố năm 667"
>
> `nơi: trung lưu Mekong và chân núi Dangrek, nay thuộc Campuchia, đông bắc Thái Lan và nam Lào`

**Không bi ký nào trong ba cái được nêu nằm ở đông bắc Thái Lan hay nam Lào.**

- **K.151 và K.439 đều ở Sambor Prei Kuk (Īśānapura), tỉnh Kompong Thom, miền trung Campuchia.** Heng & Lavy liệt "Robang Romeas Complex" là **mục số 4 trong bản đồ lõi Sambor Prei Kuk**, và xếp K.151 cùng K.439 vào nhóm bi ký của "four regional governors… [who] endowed smaller temples **in Ishanapura**".
- **K.53 ở Ba Phnom**, tỉnh Prey Veng, **đông nam** Campuchia (hạ lưu Mekong) — Vickery 1994: "K53 from Ba Phnom, dated AD 667".

Cả ba đều nằm trong lãnh thổ Campuchia ngày nay, hai cái ở miền trung và một ở đông nam. Phạm vi "bắc Campuchia → đông bắc Thái Lan → nam Lào" được gán cho một nhóm bi ký không gồm cái nào như vậy.

**Và đây là chỗ nặng nhất: trường `nơi:` tái dựng đúng cái bức tranh mà bài được dẫn tồn tại để phá.** Xem mục (2) ngay dưới.

**Câu thay thế cho thân mục (viết sẵn):**
> "…trong một cụm bi ký Phạn ngữ ngắn do ông và anh em ông để lại ở cả hai phía dãy Dangrek — K.151 và K.439 ở Sambor Prei Kuk thuộc Kompong Thom, K.53 ở Ba Phnom thuộc Prey Veng. K.439 cho thấy vị thần chính của nhóm đền phía bắc Sambor Prei Kuk là một dạng Śiva tên Gambhireśvara, vị thần mà giới nghiên cứu thấy gắn riêng với ông; K.53, văn bản hồi cố năm 667, xếp ông thứ hai trong một danh sách năm vua."

**Trường `nơi:` thay thế (viết sẵn):**
> `nơi: lưu vực Mekong ở Campuchia, từ Sambor Prei Kuk (Kompong Thom) tới Ba Phnom (Prey Veng)`

#### 1d. KHÔNG CÓ LỖI — K.439 và Gambhireśvara

Heng & Lavy, nguyên văn: "Epigraphic evidence (including **K. 439**) indicates that the principal deity of the northern group (Group N) was a form of Shiva named **Gambhireshvara** ('Lord of the Depths'), a god that **seems to have been particularly associated with King Bhavavarman I**." ✓ Mục viết đúng. Chỉ nên giữ sắc thái "seems to" — nguồn có rào, mục thì không.

#### 1e. KHÔNG CÓ LỖI — K.53 là văn bản hồi cố năm 667

Vickery 1994: "K53 from Ba Phnom, **dated AD 667**", "the inscriptions which **retrospectively** bridge the so-called Funan-Chenla transition". ✓ Mục viết đúng từng chữ.

#### 1f. CÂN NHẮC — "K.151… nêu ông trong một chuỗi ba vua"

**[KHÔNG KIỂM ĐƯỢC].** Hai nguồn được dẫn đều không nói K.151 chứa một chuỗi ba vua: Heng & Lavy mô tả K.151 là bi ký của một **quan trấn nhậm** dâng cúng đền nhỏ ở Īśānapura; Vickery chỉ nói K.151 "seems to associate Bhavavarman with that region" và có niên đại 598. Danh sách **năm** vua là của **K.53**, không phải K.151. Nếu không mở được ấn bản bi ký (Coedès, *IC*), không nên viết "chuỗi ba vua" như sự kiện.

### (2) Quy tắc 7 — nguồn bị dẫn ngược chính nó

**Có, và là ca rõ nhất trong cả bốn mục.**

Bài Vickery 1994 mà mục dẫn tồn tại để **bác bỏ** cách định vị địa lý mà mục đang dùng. Mở bài, Vickery nêu đúng mệnh đề ấy để đánh đổ nó:

> "There has been a traditional consensus that Chenla was centered in **Champassak in southern Laos**, or even farther north, and it has even been said that '…dans la seconde moitié du VIe siècle…il occupait **la vallée de la Se Moun** et une partie…du **Cambodge septentrional**' (Jacques, 1986: 61). The inscriptions to which reference is made are those of the **Dangrek chieftains, Vīravarman, Bhavavarman, and Mahendravarman**. But they in fact make no reference to Chenla at all… and **they themselves are not at all evidence for the existence of Chenla in their area**."

Kết luận của bài thì ngược hẳn:

> "The most significant aspect of Jacques' new readings is the indication that **the original home area of these two kings as well as their father Vīravarman was within Cambodia south of the Dangrek mountains**."
>
> "With the careers of **Bhavavarman I and Citrasena, and their father Vīravarman, placed firmly within Cambodia south of the Dangrek**… The 'Dangrek chieftains' were indeed conquerors… but **not of the south (Funan) by the north (Chenla), rather in the other direction**."

"la vallée de la Se Moun" chính là đông bắc Thái Lan; "Champassak" chính là nam Lào; "Cambodge septentrional" chính là bắc Campuchia. Trường `nơi:` của mục liệt **cả ba**, và thân mục lặp lại cùng ba vùng ấy — tức atlas đang chép lại nguyên văn bức tranh Coedès–Jacques trong khi dẫn bài phá bức tranh đó làm nguồn. Đây đúng hình dạng lỗi quy tắc 7.

Phải nói cho công bằng: Vickery có viết rằng các ông hoàng này để lại "short Sanskrit inscriptions **north and south of the Dangrek mountains**", nên một corpus rộng hơn thì đúng là trải qua dãy Dangrek. Cái sai là (a) gán phạm vi ấy cho **ba bi ký cụ thể** không cái nào ở đó, và (b) đặt **nơi hoạt động chính** của ông ở vùng mà nguồn kết luận là *không* phải quê gốc của ông.

**Phần ghi chú biên tập đã rào đúng một nửa.** Khối "Chân Lạp chinh phục Phù Nam là câu không được viết" cảnh báo rất chuẩn về việc đừng dùng "Funan Reviewed" ngược chiều. Nhưng cảnh báo ấy dừng ở mệnh đề *chinh phục*, trong khi lỗi thực tế nằm ở mệnh đề *địa lý* — và nằm ngay trong mục.

**Kiểm thư mục của cả hai nguồn:**

- **Vickery 1994 — ĐÚNG hoàn toàn.** Trang 1 của chính PDF ghi: "'What and Where was Chenla?', *Recherches nouvelles sur le Cambodge*. Publiées sous la direction de **F. Bizot**. **École française d'Extrême-Orient**, Paris, **1994**, pp. **197-212**." Trùng từng chi tiết với dòng `**Nguồn:**`, kể cả tên chủ biên và số trang. ✓ URL `michaelvickery.org/vickery1994what.pdf` trả 200 / 205.860 byte PDF thật. ✓
- **Heng & Lavy — ĐÚNG.** Tiêu đề trang đầu PDF: "PIPHAL HENG & PAUL A. LAVY — Pre-Angkorian cities: Ishanapura and Mahendraparvata". ✓ URL trả 200 / 998.294 byte PDF thật. ✓ **Thiếu dữ liệu xuất bản** (sách/tạp chí nào, năm nào, trang nào) — NÊN bổ sung, vì hiện chỉ có một URL trần.

### (3) Quy tắc 8 — liên kết và mức bằng chứng

| Dòng | Đích | Đánh giá |
|---|---|---|
| `Kế thừa từ: Truyền thống bi ký Phạn ngữ và vương quyền Śaiva Nam Á · kế thừa · trực tiếp` | mô tả | **Đúng.** K.439/Gambhireśvara đỡ được phần Śaiva; toàn bộ cụm bi ký là Phạn ngữ. |
| `Ảnh hưởng tới: Īśānavarman I và kinh đô Īśānapura (Sambor Prei Kuk) · kế thừa · trực tiếp` | mô tả | **Đúng, và có nguồn**: Heng & Lavy viết K.151, K.53, K.439 "imply that the foundation of this city should **perhaps** be associated with Bhavavarman I". Lưu ý nguồn rào bằng "perhaps", và giữa hai người còn có Mahendravarman (Vickery: sau khi Bhavavarman I chết "probably around 600", Mahendravarman tiếp quản và cũng đóng ở Sambor Prei Kuk). Mức `trực tiếp` vẫn đứng được vì là kế tục triều đại liền kề, nhưng nếu muốn chặt thì `qua trường phái` cũng đỡ được. |
| `Ảnh hưởng tới: Vương quyền Angkor · kế thừa · qua trường phái` | mô tả | **Đúng mức**, rào hợp lý. |

**Mục này không có liên kết nào trỏ sang ID của mục khác** (cả `Kế thừa từ` lẫn `Ảnh hưởng tới` đều là mô tả văn xuôi), nên **không thể có lỗi trỏ nhầm người ở đây**. Nói thẳng: quy tắc 8 **không có lỗi**. Đổi lại, mục bị cô lập hoàn toàn khỏi phần còn lại của atlas — không phải lỗi, nhưng đáng biết.

### (4) Chi tiết viết như sự kiện mà không truy được về nguồn

1. **"chuỗi ba vua" trong K.151** — xem 1f. [KHÔNG KIỂM ĐƯỢC].
2. **"rải từ bắc Campuchia qua đông bắc Thái Lan tới nam Lào"** — xem 1c. Không nguồn nào được dẫn đặt ba bi ký ấy ở đó; nguồn được dẫn đặt chúng ở Kompong Thom và Prey Veng.
3. **"không bi ký nào gắn với ông ghi niên đại Śaka"** — xem 1b. Nguồn được dẫn nói ngược.
4. **"Mô hình ông để lại là mô hình tồn tại: vua Hindu hóa dùng Phạn ngữ làm ngôn ngữ bi ký và Śiva làm thần bảo trợ, chính là khuôn mà Īśānapura rồi Angkor kế tục."** — mệnh đề tổng hợp, không nguồn nào được dẫn phát biểu nó. Đỡ được một phần (K.439/Gambhireśvara là Śaiva; Heng & Lavy nối K.151/K.53/K.439 với việc lập Īśānapura), nhưng cái khung "khuôn mà Angkor kế tục" là suy diễn của người viết. CÂN NHẮC — nên hạ giọng thành "cái khuôn ấy còn nhận ra được ở Īśānapura và về sau ở Angkor".

### (5) Rà khối ghi chú biên tập "'Chân Lạp chinh phục Phù Nam' là câu không được viết"

| | Mệnh đề | Kết quả |
|---|---|---|
| **A** | "Vickery 1994 tháo rời mệnh đề ấy từ chính nguồn sơ cấp" | **ĐÚNG.** Nguyên văn: "the inscriptions which retrospectively bridge the so-called Funan-Chenla transition **do not indicate a political break at all**"; và về K.44 (674 CN): "again there is no suggestion of political discontinuity". ✓ |
| **B** | "'Chân Lạp' với 'Phù Nam' phần lớn là **phạm trù của thư tịch Trung Hoa**, không phải tên mà người tại chỗ tự gọi" | **ĐÚNG.** Vickery: "**no inscriptions refer to Chenla at all**"; "Coedès **accepted the Chinese framework** and erected on the very terse inscriptions of the Dangrek chieftains an impressive edifice about the conquest of Funan by Chenla." ✓ |
| **C** | "Mục `CH05-CE06-11` vì vậy **chỉ giữ đúng một luận điểm**" | **Đúng về hình thức, nhưng luận điểm duy nhất ấy lại là luận điểm sai** — xem 1a. Việc thu gọn xuống một mệnh đề không bảo vệ được gì nếu mệnh đề ấy không được kiểm. |
| **D** | Cảnh báo quy tắc 7: bài "Funan Reviewed: Deconstructing the Ancients" **phá** khái niệm Phù Nam như một đế quốc, nên không dùng nó để đỡ cho câu "Phù Nam là đế quốc hàng hải hùng mạnh bị Chân Lạp đánh bại" | **ĐÚNG, và thư mục kiểm được**: Michael Vickery, "Funan Reviewed: Deconstructing the Ancients", *BEFEO* **90–91 (2003), tr. 101–143**, doi **10.3406/befeo.2003.3609** — đọc từ trang đầu của chính PDF. ✓ Cảnh báo này nên giữ nguyên. **Bổ sung đáng kể:** chính bài ấy chứa phản chứng cho mệnh đề trung tâm của mục (K.5, K.40, K.875). Khối ghi chú nên nói thêm điều đó. |
| **E** | "Goodall & Revire đặt thẳng câu hỏi có bao nhiêu vua tên Bhavavarman trong bi ký Campuchia thế kỷ 6–7, nên việc gán một bi ký không niên đại cho 'Bhavavarman I' tự nó đã là một phán đoán cổ tự học" | **Thư mục ĐÚNG**: Dominic Goodall & Nicolas Revire, "East and West — New Inscriptions from Funan, Zhenla and Dvāravatī", *BEFEO* **107 (2021), tr. 257–301**, doi **10.3406/befeo.2021.6376**, bản OA xanh tại HAL `halshs-04142364` (kiểm qua OpenAlex 200 / 328.257 byte). Nội dung mệnh đề: xem phần bổ sung bên dưới nếu đã kiểm xong, nếu không thì **[KHÔNG KIỂM ĐƯỢC]**. Riêng **suy luận** của khối thì vững không phụ thuộc vào đó: Vickery 1994 độc lập cho thấy có ít nhất **Bhavavarman II** (K.1150, em của Śivadatta, con Īśānavarman I), tức tên "Bhavavarman" đúng là dùng cho nhiều hơn một vua. ✓ |
| **F** | "Đông Nam Á **không còn ở 0,0%**" (khối "Hai đính chính") | **ĐÚNG**, và khối "Đông Nam Á ở lại **0,5%**" cũng đúng: tính lại trên `data/persons.json`, atlas chính (trừ CH90) có **221** người, Đông Nam Á có **1** = **0,45%** → làm tròn 0,5%. ✓ Mục Đông Nam Á duy nhất ấy đúng là `CH05-CE06-11`, nên câu "Đây là mục Đông Nam Á đầu tiên của atlas chính" trong `**Vì sao chọn**` cũng **đúng**. ✓ |

**Câu bổ sung cho khối D (viết sẵn):**
> "Và phải đọc bài ấy theo chiều ngược lại nữa: chính 'Funan Reviewed' là chỗ ghi rằng bi ký Phạn ngữ tại chỗ ở hạ lưu Mekong đã nêu tên Gunavarman (K.5, đầu thế kỷ 5), rồi Jayavarman và con là Rudravarman (K.40, chữ giữa thế kỷ 6, tìm ở Tonle Bati cách Phnom Penh 30 km tây nam). Vì vậy **không được viết rằng Bhavavarman I là vị vua sớm nhất ở lưu vực Mekong được bi ký Phạn ngữ tại chỗ định danh** — ông không phải."

### Kết luận `CH05-CE06-11`

**Đây là mục có vấn đề nặng nhất trong bốn mục.** Không phải vì nguồn giả — cả hai URL trong `**Nguồn:**` đều sống, đều là PDF thật, và thư mục Vickery 1994 thì chép đúng đến từng chi tiết. Vấn đề là **mục nói ngược với nguồn nó dẫn, ở ba chỗ cùng lúc**: mệnh đề mở đầu (vị vua sớm nhất), lý do để niên đại Thấp (không bi ký nào có niên đại), và địa lý (ba vùng mà bài Vickery tồn tại để bác).

Lỗi quy tắc 7 ở đây **rõ hơn** ca Sinor ở `CH05-CE06-10`: ở mục Bumin, một chuyên gia bị nêu sai lập trường; ở đây, atlas tái dựng nguyên bức tranh Coedès–Jacques về "các tù trưởng Dangrek" trong khi dẫn làm nguồn chính bài báo bác bức tranh ấy.

Quy tắc 8 thì **không có lỗi** — mục không có liên kết ID nào.

Hai chi tiết nhỏ nhưng đúng và nên giữ nguyên: K.439 ↔ Gambhireśvara, và K.53 là văn bản hồi cố năm 667.

---

## Rà các khối `## Ghi chú biên tập` bàn về nhóm CE06 (phần liên-mục)

Mười một khối trong `## Ghi chú biên tập` bàn về nhóm CE06. Sáu khối đã rà trong từng mục ở trên (Bumin ×1, Kaleb ×1, Bhavavarman ×1, Boethius ×2, HTTP 200 ×1). Năm khối còn lại rà ở đây.

### N1. "Bốn vùng, và chỗ atlas vừa hết số không" — ĐÚNG

Đếm lại bằng `data/persons.json` (atlas chính = 221 người, trừ CH90):

| Vùng | Số | % |
|---|---|---|
| Trung Đông/Bắc Phi | 73 | 33,03% |
| Châu Âu | 59 | 26,70% |
| Đông Á | 54 | 24,43% |
| Nam Á | 26 | 11,76% |
| Châu Phi hạ Sahara | 4 | 1,81% |
| **Trung Á** | **2** | **0,90%** |
| Châu Mỹ | 2 | 0,90% |
| **Đông Nam Á** | **1** | **0,45%** |
| Châu Đại Dương | 0 | 0,00% |

- "`CH05-CE06-11` Bhavavarman I là **mục Đông Nam Á đầu tiên của atlas chính**" ✓ — đúng, và vẫn là **duy nhất**.
- "trước mục này con số thật của Đông Nam Á là 0,0%" ✓.
- "chỉ còn Châu Đại Dương ở số không" ✓ — Châu Đại Dương không xuất hiện lần nào.
- "Vòng kiểm đề nghị **nếu phải bỏ một người thì bỏ ông trước**" — vòng kiểm này **không** đưa ra đề nghị đó, nhưng xác nhận mục mỏng và nay thêm: mục còn **nói ngược nguồn ở ba chỗ** (xem `CH05-CE06-11`). Khuyến nghị của vòng này là **sửa, không bỏ**: cái thật — K.439/Gambhireśvara, K.53 năm 667, cụm bi ký Phạn ngữ của một triều đại nội địa — đủ để giữ mục.

### N2. "Wikidata sai ở cả bốn ứng viên nhóm này" — HAI ĐÚNG, HAI SAI

Đã mở `Special:EntityData/<Q>.json` cho cả năm Q-ID (mỗi cái HTTP **200**, cỡ ghi trong bảng), đọc thẳng `claims` thô:

| Q-ID | Khối ghi chú nói | Dữ liệu thật | Kết |
|---|---|---|---|
| Q854920 (13.487 B) | "ghi **sinh 600 và mất 600**" → "vô nghĩa" | P569 `+0600` **precision 7 (thế kỷ)**, có **1 reference**; P570 `+0600` precision 9, có 1 reference | **SAI** |
| Q29001 (27.534 B) | "sinh 490 **không nguồn**" | P569 `+0490` precision 9, **refs = 0** | **ĐÚNG** ✓ |
| Q705378 (25.273 B) | "sinh **k. 450 không nguồn**" | P569 `+0450` **precision 7 (thế kỷ)**, **có 1 reference**; cái không nguồn là **P570 `+0540`, refs = 0** | **SAI, và ngược** |
| Q8046995 (12.225 B) | "hai giá trị P570 — 603 normal và 593 deprecated" | đúng y như vậy | **ĐÚNG** ✓ |
| Q102851 (218.884 B) | (khối Boethius) "480–524 là cặp số Wikidata để ở **rank preferred**" | P569 `+0480` prec 9 **preferred** (9 refs); P570 `+0524` prec 9 **preferred** (3 refs); song song có P569 `+0475` prec 8 và P570 `+0525` prec 8 ở rank normal | **ĐÚNG hoàn toàn** ✓ |

**BẮT BUỘC — Q854920.** Giá trị thô đúng là `+0600` ở cả hai, nhưng P569 ở **độ chính xác thế kỷ**, nên Wikidata không hề nói "sinh năm 600 và mất năm 600". Kết luận "vô nghĩa" vì thế không đứng. Trớ trêu là chính atlas có một khối khác (`Wikidata khai độ chính xác, nó không khai độ tin cậy`) dạy đúng cách đọc này.

**Câu thay thế (viết sẵn):**
> "Q854920 (Bhavavarman) để P569 ở **độ chính xác thế kỷ** rồi P570 ở độ chính xác năm trên cùng giá trị thô `+0600` — đọc ẩu thành 'sinh 600, mất 600' là rơi đúng cái bẫy độ chính xác mà atlas đã ghi ở khối dưới;"

**BẮT BUỘC — Q705378.** Nói ngược: P569 (`+0450`, thế kỷ) **có** reference, P570 (`+0540`) thì **không**.

**Câu thay thế (viết sẵn):**
> "Q705378 (Kaleb) để P569 ở độ chính xác thế kỷ và có nguồn, nhưng **năm mất 540 thì không có reference nào**;"

**Hệ quả cho kết luận của khối.** Câu "khớp Wikidata là sàn, không phải trần" vẫn đúng, nhưng chứng cứ đỡ nó chỉ còn **hai trong bốn** ca. Nên sửa "sai ở cả bốn" thành "phải đọc kỹ ở cả bốn".

### N3. "Nhóm CE06: một ứng viên bị loại…" (Yajaw Teʼ Kʼinich II) — KHÔNG KIỂM TRONG VÒNG NÀY

Khối này bàn một ứng viên **bị loại**, không phải nội dung đã xuất bản về bốn người được giao. Phần Wikidata của nó (Q8046995, hai giá trị P570) đã kiểm ở N2 và **đúng**. Các mệnh đề về Simon Martin, Caracol Altar 21, Chase & Chase 2020 tr. 35 và phép quy đổi 9.9.18.16.3 → 631/633: **[KHÔNG KIỂM ĐƯỢC]** trong vòng này — ngoài phạm vi bốn mục được giao, và chưa mở nguồn nào.

### N4. "Một câu hỏi thủ tục đã được quyết" (Tì-ni-đa-lưu-chi) — KHÔNG KIỂM

Đây là phán quyết thủ tục nội bộ của dự án về quy tắc 6, không phải mệnh đề sự kiện lịch sử. Phần kiểm được: `Q4111528` có thật và được dùng ở `CH90-CE01_09-04` — kiểm bằng `data/persons.json`. ✓ Phần còn lại là chính sách, không thuộc phạm vi kiểm sự kiện.

### N5. "Hai đính chính cho chính ghi chú này, và năm cái bẫy URL mới"

| | Mệnh đề | Kết quả |
|---|---|---|
| a | "Đông Nam Á **không còn ở 0,0%**" | **ĐÚNG** ✓ — 1/221 = 0,45%. |
| b | "Nghệ thuật/Kiến trúc **không còn trống**" | Không kiểm lại độc lập (thuộc nhóm CE07). |
| c | "**Lý Xuân, người được gán cho cầu An Tế, không có thực thể Wikidata nào là người**" | **ĐÚNG theo mức kiểm được** ✓ — `wbsearchentities` cho 李春 (HTTP 200) trả về 10 kết quả, toàn người đời Minh/Đường trong CBDB cộng một diễn viên Hàn Quốc và một chính khách; không có ai là thợ cầu đời Tùy. Vẫn nên hiểu là "không tìm thấy", không phải "chứng minh không tồn tại". |
| d | "`Q551446` **không có cả P84 lẫn P170**, và P571 ghi **606**" | **ĐÚNG từng chi tiết** ✓ — kiểm trực tiếp JSON (200 / 20.496 B): P84 vắng, P170 vắng, P571 = `+0606` precision 9, refs = 0. |
| e | Năm cái bẫy URL mới (ctext 200/2.781 B, JSTOR 200/3.038 B "Client Challenge", Brill 202/0 B, Wikisource 404 có `<title>` giống trang thật, Britannica/Iranica 403) | Không kiểm lại từng cái trong vòng này; **cùng loại hiện tượng thì vòng này gặp lại** — xem N6. |

### N6. Đính chính cho khối "HTTP 200 không có nghĩa là đọc được"

**Câu hiện tại:**
> "trong một vòng đã gặp **bốn** URL trả 200 mà không có nội dung — **HAL và DASI trả trang chặn bot**, JSTOR trả một landing page 3 KB, một thread diễn đàn trả 202."

**Nửa về HAL nay sai.** Với đúng User-Agent chung `history-atlas/0.1 (research)`, `hal.science/halshs-04142364v1/document` trả **200 / 2.549.302 byte / PDF thật 50 trang**, và `shs.hal.science/halshs-04142364/document` trả **200 / 2.063.865 byte / PDF thật 50 trang**. HAL **không** chặn bot.

**Nửa về DASI thì nay còn tệ hơn mô tả:** `dasi.cnr.it/csai-epi-2416` và cả `dasi.cnr.it/` trả **000 / 0 byte** — không phải trang chặn bot mà là **không kết nối được**.

**Và vòng này tìm ra một cái bẫy mới, nguy hiểm hơn cả năm cái ở N5e — đã truy ra tận gốc.** Cùng một URL HAL, cùng một lệnh, trả về **kích thước khác nhau mỗi lần kéo**: 2.549.302 B, rồi 4.175.578 / 2.650.112 / 2.063.865 / 1.662.976 / 3.248.128 B. `pypdf` từ chối mọi bản bằng `PdfStreamError: Stream has ended unexpectedly`.

Gốc của vấn đề tìm được bằng một yêu cầu **HEAD**:

```
HTTP/2 200
content-length: 10911072
content-type: application/pdf
```

**File thật nặng 10.911.072 byte.** Mọi lần kéo đều đứt ở một chỗ ngẫu nhiên giữa chừng, và **`curl` vẫn thoát với mã 0**, không báo lỗi gì. Máy chủ **không trả `accept-ranges`**, nên `curl -C -` (tải tiếp) lại càng tệ: nó nối thêm dữ liệu vào sai vị trí và cho ra một file **lớn hơn cả bản thật** (3.184.228 B) mà vẫn hỏng.

Bài học cụ thể, nên đưa thẳng vào CONTRIBUTING: **so kích thước tải về với `content-length` lấy từ HEAD**, đừng so với lần kéo trước; mã 200 cộng kích thước khác 0 cộng `curl` thoát 0 **vẫn chưa chứng minh được gì**. Với PDF, phép kiểm cuối cùng là mở được bằng thư viện và đủ số trang.

**Câu thay thế (viết sẵn):**
> "trong một vòng đã gặp **bốn** URL trả 200 mà không có nội dung — DASI nay còn không kết nối được (000 / 0 byte), JSTOR trả một landing page 3 KB, một thread diễn đàn trả 202. **Đính chính:** HAL **không** chặn bot — với User-Agent chung `history-atlas/0.1 (research)` nó trả PDF thật 50 trang. Nhưng HAL cho một cái bẫy khác và tinh vi hơn: cùng một URL trả 200 với **kích thước khác nhau mỗi lần kéo**, phần lớn là file cắt dở mà `pypdf` không mở được. Với PDF, phép kiểm phải là **mở được và đủ số trang**, không phải mã trạng thái cộng kích thước."

### N7. BẮT BUỘC — "Trung Á vì vậy vẫn ở đúng một người" nay sai

**Câu hiện tại (khối Boethius, dòng 668):**
> "Trung Á vì vậy vẫn ở đúng một người."

**Sai tại thời điểm kiểm.** `data/persons.json` cho Trung Á = **2** người: `CH02-BCE06-09` (Zarathustra) và `CH05-CE08-01` (Abu Muslim). Chính một khối ghi chú khác trong cùng file đã ghi điều này: "Trung Á và Châu Mỹ lần đầu nhúc nhích, **từ 1 lên 2 người mỗi ô**."

Đây là lỗi kiểu mục này chạy đua với mục khác trong cùng file: câu được viết khi Trung Á còn 1 người, rồi mục `CH05-CE08-01` vào dữ liệu và làm nó sai mà không ai chạm vào câu.

**Câu thay thế (viết sẵn):**
> "Việc không chọn Maniakh vì vậy không mở thêm được ô Trung Á ở nhóm này; ô ấy chỉ nhúc nhích ở nhóm CE08, với Abu Muslim `CH05-CE08-01`."

### N8. NÊN — "Châu Âu đang ở 26,9%"

**Câu hiện tại (khối Boethius, dòng 668):**
> "lựa chọn này **không có lợi** cho thống kê vùng — Châu Âu đang ở 26,9% và mục này đẩy nó lên."

Số không khớp ở cả hai cách đọc: **sau** khi thêm Boethius, Châu Âu = 59/221 = **26,70%**; **trước** khi thêm, = 58/220 = **26,36%**. Không có mốc nào cho 26,9%.

Lập luận thì **vẫn đúng** — thêm một người châu Âu đúng là đẩy tỷ lệ châu Âu lên (26,36% → 26,70%). Chỉ con số là sai. Và vì các nhóm khác vẫn đang được thêm trong cùng phiên, mọi con số phần trăm viết cứng trong ghi chú sẽ còn tiếp tục trôi.

**Câu thay thế (viết sẵn):**
> "lựa chọn này **không có lợi** cho thống kê vùng — Châu Âu đã là ô lớn thứ hai của atlas, trên một phần tư tổng số, và mục này đẩy nó lên thêm."

Khuyến nghị kèm theo: **đừng viết tỷ lệ phần trăm cứng vào `## Ghi chú biên tập`** khi script `atlaslib` tính được chúng; mọi con số cứng đều có tuổi thọ bằng đúng khoảng cách tới mục tiếp theo.

### N9. CÂN NHẮC — "qua lăng kính Tân Plato, và lăng kính đó là của ông"

**Câu hiện tại (khối "Bốn điều không được viết về Boethius"):**
> "Tức châu Âu trung cổ đọc Aristotle **qua lăng kính Tân Plato**, và lăng kính đó là của ông."

Nửa đầu có nguồn đỡ (Boethius truyền bộ *Organon* kèm chú giải trong truyền thống Porphyry, và ông lặp lại tham vọng hoà giải Plato–Aristotle). Nửa sau — **lăng kính đó là của ông** — thì quá mạnh: lăng kính ấy là của Porphyry và trường phái Tân Plato muộn; Boethius là **người chuyển**, đúng như chính atlas đã mô tả ông ở `CH04-CE03-03` bằng chữ "qua Boethius". Gán quyền sở hữu cái lăng kính cho người chuyển là mâu thuẫn với cách atlas đã định vị ông ở chỗ khác.

**Câu thay thế (viết sẵn):**
> "Tức châu Âu trung cổ đọc Aristotle **qua lăng kính Tân Plato** — lăng kính của Porphyry, nhưng mài và lắp bởi ông."

---

# Tổng hợp cuối — xếp theo mức

Ký hiệu: **[M]** = sửa trong thân mục `content/ch05.md`; **[G]** = sửa trong `## Ghi chú biên tập`; **[N]** = sửa dòng `**Nguồn:**`; **[R]** = sửa dòng quan hệ (cần sửa đối xứng ở cả hai file).

## BẮT BUỘC — sai sự kiện, phải sửa

| # | Mục | Câu hiện tại (nguyên văn, rút gọn) | Sai ở đâu | Câu thay thế |
|---|---|---|---|---|
| **B1** | `CH05-CE06-11` **[M]** | "Ông là vị vua sớm nhất ở lưu vực Mekong được chính bi ký Phạn ngữ tại chỗ định danh" | Chính Vickery — tác giả mục dẫn — ghi bi ký Phạn ngữ tại chỗ sớm hơn: K.5 (đầu thế kỷ 5, Gunavarman), K.40 (Tonle Bati, Jayavarman và Rudravarman), và K.53 mà mục tự dẫn thì mở danh sách vua **bằng Rudravarman** | "Ông là vị vua đầu tiên của vùng nội địa Campuchia để lại một cụm bi ký Phạn ngữ tại chỗ đủ để dựng lại một triều đại — trước ông, bi ký tại chỗ ở hạ lưu Mekong chỉ cho tên rời rạc của vài vua Phù Nam như Gunavarman, Jayavarman và Rudravarman." |
| **B2** | `CH05-CE06-11` **[M]** | "trong một nhóm văn bản ngắn rải từ bắc Campuchia qua đông bắc Thái Lan tới nam Lào — K.151… K.439… K.53" + `nơi: trung lưu Mekong và chân núi Dangrek, nay thuộc Campuchia, đông bắc Thái Lan và nam Lào` | Không bi ký nào trong ba cái ở Thái Lan hay Lào: K.151 và K.439 ở Sambor Prei Kuk (Kompong Thom), K.53 ở Ba Phnom (Prey Veng) | thân mục: "…trong một cụm bi ký Phạn ngữ ngắn do ông và anh em ông để lại ở cả hai phía dãy Dangrek — K.151 và K.439 ở Sambor Prei Kuk thuộc Kompong Thom, K.53 ở Ba Phnom thuộc Prey Veng."; trường: `nơi: lưu vực Mekong ở Campuchia, từ Sambor Prei Kuk (Kompong Thom) tới Ba Phnom (Prey Veng)` |
| **B3** | `CH05-CE06-11` **[M]** | "không bi ký nào gắn với ông ghi niên đại Śaka, nên niên đại để Thấp" | Vickery: Coedès "took the date **598** from inscription K151" | "…niên đại để Thấp vì khung trị vì phần lớn là cổ tự học cộng đếm ngược từ Īśānavarman I: con số 598 mà Coedès rút từ K.151 là mốc duy nhất, và chính Vickery cho thấy Coedès đã dùng nó sai ngữ cảnh." |
| **B4** | `CH05-CE06-12` **[M]** | "cho tới làn sóng dịch từ tiếng Ả Rập thế kỷ 12, Aristotle của Boethius chính là Aristotle ở phương Tây" | Sai đường truyền (phần còn lại của *Organon* đến qua chính bản dịch Latinh của Boethius được tìm lại) và sai mốc (SEP: bản dịch của ông "remained standard throughout the Middle Ages"); `Arabic` xuất hiện **0 lần** trong bài SEP được dẫn | "Lựa chọn ấy quyết định Tây Âu có thể nghĩ bằng cái gì trong hơn sáu thế kỷ sau đó: tới thế kỷ 11 chương trình logic Latinh gồm đúng hai tác phẩm Aristotle cộng Porphyry và chính Boethius — bộ *logica vetus* — và phải tới đầu thế kỷ 13 phần còn lại của *Organon* mới lưu hành rộng, phần lớn vẫn qua chính các bản dịch Latinh của ông được tìm lại." |
| **B5** | `CH05-CE06-12` **[R]** | `CH04-CE03-03 · kế thừa · trực tiếp` (và dòng đối xứng ở `ch04.md`) | Porphyry mất k. 305, Boethius sinh k. 477 — cách ~172 năm, vượt cả ca 130 năm mà quy tắc 8 nêu đích danh; commit `045c86d` đã **nâng** mức từ `qua trường phái` lên `trực tiếp` mà không thêm bằng chứng nào; và cùng mục lại chấm Aristotle là `qua trường phái` cho đúng loại quan hệ ấy | `ch05.md`: `- CH04-CE03-03 · kế thừa · qua trường phái` · `ch04.md`: `- CH05-CE06-12 · kế thừa · qua trường phái` |
| **B6** | `CH05-CE06-10` **[M]** | "mọi chinh phục thường bị gán cho ông — diệt Nhu Nhiên, phá Hiệt Đát, mở đường tới Byzantium — chính văn đều chép dưới tên Mộc Hãn khả hãn" | Sai cả ba: Nhu Nhiên do chính Bumin đánh (chính mục nói thế ở câu trước); Byzantium **chính sử Trung Hoa không chép một dòng nào**, và Sinor gán hai sứ đoàn cho Askel/Silziboulos; Hiệt Đát thì Sinor gán cho **Ishtemi** | "Ông làm khả hãn nhiều nhất một năm, nên hầu hết những gì thường được gán cho ông thì chính văn lại chép dưới tên người khác: Chu thư và Bắc sử đặt việc diệt nốt tàn dư Nhu Nhiên (鄧叔子) và phá Hiệt Đát dưới tên Mộc Hãn khả hãn, sau khi ông chết; còn việc mở đường tới Byzantium thì chính sử Trung Hoa không chép một dòng nào — hai sứ đoàn 563 và 568 chỉ được biết qua Menander Protector, và đều thuộc cánh Tây chứ không thuộc ông." |
| **B7** | `CH05-CE06-09` **[M]** | "tiền đúc mang tên ông là bằng chứng vật chất rằng quân Aksum có mặt thật ở Nam Arabia, **độc lập với mọi nguồn Kitô giáo**" | Mục từ "Kālēb" chứa `coin` **0 lần**; mục "Aksum" có 1 lần nhưng về `ABACCIN` k. 400, không liên quan. Và bi ký Geʿez ở Yemen **trích Isaiah và Thi thiên**, nên không "độc lập với mọi nguồn Kitô giáo" | "Các bi ký Geʿez do quân Aksum khắc ngay tại Maʾrib và Ẓafār, cộng hai bi ký Sabaic (`Ist 7608 bis`, `Wellcome A 103664`) do người tại chỗ khắc mà khấn 'các chúa của họ, những vua Aksum', là bằng chứng vật chất tại chỗ rằng quân Aksum có mặt thật ở Nam Arabia — độc lập với các hagiography Hy Lạp và Syriac." |
| **B8** | Ghi chú CE06 **[G]** | "Denis Sinor nêu đích danh và **bác** cách hiểu này ['chia đôi hãn quốc cho em là Istämi']" | Sinor & Klyashtorny tr. 327 **khẳng định** cả hai vế: Istämi là em Bumin, và đế quốc "bicephalous almost from the moment of its inception" | "Thứ nhất, 'Bumin chia đôi hãn quốc cho em là Istämi': phải tách làm hai mệnh đề. Sinor và Klyashtorny (tr. 327) **xác nhận** Istämi là em Bumin và hãn quốc có hai đầu 'gần như ngay từ lúc khai sinh' — nhưng việc chia ấy xảy ra **sau khi Bumin và con cả ông là 科羅 đã chết**, và là giữa con ông là Mộc Hãn với em ông, chứ không phải một sự phân phong do chính Bumin thực hiện. Còn sự **đứt gãy** thành hai nhà nước Đông/Tây đối địch thì hai ông đặt ở thời Nivar (581–587), tr. 328. Mục vì vậy không ghi bất kỳ hành vi phân phong nào cho Bumin." |
| **B9** | Ghi chú CE06 **[G]** | "chỉ 周書卷50 mới chép đủ chuỗi 545/546/551/552 và gọi tên ông" + "北史卷99 ghép hai bản cạnh nhau mà không hòa giải" | 北史卷099 chép **cùng một chuỗi, cùng chữ**, gọi 土門 **8 lần**, và cho **đúng một** bản liền mạch. Chỗ bất nhất nằm ở **隋書卷84** (「卒，**弟**逸可汗立」) | "chỉ 周書卷50 và 北史卷099 mới chép đủ chuỗi 545/546/551/552 và gọi đích danh 土門 (Bắc sử 8 lần, gần như trùng chữ với Chu thư). Chỗ chính sử Trung Hoa **không thống nhất** là người kế vị: Chu thư và Bắc sử đều chép 「土門死，**子**科羅立」, còn 隋書卷84 chép 「卒，**弟**逸可汗立」 — và 校勘記 in kèm Chu thư nêu thẳng sự khác biệt 「作『子』作『弟』不同」." |
| **B10** | Ghi chú CE06 **[G]** | "Trung Á vì vậy vẫn ở đúng một người." | `data/persons.json` cho Trung Á = **2** (`CH02-BCE06-09`, `CH05-CE08-01`); một khối ghi chú khác trong cùng file đã ghi "từ 1 lên 2 người mỗi ô" | "Việc không chọn Maniakh vì vậy không mở thêm được ô Trung Á ở nhóm này; ô ấy chỉ nhúc nhích ở nhóm CE08, với Abu Muslim `CH05-CE08-01`." |
| **B11** | Ghi chú CE06 **[G]** | "Q854920 (Bhavavarman) ghi **sinh 600 và mất 600**" → "vô nghĩa" | P569 ở **độ chính xác thế kỷ** và **có 1 reference**; chỉ P570 mới ở độ chính xác năm. Không hề "sinh 600 mất 600" | "Q854920 (Bhavavarman) để P569 ở **độ chính xác thế kỷ** rồi P570 ở độ chính xác năm trên cùng giá trị thô `+0600` — đọc ẩu thành 'sinh 600, mất 600' là rơi đúng cái bẫy độ chính xác mà atlas đã ghi ở khối dưới;" |
| **B12** | Ghi chú CE06 **[G]** | "Q705378 (Kaleb) sinh k. 450 **không nguồn**" | Nói ngược: P569 (`+0450`, độ chính xác thế kỷ) **có** 1 reference; cái không có reference là **P570 `+0540`** | "Q705378 (Kaleb) để P569 ở độ chính xác thế kỷ và có nguồn, nhưng **năm mất 540 thì không có reference nào**;" |

**12 lỗi BẮT BUỘC, phân bố:** `CH05-CE06-11` **3** (và cả ba đều ở mệnh đề cốt lõi), `CH05-CE06-12` **2**, `CH05-CE06-10` **1**, `CH05-CE06-09` **1**, ghi chú biên tập **5**.

## NÊN — phải rào hoặc phải nói chính xác hơn

| # | Mục | Vấn đề | Sửa |
|---|---|---|---|
| **N1** | `CH05-CE06-12` **[M]**+**[N]** | "dịch và **chú giải bộ Organon**" — ông chỉ chú giải *Phạm trù* (1 bản) và *Về mệnh đề* (2 bản), không chú giải bốn tác phẩm còn lại; dòng Nguồn cũng ghi "các bình luận *Organon*" số nhiều | thân mục: "…dịch trọn bộ *Organon* của Aristotle sang Latinh và chú giải phần đầu của nó — *Phạm trù* một lần, *Về mệnh đề* hai lần."; Nguồn: "hai bình luận *Isagoge*; bình luận *Phạm trù* và hai bình luận *Về mệnh đề*" |
| **N2** | `CH05-CE06-12` **[M]** | `nơi: Rome và Pavia` — `Pavia` xuất hiện **0 lần** trong cả hai bài SEP được dẫn; nơi hành quyết còn tranh luận (*ager Calventianus*) | `nơi: Rome và Ravenna, vương quốc Ostrogoth ở Ý` (Ravenna có trong SEP), hoặc giữ Pavia nhưng rào trong văn xuôi |
| **N3** | `CH05-CE06-10` **[N]** | Dòng Nguồn dẫn trống "Denis Sinor" cho một chương **đồng tác giả với S. G. Klyashtorny**, và dẫn tr. 328 trong khi phần về chính Bumin ở **tr. 327** | "…北史 quyển 99, liệt truyện 87, Đột Quyết – Thiết Lặc (Lý Diên Thọ); **D. Sinor và S. G. Klyashtorny**, chương 14 "The Türk Empire", trong *History of Civilizations of Central Asia*, tập III (UNESCO), tr. **327–328**." |
| **N4** | `CH05-CE06-10` **[M]** | `nơi: cao nguyên Mông Cổ, núi Ötükän (都斤山) và lưu vực Orkhon` — không nguồn nào đặt **chính Bumin** ở đó; 「lưu vực Orkhon」 không xuất hiện trong bất kỳ nguồn nào mục dẫn; chính văn đặt gốc A Sử Na ở **金山** (Altai) | `nơi: biên giới bắc Tây Ngụy và thảo nguyên Mông Cổ; gốc A Sử Na ở Kim Sơn (金山, dãy Altai)` |
| **N5** | Ghi chú CE06 **[G]** | Yoshida 2019: cái "không còn tồn tại trong bi ký" là **Mahan Tegin**, không phải Bumin — ghi chú đặt câu ngay sau "bi ký Bugut nhắc tên ông" nên người đọc hiểu nhầm | "…Yoshida Yutaka, "Sogdian Version of the Bugut Inscription Revisited", *Journal Asiatique* 307/1 (2019), tr. 97–108, đã hiệu đính lại bằng ảnh 3D và kết luận rằng **Mahan Tegin** — người mà cách đọc cũ cho là bia đề tặng — "không còn tồn tại trong bi ký"; theo bản mới, bia nói về tính chính danh của Tatpar khả hãn và con là Umna." |
| **N6** | Ghi chú CE06 **[G]** | Khối "Năm 525 của Kaleb" điểm D: Hatke gán Ja 1028 / Ry 507 / Ry 508 cho vụ **Ẓafār**, và viết thẳng "**Although no Sabaic inscriptions refer directly to this campaign** [Najrān]…" | "…năm bi ký Sabaic quanh Najrān… ghi niên đại 633 lịch Ḥimyar. Phải nói rõ phạm vi: theo Hatke, nhóm Ja 1028 / Ry 507 / Ry 508 chép **chiến dịch của Yūsuf ở Ẓafār và việc phong toả bờ Biển Đỏ**, còn **cuộc tàn sát Najrān mùa thu 523 thì không bi ký Sabaic nào chép trực tiếp** — nó chỉ được biết qua hagiography Hy Lạp và Syriac thế kỷ 6." |
| **N7** | Ghi chú CE06 **[G]** | Khối "Năm 525 của Kaleb" điểm B: "633 HE = tháng 6–7 năm 523 CN" viết dấu bằng trần trụi, trong khi phép quy đổi phụ thuộc kỷ nguyên Ḥimyar và một phần tài liệu cho **524** | thêm "theo quy ước kỷ nguyên Ḥimyar thường dùng" trước phép quy đổi |
| **N8** | `CH05-CE06-09` **[M]** | Chuỗi `klb ʾl ʾṣbḥ wld tzn` **[KHÔNG KIỂM ĐƯỢC]** — 0 lần trong 183.343 ký tự PAN và 0 lần trong cả hai mục từ điển đã mở. (Nửa sau của câu — vương hiệu dài mô phỏng lối xưng vua Ḥimyar — thì **đúng và có nguồn mạnh**) | hoặc dẫn ấn bản bi ký RIÉth 191 trực tiếp, hoặc bỏ chuỗi chữ phiên âm và giữ lại phần vương hiệu |
| **N9** | `CH05-CE06-09` **[N]** | Dòng Nguồn: mệnh đề về vương hiệu nằm ở mục từ **"Kālēb"** (doi 10.60667/tdaa-0059), không phải mục "Aksum [and South Arabia]" (doi 10.60667/tdaa-0005) đang được dẫn; cộng ba lỗi hình thức thư mục (chữ "A" thừa ở đầu, tên mục bị cắt, thiếu năm và DOI) | dùng dòng Nguồn thay thế đã viết sẵn ở `CH05-CE06-09` mục 2b |
| **N10** | Ghi chú CE06 **[G]** | Khối "HTTP 200 không có nghĩa là đọc được": "HAL và DASI trả trang chặn bot" — **HAL không chặn bot** (200, `content-type: application/pdf`, UA chung); DASI thì nay **000 / 0 byte**, tệ hơn mô tả | dùng câu thay thế đã viết sẵn ở N6 của phần liên-mục, có kèm cái bẫy mới và nặng hơn: HEAD cho `content-length: 10911072` trong khi mọi lần kéo đều đứt giữa chừng ở kích thước ngẫu nhiên **mà `curl` vẫn thoát mã 0** — phải so với `content-length`, không so với lần kéo trước |
| **N11** | Ghi chú CE06 **[G]** | "Châu Âu đang ở **26,9%**" — thật ra 26,70% (sau Boethius) hoặc 26,36% (trước). Lập luận đúng, con số sai | "lựa chọn này **không có lợi** cho thống kê vùng — Châu Âu đã là ô lớn thứ hai của atlas, trên một phần tư tổng số, và mục này đẩy nó lên thêm." Kèm khuyến nghị: **đừng viết tỷ lệ cứng vào ghi chú** khi `atlaslib` tính được. |
| **N12** | Ghi chú CE06 **[G]** | "Wikidata sai ở cả **bốn** ứng viên nhóm này" — chỉ **hai trong bốn** đúng như mô tả (xem B11, B12) | đổi tiêu đề khối thành "Wikidata phải đọc kỹ ở cả bốn ứng viên nhóm này" |

## CÂN NHẮC — phong cách, sắc thái, hoặc tự mâu thuẫn nhẹ

| # | Mục | Vấn đề | Gợi ý |
|---|---|---|---|
| **C1** | `CH05-CE06-11` **[M]** | "K.151… nêu ông trong một **chuỗi ba vua**" — **[KHÔNG KIỂM ĐƯỢC]**; danh sách **năm** vua là của K.53, còn K.151 theo Heng & Lavy là bi ký của một quan trấn nhậm | bỏ "chuỗi ba vua", hoặc dẫn ấn bản Coedès *IC* |
| **C2** | `CH05-CE06-11` **[M]** | "Mô hình ông để lại… chính là khuôn mà Īśānapura rồi Angkor kế tục" — mệnh đề tổng hợp, không nguồn nào được dẫn phát biểu | hạ giọng: "…cái khuôn ấy còn nhận ra được ở Īśānapura và về sau ở Angkor" |
| **C3** | `CH05-CE06-11` **[N]** | Heng & Lavy chỉ có URL trần, thiếu dữ liệu xuất bản | bổ sung sách/tạp chí, năm, số trang |
| **C4** | `CH05-CE06-09` **[M]** | "lần cuối một thế lực châu Phi hạ Sahara cai trị đất Arabia" — Abraha cai trị tự trị tới k. 570, nên mốc "cuối" thuộc về Abraha chứ không phải Kaleb | nói rõ quyền cai trị Ethiopia kéo tới k. 570 dưới Abraha, không chấm dứt với Kaleb |
| **C5** | Ghi chú CE06 **[G]** | Khối Kaleb điểm K: "hagiography soạn khoảng **ba mươi lăm năm sau**" — 560 − 525 = 35 nếu đếm từ chiến dịch, nhưng câu đang nói về **thoái vị**, mà Hatke đặt ở **k. 540** → khoảng **20** năm | ghi rõ đếm từ mốc nào |
| **C6** | `CH05-CE06-12` **[M]** | "Boethius thì tác phẩm **còn nguyên vẹn**" — bản dịch *Phân tích hậu* đã mất, chính mục nói thế hai đoạn trên | "tác phẩm chính còn nguyên vẹn" |
| **C7** | Ghi chú CE06 **[G]** | "tên ông đã hai lần xuất hiện… một lần ngay trong dòng quan hệ" — dòng quan hệ ấy **đã bị chính commit này xoá**; `grep` hiện tại chỉ còn 1 lần | "…một lần trong văn xuôi, một lần trong dòng quan hệ mà mục này vừa thay bằng một liên kết thật…" |
| **C8** | Ghi chú CE06 **[G]** | "châu Âu trung cổ đọc Aristotle qua lăng kính Tân Plato, và **lăng kính đó là của ông**" — lăng kính là của Porphyry; atlas đã định vị Boethius là **cơ chế truyền** ở `CH04-CE03-03` | "…lăng kính của Porphyry, nhưng mài và lắp bởi ông." |
| **C9** | `CH05-CE06-12` **[N]** | Bài SEP thứ hai không ghi tên tác giả như bài thứ nhất | `Stanford Encyclopedia of Philosophy, "Literary Forms of Medieval Philosophy" (Eileen Sweeney)` |
| **C10** | `CH05-CE06-12` **[R]** | Cặp Chaucer / Jean de Meun được đỡ bởi **bài SEP thứ nhất** (§8), không phải bài thứ hai (`Chaucer` 0 lần, `Jean de Meun` 0 lần trong bài Sweeney) | dòng quan hệ **đúng, giữ nguyên** — chỉ cần biết nó tựa vào bài nào |
| **C11** | Ghi chú CE06 **[G]** | "DOI 10.2143/JA.307.1.3286342 trả **406**" — kiểm lại 31-10-2026: nay **200** qua `data.medra.org`, 421 B CSL-JSON | thêm ngày kiểm và kết quả mới |
| **C12** | `CH05-CE06-10` **[M]** | Nếu ở đâu đó phiên 伊利可汗 thành "Illig Qaghan" thì đó là tái dựng của giới nghiên cứu, không phải chữ của nguồn | rào nếu có dùng |
| **C13** | `CH05-CE06-11` **[R]** | `Īśānavarman I… · kế thừa · trực tiếp` — Heng & Lavy rào bằng "**perhaps**", và giữa hai người còn có Mahendravarman | `trực tiếp` vẫn đứng được (kế tục triều đại liền kề); nếu muốn chặt thì hạ xuống `qua trường phái` |
| **C14** | Ghi chú CE06 **[G]** | Khối "Chân Lạp chinh phục Phù Nam" nên nói thêm chiều ngược: chính "Funan Reviewed" chứa phản chứng cho mệnh đề trung tâm của mục | dùng câu bổ sung đã viết sẵn ở `CH05-CE06-11` mục (5)D |

## Những chỗ KHÔNG CÓ LỖI — ghi lại để vòng sau khỏi "sửa" nhầm

- `CH05-CE06-09`: RIÉth 191 ở **chữ musnad** ✓; câu cuối về Abraha ✓; "Thập niên 520 ông vượt Biển Đỏ" ✓; **quy tắc 8 sạch hoàn toàn** (hai liên kết ID đúng người, bốn mức bằng chứng đều hợp); **quy tắc 7 sạch** — không nguồn nào bị dẫn ngược trong thân mục. Khối ghi chú điểm G ("bốn lần xâm nhập, một lần đích thân cầm quân") **đúng từng chữ**.
- `CH05-CE06-10`: **mục chắc nhất về nguồn sơ cấp trong cả bốn**. Mọi mốc 545/546/551/552, câu 「爾是我鍛奴」, vương hiệu 伊利可汗, quan hệ cha–con với Mộc Hãn và hai mốc 553–572 đều khớp nguyên văn 周書卷50 / 北史卷099 và Sinor tr. 327. Số quyển của cả hai bộ sử **đúng** khi mở mục lục thật. **Quy tắc 8: không lỗi** — kể cả dòng Mặc Đốn `tương đồng độc lập · suy đoán học giả`, là cách ghi thận trọng đúng mức. `hoạt động 545–552 CN` truy được tới gốc ✓.
- `CH05-CE06-11`: K.439 ↔ Gambhireśvara ✓; K.53 là văn bản hồi cố **năm 667** ✓; `trị vì k. 550 – k. 600` ✓ khớp nguyên văn Heng & Lavy; citation Vickery 1994 (EFEO, 1994, F. Bizot chủ biên, tr. 197–212) **đúng đến từng chi tiết**; cả hai URL Nguồn đều 200 và là PDF thật. **Quy tắc 8 không áp dụng** — mục không có liên kết ID nào.
- `CH05-CE06-12`: `năm: k. 477 – k. 526 CN` ✓ khớp SEP từng chữ; "bản *Phân tích hậu* đã mất" ✓; "kế hoạch dịch trọn Plato lẫn Aristotle không xong" ✓; "viết trong tù chờ án tử" ✓; dòng quan hệ Chaucer / Jean de Meun ✓.
- Ghi chú biên tập: điểm (1) của khối "Bốn điều không được viết về Boethius" — "480–524 là cặp số Wikidata ở rank preferred" — **kiểm đúng hoàn toàn** (P569 `+0480` preferred/9 refs, P570 `+0524` preferred/3 refs). Khối "Đông Nam Á ở lại 0,5%" ✓ (1/221 = 0,45%). Khối "Bốn vùng, và chỗ atlas vừa hết số không" ✓ toàn bộ. `Q551446` không có P84 lẫn P170, P571 = 606 ✓ **đúng từng chi tiết**. Q29001 sinh 490 không nguồn ✓. Q8046995 hai giá trị P570 (603 normal, 593 deprecated) ✓.

## Những chỗ `[KHÔNG KIỂM ĐƯỢC]` — liệt kê đủ

| Mệnh đề | Lý do |
|---|---|
| Chuỗi `klb ʾl ʾṣbḥ wld tzn` của RIÉth 191 | 0 lần trong PAN (183.343 ký tự) và trong cả hai mục từ điển; không mở được ấn bản bi ký |
| "Robin đặt chiến dịch **sau Lễ Ngũ Tuần 525**" | Robin 2008 đóng, không có bản toàn văn ở kho lưu trữ nào mở được |
| Ry 513 và Ry 515 ghi 633 HE | DASI `000 / 0 byte` |
| CIH 621 = 640 HE = tháng 2 năm 530 | DASI `000`, academia.edu 403, Open Book Publishers 405 |
| Niên đại k. 560 của *Martyrium Arethae* | không mở được ấn bản nào |
| K.151 "nêu ông trong một chuỗi ba vua" | không nguồn nào được dẫn nói vậy |
| ~~Goodall & Revire: "có bao nhiêu vua tên Bhavavarman"~~ | **Đã kiểm được bằng đường khác — xem Phụ lục cuối báo cáo.** Kết quả: chữ `Bhavavarman` **không có trong toàn văn bài báo ấy**. Chuyển sang mức **NÊN** (N13). |
| Khối Yajaw Teʼ Kʼinich II (Simon Martin, Caracol Altar 21, Chase & Chase 2020 tr. 35, 9.9.18.16.3 → 631/633) | ngoài phạm vi bốn mục được giao; chưa mở nguồn nào |
| "Lý Xuân không có thực thể Wikidata nào là người" | `wbsearchentities` cho 李春 không trả về ai là thợ cầu đời Tùy — nhưng đây là "không tìm thấy", không phải chứng minh không tồn tại |

## Ghi chú phương pháp

Mọi lệnh mạng trong vòng này dùng đúng một User-Agent: `history-atlas/0.1 (research)`. **Không có thông tin cá nhân nào** (email, tên người dùng, tham số `mailto`) xuất hiện trong header, URL hay payload của bất kỳ yêu cầu nào — kể cả với OpenAlex, nơi tham số `mailto` thường được khuyến nghị nhưng đã **cố ý bỏ**.

---

# Phụ lục — kiểm được Goodall & Revire bằng đường vòng, và kết quả lật ngược một mệnh đề

Mục `[KHÔNG KIỂM ĐƯỢC]` cuối cùng của vòng này **đã giải được**, nên phải ghi bổ sung.

## Vì sao không tải được file

Sáu lần tải mới hoàn toàn (không dùng `-C -`), mỗi lần `--max-time 900`, đều đứt giữa chừng:

| Lần | Byte tải được | / tổng thật |
|---|---|---|
| 1 | 5.767.443 | 10.911.072 |
| 2 | 3.709.026 | 10.911.072 |
| 3 | 9.925.242 | 10.911.072 |
| 4 | 9.069.210 | 10.911.072 |
| 5 | 10.181.034 | 10.911.072 |
| 6 | 4.626.235 | 10.911.072 |

**Sáu lần, không lần nào đủ**, và `curl` thoát mã **0** cả sáu lần. Persée (`persee.fr/doc/befeo_0336-1519_2021_num_107_1_6376`, **200 / 142.025 B**) chỉ cho **3.326 ký tự chữ thật** — tóm tắt cộng trang đầu; `docAsPDF` thì **403**.

## Đường vòng dùng được: tra thẳng chỉ mục toàn văn của HAL

HAL đánh chỉ mục toàn văn PDF đã nộp vào trường `text_fulltext`, và API cho lọc trên trường ấy mà **không phải tải file**:

```
api.archives-ouvertes.fr/search/?q=halId_s:halshs-04142364&fq=text_fulltext:<từ>
```

Mỗi truy vấn trả **HTTP 200**, cỡ ~116 byte JSON. Kiểm chứng bằng từ đối chứng trước:

| Từ tra | numFound |
|---|---|
| `inscription` | **1** |
| `Isanavarman` | **1** (chỉ mục bỏ dấu: bài viết "Īśānavarman I") |
| `Jayavarman` | **1** |
| `Gunavarman` | **1** |
| `Funan` | **1** |
| `Zhenla` | **1** |
| `palaeography` | **1** |
| `Vickery` | **1** |
| `Coedes` | **1** |
| **`Bhavavarman`** | **0** |
| **`Bhavavarmman`** | **0** |
| **`Bhavavarmmā`** | **0** |
| **`Bhavavarma`** | **0** |
| **`Rudravarman`** | **0** |

Chỉ mục rõ ràng **có** xử lý tên riêng Phạn ngữ đúng cách — `Gunavarman`, `Jayavarman`, `Isanavarman` đều trúng, kể cả khi bài viết có dấu phụ. Trong bối cảnh ấy, **bốn** cách viết của Bhavavarman đều cho 0 là kết quả có nghĩa.

## N13 — NÊN. Mệnh đề về Goodall & Revire gán sai bài

**Câu hiện tại (khối "'Chân Lạp chinh phục Phù Nam' là câu không được viết"):**
> "Còn một vấn đề định danh ít được nói: **Goodall & Revire đặt thẳng câu hỏi có bao nhiêu vua tên Bhavavarman trong bi ký Campuchia thế kỷ 6–7**, nên việc gán một bi ký không niên đại cho "Bhavavarman I" tự nó đã là một phán đoán cổ tự học."

Bài "East and West — New Inscriptions from Funan, Zhenla and Dvāravatī" (*BEFEO* 107, 2021, tr. 257–301) **không chứa chữ Bhavavarman dưới bất kỳ cách viết nào**. Nội dung bài, theo phần mở đầu đọc được trên Persée, là ba nhóm bi ký mới: K.1455 ở Angkor Borei, K.1563 ở Mueang Phaniat (Chanthaburi) nêu Īśānavarman I, và N. Th. 21 ở Wat Phra Ngam (Nakhon Pathom) nêu địa danh Dvāravatī. Không có phần nào về việc đếm số vua tên Bhavavarman.

Thư mục của bài thì **đúng hết** (tác giả, tạp chí, tập 107, năm 2021, tr. 257–301, DOI `10.3406/befeo.2021.6376`) — tức đây **không** phải nguồn giả. Đây là lỗi **gán mệnh đề cho sai bài**: cùng tác giả, cùng lĩnh vực, nhưng bài được dẫn không nói điều đang được dẫn. Đúng họ hàng với lỗi quy tắc 7, và là loại lint không bao giờ bắt được.

**Phải nói công bằng hai điều:**
1. Phương pháp này là **chỉ mục dẫn xuất**, không phải chính file PDF. Nếu chữ ấy nằm trong một ảnh quét không có lớp chữ, chỉ mục sẽ không thấy. Nhưng bài này có lớp chữ (chín từ đối chứng đều trúng), nên khả năng ấy thấp.
2. **Suy luận của khối vẫn đúng** và không phụ thuộc vào bài này: Vickery 1994 độc lập ghi nhận **Bhavavarman II** trong K.1150 (em của Śivadatta, con Īśānavarman I), nên "gán một bi ký không niên đại cho Bhavavarman I là một phán đoán cổ tự học" là mệnh đề **đúng**. Chỉ cái tên nguồn là sai chỗ.

**Câu thay thế (viết sẵn):**
> "Còn một vấn đề định danh ít được nói: bi ký Campuchia thế kỷ 6–7 biết tới **hơn một** vua mang tên Bhavavarman — Vickery 1994 nêu Bhavavarman II trong K.1150, em của Śivadatta và con của Īśānavarman I — nên việc gán một bi ký không niên đại cho "Bhavavarman I" tự nó đã là một phán đoán cổ tự học."

(Nếu muốn giữ tham chiếu Goodall & Revire thì **phải tìm đúng bài**; bài *BEFEO* 107 (2021) không phải bài đó.)

## Bổ sung cho khối "HTTP 200 không có nghĩa là đọc được" — một mẹo nên ghi vào CONTRIBUTING

> "Khi một PDF trên HAL không tải nổi, **đừng bỏ cuộc ở đó**: HAL đánh chỉ mục toàn văn vào trường `text_fulltext`, và `api.archives-ouvertes.fr/search/?q=halId_s:<id>&fq=text_fulltext:<từ>` trả lời được câu 'bài này có nhắc tới X không' bằng một yêu cầu ~116 byte, không cần tải file. Luôn chạy vài **từ đối chứng** chắc chắn có trong bài trước khi tin một kết quả 0."

**Cập nhật bảng mức:** mục Goodall & Revire chuyển từ `[KHÔNG KIỂM ĐƯỢC]` sang **NÊN (N13)**. Tổng cuối: **12 BẮT BUỘC, 13 NÊN, 14 CÂN NHẮC**, và **8** mệnh đề còn `[KHÔNG KIỂM ĐƯỢC]`.
