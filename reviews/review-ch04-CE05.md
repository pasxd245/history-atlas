# Bình duyệt độc lập — Chapter 4, nhóm CE05 (TK 5, 401–500)

Phạm vi: dòng **Bối cảnh** của nhóm CE05, 12 mục `CH04-CE05-01` → `-12`, và toàn bộ `## Ghi chú biên tập` của `content/ch04.md`.
Người rà: agent bình duyệt độc lập (không viết chapter). Ngày: 2026-10-31.
Xếp loại: **Sai** (chắc chắn sai, có nguồn) · **Nghi vấn** (nhiều khả năng sai hoặc không chống đỡ được) · **Thiếu** (đúng nhưng bỏ mất điều kiện/ngữ cảnh làm câu thành gây hiểu sai) · **Thể thức** (vi phạm §5 / CONTRIBUTING).

---

## 0. Kiểm nền (chạy trước, áp dụng cho cả nhóm)

**Q-ID — 12/12 trỏ đúng người.** Đối chiếu `wbgetentities` (labels/descriptions/P569/P570):

| ID | Q | nhãn Wikidata | năm trong file | P569/P570 | kết luận |
|---|---|---|---|---|---|
| -01 | Q8018 | Augustine of Hippo | 354–430 | 354 / 430 | khớp |
| -02 | Q43954 | Leo I | k. 400–461 | 390 **hoặc** 400 / 461 | khớp (dung sai Trung bình ±25) |
| -03 | Q271809 | Proclus | 412–485 | 412 / 485 | khớp |
| -04 | Q36724 | Attila | k. 406–453 | 395/400/500 / 453 | khớp (Trung bình) |
| -05 | Q160353 | Theodosius II | 401–450 | 401 / 450 | khớp |
| -06 | Q11903 | Hypatia | k. 360–415 | 360 / 415 | khớp |
| -07 | Q335293 | Kumārajīva | 344–413 | 344 / 413 | khớp |
| -08 | Q335247 | Buddhaghosa | hoạt động k. 410–450 | 401 / 500 | bỏ qua đối chiếu (dạng `hoạt động`) |
| -09 | Q11359 | Aryabhata | 476–550 | 476 / 550 | khớp |
| -10 | Q740373 | Fan Ye | 398–445 | 398 / 445 | khớp |
| -11 | Q227444 | Zu Chongzhi | 429–500 | 429 / 500 | khớp |
| -12 | Q1327614 | Emperor Xiaowen of Northern Wei | 467–499 | 467 / 499 | khớp |

Không có lỗi Q-ID trỏ nhầm người ở nhóm này.

**URL nguồn.** `https://plato.stanford.edu/entries/proclus/` → **HTTP 200**, bài có thật, đúng về Proclus. Đây là URL duy nhất trong nhóm CE05.

**Danh sách nhân vật đã được chọn trong atlas** (221 mục, `grep '^### ' content/ch0*.md content/ch90.md`) — dùng cho kiểm "ứng viên bị loại nhưng thực ra đã được chọn". Kết quả chi tiết ở §13.

---
## Bối cảnh nhóm CE05

**Thể thức — ĐẠT theo cách đếm từ.** Template §5 ghi `**Bối cảnh (≤ 60 chữ)**`. Dòng thực tế **58 từ** → trong trần. (Nếu "chữ" được hiểu là **âm tiết** thì mọi dòng Bối cảnh trong atlas đều vượt trần — đó là vấn đề định nghĩa của template, không phải lỗi của nhóm CE05. Nên chốt định nghĩa ở `prompts/atlas-prompt.md`.)

**Thiếu.** "Phật giáo ... được hệ thống hoá bằng tiếng Pali ở Sri Lanka" — đúng, nhưng dòng Bối cảnh nêu bốn chuyển biến và cả bốn đều ở Âu/Đông Á/Nam Á. Nhóm CE05 có một mục Trung Đông/Bắc Phi (Augustinô) và một mục nữa (Hypatia) cũng Bắc Phi, nhưng cả hai đều là nhân vật Hy–La; Ba Tư Sasan (triều Peroz I, chiến tranh với Hephthalite, mất Peroz năm 484) và Ấn Độ Gupta (suy sụp trước Hephthalite) biến mất hoàn toàn khỏi cả dòng Bối cảnh lẫn danh sách mục — trong khi nhóm CE03 và CE04 đều có hai mục Sasan. Đây là chỗ nên nói thẳng là nhóm này bỏ trắng Ba Tư.

---

## CH04-CE05-01 · Augustinô thành Hippo

**1. Nghi vấn — "không tác giả Kitô giáo nào khác được cả Thomas Aquinas lẫn Luther và Calvin cùng viện dẫn làm thẩm quyền"**
Nguyên văn: *"không tác giả Kitô giáo nào khác được cả Thomas Aquinas lẫn Luther và Calvin cùng viện dẫn làm thẩm quyền."*
Câu này sai ở dạng tuyệt đối. Cả ba đều viện dẫn Hieronymus, Ambrosiô, Gregôriô Cả và Gioan Kim Khẩu làm thẩm quyền — Calvin đặc biệt dẫn Kim Khẩu dày đặc trong *Institutio*. Điều đúng và kiểm được là Augustinô là người **được dẫn nhiều nhất**, không phải người **duy nhất** được cả ba dẫn.
Câu thay thế đề xuất: *"...: không tác giả Kitô giáo hậu Tân Ước nào khác được cả Thomas Aquinas lẫn Luther và Calvin viện dẫn dày đặc đến thế."*

**2. Nghi vấn — "tác phẩm phương Tây đầu tiên lấy đời sống nội tâm của chính tác giả làm đối tượng khảo sát"**
Cách diễn đạt đã khéo hơn "tự truyện đầu tiên", nhưng vẫn cần hàng rào. Phản ví dụ cùng thế kỷ hoặc trước: **Libanius, *Oration I* (Autobiography, soạn k. 374)** và **Gregôriô thành Nazianzus, *De vita sua* (k. 382)** — cả hai đều là tự thuật của chính tác giả và đều có trước *Confessiones* (397–400). Mục có thể tự bảo vệ bằng chữ "phương Tây" (hai tác phẩm kia thuộc phần Hy Lạp hoá của đế chế), nhưng hàng rào đó không được nói ra, nên người đọc nhận một tuyên bố mạnh hơn mức tác giả định.
Câu thay thế đề xuất: thêm mệnh đề: *"...đối tượng khảo sát — Libanius và Gregôriô Nazianzus đã viết tự thuật trước đó, nhưng ở phần Hy Lạp hoá của đế chế và không lấy chính sự bất minh của nội tâm làm đề tài."*

**3. Đúng — các chi tiết còn lại.** Rome bị cướp phá **410** ✓ (Alaric, 24/8/410); *De Civitate Dei* khởi thảo 413 ✓ "viết sau"; tranh luận với Pelagius ✓; "theo Manichaeism chín năm" ✓ — chính Augustinô ghi *per idem tempus annorum novem* (*Conf.* IV.1); Ambrosiô rửa tội cho ông ✓ (Phục sinh 387); Hieronymus dịch Vulgata ✓.

**4. Thể thức — trường `nơi:`.** `nơi: Thagaste, Milano và Hippo Regius, Bắc Phi` đặt **Milano** vào "Bắc Phi". Template §5 yêu cầu `{{địa danh, vùng lãnh thổ ngày nay}}`. Đề xuất: `Thagaste và Hippo Regius, nay là Algeria`.

**5. Liên kết — kiểm bằng cách mở đích.** `CH04-CE03-01` = Plotinus ✓ (mục có thật, đúng chiều: Augustinô đọc Plotinus). `CH04-CE01-02` = Phaolô thành Tarsus ✓. `CH04-CE02-10` = Tertullian — mục có thật, đúng chiều thời gian, nhưng quan hệ yếu: ảnh hưởng Latinh lên Augustinô đi qua Cyprianô và Ambrosiô rõ hơn qua Tertullian, và Augustinô phê Tertullian về thuyết vật thể của linh hồn. Mức `qua trường phái` đã hạ thấp đủ, không đề nghị gỡ, nhưng đây là liên kết yếu nhất trong ba.

**6. Thể thức §5 — ứng viên cùng thời: ĐẠT.** Hieronymus (k. 347–420) và Ambrosiô (k. 339–397) đều thật sự cùng thời với Augustinô (354–430). `grep '^### '` trên 221 mục của atlas: **không ai trong hai người có mục riêng** → không mắc lỗi hệ thống "nêu người đã được chọn".

**7. Nguồn — ĐẠT.** Peter Brown, *Augustine of Hippo: A Biography*, bản mới kèm epilogue, University of California Press, **2000** ✓ — có thật, đúng năm, đúng thể loại (tiểu sử chuyên khảo), đúng chủ đề.

---

## CH04-CE05-02 · Giáo hoàng Lêô I

**1. Đúng — cả ba mốc Owner nghi.** Kiểm riêng từng mốc:
- *Tomus ad Flavianum* gửi **449** ✓ (13/6/449, gửi Flavianus thành Constantinopolis).
- Công đồng **Chalcedon 451** ✓, chấp nhận Tomus làm chuẩn ✓.
- Gặp Attila **452** ✓ (phái đoàn tới trại Attila gần Mantua).
Không có lỗi niên đại ở mục này.

**2. Nghi vấn — "người đầu tiên lập luận có hệ thống rằng giám mục Rome kế thừa quyền của Phêrô theo nghĩa pháp lý"**
Nguyên văn: *"Ông cũng là người đầu tiên lập luận có hệ thống rằng giám mục Rome kế thừa quyền của Phêrô theo nghĩa pháp lý, không chỉ danh dự."*
Chữ "đầu tiên" không đứng được. Damasus I (366–384) đã dùng ngôn ngữ *sedes apostolica*; Siricius (384–399) ban decretal đầu tiên theo khuôn sắc lệnh hoàng đế; **Innocentê I (401–417)** đã viết thẳng rằng mọi vụ lớn phải trình về Rome; Bonifaciô I tiếp tục. Đóng góp riêng của Lêô là khái niệm **Phêrô là *heres* — người kế vị thừa hưởng tư cách pháp lý, "indignus haeres"** — tức là hệ thống hoá và đặt nền pháp lý chặt hơn, không phải khởi đầu.
Câu thay thế đề xuất: *"Ông đưa lập luận ấy tới dạng pháp lý chặt nhất trước đó chưa ai đạt: giám mục Rome là người thừa kế (heres) tư cách của Phêrô, chứ không chỉ giữ ngôi danh dự — Damasus và Innocentê I đã nêu yêu sách, Lêô là người làm nó thành học thuyết."*

**3. Thiếu — "Năm 452 ông đi gặp Attila ở bắc Italia, và quân Hung rút."**
Hai vế đặt cạnh nhau không có từ nối nhân quả, nhưng vị trí trong câu khiến người đọc tự nối. Sử học hiện nay quy việc Attila rút chủ yếu cho **nạn đói và dịch bệnh ở Italia năm 452, cộng với việc Marcianus mở chiến dịch đánh vào chính đất Hung ở bắc sông Donau** — Hydatius chép cả hai yếu tố; vai trò của phái đoàn Lêô là không xác định được. Mục này đang để nguyên truyền thống Công giáo mà không gắn hàng rào, trong khi chính chapter ở mục Giê-su (CE01-01) lại rất cẩn thận phân tầng. Không nhất quán.
Câu thay thế đề xuất: *"Năm 452 ông dẫn một phái đoàn tới gặp Attila ở bắc Italia; quân Hung rút ngay sau đó, tuy các nguồn gần thời quy việc rút cho nạn đói, dịch bệnh và chiến dịch của Marcianus đánh vào đất Hung hơn là cho cuộc gặp."*

