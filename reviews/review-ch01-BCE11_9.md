# Bình duyệt độc lập — Chapter 1, nhóm BCE11_9 (TK 11–9 TCN)

Phạm vi: `content/ch01.md`, dòng `**Bối cảnh**` của nhóm BCE11_9 và 12 mục `CH01-BCE11_9-01` → `-12`.
Người duyệt: agent độc lập, không viết chapter. Ngày: 2026-10-31.
Xếp loại: **Sai** (khẳng định sai sự thật) · **Nghi vấn** (gây tranh cãi / không quy thuộc / thiếu dè dặt) · **Thiếu** (thiếu thông tin bắt buộc) · **Thể thức** (vi phạm template §5 / CONTRIBUTING).

Kết quả đối chiếu Wikidata (nhãn EN, API `wbgetentities`): **cả 12 Q-ID đều trỏ đúng nhân vật.**

| ID | Q-ID | Nhãn Wikidata EN | Khớp |
|---|---|---|---|
| -01 | Q296295 | Tiglath-Pileser I | ✓ |
| -02 | Q1061289 | King Wu of Zhou | ✓ |
| -03 | Q468747 | Dan of Zhou | ✓ |
| -04 | Q41370 | David | ✓ |
| -05 | Q37085 | Solomon | ✓ |
| -06 | Q467115 | Hiram I | ✓ (nhưng xem lỗi tên gốc ở mục -06) |
| -07 | Q311811 | Shoshenq I | ✓ |
| -08 | Q193290 | Ashurnasirpal II | ✓ |
| -09 | Q211928 | Shalmaneser III | ✓ |
| -10 | Q133507 | Elijah | ✓ |
| -11 | Q350258 | Mesha | ✓ |
| -12 | Q211326 | Lycurgus of Sparta | ✓ |

Nhắc lại cảnh báo của `CONTRIBUTING.md` §4: khớp Wikidata là sàn, không phải trần. Mọi lỗi dưới đây đều là lỗi mà lint và đối chiếu Wikidata **không** bắt được.

## Bảng tổng hợp phát hiện

**12 Sai · 18 Nghi vấn · 4 Thiếu · 7 Thể thức** trên 12 mục + dòng Bối cảnh. Không mục nào sạch hoàn toàn.

| Mục | Sai | Nghi vấn | Thiếu | Thể thức | Lỗi nặng nhất |
|---|:-:|:-:|:-:|:-:|---|
| Bối cảnh | 1 | 1 | – | – | "mở đường cho chữ viết ghi âm" — chữ ghi âm có trước hơn 1000 năm |
| -01 Tiglath-Pileser I | 1 | 2 | – | – | gán vai trò của **danh sách niên quan** cho **biên niên** |
| -02 Chu Vũ Vương | – | 1 | – | 1 | "Vì sao chọn" không so sánh với ứng viên đã nêu |
| -03 Chu Công Đán | 2 | 2 | – | – | dẫn **Thiệu cáo** (lời của Thiệu Công Thích) làm chứng cứ cho Chu Công; "Khổng Tử... không phải vị vua nào" sai với Luận ngữ 8.19 |
| -04 David | 2 | 2 | 1 | – | "chỉ có một dòng Tel Dan" mâu thuẫn với nguồn của chính mục -11 |
| -05 Solomon | 1 | 1 | – | 1 | tập trung hoá phụng tự là của **Hezekiah/Josiah**, không phải Solomon |
| -06 Hiram I | 1 | 1 | – | 2 | **"Ahiram xứ Tyre"** — trộn vua Tyre với vua Byblos |
| -07 Shoshenq I | – | 1 | – | 1 | danh sách Karnak **không nhắc Jerusalem**, nên không phải "điểm chạm trực tiếp" |
| -08 Ashurnasirpal II | 2 | – | – | – | "tự sự bằng hình đầu tiên ở quy mô kiến trúc" — phản ví dụ nằm ngay trong atlas (Ramesses II, Ramesses III, Zimri-Lim) |
| -09 Shalmaneser III | 1 | 1 | 1 | – | nguồn **sai tập, sai năm**: phải là RIMA 3 (1996), không phải RIMA 2 (1991) |
| -10 Elijah | – | 2 | 1 | 1 | Nathan bị gọi là "thế hệ trước" dù cách 130–150 năm |
| -11 Mesha | 1 | 2 | 1 | – | "tiếng nói trực tiếp duy nhất của một vương quốc Transjordan" — Ammon có bi ký riêng |
| -12 Lycurgus | – | 2 | – | 1 | – (mục kiểm được tốt nhất nhóm; câu Plutarch **đúng nguyên văn**) |

**Những chi tiết đã kiểm và ĐÚNG** (nêu ra để lần sửa sau không động vào nhầm): 12/12 Q-ID; bia Tel Dan k. 840 TCN; Finkelstein & Silberman *David and Solomon* (2006); 1 V chương 5 và 9 cho Hiram; ~150 vòng tên ở Cổng Bubastite; **69.574 khách / 10 ngày** của Ashurnasirpal II; Qarqar 853 TCN; Layard **1846**; **BM 118885**; Mesha **1868 / Dhiban / Louvre AO 5066**; Lemaire **BAR 20:3 (1994), tr. 30–37**; 1 V 17–19 và 21 cho Elijah; Sweeney *I & II Kings* (2007); Cartledge *Sparta and Lakonia* (2002); câu mở đầu *Lycurgus* 1.1 của Plutarch.


---

## Dòng `**Bối cảnh**` của nhóm

**Nguyên văn:** "Sau sụp đổ, sắt thay đồng và các vương quốc nhỏ mọc lên ở Levant. Assyria hồi phục rồi bành trướng bằng quân sự có tổ chức. Nhà Chu thay nhà Thương và đưa ra học thuyết thiên mệnh. Bảng chữ cái Phoenicia lan theo đường biển, **mở đường cho chữ viết ghi âm**."

### [Sai] "mở đường cho chữ viết ghi âm"
- **Cái đúng:** chữ viết ghi âm đã có từ trước đó hơn một nghìn năm — chữ nêm Akkad ghi âm tiết, Linear B ghi âm tiết tiếng Hy Lạp (TK 15–12 TCN), chữ Ai Cập có thành phần ghi phụ âm. Cái mới của Phoenicia **không phải** việc ghi âm, mà là một hệ **ký tự phụ âm (abjad) ít ký hiệu**, dễ học. Hơn nữa bản thân hệ chữ ấy không ra đời trong giai đoạn này: nó đi lên từ chữ Proto-Sinaitic/Proto-Canaanite khoảng TK 18–15 TCN; cái thuộc về TK 11–9 TCN chỉ là **sự lan tỏa**.
- **Câu thay thế đề xuất:** "Bảng chữ cái Phoenicia lan theo đường biển, đưa mô hình chữ viết ít ký hiệu ra khắp Địa Trung Hải."

### [Nghi vấn] "sắt thay đồng"
Quá dứt khoát cho giai đoạn này: đồ đồng vẫn là vật liệu chính cho nhiều công dụng suốt TK 11–9 TCN; sắt phổ biến dần chứ không "thay". Đề xuất: "sắt bắt đầu phổ biến bên cạnh đồng".

---

## CH01-BCE11_9-01 · Tiglath-Pileser I

**Khớp:** Q296295 = Tiglath-Pileser I ✓. Trị vì 1114–1076 TCN ✓ (chuẩn trong học giới). Cha là Ashur-resh-ishi I ✓. Nebuchadnezzar I của Babylon (k. 1125–1104 TCN) có chồng lấn với đầu triều TP I và đúng là đã đánh bại Elam ✓. Vườn cây và sưu tập thú sống mang về từ chiến dịch ✓ (có trong bi ký của ông). Nguồn Grayson, *RIMA 2 = Assyrian Rulers of the Early First Millennium BC I (1114–859 BC)*, 1991 — **đúng tập, đúng năm, và TP I nằm trong phạm vi tập này** ✓.

