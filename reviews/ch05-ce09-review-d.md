# Bình duyệt độc lập — ghi chú biên tập CE09, khối 7–13
Ngày: 2026-11-02 · phạm vi: content/ch05.md dòng 996–1018

---

## Khối 7 — **Độ nghiêng vùng không sửa được ở tầng chọn người của một thế kỷ** (dòng 996–997)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **Phân bổ vùng đúng từng người.** Rút 12 dòng metadata của `content/ch05.md` dòng 631–845: Trung Đông/Bắc Phi 3 (`CE09-04` Al-Khwarizmi, `-06` Hunayn, `-07` Ibn Hanbal); Đông Á 3 (`-02` Hàn Dũ, `-03` Kūkai, `-05` Trương Bảo Cao); mỗi vùng còn lại đúng 1 — Đông Nam Á `-01`, Châu Phi hạ Sahara `-08`, Trung Á `-09`, Châu Âu `-10`, Nam Á `-11`, Châu Mỹ `-12`. Tổng 12. ✔
- **Mọi tỉ lệ khớp `reports/stats.txt`, tính tay lại từ số đếm:** Trung Đông/Bắc Phi 76/233 = 32,6% và trước vòng 73/221 = 33,03% → "33,0% → 32,6%" ✔; Châu Âu 60/233 = 25,8%, trước 59/221 = 26,70% ✔; Nam Á 27/233 = 11,6%, trước 26/221 = 11,76% ✔.
- **Ba vùng mỏng:** Trung Á 2/221 = 0,90% → 3/233 = 1,29%; Châu Mỹ như trên; Đông Nam Á 1/221 = 0,45% → 2/233 = 0,86%. Các số hiển thị 1,3% / 1,3% / 0,9% khớp `stats.txt` ✔.
- **Ca kiểm chứng Al-Khwarizmi đúng và đúng quy tắc.** Mục `CH05-CE09-04` ghi `vùng: Trung Đông/Bắc Phi` với lý do "nơi hoạt động chính", khớp `CONTRIBUTING.md` *Quy ước trường `vùng:`* điểm 1. ✔
- **Mệnh đề "đổi nhãn `vùng:` cho hợp thống kê bị cấm" có chỗ dựa thật:** `CONTRIBUTING.md`, *Quy ước trường `vùng:`* điểm 4 ("Đừng đổi `vùng:` của một người để cải thiện thống kê"). ✔

**BẮT BUỘC — "hai cách duy nhất để nhích nhanh hơn" là sai, và chính hồ sơ cổng của vòng này bác nó.**

Nguyên văn: *"0,4 điểm là **mức tối đa một vòng trung thực có thể làm**, vì hai cách duy nhất để nhích nhanh hơn — hạ chuẩn, hoặc đổi nhãn `vùng:` cho hợp thống kê — đều bị `CONTRIBUTING.md` cấm."*

Sai ở hai chỗ:

1. **Tồn tại một cách thứ ba, hoàn toàn trung thực, và vòng này đã khảo sát nó rồi bỏ qua vì lý do khác.** `reports/ch05-ce09-gate.md` dòng 226 ghi **al-Tirmidhī `Q293578`** (824–892, Termez) là ứng viên Trung Á "mạnh", bị loại vì **trùng vai với al-Bukhārī**, không vì vùng. Dành cho ông một trong ba suất Trung Đông sẽ đưa Trung Á lên 4/233 = 1,7% thay vì 1,3% — tức **gấp đôi mức nhích mà khối đang gọi là "tối đa"** — mà không hạ chuẩn và không đổi nhãn vùng nào. Phân bổ 3 Trung Đông / 3 Đông Á là **một lựa chọn của người chọn**, đúng như khối 8 ngay bên dưới tự khai; gọi kết quả của lựa chọn ấy là trần vật lý của sự trung thực là tự bào chữa.
2. **`CONTRIBUTING.md` không có điều khoản nào cấm "hạ chuẩn".** Điều được viết ra là *Quy ước trường `vùng:`* điểm 4, và nó chỉ nói về việc **đổi nhãn vùng**. Khối gán cho `CONTRIBUTING.md` một lệnh cấm mà văn bản ấy không chứa — đúng loại thao tác "viện quy tắc nội bộ làm chỗ dựa giả" mà `reports/ch05-ce09-review-c.md` đã bắt một lần ở khối 2 (ca viện quy tắc 7 cho chuyện gán nhãn).

*Câu thay thế đề nghị:* "Mười hai người không sửa được một bảng đã có 221 người, và 0,4 điểm là mức mà **phân bổ 3 Trung Đông / 3 Đông Á của vòng này** cho phép. Một phân bổ khác nhích nhanh hơn được mà không phải hạ chuẩn: dành một suất Trung Đông cho al-Tirmidhī `Q293578` (824–892, Termez) sẽ đưa Trung Á lên 1,7%. Vòng này **không** chọn thế, vì ông trùng vai với `CH05-CE09-09` (xem `reports/ch05-ce09-gate.md` §3.7) — đó là một đánh đổi về tiêu chí, không phải một giới hạn của số học. Cái thật sự bị `CONTRIBUTING.md` cấm chỉ có một: đổi nhãn `vùng:` của một người để cải thiện thống kê (*Quy ước trường `vùng:`*, điểm 4)."

**NÊN — con số "221" không tồn tại trong `reports/stats.txt`, và khối không nói nó là số trước vòng.**

Nguyên văn: *"Mười hai người không sửa được một bảng **221 người**"*. `reports/stats.txt` dòng 1 ghi **233 nhân vật (atlas chính)**. 221 = 233 − 12, tức số **trước** khi dựng CE09 — đúng về số học, nhưng cả câu đứng ngay sau một loạt tỉ lệ "đo sau khi dựng", nên người đọc đối chiếu `stats.txt` sẽ thấy một con số không khớp và không có chỗ nào trong file giải thích. Mọi con số khác trong khối đều tự khai là "trước → sau"; riêng con số này thì không.
*Câu thay thế đề nghị:* "Mười hai người không sửa được một bảng vốn đã có 221 người (233 sau vòng này, theo `reports/stats.txt`)".

**NÊN — "ba vùng mỏng nhất" không phải ba vùng mỏng nhất.**

Theo `reports/stats.txt`, vùng mỏng nhất atlas là **Châu Đại Dương, 0,0%** — và nó không nhích 0,4 điểm, nó không nhích gì cả; chính khối 11 bên dưới tồn tại để giải thích điều đó. Ba vùng khối đang nói tới là ba vùng mỏng **có người vào ở vòng này**. Thêm nữa Châu Phi hạ Sahara cũng được thêm một người (`CE09-08`) và chỉ nhích 4/221 = 1,81% → 5/233 = 2,15%, tức **0,3 điểm**, không phải 0,4 — nên câu "mỗi vùng nhích đúng 0,4" chỉ đúng nếu hiểu phạm vi là đúng ba vùng kia.
*Câu thay thế đề nghị:* "…ba vùng mỏng có người vào ở vòng này mỗi vùng nhích **0,4 điểm phần trăm** — Trung Á và Châu Mỹ lên 1,3%, Đông Nam Á lên 0,9%; Châu Phi hạ Sahara cũng thêm một người và lên 2,1%. Châu Đại Dương vẫn 0,0% — xem khối về ʻAhoʻeitu bên dưới."

**CÂN NHẮC — chữ "đúng" trong "nhích đúng 0,4 điểm phần trăm" là sản phẩm của làm tròn.**

Tính từ giá trị chưa làm tròn: Trung Á +0,38 đ%, Châu Mỹ +0,38 đ%, Đông Nam Á +0,41 đ%. Ba con số ấy không bằng nhau; chúng chỉ trùng nhau sau khi làm tròn một chữ số thập phân. Trong một khối đang dạy cách đọc thống kê cho đúng, chữ "đúng" nên bỏ.

---

## Khối 8 — **Châu Âu 1/12 và Trung Đông 3/12 là cắt có chủ ý, không phải khan ứng viên** (dòng 999–1000)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **1/12 và 3/12 khớp metadata 12 mục** (xem khối 7). ✔
- **"ít nhất tám ứng viên qua cổng" ở Châu Âu** khớp `reports/ch05-ce09-gate.md` §3.8, liệt kê đúng tám tên bị cắt (Alfred, Photios I, Constantinus–Cyrillus và Methodius, Rabanus Maurus, Hincmar, Gottschalk, ʿAbd al-Raḥmān II, Ziryāb). ✔
- **Alfred Đại đế: 848/9 – 26-10-899, có *Asser* và *Anglo-Saxon Chronicle*.** Wikidata `Q83476` (`wbgetentities`, UA `history-atlas/0.1 (research)`): `P569 +0849` (precision 9), `P570 preferred +0899-10-26` (precision 11). ✔
- **Châu Âu "đang ở 26,7%"** khớp số trước vòng, 59/221. ✔
- **Mahāvīrācārya: *Gaṇitasārasaṅgraha*, 850, "văn bản Ấn Độ sớm nhất dành riêng hoàn toàn cho toán học", và chỗ ông sai về phép chia cho không.** Bài *Mahāvīra (mathematician)* trên en.wikipedia viết nguyên văn rằng ông soạn sách năm 850 CE dưới sự bảo trợ của Amoghavarsha, rằng ông tách chiêm tinh khỏi toán học, và rằng "It is the earliest Indian text entirely devoted to mathematics". ✔
- **Glagolitic và việc dịch phụng vụ sang tiếng Slav** — bài *Glagolitic script* trên en.wikipedia: bảng chữ được tạo ra trong thế kỷ 9 để dịch văn bản phụng vụ Hy Lạp sang tiếng Slav Giáo hội cổ. ✔
- **Quy tắc 6 sạch.** `grep` toàn bộ `content/*.md`: Alfred, Mahāvīrācārya, Cyrillus, Methodius **không có mục riêng ở bất kỳ chapter nào**, kể cả `content/ch90.md`. Nêu họ làm ứng viên bị loại là hợp quy tắc 6. ✔