**4. Thể thức §5 — ứng viên: ĐẠT, có một hàng rào đúng.** Cyrillô thành Alexandria (k. 376–444) — mục **tự ghi "ở thế hệ trước"**, đúng cách xử lý theo CONTRIBUTING §5; thực ra hai người còn chồng lấn (Lêô làm giáo hoàng từ 440, Cyrillô mất 444). Flavianus (mất 449) cùng thời chính xác ✓. Cả hai **không có mục riêng** trong atlas ✓.

**5. Liên kết.** `CH04-CE02-09` = Irenaeus thành Lyon ✓ — mở mục ra, đúng người, đúng chiều, và Irenaeus thật sự là nguồn sớm cho lập luận về vị thế toà Rome (*Adv. Haer.* III.3). Hợp lệ.

**6. Nguồn — ĐẠT.** Susan Wessel, *Leo the Great and the Spiritual Rebuilding of a Universal Rome*, Brill, Supplements to Vigiliae Christianae 93, **2008** ✓ — có thật, đúng năm, đúng thể loại (chuyên khảo), và luận điểm trung tâm của sách (Lêô thay Rome thế tục bằng Rome Kitô giáo phổ quát) **đúng hướng** với điều mục này dẫn, không bị dùng ngược.

---

## CH04-CE05-03 · Proclus

**1. SAI — "hai trăm mười mệnh đề"** ← lỗi Owner nghi, xác nhận.
Nguyên văn: *"Bộ Yếu lược thần học trình bày toàn bộ siêu hình học Tân Plato theo lối hình học: hai trăm mười mệnh đề, mỗi mệnh đề kèm chứng minh dựa vào các mệnh đề trước."*
Con số đúng là **211**. Chính bản dịch được dẫn trong mục — E. R. Dodds, *Proclus: The Elements of Theology*, 2nd ed. 1963 — đánh số tới mệnh đề 211; cấu trúc chuẩn được mô tả là mệnh đề 1–112 (các cặp đối lập Tân Plato) và 113–211 (henad, trí tuệ, linh hồn). Đây đúng là dạng lỗi CONTRIBUTING §3 cảnh báo: con số được sinh ra chứ không tra.
**Lưu ý nghịch**: bài SEP "Proclus" được chính mục này dẫn lại ghi *"a concatenated demonstration of 217 propositions"*. Hai nguồn vênh nhau, và **không nguồn nào trong hai cho ra 210**. Khuyến nghị: lấy 211 (số mệnh đề trong bản Dodds, tức bản mà mục đang dẫn) và nếu muốn chặt thì ghi "hai trăm mười một mệnh đề theo bản Dodds".
Câu thay thế đề xuất: *"...theo lối hình học: **hai trăm mười một** mệnh đề trong bản Dodds, mỗi mệnh đề kèm chứng minh dựa vào các mệnh đề trước."*

**2. Đúng — Liber de Causis và Aquinas.** Kiểm riêng từng vế của câu *"một tuyển tập Arab rút từ tác phẩm này, dịch sang Latinh thành Liber de Causis, được châu Âu trung cổ đọc như của Aristotle cho tới khi Aquinas phát hiện nguồn thật"*:
- tuyển tập Arab rút từ *Elements of Theology* ✓ — SEP: *Book of Causes* là bản phỏng Arab của *Elements of Theology*, soạn thế kỷ 9.
- bị đọc như của Aristotle ✓ — nó được xếp kèm *Metaphysica* làm sách giáo khoa đại học.
- Aquinas phát hiện nguồn thật ✓ — và chi tiết xác nhận mạnh: ông làm được nhờ bản dịch Latinh *Elements of Theology* do **William xứ Moerbeke** hoàn thành **1268**.
Cả ba vế đứng vững. Đây là phần chắc nhất của mục.

**3. Thiếu — "Đây là nỗ lực sớm nhất biến siêu hình học thành một hệ diễn dịch có cấu trúc như Euclid."**
Chữ "sớm nhất" bỏ qua **Proclus, *Elements of Physics* (Στοιχείωσις φυσική)** — cũng của chính ông, cũng theo lối Euclid, và thường được coi là **tác phẩm sớm hơn** trong sự nghiệp ông. Nếu *Elements of Physics* có trước, thì "nỗ lực sớm nhất" theo lối hình học không phải *Elements of Theology*, chỉ là nỗ lực sớm nhất **trong siêu hình học**. Câu hiện tại đã nói "siêu hình học" nên vẫn cứu được, nhưng chênh vênh; đề nghị siết: *"là nỗ lực sớm nhất còn lại áp lối diễn dịch Euclid vào siêu hình học"*.

**4. Thể thức §5 — ứng viên: ĐẠT.** Syrianus (mất k. 437, thầy Proclus, đứng đầu Academy sau khi Plutarchos mất năm 432 — SEP xác nhận) và Damascius (k. 458–538, người đứng đầu cuối cùng). Cả hai **cùng trường, cùng mạch, kề thời** — Syrianus thật sự chồng thời với Proclus (412–485), Damascius sinh trước khi Proclus mất. **Không ai có mục riêng** trong atlas ✓. Mục còn tự dán nhãn "cùng trường" thay vì "cùng thời", chính xác hơn.
*Lưu ý nhỏ:* mốc "trường bị đóng năm 529" là mốc truyền thống (sắc lệnh Justinianus); giới nghiên cứu hiện chia rẽ về việc sắc lệnh ấy có thật sự đóng cửa trường Athens hay không. SEP bản được dẫn **không bàn tới mốc 529**, nên chi tiết này không có nguồn đỡ trong dòng Nguồn của mục.

**5. Liên kết.** `CH04-CE03-01` = Plotinus ✓. `CH03-BCE04-01` — mở `content/ch03.md` để đọc tên: cần xác nhận là Plato/Aristotle (xem §13).

**6. Nguồn — ĐẠT, URL sống.** Dodds (1963) ✓ có thật, đúng thể loại (bản dịch kèm chú giải — và đây là điểm quan trọng vì bản này chính là nơi tra được số mệnh đề, lẽ ra mục đã tránh được lỗi §1 nếu mở ra). SEP "Proclus" → **HTTP 200**, bài có thật, đúng về nhân vật ✓.

---
## CH04-CE05-04 · Attila

**1. SAI — đảo ngược trình tự nhân quả của làn sóng di cư German.**
Nguyên văn: *"áp lực của liên minh ấy đẩy hàng loạt dân German vào trong biên giới La Mã, và chính dòng di cư đó chứ không phải trận đánh nào là cái làm nửa tây đế chế tan rã."*
Attila trị vì **434–453**. Các đợt vượt biên lớn của người German đều **đã xảy ra trước đó**: người Goth vượt sông Danube **376**, vượt sông Rhine hàng loạt **406/407** (Vandal, Alan, Sueve), người Vandal sang Bắc Phi **429** và chiếm Carthage **439**. Áp lực Hung có thật, nhưng đó là áp lực từ **đợt người Hung tới thảo nguyên Pontus từ những năm 370**, dưới các thủ lĩnh trước Attila — không phải từ liên minh của Attila. Mục đang gán cho cá nhân Attila một chuỗi nhân quả diễn ra một tới hai thế hệ trước khi ông cầm quyền.
Câu thay thế đề xuất: *"...không chiếm được đất. Áp lực của người Hung trên thảo nguyên — bắt đầu từ những năm 370, tức trước Attila hai thế hệ — là cái đẩy hàng loạt dân German vào trong biên giới La Mã; đóng góp riêng của Attila là biến sức ép rời rạc ấy thành một quyền lực tập trung rút được vàng của Constantinopolis một cách đều đặn."*

**2. SAI (lỗi lập luận) — counterfactual tự phản.** ← mục Owner yêu cầu đánh giá.
Nguyên văn: *"chính cấu trúc liên minh ấy phụ thuộc vào cá nhân ông tới mức tan ngay khi ông chết — một ca hiếm mà counterfactual kiểm chứng được bằng chính sự sụp đổ."*
Lập luận này **chứng minh ngược lại điều nó muốn chứng minh**. Tiêu chí (d) hỏi: *không có người này thì thay đổi có đến muộn hơn đáng kể không?* Việc liên minh tan ngay ở Nedao (454) chỉ chứng minh **liên minh phụ thuộc vào ông**, chứ không chứng minh **hệ quả lịch sử** phụ thuộc vào ông. Thực tế ngược lại: nếu cấu trúc ấy bốc hơi trong vòng một năm mà Tây La Mã vẫn sụp (455 Vandal cướp Rome, 476 phế Romulus Augustulus) theo đúng quỹ đạo cũ, thì đó là **bằng chứng rằng dấu vết lâu dài của Attila nhỏ**, không phải lớn. Đây là lỗi đánh tráo: lấy "ảnh hưởng của ông lên tổ chức của chính ông" thay cho "ảnh hưởng của ông lên lịch sử".
Câu thay thế đề xuất: *"Attila được chọn theo phạm vi (a) chứ không theo counterfactual (d): trong hai thập niên ông là trung tâm chính trị duy nhất mà cả hai nửa đế chế phải thương lượng, và việc liên minh tan ngay ở Nedao năm 454 cho thấy chính cấu trúc ấy là của riêng ông — nhưng cũng vì thế counterfactual (d) ở đây **yếu**: Tây La Mã vẫn đi tiếp đúng quỹ đạo cũ sau khi ông chết."*

**3. Nghi vấn — nguồn bị dùng lệch hướng.** Christopher Kelly, *The End of Empire: Attila the Hun and the Fall of Rome* (W. W. Norton, **2009**) — sách **có thật, đúng năm, đúng thể loại** ✓. Nhưng luận điểm của Kelly là Attila làm **kiệt quệ tài nguyên La Mã bằng chiến tranh kéo dài**, và ông viết lại Attila thành nhà chiến lược chính trị dựa vào liên minh hơn là kẻ chinh phạt. Mục này lại dùng Kelly để đỡ cho câu *"chính dòng di cư đó chứ không phải trận đánh nào"* — tức đúng mệnh đề Kelly **không** chủ trương. Đây đúng loại lỗi CONTRIBUTING §7 mô tả (ca Hansen).

**4. Đúng.** Cống phẩm bằng vàng từ Constantinopolis ✓ (hoà ước Margus 435 và nhất là 447, nâng mức cống hằng năm lên nhiều lần); chiến dịch Gallia **451** ✓ (Campus Mauriacus) và Italia **452** ✓, không giữ được đất ✓; liên minh sụp sau khi ông chết **453** ✓ (Nedao 454). Priscus chỉ còn qua mảnh, phần lớn truyền qua Jordanes ✓.

**5. Thể thức §5 — ứng viên: ĐẠT.** Aetius (k. 391–454) và Geiseric (k. 389–477) đều **thật sự cùng thời** với Attila (k. 406–453) ✓. Cả hai **không có mục riêng** trong atlas ✓, và cả hai cũng nằm trong danh sách bị loại ở Ghi chú biên tập — nhất quán.

**6. Thể thức — liên kết "Rugila · kế thừa · trực tiếp" không nhất quán với chính chapter.**
Rugila (Rua) là chú và người tiền nhiệm của Attila ✓, quan hệ có thật. Nhưng khối Ghi chú biên tập của chính chapter này đã gỡ liên kết Hán Quang Vũ Đế "phản bác" Hai Bà Trưng với lý do *"đàn áp quân sự không phải quan hệ tư tưởng"*. Theo đúng tiêu chuẩn đó, "kế thừa ngôi thủ lĩnh bộ lạc" cũng không phải quan hệ tư tưởng. Hoặc nới tiêu chuẩn, hoặc gỡ dòng này — hiện tại hai chỗ đang áp hai tiêu chuẩn khác nhau trong cùng một chapter.

---

## CH04-CE05-05 · Theodosius II

