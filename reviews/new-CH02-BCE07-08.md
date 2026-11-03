# Mục mới đề xuất · CH02-BCE07-08 · Sennacherib

Soạn theo `prompts/atlas-prompt.md`, trả lời phát hiện **N12** của `reports/review-ch02.md` ("Lưỡng Hà thiếu đúng một người, là Sennacherib").
**Không chỉnh sửa `content/ch02.md`.** Tài liệu này chỉ đề xuất.

---

## 0 · Các quyết định khung (đã chốt, ghi lại để không phải dẫn lại)

- **Wikidata Q207140** = Sennacherib, `P31 = Q5`, `P569 = 745 TCN` (độ chính xác: năm), `P570 = 20/10/681 TCN`. Trường `năm: k. 745–681 TCN`, `độ tin cậy niên đại: Cao` — khớp Wikidata ở cả hai đầu (lệch 0 năm, dung sai Cao là ±5). **Không** ghi "trị vì 705–681 TCN": năm 705 lệch 40 năm so với P569 và sẽ vướng lint; cách ghi theo thời gian trị vì chỉ dành cho vua không có năm sinh (Tiglath-Pileser III, Piye).
- **Nhóm BCE07** đúng theo quy tắc floruit: hai công trình biện minh cho ông — chương trình kênh Nineveh (703–688 TCN) và việc tái thiết Nineveh — đều thuộc TK 7 TCN. Chiến dịch 701 và vụ phá Babylon 689 cũng vậy.
- **Lĩnh vực: Kỹ thuật/Công nghệ, Nghệ thuật/Kiến trúc.** Nhóm BCE07 hiện chưa có lĩnh vực nào trong hai lĩnh vực này; đồng thời cách gán này giữ ông ngoài trục Chính trị/Nhà nước mà Tiglath-Pileser III (CH02-BCE08-05) và Ashurbanipal (CH02-BCE07-01) đã đại diện — đúng như N12 lập luận: vấn đề không phải thiếu chỗ cho Lưỡng Hà, mà là chapter chọn nhầm người cho tiêu chí kỹ thuật.
- **Đối thủ cùng thời** cho "Vì sao chọn": Sargon II (Q208336, P569 765 / P570 705, trị vì 722–705) và Taharqa (Q315714, P570 664, trị vì 690–664). Cả hai đều giao đời với Sennacherib. Hezekiah **không** được nêu làm đối thủ bị loại — ông là ứng viên riêng (N12 đề nghị thêm) chứ không phải người cạnh tranh cùng lĩnh vực.
- **Liên kết Hezekiah** dùng tên thường "Hezekiah xứ Judah". Nếu mục Hezekiah được thêm thành **CH02-BCE08-07**, đổi dòng đó sang ID.

---

## 1 · Mục hoàn chỉnh, sẵn sàng dán vào `content/ch02.md` (cuối nhóm BCE07, sau CH02-BCE07-07)

