# Bình duyệt độc lập — `content/ch04.md`, nhóm CE02 (TK 2, 101–200 CN)

Người duyệt: agent độc lập (không viết chapter). Ngày: 2026-10-31.
Phạm vi: dòng `**Bối cảnh**` của nhóm CE02 + 11 mục `CH04-CE02-01` … `-11`.
Xếp loại: **Sai** (chắc chắn sai, cần sửa) · **Nghi vấn** (không đứng vững như đang viết) · **Thiếu** (thiếu quy thuộc/thiếu thông tin làm câu mất giá trị) · **Thể thức** (vi phạm §5 / CONTRIBUTING).

## 0. Kiểm Q-ID (toàn nhóm)

Gọi `wbgetentities` cho cả 11 Q-ID. **Tất cả đều trỏ đúng người.**

| ID | Q-ID | Nhãn Wikidata | năm: trong atlas | WD P569/P570 | Kết luận |
|---|---|---|---|---|---|
| -01 | Q229235 | Cai Lun / Thái Luân | k. 50–121, Trung bình | 48 hoặc 50 – 121 | khớp |
| -02 | Q197206 | Zhang Heng / Trương Hành | 78–139, Cao | 78–139 | khớp |
| -03 | Q312544 | Kanishka | trị vì k. 127–150, Thấp | (78–144, thực chất là niên đại trị vì) | bỏ qua đối chiếu đúng quy ước |
| -04 | Q312552 | Aśvaghoṣa / Mã Minh | k. 80–150, Thấp | 80–150 | bỏ qua / khớp |
| -05 | Q34943 | Ptolemy | k. 100–170, Thấp | 100 (hoặc 85/87) – 170 (hoặc 165) | bỏ qua / khớp |
| -06 | Q8778 | Galen | 129–216, **Cao** | sinh 129-09; mất chỉ có mức "thế kỷ" | xem §6 — độ tin cậy Cao là quá mạnh |
| -07 | Q1430 | Marcus Aurelius | 121–180, Cao | 121-04-26 – 180-03-17 | khớp |
| -08 | Q171195 | Nagarjuna | k. 150–250, Thấp | 150–250 | khớp |
| -09 | Q182123 | Irenaeus | k. 130–202, Trung bình | 130–202 | khớp |
| -10 | Q174929 | Tertullian | k. 155–220, Thấp | 150/155/160 – 220/230/240 | khớp |
| -11 | Q197350 | Zhang Zhongjing | k. 150–219, Thấp | 150–219 | khớp |

Nhắc lại CONTRIBUTING §4: khớp Wikidata là sàn, không phải trần. Các phần dưới kiểm nội dung văn xuôi.

## 0b. Kiểm liên kết (mở mục đích đọc tên)

Mọi ID được dẫn trong nhóm đều tồn tại và trỏ đúng người:

- `CH03-BCE02-01` = Đổng Trọng Thư · `CH03-BCE03-01` = Ashoka · `CH03-BCE02-06` = Patañjali · `CH03-BCE02-03` = Hipparchus · `CH03-BCE02-08` = Apollonius xứ Perga · `CH02-BCE05-04` = Hippocrates · `CH04-CE01-08` = Dioscorides · `CH03-BCE04-02` = Aristotle · `CH03-BCE03-07` = Zeno xứ Citium · `CH04-CE01-05` = Seneca · `CH02-BCE06-03` = Đức Phật · `CH04-CE01-02` = Phaolô · `CH04-CE03-02` = Origen · `CH03-BCE01-03` = Cicero · `CH04-CE05-01` = Augustinô · `CH04-CE05-07` = Cưu-ma-la-thập · `CH90-CE10_14-04` = Lý Thái Tổ · `CH90-CE19_20-09` = Tôn Thất Tùng.

Không có liên kết nào trỏ nhầm người. Hai liên kết **đáng ngờ về nội dung** (không phải sai ID) ghi riêng ở §2 và §11.

## Dòng **Bối cảnh** của nhóm

> "Đế chế La Mã đạt cực điểm rồi gặp dịch Antonine. Đế chế Kushan nối Trung Á với Ấn Độ và bảo trợ Phật giáo Đại thừa đang hình thành. Nhà Đông Hán có giấy, địa động nghi và y thư. Ở Alexandria và Pergamon, thiên văn và y học được tổng hợp thành hệ thống đứng hơn một nghìn năm."

- **Thể thức (nhỏ) — vượt trần độ dài.** Đếm bằng `wc -w`: **61 chữ**, trần template §5 là **≤ 60**. Lint không chặn chỗ này nên nó lọt. Cắt một chữ là đủ; đề xuất sửa ở gạch đầu dòng dưới cũng giải quyết luôn.
- Ba câu đầu kiểm được và đúng (cực đại lãnh thổ La Mã dưới Trajan năm 117; dịch Antonine 165–180).
- **Nghi vấn — vế "Ở Alexandria và Pergamon ... y học được tổng hợp".** Thiên văn được tổng hợp ở Alexandria (Ptolemy) là đúng. Nhưng y học thì **không** được tổng hợp ở Pergamon: Galen sinh ra và học nghề ở Pergamon, còn gần như toàn bộ việc viết và mổ công khai dựng nên hệ thống Galen diễn ra ở **Rome** sau năm 162 — chính mục `-06` cũng ghi nơi là "Pergamon, Alexandria và Rome". Câu Bối cảnh bỏ mất Rome, tức bỏ mất nơi thật sự xảy ra việc được mô tả.
- Đề xuất: *"Ở Alexandria thiên văn, và ở Rome y học, được tổng hợp thành những hệ thống đứng hơn một nghìn năm."*

## 1. `CH04-CE02-01` · Thái Luân

**Đúng, kiểm được:**
- Mốc **105 CN** dâng quy trình lên Hán Hoà Đế (trị vì 88–106): khớp ghi chép truyền thống. Nguyên liệu (vỏ cây, sợi gai, giẻ rách, lưới cá cũ) khớp Hậu Hán thư.
- **Hậu Hán thư chép ở Hoạn giả liệt truyện** (後漢書・宦者列傳, quyển 78): **đúng**. Tiểu sử Thái Luân nằm đúng ở liệt truyện hoạn giả, không phải ở liệt truyện riêng.
- **"Ông không phải người phát minh ra giấy"**: đúng và là quan điểm chuẩn hiện nay.
- Nguồn Tsien Tsuen-hsuin, *Paper and Printing*, Science and Civilisation in China **t. 5, ph. 1 (1985)**: tồn tại, đúng tác giả, đúng tập/phần, đúng năm, đúng chủ đề. Đây là một trong số ít dòng Nguồn của nhóm mà số tập kiểm được và khớp.

**Nghi vấn — "đã tìm được mảnh giấy có niên đại sớm hơn hai thế kỷ"**
Câu đúng về hướng nhưng **hạ thấp con số**. Mảnh giấy sớm nhất còn lại là bản đồ giấy Phóng Mã Than (放馬灘, Cam Túc), niên đại **179–141 TCN**, tức sớm hơn mốc 105 CN khoảng **250–280 năm**, gần ba thế kỷ. Một mảnh khác ở Bá Kiều (灞橋) thuộc thế kỷ 2 TCN. "Hai thế kỷ" không sai về mặt logic (sớm hơn hai thế kỷ *là* đúng) nhưng người đọc sẽ hiểu thành "đúng hai thế kỷ".
Đề xuất: *"— đã tìm được mảnh giấy Tây Hán sớm hơn gần ba thế kỷ, trong đó bản đồ giấy Phóng Mã Than niên đại 179–141 TCN —"*.

**Sai (mệnh đề tối cao) + Thể thức — "Vì sao chọn"**
> "Không nêu được ứng viên cùng thời: không người thợ hay quan chế tác nào khác của nhà Hán để lại tên gắn với một kỹ thuật cụ thể."

Mệnh đề này **có phản ví dụ, nhiều và dễ tìm**, tất cả đều được chép tên trong Hậu Hán thư và đều gắn với một kỹ thuật xác định:

1. **Tất Lam (畢嵐)** — hoạn quan Đông Hán, năm **186 CN** chế **phiên xa (翻車, guồng gàu xích)** và **khát ô (渴烏, ống xi-phông)** dẫn nước cho cung thành Lạc Dương. Đây là phản ví dụ đúng *cùng loại người* với Thái Luân: cũng hoạn quan, cũng coi việc chế tác cho triều đình, cũng được chép tên gắn một kỹ thuật cụ thể.
2. **Đỗ Thi (杜詩)** — thái thú Nam Dương, mất năm **38 CN**, chế **thuỷ bài (水排)**, dùng sức nước đạp bễ lò luyện sắt; Hậu Hán thư chép rõ công trạng này.
3. **Đinh Hoãn (丁緩)** — thợ thủ công, k. **180 CN**, chế quạt quay bảy bánh và lư hương treo trục các-đăng (gimbal).

Nghiêm trọng hơn: **phản ví dụ nằm ngay ở mục kế tiếp trong chính nhóm này.** `CH04-CE02-02` Trương Hành là quan nhà Đông Hán có tên gắn với hai kỹ thuật cụ thể (hỗn thiên nghi chạy nước, hậu phong địa động nghi). Câu ở `-01` và mục `-02` phủ định nhau trong cùng một nhóm.

CONTRIBUTING §5 cho phép viết thẳng "không có ai để so" — nhưng chỉ khi điều đó đúng. Ở đây nó không đúng, nên đây vừa là lỗi **Sai**, vừa là lỗi **Thể thức** (mục không nêu đích danh ứng viên bị loại dù có ứng viên).

So với hai ca cùng kiểu lập luận ở Ch1: `CH01-BCE14_12-05` Kikkuli và `CH01-BCE17_15-07` Ahmes — ở đó "người duy nhất để lại tên" đứng được vì tư liệu thật sự trống. Ở Hán thì không trống.

Đề xuất thay thế:
> *"Ứng viên cùng loại là Tất Lam, hoạn quan Đông Hán chế phiên xa và khát ô năm 186, và Đỗ Thi, thái thú Nam Dương chế thuỷ bài đạp bễ lò sắt — cả hai đều được Hậu Hán thư chép tên gắn một kỹ thuật cụ thể. Thái Luân được chọn theo counterfactual (d): bước từ giấy có tồn tại sang giấy đủ rẻ để dùng đại trà là chỗ quyết định, và chỉ bước ấy mới đổi điều kiện vật chất của việc lưu trữ và truyền bá văn bản."*

