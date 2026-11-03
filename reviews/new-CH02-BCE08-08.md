# Mục mới đề xuất · CH02-BCE08-08 · Baudhāyana

Soạn theo `prompts/atlas-prompt.md`, trả lời phát hiện **N12** của `reports/review-ch02.md`.
**Không chỉnh sửa `content/ch02.md`.** Tài liệu này chỉ đề xuất.

---

## 1 · Mục hoàn chỉnh, sẵn sàng dán vào `content/ch02.md` (nhóm BCE08)

```markdown
### CH02-BCE08-08 · Baudhāyana (बौधायन) [Tranh cãi lịch sử]
`năm: hoạt động k. 800–700 TCN | nơi: không xác định; trường phái Taittirīya của Kṛṣṇa Yajurveda, bắc Ấn Độ ngày nay | vùng: Nam Á | lĩnh vực: Toán học, Tôn giáo/Tâm linh | độ tin cậy niên đại: Thấp | wikidata: Q3384944 | câu hỏi lớn: Thực tại`

**Tư tưởng / đóng góp chính (~100 chữ):** Baudhāyana Śulbasūtra là phần "dây đo" (śulba) trong bộ Kalpasūtra của trường phái Taittirīya, soạn để dựng bàn thờ lửa đúng diện tích quy định cho tế lễ śrauta: hình học ở đây sinh ra từ ràng buộc nghi lễ, không từ nhu cầu lý thuyết. Văn bản phát biểu quy tắc đường chéo cho hình chữ nhật bất kỳ — hình vuông trên đường chéo bằng tổng hai hình vuông trên hai cạnh — kèm các bộ ba (3,4,5), (5,12,13), (8,15,17), (12,35,37). Đây là phát biểu bằng lời ở dạng tổng quát sớm nhất còn lại của quan hệ về sau mang tên Pythagoras. Sách còn cho xấp xỉ √2 bằng phân số 577/408, đúng tới năm chữ số thập phân, và phép biến đổi gần đúng vuông–tròn.

**Vì sao chọn (~80 chữ):** Ứng viên cùng truyền thống là Mānava, người Plofker xếp cùng tầng niên đại với ông, và Āpastamba, soạn Śulbasūtra kế tiếp khoảng 600 TCN. Baudhāyana thắng ở tính nguyên bản (c): Pingree xếp ba văn bản kia sau ông dựa trên dấu vết vay mượn, và cả ba chỉ chép lại xấp xỉ √2 cùng quy tắc đường chéo đã có ở ông. Về độ bền (b), bộ quy tắc này chi phối việc dựng bàn thờ Vệ Đà suốt nhiều thế kỷ. Kātyāyana bị loại vì soạn sau Pāṇini, không cùng thời.

**Kế thừa từ:**
- Quy tắc dựng bàn thờ trong tế lễ Vệ Đà (Taittirīya Saṃhitā, Śatapatha Brāhmaṇa) · kế thừa · trực tiếp
- Toán học Babylon cổ · tương đồng độc lập · suy đoán học giả

**Ảnh hưởng tới:**
- Truyền thống Śulbasūtra về sau (Āpastamba, Kātyāyana, Mānava) · kế thừa · trực tiếp
- CH02-BCE06-06 · tương đồng độc lập · suy đoán học giả

**Nguồn:** S. N. Sen và A. K. Bag, *The Śulbasūtras of Baudhāyana, Āpastamba, Kātyāyana and Mānava, with Text, English Translation and Commentary* (Indian National Science Academy, New Delhi, 1983); Kim Plofker, *Mathematics in India* (Princeton University Press, 2009), chương 2.
```

---

## 2 · Bảng kiểm chứng

