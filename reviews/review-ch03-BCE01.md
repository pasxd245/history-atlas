# Bình duyệt độc lập — `content/ch03.md`, nhóm **BCE01** (TK 1 TCN, 100–1 TCN)

Người rà: agent bình duyệt độc lập (không viết chapter này).
Phạm vi: dòng `**Bối cảnh**` của nhóm + 12 mục `CH03-BCE01-01` … `-12`.
Đối chiếu theo `prompts/atlas-prompt.md` §5 và `CONTRIBUTING.md`.
Xếp loại: **Sai** (khẳng định sai sự thật) · **Nghi vấn** (chưa chứng minh được / nhiều khả năng sai) · **Thiếu** (bỏ sót cần bổ sung) · **Thể thức** (vi phạm template / quy tắc dự án).

> Ghi chú phương pháp: mọi mục ghi "không kiểm được" là chỗ tôi **không** mở được nguồn gốc hoặc mục lục, không phải chỗ tôi phỏng đoán.

---

## 0. Đối chiếu Wikidata — 12/12 Q-ID trỏ đúng người

Gọi `wbgetentities` / `wbgetclaims` trực tiếp. Kết quả:

| ID mục | Q-ID | Nhãn Wikidata (en) | P569 / P570 | Trường `năm:` | Độ tin cậy | Kết luận |
|---|---|---|---|---|---|---|
| -01 Caesar | Q1048 | Julius Caesar | −100-07-12 / −44-03-15 | 100–44 TCN | Cao (±5) | khớp |
| -02 Augustus | Q1405 | Augustus | −63-09-23 / +14-08-19 | 63 TCN – 14 CN | Cao | khớp |
| -03 Cicero | Q1541 | Cicero | −106-01-03 / −43-12-07 | 106–43 TCN | Cao | khớp |
| -04 Lucretius | Q47154 | Lucretius | −94 / −55-10-15 | k. 99–55 TCN | Trung bình (±25) | khớp |
| -05 Virgil | Q1398 | Virgil | −70-10-15 / −19-09-21 | 70–19 TCN | Cao | khớp |
| -06 Tư Mã Thiên | Q9372 | Sima Qian (vi: Tư Mã Thiên) | −145 / −86 | k. 145–86 TCN | Trung bình | khớp |
| -07 Hillel | Q319219 | Hillel the Elder | −50 / +8 (và −100/+100 prec. thế kỷ) | hoạt động k. 30 TCN – 10 CN | Thấp | bỏ qua đối chiếu, hợp lệ |
| -08 Vitruvius | Q47163 | Vitruvius | −80 / −15 | k. 80–15 TCN | Thấp | bỏ qua đối chiếu |
| -09 Cleopatra | Q635 | Cleopatra (vi: Cleopatra VII) | −69-01-13 / −30-08-12 | 69–30 TCN | Cao | khớp |
| -10 Lưu Hướng | Q465282 | Liu Xiang (vi: Lưu Hướng) | −77 / −6 | k. 77–6 TCN | Trung bình | khớp |
| -11 Strabo | Q45936 | Strabo | mô tả WD "64/63 BC–c.24 AD"; P570 +21/+23/+24 | k. 64 TCN – 24 CN | Trung bình | khớp (P569 không tải được do rate-limit — **không kiểm được** trực tiếp, chỉ dựa vào mô tả WD) |
| -12 Posidonius | Q185770 | Posidonius | −135 / −51 | k. 135–51 TCN | Trung bình | khớp |

Không có lỗi định danh Q-ID ở nhóm này. Theo `CONTRIBUTING.md` §"Khớp Wikidata không đồng nghĩa với đúng", phần còn lại của báo cáo không dựa vào bảng này.

---

## 1. Dòng `**Bối cảnh**` của nhóm

**Nghi vấn** — "Nhà Hán ở đỉnh cao bắt đầu tổng kết chính mình bằng sử học và thư mục học."
- Nhóm BCE01 phủ 100–1 TCN. Giai đoạn thường được coi là đỉnh của Tây Hán là thời Vũ Đế (141–87 TCN), tức chủ yếu nằm ở nhóm **BCE02** — chính chapter này đã xếp Hán Vũ Đế ở BCE02 với lý do "hai thiết chế được chọn làm lý do … đều ở nửa đầu". Thế kỷ 1 TCN của Tây Hán là giai đoạn ngoại thích (họ Hoắc, rồi họ Vương) lên nắm quyền, ngân khố căng thẳng sau chiến tranh Hung Nô, và kết thúc bằng việc Vương Mãng chiếm ngôi năm 9 CN. Nói "ở đỉnh cao" cho đúng thế kỷ này là ngược với cách chính chapter định vị Vũ Đế.
- Nguồn dùng để kết luận: chính `content/ch03.md` mục `CH03-BCE02-02` và khối "Nhân vật có thể thuộc thế kỷ khác" trong Ghi chú biên tập của file.
- Câu thay thế đề xuất: "Nhà Hán sau thời Vũ Đế chuyển từ bành trướng sang tổng kết chính mình bằng sử học và thư mục học."

**Nghi vấn** — "Vương quốc Hellenistic cuối cùng mất độc lập năm 30 TCN."
- Đúng theo cách nói quy ước của sách giáo khoa (Ai Cập Ptolemy sáp nhập 30 TCN), nhưng là một mệnh đề "cuối cùng" không có quy thuộc. Vương quốc Ấn–Hy Lạp (Indo-Greek) còn tồn tại tới khoảng năm 10 CN dưới Strato II/III, và vương quốc Bosporus kéo dài tới TK 4 CN với tư cách chư hầu. Theo yêu cầu trung lập của `prompts/atlas-prompt.md`, mọi chữ "cuối cùng"/"duy nhất" cần hoặc được giới hạn hoặc được quy thuộc.
- Câu thay thế đề xuất: "Vương quốc Ptolemy ở Ai Cập, vương quốc Hellenistic lớn cuối cùng quanh Địa Trung Hải, mất độc lập năm 30 TCN."

---

## 2. `CH03-BCE01-01` · Julius Caesar

**Sai** — Số chương trong dòng Nguồn: "Mary Beard, SPQR: A History of Ancient Rome (2015), ch. 7–8."
- Mục lục SPQR (bản 2015): ch. 7 "From Empire to Emperors" (tr. 253), ch. 8 "**The Home Front**" (tr. 297), ch. 9 "The Transformations of Augustus". Ch. 8 bàn đời sống gia đình, xã hội và kinh tế hộ, **không** phải sự nghiệp của Caesar. Phần trình bày Caesar nằm trong ch. 7.
- Nguồn dùng để kết luận: mục lục SPQR qua OPAC thư viện (Villanova, Schlow) và trang Wikipedia "SPQR: A History of Ancient Rome".
- Đây đúng dạng lỗi mà `CONTRIBUTING.md` cảnh báo ("+1" vào số chương). Sửa đề xuất: `Mary Beard, SPQR: A History of Ancient Rome (2015), ch. 7.`

**Sai** — Liên kết sai loại quan hệ: `Ảnh hưởng tới: CH03-BCE01-09 · kế thừa · trực tiếp` (Cleopatra VII).
- Đích đến đúng người (CH03-BCE01-09 là Cleopatra VII), nhưng quan hệ "kế thừa" là sai bản chất: Cleopatra không kế thừa tư tưởng hay phương pháp nào từ Caesar: đó là một liên minh chính trị và quan hệ cá nhân. Từ vựng `RELATION_TYPES` của dự án (kế thừa · tổng hợp · phản bác · tương đồng độc lập) không có mục nào mô tả được liên minh, nghĩa là liên kết này không nên tồn tại chứ không phải nên đổi nhãn.
- Đề xuất: **bỏ** dòng này (và bỏ dòng đối xứng `CH03-BCE01-01` trong `Kế thừa từ` của mục Cleopatra). Quan hệ Caesar–Cleopatra đã được kể đủ trong phần văn xuôi của cả hai mục.

**Nghi vấn** — `Ảnh hưởng tới: Lịch Julius và lịch Gregory · kế thừa · trực tiếp`.
- Lịch Gregory là bản hiệu chỉnh năm 1582 do uỷ ban của Christopher Clavius soạn, cách Caesar 16 thế kỷ. Mức bằng chứng "trực tiếp" chỉ đúng với lịch Julius. Đề xuất tách hoặc hạ xuống: `Lịch Julius, và qua đó lịch Gregory · kế thừa · qua trường phái`.

*Đã kiểm và **đúng**:* chinh phục Gallia 58–50 TCN; vượt Rubicon năm 49 TCN; `dictator perpetuo` năm 44 TCN; lịch Julius đặt năm 46 TCN với năm trung bình 365,25 ngày; `Commentarii de Bello Gallico` là tác phẩm có thật của Caesar. `Kế thừa từ: CH03-BCE02-09` trỏ đúng Tiberius Gracchus (k. 163–133 TCN), mức "qua trường phái" hợp lý.

*Thể thức — đạt:* "Vì sao chọn" nêu đích danh Pompey (106–48 TCN) và Sulla (k. 138–78 TCN). Cả hai **thật sự cùng thời** với Caesar (100–44 TCN): Pompey trùng gần trọn đời, Sulla chết khi Caesar 22 tuổi và đã là đối thủ chính trị của ông. Không vi phạm §5.

---

## 3. `CH03-BCE01-02` · Augustus

**Nghi vấn** — "Caesar nắm quyền tuyệt đối nhưng **bị giết sau năm tháng** vì công khai phá bỏ hình thức cộng hoà."
- Con số "năm tháng" không có mốc khởi tính và không khớp với mốc mà chính câu này viện dẫn. Cái bị người La Mã coi là "công khai phá bỏ hình thức cộng hoà" là chức `dictator perpetuo`, nhận khoảng tháng 2 năm 44 TCN; Caesar bị giết ngày 15 tháng 3 năm 44 TCN — tức **khoảng một tháng**, không phải năm tháng. Nếu tính từ lúc ông về Rome sau trận Munda (tháng 9–10 năm 45 TCN) thì ra khoảng năm–sáu tháng, nhưng đó không phải mốc mà câu đang nói tới.
- Đề xuất: "Caesar nhận chức độc tài trọn đời rồi bị giết chỉ ít tuần sau đó, vì chính việc công khai phá bỏ hình thức cộng hoà."

**Nghi vấn** — `Ảnh hưởng tới: CH03-BCE01-08 · kế thừa · trực tiếp` (Vitruvius), và dòng đối xứng `Kế thừa từ: CH03-BCE01-02` ở mục Vitruvius.
- Đích đến đúng người và đúng chiều niên đại. Nhưng quan hệ thực tế là **đề tặng và bảo trợ**, không phải kế thừa tư tưởng: `De architectura` dâng lên Augustus, còn nội dung lý luận của sách truy về truyền thống Hy Lạp (Hermogenes, Pytheos). Gắn nhãn "kế thừa · trực tiếp" làm Augustus trông như nguồn tư tưởng kiến trúc của Vitruvius.
- Đề xuất: giữ liên kết nhưng hạ mức, hoặc bỏ và để Vitruvius chỉ kế thừa từ truyền thống Hy Lạp (dòng Hermogenes đã có sẵn).

