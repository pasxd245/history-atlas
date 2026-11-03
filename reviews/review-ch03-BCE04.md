# Bình duyệt độc lập — `content/ch03.md`, nhóm **BCE04** (TK 4 TCN, 400–301 TCN)

Người rà: agent bình duyệt độc lập (không viết chapter này).
Ngày: 2026-10-31.
Phạm vi: dòng `**Bối cảnh**` của nhóm BCE04 và 11 mục `CH03-BCE04-01` → `CH03-BCE04-11`. Không rà BCE03/BCE02/BCE01.

Phân loại: **Sai** (sai sự thật, phải sửa) · **Nghi vấn** (khả nghi / gây hiểu sai) · **Thiếu** (thiếu hedge, thiếu ghi nhận tranh luận) · **Thể thức** (vi phạm template §5).

---

## 0 · Kết quả đối chiếu Wikidata (toàn nhóm)

Gọi `wbgetentities` (labels/descriptions) + `wbgetclaims` (P569/P570) cho cả 11 Q-ID, 2026-10-31.

| ID mục | Q-ID | Nhãn Wikidata en | `năm:` trong file | P569 / P570 (rank preferred nếu có) | Độ tin cậy | Kết luận |
|---|---|---|---|---|---|---|
| -01 Plato | Q859 | Plato | k. 427–347 | −428 / −348 | Trung bình (±25) | khớp |
| -02 Aristotle | Q868 | Aristotle | 384–322 | −384 / −322 | Cao (±5) | khớp |
| -03 Alexander | Q8409 | Alexander the Great | 356–323 | −356-07-20 / −323-06-10 | Cao (±5) | khớp |
| -04 Mạnh Tử | Q188903 | Mencius | k. 372–289 | −372 / −289 | Trung bình | khớp |
| -05 Trang Tử | Q47739 | Zhuang Zhou | k. 369–286 | −369 / −288 | Trung bình | khớp |
| -06 Thương Ưởng | Q351345 | Shang Yang | k. 390–338 | −390 / −338 | Trung bình | khớp |
| -07 Kauṭilya | Q9045 | Chanakya | k. 375–283 | −375 / −283 | Thấp | khớp |
| -08 Chandragupta | Q188541 | Chandragupta Maurya | k. 340–297 | −340 / −297 | Trung bình | khớp |
| -09 Eudoxus | Q185150 | Eudoxus of Cnidus | k. 408–355 | −408 / −355 | Trung bình | khớp |
| -10 Diogenes | Q59180 | Diogenes of Sinope | k. 412–323 | −400 (pref) / −323 | Thấp (bỏ qua) | khớp nhãn |
| -11 Praxiteles | Q105290 | Praxiteles | k. 395–330 | −395 / −330 | Thấp | khớp |

**Không có lỗi Q-ID nào trong nhóm này** — cả 11 nhãn đều trỏ đúng người, không có ca gộp nhầm kiểu Patañjali/Q231680.

Hai ghi chú để dùng về sau, không phải lỗi:
- **Q188541 (Chandragupta)**: mô tả tiếng Anh của chính Wikidata ghi "(350–295 BCE)" trong khi P569/P570 ghi −340/−297. Wikidata tự mâu thuẫn; file chọn theo P569/P570 là lựa chọn đúng, nhưng đừng coi con số này là đã được xác lập.
- **Q59180 (Diogenes)**: P569 có ba giá trị cạnh tranh (−412, −403, −400, giá trị `preferred` là −400). File ghi k. 412; vì độ tin cậy Thấp nên lint bỏ qua, song con số 412 là một trong ba, không phải con số được Wikidata ưu tiên.

---

## Bối cảnh nhóm BCE04

> "Thành bang Hy Lạp suy yếu sau chiến tranh Peloponnese rồi bị Macedonia thu phục; chinh phục của Alexander mở ra thế giới Hellenistic. Ở Trung Hoa, thời Chiến Quốc đẩy các nước lớn vào cải cách pháp chế. Bắc Ấn Độ chuyển từ các mahājanapada sang đế chế Maurya."

Không có lỗi sự thật. Ba mệnh đề đều đứng được và đều trung tính. Độ dài nằm trong trần 60 chữ.

Một nhận xét về **độ phủ**, không phải lỗi của riêng dòng này: bối cảnh nêu ba vùng, và nhóm cũng chỉ có ba vùng (Châu Âu 6, Đông Á 3, Nam Á 2). §5 yêu cầu "ít nhất 3 vùng khi tư liệu cho phép" nên nhóm đạt chuẩn tối thiểu — nhưng xem mục "Đánh giá lựa chọn nhân vật" ở cuối báo cáo: với TK 4 TCN thì tư liệu **có** cho phép nhiều hơn ba vùng, và nhóm còn một chỗ trống (11/12).

---

## CH03-BCE04-01 · Plato

### Nghi vấn — "trước tác ... của họ chỉ còn một phần" nói sai về Xenophon

> "Plato vượt cả hai theo độ bền (b) và phạm vi (a): **toàn bộ trước tác của ông còn nguyên trong khi của họ chỉ còn một phần**"

"Họ" ở đây là Isocrates và Xenophon. Mệnh đề đúng với Isocrates (còn 21 bài diễn văn và 9 lá thư trên khoảng 60 tác phẩm từng được quy cho ông), nhưng **sai với Xenophon**: toàn bộ corpus Xenophon được truyền lại gần như nguyên vẹn, và ông thường được nêu đúng như một ngoại lệ — người duy nhất ngoài Plato trong số môn đồ Socrates có trước tác còn trọn.