### [Sai] "nó là nguồn chính cho niên biểu Cận Đông thiên niên kỷ 1 TCN" / "nhờ nó mà niên biểu của cả vùng này dựng lại được"
- **Nguyên văn (Tư tưởng):** "biên niên vua Assyria trở thành khuôn ghi chép mà các vua sau dùng suốt bốn thế kỷ, và **nó là nguồn chính cho niên biểu Cận Đông thiên niên kỷ 1 TCN**."
- **Nguyên văn (Vì sao chọn):** "**nhờ nó mà niên biểu của cả vùng này dựng lại được** — một hệ quả về tư liệu vượt xa phạm vi quân sự của ông."
- **Cái đúng:** xương sống của niên biểu tuyệt đối Cận Đông thiên niên kỷ 1 TCN **không phải biên niên** mà là **danh sách niên quan (limmu/eponym lists)** và các danh sách vua, được neo tuyệt đối vào **nhật thực Bur-Sagale năm 763 TCN** (và đối chiếu với Canon Ptolemy cùng các ghi chép thiên văn Babylon). Biên niên cung cấp **đồng bộ** (synchronism) với các vùng lân cận, chứ không cung cấp khung năm tuyệt đối. Hai thứ này là hai loại tư liệu khác nhau và cả hai cùng tồn tại ở Assyria — gán vai trò của danh sách niên quan cho biên niên là nhầm thể loại tư liệu.
- **Câu thay thế đề xuất:** "...và biên niên ấy, đặt cạnh danh sách niên quan Assyria, cho phép đồng bộ niên đại Assyria với các vùng lân cận."

### [Nghi vấn] "khuôn ghi chép mà các vua sau dùng suốt bốn thế kỷ" — bỏ qua đứt đoạn
- Giữa Ashur-bel-kala (mất k. 1056 TCN) và Adad-nirari II (trị vì 911–891 TCN) **gần như không có biên niên nào còn lại** — một quãng đứt khoảng 150 năm trùng với giai đoạn Assyria suy. Câu "dùng suốt bốn thế kỷ" vẽ ra một mạch liên tục không có. Ngoài ra "bốn thế kỷ" không khớp với mốc nào rõ: tới khi Nineveh sụp (612 TCN) là **năm** thế kỷ, còn chỉ tính Tân Assyria (911–612) là **ba**.
- **Đề xuất:** "...khuôn ghi chép mà các vua Tân Assyria nối lại từ đầu TK 9 TCN và dùng tới khi đế quốc sụp."

### [Nghi vấn] "thể loại ông định hình" — mệnh đề tối cao, nhưng lần này **đứng được**
- Đã tìm phản ví dụ: Adad-nirari I, Shalmaneser I, Tukulti-Ninurta I (TK 14–13 TCN) đều để lại bi ký có tường thuật chiến dịch dài, nhưng **không xếp theo thứ tự từng năm trị vì**. Giới nghiên cứu quy việc hình thành thể loại "annals" cho Tiglath-Pileser I. Mệnh đề giữ được, nhưng vì là mệnh đề tối cao nên **nên quy thuộc**: ví dụ "giới Assyria học quy việc hình thành thể loại này cho ông".

---

## CH01-BCE11_9-02 · Chu Vũ Vương

**Khớp:** Q1061289 = King Wu of Zhou ✓. Trị vì 1046–1043 TCN ✓ (theo Dự án Hạ–Thương–Chu). Trận Mục Dã ✓. Chu 1046–256 TCN là triều đại dài nhất ✓. Thiên **Mục thệ** (牧誓) là thiên "kim văn" (今文) của Thượng thư, đúng là lời thệ trước trận, và đúng là nói "thi hành sự trừng phạt của Trời" (恭行天之罰) ✓ — mục này đã **tránh được** cái bẫy dẫn thiên **Thái thệ** (泰誓), vốn là ngụy thư cổ văn. Đây là chỗ mục làm đúng. Shaughnessy, *Sources of Western Zhou History* (1991), University of California Press — sách có thật, đúng năm, có bàn niên đại chinh phạt ✓.

### [Nghi vấn] Thuật ngữ "thiên mệnh" bị đọc ngược vào Mục thệ
- **Nguyên văn:** "Lời tuyên cáo trước trận, chép trong Thượng thư, **đặt nền cho lập luận ấy**: vua Thương mất tư cách vì bạo ngược, nên việc thay thế là thi hành ý trời chứ không phải phản nghịch."
- **Ghi nhận:** từ 天命 (thiên mệnh) **không xuất hiện** trong Mục thệ; thiên này nói 天之罰 (sự trừng phạt của Trời) và liệt tội Trụ. Chữ "đặt nền" đã dè dặt vừa đủ nên không xếp là Sai, nhưng cần biết rằng học thuyết thiên mệnh dạng hoàn chỉnh nằm ở **các bài cáo** (mục -03), không ở Mục thệ. Ngoài ra, nhiều nhà nghiên cứu xếp Mục thệ muộn hơn chính biến cố nó kể.
- **Đề xuất:** thêm "theo văn bản truyền lại" hoặc "thiên Mục thệ, dạng văn bản còn lại, đã nói...".

### [Thể thức] "Vì sao chọn" không thật sự so sánh với ứng viên đã nêu
- Mục nêu đích danh Chu Văn Vương và Chu Công Đán, rồi chuyển ngay sang bàn **độ tin cậy niên đại**. **Không có câu nào** nói vì sao Vũ Vương vượt Văn Vương theo (a)–(d). Lý do duy nhất đưa ra — "chiến thắng Mục Dã là sự kiện chuyển quyền" — là một khẳng định về tầm quan trọng của biến cố, không phải một lập luận counterfactual (d) ("nếu không có người này, thay đổi có đến muộn hơn đáng kể không").
- **Đề xuất:** "...Văn Vương được truyền thống coi là đã nhận mệnh nhưng chết trước khi ra quân; chính Vũ Vương biến một yêu sách tượng trưng thành chuyển giao quyền lực thực, nên theo counterfactual (d) ông là nút thắt."

---

## CH01-BCE11_9-03 · Chu Công Đán

**Khớp:** Q468747 = "Dan of Zhou" ✓. Loạn Tam giám (三監之亂) ✓. Khổng Tử mơ thấy Chu Công — *Luận ngữ* 7.5 ✓.

### [Sai] Dẫn thiên **Thiệu cáo** (召誥) làm nơi chứa lập luận của **Chu Công Đán**
- **Nguyên văn (Nguồn):** "Thượng thư, các thiên **Khang cáo, Thiệu cáo, Đa sĩ**"; **(Tư tưởng):** "**Các bài cáo trong Thượng thư** dùng chính sự diệt vong của Thương làm chứng cứ cho lập luận ấy".
- **Cái đúng:** **Thiệu cáo** là lời cáo của **Thiệu Công Thích** (召公奭) — nhan đề thiên nói đúng điều đó, và cách đọc phổ thông cũng như cách đọc của Shaughnessy đều lấy Thiệu Công làm người nói chính (có một dòng phản biện cho rằng người nói là Chu Công, nhưng đó là **thiểu số và đang tranh luận**, không phải mặc định). Đáng chú ý hơn: mục này nêu **chính Thiệu Công Thích** làm "ứng viên bị loại", rồi lại dùng bài cáo của ông ta làm chứng cứ cho công trạng tư tưởng của Chu Công. Hai câu trong cùng một mục chống nhau.
- **Khang cáo** (惟命不于常 — "mệnh trời không cố định") và **Đa sĩ** (Chu Công đích danh nói với di thần nhà Thương) thì **đúng** là chỗ chứa lập luận ấy ✓.
- **Câu thay thế đề xuất (Nguồn):** "Thượng thư, các thiên Khang cáo, Đa sĩ, Đa phương; Edward L. Shaughnessy, *Sources of Western Zhou History* (1991)." Nếu muốn giữ Thiệu cáo thì phải viết rõ "thiên Thiệu cáo, do Thiệu Công Thích nói, cùng một mạch lập luận".

### [Sai] "Khổng Tử lấy chính ông, không phải vị vua nào, làm hình mẫu"
- **Cái đúng:** *Luận ngữ* 8.19 ca ngợi **Nghiêu** với tư cách **vua**: "大哉堯之為君也" ("Lớn thay, Nghiêu làm vua!"); 8.18 ca ngợi **Thuấn và Vũ**. Khổng Tử dựng hình mẫu từ cả vua lẫn bề tôi. Mệnh đề "không phải vị vua nào" sai trực tiếp với văn bản.
- **Câu thay thế đề xuất:** "...và Khổng Tử, bên cạnh các vua Nghiêu Thuấn, lấy ông làm hình mẫu cho người phò tá — vai mà chính Khổng Tử tự nhận."