```markdown
### CH02-BCE07-08 · Sennacherib (Sîn-aḫḫē-erība)
`năm: k. 745–681 TCN | nơi: Nineveh, Assyria, nay thuộc Iraq | vùng: Trung Đông/Bắc Phi | lĩnh vực: Kỹ thuật/Công nghệ, Nghệ thuật/Kiến trúc | độ tin cậy niên đại: Cao | wikidata: Q207140 | câu hỏi lớn: Không áp dụng`

**Tư tưởng / đóng góp chính (~100 chữ):** Vua Assyria, nổi tiếng vì cuộc vây Jerusalem năm 701 TCN, nhưng dấu ấn bền nhất là kỹ thuật thuỷ lợi và đô thị. Từ 703 đến 688 TCN ông đào bốn hệ kênh đưa nước núi về Nineveh; hệ cuối, kênh Khinis dài khoảng 55 km, vượt thung lũng Jerwan bằng cầu máng đá vôi đẽo dài 280 m, khắc bi ký của ông — kiểu công trình chưa thấy ở đâu trước thời La Mã. Nineveh mở rộng tới 750 ha, tường thành 12 km, dân số ước trên 100.000, vào hàng lớn nhất đương thời; cung "Không đối thủ" (ekallu ša šānina lā īšû) chứa phù điêu Lachish. Năm 689 ông phá huỷ Babylon, cho nước Arahtu cuốn trôi nền thành.

**Vì sao chọn (~80 chữ):** Hai ứng viên cùng thời đã cân nhắc: Sargon II (trị vì 722–705 TCN), cha ông, người xây kinh đô mới Dur-Sharrukin; và Taharqa (trị vì 690–664 TCN), vua Kush–Ai Cập với các công trình đền ở Kawa và Karnak. Sennacherib vượt ở tính nguyên bản (c): cầu máng Jerwan là kiểu công trình không thấy ở đâu khác trước thời La Mã, còn Dur-Sharrukin bị bỏ ngay khi Sargon chết; và ở độ bền (b): hệ kênh Khinis còn để lại dấu vết vật chất lẫn bi ký định niên tại chỗ, nguồn hiếm có về kỹ thuật cổ đại.

**Kế thừa từ:**
- Sargon II (chương trình xây Dur-Sharrukin) · kế thừa · trực tiếp
- CH02-BCE08-05 · kế thừa · qua trường phái
- Truyền thống vườn thượng uyển Assyria (Ashurnasirpal II ở Kalhu) · kế thừa · suy đoán học giả

**Ảnh hưởng tới:**
- CH02-BCE07-01 · kế thừa · trực tiếp
- Esarhaddon (tái thiết Babylon) · phản bác · trực tiếp
- Hezekiah xứ Judah · phản bác · suy đoán học giả

**Nguồn:** Thorkild Jacobsen và Seton Lloyd, *Sennacherib's Aqueduct at Jerwan*, Oriental Institute Publications 24 (Chicago, 1935), https://isac-assets.s3.amazonaws.com/isac-publications/oip24.pdf; John Malcolm Russell, *Sennacherib's Palace Without Rival at Nineveh* (University of Chicago Press, 1991).
```

---

## 2 · Bảng kiểm chứng