**BẮT BUỘC — "Nếu CE10 không nhận họ" mô tả một khả năng không tồn tại, và nó trái với chính quy tắc niên đại mà cùng mục Ghi chú biên tập này áp hai lần.**

Nguyên văn: *"**Nếu CE10 không nhận họ**, vòng duyệt nên cân nhắc đảo họ vào chỗ một người Đông Á của nhóm này."*

Cả hai người chết trong thế kỷ 9. Tra Wikidata (`wbgetentities`, UA trung lập): `Q351026` *Saint Cyril the Philosopher*, `P31 = Q5`, sinh 827, **mất 14-02-869**; `Q470621` *Methodius of Thessaloniki*, `P31 = Q5`, sinh 815, **mất 06-04-885**. Sứ mệnh Moravia bắt đầu 863. Không có một phần nào của sự nghiệp họ rơi vào 901–1000. CE10 **không thể** nhận họ.

Đây không phải chuyện nhỏ về cách nói, vì chính mục `## Ghi chú biên tập` này áp quy tắc "thuộc thế kỷ của thời kỳ hoạt động chính" **hai lần theo đúng hướng ngược lại**: khối về Alcuin (dòng 975) đẩy ông sang CE08 vì ông hoạt động 782–804, và khối 12 (dòng 1012) đẩy Khúc Thừa Dụ sang CE10 vì ông bắt đầu từ 905. Một khối để ngỏ CE10 cho hai người mất năm 869 và 885 thì phá chính quy tắc ấy. (`README.md` dòng 77 còn ghi lint cảnh báo "đời sống không giao với nhóm" — nên gợi ý này cũng không qua được build.)

*Câu thay thế đề nghị:* "Họ **thuộc đúng thế kỷ 9** — Cyrillus mất 869, Methodius mất 885 — nên không có vòng nào sau CE09 nhận họ được; nếu vòng duyệt thấy đóng góp ấy phải có mặt thì chỗ duy nhất là **trong chính mười hai suất này**."

**BẮT BUỘC — "cùng dạng vấn đề đơn vị với Banū Mūsā" là một so sánh sai, và nó mâu thuẫn với khối 6 ngay phía trên.**

Nguyên văn: *"họ là **hai người cho một đóng góp**, cùng dạng vấn đề đơn vị với Banū Mūsā".*

Khối 6 (dòng 994) nêu đích danh hai điều làm hỏng ca Banū Mūsā: `Q423210` "**không phải `P31 = Q5`** mà là một thực thể tập thể", và "**việc tách ra một trong ba anh em không có cơ sở văn bản**". Không điều nào áp được vào ca này:

1. **Mỗi người có thực thể người riêng.** `Q351026` và `Q470621` đều `P31 = Q5`, đều có năm sinh–mất riêng. Thực thể cặp `Q239925` *Saints Cyril and Methodius* thì **không** `P31 = Q5` (nó là `Q125143602`/`Q125258836`) — tức atlas có thể chọn một người mà không phải dùng tới thực thể cặp, điều không làm được với Banū Mūsā.
2. **Việc tách có cơ sở văn bản.** Bảng chữ Glagolitic được quy cho **riêng Cyrillus**: bài *Glagolitic script* trên en.wikipedia viết "it was created in the 9th century ... by Cyril, a Christian monk from Thessalonica". Đóng góp chung là bản dịch phụng vụ; đóng góp được quy cho một người là bảng chữ.

Hệ quả: lý do loại thứ nhất **không đứng**, và vì vậy câu "hai lý do không liên quan tới chất lượng" chỉ còn một lý do (Châu Âu đã có Eriugena) — một lý do về **phân bổ vùng**, tức đúng loại lựa chọn mà cả khối này tồn tại để khai ra.

*Câu thay thế đề nghị:* "Ca gần nhất ở châu Âu là **Constantinus–Cyrillus và Methodius**: bảng chữ Glagolitic và việc dịch phụng vụ sang tiếng Slav là đóng góp thật và bền. Khác ca Banū Mūsā, ở đây **tách được**: `Q351026` và `Q470621` đều là thực thể người riêng, và bảng chữ Glagolitic được quy cho riêng Cyrillus. Vậy lý do loại thật chỉ có một, và nó là lý do phân bổ: **Châu Âu đã có Eriugena, và vòng này quyết giữ Châu Âu ở một suất.**"

**NÊN — đề xuất "đảo họ vào chỗ một người Đông Á" không thực hiện được: hai người vào một suất là 13 người.**

`CONTRIBUTING.md` dòng 13 ghi "mỗi nhóm trần 12 người", và mục *Lỗi chặn build* liệt "nhóm quá 12 người" là **lỗi chặn build**, không phải cảnh báo. Đưa hai người vào chỗ một người thì nhóm thành 13 và `build.py --offline` dừng. Nếu ý thật là "bỏ hai người Đông Á" thì phải viết ra, vì đó là một đánh đổi lớn hơn hẳn.
*Câu thay thế đề nghị:* "…thì chỗ duy nhất là trong chính mười hai suất này, và phải nói rõ cái giá: trần 12 là lỗi chặn build, nên **nhận cả hai nghĩa là bỏ hai người**, còn nhận một mình Cyrillus thì bỏ một."

**NÊN — "niên đại tốt nhất cả nhóm" không chứng minh được, và ít nhất là hoà.**

Nguyên văn: *"**Alfred Đại đế** có niên đại tốt nhất cả nhóm — 848/9 đến 26-10-899".* Năm sinh của Alfred là một khoảng một năm (Wikidata chỉ ghi `+0849` ở precision 9, và còn mang một `P570` hạng `deprecated` là 900). Trong nhóm, `CH05-CE09-02 · Hàn Dũ` ghi `768–824` và `CH05-CE09-03 · Kūkai` ghi `774–835`, cả hai `độ tin cậy niên đại: Cao`, cả hai năm sinh là một con số chứ không phải một khoảng. Chính `reports/ch05-ce09-gate.md` §3.9 mô tả Ḥunayn là "808/809–873, biên độ 1 năm" — **cùng hình dạng** với Alfred. Câu "tốt nhất cả nhóm" vì vậy là một xếp hạng không có thước đo đi kèm.
*Câu thay thế đề nghị:* "**Alfred Đại đế** có niên đại thuộc loại chắc nhất trong số ứng viên — 848/9 đến 26-10-899, có *Asser* và *Anglo-Saxon Chronicle* — và bị cắt vì trần 12 cộng với việc Châu Âu đang ở 26,7%."

**NÊN — "ở Trung Đông cũng vậy" đếm vào danh sách một ứng viên mà khối 6 vừa khai là không phải một con người.**

`reports/ch05-ce09-gate.md` §3.9 dựng danh sách tám người Trung Đông qua cổng, trong đó có "anh em Banū Mūsā". Khối 6 (dòng 994) nói thẳng `Q423210` "không phải `P31 = Q5` mà là một thực thể tập thể". Một thực thể tập thể không thể là "ứng viên qua cổng" của một atlas lập chỉ mục con người. Con số "cũng vậy" vì vậy nên được viết là bảy, hoặc phải kèm chú.

**CÂN NHẮC — "(850)" cho *Gaṇitasārasaṅgraha* viết chặt hơn mức hồ sơ của chính vòng này cho phép.**

`reports/ch05-ce09-gate.md` dòng 88 xếp Mahāvīrācārya `độ tin cậy niên đại: **Thấp**` với lý do "Không có niên đại độc lập; khung duy nhất là triều Amoghavarsha I" (trị vì 814–878). Chapter này viết "k. 850", "k. 870" cho các tác phẩm khác; riêng chỗ này bỏ chữ "k.".

**CÂN NHẮC — "một bước lùi so với `CH05-CE07-08`" đúng, nhưng chỉ ở đúng một phép tính.**