### [Nghi vấn] "trả quyền thay vì giữ" — trình thuật truyền thống nêu như sự kiện
- **Nguyên văn:** "ông dẹp loạn Tam giám rồi **trả quyền thay vì giữ** — hành động mà Nho gia về sau lấy làm mẫu mực tối cao của bề tôi."
- **Vấn đề:** việc nhiếp chính bảy năm rồi trả quyền là **trình thuật của chính Thượng thư và Sử ký**, tức của truyền thống mà mục đang mô tả. Có tranh luận học thuật thật sự về việc Chu Công đã **xưng vương** (稱王) trong thời gian đó hay không, và ngay trong Thượng thư cũng có dấu vết lời gièm tố ông định cướp ngôi. Mệnh đề được viết như sự kiện đã xác lập.
- **Đề xuất:** "...rồi, theo trình thuật truyền lại, trả quyền thay vì giữ — có nhà nghiên cứu cho rằng ông đã thực sự xưng vương trong giai đoạn ấy."

### [Nghi vấn] Niên đại các bài cáo chưa được nêu là vấn đề
Giới nghiên cứu **không** nhất trí mấy thiên này là văn bản đương thời. Creel (*The Origins of Statecraft in China*, 1970) nhận 12 thiên là Tây Chu, trong đó 9 thiên thuộc **thời** Chu Công; Shaughnessy nhận một lõi sớm; Michael Nylan (*The Five "Confucian" Classics*, 2001) dè dặt hơn hẳn, kể cả với các thiên kim văn. Mục đang nói như thể các bài cáo là lời ghi trực tiếp của ông. Nên thêm một mệnh đề nhượng bộ.

### [Nghi vấn] Liên kết `Kế thừa từ: CH01-BCE17_15-01` (Thành Thang) · kế thừa · qua trường phái
Đích đúng người (Thành Thang, mục -01 nhóm BCE17_15) ✓, đúng chiều thời gian ✓. Nhưng "kế thừa" giữa người sáng lập nhà Thương và người biện minh cho việc **lật** nhà Thương là quan hệ gượng. Nếu ý là Chu mượn tiền lệ "Thang nhận mệnh từ Hạ", thì loại quan hệ đúng hơn là **tương đồng độc lập**, hoặc nên bỏ dòng này.

---

## CH01-BCE11_9-04 · David

**Khớp:** Q41370 = David ✓. Bia **Tel Dan**: niên đại học giới đồng thuận là **nửa sau TK 9 TCN, thường ghi k. 840 TCN** ✓ — **con số trong mục đúng**. Cụm `bytdwd` ("nhà David") ở dòng 9, là nhắc tới David sớm nhất ngoài Kinh Thánh, tác giả thường được quy cho Hazael ✓. **Finkelstein & Silberman, *David and Solomon*, 2006** — sách có thật, **đúng năm** (Free Press, 2006), **đúng nội dung được dẫn**: lập luận trung tâm của sách là vương quốc thống nhất nhỏ hơn nhiều so với mô tả Kinh Thánh ✓. Đây là một trong vài trích dẫn vững nhất của nhóm.

### [Sai] "bằng chứng ngoài Kinh Thánh **chỉ có một dòng** trên bia Tel Dan" — mâu thuẫn với chính mục -11 của atlas
- **Cái đúng:** có ít nhất hai ứng viên khác, cả hai đều đang tranh luận chứ không phải không tồn tại: (1) **dòng 31 bia Mesha**, nơi André Lemaire (1994) phục nguyên `bt[d]wd` — **chính bài báo này đang được mục -11 dẫn làm nguồn**; (2) cụm `hdbt dwt` ("cao nguyên của David"?) trong danh sách Karnak của Shoshenq I — **chính nhân vật ở mục -07**. Viết "chỉ có một dòng" là tự xoá hai mục khác trong cùng nhóm.
- **Câu thay thế đề xuất:** "...bằng chứng ngoài Kinh Thánh mỏng và đều đang tranh luận: chắc nhất là dòng 'nhà David' trên bia Tel Dan khoảng 840 TCN; cách phục nguyên tương tự ở dòng 31 bia Mesha thì chưa ngã ngũ."

### [Sai] "Truyền thống cũng gắn **phần lớn** Thánh vịnh với tên ông"
- **Cái đúng:** trong bản Masoretic, **73 trên 150** thánh vịnh mang đề từ `lə-Dāwid` — **chưa tới một nửa**, không phải "phần lớn". (Bản Bảy Mươi gán nhiều hơn, nhưng mục không nói mình dùng bản nào.)
- **Câu thay thế đề xuất:** "Truyền thống gắn gần một nửa số Thánh vịnh với tên ông."

### [Nghi vấn] "khảo cổ học hiện nay, **nhất là Finkelstein**, cho là phóng đại" — trung lập
Finkelstein đại diện cho một **phe** trong một tranh luận còn sống (niên đại thấp). Phe đối lập có tên tuổi không kém: Amihai Mazar (niên đại truyền thống hiệu chỉnh), William Dever, Eilat Mazar. Câu hiện tại biến lập trường của một phe thành "khảo cổ học hiện nay".
- **Đề xuất:** "...quy mô vương quốc như sách Samuel mô tả bị phe niên đại thấp (Finkelstein) cho là phóng đại, trong khi Amihai Mazar và Dever bảo vệ một quy mô lớn hơn; tranh luận chưa ngã ngũ."

### [Nghi vấn] "chân dung quyền lực sắc nét bậc nhất của văn chương cổ" — mệnh đề tối cao không quy thuộc
Đây là một đánh giá thẩm mỹ, không phải sự kiện, và không được gán cho ai. Vi phạm yêu cầu "trung lập, không tô vẽ" của §5. Đề xuất bỏ "bậc nhất" hoặc quy thuộc ("giới phê bình văn chương Kinh Thánh, từ Auerbach trở đi, thường đọc trình thuật này như...").

### [Thiếu] `Kế thừa từ: Không xác định` trong khi chính mục nêu Saul là vua trước
Nếu Saul không được coi là có quan hệ kế thừa thì nên nói ra; để trống trong khi đoạn văn xuôi nêu tên ông là một lỗ hổng.

---

## CH01-BCE11_9-05 · Solomon

**Khớp:** Q37085 = Solomon ✓. Niên đại ghi rõ "theo trình thuật Kinh Thánh" ✓ — cách đề phòng đúng. Việc quy Châm ngôn, Giảng viên, Diễm ca cho ông ✓. Tranh luận niên đại các cổng Hazor–Megiddo–Gezer ✓ (Yadin đối lại niên đại thấp của Finkelstein). Finkelstein & Silberman 2006 ✓ (xem mục -04).

### [Sai] "nó biến việc thờ phụng từ nhiều nơi thành một trung tâm duy nhất"
- **Nguyên văn:** "Việc gắn với tên ông có hệ quả dài nhất là ngôi đền ở Jerusalem: **nó biến việc thờ phụng từ nhiều nơi thành một trung tâm duy nhất**, và chính nguyên tắc tập trung ấy định hình Do Thái giáo..."
- **Cái đúng:** **tập trung hoá phụng tự không xảy ra dưới thời Solomon.** Việc thờ ở các "nơi cao" (bāmôt) tiếp tục suốt mấy thế kỷ sau — chính sách Các Vua lặp đi lặp lại công thức chê từng vua vì "các nơi cao vẫn chưa bị dẹp" (vd. 1 V 15:14; 22:44; 2 V 12:4; 14:4; 15:4). Nguyên tắc **một nơi thờ duy nhất** là của sách Đệ nhị luật và được thi hành trong cải cách của **Hezekiah** (2 V 18:4) rồi **Josiah** (2 V 23, năm 622 TCN). Đền của Solomon là **điều kiện** cho việc tập trung về sau, chứ không phải là việc tập trung. Đáng chú ý: atlas đã có mục Hezekiah (`CH02-BCE08-07`), nên công trạng đang bị gán nhầm người **trong chính atlas này**.
- **Câu thay thế đề xuất:** "...ngôi đền ở Jerusalem: nó tạo ra chỗ dựa vật chất mà ba thế kỷ sau, trong cải cách của Hezekiah rồi Josiah, được dùng để dồn toàn bộ phụng tự về một nơi duy nhất — và chính nguyên tắc tập trung ấy định hình Do Thái giáo..."

### [Nghi vấn] "định hình Do Thái giáo cả sau khi đền bị phá hai lần"
Sau năm 70 CN, Do Thái giáo chuyển sang mô hình **hội đường và Torah**, tức theo hướng **phi tập trung** về không gian thờ tự; cái còn lại là hướng về Jerusalem trong kinh nguyện, không phải nguyên tắc tập trung phụng tự. Câu hiện tại dễ gây hiểu sai.