*Đã kiểm và **đúng**:* Actium 31 TCN; không xưng vua mà giữ `imperium` và `tribunicia potestas`; quân đội chuyên nghiệp thường trực với `aerarium militare` (lập năm 6 CN); `Res Gestae Divi Augusti` có thật; "nguyên thủ đứng vững ba thế kỷ" khớp mốc quy ước 27 TCN – 284 CN. Werner Eck, *The Age of Augustus*, Blackwell 2003 — có thật, đúng năm.

*Thể thức — đạt:* nêu Marcus Antonius (83–30 TCN) và Caesar (100–44 TCN), cả hai cùng thời thật với Augustus (63 TCN – 14 CN). Caesar là cha nuôi chứ không phải đối thủ, nhưng ở đây ông được nêu đúng với tư cách **ứng viên cạnh tranh cho cùng một vị trí trong atlas**, và lập luận so sánh (d)/(b) giữa hai người là lập luận thật, không phải so sánh cộng sự. Chấp nhận được.

---

## 4. `CH03-BCE01-03` · Cicero

**Sai** — `Kế thừa từ: CH03-BCE02-10 · kế thừa · **trực tiếp**` (Carneades xứ Cyrene).
- Theo chính `content/ch03.md`, Carneades là `k. 214–129 TCN`. Cicero sinh năm 106 TCN, tức **23 năm sau khi Carneades chết**. Không thể có quan hệ trực tiếp. Cicero tiếp nhận Hàn lâm viện hoài nghi qua Philo xứ Larissa, người ông thực sự nghe giảng ở Rome khoảng năm 88 TCN.
- Nguồn dùng để kết luận: trường `năm:` của chính mục `CH03-BCE02-10` trong file, đối chiếu với `năm:` của mục này; SEP "Cicero" (Raphael Woolf, 2022) về đường truyền Hàn lâm viện qua Philo.
- Sửa đề xuất: `- CH03-BCE02-10 · kế thừa · qua trường phái`.

**Sai** — `Kế thừa từ: CH03-BCE02-04 · kế thừa · **trực tiếp**` (Polybius).
- `content/ch03.md` ghi Polybius `k. 200–118 TCN` — chết 12 năm trước khi Cicero sinh. "Trực tiếp" là bất khả. Cicero đọc Polybius qua văn bản và qua truyền thống vòng Scipio, không qua tiếp xúc.
- Sửa đề xuất: `- CH03-BCE02-04 · kế thừa · qua trường phái`.
- Lưu ý: đây là hai lỗi **nằm ở chiều `Kế thừa từ`**, tức chiều lint CÓ quét — nhưng lint chỉ kiểm ID hợp lệ và tính đối xứng, không kiểm niên đại so với mức bằng chứng. `reports/lint-ch03.txt` báo 0 ERROR / 0 WARN, nên hai lỗi này lọt hoàn toàn.

**Thiếu** — Posidonius vắng mặt trong `Kế thừa từ` của Cicero.
- Mục `CH03-BCE01-12` ghi `Ảnh hưởng tới: CH03-BCE01-03 · kế thừa · trực tiếp`, và đó là liên kết **đúng** (Cicero học Posidonius ở Rhodes khoảng 78–77 TCN — quan hệ trực tiếp duy nhất đúng trong cả ba nguồn của Cicero). `reports/lint-ch03.txt` đã báo đúng chỗ này ở mức INFO. Nghịch lý: hai người Cicero **không** gặp được ghi "trực tiếp", còn người ông thật sự học thì không có mặt.
- Sửa đề xuất: thay một trong hai dòng sai trên bằng `- CH03-BCE01-12 · kế thừa · trực tiếp`.

**Nghi vấn (trung lập)** — "De Officiis … là **sách đạo đức được đọc liên tục nhất ở châu Âu trước thời cận đại**."
- Mệnh đề tối cao không quy thuộc. Có thể bảo vệ được bằng số liệu (De Officiis nằm trong nhóm sách in sớm nhất sau Kinh Thánh Gutenberg, và là sách giáo khoa đạo đức chuẩn của trường Dòng Tên), nhưng câu hiện tại không nói theo ai, nên vi phạm yêu cầu "không tô vẽ" của prompt.
- Câu thay thế đề xuất: "De Officiis bàn nghĩa vụ trong xung đột giữa cái lợi và cái phải, và là một trong những sách đạo đức được sao chép, in và dạy liên tục nhất ở châu Âu trước thời cận đại."

*Đã kiểm và **đúng**:* `De Legibus`, `De Re Publica`, `De Officiis` đều là tác phẩm thật của Cicero và đều bàn đúng nội dung được dẫn. Mục SEP `https://plato.stanford.edu/entries/cicero/` **tồn tại**, tác giả Raphael Woolf (2022), và có bàn `De Re Publica`, `De Legibus`, `De Officiis` cùng luật tự nhiên — đạt cả hai yêu cầu của `CONTRIBUTING.md` (URL có thật *và* nói về nhân vật). Mốc **Petrarca tìm lại thư Cicero năm 1345** tại thư viện nhà thờ Verona (ad Atticum, ad Quintum, ad Brutum) — **đúng**, xác nhận qua Britannica mục Petrarch 1340–46 và historyofinformation.com. `CH03-BCE03-07` trỏ đúng Zeno xứ Citium, mức "qua trường phái" đúng.

*Thể thức — đạt:* nêu Lucretius (k. 99–55 TCN) và Varro (116–27 TCN), cả hai cùng thời thật với Cicero (106–43 TCN). Varro còn là bạn và người cùng đề tặng tác phẩm — nhưng cũng là ứng viên cạnh tranh thật cho vị trí "người chuyển tri thức Hy Lạp sang Latinh", nên không rơi vào lỗi "cộng sự chứ không phải ứng viên".

---

## 5. `CH03-BCE01-04` · Lucretius

**Nghi vấn** — "Giá trị của văn bản nằm ở chỗ nó là **trình bày đầy đủ duy nhất còn lại** của nguyên tử luận cổ đại, vì trước tác chính của Epicurus và Democritus đều mất."
- Mệnh đề "duy nhất" không quy thuộc, và không hoàn toàn đúng: ba bức thư của Epicurus (gửi Herodotus, Pythocles, Menoeceus) còn nguyên trong Diogenes Laertius quyển X, và thư gửi Herodotus chính là bản tóm tắt vật lý nguyên tử luận do chính Epicurus viết. Thêm vào đó các cuộn giấy Herculaneum còn giữ phần `Peri Phuseōs` của Epicurus và trước tác Philodemus.
- Cái đúng là: De rerum natura là trình bày **đầy đủ và liên tục nhất** còn lại, chứ không phải duy nhất.
- Câu thay thế đề xuất: "…nó là trình bày đầy đủ và liền mạch nhất còn lại của nguyên tử luận cổ đại; trước tác chính của Epicurus và Democritus chỉ còn qua tóm lược và mảnh vụn."

**Nghi vấn** — "bản sao **duy nhất** được Poggio Bracciolini tìm thấy năm 1417".
- Mốc 1417 và vai trò Poggio là đúng và được chấp nhận rộng rãi. Nhưng chữ "bản sao duy nhất" thì không: bản Poggio tìm được đã mất, cái còn lại là bản chép tay của Niccolò Niccoli; và hai bản thế kỷ 9 độc lập với dòng này — `Oblongus` và `Quadratus` ở Leiden — đã tồn tại từ trước, chúng chính là cơ sở của mọi bản phê bình hiện đại. Nói "bản sao duy nhất" biến một chuỗi truyền bản thành một tai nạn may mắn.
- Câu thay thế đề xuất: "…bản thảo được Poggio Bracciolini tìm thấy năm 1417 đã đưa nguyên tử luận trở lại lưu thông ở châu Âu…"
- Ghi rõ: tôi **không kiểm được** trực tiếp mục lục Greenblatt, *The Swerve* (2011) để biết sách đó có viết "bản sao duy nhất" hay không. Nếu câu này lặp lại cách kể của Greenblatt thì vẫn cần sửa, vì chính luận điểm "bản duy nhất" của Greenblatt là chỗ bị giới nghiên cứu Phục hưng phê bình nhiều nhất.

**Nghi vấn (nguồn)** — "Stephen Greenblatt, *The Swerve: How the World Became Modern* (2011)."
- Sách có thật, đúng năm, đúng chủ đề. Nhưng đây là sách phổ thông có luận đề gây tranh cãi học thuật (bị phê bình nặng vì dựng hình ảnh "thời trung cổ đen tối" và phóng đại tính đơn độc của bản thảo), và nó đang là **nguồn thứ cấp duy nhất** của mục. Theo yêu cầu "ưu tiên nguồn học thuật", nên bổ sung hoặc thay bằng một nguồn chuyên khảo, ví dụ mục SEP "Lucretius" hoặc Stuart Gillespie & Philip Hardie (chủ biên), *The Cambridge Companion to Lucretius* (2007).

*Đã kiểm và **đúng**:* `De rerum natura` gồm **sáu quyển** — đúng; nội dung nêu (nguyên tử và chân không, `clinamen` tức độ lệch tối thiểu dùng để cứu chỗ cho ý chí tự do, linh hồn khả tử, lịch sử tự nhiên của loài người không cần thần can thiệp) — đúng và đúng cả thứ tự quan trọng. Mốc Poggio **1417** — đúng. Ảnh hưởng tới Gassendi, Montaigne, Newton — Montaigne (1533–1592) ghi chú dày đặc trên bản De rerum natura của mình, Gassendi phục hồi nguyên tử luận Epicurus, Newton đọc Lucretius; cả ba đều đứng được. `Kế thừa từ: CH03-BCE03-08` trỏ đúng Epicurus, `CH02-BCE05-05` trỏ đúng Democritus.

*Thể thức — nửa đạt:* hai ứng viên nêu là Epicurus và Philodemus. **Philodemus (k. 110–35 TCN) thật sự cùng thời** với Lucretius (k. 99–55 TCN) — hợp lệ. **Epicurus (k. 341–270 TCN) thì không**, cách Lucretius hơn hai thế kỷ; văn bản có nói rõ "đã được chọn ở nhóm trước" nên người đọc không bị đánh lừa, nhưng theo đúng chữ của §5 ("1–2 người cùng lĩnh vực, **cùng thời**") thì chỉ có một ứng viên hợp lệ. Mức độ nghiêm trọng thấp hơn trường hợp Strabo và Vitruvius dưới đây.