| # | Khẳng định trong mục | Nguồn | Đã làm gì để xác nhận |
|---|---|---|---|
| 1 | Q-ID `Q3384944` là đúng người | Wikidata API | Gọi `wbsearchentities` cho "Baudhayana" → sáu thực thể, chỉ **một** là người: Q3384944 "ancient Indian mathematician". Gọi `wbgetentities` → `P31 = Q5` (human), `P106 = Q170790` (mathematician), `P101 = Q395` (mathematics), `P800 = Q15668516` (Śulbasūtra) **và** `Q4873430` (Śrautasūtra). Xem mục 5 về vấn đề đồng nhất. |
| 2 | P569 / P570 | Wikidata Q3384944 | `P569 = -0800` (circa), `P570 = -0800` (circa). Hai giá trị **trùng nhau**, tức đây là giá trị quy ước thay cho floruit chứ không phải niên đại sinh–mất thật. Trường `năm:` ghi `hoạt động k. 800–700 TCN`, cận dưới trùng P569. Độ tin cậy đặt **Thấp**, nên theo quy ước dự án không phải đối chiếu sai số; vẫn báo cáo để minh bạch. |
| 3 | Thuộc trường phái Taittirīya của Kṛṣṇa Yajurveda; bộ Kalpasūtra gồm sáu phần, Śulbasūtra là phần thứ sáu (3 adhyāya) | Wikipedia "Baudhayana sutras" (https://en.wikipedia.org/wiki/Baudhayana_sutras) | Fetch trang, lấy nguyên văn danh sách sáu văn bản: Śrauta-, Karmānta-, Dvaidha-, Gṛhya-, Dharma-, Śulbasūtra, và câu "belong to the Taittiriya branch of the Krishna Yajurveda school". |
| 4 | Mục đích văn bản là dựng bàn thờ lửa cho tế lễ śrauta | MacTutor, "Indian Sulbasutras" (https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_sulbasutras/); Plofker ch. 2 | MacTutor: các văn bản là sổ tay thi công, cho "rules for constructing altars", độ chính xác là điều kiện để nghi lễ thành. Trang tiểu sử MacTutor về Baudhāyana mô tả ông là tư tế Vệ Đà kiêm thợ lành nghề, "probably not interested in mathematics for its own sake". |
| 5 | **Phát biểu TỔNG QUÁT cho hình chữ nhật có trong Baudhāyana** (không chỉ trường hợp hình vuông) | Thibaut 1875; Sen–Bag 1983; S. G. Dani | Đây là điểm tôi được yêu cầu kiểm tra riêng, và **có mâu thuẫn giữa các nguồn**. Trang chuyên đề "Indian Sulbasutras" của MacTutor gán dạng tổng quát cho **Kātyāyana** và chỉ cho Baudhāyana trường hợp hình vuông — **trang này sai**. Câu sūtra gốc `dīrghacaturaśrasyākṣṇayā rajjuḥ pārśvamānī tiryaṅmānī ca yat pṛthagbhūte kurutas tad ubhayaṃ karoti` là của **Baudhāyana**, được Thibaut dịch năm 1875 ("The cord stretched in the diagonal of an oblong produces both areas which the cords forming the longer and shorter sides of an oblong produce separately"), và Wikipedia "Shulba Sutras" dẫn nó ở BŚS 1.12–1.13 (đánh số Sen–Bag; = 1.48 theo Thibaut), ngay sau trường hợp hình vuông ở 1.9 (= 1.45 Thibaut). Kātyāyana có một sūtra song song, nhưng muộn hơn. |
| 6 | Bộ ba (3,4,5), (5,12,13), (8,15,17), (12,35,37) | Wikipedia "Shulba Sutras"; S. G. Dani, *Current Science* 85 (2003) | Nguyên văn sūtra liệt kê các hình chữ nhật cạnh 3–4, 12–5, 15–8, 7–24, 12–35, 15–36. Tôi ghi bốn bộ ba dưới dạng (a,b,c) đã rút gọn và **không** ghi (7,24,25) hay (15,36,39) để giữ số chữ; danh sách trong mục là tập con, không khẳng định là đủ. |
| 7 | √2 ≈ 577/408, đúng tới năm chữ số thập phân, **có trong chính Baudhāyana** | MacTutor "Baudhayana"; Wikipedia "Baudhayana sutras"; Wikipedia "Shulba Sutras" | MacTutor dẫn đích danh "Chapter 1 verse 61 of Baudhayana's Sulbasutra", cho 577/408 = 1.414215686, "correct to five decimal places". Wikipedia định vị ở "Baudhāyana i.61-2". Công thức 1 + 1/3 + 1/(3·4) − 1/(3·4·34) lặp lại ở Āpastamba và Kātyāyana, kèm từ kỹ thuật `saviśeṣaḥ`. Tức **không phải** của Śulbasūtra muộn — Baudhāyana có trước. |
| 8 | Phép biến đổi gần đúng vuông–tròn | Wikipedia "Shulba Sutras"; Wikipedia "Baudhayana sutras" | "Circling the square" ở BŚS 2.9 (= i.58 Thibaut), "squaring the circle" ở 2.10–2.11, cho các giá trị π hàm ý khoảng 3,088 và 3,004. Mục chỉ ghi "gần đúng", không nêu con số, vì các nguồn không thống nhất về giá trị π hàm ý. |
| 9 | Āpastamba soạn khoảng 600 TCN; Pingree xếp Āpastamba thứ hai, Kātyāyana và Mānava sau, "trên dấu vết vay mượn" | MacTutor "Indian Sulbasutras"; Wikipedia "Shulba Sutras" dẫn Pingree | MacTutor: Baudhāyana k. 800 TCN, Mānava k. 750 TCN, Āpastamba k. 600 TCN, Kātyāyana k. 200 TCN. Wikipedia dẫn Pingree: Āpastamba "likely the next oldest", Kātyāyana và Mānava thứ ba–thứ tư "on the basis of apparent borrowings". |
| 10 | Plofker xếp Mānava cùng tầng niên đại với Baudhāyana, và xếp Kātyāyana sau Pāṇini | Wikipedia "Shulba Sutras" dẫn Plofker, *Mathematics in India* | Nguyên văn: Plofker đặt Kātyāyana sau "the great grammatical codification of Sanskrit by Pāṇini in probably the mid-fourth century BCE", nhưng đặt Mānava "in the same period as the Baudhayana". Đây là cơ sở để gọi Mānava là ứng viên **cùng thời** trong mục "Vì sao chọn", và để loại Kātyāyana vì không cùng thời. |
| 11 | Độ tin cậy niên đại **Thấp** | Plofker, *Mathematics in India*, ch. 2 | Wikipedia "Mathematics in India (book)" tóm tắt chương 2: "the absence of concrete astronomical observations within these texts has made it impossible to date them precisely". Đây là lý do trực tiếp cho nhãn Thấp, không phải suy đoán của tôi. |
| 12 | Quan hệ với toán học Babylon là **tương đồng độc lập**, không phải truyền thừa | Pingree; Plofker; Seidenberg (xem mục 5 bên dưới) | Quan hệ Pythagoras đã được biết ở Babylon cổ (Plimpton 322, k. 1800 TCN) dưới dạng bài toán ứng dụng, không phải phát biểu tổng quát bằng lời. Không nguồn nào tôi đọc nêu bằng chứng tiếp xúc. Pingree cảnh báo "it would be a mistake to see in [the altar builders'] works the unique origin of geometry". Seidenberg (1962) lập luận ngược chiều — rằng Babylon nhận từ Ấn Độ hoặc cả hai nhận từ nguồn thứ ba — nhưng đó là **thiểu số**, và Plofker còn nêu khả năng ngược lại, rằng tri thức hình học có sẵn được "consciously incorporated into ritual practice". Vì không bên nào có bằng chứng tiếp xúc, `tương đồng độc lập` là giá trị đúng theo §5. |
| 13 | Nguồn 1 tồn tại và bàn về Baudhāyana | archive.org, WorldCat, Google Books, sanskritlibrary.org | Sen & Bag 1983, INSA New Delhi, 293 trang, có bản quét toàn văn trên Internet Archive (`Kium_the-sulaba-sutras-of-baudayana-apastamba-katyayana-and-manava-by-sn-sen-and-ak-b`), có mục WorldCat. Bản XML Baudhāyana-Śulbasūtra của sanskritlibrary.org ghi rõ "based on the edition by Sen, S.N., and Bag, A.K." — tức đây là bản chuẩn đang được dùng. Tên trong nhan đề đã chứa Baudhāyana. |
| 14 | Nguồn 2 tồn tại và chương 2 bàn về Baudhāyana | Wikipedia "Mathematics in India (book)" | Kim Plofker, *Mathematics in India*, Princeton University Press, 2009, chín chương. Chương 2 phủ thời Vệ Đà 1500–500 TCN và Śulbasūtra, gồm "geometric rope constructions, the Pythagorean theorem, approximations for pi and the square root of two" — đúng bốn nội dung mục này khẳng định. |
| 15 | Năm trong trường `năm:` phân tích được | `atlaslib/common.py: parse_years` | Đọc hàm: chuỗi bị loại chỉ khi chứa `TK|thế kỷ|century|thiên niên kỷ`. `hoạt động k. 800–700 TCN` tách thành born = 800 TCN, died = 700 TCN, giao với khoảng nhóm BCE08 (800–701), nên `lint` không cảnh báo. Mẫu này đã dùng cho Homer, Hesiod, Amos, Isaiah trong cùng nhóm. |
| 16 | Từ vựng metadata hợp lệ | `atlaslib/common.py` | `Toán học` và `Tôn giáo/Tâm linh` đều có trong FIELDS (2 ≤ 2). `Nam Á` có trong REGIONS. `Thực tại` có trong BIG_QUESTIONS. `Thấp` có trong CONFIDENCE. `kế thừa` / `tương đồng độc lập` có trong RELATION_TYPES. `trực tiếp` / `suy đoán học giả` có trong EVIDENCE_LEVELS. Mỗi danh sách liên kết 2 mục (≤ 3). |
| 17 | Thêm mục này không phá ràng buộc nhóm | `atlaslib/lint.py` | BCE08 hiện 6 mục, thành 7 khi thêm Hezekiah, thành 8 với mục này — dưới trần 12. Mục này thêm lĩnh vực **Toán học** vào nhóm (nhóm hiện chỉ có Văn học, Tôn giáo/Tâm linh, Chính trị/Nhà nước, Quân sự) và thêm vùng **Nam Á** (nhóm hiện chỉ có Châu Âu, Trung Đông/Bắc Phi, Châu Phi hạ Sahara). Cả hai chỉ số đa dạng đều tăng. |

---

## 3 · Số chữ (đếm bằng token tách theo khoảng trắng, đúng cách `atlaslib/lint.py: words()` đếm)

| Mục | Số chữ | Khoảng cho phép | Kết quả |
|---|---|---|---|
| Tư tưởng / đóng góp chính | **129** | 70–130 | đạt (sát trần) |
| Vì sao chọn | **94** | 56–104 | đạt |

Đếm bằng `len([w for w in text.split() if w])` trên đúng chuỗi văn bản sau dấu hai chấm của nhãn in đậm.

---

## 4 · Đề xuất sửa liên kết đối ứng

Giữ ở mức tối thiểu. Chỉ **một** mục hiện có thực sự cần sửa.

### 4.1 · CH02-BCE06-06 (Pythagoras) — thêm một dòng vào "Kế thừa từ"

Đây là sửa đổi đáng làm nhất, vì chính mục Pythagoras là nơi chapter tự mâu thuẫn: phần văn xuôi đã viết "Định lý mang tên ông đã được biết trước ở Babylon và Ấn Độ" nhưng danh sách liên kết chỉ trỏ tới Babylon.

Dòng hiện tại (`content/ch02.md`, ngay dưới `**Kế thừa từ:**` của mục Pythagoras):

```
- CH02-BCE06-10 · kế thừa · suy đoán học giả
- Toán học Babylon · kế thừa · suy đoán học giả
```

Đổi thành:

```
- CH02-BCE06-10 · kế thừa · suy đoán học giả
- Toán học Babylon · kế thừa · suy đoán học giả
- CH02-BCE08-08 · tương đồng độc lập · suy đoán học giả
```

Thành 3 mục, đúng trần. **Không cần sửa phần văn xuôi của Pythagoras** — câu đã có sẵn ở đó nay có liên kết đỡ.

Lưu ý loại quan hệ: `tương đồng độc lập` là giá trị đúng, không phải `kế thừa`. Không có bằng chứng tiếp xúc nào giữa truyền thống Śulbasūtra và Pythagoras; §5 của prompt quy định chính trường hợp này dùng `tương đồng độc lập`. Tiền lệ trong chapter: mục Hesiod đặt `Vũ trụ luận Cận Đông (Enūma Eliš) · tương đồng độc lập · suy đoán học giả` ngay trong danh sách "Kế thừa từ".

### 4.2 · Hai sửa đổi ghi sổ, không phải liên kết

- **Phần "Giới thiệu chapter"** ghi "Bốn nhóm thế kỷ gồm **33 nhân vật**". Con số này phải tăng theo số mục thực tế được thêm (34 nếu chỉ thêm Baudhāyana; 35 nếu thêm cả Hezekiah). Người biên tập cần cập nhật một lần sau khi chốt toàn bộ các mục bổ sung từ `review-ch02.md`.
- **Mục "Ứng viên mạnh đã bị loại và lý do"** trong Ghi chú biên tập nên có thêm một dòng, để các Śulbasūtra còn lại được nêu công khai như §5 đòi hỏi:

```
- Āpastamba, Kātyāyana, Mānava (truyền thống Śulbasūtra): xếp sau Baudhāyana theo thứ tự tương đối của Pingree, dựa trên dấu vết vay mượn văn bản. Kātyāyana còn bị loại vì niên đại: Plofker đặt ông sau Pāṇini, tức thuộc Chapter 3.
```

### 4.3 · Liên kết đã cân nhắc và **không** đề xuất

- **Baudhāyana → Pāṇini (CH02-BCE05-08).** Có lập luận học thuật (Frits Staal, Subhash Kak) rằng hình thức sūtra giàu tính thuật toán của nghi lễ Vệ Đà đi trước và định hình văn phong quy tắc của Aṣṭādhyāyī. Tôi **không** đề xuất liên kết này: nó thuộc loại suy đoán ở tầng "phong cách văn bản", không kiểm chứng được bằng nguồn tôi đã đọc, và thêm vào sẽ là đúng loại suy diễn mà §5 cấm. Nếu Owner muốn, mức đúng nhất sẽ là `tương đồng độc lập · suy đoán học giả`, không phải `kế thừa`.
- **Baudhāyana → Thales (CH02-BCE06-05).** Không có cơ sở. Bỏ.
- **Baudhāyana → Uddālaka Āruṇi / Yajnavalkya.** Cùng vùng, cùng tầng văn bản Vệ Đà muộn, nhưng khác hẳn thể loại và không có quan hệ nội dung nào kiểm chứng được. Bỏ.

---

## 5 · Những điều tôi **không** kiểm chứng được, nói thẳng

1. **"Baudhāyana" là một cá nhân hay một trường phái.** Đây là điểm yếu lớn nhất của mục này. Bộ Baudhāyana Kalpasūtra gồm sáu văn bản nghi lễ của cùng một śākhā; Wikidata gộp tác giả Śulbasūtra và tác giả Śrautasūtra làm **một người** (Q3384944, `P800` trỏ tới cả hai), và **không có** thực thể Wikidata riêng cho tác giả Dharmasūtra (tìm "Baudhayana Dharmasutra" trả về rỗng). Nhưng việc Wikidata gộp **không phải** là phán quyết học thuật. "Baudhāyana" là tên theo gotra, và quy ước đặt tên văn bản sūtra theo tên người sáng lập dòng truyền là chuyện thường. Tôi **không** tìm được nguồn chuyên khảo khẳng định dứt khoát rằng một cá nhân duy nhất soạn cả sáu văn bản. Vì vậy tôi gắn nhãn **[Tranh cãi lịch sử]**, cùng loại với Homer, Yajnavalkya và Lão Tử trong chapter này. Đây là lựa chọn biên tập, Owner có thể bác.
2. **Số sūtra có hai hệ đánh số không khớp nhau.** Bản Thibaut (1875) đánh liên tục trong adhyāya 1 (quy tắc đường chéo = 1.48, √2 = 1.61–62, vuông→tròn = 1.58); bản Sen–Bag (1983) đánh lại (1.9, 1.12–1.13, 2.9–2.12). Tôi **cố ý không đưa số sūtra vào mục**, vì không có bản in nào trong tay để đối chiếu trực tiếp hai hệ. Bảng kiểm chứng ghi cả hai cách đánh số kèm nguồn.
3. **Tôi không đọc được trực tiếp Plofker và Sen–Bag.** Máy không có công cụ trích xuất PDF (`pdftotext`, `pypdf`, `pdftoppm` đều thiếu), nên bản review của David Mumford về Plofker (AMS *Notices*, 2010) và bài S. G. Dani, *Current Science* 85 (2003) 219–224 tải về được nhưng **không đọc được**. Cả hai URL trả HTTP 200 và đúng loại tệp, nên tôi xác nhận **tài liệu tồn tại**; nội dung chương 2 của Plofker thì tôi xác nhận gián tiếp qua bản tóm tắt chương (xem bảng, dòng 14). Nếu Owner muốn chặt hơn, nên đối chiếu tay một lần với bản in Plofker tr. 16–27.
4. **Niên đại 800–700 TCN là quy ước, không phải kết quả đo.** Không có mốc thiên văn, không có bi ký, không có khảo cổ gắn với văn bản. Con số k. 800 TCN là niên đại truyền thống do giới sử toán học dùng (MacTutor, Wikidata); Plofker nói thẳng là không định niên đại chính xác được, và một số nhà nghiên cứu đẩy muộn hơn. `độ tin cậy niên đại: Thấp` phản ánh đúng điều đó. Nếu P4 siết chuẩn niên đại, mục này nằm cùng loại rủi ro với Homer, Yajnavalkya và Lão Tử — không hơn, nhưng cũng không kém.
5. **"Phát biểu bằng lời ở dạng tổng quát sớm nhất còn lại"** là khẳng định về *cái còn sót lại*, không phải về *cái đã từng có*. Người Babylon cổ biết quan hệ này sớm hơn ít nhất một nghìn năm, nhưng dưới dạng bài toán số cụ thể. Nếu Owner thấy câu này vẫn dễ bị đọc thành tuyên bố ưu tiên phát minh, có thể đổi thành "phát biểu tổng quát bằng lời sớm nhất còn giữ được" — cùng nghĩa, nhấn mạnh hơn vào chữ "còn giữ được".
6. **`nơi:` là trường yếu nhất.** Không ai biết Śulbasūtra được soạn ở đâu. Tôi ghi `không xác định` trước, rồi mới nêu trường phái và vùng địa lý rộng. Trường này sẽ không khớp với kỳ vọng "địa danh, vùng lãnh thổ ngày nay" của template, nhưng bịa một địa danh thì tệ hơn.

---

## 6 · Về câu hỏi "liệu Āpastamba hay Kātyāyana có cơ sở mạnh hơn không"

Tôi đã kiểm tra riêng và câu trả lời là **không**. Ba lý do:

1. **Xấp xỉ √2 nằm trong chính Baudhāyana**, không phải chỉ trong Śulbasūtra muộn. MacTutor dẫn đích danh chương 1 câu 61 của Baudhāyana. Āpastamba và Kātyāyana chép lại **cùng một công thức**, kèm cùng một thuật ngữ `saviśeṣaḥ`.
2. **Phát biểu tổng quát nằm trong chính Baudhāyana.** Đây là điểm tôi suýt kết luận ngược: trang chuyên đề của MacTutor gán dạng tổng quát cho Kātyāyana. Nhưng câu Sanskrit gốc đã được Thibaut dịch từ 1875 **từ bản Baudhāyana**, và Sen–Bag đánh nó ở BŚS 1.12. Trang MacTutor đó không đáng tin ở điểm này.
3. **Kātyāyana không đủ điều kiện về niên đại.** Plofker đặt ông sau Pāṇini (giữa TK 4 TCN), tức ngoài cửa sổ 800–401 TCN của Chapter 2 nếu tính nghiêm. Āpastamba (k. 600 TCN) thì nằm trong chapter nhưng ở nhóm BCE07/BCE06, và theo Pingree là người vay mượn chứ không phải người khởi xướng.

Nói cách khác: lập luận của N12 **đứng vững** sau khi kiểm tra, và đứng vững đúng ở những điểm nó nêu. Điều duy nhất tôi phải chỉnh so với cách N12 diễn đạt là sắc thái của chữ "sớm nhất" — xem mục 5.5 bên trên.