### [Thể thức] Loại quan hệ `kế thừa` dùng cho một liên doanh thương mại
`Kế thừa từ: CH01-BCE11_9-06 (Hiram I) · kế thừa · trực tiếp` — Hiram cấp gỗ, thợ và tàu; đó là quan hệ **đối tác**, không phải kế thừa tư tưởng. Từ vựng `RELATION_TYPES` (kế thừa · tổng hợp · phản bác · tương đồng độc lập) không có mục nào hợp. Nên bỏ liên kết này (ở cả hai chiều -05/-06) và để nội dung ấy trong văn xuôi, thay vì ép vào một loại quan hệ sai.

---

## CH01-BCE11_9-06 · Hiram I

**Khớp:** Q467115 = "Hiram I, Phoenician king" ✓, và bí danh Wikidata của mục này đúng là `𐤇𐤓𐤌` — **ký tự Phoenicia trong tiêu đề mục là đúng**. Trị vì k. 980–947 TCN là một trong các niên biểu Tyre đang lưu hành ✓ (Britannica dùng k. 969–936, có thể đồng nhiếp từ k. 980 — chênh lệch này thuộc về nguồn, không phải lỗi). **Sách Các Vua quyển I, chương 5 và 9** — **kiểm mục lục: đúng**: 1 V 5 là gỗ bá hương và thợ, 1 V 9:26–28 là đội tàu Ezion-geber đi Ophir ✓. Aubet, *The Phoenicians and the West: Politics, Colonies and Trade*, Cambridge University Press, bản 2 **2001** ✓ (bản 1 tiếng Anh 1993; bản Tây Ban Nha gốc 1987).

### [Sai] Tên gốc trong ngoặc: "Ahiram xứ Tyre" — trộn hai người ở hai thành khác nhau
- **Nguyên văn tiêu đề:** `### CH01-BCE11_9-06 · Hiram I (𐤇𐤓𐤌, **Ahiram xứ Tyre**)`
- **Cái đúng:** **Ahiram (ʾḤRM) là vua xứ Byblos**, người có chiếc quan tài đá khai quật năm 1923 mang bi ký Phoenicia nổi tiếng (Wikidata: nhân vật **Q400275**, hiện vật **Q1972397**). Hiram I (ḤRM) là vua **Tyre** — **Q467115**, đúng là Q-ID mục đang dùng. Đây là **hai người, hai thành**, dù gần như đồng thời (cả hai quanh TK 10 TCN) và dù về mặt từ nguyên "Hiram" được nhiều nhà nghiên cứu coi là dạng rút gọn của "Ahiram". **Không nguồn nào gọi vua Tyre là "Ahiram xứ Tyre"** — cụm ấy là một dạng lai không tồn tại, và nó dẫn thẳng người đọc tới quan tài Byblos.
- Lint **không bắt được** lỗi này: Q-ID đúng, ký tự Phoenicia đúng, chỉ có phần chú tên Latinh sai.
- **Câu thay thế đề xuất:** `### CH01-BCE11_9-06 · Hiram I (𐤇𐤓𐤌 Ḥīrām, Hiram xứ Tyre)` — và nếu muốn giữ liên hệ từ nguyên thì đưa vào văn xuôi: "tên ông là dạng rút gọn của Ahiram, trùng tên với một vua Byblos cùng thời, **không phải cùng người**."

### [Nghi vấn] Dùng Aubet để đỡ cho một mệnh đề ngược với luận điểm của chính bà
- **Nguyên văn:** "**Đợt bành trướng Phoenicia bắt đầu từ giai đoạn này** mang theo bảng chữ cái của họ sang Aegean"; **Vì sao chọn:** "giai đoạn ông cai trị là lúc mô hình thành bang thương mại Phoenicia định hình".
- **Vấn đề:** *The Phoenicians and the West* dựng khung niên đại cho hệ thống thương mại Phoenicia ở phương Tây vào khoảng **TK 8–6 TCN**, với một giai đoạn "tiền thuộc địa" tiếp xúc rời rạc trước đó; Aubet nổi tiếng vì **hạ thấp** độ tin cậy của các niên đại lập thuộc địa sớm theo truyền thống (Gadir, Utica, Carthage 814 TCN). Gắn "đợt bành trướng bắt đầu" vào triều Hiram (TK 10 TCN) rồi dẫn Aubet làm nguồn là đúng dạng lỗi mà `CONTRIBUTING.md` §7 mô tả (ca Hansen): nguồn có thật, đúng chủ đề, nhưng bị dùng ngược chiều lập luận.
- **Câu thay thế đề xuất:** "Mạng lưới hàng hải mà Tyre dựng trong giai đoạn này là tiền đề cho đợt lập thuộc địa Phoenicia ở phương Tây — đợt mà khảo cổ học định vào TK 8 TCN — và chính dòng người đi biển ấy mang bảng chữ cái sang Aegean."

### [Thể thức] Thiếu nhãn `[Tranh cãi lịch sử]` trong khi David và Solomon cùng nhóm đều có
Bằng chứng về Hiram I chỉ gồm sách Các Vua và Josephus (dẫn lại Menander xứ Ephesus và Dios) — **không có bi ký đương thời nào**. Cơ sở sử liệu của ông mỏng ngang David/Solomon ở hai mục liền kề, vốn được gắn nhãn. Hoặc gắn nhãn cho Hiram, hoặc nói rõ trong văn xuôi vì sao ông được coi là chắc chắn hơn.

### [Thể thức] "Ứng viên cùng vùng là Ithobaal I" — không cùng thời
Ithobaal I trị vì **k. 878–847 TCN**, tức **sau Hiram khoảng 70–100 năm**. Mục đã khéo viết "cùng **vùng**" thay vì "cùng thời", nhưng template §5 đòi "cùng lĩnh vực, **cùng thời**", và đây đúng là loại ca mà `CONTRIBUTING.md` §5 cảnh báo. Ứng viên thật sự cùng thời: **Abibaal xứ Tyre** (cha Hiram) hoặc **Ahiram xứ Byblos** — và nêu Ahiram ở đây sẽ đồng thời sửa được lỗi tên gốc ở trên.

---

## CH01-BCE11_9-07 · Shoshenq I

**Khớp:** Q311811 = Shoshenq I ✓. Trị vì k. 943–922 TCN ✓. Gốc thủ lĩnh Libya (Meshwesh) ở châu thổ ✓. Lập vương triều XXII ✓. Đặt con làm Thượng tế Amun ở Thebes, tạm hợp nhất Bắc–Nam ✓. Danh sách Cổng Bubastite ở Karnak có **khoảng 150 vòng tên** ✓ — **con số trong mục đúng**. Kitchen, *The Third Intermediate Period in Egypt (1100–650 BC)* — sách có thật, bản in 1996 tồn tại (Aris & Phillips) ✓. Câu dè dặt về việc đồng nhất Shoshenq với Shishak ✓ — viết đúng mức.

### [Nghi vấn] "điểm mà niên biểu Ai Cập và trình thuật Kinh Thánh **chạm vào nhau trực tiếp**" / "mốc đồng bộ"
- **Cái đúng:** danh sách Karnak **không nhắc tới Jerusalem** — mà Jerusalem mới là chỗ trình thuật 1 V 14:25–26 nói Shishak lấy kho báu. Các địa danh đọc được chủ yếu nằm ở **vương quốc Israel phía bắc và vùng Negev** (Megiddo, Taanach, Beth-Shean, Gibeon, Aijalon), không ở Judah. Nghĩa là hai nguồn **không trùng khớp về nội dung**; cái nối chúng lại là **giả thiết đồng nhất Shoshenq = Shishak**, chứ không phải một điểm chạm trực tiếp. Có nhà nghiên cứu (Finkelstein trong số đó) đọc chiến dịch này với mục tiêu khác hẳn mục tiêu mà Kinh Thánh gán cho nó.
- **Câu thay thế đề xuất:** "Danh sách ấy là một trong rất ít chỗ niên biểu Ai Cập có thể đặt cạnh trình thuật Kinh Thánh — dù bản thân nó không nhắc Jerusalem, và việc nối hai nguồn vẫn dựa trên giả thiết Shoshenq chính là Shishak."