**1. SAI — "giữ được thành phố gần một nghìn năm"** (lệch sai hướng).
Nguyên văn: *"Tường thành Constantinopolis dựng dưới triều ông giữ được thành phố gần một nghìn năm."*
Tường thành đất liền dựng **413** (dưới quyền quan trấn thủ Anthemius), được gia cố và thêm tường ngoài **447** sau động đất. Thành thất thủ trước quân Ottoman **1453**. 1453 − 413 = **1040 năm** — tức **hơn** một nghìn năm, không phải "gần". Con số đang bị hạ thấp chứ không nâng, nên không phải lỗi phóng đại, nhưng vẫn là con số sai.
Câu thay thế đề xuất: *"Tường thành Constantinopolis dựng năm 413 dưới triều ông giữ được thành phố **hơn một nghìn năm**, tới khi Ottoman phá vỡ năm 1453."*
*(Lưu ý: nếu muốn chặt hơn nữa thì nên thêm "tường thành đất liền chưa từng bị chọc thủng" — thành đã bị Thập tự quân thứ tư chiếm năm 1204, nhưng từ phía biển.)*

**2. ĐỨNG ĐƯỢC nhưng THIẾU — "lần đầu luật đế chế được pháp điển hoá chính thức".** ← mục Owner yêu cầu tìm phản ví dụ.
Đã tìm. Hai phản ví dụ ứng viên là **Codex Gregorianus** (k. 291) và **Codex Hermogenianus** (k. 295). Kết quả kiểm: cả hai là **sưu tập tư nhân** do luật gia soạn, **không** do hoàng đế ban hành — chúng chỉ được nâng lên hiệu lực pháp lý **năm 439**, cùng lúc Codex Theodosianus có hiệu lực. Vậy chữ **"chính thức"** trong câu của mục **cứu được mệnh đề**: Codex Theodosianus đúng là bộ pháp điển **chính thức** đầu tiên của luật đế chế.
Nhưng mục **không nêu hai bộ kia**, nên người đọc không có cách nào biết chữ "chính thức" đang gánh toàn bộ sức nặng của câu. Đề nghị ghi ra.
Câu thay thế đề xuất: *"...loại bỏ phần mâu thuẫn — bộ pháp điển **chính thức** đầu tiên của luật đế chế: hai bộ trước đó, Codex Gregorianus (k. 291) và Codex Hermogenianus (k. 295), là sưu tập tư nhân của luật gia và chỉ được nâng lên hiệu lực pháp lý cùng năm 439 với chính bộ này."*

**3. SAI — liên kết `CH03-BCE01-03` trỏ đúng ID nhưng sai người.** ← đúng loại lỗi CONTRIBUTING §8 cảnh báo.
Mở đích ra đọc tên: `content/ch03.md` dòng 643 → **`CH03-BCE01-03 · Cicero (Marcus Tullius Cicero)`**.
Theodosius II "kế thừa · qua trường phái" từ **Cicero** là sai đích. Cicero là nhà hùng biện và triết gia chính trị, không phải mạch mà Codex Theodosianus nối vào. Mạch thật là **luật học cổ điển La Mã** — Papinianus, Ulpianus, Paulus, Gaius, Modestinus — tức chính năm luật gia mà **Luật Trích dẫn (Lex citationum) năm 426 do chính Theodosius II ban** chỉ định làm thẩm quyền. Atlas hiện **không có mục nào** cho các luật gia đó, nên không có ID để trỏ.
Đề nghị: **gỡ dòng `CH03-BCE01-03`**, thay bằng dòng văn bản `- Luật học cổ điển La Mã (Papinianus, Ulpianus, Paulus) · kế thừa · qua trường phái`. Liên kết còn lại `CH04-CE04-01` = **Constantinus I** ✓ đúng — pháp điển thu sắc lệnh từ thời Constantinus trở đi, chiều và niên đại đều chuẩn.

**4. Đúng.** Codex Theodosianus ban hành **438** ✓ (hiến chế 15/2/438; có hiệu lực 1/1/439 ở cả hai nửa — nếu muốn chặt có thể nêu cả hai mốc). Thu sắc lệnh **từ thời Constantinus trở đi** ✓ (312–438). Khuôn mẫu cho bộ Justinianus ✓ (Codex Justinianus 529, tức 91 năm — "một thế kỷ sau" chấp nhận được). Là nguồn chính cho hành chính, thuế khoá, chính sách tôn giáo La Mã hậu kỳ ✓.

**5. Thể thức §5 — ứng viên: ĐẠT.** Pulcheria (399–453) ✓ cùng thời, và mô tả "chị ông và là người nắm phần lớn quyền điều hành" ✓ đúng. Anthemius (quan trấn thủ 405–414) ✓ cùng thời, đúng là người chủ trì xây tường thành 413. **Không ai có mục riêng** ✓.
*Nhận xét về lập luận:* mục thừa nhận Pulcheria "nắm phần lớn quyền điều hành" rồi vẫn chọn Theodosius II — đây là **cùng dạng vấn đề với mục -12** (xem dưới), nhưng ở đây **không tự mâu thuẫn**, vì đóng góp được viện dẫn (pháp điển mang tên ông, do uỷ ban ông lập năm 429) là thứ gắn với ngôi vị hoàng đế chứ không với người nhiếp chính.

**6. Nguồn — ĐẠT.** Clyde Pharr, *The Theodosian Code and Novels and the Sirmondian Constitutions*, Princeton, **1952** ✓ có thật, đúng năm, đúng thể loại (bản dịch kèm chú). Fergus Millar, *A Greek Roman Empire: Power and Belief under Theodosius II (408–450)*, University of California Press, **2006** ✓ — có thật, đúng năm, đúng thể loại, và **đúng chính xác nhân vật và triều đại** của mục. Nguồn tốt nhất của cả nhóm CE05.

---

## CH04-CE05-06 · Hypatia

**1. Nghi vấn — "Các nguồn gần thời nhất quy việc đó cho xung đột chính trị giữa tổng trấn Orestes và giám mục Cyrillô."** ← mục Owner yêu cầu kiểm Socrates q. VII.
Đã mở. **Socrates Scholasticus, *Historia Ecclesiastica* VII.15** (soạn k. 439) nói ba điều, và chỉ ba điều:
- bà bị giết vì **"sự ghen ghét chính trị đang thịnh hành lúc đó"** (political jealousy), do bà hay gặp Orestes và có tin đồn rằng chính bà ngăn việc hoà giải giữa Orestes và Cyrillô;
- ông **không nêu đích danh ai ra lệnh**, và **không quy trách nhiệm cho Cyrillô**;
- ông **không hề nhắc** tới việc bà theo ngoại giáo như một nguyên nhân.
So với câu trong mục, có hai chỗ lệch:
(a) **"các nguồn gần thời nhất"** ở số nhiều là sai. Socrates gần như là nguồn gần thời **duy nhất**. Hai nguồn còn lại đi theo hai hướng **khác hẳn**: Damascius (TK 6) quy thẳng cho lòng ghen của Cyrillô, còn Gioan xứ Nikiu (TK 7) kể như việc trừ một mụ phù thuỷ, tức khung **tôn giáo** chứ không phải chính trị. Nói "các nguồn gần thời nhất" quy cho xung đột chính trị là dựng ra một sự đồng thuận không có.
(b) Chữ **"xung đột giữa Orestes và Cyrillô"** hợp với Socrates, nhưng Socrates lại **không** nói đám đông hành động theo lệnh Cyrillô — mục để ngỏ đúng chỗ này, nên không sai, chỉ cần không gộp vào số nhiều.
Câu thay thế đề xuất: *"Nguồn gần thời nhất — Socrates Scholasticus, viết khoảng hai mươi năm sau — quy việc đó cho 'sự ghen ghét chính trị' quanh xung đột giữa tổng trấn Orestes và giám mục Cyrillô, và không nêu đích danh ai ra lệnh; các nguồn muộn hơn thì chia hai hướng, Damascius quy thẳng cho Cyrillô còn Gioan xứ Nikiu kể lại như việc trừ phù thuỷ."*

**2. Nghi vấn — ba tác phẩm hiệu đính không cùng một mức bằng chứng.** ← mục Owner yêu cầu kiểm.
Nguyên văn: *"Công việc chính được ghi lại là hiệu đính và chú giải: Almagest của Ptolemy, Conics của Apollonius và Arithmetica của Diophantus."*
Ba mục này có ba mức bằng chứng **rất khác nhau**, và mục đang trình bày chúng như nhau:
- **Almagest quyển III** — chắc nhất. Có lập luận văn bản học (quy ước tiêu đề) cho thấy bà hiệu đính chính văn bản quyển III ✓.
- **Arithmetica** — **suy đoán có cơ sở nhưng đang tranh cãi**. Bản chú giải đã mất; giả thuyết là các phần thêm trong bản chép tay Arab bắt nguồn từ công việc của bà — chưa có đồng thuận.
- **Conics** — **yếu nhất**. Bản chú giải **không còn**, và quy thuộc dựa vào Suda (TK 10), tức muộn hơn bà sáu thế kỷ.
Đồng thời, chữ **"nguồn đương thời"** ở phần Vì sao chọn (*"công việc cụ thể được ghi lại bằng nguồn đương thời"*) không đứng được cho ba tác phẩm này: danh mục tác phẩm của bà đến từ **Suda**, TK 10. Nguồn đương thời thật sự (thư Synesius) chứng thực bà **dạy học**, không chứng thực danh mục trước tác.
Câu thay thế đề xuất: *"Công việc chính được ghi lại là hiệu đính và chú giải, nhưng ba tác phẩm ở ba mức bằng chứng khác nhau: việc bà hiệu đính quyển III của Almagest được văn bản học xác nhận; phần chú giải Arithmetica của Diophantus chỉ còn là suy đoán từ các bản chép tay Arab; còn chú giải Conics của Apollonius thì mất hẳn và chỉ được Suda, soạn sáu thế kỷ sau, nhắc tới."*

**3. Đúng.** Học trò gồm cả người Kitô giáo lẫn người ngoại ✓ (thư Synesius, và Socrates VII.15). Bà bị đám đông giết năm **415** ✓ (tháng 3, mùa Chay). Nhận định *"hình tượng về bà ở thế kỷ 18–19 phần lớn là kiến tạo phục vụ tranh luận khác"* ✓ **đúng và được chính nguồn được dẫn đỡ**: đó là luận điểm trung tâm của Watts — nguồn dùng **đúng chiều**, không bị dùng ngược.

**4. Thể thức §5 — ứng viên: ĐẠT.** Theon (hoạt động k. 364–385, mất k. 405) và Synesius thành Cyrene (k. 373–414) đều **thật sự cùng thời** với Hypatia (k. 360–415) ✓. **Không ai có mục riêng** ✓ (Theon cũng nằm trong danh sách bị loại ở Ghi chú biên tập — nhất quán).

**5. Nguồn — ĐẠT, kể cả số quyển.** Socrates Scholasticus, *Historia Ecclesiastica*, **quyển VII** ✓ — đã mở kiểm: đoạn về Hypatia đúng là ở VII.15. Đây là một trong số ít chỗ trong atlas ghi số quyển **và tra đúng** (xem CONTRIBUTING §3). Edward J. Watts, *Hypatia: The Life and Legend of an Ancient Philosopher*, Oxford University Press, **2017** ✓ có thật, đúng năm, đúng thể loại, đúng chủ đề.

---

## CH04-CE05-07 · Cưu-ma-la-thập

**1. Đúng — các mốc Owner nghi.** Về Trường An **401** ✓; mất **413** ✓ (thọ 68–69). Bị giữ ở Lương Châu: bị Lã Quang bắt khi chiếm Khâu Tư khoảng **384**, tới Trường An **401** → **17 năm**. Mục ghi "mười sáu năm" — nằm trong khoảng các con số lưu hành (16 hoặc 17 tuỳ cách tính mốc bắt), nhưng **384–401 cho ra 17**; nếu giữ "mười sáu" thì nên đổi thành "gần hai mươi năm" hoặc ghi thẳng mốc 384–401. Xếp **Nghi vấn nhẹ**, không phải Sai.

