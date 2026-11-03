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
uv sync --extra images                  # dựng .venv đúng theo uv.lock
uv run python build.py --offline        # lint, không gọi mạng
uv run python build.py                  # lint + đối chiếu Wikidata + sinh HTML
```

`uv sync` đọc `pyproject.toml` và `uv.lock`, nên môi trường tái lập được y hệt;
`.python-version` ghim CPython 3.12. Extra `images` chứa PyYAML và Pillow — code có
bắt `ImportError` và chạy tiếp mà không có chúng, nhưng bản dựng chuẩn 191 ảnh nhúng
thì cần, nên cứ cài kèm. `markdown` ghim **đúng** `3.10.3` vì đó là bản đã dựng ra
output đang nằm trong git; nâng nó là một quyết định riêng, phải dựng lại rồi soi diff.

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

**Chín điều bắt buộc TRƯỚC khi viết** — bỏ qua là lint sẽ ngập cảnh báo:

1. **Tra Wikidata Q-ID bằng API**, đừng đoán. `wbgetentities` với `sites=enwiki&titles=...` trả về P569/P570/nhãn thật; viết trường `năm:` khớp dung sai (Cao ±5 năm, Trung bình ±25, Thấp bỏ qua đối chiếu).
2. **Kiểm URL nguồn tồn tại** trước khi trích. Nhiều slug Stanford Encyclopedia không có thật (`mozi` → thực tế là `mohism`; không hề có `thales`, `anaximander`, `herodotus`, `hippocrates`). Tồn tại chưa đủ — phải mở ra xem nó **có nói về nhân vật không**: Ch2 từng dẫn một bài SEP không nhắc tới Solon một chữ nào.
3. **Không ghi số chương / quyển / tập nếu chưa mở mục lục.** Kiểm toán 95 trích dẫn của phụ lục cho thấy 5/6 số chương Keith Taylor sai — và cả 5 lệch đúng +1. Hình dạng đó nghĩa là con số đã được sinh ra chứ không tra cứu. Một số chương sai khiến cả dòng Nguồn mất giá trị, nên thà bỏ số chương còn hơn ghi đoán.
4. **Khớp Wikidata không đồng nghĩa với đúng.** Lint chỉ bắt lỗi *lệch* Wikidata, hoàn toàn mù trước lỗi mà Wikidata *cùng mắc*: Jeremiah từng ghi mất 587 TCN — sai, ông sống qua biến cố đó và mất ở Ai Cập k. 570 — nhưng Wikidata cũng ghi −587 nên lint báo sạch. Với nhân vật cổ đại, năm sinh Wikidata nhiều khi là suy diễn không nguồn (Triệu Đà k. 230 TCN). Đối chiếu Wikidata là sàn, không phải trần.
5. **"Ứng viên cùng thời" phải thật sự cùng thời.** Đánh giá độc lập bắt 6 trường hợp ở phụ lục và thêm 11 ở Ch3: Tử Sản sinh sau khi Quản Trọng mất 64 năm; Lương Thế Vinh mất 5 năm trước khi Nguyễn Bỉnh Khiêm sinh; Ban Siêu cách Trương Khiên 210 năm. Kiểm năm sinh–mất của cả hai bên trước khi viết đoạn so sánh. Nếu giai đoạn đó thật sự không có ai để so, **viết thẳng là không có** — đó là một phát hiện về tư liệu, không phải chỗ để mượn tạm một cái tên lệch thế kỷ.
6. **Đừng nêu làm "ứng viên bị loại" một người đã được chọn ở chỗ khác trong atlas.** Ch3 mắc 11 lần: mục Tần Thủy Hoàng nêu Lý Tư, mục Ashoka nêu Chandragupta, mục Cicero nêu Lucretius — tất cả đều có mục riêng. Câu văn khi đó tự mâu thuẫn: không có đánh đổi nào xảy ra. Nếu muốn nhắc để so sánh thì nói rõ *"có mục riêng ở nhóm X nên không phải ứng viên bị loại"*. Dò bằng script đối chiếu mọi tên trong "Vì sao chọn" với `data/persons.json` nhanh hơn dò tay, và bắt được cả những ca người rà bỏ sót. **Chạy lại phép dò ấy mỗi lần atlas thêm một nhóm, không chỉ một lần lúc chấm.** Đây là lỗi phát sinh theo thời gian: câu đúng lúc viết sẽ thành sai khi người được nêu có mục riêng ở một nhóm viết sau. `CH05-CE07-11` từng nêu Trisong Detsen làm ứng viên bị loại và chỉ sai sau khi nhóm CE08 cho ông `CH05-CE08-10`.
7. **Nguồn tồn tại, đúng chủ đề, vẫn có thể bị dùng ngược.** Ch3 dẫn Hansen, *The Silk Road: A New History* (2012) để đỡ cho câu về sự hình thành Con đường tơ lụa — trong khi luận điểm trung tâm của bà là lưu lượng tuyến ấy nhỏ hơn nhiều so với hình dung phổ biến. Loại lỗi này không URL nào bắt được: phải biết sách đó **lập luận gì**, không chỉ nó nói về cái gì. Tương tự, kiểm cả **thể loại**: Fried & Unguru (2001) bị ghi là "bản dịch Conics", thực tế là chuyên khảo.
8. **Lint mù trước liên kết trỏ đúng ID nhưng sai người.** Vòng đối xứng (thêm ở P2) chỉ báo được rằng liên kết một chiều, không báo được đích sai: Ch3 từng cho Tư Mã Thiên "ảnh hưởng tới" Đinh Bộ Lĩnh và Lưu Hướng "ảnh hưởng tới" Nguyễn Hoàng. **Mở mục đích ra đọc tên** trước khi commit. Lint có bắt nghịch niên đại, nhưng chỉ khi người tác động sinh sau khi người kia đã mất — nó không bắt được `trực tiếp` giữa hai người cách nhau 130 năm mà vẫn "đúng thứ tự".
9. **`trực tiếp` là mức bằng chứng chặt nhất, không phải mức mạnh nhất.** Trước khi viết `trực tiếp`, mở cả hai mục ra và cộng trừ năm: đời hai người phải chồng lấn, **và** phải có tiếp xúc nói được bằng nguồn. Không chồng đời thì viết `qua trường phái`. Đây là lỗi phổ biến nhất trong atlas hiện tại, không phải lỗi hiếm — xem khối "Quy ước mức bằng chứng" bên dưới để biết quy mô. Lint không đỡ được chỗ này (quy tắc 8).

**Quy ước trường `năm:`** — parser cần dạng đọc được, nhưng đừng bịa:

| Trường hợp | Viết |
|---|---|
| biết năm sinh–mất | `551–479 TCN` |
| vua không có năm sinh | `trị vì 745–727 TCN` |
| chỉ biết khoảng hoạt động | `hoạt động k. 750–700 TCN` |
| còn sống | `1926–nay` |

Tránh dạng `TK 6 TCN` — parser bỏ qua, nhân vật sẽ mất chỗ trên timeline.

**Quy ước trường `vùng:`** — quy tắc này trước nay **chưa từng được viết ra**, và cả hai vòng bình duyệt độc lập của Chapter 4 đều kết luận rằng con số "atlas chỉ có 1 người Trung Á" đo quy ước nhiều hơn đo lịch sử. Ghi thành văn:

1. **Mặc định là nơi hoạt động chính, không phải nơi sinh** — đúng thứ mà trường `nơi:` in ra. Plotinus sinh ở Lycopolis thuộc Ai Cập nhưng dạy ở Rome nên ghi Châu Âu; Diophantus làm việc ở Alexandria nên ghi Trung Đông/Bắc Phi. Hai mục này **không** mâu thuẫn, dù đọc theo nơi sinh thì trông như có.
2. **Ngoại lệ đã khai báo: các thành bang nói tiếng Hy Lạp ở Tiểu Á** (Miletus, Nicaea, Cos, Amaseia, Pergamon) ghi **Châu Âu**, vì chúng là bộ phận cấu thành thế giới Hy Lạp. Alexandria **không** theo ngoại lệ này; lý do đầy đủ nằm ở `## Ghi chú biên tập` của Chapter 3.
3. **`REGIONS` không có ô nào cho Nội Á / thế giới thảo nguyên.** Hệ quả: cao nguyên Mông Cổ ghi **Đông Á** (Mặc Đốn thiền vu, `CH03-BCE02-12`), còn "Trung Á" trên thực tế chỉ còn dùng cho vành đai Transoxiana–Iran đông. Thế giới du mục vì vậy **không tồn tại như một hạng mục** trong thống kê vùng, dù nó là một trong những lực định hình lịch sử Á–Âu. Mọi con số Trung Á phải đọc kèm giới hạn từ vựng này.
4. **Đừng đổi `vùng:` của một người để cải thiện thống kê.** Khi một vùng trống, chỉ có hai câu trả lời đúng: tìm người thật sự thuộc vùng đó, hoặc ghi vào Ghi chú biên tập rằng vùng ấy trống và vì sao. Vòng rà soát vùng đã **bác** đề xuất chuyển Kanishka từ Nam Á sang Trung Á đúng theo điều này — kinh đô Purushapura nằm ở Nam Á, nên đổi nhãn chỉ phá quy tắc 1 để lấy một con số đẹp hơn.

