# CE10 — kiểm Wikidata trước vòng chọn (801–900 → 901–1000)

Kiểm độc lập bằng `wd-qids.py` / `wd-titles.py`, User-Agent trung tính, ngày 2026-10-31.
Mục đích: **phát hiện bẫy trước khi viết**, theo đúng bài học của CE08 và CE09 — Wikidata khai
độ chính xác chứ không khai độ tin cậy, và đôi khi khai cả thứ hạng sai (ca `Q493856`).

Toàn bộ 14 ứng viên dưới đây đã xác nhận `P31 = ['Q5']`. Không ai là thực thể tập thể hay sự kiện.

## 1. Bẫy niên đại phải xử trước khi viết

| QID | Người | Wikidata | Vấn đề |
|---|---|---|---|
| `Q169234` | Abu Bakr al-Rāzī | b = **866, 854, 854, 864, 865** (5 giá trị, đều p9); d = 925 | Biên độ sinh **12 năm**. Không được ghi `độ tin cậy niên đại: Cao`. Viết `k. 854–925`, mức `Trung bình`. |
| `Q1292812` | Vācaspati Miśra | b = 900, d = 980, cả hai p9 | **Wikidata đang khai độ chính xác giả.** Học thuật để niên đại ông dao động khoảng **841–976**, biên độ ~135 năm, tuỳ đọc niên hiệu trong *Nyāyasūcīnibandha* là Vikrama hay Śaka. Nếu dùng, phải ghi `hoạt động` + `Thấp`, tuyệt đối không chép 900–980. |
| `Q192124` | al-Ṭabarī | d = **922** (p9) | Học thuật chuẩn ghi **923** (26 Shawwāl 310 AH). Chênh một năm, dạng sai quy đổi AH→CE. Phải kiểm lại trước khi ghi. |
| `Q316349` | al-Ashʿarī | b = 873, d = 935 | Học thuật thường ghi **874–936**. Lệch một năm ở **cả hai đầu** — dấu hiệu điển hình của quy đổi AH→CE bằng công thức thay vì tra lịch. Phải kiểm. |
| `Q172383` | Gerbert / Silvestrô II | b = **938** (p9) | Học thuật phổ biến để **k. 945–950**. Con số 938 ở p9 là một khẳng định mạnh hơn nguồn cho phép. |
| `Q170248` | Hrotsvitha | b = 935, d = **968** | Bà còn viết sau **973** (*Primordia coenobii Gandeshemensis*). Năm mất 968 ở p9 nhiều khả năng sai. Nếu dùng, viết `hoạt động k. 960–975`. |

## 2. Ca không có niên đại sinh — phải dùng `trị vì` / `hoạt động`

- `Q47684` **Mpu Sindok**: `b` trống, `d = 947`. Viết `trị vì k. 929–947 CN`, mức `Thấp`.
  Lưu ý: `NON_BIO_YEARS_RE` chỉ nhận trường `năm:` **mở đầu** bằng "trị vì" hoặc "hoạt động";
  viết sai thứ tự sẽ kích hoạt đối chiếu sinh/mất của Wikidata.
- `Q1270024` **Gudit**: `b = +0950 ở precision 7` — tức **giá trị độn "thế kỷ 10"**, không phải năm sinh 950;
  `d` trống hoàn toàn. Cùng dạng bẫy với `Q1001807` ở mục 3. Cộng thêm việc bà phần lớn là
  nhân vật truyền thống. **Khuyến nghị: không dùng cho atlas chính.**

## 3. Xác nhận lại cảnh báo đã ghi trong ghi chú CE09

`Q1001807` **Khúc Thừa Dụ**: `b = +0801-01-01 ở precision 7`, `d = +0907 ở p9`.
Kiểm lại lần này **khớp đúng** cảnh báo đã công bố trong ghi chú biên tập CE09: 801 là
giá trị độn thế kỷ, không phải năm sinh. Người viết CE10 ghi `hoạt động 905–907 CN`.

## 4. Ứng viên không tìm được thực thể