**2. Không kiểm được — "ban dịch ... với hàng trăm người".**
Các con số truyền thống rất phân tán: Cao tăng truyện và các ghi chép của Tăng Duệ nêu từ 500, 800 tới 2000–3000 tăng sĩ dự hội dịch Pháp hoa. "Hàng trăm người" nằm trong khoảng đó và là cách diễn đạt **thận trọng đúng mức** — nhưng không có cách xác minh độc lập con số nào là thật, nên: **không kiểm được**. Không đề nghị sửa.

**3. Không kiểm được — "vẫn là bản tụng niệm chuẩn ở ... Việt Nam".** ← mục Owner yêu cầu kiểm.
Phần Trung Hoa, Nhật Bản, Triều Tiên có cơ sở: các bản Pháp hoa, Kim cương, Duy-ma-cật của ông được dùng phổ biến hơn bản Huyền Trang sát nguyên văn hơn ✓. Phần **Việt Nam** thì **không kiểm được bằng nguồn học thuật**: thực tế nghi lễ Việt Nam hiện nay phần lớn tụng **bản dịch tiếng Việt** (hoặc âm Hán–Việt), mà các bản ấy lại dịch **từ** bản chữ Hán của ông — nên mệnh đề có thể đúng theo nghĩa "văn bản nền", nhưng chữ "bản tụng niệm chuẩn" thì mơ hồ. Đề nghị siết lại:
Câu thay thế đề xuất: *"...tới nay vẫn là bản chữ Hán nền cho kinh tụng ở Trung Hoa, Nhật Bản, Triều Tiên và Việt Nam — ở Việt Nam qua âm Hán–Việt và các bản dịch quốc ngữ làm từ chính bản của ông."*

**4. Đúng.** Bỏ lối **cách nghĩa (格義 géyì)** mượn từ ngữ Đạo gia ✓ — việc này thường được quy cho vòng Cưu-ma-la-thập và học trò (Tăng Duệ), tuy **Đạo An đã phê géyì trước đó**, và chính mục đã nêu Đạo An ở phần Vì sao chọn, nên không mâu thuẫn. Danh mục dịch phẩm (Pháp hoa, Kim cương, Duy-ma-cật, Trung luận) ✓ đúng.

**5. Thể thức §5 — một ứng viên cùng thời, một không, và cái không ĐÃ ĐƯỢC NÓI RA.** Đạo An (312–385) — mất 385, tức **không cùng thời với giai đoạn hoạt động** của Cưu-ma-la-thập ở Trường An, nhưng mục mô tả đúng là "người tổ chức việc dịch thuật **trước ông**" ✓ nên không giấu. Huyền Trang — mục ghi rõ "ở thế kỷ 7" ✓ nên cũng không giấu. **Không ai có mục riêng** ✓ (Đạo An nằm trong danh sách bị loại — nhất quán). Không mắc hai lỗi hệ thống, nhưng cũng **không có ứng viên cùng thời thật sự nào** được nêu; theo CONTRIBUTING §5, chỗ này lẽ ra nên nói thẳng là giai đoạn ấy không có đối thủ dịch thuật cùng tầm.

**6. Liên kết.** `CH04-CE02-08` = Nāgārjuna ✓ (ông dịch Trung luận — "trực tiếp" đúng). `CH04-CE04-11` = Vasubandhu ✓. `CH04-CE03-10` = **Vương Bật** — mở ra đọc tên, đúng người; quan hệ "phản bác · qua trường phái" hiểu được (bác lối géyì mượn từ vựng huyền học mà Vương Bật là đại biểu), nhưng đây là **suy luận của người soạn**, không phải quan hệ được ghi trong nguồn; mức `qua trường phái` đã hạ đủ, giữ được.
`CH90-CE01_09-04` — mở `content/ch90.md` dòng 89 → **Tì-ni-đa-lưu-chi (Vinītaruci)** ✓ mục có thật, đúng chiều thời gian (Vinītaruci tới Việt Nam 580). Nhưng quan hệ **yếu**: Vinītaruci là tăng Ấn Độ, học trò Tăng Xán trong mạch Thiền, không phải người thừa kế trực tiếp mạch dịch thuật của Cưu-ma-la-thập. Mức `qua trường phái` cứu được, nhưng đây là liên kết yếu nhất của mục.

**7. Nguồn — ĐẠT.** *Cao tăng truyện*, Cưu-ma-la-thập truyện ✓ có thật (Huệ Hạo, TK 6, quyển 2). Erik Zürcher, *The Buddhist Conquest of China*, Brill, **1959** ✓ có thật, đúng năm, đúng thể loại (chuyên khảo), đúng chủ đề.

---

## CH04-CE05-08 · Buddhaghosa

**1. SAI — tên sách trong dòng Nguồn.**
Nguyên văn: *"Kate Crosby, Theravada Buddhism: A New History (2013)."*
Sách của Kate Crosby năm 2013 (Wiley-Blackwell, bộ *Wiley-Blackwell Guides to Buddhism*) có nhan đề **_Theravada Buddhism: Continuity, Diversity, and Identity_**. **Không tồn tại** cuốn nào tên *"Theravada Buddhism: A New History"* của Crosby. Tác giả đúng, năm đúng, nhà xuất bản đúng — **phụ đề bị sinh ra**. Đây là dạng lỗi CONTRIBUTING mục "Phản hồi mà không cần viết code" gọi là hữu ích nhất để báo.
Câu thay thế đề xuất: *"Kate Crosby, Theravada Buddhism: Continuity, Diversity, and Identity (2013)."*

**2. Nghi vấn — "sách chuẩn ... ở Sri Lanka, Miến Điện, Thái Lan, Lào và Campuchia suốt mười lăm thế kỷ".**
"Mười lăm thế kỷ" đúng với **Sri Lanka** (TK 5 → nay). Không đúng với ba nước còn lại: Theravāda chỉ thành dòng chủ lưu ở **Miến Điện từ TK 11** (Anawrahta), và ở **Thái Lan, Lào, Campuchia từ khoảng TK 13–14**. Câu hiện tại gán mười lăm thế kỷ cho cả năm nước.
Câu thay thế đề xuất: *"...là sách chuẩn của Theravāda ở Sri Lanka suốt mười lăm thế kỷ, và ở Miến Điện, Thái Lan, Lào, Campuchia từ khi Theravāda thành dòng chủ lưu tại đó, tức từ khoảng thế kỷ 11 tới 14."*

**3. Đúng.** *Visuddhimagga* dựng theo ba phần **giới – định – tuệ** ✓. Việc ông dịch tầng chú giải tiếng Sinhala sang Pali ✓, và các bản Sinhala về sau mất hết ✓ — lập luận "nếu không có việc dịch ấy thì tầng chú giải cổ cũng mất theo" đứng vững. Câu *"Tiểu sử của ông gần như toàn truyền thuyết muộn"* ✓ **đúng và là một hàng rào tốt** (phần lớn đến từ *Mahāvaṃsa* và *Buddhaghosuppatti* muộn) — đúng tinh thần prompt §Kiểm soát chất lượng.

**4. Thể thức §5 — ứng viên: ĐẠT.** Buddhadatta ✓ **thật sự cùng thời** ở Sri Lanka/Nam Ấn (TK 5). Dhammapāla — mục ghi rõ "ở thế kỷ sau" ✓ không giấu. **Không ai có mục riêng** ✓ (Dhammapāla nằm trong danh sách bị loại — nhất quán).

**5. Liên kết.** `CH03-BCE03-01` = **Ashoka** ✓ mở ra đọc tên, đúng người, chiều đúng (phái đoàn Mahinda đưa Theravāda sang Sri Lanka). `CH02-BCE06-03` = **Đức Phật** ✓.

**6. Trường `năm:` và độ tin cậy — ĐẠT.** `hoạt động k. 410–450` với `độ tin cậy niên đại: Thấp` là cách xử lý **đúng** theo bảng quy ước CONTRIBUTING: lint bỏ qua đối chiếu, và Wikidata (401/500) thật sự chỉ là khoảng ước.

---

## CH04-CE05-09 · Āryabhaṭa

**1. SAI — "bảng sin đầu tiên của lịch sử".** ← mục Owner yêu cầu tìm phản ví dụ. Tìm được **hai**, một trong đó nằm ngay trong chính atlas.
Nguyên văn: *"Ông lập bảng sin đầu tiên của lịch sử..."*
- **Phản ví dụ 1 (quyết định): *Sūrya Siddhānta*.** Đây là văn bản **sớm nhất được biết có chứa bảng sin**, và nó **có trước** Āryabhaṭīya (soạn k. TK 4, bản còn lại muộn hơn). Bảng sin của Āryabhaṭa cho **đúng các giá trị** như trong *Sūrya Siddhānta* — tức ông đứng trong một truyền thống đã có bảng, không khởi đầu nó.
- **Phản ví dụ 2 (nội bộ atlas): `CH03-BCE02-03 · Hipparchus xứ Nicaea`.** Mở mục ra đọc: *"Ông lập danh mục sao có ghi độ sáng, và **dựng bảng dây cung, tiền thân của bảng lượng giác**."* Bảng dây cung không đồng nhất với bảng sin, nhưng khi chính atlas đã gọi nó là "tiền thân của bảng lượng giác" thì câu "bảng sin đầu tiên của lịch sử" ở mục này **tự mâu thuẫn với mục kia** trong cùng bộ sách.
Thêm nữa, **nguồn được chính mục dẫn** — Kim Plofker, *Mathematics in India* (2009) — là nơi bàn kỹ bảng sin *Sūrya Siddhānta*, tức nguồn **nói ngược** với câu được đỡ (lỗi CONTRIBUTING §7).
Đóng góp thật và riêng của Āryabhaṭa là **bảng hiệu sin (sine differences) nén vào một câu kệ duy nhất bằng hệ ký số chữ cái của ông** — đó mới là cái không có tiền lệ.
Câu thay thế đề xuất: *"Ông nén cả bảng hiệu sin vào một câu kệ duy nhất bằng hệ ký số chữ cái tự đặt — bảng sin thì truyền thống Siddhānta trước ông, trong Sūrya Siddhānta, đã có, nhưng cách mã hoá và độ gọn là của riêng ông."*
Và ở phần Vì sao chọn, câu *"bảng sin và lập trường Trái Đất tự quay đều không có tiền lệ ở Nam Á"* phải sửa theo: **bảng sin thì có tiền lệ**; lập trường Trái Đất tự quay thì đúng là không.

**2. Đúng — các con số Owner nghi.** Āryabhaṭīya soạn xong **499** ✓ và ông **23 tuổi** khi đó ✓ (chính văn bản ghi: năm 3600 Kali Yuga, ông 23 tuổi); **121 câu kệ** ✓. Ba con số này **đều tra được và đều đúng** — hiếm trong nhóm này.

**3. Đúng.** Giá trị pi **3,1416** ✓ (62832/20000) và chữ **āsanna** ("tiệm cận / gần đúng") trong Gaṇitapāda 10 ✓ — nhận định "nói thẳng đó chỉ là gần đúng" có nguồn thật. Giải thích nhật/nguyệt thực bằng bóng che ✓. Trái Đất tự quay ✓. `nơi: Kusumapura, nay là vùng Patna` ✓.

**4. Thể thức §5 — KHÔNG có ứng viên cùng thời nào, và không nói ra là không có.**
Nguyên văn: *"Ứng viên là Varāhamihira ở thế hệ sau, người tổng hợp năm hệ thiên văn, và Brahmagupta ở thế kỷ 7."*
Varāhamihira (505–587) và Brahmagupta (598–668) **đều sinh sau khi Āryabhaṭīya hoàn thành**, Brahmagupta sinh sau khi Āryabhaṭa mất ~48 năm. Mục **có dán nhãn** "ở thế hệ sau" và "ở thế kỷ 7" nên **không mắc lỗi hệ thống giấu giếm** — nhưng kết quả là mục **nêu số 0 ứng viên cùng thời**, trong khi §5 yêu cầu "1–2 người cùng lĩnh vực, **cùng thời**". CONTRIBUTING §5 chỉ rõ cách xử lý: *"Nếu giai đoạn đó thật sự không có ai để so, viết thẳng là không có."* Mục chưa làm bước đó.
Câu thay thế đề xuất: thêm một mệnh đề mở đầu: *"Nam Á thế kỷ 5 không để lại nhà thiên văn nào cùng tầm mà xác định được niên đại, nên hai ứng viên gần nhất đều ở sau ông: Varāhamihira (505–587) và Brahmagupta (598–668)."*
Cả hai **không có mục riêng** trong atlas ✓, và cả hai cũng nằm trong danh sách bị loại ở Ghi chú biên tập — nhất quán.