**Thiếu — quy thuộc ở dòng "Ảnh hưởng tới"**
`- Sự lan truyền của giấy sang thế giới Hồi giáo và châu Âu · kế thừa · qua trường phái`. Văn xuôi viết "từ đó kỹ thuật lan dần sang Triều Tiên, Nhật Bản rồi thế giới Hồi giáo" như một chuỗi truyền thừa đã xác lập. Mốc thường dẫn là trận Talas 751 và xưởng giấy Samarkand, nhưng chính Tsien và các khảo cứu sau đều coi câu chuyện "tù binh Talas dạy làm giấy" là giai thoại muộn, không có nguồn đương thời. Văn xuôi không nói ra chỗ này. Mức bằng chứng `qua trường phái` cho một chặng truyền bá kéo sáu thế kỷ là quá mạnh; nên hạ xuống `suy đoán học giả` hoặc thêm một mệnh đề nói rõ chặng sang phía tây không có nguồn đương thời.

## 2. `CH04-CE02-02` · Trương Hành

**Đúng, kiểm được:** chức thái sử lệnh ✓ · hỗn thiên nghi chạy bằng sức nước ✓ · **năm 132 CN** dựng hậu phong địa động nghi ✓ (mốc chuẩn, không phải 138) · **tám con rồng** ngậm bi, con nào nhả bi thì chỉ hướng chấn ✓ · giai thoại Lũng Tây ✓ (Hậu Hán thư chép máy báo mà kinh đô không ai cảm thấy, vài ngày sau tin từ Lũng Tây tới — thường quy vào năm 138) · viết phú ✓ (Nhị kinh phú) · nguồn Needham, *Science and Civilisation in China* **t. 3 (1959)** ✓ đúng tập (phần địa chấn học nằm ở t. 3) và đúng năm.

**Nghi vấn nhẹ — pi = căn bậc hai của mười.** Đúng, nhưng chưa đủ: Trương Hành đưa ra **nhiều** giá trị, trong đó cả √10 ≈ 3,162 lẫn phân số 730/232 ≈ 3,1466 (và 92/29). Viết như thể ông chỉ có một giá trị là đơn giản hoá. Đề xuất: *"Ông cũng đưa ra mấy giá trị xấp xỉ cho số pi, trong đó có căn bậc hai của mười."*

**Sai — "không có hậu duệ trực tiếp, tức nó là một sáng chế đơn độc"**
Vế "không có tiền lệ ở bất kỳ nền văn minh nào" đứng được: đây vẫn được coi là dụng cụ báo động đất sớm nhất được ghi chép, chưa tìm thấy phản ví dụ.
Nhưng vế **hậu duệ** thì sai. Có hai hậu duệ **văn bản trực tiếp**, đều mang mục đích chép lại cách dựng máy:
- **Tín Đô Phương (信都芳)**, Bắc Tề, soạn *Khí chuẩn* (器準);
- **Lâm Hiếu Cung (臨孝恭)**, đầu đời Tuỳ, soạn ***Địa động đồng nghi kinh*** (地動銅儀經).
Cả hai đều chép mô tả và phương pháp chế tác địa động nghi. Nói "không có hậu duệ trực tiếp" đúng với *cỗ máy* (bản gốc mất, không bản phục dựng cổ nào còn), nhưng sai với *truyền thống*.
Đề xuất: *"...không có tiền lệ ở bất kỳ nền văn minh nào, và cỗ máy gốc thì mất hẳn — đời sau chỉ còn những bản chép cách dựng, như Khí chuẩn của Tín Đô Phương và Địa động đồng nghi kinh của Lâm Hiếu Cung, chứ không còn vật thật."*

Lưu ý: câu cuối mục ("Cơ cấu bên trong máy không được chép lại, nên mọi bản phục dựng hiện nay đều là giả thuyết") là đúng và nên giữ — nhưng nó lại mâu thuẫn một phần với chính hai cuốn sách trên, vốn *được mô tả* là có chép cách dựng. Cách an toàn: nói rõ các sách ấy cũng đã thất truyền.

**Thể thức — "ứng viên cùng thời" không có ai cùng thời**
> "Ứng viên cùng lĩnh vực là Mã Quân ở thế kỷ sau, chế xe chỉ nam và máy dệt, và Vương Sung, chọn ở nhóm trước."

Hai tên, không tên nào dùng được:
- **Mã Quân (馬鈞)** hoạt động k. 220–265, thời Tào Nguỵ — cách Trương Hành (78–139) khoảng một thế kỷ. Mục **có nói ra** ("ở thế kỷ sau"), nên không rơi vào lỗi hệ thống thứ nhất, nhưng cũng không thoả yêu cầu "cùng thời" của §5.
- **Vương Sung** = `CH04-CE01-10`, **đã được chọn** trong atlas. Mục **có nói ra** ("chọn ở nhóm trước") đúng theo CONTRIBUTING §6, nên không phải lỗi — nhưng kết quả là mục này **không nêu được một ứng viên bị loại nào thật sự cùng thời**.

Mà ứng viên cùng thời thì có, và rất sát đề tài:
- **Giả Quỳ (賈逵, 30–101)** cùng **Phó An (傅安)**: chính hai người này đưa vòng hoàng đạo vào hỗn thiên nghi — báo cáo của Giả Quỳ năm 92, dụng cụ chính thức có vòng hoàng đạo đầu tiên năm **103**. Trương Hành là người sau đó thêm vòng chân trời và vòng tí ngọ. Đây vừa là ứng viên cùng thời, vừa làm rõ Trương Hành đứng ở đâu trong chuỗi.
- **Lưu Hồng (劉洪, k. 129–210)**, tác giả lịch Càn Tượng, người đầu tiên đưa bất đẳng tốc chuyển động của Mặt Trăng vào lịch pháp.

Đề xuất: *"Ứng viên cùng thời là Giả Quỳ, người đưa vòng hoàng đạo vào hỗn thiên nghi năm 103, và Lưu Hồng, tác giả lịch Càn Tượng. Trương Hành được chọn theo tính nguyên bản (c): ..."*

**Nghi vấn — "Kế thừa từ: CH03-BCE02-01 · kế thừa · qua trường phái"**
ID trỏ đúng **Đổng Trọng Thư**. Nhưng Đổng Trọng Thư là người hệ thống hoá thiên nhân cảm ứng và tai dị luận, không phải nguồn của *bất cứ thứ gì* được mô tả trong mục: hỗn thiên nghi thuộc truyền thống hỗn thiên thuyết và chuỗi chế tạo Lạc Hạ Hoành → Giả Quỳ/Phó An → Trương Hành; địa động nghi thuộc truyền thống đo đạc. Liên kết này đúng ID, sai nội dung — đúng loại lỗi CONTRIBUTING §8 cảnh báo (lint mù vì chiều và niên đại đều hợp lệ).
Nếu muốn giữ, phải nói rõ là kế thừa **khung tai dị luận** (máy báo động đất phục vụ chính trị điềm triệu), chứ không phải kế thừa kỹ thuật. Tốt hơn: đổi sang Giả Quỳ/truyền thống hỗn thiên thuyết nếu atlas có mục, hoặc ghi `- Truyền thống hỗn thiên thuyết và chế tạo hỗn thiên nghi thời Hán · kế thừa · qua trường phái`.

## 3. `CH04-CE02-03` · Kanishka

**Đúng, kiểm được:**
- **Nguồn Falk tồn tại và được trích chính xác**: Harry Falk, "The yuga of Sphujiddhvaja and the era of the Kuṣâṇas", ***Silk Road Art and Archaeology* 7 (2001), tr. 121–136**. Đúng tác giả, đúng tên bài, đúng tạp chí, đúng số, đúng năm, và **đúng việc được dẫn** — đây chính là bài xác lập kỷ nguyên Kanishka khởi từ **127 CN**, mốc mà mục đang dùng. Dòng `trị vì k. 127–150` nhất quán với Falk.
- Đế chế Kushan trải từ Trung Á tới lưu vực sông Hằng ✓ · bảo trợ Phật giáo quy mô nhà nước ✓ · tiền cùng một triều đúc hình Phật kèm chữ Hy Lạp (ΒΟΔΔΟ), thần Iran và thần Ấn Độ ✓ · kỳ kết tập được gắn với ông **theo truyền thống** — mục đã rào đúng ("truyền thống Phật giáo gắn ông với…") ✓.

**Sai — nguồn thứ hai không tồn tại như được ghi**
> "Vincent Lefèvre (chủ biên), *L'art du Gandhara* (2010)."

Không tìm thấy sách nào tên *L'art du Gandhara* do Vincent Lefèvre chủ biên, năm 2010 hay năm khác. Cuốn **thật** mà trích dẫn này rõ ràng đang nhắm tới là catalogue triển lãm Guimet cùng năm:
**Pierre Cambon (dir.), *Pakistan, terre de rencontre, Ier–VIe siècle. Les arts du Gandhara*, Réunion des musées nationaux / Musée Guimet, 2010** (ISBN 978-2-7118-5731-9, triển lãm 21/4–16/8/2010).
Sai cả **tên sách** lẫn **người chủ biên**. Vincent Lefèvre là bảo quản viên Guimet chuyên nghệ thuật Ấn Độ — tên có thật, nên lỗi này thuộc loại "trích dẫn được ghép từ các mảnh đúng", khó bắt bằng mắt. Đây là đúng loại lỗi CONTRIBUTING §2 nói tới.
Đề xuất: thay bằng dòng Cambon ở trên.

**Nghi vấn — "các đề xuất trải từ 78 tới 144 CN"** (lặp lại ở Ghi chú biên tập, dòng ~997)
Cận dưới 78 đúng (kỷ nguyên Śaka). Cận trên **144 thì hẹp hơn thực tế**: lịch sử tranh luận còn có những đề xuất muộn hơn hẳn (trường phái "niên đại muộn" đẩy Kanishka sang thế kỷ 3). Hội nghị London 1960 về niên đại Kaniṣka tập hợp đúng vì các đề xuất phân tán rộng, không gói trong 78–144. **Tôi không kiểm được một bản tổng kết có thẩm quyền ghi cận trên chính xác**, nên không khẳng định con số thay thế; nhưng viết "trải từ 78 tới 144" như thể đó là toàn bộ biên độ là một mệnh đề mạnh hơn cái kiểm được.
Đề xuất (an toàn hơn và vẫn đúng): *"...với các đề xuất trải từ 78 CN tới tận thế kỷ 3; mục này theo Falk (2001)."*