---

## 6. `CH03-BCE01-05` · Virgil

**Sai** — "Trước đó, Bucolica **dựng ra khuôn thơ điền viên**."
- Khuôn thơ điền viên (bucolic/pastoral) là của **Theocritus xứ Syracuse** (k. 300–260 TCN) trong tập `Idylls`; Bucolica của Virgil là bản phỏng và chuyển vào tiếng Latinh — quan hệ mô phỏng này là một trong những sự thật được xác lập chắc nhất của ngành cổ điển học, và chính `The Virgil Encyclopedia` (nguồn mục này dẫn) có mục riêng về nó. Câu hiện tại trao cho Virgil tính nguyên bản (c) mà ông không có, ngay trong một mục mà lập luận chọn người dựa vào (a) và (b).
- Câu thay thế đề xuất: "Trước đó, Bucolica đưa khuôn thơ điền viên của Theocritus vào tiếng Latinh và định hình nó cho toàn bộ truyền thống châu Âu về sau."

**Thiếu** — `Kế thừa từ` bỏ sót Lucretius, người **cùng nhóm** (`CH03-BCE01-04`).
- `Georgica` của Virgil là tác phẩm chịu nợ `De rerum natura` nặng nhất trong toàn bộ thơ Latinh — ở thể loại (thơ giáo huấn hexameter), ở cấu trúc, và ở hàng loạt chỗ mô phỏng trực tiếp; câu nổi tiếng `felix qui potuit rerum cognoscere causas` (Georgica II) được đọc gần như phổ quát là lời nhắc tới Lucretius. Liên kết này mạnh hơn nhiều so với dòng `CH03-BCE01-02` (Augustus) hiện đang chiếm chỗ.
- Sửa đề xuất: thêm `- CH03-BCE01-04 · kế thừa · trực tiếp`. Việc này cũng vá được một lỗ của mục Lucretius, hiện chỉ có đúng một dòng `Ảnh hưởng tới` và dòng đó lại là văn bản tự do.

**Nghi vấn** — `Kế thừa từ: CH03-BCE01-02 · kế thừa · trực tiếp` (Augustus).
- Cùng loại vấn đề với mục Vitruvius: quan hệ thật là bảo trợ (và trung gian thực tế là Maecenas, không phải Augustus). Aeneis đúng là một lập luận về tính chính đáng của trật tự Augustus, nên liên kết không vô lý như trường hợp Vitruvius, nhưng nhãn "kế thừa" vẫn mô tả sai: Virgil không kế thừa tư tưởng từ Augustus, ông viết **cho** trật tự đó.

**Nghi vấn (trung lập)** — "điều **không tác giả Latinh nào khác có**."
- Mệnh đề tối cao không quy thuộc. Dễ sửa bằng cách gắn vào sự kiện cụ thể đã nêu ngay trước đó (việc Dante chọn ông làm người dẫn đường), thay vì phát biểu thành một khẳng định phổ quát.

*Đã kiểm và **đúng**:* niên đại 70–19 TCN; ba tác phẩm `Bucolica`, `Georgica`, `Aeneis`; Aeneis nối Rome với Troy; nhân vật chính định nghĩa bằng `pietas` chứ không bằng `kleos`; việc rời Dido được viết ra chứ không giấu; Dante chọn Virgil làm người dẫn trong `Thần khúc`; ba tác phẩm là nền chương trình học Latinh. `Kế thừa từ: CH02-BCE08-01` trỏ **đúng** Homer trong `content/ch02.md`. Nguồn `Richard F. Thomas và Jan M. Ziolkowski (chủ biên), The Virgil Encyclopedia (2014)` — **có thật, đúng năm, đúng nhà xuất bản** (Wiley-Blackwell, 3 tập, I: A–E, II: F–Pe, III: Ph–Z), xác nhận qua trang Wiley, WorldCat và bài điểm sách trên *The Classical Review*.

*Thể thức — nửa đạt:* Horace (65–8 TCN) cùng thời trọn vẹn với Virgil (70–19 TCN) — hợp lệ. Ovid (43 TCN – 17 CN) thì chỉ chồng lấn 24 năm và toàn bộ sự nghiệp nằm **sau** khi Virgil chết, nên gọi là "ứng viên cùng thời" là kéo dãn. Không nghiêm trọng, nhưng nếu muốn chặt thì thay Ovid bằng Catullus (k. 84–54 TCN, đã có tên trong danh sách bị loại ở Ghi chú biên tập) hoặc Gallus.

---

## 7. `CH03-BCE01-06` · Tư Mã Thiên

**Sai** — Liên kết trỏ **sai người**: `Ảnh hưởng tới: CH90-CE10_14-02 · kế thừa · qua trường phái`.
- `CH90-CE10_14-02` trong `content/ch90.md` là **Đinh Bộ Lĩnh (Đinh Tiên Hoàng, 924–979)**, lĩnh vực `Chính trị/Nhà nước` — một người dựng nước, không liên quan gì tới thể tài sử học. Câu văn xuôi ngay phía trên nói "sử học Triều Tiên, Nhật Bản, Việt Nam cũng theo", nên đích định trỏ rõ ràng là một nhà sử học Việt Nam, không phải một vị vua.
- Nguồn dùng để kết luận: đọc trực tiếp mục `CH90-CE10_14-02` trong `content/ch90.md`.
- Đây đúng dạng lỗi mà lint mù: `reports/lint-ch03.txt` có báo dòng này, nhưng chỉ ở mức `[INFO] … không ghi 'Kế thừa từ' … (P4 sẽ đồng bộ)` — tức lint coi đây là **lỗi đối xứng cần đồng bộ**, và nếu P4 "đồng bộ" thật thì Đinh Bộ Lĩnh sẽ được gắn là người kế thừa Tư Mã Thiên. Lỗi sẽ được nhân lên chứ không bị bắt.
- Sửa đề xuất: không có nhà sử học Việt Nam nào trong nhóm `CH90-CE10_14` — Ghi chú biên tập của `ch90.md` nói rõ **Lê Văn Hưu (1230–1322) đã bị loại vì nhóm kín**. Vậy nên thay bằng một dòng văn bản tự do: `- Lê Văn Hưu và truyền thống quốc sử Đại Việt · kế thừa · qua trường phái`.

**Nghi vấn** — "Ông chịu cung hình **năm 99 TCN** vì bênh Lý Lăng."
- Cần tách hai mốc. Vụ Lý Lăng đầu hàng và việc Tư Mã Thiên lên tiếng bênh rồi bị kết án là năm **99 TCN**; bản thân hình phạt được thi hành vào **Thiên Hán năm thứ 3, tức 98 TCN** (niên hiệu Thiên Hán: 100–97 TCN). Nguồn phổ thông thường gộp hai mốc thành 99, nhưng chapter đang khẳng định đích danh năm chịu hình.
- Nguồn dùng để kết luận: mô tả vụ Lý Lăng và niên hiệu Thiên Hán qua Wikipedia "Sima Qian" và mục "Li Ling Incident"; quy đổi niên hiệu Thiên Hán 3 = 98 TCN. Tôi **không kiểm được** trực tiếp Durrant (1995) để xem sách đó chọn mốc nào.
- Câu thay thế đề xuất: "Năm 99 TCN ông bênh Lý Lăng và bị kết án, rồi chịu cung hình thay cho án tử, và chọn sống tiếp để viết xong — điều ông nói rõ trong thư gửi Nhậm An."

**Nghi vấn** — "thư gửi Nhậm An" không ghi niên đại.
- Thư gửi Nhậm An (`Báo Nhậm Thiếu Khanh thư`) được định niên khoảng **91 TCN**, tức khoảng bảy–tám năm sau hình phạt và gần cuối đời ông. Trong một mục mà trường `năm:` ghi mất k. 86 TCN, việc nêu mốc này giúp người đọc thấy khoảng cách; không nêu thì không sai, nên chỉ là đề nghị.

**Nghi vấn** — `Kế thừa từ: CH03-BCE02-02 · kế thừa · trực tiếp` (Hán Vũ Đế) và `CH03-BCE02-05 · kế thừa · trực tiếp` (Trương Khiên).
- Hán Vũ Đế: Tư Mã Thiên làm quan dưới triều ông và chính ông ra lệnh hình phạt — nhưng đó không phải quan hệ "kế thừa" tư tưởng hay phương pháp. Mục `CH03-BCE02-01` (Đổng Trọng Thư) sẽ là nguồn tư tưởng hợp lý hơn nhiều nếu muốn giữ một liên kết loại này.
- Trương Khiên: mất **114 TCN**, trong khi Tư Mã Thiên chỉ nhậm chức Thái sử lệnh năm **108 TCN**. Tư Mã Thiên dùng **báo cáo văn bản** của Trương Khiên cho thiên `Đại Uyên liệt truyện`; không có bằng chứng tiếp xúc cá nhân trong giai đoạn ông soạn sử. Mức "trực tiếp" nên hạ xuống `qua trường phái`, hoặc giữ "trực tiếp" chỉ nếu mở được chỗ Sử ký nói hai người gặp nhau — tôi **không kiểm được** điều đó.

**Thể thức (vi phạm §5)** — "Ứng viên là cha ông, Tư Mã Đàm, … và **Ban Cố**, tác giả Hán thư."
- **Ban Cố sống 32–92 CN**, tức sinh khoảng **118 năm sau khi Tư Mã Thiên chết** (k. 86 TCN). Không cùng thời theo bất kỳ nghĩa nào. Khác với mục Strabo và Vitruvius — nơi văn bản ít nhất có ghi rõ "ở thế kỷ 2 CN" và "một thế kỷ sau" — ở đây **không có một chữ nào báo cho người đọc biết khoảng cách này**, nên người đọc hoàn toàn có thể hiểu nhầm hai người là đối thủ đương thời. Đây là ca vi phạm §5 nặng nhất của nhóm.
- Tư Mã Đàm (mất 110 TCN) thì hợp lệ: cùng thời thật, và là ứng viên cạnh tranh thật (ông khởi thảo công trình), không phải "cộng sự".
- Sửa đề xuất: "Ứng viên là cha ông, Tư Mã Đàm, người khởi thảo công trình, và — ở thế hệ sau hai thế kỷ, nêu để so sánh chứ không cùng thời — Ban Cố, tác giả Hán thư. Tư Mã Thiên được chọn theo tính nguyên bản (c): …". Nếu muốn một ứng viên **thật sự cùng thời**, có thể nêu Đổng Trọng Thư (k. 179–104 TCN) hoặc Lưu An (179–122 TCN, chủ biên `Hoài Nam tử`).