- Cái đúng: Xenophon không thua Plato ở độ bền văn bản; chỗ ông thua là độ sâu triết học và sức sinh ra truyền thống kế tiếp.
- Nguồn: SEP, "Plato" (Richard Kraut, bản sửa 2026-04-24, https://plato.stanford.edu/entries/plato/) — mục bàn Xenophon chỉ nói chân dung Socrates của Xenophon "thiếu độ tinh tế và chiều sâu triết học" so với Plato, **không** nói gì về chuyện mất mát văn bản. Tức chính nguồn được dẫn ở mục này không chống đỡ được câu đang viết.
- Câu thay thế đề xuất: "Plato vượt cả hai theo độ bền (b) và phạm vi (a): Isocrates chỉ còn khoảng một phần ba số bài được quy cho ông, còn Xenophon — dù corpus còn gần trọn — không sinh ra một truyền thống diễn giải nối tiếp; trong khi truyền thống Tân Plato qua Plotinus đã thành khung tư duy cho thần học Kitô giáo lẫn Hồi giáo nhiều thế kỷ."

### Thiếu — "suốt mười lăm thế kỷ" là con số không quy thuộc

> "truyền thống Tân Plato qua Plotinus đã thành khung tư duy cho thần học Kitô giáo lẫn Hồi giáo **suốt mười lăm thế kỷ**"

Con số 15 thế kỷ (tính từ Plotinus TK 3 CN sẽ ra TK 18) là một đánh giá về độ bền, không phải một dữ kiện; mức độ Tân Plato còn là "khung tư duy" của thần học sau Cải cách và sau Kant là điều tranh luận được. Prompt dự án cấm "tô vẽ" và yêu cầu không viết chung chung như một kết luận của giới nghiên cứu.
- Câu thay thế đề xuất: bỏ "suốt mười lăm thế kỷ", hoặc đổi thành "từ Late Antiquity tới ít nhất thời Phục hưng".

### Ghi nhận — phần không có lỗi

- "lập Academy ở Athens khoảng năm 387 TCN": mốc quy ước, có chữ "khoảng" — đạt.
- Nguồn SEP "Plato" **tồn tại** (đã mở, HTTP 200, tác giả Richard Kraut). Lưu ý nhỏ: entry này **không** bàn việc lập Academy năm 387, nên nếu muốn giữ con số thì cần nguồn thứ hai; "Plato, Cộng hoà" cũng không nói điều đó.
- "Vì sao chọn" nêu đích danh Isocrates (436–338 TCN) và Xenophon (k. 430–354 TCN) — cả hai **thật sự cùng thời** với Plato (k. 427–347). Đạt thể thức §5. Cả hai cũng nằm trong danh sách bị loại ở Ghi chú biên tập (Isocrates có tên; Xenophon thì không — xem mục cuối).
- Liên kết `Kế thừa từ`: CH02-BCE05-01 = Socrates, CH02-BCE05-02 = Parmenides, CH02-BCE06-06 = Pythagoras. Cả ba đích đều đúng người và đúng chiều niên đại.
- Liên kết `Ảnh hưởng tới`: CH03-BCE04-02 = Aristotle (đúng), CH03-BCE03-07 = Zeno xứ Citium (đúng). Đúng chiều.

---
## CH03-BCE04-02 · Aristotle

### Sai — "giữ vị trí độc tôn cho tới khi Frege viết lại luận lý vào thế kỷ 19"

> "Bộ Organon đặt ra luận lý hình thức đầu tiên, với tam đoạn luận làm hạt nhân; **nó giữ vị trí độc tôn cho tới khi Frege viết lại luận lý vào thế kỷ 19**."

Hai lỗi chồng lên nhau.

1. **"độc tôn" trong thời cổ đại là sai.** Luận lý mệnh đề của phái Khắc kỷ, mà Chrysippus là người hệ thống hoá, là một hệ thống **đối lập** với tam đoạn luận hạn từ của Aristotle và tồn tại song song suốt thời Hellenistic; thời cổ đại coi đây là hai trường phái luận lý cạnh tranh. Điều này đáng chú ý hơn nữa vì chính chapter này có mục Zeno xứ Citium (`CH03-BCE03-07`), người lập phái ấy.
2. **Mốc "Frege ... thế kỷ 19" bỏ qua Boole.** George Boole đã đại số hoá luận lý trong *The Mathematical Analysis of Logic* (1847) và *An Investigation of the Laws of Thought* (1854), tức hơn hai mươi năm trước *Begriffsschrift* của Frege (1879). Nếu muốn nêu một mốc "phá thế độc tôn" thì mốc sớm hơn là Boole, không phải Frege.

- Câu thay thế đề xuất: "Bộ Organon đặt ra hệ luận lý hình thức được hệ thống hoá sớm nhất còn lại của phương Tây, với tam đoạn luận làm hạt nhân; nó cạnh tranh với luận lý mệnh đề của phái Khắc kỷ thời cổ đại, rồi thống trị chương trình học phương Tây cho tới khi bị thay thế bởi luận lý toán học của Boole (1847) và Frege (1879)."

### Nghi vấn — gọi sinh vật học của Aristotle là "thực nghiệm"

> "Phần sinh vật học dựa trên quan sát trực tiếp ở Lesbos, mô tả và phân loại hàng trăm loài, là **công trình thực nghiệm quy mô lớn sớm nhất** còn lại."

Chính câu này tự mâu thuẫn: "quan sát trực tiếp" và "mô tả, phân loại" là công việc **quan sát và mô tả**, không phải thực nghiệm (experiment — can thiệp có kiểm soát vào đối tượng). Aristotle có giải phẫu, nhưng không thiết kế thí nghiệm theo nghĩa thông thường của từ này. Dùng "thực nghiệm" ở đây dễ dẫn người đọc Việt Nam tới một hiểu sai cụ thể về lịch sử phương pháp khoa học.
- Câu thay thế đề xuất: "... là công trình **quan sát và mô tả sinh vật** quy mô lớn sớm nhất còn lại."

### Thể thức — "chính Plato, thầy ông" không phải ứng viên bị loại

> "Ứng viên cùng trường là Theophrastus, ... và **chính Plato, thầy ông**."

§5 yêu cầu nêu đích danh 1–2 người cùng lĩnh vực, cùng thời **đã được cân nhắc** và bị xếp sau. Plato **có mặt trong chính nhóm này** (`CH03-BCE04-01`), ở ngay mục liền trước. Nêu một người đã được chọn làm "ứng viên" cho chỗ của người khác là vô nghĩa: không có sự đánh đổi nào xảy ra, nên lập luận "Aristotle được chọn" không nói được điều gì. Thực tế mục này chỉ có **một** ứng viên hợp lệ (Theophrastus).
- Đề xuất: thay "chính Plato, thầy ông" bằng một ứng viên thật sự bị loại và thật sự cùng thời — ví dụ **Xenocrates** (k. 396–314 TCN, trưởng Academy 339–314, cùng thời trọn vẹn với Aristotle 384–322, và là người cạnh tranh trực tiếp chức trưởng Academy với ông), hoặc **Heraclides Ponticus** (k. 390–310 TCN).

### Nghi vấn — liên kết `Ảnh hưởng tới` CH03-BCE03-03 (Euclid)

> "- CH03-BCE03-03 · kế thừa · qua trường phái"

Đích trỏ đúng người (CH03-BCE03-03 = Euclid). Nhưng quan hệ "Euclid kế thừa Aristotle" là một **luận điểm học giả còn tranh luận** (rằng cấu trúc tiên đề của *Cơ sở* chịu ảnh hưởng lý thuyết chứng minh trong *Posterior Analytics*), không phải một dữ kiện. Theo từ vựng dự án, mức bằng chứng đúng ở đây là **`suy đoán học giả`**, không phải `qua trường phái`.
- Đề xuất: đổi mức bằng chứng thành `suy đoán học giả`.

### Ghi nhận — phần không có lỗi

- `năm: 384–322 TCN`, độ tin cậy **Cao** (±5): Wikidata Q868 P569 = −384 (preferred), P570 = −322 (preferred). Khớp chính xác.
- Nguồn SEP "Aristotle" (https://plato.stanford.edu/entries/aristotle/) tồn tại. Jonathan Barnes (chủ biên), *The Complete Works of Aristotle: The Revised Oxford Translation*, Princeton University Press, 1984 — đúng tên, đúng vai trò chủ biên, đúng năm.
- "quan sát trực tiếp ở Lesbos": đúng; phần lớn tư liệu sinh vật biển trong *Historia Animalium* gắn với đầm Pyrrha trên đảo Lesbos.
- `Kế thừa từ` CH03-BCE04-01 (Plato, `phản bác`) và CH02-BCE05-05 (Democritus, `phản bác`) — cả hai đích đúng người, đúng chiều, đúng loại quan hệ.
- `Ảnh hưởng tới` CH03-BCE04-03 = Alexander: đúng người, đúng chiều (gia sư của Alexander từ k. 343 TCN).
- Theophrastus là ứng viên bị loại **thật**: có tên trong danh sách ở Ghi chú biên tập cuối file, và cùng thời thật (k. 371–287 TCN).

---
## CH03-BCE04-03 · Alexander Đại đế

### Sai — liên kết `Kế thừa từ: CH02-BCE05-10 · phản bác · trực tiếp` trỏ nhầm Darius

> **Kế thừa từ:**
> "- CH02-BCE05-10 · phản bác · trực tiếp"

`CH02-BCE05-10` là **Darius I** (`năm: k. 550–486 TCN`, Q44387), không phải Darius III (trị vì 336–330 TCN) — người mà Alexander thực sự đánh bại ở Issus và Gaugamela. Alexander sinh năm 356 TCN, tức **130 năm sau khi Darius I chết**. Mức bằng chứng `trực tiếp` là bất khả về mặt niên đại.

Lỗi lộ ra rõ hơn khi đối chiếu hai chiều: mục Darius I ở `content/ch02.md` ghi ngược lại

> **Ảnh hưởng tới:**
> "- Alexander Đại đế · kế thừa · qua trường phái"

Hai mục mô tả **cùng một cặp** bằng hai loại quan hệ trái nhau (`phản bác` vs `kế thừa`) và hai mức bằng chứng trái nhau (`trực tiếp` vs `qua trường phái`). Lint chỉ quét chiều `Kế thừa từ` nên không bắt được mâu thuẫn này.

- Cái đúng: quan hệ Alexander–Darius I là quan hệ **kế thừa thiết chế** (Alexander giữ lại bộ máy satrapy, hệ thuế và mạng đường trạm của Achaemenid), đúng như chính mục Darius I viết trong "Vì sao chọn": "được Alexander, Seleucid, Parthia rồi Rome tiếp nhận". Không có quan hệ `phản bác trực tiếp` nào.
- Nguồn: `content/ch02.md` dòng 643–644 và 659–661; Pierre Briant, *From Cyrus to Alexander* (2002) — chính nguồn mục Darius I dẫn — là công trình lập luận cho tính liên tục Achaemenid–Hellenistic.
- Dòng thay thế đề xuất: `- CH02-BCE05-10 · kế thừa · qua trường phái` (và sửa lại mục Darius I cho khớp, hoặc chỉ giữ một chiều).

### Nghi vấn — `Ảnh hưởng tới: CH03-BCE04-08 · kế thừa · trực tiếp` (Chandragupta)

Đích trỏ đúng người. Nhưng toàn bộ bằng chứng cho một quan hệ **trực tiếp** Alexander → Chandragupta là một giai thoại trong Plutarch (*Alexander* 62) kể rằng "Androcottus" khi còn trẻ đã gặp Alexander — một mẩu chuyện muộn, một dòng, không được xác nhận ở đâu khác, và bản thân việc đồng nhất Androcottus với Chandragupta là suy luận của học giả hiện đại. Mức `trực tiếp` vượt quá bằng chứng.
- Đề xuất: đổi thành `suy đoán học giả`, hoặc bỏ liên kết này và giữ ảnh hưởng gián tiếp (sự sụp đổ của quyền lực Macedonia ở Punjab tạo khoảng trống cho Chandragupta).
- Lưu ý: mục `CH03-BCE04-08` ghi chiều ngược lại cũng bằng `trực tiếp`, nên nếu sửa thì phải sửa cả hai.

### Nghi vấn — `Ảnh hưởng tới: CH03-BCE03-04 · kế thừa · qua trường phái` (Ptolemaios I)

Ptolemaios I Soter là **somatophylax và tướng trực tiếp của Alexander**, người cướp thi hài ông đưa về Ai Cập và tự viết hồi ký về chiến dịch (nguồn chính của Arrian). Đây là quan hệ trực tiếp nhất có thể có; gán `qua trường phái` là đánh giá thấp bằng chứng, và không nhất quán với dòng ngay bên dưới ("Các vương quốc Hellenistic và Hy Lạp–Bactria · kế thừa · trực tiếp").
- Đề xuất: đổi thành `trực tiếp`.

### Thiếu — "kế hoạch của Philip, vốn chỉ nhắm Tiểu Á" nói chắc về một điểm còn tranh luận

> "phạm vi và hướng của cuộc viễn chinh, nhất là việc đi tới sông Ấn, không suy ra được từ kế hoạch của Philip, **vốn chỉ nhắm Tiểu Á**."

Cái chắc chắn là **đội tiền trạm** năm 336 TCN dưới Parmenion và Attalus được giao nhiệm vụ "giải phóng các thành phố Hy Lạp" ở Tiểu Á (Diodorus 16.91). Cái **không** chắc chắn là tham vọng cuối cùng của Philip: giới nghiên cứu còn chia rẽ về việc Philip định dừng ở Tiểu Á hay định đánh đổ cả đế chế, và không có nguồn cổ nào nói Philip "chỉ nhắm Tiểu Á". Mục này biến một suy luận từ quy mô đội tiền trạm thành một dữ kiện, rồi dựng counterfactual (d) — tức toàn bộ lý do chọn — lên trên nó.
- Nguồn: Diodorus Siculus 16.89 và 16.91 (bản Perseus, http://perseus.uchicago.edu/perseus-cgi/citequery3.pl?dbname=GreekFeb2011&getid=1&query=Diod.+Sic.+16.89); tổng quan tranh luận ở mục "Expansion of Macedonia under Philip II".
- Câu thay thế đề xuất: "... không suy ra được từ những gì ta biết về kế hoạch của Philip, mà bằng chứng chắc chắn duy nhất là đội tiền trạm năm 336 TCN được giao giải phóng các thành phố Hy Lạp ở Tiểu Á; tham vọng cuối cùng của Philip vẫn là điểm tranh luận."

### Ghi nhận — phần không có lỗi

- `năm: 356–323 TCN`, Cao (±5): Q8409 P569 = −356-07-20, P570 = −323-06-10. Khớp chính xác.
- "Trong mười một năm": chiến dịch châu Á khởi từ 334 TCN tới khi ông chết 323 TCN = 11 năm. Đúng.
- "trật tự Ba Tư đã đứng hai thế kỷ": Achaemenid 550–330 TCN = 220 năm. Đúng.
- Nguồn: Arrian, *Anabasis Alexandri* — có thật, là nguồn chính. Robin Lane Fox, *Alexander the Great*, Allen Lane, **1973** — đúng tên, đúng năm.
- "Vì sao chọn" nêu Philip II (382–336 TCN) — thật sự cùng thời với Alexander (356–323). Đạt thể thức, dù chỉ nêu một người (§5 cho phép 1–2).
- `Kế thừa từ` CH03-BCE04-02 = Aristotle: đúng người, đúng chiều.

---
## CH03-BCE04-04 · Mạnh Tử

### Sai — Nhật Bản không có khoa cử lấy Tứ thư làm nội dung bắt buộc

> "từ khi Chu Hy xếp sách ông vào Tứ thư thế kỷ 12, văn bản này thành nội dung khoa cử bắt buộc ở Trung Hoa, Triều Tiên, **Nhật Bản** và Việt Nam"

Ba nước kia đúng; **Nhật Bản sai**. Nhật có một hệ thi cử phỏng theo Trung Hoa thời Heian, nhưng nó dành cho việc thăng chức của quý tộc nhỏ, dựa trên kinh điển Hán học thời đó chứ không phải Tứ thư (Tứ thư chỉ thành bộ sau Chu Hy, 1190), và đã bị chế độ thế tập thay thế từ thời Kamakura (sau 1185). Thời Tokugawa, Chu Tử học là học thuyết chính thống nhưng **không hề có chế độ khoa cử tuyển quan**: quan chức bakufu và các han được bổ nhiệm theo thân phận thế tập. Nêu Nhật Bản ở đây là nói sai về đúng cái điểm đang được dùng làm bằng chứng cho tiêu chí độ bền (b).

- Cái đúng: Tứ thư là nội dung khoa cử bắt buộc ở **Trung Hoa, Triều Tiên (Joseon) và Việt Nam**. Ở Nhật Bản, Chu Tử học có ảnh hưởng lớn qua các phiên hiệu và Shōheizaka Gakumonjo, nhưng không qua khoa cử.
- Nguồn: Wikipedia "Education in Joseon" và "Vietnamese Confucianism" (xác nhận Tứ thư là nội dung thi ở Triều Tiên và Việt Nam); về Nhật, hệ thi Heian bị thay bằng thế tập từ thời samurai.

### Sai — "suốt bảy thế kỷ" lệch khoảng 120 năm

> "**từ khi Chu Hy xếp sách ông vào Tứ thư thế kỷ 12**, văn bản này thành nội dung khoa cử bắt buộc ... **suốt bảy thế kỷ**."

Câu này ghép hai mốc khác nhau rồi tính thời lượng theo mốc sai. Chu Hy công bố *Tứ thư tập chú* năm **1190**, nhưng Tứ thư với chú giải của ông chỉ trở thành **nội dung thi bắt buộc** từ chiếu chỉ năm **1313** đời Nguyên, và giữ nguyên tới khi khoa cử bị bãi năm **1905**. Tức giai đoạn "khoa cử bắt buộc" là **1313–1905 ≈ 592 năm, chưa tới sáu thế kỷ**, không phải bảy. Con số bảy thế kỷ chỉ đúng nếu tính từ 1190 — nhưng trong khoảng 1190–1313 thì mệnh đề "nội dung khoa cử bắt buộc" lại không đúng.

- Nguồn: chiếu chỉ 1313 lấy chú giải Tứ thư của Chu Hy (công bố 1190) làm bản diễn giải chính thức và làm cơ sở khoa cử, có hiệu lực tới khi khoa cử bị bãi năm 1905.
- Câu thay thế đề xuất: "Mạnh Tử được chọn theo độ bền (b): sau khi Chu Hy xếp sách ông vào Tứ thư năm 1190, chú giải ấy được lấy làm chuẩn khoa cử từ năm 1313 và giữ vị trí đó tới khi khoa cử bị bãi năm 1905 — gần sáu thế kỷ ở Trung Hoa, và ở Triều Tiên cùng Việt Nam cũng là nội dung thi bắt buộc."

### Nghi vấn — "lập luận quy nạp" mô tả sai hình thức lập luận

> "Thí dụ đứa bé sắp ngã xuống giếng là **lập luận quy nạp** về bản tính được dẫn lại nhiều nhất trong triết học Trung Hoa."

Đoạn 2A6 là một **thí nghiệm tư tưởng** (thought experiment): Mạnh Tử mời người đọc xét một tình huống giả định và tự quan sát phản ứng của chính mình, chứ không khái quát từ một tập hợp quan sát thực tế — tức không phải quy nạp. SEP gọi đúng nó là "famous thought experiment".
- Nguồn: SEP, "Mencius" (Bryan Van Norden, bản sửa 2024-09-27, https://plato.stanford.edu/entries/mencius/), mục bàn 2A6.
- Câu thay thế đề xuất: "Thí dụ đứa bé sắp ngã xuống giếng là thí nghiệm tư tưởng về bản tính được dẫn lại nhiều nhất trong triết học Trung Hoa."

### Nghi vấn (thể thức nhẹ) — "ứng viên cùng thời" Tuân Tử gần như không trùng đời hoạt động

> "Ứng viên cùng truyền thống là Tuân Tử, người chủ trương tính ác và được chọn riêng ở nhóm sau"

Tuân Tử ghi `k. 313–230 TCN` (`CH03-BCE03-11`), Mạnh Tử `k. 372–289 TCN`. Hai đời chỉ chồng nhau 313–289, và trong khoảng đó Tuân Tử ở tuổi 0–24 còn Mạnh Tử ở tuổi 59–83. Hai người không hề tranh luận với nhau; Tuân Tử phản bác Mạnh Tử trong văn bản, sau khi Mạnh Tử đã chết. Đây đúng là dạng ca mà `CONTRIBUTING.md` §5 cảnh báo (Tử Sản / Quản Trọng). Mục này viết "cùng truyền thống" chứ không viết "cùng thời" nên không sai hẳn, nhưng nó cũng không cung cấp được **ứng viên cạnh tranh cùng thời** mà §5 đòi; và Tuân Tử lại **đã được chọn** ở nhóm sau, nên không phải ứng viên bị loại.
- Ứng viên hợp lệ hơn, cùng thời thật: **Huệ Thi (惠施, k. 370–310 TCN)** hoặc **Thận Đáo (慎到, k. 350–275 TCN)**. Cáo Tử thì giữ được — nhưng Cáo Tử chỉ tồn tại qua chính sách Mạnh Tử, nên nêu ông làm "ứng viên bị loại" cũng yếu.

### Ghi nhận — phần không có lỗi

- Q188903 = Mencius, P569 −372 / P570 −289, khớp `k. 372–289 TCN` ở mức Trung bình (±25). Nhãn đúng người.
- Nguồn SEP "Mencius" **tồn tại** và **thật sự bàn** cả ba điều được dẫn: tứ đoan, thí dụ đứa bé bên giếng (2A6), và việc Chu Hy gộp Tứ thư (mục 5). Đây là một dòng Nguồn đạt chuẩn.
- "bốn mầm — trắc ẩn, tu ố, từ nhượng, thị phi": đúng bốn 四端 (惻隱, 羞惡, 辭讓, 是非).
- "đặt dân lên trước xã tắc và vua": đúng, Mạnh Tử 7B14 (民為貴，社稷次之，君為輕).
- "giết một bạo chúa thì không phải là thí quân": đúng, Mạnh Tử 1B8.
- Liên kết: `Kế thừa từ` CH02-BCE06-01 = Khổng Tử (đúng). `Ảnh hưởng tới` CH03-BCE03-11 = Tuân Tử (đúng người; `phản bác · trực tiếp` chấp nhận được vì Tuân Tử phản bác đích danh trong *Tính ác* và *Phi thập nhị tử*), CH03-BCE02-01 = Đổng Trọng Thư (đúng người, đúng chiều).

---
## CH03-BCE04-05 · Trang Tử

### Sai — "văn bản của ông còn nguyên vẹn"

> "Trang Tử được chọn theo độ bền (b) và tính nguyên bản (c): **văn bản của ông còn nguyên vẹn**, và chính lập trường hoài nghi ngôn ngữ ấy là thành phần Trung Hoa hoà vào Phật giáo để thành Thiền tông."

Sách *Trang Tử* **không** còn nguyên vẹn. Bản lưu hành là bản biên tập 33 thiên của Quách Tượng (郭象, mất 312 CN), được rút gọn từ một bản 52 thiên mà *Hán thư · Nghệ văn chí* còn ghi — tức khoảng 19 thiên đã mất trong quá trình biên tập. Điều này nghiêm trọng hơn vì chính mục này đang lấy "còn nguyên vẹn" làm **lý do chọn** đối lại Liệt Tử và Dương Chu.

- Nguồn: SEP, "Zhuangzi" (xuất bản 2014-12-17, sửa 2024-03-24, https://plato.stanford.edu/entries/zhuangzi/) — nói thẳng rằng Quách Tượng rút bộ sưu tập trước đó "from fifty-two chapters to thirty-three", và bản 33 thiên chia Nội thiên 1–7, Ngoại thiên 8–22, Tạp thiên 23–33.
- Câu thay thế đề xuất: "Trang Tử được chọn theo độ bền (b) và tính nguyên bản (c): bảy thiên Nội thiên được truyền lại liên tục và vẫn được coi là của chính ông, trong khi văn bản của hai người kia đều không ở tình trạng ấy — dù bản *Trang Tử* hiện hành chỉ là bản 33 thiên do Quách Tượng rút từ một bản 52 thiên thời Hán."

### Nghi vấn — "ông không bàn phép trị nước" bị chính Nội thiên bác lại

> "Khác Lão Tử ở chỗ **ông không bàn phép trị nước**, mà hướng vào tự do của cá nhân trước các chuẩn mực xã hội"

Thiên thứ bảy của Nội thiên — tức nằm trọn trong phần mà chính mục này vừa nói "được coi là của chính ông" — là **Ứng đế vương (應帝王)**, nghĩa đen "Đáp ứng bậc đế vương", và nội dung là về cách người đạt đạo ứng xử với việc cai trị. Các thiên Ngoại thiên như *Thiên địa*, *Thiên đạo* còn bàn trị nước nhiều hơn nữa. Mệnh đề "không bàn phép trị nước" vì thế quá mạnh.
- Câu thay thế đề xuất: "Khác Lão Tử ở chỗ trọng tâm của ông không phải thuật trị nước mà là tự do của cá nhân trước các chuẩn mực xã hội — dù Nội thiên vẫn khép lại bằng thiên *Ứng đế vương* bàn tới việc cai trị."

### Nghi vấn (thể thức) — Dương Chu và Liệt Tử đều không thật sự "cùng thời"

> "Ứng viên cùng dòng là **Liệt Tử**, mà văn bản mang tên ông phần lớn được xác định là nguỵ tác đời sau, và **Dương Chu**, chỉ còn qua trích dẫn của người khác."

- **Dương Chu**: niên đại thường được đặt k. 440–360 TCN. Trang Tử k. 369–286 TCN. Hai đời chồng nhau khoảng chín năm, trong đó Trang Tử còn là đứa trẻ. Không phải "ứng viên cùng thời" theo nghĩa §5 đòi.
- **Liệt Tử**: bản thân sự tồn tại lịch sử của nhân vật này là điều ngờ vực — ông xuất hiện chủ yếu như một **nhân vật trong chính sách Trang Tử**, và sách mang tên ông là hợp soạn TK 3–4 CN. Đưa một nhân vật có thể hư cấu vào vai "ứng viên cạnh tranh đã bị loại" làm rỗng chính cái việc so sánh mà §5 yêu cầu.
- Ứng viên hợp lệ hơn, cùng thời thật: **Huệ Thi (惠施, k. 370–310 TCN)** — người đối thoại thường xuyên nhất của Trang Tử trong chính văn bản, cùng thời trọn vẹn, cùng lĩnh vực Triết học, và là đại diện của phái Danh gia mà Trang Tử phản bác. Đây là ứng viên tự nhiên nhất và mục này lại không nhắc tới.

### Thiếu — mệnh đề về Thiền tông không quy thuộc

> "chính lập trường hoài nghi ngôn ngữ ấy là **thành phần Trung Hoa hoà vào Phật giáo để thành Thiền tông**"

Luận điểm "Thiền = Phật giáo + Trang Tử/Đạo gia" là một giả thuyết quen thuộc nhưng **đang bị tranh luận mạnh** trong nghiên cứu Thiền tông từ thập niên 1980 trở đi (hướng phê phán cho rằng câu chuyện "Đạo hoá" ấy phần lớn do truyền thống Thiền đời sau và học giới Nhật thế kỷ 20 dựng lên). Viết thẳng như một dữ kiện là vi phạm yêu cầu trung lập.
- Câu thay thế đề xuất: "... và lập trường hoài nghi ngôn ngữ ấy thường được coi là một trong những thành phần Trung Hoa hoà vào Phật giáo để thành Thiền tông, dù mức độ ảnh hưởng này còn tranh luận."

### Ghi nhận — phần không có lỗi

- Q47739 = Zhuang Zhou, P569 −369 / P570 −288; file ghi `k. 369–286`, Trung bình (±25) — khớp.
- Nguồn SEP "Zhuangzi" tồn tại và bàn đúng các điểm được dẫn (Tề vật luận, cấu trúc văn bản).
- "bảy thiên Nội thiên được coi là của chính ông": đúng, và SEP xác nhận Quách Tượng chỉ quy phần đầu cho thời Trang Tử.
- "Thiên Tề vật luận", "giấc mộng hồ điệp": đúng; hồ điệp nằm ở cuối thiên Tề vật luận (thiên 2).
- `Kế thừa từ` CH02-BCE06-02 = Lão Tử: đúng người, đúng chiều.
- `Ảnh hưởng tới` chỉ dùng tên trào lưu, không có ID sai đích.
- Nguồn "Trang Tử, *Nam Hoa kinh*": đúng — *Nam Hoa chân kinh* là tên được phong năm 742 CN cho chính sách này, không phải một tác phẩm khác.

---
## CH03-BCE04-06 · Thương Ưởng

### Nghi vấn — "hai mươi bậc tước" là con số của hệ thống **về sau**, không phải của cải cách Thương Ưởng

> "Hai đợt cải cách ở nước Tần, khởi từ khoảng năm 356 và 350 TCN, thay chế độ quý tộc thế tập bằng **hai mươi bậc tước ban theo quân công**"

Hệ nhị thập đẳng tước (二十等爵) đúng là hệ thống Tần rồi Tây Hán dùng, nhưng nó **không ra đời đủ hai mươi bậc ngay từ cải cách của Thương Ưởng**: nó bắt đầu với số bậc ít hơn và lớn dần về sau. Viết "thay ... bằng hai mươi bậc tước" đặt con số cuối cùng vào thời điểm khởi đầu.

- Nguồn: SEP, "Legalism in Chinese Philosophy" (Yuri Pines — chính tác giả cuốn sách mục này dẫn), https://plato.stanford.edu/entries/chinese-legalism/ : cải cách nổi tiếng nhất của Thương Ưởng là thay trật tự quý tộc thế tập bằng hệ ranks of merit "consisting of 20 (**initially fewer**) ranks".
- Nguồn này cũng ghi rằng các bậc thấp ngoài việc ban theo quân công còn **có thể mua bằng thóc dư** — nên "ban theo quân công" cũng là một nửa bức tranh.
- Câu thay thế đề xuất: "... thay chế độ quý tộc thế tập bằng một hệ bậc tước ban theo quân công — về sau định hình thành hai mươi bậc — mà các bậc thấp còn có thể đổi bằng thóc nộp thêm, ..."

### Thiếu — "cải cách của Thân Bất Hại không sống quá đời ông" là phán đoán của nguồn cổ, không phải dữ kiện

> "Thương Ưởng được chọn theo counterfactual (d): **cải cách của Thân Bất Hại không sống quá đời ông**, còn thiết chế Tần thì tồn tại"

Đánh giá này vốn là lập luận của *Hàn Phi Tử* (chê Thân Bất Hại chỉ có "thuật" mà không có "pháp") và của Tư Mã Thiên, tức của những người viết **sau khi Tần đã thắng** và đang giải thích ngược kết cục. Nước Hàn bị Tần diệt năm 230 TCN, hơn một thế kỷ sau khi Thân Bất Hại mất (k. 337 TCN), nên "không sống quá đời ông" là một mệnh đề mạnh mà tư liệu về nước Hàn quá mỏng để chống đỡ. Đây là điểm cần hedge hoặc quy thuộc.
- Câu thay thế đề xuất: "... cải cách của Thân Bất Hại, theo cách đánh giá đã có từ *Hàn Phi Tử*, không để lại thiết chế bền như của Thương Ưởng, còn bộ khung Tần thì tồn tại và trực tiếp tạo ra năng lực thống nhất năm 221 TCN."

### Nghi vấn — `Ảnh hưởng tới: CH03-BCE03-02 · kế thừa · trực tiếp` (Tần Thủy Hoàng)

Đích trỏ đúng người. Nhưng Thương Ưởng chết năm 338 TCN, Tần Thủy Hoàng sinh năm 259 TCN — cách nhau **79 năm**; không thể có bằng chứng tiếp xúc nào. Quan hệ ở đây là kế thừa **thiết chế**, đúng loại mà từ vựng dự án gọi là `qua trường phái`. So sánh với chính dòng ngay trên (`CH03-BCE03-06` Hàn Phi, `qua trường phái`) và dòng dưới (`CH03-BCE03-10` Lý Tư, `qua trường phái`) thì mức `trực tiếp` ở dòng giữa là không nhất quán.
- Đề xuất: đổi thành `qua trường phái`.

### Ghi nhận — phần không có lỗi

- Q351345 = Shang Yang, P569 −390 / P570 −338, khớp `k. 390–338 TCN` ở mức Trung bình.
- "khởi từ khoảng năm 356 và 350 TCN": đúng hai đợt cải cách theo *Sử ký*; đợt hai năm 350 TCN được xác nhận độc lập.
- "dời đô về Hàm Dương": đúng, năm 350 TCN, thuộc đợt cải cách thứ hai.
- "chia hộ thành tổ liên đới trách nhiệm": đúng (thập ngũ 什伍).
- "bị xe xé xác năm 338 TCN": đúng (車裂), sau khi Tần Hiếu công chết cùng năm.
- Nguồn: **Tư Mã Thiên, *Sử ký*, Thương Quân liệt truyện** — có thật, là nguồn gốc cho hầu hết những gì ta biết về ông. Mục này **không ghi số quyển**, đúng theo khuyến nghị §3 của `CONTRIBUTING.md`; không có số nào để kiểm sai.
- Nguồn: **Yuri Pines, *The Book of Lord Shang*, Columbia University Press, 2017** — đúng tác giả, đúng năm, đúng chủ đề.
- `Kế thừa từ`: "Lý Khôi và Ngô Khởi" — cả hai đều là tiền bối thật (Lý Khôi k. 455–395 TCN ở Nguỵ; Ngô Khởi k. 440–381 TCN ở Nguỵ rồi Sở), đúng chiều niên đại.
- Thân Bất Hại (mất k. 337 TCN, làm tướng quốc nước Hàn k. 354–337) **thật sự cùng thời** với Thương Ưởng (k. 390–338). Đạt thể thức §5 — đây là mục làm đúng phần "ứng viên cùng thời" rõ nhất trong nhóm.

---
## CH03-BCE04-07 · Kauṭilya [Tranh cãi lịch sử]

### Sai — quy sai niên đại cho Trautmann (1971), và con số thế kỷ lệch

> "Nhãn [Tranh cãi lịch sử] vì nghiên cứu văn bản học, **nhất là Trautmann (1971)**, cho thấy Arthaśāstra là hợp soạn nhiều tầng, **phần định hình sau cùng có thể tới thế kỷ 2 CN**."

Hai vấn đề.

1. **Sai quy thuộc.** Trautmann (1971) là một **khảo sát thống kê về quyền tác giả**: ông đối chiếu tần suất các tiểu từ Sanskrit giữa các quyển và kết luận Quyển II, III, VII do những người khác nhau viết — tức văn bản là hợp soạn. Việc **định niên đại từng tầng** là công của Olivelle (2013), không phải của Trautmann.
2. **Sai con số thế kỷ.** Olivelle (2013) chia ba tầng và đặt **"Kauṭilya recension" vào 50–125 CN**, còn **"Śāstric recension" — tức bản định hình sau cùng, chính là bản còn trong các thủ bản ta có — vào 175–300 CN**. Nói "có thể tới thế kỷ 2 CN" là cắt mất đoạn cuối: mốc đúng là **tới khoảng năm 300 CN, tức thế kỷ 3**.

- Nguồn: Thomas R. Trautmann, *Kauṭilya and the Arthaśāstra: A Statistical Investigation into the Authorship and Evolution of the Text*, Brill, Leiden, 1971 (lời tựa A. L. Basham); Patrick Olivelle, *King, Governance, and Law in Ancient India: Kauṭilya's Arthaśāstra*, Oxford University Press, 2013.
- Câu thay thế đề xuất: "Nhãn [Tranh cãi lịch sử] vì nghiên cứu văn bản học cho thấy Arthaśāstra là hợp soạn nhiều tầng: Trautmann (1971) dùng phân tích thống kê văn phong để chứng minh nhiều tác giả, còn Olivelle (2013) đặt bản định hình sau cùng vào khoảng 175–300 CN."

### Sai (nội bộ) — mục này và Ghi chú biên tập của cùng file nói ngược nhau

Mục `CH03-BCE04-07` quy niên đại "thế kỷ 2 CN" cho **Trautmann**. Phần "Điểm cần kiểm chứng thêm" ở cuối `content/ch03.md` lại viết:

> "Trautmann (1971) dùng phân tích thống kê văn phong để kết luận Arthaśāstra là hợp soạn nhiều tầng; **Olivelle (2013) đặt phần định hình sau cùng vào khoảng thế kỷ 2 CN**."

Ghi chú biên tập quy đúng người (Olivelle) nhưng **vẫn sai con số** (phải là 175–300 CN). Hai chỗ trong cùng một file đang nói khác nhau về cùng một điều; phải sửa cả hai cho khớp.

### Thể thức — "chính Chandragupta Maurya" không phải ứng viên bị loại

> "Ứng viên thay thế là **chính Chandragupta Maurya**, người mà truyền thống coi ông là cố vấn, và Megasthenes"

Chandragupta Maurya là `CH03-BCE04-08`, **mục liền sau trong chính nhóm này**. Nêu một người đã được chọn làm "ứng viên thay thế" cho chỗ của người khác là vô nghĩa — không có đánh đổi nào xảy ra. Đây là lần thứ hai lỗi này lặp lại trong nhóm (lần đầu: Plato trong mục Aristotle), nên nó là **lỗi hệ thống của nhóm BCE04**, không phải sơ suất lẻ.
- Đề xuất: giữ Megasthenes (k. 350–290 TCN, sứ thần tại Pataliputra k. 302 TCN — thật sự cùng thời, và **có tên trong danh sách bị loại** ở Ghi chú biên tập), và thay Chandragupta bằng một ứng viên thật sự bị loại.

### Nghi vấn — lý do chọn tự mâu thuẫn với nhãn [Tranh cãi lịch sử]

> "Kauṭilya được chọn theo **tính nguyên bản (c) của văn bản**. Nhãn [Tranh cãi lịch sử] vì ... Arthaśāstra là hợp soạn nhiều tầng, phần định hình sau cùng có thể tới thế kỷ 2 CN."

Hai câu liền nhau triệt tiêu nhau: nếu văn bản là hợp soạn nhiều tầng mà tầng cuối cách niên đại truyền thống của Kauṭilya tới bốn, năm thế kỷ, thì "tính nguyên bản của văn bản" không quy về **cá nhân** Kauṭilya được. Ghi chú biên tập cuối file nhận ra điều này ("mục này ghi nhận một **tên gắn với một văn bản**, không phải một tiểu sử") nhưng chính mục thì không.
- Câu thay thế đề xuất: "Kauṭilya được chọn theo tính nguyên bản (c) **của bản thân chuyên luận** — không có văn bản Nam Á nào trước nó bàn trị quốc như một bài toán kỹ thuật — chứ không theo thành tựu của một cá nhân xác định được; xem nhãn [Tranh cãi lịch sử] bên dưới."

### Ghi nhận — phần không có lỗi

- Q9045 = Chanakya, P569 −375 / P570 −283, khớp `k. 375–283 TCN`; độ tin cậy **Thấp** là lựa chọn đúng cho một nhân vật kiểu này.
- "thất truyền rồi được R. Shamasastry tìm lại năm **1905**": **đúng**. Thủ bản được tìm thấy ở Tanjore và được Shamasastry, thủ thư Mysore Government Oriental Library, nhận diện năm 1905.
- "thuyết maṇḍala xếp các nước theo vòng đồng tâm, lấy nước kề làm địch và nước kề nước địch làm bạn": đúng.
- "tách khỏi khung đạo đức dharma": đúng, và là luận điểm trung tâm của Olivelle (2013).
- Cả hai nguồn **tồn tại, đúng tên, đúng năm, đúng nhà xuất bản**, và cả hai **thật sự bàn chính điều được dẫn**. Không ghi số quyển/chương — đúng khuyến nghị §3.
- `Ảnh hưởng tới` CH03-BCE04-08 = Chandragupta: đích đúng người.

---
## CH03-BCE04-08 · Chandragupta Maurya

### Trung lập / Thiếu — "bước không có tiền lệ" là mệnh đề tối cao không quy thuộc

> "Chandragupta được chọn theo counterfactual (d): việc hợp nhất tiểu lục địa dưới một chính quyền là **bước không có tiền lệ**, còn Bindusara chỉ kế tục."

"Không có tiền lệ" là đúng loại mệnh đề mà prompt dự án cấm viết trần (§Ngôn ngữ: "trung lập, không tô vẽ"). Nó cũng không chính xác: đế chế Nanda mà ông lật đổ **đã** là nhà nước lớn nhất Nam Á thời đó, trải từ Magadha ra phần lớn đồng bằng sông Hằng. Cái thật sự mới ở Chandragupta là **phạm vi** — nối đồng bằng sông Hằng với vùng tây bắc sau khi quyền lực Macedonia rút đi — chứ không phải bản thân ý tưởng về một nhà nước liên vùng.
- Câu thay thế đề xuất: "... việc nối vùng tây bắc với đồng bằng sông Hằng dưới một chính quyền là bước mà đế chế Nanda trước đó chưa làm được, còn Bindusara thì kế tục một bản đồ đã thành hình."

### Thiếu — "Bindusara ... giữ và mở rộng đế chế về phía nam" dựa trên tư liệu rất muộn

> "Ứng viên kế cận là Bindusara, con ông, **người giữ và mở rộng đế chế về phía nam**"

Việc Bindusara chinh phục Deccan **không có tư liệu đương thời nào xác nhận**. Nguồn chính là Tāranātha, tác giả Phật giáo Tây Tạng **thế kỷ 16**, và một số sử gia nghi ngờ tính xác thực của ghi chép này; đáng chú ý là các bi ký của chính Ashoka tìm thấy ở nam Ấn **không nhắc gì** tới cuộc chinh phục Deccan của cha ông. Viết thẳng như dữ kiện là thiếu hedge, nhất là khi nó đang được dùng để đo tiêu chí (d) của người khác.
- Câu thay thế đề xuất: "Ứng viên kế cận là Bindusara, con ông, người mà truyền thống muộn gán cho việc mở rộng xuống Deccan — dù bi ký Ashoka không xác nhận điều đó — và Dhana Nanda, vua bị ông lật đổ."

### Nghi vấn — "nền cho các chỉ dụ của Ashoka" nối sai hai thứ

> "Bộ máy thu thuế và đo đạc ruộng đất ông lập là **nền cho các chỉ dụ của Ashoka** sau đó."

Các **chỉ dụ** (edicts) của Ashoka là văn bản về dhamma, đạo đức cai trị, bất bạo lực và tổ chức tăng đoàn; chúng **không** bàn thuế khoá hay đo đạc ruộng đất. Cái mà bộ máy thu thuế làm nền cho là **đế chế** và **bộ máy hành chính** Ashoka thừa hưởng, không phải nội dung các chỉ dụ.
- Câu thay thế đề xuất: "Bộ máy thu thuế và đo đạc ruộng đất ông lập là nền hành chính mà Ashoka thừa hưởng, và là điều kiện vật chất cho việc khắc và phân phát các chỉ dụ khắp đế chế."

### Nghi vấn — `Kế thừa từ: CH03-BCE04-03 · kế thừa · trực tiếp` (Alexander)

Xem chi tiết ở mục `CH03-BCE04-03`. Tóm lại: bằng chứng duy nhất cho một quan hệ **trực tiếp** là một câu trong Plutarch (*Alexander* 62) về "Androcottus" gặp Alexander thời trẻ, và việc đồng nhất Androcottus với Chandragupta vốn đã là suy luận học giả. Mức `trực tiếp` vượt quá bằng chứng; đề xuất `suy đoán học giả`.

### Thể thức (nhẹ) — cả hai "ứng viên" đều không phải ứng viên cạnh tranh

Bindusara là **con** và người kế vị (trị vì bắt đầu sau khi Chandragupta thoái vị), Dhana Nanda là **vua bị lật đổ**. Không ai trong hai người là một lựa chọn thay thế thật sự cho chỗ trong nhóm: người đầu thuộc thế kỷ sau về mặt hoạt động, người sau không có di sản để cân. Mục này về hình thức có nêu đích danh hai cái tên nên không vi phạm chữ của §5, nhưng nó không thực hiện được chức năng của §5 là **cho thấy một đánh đổi đã được cân nhắc**.
- Ứng viên hợp lệ hơn: **Megasthenes** (k. 350–290 TCN) hoặc **Seleucus I Nicator** (k. 358–281 TCN) — cả hai cùng thời thật, cùng lĩnh vực Chính trị/Nhà nước, và cả hai đều **đã có tên trong danh sách bị loại** ở Ghi chú biên tập cuối file.

### Ghi nhận — phần không có lỗi

- Q188541 = Chandragupta Maurya, P569 −340 / P570 −297, khớp `k. 340–297 TCN` ở mức Trung bình. (Xem §0: mô tả tiếng Anh của Wikidata ghi 350–295, tự mâu thuẫn với P569/P570 của chính nó — file chọn theo claim là đúng.)
- "lật đổ triều Nanda ở Magadha khoảng năm 322 TCN": khớp niên đại quy ước (322/321 TCN).
- "Hoà ước với Seleucus I khoảng năm 303 TCN đổi **năm trăm voi chiến** lấy các tỉnh phía tây và mở quan hệ sứ thần": đúng cả ba vế; con số 500 voi là con số truyền thống trong nguồn Hy Lạp, và hoà ước được định khoảng 305–303 TCN.
- "nguồn ngoài đương thời hiếm hoi": đúng và hedge tốt.
- Nguồn: **Romila Thapar, *The Mauryas Revisited*, K.P. Bagchi & Co. cho Centre for Studies in Social Sciences, Calcutta, 1987** (loạt bài giảng Sakharam Ganesh Deuskar, đọc tháng 12-1985) — tồn tại, đúng tác giả, **đúng năm**, đúng chủ đề.
- Nguồn: **Megasthenes, *Indica* (qua trích dẫn của Arrian và Strabo)** — cách ghi này **đúng và trung thực**: *Indica* không còn nguyên, chỉ còn qua trích dẫn, và mục đã nói rõ điều đó thay vì dẫn như một văn bản còn đủ. Đây là dòng Nguồn làm đúng nhất trong nhóm.
- `Ảnh hưởng tới` CH03-BCE03-01 = Ashoka: đúng người, đúng chiều (ông nội → cháu).
- `Kế thừa từ` CH03-BCE04-07 = Kauṭilya: đích đúng người.

---
## CH03-BCE04-09 · Eudoxus xứ Cnidus

### Sai — `Kế thừa từ: CH03-BCE04-01 · tương đồng độc lập · suy đoán học giả` dùng sai loại quan hệ

> **Kế thừa từ:**
> "- CH03-BCE04-01 · tương đồng độc lập · suy đoán học giả"

Prompt dự án định nghĩa rõ: *"Loại quan hệ 'tương đồng độc lập' là hợp lệ và **nên dùng khi không có bằng chứng tiếp xúc**"* (§Kiểm soát chất lượng). Nhưng giữa Eudoxus và Plato **có bằng chứng tiếp xúc trực tiếp**, và nó thuộc loại được ghi chép sớm nhất mà ta có cho cả hai người:

- Eudoxus tới Athens và dự giảng của Plato — Diogenes Laërtius 8.86–8.90 kể ông từ Piraeus lên Athens hằng ngày để nghe giảng, rồi về sau quay lại Athens cùng một nhóm môn đồ;
- vẫn theo Diogenes Laërtius, ông **tạm nắm Academy trong thời gian Plato ở Syracuse**.

Tư liệu này là giai thoại và có nhắc tới va chạm giữa hai người, nhưng "giai thoại về một quan hệ có thật" khác hẳn "không có bằng chứng tiếp xúc". Dùng `tương đồng độc lập` ở đây là **nói ngược lại tình trạng tư liệu**, và đồng thời xoá mất một trong những liên kết thể chế quan trọng nhất của nhóm BCE04 (Academy là chỗ Eudoxus, Plato, Aristotle và Theaetetus gặp nhau).

- Nguồn: Diogenes Laërtius, *Lives* 8.86–8.90; Britannica, "Eudoxus of Cnidus" (https://www.britannica.com/biography/Eudoxus-of-Cnidus); Encyclopedia.com, "Eudoxus of Cnidus" (bản DSB).
- Dòng thay thế đề xuất: `- CH03-BCE04-01 · tương đồng · trực tiếp` — hoặc, nếu muốn giữ đúng tinh thần "không suy diễn kế thừa tư tưởng", thì `- CH03-BCE04-01 · tương đồng · suy đoán học giả`, nhưng **không** được dùng `tương đồng độc lập`. (Lưu ý: `tương đồng` không nằm trong `RELATION_TYPES`; nếu từ vựng chỉ có bốn giá trị thì giá trị đúng ở đây là `kế thừa · trực tiếp` với hàm ý tiếp xúc, không phải kế thừa học thuyết.)

### Thiếu — "nỗ lực hình học hoá chuyển động hành tinh sớm nhất" thiếu hedge

> "Mô hình thiên văn các mặt cầu đồng tâm của ông là **nỗ lực hình học hoá chuyển động hành tinh sớm nhất**."

Đây là mệnh đề tối cao ("sớm nhất") về một lĩnh vực mà tư liệu Hy Lạp trước Eudoxus gần như chỉ còn qua trích dẫn, và mà các truyền thống Babylon đã có mô hình **số học** (không phải hình học) cho chuyển động hành tinh từ trước. Mệnh đề có thể đúng trong giới hạn "còn lại" và "hình học", nhưng mục không nói giới hạn ấy ra.
- Câu thay thế đề xuất: "... là nỗ lực **còn lại** sớm nhất nhằm giải thích chuyển động hành tinh bằng một mô hình hình học, khác với các mô hình số học của thiên văn Babylon."

### Ghi nhận — phần không có lỗi

- Q185150 = Eudoxus of Cnidus, P569 −408 (preferred) / P570 −355, khớp chính xác `k. 408–355 TCN` ở mức Trung bình. (P569 còn một giá trị −390 ở rank normal; file dùng giá trị preferred — đúng.)
- "lý thuyết tỉ lệ ... thành Quyển V của Euclid gần như nguyên vẹn": đúng, là quy thuộc chuẩn trong lịch sử toán học.
- "phương pháp vét cạn ... là tiền thân trực tiếp của phép tích phân và là công cụ Archimedes dùng": đúng.
- "vấn đề mà việc phát hiện tính vô ước của đường chéo hình vuông đã để lại cho truyền thống Pythagoras": đúng, và nhất quán với mục Pythagoras ở `content/ch02.md` (`CH02-BCE06-06`), vốn cũng nêu đúng chi tiết này.
- Nguồn: **Thomas Heath, *A History of Greek Mathematics*, Oxford, 1921, quyển I** — sách có thật, đúng năm, và **số quyển đúng**: bộ gồm 2 quyển, quyển I là *From Thales to Euclid*, nên Eudoxus (k. 408–355 TCN) nằm đúng trong quyển I. Kiểm được, không phải số bịa.
- Nguồn: **Euclid, *Cơ sở*, Quyển V** — đúng: Quyển V là quyển về lý thuyết tỉ lệ, chính là phần được quy cho Eudoxus.
- "Vì sao chọn" nêu **Theaetetus** (k. 417–369 TCN) và **Archytas xứ Tarentum** (k. 435–360 TCN). Cả hai **thật sự cùng thời** với Eudoxus (k. 408–355), cùng lĩnh vực Toán học, và đều là ứng viên cạnh tranh thật chứ không phải cộng sự hay người kế tục. **Đây là mục làm đúng thể thức §5 tốt nhất trong nhóm BCE04.**
- "Theaetetus, người phân loại các đại lượng vô ước và góp phần vào Quyển X của Euclid": đúng cả nội dung lẫn số quyển.
- `Ảnh hưởng tới`: CH03-BCE03-03 = Euclid, CH03-BCE03-05 = Archimedes, CH03-BCE02-03 = Hipparchus. Cả ba đích đúng người, đúng chiều niên đại, và mức bằng chứng (`trực tiếp`, `trực tiếp`, `qua trường phái`) đều hợp lý.

---
## CH03-BCE04-10 · Diogenes xứ Sinope

### Sai — URL nguồn **không tồn tại** (HTTP 404)

> **Nguồn:** "... Stanford Encyclopedia of Philosophy, "Ancient Cynicism" (**https://plato.stanford.edu/entries/cynicism/**)."

Đã mở trực tiếp: **HTTP 404 Not Found**. Đã kiểm thêm bằng công cụ tìm kiếm nội bộ của SEP (`plato.stanford.edu/search/searcher.py?query=Cynicism`, 25 kết quả): **SEP không có entry riêng nào về Cynicism, Cynics, hay Diogenes of Sinope**. Những entry thật sự bàn tới Diogenes chỉ là các entry rộng hơn: "Ancient Ethical Theory", "Ancient Political Philosophy", "Cosmopolitanism", "Ancient Skepticism".

Đây đúng loại lỗi mà `CONTRIBUTING.md` §2 cảnh báo ("Nhiều slug Stanford Encyclopedia không có thật"). Cả **tên entry** ("Ancient Cynicism") lẫn **slug** (`cynicism`) đều là bịa.

- Nguồn thay thế đề xuất, và là nguồn **thật sự nói điều mục này đang dẫn**: Stanford Encyclopedia of Philosophy, "Cosmopolitanism" (https://plato.stanford.edu/entries/cosmopolitanism/) — entry này nêu đích danh Diogenes là triết gia phương Tây đầu tiên phát biểu tường minh lập trường cosmopolitan, với câu "tôi là công dân thế giới". Đây chính là mệnh đề trung tâm của mục.
- Dòng Nguồn thay thế đề xuất: "Diogenes Laërtius, *Cuộc đời các triết gia danh tiếng*, q. VI; Stanford Encyclopedia of Philosophy, "Cosmopolitanism" (https://plato.stanford.edu/entries/cosmopolitanism/)."

### Thể thức — Crates là học trò, không phải ứng viên cạnh tranh

> "Ứng viên cùng phái là Antisthenes, người thường được coi là khởi đầu của Khuyển nho, và **Crates xứ Thebes, học trò ông và là thầy của Zeno xứ Citium**."

Mục tự khai rằng Crates là **học trò của chính Diogenes**, rồi vài dòng sau lại dùng chuỗi Diogenes → Crates → Zeno làm **lý do chọn Diogenes**. Một người vừa là học trò vừa là mắt xích trong lập luận ủng hộ thầy thì không thể đồng thời là "ứng viên cạnh tranh đã bị loại" — đây đúng là dạng "cộng sự chứ không phải ứng viên cạnh tranh". Antisthenes là ứng viên hợp lệ; Crates thì không.
- Ứng viên hợp lệ hơn, cùng thời thật, cùng lĩnh vực Triết học: **Aristippus xứ Cyrene** (k. 435–356 TCN, lập phái Cyrenaic — lập trường đối cực với Khuyển nho về khoái lạc, nên là một đánh đổi thật), hoặc **Xenocrates** nếu muốn giữ mạch Academy.

### Thiếu — hai mệnh đề tối cao chưa quy thuộc

> "ông trả lời mình là công dân thế giới — **ghi nhận sớm nhất còn lại** của khái niệm kosmopolitēs"

Mệnh đề này **đúng** và có thể quy thuộc được — SEP "Cosmopolitanism" nói chính điều đó. Nhưng nó đang được viết trần, trong khi toàn bộ tiểu sử Diogenes là giai thoại do người đời sau chép (chính mục cũng thừa nhận: "những gì còn là giai thoại và cách ngôn do người đời sau ... tập hợp"). Việc một câu thoại chỉ có ở Diogenes Laërtius (TK 3 CN) được dùng làm "ghi nhận sớm nhất" cần nói rõ nó là ghi nhận **được truyền lại**, không phải ghi nhận đương thời.
- Câu thay thế đề xuất: "... ông trả lời mình là công dân thế giới — câu thoại được Diogenes Laërtius chép lại, và thường được coi là phát biểu tường minh sớm nhất còn lại của khái niệm kosmopolitēs ..."

### Ghi nhận — phần không có lỗi

- Q59180 = Diogenes of Sinope, nhãn đúng người. Độ tin cậy **Thấp** nên không đối chiếu niên đại — lựa chọn đúng, và được mục giải thích thẳng ("Độ tin cậy Thấp vì tiểu sử gần như toàn giai thoại"). (Xem §0: P569 của Wikidata có ba giá trị cạnh tranh và giá trị preferred là −400, không phải −412 như file ghi; không phải lỗi, chỉ là điều nên biết.)
- "Ông không để lại trước tác chắc chắn; những gì còn là giai thoại và cách ngôn do người đời sau, chủ yếu Diogenes Laërtius, tập hợp": **đúng, và là một trong những câu hedge tốt nhất của cả nhóm**.
- Nguồn **Diogenes Laërtius, *Cuộc đời các triết gia danh tiếng*, q. VI** — **số quyển đúng**: Quyển VI của *Lives* là quyển dành cho phái Khuyển nho và chứa tiểu sử Diogenes (6.20–81), gồm cả giai thoại "công dân thế giới" (6.63). Kiểm được.
- Antisthenes (k. 446–366 TCN) **thật sự cùng thời** với Diogenes (k. 412–323). Việc mục ghi "**thường được coi là** khởi đầu của Khuyển nho" là hedge đúng chỗ — quan hệ thầy trò Antisthenes–Diogenes bị chính giới nghiên cứu nghi ngờ về mặt niên đại.
- `Kế thừa từ`: "Antisthenes" (tên, không ID — hợp lệ) và CH02-BCE05-01 = Socrates, `qua trường phái` — đúng người, đúng chiều, đúng mức bằng chứng.
- `Ảnh hưởng tới` CH03-BCE03-07 = Zeno xứ Citium: đúng người, đúng chiều (Zeno k. 334–262 TCN, học Crates sau khi tới Athens k. 312 TCN).

---
## CH03-BCE04-11 · Praxiteles

### Trung lập — "không có tiền lệ" là mệnh đề tối cao, dù có một nửa quy thuộc

> "Praxiteles được chọn theo tính nguyên bản (c): bước mở rộng đề tài ở tượng Cnidus **không có tiền lệ** và được chính nguồn cổ ghi nhận là gây chấn động."

Vế sau (**"được chính nguồn cổ ghi nhận là gây chấn động"**) là **đúng và quy thuộc được**: Pliny, *NH* 36.20–21 kể rằng người ta vượt biển tới Cnidus chỉ để xem tượng, rằng đền được xây mở bốn phía để nhìn được từ mọi hướng, và rằng vua Nicomedes đề nghị xoá toàn bộ nợ công của Cnidus để mua lại mà bị từ chối. Vế này giữ nguyên.

Vế trước (**"không có tiền lệ"**) thì không. Đây là mệnh đề tối cao không quy thuộc, và nó mạnh hơn mức tư liệu cho phép: cái đúng là *không có tượng tròn khoả thân nữ quy mô lớn nào **được ghi nhận** trước đó trong nghệ thuật Hy Lạp* — tức một mệnh đề về **tình trạng tư liệu**, không phải về thực tế lịch sử. Chính mục ở đoạn trên đã viết đúng cách rồi ("**được ghi nhận** trong nghệ thuật Hy Lạp"), nên vế này chỉ là chỗ trượt tay ở phần "Vì sao chọn".
- Câu thay thế đề xuất: "Praxiteles được chọn theo tính nguyên bản (c): không có tượng tròn khoả thân nữ quy mô lớn nào được ghi nhận trước tượng Cnidus, và chính nguồn cổ ghi lại rằng tác phẩm gây chấn động — Pliny kể người ta vượt biển tới Cnidus chỉ để xem nó."

### Nghi vấn (nhẹ) — "thay cho thế đứng cân bằng của thế kỷ 5 TCN" hơi lệch với dòng `Kế thừa từ`

> "Ông cũng đẩy mạnh dáng đứng cong chữ S, cho thân người tựa trọng tâm lệch hẳn sang một bên, **thay cho thế đứng cân bằng của thế kỷ 5 TCN**."

Dòng `Kế thừa từ` ngay bên dưới ghi "Polykleitos và truyền thống contrapposto · kế thừa · qua trường phái" — tức nhận rằng tư thế lệch trọng tâm **đã là** di sản thế kỷ 5. Hai câu không mâu thuẫn hẳn (contrapposto Polykleitos là cân bằng, đường cong Praxiteles đẩy nó đi xa hơn), nhưng chữ "thay cho" dễ làm người đọc hiểu là Praxiteles bỏ contrapposto trong khi ông **phóng đại** nó.
- Câu thay thế đề xuất: "... đẩy dáng đứng lệch trọng tâm của thế kỷ 5 TCN đi xa hơn thành đường cong chữ S, cho thân người đổ hẳn sang một bên."

### Ghi nhận — phần không có lỗi

- Q105290 = Praxiteles ("Attic sculptor"), P569 −395 / P570 −330, khớp `k. 395–330 TCN`. Độ tin cậy **Thấp** và mục giải thích thẳng vì sao ("niên đại chỉ suy từ niên biểu tác phẩm, và mọi hiện vật đều là bản sao") — đúng cách.
- "tượng tròn khoả thân nữ quy mô lớn đầu tiên **được ghi nhận**": hedge đúng, giữ nguyên.
- "**Không tác phẩm gốc nào chắc chắn còn lại**": hedge chính xác. Chữ "chắc chắn" là cần thiết vì tượng Hermes ở Olympia vẫn được một số học giả coi là bản gốc — mục đã xử lý đúng chỗ tranh luận này mà không phải viết dài.
- Nguồn: **Pliny Cả, *Naturalis Historia*, q. XXXVI** — **số quyển đúng và kiểm được**: Quyển XXXVI là quyển về đá và điêu khắc đá cẩm thạch, và đoạn về Aphrodite xứ Cnidus nằm ở 36.20–21. Không phải số bịa.
- Nguồn: **Nigel Spivey, *Greek Sculpture*, Cambridge University Press, 2013** — tồn tại, **đúng năm** (25-03-2013), đúng nhà xuất bản, ISBN 978-0-521-75698-3 / 978-0-521-76031-7, bao quát từ k. 700 TCN tới hết thời cổ đại, nên có bàn Praxiteles.
- "Vì sao chọn" nêu **Lysippos** (k. 390–300 TCN) và **Scopas** (k. 395–350 TCN). Cả hai **thật sự cùng thời** với Praxiteles (k. 395–330), cùng lĩnh vực, và là ứng viên cạnh tranh thật. Lysippos còn **có tên trong danh sách bị loại** ở Ghi chú biên tập cuối file. Đạt thể thức §5 (cùng với mục Eudoxus, là hai mục làm tốt nhất phần này).
- "Lysippos, điêu khắc gia của triều Alexander và người đổi tỉ lệ thân người sang dáng thon": đúng.
- Không có liên kết ID nào trong `Kế thừa từ` / `Ảnh hưởng tới` — cả hai dùng tên trào lưu, nên không có đích sai.

---
## Đánh giá lựa chọn nhân vật (nhóm BCE04)

### Độ phủ hiện tại

**Vùng** — 3/9, đạt mức tối thiểu §5 nhưng không hơn:

| Vùng | Số người |
|---|---|
| Châu Âu | 6 (Plato, Aristotle, Alexander, Eudoxus, Diogenes, Praxiteles) |
| Đông Á | 3 (Mạnh Tử, Trang Tử, Thương Ưởng) |
| Nam Á | 2 (Kauṭilya, Chandragupta) |
| Trung Đông/Bắc Phi, Trung Á, Đông Nam Á, Châu Phi hạ Sahara, Châu Mỹ, Châu Đại Dương | **0** |

**Lĩnh vực** — 8/16, vượt mức tối thiểu §5 (≥4). Vắng mặt: **Văn học, Y học, Sử học, Khám phá/Địa lý, Giáo dục, Ngôn ngữ học, Tôn giáo/Tâm linh, Kỹ thuật/Công nghệ**.

**Sĩ số**: **11/12**. Nhóm **còn một chỗ trống**. Đây là dữ kiện quan trọng cho mọi nhận xét bên dưới.

**Giới**: 11/11 là nam. Không có nhân vật nữ nào được chọn, và cũng **không có tên nữ nào trong danh sách ứng viên bị loại** của Ghi chú biên tập.

### Lỗi trong chính Ghi chú biên tập: lý do loại không đứng được với BCE04

> "Demosthenes, Isocrates, Lysippos, Apelles, Ctesibius, Seleucus I, Berossus, Manetho, **Pytheas**, **Megasthenes**, ...: đều xứng đáng xét tới, nhưng **các nhóm tương ứng đã đủ 11–12 người** và họ xếp sau ở ít nhất một trong bốn tiêu chí. Trần nhóm là 12."

Trong danh sách này, những người thuộc **TK 4 TCN** — Demosthenes (384–322), Isocrates (436–338), Lysippos (k. 390–300), Pytheas (k. 350–285), Megasthenes (k. 350–290) — đều lẽ ra rơi vào nhóm BCE04. Nhưng **BCE04 chỉ có 11 người, chưa đủ 12**. Lý do "nhóm tương ứng đã đủ" là **sai sự thật đối với đúng nhóm này**, và nó đang che một chỗ trống có thật.
- Đề xuất: hoặc điền chỗ thứ 12, hoặc sửa lý do thành một lý do đứng được (ví dụ: "để trống chỗ thứ 12 thay vì lấp bằng một tên yếu" — đúng tinh thần quy tắc 2 của §5, vốn nói thẳng "KHÔNG cố cho đủ 12").

### Ứng viên đáng ra phải được cân nhắc mà **chưa từng được nhắc tới ở đâu** (kể cả trong danh sách bị loại)

**1. Khuất Nguyên (屈原 Qū Yuán, k. 343–278 TCN) — thiếu sót mạnh nhất.** Lĩnh vực Văn học, vùng Đông Á.
- (a) Phạm vi: *Sở từ* (*Chu ci*), với *Ly Tao* làm trung tâm, là **một trong hai cội nguồn của toàn bộ thi ca Trung Hoa**, bên cạnh *Kinh Thi*. Ông là **người Trung Hoa đầu tiên nổi danh với tư cách tác giả thơ, và là nhà thơ sớm nhất được biết bằng tên** trong truyền thống ấy.
- (b) Độ bền: Tết Đoan Ngọ tưởng niệm ông vẫn được giữ tới nay ở Trung Quốc, Việt Nam, Triều Tiên và cộng đồng Hoa kiều — một trong số rất ít nhân vật TK 4 TCN còn có ngày lễ mang tên mình.
- (c)/(d): bước chuyển từ thơ khuyết danh sang **thơ có tác giả xưng "tôi"** trong truyền thống Trung Hoa gắn với ông.
- Lý do đây là thiếu sót đặc biệt nặng: **lĩnh vực Văn học hoàn toàn vắng mặt trong nhóm BCE04**, và Khuất Nguyên là ứng viên Văn học mạnh nhất của thế kỷ 4 TCN trên toàn cầu.
- Hai điểm cần xử lý nếu thêm: (i) niên đại k. 343–278 TCN **vắt qua ranh 301/300**, nên cần một dòng ở mục "Nhân vật có thể thuộc thế kỷ khác" — nhưng giai đoạn ông làm quan cho Sở Hoài vương nằm trong TK 4 TCN, và **nhóm BCE03 đã đủ 12 người** trong khi BCE04 còn chỗ; (ii) sự tồn tại lịch sử và quyền tác giả của ông **đều bị tranh luận**, nên cần nhãn **[Tranh cãi lịch sử]** — đúng theo quy tắc 8 của §5, vốn nói rõ nhân vật còn tranh cãi về sự tồn tại "vẫn được chọn nếu ảnh hưởng lớn".

**2. Huệ Thi (惠施, k. 370–310 TCN).** Lĩnh vực Triết học, vùng Đông Á.
- Ông là **người đối thoại thường xuyên nhất của Trang Tử trong chính văn bản *Trang Tử*** và là đại diện chính của Danh gia (名家) — truyền thống Trung Hoa về nghịch lý, tên gọi và lập luận.
- Lý do đáng chú ý: mục Aristotle (`CH03-BCE04-02`) viết rằng "luận lý hình thức là bộ môn ông dựng từ không có gì". Một mục về Danh gia ở cùng nhóm, cùng thế kỷ, sẽ đặt mệnh đề ấy vào đúng khung so sánh toàn cầu mà §5 (chống thiên lệch châu Âu) yêu cầu — thay vì để nó đứng một mình.
- Ông cũng là ứng viên "cùng thời" hợp lệ mà **cả hai** mục Mạnh Tử và Trang Tử đang thiếu (xem hai mục đó).

**3. Diocles xứ Carystus (k. 375–295 TCN).** Lĩnh vực Y học, vùng Châu Âu.
- **Y học hoàn toàn vắng mặt** trong BCE04; Hippocrates nằm ở nhóm trước (`CH02-BCE05-04`), nên thế kỷ 4 TCN hiện là một khoảng trống y học hoàn toàn trong atlas.
- Thời cổ đại gọi ông là "Hippocrates thứ hai"; ông được coi là người viết sách giải phẫu có hệ thống đầu tiên bằng tiếng Hy Lạp.
- Thừa nhận: trước tác chỉ còn qua trích dẫn, nên (b) yếu. Có thể bị loại — nhưng **phải được nêu ra rồi loại**, chứ không phải không tồn tại trong hồ sơ.

**4. Ứng viên nữ — chưa có tên nào được cân nhắc.** Thế kỷ 4 TCN quả thật rất nghèo tư liệu về phụ nữ, nhưng không phải trống rỗng:
- **Axiothea xứ Phlius** và **Lastheneia xứ Mantinea** — hai nữ môn đồ của Academy, được Diogenes Laërtius ghi tên (3.46, 4.2);
- **Artemisia II của Caria** (mất 350 TCN) — người cai trị, và là người cho dựng Lăng Halicarnassus, một trong bảy kỳ quan.
- Nhiều khả năng không ai trong số này thắng được 11 người hiện có theo (a)–(d). Nhưng dự án đã có tiền lệ xử lý đúng cho trường hợp tương tự: ứng viên Việt Nam được **nêu ra, cân nhắc, rồi giải thích vì sao không vào** (xem mục "Ứng viên Việt Nam"). Khoảng trống giới xứng đáng được xử lý cùng cách, thay vì im lặng.

**5. Trung Đông/Bắc Phi — khoảng trống có thể là thật, nhưng chưa được ghi ra.** Ghi chú biên tập của chapter dành hẳn một khối cho quy ước vùng Hellenistic và nói rõ Chapter 3 xếp người Hy Lạp làm việc ở Alexandria vào Trung Đông/Bắc Phi. Nhưng **BCE04 không có ai ở vùng đó** — vì Alexandria mới lập năm 331 TCN và chỉ thành trung tâm học thuật ở thế kỷ sau. Ứng viên có thể xét: **Mausolus xứ Caria** (mất 353 TCN, Chính trị/Nhà nước + Nghệ thuật/Kiến trúc) hoặc **Nectanebo II** (pharaoh bản địa cuối cùng của Ai Cập, mất k. 340 TCN) — cả hai đều yếu theo (b) và (d), nên kết luận "không có ứng viên đủ mạnh" có thể đúng. Vấn đề là kết luận ấy **chưa được viết ra**, trong khi Ghi chú biên tập đã làm đúng việc này cho nhóm BCE01 ("Nhóm BCE01 không có mục nào thuộc vùng Nam Á. Đây là khoảng trống thật ... Ghi ra thay vì lấp bằng một cái tên yếu").

**6. Đông Nam Á / Việt Nam — BCE04 nằm ngoài cửa sổ mà Ghi chú biên tập xét.** Mục "Ứng viên Việt Nam đã được cân nhắc" của chapter mở đầu bằng "Giai đoạn **300 TCN – 1 TCN**..." — tức bắt đầu đúng ở chỗ nhóm BCE04 (400–301 TCN) kết thúc. Nhóm BCE04 vì thế là **nhóm duy nhất của Chapter 3 mà không có ứng viên Việt Nam/Đông Nam Á nào được xét, kể cả để loại**. Kết luận thực chất nhiều khả năng vẫn là "không có" (niên đại truyền thống của An Dương Vương và Âu Lạc là 257 TCN, thuộc BCE03), nhưng cửa sổ 400–301 TCN cần được nói tới rõ ràng thay vì bỏ trống.

### Hai ghi chú nhỏ về tính nhất quán của hồ sơ ứng viên

- **Xenophon** được nêu đích danh làm ứng viên bị loại **bên trong** mục Plato, nhưng **không có tên** trong danh sách "Ứng viên mạnh đã bị loại" ở Ghi chú biên tập (Isocrates và Demosthenes thì có). Tương tự với Theaetetus, Archytas, Antisthenes, Cáo Tử, Dương Chu, Thân Bất Hại, Scopas, Dhana Nanda, Philip II.
- Ngược lại, hai cái tên được dùng làm "ứng viên" trong nhóm — **Plato** (trong mục Aristotle) và **Chandragupta** (trong mục Kauṭilya) — lại **đã được chọn vào chính nhóm này**. Xem hai mục đó; đây là lỗi thể thức §5 lặp lại hai lần.

---

## Tổng hợp phát hiện

| Loại | Số | Phân bố theo mục |
|---|---|---|
| **Sai** | 9 | -02 (luận lý "độc tôn" + mốc Frege) · -03 (`CH02-BCE05-10` trỏ Darius I) · -04 (Nhật Bản) · -04 ("bảy thế kỷ") · -05 ("văn bản còn nguyên vẹn") · -07 (quy sai Trautmann + lệch thế kỷ) · -07 (nói ngược Ghi chú biên tập cùng file) · -09 (`tương đồng độc lập` sai định nghĩa) · -10 (**URL SEP trả 404**) |
| **Nghi vấn** | 15 | -01 (×1) · -02 (×2) · -03 (×2) · -04 (×2) · -05 (×2) · -06 (×2) · -07 (×1) · -08 (×2) · -11 (×1) |
| **Thiếu / Trung lập** | 9 | -01 ("mười lăm thế kỷ") · -03 (kế hoạch Philip) · -05 (Thiền tông) · -06 (Thân Bất Hại) · -08 ("không có tiền lệ") · -08 (Bindusara xuống Deccan) · -09 ("sớm nhất") · -10 (kosmopolitēs) · -11 ("không có tiền lệ") |
| **Thể thức §5** | 4 | -02 (Plato — đã có trong nhóm) · -07 (Chandragupta — đã có trong nhóm) · -08 (con trai + vua bị lật đổ, không phải ứng viên cạnh tranh) · -10 (Crates — học trò của chính đương sự) |

Ngoài ra, một lỗi nằm ở **Ghi chú biên tập** chứ không ở mục nào: lý do loại "các nhóm tương ứng đã đủ 11–12 người" **không đúng với BCE04**, vốn chỉ có 11/12 (xem mục trên).

Ba mục **không có lỗi `Sai` nào**: `-01` Plato, `-06` Thương Ưởng, `-11` Praxiteles. Hai mục làm đúng thể thức §5 tốt nhất (ứng viên cùng thời thật, cạnh tranh thật): `-09` Eudoxus (Theaetetus, Archytas) và `-11` Praxiteles (Lysippos, Scopas).

**Ba việc cần sửa trước tiên**, theo thứ tự nghiêm trọng:

1. **`CH03-BCE04-10` — URL `https://plato.stanford.edu/entries/cynicism/` trả 404 và entry "Ancient Cynicism" không tồn tại ở SEP.** Đây là lỗi duy nhất trong nhóm thuộc loại mà `CONTRIBUTING.md` gọi là "loại báo lỗi hữu ích nhất": nguồn không tồn tại. Thay bằng SEP "Cosmopolitanism", entry **thật sự** nói điều đang được dẫn.
2. **`CH03-BCE04-03` — `Kế thừa từ: CH02-BCE05-10 · phản bác · trực tiếp` trỏ Darius I thay vì Darius III**, và mâu thuẫn trực tiếp với chiều ngược lại đã ghi ở `content/ch02.md` (`kế thừa · qua trường phái`). Lint không bắt được vì nó chỉ kiểm có/không đối ứng, không kiểm **loại quan hệ** và **mức bằng chứng** có khớp nhau giữa hai chiều.
3. **`CH03-BCE04-04` — "khoa cử bắt buộc ở ... Nhật Bản ... suốt bảy thế kỷ"**: Nhật Bản không có khoa cử lấy Tứ thư làm nội dung, và quãng thời gian đúng là 1313–1905 (gần sáu thế kỷ), không phải bảy. Cả hai sai nằm trong đúng câu được dùng làm bằng chứng cho tiêu chí (b).

**Gợi ý cho lint (ngoài phạm vi, ghi lại vì tìm ra từ nhóm này):** hai lỗi số 2 ở trên và các ca `trực tiếp` bất khả về niên đại (Thương Ưởng → Tần Thủy Hoàng, cách 79 năm; Alexander → Chandragupta) đều bắt được bằng máy. Hai kiểm tra đề nghị: (i) khi A và B cùng khai một cặp theo hai chiều, cảnh báo nếu **loại quan hệ** hoặc **mức bằng chứng** không khớp; (ii) cảnh báo `trực tiếp` khi hai đời không chồng nhau năm nào.