**Nghi vấn (mệnh đề tối cao, lệch trung lập) — "Nghệ thuật Gandhāra tạc Phật theo lối tượng người, định hình mọi hình tượng Phật về sau"**
Hai vấn đề:
1. **"định hình mọi hình tượng Phật về sau"** bỏ qua **trường phái Mathurā**, vốn phát triển hình Phật dạng người gần như cùng lúc và từ truyền thống tạo hình Ấn Độ bản địa, không phải từ Gandhāra. Câu hỏi Gandhāra hay Mathurā có trước vẫn **chưa ngã ngũ**; học giới hiện nay phần lớn coi hai nơi là song song và phần nào độc lập. Chính mục này ghi `nơi: Purushapura ... và Mathura` — tức đã nhắc Mathurā ở dòng metadata rồi lại gán toàn bộ công cho Gandhāra ở văn xuôi.
2. Mệnh đề tối cao "mọi ... về sau" không có quy thuộc.
Đề xuất: *"Nghệ thuật Gandhāra tạc Phật theo lối tượng người, cùng lúc với trường phái Mathurā và theo một gốc tạo hình khác hẳn; câu hỏi nơi nào có trước vẫn chưa ngã ngũ. Cả hai nở rộ trong giai đoạn này và cùng là nguồn của hình tượng Phật về sau."*

**Nghi vấn — mức bằng chứng của liên kết tới `-04`**
`- CH04-CE02-04 · kế thừa · trực tiếp` (và dòng đối xứng ở `-04`). ID trỏ đúng Aśvaghoṣa. Nhưng việc Aśvaghoṣa ở triều đình Kanishka **chỉ có trong truyền thống hậu kỳ** (chủ yếu nguồn Hán văn), không có bằng chứng đương thời — chính mục `-04` để `độ tin cậy niên đại: Thấp` vì lý do đó. Gắn mức `trực tiếp` cho một quan hệ mà cả hai đầu đều niên đại Thấp là mâu thuẫn nội bộ.
Đề xuất: hạ cả hai dòng xuống `· kế thừa · suy đoán học giả`.

**Ghi nhận tốt:** hai ứng viên bị loại (Gautamiputra Satakarni, Huvishka) đều **cùng thời thật** và **đều không có mục riêng** trong atlas (đã đối chiếu 221 đầu mục `### ` của cả 5 file content). Mục này không mắc hai lỗi hệ thống của §5.

## 4. `CH04-CE02-04` · Aśvaghoṣa

**Sai — "Saundarananda kể chuyện người em họ của Phật"**
Nanda là **em cùng cha khác mẹ** của Đức Phật, con của Tịnh Phạn (Śuddhodana) và Ma-ha-ba-xà-ba-đề (Mahāprajāpatī) — tức cùng cha, khác mẹ. "Em họ" là quan hệ của **Ānanda** (và Devadatta), không phải Nanda. Lỗi này đổi hẳn nội dung tác phẩm: sức nặng của Saundarananda nằm ở chỗ người bị giằng xé là em ruột-cùng-cha trong chính hoàng tộc Thích-ca, không phải một người họ hàng xa.
Đề xuất: *"...kể chuyện Nanda, em cùng cha khác mẹ của Phật, bị giằng giữa người vợ Janapadakalyāṇī và đời xuất gia."*

**Sai — "Đây là những bài kāvya *hoàn chỉnh* sớm nhất còn lại"**
Hai lỗi chồng nhau:
1. **Buddhacarita không còn hoàn chỉnh.** Trong 28 phẩm, **chỉ 14 phẩm đầu còn nguyên văn Sanskrit**; phẩm 15–28 chỉ còn qua bản Hán (thế kỷ 5) và bản Tạng. Chính bản dịch được dẫn ngay ở dòng Nguồn — Johnston (1936) — mang đúng phụ đề nói điều đó: *cantos I–XIV translated from the original Sanskrit, cantos XV–XXVIII from the Tibetan and Chinese versions*. Tức dòng Nguồn của mục **tự bác** câu văn xuôi của mục. Chỉ **Saundarananda** mới còn đủ bằng Sanskrit.
2. **Có phản ví dụ gần như cùng thời cho "kāvya sớm nhất còn lại"**: **bia đá Junagadh của Rudradāman I, k. 150 CN** — văn bia Sanskrit chuẩn, thể văn xuôi kāvya (gadya-kāvya / praśasti), được coi là mẫu văn kāvya cổ điển còn lại sớm nhất và là nguyên mẫu cho các praśasti thời Gupta. Nếu muốn giữ mệnh đề tối cao thì phải thu hẹp phạm vi cho rõ: **mahākāvya dạng tác phẩm văn học** (không tính văn bia).

Đề xuất gộp: *"Saundarananda còn nguyên vẹn bằng Sanskrit, còn Buddhacarita chỉ còn 14 trong 28 phẩm bản gốc, phần sau phải đọc qua bản Hán và bản Tạng. Đây vẫn là những mahākāvya sớm nhất còn lại dưới dạng tác phẩm văn học — gần như cùng lúc với bia Junagadh của Rudradāman, mẫu văn xuôi kāvya sớm nhất — nên lịch sử thơ Sanskrit cổ điển bắt đầu từ một tác giả Phật giáo chứ không phải từ truyền thống Bà-la-môn."*

**Sai (nghiêm trọng, lỗi hệ thống §5 loại 2 đảo ngược) — "Kālidāsa ... được chọn ở chapter này theo nhóm khác"**
**Kālidāsa không có mục nào trong toàn bộ atlas.** Đã grep `^### ` toàn bộ `content/ch01.md … ch04.md, ch90.md` (221 đầu mục): không có Kālidāsa.
Tệ hơn, **chính Ghi chú biên tập của Chapter 4 (dòng ~993) nói ngược lại**:
> "Samudragupta, **Kālidāsa**, Āryadeva, … : Kālidāsa là ca đáng tiếc nhất … nhưng niên đại của ông trải từ thế kỷ 4 tới thế kỷ 5 mà không mốc nào chắc, và cả hai nhóm tương ứng đều đã kín."
Tức Kālidāsa là **ứng viên bị loại**, không phải người "được chọn ở nhóm khác". Hai câu trong cùng một file mâu thuẫn trực tiếp.
Thêm một lỗi nhỏ nằm trong cùng mệnh đề: **"thuộc thế kỷ sau"** cũng sai — Kālidāsa thường được đặt ở thế kỷ 4–5, tức cách Aśvaghoṣa hai tới ba thế kỷ, không phải một.
Đề xuất: *"...và Kālidāsa, cách ông hai tới ba thế kỷ, được cân nhắc nhưng bị loại vì niên đại không chắc (xem Ghi chú biên tập)."* — hoặc bỏ hẳn Kālidāsa và thay bằng một ứng viên cùng thời thật.

**Đúng, kiểm được:** Buddhacarita viết theo thể kāvya ✓ · Mātṛceṭa là ứng viên hợp lệ (cũng soạn tán ca Phật giáo bằng Sanskrit, k. thế kỷ 2, **không có mục riêng** trong atlas) ✓ · Nguồn Johnston (1936) tồn tại, đúng năm, đúng thể loại (bản dịch kèm nguyên bản) ✓ · Nguồn Patrick Olivelle, *Life of the Buddha* (2008), Clay Sanskrit Library / NYU Press — tồn tại, đúng năm, đúng chủ đề (bản dịch Buddhacarita) ✓ · Liên kết `CH03-BCE02-06` trỏ đúng **Patañjali nhà văn phạm** (mục ở Ch3 nói rõ "chỉ nói về nhà văn phạm"), nên quan hệ kāvya ← Sanskrit chuẩn hoá là hợp lý ✓.

**Nghi vấn nhẹ:** `- CH04-CE05-07 · kế thừa · qua trường phái` (Cưu-ma-la-thập). Bản Hán của Buddhacarita (佛所行讚) do **Đàm-vô-sấm (曇無讖)** dịch, không phải Cưu-ma-la-thập; cái Cưu-ma-la-thập được gắn tên là *Mã Minh Bồ-tát truyện*. Liên kết không sai hẳn nhưng mỏng; nếu giữ thì nên là `suy đoán học giả`.

## 5. `CH04-CE02-05` · Claudius Ptolemy

**Đúng, kiểm được:**
- **"khoảng tám nghìn địa điểm" trong Địa lý học: đúng.** Danh mục toạ độ của Geographia liệt kê khoảng 8.000 địa danh (chừng hai phần ba nằm trong đế chế La Mã). Con số này kiểm được và khớp.
- Mô hình địa tâm với ngoại luân (epicycle) trên vòng lệch tâm (deferent/eccentric), kèm bảng số ✓ · bàn phép chiếu mặt cầu lên mặt phẳng trong Geographia ✓ · Tetrabiblos, Optics, Harmonics ✓ · "đứng mười bốn thế kỷ cho tới Copernicus" ✓ (k. 150 → 1543).
- Nguồn **Toomer, *Ptolemy's Almagest* (1984)** ✓ tồn tại, đúng năm, đúng thể loại (bản dịch kèm chú). Nguồn **Alexander Jones (ed.), *Ptolemy in Perspective* (2010)** ✓ tồn tại (Springer, loạt Archimedes), đúng chủ biên, đúng năm, đúng chủ đề.
- Ứng viên **Menelaus xứ Alexandria** ✓ cùng thời thật (k. 70–140), đúng việc được gán (Sphaerica, lượng giác cầu), **không có mục riêng** trong atlas. **Hipparchus** được khai báo đúng là "chọn ở Chapter 3" theo CONTRIBUTING §6 ✓.

**Sai (quy thuộc) — "Việc *ông* ước lượng chu vi Trái Đất quá nhỏ là một trong các cơ sở khiến Columbus tính sai"**
Ptolemy **không ước lượng** chu vi Trái Đất. Con số 180.000 stadia là của **Posidonius** (bản Strabo phổ biến, sửa khoảng cách Rhodes–Alexandria thành 3.750 stadia), được **Marinus xứ Tyre** tiếp nhận, rồi Ptolemy lấy lại từ Marinus. Ptolemy là người **truyền**, không phải người **đo**. (Con số đúng, của Eratosthenes, là 252.000 stadia.)

Điều này không chỉ sai về sử — nó **mâu thuẫn với chính atlas**. Mục `CH03-BCE01-12` Posidonius viết đúng:
> "...con số chu vi Trái Đất nhỏ hơn **của ông, qua Ptolemy**, là một trong các cơ sở khiến Columbus tính sai khoảng cách."

Hai mục cùng kể một việc, Ch3 quy đúng cho Posidonius và ghi rõ Ptolemy là khâu trung chuyển, Ch4 lại quy thẳng cho Ptolemy và xoá Posidonius. Một trong hai phải sửa, và cái phải sửa là Ch4.