`CH05-CE07-08` là Brahmagupta (`content/ch05.md` dòng 327) ✔. Brahmagupta cũng sai về số không, chỉ sai chỗ khác: ông khẳng định 0 ÷ 0 = 0. "Bước lùi" vì vậy chỉ đúng cho phép chia một số khác không cho không — chỗ Brahmagupta để ngỏ còn Mahāvīrācārya gán cho một giá trị sai. Nói rõ một dòng thì người đọc không hiểu thành "Brahmagupta đã làm đúng".

---

## Khối 9 — **Độ nghiêng lĩnh vực của CE09: hình dạng của thế kỷ, và thiên kiến của người chọn — tách được** (dòng 1002–1003)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **Đếm tay 24 ô lĩnh vực của 12 mục** (`content/ch05.md` dòng 631–845): Tôn giáo/Tâm linh **5** (`-01`, `-03`, `-07`, `-09`, `-10`); Triết học 4; Chính trị/Nhà nước **3** (`-01`, `-08`, `-12`); Văn học 2; Kinh tế 2; Quân sự 2; Toán học, Khám phá/Địa lý, Y học, Ngôn ngữ học, Luật, Sử học mỗi ô 1. Tổng 24. Hai con số "5 trong 24" và "3/24" **đúng**. ✔
- **"toàn atlas ở 23,4%"** khớp `reports/stats.txt` (`Chính trị/Nhà nước 90 23.4%`). ✔ Đáng ghi nhận: `reports/ch05-ce09-gate.md` dòng 769 ghi 24,1% (số trước vòng, 87/361); chapter đã cập nhật sang số sau vòng, đúng hướng.
- **Bảy người bị loại theo nguyên tắc "loại người bảo trợ"** — Harun, al-Maʾmun, Amoghavarsha I, Balaputradeva, Rakai Pikatan, Devapala, ʿAbd al-Raḥmān II — khớp từng tên với `reports/ch05-ce09-gate.md` dòng 769, và cả bảy đều là người cai trị/bảo trợ thế kỷ 9. ✔
- **al-Kindī và al-Farghānī bị loại vì trần 12 và cân vùng** khớp `reports/ch05-ce09-gate.md` dòng 642 và 679. ✔

**BẮT BUỘC — khối nhận 5 ô `Tôn giáo/Tâm linh` rồi chỉ giải thích 4, và ô thứ năm là ô khó giải thích nhất.**

Nguyên văn: *"`Tôn giáo/Tâm linh` chiếm **5 trong 24** ô lĩnh vực của nhóm này, và phần ấy **thuộc về thế kỷ**: thế kỷ 9 đúng là lúc **bốn** truyền thống lớn cùng đóng khung chính điển của mình — ḥadīth Sunni (al-Bukhari), thẩm quyền giáo lý Sunni qua *Miḥna* (Ibn Hanbal), Mật giáo Nhật Bản (Kūkai), siêu hình Latin–Hy Lạp (Eriugena)."*

Ô thứ năm là **`CH05-CE09-01 · Jayavarman II`** (`lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh`). Nó không được kể, và nó **không** khớp mệnh đề đang dùng để biện minh: nghi lễ 802 trên Phnom Kulen là việc **lập** một giáo phái vương quyền, không phải việc **đóng khung một chính điển**. Mà đây đúng là mục mà chính chapter gọi là "mục có bằng chứng yếu nhất nhóm" (dòng 638). Nói "phần ấy thuộc về thế kỷ" cho cả 5 ô trong khi chỉ chứng minh được 4 là đúng loại khai thiếu mà cả mục Ghi chú biên tập này tồn tại để chống.

*Câu thay thế đề nghị:* "`Tôn giáo/Tâm linh` chiếm 5 trong 24 ô lĩnh vực của nhóm này. **Bốn ô thuộc về thế kỷ**: thế kỷ 9 là lúc các truyền thống lớn cùng đóng khung chính điển của mình — ḥadīth Sunni (`CH05-CE09-09`), thẩm quyền giáo lý Sunni qua *Miḥna* (`CH05-CE09-07`), Mật giáo Nhật Bản (`CH05-CE09-03`), siêu hình Latin–Hy Lạp (`CH05-CE09-10`). **Ô thứ năm thì không**: `CH05-CE09-01 · Jayavarman II` được xếp `Tôn giáo/Tâm linh` vì giáo phái vương quyền devarāja, một việc khác loại, và mục ấy cũng là mục bằng chứng yếu nhất nhóm — ghi ra đây để vòng duyệt xét riêng."

**NÊN — "bốn truyền thống lớn" thực ra là ba, và Bối cảnh của chính nhóm này đếm là ba.**

Hai mục đầu danh sách — ḥadīth Sunni và thẩm quyền giáo lý Sunni qua *Miḥna* — nằm trong **cùng một truyền thống**, Hồi giáo Sunni thế kỷ 9 ở Baghdad; tách đôi để đủ con số "bốn" là đếm hai lần. `content/ch05.md` dòng 628 (Bối cảnh của chính nhóm CE09) viết đúng chỗ ấy là **một**: "ḥadīth và luật Sunni ở Baghdad, Mật giáo ở Nhật Bản, siêu hình Latin–Hy Lạp ở Tây Frank" — ba khoản. Hai chỗ trong cùng một file đang đếm khác nhau.
*(Lưu ý kèm: dòng 628 mở đầu bằng chữ "Bốn truyền thống lớn" rồi liệt kê ba khoản — lỗi ấy nằm ngoài phạm vi bảy khối này nhưng nên sửa cùng lúc để hai chỗ khớp nhau.)*

**NÊN — "`Khoa học tự nhiên` và `Giáo dục` bằng 0" bỏ sót ô trống thứ ba, và ô ấy là ô do chính vòng này tạo ra.**

Theo bảng đếm ở trên, `Nghệ thuật/Kiến trúc` của nhóm CE09 cũng **bằng 0**. Và khối 10 ngay bên dưới khai rằng `Nghệ thuật/Kiến trúc` "từng được chọn ở vòng dựng và đã bị bác" cho `CH05-CE09-12` — tức ô ấy trống **vì một quyết định biên tập ghi được ngày tháng**, chính là thứ mà khối này tự nhận có nhiệm vụ khai. Khối nêu hai ô trống mà bỏ ô thứ ba, đúng cái ô có bằng chứng rõ nhất về "lựa chọn của người chọn".
*Câu thay thế đề nghị:* "Hai, **`Khoa học tự nhiên`, `Giáo dục` và `Nghệ thuật/Kiến trúc` đều bằng 0**, và ở đây không có biện hộ."

**NÊN — chỗ dựa "al-Kindī và al-Farghānī" chỉ đỡ được một trong hai ô trống đang nói.**

Nguyên văn: *"`Khoa học tự nhiên` và `Giáo dục` bằng 0, và ở đây không có biện hộ: thế kỷ 9 có al-Kindī và al-Farghānī, vòng này loại họ vì trần 12 và vì cân vùng."* Cả hai người ấy là ứng viên của ô **`Khoa học tự nhiên`** — al-Kindī là nhà triết học – bác học, al-Farghānī là nhà thiên văn. Không ai trong hai người lấp ô **`Giáo dục`**, và khối không nêu được một ứng viên `Giáo dục` nào của thế kỷ 9. Ứng viên `Giáo dục` duy nhất mà cả mục Ghi chú biên tập này nhắc tới là Alcuin (dòng 975), mà chính khối ấy kết luận ông **thuộc CE08**. Vậy ô `Giáo dục` trống hiện chưa được chứng minh là lựa chọn của người chọn — có thể nó đúng là hình dạng của thế kỷ, và khối đang tự nhận một lỗi mà nó chưa chứng minh là lỗi.
*Câu thay thế đề nghị:* "…và ở đây chỉ một trong hai ô có biện hộ rõ: `Khoa học tự nhiên` trống **là lựa chọn của người chọn** — thế kỷ 9 có al-Kindī và al-Farghānī, vòng này loại họ vì trần 12 và vì cân vùng. Với `Giáo dục` thì vòng này **không tìm được ứng viên thế kỷ 9 nào** (ứng viên `Giáo dục` gần nhất, Alcuin, thuộc CE08 — xem khối đầu), nên ô ấy hiện chưa quy được cho bên nào; ghi lại để vòng sau xét."

**CÂN NHẮC — so 3/24 của nhóm với 23,4% của atlas là so một phân số với một tỉ lệ đã gồm chính nhóm ấy.**

23,4% là số **sau** khi CE09 đã nhập vào (90/385, trong đó 3 ô là của CE09). Chênh lệch thật giữa nhóm và phần atlas còn lại lớn hơn con số đang trưng: 87/361 = 24,1% (chính là con số `reports/ch05-ce09-gate.md` dùng). Viết "12,5% so với 24,1% của phần atlas trước vòng này" thì mạnh hơn và chính xác hơn, dù `stats.txt` không in sẵn con số ấy.

---

