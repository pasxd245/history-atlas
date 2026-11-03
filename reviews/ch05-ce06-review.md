# Bình duyệt độc lập — nhóm CE06, `content/ch05.md` (dòng 4–208)

Vòng rà do một agent **không viết** nhóm này thực hiện. Không spawn sub-agent. Báo cáo ghi tăng dần sau mỗi mục.
Xếp hạng: **BẮT BUỘC** (phải sửa) · **NÊN** · **CÂN NHẮC** · `[KHÔNG KIỂM ĐƯỢC]`.

## Cách kiểm (áp cho cả 12 mục)

- **Q-ID**: `wbgetentities` một lượt cho cả 12 Q-ID, đọc nhãn en/vi, P569/P570 kèm **precision**, **rank** và **số reference**, P31. Bẫy `/p7` (thế kỷ = một KHOẢNG) được xử theo `atlaslib/common.py:year_in_bucket`; dung sai theo `DATE_TOLERANCE` (`common.py:82`).
- **Trần chữ**: đếm bằng `len([w for w in s.split() if w])` đúng như `atlaslib/lint.py:12`. Trần cảnh báo: `ideas ≤ 130`, `why ≤ 104`, `context ≤ 78`.
- **Quy tắc 6**: grep từng tên bị loại trên **toàn bộ** `content/*.md`, đối chiếu với danh sách 253 tiêu đề `### CHxx-...`.
- **Liên kết ID**: mở từng mục đích, đọc tên người ở đầu kia (`lint.py:151-152` chỉ kiểm ID tồn tại).
- **URL**: `curl -A 'history-atlas/0.1 (research)'` kèm `-w` mã trạng thái + **kích thước** + content-type, rồi đọc nội dung thật (giải nén stream PDF bằng zlib vì máy không có `pdftotext`).
- **Sách không có URL**: đối chiếu OpenLibrary Search API và Crossref API.

### Hai kết quả đo được, dùng chung cho cả nhóm

**Trần chữ — không mục nào vượt, nhưng bốn mục đã chạm trần:**

| Mục | ideas (≤130) | why (≤104) |
|---|---|---|
| CE06-01 | 109 | 87 |
| CE06-02 | 101 | 76 |
| CE06-03 | 106 | 94 |
| CE06-04 | 110 | 88 |
| CE06-05 | 95 | 82 |
| CE06-06 | 122 | 87 |
| CE06-07 | 105 | 87 |
| CE06-08 | 108 | 92 |
| CE06-09 | **130** | 85 |
| CE06-10 | **130** | 79 |
| CE06-11 | 126 | 82 |
| CE06-12 | **130** | 84 |

Bối cảnh nhóm: 57 chữ (≤78) ✔.

**Mười hai Q-ID đều trỏ đúng người** (nhãn Wikidata vs tên mục), và P31 = Q5 cả mười hai:

| ID | Q | nhãn en | P569 | P570 |
|---|---|---|---|---|
| CE06-01 | Q41866 | Justinian I | 482-05-11 /p11 pref | 565-11-14 /p11 |
| CE06-02 | Q44265 | Benedict of Nursia | 480 /p11 | 547 /p11 |
| CE06-03 | Q207381 | Khosrow I | 501 /p9 | 579 /p9 |
| CE06-04 | Q858348 | Varāhamihira | 505 **/p7** | 587 **/p7** |
| CE06-05 | Q558272 | Dignāga | 480 /p9, 0 ref | 540 /p9, 0 ref |
| CE06-06 | Q7418 | Emperor Wen of Sui | 541-07-21 /p11 | 604-08-13 /p11 |
| CE06-07 | Q197778 | Zhiyi | 538 /p9 | 597 /p9 |
| CE06-08 | Q187172 | Bodhidharma | 483 và 440 /p9 | 540 /p9 |
| CE06-09 | Q705378 | Kaléb | 450 **/p7** | 540 /p9, **0 ref** |
| CE06-10 | Q29001 | Bumin Qaghan | 490 /p9, **0 ref** | 552 /p9 |
| CE06-11 | Q854920 | Bhavavarman I | 600 **/p7** | 600 /p9 |
| CE06-12 | Q102851 | Boethius | 480 /p9 pref; 475 /p8 | 524 /p9 pref; 525 /p8 |

Ba ca bẫy mà **mục đã xử đúng**: CE06-04 dùng `/p7` như một khoảng chứ không phải điểm; CE06-09 và CE06-11 dùng `trị vì …` nên `NON_BIO_YEARS_RE` (`common.py:133`) chặn đối chiếu — và chuỗi "trị vì" đứng **đầu** trường ở cả hai, đúng yêu cầu; CE06-10 từ chối chép năm sinh 490 không reference, đúng như khối ghi chú tự khai.

---
## 1. `CH05-CE06-01 · Justinianus I` — dòng 8–22