`Topiltzin Quetzalcoatl`, `Ibn Fadlan`, `Abu al-Wafa' Buzjani`, `al-Muqaddasi` không
resolve được bằng tiêu đề Wikipedia tiếng Anh đã thử. Chưa kết luận là không có —
phải tra lại bằng dạng tên khác trước khi loại. **[CHƯA KẾT LUẬN]**

## 5. Ứng viên sạch (không phát hiện bẫy ở vòng này)

`Q328748` Saadia Gaon (882-07 → 16-05-942) · `Q862648` Ismail Samani (06-849 → 24-11-907) ·
`Q468288` Ki no Tsurayuki (866/872 → 30-06-945, hai năm sinh, biên độ 6 năm) ·
`Q2128757` Rajaraja I (947–1014) · `Q4989` Liêu Thái Tổ / Abaoji (872 → 06-09-926) ·
`Q190418` ʿAbd al-Raḥmān III (07-01-891 → 15-10-961) · `Q160460` al-Fārābī (ba năm sinh: 872 p11, 870, 872 → 951) ·
`Q168705` al-Masʿūdī (896 → 957) · `Q334312` Cao Ly Thái Tổ / Wang Geon (31-01-877 → 04-07-943) ·
`Q182498` Ḥasdai ibn Shaprut (915–975) · `Q720129` Dunash ben Labrat (920 p9 và p8 → 990) ·
`Q231603` Sei Shōnagon (966–1025) · `Q320619` Abhinavagupta (950–1020).

"Sạch" ở đây chỉ nghĩa là **Wikidata không tự mâu thuẫn**. Nó không thay cho việc kiểm nguồn học thuật.

## 6. Kiểm quy tắc 6 cho pool CE10 — và ba liên kết tự do sẽ phải nâng cấp

Rà 25 dạng tên của pool trong toàn bộ `content/`. **Không ai vi phạm quy tắc 6** — không
ứng viên CE10 nào đang bị nêu tên như "ứng viên bị loại" ở chỗ khác. Nhưng việc rà làm lộ ra
ba chỗ thuộc đúng cái bẫy bảo trì mà ghi chú CE09 vừa công bố:

1. **Abhinavagupta** đã được nêu hai lần trong `CH05-CE09-11 · Ānandavardhana`: một lần trong
   "Vì sao chọn" như chứng cứ tiêu chí (d), và một lần ở `Ảnh hưởng tới:` dưới dạng **văn bản tự do**
   — `- Abhinavagupta và bình chú Locana · kế thừa · trực tiếp`. Niên đại của ông (k. 950–1016,
   `Q320619` ghi 950–1020) đặt ảnh hưởng chính ở **quanh năm 1000**, tức CE11 chứ không phải CE10.
   Khi ông có mục riêng, dòng ấy **phải** đổi thành ID.
2. **Vācaspati Miśra** được nêu hai lần như mỏ neo niên đại cho Śaṅkara — trong "Vì sao chọn"
   của mục Śaṅkara và trong một khối ghi chú biên tập. Cùng tình trạng: không vi phạm quy tắc 6,
   nhưng là một đích sẽ phải nâng cấp nếu ông vào atlas.
3. **al-Ṭabarī** xuất hiện **ba lần, chỉ với tư cách nguồn** (`Ṭabarī, Tārīkh`, các quyển V, XII–XIV,
   XVI–XVII, bản dịch SUNY). Đây là một ca đáng chú ý theo chiều ngược: atlas đã dựa vào công trình
   của ông để viết ba mục thế kỷ 6–7 **trước khi** xét ông như một nhân vật. Nếu ông vào CE10,
   mục của ông nên nói thẳng điều đó — nó là bằng chứng tiêu chí (d) có sẵn ngay trong chính atlas.

Ba ca này xác nhận quy trình mà ghi chú CE09 đề ra là cần thật: **mỗi vòng thêm nhóm mới, phải
`grep` tên người vừa thêm trong toàn bộ `content/` để tìm đích tự do cần nâng cấp.** Lint không
nhắc được việc này.