| # | Khẳng định trong mục | Nguồn | Đã làm gì để xác nhận |
|---|---|---|---|
| 1 | Q207140 đúng người; P569 = 745 TCN, P570 = 681 TCN | Wikidata API | Chốt ở phiên trước (§0). Trường `năm:` lệch 0 năm so với cả hai mốc. |
| 2 | "nổi tiếng vì cuộc vây Jerusalem năm 701 TCN" | Wikipedia "Sennacherib's campaign in the Levant"; 2 Các Vua 18–19 (NRSVUE, biblegateway) | Fetch cả hai. Xem §6 về cách hai phía kể khác nhau. |
| 3 | "Từ 703 đến 688 TCN ông đào bốn hệ kênh" | Reade, "Studies in Assyrian Geography I: Sennacherib and the Waters of Nineveh", *RA* 72 (1978), qua trích dẫn trong Morandi Bonacossi 2018 và Stampoultzidis et al. 2024 | Trích đoạn máy tìm kiếm trả về từ tài liệu Udine: chương trình thuỷ lợi "in four stages over 15 years from 703 to 688 BC"; giai đoạn 1 là kênh Kisiri lấy nước Khosr cách Nineveh 16 km. **Không mở được PDF gốc** (ResearchGate và air.uniud.it trả 403), nên đây là xác nhận qua trích đoạn. |
| 4 | "kênh Khinis dài khoảng 55 km" | Morandi Bonacossi / Land of Nineveh Archaeological Project; Ur, *Iraq* 67 (2005) | Trích đoạn tìm kiếm: "The Khinis canal was a 55-km-long canal that started at Khinis", "the fourth and last stage of Sennacherib's irrigation program". Các nguồn phổ thông ghi "50 km" (Wikipedia "Jerwan"), "50+ km" (Wikipedia "Hanging Gardens"), review N12 ghi "~50 km". Tôi dùng con số chuyên ngành 55 km kèm chữ "khoảng". Không mở được PDF gốc (403). |
| 5 | Jerwan: "cầu máng đá vôi đẽo dài 280 m" | Jacobsen & Lloyd 1935, tr. 6 (bản OCR trên archive.org, `oip24_djvu.txt`) | Đọc trực tiếp: "over 280 meters in length", rộng 22 m không kể trụ chống, vòm giữa cao khoảng 9 m. Chữ "rộng 22 m" bị cắt khỏi mục vì giới hạn số chữ. |
| 6 | Số khối đá — **không đưa vào mục** | Jacobsen & Lloyd 1935, tr. 6; Fales & Del Fabbro, "Back to Sennacherib's Aqueduct at Jerwan", *Iraq* 76 (2014) | OIP 24 viết nguyên văn: nếu khối đá trung bình "rather less than 50 centimeters cubed" thì số khối "well in excess of two million" — tức là **suy ra từ thể tích**, không đếm. Fales & Del Fabbro (2014) tính lại còn **443.520** khối. Con số "khoảng 2 triệu" của N12 là con số cũ; tôi bỏ hẳn khỏi mục để không phải chọn phe trong 125 chữ. Nếu Owner muốn có, dạng an toàn là "từ hơn bốn trăm nghìn tới hai triệu khối đá, tuỳ ước tính". |
| 7 | "khắc bi ký của ông" | Jacobsen & Lloyd 1935, tr. 19–27 (Inscription A–D) | Đọc bản OCR. Inscription A (lặp nhiều lần trên khối đá): "Belonging to Sennacherib, king of the world, king of Assyria." Inscription B (bi ký xây dựng): "...For a long distance, adding to it the waters of the twain Hazur River... I caused a canal to be dug to the meadows of Nineveh. Over deep-cut ravines I spanned a bridge of white stone blocks." Đây là bi ký xây dựng tại chỗ mà N12 nhắc. |
| 8 | "kiểu công trình chưa thấy ở đâu trước thời La Mã" | Trang ISAC mô tả OIP 24 | Fetch trực tiếp: "a type of structure unknown elsewhere before Roman times". Đây là dạng có thể quy nguồn của khẳng định "cổ nhất cùng loại"; Wikipedia "Jerwan" dè dặt hơn: "Some consider it to be the world's oldest aqueduct". Mục dùng cách nói của ISAC, không dùng chữ "cổ nhất thế giới". |
| 9 | "Nineveh mở rộng tới 750 ha" | Uni Heidelberg, "History of Nineveh" (ninive.uni-heidelberg.de); Wikipedia "Nineveh" | Heidelberg: "expanded to around 750 hectares". Wikipedia: "about 7 square kilometres (1,730 acres)" = 700 ha, cùng bậc. Con số 150 ha trước Sennacherib chỉ có trong trích đoạn tìm kiếm, nên đã **bỏ** khỏi mục. |
| 10 | "tường thành 12 km" | Wikipedia "Nineveh" | Fetch: "About 12 km in length, the wall system consisted of an ashlar stone retaining wall..." Wikipedia "Sennacherib": tường cao tới 25 m, dày 15 m, có hào. |
| 11 | "dân số ước trên 100.000, vào hàng lớn nhất đương thời" | Wikipedia "Nineveh"; Heidelberg; Wikipedia "List of largest cities throughout history" | Wikipedia Nineveh: "more than 100,000 inhabitants (maybe closer to 150,000), about twice as many as Babylon at the time, placing it among the largest settlements worldwide". Heidelberg: "the largest metropolis in the world at the time". Bảng Chandler/Modelski/Morris: Ian Morris xếp Nineveh lớn nhất quanh 700–650 TCN (100.000–120.000); Modelski và Chandler lại xếp Thebes/Babylon ở một số mốc. Vì các bảng không thống nhất, mục viết "vào hàng lớn nhất" chứ **không** viết "lớn nhất thế giới" như N12. |
| 12 | Cung "Không đối thủ" (ekallu ša šānina lā īšû) | Wikipedia "Sennacherib" | Fetch: "Sennacherib called this palace the *ekallu ša šānina la išu*, the 'Palace without Rival'". Kích thước cung **không đưa vào mục** vì hai trang Wikipedia mâu thuẫn (450 × 220 m vs 503 × 242 m); Russell 1991 là chỗ để Owner tra khi cần. |
| 13 | "chứa phù điêu Lachish" | Wikipedia "Lachish reliefs" | Fetch: tìm thấy trong South-West Palace của Sennacherib ở Nineveh, Layard khai quật 1845–1847, nay ở British Museum, mô tả cuộc vây Lachish 701 TCN. Chữ "nay ở British Museum" bị cắt vì số chữ. |
| 14 | "Năm 689 ông phá huỷ Babylon, cho nước Arahtu cuốn trôi nền thành" | Bi ký Bavian (RINAP 3/2, Sennacherib 223), qua Wikipedia "Sennacherib" và trích dẫn RINAP | Wikipedia: "I destroyed the city and its houses, from foundation to parapet; I devastated and burned them"; đào kênh dẫn nước Arahtu qua thành, "utterly dissolved it with water and made it like inundated land"; mang tượng Marduk về Assyria. Trích đoạn RINAP: "The wall and the outer-wall, temples and gods, temple-towers of brick and earth... I razed and dumped them into the Arahtu canal." Xem §7. |
| 15 | Sargon II trị vì 722–705, xây Dur-Sharrukin, thành bị bỏ khi ông chết | Wikidata Q208336 (P39 qualifiers 722–705); Wikipedia "Dur-Sharrukin" | Fetch cả hai: thành xây k. 716–706; "After his unexpected death his son and successor Sennacherib abandoned the project, and relocated the capital... to the city of Nineveh, 20 km south." |
| 16 | Taharqa trị vì 690–664, đền ở Kawa và Karnak | Wikidata Q315714 (P570 664); Wikipedia "Taharqa" | Fetch: "690–664 BC"; "new temple at Kawa", "additions to the Temple at Karnak", Jebel Barkal. Ông cũng xuất hiện trong 2 Các Vua 19:9 liên quan chiến dịch 701 (dù lên ngôi mười năm sau) — đúng là nhân vật cùng thời, cùng lĩnh vực xây dựng. |
| 17 | Kế thừa: Sargon II · kế thừa · trực tiếp | Wikipedia "Dur-Sharrukin" | Sennacherib là thái tử dưới triều Sargon và kế thừa trực tiếp chương trình xây kinh đô (chuyển địa điểm chứ không bỏ ý tưởng). |
| 18 | Kế thừa: CH02-BCE08-05 · qua trường phái | Mục Tiglath-Pileser III hiện có | Ông vận hành bộ máy tỉnh và quân thường trực do Tiglath-Pileser III tạo ra; mục hiện có đã mô tả điều này cho Ashurbanipal theo cùng cách. |
| 19 | Kế thừa: vườn thượng uyển Assyria (Ashurnasirpal II ở Kalhu) · suy đoán học giả | Wikipedia "Nimrud" | Fetch: Ashurnasirpal "established botanical gardens, filled with foreign plants brought back from his wide-ranging campaigns". Sennacherib cũng nhập cây từ khắp đế chế (Wikipedia "Sennacherib"). **Không** tìm được xác nhận trực tiếp cho tên kênh Patti-ḫegalli trong các trang đã mở, nên dòng liên kết nói về vườn, không nói về kênh, và để mức "suy đoán học giả". |
| 20 | Ảnh hưởng: CH02-BCE07-01 · kế thừa · trực tiếp | Wikipedia "Library of Ashurbanipal" | Fetch: phát hiện đầu tiên của thư viện (Layard, cuối 1849) là "in the so-called South-West Palace, which was the Royal Palace of king Sennacherib"; Rassam tìm phần còn lại ở cung Bắc (1852). Tức thư viện mà mục Ashurbanipal ca ngợi nằm một phần ngay trong cung của Sennacherib, trong kinh đô ông dựng. |
| 21 | Ảnh hưởng: Esarhaddon · phản bác · trực tiếp | Wikipedia "Sennacherib" | Fetch: Esarhaddon "eventually rebuilt Babylon, reversing this policy". Đảo ngược chính sách của cha là quan hệ "phản bác" theo đúng nghĩa; bằng chứng là bi ký của chính Esarhaddon, tức trực tiếp. |
| 22 | Ảnh hưởng: Hezekiah xứ Judah · phản bác · suy đoán học giả | Wikipedia "Siloam tunnel"; 2 Sử Ký 32:2–4, 30 | Đường hầm 533 m được truyền thống quy cho Hezekiah như biện pháp chống vây trước Sennacherib (2 Sử Ký 32:2–4). Nhưng Reich & Shukron (2011) đẩy niên đại lên cuối TK 9 – đầu TK 8 TCN, trước Hezekiah. Vì vậy quan hệ "phản bác" (kháng cự về quân sự–kỹ thuật) để ở mức **suy đoán học giả**, không phải trực tiếp. |
| 23 | Nguồn 1 tồn tại, đúng chủ đề, URL hoạt động | Trang ISAC; archive.org | Trang ISAC: "Thorkild Jacobsen and Seton Lloyd, with a preface by Henri Frankfort. OIP 24. Chicago, 1935. Pp. xii + 52, 12 figures, frontispiece, 36 plates." URL PDF đã được phiên trước xác nhận; phiên này đọc nội dung qua bản OCR archive.org (PDF gốc vượt giới hạn 10 MB của công cụ fetch). |
| 24 | Nguồn 2 tồn tại, đúng chủ đề | Phiên trước xác minh (ISBN 0226731758) | Không kiểm lại trong phiên này; chủ đề nằm ngay trong nhan đề. |
| 25 | Từ vựng metadata hợp lệ | `atlaslib/common.py` | `Kỹ thuật/Công nghệ`, `Nghệ thuật/Kiến trúc` ∈ FIELDS (2 ≤ 2). `Trung Đông/Bắc Phi` ∈ REGIONS. `Không áp dụng` ∈ BIG_QUESTIONS. `Cao` ∈ CONFIDENCE. `kế thừa`/`phản bác` ∈ RELATION_TYPES. `trực tiếp`/`qua trường phái`/`suy đoán học giả` ∈ EVIDENCE_LEVELS. Mỗi danh sách 3 mục = trần. |
| 26 | `năm:` phân tích được | `atlaslib/common.py: parse_years` | "k. 745–681 TCN": `_APPROX_RE` bắt "k.", vế sau có TCN nên cả hai vế âm → born −745, died −681; giao với khoảng BCE07 (−700…−601). |