**Quy ước mức bằng chứng** — như quy ước `vùng:` ở trên, điều này trước nay **chưa từng được viết ra**. `trực tiếp` chỉ tồn tại như một giá trị enum ở `prompts/atlas-prompt.md` §5 và trong `EVIDENCE_LEVELS`; không chỗ nào nói nó nghĩa là gì. Đo trên mạch chính (245 người, không tính phụ lục): **346 trên 928 quan hệ, tức 37,3%, đang mang nhãn này**. Một từ không định nghĩa đang gánh hơn một phần ba mạng lưới.

Định nghĩa, từ nay:

1. **`trực tiếp`** — tiếp xúc người với người, chứng minh được bằng nguồn: thầy–trò, đồng sự, thư từ qua lại, cùng ngồi một hội đồng hay một triều đình. **Điều kiện cần: đời hai người chồng lấn.** Hai người không cùng sống thì không có tiếp xúc nào để chứng minh, ảnh hưởng mạnh tới đâu cũng vậy.
2. **`qua trường phái`** — truyền qua văn bản, bản dịch, học phái, định chế, dòng tu, trường luật. Đây là mức **mặc định** cho mọi cặp không chồng đời, và cho mọi quan hệ mà đích không phải một con người (một chế độ, một bộ kinh, một truyền thống).
3. **`suy đoán học giả`** — không có đường truyền chứng minh được; mối liên hệ là giả thuyết của giới nghiên cứu, và nên nói rõ giả thuyết của ai.