*Đã kiểm và **đúng**:* Sử ký gồm **130 thiên** — đúng; cấu trúc năm phần (bản kỷ · biểu · thư · thế gia · liệt truyện) — đúng; "Hai mươi bốn bộ chính sử" (Nhị thập tứ sử) — đúng con số và đúng tên gọi; liệt truyện có chép thích khách, thương nhân (`Hoá thực liệt truyện`) và người bói toán (`Nhật giả liệt truyện`) — đúng. Stephen W. Durrant, *The Cloudy Mirror: Tension and Conflict in the Writings of Sima Qian*, SUNY Press 1995 — có thật, đúng năm, đúng chủ đề. `Ảnh hưởng tới: CH03-BCE01-10` trỏ **đúng** Lưu Hướng và đúng chiều.

---

## 8. `CH03-BCE01-07` · Hillel Trưởng lão

**Hai trích dẫn được yêu cầu kiểm riêng đều ĐÚNG, và đúng tới số câu.** Ghi lại đầy đủ để lần sau khỏi kiểm lại:

- `Mishnah, Shevi'it 10:3` cho prosbul — **đúng**. Kiểm qua Sefaria: Shevi'it 10:3 chứa đúng câu "This was one of the things enacted by Hillel the Elder; for when he observed people refraining from lending to one another…", kèm công thức prosbul đọc trước toà. Không phải 10:4, không phải 10:2.
- `Avot 1:12–14` cho Hillel — **đúng và chính xác tới từng câu**. Kiểm qua Sefaria API v3 (`Pirkei_Avot.1.10-16`): 1:10 Shemaiah, 1:11 Avtalyon, **1:12 "Hillel and Shammai received [the oral tradition] from them. Hillel used to say: be of the disciples of Aaron…"**, **1:13 "He [also] used to say: one who makes his name great causes his name to be destroyed…"**, **1:14 "He [also] used to say: If I am not for myself, who is for me?…"**, rồi 1:15 chuyển sang Shammai. Khoảng 1:12–14 cắt đúng phần Hillel, không thừa không thiếu một câu.
- `Shaye J. D. Cohen, From the Maccabees to the Mishnah (2014)` — **có thật, đúng năm**: bản in lần thứ ba, Westminster John Knox Press, 12/11/2014, ISBN 978-0664239046, phạm vi 164 TCN – 300 CN, tức đúng giai đoạn được dẫn.

**Sai** — `Kế thừa từ: CH03-BCE02-11 · kế thừa · qua trường phái` (Judah Maccabee).
- Judah Maccabee là thủ lĩnh quân sự – tôn giáo (lĩnh vực ghi trong atlas: `Tôn giáo/Tâm linh, Quân sự`, hoạt động k. 167–160 TCN). Ông không nằm trong chuỗi truyền thừa học thuật của Hillel ở bất kỳ nguồn rabbi nào.
- Cái đúng nằm **ngay trong nguồn mà mục này đã dẫn**: `Avot 1:12` mở đầu bằng "Hillel and Shammai received [the oral tradition] from **them**" — "them" là **Shemaiah và Avtalyon** ở `Avot 1:10–11`. Đó là chuỗi `zugot` được chính truyền thống ghi lại, và là liên kết "kế thừa · trực tiếp" đúng duy nhất có tư liệu cho mục này.
- Sửa đề xuất: thay bằng `- Shemaiah và Avtalyon (chuỗi zugot, Avot 1:10–12) · kế thừa · trực tiếp`. Nếu muốn giữ một liên kết tới nhóm trước, có thể thêm `- CH03-BCE02-11 · kế thừa · qua trường phái` **chỉ khi** viết rõ đó là quan hệ bối cảnh (nền Judea tự trị sau Maccabee), chứ không phải truyền thừa học thuật.

**Nghi vấn (nhỏ)** — "Ứng dụng nổi tiếng nhất là prosbul, thủ tục cho phép **khoản nợ không bị xoá** khi tới năm sabát."
- Chính xác hơn: prosbul không làm nợ "không bị xoá"; nó **chuyển khoản nợ sang toà án** (`moser shtarotav le-beit din`), và vì năm sabát chỉ xoá nợ giữa cá nhân chứ không xoá nợ do toà nắm, kết quả là khoản nợ vẫn đòi được. Cơ chế này là điểm mấu chốt của lập luận "diễn giải để giữ cho luật vận hành", nên nói rõ ra thì mạnh hơn chứ không dài hơn bao nhiêu.
- Câu thay thế đề xuất: "…prosbul, thủ tục chuyển khoản nợ cho toà án để năm sabát không xoá nó, đặt ra vì quy định xoá nợ đang khiến người ta ngừng cho vay."

**Nghi vấn (nhỏ)** — mục liệt kê bảy quy tắc là "được truyền thống gắn với", và tự hạ độ tin cậy xuống Thấp với lý do "dựa vào nguồn rabbi muộn". Đây là cách xử lý **đúng** và nên giữ nguyên. Chỉ ghi thêm cho đủ: bảy `middot` xuất hiện ở `Tosefta Sanhedrin 7:11` và baraita mở đầu `Sifra`, cả hai đều muộn hơn Hillel — nếu muốn, có thể ghi hai xuất xứ này vào dòng Nguồn để người đọc tự kiểm được chính cái caveat đó.

*Đã kiểm và **đúng**:* Đền thờ bị phá năm **70 CN** — đúng; truyền thống halakhah về sau phần lớn theo trường phái Hillel — đúng (quy tắc này được phát biểu ở `Eruvin 13b`); nơi "Babylonia và Jerusalem" khớp truyền thống về tiểu sử ông; vùng `Trung Đông/Bắc Phi` đúng. Trường `năm:` dùng dạng "hoạt động k. …" đúng quy ước `CONTRIBUTING.md` cho người chỉ biết khoảng hoạt động.

*Thể thức — đạt:* Shammai là người cùng thời và đối lập thật (đúng nghĩa ứng viên cạnh tranh, không phải cộng sự); Yohanan ben Zakkai (k. 30 TCN – 90 CN) được nêu **kèm chữ "ở thế hệ sau"**, tức người đọc được báo trước. Đây là cách xử lý mẫu mà các mục Ban Cố (-06), Hermogenes (-08) và Eratosthenes (-11) nên theo.

---

## 9. `CH03-BCE01-08` · Vitruvius

**Thể thức (vi phạm §5)** — "Ứng viên cùng lĩnh vực là **Hermogenes**, kiến trúc sư Hy Lạp mà Vitruvius trích dẫn, và **Frontinus**, người viết về hệ cấp nước Rome một thế kỷ sau."
- **Cả hai đều không cùng thời với Vitruvius** (k. 80–15 TCN):
  - **Hermogenes xứ Priene**: hoạt động cuối TK 3 – đầu TK 2 TCN (đền Artemis Leukophryene ở Magnesia khoảng 220–190 TCN; bộ sách hệ thống hoá thức Ionic khoảng 150 TCN). Cách Vitruvius **hơn một thế kỷ về trước**, và văn bản **không hề báo cho người đọc biết điều đó** — chỉ nói "kiến trúc sư Hy Lạp mà Vitruvius trích dẫn", nghe như người đương thời.
  - **Frontinus**: `De aquaeductu` soạn năm 97–98 CN, tức **hơn một thế kỷ sau**. Chỗ này văn bản **có** ghi "một thế kỷ sau", nên không đánh lừa người đọc, nhưng vẫn không thoả §5.
- Hệ quả: mục này **không có một ứng viên hợp lệ nào** theo §5. Thêm nữa, Hermogenes được nêu đúng với tư cách **nguồn mà Vitruvius dẫn lại**, tức là bậc tiền bối chứ không phải đối thủ tranh vị trí — rơi vào đúng lỗi "nêu người không phải ứng viên cạnh tranh".
- Nguồn dùng để kết luận: niên đại Hermogenes qua Wikipedia "Hermogenes of Priene" và tư liệu khảo cổ Magnesia (Vitruvius dẫn ông 5 lần, `De architectura` III.2 và III.6); niên đại Frontinus theo `De aquaeductu` (97–98 CN).
- Sửa đề xuất: thay bằng ứng viên **thật sự cùng thời**: **Lucius Cocceius Auctus** (kiến trúc sư–kỹ sư thời Augustus, xây `Crypta Neapolitana` và cảng Misenum) hoặc **Agrippa** (63–12 TCN, người thực hiện chương trình cấp nước và công trình công cộng lớn nhất của Rome đương thời, và cũng là người Vitruvius phục vụ). So Vitruvius với Agrippa là một so sánh thật và ăn khớp với lập luận (d): Agrippa **xây**, Vitruvius **viết ra lý luận**, và cái truyền được 15 thế kỷ là cái viết.

**Nghi vấn** — "bản thảo **được Poggio Bracciolini tìm lại** năm 1414 và in năm 1486 là văn bản mà Alberti rồi Palladio dựa vào".
- Ba vấn đề chồng lên nhau:
  1. Chữ "tìm lại" hàm ý `De architectura` từng thất truyền. Thực tế nó **chưa bao giờ mất**: còn hơn 80 bản chép tay thời trung cổ, bản cổ nhất và tốt nhất là `British Library MS Harley 2767` chép đầu TK 9 (có thể ở scriptorium triều Charlemagne), và sách được Alcuin, Einhard biết tới. Cái Poggio làm là đưa nó trở lại vòng lưu thông của giới nhân văn Ý, không phải cứu nó khỏi quên lãng.
  2. Năm **1414 so với 1416**: các nguồn không thống nhất; nhiều mô tả bản Harley 2767 ghi 1416. Nếu giữ 1414 thì nên ghi "k. 1414" hoặc nêu cả hai.
  3. **Alberti không thể dựa vào bản in 1486**: `De re aedificatoria` soạn khoảng 1450, trước bản in 36 năm; ông dùng bản chép tay. Câu hiện tại nối "in năm 1486" với "Alberti rồi Palladio" thành một chuỗi, nên sai thứ tự cho vế Alberti. Palladio (`I quattro libri`, 1570) thì đúng là thời đại bản in.
- Hệ quả cho lập luận chọn người: toàn bộ lý do (d) của mục này đặt trên tiền đề "thất truyền rồi được tìm lại". Tiền đề ấy yếu hơn nhiều so với trường hợp Lucretius, nên lập luận cần viết lại chứ không chỉ sửa chữ.
- Câu thay thế đề xuất: "Vitruvius được chọn theo counterfactual (d): `De architectura` là chuyên luận kiến trúc duy nhất còn lại từ thời cổ đại, nên khi giới nhân văn Ý đưa nó trở lại lưu thông từ đầu TK 15 — Poggio Bracciolini là một trong những người làm việc đó — và in lần đầu năm 1486, nó thành văn bản chuẩn mà Alberti rồi Palladio dựng lý luận kiến trúc Phục hưng lên trên."
- **Không kiểm được**: tôi không mở được McEwen (2003) hay bản dịch Rowland (1999) để xem hai sách đó định niên việc Poggio tìm bản thảo là 1414 hay 1416.