---

## 3 · Số chữ

Đếm bằng đúng hàm `atlaslib/lint.py: words()` = `len([w for w in s.split() if w])`, trên phần văn bản sau nhãn in đậm:

| Trường | Số chữ | Khoảng lint | Kết quả |
|---|---|---|---|
| Tư tưởng / đóng góp chính | **124** | 70–130 | đạt |
| Vì sao chọn | **101** | 56–104 | đạt |

(Bản nháp đầu dài 162 chữ; đã cắt số khối đá, chiều rộng cầu máng, "nay ở British Museum" và con số 150 ha — tất cả chuyển sang bảng kiểm chứng.)

**Kiểm tra lint thật:** đã chèn mục vào một bản sao `content/ch02.md` trong scratchpad (cuối nhóm BCE07) và chạy `python build.py --lint-only <bản sao>`. Kết quả: *Parse: 1 chapter, 37 nhân vật · 0 lỗi · 2 cảnh báo · 17 ghi chú*. Hai cảnh báo là của Jeremiah và Mahāvīra (P31 không phải Q5), có sẵn từ trước. Mục mới chỉ sinh **một INFO**: "kế thừa từ CH02-BCE08-05 nhưng CH02-BCE08-05 không ghi 'Ảnh hưởng tới' CH02-BCE07-08 (P4 sẽ đồng bộ)" — đúng điều §4.2 đã giải thích. Đối chiếu Wikidata Q207140 không sinh cảnh báo niên đại. `content/ch02.md` gốc không bị đụng tới.