### [Thể thức] Cả hai "ứng viên" đều không cùng thời
**Psusennes I** trị vì k. **1047–1001 TCN** — trước Shoshenq I hơn **nửa thế kỷ**; **Osorkon II** trị vì k. **872–837 TCN** — sau ông khoảng **50–85 năm**, và là chắt ông. Mục dùng chữ "cùng **giai đoạn**", đỡ được một phần vì nhóm BCE11_9 gộp ba thế kỷ, nhưng không ai trong hai người là ứng viên **cùng thời** theo nghĩa §5. Ứng viên thật sự cùng thời: **Osorkon I** (con và người kế vị trực tiếp) hoặc **Siamun** (vua Tanis ngay trước vương triều XXII).

---

## CH01-BCE11_9-08 · Ashurnasirpal II

**Khớp:** Q193290 = Ashurnasirpal II ✓. Trị vì 883–859 TCN ✓, độ tin cậy Cao hợp lý (neo vào danh sách niên quan Assyria). Dời đô về Kalhu/Nimrud ✓. Nguồn Grayson, *RIMA 2* (1991) **đúng tập** — 1114–859 TCN bao trọn triều ông ✓. Phù điêu cung điện Tây Bắc ở Bảo tàng Anh ✓.

### Con số bữa tiệc — **đúng**, kiểm được
- **Nguyên văn:** "Bia khánh thành ghi bữa tiệc **mười ngày** đãi **sáu vạn chín nghìn năm trăm bảy mươi tư** người, kèm danh sách thực phẩm."
- **Kiểm:** Banquet Stele (tìm ở Nimrud năm 1951) ghi **69.574** khách trong **mười ngày**, năm **879 TCN**, kèm danh mục thực phẩm (300 bò, 17.000 cừu và cừu non, 1.000 hươu và linh dương, 34.000 chim, 10.000 vò bia, 10.000 bầu rượu). **Cả hai con số đều đúng.** ✓
- Gợi ý nhỏ: nên ghi thẳng "69.574" bên cạnh dạng chữ, để người đọc đối chiếu được.

### [Sai] "dòng nghệ thuật kể chuyện bằng hình liên tục **đầu tiên ở quy mô kiến trúc**"
- **Phản ví dụ, và nằm ngay trong chính atlas này:** các chu trình phù điêu tự sự trên tường đền Ai Cập — trận Kadesh của **Ramesses II** (`CH01-BCE14_12-06`) khắc ở Karnak, Luxor, Abu Simbel; các cảnh chiến trận của **Seti I** ở Đại sảnh Cột Karnak; các cảnh chống Dân Biển của **Ramesses III** (`CH01-BCE14_12-09`) ở Medinet Habu. Tất cả là tự sự bằng hình liên tục, ở quy mô kiến trúc, và **sớm hơn Ashurnasirpal II ba tới bốn thế kỷ**. Thêm vào đó, tranh tường tự sự ở cung điện **Zimri-Lim** tại Mari (`CH01-BCE20_18-05`, TK 18 TCN) cũng là trang trí tường cung điện kể chuyện.
- Mệnh đề hẹp hơn — "**phiến đá chạm ốp tường cung điện** là cái Assyria chưa từng có trước ông" — thì **đúng** và được học giới xác nhận.
- **Câu thay thế đề xuất:** "...khởi đầu của phù điêu tự sự Assyria: trước ông chưa cung điện Assyria nào ốp tường bằng phiến đá chạm."