## Khối 10 — **Ba lựa chọn lĩnh vực của nhóm này tự nhận là có thể bị bác** (dòng 1005–1006)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **Ba nhãn lĩnh vực khớp metadata:** `CH05-CE09-08` = `Chính trị/Nhà nước, Kinh tế` ✔; `CH05-CE09-09` = `Tôn giáo/Tâm linh, Sử học` ✔; `CH05-CE09-12` = `Chính trị/Nhà nước, Quân sự` ✔.
- **`Kinh tế` đúng là ô mỏng, và "tụt lại" đúng về số học.** `reports/stats.txt`: `Kinh tế 8 2.1%`; đổi `CE09-08` sang `Tôn giáo/Tâm linh` thì còn 7/385 = 1,8%, bằng `Kỹ thuật/Công nghệ`. ✔
- **`al-Tārīkh al-kabīr` là phê phán tiểu sử người truyền** — khớp chính mục `CH05-CE09-09` ("Bộ tiểu sử ấy, al-Tārīkh al-kabīr, là một công trình riêng"). ✔
- **"`Nghệ thuật/Kiến trúc` từng được chọn ở vòng dựng và đã bị bác"** — khớp `reports/ch05-ce09-gate.md` dòng 769, mục (iii): hồ sơ cổng đề xuất `Nghệ thuật/Kiến trúc` cho Kʼakʼupakal. ✔
- **Ca (3) kiểm được tới tận bản gốc, và đúng từng khoản.** Tải PDF toàn văn Voss & Kremer qua `ecoyuc.com.mx/scripts/getpdf.php?key=ARTICLEPDF&id=1` (HTTP 200, 1,67 MB; UA `history-atlas/0.1 (research)`). Bài có hẳn một tiết mang tên **"1.2.4. The k'ul ah ts'ul wahob – The military aspect"**, mở đầu nguyên văn: *"K'ak'-u-pakal's role as military commander can be deduced from the inscriptions of Chichén Itzá as well. The decisive textual information derives from the inscriptions of lintels 1 and 4 of the Temple of the Four Lintels and block no.12 of the Hieroglyphic Serpents from the Caracol."* Đoạn tiếp theo mô tả sự kiện ngày 9–10 tháng 7 năm 881 trên rầm 4, trong đó `k'ul ah ts'ul wahob` Kʼakʼupakal dự một sự kiện về **tokʼ-pakal**, và ghi rằng tokʼ-pakal (flint-shield) là vật gắn với lễ đăng vị và **chiến tranh**. Cả ba khoản bằng chứng khối nêu — rầm 1 và 4, khối 12 Caracol, quan hệ `kʼul ah tsʼul wah` ↔ `tokʼ-pakal` — **có thật, đúng nguồn, và đúng chiều luận điểm** (quy tắc 7 sạch). ✔
- Nhân tiện: con số "57 người nam và 7 người nữ" ở mục `CH05-CE09-12` cũng khớp nguyên văn bài báo. ✔

**BẮT BUỘC — ca (2): "lý do không chọn là ông không lập madhhab" là một tiêu chí không tồn tại trong atlas này, và nó bị chính atlas bác bằng 20 mục.**

Nguyên văn: *"(2) `CH05-CE09-09 · Al-Bukhari` ghi **`Sử học`** … lựa chọn thay thế là `Luật`, và **lý do không chọn là ông không lập madhhab** — vai ấy trong nhóm này đã thuộc `CH05-CE09-07`."*

Hai chỗ hỏng, và khối tự mời người đọc bác nên tôi bác thẳng:

1. **Lập madhhab chưa bao giờ là điều kiện của ô `Luật`.** `reports/stats.txt` cho `Luật` **20 người**. `grep` metadata toàn bộ `content/`: Hammurabi (`ch01` dòng 8), Hattusili III (`ch01` 335), Lycurgus (`ch01` 607), Draco (`ch02` 214), Solon (`ch02` 422), Thương Ưởng (`ch03` 97), Hàn Phi (`ch03` 302), Tiberius Gracchus (`ch03` 560), Cicero (`ch03` 664), Tertullianus (`ch04` 357), Leo I (`ch04` 836), Theodosius II (`ch04` 884), Justinianus I (`ch05` 8), Tùy Văn Đế (`ch05` 93), ʿUmar (`ch05` 230) — **không ai trong số này lập một madhhab**, và nhiều người còn không ở trong thế giới Hồi giáo. Lấy một điều kiện mà 15/20 mục `Luật` của chính atlas không thoả làm lý do loại là dựng một tiêu chí cho riêng ca này.
2. **"Vai ấy trong nhóm này đã thuộc người khác" cũng không phải một nguyên tắc của nhóm này.** Chính nhóm CE09 có **5 người cùng ô `Tôn giáo/Tâm linh`** và **4 người cùng ô `Triết học`**. Nếu trùng ô là lý do loại thì bốn trong năm ô `Tôn giáo/Tâm linh` phải bị loại trước.

Lý do thật sự đứng được đã nằm sẵn trong mục `CH05-CE09-09`: cái được chỉ mục ở đây là **thao tác phê phán nguồn**, và ô `Sử học` mô tả thao tác ấy sát hơn ô `Luật`.

*Câu thay thế đề nghị:* "(2) `CH05-CE09-09 · Al-Bukhari` ghi **`Sử học`** vì *al-Tārīkh al-kabīr* của ông là phê phán tiểu sử người truyền, cùng loại thao tác với sử học — tức ô này mô tả **cách ông làm việc**, không mô tả lĩnh vực mà kết quả của ông được dùng. Lựa chọn thay thế là `Luật`, và nó không yếu: *al-Jāmiʿ al-Ṣaḥīḥ* được sắp theo đề mục pháp lý, còn `Luật` trong atlas này chưa bao giờ đòi người giữ ô phải lập một trường phái — 15 trong 20 mục `Luật` hiện có không lập trường phái nào. Nếu vòng duyệt đổi, nhóm này chấp nhận; cái mất khi ấy là chỗ duy nhất trong CE09 ghi nhận phê phán nguồn như một thao tác."

**NÊN — ca (3): "các văn bản nêu tên ông **đều** là lễ khoan lửa và hiến cúng công trình" bị chính bài Voss & Kremer bác.**

Theo bản PDF toàn văn vừa tải, các sự kiện mà bài quy cho Kʼakʼupakal gồm: **lễ khánh thành sân bóng** trên khối điêu khắc bán cầu từ Great Ballcourt (14-11-864); một **vision quest** ở văn bản Casa Colorada (11-9-869); một **sự kiện sân bóng** ở Yula Lintel 1 (03-01-874); và sự kiện **tokʼ-pakal** ở Đền Bốn Rầm (09–10-7-881). Bài có nói ông gắn với "the fire ceremonies" qua chức danh, nhưng không ở đâu nói các văn bản nêu tên ông **đều** là lễ khoan lửa và hiến cúng công trình. Chữ "đều" làm lựa chọn thay thế (`Tôn giáo/Tâm linh`) trông mạnh hơn thực tế, tức khối đang tự dựng một đối thủ sai cho chính mình.
*Câu thay thế đề nghị:* "…lựa chọn thay thế là `Tôn giáo/Tâm linh`, vì phần lớn văn bản nêu tên ông mô tả ông trong vai người chủ trì nghi lễ — khánh thành sân bóng (864), vision quest ở Casa Colorada (869), sự kiện sân bóng ở Yula (874)."

**NÊN — ca (1) dựng một lựa chọn thay thế yếu rồi tự nhận là "hợp lý", làm phép tự-bác mất giá trị.**

Nguyên văn: *"lựa chọn thay thế hợp lý là `Tôn giáo/Tâm linh`, vương quyền Kitô giáo Nubia."* Nhưng ô thứ nhất của mục đã là `Chính trị/Nhà nước`, nên phần "vương quyền" đã được ghi; phần `Tôn giáo/Tâm linh` chỉ thêm tính từ "Kitô giáo", mà toàn bộ đoạn "Tư tưởng / đóng góp chính" của `CH05-CE09-08` không có một câu nào về giáo lý, phụng tự hay tổ chức giáo hội — nó nói về baqt từ đầu tới cuối. Đây không phải một lựa chọn thay thế ngang ngửa; gọi nó là "hợp lý" làm loãng chính cơ chế tự-bác mà khối đang dựng. Nếu có một lựa chọn thay thế thật thì nó là `Chính trị/Nhà nước` + **`Khám phá/Địa lý`** hoặc `Quân sự` — và nếu không có cái nào, nên nói thẳng là `Kinh tế` không có đối thủ.

**CÂN NHẮC — chỉ một trong ba mục tự khai "có thể bị bác" ở ngay thân mục.**

`CH05-CE09-09` viết hẳn trong "Vì sao chọn": "đó là một lựa chọn có thể bị bác". `CH05-CE09-08` và `CH05-CE09-12` thì chỉ nêu lý do chọn, không nêu rằng lựa chọn ấy đang tự nhận có thể sai. Người đọc chapter mà không đọc tới `## Ghi chú biên tập` sẽ thấy ba mức tự tin khác nhau cho ba quyết định mà khối này xếp ngang hàng.