---

## 4 · Đề xuất sửa liên kết đối ứng

Giữ tối thiểu: **một** sửa liên kết, hai sửa ghi sổ.

### 4.1 · CH02-BCE07-01 (Ashurbanipal) — thêm một dòng "Kế thừa từ"

Hiện tại (`content/ch02.md`, dưới `**Kế thừa từ:**` của mục Ashurbanipal):

```
- CH02-BCE08-05 · kế thừa · qua trường phái
```

Đổi thành:

```
- CH02-BCE08-05 · kế thừa · qua trường phái
- CH02-BCE07-08 · kế thừa · trực tiếp
```

Lý do: Ashurbanipal là cháu nội; kinh đô Nineveh và cung Tây Nam — nơi Layard tìm thấy phần đầu của thư viện năm 1849 — đều do Sennacherib dựng. Đây là mắt xích vật chất giữa "người xây thành" và "người gom sách", đúng loại liên kết mà Owner muốn nhìn thấy.

### 4.2 · CH02-BCE08-05 (Tiglath-Pileser III) — **không** sửa

"Ảnh hưởng tới" của mục này đã đủ 3 dòng (trần). Liên kết ngược được giữ ở phía Sennacherib (dòng "CH02-BCE08-05 · kế thừa · qua trường phái").

### 4.3 · Hai sửa ghi sổ