**5. Nghi vấn nhẹ — đường truyền sang Arab.** *"bảng sin của ông qua các bản dịch Arab là nguồn của lượng giác Hồi giáo rồi châu Âu"* — đường truyền chính được ghi nhận là qua **Brāhmasphuṭasiddhānta của Brahmagupta → *Zīj al-Sindhind* (al-Fazārī, k. 770)**, không phải trực tiếp từ Āryabhaṭīya (tuy có tồn tại bản Arab *Zīj al-Arjabhar*). Câu không sai hẳn nhưng rút ngắn một mắt xích; mắt xích ấy lại chính là Brahmagupta — người mục vừa gạt ra ở phần trên. Nên nói ra.

**6. Nguồn — ĐẠT về thư mục, nhưng xem §1 về cách dùng.** K. S. Shukla và K. V. Sarma, *Āryabhaṭīya of Āryabhaṭa*, Indian National Science Academy, **1976** ✓ có thật, đúng năm, đúng thể loại (bản dịch kèm chú giải). Kim Plofker, *Mathematics in India*, Princeton University Press, **2009** ✓ có thật, đúng năm, đúng thể loại — nhưng bị dùng để đỡ cho mệnh đề nó phản bác (§1).

---
## CH04-CE05-10 · Phạm Diệp

**1. SAI — "nguồn chữ Hán sớm nhất còn lại về ... Giao Chỉ".**
Nguyên văn: *"Các thiên về Tây Vực và Nam Man cũng là nguồn chữ Hán sớm nhất còn lại về nhiều vùng, trong đó có Giao Chỉ."*
Không đúng với Giao Chỉ. **Hán thư** của Ban Cố (hoàn thành k. 111 CN, tức ba thế kỷ trước Phạm Diệp) đã có quận Giao Chỉ trong **Địa lý chí**, kèm số hộ khẩu — và *Sử ký* của Tư Mã Thiên đã chép Nam Việt trước đó nữa. Lỗi này **tự mâu thuẫn ngay trong chapter**: `CH04-CE01-11` là **Ban Cố**, và chính mục Phạm Diệp lại liên kết "kế thừa từ `CH04-CE01-11`".
Điều **đúng** và đáng giữ: Hậu Hán thư là nguồn **sớm nhất còn lại chép tường thuật về khởi nghĩa Hai Bà Trưng**, không phải nguồn sớm nhất về Giao Chỉ nói chung.
Câu thay thế đề xuất: *"Các thiên về Tây Vực và Nam Man là nguồn chữ Hán còn lại sớm nhất **chép tường thuật** về nhiều vùng — trong đó có đoạn về khởi nghĩa Hai Bà Trưng ở Giao Chỉ, dù Hán thư của Ban Cố đã ghi quận này từ ba thế kỷ trước."*

**2. Đúng.** Soạn Hậu Hán thư bằng cách chọn lọc từ **hơn mười** bộ Đông Hán sử đã có, và chính bản của ông sống sót ✓. Thêm thiên **Liệt nữ truyện** vào **chính sử** ✓ — phát biểu này **chính xác về mặt thể loại**: *Liệt nữ truyện* của Lưu Hướng (TK 1 TCN) có trước nhưng là sách rời, Hậu Hán thư mới là bộ chính sử đầu tiên có thiên ấy. Bị xử tử **445** vì dính mưu phản ✓ (vụ Lưu Nghĩa Khang). Các thiên 西域傳 và 南蠻西南夷列傳 có thật ✓.

**3. Thể thức §5 — KHÔNG có ứng viên cùng thời nào; cả hai đều cách ông một thế kỷ trở lên, nhưng ĐÃ được nói ra.**
Trần Thọ (233–297) — mục ghi "ở thế kỷ trước"; thực tế ông **mất 101 năm trước khi Phạm Diệp sinh (398)**. Tư Mã Bưu (k. 240–306) — mục mô tả là "một trong các tác giả Đông Hán sử mà ông dựa vào", tức hiển nhiên trước. Vậy mục **không giấu**, nhưng nêu **số 0 ứng viên cùng thời**, giống hệt -09. Trong khi đó thế kỷ 5 Trung Hoa **có** sử gia cùng thời để so — ví dụ **Bùi Tùng Chi (372–451)**, người chú Tam Quốc chí, đúng cùng thời với Phạm Diệp và làm quan cùng triều Lưu Tống. Đó mới là ứng viên §5 yêu cầu.
Câu thay thế đề xuất: *"Ứng viên **cùng thời** là Bùi Tùng Chi (372–451), người làm phần chú cho Tam Quốc chí ngay tại triều Lưu Tống; ứng viên xa hơn là Trần Thọ ở thế kỷ 3, tác giả chính văn bộ ấy."*
Trần Thọ và Tư Mã Bưu **không có mục riêng** trong atlas ✓ (Trần Thọ nằm trong danh sách bị loại — nhất quán).

**4. Liên kết — ĐẠT, đã mở đích đọc tên.** `CH04-CE01-11` → **Ban Cố** ✓ đúng người, đúng chiều (Hậu Hán thư nối tiếp thể kỷ truyện của Hán thư). `CH03-BCE01-06` → `content/ch03.md` dòng 694 = **Tư Mã Thiên** ✓ đúng người, đúng chiều.

**5. Nguồn — ĐẠT.** *Hậu Hán thư* ✓. Rafe de Crespigny, *Fire over Luoyang: A History of the Later Han Dynasty 23–220 AD*, Brill (Sinica Leidensia 134), **2016** ✓ có thật, đúng năm, đúng thể loại (chuyên khảo sử), đúng chủ đề.

---

## CH04-CE05-11 · Tổ Xung Chi

**1. Đúng — cả ba con số Owner nghi.** Kiểm riêng từng con số:
- Chặn pi giữa **3,1415926** và **3,1415927**, tức **đúng tới bảy chữ số thập phân** ✓.
- **Mật suất 355/113** ✓ (密率) — và mô tả "xấp xỉ tốt nhất với mẫu số nhỏ" đúng (nó là xấp xỉ tốt nhất với mọi mẫu số dưới 16604).
- Giữ kỷ lục **"khoảng chín trăm năm"** ✓ — bị al-Kāshī vượt năm **1424** (16 chữ số); 1424 − k. 480 ≈ **944 năm**. "Khoảng chín trăm năm" là cách nói chuẩn trong văn liệu.
**Không có lỗi số học nào trong mục này.** Đây là mục chính xác nhất của nhóm CE05.

**2. Đúng.** Cùng con trai (**Tổ Cắng**) giải thể tích hình cầu ✓, đúng là bài Lưu Huy thừa nhận bỏ dở ✓, bằng nguyên lý thiết diện (nguyên lý Tổ Cắng) ✓. "Cavalieri phát biểu lại ở châu Âu mười một thế kỷ sau" ✓ — Tổ Cắng k. 500, Cavalieri **1635**, tức ~1135 năm ≈ mười một thế kỷ.

**3. Thể thức §5 — vi phạm một nửa lỗi hệ thống số 6, có giảm nhẹ.**
Nguyên văn: *"Ứng viên là Lưu Huy, **chọn ở nhóm trước** và là người đặt phương pháp ông dùng, và Hà Thừa Thiên, nhà lịch pháp cùng thời."*
Lưu Huy **có mục riêng: `CH04-CE03-09`** — và mục chính của Tổ Xung Chi còn liên kết "kế thừa từ `CH04-CE03-09`". CONTRIBUTING §6 cấm nêu người đã được chọn ở chỗ khác làm "ứng viên bị loại", và yêu cầu nói rõ *"có mục riêng ở nhóm X nên không phải ứng viên bị loại"*. Mục **có** nói "chọn ở nhóm trước" → đã công khai, nên **không phải lỗi giấu giếm**; nhưng vẫn gọi ông là **"Ứng viên"**, tức vẫn giữ cái khung "đánh đổi" trong khi không có đánh đổi nào xảy ra. Nên sửa cho khớp đúng chữ §6.
Về **Hà Thừa Thiên (370–447)**: chỉ chồng thời với Tổ Xung Chi (429–500) **18 năm đầu đời ông**, và Hà mất khi Tổ 18 tuổi. Gọi là "nhà lịch pháp cùng thời" là **nới**; quan hệ thật là **thế hệ trước** — lịch Nguyên Gia (443) của Hà chính là bộ lịch mà lịch Đại Minh (462) của Tổ thay thế. Ứng viên **thật sự cùng thời** đúng nghĩa thì atlas chưa nêu được ai.
Câu thay thế đề xuất: *"Lưu Huy, người đặt phương pháp ông dùng, **đã có mục riêng ở nhóm CE03 nên không phải ứng viên bị loại**. Ứng viên bị loại gần nhất là Hà Thừa Thiên (370–447) ở thế hệ ngay trước, tác giả lịch Nguyên Gia mà lịch Đại Minh của Tổ Xung Chi thay thế."*
Hà Thừa Thiên **không có mục riêng** ✓.

**4. Liên kết — ĐẠT.** `CH04-CE03-09` → **Lưu Huy** ✓ đúng người, đúng chiều, `trực tiếp` đúng mức (Tổ dùng thẳng phương pháp cát viên của Lưu Huy).

**5. Nguồn — ĐẠT.** *Tống thư*, **Luật lịch chí** ✓ — đúng tên thiên (宋書·律曆志), và đó chính là nơi chép kết quả pi của Tổ Xung Chi; số/tên thiên này tra được, không phải đoán. Jean-Claude Martzloff, *A History of Chinese Mathematics*, Springer, **1997** ✓ có thật (bản dịch tiếng Anh của *Histoire des mathématiques chinoises*, 1987), đúng thể loại, đúng chủ đề.

---

## CH04-CE05-12 · Bắc Nguỵ Hiếu Văn Đế

**1. Đúng — hai mốc Owner nghi.** Dời đô Lạc Dương **494** ✓. Chế độ **quân điền (均田制) ban năm 485** ✓. Cấm tiếng Tiên Ti, y phục Tiên Ti ở triều, đổi họ hoàng tộc Thác Bạt → Nguyên, khuyến khích hôn nhân Hán–Tiên Ti ✓ (các sắc lệnh 495–496). Tên `Thác Bạt Hoằng` ✓ đúng chữ (拓跋宏, phân biệt với cha ông Hiến Văn Đế 拓跋弘).

