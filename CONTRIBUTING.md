# Đóng góp cho history-atlas

Cảm ơn bạn đã quan tâm. Đây là dự án nghiên cứu cá nhân; đóng góp được hoan nghênh, nhưng nội dung phải qua được cổng lint tự động và tuân thủ chính sách giấy phép ảnh. Đọc phần **Bản chất và giới hạn của nội dung** trong `README.md` trước.

Mọi đóng góp được phát hành theo **MIT** (xem `LICENSE`). Gửi PR nghĩa là bạn đồng ý điều đó, và xác nhận phần bạn viết là của bạn — không chép từ nguồn có bản quyền.

## Phản hồi mà không cần viết code

Dạng đóng góp giá trị nhất, và cũng dễ nhất:

- **Chi tiết sai** — mở issue kèm **nguồn**. Phản hồi có nguồn sẽ được sửa; phản hồi chỉ là quan điểm sẽ được ghi nhận nhưng không làm đổi nội dung.
- **Nguồn không tồn tại hoặc không nói điều được dẫn.** Đây là lỗi đã biết của mô hình ngôn ngữ và là loại báo lỗi hữu ích nhất.
- **Một ứng viên xứng đáng bị bỏ sót.** Kèm lập luận theo bốn tiêu chí (a) phạm vi · (b) độ bền · (c) tính nguyên bản · (d) counterfactual, và nêu bạn muốn loại ai để lấy chỗ — mỗi nhóm trần 12 người.
- **Một mục nghiêng lệch** ở giai đoạn còn tranh luận. Xem nguyên tắc ở mục *Về những giai đoạn còn tranh luận* trên trang Overview.

## Môi trường

```bash
uv venv --python 3.12
uv pip install -r requirements.txt PyYAML Pillow
.venv/bin/python build.py --offline     # lint, không gọi mạng
.venv/bin/python build.py               # lint + đối chiếu Wikidata + sinh HTML
```

Không cần Node, không cần server. Mở `index.html` bằng `file://` là chạy.

## Quy tắc nội dung

Template và từ vựng cố định nằm ở `prompts/atlas-prompt.md` (§5) và `atlaslib/common.py`. Lint chặn build nếu sai, nên cứ chạy `build.py --offline` là biết.

**Lỗi chặn build:** thiếu trường bắt buộc · ID sai quy ước `CHxx-GROUP-nn` hoặc trùng · nhóm không thuộc chapter · lĩnh vực / vùng / câu hỏi lớn / loại quan hệ / mức bằng chứng / độ tin cậy ngoài từ vựng · quá 2 lĩnh vực hoặc 2 câu hỏi lớn · nhóm quá 12 người · năm mất trước năm sinh · liên kết tới chính mình · thiếu `## Ghi chú biên tập`.

**Từ vựng cố định** — muốn thêm giá trị mới thì sửa `atlaslib/common.py` **và** `prompts/atlas-prompt.md`; sửa một nơi thôi là các chapter sau sẽ sinh lỗi:

| Danh sách | Số lượng | Giới hạn mỗi người |
|---|---|---|
| `FIELDS` lĩnh vực | 16 | tối đa 2 |
| `REGIONS` vùng | 9 | 1 |
| `BIG_QUESTIONS` câu hỏi lớn | 4 | tối đa 2 |
| `RELATION_TYPES` loại quan hệ | 4 | — |
| `EVIDENCE_LEVELS` mức bằng chứng | 3 | — |
| `CONFIDENCE` độ tin cậy niên đại | 3 | 1 |

**Hai việc bắt buộc TRƯỚC khi viết** — bỏ qua là lint sẽ ngập cảnh báo:

1. **Tra Wikidata Q-ID bằng API**, đừng đoán. `wbgetentities` với `sites=enwiki&titles=...` trả về P569/P570/nhãn thật; viết trường `năm:` khớp dung sai (Cao ±5 năm, Trung bình ±25, Thấp bỏ qua đối chiếu).
2. **Kiểm URL nguồn tồn tại** trước khi trích. Nhiều slug Stanford Encyclopedia không có thật (`mozi` → thực tế là `mohism`; không hề có `thales`, `anaximander`, `herodotus`, `hippocrates`). Tồn tại chưa đủ — phải mở ra xem nó **có nói về nhân vật không**: Ch2 từng dẫn một bài SEP không nhắc tới Solon một chữ nào.
3. **Không ghi số chương / quyển / tập nếu chưa mở mục lục.** Kiểm toán 95 trích dẫn của phụ lục cho thấy 5/6 số chương Keith Taylor sai — và cả 5 lệch đúng +1. Hình dạng đó nghĩa là con số đã được sinh ra chứ không tra cứu. Một số chương sai khiến cả dòng Nguồn mất giá trị, nên thà bỏ số chương còn hơn ghi đoán.
4. **Khớp Wikidata không đồng nghĩa với đúng.** Lint chỉ bắt lỗi *lệch* Wikidata, hoàn toàn mù trước lỗi mà Wikidata *cùng mắc*: Jeremiah từng ghi mất 587 TCN — sai, ông sống qua biến cố đó và mất ở Ai Cập k. 570 — nhưng Wikidata cũng ghi −587 nên lint báo sạch. Với nhân vật cổ đại, năm sinh Wikidata nhiều khi là suy diễn không nguồn (Triệu Đà k. 230 TCN). Đối chiếu Wikidata là sàn, không phải trần.
5. **"Ứng viên cùng thời" phải thật sự cùng thời.** Đánh giá độc lập bắt 6 trường hợp: Tử Sản sinh sau khi Quản Trọng mất 64 năm; Lương Thế Vinh mất 5 năm trước khi Nguyễn Bỉnh Khiêm sinh; Khương Tăng Hội dịch kinh 21 năm sau khi Sĩ Nhiếp mất. Kiểm năm sinh–mất của cả hai bên trước khi viết đoạn so sánh.