- **Ghi chú biên tập → "Ứng viên mạnh đã bị loại"**, dòng hiện tại:
  ```
  - Taharqa, Sargon II, Nebuchadnezzar II: bị loại vì kế thừa mô hình do Piye và Tiglath-Pileser III tạo ra (riêng Nebuchadnezzar II chỉ kế thừa ở mức lỏng).
  ```
  Đề nghị thêm một vế để lý do loại Sargon II và Taharqa cũng bao luôn trục kỹ thuật:
  ```
  - Taharqa, Sargon II, Nebuchadnezzar II: bị loại vì kế thừa mô hình do Piye và Tiglath-Pileser III tạo ra (riêng Nebuchadnezzar II chỉ kế thừa ở mức lỏng); ở trục Kỹ thuật/Kiến trúc, Sargon II và Taharqa cũng xếp sau Sennacherib (xem CH02-BCE07-08).
  ```
- **"Giới thiệu chapter"** hiện ghi "Bốn nhóm thế kỷ gồm 36 nhân vật"; thêm mục này thành **37** (và tăng tiếp nếu Hezekiah, Croesus được thêm). Sửa một lần sau khi chốt toàn bộ các mục bổ sung từ `review-ch02.md`.

### 4.4 · Liên kết đã cân nhắc và **không** đề xuất

- **Sennacherib → Vườn treo Babylon / truyền thống Hy Lạp.** Là giả thuyết của Dalley (xem §8), chưa được chấp nhận rộng; đưa vào danh sách liên kết sẽ là chọn phe. Để ở ghi chú.
- **Sennacherib → Herodotus (CH02-BCE05-03).** Herodotus II.141 kể về ông (xem §6), nhưng đó là Herodotus *nhắc đến* ông, không phải chịu ảnh hưởng. Bỏ.
- **Sennacherib → CH02-BCE06-07 Cyrus / CH02-BCE05-10 Darius.** Kỹ thuật kênh–vườn Achaemenid có thể kế thừa Assyria, nhưng không nguồn nào đã mở nói điều đó cụ thể cho Sennacherib. Bỏ.

---

## 5 · Những điều **không** kiểm chứng được, nói thẳng

1. **Các PDF chuyên ngành đều không mở được.** ResearchGate, air.uniud.it, Semantic Scholar, Cambridge Core (429), British Museum blog — tất cả chặn công cụ fetch. Con số **55 km** (kênh Khinis), **703–688** (bốn giai đoạn theo Reade) và **443.520** khối (Fales & Del Fabbro 2014) đều đến từ **trích đoạn do máy tìm kiếm trả về** của chính các tài liệu đó, không phải từ việc tôi đọc trang. Tôi coi đây là xác nhận ở mức "nguồn tồn tại và nói điều đó", chưa phải "đã đọc đúng ngữ cảnh". Nếu Owner có quyền truy cập thư viện, nên đối chiếu Morandi Bonacossi 2018 (*Ash-sharq* 2/2) và Fales & Del Fabbro 2014 (*Iraq* 76) một lần.
2. **Niên đại riêng của Jerwan.** N12 viết "k. 703–690 TCN" — đó là khung của *toàn bộ* chương trình kênh (hoặc gần vậy). Riêng hệ Khinis–Jerwan là giai đoạn **cuối**, k. 690 TCN (Wikipedia "Khinnis Reliefs": "around 690 BCE"), bi ký Bavian được định niên **688** theo một nguồn và "chủ đề chính là các sự kiện năm 689" theo nguồn khác. Jacobsen & Lloyd 1935 (bản OCR) không cho niên đại tuyệt đối. Mục viết "Từ 703 đến 688 TCN ông đào bốn hệ kênh... hệ cuối, kênh Khinis" — tức tránh gán một năm cụ thể cho riêng Jerwan.
3. **"Hazur" trong Inscription B** là cách đọc năm 1935; các bản dịch mới (RINAP 3/2) có thể đọc tên sông khác. Tôi không dẫn tên sông vào mục.
4. **Phản ứng học thuật với Dalley** (§8): tôi chỉ có (i) Frahm "unlikely" qua Wikipedia "Sennacherib", (ii) Bichler & Rollinger qua một bản tóm tắt thứ cấp trong kết quả tìm kiếm, (iii) một bài điểm sách trên academia.edu không mở được (chỉ có tóm tắt máy tìm kiếm). Không có trích dẫn nào tôi đọc trực tiếp từ nguồn gốc.
5. **Herodotus II.141**: xác nhận nội dung (chuột cắn dây cung ở Pelusium) qua Wikipedia "Sennacherib" và World History Encyclopedia; Perseus trả về trang rỗng và sacred-texts chặn. Số chương II.141 là theo quy ước phổ biến, chưa đối chiếu bản gốc trong phiên này.
6. **Russell 1991**: phiên này không kiểm lại; dựa vào xác minh của phiên trước (ISBN 0226731758).