**2. SAI (lỗi lập luận) — mục TỰ MÂU THUẪN giữa đoạn "đóng góp chính" và đoạn "Vì sao chọn".** ← mục Owner yêu cầu đánh giá.
Hai câu đặt cạnh nhau:
- Đoạn đóng góp: *"Nhưng **thiết chế có hệ quả dài nhất** là chế độ quân điền đặt từ năm 485..."*
- Đoạn Vì sao chọn: *"Ứng viên cùng triều là Thái hậu Phùng thị, người nhiếp chính và **thực sự ban chế độ quân điền năm 485**..."*
Mâu thuẫn là có thật và nằm ở chỗ này: mục **tự khai rằng thành tựu nó gọi là "có hệ quả dài nhất" không phải của người được chọn**. Năm 485 Hiếu Văn Đế **18 tuổi** và Thái hậu Phùng thị nhiếp chính cho tới khi bà mất **năm 490**; mục thừa nhận đúng sự thật đó. Nhưng sau khi thừa nhận, mục lại **chuyển trụ** sang chương trình Hán hoá để biện minh cho lựa chọn — mà không rút lại hay hạ bớt câu "hệ quả dài nhất" ở trên, và **dòng "Ảnh hưởng tới" vẫn giữ nguyên "Chế độ quân điền ở nhà Tuỳ, Đường, Nhật Bản và Việt Nam"** như thành tựu của ông.
Khác với mục -05 (Theodosius II / Pulcheria), ở đó đóng góp được viện dẫn gắn với ngôi hoàng đế; ở đây **chính mục nói Phùng thị mới là người ban**. Đây là tự mâu thuẫn thật, không phải chỉ vụng về.
Cách sửa đề xuất (hai bước):
(a) đoạn đóng góp đổi thành: *"Thiết chế có hệ quả dài nhất gắn với triều ông là chế độ quân điền ban năm 485 — do Thái hậu Phùng thị nhiếp chính ban, và được ông duy trì cùng mở rộng sau khi bà mất năm 490."*
(b) đoạn Vì sao chọn giữ nguyên trụ Hán hoá, nhưng thêm một câu nói thẳng: *"Chế độ quân điền thuộc về bà chứ không về ông; lựa chọn này đặt trên chương trình Hán hoá, là phần ông tự quyết sau năm 490."*
(c) dòng "Ảnh hưởng tới" thứ nhất đổi thành *"Chế độ quân điền ở nhà Tuỳ, Đường và các nước phỏng theo · kế thừa · qua trường phái"* và hạ mức, vì đóng góp gốc không phải của ông.

**3. Nghi vấn — "Nhà Tuỳ và nhà Đường kế thừa **nguyên** chế độ này, và **Nhật Bản cùng Việt Nam** về sau đều phỏng theo."**
Hai chỗ nới:
- **"nguyên"** quá mạnh. Quân điền đời Đường khác đáng kể bản Bắc Nguỵ về hạn mức, về phân biệt ruộng khẩu phần / ruộng vĩnh nghiệp, và về đối tượng; nó là **kế thừa có sửa đổi**, không phải sao nguyên.
- **"Việt Nam ... phỏng theo"** nối hai thứ cách nhau gần mười thế kỷ. Chế độ **quân điền ở Việt Nam** là của **Lê Thánh Tông (phép quân điền 1477)** và **Gia Long (1804)**, và về cơ chế là **chia định kỳ ruộng công của làng xã**, không phải nhà nước cấp ruộng theo nhân khẩu rồi thu hồi khi người chết như bản Bắc Nguỵ. Nhật Bản thì vững hơn nhiều (**ban điền thu thụ pháp 班田収授法**, từ cải cách Taika 646, mô phỏng trực tiếp quân điền nhà Đường).
Câu thay thế đề xuất: *"Nhà Tuỳ và nhà Đường kế thừa chế độ này với nhiều sửa đổi, và Nhật Bản phỏng theo bản nhà Đường thành ban điền thu thụ pháp từ cải cách Taika. Ở Việt Nam, phép quân điền thời Lê Thánh Tông và thời Nguyễn dùng lại tên gọi và nguyên tắc chia ruộng theo nhân khẩu, nhưng vận hành trên ruộng công làng xã chứ không theo cơ chế nhà nước cấp–thu của Bắc Nguỵ."*

**4. Thể thức §5 — ứng viên: ĐẠT.** Thái hậu Phùng thị (442–490) ✓ **thật sự cùng thời** và cùng triều. Thác Bạt Khuê (Đạo Vũ Đế, 371–409) — **không cùng thời**, cách ông gần một thế kỷ, và mục **không dán nhãn** cho chỗ này (chỉ gọi là "người lập triều", đủ để người đọc hiểu là trước, nhưng không nêu niên đại). Đây là chỗ mỏng nhất; đề nghị ghi rõ "người lập triều **gần một thế kỷ trước**". **Không ai trong hai người có mục riêng** ✓ (Thái hậu Phùng thị nằm trong danh sách bị loại — nhất quán).

**5. Liên kết — ĐẠT, đã mở đích đọc tên.** `CH03-BCE02-02` → `content/ch03.md` dòng 439 = **Hán Vũ Đế** ✓ đúng người; quan hệ "kế thừa · qua trường phái" hợp lý (mô hình nhà nước Nho giáo hoá mà chương trình Hán hoá lấy làm chuẩn), chiều và niên đại đúng.

**6. Nguồn — ĐẠT, kể cả tên thiên.** *Nguỵ thư*, **Cao Tổ kỷ** ✓ — **tra đúng**: miếu hiệu của Hiếu Văn Đế là **Cao Tổ (高祖)**, nên 魏書·高祖紀 là đúng thiên, không phải đoán. Scott Pearce, Audrey Spiro và Patricia Ebrey (chủ biên), *Culture and Power in the Reconstitution of the Chinese Realm, 200–600*, Harvard University Asia Center, **2001** ✓ có thật, đúng năm, đúng thể loại (tuyển tập chuyên khảo có chủ biên — và mục ghi đúng là "chủ biên"), đúng giai đoạn.

---
## Ghi chú biên tập — rà toàn bộ

### A. Khối "Cách chapter này được soạn" — ĐẠT
So từng chữ với khối nguyên văn ở cuối `prompts/atlas-prompt.md`: **khớp hoàn toàn**, và đặt đúng vị trí mở đầu `## Ghi chú biên tập` theo yêu cầu CONTRIBUTING ("Khối minh bạch bắt buộc"). Không có lỗi.

### B. Khối "Vì sao chapter này nặng về tôn giáo, và chuyện đó có làm lệch không"

**B1. SAI — "Mười bảy trên năm mươi tám mục lấy Tôn giáo/Tâm linh làm một trong hai lĩnh vực".**
Đếm thật trên `content/ch04.md`: **hai mươi** trên năm mươi tám. Lệnh kiểm:
```
awk '/^### CH04/{id=$2} /lĩnh vực:.*Tôn giáo\/Tâm linh/{print id}' content/ch04.md
```
Hai mươi ID: `CE01-01, -02, -06` · `CE02-03, -04, -08, -09, -10` · `CE03-02, -04` · `CE04-01, -02, -03, -10, -11, -12` · `CE05-01, -02, -07, -08`.
Con số sai lệch **+3**, và sai theo hướng **giảm nhẹ chính vấn đề mà khối này đang tự phê bình** — tức là một con số sai làm khối minh bạch bớt gắt hơn thực tế. Tỉ lệ thật là **34,5%** chứ không phải 29,3%.
Câu thay thế đề xuất: *"**Hai mươi** trên năm mươi tám mục lấy Tôn giáo/Tâm linh làm một trong hai lĩnh vực — hơn một phần ba, tỉ lệ cao nhất của atlas tới nay."*

**B2. SAI — "ở cả bốn vùng" rồi liệt kê năm hiện tượng trải trên sáu vùng.**
Khối viết *"hình thành hoặc được thiết chế hoá ở **cả bốn vùng**"* rồi liệt kê **năm** mục: Kitô giáo ở Địa Trung Hải, Phật giáo Đại thừa từ Kushan sang Đông Á, Manichaeism ở Lưỡng Hà, Hoả giáo thành quốc giáo Sasan, Theravāda ở Sri Lanka. Chiếu vào từ vựng `REGIONS` của chính dự án, năm hiện tượng ấy nằm ở **Châu Âu, Trung Đông/Bắc Phi, Trung Á, Đông Á, Nam Á** — tức **năm** vùng, không phải bốn. Số "bốn" không tương ứng với bất kỳ cách đếm nào.

**B3. SAI (nghiêm trọng hơn B1–B2) — khối giải thích thống kê bằng một hiện tượng KHÔNG CÓ trong thống kê.**
Khối nêu *"Hoả giáo thành quốc giáo Sasan"* làm một trong các lý do khiến chapter nặng về tôn giáo. Nhưng đã kiểm cả ba mục Sasan của chapter:
- `CH04-CE03-05 · Ardashir I` → lĩnh vực **Chính trị/Nhà nước**
- `CH04-CE03-06 · Shapur I` → **Quân sự, Chính trị/Nhà nước**
- `CH04-CE04-05 · Shapur II` → **Chính trị/Nhà nước, Quân sự**
**Không mục nào** gắn nhãn Tôn giáo/Tâm linh, và **Kartir** — đại giáo sĩ, người thật sự thiết chế hoá Hoả giáo — nằm trong danh sách **bị loại**. Vậy Hoả giáo đóng góp **0 trên 20** mục tôn giáo. Lấy nó ra giải thích con số là giải thích bằng thứ không có trong con số.
Câu thay thế đề xuất: *"...ở nhiều vùng — Kitô giáo ở Địa Trung Hải, Phật giáo Đại thừa từ Kushan sang Đông Á, Manichaeism ở Lưỡng Hà, Theravāda được hệ thống hoá ở Sri Lanka. (Hoả giáo Sasan cũng được thiết chế hoá trong giai đoạn này nhưng **không** đóng góp mục nào vào con số trên: ba mục Sasan của chapter đều gắn nhãn chính trị/quân sự, còn Kartir thì bị loại — đó là một lỗ hổng của chapter chứ không phải của giai đoạn.)"*

**B4. Nghi vấn — "Đây không phải lựa chọn của người soạn mà là đặc điểm của giai đoạn."**
Mệnh đề này chối trách nhiệm quá mức. Tỉ lệ 20/58 là kết quả của **cả hai**: đặc điểm giai đoạn **và** các quyết định chọn–loại cụ thể. B3 chứng minh điều đó: cùng một giai đoạn ấy, chapter đã chọn gắn nhãn Hoả giáo là chính trị chứ không phải tôn giáo, và đã loại Kartir. Những cái đó là lựa chọn của người soạn.

**B5. ĐÚNG và đáng giữ — nửa sau của khối.** Câu *"nếu tiêu chí (b) độ bền được ưu tiên thì các tôn giáo còn sống tới nay tất nhiên chiếm ưu thế, và đó là một thiên lệch có sẵn trong bộ tiêu chí chứ không riêng của chapter này"* là **nhận định trung thực, đúng, và tự phê bình đúng chỗ**. Đây là phần tốt nhất của toàn bộ Ghi chú biên tập.

**Đánh giá tổng về tính trung thực của khối:** **trung thực về ý hướng, không trung thực về số liệu.** Nửa sau nêu đúng thiên lệch gốc của bộ tiêu chí (B5). Nhưng nửa đầu đứng trên **một con số sai (B1)**, **một cách đếm vùng sai (B2)**, **một ví dụ không có trong dữ liệu (B3)**, và **một câu chối trách nhiệm (B4)**. Một khối minh bạch mà bản thân nó sai số liệu thì làm hỏng đúng cái nó định bảo vệ. Cần sửa cả bốn trước khi commit.

### C. Khối "Một mục bị gỡ liên kết vì lint bắt nghịch niên đại" — ĐẠT
- "ông sinh năm **398**, tức **ba trăm năm mươi lăm năm** sau khi bà mất" ✓ — Trưng Trắc mất **43 CN**; 398 − 43 = **355**. Số học đúng.
- Lập luận "quan hệ thật là ông **viết về** bà, không phải tác động lên bà" ✓ đúng và đúng tinh thần CONTRIBUTING §8.
- Lý do gỡ cặp Hán Quang Vũ Đế–Hai Bà Trưng ("đàn áp quân sự không phải quan hệ tư tưởng") ✓ nhất quán với tiền lệ Hán Vũ Đế–Triệu Đà ở Ch3.
- **Nhưng xem CH04-CE05-04 §6**: cùng tiêu chuẩn ấy chưa được áp cho dòng `Rugila · kế thừa · trực tiếp` ở mục Attila. Khối này tự đặt ra một quy tắc mà chapter chưa áp đều.