*Đã kiểm và **đúng**:* `De architectura` gồm **mười quyển** — đúng; đề tặng Augustus — đúng; "chuyên luận kiến trúc duy nhất còn lại từ thời cổ đại" — đúng và là cách nói chuẩn của ngành; bộ ba `firmitas / utilitas / venustas` — đúng; nội dung bàn quy hoạch đô thị, vật liệu, cấp nước, máy móc — đúng; tỉ lệ thân người ở quyển III là cơ sở bản vẽ `Người Vitruvius` của Leonardo (k. 1490) — đúng. **Bản in đầu (editio princeps) năm 1486 tại Rome do Fra Giovanni Sulpitius da Veroli** — đúng (bản không ghi năm, giới thư mục chấp nhận 1486). Ingrid D. Rowland (dịch, 1999, Cambridge UP) và Indra Kagis McEwen, *Vitruvius: Writing the Body of Architecture* (MIT Press, 2003) — cả hai có thật, đúng năm.

---

## 10. `CH03-BCE01-09` · Cleopatra VII

**Nghi vấn (quy thuộc sai)** — "**Plutarch chép rằng** bà là người **duy nhất** trong dòng họ chịu học tiếng Ai Cập."
- Nguyên văn Plutarch, `Antonius` 27 nói: "…it is said that she knew the speech of many other peoples also, although **the kings of Egypt before her had not even made an effort to learn the native language**, and some actually gave up their Macedonian dialect." Tức Plutarch khẳng định **các vua trước bà** không buồn học — một mệnh đề về quá khứ, không phải mệnh đề "duy nhất trong cả dòng họ" (vốn bao gồm cả các thành viên cùng thời và sau bà). Plutarch cũng gài sẵn chữ "it is said", tức ông đang truyền lại một lời đồn chứ không khẳng định.
- Nguồn dùng để kết luận: bản dịch Perrin của `Antonius` 27 (lexundria.com/plut_ant/27).
- Câu thay thế đề xuất: "Plutarch chép lại lời truyền rằng bà thạo nhiều thứ tiếng, và rằng các vua Ptolemy trước bà thậm chí không buồn học tiếng Ai Cập."

**Nghi vấn (trung lập)** — "vương quốc **giàu nhất** Địa Trung Hải".
- Mệnh đề tối cao không quy thuộc. Đề xuất: "vương quốc giàu nhất vùng Đông Địa Trung Hải theo đánh giá của chính người La Mã đương thời", hoặc đơn giản "vương quốc giàu có nhờ lúa mì và thuế quan".

**Thể thức / Nghi vấn (lựa chọn nhân vật)** — mục "Vì sao chọn" không bảo vệ được Cleopatra theo bốn tiêu chí (a)–(d); lập luận hiện tại chỉ đứng trên một nửa của (d).
- Lập luận hiện tại: "Actium là trận quyết định ngôi vị tối cao ở Rome, và việc bà đưa hạm đội cùng ngân khố Ai Cập vào một phe là điều kiện khiến trận đó xảy ra như đã xảy ra."
  - Đó là một luận cứ về **điều kiện cần cho hình dạng một trận đánh**, không phải về ảnh hưởng tới nhân loại. Và nó tự mâu thuẫn một nửa: nếu Actium quyết định ngôi vị tối cao ở Rome, thì người hưởng và người được atlas ghi công là Augustus — vốn **đã có mặt ngay trong cùng nhóm** (`CH03-BCE01-02`), với chính Actium làm mốc. Cleopatra ở đây là phía thua của một sự kiện đã được tính công cho người khác.
  - (a) phạm vi: không được nêu. (b) độ bền: dòng `Ảnh hưởng tới` duy nhất là "Ai Cập thành tỉnh La Mã và nguồn lúa mì cho Rome" — một hệ quả **của việc bà thất bại**, không phải của việc bà làm. (c) tính nguyên bản: không được nêu, và mục văn xuôi cũng không nêu được đóng góp nguyên bản nào.
  - Chính mục tự viết: "Phần lớn hình ảnh về bà là do đối thủ và văn chương đời sau dựng." Câu ấy là lời thú nhận rằng cái khiến bà nổi bật là **mức nổi tiếng được kiến tạo**, đúng thứ mà tiêu chí (a)–(d) được đặt ra để lọc bỏ.
- Đây không phải đề nghị loại bà khỏi atlas; đây là đề nghị **viết lại lập luận hoặc đổi chỗ**. Nếu giữ, lập luận mạnh nhất thực sự có là (b) qua đường tiếp nhận: Cleopatra là nhân vật nữ được tái dựng liên tục nhất trong văn hoá châu Âu từ Horace và Shakespeare tới nay, và chính lịch sử tiếp nhận đó là một hiện tượng có thật, đo được, kéo dài hai nghìn năm. Nhưng nếu lấy lý do đó thì lĩnh vực nên là `Văn học`/`Chính trị/Nhà nước` chứ không chỉ `Chính trị/Nhà nước`, và phải nói thẳng ra rằng mục ghi nhận **sức sống của một hình tượng**, không phải một đóng góp.
- Phương án thay thế nếu Owner muốn giữ tiêu chí chặt: xem mục 14 dưới đây (ứng viên bị bỏ sót).

**Nghi vấn** — `Kế thừa từ: CH03-BCE01-01 · kế thừa · trực tiếp` (Caesar).
- Cùng vấn đề đã nêu ở mục 2: "kế thừa" mô tả sai một quan hệ liên minh/cá nhân. Đề xuất bỏ cả cặp liên kết.

*Đã kiểm và **đúng**:* niên đại 69–30 TCN; là người cuối cùng cai trị Ai Cập thời Ptolemy; Actium **31 TCN**, bà chết **năm sau (30 TCN)** — đúng; Ai Cập thành tỉnh La Mã năm 30 TCN — đúng; bà tự đặt mình vào khuôn `Nea Isis` để có chính danh với dân bản xứ — đúng; `Kế thừa từ: CH03-BCE03-04` trỏ **đúng** Ptolemaios I Soter, đúng chiều. Duane W. Roller, *Cleopatra: A Biography* (Oxford UP, 2010) — có thật, đúng năm, đúng tác giả (cùng người dịch Strabo ở mục -11). Plutarch, `Antonius` — có thật và đúng là nguồn cổ chính.

*Thể thức — đạt:* Herod Cả (k. 73–4 TCN) **thật sự cùng thời** với Cleopatra (69–30 TCN) và là đối thủ chính trị thật trong vùng. §5 cho phép nêu 1 ứng viên, nên nêu một người là hợp lệ. Lý do loại Herod còn được nhắc lại nhất quán trong Ghi chú biên tập cuối file.

---

## 11. `CH03-BCE01-10` · Lưu Hướng

**Sai** — Liên kết trỏ **sai người**: `Ảnh hưởng tới: CH90-CE15_18-05 · kế thừa · qua trường phái`.
- `CH90-CE15_18-05` trong `content/ch90.md` là **Nguyễn Hoàng (Chúa Tiên, 1525–1613)**, lĩnh vực `Chính trị/Nhà nước` — một chúa mở cõi, không dính gì tới thư mục học hay hiệu khám văn bản.
- Đích định trỏ gần như chắc chắn là **`CH90-CE15_18-08` · Lê Quý Đôn (1726–1784)**, lĩnh vực `Sử học, Triết học`, mà mục ch90 mô tả đúng bằng chính từ khoá của mục Lưu Hướng: "bao quát sử, địa chí, triết học, **thư mục** và **khảo chứng**", "Vân đài loại ngữ là bộ **bách khoa phân loại tri thức theo chủ đề**", "chủ trương **khảo chứng dựa trên đối chiếu văn bản**". Đó chính xác là truyền thống Lưu Hướng.
- Nguồn dùng để kết luận: đọc trực tiếp `content/ch90.md` dòng 405–406 (Nguyễn Hoàng) và 453–466 (Lê Quý Đôn).
- Lại là lỗi lint mù theo đúng cách đã mô tả ở mục 7: `reports/lint-ch03.txt` chỉ báo `[INFO] CH03-BCE01-10: ảnh hưởng tới CH90-CE15_18-05 … (P4 sẽ đồng bộ)`, nghĩa là nếu P4 đồng bộ thật thì Nguyễn Hoàng sẽ được ghi là kế thừa Lưu Hướng.
- Sửa đề xuất: `- CH90-CE15_18-08 · kế thừa · qua trường phái`.
- **Lưu ý khi sửa**: hai lỗi trỏ sai (-06 → Đinh Bộ Lĩnh, -10 → Nguyễn Hoàng) đều là ID **đúng định dạng, đúng nhóm, tồn tại thật** nhưng sai số thứ tự. Đây là dạng lỗi duy nhất mà toàn bộ cổng lint của dự án không thể bắt, và nó đã xảy ra **hai lần trong cùng một nhóm 12 mục** — đáng cân nhắc thêm một bước kiểm thủ công "mở đích ra đọc tên" cho mọi liên kết liên chapter.

**Nghi vấn** — "Thất lược, **bộ phân loại tri thức theo bảy ngành**".
- Thất lược có **bảy phần** nhưng chỉ **sáu ngành thực chất**: phần thứ nhất, `Tập lược` (輯略), là thiên tổng luận chứ không phải một ngành tri thức ngang hàng; sáu ngành còn lại là `Lục nghệ`, `Chư tử`, `Thi phú`, `Binh thư`, `Thuật số`, `Phương kỹ`. Chính vì thế khi Ban Cố dựng `Nghệ văn chí` ông bỏ `Tập lược` và trở lại hệ **sáu ngành**. Nói "bảy ngành" làm sai chính cái điểm mà mục này muốn nêu (mạng phân loại).
- Nguồn dùng để kết luận: chinaknowledge.de mục "Qilüe 七略 and Bielu 別錄"; Wikipedia "Yiwenzhi" và "Liu Xin (scholar)".
- Câu thay thế đề xuất: "…con ông là Lưu Hâm tiếp tục thành Thất lược, bộ phân loại tri thức gồm sáu ngành kèm một thiên tổng luận."

**Thể thức (vi phạm §5)** — "và **Ban Cố**, người đưa thư mục ấy vào Hán thư."
- **Lần thứ hai trong cùng một nhóm** Ban Cố (32–92 CN) được nêu làm "ứng viên cùng lĩnh vực, cùng thời" — ở đây là với Lưu Hướng (k. 77–6 TCN), tức cách nhau khoảng **38 năm tới hơn một thế kỷ**, và lần này cũng **không có chữ nào báo cho người đọc biết**. Xem mục 7 cho trường hợp song song ở `CH03-BCE01-06`.
- Lưu Hâm (k. 50 TCN – 23 CN) thì hợp lệ về niên đại và là ứng viên cạnh tranh thật (ông hoàn thành Thất lược, và đã có tên trong danh sách bị loại ở Ghi chú biên tập).
- Sửa đề xuất: giữ Lưu Hâm, và thay Ban Cố bằng một người **cùng thời thật**, ví dụ **Dương Hùng (53 TCN – 18 CN)** — học giả văn tự và từ phú đương thời, cũng làm việc trong vòng thư viện hoàng cung — hoặc đơn giản ghi rõ "Ban Cố ở thế kỷ sau".