---

## 6 · Chiến dịch 701 TCN — hai phía kể, không phân xử

Mục chỉ dành bảy chữ cho việc này ("nổi tiếng vì cuộc vây Jerusalem năm 701 TCN"); phần dưới là để Owner có đủ ngữ cảnh.

**Phía Assyria — lăng trụ của chính Sennacherib.** Ba bản chính, gần như cùng văn bản: *Taylor Prism* (British Museum, viết năm 691, tìm ở Nineveh k. 1830), *lăng trụ ISAC/Chicago* (viết 689, mua năm 1919), *lăng trụ Jerusalem* (Bảo tàng Israel, viết 691, mua tại Sotheby's 1970). Nội dung: ông vây và chiếm **46 thành có tường** của Hezekiah, bắt đi **200.150 người**, nhốt Hezekiah "trong Jerusalem như chim trong lồng", chia đất Judah cho các chư hầu, và nhận cống **30 talent vàng, 800 talent bạc** cùng ngà voi, con gái, cung nữ, nhạc công. Lăng trụ **không** nói ông chiếm Jerusalem, không mô tả trận đánh ở Jerusalem, và kết thúc bằng việc Hezekiah thần phục nộp cống.

**Phía Kinh Thánh — 2 Các Vua 18–19.** 18:13–16: Sennacherib chiếm các thành kiên cố; Hezekiah nộp **300 talent bạc, 30 talent vàng** (khớp vàng, lệch bạc 300/800). 18:17–37: Rabshakeh đến dưới tường Jerusalem khiêu khích. 19:35–37: "thiên sứ của Đức Chúa" giết **185.000** quân Assyria trong trại; Sennacherib rút về Nineveh và bị hai con Adrammelech và Sharezer giết khi đang thờ trong đền Nisroch; Esarhaddon kế vị. (Vụ ám sát là có thật — 20/10/681 — nhưng xảy ra **hai mươi năm** sau chiến dịch; văn bản Kinh Thánh nén thời gian.)

**Phía thứ ba — Herodotus II.141**: Sennacherib tiến đến Pelusium, chuột đồng cắn nát dây cung và tay cầm khiên của quân Assyria trong đêm, quân tan.

**Cách giới nghiên cứu xử lý** (theo Wikipedia "Sennacherib's campaign in the Levant"): (i) giả thuyết dịch bệnh trong trại Assyria — giải thích vì sao cả hai phía đều kết thúc đột ngột; (ii) tranh luận "halsu" là tường vây hay chỉ phong toả — nhiều người cho rằng chưa từng có cuộc vây thật sự ở Jerusalem; (iii) thực dụng chiến lược — Judah đã bị cắt đất và nộp cống, không cần đánh thành. Điểm chung của mọi cách đọc: **hai phía nhất trí ở chỗ Jerusalem không bị chiếm và Hezekiah có nộp cống**; khác nhau ở cách giải thích vì sao Sennacherib rút. Mục không chọn cách đọc nào.

---

## 7 · Phá huỷ Babylon 689 TCN — bi ký trình bày thế nào

Nguồn chính là **bi ký Bavian** (khắc trên vách đá ở Khinis, đầu kênh; RINAP 3/2 số 223) — cùng một văn bản vừa kể việc đào kênh ("I dug that canal with (only) seventy men and I named it Nār-Sennacherib", một năm ba tháng) vừa kể việc phá Babylon. Về Babylon, bi ký nói: phá thành và nhà cửa "from foundation to parapet", đốt; "tường và tường ngoài, đền và thần, tháp đền bằng gạch và đất... tôi san phẳng và đổ xuống kênh Arahtu"; đào kênh dẫn nước qua giữa thành, "làm tan nó hoàn toàn bằng nước và biến nó thành đất ngập"; mang tượng Marduk và của cải về Assyria. Wikipedia "Khinnis Reliefs" nhận xét đúng: cùng một bi ký ca ngợi khả năng **điều khiển nước** của vua theo hai chiều — tưới cho Assyria và nhấn chìm Babylon.

**Khung biện minh**: Sennacherib cho soạn một huyền thoại trong đó Marduk bị xét xử trước Aššur, và dùng ngôn ngữ *Enūma Eliš* để đồng nhất Babylon với Tiamat. Giới nghiên cứu (theo Wikipedia "Sennacherib", dẫn Frahm) đọc động cơ là trả thù việc con trai ông Aššur-nādin-šumi bị Elam bắt và giết (694) sau khi Babylon nổi dậy, cộng ý muốn chấm dứt chuỗi nổi loạn. Hệ quả: lòng căm ghét sâu ở Babylonia; biên niên sử miền nam gọi giai đoạn sau là "thời không vua"; **Esarhaddon đảo ngược chính sách và tái thiết Babylon**. Đó là lý do dòng "Esarhaddon · phản bác · trực tiếp".

---

## 8 · Giả thuyết Dalley về Vườn treo — chỉ ở ghi chú, không vào mục

**Giả thuyết**: Stephanie Dalley (Oxford, Shillito Fellow in Assyriology 1988–2007) đề xuất từ bài "Nineveh, Babylon and the Hanging Gardens: Cuneiform and Classical Sources Reconciled", *Iraq* 56 (1994), rồi sách *The Mystery of the Hanging Garden of Babylon: An Elusive World Wonder Traced* (Oxford University Press, 2013), rằng "Vườn treo Babylon" của các tác giả Hy Lạp–La Mã thực ra là vườn của **Sennacherib ở Nineveh**. Lý lẽ: bi ký của Sennacherib mô tả vườn "a wonder for all peoples" và thiết bị nâng nước kiểu trục vít; không có bi ký nào của Nebuchadnezzar nhắc vườn; Sennacherib đặt tên cổng thành theo tên thần, tức muốn Nineveh được coi là "một Babylon"; hệ kênh Khinis–Jerwan là nguồn nước; các tác giả cổ điển hay lẫn hai thành.

**Tiếp nhận**: chưa thành đồng thuận. Eckart Frahm, chuyên gia hàng đầu về Sennacherib, cho giả thuyết này "unlikely" vì chính Babylon cũng có vườn hoàng gia đồ sộ (theo Wikipedia "Sennacherib"). Bichler và Rollinger chỉ ra điểm yếu then chốt: không có bằng chứng nào nối vườn Assyria với các câu chuyện Hy Lạp (theo tóm tắt thứ cấp). Một bài điểm sách học thuật (academia.edu, không mở được) phê bình cách chọn lọc nguồn cổ điển. Điểm mọi bên đồng ý: **không có dấu vết khảo cổ của vườn ở cả Babylon lẫn Nineveh.** Vì vậy mục không nhắc Vườn treo; nếu Owner muốn, câu an toàn là "Dalley (2013) đặt giả thuyết Vườn treo 'Babylon' là vườn Nineveh của ông; giới chuyên môn chưa thuận" — nhưng sẽ phải cắt chỗ khác để giữ dưới 130 chữ.

---

## 9 · Về chữ "cổ nhất" — sắc thái cần giữ

N12 viết Jerwan là "công trình cùng loại cổ nhất được biết ở bất kỳ đâu". Dạng quy nguồn được là của ISAC: "a type of structure unknown elsewhere before Roman times" — tức khẳng định về *cái đã biết*, không phải *cái đã từng có*. Mục dùng đúng sắc thái đó ("kiểu công trình chưa thấy ở đâu trước thời La Mã"). Lưu ý thêm: "cầu máng" ở đây là cầu dẫn nước bằng đá vượt thung lũng, không phải toàn bộ hệ kênh; kênh dẫn nước thì Assyria đã có từ Ashurnasirpal II.