---

## Khối 11 — **Một ghi chú về ʻAhoʻeitu, bổ sung cho khối Châu Đại Dương của vòng CE08** (dòng 1008–1009)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **"Khối CE08 đã dựng ba tầng lý do"** ✔ — `content/ch05.md` dòng 967 dựng đúng ba tầng: (1) Đông Polynesia chưa có cư dân (Wilmshurst et al., *PNAS* 2011); (2) không có hệ chữ viết trước tiếp xúc châu Âu; (3) Tây Polynesia/Melanesia/Micronesia có người ở nhưng tên người truyền khẩu, chỉ chép thành văn từ thế kỷ 19.
- **ʻAhoʻeitu là Tuʻi Tonga đầu tiên** ✔ — bài *Tuʻi Tonga* trên en.wikipedia: dòng vua này "originated in the tenth century with the mythical ʻAhoʻeitu".
- **Con của thần bầu trời Tangaloa** ✔ — bài *ʻAhoʻeitu* gọi cha ông là "the sky-god, Tangaloa 'Eitumatupu'a"; mô tả tiếng Anh của Wikidata `Q1245849` cũng là "son of the god Tangaloa ʻEitumātupuʻa and a mortal woman". (Tên đầy đủ của vị thần là **Tangaloa ʻEitumātupuʻa**; viết trần "Tangaloa" là một họ thần, nên ghi đủ tên thì chặt hơn.)
- **Bị anh em giết rồi hồi sinh** ✔ — bài en.wikipedia có hẳn tiết "Sibling treachery and murder": các anh cùng cha khác mẹ ghen tị và giết ông bằng lao trong trò sika-ʻulu-toa.
- **Thuộc CE10, không thuộc CE09** ✔ — cả hai bài đều đặt ông ở thế kỷ 10.

**BẮT BUỘC — "một nhân vật thần thoại, cùng loại đã bị atlas từ chối ở các chapter trước" là sai: atlas chưa từng từ chối loại này, atlas có hẳn một nhãn dành cho nó.**

Nguyên văn: *"trong chính truyền thống ấy ông là **con của thần bầu trời Tangaloa**, bị anh em giết rồi hồi sinh — một nhân vật thần thoại, **cùng loại đã bị atlas từ chối ở các chapter trước**."*

`content/ch01.md` dòng 634 tổng kết chính sách của atlas bằng một câu: *"Năm mục mang nhãn **[Truyền thuyết]** (Abraham, Moses, Viśvāmitra, Vasiṣṭha, Lycurgus) và bốn mang **[Tranh cãi lịch sử]** (Thành Thang, David, Solomon, Elijah)."* Tức atlas **nhận** nhân vật truyền thuyết, có nhãn riêng cho họ, và đã dùng nhãn ấy năm lần — `CH01-BCE14_12-08 · Moses [Truyền thuyết]` (`năm: k. 1393–1273 TCN **theo niên đại truyền thống**`), `CH01-BCE11_9-12 · Lycurgus xứ Sparta [Truyền thuyết]` (`hoạt động k. 900–820 TCN **theo truyền thống**`) và ba mục khác. Nhãn `[Tranh cãi lịch sử]` thì còn được dùng thêm ở `ch02` (Homer, Lão Tử, Zarathustra, Yajnavalkya, Baudhāyana, Isaiah) và `ch04` (Trương Đạo Lăng).

Hệ quả: **lý do thứ hai của khối sụp**, và cùng với nó sụp cả câu "ông thất bại hai lần độc lập". Tính thần thoại trong atlas này không phải lý do loại, nó là lý do **gắn nhãn**.

Có một lý do thứ hai thật, cứng hơn, và máy kiểm được — khối không nêu: **Wikidata `Q1245849` có `P31 = Q6949213` ("mythological king"), không phải `Q5`** (tra `wbgetentities`, UA `history-atlas/0.1 (research)`). Theo đúng phép kiểm mà khối 4 của cùng mục Ghi chú biên tập này mô tả (dòng 988: lint kiểm `wikidata:` tồn tại và có `P31 = Q5`), một mục cho ông sẽ **không qua được lint** — cùng hình dạng với ca `Q423210` Banū Mūsā ở khối 6, và ngược hình dạng với ca `Q6771941` ở khối 12.

*Câu thay thế đề nghị:* "Chỉ thêm một dữ kiện mà vòng ấy chưa nêu: **ʻAhoʻeitu**, vị Tuʻi Tonga đầu tiên, là ứng viên gần nhất có thể phá thế trống, và ông **thất bại hai lần độc lập**. Niên đại truyền thống đặt ông ở thế kỷ 10, tức thuộc CE10 chứ không thuộc nhóm này. Và Wikidata `Q1245849` khai `P31 = Q6949213` — "mythological king" — **không phải `Q5`**, nên một mục cho ông sẽ không qua được phép kiểm `P31 = Q5` của lint; đây là cùng hình dạng với ca Banū Mūsā ở trên. Tính truyền thuyết tự nó **không** phải lý do loại — atlas có nhãn `[Truyền thuyết]` và đã dùng năm lần (`content/ch01.md` dòng 634) — nên đừng viện nó. Hai lý do trên thì độc lập nhau: chữa được cái thứ nhất cũng không chữa được cái thứ hai."

**NÊN — "thất bại hai lần" đếm thiếu một tầng mà chính khối vừa nói là không sửa.**

Khối mở đầu bằng "vòng CE09 **không sửa tầng nào**" của khối CE08. Nhưng Tonga nằm ở **Tây Polynesia**, đúng phạm vi tầng (3) của khối ấy — "tên người ở đó truyền qua gia phả truyền khẩu, chỉ được chép thành văn từ thế kỷ 19 — khoảng cách hơn một nghìn năm". Tầng (3) một mình đã đủ loại ʻAhoʻeitu, và nó độc lập với cả niên đại lẫn tính truyền thuyết. Khối vừa khẳng định ba tầng còn nguyên, vừa đếm ca này chỉ hỏng hai lần.
*Câu thay thế đề nghị (thêm một câu cuối):* "Và tầng (3) của khối CE08 vẫn áp lên ông nguyên vẹn: Tonga thuộc Tây Polynesia, nơi tên người truyền qua gia phả truyền khẩu và chỉ được chép thành văn từ thế kỷ 19 — nên dù chữa được hai lý do trên thì vẫn còn lý do ấy."

**CÂN NHẮC — con số "khoảng 950" không khớp nguồn tra được, dù kết luận không đổi.**

Bài *ʻAhoʻeitu* trên en.wikipedia viết ông lên ngôi "in the **early** 10th century"; bài *Tuʻi Tonga* chỉ viết "the tenth century". Con số **950** mà khối dùng **[KHÔNG KIỂM ĐƯỢC]** — tôi không tìm được nguồn nào trong tầm tra của vòng này nói đúng 950. Vì cả hai cách đọc đều rơi vào 901–1000, kết luận "thuộc CE10" không đổi; nhưng con số nên viết là "thế kỷ 10" thay vì "khoảng 950", hoặc phải kèm nguồn.

---

## Khối 12 — **Ứng viên Việt Nam trong nhóm CE09 (yêu cầu D5)** (dòng 1011–1012)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **Yêu cầu D5 được thoả.** `README.md` dòng 77 liệt "Ghi chú biên tập không nhắc ứng viên Việt Nam (D5)" là một cảnh báo lint; khối có mặt và nêu đích danh ba người. ✔
- **Dương Thanh, 819, Tống Bình, Lý Tượng Cổ, "gần một năm"** — bài *Khởi nghĩa Dương Thanh* trên vi.wikipedia: năm 819 ông được giao 3.000 quân đi đánh Hoàng Động, quay lại đánh chiếm phủ thành Tống Bình, "giết chết quan đô hộ Lý Tượng Cổ", và "đã giành độc lập trong khoảng gần một năm". ✔
- **"820/828?" có thật và đúng nguyên văn** — câu mở đầu bài ấy là "Dương Thanh (771 - 820/828?)". ✔
- **Lỗi `Q6771941`** — tra `wbgetentities` (UA `history-atlas/0.1 (research)`): nhãn duy nhất là nhãn tiếng Việt "Khởi nghĩa Dương Thanh", **không có nhãn tiếng Anh**, và `P31 = Q5`. ✔
- **"không có thực thể nào là con người Dương Thanh"** — `wbsearchentities` với "Dương Thanh" (vi) trả về mười kết quả, không kết quả nào là người thế kỷ 9 này. ✔ (Trong tầm tra của vòng này; một thực thể không có nhãn Việt–Anh thì phép tra này không thấy.)
- **Cao Biền `Q5521624`** — `wbgetentities`: nhãn vi "Cao Biền", en "Gao Pian", `P31 = Q5`, `P569 +0821`, `P570 +0887-09-24`. ✔ Bài *Gao Pian* trên en.wikipedia: năm 866 Đường Ý Tông lập **Tĩnh Hải quân (Jinghai Circuit)** và cử ông làm tiết độ sứ, sau đó ông "rebuilt Jiaozhi's defenses"; ông chết ở Hoài Nam, trị sở **Dương Châu**, năm 887. ✔ Bài 高駢 trên zh.wikipedia: "燕人。祖先為渤海郡人，遷居幽州" và "出身渤海高氏，遷居幽州（今北京）后，七世合居" — tức dòng họ đã ở **U Châu** bảy đời. ✔
- **Khúc Thừa Dụ `Q1001807`: `P569` ghi `+0801-01-01` ở `precision` 7** — kiểm trực tiếp, **đúng từng chữ**; `P570 +0907` ở precision 9. Cảnh báo "người viết CE10 không được chép" là một cảnh báo thật và đúng. ✔
- **Quy tắc 6 sạch.** `grep` `content/*.md`: Dương Thanh, Cao Biền, Khúc Thừa Dụ **không có mục riêng ở bất kỳ chapter nào**, kể cả `ch90`. ✔