**Nghi vấn (nhỏ)** — "Biệt lục, công trình thư mục **có chú giải đầu tiên** của Trung Hoa".
- Mệnh đề "đầu tiên" không quy thuộc. Khẳng định này đứng được (Biệt lục và Thất lược được coi là bộ thư mục cổ nhất của Trung Hoa, công trình hiệu khám khởi đầu năm **26 TCN** theo lệnh Hán Thành Đế), nhưng theo chuẩn trung lập của dự án nên gắn mốc thay vì để trống: "…bộ thư mục có chú giải sớm nhất còn truy được của Trung Hoa, khởi làm từ năm 26 TCN."

**Nghi vấn (nhỏ, phân loại)** — `lĩnh vực: Giáo dục, Sử học`.
- Đóng góp cốt lõi của Lưu Hướng là **thư mục học và hiệu khám văn bản**, mà từ vựng `FIELDS` 16 mục của dự án không có mục tương ứng. `Giáo dục` là chọn thay thế có thể hiểu được, nhưng người đọc tra theo lĩnh vực sẽ không tìm thấy ông. Không phải lỗi của mục này — là một lỗ hổng từ vựng đáng ghi vào "Điểm cần kiểm chứng thêm", cùng loại với lỗ hổng §5 đã treo ở Ch2.

*Đã kiểm và **đúng**:* niên đại k. 77–6 TCN; việc hiệu khám thư viện hoàng cung, đối chiếu bản sao, loại trùng lặp, định bản chuẩn và viết bài tự cho từng sách — đúng; tập hợp các bài tự thành `Biệt lục` — đúng; `Biệt lục` nay chỉ còn qua trích dẫn — đúng; `Thất lược` là nguồn trực tiếp của `Hán thư · Nghệ văn chí` — đúng (Ban Cố ghi rõ điều đó); hệ `kinh–sử–tử–tập` (`tứ bộ`) truy nguồn về mạng phân loại này — đúng theo cách trình bày chuẩn; ông biên `Chiến quốc sách` và `Liệt nữ truyện` — đúng. `Kế thừa từ: CH03-BCE01-06` trỏ **đúng** Tư Mã Thiên. Endymion Wilkinson, *Chinese History: A New Manual* — có thật; bản in thứ năm năm **2018** tồn tại, và dòng Nguồn ghi "mục thư mục học" thay vì bịa số chương, đúng tinh thần `CONTRIBUTING.md` §3.

---

## 12. `CH03-BCE01-11` · Strabo

**Thể thức (vi phạm §5)** — "Ứng viên là **Eratosthenes**, đã được chọn ở nhóm trước, và **Ptolemy ở thế kỷ 2 CN**, người lập bảng toạ độ."
- **Không một ứng viên nào cùng thời với Strabo** (k. 64 TCN – 24 CN):
  - Eratosthenes: k. 276–194 TCN theo chính `content/ch03.md` — cách **hơn một thế kỷ rưỡi về trước**.
  - Ptolemy: k. 100–170 CN — cách **hơn một thế kỷ về sau**.
- Cách viết hiện tại **có** báo cho người đọc biết khoảng cách ("đã được chọn ở nhóm trước", "ở thế kỷ 2 CN"), nên không đánh lừa ai — đây là điểm khác biệt quan trọng so với trường hợp Ban Cố ở mục -06 và -10, và với Hermogenes ở -08. Nhưng §5 đòi "nêu ĐÍCH DANH 1–2 người cùng lĩnh vực, **cùng thời** đã được cân nhắc", và mục này nêu **không người nào** như vậy. Sự trung thực của cách viết làm nhẹ lỗi chứ không xoá lỗi: người đọc vẫn không biết được Strabo đã vượt qua ai trong số những người đang viết cùng lúc với ông.
- Có ứng viên cùng thời thật và không hiếm: **Diodorus Siculus** (k. 90–30 TCN, `Bibliotheca historica` có phần địa chí lớn), **Juba II xứ Mauretania** (k. 48 TCN – 23 CN, viết khảo địa về Libya và Arabia, được chính Pliny dẫn), **Isidore xứ Charax** (hoạt động k. 1 CN, `Parthian Stations`), và bản đồ cùng `commentarii` của **Agrippa** (63–12 TCN) — tức một công trình địa lý nhà nước đương thời, đúng loại đối chiếu mà lập luận "viết cho người cai trị" của mục này cần.
- Sửa đề xuất: "Ứng viên cùng thời là Juba II xứ Mauretania, người viết khảo địa về Libya và Arabia, và tấm bản đồ cùng `commentarii` của Agrippa, công trình địa lý nhà nước đương thời. Strabo được chọn theo phạm vi (a) của văn bản còn lại: cả hai công trình kia chỉ còn qua trích dẫn, còn bộ của ông sống sót gần trọn, nên hiểu biết hiện nay về thế giới quan Hellenistic chủ yếu đi qua ông."

**Nghi vấn (quy ước vùng — mâu thuẫn nội bộ)** — `nơi: Amaseia, xứ Pontus, và Rome | vùng: **Trung Đông/Bắc Phi**`.
- Đặt cạnh `CH03-BCE02-03 · Hipparchus xứ Nicaea`: `nơi: Nicaea, Bithynia, và đảo Rhodes | vùng: **Châu Âu**`. Bithynia và Pontus là hai vùng kề nhau trên bờ nam Hắc Hải thuộc Anatolia, cả hai nhân vật đều nói tiếng Hy Lạp, và địa điểm thứ hai của cả hai đều nằm ở Châu Âu (Rome / Rhodes). Vậy mà hai người được xếp **hai vùng ngược nhau**.
- Khối "Quy ước vùng cho thế giới Hellenistic" trong Ghi chú biên tập chỉ xử lý **Alexandria**, không nói gì về Tiểu Á, nên quy ước hiện hành không giải thích được chênh lệch này. Vì chính khối đó tự nhận là "chỗ đáng tranh luận nhất về mặt phương pháp của chapter", để lọt một mâu thuẫn trực tiếp bên trong nó là vấn đề thật.
- Hệ quả định lượng: nếu đổi Strabo sang `Châu Âu` cho nhất quán với Hipparchus, nhóm BCE01 thành **8 Châu Âu / 2 Trung Đông-Bắc Phi / 2 Đông Á**, và `Trung Đông/Bắc Phi` chỉ còn Hillel và Cleopatra.
- Đề xuất: hoặc đổi Strabo sang `Châu Âu`, hoặc đổi Hipparchus sang `Trung Đông/Bắc Phi`, và bổ sung một câu vào khối quy ước nói rõ Tiểu Á được xử lý thế nào. Không nên để nguyên.

**Nghi vấn (trung lập, nhỏ)** — "mô tả **đầy đủ nhất** về thế giới có người ở mà thời cổ đại để lại".
- Khẳng định này đứng được, nhưng là mệnh đề tối cao không quy thuộc. Dueck (2000) — nguồn mục này đã dẫn — là chỗ quy thuộc sẵn có; chỉ cần "theo Dueck (2000)" hoặc "theo cách đánh giá chuẩn của ngành".

*Đã kiểm và **đúng**:* `Địa lý học` gồm **mười bảy quyển** và còn gần trọn vẹn (chỉ quyển VII khuyết) — đúng; đối tượng người đọc là nhà cai trị và tướng lĩnh chứ không phải nhà toán học — đúng, chính Strabo nói vậy ở quyển I; tác phẩm giữ lại nhiều đoạn Eratosthenes, Polybius và Pytheas mà bản gốc đã mất — đúng, và đây là một trong những giá trị được ngành nhấn mạnh nhất. Niên đại k. 64 TCN – 24 CN khớp Wikidata. Bản dịch **Duane W. Roller, *The Geography of Strabo*, Cambridge UP, 2014** — có thật, đúng năm. **Daniela Dueck, *Strabo of Amasia: A Greek Man of Letters in Augustan Rome*, Routledge, 2000** — có thật, đúng năm. `Kế thừa từ: CH03-BCE03-09` trỏ **đúng** Eratosthenes, `CH03-BCE02-04` trỏ **đúng** Polybius, và mức "qua trường phái" đúng cho cả hai (cả hai đều chết trước khi Strabo sinh).

---

## 13. `CH03-BCE01-12` · Posidonius

**Dòng Nguồn được yêu cầu kiểm riêng là ĐÚNG.** `Strabo, Địa lý học, **q. III** (ghi lại quan sát thuỷ triều)` — **đúng quyển**. Kiểm trực tiếp văn bản Strabo quyển III chương 5 (bản Thayer / LacusCurtius): các mục **III.5.7–9** trình bày đúng quan sát của Posidonius ở Gades, gồm cả ba chu kỳ ông nêu (ngày, tháng, năm) và quan hệ với vị trí Mặt Trăng. Nếu muốn chặt hơn nữa, có thể ghi `q. III, 5.7–9`.

**Sai** — "một trong những lần **sớm nhất** một quy luật thiên văn được nối với hiện tượng trên Trái Đất bằng dữ liệu."
- Hai tiền lệ rõ ràng, và tiền lệ thứ hai được ghi lại **bởi chính Strabo**, tức bởi chính nguồn mục này đang dẫn:
  - **Pytheas xứ Massalia** (TK 4 TCN) là người Hy Lạp đầu tiên ghi quan hệ giữa thuỷ triều và các tuần trăng, và ông quan sát hai con nước mỗi ngày trăng.
  - **Seleucus xứ Seleucia** (k. 150 TCN) — Strabo chép rằng chính Seleucus là người **đầu tiên** phát biểu thuỷ triều do Mặt Trăng hút, và biên độ phụ thuộc vị trí Mặt Trăng so với Mặt Trời.