### D. Khối "Ứng viên Việt Nam đã được cân nhắc và kết quả" — ĐẠT
- Hai Bà Trưng, khởi nghĩa **40–43** ✓; Bà Triệu **248** ✓; Sĩ Nhiếp **137–226** ✓.
- "cả ba đã có mục riêng ở phụ lục (`CH90-CE01_09-01`, `-02`, `-03`)" — **đã mở `content/ch90.md` đọc tên**: dòng 42 `Trưng Trắc`, dòng 58 `Bà Triệu`, dòng 73 `Sĩ Nhiếp` ✓ **cả ba ID trỏ đúng người**.
- Lâm Ấp lập **192** ✓.
- *Nghi vấn nhẹ:* *"không có nhân vật nào định danh được bằng nguồn đương thời"* về Lâm Ấp — thư tịch Trung Hoa **có** nêu tên **Khu Liên (區連)** làm người lập quốc. Chữ "**đương thời**" cứu được mệnh đề (các ghi chép ấy đều muộn hơn nhiều), nhưng nên nói ra tên ấy rồi giải thích vì sao loại, thay vì để người đọc tưởng là không có tên nào.

### E. Khối "Ứng viên mạnh đã bị loại và lý do"

**E1. ĐẠT — không mắc lỗi hệ thống CONTRIBUTING §6.**
Đối chiếu **toàn bộ 49 tên** trong năm gạch đầu dòng với **221 tiêu đề `### `** của `content/ch0*.md` + `content/ch90.md`: **không tên nào trong danh sách bị loại có mục riêng trong atlas**. (Một kết quả khớp duy nhất khi dò thô — `CH02-BCE05-10 · Darius I` — là **dương tính giả**: chuỗi "Arius" nằm trong "Darius".) Đây là chỗ Ch3 mắc 11 lần; Ch4 **sạch**.

**E2. ĐẠT — mệnh đề "mỗi người đều được nêu đích danh trong mục tương ứng" kiểm được và đúng.**
Đã đếm số lần xuất hiện của từng tên trong `content/ch04.md`. **Tất cả** các tên ở gạch đầu dòng 1, 3, 4 và 5 đều xuất hiện **≥ 2 lần** (một lần trong danh sách bị loại, ít nhất một lần nữa trong một mục) → mệnh đề đứng vững.

**E3. SAI — lý do loại Iamblichus (và Epictetus) không đúng.**
Nguyên văn: *"Epictetus, Musonius Rufus, Libanius, Themistius, Iamblichus, Damascius, Syrianus: xếp sau ở độ bền **hoặc không để lại văn bản đủ**."*
Vế "không để lại văn bản đủ" không áp được cho hai người trong danh sách:
- **Iamblichus** còn nguyên một khối lớn: *De mysteriis*, *De vita pythagorica*, *Protrepticus*, *De communi mathematica scientia*, *In Nicomachi arithmeticam introductionem*. Ông là người định hình toàn bộ Tân Plato hậu kỳ mà Proclus (`CE05-03`) thừa kế — tức lý do loại càng khó đứng.
- **Epictetus** còn *Diatribai* và *Encheiridion* qua Arrianus, và *Encheiridion* là một trong những văn bản **bền nhất** của truyền thống phương Tây — nên vế "xếp sau ở độ bền" cũng không áp được cho ông.
Vì câu dùng "hoặc", nó chỉ cần **một** vế đúng cho **mỗi** người; nhưng với Iamblichus thì **cả hai vế đều sai**, và với Epictetus thì vế độ bền sai còn vế văn bản cũng sai. Câu như đang viết không cho người đọc biết lý do thật.
Câu thay thế đề xuất: *"Epictetus, Musonius Rufus, Libanius, Themistius, Iamblichus, Damascius, Syrianus: đều để lại văn bản và đều có ảnh hưởng thật; bị loại vì các suất Triết học của chapter đã dành cho những người có **phạm vi (a)** rộng hơn — Iamblichus và Syrianus là hai ca sát nút nhất, vì mạch Tân Plato hậu kỳ mà Proclus kế thừa là do họ định hình."*

**E4. Nghi vấn — "trần nhóm CE05 được nới thì [Hieronymus] là người đầu tiên nên xét".**
Mệnh đề này không khớp với tình trạng thật của chapter: theo chính khối "Điểm cần kiểm chứng thêm", **CE02 và CE03 mới là hai nhóm còn chỗ trống** (11/12), còn CE05 đã kín 12. Hieronymus (k. 347–420) thuộc CE04/CE05 nên lập luận vẫn đúng về nhóm, nhưng nói "nếu trần được nới" là đặt vấn đề sai: trần 12 là quy tắc cứng của dự án, không phải thứ sẽ được nới. Cách nói đúng là **ai bị đẩy ra để lấy chỗ** — đúng khuôn CONTRIBUTING yêu cầu ở phần "Phản hồi mà không cần viết code".

### F. Khối "Điểm cần kiểm chứng thêm"

**F1. ĐÚNG — Kanishka.** "đề xuất trải từ 78 tới 144 CN", "dùng khoảng 127–150 theo Falk" ✓ — Falk (2001) đặt năm lên ngôi của Kanishka ở **127**. Niên đại và quy thuộc học giả đều đúng.

**F2. ĐÚNG — phân bố nhóm.** *"Tổng số mục là 58 nhưng phân bố không đều: CE01 và CE04, CE05 đủ 12, còn CE02 và CE03 chỉ 11."*
Đếm thật: **CE01 = 12, CE02 = 11, CE03 = 11, CE04 = 12, CE05 = 12**, tổng **58** ✓. **Cả năm con số và tổng đều đúng.**

**F3. SAI — "Chỉ ba trên năm mươi tám mục là phụ nữ", và khối TỰ MÂU THUẪN trong cùng một câu.**
Nguyên văn: *"**Chỉ ba** trên năm mươi tám mục là phụ nữ (**Ban Chiêu, Hypatia, và không ai khác** — Thái hậu Phùng thị cùng Pulcheria chỉ có trong danh sách bị loại)."*
Câu nói "ba" rồi **tự liệt kê đúng hai tên** và đóng bằng chữ "**và không ai khác**". Đếm thật trên 58 mục: **hai** — `CH04-CE01-12 · Ban Chiêu` và `CH04-CE05-06 · Hypatia`. Con số đúng là **2/58 (3,4%)**, không phải 3/58.
Lỗi này nặng hơn B1 vì nó nằm trong câu tự phê bình về thiên lệch giới, và sai **theo hướng làm con số đỡ gắt hơn**. Và nó đáng lẽ bắt được mà không cần tra cứu gì: câu tự bác chính nó.
Câu thay thế đề xuất: *"**Chỉ hai** trên năm mươi tám mục là phụ nữ — Ban Chiêu (CH04-CE01-12) và Hypatia (CH04-CE05-06), và không ai khác; Thái hậu Phùng thị cùng Pulcheria chỉ có trong danh sách bị loại, dù mục CH04-CE05-12 tự thừa nhận Phùng thị mới là người ban chế độ quân điền. Cần kiểm lại ở P4."*

**F4. Nghi vấn nhẹ — mô tả cơ chế lint ở mục Giê-su/Wikidata.**
Nguyên văn: *"Wikidata xếp Giê-su (Q302) vào lớp Q178885 'thần linh' bên cạnh lớp 'nhân vật Kinh Thánh là người'. **Lint không cảnh báo vì lớp thứ hai dẫn về Q5**..."*
Đã tra `Q302` → P31 gồm: **Q178885 (deity)** ✓, Q20643955 (human biblical figure) ✓, **và Q5 (human) được khai báo TRỰC TIẾP**, cùng Q4271324, Q18563360, Q825, Q51625. Nhận định về Q178885 ✓ **đúng**, và kết luận ("phân loại Wikidata mang theo phán đoán thần học") ✓ **đúng và đáng giữ**. Chỉ phần giải thích cơ chế hơi lệch: lint không cảnh báo vì **Q5 nằm thẳng trong P31**, không cần đi vòng qua "lớp thứ hai".

**F5. ĐẠT — các mục còn lại.** Nhận định về niên đại Nāgārjuna / Asaṅga / Vasubandhu và giả thuyết hai-Vasubandhu của Frauwallner ✓ đúng. Việc phân tầng ở mục Giê-su ✓ đúng và là cách xử lý tốt. Ba mục "chỉ còn qua bản dịch hoặc bản mô" (Origen qua Rufinus, Vương Hi Chi không còn nét bút gốc, Cố Khải Chi chỉ còn bản mô đời Đường) ✓ cả ba đều đúng.

### G. Khối "Nhân vật có thể thuộc thế kỷ khác" — ĐẠT, một chỗ cần siết
Galen 129–216 ✓ · Tertullianô và Nāgārjuna sang TK 3 ✓ · Diocletianus trị vì 284–305, mất **311** ✓ · Augustinô sinh 354, *Confessiones* 397–400 và *De Civitate Dei* 413–426 → "đều viết sau năm 397" ✓ · Āryabhaṭa 476–k. 550, Āryabhaṭīya 499 ✓ · Cưu-ma-la-thập sinh 344, dịch ở Trường An 401–413 ✓.
*Siết nhỏ:* dòng Diocletianus viết *"toàn bộ chương trình cải cách nằm trong thế kỷ 3 và đầu thế kỷ 4"* — cải cách thuế của ông, và nhất là **Sắc lệnh giá tối đa 301** cùng cuộc bách hại từ **303**, đều nằm ở **thế kỷ 4**, không phải TK 3. Lý do xếp nhóm vẫn đứng (trị vì từ 284), nhưng câu giải thích thì nghiêng.

---

## §13. Bảng kiểm liên kết — đã mở từng đích đọc tên

| Mục nguồn | ID đích | Tên thật ở đích | Kết luận |
|---|---|---|---|
| -01 | CH04-CE03-01 | Plotinus | ✓ |
| -01 | CH04-CE01-02 | Phaolô thành Tarsus | ✓ |
| -01 | CH04-CE02-10 | Tertullian | ✓ đúng người, quan hệ yếu |
| -02 | CH04-CE02-09 | Irenaeus thành Lyon | ✓ |
| -03 | CH04-CE03-01 | Plotinus | ✓ |
| -03 | CH03-BCE04-01 | **Plato** (ch03 dòng 7) | ✓ |
| -05 | CH03-BCE01-03 | **Cicero** (ch03 dòng 643) | ✗ **SAI ĐÍCH** — xem -05 §3 |
| -05 | CH04-CE04-01 | Constantinus I | ✓ |
| -06 | CH04-CE03-01 | Plotinus | ✓ |
| -07 | CH04-CE02-08 | Nāgārjuna | ✓ |
| -07 | CH04-CE04-11 | Vasubandhu | ✓ |
| -07 | CH04-CE03-10 | Vương Bật | ✓ đúng người, quan hệ là suy luận |
| -07 | CH90-CE01_09-04 | **Tì-ni-đa-lưu-chi** (ch90 dòng 89) | ✓ đúng người, quan hệ yếu nhất nhóm |
| -08 | CH03-BCE03-01 | **Ashoka** (ch03 dòng 214) | ✓ |
| -08 | CH02-BCE06-03 | **Đức Phật** (ch02 dòng 318) | ✓ |
| -10 | CH04-CE01-11 | Ban Cố | ✓ |
| -10 | CH03-BCE01-06 | **Tư Mã Thiên** (ch03 dòng 694) | ✓ |
| -11 | CH04-CE03-09 | Lưu Huy | ✓ |
| -12 | CH03-BCE02-02 | **Hán Vũ Đế** (ch03 dòng 439) | ✓ |

**19 liên kết nội bộ, 1 sai đích** (`-05 → Cicero`). Không có liên kết nghịch niên đại, không có liên kết tới chính mình.

---

## Tổng hợp theo mức