Thêm một lớp nữa nên nói ra cho đủ: Columbus còn dựa vào **Marinus** nhiều hơn Ptolemy ở một điểm then chốt — ông bác con số 180° chiều dài Á–Âu của Ptolemy để lấy 225° của Marinus, rồi cộng thêm sai lệch từ độ dài "dặm" của al-Farghānī. Nói gọn "vì Ptolemy" là rút ngắn một chuỗi mà chính atlas đã kể đúng ở chỗ khác.

Đề xuất: *"Ông lấy lại con số chu vi Trái Đất quá nhỏ của Posidonius qua Marinus xứ Tyre, và chính việc Almagest cùng Địa lý học chuyên chở con số ấy là một trong các cơ sở khiến Columbus tính sai khoảng cách."*

**Thiếu — bản đồ của Geographia**
Dòng "Ảnh hưởng tới" có `Bản đồ học thời Phục hưng · kế thừa · qua trường phái`, nhưng văn xuôi không nói chỗ quyết định: bản đồ đi kèm Geographia **không còn từ thời cổ**; thứ châu Âu thế kỷ 15 dựng lại là từ **danh mục toạ độ** cộng hướng dẫn phép chiếu, qua bản Hy Lạp Byzantine và bản dịch Latinh của Jacopo d'Angelo (1406). Đây đúng là lý do con số "tám nghìn địa điểm" quan trọng, và mục đang bỏ sót nó.

## 6. `CH04-CE02-06` · Galen

**Đúng, kiểm được:**
- **Thí nghiệm động mạch chứa máu chứ không chứa khí: đúng.** Đây là chuyên luận *An in arteriis natura sanguis contineatur* ("Động mạch có chứa máu tự nhiên không"), trong đó Galen cột một đoạn động mạch ở thú sống rồi mở ra, bác học thuyết Erasistratus cho rằng động mạch chứa pneuma. Kiểm được và đúng.
- Cắt tuỷ sống ở các mức khác nhau gây liệt khác nhau ✓ · giải phẫu trên khỉ (Barbary ape) và lợn ✓ · đòi thầy thuốc học logic và triết học ✓ (*Quod optimus medicus sit quoque philosophus*) · gắn dịch thể luận Hippocrates với giải phẫu thực nghiệm ✓.
- Nguồn **Vivian Nutton, *Ancient Medicine* (2013)** ✓ tồn tại (Routledge, bản 2), đúng năm, đúng chủ đề — và đúng là nguồn đứng sau nhiều số liệu của mục. **Galen, *On the Natural Faculties*, bản dịch A. J. Brock (1916)** ✓ Loeb Classical Library, đúng năm, đúng thể loại (bản dịch).
- Liên kết `CH02-BCE05-04` Hippocrates, `CH03-BCE04-02` Aristotle, `CH04-CE01-08` Dioscorides — cả ba đều trỏ đúng người và hợp lý về nội dung ✓.
- Vùng `Châu Âu` cho Pergamon: nhất quán với quy ước đã khai báo ở Ghi chú biên tập Ch3 (thành bang Hy Lạp ở Tiểu Á ghi Châu Âu) ✓, không phải lỗi.

**Thiếu (mệnh đề không quy thuộc, và bỏ mất con số) — "chiếm một phần đáng kể toàn bộ văn chương Hy Lạp cổ còn lại"**
Mệnh đề đúng về hướng nhưng **mơ hồ tới mức không kiểm được**, trong khi con số thật thì có và được dẫn rộng rãi: trước tác còn lại của Galen chiếm **khoảng 10%** toàn bộ văn chương Hy Lạp cổ còn lại **tính tới năm 350 CN** — con số gắn với chính Nutton, tức nguồn số 1 của mục. Hai chi tiết bị bỏ đều quan trọng: **con số** và **mốc cắt 350 CN** (không có mốc ấy thì mệnh đề vô nghĩa, vì "văn chương Hy Lạp cổ" kéo tới Byzantium).
Đề xuất: *"Trước tác còn lại của ông chiếm khoảng một phần mười toàn bộ văn chương Hy Lạp còn lại từ trước năm 350 CN."*