**Quy ước trường `năm:`** — parser cần dạng đọc được, nhưng đừng bịa:

| Trường hợp | Viết |
|---|---|
| biết năm sinh–mất | `551–479 TCN` |
| vua không có năm sinh | `trị vì 745–727 TCN` |
| chỉ biết khoảng hoạt động | `hoạt động k. 750–700 TCN` |
| còn sống | `1926–nay` |

Tránh dạng `TK 6 TCN` — parser bỏ qua, nhân vật sẽ mất chỗ trên timeline.

**Khối minh bạch bắt buộc.** Mỗi chapter phải mở đầu `## Ghi chú biên tập` bằng khối "Cách chapter này được soạn" (nguyên văn ở cuối `prompts/atlas-prompt.md`). Build không kiểm tự động — đây là việc của người biên tập.

## Quy tắc ảnh

Đừng tự thêm file vào `assets/img/`. Ảnh do `fetch_images.py` tải về từ Wikimedia Commons theo P18 của Wikidata, và chính sách giấy phép là **cứng**:

| Commons | Xử lý |
|---|---|
| Public domain / CC0 | nhúng, vẫn ghi nguồn |
| CC BY / CC BY-SA | nhúng kèm tác giả + giấy phép có link + link tệp gốc + "đã thu nhỏ" |
| có `Restrictions`, hoặc **không xác minh được** `Restrictions` | **không nhúng** — chờ Owner quyết qua `content/images.yaml` |
| NC / ND / GFDL-only / không rõ | không nhúng, chỉ đặt link tham khảo |
| không có P18 | link tới Wikipedia (ưu tiên vi) hoặc Wikidata |

Muốn đổi ảnh thì dùng `content/images.yaml` (`overrides.<ID>.file` / `.caption` / `.skip`), đừng sửa `data/images.json` — file đó do script sinh ra.

**Khi đổi ID của một nhân vật** (chuyển nhóm, đánh số lại): phải xoá bản ghi cũ trong `data/images.json` và file `assets/img/<ID cũ>.*`. Script bỏ qua ID "đã có", nên người kế thừa ID cũ sẽ hiển thị chân dung của người trước — đã xảy ra một lần (Hezekiah nhận ảnh của Yajnavalkya sau khi Yajnavalkya chuyển từ BCE08-07 sang BCE07-07).

## Quy trình một chapter

Áp dụng cho mọi chapter từ Ch3 trở đi.

1. `build.py --groups N` để lấy danh sách nhóm.
2. Tra Q-ID và kiểm URL nguồn (xem trên).
3. Viết `content/chNN.md` theo template §5, mở đầu Ghi chú biên tập bằng khối minh bạch.
4. `build.py --offline` → sửa tới khi **0 lỗi**.
5. `build.py` (online) → sửa mọi cảnh báo lệch niên đại / lệch nhãn Wikidata.
6. `fetch_images.py CHNN` → đọc `reports/images-review.txt`, xử lý mục `[review]` và `[no-image]`.
7. `build.py` lần nữa để nhúng ảnh.
8. **Đánh giá độc lập — bắt buộc.** Một lượt rà soát do người (hoặc agent) **không viết chapter đó** thực hiện, đối chiếu ít nhất:
   - từng Q-ID có đúng nhân vật không (nhãn Wikidata so với tên);
   - từng nguồn có tồn tại không, và có nói điều được dẫn không;
   - mọi niên đại, số liệu, tên tác phẩm nêu trong phần văn xuôi;
   - mục "Vì sao chọn" có nêu đích danh ứng viên bị loại không, lập luận có đứng được không;
   - độ phủ lĩnh vực/vùng của từng nhóm;
   - thiên lệch vùng và thiên lệch quan điểm ở các giai đoạn tranh luận.

   Kết quả ghi vào `reports/review-chNN.md`. Sửa theo kết quả rồi mới commit. Lý do quy trình này tồn tại: phần văn xuôi do model viết, mà model thì tự tin kể cả khi sai — một lượt kiểm của bên thứ hai là lớp bảo vệ duy nhất có thật.
9. Commit. Cứ 3 chapter → ZIP checkpoint.

## Code

Theo phong cách sẵn có: không thêm thư viện, không framework, không CDN. Mọi trang phải mở được bằng `file://`. Comment viết tiếng Việt, giải thích **vì sao** chứ không phải **cái gì**.

HTML do `atlaslib/render.py` sinh bằng f-string — đừng sửa trực tiếp `index.html`, `overview.html`, `credits.html`, `chapters/*.html`, chúng bị ghi đè mỗi lần build.

Trước khi gửi PR: `build.py` chạy sạch (0 lỗi), và `git status` không còn file sinh ra chưa commit.