### [Sai] "phù điêu tự sự ốp tường cung điện là **thể loại bắt đầu từ công trình của ông**"
- **Phản ví dụ:** kỹ thuật ốp tường bằng **orthostat chạm** đã có ở các thành **Tân Hittite / Syro-Hittite** — Carchemish, Tell Halaf (Guzana), Zincirli (Sam'al) — và học giới thường cho rằng chính các vua Assyria **mượn** hình thức này sau các chiến dịch sang phía tây. Tell Halaf có chuỗi orthostat chạm thuộc TK 10–9 TCN, tức **trước hoặc đồng thời** với cung điện Tây Bắc.
- **Câu thay thế đề xuất (Vì sao chọn):** "Ashurnasirpal được chọn theo tính nguyên bản (c) **của quy mô và chương trình**: hình thức orthostat chạm đã có ở các thành Tân Hittite, nhưng ông là người đầu tiên biến nó thành một chương trình hình ảnh phủ kín một cung điện, và chính chương trình ấy là nguồn hình ảnh chính cho mọi hình dung hiện nay về Assyria."

---

## CH01-BCE11_9-09 · Shalmaneser III

**Khớp:** Q211928 = Shalmaneser III ✓. Trị vì 858–824 TCN = **35 năm** ✓ (khớp "ba mươi lăm năm" trong mục). Trận **Qarqar năm 853 TCN** ✓. Tháp bia đen do **Austen Henry Layard** tìm thấy năm **1846** tại Nimrud ✓. Số hiệu **Bảo tàng Anh BM 118885** ✓ — **cả bốn chi tiết đều đúng**. Tháp bia tổng kết 31 năm chiến dịch ✓.

### [Sai] Nguồn dẫn **sai tập và sai năm**
- **Nguyên văn:** "A. Kirk Grayson, *Assyrian Rulers of the Early First Millennium BC* (**1991**)".
- **Cái đúng:** bộ RIM/RIMA tách làm hai tập cùng tên:
  - **RIMA 2** = *Assyrian Rulers of the Early First Millennium BC **I (1114–859 BC)***, Toronto, **1991**;
  - **RIMA 3** = *Assyrian Rulers of the Early First Millennium BC **II (858–745 BC)***, Toronto, **1996**.
  Shalmaneser III trị vì **858–824 TCN**, tức nằm trọn trong **RIMA 3 (1996)**, **không** trong tập 1991. Bi ký của ông không có trong cuốn đang được dẫn.
- Đây đúng là loại lỗi `CONTRIBUTING.md` §3 cảnh báo (số tập/năm được sinh ra chứ không tra cứu) — và nó xuất hiện vì mục -08 và -09 **chép lại cùng một dòng nguồn**, trong khi hai nhân vật nằm ở hai tập khác nhau.
- **Câu thay thế đề xuất:** "A. Kirk Grayson, *Assyrian Rulers of the Early First Millennium BC II (858–745 BC)* (RIMA 3, 1996); Tháp bia đen Shalmaneser III, Bảo tàng Anh BM 118885."

### [Nghi vấn] "cảnh vua Jehu của Israel quỳ dâng cống — hình ảnh sớm nhất còn lại của **một người Israel được định danh**"
- **Cái đúng:** bi ký trên tháp bia ghi "cống của **Iaua** (Jehu) **người Bīt-Ḫumrî**", nhưng **không nói** nhân vật đang quỳ là chính Jehu hay sứ giả của ông — và học giới chia rẽ về điểm này. Irit Ziffer lập luận rằng các hình quỳ chỉ là người dâng cống theo quy ước, không phải chân dung một vị vua cụ thể. Vua chư hầu thường không đích thân tới Assyria.
- Công thức thông dụng trong học giới là "**hình ảnh một người Israel sớm nhất còn lại**" — mục đã nâng lên thành "một người Israel **được định danh**", tức khẳng định đúng cái đang tranh cãi.
- **Câu thay thế đề xuất:** "...có cảnh một người mặc trang phục Israel quỳ dâng cống, dưới dòng chữ ghi tên Jehu — hình ảnh sớm nhất còn lại về một người Israel, dù việc hình đó là chính Jehu hay sứ giả của ông vẫn đang tranh luận."

### [Thiếu] Không nêu tên vua Kinh Thánh được nhắc, cũng không nêu nguồn nhắc
"là chỗ sử liệu Assyria lần đầu nhắc tới một vị vua cũng xuất hiện trong Kinh Thánh" — người đó là **Ahab xứ Israel** (A-ha-ab-bu Sir-'i-la-a-a), và chỗ nhắc là **Bia một khối Kurkh**, không phải tháp bia đen. Nêu tên và hiện vật ra sẽ làm câu này kiểm được; hiện tại nó không kiểm được như đang viết.

---

## CH01-BCE11_9-10 · Elijah

**Khớp:** Q133507 = Elijah ✓. Hoạt động k. 870–850 TCN ✓ (trùng triều Ahab, k. 874–853). **Sách Các Vua quyển I, chương 17–19 và 21** — **kiểm mục lục: đúng**: 1 V 17–18 là hạn hán và cuộc thách đấu trên núi Carmel, 1 V 19 là Horeb, 1 V 21 là vườn nho Naboth ✓. **Marvin A. Sweeney, *I & II Kings: A Commentary*, Westminster John Knox, Old Testament Library, 2007** — sách có thật, **đúng năm, đúng thể loại (chú giải)**, và đúng chủ đề ✓. Ly rượu và ghế dành cho Elijah trong lễ Vượt qua ✓; Malachi 3:23–24 và Tân Ước (Mc 9:11–13; Mt 11:14) ✓.

### [Thể thức] "Nathan ở thế hệ trước" — lệch khoảng 130–150 năm
- **Cái đúng:** Nathan là tiên tri trong triều **David và Solomon**, tức khoảng **1000 TCN**; Elijah hoạt động giữa **TK 9 TCN**. Khoảng cách **4–5 thế hệ**, không phải "thế hệ trước". Đây đúng ca mà `CONTRIBUTING.md` §5 mô tả (Tử Sản/Quản Trọng, Ban Siêu/Trương Khiên).
- **Ứng viên thay thế thật sự cùng thời:** **Micaiah con Imlah** (1 V 22) — tiên tri đối đầu chính Ahab và Jehoshaphat, cùng triều, cùng sách, cùng mô-típ chất vấn vua; hoặc **Obadiah**, quan cai cung của Ahab (1 V 18). Micaiah là ứng viên lý tưởng vì ông làm **đúng việc** mà mục đang gán công cho Elijah.
- **Câu thay thế đề xuất:** "Ứng viên cùng mạch là Elisha, học trò kế tục ông, và Micaiah con Imlah, người cùng triều Ahab và cũng nói ngược ý vua."

### [Nghi vấn] "mẫu tiên tri chất vấn vua... **bắt đầu rõ nét ở ông**" — bị chính mục tự phản bác
- Mục vừa nêu tên **Nathan**, mà Nathan đối chất David về vụ Bathsheba và Uriah (2 Sm 12, dụ ngôn con chiên của người nghèo) là **nguyên mẫu kinh điển** của đúng mô-típ ấy, sớm hơn Elijah khoảng 150 năm. Thêm **Samuel** quở Saul (1 Sm 13; 15) và **Ahijah** xứ Shiloh chống Jeroboam (1 V 14).
- **Câu thay thế đề xuất:** "...mẫu tiên tri chất vấn vua đã có từ Nathan đối chất David, nhưng ở Elijah nó chuyển từ một lần quở trách trong cung thành thế đối đầu công khai, kéo dài, với cả vương triều — và chính dạng ấy là cái Amos và Isaiah ở Chapter 2 làm việc bên trong."

### [Thiếu] Nguồn không phủ được mệnh đề được cất lên trời
"Vì ông được chép là **không chết mà được cất lên**" nằm ở **2 Các Vua chương 2**, trong khi dòng Nguồn chỉ dẫn **1 Các Vua 17–19 và 21**. Thêm "2 V 2" vào dòng Nguồn.

### [Nghi vấn] "không có nguồn đương thời nào **ngoài** trình thuật Các Vua"
Câu này hàm ý sách Các Vua **là** nguồn đương thời. Thực tế trình thuật Các Vua ở dạng còn lại thuộc Lịch sử Đệ nhị luật, biên soạn TK 7–6 TCN, tức **sau Elijah hai tới ba thế kỷ**. Đề xuất: "không có nguồn nào đương thời với ông; trình thuật Các Vua được biên soạn muộn hơn hai tới ba thế kỷ."

---

## CH01-BCE11_9-11 · Mesha

**Khớp:** Q350258 = Mesha ✓. Bia tìm thấy **năm 1868** tại **Dhiban** (Dibon cổ), do mục sư F. A. Klein ✓ — **đúng**. **Louvre AO 5066** ✓ — **đúng số hiệu**, vào bộ sưu tập Louvre từ 1873. 34 dòng chữ Moab, hệ chữ Phoenicia ✓. Mô-típ "Kemosh giận đất của mình → để dân bị áp bức → nguôi giận → ban chiến thắng" ✓ (dòng 5–6). Bia nhắc đích danh **Omri** ✓ (dòng 4–5, 7). **André Lemaire, "'House of David' Restored in Moabite Inscription", *Biblical Archaeology Review* 20:3 (1994)** — **kiểm được: có thật, đúng tập 20, đúng số 3, đúng năm 1994 (số tháng 5–6), tr. 30–37** ✓. Hazael và Ahab đều **không** có mục riêng trong atlas ✓ (không vi phạm §6), và cả hai đều có chồng lấn niên đại với Mesha ✓.

### [Sai] "tiếng nói trực tiếp **duy nhất** còn lại của một vương quốc Transjordan"
- **Phản ví dụ:** **Bi ký Thành cổ Amman** (Amman Citadel Inscription) — bi ký Ammon cổ nhất đã biết, **nửa sau TK 9 TCN**, tức gần như **cùng thời với bia Mesha**, nhắc thần Milcom; **bình đồng Tell Siran** (cuối TK 7 / đầu TK 6 TCN), 92 ký tự, nêu đích danh ba đời vua Ammon (Amminadab con Hissal'el con Amminadab); và **bi ký thạch cao Deir Alla** (k. 800 TCN, thung lũng Jordan) với trình thuật Balaam con Beor. Ammon là một vương quốc Transjordan và nó **có** tiếng nói trực tiếp còn lại.
- **Câu thay thế đề xuất:** "...bia của ông là trình thuật tự sự dài nhất còn lại từ một vương quốc Transjordan — Ammon chỉ để lại các bi ký ngắn — tức một bên mà nếu không có nó thì gần như chỉ được biết qua lời của đối thủ."

### [Nghi vấn] "bi ký **dài nhất** còn lại của một vương quốc Levant thời đồ sắt"
- Công thức chuẩn trong học giới hẹp hơn: "bi ký thời đồ sắt dài nhất **tìm được trong vùng** [Levant nam]", hoặc "văn bản dài nhất còn lại có nhắc tới vương quốc Israel". Mở rộng ra "một vương quốc Levant" thì có đối thủ: bi ký song ngữ **Karatepe** (Phoenicia–Luwian, cuối TK 8 TCN) dài hơn hẳn, dù nằm ở Cilicia; các bi ký **Hadad** và **Panamuwa** từ Sam'al (Zincirli, bắc Levant) cũng cỡ 34 dòng. Nên thu hẹp lại thành "ở Levant nam".

### [Thiếu] Dẫn Lemaire mà không hề nói tới điều Lemaire lập luận, và không nói nó đang bị tranh cãi
- Dòng Nguồn dẫn bài báo của Lemaire về **dòng 31**, nhưng **toàn bộ văn xuôi của mục không nhắc tới "nhà David" một chữ nào**. Nguồn có thật và đúng chủ đề nhưng **không đỡ cho mệnh đề nào trong mục** — đây là lỗi ngược với ca SEP/Solon ở Ch2, nhưng cùng hệ quả: dòng Nguồn không kiểm được bằng nội dung mục.
- **Và nếu đưa nội dung ấy vào thì phải kèm tình trạng tranh luận**: Michael Langlois (2019) cho rằng ảnh chụp kỹ thuật mới **xác nhận** cách đọc; Finkelstein, Na'aman và Römer (2019) đề nghị đọc thành **Balak**; Hendel phản bác; Richelle và Burlingame (2023) kết luận cách đọc vẫn **"chưa chắc, mang tính giả thiết"**. Tức **chưa có đồng thuận**.
- **Câu thay thế đề xuất (thêm vào Tư tưởng):** "Dòng 31, chỗ bia bị hỏng, được André Lemaire phục nguyên thành 'nhà David' năm 1994 — nếu đúng thì đây là chỗ nhắc David thứ hai ngoài Kinh Thánh; cách đọc này tới nay vẫn chưa ngã ngũ, có người đọc thành 'Balak'."
- **Hệ quả bắt buộc:** đối chiếu lại với mục **-04**, nơi đang viết bằng chứng ngoài Kinh Thánh về David "**chỉ có một dòng** trên bia Tel Dan". Hai mục đang nói ngược nhau.

### [Nghi vấn] "Hazael của Damascus, **người để lại bia Tel Dan**"
Tên Hazael **không xuất hiện** trên bia Tel Dan; việc quy tác giả cho ông là suy luận của học giới (đa số, nhưng là suy luận). Đề xuất: "người thường được coi là tác giả bia Tel Dan".

---

## CH01-BCE11_9-12 · Lycurgus xứ Sparta

**Khớp:** Q211326 = Lycurgus of Sparta ✓. Nhãn `[Truyền thuyết]` đúng ✓. **Paul Cartledge, *Sparta and Lakonia: A Regional History 1300–362 BC*, Routledge, bản 2 **2002*** ✓ — sách có thật, đúng năm bản 2, đúng thể loại (chuyên khảo sử vùng), đúng chủ đề. Liên kết `Ảnh hưởng tới: CH02-BCE06-08` trỏ đúng **Solon** ✓, đúng chiều thời gian ✓.

### Câu mở đầu Plutarch — **đúng, kiểm được nguyên văn**
- **Nguyên văn mục:** "Plutarch mở tiểu sử bằng chính lời thừa nhận rằng **không điều gì về ông nói được mà không bị phản bác**."
- **Kiểm:** *Lycurgus* 1.1 mở đúng như vậy: "Περὶ Λυκούργου τοῦ νομοθέτου καθόλου μὲν οὐδὲν ἔστιν εἰπεῖν ἀναμφισβήτητον" — "Về Lycurgus nhà lập pháp, nói chung không điều gì nói được mà không bị tranh cãi", rồi liệt kê: xuất thân, các chuyến đi, cái chết, và nhất là sự nghiệp lập pháp của ông; và **thời đại ông sống là chỗ các sử gia bất đồng nhất**. **Mệnh đề trong mục chính xác** ✓. Đây là trích dẫn vững nhất của cả nhóm.
- Gợi ý: có thể bổ sung nửa sau của câu Plutarch (sử gia bất đồng nhất về **niên đại**) vì nó đỡ trực tiếp cho `độ tin cậy niên đại: Thấp` và cho ghi chú biên tập ở dòng 662.

### [Thể thức] Nêu Dracon và Solon trong "Vì sao chọn" — cách ghi chưa đúng khuôn §6
- Mục **có** nói ra việc hai người thuộc Chapter 2 ✓ (hơn hẳn 11 ca mà `CONTRIBUTING.md` §6 liệt ở Ch3), nhưng lý do loại được ghi là "**không phải ứng viên cùng thời**", trong khi lý do thật sự và mạnh hơn là **cả hai đã được chọn, có mục riêng** (`CH02-BCE07-05` Dracon, `CH02-BCE06-08` Solon) — tức không có đánh đổi nào xảy ra. §6 đòi đúng chữ "*có mục riêng ở nhóm X nên không phải ứng viên bị loại*".
- **Câu thay thế đề xuất:** "Dracon và Solon ở Athens đều có mục riêng ở Chapter 2 (nhóm BCE07 và BCE06) nên không phải ứng viên bị loại, và họ cũng sau ông hơn hai thế kỷ."

### [Nghi vấn] "sau ông **hơn một thế kỷ**" — thực tế hơn gấp đôi
Dracon k. 621 TCN, Solon k. 594 TCN; đầu muộn của niên đại truyền thống Lycurgus trong mục là **820 TCN**. Khoảng cách là **~200 và ~226 năm**, tức **hơn hai thế kỷ**. "Hơn một thế kỷ" đúng về mặt logic nhưng làm nhẹ đi một nửa khoảng cách, ngay trong câu đang dùng khoảng cách ấy làm lý do loại.

### Khẳng định "không có nhà lập pháp nào khác được nêu tên" — **đứng được**
Đã tìm phản ví dụ: **Zaleucus xứ Locri** (truyền thống k. 662 TCN) và **Charondas xứ Catania** (TK 6 TCN) đều **muộn hơn** khung 900–820 TCN; **Pheidon xứ Argos** được xếp TK 7 TCN và là bạo chúa, không phải nhà lập pháp. Trong khung niên đại mục đang dùng, thế giới Hy Lạp thật sự không có nhà lập pháp nào khác được nêu tên. Cách xử lý này đúng với `CONTRIBUTING.md` §5 ("viết thẳng là không có").

### [Nghi vấn] Mức bằng chứng của liên kết tới Solon
`CH02-BCE06-08 · kế thừa · qua trường phái` — với một nhân vật mang nhãn `[Truyền thuyết]`, mà bản thân mục thừa nhận không điều gì về ông là không bị phản bác, mức **`suy đoán học giả`** trung thực hơn `qua trường phái`. Không có bằng chứng nào về một "trường phái" truyền từ Sparta sang Solon; cái có là việc truyền thống cổ đại ghép cặp hai nhà lập pháp.

---

# Đánh giá lựa chọn nhân vật

## Cơ cấu hiện tại của nhóm (12/12, nhóm kín)

| Chiều | Phân bố |
|---|---|
| **Vùng** | Trung Đông/Bắc Phi **9** · Đông Á **2** · Châu Âu **1** → **3 vùng**, đúng mức sàn §5 nhưng không hơn |
| **Lĩnh vực** | 10 lĩnh vực, vượt sàn 4 ✓. Chính trị/Nhà nước **7**, Quân sự **5** — hai lĩnh vực này chiếm phần lớn |
| **Câu hỏi lớn** | **9/12 ghi "Không áp dụng"**; chỉ -03, -04, -10 mang "Con người" |
| **Nghề** | **8/12 là vua hoặc nhiếp chính**; không mục nào thuộc Toán học, Khoa học tự nhiên, Y học, Kỹ thuật, Sử học, Ngôn ngữ học |
| **Giới** | **0/12 là phụ nữ** |
| **Cơ sở sử liệu** | **4/12** (-04, -05, -06, -10) đứng chủ yếu trên trình thuật Kinh Thánh — một hợp tuyển biên soạn muộn hơn vài thế kỷ |

Ghi chú biên tập của chapter đã nói rất sòng phẳng rằng cái quyết định chapter này là **chữ viết**, không phải bốn tiêu chí, và đã liệt năm vùng trống trong cả 1200 năm. Phần dưới chỉ nêu những chỗ lập luận ấy **chưa phủ hết** cho riêng nhóm BCE11_9.

## Có ai ngoài Trung Đông/Bắc Phi, giai đoạn 1100–801 TCN, đủ tiêu chuẩn mà chưa được cân nhắc?

**Có — ba ứng viên, và một vấn đề đặt chỗ.**

### 1. Nam Á — Parikṣit / Janamejaya (Kuru), ứng viên mạnh nhất bị bỏ sót
- **Vấn đề:** nhóm BCE11_9 **không có mục Nam Á nào**, trong khi hai nhóm trước đều có (Viśvāmitra ở BCE17_15, Vasiṣṭha ở BCE14_12). Lập luận "không có chữ viết" của Ghi chú biên tập **không áp dụng được ở đây**, vì chapter đã **tự nhận là dùng có ý thức** quy ước quy một mandala Rigveda cho một cá nhân theo truyền thống. Cùng quy ước ấy cho ra ứng viên có tên ở giai đoạn 1100–801 TCN.
- **Nội dung:** 1100–801 TCN đúng là **thời Vệ-đà hậu kỳ** — giai đoạn hình thành vương quốc **Kuru**, sắp xếp các bài tụng thành bốn Saṃhitā, và định hình nghi lễ **śrauta** chính thống. Michael Witzel, *Early Sanskritization: Origins and Development of the Kuru State* (EJVS, 1995), đặt vương quốc Kuru vào **k. 1200–800 TCN** và coi **Parikṣit** rồi **Janamejaya** là trung tâm của quá trình ấy: củng cố nhà nước Kuru, sắp xếp các tuyển tập Vệ-đà, phát triển nghi lễ śrauta. Đây là một biến cố về **tổ chức tri thức** ngang hàng với những gì nhóm này đang khen ở phía Assyria.
- **Đối chiếu §6:** Parikṣit và Janamejaya **không có mục nào trong toàn atlas** (đã dò `grep '^### '` trên cả bốn file) — tức đây là ứng viên thật, không phải người đã được chọn chỗ khác. Yājñavalkya thì đã có mục (`CH02-BCE07-07`) nên không dùng được.
- **Khuyến nghị:** nhóm đang kín 12/12 nên phải có người ra. Ứng viên để đổi: **-05 Solomon** (không bằng chứng đương thời, và phần lớn đóng góp được mục mô tả — tập trung hoá phụng tự — vừa bị phát hiện là gán nhầm thời; xem mục -05) hoặc **-02 Chu Vũ Vương** (phần lớn lập luận của mục -02 thật ra nói về -03). Nếu Owner không muốn đổi, thì **tối thiểu** phải nêu Parikṣit/Janamejaya trong "Ứng viên mạnh đã bị loại và lý do" — hiện giờ **không một cái tên Nam Á nào** xuất hiện trong danh sách bị loại của chapter cho giai đoạn này.

### 2. Trung Đông/Bắc Phi nhưng sửa được lỗ hổng giới — Sammu-ramat
- Dù vẫn thuộc vùng đang thừa, đây là ứng viên nữ **duy nhất kiểm được** của giai đoạn, và Ghi chú biên tập của chapter đã tự đặt việc này làm mục cần kiểm ở P4 ("danh sách bị loại hiện chỉ có Ahhotep, Tiye, Puduhepa và Phụ Tỉnh" — **cả bốn đều thuộc các nhóm trước**, không ai thuộc BCE11_9).
- **Sammu-ramat** (Shammuramat): vợ Shamshi-Adad V (trị vì 824–811 TCN), mẹ Adad-nirari III; giữ vị thế nổi bật bất thường trong những năm đầu triều con. Bà có **bia riêng ở Ashur**, có bi ký ở Kalhu, và **bia Pazarcık** ghi bà **cùng con vượt sông Euphrates trong chiến dịch** — việc một phụ nữ Assyria được nêu tên cùng vua trên đài kỷ niệm là chuyện gần như độc nhất. Từ bà mọc ra truyền thuyết **Semiramis**, đi qua Herodotus, Ctesias, Diodorus Siculus rồi vào văn chương và nhạc kịch châu Âu tới tận TK 19 — tức rất mạnh ở tiêu chí **độ bền (b)**.
- **Cảnh báo cần viết kèm nếu chọn:** học giới hiện **phần lớn bác bỏ** việc bà thực sự làm **nhiếp chính**; cái chắc chắn là vị thế nổi bật khác thường, không phải quyền nhiếp chính. Viết sai điểm này là lặp đúng lỗi "mệnh đề tối cao không quy thuộc" của cả nhóm.
- **Ứng viên nữ thứ hai, yếu hơn:** **Athaliah**, người duy nhất cai trị Judah với tư cách nữ vương (841–835 TCN) — nhưng bằng chứng chỉ có trình thuật Các Vua, tức làm nặng thêm đúng cái lệch nguồn đã nêu ở bảng trên.

### 3. Đông Á — Chu Mục Vương, và chân trời 841 TCN
- **Chu Mục Vương** (trị vì k. 976–922 TCN): thiên **Lữ hình** (呂刑) của Thượng thư được gán cho triều ông và là văn bản sớm nhất của Trung Hoa bàn về **hình pháp** — ngũ hình, chuộc tội bằng tiền, và lời răn phải xử án thận trọng. Lĩnh vực **Luật** hiện trong nhóm chỉ có **một** mục (Lycurgus), và mục ấy lại mang nhãn `[Truyền thuyết]`. **Phải nói rõ nếu chọn:** niên đại của Lữ hình đang tranh luận, nhiều nhà nghiên cứu xếp nó về cuối Tây Chu hoặc muộn hơn.
- **Chân trời 841 TCN** (nhiếp chính **Cộng Hoà** 共和, sau khi Chu Lệ Vương bị đuổi): đây là **năm sớm nhất có niên đại tuyệt đối liên tục trong sử Trung Hoa**, theo Sử ký. Nhóm này dành hẳn ba mục (-01, -07, -09) để khen giá trị tư liệu của những mốc neo niên đại kiểu đó ở phía Cận Đông, nhưng **mốc tương đương ở Đông Á không được nhắc một chữ**. Dù "Cộng Hoà" khó quy cho một cá nhân (Cộng Bá Hoà 共伯和, hay chế độ đồng nhiếp của Chu Định Công và Thiệu Mục Công), nó **xứng đáng có một dòng trong Ghi chú biên tập**, vì nó là một bất đối xứng về cách đối xử giữa hai vùng trong cùng một nhóm.

### 4. Trung Á — không phải thiếu sót, mà là một **phụ thuộc chưa được nói ra**
Ghi chú biên tập khẳng định Trung Á trống suốt 1200 năm vì lý do tư liệu. Khẳng định ấy **chỉ đúng với điều kiện Zarathustra được đặt ở TK 6 TCN** (`CH02-BCE06-09`). Nhưng niên đại Zarathustra là một trong những tranh luận lớn nhất của ngành: cách định niên theo ngôn ngữ học (Boyce, Skjærvø, Hintze — dựa trên độ gần của tiếng Avesta Gāthā với tiếng Sanskrit Rigveda) đặt ông vào khoảng **1500–1000 TCN**, tức **trong hoặc ngay trước nhóm BCE11_9**; còn mốc TK 6 TCN đến từ truyền thống "258 năm trước Alexander". **Nếu lấy niên đại sớm, Zarathustra rơi vào đúng nhóm này** và một mình ông sửa được cả ba chỗ lệch: thêm vùng **Trung Á**, thêm lĩnh vực **Tôn giáo/Tâm linh + Triết học**, và thêm một mục có **câu hỏi lớn** thật.
- **Đây là vấn đề đặt chỗ liên chapter, không phải ứng viên bị bỏ sót** — và theo ghi chú treo của dự án thì Zarathustra vẫn đang là câu hỏi mở của Ch2. **Khuyến nghị:** thêm một dòng vào mục "Nhân vật có thể thuộc thế kỷ khác" của Ch1 nói rõ rằng việc nhóm BCE11_9 không có mục Trung Á là **hệ quả của quyết định đặt Zarathustra ở Ch2**, chứ không phải của tư liệu. Hiện tại người đọc không có cách nào biết điều đó.

### 5. Các vùng thật sự trống — xác nhận, không phản đối
- **Châu Phi hạ Sahara:** vua Napata có tên sớm nhất là **Alara** (k. 785–760 TCN), **sau** mốc 801 TCN; Piye đã nằm ở `CH02-BCE08-06`. Văn hoá Nok không để lại tên người. **Không có ứng viên.**
- **Châu Mỹ:** La Venta thịnh k. 900–400 TCN và Chavín de Huántar từ k. 900 TCN, nhưng không hệ chữ nào giải mã được nêu tên cá nhân. **Không có ứng viên.**
- **Châu Đại Dương:** đợt bành trướng Lapita phần lớn đã xong trước 800 TCN và không để lại tên. **Không có ứng viên.**
- **Đông Nam Á:** Ghi chú biên tập đã xử lý đầy đủ và đúng (Phùng Nguyên → Đông Sơn sớm, không chữ viết; Hùng Vương không đặt được vào một thế kỷ). **Không có ứng viên.**
- **Châu Âu ngoài Lycurgus:** Homer ở `CH02-BCE08-01` là chỗ đúng theo niên đại soạn thông dụng (k. 750–700 TCN); việc người Hy Lạp mượn bảng chữ cái quanh 800 TCN không gắn với tên ai. **Không có ứng viên.**

## Kết luận về lựa chọn

Nhóm **không** mắc lỗi hệ thống số 6 của `CONTRIBUTING.md` (nêu làm "ứng viên bị loại" một người đã được chọn chỗ khác): **cả 12 mục đều nói ra** khi người được nêu có mục riêng. Đây là tiến bộ rõ so với Ch3.

Nhóm **vẫn mắc** lỗi hệ thống số 5 (ứng viên "cùng thời" không cùng thời), **ba lần không nói ra**: `-07` (Psusennes I sớm hơn ~55 năm, Osorkon II muộn hơn ~50–85 năm), `-06` (Ithobaal I muộn hơn ~70–100 năm), `-10` (Nathan sớm hơn ~130–150 năm, lại còn được gọi là "thế hệ trước"). Lỗi ở `-10` nặng nhất vì mục vừa nêu Nathan vừa khẳng định mô-típ "bắt đầu rõ nét ở Elijah" — hai câu phủ định nhau.

Lỗ hổng lớn nhất về lựa chọn **không phải vùng mà là thể loại nhân vật**: 8/12 là vua, 9/12 không gắn với câu hỏi lớn nào. Giai đoạn 1100–801 TCN **có** những người không phải vua để chọn — Parikṣit/Janamejaya ở phía tổ chức tri thức Vệ-đà là ví dụ rõ nhất — và việc nhóm chỉ còn mỗi Elijah và Chu Công Đán ở ngoài hàng ngũ quân vương là một kết quả của cách tìm, không phải của tư liệu.