**Sai — "cho tới khi Vesalius mổ xác người năm 1543"**
Câu này hàm ý Vesalius là người mở lại việc mổ xác người ở châu Âu. Không phải: **mổ xác người đã được làm công khai ở Bologna từ k. 1315** (Mondino de' Liuzzi, *Anathomia* 1316) và thành thông lệ trong chương trình y khoa đại học suốt hai thế kỷ trước Vesalius. Điều Vesalius làm năm **1543** là xuất bản *De humani corporis fabrica*, bộ sách **đối chiếu có hệ thống** và sửa hàng loạt sai lầm giải phẫu của Galen — chính vì Galen mổ khỉ và lợn chứ không mổ người. Mốc 1543 và tên Vesalius đều đúng; **cái sai là động từ**.
Đề xuất: *"...cho tới khi Vesalius công bố De humani corporis fabrica năm 1543, bộ sách đối chiếu có hệ thống và sửa hàng loạt sai lầm giải phẫu của Galen."*

**Nghi vấn — `độ tin cậy niên đại: Cao` cho 129–216**
Năm sinh 129 thì chắc. Năm mất thì **không**: đây là con số **suy ra** từ các nhà viết tiểu sử Arab (thọ 87 tuổi) và từ việc tác phẩm cuối của Galen viết sau 207 — lập luận của Nutton, hiện được chấp nhận, nhưng vẫn là suy luận; truyền thống cũ ghi 199. Mức `Cao` nghĩa là dung sai ±5, trong khi biên độ thật giữa 199 và 216/217 là 17 năm.
Lưu ý về lint: **Wikidata không bắt được chỗ này** — P570 của Q8778 chỉ có claim ở mức "thế kỷ" (prec 7), nên đối chiếu tự động báo sạch. Đúng loại điểm mù CONTRIBUTING §4 mô tả.
Đề xuất: giữ `129–216 CN` nhưng hạ `độ tin cậy niên đại` xuống **Trung bình** (±25 vẫn phủ cả 199), và thêm một mệnh đề trong văn xuôi hoặc Ghi chú biên tập nói năm mất là suy ra.

**Thể thức — hai "ứng viên cùng thời" đều không chồng lấn sự nghiệp Galen**
- **Soranus xứ Ephesus** hoạt động k. 98–138 (thời Trajan và Hadrian). Galen sinh **129**: khi Soranus ngừng hoạt động thì Galen mới chín tuổi. Không có chồng lấn sự nghiệp, và mục **không nói ra điều đó** — đúng lỗi hệ thống thứ nhất của CONTRIBUTING §5.
- **Aretaeus xứ Cappadocia**: niên đại không xác định được, các đề xuất trải từ thế kỷ 1 tới thế kỷ 2. **Không kiểm được** có cùng thời hay không — mà chính vì thế không nên dùng làm ứng viên "cùng thời" mà không rào.
Cả hai vẫn là lựa chọn hợp lý về *lĩnh vực*, và cả hai **không có mục riêng** trong atlas ✓ (không mắc lỗi hệ thống thứ hai). Chỉ cần sửa cách diễn đạt.
Đề xuất: *"Ứng viên cùng lĩnh vực là Soranus xứ Ephesus, hoạt động một thế hệ trước ông và để lại bộ sản khoa được dùng lâu dài, và Aretaeus xứ Cappadocia, người mà niên đại tới nay vẫn không xác định được."*

## 7. `CH04-CE02-07` · Marcus Aurelius

**Đúng, kiểm được:** viết bằng tiếng Hy Lạp trong các chiến dịch ở biên giới Danube ✓ · không nhằm xuất bản ✓ · nội dung (phân biệt cái thuộc quyền mình / không thuộc quyền mình, cộng đồng lý tính) ✓ · dịch Antonine quét qua đế chế trong triều ông ✓ (165–180) · truyền ngôi cho Commodus bị chê từ thời cổ ✓ (Cassius Dio, Herodian) · ứng viên **Fronto** cùng thời thật, đúng vai trò (thầy dạy hùng biện, thư từ còn lại), **không có mục riêng** trong atlas ✓ · Nguồn **Robin Hard (2011)** ✓ tồn tại (Oxford World's Classics, *Meditations with Selected Correspondence*), đúng năm, đúng thể loại · Nguồn **Pierre Hadot, *The Inner Citadel* (1998)** ✓ tồn tại (Harvard UP, Michael Chase dịch; nguyên bản Pháp *La citadelle intérieure*, 1992), đúng năm bản Anh, đúng thể loại (chuyên khảo).

**Sai (mệnh đề tối cao, và nguồn bị dùng ngược) — "Suy tưởng không có tiền lệ nào cùng dạng trong văn chương cổ đại"**
Đây là lỗi nặng nhất của mục, vì nó **mâu thuẫn trực tiếp với nguồn số 2 của chính mục**. Luận điểm trung tâm của Hadot trong *The Inner Citadel* là **ngược lại**: Suy tưởng là một tập ***hypomnēmata*** (ghi chép cá nhân), tức một **thể loại đã có sẵn và được khuyến khích** trong truyền thống Khắc kỷ — người học triết được dặn phải luôn giữ sẵn trong tay (*procheiron*) một tập ghi chép như vậy và đọc lại thường xuyên. Hadot viết cuốn sách ấy chính là để **đặt Suy tưởng vào trong một truyền thống**, không phải để nói nó đứng ngoài mọi truyền thống.

Tiền lệ cụ thể, tất cả đều cổ hơn:
- **Arrianus** gọi bản ghi lời Epictetus của mình là *hupomnēmata*, đặt theo ***Memorabilia* của Xenophon** (tên Hy Lạp cũng là *hupomnēmata*) — tức chuỗi thể loại này lùi tới thế kỷ 4 TCN;
- chính Marcus ghi ơn Rusticus **vì đã đưa cho ông một tập *hypomnemata*** chép lời Epictetus — nghĩa là ông biết thể loại ấy trước khi tự viết;
- *askēsis / meletē* (bài tập tinh thần) là thực hành chung của mọi trường phái Hellenistic.

Đây đúng loại lỗi CONTRIBUTING §7 cảnh báo: nguồn tồn tại, đúng chủ đề, nhưng **lập luận gì** thì ngược với câu được nó đỡ.
Đề xuất: *"...được chọn theo tính nguyên bản (c) của tình huống chứ không của thể loại: Suy tưởng thuộc thể hypomnēmata vốn đã là thực hành chuẩn của Khắc kỷ — Hadot đọc nó đúng theo nghĩa ấy — nhưng không có văn bản cổ đại nào khác cùng thể lại do một người nắm quyền lực tuyệt đối viết cho riêng mình, và chính điều đó khiến nó được đọc như sách thực hành cho tới nay."*

**Nghi vấn — "Epictetus, người thầy ông đọc và trích"**
Về niên đại thì hai người có chồng lấn (Epictetus k. 50–135; Marcus sinh 121), nên không phạm lỗi "không cùng thời". Nhưng chữ **"người thầy"** gây hiểu sai: **hai người chưa từng gặp nhau.** Epictetus mất khi Marcus khoảng mười bốn tuổi, và quan hệ là **qua văn bản**: Junius Rusticus đưa cho Marcus bản chép lời Epictetus. Người thầy thật là Rusticus.
Đề xuất: *"Ứng viên cùng truyền thống là Epictetus, người ông chưa từng gặp nhưng đọc và trích qua bản chép Rusticus đưa cho, và Fronto, thầy dạy hùng biện của ông."*

## 8. `CH04-CE02-08` · Nāgārjuna

**Đúng, kiểm được:** Trung luận (Mūlamadhyamakakārikā) lập luận không sự vật nào có tự tính (svabhāva) ✓ · tứ cú (catuṣkoṭi): có / không / vừa có vừa không / không có không không ✓ · các phạm trù được mổ xẻ (nhân quả MMK ph. 1, chuyển động ph. 2, thời gian ph. 19, chính tính không ph. 24) ✓ · nhị đế (saṃvṛti / paramārtha) tách chân lý quy ước khỏi chân lý tối hậu, MMK 24.8–10 ✓ · rào "tiểu sử gần như toàn truyền thuyết, nhiều tác phẩm mang tên ông có thể của nhiều người" ✓ đúng và nên giữ · **Āryadeva** là ứng viên hợp lệ (học trò trực tiếp theo truyền thống, k. thế kỷ 3, **không có mục riêng** trong atlas) ✓ · **Vasubandhu** được khai báo đúng là "chọn riêng ở nhóm sau" (`CH04-CE04-11`) theo CONTRIBUTING §6 ✓ · liên kết `CH04-CE05-07` Cưu-ma-la-thập rất chắc (chính ông dịch Trung luận sang Hán, 中論) ✓.

**Nghi vấn — nguồn đúng nhưng thể loại cần nói rõ**
*Nāgārjuna, Mūlamadhyamakakārikā, bản dịch **Jay L. Garfield** (1995)*: sách tồn tại (*The Fundamental Wisdom of the Middle Way*, Oxford University Press, 1995), đúng năm, đúng chủ đề. Nhưng **Garfield dịch từ bản Tạng**, không từ Sanskrit — và là bản dịch **kèm bình giải triết học dài**, không phải bản dịch thuần. Trong một chapter mà CONTRIBUTING §7 đã từng bắt lỗi "ghi bản dịch nhưng thực ra là chuyên khảo", nên ghi rõ: *"bản dịch từ bản Tạng kèm bình giải của Jay L. Garfield (1995)"*. **Jan Westerhoff, *Nāgārjuna's Madhyamaka: A Philosophical Introduction* (2009)** ✓ đúng hoàn toàn.

**Nghi vấn (mệnh đề quá mạnh) — "phái Trung quán do ông lập là nền chung của Phật giáo Đại thừa ở Tây Tạng, Trung Hoa, Triều Tiên, Nhật Bản và Việt Nam"**
Vế **Tây Tạng** đúng và mạnh: Trung quán (đặc biệt Prāsaṅgika) được các tông phái Tạng xếp làm kiến giải cao nhất, dạy theo chương trình chính quy.
Vế **Đông Á thì quá mạnh.** Trung quán vào Trung Hoa thành tông **Tam Luận (三論宗)**, và tông này **suy tàn sau đời Đường**, không trở thành "nền chung". Các dòng thật sự chi phối Phật giáo Trung – Triều – Nhật – Việt là Thiên Thai, Hoa Nghiêm, Thiền và Tịnh Độ, với Duy thức (Yogācāra) và Như Lai tạng đóng vai trò giáo lý ít nhất ngang Trung quán. Nói **giáo lý tính không** của ông thấm vào tất cả các dòng ấy thì đúng; nói **phái** của ông là nền chung của chúng thì không.
Đề xuất: *"...giáo lý tính không của ông là nền chung mà mọi dòng Đại thừa về sau đều phải đi qua, và ở Tây Tạng thì phái Trung quán do ông lập được xếp thẳng làm kiến giải cao nhất."*

**Sai — liên kết `- CH90-CE10_14-04 · kế thừa · qua trường phái` (Lý Thái Tổ)**
Đã mở mục đích ra đọc. `CH90-CE10_14-04` là **Lý Thái Tổ (Lý Công Uẩn, 974–1028)**, và toàn bộ mục ấy nói về **việc dời đô ra Thăng Long** — lĩnh vực `Chính trị/Nhà nước`, không một chữ nào về Trung quán, tính không hay Phật học. Dòng "Kế thừa từ" của mục ấy là `CH90-CE10_14-03` và `CH90-CE10_14-02`, **không có Nāgārjuna**.

Đây đúng loại lỗi CONTRIBUTING §8 mô tả ("Tư Mã Thiên ảnh hưởng tới Đinh Bộ Lĩnh"): ID có thật, chiều hợp lệ, niên đại hợp lệ, nên lint không bắt được — nó chỉ báo một dòng **[INFO]** bất đối xứng ở `reports/lint-ch04.txt:31`:
> `[INFO] CH04-CE02-08: ảnh hưởng tới CH90-CE10_14-04 nhưng CH90-CE10_14-04 không ghi 'Kế thừa từ' CH04-CE02-08 (P4 sẽ đồng bộ)`

**Cảnh báo quy trình:** nếu P4 "đồng bộ" tự động theo dòng INFO này, nó sẽ **viết một quan hệ sai vào mục Lý Thái Tổ** thay vì sửa chỗ sai. Phải xoá liên kết ở `-08` trước khi chạy đồng bộ.
Đề xuất: bỏ hẳn dòng này. Nếu muốn giữ một móc nối Việt Nam, đích đúng là một mục về Phật giáo Việt Nam / thiền phái, không phải một ông vua được chọn vì quyết định quy hoạch đô thị.

## 9. `CH04-CE02-09` · Irenaeus thành Lyon

**Đúng, kiểm được:**
- **Nag Hammadi 1945: đúng.** Kho văn bản Coptic được tìm thấy ở Nag Hammadi (Thượng Ai Cập) **tháng 12 năm 1945**. Năm đúng.
- **Quy điển bốn Phúc Âm "không hơn không kém": đúng.** Irenaeus là tác giả đầu tiên còn lại **lập luận dứt khoát** rằng phải đúng bốn Phúc Âm, trong đoạn nổi tiếng *Adversus Haereses* 3.11.8 (bốn phương, bốn gió, bốn sinh vật).
- Smyrna và Lugdunum ✓ · truyền thừa tông đồ và *regula fidei* ("thước đo đức tin") là ba trục của bộ sách ✓ · hai ứng viên **Justin Tử đạo** (k. 100–165, biện giáo, có chồng lấn đời với Irenaeus) và **Marcion** (k. 85–160) — cả hai hợp lệ, cả hai **không có mục riêng** trong atlas ✓.
- **Nguồn Unger (1992–2012): đúng và chính xác đến mức hiếm.** Dominic J. Unger dịch *Against the Heresies*, loạt Ancient Christian Writers: **Q. 1 = ACW 55 (1992)**, **Q. 2 = ACW 65 (2012)**, **Q. 3 = ACW 64 (2012, cùng M. C. Steenberg)**; Unger mất năm 1982 nên các quyển sau do John J. Dillon biên tập xuất bản. Khoảng năm "1992–2012" ghi đúng.
- **Bart D. Ehrman, *Lost Christianities* (2003)** ✓ Oxford University Press, 2003, đúng chủ đề.

**Nghi vấn — "ông **đặt ra** ba công cụ"**
Trong ba công cụ, chỉ cái thứ nhất mới thật sự là của ông. Hai cái còn lại đã có trước:
- **Truyền thừa tông đồ**: người lập danh sách kế vị ở Rome **trước Irenaeus là Hegesippus, k. 160** (Eusebius còn giữ lại). Irenaeus là người **dùng** nó làm vũ khí biện luận, không phải người nghĩ ra nó.
- **Bản tóm tắt đức tin (*regula fidei* / "quy luật chân lý")**: dạng sơ khai đã có trong các tác giả trước và trong công thức rửa tội.
Đề xuất: *"...ông **gom lại và biến thành vũ khí biện luận** ba công cụ... — một quy điển gồm đúng bốn sách Phúc Âm, cái duy nhất trong ba cái thật sự bắt đầu từ ông; nguyên tắc truyền thừa từ các tông đồ, vốn đã được Hegesippus lập danh sách trước đó; và một bản tóm tắt đức tin làm thước đo."*

**Nghi vấn — "phần lớn văn bản của họ đã mất cho tới khi tìm thấy kho Nag Hammadi năm 1945"**
Đúng về đại thể nhưng bỏ mất ba bộ pháp điển Ngộ đạo **đã biết trước 1945**, và chính chúng là nền của nghiên cứu Ngộ đạo học thế kỷ 19: **Askew Codex** (Pistis Sophia), **Bruce Codex**, và **Berlin Codex 8502** (mua ở Cairo tháng 1/1896, chứa *Apocryphon of John* và *Gospel of Mary*). Nag Hammadi mở rộng kho tư liệu gấp nhiều lần, nhưng không phải là "trước đó không có gì".
Đề xuất: *"...vì ngoài ba bộ pháp điển lẻ đã biết từ thế kỷ 19, phần lớn văn bản của họ chỉ xuất hiện trở lại khi tìm thấy kho Nag Hammadi năm 1945."*

**Nghi vấn (luận điểm gây tranh cãi được viết như sự kiện) — "Marcion ... chính là thứ buộc phía bên kia phải trả lời"**
Đây là **luận đề Harnack** về việc quy điển của Marcion ép phía chính thống phải lập quy điển đối lại. Luận đề này có trọng lượng nhưng **đang bị tranh luận**: một dòng nghiên cứu cho rằng tập hợp bốn Phúc Âm đã hình thành độc lập với Marcion. Viết "chính là thứ buộc" là chọn một bên mà không nói ra — ngược với yêu cầu trung lập của prompt §Ngôn ngữ.
Đề xuất: *"...và Marcion, người lập quy điển riêng mà nhiều học giả coi là áp lực buộc phía bên kia phải trả lời."*

## 10. `CH04-CE02-10` · Tertullian

**Đúng — câu "tôi tin vì phi lý" (kiểm kỹ theo yêu cầu)**
Mệnh đề của mục **đứng được**: công thức *credo quia absurdum* **không có trong bất kỳ văn bản nào của Tertullianô**. Nó là cách diễn giải lại của thời cận đại.
Nhưng mục **bỏ mất chỗ làm cho lời đính chính có sức nặng**: cái thật sự có trong *De carne Christi* 5.4 là **"prorsus credibile est, quia ineptum est"** ("điều ấy hoàn toàn đáng tin, chính vì nó lố bịch") và **"certum est, quia impossibile"** ("chắc chắn, vì bất khả"). Thiếu hai câu này thì người đọc không hiểu vì sao câu gán sai kia lại dai dẳng đến thế. Thêm nữa, điểm đính chính quan trọng hơn **không phải là từ ngữ mà là nghĩa**: Tertullianô không đang kể trạng thái tâm lý của mình ("tôi tin vì…") mà đang lập luận chống phái Ngộ đạo rằng chính sự nhục nhã và bất khả của việc nhập thể và phục sinh là bằng chứng cho tính có thật của chúng. Eric Osborn kết luận rằng công thức ấy, **kể cả khi được sửa lại thành *quia ineptum*, vẫn không phản ánh tư tưởng Tertullianô**.
Đề xuất: *"Câu 'tôi tin vì phi lý' thường bị gán cho ông không có trong văn bản nào của ông. Cái ông thật sự viết, trong De carne Christi, là 'đáng tin, chính vì lố bịch' và 'chắc chắn, vì bất khả' — và đó không phải lời thú nhận về đức tin của mình mà là một nước cờ biện luận chống phái Ngộ đạo."*

**Sai — "trinitas, persona, substantia, sacramentum **đều đi vào tiếng Latinh qua ông**"**
Chỉ đúng với **trinitas** (cùng *trias*), là từ ông thật sự tạo ra cho nghĩa thần học. Ba từ còn lại **đã có sẵn trong tiếng Latinh cổ điển từ lâu trước ông**:
- ***persona***: mặt nạ diễn viên, rồi vai kịch, rồi "nhân thân" trong luật và trong tu từ — dùng rộng rãi từ thời Cicero. Tertullianô lấy nó từ **thực hành chú giải theo vai nói (*prosopographical exegesis*)** của các nhà văn phạm và tu từ, rồi gán nghĩa thần học.
- ***substantia***: đã là từ Latinh thường dùng (kể cả ở Seneca và Quintilianus) trước khi ông dùng nó dịch *ousia*.
- ***sacramentum***: trong Latinh cổ điển là **lời thề quân ngũ** và khoản ký quỹ trong một vụ kiện; ông chuyển nó sang dịch *mystērion*.
Cái ông làm — và nó vẫn rất lớn — là **gán nghĩa thần học mới cho các từ Latinh có sẵn**, cộng với một số từ tự tạo. Viết "đều đi vào tiếng Latinh qua ông" là biến ba lần chuyển nghĩa thành bốn lần sáng tạo từ.
Đề xuất: *"...ông phải tự dựng: *trinitas* là từ ông tạo ra, còn *persona*, *substantia*, *sacramentum* là những từ Latinh đã có — mặt nạ sân khấu, bản thể, lời thề quân ngũ — được ông gán nghĩa thần học mới. Bộ nghĩa ấy rồi đi vào các ngôn ngữ châu Âu."*
(Lưu ý: dòng "Ảnh hưởng tới → Từ vựng thần học Latinh · kế thừa · **trực tiếp**" vẫn đứng được sau khi sửa.)

**Đúng, kiểm được:** *Apologeticum* viết theo dạng bài bào chữa trước toà ✓ · lập luận việc xử người Kitô hữu vi phạm chính nguyên tắc tố tụng La Mã ✓ (Apol. 2, dựa trên thư Pliny – Trajan) · cuối đời ngả sang phái Montanus ("Tân Tiên tri") ✓ · **Cyprianô thành Carthage** được khai báo đúng là "ở thế hệ sau" ✓ và **không có mục riêng** ✓ · **Minucius Felix** cũng không có mục riêng ✓ · liên kết `CH03-BCE01-03` Cicero và `CH04-CE02-09` Irenaeus đều trỏ đúng người và hợp lý (Tertullianô dùng *Adversus Haereses* trong *Adversus Valentinianos*) ✓ · **Geoffrey D. Dunn, *Tertullian* (2004)** ✓ tồn tại (Routledge, loạt The Early Church Fathers), đúng năm, đúng thể loại (chuyên khảo).

**Nghi vấn — "Minucius Felix ... cùng vùng cùng thời"**
Thứ tự giữa *Octavius* của Minucius Felix và *Apologeticum* **chưa ngã ngũ**: có phái đặt Minucius trước Tertullianô, có phái đặt sau, chênh nhau có thể tới nửa thế kỷ. Và *Octavius* lấy bối cảnh ở **Ostia**, tác giả thường được coi là hoạt động ở Rome; gốc Bắc Phi là suy đoán. Nói "cùng vùng cùng thời" là khẳng định hai điều mà **không kiểm được**.
Đề xuất: *"Ứng viên gần nhất là Minucius Felix, cũng viết biện giáo Latinh nhưng không rõ trước hay sau ông, và Cyprianô thành Carthage ở thế hệ sau."*

**Nghi vấn — lĩnh vực `Luật`**
Việc Tertullianô là luật gia dựa trên việc đồng nhất ông với một "Tertullianus" được trích trong *Digesta*. Phép đồng nhất ấy **đã bị học giới bác** (từ T. D. Barnes, *Tertullian*, 1971). Cái chắc chắn là ông được đào tạo **tu từ** và viết theo **khuôn pháp lý**, không phải ông hành nghề luật. Gán hẳn lĩnh vực `Luật` là đi xa hơn bằng chứng; nên cân nhắc đổi sang `Văn học` hoặc để một lĩnh vực.

**Thể thức (nhỏ) — tên không nhất quán trong cùng một mục**
Đầu mục ghi **"Tertullian"**, nhưng văn xuôi mục "Vì sao chọn" và dòng Nguồn ghi **"Tertullianô"**; Ghi chú biên tập (dòng ~1007) cũng ghi "Tertullianô". Chọn một dạng. Theo prompt §Ngôn ngữ ("dùng tên tiếng Việt phổ biến nếu có"), dạng Việt hoá **Tertullianô** hợp hơn cho đầu mục, với `(Quintus Septimius Florens Tertullianus)` giữ nguyên trong ngoặc.

**Thiếu — dòng Nguồn**
`Tertullianô, Apologeticum` không ghi bản dịch, nhà xuất bản hay năm. Mọi mục khác trong nhóm đều ghi bản dịch cho nguồn sơ cấp (Toomer, Brock, Johnston, Garfield, Unger, Hard). Nên bổ sung một bản cụ thể để dòng Nguồn dùng được.

## 11. `CH04-CE02-11` · Trương Trọng Cảnh

**Đúng, kiểm được:** lời tựa kể dòng họ hơn hai trăm người chết quá nửa trong mười năm, phần lớn vì thương hàn ✓ (đúng nội dung tự tự của Thương hàn tạp bệnh luận) · phân thành **sáu kinh** (六經) ✓ · mỗi chứng ứng một phương cụ thể ✓ · là khung lâm sàng còn dùng ở Trung – Nhật – Triều – Việt ✓ (phái Cổ phương 古方派 của Kampo Nhật Bản dựng thẳng trên bộ này) · "Tiểu sử ông không có trong chính sử, nên niên đại để Thấp" ✓ **đúng và là một câu rào tốt** — không có truyện riêng trong Hậu Hán thư hay Tam quốc chí · **Hoa Đà** (k. 140–208) là ứng viên **cùng thời thật**, đúng việc được gán (ngoại khoa, ma phí tán), **không có mục riêng** ✓ · **Hoàng Phủ Mật** (215–282, *Châm cứu giáp ất kinh*) được khai báo đúng là "ở thế kỷ sau" ✓, không có mục riêng ✓ · **Paul U. Unschuld, *Medicine in China: A History of Ideas*** ✓ tồn tại, **2010 là năm bản 2 có sửa chữa** (University of California Press; bản 1 năm 1985) — ghi 2010 là hợp lệ, đúng thể loại (chuyên khảo), đúng chủ đề.

**Sai — "văn bản của ông còn lại và được chú giải liên tục mười tám thế kỷ"**
Cả hai vế đều không đứng được như đang viết:
1. **"Văn bản của ông còn lại"** — không trực tiếp. *Thương hàn tạp bệnh luận* bản gốc **thất tán**; cái còn lại là bản **Vương Thúc Hoà (王叔和)** thu thập và sắp xếp lại ở đời Tấn (k. thế kỷ 3), rồi bản hiệu đính của **Hiệu chính y thư cục** đời Bắc Tống: **năm 1065** Cao Bảo Hành, Lâm Ức và Tôn Kỳ tách bộ sách làm hai — ***Thương hàn luận*** và ***Kim quỹ yếu lược*** — và in lại năm 1088. Dòng Nguồn của mục ghi "Trương Trọng Cảnh, *Thương hàn luận*" chính là **sản phẩm của lần tách năm 1065**, không phải tên bộ sách gốc mà văn xuôi đang nói tới.
2. **"chú giải liên tục mười tám thế kỷ"** — truyền thống chú giải bắt đầu muộn hơn rất nhiều: bản chú giải đầy đủ sớm nhất còn lại là của **Thành Vô Kỷ (成無己), in năm 1144**, tức **gần một nghìn năm sau** Trương Trọng Cảnh. Chín thế kỷ đầu không có "chú giải liên tục".
Đề xuất: *"Trương Trọng Cảnh được chọn theo độ bền (b): bộ sách của ông sống sót — qua bản thu thập của Vương Thúc Hoà đời Tấn rồi bản hiệu đính năm 1065 tách thành Thương hàn luận và Kim quỹ yếu lược — và từ Thành Vô Kỷ (1144) trở đi thành đối tượng của một truyền thống chú giải không đứt đoạn, còn kỹ thuật của Hoa Đà thì mất theo người."*

**Nghi vấn — "biện chứng luận trị" là thuật ngữ hiện đại áp ngược**
辨證論治 (*biện chứng luận trị*) được chuẩn hoá thành khẩu hiệu của Trung y **ở thế kỷ 20**, trong quá trình định chế hoá y học cổ truyền tại Trung Quốc. Trương Trọng Cảnh không dùng từ này. Viết "ông đưa ra lối biện chứng luận trị" là gán cho một văn bản thế kỷ 2–3 một nhãn thế kỷ 20 — chính là loại "câu chuyện tiến bộ" mà phần đầu `prompts/atlas-prompt.md` yêu cầu tránh.
Đề xuất: giữ **mô tả** (không chữa theo tên bệnh mà theo chứng hậu đang biểu hiện, phân sáu kinh) và bỏ hoặc rào thuật ngữ: *"...lối chữa về sau được Trung y hiện đại gọi là biện chứng luận trị: không chữa theo tên bệnh mà..."*

**Sai — liên kết `- CH90-CE19_20-09 · kế thừa · qua trường phái` (Tôn Thất Tùng)**
Đã mở mục đích ra đọc. `CH90-CE19_20-09` là **Tôn Thất Tùng (1912–1982)**, phẫu thuật viên gan đào tạo theo y học phương Tây; toàn bộ mục nói về kỹ thuật cắt gan có kế hoạch công bố trên *The Lancet* năm 1963 và về chất độc da cam. **Không có gì liên quan tới Thương hàn luận hay y học cổ truyền.** Dòng "Kế thừa từ" của mục ấy là **Hồ Đắc Di** và `CH90-CE15_18-09`, không có Trương Trọng Cảnh.

Lint chỉ báo một dòng **[INFO]** bất đối xứng (`reports/lint-ch04.txt:35`) kèm ghi chú "P4 sẽ đồng bộ" — tức **nếu đồng bộ tự động, nó sẽ viết một quan hệ sai vào mục Tôn Thất Tùng.** Phải xoá trước.

**Đích đúng đã có sẵn trong atlas:** `CH90-CE15_18-09` · **Lê Hữu Trác (Hải Thượng Lãn Ông, 1724–1791)**, mà mục mô tả thẳng là "không chép lại y thư Trung Hoa mà hiệu chỉnh theo khí hậu, thể chất và dược liệu bản địa". Đó mới là chỗ ảnh hưởng của Trương Trọng Cảnh chạm vào Việt Nam.
Đề xuất: thay `- CH90-CE19_20-09 · kế thừa · qua trường phái` bằng `- CH90-CE15_18-09 · kế thừa · qua trường phái`.

## 12. Độ phủ lĩnh vực / vùng / câu hỏi lớn của nhóm

**Lĩnh vực** (9 giá trị khác nhau, trần §5 là ≥4 → **đạt**): Kỹ thuật/Công nghệ ×2 · Khoa học tự nhiên ×2 · Chính trị/Nhà nước ×2 · Tôn giáo/Tâm linh ×5 · Văn học ×1 · Khám phá/Địa lý ×1 · Y học ×2 · Triết học ×2 · Luật ×1.
Vắng: Toán học, Quân sự, Kinh tế, Sử học, Nghệ thuật/Kiến trúc, Giáo dục, Ngôn ngữ học.
Nhận xét: Tôn giáo/Tâm linh chiếm 5/11 — Ghi chú biên tập của chapter đã tự nhận và giải thích thiên lệch này ở cấp chapter, đó là cách xử lý đúng. Nhưng **`Luật` chỉ xuất hiện một lần, và chính cái nhãn đó (`-10` Tertullianô) lại là nhãn tôi nghi ngờ nhất** (xem §10). Nếu bỏ nhãn `Luật` ở `-10` thì nhóm mất hẳn lĩnh vực này — xem đề xuất ở §13.

**Vùng** (4 giá trị, trần §5 là ≥3 → **đạt**): Đông Á ×3 · Nam Á ×3 · Châu Âu ×3 · Trung Đông/Bắc Phi ×2.
Vắng: Trung Á, Đông Nam Á, Châu Phi hạ Sahara, Châu Mỹ, Châu Đại Dương.
**Đáng nói:** nhóm **không có mục Trung Á nào**, trong khi `-03` Kanishka là cơ hội duy nhất — đế chế Kushan có trọng tâm ở Bactria/Trung Á và chính dòng Bối cảnh mở đầu bằng "Đế chế Kushan nối **Trung Á** với Ấn Độ". Ghi `Nam Á` theo kinh đô Purushapura là một lựa chọn bảo vệ được, nhưng nó **không được khai báo** ở đâu cả, khác hẳn với cách Ch3 khai báo rõ quy ước vùng cho thế giới Hellenistic. Nên thêm một dòng trong Ghi chú biên tập nói rõ đã cân nhắc và vì sao chọn Nam Á.

**Câu hỏi lớn**: Vũ trụ ×2 · Con người ×3 · Thực tại ×1 · Không áp dụng ×5. Cả bốn giá trị đều xuất hiện, không ai quá 2 ✓.

## 13. Đánh giá lựa chọn nhân vật

Nhóm có **11/12**, tức **còn một chỗ trống** — nên câu hỏi không phải "loại ai" mà "còn thiếu ai". Tôi đã đối chiếu toàn bộ danh sách "Ứng viên mạnh đã bị loại" ở Ghi chú biên tập Ch4 với giai đoạn 101–200 CN để tách ra những người **chưa từng được cân nhắc ở bất kỳ đâu** (không có mục, không nằm trong danh sách bị loại, không được nêu trong "Vì sao chọn" của ai).

### Ứng viên số 1 — Trương Đạo Lăng (張道陵), lập Thiên Sư đạo năm 142 CN

**Đây là một lỗ hổng do chính chapter tự tạo ra.** Giới thiệu chapter (`content/ch04.md`, dòng 2) viết:
> "Câu trả lời xuất hiện gần như đồng thời ở nhiều nơi dưới dạng tôn giáo có giáo lý thành văn và tăng đoàn xuyên biên giới — Kitô giáo, Phật giáo Đại thừa, Manichaeism, **Đạo giáo có tổ chức**."

Ba trong bốn tôn giáo ấy có người đại diện trong atlas. **Đạo giáo có tổ chức thì không có ai** — không một mục nào, ở bất kỳ chapter nào. Grep toàn bộ `content/`: "Trương Đạo Lăng", "Thiên Sư", "Trương Giác", "Khăn Vàng" đều **0 lần xuất hiện**. Tức nhân vật này chưa từng được cân nhắc rồi loại; ông đơn giản là không có trong tầm nhìn.

Lập luận theo bốn tiêu chí:
- **(a) phạm vi** — Thiên Sư đạo (còn gọi Ngũ Đấu Mễ đạo) là **phong trào Đạo giáo có tổ chức đầu tiên**, và phần áp đảo đạo sĩ không xuất gia ở Trung Quốc lẫn trong cộng đồng người Hoa hải ngoại tới nay vẫn tự nhận thuộc truyền thống này.
- **(b) độ bền** — gần **mười chín thế kỷ liên tục**, và hiện vẫn còn một vị Thiên Sư tự nhận là hậu duệ trực hệ. Đây là độ bền thể chế ngang hàng với bất kỳ ai trong nhóm.
- **(c) tính nguyên bản** — bước đi của ông không phải là tư tưởng mà là **hình thức tổ chức**: giáo phẩm (tế tửu), lễ nhập đạo, văn bản bí truyền trao cho người thụ pháp, và thu "ngũ đấu mễ" để nuôi bộ máy. Đây là lần đầu tư tưởng Đạo gia (Lão Tử, đã có mục `CH02-...`) chuyển thành một **giáo hội**. Đúng kiểu đóng góp mà atlas đã thưởng cho Irenaeus ở `-09` (ba công cụ tổ chức, không phải một học thuyết mới).
- **(d) counterfactual** — không có bước thiết chế hoá này thì "Đạo giáo" ở lại dạng văn bản triết học và kỹ thuật dưỡng sinh; mọi thứ đi sau (nhà nước thần quyền Hán Trung của Trương Lỗ, Đạo giáo nhà Đường, Toàn Chân, Chính Nhất) đều đi qua nó.

Về niên đại và tính lịch sử: mốc **142 CN** (Lão Tử giáng ở núi Hạc Minh) nằm gọn trong 101–200, và **bằng chứng cứng sớm nhất là tấm bia năm 173 CN** ghi việc thụ pháp cho một nhóm tế tửu mới, gọi đích danh *Thiên Sư đạo pháp* — tức phong trào chắc chắn đã tồn tại có tổ chức trong thế kỷ 2. Bản thân Trương Đạo Lăng thì ranh giới giữa người thật và truyền thuyết rất mờ, nhưng **prompt §Quy tắc chọn nhân vật điều 8 cho phép đúng trường hợp này**: gắn nhãn `[Tranh cãi lịch sử]` ngay sau tên, đặt `độ tin cậy niên đại: Thấp`.
*Nếu muốn một nhân vật chắc chắn có thật hơn*, phương án thay là **Trương Lỗ (張魯, mất 216)**, cháu ông, người cai trị nhà nước thần quyền Hán Trung — nhưng Trương Lỗ hoạt động chính ở 190–215, nên thuộc ranh CE02/CE03 và yếu hơn ở tiêu chí (c).

Lợi ích phụ: mục này lấp luôn hai lỗ của nhóm — nó cho Đông Á một đại diện **tôn giáo** (hiện Đông Á chỉ có kỹ thuật và y học), và nó làm cho câu mở đầu chapter không còn là một lời hứa không được thực hiện.

### Ứng viên số 2 — Gaius, nhà luật học La Mã (hoạt động k. 130–180), *Institutiones* k. 161 CN

Cũng **chưa từng được cân nhắc**: mọi lần xuất hiện của chữ "Gaius" trong `content/` đều là praenomen của người khác (Gaius Gracchus, Gaius Iulius Caesar, Gaius Plinius, Gaius Aurelius Valerius Diocletianus).

- **(a)(b)** — *Institutiones* là **tác phẩm luật học cổ điển La Mã duy nhất còn lại gần như trọn vẹn**, và nó là **khuôn mẫu trực tiếp** cho *Institutiones* của Justinianus (533), nhiều đoạn chép thẳng. Qua đó, sơ đồ ba phần của ông — **personae / res / actiones** (người, vật, tố quyền) — thành bộ xương của mọi bộ dân luật châu Âu lục địa, Bộ luật Napoléon, và các hệ dân luật ở Mỹ Latinh, Nhật Bản, Trung Quốc và Việt Nam.
- **(c)** — chính **sơ đồ phân loại** ấy là phát kiến, không phải một quy tắc lẻ nào.
- **(d)** — có người gọi ông là "kiến trúc sư thật sự" của bộ sưu tập Justinianus; không có *Institutiones*, việc tái lập luật cổ điển cho đời sau mất đi cái sườn duy nhất còn nguyên.
- Một chi tiết hợp với tinh thần của atlas: văn bản của ông **mất hẳn** cho tới năm **1816**, khi tìm được bản chép đè (palimpsest, Codex Veronensis, chép k. năm 500) ở Verona dưới lớp chữ của Hieronymus.

Và về mặt cơ cấu: lĩnh vực `Luật` hiện chỉ xuất hiện **một lần** trong nhóm, ở chỗ tôi cho là gán sai (`-10` Tertullianô, xem §10). Gaius lấp chỗ ấy bằng một ca không thể bàn cãi.

### Xếp hạng và khuyến nghị

Chỗ trống chỉ có một. Tôi xếp **Trương Đạo Lăng trước Gaius**, vì:
- nó sửa một **mâu thuẫn nội bộ** (giới thiệu chapter hứa bốn tôn giáo, giao ba);
- nó cân lại thiên lệch vùng–lĩnh vực nặng hơn (Đông Á hiện không có mục tôn giáo nào trong cả chapter ở giai đoạn này);
- tiêu chí (b) của nó — mười chín thế kỷ thể chế liên tục — mạnh hơn hầu hết mục đang có trong nhóm.

Gaius nên được **ghi vào danh sách "Ứng viên mạnh đã bị loại"** của Ghi chú biên tập với lý do rõ ràng, thay vì tiếp tục vô hình. Theo CONTRIBUTING, một ứng viên chưa từng được nêu tên thì không thể nói là "đã cân nhắc".

### Hai ứng viên nhỏ hơn, nêu để Ghi chú biên tập có chỗ dựa
- **Rudradāman I** (trị vì k. 130–150, Tây Kṣatrapa): bia Junagadh k. 150 CN, văn bia Sanskrit chuẩn sớm nhất còn lại, mở đầu việc Sanskrit thay Prakrit làm ngôn ngữ của văn khắc công quyền ở Nam Á. Liên quan trực tiếp tới mệnh đề "kāvya sớm nhất" ở `-04` (xem §4), nên dù không chọn thì cũng nên nêu tên.
- **Lucian xứ Samosata** (k. 125–180) hoặc **Apuleius** (k. 124–170): hai ca duy nhất có thể bổ sung lĩnh vực `Văn học` **phi tôn giáo** cho nhóm, hiện `Văn học` chỉ có một mục và nó là thơ Phật giáo. Cả hai đều chưa từng được nêu.

## 14. Bảng tổng hợp

| # | Mục | Loại | Vấn đề |
|---|---|---|---|
| 1 | `-01` | **Sai** | "không người thợ hay quan chế tác nào khác của nhà Hán để lại tên gắn với một kỹ thuật cụ thể" — phản ví dụ: Tất Lam, Đỗ Thi, Đinh Hoãn, **và chính `-02` Trương Hành** |
| 2 | `-01` | Thể thức | hệ quả: mục không nêu được ứng viên bị loại nào dù có sẵn |
| 3 | `-01` | Nghi vấn | "sớm hơn hai thế kỷ" — thực tế gần ba thế kỷ (Phóng Mã Than, 179–141 TCN) |
| 4 | `-01` | Thiếu | chặng truyền giấy sang phía tây không có nguồn đương thời, mức `qua trường phái` quá mạnh |
| 5 | `-02` | **Sai** | "không có hậu duệ trực tiếp" — có *Khí chuẩn* (Tín Đô Phương) và *Địa động đồng nghi kinh* (Lâm Hiếu Cung) |
| 6 | `-02` | Thể thức | không ứng viên nào thật sự cùng thời; Giả Quỳ (k. 103) là lựa chọn đúng |
| 7 | `-02` | Nghi vấn | `Kế thừa từ` Đổng Trọng Thư — đúng ID, sai nội dung |
| 8 | `-02` | Nghi vấn | pi: ông có nhiều giá trị, không chỉ √10 |
| 9 | `-03` | **Sai** | nguồn *L'art du Gandhara* / Vincent Lefèvre (2010) **không tồn tại** — đúng phải là Pierre Cambon (dir.), *Pakistan, terre de rencontre… Les arts du Gandhara* (2010) |
| 10 | `-03` | Nghi vấn | "Gandhāra … định hình mọi hình tượng Phật về sau" — bỏ qua Mathurā, vấn đề chưa ngã ngũ |
| 11 | `-03` | Nghi vấn | biên độ tranh luận "78 tới 144" hẹp hơn thực tế (**không kiểm được** cận trên chính xác) |
| 12 | `-03` | Nghi vấn | liên kết tới `-04` để mức `trực tiếp` dù cả hai đầu niên đại Thấp |
| 13 | `-04` | **Sai** | Nanda là **em cùng cha khác mẹ**, không phải "em họ" |
| 14 | `-04` | **Sai** | "kāvya **hoàn chỉnh** sớm nhất" — Buddhacarita chỉ còn 14/28 phẩm Sanskrit; chính dòng Nguồn (Johnston) nói điều đó |
| 15 | `-04` | **Sai** | "Kālidāsa … được chọn ở chapter này theo nhóm khác" — **không có mục nào**, và Ghi chú biên tập dòng ~993 ghi ông là ứng viên **bị loại** |
| 16 | `-05` | **Sai** | chu vi Trái Đất quá nhỏ là của **Posidonius** (qua Marinus), không phải ước lượng của Ptolemy — và `CH03-BCE01-12` trong chính atlas đã ghi đúng |
| 17 | `-05` | Thiếu | bản đồ Geographia không còn từ thời cổ; Phục hưng dựng lại từ danh mục toạ độ |
| 18 | `-06` | **Sai** | "cho tới khi Vesalius **mổ xác người** năm 1543" — mổ xác người đã có từ Mondino, k. 1315; 1543 là năm xuất bản *Fabrica* |
| 19 | `-06` | Thiếu | "một phần đáng kể" → con số thật là **~10% văn chương Hy Lạp còn lại trước năm 350 CN** |
| 20 | `-06` | Nghi vấn | `độ tin cậy: Cao` cho năm mất 216 (suy ra, biên độ tới 199); Wikidata chỉ có mức thế kỷ nên lint mù |
| 21 | `-06` | Thể thức | Soranus không chồng lấn sự nghiệp Galen mà không nói ra; Aretaeus không kiểm được niên đại |
| 22 | `-07` | **Sai** | "Suy tưởng không có tiền lệ nào cùng dạng" — **ngược với luận điểm của Hadot**, nguồn số 2 của chính mục (thể *hypomnēmata*, có từ *Memorabilia* của Xenophon) |
| 23 | `-07` | Nghi vấn | Epictetus không phải "người thầy" — hai người chưa từng gặp; thầy là Rusticus |
| 24 | `-08` | **Sai** | liên kết `CH90-CE10_14-04` (Lý Thái Tổ) vô căn cứ; lint chỉ báo INFO và **P4 đồng bộ tự động sẽ nhân bản lỗi** |
| 25 | `-08` | Nghi vấn | "phái Trung quán … nền chung của Đại thừa ở Đông Á" — Tam Luận tông suy tàn sau Đường |
| 26 | `-08` | Nghi vấn | Garfield (1995) dịch từ **bản Tạng** và kèm bình giải — nên ghi rõ thể loại |
| 27 | `-09` | Nghi vấn | "ông **đặt ra** ba công cụ" — truyền thừa tông đồ đã có ở Hegesippus (k. 160) |
| 28 | `-09` | Nghi vấn | trước 1945 đã biết Askew, Bruce và Berlin Codex 8502 (1896) |
| 29 | `-09` | Nghi vấn | luận đề Harnack về Marcion viết như sự kiện |
| 30 | `-10` | **Sai** | *persona*, *substantia*, *sacramentum* **đã có trong Latinh cổ điển**; chỉ *trinitas* là từ ông tạo |
| 31 | `-10` | Thiếu | mệnh đề "credo quia absurdum" **đúng**, nhưng thiếu cái ông thật sự viết (*De carne Christi* 5.4) nên lời đính chính mất sức |
| 32 | `-10` | Nghi vấn | Minucius Felix "cùng vùng cùng thời" — cả hai đều không kiểm được |
| 33 | `-10` | Nghi vấn | lĩnh vực `Luật` dựa trên phép đồng nhất đã bị Barnes (1971) bác |
| 34 | `-10` | Thể thức | tên không nhất quán: "Tertullian" ở đầu mục, "Tertullianô" trong thân mục |
| 35 | `-11` | **Sai** | liên kết `CH90-CE19_20-09` (Tôn Thất Tùng) vô căn cứ — đích đúng là `CH90-CE15_18-09` Lê Hữu Trác |
| 36 | `-11` | **Sai** | "văn bản của ông còn lại và được chú giải **liên tục mười tám thế kỷ**" — bản còn lại là của Vương Thúc Hoà + hiệu đính 1065; chú giải bắt đầu với Thành Vô Kỷ **1144** |
| 37 | `-11` | Nghi vấn | "biện chứng luận trị" là thuật ngữ Trung y thế kỷ 20 áp ngược lên văn bản thế kỷ 2 |
| 38 | Bối cảnh | Nghi vấn | y học không được tổng hợp "ở Pergamon" mà ở **Rome** |
| 38b | Bối cảnh | Thể thức | 61 chữ, vượt trần ≤ 60 của template §5 |
| 39 | nhóm | Thiếu | không có mục Trung Á dù Bối cảnh mở bằng "Kushan nối Trung Á…"; quy ước vùng cho Kanishka không được khai báo |
| 40 | nhóm | Thiếu | chỗ trống thứ 12: **Trương Đạo Lăng** (và **Gaius**) chưa từng được cân nhắc |

**Thống kê:** 12 lỗi **Sai** · 17 **Nghi vấn** · 6 **Thiếu** · 6 **Thể thức**.
Trong đó **4 lỗi có thể bắt bằng cách đối chiếu nội bộ atlas, không cần nguồn ngoài**: #1 (`-01` vs `-02`), #15 (`-04` vs Ghi chú biên tập), #16 (`-05` vs `CH03-BCE01-12`), #14 (`-04` vs dòng Nguồn của chính nó). Và **2 lỗi (#24, #35) sẽ bị nhân đôi nếu P4 chạy đồng bộ liên kết tự động theo các dòng INFO ở `reports/lint-ch04.txt`** — nên xử lý hai dòng ấy trước khi đồng bộ.