**BẮT BUỘC — lý do loại Cao Biền khỏi phụ lục dựa vào một "định nghĩa của phụ lục" mà `content/ch90.md` không có, và phụ lục ấy đã nhận hai người cùng loại.**

Nguyên văn: *"nhưng ông sinh ở U Châu, mất ở Dương Châu, và sự nghiệp của ông là sự nghiệp một tướng nhà Đường: **đưa ông vào phụ lục Việt Nam sẽ làm hỏng định nghĩa của chính phụ lục ấy**."*

Định nghĩa thật nằm ở `content/ch90.md` dòng 3: *"Phụ lục này dùng chung bốn tiêu chí (a)–(d) của atlas, nhưng đổi **hệ quy chiếu**: ảnh hưởng được **đo trong phạm vi Việt Nam và Đông Nam Á**, không phải toàn nhân loại."* Đó là một tiêu chí về **thước đo ảnh hưởng**, không phải về nguồn gốc hay quốc tịch của nhân vật. Và phụ lục đã nhận đúng hai người mà lập luận này sẽ loại:

- `CH90-BCE03_01-02 · Triệu Đà` — "Viên quan nhà Tần", `nơi: Phiên Ngung, Nam Việt, **nay thuộc Quảng Châu, Trung Quốc**", người **thôn tính** Âu Lạc.
- `CH90-CE01_09-03 · Sĩ Nhiếp` — Thái thú Giao Chỉ của nhà Hán, `năm: 137–226`.

Theo chính thước đo ấy, Cao Biền đạt: khối vừa tự nhận việc ông làm là "một quyết định quy hoạch **có hệ quả nghìn năm**" trong phạm vi Việt Nam — đúng loại ảnh hưởng mà phụ lục đo. Lập luận hiện tại vì vậy không loại được ông, và nó còn kéo theo hệ quả cho khối 13 ngay bên dưới (vốn đề cử Dương Thanh làm "ứng viên số một" để lấp khoảng trống thế kỷ 9 của phụ lục).

*Câu thay thế đề nghị:* "**Cao Biền** `Q5521624` cho Tĩnh Hải quân và việc đắp lại thành Đại La năm 866 — một quyết định quy hoạch có hệ quả nghìn năm — nhưng ở atlas chính ông yếu ở (c): cái nguyên bản ở đây là một quyết định chọn vị trí, không phải một tư tưởng hay một phương pháp, và công trạng quân sự của ông là công trạng dẹp Nam Chiếu cho nhà Đường. Với **phụ lục** thì khác: theo hệ quy chiếu của `content/ch90.md` (ảnh hưởng đo trong phạm vi Việt Nam), ông là ứng viên đứng được — phụ lục đã nhận Triệu Đà và Sĩ Nhiếp theo đúng hệ quy chiếu ấy. Vòng này **không** xét ông cho phụ lục; việc đó thuộc P4, xem khối dưới."

**BẮT BUỘC — hai lý do loại Dương Thanh rút từ cùng một nguồn và chúng loại trừ nhau.**

Nguyên văn: *"bị loại vì cuộc khởi nghĩa **bị dập trong vòng một năm** và không đổi cấu trúc An Nam đô hộ phủ, tức yếu ở (b) và (d), **và** vì năm mất ghi "820/828?" — biên độ tám năm **kèm dấu hỏi** ngay trong nguồn."*

Biên độ "820/828?" **có** từ nguồn, nhưng nó có vì một lý do cụ thể, và lý do ấy chính là phủ định của vế đầu. Bài *Khởi nghĩa Dương Thanh* trên vi.wikipedia chép: *"theo Đại Việt sử ký toàn thư thì Dương Thanh không bị Quế Trọng Vũ giết chết mà vượt ngục, còn sống đến năm 828"*, rồi liệt ba viên An Nam đô hộ kế tiếp — Bùi Hành Lập (820), Vương Thừa Điển (822), Lý Nguyên Hỷ (822) — "đánh Dương Thanh nhưng vẫn không thắng", và ghi ông "lại vào trong người Man Lạo làm loạn, cướp phá phủ thành những năm 822–826". Tức: **nếu nhận con số 828 thì cuộc chống cự kéo gần một thập kỷ, không phải "bị dập trong vòng một năm"; còn nếu nhận 820 thì không còn biên độ tám năm để nói.** Khối lấy nửa này của nguồn để dựng biên độ niên đại và nửa kia để dựng lý do (b), trong khi hai nửa ấy là hai giả thuyết cạnh tranh.

*Câu thay thế đề nghị:* "**Dương Thanh**, người năm 819 quay quân đánh chiếm Tống Bình và giết An Nam đô hộ Lý Tượng Cổ, chiếm Giao Châu gần một năm: bị loại vì niên đại không chốt được và vì chính chỗ không chốt ấy làm hỏng cả phần đánh giá. Nguồn tiếng Việt thông dụng ghi "771 – 820/828?", và biên độ tám năm kèm dấu hỏi ấy **là hai giả thuyết khác nhau về chính sự nghiệp của ông**: một bên là bị Quế Trọng Vũ bắt giết đầu năm 820, bên kia là *Đại Việt sử ký toàn thư* chép ông vượt ngục và còn chống cự tới 828. Chừng nào chưa quyết được giữa hai bản, atlas không đánh giá được ông theo (b) hay (d) — nên lý do loại phải ghi là **chưa quyết được**, không phải "bị dập trong một năm"."

**NÊN — "không đổi cấu trúc An Nam đô hộ phủ" bị chính nguồn ấy bác một nửa.**

Cùng bài trên: *"Năm 824, Lý Nguyên Hỷ **dời phủ trị vào huyện Long Đỗ, Tô Lịch, đắp một cái thành nhỏ, gọi là La Thành**"*. Trị sở của An Nam đô hộ phủ dời khỏi Tống Bình sau cuộc nổi dậy, tới đúng vị trí mà Cao Biền đắp lại thành Đại La năm 866 — ứng viên thứ hai của chính khối này. Quan hệ **nhân quả** giữa cuộc nổi dậy và việc dời trị sở thì **[KHÔNG KIỂM ĐƯỢC]** từ các nguồn tôi mở được; nhưng mệnh đề "không đổi cấu trúc" như đang viết là một mệnh đề quá mạnh so với nguồn.

**NÊN — "ngay trong nguồn" không nói nguồn nào, và nó không phải Wikidata.**

Khối đặt câu "biên độ tám năm kèm dấu hỏi ngay trong nguồn" sát ngay câu về `Q6771941`, nên người đọc dễ hiểu con số đến từ Wikidata. Thực tế `Q6771941` **không có `P570` nào cả** (chỉ có `P569 +0750` ở precision 7 — tức "thế kỷ 8", một giá trị độn cùng loại với ca Khúc Thừa Dụ mà khối nêu ở câu sau). Nguồn thật của "820/828?" là câu mở đầu bài *Khởi nghĩa Dương Thanh* trên vi.wikipedia. `CONTRIBUTING.md` yêu cầu phản hồi và mệnh đề phải kèm nguồn; chỗ này nên nêu tên.
*Câu thay thế đề nghị (thêm vào cuối câu Wikidata):* "…mà `P31` lại là `Q5`; thực thể ấy còn **không có `P570`** nào, nên biên độ "820/828?" không đến từ Wikidata mà từ truyền thống sử liệu Việt (xem câu trên), và `P569` của nó là `+0750` ở `precision` 7 — lại một giá trị độn thế kỷ."

**NÊN — "đô hộ sứ" không phải chức danh có thật.**

Chức của Lý Tượng Cổ là **An Nam đô hộ** (都護). Cả vi.wikipedia ("Viên đô hộ An Nam là Lý Tượng Cổ", "quan đô hộ Lý Tượng Cổ") lẫn mạch văn các viên kế nhiệm trong cùng bài đều dùng "An Nam đô hộ". "Đô hộ sứ" trộn hai chức danh khác nhau; trong một khối đang dạy cách đọc nhãn cho đúng thì nên viết đúng.

**NÊN — Cao Biền bị chấm trên đúng một tiêu chí, trong khi câu trước đó vừa cho ông điểm ở hai tiêu chí khác.**

Nguyên văn: *"một quyết định quy hoạch **có hệ quả nghìn năm** … còn ở atlas chính thì ông yếu ở **(c)**, vì đắp thành là thi công."* "Hệ quả nghìn năm" là mệnh đề về **(b) độ bền** và **(d) counterfactual** — hai tiêu chí mà câu này không chấm. Và "đắp thành là thi công" mâu thuẫn với chính nửa câu trước: khối vừa gọi đó là **một quyết định quy hoạch**, không phải việc thi công. Nếu kết luận là loại, phải nói vì sao (c) thắng (b) và (d), hoặc đổi lý do.

**CÂN NHẮC — Phùng Hưng không được nhắc, và chuyện ấy đúng, nhưng còn một việc nên nhắc.**

Phùng Hưng có mục riêng (`CH90-CE01_09-07`, `năm: hoạt động k. 766–791`), nằm ngoài khung 801–900, nên **không** phải ứng viên bị loại của CE09 và việc khối im lặng về ông là đúng quy tắc 6. Nhưng chính mục ấy, ở `content/ch90.md` dòng 142, đã viết: *"Ứng viên cùng giai đoạn là **Dương Thanh**, nổi dậy năm 819, và **Khúc Thừa Dụ** đầu thế kỷ 10."* Tức hai trong ba cái tên của khối này đã được phụ lục xét và loại một lần rồi. `CONTRIBUTING.md` quy tắc 6 khuyên nói rõ quan hệ ấy thay vì để vòng sau phát hiện lại; một câu trỏ sang `CH90-CE01_09-07` sẽ tiết kiệm đúng một vòng rà.

---

## Khối 13 — **Một khoảng trống trong chính phụ lục Việt Nam, ghi lại cho P4** + **Một liên kết tự do được nâng thành ID, và vì sao điều đó đáng ghi** (dòng 1014–1018)

**Đã kiểm được (không có phát hiện ở các chỗ này):**

- **Khoảng trống thể thức có thật.** `grep '^### CH90-'`: `content/ch90.md` đi từ `CH90-CE01_09-08 · Khương Công Phụ` (dòng 153) thẳng tới `CH90-CE10_14-01 · Ngô Quyền` (dòng 171). ✔
- **Niên đại hai mốc đúng.** Khương Công Phụ: `năm: 731–805`. Ngô Quyền: 938. ✔
- **Lịch sử liên kết Brahmagupta — xác minh được chính xác bằng `git`.** Commit `db07f09` ("ch05: thêm nhóm CE09 (12 mục, TK 9) và ghi chú biên tập") trong cùng một diff đã **xoá** dòng `- al-Khwārizmī và toán học Ả Rập · kế thừa · qua trường phái` và **thêm** `- CH05-CE09-04 · kế thừa · qua trường phái`. Mệnh đề "trước đây ghi dưới dạng văn bản tự do… khi `CH05-CE09-04` ra đời, dòng ấy được đổi thành ID" đúng từng chữ. ✔
- **Thao tác bảo trì ấy đã làm đủ cho vòng CE09.** Tôi chạy đúng phép `grep` mà khối khuyến nghị — rà cả 12 tên CE09 (Jayavarman II, Hàn Dũ, Kūkai, al-Khwārizmī, Trương Bảo Cao, Hunayn ibn Ishaq, Ahmad ibn Hanbal, Georgios I, al-Bukhārī, Eriugena, Anandavardhana, Kʼakʼupakal) trên toàn bộ `content/*.md`, lọc các dòng quan hệ không trỏ ID. **Không còn đích tự do nào mang tên một trong 12 người.** Kết quả duy nhất là `content/ch05.md` dòng 751, `- Trường phái luật Hanbalī, một trong bốn madhhab Sunni · kế thừa · trực tiếp` — đích là một trường phái, không phải một mục nhân vật, nên hợp lệ. ✔

**BẮT BUỘC — lý do giải thích khoảng trống sai, và `content/ch90.md` bác nó ở ngay dòng tiêu đề nhóm.**

Nguyên văn: *"**Thế kỷ 9 là một khoảng trống trong chính phụ lục Việt Nam** — không phải vì ai bỏ sót, mà vì **nhóm `CE01_09` kết thúc đúng ở đầu thế kỷ 9**."*

Nhóm không kết thúc ở đầu thế kỷ 9. `content/ch90.md` dòng 39 ghi tiêu đề nhóm nguyên văn: **`## Nhóm CE01_09 · TK 1–9 (1 – 900)`**. Khung nhóm chạy hết năm 900, tức **toàn bộ thế kỷ 9 nằm trong khung** — chính ID `CE01_09` nói thế. Ba chứng cứ nữa cùng hướng:

1. Mục cuối nhóm, `CH90-CE01_09-08 · Khương Công Phụ`, có `năm: 731–805` — một người **mất trong thế kỷ 9**, đã nằm trong nhóm. Nên không phải khung chặn.
2. Nhóm mới dùng **8 trên 12** chỗ. Trần 12 không chặn.
3. Khoảng trống là **một lựa chọn biên tập đã được ghi lại**: `content/ch90.md` dòng 142, phần "Vì sao chọn" của `CH90-CE01_09-07 · Phùng Hưng`, viết *"Ứng viên cùng giai đoạn là **Dương Thanh, nổi dậy năm 819**, và Khúc Thừa Dụ đầu thế kỷ 10."* Tức người soạn phụ lục **đã xét Dương Thanh và đã không lấy**.

Như đang viết, câu này còn tự mâu thuẫn: nếu khung nhóm thật sự chặn ở đầu thế kỷ 9 thì không có khoảng trống nào để P4 lấp, và đề nghị "ứng viên số một là Dương Thanh" ở câu sau trở thành vô nghĩa.

*Câu thay thế đề nghị:* "**Thế kỷ 9 là một khoảng trống trong chính phụ lục Việt Nam** — và không phải vì khung nhóm: `content/ch90.md` dòng 39 ghi `## Nhóm CE01_09 · TK 1–9 (1 – 900)`, tức cả thế kỷ 9 nằm trong khung, nhóm mới dùng 8/12 chỗ, và mục cuối nhóm (Khương Công Phụ, 731–805) đã mất trong thế kỷ ấy. Khoảng trống là một **lựa chọn đã ghi**: mục `CH90-CE01_09-07 · Phùng Hưng` nêu Dương Thanh làm ứng viên cùng giai đoạn rồi chọn Phùng Hưng. Nếu P4 muốn xét lại, điểm vào là chính dòng ấy."

**BẮT BUỘC — "những quan hệ có thật nhưng không đếm được" sai: chúng được đếm đủ.**

Nguyên văn: *"nếu không, atlas sẽ tích dần những quan hệ **có thật nhưng không đếm được**."*

Đếm được hết. Tôi đối chiếu số dòng quan hệ trong `content/` với `reports/stats.txt`:

| chapter | dòng quan hệ | trong đó trỏ ID | đích tự do | `stats.txt` [chXX] Loại quan hệ, cộng lại |
|---|---|---|---|---|
| ch01 | 100 | 51 | 49 | 94 + 6 = **100** |
| ch03 | 188 | 118 | 70 | 171 + 13 + 4 = **188** |
| ch04 | 214 | 124 | 90 | 201 + 13 = **214** |
| ch05 | 206 | 65 | 141 | 185 + 16 + 5 = **206** |

Tổng trong `stats.txt` khớp với **toàn bộ** dòng quan hệ, không phải chỉ phần trỏ ID — ở ch05 là 206 chứ không phải 65. Đích tự do vào thống kê như mọi dòng khác. Cái chúng **không** làm được là chuyện khác và quan trọng hơn: chúng không **giải được về một mục**, nên không sinh cạnh hai chiều, không duyệt được như đồ thị, và không vào được phép kiểm ID của lint. Viết là "không đếm được" sẽ khiến vòng sau đi tìm sai chỗ — tìm trong `stats.txt`, nơi mọi con số đều đã đúng.

*Câu thay thế đề nghị:* "Hệ quả cho các vòng sau: mỗi khi thêm một nhóm mới, phải `grep` tên những người vừa thêm trong toàn bộ `content/` để tìm các đích tự do cần nâng cấp. Các đích tự do **vẫn vào thống kê** — `reports/stats.txt` đếm chúng đủ, ở ch05 là 206 dòng quan hệ trong khi chỉ 65 dòng trỏ ID. Cái mất không phải con số mà là **cạnh**: một đích tự do không giải được về mục nào, nên không sinh quan hệ hai chiều, không duyệt được như đồ thị, và nằm ngoài tầm phép kiểm ID của lint."

**NÊN — khoảng trống này không phải phát hiện mới; `content/ch90.md` đã mở một mục tồn đọng chồng lên nó.**

Nguyên văn: *"Kiểm quy tắc 6 cho khối trên **làm lộ ra một việc khác**."*

Ghi chú biên tập của chính phụ lục, `content/ch90.md` dòng 711, đã ghi: *"bốn mục chưa đạt thể thức 'Vì sao chọn' của §5: … **Lê Thánh Tông và Phùng Hưng nêu người không thật sự cùng thời**. Ghi ra đây thay vì vá vội, để lần rà sau xử lý đúng mức."* Mục Phùng Hưng ấy chính là nơi Dương Thanh (819) và Khúc Thừa Dụ (thế kỷ 10) được nêu. Hai việc — "sửa danh sách ứng viên của Phùng Hưng" và "lấp thế kỷ 9" — là một chỗ. Nếu khối ghi như một phát hiện mới, P4 sẽ mở hai phiếu cho một vấn đề.

**NÊN — khối 12 và khối 13 ràng vào nhau, và chiều ràng ngược không được ghi.**

Khối 13 đề nghị P4 thêm Dương Thanh vào `ch90`. Nhưng khối 12 ngay trên nêu đích danh Dương Thanh làm **ứng viên bị loại** của CE09. Theo quy tắc 6, ngày P4 cho ông một mục ở `ch90` thì câu ấy trong `content/ch05.md` thành vi phạm và phải sửa (thành dạng "có mục riêng ở `CH90-…`"). Câu "Việc này **không** thuộc vòng CE09 và không được làm lẫn vào đây" đúng về phạm vi nhưng bỏ mất ràng buộc ngược — nên ghi thêm một vế để P4 không để lại lỗi ở chapter này.

**NÊN — một ca sống mà chính khối này bỏ sót, nằm ngay trong tệp nó vừa đọc.**

`content/ch90.md` dòng 148, phần "Ảnh hưởng tới" của `CH90-CE01_09-07 · Phùng Hưng`: **`- Khúc Thừa Dụ · kế thừa · qua trường phái`** — một đích tự do mang tên **một con người**, và khối 12 ngay trên vừa kết luận Khúc Thừa Dụ thuộc CE10. Nghĩa là đúng cái bẫy khối này mô tả đang chờ sẵn ở vòng CE10. Khối nêu được quy tắc nhưng không nêu được ca sống đã có; thêm một câu trỏ vào dòng ấy sẽ làm lời cảnh báo có răng.

**CÂN NHẮC — "lint không nhắc được" đúng với lint hiện tại, không đúng về nguyên tắc; và phép `grep` theo chiều đang đề nghị không co giãn được.**

Khối kê quy trình thủ công: mỗi vòng, `grep` tên người mới trên toàn `content/`. Chiều ngược rẻ hơn và bắt được nhiều hơn: rút **danh sách đích tự do** (ở ch05 là 141 dòng) rồi đối chiếu một lượt với chỉ mục tiêu đề mục — cách này còn bắt được những đích tự do có từ các vòng trước mà không nhóm mới nào gợi ra. Và vì phép đối chiếu ấy là cơ học, nó **làm được trong lint** dưới dạng cảnh báo (không phải lỗi chặn, vì đích tự do hợp lệ như `Trường phái luật Hanbalī` ở `content/ch05.md` dòng 751 phải được phép tồn tại). Nếu owner đồng ý, câu "lint không nhắc được" nên đổi thành "lint **hiện chưa** nhắc" kèm đề nghị thêm cảnh báo — khác nhau ở chỗ một bên đóng cửa, một bên mở một việc làm được.

---

## Tổng kết

| Khối | Nội dung | BẮT BUỘC | NÊN | CÂN NHẮC |
|---|---|---|---|---|
| 7 | Độ nghiêng vùng không sửa được ở tầng chọn người của một thế kỷ | 1 | 2 | 1 |
| 8 | Châu Âu 1/12 và Trung Đông 3/12 là cắt có chủ ý, không phải khan ứng viên | 2 | 3 | 2 |
| 9 | Độ nghiêng lĩnh vực của CE09: hình dạng của thế kỷ, và thiên kiến của người chọn | 1 | 3 | 1 |
| 10 | Ba lựa chọn lĩnh vực của nhóm này tự nhận là có thể bị bác | 1 | 2 | 1 |
| 11 | Một ghi chú về ʻAhoʻeitu, bổ sung cho khối Châu Đại Dương của vòng CE08 | 1 | 1 | 1 |
| 12 | Ứng viên Việt Nam trong nhóm CE09 (yêu cầu D5) | 2 | 4 | 1 |
| 13 | Khoảng trống thế kỷ 9 của phụ lục + liên kết tự do nâng thành ID | 2 | 3 | 1 |
| **Tổng** | | **10** | **18** | **8** |

**Mười lỗi BẮT BUỘC, gom theo loại:**

- **Mệnh đề "chỉ có hai/duy nhất cách" không đứng được** (khối 7): phương án al-Tirmidhī `Q293578` có trong hồ sơ cửa của chính vòng này, và `CONTRIBUTING.md` không có điều cấm "hạ chuẩn".
- **Hai lỗi về cặp Constantinus–Methodius** (khối 8): "nếu CE10 không nhận họ" bất khả vì cả hai mất trong thế kỷ 9 (`Q351026` mất 869-02-14, `Q470621` mất 885-04-06); và "cùng dạng vấn đề đơn vị với Banū Mūsā" sai vì mỗi người có thực thể `P31 = Q5` riêng.
- **Một ô lĩnh vực bị đếm thiếu lời giải** (khối 9): 5 chỗ `Tôn giáo/Tâm linh` nhưng chỉ 4 được giải thích.
- **Một tiêu chí không tồn tại được dùng để loại** (khối 10): "ông không lập madhhab" — 15/20 mục `Luật` của atlas không lập trường phái nào.
- **Một mệnh đề về chính sách nhãn của atlas sai** (khối 11): atlas **có** nhãn `[Truyền thuyết]`, dùng năm lần (`content/ch01.md` dòng 634); lý do cứng thật nằm ở `P31` của `Q1245849`.
- **Hai lỗi lập luận về phụ lục và về Dương Thanh** (khối 12): "làm hỏng định nghĩa của phụ lục" bị `content/ch90.md` dòng 3 cùng hai mục Triệu Đà và Sĩ Nhiếp bác; và hai lý do loại Dương Thanh rút từ cùng một nguồn nhưng loại trừ nhau.
- **Hai lỗi sự kiện kiểm được ngay trong repo** (khối 13): `## Nhóm CE01_09 · TK 1–9 (1 – 900)` bác câu "nhóm kết thúc đúng ở đầu thế kỷ 9"; và `reports/stats.txt` bác câu "quan hệ không đếm được" — ở ch05 là 206 dòng quan hệ được đếm trong khi chỉ 65 dòng trỏ ID.

**Nhận xét chung về bảy khối.** Phần số liệu rất vững: mọi tỷ lệ vùng và lĩnh vực tôi tính tay lại đều khớp `reports/stats.txt`, cách phân bổ 3/3/1×6 đúng, và hai cảnh báo Wikidata đắt giá nhất của cả cụm — `Q6771941` mang `P31 = Q5` cho một sự kiện, và `Q1001807` có `P569 = +0801-01-01` ở `precision` 7 — đều đúng từng chữ và đều đáng giữ nguyên. Điểm yếu lặp lại nằm ở chỗ khác: **khối thường dựng một nguyên tắc chung từ một ca lẻ rồi dùng nguyên tắc ấy để kết luận**, trong khi `CONTRIBUTING.md`, `content/ch90.md` và `reports/stats.txt` có câu phủ định sẵn. Bảy trong mười lỗi BẮT BUỘC thuộc loại này, và cả bảy đều kiểm được mà không cần ra khỏi repo.

**Những chỗ tôi không xác minh được, ghi lại để không ai coi là đã kiểm:**

- `[KHÔNG KIỂM ĐƯỢC]` Niên đại "khoảng 950" cho ʻAhoʻeitu (khối 11). en.wikipedia ghi "early 10th century" / "the tenth century", không có con số 950. Kết luận của khối (ngoài khung CE09) không đổi.
- `[KHÔNG KIỂM ĐƯỢC]` Quan hệ nhân quả giữa cuộc nổi dậy 819 và việc Lý Nguyên Hỷ dời trị sở về Long Đỗ/Tô Lịch năm 824 (khối 12). Hai sự kiện đều có trong nguồn; mối nối thì không.
- `[KHÔNG KIỂM ĐƯỢC]` "Không có thực thể Wikidata nào là con người Dương Thanh" (khối 12) chỉ kiểm được tới mức `wbsearchentities` theo nhãn Việt và Anh; một thực thể không mang hai nhãn ấy thì phép tra này không thấy.
- `[KHÔNG KIỂM ĐƯỢC]` "Niên đại của Alfred là loại tốt nhất trong cả nhóm" (khối 8): `Q83476` có `P569 = +0849` ở độ chính xác năm và một `P570` hạng `deprecated`, nên không chứng minh được là tốt hơn các mục có năm sinh đơn trị như Hàn Dũ hay Kūkai.