Vì sao chọn cách đọc chặt: ba mức này đo **đường truyền**, nên mức đầu phải là đường ngắn nhất. Đọc rộng thì `trực tiếp` chỉ còn nghĩa "ảnh hưởng rõ ràng" — mà điều đó đã nằm sẵn ở `kế thừa`, và từ ấy thôi mang thông tin.

**Hiện trạng cần dọn**, đo lúc viết điều này. Trong 346 quan hệ `trực tiếp`: **183 có đích là văn bản tự do** chứ không phải một mục trong atlas, phần lớn thuộc nhóm 2 theo định nghĩa trên. Trong 163 quan hệ đích-là-ID còn lại, **50 cặp không chồng đời** — xa nhất `CH05-CE09-02 → CH02-BCE06-03` cách **1251 năm**, rồi `CH05-CE09-02 → CH03-BCE04-04` cách 1057 năm và `CH04-CE03-10 → CH02-BCE06-02` cách 716 năm. Lint mù trước cả nhóm này: nó chỉ báo nghịch niên đại khi người tác động sinh sau khi người kia đã mất, nên một `trực tiếp` "đúng thứ tự" mà cách nhau mười thế kỷ vẫn qua sạch.

**Không thêm mức thứ tư.** Phương án tách nghĩa bằng một mức `qua văn bản` mới đã được cân nhắc và gác lại: đổi `EVIDENCE_LEVELS` trong `atlaslib/common.py` kéo theo lint, thống kê và cả sáu chapter cùng lúc. Việc ấy chỉ đáng làm **sau** khi đã có định nghĩa, không phải thay cho nó.

**Quy ước tiêu chí (a) phạm vi** — đo **trong mạng lưới tiếp xúc tồn tại ở thời điểm ấy**, không đo trên bản đồ thế giới hiện đại.