**Đã kiểm được (không có phát hiện)**
- Q41866 = "Justinian I" / vi "Justinianus I", P31 = Q5 ✔.
- `năm: k. 482–565 CN`, độ tin cậy **Cao** (dung sai ±5). Wikidata 482-05-11 (rank preferred, 2 ref) và 565-11-14 (4 ref) → lệch 0 và 0 ✔.
- `vùng: Châu Âu` ∈ `REGIONS`; `lĩnh vực: Luật, Chính trị/Nhà nước` cả hai ∈ `FIELDS`, đúng trần 2 ✔.
- ideas 109 / why 87 — trong trần ✔.
- Bốn phần Corpus Juris Civilis (Codex, Digesta, Institutiones, Novellae) ✔. Con số "khoảng hai nghìn cuốn" khớp lời khai của chính *Constitutio Tanta* ✔. Mốc Bologna thế kỷ 11 ✔.
- Nguồn: *The Cambridge Companion to the Age of Justinian* (Michael Maas chủ biên, CUP, 2005) có thật, và Caroline Humfress đúng là tác giả chương luật trong đó ✔. Procopius, *Wars* + *Secret History* ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE05-05` mở ra là **Theodosius II** (`content/ch04.md:883`) — đúng người cho mệnh đề kế thừa (Codex Theodosianus) ✔.
- **Quy tắc 6 sạch**: `Tribonianus` và `Theodora` được grep trên toàn bộ `content/*.md`; không ai có tiêu đề `### CHxx-…` ở bất kỳ chapter nào, kể cả `ch90.md` ✔.

**Phát hiện 1 — BẮT BUỘC. Hội đồng năm 528 không do Tribonianus đứng đầu.**

Nguyên văn câu sai (dòng 10):
> Năm 528, một năm sau khi lên ngôi, ông lập hội đồng do Tribonianus đứng đầu để rà toàn bộ luật La Mã tích tụ gần một nghìn năm.

Hội đồng mười người lập tháng 2 năm 528 cho bản Codex thứ nhất do **John xứ Cappadocia** chủ trì; Tribonianus khi ấy là **một ủy viên**, chưa cả giữ chức quaestor sacri palatii (nhận tháng 9 năm 529). Chỉ từ năm 530, cho bộ *Digesta*, Justinianus mới đặt ông đứng đầu. Đáng chú ý là chính mục này ở phần "Vì sao chọn" lại mô tả đúng vai trò ấy ("người thật sự chủ trì việc biên soạn"), nên lỗi chỉ nằm ở mốc 528.

Câu thay thế đề xuất, nguyên văn:
> Năm 528, một năm sau khi lên ngôi, ông lập một hội đồng mười người rà toàn bộ luật La Mã tích tụ gần một nghìn năm; Tribonianus khi ấy là một ủy viên, và từ năm 530 mới đứng đầu hội đồng soạn Digesta.

*Soi lại câu thay thế:* 45 chữ, thay cho 29 chữ cũ → ideas thành **125 chữ**, vẫn dưới trần 130 ✔. Không mệnh đề nào trong câu thay thế vượt quá điều đã kiểm được: con số "mười người" và mốc 530 đều là mô tả chuẩn của bộ hồ sơ Codex/Digesta. `[KHÔNG KIỂM ĐƯỢC]` — tên **John xứ Cappadocia** với tư cách chủ tịch hội đồng 528 tôi **không** đưa vào câu thay thế, vì trong vòng này không mở được một bản chuyên khảo (Honoré, *Tribonian*) để xác nhận; câu thay thế vì vậy chỉ nói Tribonianus **không** đứng đầu năm 528 — mệnh đề này đứng độc lập, không cần tên người chủ trì.

**Phát hiện 2 — NÊN. `trực tiếp` gán cho một đích không phải người, cách nhau năm thế kỷ.**

Nguyên văn (dòng 21):
> - Đại học luật Bologna thế kỷ 11 · kế thừa · trực tiếp

Đích là một thiết chế, không phải người, và cách Justinianus hơn 500 năm. Đây đúng loại lỗi mà khối ghi chú chapter đã mô tả ("mức bằng chứng `trực tiếp` đang mang hai nghĩa") và lint mù hoàn toàn.

Câu thay thế đề xuất, nguyên văn:
> - Đại học luật Bologna thế kỷ 11 · kế thừa · qua trường phái

*Soi lại:* `qua trường phái` ∈ `EVIDENCE_LEVELS` (`common.py:79`) ✔, không đổi số dòng nên không chạm trần 3 mục ✔.

**Phát hiện 3 — CÂN NHẮC. `CH04-CE05-05 · kế thừa · trực tiếp`.**
Theodosius II mất năm 450, Justinianus sinh k. 482 — không thể là quan hệ người–người; đây là quan hệ **văn bản** (Codex Justinianus dựng trên Codex Theodosianus). Để CÂN NHẮC chứ không NÊN vì định nghĩa `trực tiếp` chưa được chốt: khối ghi chú chapter đã ghi việc này cho P4 và nói rõ "nếu định nghĩa chọn nghĩa người–người thì một loạt dòng trong Chapter 5 phải hạ xuống `qua trường phái`". Dòng này nằm trong loạt đó.

**Phát hiện 4 — CÂN NHẮC. Theodora được nêu tên nhưng không được nêu lý do loại.**
Nguyên văn (dòng 12): *"Ứng viên cùng thời là Tribonianus, người thật sự chủ trì việc biên soạn, và Theodora. Tribonianus bị loại vì luận điểm trùng hoàn toàn với mục này."* Chỉ Tribonianus có lý do; Theodora đứng trơ. Template §5 đòi "lý do người này vượt trội theo tiêu chí (a)–(d)" cho **mỗi** ứng viên được nêu. Vì `why` mới ở 87/104 nên vẫn còn 17 chữ dư để thêm một mệnh đề ngắn.

---
## 2. `CH05-CE06-02 · Biển Đức thành Norcia` — dòng 23–37

**Đã kiểm được (không có phát hiện)**
- Q44265 = "Benedict of Nursia" / vi "Biển Đức thành Norcia", P31 = Q5 ✔.
- `độ tin cậy niên đại: Thấp` → `DATE_TOLERANCE["Thấp"] is None`, lint bỏ đối chiếu niên đại (`lint.py:289-291`); quyết định này được mục tự biện minh bằng vấn đề nguồn Dialogi ✔.
- `vùng: Châu Âu`, `lĩnh vực: Tôn giáo/Tâm linh, Giáo dục` — cả hai ∈ `FIELDS` ✔. ideas 101 / why 76 ✔.
- "bảy mươi ba chương" ✔; viện trưởng do cộng đoàn bầu (RB 64) và phải hỏi người trẻ nhất (RB 3) ✔; Dialogi quyển II gán cho Gregorius Cả, k. 593 ✔.
- **Nguồn tồn tại**: Marilyn Dunn, *The Emergence of Monasticism*, 2000 — OpenLibrary trả đúng một bản ghi tác giả "Marilyn Dunn", năm xuất bản đầu 2000 ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE05-01` = **Augustinô thành Hippo** (`ch04.md:817`) ✔.
- **Quy tắc 6 sạch**: `Cassiodorus` và `Caesarius xứ Arles` không có mục ở bất kỳ chapter nào, kể cả `ch90.md` ✔.

**Phát hiện 1 — NÊN (quy tắc 7). Nguồn được dẫn là người chủ trương bác chính mệnh đề mà nó đang đỡ.**

Nguyên văn câu (dòng 27):
> Ông soạn Regula Benedicti, bản quy tắc bảy mươi ba chương cho đời sống tu viện.

Nguồn duy nhất mang tính chuyên khảo của mục là Dunn 2000. Marilyn Dunn là tác giả của lập luận nổi tiếng rằng *Regula Benedicti* có thể **hậu** Biển Đức, tức quyền tác giả của ông không phải tiền đề mà là thứ đang bị tranh cãi. Dẫn bà để đỡ cho một câu khẳng định tác quyền là đúng hình dạng lỗi mà `CONTRIBUTING.md:52` mô tả với ca Hansen.

`[KHÔNG KIỂM ĐƯỢC]`: tôi **không** mở được nội dung sách Dunn 2000 trong vòng này (OpenLibrary chỉ trả metadata; không có bản toàn văn truy cập được). Tôi xác nhận được sách **tồn tại** và tác giả đúng, nhưng **không** xác nhận được bà viết gì trong đó. Vì vậy phát hiện này là **NÊN**, không phải BẮT BUỘC: việc cần làm là mở sách ra đọc, không phải sửa mù.

Câu thay thế đề xuất, nguyên văn:
> Bản quy tắc mang tên ông, Regula Benedicti, gồm bảy mươi ba chương cho đời sống tu viện.

*Soi lại câu thay thế:* 18 chữ thay cho 16 → ideas thành **103 chữ**, trong trần ✔. Câu này **không** mang mệnh đề nào tôi chưa kiểm được: nó không khẳng định ai soạn, không khẳng định ai không soạn, và con số 73 chương thì kiểm được độc lập với tranh luận tác quyền. Nếu vòng sau mở được Dunn và thấy bà **không** bác tác quyền, câu gốc có thể giữ nguyên — nhưng câu thay thế vẫn đúng trong cả hai trường hợp, nên nó là lựa chọn an toàn hơn chứ không phải lựa chọn đánh cược.

**Phát hiện 2 — NÊN. `trực tiếp` gán cho một đích không phải người, và mâu thuẫn với chính câu kế trên.**

Nguyên văn (dòng 35):
> - Phòng chép sách tu viện và việc bảo tồn văn học Latin · kế thừa · trực tiếp

Chính văn xuôi của mục gọi đây là "**hệ quả ngoài ý định**" (dòng 27). Một hệ quả ngoài ý định không thể đồng thời là bằng chứng `trực tiếp`; hai câu đứng cách nhau tám dòng và nói ngược nhau.

Câu thay thế đề xuất, nguyên văn:
> - Phòng chép sách tu viện và việc bảo tồn văn học Latin · kế thừa · qua trường phái

*Soi lại:* `qua trường phái` ∈ `EVIDENCE_LEVELS` ✔; sửa này làm dòng quan hệ **khớp** với văn xuôi thay vì chọi nó, nên nó không mang lại lỗi mới.

**Phát hiện 3 — CÂN NHẮC. Liên kết Augustinô không được văn xuôi đỡ.**
`- CH04-CE05-01 · kế thừa · qua trường phái` trỏ đúng người, nhưng phần "Tư tưởng" chỉ nêu **truyền thống đan tu Ai Cập** và **Regula Magistri** làm nguồn; Augustinô không xuất hiện một chữ nào trong mục. Liên kết có thể đứng được (Regula Augustini), nhưng hiện người đọc không có đường nào để kiểm nó từ chính mục.

---
## 3. `CH05-CE06-03 · Khosrow I` — dòng 38–52

**Đã kiểm được (không có phát hiện)**
- Q207381 = "Khosrow I" / vi "Khosrau I", P31 = Q5 ✔.
- `năm: k. 501–579 CN`, **Cao** (±5). Wikidata 501 (/p9, 1 ref) và 579 (/p9, 2 ref) → lệch 0 và 0 ✔.
- `vùng: Trung Đông/Bắc Phi`; `lĩnh vực: Chính trị/Nhà nước, Kinh tế` ✔. ideas 106 / why 94 ✔.
- Lên ngôi 531 ✔; phong trào Mazdak bị đàn áp dưới triều Kavad I **trước** khi ông lên ngôi ✔ (trình tự trong câu đúng); bốn vùng quân sự ✔; mốc 651 (kết thúc nhà Sasanian) ✔.
- "Khosrow II, cháu ông" — Khosrow II là **cháu nội** (con của Hormizd IV, con Khosrow I); chữ "cháu" dùng đúng ✔.
- **Nguồn khớp từng thành phần**: bộ SUNY *The History of al-Ṭabarī* **tập V** đúng là tập về Sasanian/Byzantine/Lakhmid/Yemen, dịch giả đúng là **C. E. Bosworth**, nhà xuất bản **SUNY Press**, năm **1999** ✔. Daryaee, *Sasanian Persia* (I.B. Tauris, 2009) ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE04-05` = **Shapur II** (`ch04.md:680`) ✔; `CH04-CE03-06` = **Shapur I** (`ch04.md:496`) ✔. Cả hai là tiền bối Sasanian thật, không phải đích lạc.
- **Quy tắc 6 sạch**: `Mazdak` và `Khosrow II` không có mục ở bất kỳ chapter nào ✔.

**Phát hiện 1 — NÊN. `trực tiếp` cho hai người cách nhau 122 năm.**

Nguyên văn (dòng 48):
> - CH04-CE04-05 · kế thừa · trực tiếp

Shapur II mất năm 379; Khosrow I sinh k. 501. Khoảng cách 122 năm làm quan hệ người–người bất khả, và `lint.py` **không** bắt được vì phép kiểm nghịch niên đại (`lint.py:234-247`) chỉ báo khi người tác động sinh **sau** khi người kia mất — đây đúng ca mà `CONTRIBUTING.md:53` nêu đích danh ("nó không bắt được `trực tiếp` giữa hai người cách nhau 130 năm mà vẫn 'đúng thứ tự'").

Câu thay thế đề xuất, nguyên văn:
> - CH04-CE04-05 · kế thừa · qua trường phái

*Soi lại:* `qua trường phái` ∈ `EVIDENCE_LEVELS` ✔. Lưu ý để không sửa quá tay: dòng `CH04-CE03-06 · kế thừa · qua trường phái` ngay dưới **đã** ở mức đúng, nên chỉ một dòng cần đổi — và sau khi đổi, hai dòng cùng mức không làm mất thông tin nào, vì khoảng cách thời gian tới Shapur I còn xa hơn.

**Phát hiện 2 — CÂN NHẮC. `Bộ máy thuế đất của nhà nước Hồi giáo sơ kỳ · kế thừa · trực tiếp` (dòng 50).**
Đích là một thể chế, không phải người. Cùng loạt với các dòng chapter đã ghi nhận cho P4; để CÂN NHẮC vì ở đây nghĩa "tiếp quản nguyên vẹn một bộ máy hành chính" là nghĩa `trực tiếp` **mạnh nhất** trong cả nhóm — nếu định nghĩa P4 chọn nghĩa thể chế/văn bản thì dòng này nên được giữ, không hạ.

**Phát hiện 3 — `[KHÔNG KIỂM ĐƯỢC]`. Chi tiết "nộp ba kỳ mỗi năm".**
Nguyên văn (dòng 44): *"…rồi ấn định mức cố định nộp ba kỳ mỗi năm…"*. Chi tiết này thuộc về mô tả cải cách thuế trong al-Ṭabarī. Tôi **không** mở được bản dịch Bosworth 1999 (sách in, không có bản toàn văn truy cập được), nên **không** xác nhận được con số "ba kỳ". Không đoán, không suy diễn thành "có vẻ đúng". Việc cần làm: tra số trang trong tập V — và theo `CONTRIBUTING.md:48`, nếu không mở được mục lục thì **đừng** ghi số trang, chứ không phải ghi đoán. Mục hiện **không** ghi số trang, tức đã xử đúng tinh thần quy tắc ấy.

---
## 4. `CH05-CE06-04 · Varāhamihira` — dòng 53–67

**Đã kiểm được (không có phát hiện)**
- Q858348 = "Varāhamihira", P31 = Q5 ✔.
- `năm: k. 505 – k. 587 CN`, **Trung bình** (±25). Wikidata để **cả hai** giá trị ở `precision 7` — tức **thế kỷ**, một KHOẢNG 501–600, không phải một điểm. Cả 505 lẫn 587 nằm trong khoảng, nên `year_in_bucket` (`common.py:133+`) cho khớp ✔. Mục đã không rơi vào bẫy `/p7`.
- `vùng: Nam Á`; `lĩnh vực: Toán học, Khoa học tự nhiên`; `câu hỏi lớn: Vũ trụ` — tất cả ∈ từ vựng ✔. ideas 110 / why 88 ✔.
- Năm siddhānta (Paitāmaha, Vāsiṣṭha, Romaka, Pauliśa, Sūrya) ✔; *Bṛhat Saṃhitā* 106 chương ✔; chương dò mạch nước ngầm (dakārgala) ✔.
- Nguồn: Neugebauer & Pingree hiệu đính *Pañcasiddhāntikā*, Det Kongelige Danske Videnskabernes Selskab, 1970–71 ✔; Pingree, *Jyotiḥśāstra: Astral and Mathematical Literature*, Otto Harrassowitz, 1981 ✔.
- **Quy tắc 6 — mục này tự xử đúng ở cả hai chiều**: nó khai "Āryabhaṭa **có mục riêng** ở `CH04-CE05-09` nên không phải ứng viên bị loại", đúng câu chữ `CONTRIBUTING.md:51`; và mục Āryabhaṭa (`ch04.md:955`) cũng đã được sửa đối xứng, khai "Varāhamihira **có mục riêng** ở `CH05-CE06-04`" ✔. `Lāṭadeva` không có mục ở đâu ✔.
- Hai tiền lệ được viện dẫn tồn tại thật: Pappus = `CH04-CE04-06`, Wulfila = `CH04-CE04-03` ✔.

**Phát hiện 1 — BẮT BUỘC (quy tắc 6, phát sinh theo thời gian). Varāhamihira vẫn nằm trong danh sách "ứng viên bị loại" ở `content/ch04.md`.**

Nguyên văn câu sai, `content/ch04.md:1034`:
> - Samudragupta, Kālidāsa, Āryadeva, Dhammapāla, Varāhamihira, Gautamiputra Satakarni, Huvishka: Kālidāsa là ca đáng tiếc nhất — thơ và kịch Sanskrit của ông là đỉnh của truyền thống ấy — nhưng niên đại của ông trải từ thế kỷ 4 tới thế kỷ 5 mà không mốc nào chắc, và cả hai nhóm tương ứng đều đã kín.

Đây là đúng kiểu lỗi phát sinh theo thời gian mà vòng này được giao đi tìm, chỉ khác là nó **do nhóm CE06 gây ra chứ không nằm trong nhóm CE06**: khi `CH05-CE06-04` ra đời, dòng này ở chapter trước tự mâu thuẫn — không có đánh đổi nào xảy ra, vì người "bị loại" đã được chọn. Mục `CH04-CE05-09` đã được sửa theo quy tắc 6 nhưng khối Ghi chú biên tập của cùng file thì bị bỏ sót, nên script đối chiếu đã chỉ quét phần mục chứ không quét ghi chú.

Câu thay thế đề xuất, nguyên văn:
> - Samudragupta, Kālidāsa, Dhammapāla, Gautamiputra Satakarni, Huvishka: Kālidāsa là ca đáng tiếc nhất — thơ và kịch Sanskrit của ông là đỉnh của truyền thống ấy — nhưng niên đại của ông trải từ thế kỷ 4 tới thế kỷ 5 mà không mốc nào chắc, và cả hai nhóm tương ứng đều đã kín. **Varāhamihira** (`CH05-CE06-04`) và **Āryadeva** (`CH04-CE03-12`) **có mục riêng** nên không phải ứng viên bị loại.

*Soi lại câu thay thế:* câu này nằm trong `## Ghi chú biên tập`, **không** chịu trần chữ nào của `lint.py` (WORD_TARGET chỉ áp cho `ideas`/`why`/`intro`/`context`) ✔. Nó dùng đúng công thức `CONTRIBUTING.md:51` ("có mục riêng … nên không phải ứng viên bị loại") ✔. Hai ID trong câu thay thế **đã được tôi mở ra kiểm**: `CH05-CE06-04` là Varāhamihira, `CH04-CE03-12` là "Āryadeva (आर्यदेव, Thánh Thiên, Đề Bà)" — tôi không mượn ID mà chưa xác nhận ✔. Lưu ý phạm vi: ca **Āryadeva** nằm ngoài nhiệm vụ của vòng này (nó là lỗi nội bộ Ch4, không do CE06 gây ra); tôi gộp vào câu thay thế vì cùng một dòng, nhưng nếu chủ repo muốn giữ phạm vi chặt thì **cắt vế Āryadeva đi, câu vẫn đứng được** và vẫn sửa xong ca Varāhamihira.

**Phát hiện 2 — NÊN. `CH04-CE02-05` (Ptolemy) có thể là đích sai người.**

Nguyên văn (dòng 65):
> - CH04-CE02-05 · kế thừa · qua trường phái

ID trỏ đúng tới **Claudius Ptolemy** (`ch04.md:273`) — tức đây *không* phải lỗi ID lạc. Vấn đề là ở chỗ khác: mạch Hy Lạp hoá mà chính mục nêu là **Romaka và Pauliśa**, và hai siddhānta ấy theo truyền thống nghiên cứu phản ánh thiên văn Hy Lạp **tiền Ptolemy** (tham số kiểu Hipparchus), chứ không phải *Almagest*. Atlas lại **có sẵn** một mục Hipparchus: `CH03-BCE02-03 · Hipparchus xứ Nicaea`.

Câu thay thế đề xuất, nguyên văn:
> - CH03-BCE02-03 · kế thừa · qua trường phái

*Soi lại câu thay thế — và đây là chỗ tôi phải tự áp đúng cái thước vừa dùng:* `[KHÔNG KIỂM ĐƯỢC]` — tôi **không** mở được Pingree 1981 hay bản Neugebauer–Pingree 1970–71 để xác nhận tham số của Romaka/Pauliśa quy về Hipparchus chứ không phải Ptolemy; cả hai là sách in không có bản toàn văn truy cập được. Tôi **đã** kiểm được rằng `CH03-BCE02-03` là Hipparchus thật. Vì vậy đề xuất này **không được áp mù**: việc đúng là mở Pingree ra trước. Nếu vòng sau không mở được, thì cách an toàn là **bỏ hẳn dòng ID này** và để lại dòng tự do `Truyền thống siddhānta Ấn Độ` — mục vẫn đủ một dòng "Kế thừa từ" nên không chạm `lint.py:140`.

**Phát hiện 3 — CÂN NHẮC. "trước thế kỷ 5" có thể cắt hẹp hơn thực tế.**
Cụm này xuất hiện hai lần (dòng 63 và dòng 67: *"phần lớn thiên văn Ấn Độ trước thế kỷ 5 biến mất khỏi tầm với"* / *"Hiểu biết hiện đại về thiên văn Ấn Độ trước thế kỷ 5"*). Nhưng các siddhānta mà ông tóm là những bộ **đang lưu hành ở thời ông**, tức tới thế kỷ 6. `[KHÔNG KIỂM ĐƯỢC]` niên đại soạn của từng siddhānta. Nếu muốn một cách viết không cần kiểm thêm: thay "trước thế kỷ 5" bằng "**trước thời ông**" ở cả hai chỗ — mệnh đề ấy đúng theo chính định nghĩa của việc tóm lược, không cần một mốc thế kỷ nào.

**Phát hiện 4 — CÂN NHẮC.** `- Truyền thống siddhānta Ấn Độ · kế thừa · trực tiếp` (dòng 66) — đích không phải người; cùng loạt đã ghi cho P4.

---
## 5. `CH05-CE06-05 · Trần-na (Dignāga)` — dòng 68–82

**Đã kiểm được (không có phát hiện)**
- Q558272 = "Dignāga" / vi "Trần-na", P31 = Q5 ✔.
- `độ tin cậy niên đại: Thấp` → bỏ đối chiếu. Quyết định này **được dữ liệu đỡ**: cả P569 (480) lẫn P570 (540) của Q558272 đều có **0 reference** — tức Wikidata ở đây là suy diễn không nguồn, đúng loại ca mà `CONTRIBUTING.md:49` cảnh báo ✔.
- `vùng: Nam Á`; `lĩnh vực: Triết học` (1 lĩnh vực — hợp lệ); `câu hỏi lớn: Thực tại` ✔. ideas 95 / why 82 ✔.
- *Pramāṇasamuccaya*, hai pramāṇa, tri giác không khái niệm, apoha ✔.
- Nguồn: Hattori, *Dignāga, On Perception*, Harvard University Press, 1968 ✔; Hayes, *Dignaga on the Interpretation of Signs*, Kluwer, 1988 ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE04-11` = **Vasubandhu / Thế Thân** (`ch04.md:781`) ✔; `CH04-CE02-08` = **Nāgārjuna / Long Thọ** (`ch04.md:323`) ✔.
- **Một chỗ dùng mức bằng chứng ĐÚNG, đáng ghi vì cả nhóm hiếm**: dòng `CH04-CE04-11 · kế thừa · suy đoán học giả` khớp chính xác với câu văn xuôi "quan hệ thầy trò với Thế Thân … không có xác nhận đương thời". Mức bằng chứng và văn xuôi nói cùng một điều ✔.
- **Quy tắc 6 sạch**: `Bhāvaviveka` và `Sthiramati` không có mục ở đâu ✔.

**Phát hiện 1 — BẮT BUỘC. Đích tự do trong khi người ấy ĐÃ CÓ MỤC, và mức bằng chứng thì bất khả.**

Nguyên văn (dòng 81):
> - Pháp Xứng (Dharmakīrti) · kế thừa · trực tiếp

**Pháp Xứng có mục riêng ở `CH05-CE07-10`**, và chính mục ấy ghi `Kế thừa từ: - CH05-CE06-05 · kế thừa · trực tiếp`. Tức cạnh này **đã** là một cạnh ID ở một đầu, còn đầu kia vẫn là văn bản tự do. Hệ quả đo được: `reports/lint-ch05.txt` in `[INFO] CH05-CE07-10: kế thừa từ CH05-CE06-05 nhưng CH05-CE06-05 không ghi 'Ảnh hưởng tới' CH05-CE07-10`. Đây đúng thao tác bảo trì mà khối ghi chú "Một liên kết tự do được nâng thành ID" kê ra — và nó chưa được áp cho chính nhóm CE06.

Thêm một lỗi chồng lên: `trực tiếp` giữa Trần-na (mất k. 540) và Pháp Xứng (k. 600–660) là quan hệ người–người bất khả.

Câu thay thế đề xuất, nguyên văn:
> - CH05-CE07-10 · kế thừa · qua trường phái

*Soi lại câu thay thế:* tôi **đã mở** `CH05-CE07-10` và xác nhận đó là "Pháp Xứng (धर्मकीर्ति Dharmakīrti)" — không mượn ID chưa kiểm ✔. `qua trường phái` ∈ `EVIDENCE_LEVELS` ✔. Số dòng "Ảnh hưởng tới" giữ nguyên 2, dưới trần 3 của `lint.py:144` ✔. Sau khi sửa, dòng INFO đối xứng vẫn còn vì `CH05-CE07-10` ghi `trực tiếp` còn mục này ghi `qua trường phái` — **hai đầu cũng nên được đồng bộ về `qua trường phái`**, nếu không thì sửa một đầu chỉ dời chỗ cho sự lệch.

**Phát hiện 2 — NÊN. "Bánh xe lý do" bị gán nhầm nội dung.**

Nguyên văn (dòng 72):
> Ông nêu "bánh xe lý do" gồm ba điều kiện để kiểm một luận chứng đúng hay sai — tức một tiêu chuẩn hình thức thay cho việc viện dẫn uy tín kinh điển.

Câu này gộp hai thứ khác nhau của Trần-na: **hetucakra** ("bánh xe lý do") là một bảng **chín** ô phân loại các dạng lý do theo tương quan với sapakṣa/vipakṣa; còn tiêu chuẩn **ba** điều kiện là **trairūpya**. Viết "bánh xe lý do gồm ba điều kiện" là ghép tên của cái này vào nội dung của cái kia.

Câu thay thế đề xuất, nguyên văn:
> Ông nêu ba điều kiện mà một lý do phải thoả, rồi xếp các khả năng của lý do thành "bánh xe lý do" — tức một tiêu chuẩn hình thức thay cho việc viện dẫn uy tín kinh điển.

*Soi lại câu thay thế:* 40 chữ thay cho 34 → ideas thành **101 chữ**, trong trần ✔. Tôi **cố ý không** viết con số "chín" vào câu thay thế: `[KHÔNG KIỂM ĐƯỢC]` — tôi không mở được Hattori 1968 hay Hayes 1988 để xác nhận bảng ấy có đúng chín ô trong *Pramāṇasamuccaya* chứ không phải trong *Nyāyamukha*. Câu thay thế vì vậy chỉ nói "các khả năng", mệnh đề đứng được mà không cần con số; nếu vòng sau mở được nguồn thì thêm "chín" vào là an toàn.

**Phát hiện 3 — CÂN NHẮC.** `- Trường phái Nyāya · phản bác · trực tiếp` (dòng 82) — đích là một trường phái, không phải người; cùng loạt `trực tiếp` đã ghi cho P4.

---
## 6. `CH05-CE06-06 · Tùy Văn Đế` — dòng 83–100

**Đã kiểm được (không có phát hiện)**
- Q7418 = "Emperor Wen of Sui" / vi "Tùy Văn Đế", P31 = Q5 ✔.
- `năm: 541–604 CN`, **Cao** (±5). Wikidata 541-07-21 và 604-08-13 → lệch 0 và 0 ✔.
- `vùng: Đông Á`; `lĩnh vực: Chính trị/Nhà nước, Luật` ✔. ideas 122 / why 87 ✔ (đây là mục dài thứ tư của nhóm, còn 8 chữ dư).
- Diệt Trần 589 ✔; chia cắt tính từ 317 → 272 năm, "gần ba thế kỷ" đúng ✔; ngũ hình ✔; *Đường luật sớ nghị* ban 653 ✔; Tùy 581–618 = 37 năm ✔; quân điền ✔.
- Nguồn: *Tùy thư*, Ngụy Trưng và nhóm biên soạn, hoàn thành 636 ✔. Arthur F. Wright, *The Sui Dynasty: The Unification of China, A.D. 581–617*, Alfred A. Knopf, 1978 — nhan đề, phụ đề, NXB và năm đều khớp ✔.
- **Quy tắc 6 sạch**: `Tùy Dạng Đế` không có mục ở bất kỳ chapter nào ✔.
- Câu về nguồn thiên lệch ("sử do nhà Đường soạn, tức nguồn có lợi ích trong việc bôi xấu triều trước") là một rào đúng chỗ, không phải phát hiện ✔.

**Phát hiện 1 — NÊN. Một cạnh mà CẢ HAI đầu đều là văn bản tự do, dù cả hai người đều có mục.**

Nguyên văn (dòng 96):
> - Chế độ quân điền Bắc Ngụy · kế thừa · trực tiếp

Đầu kia của cạnh này là `CH04-CE05-12 · Bắc Nguỵ Hiếu Văn Đế`, và mục ấy ghi `Ảnh hưởng tới: - Chế độ quân điền ở nhà Tuỳ, Đường, Nhật Bản và Việt Nam · kế thừa · trực tiếp` — **cũng** là văn bản tự do. Hai mục có thật, nói về cùng một thiết chế, trỏ về phía nhau, mà không sinh một cạnh nào. Đây đúng cái mất mà khối ghi chú "Một liên kết tự do được nâng thành ID" gọi tên ("Cái mất không phải con số mà là **cạnh**") — chỉ khác là ở đây **cả hai** đầu đều tự do nên ngay cả dòng INFO của `lint.py:224-232` cũng không xuất hiện. Lint im lặng hoàn toàn.

Câu thay thế đề xuất, nguyên văn:
> - CH04-CE05-12 · kế thừa · qua trường phái

*Soi lại câu thay thế:* tôi **đã mở** `CH04-CE05-12` (`ch04.md:1023`) và xác nhận đó là "Bắc Nguỵ Hiếu Văn Đế (北魏孝文帝, Thác Bạt Hoằng)" ✔. Và tôi chọn `qua trường phái` chứ không phải `trực tiếp` **vì chính mục đích tự khai**: nó viết "công đặt ra nó thuộc về triều đình thời Phùng thị, **không phải về riêng ông**". Gán `trực tiếp` cho một cạnh mà đầu kia đã nói rõ người ấy không phải tác giả của thiết chế sẽ là đúng cái lỗi tôi vừa chẩn ở mục khác. Số dòng "Kế thừa từ" giữ nguyên 2 ✔. Sửa này cần làm **đối xứng** ở `CH04-CE05-12`, nếu không thì chỉ đổi một dòng INFO lấy một dòng INFO khác.

**Phát hiện 2 — NÊN. `Chế độ khoa cử · kế thừa · trực tiếp` nói mạnh hơn chính văn xuôi của mục.**

Nguyên văn (dòng 99):
> - Chế độ khoa cử · kế thừa · trực tiếp

Văn xuôi (dòng 87) viết thận trọng hơn hẳn: *"bắt đầu thay việc tiến cử theo gia thế bằng khảo hạch — **mầm** của khoa cử"*. "Mầm của" và `trực tiếp` không cùng một mức khẳng định; dòng quan hệ đang leo thang so với câu nó đỡ.

Câu thay thế đề xuất, nguyên văn:
> - Chế độ khoa cử · kế thừa · qua trường phái

*Soi lại:* `qua trường phái` ∈ `EVIDENCE_LEVELS` ✔; sau khi sửa, dòng quan hệ và văn xuôi nói cùng một mức, nên sửa này không mang lỗi mới vào.

**Phát hiện 3 — CÂN NHẮC. "Bộ Khai Hoàng luật năm 583".**
Nguyên văn (dòng 87): *"Bộ Khai Hoàng luật năm 583 rút hình phạt xuống năm bậc…"*. Niên hiệu Khai Hoàng bắt đầu 581 và bộ luật có một bản ban **581** rồi một bản sửa **583**; ghi trần "năm 583" bỏ mất việc đây là bản sửa. Cách viết không cần kiểm thêm gì: "**bản 583 của** Khai Hoàng luật". `[KHÔNG KIỂM ĐƯỢC]` mức chi tiết hai bản khác nhau ra sao — tôi không mở được *Tùy thư* 刑法志 trong vòng này (khối ghi chú chapter đã ghi `ctext.org` trả 200 nhưng 2.781 byte là trang chặn bot, và tôi không thử lại để khỏi đập vào cùng một bức tường).

---
## 7. `CH05-CE06-07 · Trí Di` — dòng 101–118

**Đã kiểm được (không có phát hiện)**
- Q197778 = "Zhiyi" / vi "Trí Di", P31 = Q5 ✔.
- `năm: 538–597 CN`, **Cao** (±5). Wikidata 538 (7 ref) và 597 (6 ref) → lệch 0 và 0; đây là mục có nền tham chiếu Wikidata dày nhất nhóm ✔.
- `vùng: Đông Á`; `lĩnh vực: Tôn giáo/Tâm linh, Triết học`; `câu hỏi lớn: Thực tại` ✔. ideas 105 / why 87 ✔.
- *Ma-ha chỉ quán* ✔; "nhất niệm tam thiên" ✔; Thiên Thai → Tendai → nền đào tạo các tổ phái Kamakura ✔.
- Nguồn: Paul Swanson, *Foundations of T'ien-T'ai Philosophy*, Asian Humanities Press, 1989 ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE05-07` = **Cưu-ma-la-thập / Kumārajīva** (`ch04.md:916`) — đúng người cho mạch Kinh Pháp Hoa ✔.
- **Một dòng `trực tiếp` dùng ĐÚNG**: `- Tuệ Tư · kế thừa · trực tiếp` là quan hệ thầy–trò người với người thật, đương thời. Trong cả nhóm CE06 đây là một trong rất ít dòng `trực tiếp` chịu được định nghĩa người–người ✔.
- **Quy tắc 6 sạch**: `Cát Tạng` và `Tuệ Tư` không có mục ở đâu ✔.

**Phát hiện 1 — NÊN (quy tắc 7). "Năm thời tám giáo" gán thẳng cho Trí Di, trong khi nguồn được dẫn là chỗ bàn rằng công thức ấy là hệ thống hoá đời sau.**

Nguyên văn (dòng 105):
> Trí Di giải bằng phán giáo — xếp toàn bộ kinh vào năm thời và tám giáo, coi mâu thuẫn là do Phật giảng tuỳ căn cơ người nghe chứ không phải do kinh sai — và đặt Kinh Pháp Hoa ở đỉnh.

Công thức 五時八教 ở dạng chuẩn hoá mà người đọc ngày nay biết lan ra chủ yếu qua *Thiên Thai tứ giáo nghi* của **Chegwan**, một tăng sĩ Triều Tiên thế kỷ 10 — tức sau Trí Di khoảng bốn thế kỷ. Việc phán giáo là của Trí Di thì không ai cãi; việc **con số và cái khung năm–tám** là của ông thì có. Đây là loại lỗi quy tắc 7 ở dạng mềm: nguồn tồn tại, đúng chủ đề, nhưng là nơi bàn về độ tin cậy của chính mệnh đề đang được nó đỡ.

Câu thay thế đề xuất, nguyên văn:
> Trí Di giải bằng phán giáo — xếp kinh theo thời giảng và theo cách giảng, coi mâu thuẫn là do Phật giảng tuỳ căn cơ người nghe chứ không phải do kinh sai — và đặt Kinh Pháp Hoa ở đỉnh; công thức "năm thời tám giáo" quen thuộc là bản hệ thống hoá đời sau.

*Soi lại câu thay thế:* 57 chữ thay cho 43 → ideas thành **119 chữ**, dưới trần 130 ✔. `[KHÔNG KIỂM ĐƯỢC]` — tôi **không** mở được Swanson 1989 để chỉ ra ông viết điều này ở trang nào, và tôi **cố ý không** viết tên Chegwan hay mốc thế kỷ 10 vào câu thay thế vì sẽ là đưa một mệnh đề chưa kiểm vào chính chỗ đang sửa. Câu thay thế chỉ nói "bản hệ thống hoá đời sau" — mệnh đề yếu hơn, và đúng kể cả khi niên đại cụ thể của Chegwan có sai. Nếu chủ repo muốn một câu hoàn toàn không có mệnh đề mới: **cắt vế sau dấu chấm phẩy đi**, phần còn lại vẫn đứng được và vẫn gỡ được lỗi gán sai, chỉ mất phần giải thích.

**Phát hiện 2 — NÊN. `trực tiếp` giữa hai người cách nhau 125 năm.**

Nguyên văn (dòng 109):
> - CH04-CE05-07 · kế thừa · trực tiếp

Cưu-ma-la-thập mất năm 413; Trí Di sinh 538. Quan hệ thật là Trí Di **đọc bản dịch** của ông, tức quan hệ văn bản. Đây là ca gần như trùng khít với ví dụ ở `CONTRIBUTING.md:53` ("`trực tiếp` giữa hai người cách nhau 130 năm mà vẫn 'đúng thứ tự'"), và lint không báo gì vì thứ tự niên đại thuận.

Câu thay thế đề xuất, nguyên văn:
> - CH04-CE05-07 · kế thừa · qua trường phái

*Soi lại:* ID giữ nguyên và đã được tôi kiểm là đúng người ✔; `qua trường phái` ∈ `EVIDENCE_LEVELS` ✔; số dòng không đổi ✔. Lưu ý đừng sửa quá tay: dòng `Tuệ Tư · kế thừa · trực tiếp` ngay dưới **phải giữ nguyên** — đó là một trong số ít dòng `trực tiếp` đúng nghĩa người–người của cả nhóm.

---
## 8. `CH05-CE06-08 · Bồ-đề-đạt-ma` — dòng 119–136

**Đã kiểm được (không có phát hiện)**
- Q187172 = "Bodhidharma" / vi "Bồ-đề-đạt-ma", P31 = Q5 ✔.
- `độ tin cậy niên đại: Thấp` → bỏ đối chiếu. Được dữ liệu đỡ: Wikidata có **hai** giá trị P569 cạnh nhau (483 và 440), tức chính Wikidata cũng không chốt ✔. Mục chọn k. 440 và khai Thấp — một cách xử đúng, không phải chép một trong hai rồi im.
- `vùng: Đông Á`; `lĩnh vực: Tôn giáo/Tâm linh` (1 lĩnh vực — hợp lệ); `câu hỏi lớn: Con người` ✔. ideas 108 / why 92 ✔.
- *Lạc Dương già lam ký*, Dương Huyễn Chi, k. 547 ✔; *Nhị nhập tứ hạnh luận*, "bích quán", bốn hạnh ✔; việc các chi tiết nổi tiếng chỉ có trong đăng lục từ thế kỷ 8 ✔.
- Nguồn: John McRae, *Seeing Through Zen*, University of California Press, 2003 ✔. Bernard Faure, "Bodhidharma as Textual and Religious Paradigm", *History of Religions* **25** (1986) — tập và năm khớp ✔.
- Chỉ **một** dòng "Kế thừa từ" — hợp lệ, `lint.py:138-140` chỉ báo lỗi khi **rỗng** ✔.
- **Quy tắc 6 sạch**: `Huệ Khả` và `Tăng Xán` không có mục ở đâu. (`Tăng Xán` có xuất hiện ở `ch90.md:98` nhưng chỉ trong một dòng quan hệ tự do, không phải tiêu đề mục ✔.)

**Phát hiện 1 — BẮT BUỘC. Đích tự do trong khi Huệ Năng ĐÃ CÓ MỤC.**

Nguyên văn (dòng 135):
> - Huệ Năng và Thiền tông Trung Hoa · kế thừa · qua trường phái

**Huệ Năng có mục riêng ở `CH05-CE07-07`**, và mục ấy ghi `Kế thừa từ: - CH05-CE06-08 · kế thừa · qua trường phái`. Cạnh đã là ID ở một đầu, tự do ở đầu kia; `reports/lint-ch05.txt` in đúng dòng ấy: `[INFO] CH05-CE07-07: kế thừa từ CH05-CE06-08 nhưng CH05-CE06-08 không ghi 'Ảnh hưởng tới' CH05-CE07-07`.

Đây là ca thứ hai cùng hình dạng trong một nhóm mười hai mục (ca thứ nhất: CE06-05 → Pháp Xứng). Hai ca trong cùng một nhóm, cùng trỏ sang nhóm CE07 liền kề, nghĩa là thao tác grep mà khối ghi chú kê ra **chưa từng được chạy cho nhóm này**.

Câu thay thế đề xuất, nguyên văn:
> - CH05-CE07-07 · kế thừa · qua trường phái

*Soi lại câu thay thế:* tôi **đã mở** `CH05-CE07-07` và xác nhận đó là "Huệ Năng (慧能 Huìnéng, Lục tổ)" ✔. Mức `qua trường phái` giữ nguyên như bản gốc và **khớp** với mức mà đầu kia đã ghi, nên sau khi sửa hai đầu cân nhau và dòng INFO biến mất ✔. Số dòng "Ảnh hưởng tới" giữ nguyên 2, dưới trần 3 ✔. Lưu ý: cụm "và Thiền tông Trung Hoa" bị mất khi nâng ID; nếu muốn giữ, dòng thứ ba `- Thiền tông Trung Hoa · kế thừa · qua trường phái` vẫn nằm trong trần 3 — nhưng tôi **không** khuyến nghị, vì Thiền tông Trung Hoa đã nằm trong dòng "Zen Nhật Bản, Seon Triều Tiên và Thiền Việt Nam" ở ngay dưới theo nghĩa rộng hơn.

**Phát hiện 2 — NÊN. Mục tự đặt nguyên tắc tách nguồn thế kỷ 6 khỏi truyền thuyết thế kỷ 8, rồi tự phá nguyên tắc ấy ở trường `nơi:` và ở câu cuối.**

Nguyên văn (dòng 131):
> Vùng để Đông Á theo quy ước nơi hoạt động chính, dù ông sinh ở Nam Ấn.

Và `nơi: Nam Ấn Độ, rồi Lạc Dương và Tung Sơn thuộc Bắc Ngụy` (dòng 120).

Vấn đề: mục tuyên bố "cố ý tách nguồn thế kỷ 6 khỏi truyền thuyết thế kỷ 8", nhưng nguồn thế kỷ 6 mà chính mục dẫn — *Lạc Dương già lam ký*, k. 547 — theo đúng mô tả của mục chỉ nói "một tăng sĩ **Tây Vực**". Xuất thân **Nam Ấn** không đến từ nguồn ấy; nó đến từ tầng tư liệu muộn hơn. Thế mà Nam Ấn lại được ghi như sự kiện ở cả trường `nơi:` lẫn câu cuối "Vì sao chọn", trong khi "chín năm ngó vách" thì bị gắn nhãn truyền thuyết. Hai chi tiết cùng hạng nguồn, hai cách đối xử khác nhau.

Câu thay thế đề xuất, nguyên văn:
> Vùng để Đông Á theo quy ước nơi hoạt động chính; xuất thân Nam Ấn không có trong nguồn thế kỷ 6 mà đến từ nguồn muộn hơn.

*Soi lại câu thay thế:* 28 chữ thay cho 17 → why thành **103 chữ**, vẫn dưới trần 104 — **sát trần, chỉ dư 1 chữ**, nên nếu chủ repo muốn thêm bất cứ gì khác vào "Vì sao chọn" thì phải cắt chỗ khác. `[KHÔNG KIỂM ĐƯỢC]` — tôi **không** mở được nguyên văn *Lạc Dương già lam ký* trong vòng này (khối ghi chú chapter đã ghi `ctext.org` trả trang chặn bot, và tôi không muốn đưa vào báo cáo một trích dẫn chữ Hán mà tôi không tự đọc được từ nguồn). Vì vậy câu thay thế của tôi **chỉ dựa vào điều chính mục đã khẳng định** (nguồn 547 nói "tăng sĩ Tây Vực") chứ không thêm chi tiết nào mới, và nó **cố ý không** nói nguồn muộn hơn là nguồn nào. Nếu cắt vế "mà đến từ nguồn muộn hơn", câu vẫn đứng được dưới dạng ngắn hơn và vẫn gỡ được mâu thuẫn.

Kèm theo: trường `nơi:` nên bỏ "Nam Ấn Độ" hoặc ghi kèm rào, vì `nơi:` là thứ in ra trang và nó đang phát biểu một mệnh đề mà chính mục xếp ở hạng nguồn thấp.

---
## 9. `CH05-CE06-09 · Kaleb xứ Aksum` — dòng 137–151

**Đã kiểm được (không có phát hiện)**
- Q705378 = "Kaléb", P31 = Q5 ✔.
- `năm: trị vì k. 510 – k. 540 CN` — chuỗi "trị vì" đứng **đầu** trường, đúng yêu cầu của `NON_BIO_YEARS_RE` (`common.py:133`), nên `lint.py:296` bỏ đối chiếu Wikidata thay vì so nhầm loại ✔. Quyết định ấy được dữ liệu đỡ: P569 của Q705378 ở `precision 7` (thế kỷ) và P570 540 có **0 reference** — đúng như khối ghi chú chapter đã khai ✔.
- `vùng: Châu Phi hạ Sahara`; `lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh` ✔. why 85 ✔.
- Robin 2008: nhan đề nguyên văn "Joseph, dernier roi de Ḥimyar (de 522 à 525, ou une des années suivantes)", *Jerusalem Studies in Arabic and Islam* **34** (2008), tr. **1–124** — khớp từng thành phần ✔. Và cách mục dùng nó **đúng chiều**: nhan đề của Robin tự nó mang sự lưỡng lự, và mục viện nó để biện minh cho việc **không** chốt năm, chứ không phải để chốt ✔.
- `Yūsuf ʾAsʾar Yathʾar`, `Sumūyafaʿ Ashwaʿ`, Abraha lật vua bù nhìn rồi đánh bại hai chiến dịch trừng phạt ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE04-09` = **Ezana xứ Aksum** (`ch04.md:747`) — đúng người, đúng vương quốc ✔.
- `- Truyền thống "Năm Con Voi" trong sử liệu Hồi giáo · kế thừa · suy đoán học giả` — mức bằng chứng dùng **đúng** cho một mạch truyền thuyết ✔.

**Phát hiện 1 — BẮT BUỘC. Một dòng Nguồn không kiểm được bằng bất kỳ cách nào, và là chỗ duy nhất đỡ cho mốc 529.**

Nguyên văn (dòng 151):
> George Hatke, mục "Aksum", trong *A Thematic Dictionary of Ancient Arabia*

Tôi tra OpenLibrary Search API và Crossref API cho nhan đề này: **không có bản ghi nào** khớp (OpenLibrary trả một kết quả không liên quan; Crossref trả các nhan đề khác hẳn). Dòng trích cũng **không có** nhà xuất bản, **không có** năm, **không có** số trang và **không có** URL — tức ngay cả khi tác phẩm tồn tại, dòng này không đưa người đọc tới được nó. Công trình Hatke mà tôi kiểm được là *Aksum and Nubia* (2013), và nó là về Nubia chứ không phải Nam Arabia.

Điều này quan trọng vì mốc **mùa xuân 529** ở dòng 149 chỉ dựa vào đúng nguồn này; khối ghi chú chapter cũng dựng cả một lập luận chronology trên nó.

`[KHÔNG KIỂM ĐƯỢC]`: **vắng bản ghi không chứng minh tác phẩm không tồn tại.** Tôi không tuyên bố đây là nguồn bịa. Điều tôi xác nhận được là: dòng trích như đang viết thì không kiểm được, và tôi không tìm ra tác phẩm ấy bằng hai cơ sở dữ liệu thư mục.

Câu thay thế đề xuất, nguyên văn (nếu không xác minh được nguồn, cho dòng 149):
> Mục để Trung bình chứ không Cao vì chính chiến dịch nổi tiếng nhất chưa chốt được năm: Robin đặt nó sau Lễ Ngũ Tuần 525 "hoặc một trong những năm tiếp theo".

*Soi lại câu thay thế:* 33 chữ thay cho 38 → why thành **80 chữ**, trong trần ✔. Câu này **chỉ** giữ lại mệnh đề tôi đã kiểm được tận nhan đề (Robin), và bỏ mệnh đề duy nhất tôi không kiểm được (Hatke/529) — tức nó không mang theo chính cái lỗi nó đang chẩn. Lưu ý cái giá: bỏ Hatke đi thì câu mất **đối trọng** và chỉ còn một ý kiến, nên lý do để Trung bình yếu hơn. Vì vậy **thứ tự ưu tiên đúng là đi tìm dòng trích đầy đủ trước** (luận án Princeton 2011 của Hatke về quan hệ Aksum–Ḥimyar là đầu mối đáng thử), và chỉ dùng câu rút gọn này nếu tìm không ra.

**Phát hiện 2 — NÊN. Không nêu đích danh ứng viên bị loại nào.**
"Vì sao chọn" (dòng 149) không có một cái tên bị loại nào, trong khi template §5 (`prompts/atlas-prompt.md`) đòi "nêu ĐÍCH DANH 1–2 người cùng lĩnh vực, cùng thời đã được cân nhắc". Bốn mục của nhóm mắc điều này (CE06-09, -10, -11, -12), khớp đúng với con số **CE06 8/12** mà khối ghi chú chapter đã tự đo. Để **NÊN** chứ không BẮT BUỘC vì chapter đã khai và đẩy sang P4 như một việc ở tầng chapter, không phải vá từng mục — nhưng nó vẫn là chỗ lệch template, không phải chỗ đã xong.

**Phát hiện 3 — `[KHÔNG KIỂM ĐƯỢC]`. "Bi ký RIÉth 191 (Aksum, chữ musnad)".**
Tôi **không** mở được RIÉth 191 hay bản ghi DASI trong vòng này — và khối ghi chú chapter đã ghi sẵn rằng DASI trả về **không ổn định** (lúc 200 trang thật, lúc 0 byte), nên tôi không coi một lần kéo hỏng là bằng chứng. Hai chỗ đáng soi khi mở được: (a) một bi ký **ở Aksum** mà khắc bằng **musnad** Nam Arabia là một mệnh đề mạnh, và mục không nói vì sao; (b) khối ghi chú chapter mô tả cấu hình tư liệu khác — bi ký **Geʿez** ở Maʾrib và Ẓafār, cộng hai văn bản **Sabaic** — nên nhãn "chữ musnad" dán cho RIÉth 191 cần được đối chiếu lại với chính khối ấy.

**Phát hiện 4 — CÂN NHẮC.** `- Truyền thống vương quyền Ḥimyar và lối xưng hiệu Nam Arabia · kế thừa · trực tiếp` (dòng 150) — đích không phải người; cùng loạt `trực tiếp` đã ghi cho P4.

**Phát hiện 5 — CÂN NHẮC.** ideas = **130 chữ**, tức đúng ngưỡng cảnh báo của `lint.py:133` (`abs(130-100) > 0.3*100` là False, nhưng 131 sẽ bật WARN). Mục này không còn chỗ để thêm một chữ nào; nếu phải bổ sung rào nguồn cho bi ký thì phải cắt chỗ khác trước.

---
## 10. `CH05-CE06-10 · Bumin Qaghan` — dòng 152–166

**Đã kiểm được (không có phát hiện)**
- Q29001 = "Bumin Qaghan", P31 = Q5 ✔.
- `năm: hoạt động 545–552 CN` — "hoạt động" đứng **đầu** trường, khớp `NON_BIO_YEARS_RE` ✔. Và quyết định **không** chép năm sinh được tôi xác nhận độc lập trên Wikidata: P569 = +0490 ở `precision 9`, **0 reference**. Khối ghi chú chapter mô tả đúng dữ liệu ✔.
- `vùng: Đông Á` với lý do khai thành văn, theo đúng tiền lệ `CH03-BCE02-12` và `CONTRIBUTING.md:70` (`REGIONS` không có ô cho Nội Á) ✔. `lĩnh vực: Chính trị/Nhà nước, Quân sự` ✔. why 79 ✔.
- 周書 **quyển 50** đúng là **liệt truyện 42, 異域下**; 令狐德棻; hoàn thành **636** ✔. 北史 **quyển 99** đúng là quyển về Đột Quyết ✔.
- *History of Civilizations of Central Asia* **tập III** đúng là tập "The crossroads of civilizations: A.D. 250 to 750", và **chương 14** đúng là chương về đế chế Türk, bắt đầu khoảng tr. 327 ✔ — tức số tập, số chương và số trang đều không phải số sinh ra, khác hẳn hình dạng lỗi mà `CONTRIBUTING.md:48` cảnh báo.
- **Liên kết ID trỏ đúng người**: `CH03-BCE02-12` = **Mặc Đốn thiền vu** (`ch03.md:607`) ✔. Và quan hệ `tương đồng độc lập` được dùng đúng tinh thần `prompts/atlas-prompt.md` (khẳng định **không** có tiếp xúc), nên `lint.py:236` cũng loại nó khỏi phép kiểm nghịch niên đại một cách chính đáng ✔.

**Phát hiện 1 — BẮT BUỘC. `phản bác` dùng cho một cuộc lật đổ quân sự, đi ngược một quyết định đã thành văn của chính dự án.**

Nguyên văn (dòng 164):
> - Nhu Nhiên hãn quốc · phản bác · trực tiếp

`RELATION_TYPES` (`common.py:78`) là từ vựng về quan hệ **tư tưởng**. Dự án đã xử đúng ca này **hai lần** và ghi lại: Ghi chú biên tập của `content/ch04.md` viết *"liên kết Hán Quang Vũ Đế 'phản bác' Hai Bà Trưng cũng bị gỡ: **đàn áp quân sự không phải quan hệ tư tưởng**, cùng lý do đã gỡ cặp Hán Vũ Đế và Triệu Đà ở Chapter 3"*. Dòng này là ca thứ ba, cùng hình dạng, chưa bị gỡ — và nó còn nặng hơn hai ca kia một bậc vì đích thậm chí không phải một người mà là một chính thể, lại gắn mức `trực tiếp`.

Câu thay thế đề xuất, nguyên văn: **gỡ hẳn dòng.**

*Soi lại đề xuất:* gỡ dòng này thì "Kế thừa từ" còn **một** dòng (`CH03-BCE02-12 · tương đồng độc lập · suy đoán học giả`) — vẫn hợp lệ, vì `lint.py:138-140` chỉ báo lỗi khi mục **rỗng**, và mục CE06-08 trong chính nhóm này cũng chỉ có một dòng ✔. Không mất thông tin: sự kiện đã nằm trong văn xuôi ("đầu 552 ông đánh bại Nhu Nhiên"), đúng như cách ch04 xử hai ca trước ("Cả hai sự kiện vẫn được nêu trong phần văn xuôi của mục tương ứng") ✔. Tôi **không** đề xuất đổi `phản bác` thành một loại khác, vì không loại nào trong bốn loại mô tả đúng việc một hãn quốc lật một hãn quốc.

**Phát hiện 2 — NÊN. Dòng Nguồn bỏ mất đồng tác giả, và tự mâu thuẫn với khối ghi chú của chính nhóm.**

Nguyên văn (dòng 166):
> Denis Sinor, chương 14 trong *History of Civilizations of Central Asia*, tập III (UNESCO), tr. 328.

Chương 14 của tập III là của **D. Sinor và S. G. Klyashtorny**. Chính khối ghi chú biên tập của nhóm này dẫn đúng tên kép — *"Sinor và Klyashtorny (tr. 327) **xác nhận** Istämi là em Bumin"* — nên hai chỗ trong cùng một file đang gán cùng một chương cho hai tập tác giả khác nhau.

Câu thay thế đề xuất, nguyên văn:
> Denis Sinor và S. G. Klyashtorny, chương 14 trong *History of Civilizations of Central Asia*, tập III (UNESCO), tr. 328.

*Soi lại:* dòng Nguồn không chịu trần chữ nào ✔. Tên đồng tác giả tôi lấy từ **chính file này** (khối Ghi chú biên tập), không phải từ trí nhớ, nên nó đã được một nguồn trong repo đỡ ✔.

**Phát hiện 3 — NÊN. Mốc 563 quy cho Menander Protector có thể sai người ghi chép.**

Nguyên văn (dòng 158):
> còn đường tới Byzantium thì chính sử không chép một dòng: hai sứ đoàn 563 và 568 chỉ biết qua Menander Protector, thuộc cánh Tây.

Sứ đoàn **568** (Maniakh tới Constantinopolis) đúng là của Menander. Tiếp xúc **563** thì thường được quy cho **Theophanes Byzantinus** (còn qua Photius), không phải Menander. Nếu đúng vậy thì chữ "chỉ biết qua Menander Protector" đang phủ lên cả hai mốc một nguồn chỉ đỡ được một.

Câu thay thế đề xuất, nguyên văn:
> còn đường tới Byzantium thì chính sử không chép một dòng: sứ đoàn năm 568 chỉ biết qua Menander Protector, và nó thuộc cánh Tây.

*Soi lại câu thay thế — và đây là chỗ tôi phải tự kiềm:* 25 chữ thay cho 25 → ideas giữ nguyên **130 chữ**, đúng trần, không bật WARN ✔. `[KHÔNG KIỂM ĐƯỢC]` — tôi **không** mở được bản Blockley của Menander để xác nhận mốc 563 có hay không có trong đó, nên tôi **cố ý không** viết tên Theophanes Byzantinus vào câu thay thế. Câu thay thế chỉ **bỏ** mốc tôi không kiểm được và giữ mốc tôi kiểm được; nếu vòng sau mở được Menander và thấy 563 có trong đó thật, chỉ cần thêm lại — chứ bản sửa này không khẳng định điều ngược lại.

**Phát hiện 4 — CÂN NHẮC. "phá Hiệt Đát" không kèm chữ Hán.**
Mục rất kỷ luật trong việc kèm chữ Hán cho tên riêng khó (`鄧叔子`, `伊利可汗`, `都斤山`), nhưng "Hiệt Đát" thì không. `[KHÔNG KIỂM ĐƯỢC]` dạng phiên Hán–Việt chuẩn cho 嚈噠; các dạng gặp được gồm cả "Yếm Đát". Cách xử nhất quán với phần còn lại của mục: ghi "Hiệt Đát (嚈噠)".

**Phát hiện 5 — CÂN NHẮC.** ideas = **130 chữ**, chạm trần; không còn chỗ thêm.

---
## 11. `CH05-CE06-11 · Bhavavarman I` — dòng 167–181

**Đã kiểm được (không có phát hiện)** — đây là mục có tỉ lệ mệnh đề **kiểm được tận nguồn** cao nhất nhóm, vì cả hai nguồn đều là PDF mở được.

- Q854920 = "Bhavavarman I", P31 = Q5 ✔.
- `năm: trị vì k. 550 – k. 600 CN` — "trị vì" đứng đầu trường ✔, và khung này **khớp nguyên văn** nguồn được dẫn: Heng & Lavy viết "Bhavavarman I (reigned around 550–600)" ✔.
- `độ tin cậy niên đại: Thấp` → bỏ đối chiếu, nên bẫy Wikidata của Q854920 (P569 `+0600` ở **precision 7** = thế kỷ, cạnh P570 `+0600` ở **precision 9** = năm, trên cùng một giá trị thô) không chạm được vào lint ✔. Khối ghi chú chapter mô tả bẫy này đúng từng chi tiết.
- `vùng: Đông Nam Á`; `lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh` ✔. ideas 126 / why 82 ✔.
- **Mệnh đề "mục Đông Nam Á đầu tiên của atlas chính" — kiểm được và ĐÚNG**: grep `vùng: Đông Nam Á` trên `content/ch01..ch05.md` trả đúng bốn mục, và ba mục kia đều **sau** nhóm này (`CH05-CE09-01`, `CH05-CE10-05`, `CH05-CE10-06`); `ch90.md` là phụ lục, `C.is_main` loại nó khỏi thống kê toàn cục (`lint.py:212-213`) ✔.
- **Hai URL đều sống và có nội dung thật** (không phải ca 200/0 byte): Vickery → `200`, **205.860 byte**, `application/pdf`; Heng & Lavy → `200`, **998.294 byte**, `application/pdf`. Tôi giải nén stream và đọc nội dung, không dừng ở mã trạng thái ✔.
- **Dòng trích Vickery khớp từng thành phần với trang đầu của chính PDF**: `"What and Where was Chenla?", Recherches nouvelles sur le Cambodge. Publiés sous la direction de F. Bizot. École française d'Extrême-Orient, Paris, 1994, pp. 197-212.` — nhan đề, sách, chủ biên, NXB, năm **và số trang 197–212** đều đúng ✔. Đây là dòng trích tốt nhất của cả nhóm.
- **Mệnh đề nặng nhất của mục được xác nhận tận nguyên văn.** Mục viết: *"con số 598 mà Coedès rút từ K.151 là mốc duy nhất, và chính Vickery cho thấy Coedès đã dùng nó sai ngữ cảnh."* Vickery 1994 viết đúng điều đó: Coedès *"took the date 598 from inscription K151 … and inserted it into a section of Ma Touan-lin torn out of"* ngữ cảnh. Không bị dùng ngược, không bị thổi ✔.
- **Gambhīreśvara được nguồn thứ hai đỡ**: Heng & Lavy viết bằng chứng bi ký (**gồm K.439**) cho thấy thần chính của nhóm bắc là một dạng Śiva tên Gambhireshvara, "particularly associated with King Bhavavarman I" ✔.
- **K.151 và K.439 ở Sambor Prei Kuk** ✔ (Heng & Lavy nêu K.151, K.439, K.604, K.1250 là bi ký ở Īśānapura).
- Câu rào "Chapter 90 là phụ lục Việt Nam, nằm ngoài thống kê toàn cục" đúng với hành vi code ✔.

**Phát hiện 1 — NÊN. K.53 bị đặt sai địa điểm, theo chính nguồn được dẫn.**

Nguyên văn (dòng 171):
> K.151 và K.439 ở Sambor Prei Kuk, K.53 ở Ba Phnom.

Và trường `nơi:` (dòng 168): `… từ Sambor Prei Kuk (Kompong Thom) tới Ba Phnom (Prey Veng)`.

Bản đồ địa điểm của Heng & Lavy — nguồn thứ hai của chính mục — đánh số 12 là **"Kdei Ang (K.53)"**, không phải Ba Phnom (Ba Phnom không xuất hiện trong danh sách địa điểm của họ). Cả hai đều ở Prey Veng nên tỉnh thì đúng, nhưng tên di chỉ thì sai, và nó sai ở **hai chỗ**: trong văn xuôi và trong trường `nơi:` vốn là thứ in ra trang.

Câu thay thế đề xuất, nguyên văn (dòng 171):
> K.151 và K.439 ở Sambor Prei Kuk, K.53 ở Kdei Ang.

và cho trường `nơi:`:
> nơi: lưu vực Mekong ở Campuchia, từ Sambor Prei Kuk (Kompong Thom) tới Kdei Ang (Prey Veng)

*Soi lại câu thay thế:* "Kdei Ang" lấy trực tiếp từ bản đồ trong PDF Heng & Lavy mà tôi đã mở và đọc, không phải từ trí nhớ ✔. Số chữ giảm 1 → ideas thành **125**, trong trần ✔. Trường `nơi:` giữ nguyên cấu trúc "di chỉ (tỉnh)" nên không phá quy ước nào ✔. `[KHÔNG KIỂM ĐƯỢC]`: tôi **không** xác nhận được nội dung K.53 nói gì — tôi chỉ xác nhận được **nó ở đâu**. Nếu mục muốn giữ một mệnh đề về nội dung K.53 thì mệnh đề ấy còn phải kiểm riêng.

**Phát hiện 2 — NÊN. Không nêu đích danh ứng viên bị loại nào.**
"Vì sao chọn" (dòng 177) giải thích rất kỹ **vì sao mục mỏng**, nhưng không nêu một tên bị loại nào — lệch template §5. Cùng loạt với CE06-09, -10, -12. Ở mục này còn 22 chữ dư trong `why` (82/104) nên có chỗ để thêm.

**Phát hiện 3 — CÂN NHẮC. Mục chắc hơn nguồn một bậc ở hai chỗ.**
(a) *"mà giới nghiên cứu thấy gắn riêng với ông"* — Heng & Lavy viết "**seems to** have been particularly associated" và thêm "**if this is true**" cho bước gắn nhóm bắc với kinh đô của ông. "Thấy gắn riêng" bỏ mất cả hai lớp rào.
(b) *"Ông là vị vua đầu tiên ở vùng nội địa Campuchia để lại một cụm bi ký Phạn ngữ tại chỗ đủ dựng lại một triều đại"* — Vickery xếp ông cạnh **Citrasena** và cha **Vīravarman** như một cụm có hồ sơ bi ký chung. `[KHÔNG KIỂM ĐƯỢC]` chữ "đầu tiên" ở mức chặt: tôi không đọc được đủ Vickery để biết bi ký của Vīravarman có sớm hơn không.

**Phát hiện 4 — CÂN NHẮC.** `- Truyền thống bi ký Phạn ngữ và vương quyền Śaiva Nam Á · kế thừa · trực tiếp` (dòng 180) — đích không phải người. Cùng loạt đã ghi cho P4.

---
## 12. `CH05-CE06-12 · Boethius` — dòng 182–196

**Đã kiểm được (không có phát hiện)**
- Q102851 = "Boethius", P31 = Q5 ✔.
- `năm: k. 477 – k. 526 CN`, **Trung bình** (±25). Wikidata: P569 preferred 480 (9 ref) cạnh 475 ở `precision 8`; P570 preferred 524 (3 ref) cạnh 525 ở `precision 8`. Lệch lớn nhất so với atlas là 3 và 2 năm — sạch ✔. Khối "Bốn điều không được viết về Boethius" nói đúng về cặp 480/524 ở rank preferred, và việc chọn Trung bình thay vì Cao để khỏi chọn phe là một quyết định có lý do thành văn ✔.
- `vùng: Châu Âu`; `lĩnh vực: Triết học, Văn học`; `câu hỏi lớn: Thực tại` ✔. why 84 ✔.
- **Hai URL sống, đúng tác giả, đúng chủ đề**: SEP "boethius" → `200`, **90.315 byte**, và metadata trang xác nhận tác giả là **John Marenbon**, đúng như dòng Nguồn ghi ✔. SEP "medieval-literary" → `200`, **144.744 byte**, tác giả **Eileen Sweeney**, và nhắc Boethius **35 lần** nên đúng chủ đề chứ không phải ca "bài không nhắc nhân vật một chữ nào" mà `CONTRIBUTING.md:47` cảnh báo ✔.
- **Hai mệnh đề được SEP xác nhận nguyên văn**: bản dịch *Phân tích hậu* **đã mất** ("except for that of the Posterior Analytics, which was lost") ✔; **Jean de Meun và Chaucer** dịch *Consolatio* sang ngôn ngữ bản địa ✔.
- **Liên kết ID trỏ đúng người**: `CH04-CE03-03` = **Porphyry xứ Tyre** ✔; `CH03-BCE04-02` = **Aristotle** ✔. Cả hai ở mức `qua trường phái`, đúng mức cho quan hệ văn bản cách nhiều thế kỷ — đây là mục dùng mức bằng chứng cẩn thận nhất ở phần "Kế thừa từ" của cả nhóm ✔.

**Phát hiện 1 — BẮT BUỘC. Một niên đại trái với chính nguồn được dẫn.**

Nguyên văn (dòng 186):
> phần Organon còn lại phải tới đầu thế kỷ 13 mới lưu hành rộng, vẫn qua bản dịch Latinh của ông được tìm lại.

SEP "Boethius" (Marenbon) — nguồn đầu tiên của chính mục — viết: *Prior Analytics* "became generally available in the **later twelfth century**". Bài cũng nói các bình luận của Boethius là công cụ chính của giới logic "**from the ninth to the twelfth centuries**", và rằng **từ** thế kỷ 13 ảnh hưởng của ông mới **giảm**. Mục đang dời mốc sang muộn hơn một thế hệ, và dời đúng về phía mà nguồn nói ngược.

Câu thay thế đề xuất, nguyên văn:
> phần Organon còn lại phải tới cuối thế kỷ 12 mới lưu hành rộng, vẫn qua bản dịch Latinh của ông được tìm lại.

*Soi lại câu thay thế:* **24 chữ, đúng bằng câu cũ** → ideas giữ nguyên **130 chữ**, không vượt trần ✔ — điểm này quan trọng vì mục đang chạm trần, nên một bản sửa dài hơn dù chỉ một chữ cũng sẽ bật WARN. "Cuối thế kỷ 12" là bản dịch sát của "later twelfth century" trong chính nguồn, không phải suy diễn của tôi ✔.

**Phát hiện 2 — NÊN. Một mệnh đề đã rữa: lỗi mà mục tự nhận là đang sửa thì nay đã được sửa rồi.**

Nguyên văn (dòng 188):
> Chọn ông cũng là sửa một lỗi nội tại: tên ông đã hai lần xuất hiện trong atlas như cơ chế truyền cho Porphyry ở `CH04-CE03-03`, một lần ngay trong dòng quan hệ, mà chưa bao giờ có mục riêng.

Tôi mở `CH04-CE03-03` ra đọc: dòng quan hệ hiện tại là `- CH05-CE06-12 · kế thừa · qua trường phái`, tức **không còn** mang tên Boethius; hiện ông chỉ còn xuất hiện **một** lần trong mục ấy, ở văn xuôi. Khối Ghi chú biên tập có câu đính chính ("Dòng quan hệ cũ nay đã được nối vào một người thật") nhưng **thân mục thì không**, nên người đọc chỉ đọc mục sẽ đi tìm một dòng không còn tồn tại.

Câu thay thế đề xuất, nguyên văn:
> Chọn ông cũng là sửa một lỗi nội tại: mục Porphyry `CH04-CE03-03` từng dùng tên ông làm cơ chế truyền ngay trong dòng quan hệ, mà ông chưa bao giờ có mục riêng; dòng ấy nay đã trỏ về mục này.

*Soi lại câu thay thế:* 41 chữ thay cho 40 → why thành **85 chữ**, dưới trần 104 ✔. Mệnh đề "dòng ấy nay đã trỏ về mục này" tôi **đã kiểm trực tiếp** bằng cách đọc `content/ch04.md` ✔. Tôi **bỏ** con số "hai lần" khỏi câu thay thế: `[KHÔNG KIỂM ĐƯỢC]` trạng thái cũ (trước khi sửa) của file, vì tôi chỉ thấy được bản hiện tại chứ không chạy lịch sử git; và quan trọng hơn, một con số đếm trạng thái file là đúng loại số sẽ rữa lại ở vòng sau — viết lại nó sẽ là tái lập chính cái lỗi tôi vừa chẩn. Câu thay thế dùng thì quá khứ ("từng") cộng một mệnh đề hiện tại kiểm được, nên nó không rữa theo cách ấy nữa.

**Phát hiện 3 — NÊN. Không nêu đích danh ứng viên bị loại nào.**
"Vì sao chọn" (dòng 188) không có tên người bị loại. **Gregory xứ Tours** và **Maniakh** đều được nêu — nhưng chỉ ở Ghi chú biên tập, và grep xác nhận cả hai không có mục ở đâu, tức cả hai **hợp lệ** làm ứng viên bị loại theo quy tắc 6. Tức đây là ca dễ sửa nhất trong bốn ca thiếu: tên có sẵn, đã được kiểm, chỉ chưa được đưa vào mục. `why` còn 20 chữ dư.

**Phát hiện 4 — CÂN NHẮC. Hai mục gán hai mức bằng chứng khác nhau cho cùng một đích tự do.**
Mục này: `- Tranh luận về vấn đề phổ quát trong kinh viện trung cổ · kế thừa · **trực tiếp**` (dòng 195).
Mục Porphyry `CH04-CE03-03`: `- Tranh luận về vấn đề phổ quát thời trung cổ · kế thừa · **qua trường phái**`.
Cùng một đích (chỉ lệch hai chữ trong cách gọi), hai mức. Lint không thấy gì vì đích tự do không được giải. Ngoài việc đích không phải người, bản thân sự lệch này là một chỉ dấu rằng mức bằng chứng đang được chọn theo cảm giác từng mục.

**Phát hiện 5 — CÂN NHẮC. Dòng Nguồn ghi tác giả cho SEP thứ nhất mà không ghi cho SEP thứ hai.**
Tác giả bài "Literary Forms of Medieval Philosophy" là **Eileen Sweeney** (tôi đọc từ metadata trang). Ghi tên cho một bài mà bỏ cho bài kia là không nhất quán trong cùng một dòng.

**Phát hiện 6 — CÂN NHẮC. Hai liên kết ngược chưa được ghi nhận.**
`CH05-CE09-10` (Eriugena) và `CH05-CE10-12` (Gerbert) đều ghi `Kế thừa từ: CH05-CE06-12`, nhưng mục này không ghi ai trong hai người ở "Ảnh hưởng tới"; `reports/lint-ch05.txt` in cả hai dòng INFO. Mục đang ở 2/3 dòng "Ảnh hưởng tới" nên **chỉ còn chỗ cho một** — nếu phải chọn, khối ghi chú chapter đã gọi Gerbert là ca `trực tiếp` xa nhất của cả chapter (420 năm), nên thêm Gerbert sẽ kéo theo một quyết định về mức bằng chứng chứ không chỉ là thêm một dòng.

**Phát hiện 7 — CÂN NHẮC.** ideas = **130 chữ**, chạm trần.

---
## 13. Khối ghi chú biên tập chưa từng được bình duyệt — **"Một liên kết tự do được nâng thành ID, và vì sao điều đó đáng ghi"** (dòng 1228–1229)

**Đã kiểm được (không có phát hiện)**
- `CH05-CE07-08` đúng là **Brahmagupta**; `CH05-CE09-04` đúng là **Al-Khwarizmi** ✔.
- Thao tác được mô tả đã xảy ra thật và **đã xong ở cả hai đầu**: `CH05-CE07-08` ghi `Ảnh hưởng tới: - CH05-CE09-04 · kế thừa · qua trường phái`, và `CH05-CE09-04` ghi `Kế thừa từ: - CH05-CE07-08 · kế thừa · qua trường phái`. Cạnh cân, không sinh dòng INFO nào ✔.
- Mệnh đề "Các đích tự do **vẫn vào thống kê** — `reports/stats.txt` đếm đủ" là **đúng**: khối `[ch05] Loại quan hệ` cộng lại bằng tổng **mọi** dòng quan hệ, không phân biệt ID hay tự do ✔.
- Mệnh đề trung tâm — "Cái mất không phải con số mà là **cạnh**" — đúng, và vòng này tìm được ba ca cụ thể minh hoạ nó (xem dưới) ✔.

**Phát hiện 1 — BẮT BUỘC. Hai con số trong khối đã rữa, và chúng rữa theo đúng cái cách mà chính chapter này đặt quy ước để chặn.**

Nguyên văn câu sai (dòng 1229):
> Các đích tự do **vẫn vào thống kê** — `reports/stats.txt` đếm đủ, ở ch05 là 206 dòng quan hệ trong khi chỉ 65 dòng trỏ ID.

Đo lại ở thời điểm vòng này chạy, bằng hai cách độc lập cho ra cùng kết quả:
- `reports/stats.txt`, khối `[ch05] Loại quan hệ`: 231 + 20 + 7 = **258**;
- đếm trực tiếp trên `content/ch05.md` (cắt bỏ `## Ghi chú biên tập`): **258** dòng quan hệ, trong đó **77** dòng khớp `ID_RE`, **181** dòng tự do.

Tức **258 / 77**, không phải 206 / 65. Và câu đang viết ở **thì hiện tại, không tự khai mốc đo** — đúng điều mà quy ước ở `content/ch05.md:1271` cấm: *"con số trong ghi chú biên tập phải tự khai nó đo ở thời điểm nào, hoặc không nêu số."* Khối này nằm **sau** khối đặt ra quy ước ấy trong cùng một file.

Câu thay thế đề xuất, nguyên văn:
> Các đích tự do **vẫn vào thống kê** — `reports/stats.txt` đếm đủ, ở ch05 là 258 dòng quan hệ trong khi chỉ 77 dòng trỏ ID, **đo trên `content/ch05.md` sau vòng CE10**.

*Soi lại câu thay thế — tôi phải tự áp đúng cái thước vừa dùng:* hai con số 258 và 77 **tự khai mốc đo**, nên chúng không rữa lại được theo cách cũ ✔. Chúng là số tôi **tự đo**, không chép từ đâu, và đo được bằng hai đường cho cùng kết quả ✔. Câu nằm trong Ghi chú biên tập nên không chịu trần chữ nào ✔. Nếu chủ repo muốn một bản không bao giờ phải sửa lại: **bỏ hẳn hai con số**, giữ mệnh đề định tính ("phần lớn dòng quan hệ của ch05 là đích tự do") — quy ước ở dòng 1271 cho phép đúng hai lựa chọn, và đây là lựa chọn thứ hai.

**Phát hiện 2 — BẮT BUỘC. Khối mô tả sai mức mù của lint, và nói nhẹ hơn thực tế ở một chỗ còn nặng hơn.**

Nguyên văn câu sai (dòng 1229):
> Đây là một thao tác bảo trì mà **lint không nhắc được**, vì lint không biết một chuỗi văn bản tự do nào đó vừa trở thành một mục có thật; nó chỉ kiểm ID trỏ tới chỗ tồn tại.

Không đúng ở mức khối đang khẳng định. Vòng đối xứng ở `atlaslib/lint.py:224-232` **có** nhắc, miễn là **đầu kia đã dùng ID**: khi `B` ghi `Kế thừa từ: A` bằng ID còn `A` để đích tự do, lint in `[INFO] B: kế thừa từ A nhưng A không ghi 'Ảnh hưởng tới' B`. Trong chính nhóm CE06 có **hai** ca như vậy đang nằm sẵn trong `reports/lint-ch05.txt`:
- `[INFO] CH05-CE07-10: kế thừa từ CH05-CE06-05 nhưng CH05-CE06-05 không ghi 'Ảnh hưởng tới' CH05-CE07-10` → mục Trần-na để "Pháp Xứng (Dharmakīrti)" ở dạng tự do;
- `[INFO] CH05-CE07-07: kế thừa từ CH05-CE06-08 nhưng CH05-CE06-08 không ghi 'Ảnh hưởng tới' CH05-CE07-07` → mục Bồ-đề-đạt-ma để "Huệ Năng và Thiền tông Trung Hoa" ở dạng tự do.

Lint mù **hoàn toàn** chỉ ở một cấu hình hẹp hơn mà khối không nêu: khi **cả hai** đầu đều tự do. Nhóm này cũng có đúng một ca ấy — `CH05-CE06-06` ghi "Chế độ quân điền Bắc Ngụy" còn `CH04-CE05-12` ghi "Chế độ quân điền ở nhà Tuỳ, Đường, Nhật Bản và Việt Nam"; hai mục có thật, trỏ về phía nhau, không sinh cạnh nào, và **không có một dòng INFO nào** để ai biết.

Câu thay thế đề xuất, nguyên văn:
> Đây là một thao tác bảo trì mà lint chỉ nhắc được **một nửa**: vòng đối xứng (`atlaslib/lint.py:224-232`) in INFO khi đầu kia đã dùng ID, nhưng khi **cả hai** đầu còn là văn bản tự do thì không có dòng nào — lint không biết một chuỗi văn bản tự do nào đó vừa trở thành một mục có thật.

*Soi lại câu thay thế:* mệnh đề về hành vi lint tôi **đọc thẳng từ mã** (`lint.py:224-232`) và **xác nhận bằng đầu ra thật** (`reports/lint-ch05.txt` sau khi chạy `build.py --offline`), không suy từ mô tả ✔. Số dòng mã được ghi kèm để vòng sau kiểm lại được ✔. Không có mệnh đề nào trong câu thay thế mà tôi chưa chạy thử ✔.

**Phát hiện 3 — NÊN. Đơn thuốc của khối chưa từng được uống, và nhóm ngay trên nó là bệnh nhân.**

Nguyên văn (dòng 1229):
> Hệ quả cho các vòng sau: mỗi khi thêm một nhóm mới, phải `grep` tên những người vừa thêm trong toàn bộ `content/` để tìm các đích tự do cần nâng cấp.

Quy trình đúng. Nhưng nó được viết ở vòng CE10 và **chưa từng được chạy ngược** cho nhóm CE06, dù CE06 nằm trong cùng file và cùng chapter. Ba ca còn tồn (hai ca lint đã in INFO, một ca lint im lặng) đã liệt ở phát hiện 2 và ở các mục 5, 6, 8 của báo cáo này. Đề xuất: ghi thêm vào khối một câu rằng việc grep phải chạy **cả hai chiều** — không chỉ cho nhóm vừa thêm, mà cả cho các nhóm cũ khi một người mới xuất hiện ở nhóm sau.

**Phát hiện 4 — CÂN NHẮC. "chỉ 65 dòng trỏ ID" so với "206" là một tỉ lệ bị chôn.**
Dù sửa số, khối vẫn để người đọc tự chia. Ở số hiện tại tỉ lệ là 77/258 ≈ 29,8%. Nếu khối muốn nêu tỉ lệ thì nó cũng phải tự khai mốc đo như hai con số kia — hoặc không nêu. Ghi ra đây để vòng sau khỏi "cải thiện" khối bằng cách thêm một phần trăm không mốc.

---
## Bảng tổng

| Mục | BẮT BUỘC | NÊN | CÂN NHẮC |
|---|---:|---:|---:|
| `CH05-CE06-01` Justinianus I | 1 | 1 | 2 |
| `CH05-CE06-02` Biển Đức thành Norcia | 0 | 2 | 1 |
| `CH05-CE06-03` Khosrow I | 0 | 1 | 1 |
| `CH05-CE06-04` Varāhamihira | 1 | 1 | 2 |
| `CH05-CE06-05` Trần-na | 1 | 1 | 1 |
| `CH05-CE06-06` Tùy Văn Đế | 0 | 2 | 1 |
| `CH05-CE06-07` Trí Di | 0 | 2 | 0 |
| `CH05-CE06-08` Bồ-đề-đạt-ma | 1 | 1 | 0 |
| `CH05-CE06-09` Kaleb xứ Aksum | 1 | 1 | 2 |
| `CH05-CE06-10` Bumin Qaghan | 1 | 2 | 2 |
| `CH05-CE06-11` Bhavavarman I | 0 | 2 | 2 |
| `CH05-CE06-12` Boethius | 1 | 2 | 4 |
| Khối ghi chú "Một liên kết tự do được nâng thành ID" | 2 | 1 | 1 |
| **Tổng** | **9** | **19** | **19** |

### Chín việc BẮT BUỘC, gom lại

1. **CE06-01** — hội đồng năm 528 không do Tribonianus đứng đầu (ông là ủy viên; đứng đầu từ 530, cho *Digesta*).
2. **CE06-04** — quy tắc 6: `content/ch04.md:1034` vẫn liệt **Varāhamihira** là ứng viên bị loại, trong khi `CH05-CE06-04` tồn tại. (Cùng dòng còn **Āryadeva**, `CH04-CE03-12` — ngoài phạm vi vòng này.)
3. **CE06-05** — `Pháp Xứng (Dharmakīrti)` là đích tự do, trong khi `CH05-CE07-10` tồn tại và đã trỏ ngược; kèm `trực tiếp` bất khả.
4. **CE06-08** — `Huệ Năng và Thiền tông Trung Hoa` là đích tự do, trong khi `CH05-CE07-07` tồn tại và đã trỏ ngược.
5. **CE06-09** — nguồn "George Hatke, mục 'Aksum', trong *A Thematic Dictionary of Ancient Arabia*" không tìm được bản ghi nào, và thiếu NXB/năm/trang/URL; nó là chỗ duy nhất đỡ cho mốc 529.
6. **CE06-10** — `Nhu Nhiên hãn quốc · phản bác · trực tiếp`: đàn áp quân sự không phải quan hệ tư tưởng, đi ngược quyết định đã thành văn ở Ghi chú biên tập `ch04.md`.
7. **CE06-12** — "đầu thế kỷ 13" trái với chính SEP (Marenbon): "later twelfth century".
8. **Khối ghi chú** — "206 dòng quan hệ … 65 dòng trỏ ID" đã rữa (thực tế **258 / 77**) và không tự khai mốc đo, trái quy ước `ch05.md:1271`.
9. **Khối ghi chú** — mô tả sai mức mù của lint; vòng đối xứng `lint.py:224-232` **có** báo khi một đầu đã dùng ID, và `reports/lint-ch05.txt` đang in sẵn hai dòng ấy cho chính nhóm CE06.

### Hai việc **không** phải phát hiện, ghi lại để vòng sau khỏi "sửa" nhầm

- `Tuệ Tư · kế thừa · trực tiếp` (CE06-07) và `CH04-CE04-11 · kế thừa · suy đoán học giả` (CE06-05) là hai dòng dùng mức bằng chứng **đúng**; đợt hạ `trực tiếp` hàng loạt ở P4 không được chạm vào chúng.
- `CH05-CE06-11` khai "mục Đông Nam Á đầu tiên của atlas chính" — tôi kiểm và **đúng**, không cần rào thêm.

## Mọi `[KHÔNG KIỂM ĐƯỢC]` của vòng này

| # | Mệnh đề | Vì sao không kiểm được |
|---|---|---|
| 1 | CE06-01 — ai chủ trì hội đồng 528 (tên người) | Không mở được chuyên khảo (Honoré, *Tribonian*). Tôi chỉ khẳng định Tribonianus **không** đứng đầu, và cố ý không đưa tên người chủ trì vào câu thay thế. |
| 2 | CE06-02 — Dunn 2000 **viết gì** về tác quyền *Regula Benedicti* | Xác nhận được sách tồn tại (OpenLibrary) nhưng không có bản toàn văn truy cập được. Đây là lý do phát hiện để **NÊN**, không phải BẮT BUỘC. |
| 3 | CE06-03 — chi tiết "nộp **ba kỳ** mỗi năm" | Bản dịch Bosworth 1999 là sách in, không mở được. |
| 4 | CE06-04 — Romaka/Pauliśa quy về Hipparchus hay Ptolemy | Pingree 1981 và Neugebauer–Pingree 1970–71 đều là sách in. Vì vậy đề xuất đổi ID sang `CH03-BCE02-03` **không được áp mù**. |
| 5 | CE06-04 — niên đại soạn của từng siddhānta (cho cụm "trước thế kỷ 5") | Cùng lý do trên. Lối viết không cần kiểm thêm: "trước thời ông". |
| 6 | CE06-05 — "bánh xe lý do" có đúng chín ô trong *Pramāṇasamuccaya* không | Hattori 1968 / Hayes 1988 không mở được; vì vậy câu thay thế của tôi **không** chứa con số chín. |
| 7 | CE06-06 — khác biệt giữa bản 581 và bản 583 của Khai Hoàng luật | *Tùy thư* 刑法志 không mở được; `ctext.org` đã được khối ghi chú chapter ghi là trang chặn bot (200 / 2.781 byte). |
| 8 | CE06-07 — Swanson 1989 bàn ở trang nào về "năm thời tám giáo" là hệ thống hoá đời sau | Sách in, không mở được. Câu thay thế vì vậy không nêu tên Chegwan hay mốc thế kỷ 10. |
| 9 | CE06-08 — nguyên văn *Lạc Dương già lam ký* mô tả xuất thân Bồ-đề-đạt-ma | Không mở được nguồn chữ Hán trong vòng này. Câu thay thế chỉ dựa vào điều **chính mục** đã khẳng định. |
| 10 | CE06-09 — *A Thematic Dictionary of Ancient Arabia* có tồn tại không | OpenLibrary và Crossref đều không có bản ghi khớp. **Vắng bản ghi không chứng minh không tồn tại** — tôi không tuyên bố đây là nguồn bịa; tôi chỉ khẳng định dòng trích như đang viết thì không kiểm được. |
| 11 | CE06-09 — RIÉth 191 có khắc bằng **musnad** không | Không mở được RIÉth / DASI; khối ghi chú chapter đã ghi DASI trả về không ổn định, nên một lần kéo hỏng không đủ kết luận. |
| 12 | CE06-10 — mốc **563** có trong Menander Protector không | Không mở được bản Blockley. Câu thay thế **bỏ** mốc 563 chứ không gán nó cho người khác. |
| 13 | CE06-10 — dạng phiên Hán–Việt chuẩn của 嚈噠 ("Hiệt Đát" / "Yếm Đát") | Không có nguồn quy chuẩn trong tầm vòng này. |
| 14 | CE06-11 — nội dung bi ký **K.53** nói gì | Tôi chỉ kiểm được **nó ở đâu** (Kdei Ang, theo bản đồ Heng & Lavy), không kiểm được nó nói gì. |
| 15 | CE06-11 — "vị vua **đầu tiên**" ở mức chặt (so với Vīravarman, Citrasena) | Không đọc đủ Vickery để loại trừ. |
| 16 | CE06-12 — trạng thái **trước khi sửa** của mục Porphyry (con số "hai lần") | Chỉ thấy được bản hiện tại, không chạy lịch sử git. Câu thay thế vì vậy bỏ con số — vì một con số đếm trạng thái file là đúng loại số sẽ rữa lại. |

### Ghi chú phương pháp — một chỗ tôi suýt báo sai, ghi lại vì nó là bài học quy trình

Ở lượt tìm đầu tiên trong PDF Vickery, tôi **không** thấy chuỗi `K.151` và kết luận hụt rằng mốc 598 đến từ *Tùy thư* chứ không từ bi ký, tức sắp báo mục CE06-11 là sai trong khi nó đúng. Nguyên nhân: Vickery viết `K151` không có dấu chấm, và bản giải nén stream PDF còn làm rụng một số ký tự. Chỉ sau khi tìm lại bằng nhiều biến thể chính tả mới ra đúng câu. **Bài học**: với PDF, một lượt `grep` không thấy **không phải** bằng chứng vắng mặt — phải thử ít nhất các biến thể dấu chấm/khoảng trắng trước khi báo lỗi cho người viết. Cùng loại cảnh báo với "HTTP 200 không có nghĩa là đọc được", chỉ ở tầng sau.

### Một tác dụng phụ của vòng này, báo để chủ repo biết

Để đọc được đầu ra lint thật (thay vì tin vào `reports/lint-ch05.txt` cũ), tôi chạy `.venv/bin/python build.py --offline`. Lệnh ấy ghi lại các file sinh ra, và `git status` nay báo `M chapters/ch05.html` và `M data/persons.json`. **Tôi không sửa một dòng nào trong `content/`.** Hai file kia vốn đã **lạc hậu** so với `content/ch05.md` trước khi tôi chạy (diff cho thấy chúng còn mang bản cũ của mấy khối ghi chú nhóm CE08), nên trạng thái sau khi chạy là trạng thái **đúng** theo `CONTRIBUTING.md:119`. Tôi để nguyên chứ không revert, vì revert sẽ là khôi phục bản lạc hậu — nhưng ghi ra đây để chủ repo quyết, chứ không im lặng.