**Sai (8)**
1. `-03` Proclus — *Yếu lược thần học* **211** mệnh đề, không phải 210.
2. `-04` Attila — đảo ngược trình tự nhân quả của làn sóng di cư German (các đợt lớn đều trước khi ông cầm quyền).
3. `-04` Attila — counterfactual tự phản, chứng minh ngược điều nó muốn chứng minh.
4. `-05` Theodosius II — tường thành giữ thành phố **hơn** một nghìn năm (1040), không phải "gần".
5. `-05` Theodosius II — liên kết `CH03-BCE01-03` trỏ **Cicero**, sai đích.
6. `-08` Buddhaghosa — nhan đề sách Crosby bị sinh ra: đúng là *Continuity, Diversity, and Identity*, không phải *A New History*.
7. `-09` Āryabhaṭa — "bảng sin đầu tiên của lịch sử" sai (Sūrya Siddhānta có trước; và mâu thuẫn với `CH03-BCE02-03` trong chính atlas).
8. `-10` Phạm Diệp — Hậu Hán thư không phải nguồn chữ Hán sớm nhất về Giao Chỉ (Hán thư của Ban Cố có trước ba thế kỷ).
*Ghi chú biên tập — thêm 4:* **17/58 → 20/58** (B1) · **"bốn vùng" cho năm hiện tượng ở năm vùng** (B2) · **Hoả giáo giải thích một con số nó không góp mặt** (B3) · **"ba phụ nữ" nhưng chỉ liệt kê hai, và thật sự chỉ có hai** (F3). Cộng **E3** (lý do loại Iamblichus/Epictetus) và **G** (cải cách Diocletianus "ở TK 3").

**Nghi vấn (9)** — `-01` "không tác giả Kitô giáo nào khác" · `-01` "tác phẩm phương Tây đầu tiên" · `-02` "người đầu tiên lập luận có hệ thống" về quyền Phêrô · `-06` "các nguồn gần thời nhất" ở số nhiều · `-06` ba tác phẩm trình bày cùng một mức bằng chứng · `-07` "mười sáu năm" (384–401 cho ra 17) · `-08` "mười lăm thế kỷ" áp cho cả năm nước Theravāda · `-09` đường truyền sang Arab rút mất mắt xích Brahmagupta · `-12` "nguyên chế độ" và "Việt Nam phỏng theo".

**Thiếu (4)** — Bối cảnh bỏ trắng Ba Tư Sasan và Ấn Độ Gupta · `-02` việc Attila rút không gắn hàng rào (nạn đói, dịch, chiến dịch Marcianus) · `-05` không nêu Codex Gregorianus/Hermogenianus để đỡ cho chữ "chính thức" · `-04` nguồn Kelly bị dùng lệch hướng.

**Thể thức (6)** — `-01` trường `nơi:` xếp Milano vào Bắc Phi · `-04` liên kết Rugila áp tiêu chuẩn khác với tiêu chuẩn chính chapter đặt ra khi gỡ cặp Hán Quang Vũ Đế–Hai Bà Trưng · `-07`, `-09`, `-10` nêu **0 ứng viên cùng thời** mà không "viết thẳng là không có" theo CONTRIBUTING §5 · `-11` gọi Lưu Huy là "ứng viên" dù ông có mục riêng (có công khai, nhưng chưa đúng chữ §6) · `-12` Thác Bạt Khuê nêu không kèm niên đại.

**Không kiểm được (2)** — `-07` quy mô "hàng trăm người" của ban dịch (các con số truyền thống trải từ 500 tới 3000, không xác minh độc lập được) · `-07` "bản tụng niệm chuẩn ở Việt Nam" (không có nguồn học thuật kiểm được; mệnh đề về văn bản nền thì hợp lý).

**Đạt, không có lỗi** — 12/12 Q-ID trỏ đúng người · URL SEP Proclus HTTP 200 và đúng chủ đề · toàn bộ 49 tên trong danh sách bị loại **không ai** có mục riêng trong atlas (Ch3 từng mắc 11 lần) · **23/24** mục nguồn có thật, đúng năm, đúng thể loại (chỉ nhan đề Crosby sai) · số quyển/thiên ở `-06` (Socrates q. VII), `-11` (Tống thư, Luật lịch chí) và `-12` (Nguỵ thư, Cao Tổ kỷ) **tra đúng** · khối minh bạch khớp nguyên văn · phân bố nhóm 12/11/11/12/12 và tổng 58 **đúng** · ba ID phụ lục Việt Nam trỏ đúng người · mục `-11` Tổ Xung Chi không có lỗi số học nào.

---
## Đánh giá lựa chọn nhân vật

**Độ phủ — đạt yêu cầu tối thiểu, nhưng sát sàn ở vùng.**
Lĩnh vực: **9/16** (Triết học, Tôn giáo/Tâm linh, Luật, Chính trị/Nhà nước, Quân sự, Toán học, Khoa học tự nhiên, Ngôn ngữ học, Sử học) — vượt xa ngưỡng "ít nhất 4" của prompt §5.
Vùng: **4/9** — Châu Âu (4 mục: -02, -03, -04, -05), Đông Á (4 mục: -07, -10, -11, -12), Nam Á (2: -08, -09), Trung Đông/Bắc Phi (2: -01, -06). Qua ngưỡng "ít nhất 3", nhưng cần nói rõ rằng **cả hai mục "Trung Đông/Bắc Phi" đều là nhân vật Hy–La ở Alexandria và Hippo**, tức về mặt truyền thống trí tuệ thì nhóm này thực chất chỉ có **ba** mạch: Hy–La, Hán, và Ấn–Pali.
Vắng mặt hoàn toàn: **Trung Á, Đông Nam Á, Châu Phi hạ Sahara, Châu Mỹ** — và nghiêm trọng hơn cả, **Ba Tư Sasan**, dù chapter có hai mục Sasan ở CE03 và một ở CE04. Thế kỷ 5 Sasan không phải khoảng trống tư liệu: đó là triều Yazdegerd I và Peroz I, các cuộc chiến với Hephthalite, và cuộc ly khai của Giáo hội Đông phương sau Chalcedon.

**Ứng viên bị bỏ sót mà tôi cho là mạnh hơn ít nhất một mục đang có:**

1. **Clovis I (k. 466–511)** — đây là chỗ hổng lớn nhất của nhóm. Việc ông theo Kitô giáo **Nicaea** chứ không phải Arius (k. 496–508) là quyết định đơn lẻ có hệ quả dài nhất của thế kỷ 5 ở Tây Âu: nó gắn người Frank với hàng giám mục Gallo-La Mã trong khi mọi vương quốc German khác (Visigoth, Ostrogoth, Vandal, Burgundy) đều theo Arius và đều bị cô lập rồi tiêu vong. Vương triều ông lập kéo dài ba thế kỷ và vương quốc ấy thành nước Pháp.
   So **trực tiếp với `CE05-04 · Attila`** theo đúng bốn tiêu chí: độ bền (b) — liên minh Attila tan trong **một năm**, vương quốc Clovis sống **ba thế kỷ**; counterfactual (d) — mục Attila **tự khai** rằng cấu trúc của ông bốc hơi ngay khi ông chết (xem phê bình -04 §2), trong khi một nước Frank theo Arius sẽ cho một châu Âu khác hẳn. Theo chính bộ tiêu chí của dự án, **Clovis thắng Attila ở (b) và (d)**. Nếu phải chọn một người ra để lấy chỗ, tôi đề nghị đó là Attila.

2. **Pulcheria (399–453)** và **Thái hậu Phùng thị (442–490)** — xem dưới, mục "một khuôn mẫu lặp".

3. **Một mục Đông Nam Á.** Prompt §5 yêu cầu *"chủ động xét ... Đông Nam Á (bao gồm Việt Nam)"*, và nhóm CE05 có **0**. Thế kỷ 5 là lúc Phù Nam ở đỉnh (cảng Óc Eo, các sứ bộ sang Trung Hoa của Jayavarman Kaundinya trị vì 478–514) và là lúc các bia Phạn ngữ sớm nhất của Đông Nam Á xuất hiện. Nếu tư liệu thật sự không định danh được ai, thì theo CONTRIBUTING §5 **phải viết thẳng là không có** — Ghi chú biên tập hiện chỉ nói về Việt Nam, không nói về Đông Nam Á nói chung.

4. **Tanyao (曇曜, hoạt động k. 460–470)** — tăng chủ trì mở các hang Vân Cương dưới Bắc Nguỵ, tức khởi đầu truyền thống điêu khắc Phật giáo đá quy mô nhà nước ở Đông Á. Nhóm CE05 có **0 mục Nghệ thuật/Kiến trúc**, dù thế kỷ 5 là thế kỷ của Vân Cương và của các hang Ajanta thời Vākāṭaka.

**Một khuôn mẫu lặp đáng đưa lên mặt bàn — không phải lỗi sự kiện mà là lỗi phương pháp.**
Nhóm CE05 **hai lần** làm đúng một việc: nêu một người phụ nữ, **thừa nhận bà mới là người thực sự làm việc được viện dẫn**, rồi vẫn chọn người đàn ông giữ ngôi.
- `-05`: *"Pulcheria, chị ông và là người nắm phần lớn quyền điều hành"* → chọn Theodosius II.
- `-12`: *"Thái hậu Phùng thị, người nhiếp chính và **thực sự ban chế độ quân điền năm 485**"* → chọn Hiếu Văn Đế, trong khi đoạn trên của chính mục gọi quân điền là *"thiết chế có hệ quả dài nhất"*.
Ở `-05` lập luận còn cứu được (pháp điển gắn với ngôi hoàng đế, uỷ ban do ông lập năm 429). Ở `-12` thì **không**: mục tự khai rằng thành tựu lớn nhất nó viện dẫn không phải của người nó chọn.
Khuôn mẫu này nối thẳng với **F3**: Ghi chú biên tập ghi *"chỉ ba trên năm mươi tám mục là phụ nữ"* trong khi con số thật là **hai**, và ghi rằng Phùng thị với Pulcheria *"chỉ có trong danh sách bị loại"* — mà không nói rằng ở cả hai ca, lý do loại đã bị chính mục tương ứng làm suy yếu. Tỉ lệ 2/58 không phải thuần "đặc điểm của giai đoạn"; ít nhất hai suất đã bị quyết định chọn–loại cụ thể lấy đi.
Đề nghị cho P4: hoặc nâng **Thái hậu Phùng thị** lên mục riêng ở CE05 (và chuyển quân điền sang mục bà, giữ Hiếu Văn Đế cho chương trình Hán hoá), hoặc viết lại `-12` theo cách sửa đề xuất ở mục ấy. Giữ nguyên như hiện nay là giữ một mâu thuẫn mà chính văn bản đã chỉ ra.

**Nhận xét cuối về chất lượng nhóm.**
Nhóm CE05 **chắc hơn hẳn** các nhóm bị phê bình ở Ch3 trên hai mặt quan trọng nhất: **không một tên nào trong danh sách bị loại có mục riêng trong atlas** (Ch3 mắc 11 lần), và **không một Q-ID nào trỏ nhầm người**. Số quyển/thiên — thứ CONTRIBUTING §3 cảnh báo mạnh nhất — được tra đúng cả ba lần được dùng. Dòng Nguồn chỉ hỏng **1/24** (nhan đề Crosby), tuy thêm **2/24** bị dùng lệch hướng lập luận (Kelly ở `-04`, Plofker ở `-09`).
Lỗi còn lại tập trung vào đúng ba chỗ: **(i) những con số được sinh ra thay vì tra** (211 mệnh đề, "gần một nghìn năm", 17/58, "ba phụ nữ", nhan đề sách Crosby); **(ii) những mệnh đề "đầu tiên" không được kiểm phản ví dụ** (bảng sin, pháp điển, nguồn sớm nhất về Giao Chỉ, quyền Phêrô, tự thuật phương Tây — **năm** mệnh đề "đầu tiên" trong mười hai mục, và **ba** trong số đó sai); **(iii) lập luận chọn người tự mâu thuẫn** (-04 và -12).
Khuyến nghị quy trình: trước khi commit, grep mọi mệnh đề chứa "đầu tiên" / "sớm nhất" / "duy nhất" trong chapter và bắt mỗi mệnh đề phải kèm một phản ví dụ đã được loại trừ bằng tên. Ở nhóm này, quy tắc đó một mình đã bắt được ba trên tám lỗi "Sai".