Không có câu này, tiêu chí (a) loại trừ châu Mỹ tiền Columbus **theo cấu trúc chứ không theo công trạng**: mục `CH05-CE07-12` Pakal đã tự ghi ra điều đó — *"trước 1492 không tồn tại đường vật lý nào để ảnh hưởng ra khỏi bán cầu"*. Hệ quả là mọi suất châu Mỹ, và phần lớn suất châu Phi hạ Sahara, hoặc thua (a) một cách máy móc, hoặc phải được chọn bằng một chính sách ngầm rằng "không được để vùng ấy trống". Một chính sách ngầm thì không phân biệt được với lấp chỉ tiêu — đó là kết luận §E-2 của `reviews/ch05-ce08-review.md`.

Viết ra rồi thì Yikʼin Chan Kʼawiil (`CH05-CE08-12`) đứng được bằng chính tiêu chí (a): ông là thế lực mạnh nhất trong mạng lưới của ông. Quy ước này **không** hạ chuẩn — nó vẫn đòi người ấy phải trội trong mạng lưới của mình, và vẫn không cho phép đổi `vùng:` của ai để làm đẹp thống kê (quy ước `vùng:` điều 4).

**Quy ước hệ quy chiếu và liên kết giữa mạch chính với phụ lục** — `content/ch90.md` tồn tại vì ảnh hưởng của nhân vật Việt Nam được đo trong phạm vi Việt Nam / Đông Nam Á, không phải toàn nhân loại (`README.md`). Ba hệ quả chưa từng được viết ra:

1. **Bốn tiêu chí (a)–(d) được chấm trong hệ quy chiếu của track đang xét.** Cùng một tiêu chí cho hai kết quả khác nhau ở hai track **không phải mâu thuẫn**, nhưng mục nào rơi vào tình huống đó thì **phải nói ra hệ quy chiếu**, nếu không người đọc chỉ thấy hai file xếp hạng ngược nhau. Ca đang có: `CH05-CE10-05` Khúc Thừa Dụ và `CH90-CE10_14-01` Ngô Quyền.
2. **Một nhân vật Việt Nam đạt thang đo toàn cầu thì ở mạch chính, và vẫn được phụ lục nhắc tới.** Hai track không loại trừ nhau; lint cố tình chỉ báo `INFO` khi trùng tên hoặc trùng Wikidata giữa hai bên. Khi điều đó xảy ra, phụ lục dùng đúng câu của quy tắc 6: *"có mục riêng ở `CHxx-…` nên không phải ứng viên bị loại"*.
3. **Liên kết mạch chính → phụ lục dùng ID; liên kết phụ lục → mạch chính giữ nguyên văn bản tự do.** Tiền lệ chiều thuận: `CH05-CE08-09 → CH90-CE19_20-01`. Chiều ngược **cố ý không nâng** (`ch90.md:148` vẫn ghi `- Khúc Thừa Dụ · kế thừa · qua trường phái` dù ông đã có `CH05-CE10-05`): một cạnh có ID ở chiều ngược sẽ kéo phụ lục vào mạng lưới mà `render.py` cố tình cô lập khỏi thống kê toàn cục. Muốn đổi điều này thì phải sửa `render.py` trước, không sửa file nội dung trước.

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

   Kết quả ghi vào `reviews/review-chNN.md`. Sửa theo kết quả rồi mới commit. Lý do quy trình này tồn tại: phần văn xuôi do model viết, mà model thì tự tin kể cả khi sai — một lượt kiểm của bên thứ hai là lớp bảo vệ duy nhất có thật.
9. Commit. Cứ 3 chapter → ZIP checkpoint.

## Code

Theo phong cách sẵn có: không thêm thư viện, không framework, không CDN. Mọi trang phải mở được bằng `file://`. Comment viết tiếng Việt, giải thích **vì sao** chứ không phải **cái gì**.

HTML do `atlaslib/render.py` sinh bằng f-string — đừng sửa trực tiếp `index.html`, `overview.html`, `credits.html`, `chapters/*.html`, chúng bị ghi đè mỗi lần build.

Trước khi gửi PR: `build.py` chạy sạch (0 lỗi), và `git status` không còn file sinh ra chưa commit.