- Posidonius quan sát ở Gades khoảng **100 TCN**, tức sau cả hai. Đóng góp thật của ông là **khối lượng quan sát có hệ thống tại một điểm** và việc nối ba chu kỳ, không phải tính tiên phong.
- Thêm một điểm làm yếu câu hiện tại: Posidonius quy **nguyên nhân** thuỷ triều cho **sức nóng của Mặt Trăng** (ông cho Mặt Trăng là hỗn hợp khí và lửa), tức ông nối hiện tượng với một vật thể thiên văn nhưng bằng một cơ chế sai — gọi đó là "một quy luật thiên văn được nối với hiện tượng trên Trái Đất" là nói quá.
- Nguồn dùng để kết luận: Wikipedia "Theory of tides", "Seleucus of Seleucia", "Poseidonius"; và chính Strabo III.5.7–9 đã mở ở trên.
- Câu thay thế đề xuất: "…quan sát nhiều năm ở Gades cho ông nối ba chu kỳ thuỷ triều — ngày, tháng và năm — với vị trí Mặt Trăng; Pytheas và Seleucus đã nêu quan hệ này trước, nhưng Posidonius là người đưa vào một khối quan sát có hệ thống tại một điểm."

**Nghi vấn** — nguồn duy nhất cho quan sát Gades cũng chính là nguồn **phản bác** nó, và mục không nói ra.
- Ở `III.5.8`, Strabo chất vấn thẳng lô-gic của Posidonius: ông hỏi làm sao người Gades quan sát được chu kỳ năm vốn chỉ xảy ra mỗi năm một lần trong khi lại bỏ sót hiện tượng ngày vốn xảy ra liên tục. Mục này dùng Strabo làm bằng chứng cho giá trị của quan sát ấy mà không nhắc rằng Strabo nghi ngờ nó. Theo yêu cầu trung lập, nên ghi một mệnh đề ngắn.
- Đề xuất thêm vào cuối đoạn văn xuôi: "Chính Strabo, người ghi lại quan sát này, cũng chất vấn độ tin cậy của nó."

**Nghi vấn (quy ước vùng)** — `nơi: Apamea, xứ Syria, và đảo Rhodes | vùng: **Châu Âu**`.
- Theo quy ước "nơi làm việc thực tế" mà chapter tự đặt, Rhodes (nơi ông lập trường và dạy) là Châu Âu, nên lựa chọn này **đứng được**. Ghi ở đây chỉ để đặt cạnh mục -11: Posidonius sinh ở Syria mà ghi Châu Âu, Strabo sinh ở Anatolia mà ghi Trung Đông/Bắc Phi — hai mục liền nhau áp dụng hai lô-gic khác nhau. Sửa một trong hai là đủ, nhưng phải nhất quán.

**Thể thức — nửa đạt**, hai ứng viên đều có vấn đề nhưng ở mức nhẹ:
- **Panaetius** (k. 185–110 TCN): có chồng lấn thật với Posidonius (k. 135–51 TCN) khoảng 25 năm và là thầy ông, nên **không vi phạm** yêu cầu cùng thời. Nhưng ông là **bậc thầy và tiền bối**, và giai đoạn hoạt động chính của ông nằm ở thế kỷ 2 TCN (nhóm BCE02), nên gọi là "ứng viên cạnh tranh cho một chỗ trong nhóm BCE01" là không chặt — cùng dạng vấn đề với Hermogenes ở mục -08, chỉ nhẹ hơn vì niên đại thật sự chồng lấn.
- **Asclepiades xứ Bithynia** (k. 124–40 TCN): cùng thời **thật**, nhưng lĩnh vực là `Y học`, còn Posidonius ghi `Triết học, Khoa học tự nhiên`. Nối được (y học của Asclepiades dựa trên vật lý hạt), nhưng §5 đòi "cùng lĩnh vực" và mục không giải thích mối nối ấy.
- Nếu muốn một ứng viên cùng thời **và** cùng lĩnh vực chuẩn xác: **Antiochus xứ Ascalon** (k. 130–68 TCN), người cùng thời, cũng dạy Cicero, và cũng là một đầu mối của việc triết học Hy Lạp vào Rome — đối chiếu với ông thì lập luận (c) của mục này sắc hơn hẳn.

*Đã kiểm và **đúng**:* niên đại k. 135–51 TCN khớp Wikidata; ông viết tiếp bộ sử của Polybius — đúng (`Historiai` nối từ 146 TCN); khảo tả các tộc người phương tây — đúng, và phần lớn những gì ta biết về người Celt qua nguồn Hy Lạp đi qua ông; đo lại chu vi Trái Đất ra con số nhỏ hơn Eratosthenes, con số ấy qua Ptolemy thành một trong các cơ sở khiến Columbus tính sai khoảng cách — đúng và là cách trình bày chuẩn; trước tác mất hết, còn lại qua trích dẫn của Cicero, Strabo và Seneca — đúng. **Ian G. Kidd, *Posidonius: The Translation of the Fragments* (Cambridge UP, 1999)** — có thật, đúng năm; đây là Tập III của bộ Posidonius do Cambridge xuất bản, nên nếu muốn chặt có thể ghi "tập III". `Kế thừa từ: CH03-BCE03-07` trỏ **đúng** Zeno xứ Citium. `Ảnh hưởng tới: CH03-BCE01-03 · kế thừa · **trực tiếp**` trỏ **đúng** Cicero và **đúng mức bằng chứng** — Cicero học Posidonius ở Rhodes khoảng 78–77 TCN. Đây là liên kết "trực tiếp" đúng duy nhất trong cả chùm liên kết của Cicero (xem mục 4).

---

## 14. Đánh giá lựa chọn nhân vật — ai đáng ra phải có mặt mà chưa từng được cân nhắc?

Tôi đã đối chiếu 12 mục của nhóm với toàn bộ khối "Ứng viên mạnh đã bị loại và lý do" ở `## Ghi chú biên tập` cuối `content/ch03.md`. Danh sách bị loại có nhắc tới giai đoạn này qua các tên: Pompey, Sulla, Horace, Catullus, Sallust, Herod Cả, Lưu Hâm, Gaius Gracchus. Bốn người dưới đây **không xuất hiện ở bất kỳ đâu** trong file — không trong 12 mục, không trong danh sách bị loại, không trong bất kỳ mục "Vì sao chọn" nào. Đếm bằng `grep` trên `content/ch03.md`.

### 14.1 Marcus Vipsanius Agrippa (63–12 TCN) — thiếu sót nặng nhất của nhóm
- **Số lần xuất hiện trong `ch03.md`: 0.** Chưa từng được cân nhắc, kể cả để loại.
- (a) phạm vi: ông là người chỉ huy thực tế thắng trận **Actium** — chính trận mà nhóm này viện dẫn ba lần (ở mục -02, -09 và trong Ghi chú biên tập) làm bản lề của thế kỷ. Hiện Actium được tính công hoàn toàn cho Augustus và tính "điều kiện" cho Cleopatra, còn người cầm quân thì vắng mặt.
- (b) độ bền: chương trình cấp nước của ông (Aqua Julia, Aqua Virgo — **Aqua Virgo vẫn đang cấp nước cho Đài phun Trevi tới hôm nay**) và hệ thống cống `Cloaca Maxima` được ông tu bổ là hạ tầng đô thị còn vận hành sau hai mươi thế kỷ. Đó là độ bền vật chất đo được, không phải suy diễn.
- (c) tính nguyên bản: tấm bản đồ thế giới (`orbis terrarum`) cùng bộ `commentarii` đo đạc do ông chủ trì, dựng ở `Porticus Vipsania`, là lần đầu một nhà nước lập bản đồ toàn lãnh thổ như công cụ cai trị — một hạng mục khác hẳn địa lý học văn chương của Strabo, và Pliny Già dựa vào nó.
- (d) counterfactual: nếu không có Agrippa, phe Octavianus rất có thể thua ở Naulochus và Actium — tức toàn bộ mục `CH03-BCE01-02` sẽ phải viết khác.
- **Đối chiếu trực tiếp với mục đang có:** Agrippa mạnh hơn Cleopatra (`-09`) ở cả (b) và (c), và mạnh hơn ở (d) theo đúng cách lập luận mà mục Cleopatra đang dùng — nếu Actium là lý do đưa Cleopatra vào, thì nó là lý do mạnh hơn để đưa Agrippa vào. Ông cũng ăn khớp với mục Vitruvius (`-08`): Vitruvius phục vụ chương trình công trình của Agrippa, nên hai mục soi sáng nhau.
- **Đề nghị:** hoặc đưa Agrippa vào thay Cleopatra, hoặc — nếu giữ Cleopatra theo lập luận lịch sử tiếp nhận đã nêu ở mục 10 — thì **bắt buộc** phải nêu Agrippa đích danh trong danh sách bị loại kèm lý do. Để trống hoàn toàn là lỗ hổng lớn nhất của nhóm.

### 14.2 Varro (Marcus Terentius Varro, 116–27 TCN) — được nêu nửa chừng rồi bỏ rơi
- **Số lần xuất hiện: 1**, và chỉ trong một mệnh đề cụt ở mục Cicero: "…nhưng chỉ một trường phái, **và Varro**." Không có lý do loại, và **không có tên trong danh sách bị loại ở Ghi chú biên tập** — tức ông không được xử lý theo quy trình của chính chapter.
- Đây là chỗ bất đối xứng rõ nhất của nhóm: chapter dành một suất cho **Lưu Hướng** (`-10`) vì "hiệu khám có phương pháp", "viết tự cho từng sách", "phân loại tri thức" — và Varro là người làm **đúng loại việc đó**, ở **đúng thế kỷ đó**, ở đầu kia lục địa Á–Âu: `Antiquitates rerum humanarum et divinarum` (41 quyển) là công trình hệ thống hoá toàn bộ tôn giáo và thiết chế La Mã; `De lingua Latina` là khảo cứu ngôn ngữ học Latinh sớm nhất còn lại; `Disciplinae` định ra khung "bảy môn khai phóng" mà toàn bộ giáo dục châu Âu trung cổ dựng trên đó; `Res rusticae` là chuyên luận nông học La Mã còn nguyên.
- (b) độ bền: hiểu biết hiện nay về tôn giáo La Mã cổ phần lớn đi qua Varro, vì Augustine trích ông dày đặc trong `De civitate Dei` — chính xác cùng cơ chế "còn lại nhờ người sau trích" mà mục Strabo (`-11`) dùng làm lý do chọn người.
- **Đề nghị:** nếu giữ nguyên 12 mục, phải bổ sung Varro vào danh sách bị loại với lý do thật. Nếu mở lại trần nhóm thì ông là ứng viên đầu tiên cùng Agrippa. Việc atlas có Lưu Hướng mà không có Varro, trong khi chapter tự đặt mục tiêu "tránh thiên lệch châu Âu", là một kết quả ngược đời: thiên lệch ở đây lại đang **chống** châu Âu, ở đúng chỗ châu Âu có ứng viên tương đương.

### 14.3 Dương Hùng (揚雄, 53 TCN – 18 CN) — lấp được phần Đông Á còn mỏng
- **Số lần xuất hiện: 0** (kiểm cả "Dương Hùng" và "Yang Xiong").
- Cùng thời và cùng môi trường thư viện hoàng cung với Lưu Hướng. `Phương ngôn` (方言) là **khảo sát phương ngữ có hệ thống đầu tiên của Trung Hoa và là một trong những công trình loại này sớm nhất của thế giới**; `Thái huyền kinh` là nỗ lực dựng một hệ vũ trụ luận hình thức song song với Kinh Dịch; `Pháp ngôn` mô phỏng Luận ngữ để phản biện tư trào đương thời.
- Mạnh ở (c) tính nguyên bản — tiêu chí mà nhóm BCE01 hiện khá nghèo: trong 12 mục, chỉ `-06`, `-10` và `-12` lấy (c) làm lý do chính.
- Ông cũng sẽ lấp một lỗ hổng lĩnh vực: nhóm BCE01 hiện **không có mục nào thuộc `Ngôn ngữ học`, `Toán học`, `Y học` hay `Kinh tế`**.
- **Đề nghị:** ít nhất đưa vào danh sách bị loại kèm lý do.

### 14.4 Lỗ hổng vùng mà Ghi chú biên tập chỉ thừa nhận một nửa
- Khối "Điểm cần kiểm chứng thêm" có một mục rất đáng khen: thừa nhận thẳng "Nhóm BCE01 không có mục nào thuộc vùng Nam Á… Ghi ra thay vì lấp bằng một cái tên yếu." Đây là cách xử lý đúng.
- Nhưng nhóm cũng **không có mục nào thuộc `Châu Phi hạ Sahara`, `Châu Mỹ`, `Trung Á`, `Đông Nam Á` và `Châu Đại Dương`**, và không có dòng nào thừa nhận điều đó. Nếu đã chọn cách ghi ra khoảng trống Nam Á thì nên ghi ra cả phần còn lại trong cùng một câu, nếu không thì việc chỉ nêu Nam Á trông như một lựa chọn tuỳ tiện.
- Riêng Nam Á, nếu Owner muốn xem lại kết luận "không có ứng viên": sự kiện có niên đại chắc nhất của Nam Á TK 1 TCN là việc **kinh điển Pali lần đầu được chép thành văn tại Aluvihāra, Sri Lanka, khoảng 29 TCN**, dưới triều **Vaṭṭagāmaṇi Abhaya** (trị vì 103, rồi 89–77 TCN). Nó thoả (a), (b) và (d) rất mạnh. Vướng mắc thật là ở quy tắc "nhân vật": sự kiện gắn với một tập thể tăng đoàn, còn ông vua thì có niên đại nhưng vai trò là bảo trợ. Tôi **không kết luận** nên đưa vào hay không — nhưng nó xứng đáng được **nêu đích danh rồi loại có lý do**, thay vì gộp vào mệnh đề "rất ít nhân vật định danh được bằng tư liệu đương thời".

### 14.5 Nhận xét về cân bằng tổng thể của nhóm
- Độ phủ hiện tại: **12 lĩnh vực** (vượt xa sàn 4 của §5) nhưng chỉ **3 vùng** (đúng sàn), phân bố **7 Châu Âu / 3 Trung Đông-Bắc Phi / 2 Đông Á**. Nếu sửa quy ước vùng cho Strabo theo mục 12 thì thành **8 / 2 / 2**.
- Thực chất còn lệch hơn con số: trong 12 mục, **9 mục** lấy Rome làm khung tham chiếu chính — bảy người La Mã hoặc viết bằng tiếng Latinh, cộng Cleopatra (toàn bộ lập luận chọn bà là về nội chiến La Mã) và Strabo (`nơi:` ghi Rome, và Dueck đặt ông trong "Augustan Rome"). Chỉ `-06`, `-07` và `-10` nằm ngoài quỹ đạo đó.
- §5.5 yêu cầu "Tránh thiên lệch châu Âu; chủ động xét Trung Hoa, Ấn Độ, Ba Tư…". Thế kỷ 1 TCN đúng là thế kỷ Rome áp đảo về tư liệu, nên độ lệch này **có cơ sở thật** chứ không phải lỗi thuần tuý. Nhưng kết hợp với 14.2 (có Lưu Hướng mà không có Varro) và 14.3 (bỏ trống Dương Hùng), bức tranh hiện tại là: nhóm **vừa** thiên lệch châu Âu về số lượng, **vừa** bỏ sót ứng viên châu Âu mạnh nhất — tức vấn đề không nằm ở tỉ lệ vùng mà ở chỗ **quy trình sàng lọc chưa được chạy đều tay**. Bốn cái tên ở 14.1–14.3 và 14.4 nên được đưa vào danh sách bị loại kèm lý do, bất kể cuối cùng có ai được đổi chỗ hay không.
- Một ghi nhận tích cực để cân bằng: phần **Ba Tư / Parthia** cũng trống, nhưng đây là khoảng trống hợp lý — TK 1 TCN Parthia không để lại nhân vật nào định danh được bằng tư liệu đương thời ngang tầm các mục đang có (Orodes II và Phraates IV chỉ được biết qua nguồn La Mã thù địch). Không coi đây là thiếu sót.

---

## 15. Tổng hợp — thứ tự ưu tiên sửa

**Phải sửa trước khi commit (sai sự thật hoặc trỏ sai người):**
1. `-06` `Ảnh hưởng tới: CH90-CE10_14-02` trỏ vào **Đinh Bộ Lĩnh** thay vì một nhà sử học. → mục 7.
2. `-10` `Ảnh hưởng tới: CH90-CE15_18-05` trỏ vào **Nguyễn Hoàng** thay vì **Lê Quý Đôn (`CH90-CE15_18-08`)**. → mục 11.
3. `-03` hai dòng `Kế thừa từ` ghi mức **"trực tiếp"** cho Carneades (chết 23 năm trước khi Cicero sinh) và Polybius (chết 12 năm trước). → mục 4.
4. `-12` "một trong những lần **sớm nhất**" — Pytheas và Seleucus đã làm trước, và Strabo ghi rõ Seleucus là người đầu tiên. → mục 13.
5. `-05` "Bucolica **dựng ra** khuôn thơ điền viên" — khuôn ấy là của Theocritus. → mục 6.
6. `-01` dòng Nguồn `SPQR … ch. 7–8` — ch. 8 là "The Home Front", không bàn Caesar. → mục 2.
7. `-07` `Kế thừa từ: CH03-BCE02-11` (Judah Maccabee) thay vì Shemaiah và Avtalyon, vốn nằm ngay trong `Avot 1:12` mà mục đã dẫn. → mục 8.
8. `-10` "Thất lược … **bảy ngành**" — sáu ngành kèm một thiên tổng luận. → mục 11.

**Lỗi thể thức §5 (ứng viên không cùng thời):**
9. `-06` và `-10` cùng nêu **Ban Cố (32–92 CN)** làm ứng viên, **không báo người đọc biết khoảng cách** — nặng nhất vì gây hiểu nhầm. → mục 7, 11.
10. `-08` **cả hai** ứng viên đều không cùng thời (Hermogenes trước ~1 thế kỷ và không được báo; Frontinus sau ~1 thế kỷ, có báo). → mục 9.
11. `-11` **cả hai** ứng viên đều không cùng thời (Eratosthenes, Ptolemy) — có báo người đọc, nên nhẹ hơn, nhưng vẫn là nhóm duy nhất cùng `-08` không nêu được ứng viên hợp lệ nào. → mục 12.
12. `-04` (Epicurus) và `-12` (Panaetius) ở mức nhẹ. → mục 5, 13.

**Trung lập / quy thuộc (mệnh đề tối cao không nói theo ai):** `-03` "được đọc liên tục nhất"; `-04` "trình bày đầy đủ **duy nhất**" và "bản sao **duy nhất**"; `-05` "không tác giả Latinh nào khác có"; `-09` "vương quốc **giàu nhất**" và quy thuộc sai cho Plutarch; `-10` "**đầu tiên**"; `-11` "**đầy đủ nhất**"; `**Bối cảnh**` "Hellenistic **cuối cùng**". → mục 1, 4, 5, 6, 10, 11, 12.

**Vấn đề cấu trúc cần Owner quyết:**
13. Quy ước vùng cho Tiểu Á: Strabo (`Trung Đông/Bắc Phi`) mâu thuẫn trực tiếp với Hipparchus (`Châu Âu`), và khối quy ước trong Ghi chú biên tập không phủ trường hợp này. → mục 12.
14. Lập luận chọn **Cleopatra** chỉ đứng trên một nửa tiêu chí (d), và (d) ấy quy công cho một trận đánh đã được tính cho Augustus trong cùng nhóm. → mục 10.
15. **Agrippa, Varro, Dương Hùng** chưa từng được cân nhắc dù chỉ để loại; khoảng trống vùng chỉ được thừa nhận cho Nam Á. → mục 14.
16. Nhãn quan hệ **"kế thừa"** đang bị dùng cho các quan hệ **bảo trợ và liên minh** (Caesar→Cleopatra, Augustus→Virgil, Augustus→Vitruvius, Hán Vũ Đế→Tư Mã Thiên). Từ vựng `RELATION_TYPES` bốn giá trị không có chỗ cho loại quan hệ này — đáng ghi vào "Điểm cần kiểm chứng thêm" cùng với lỗ hổng `FIELDS` thiếu mục thư mục học (mục 11).

**Những chỗ đã kiểm và ĐÚNG, không cần đụng tới** (ghi lại để vòng sau khỏi kiểm lại): 12/12 Q-ID; `Mishnah Shevi'it 10:3` cho prosbul; `Avot 1:12–14` cho Hillel (đúng tới từng câu); `Strabo, Địa lý học, q. III` cho quan sát thuỷ triều của Posidonius (chính xác là III.5.7–9); lịch Julius 46 TCN với năm trung bình 365,25 ngày; Actium 31 TCN; Poggio tìm Lucretius 1417; Vitruvius in lần đầu 1486; Petrarca tìm thư Cicero 1345; SEP `entries/cicero/` tồn tại và đúng chủ đề; Sử ký 130 thiên và cấu trúc năm phần; `De architectura` 10 quyển; `De rerum natura` 6 quyển; `Địa lý học` 17 quyển; và toàn bộ thông tin xuất bản của Eck (2003), Thomas & Ziolkowski (2014), Durrant (1995), Cohen (2014), Rowland (1999), McEwen (2003), Roller (2010 và 2014), Dueck (2000), Kidd (1999), Greenblatt (2011), Wilkinson (2018).

**Không kiểm được** (ghi thẳng, không đoán): P569 của Strabo trên Wikidata (bị rate-limit, chỉ dựa vào trường mô tả); mục lục và cách định niên bên trong Durrant (1995), McEwen (2003), Rowland (1999), Greenblatt (2011) — nên không khẳng định được các sách này chọn mốc 99 hay 98 TCN cho cung hình, 1414 hay 1416 cho Poggio–Vitruvius, hay có dùng chữ "bản sao duy nhất" hay không.
