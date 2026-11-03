# Thẩm định vòng 2 · content/ch90.md

> Người thẩm định độc lập vòng 2: không viết chapter, không viết bản vá vòng 1.
> Ngày kiểm: 2026-10-31. Chỉ sửa đúng file này.
> Trọng tâm theo brief: (1) hồi quy sau 78 bản vá, (2) liên kết chéo, (3) ghi chú biên tập lỗi thời, (4) trung lập sau sửa, (5) gỡ các mục kiểm toán ghi KHÔNG KIỂM ĐƯỢC.

**Kết luận: ⚠️ Chưa in được — cần một vòng vá nhỏ, nhưng KHÔNG cần làm lại.**

Phần lớn 78 bản vá là **đúng và cải thiện thật**. Tôi tra lại tận nguồn mười hai chỗ sửa khó nhất và mười một chỗ đứng vững (xem *Đã kiểm, đúng*). Vấn đề nằm ở ba chỗ, đúng như brief dự đoán:

1. **Các trường do biên tập viên tự viết, không qua bản vá JSON, là nơi lỗi mới tập trung** — 3/3 chỗ tôi kiểm sâu trong nhóm BCE03_01 đều có vấn đề (H2 sai niên đại ĐVSKTT, H3 sai nơi tìm được khuôn đúc Cổ Loa).
2. **Một "xác minh dương tính giả" của vòng 1** khiến một lỗi Sai đã được báo đúng lại không được vá (H1).
3. **Liên kết chéo và ghi chú biên tập** — đúng chỗ brief cảnh báo. Một liên kết trỏ nhầm số mục mà lint **không thể thấy** (L1), một nhãn quan hệ tự mâu thuẫn chưa sửa (L2), và bốn chỗ trong *Ghi chú biên tập* đã lỗi thời so với chính các mục vừa sửa (G1–G4).

**Thống kê phát hiện vòng 2**

| Mức | Số |
|---|---|
| **Sai** (hồi quy hoặc Sai vòng 1 chưa vá) | **6** — H1, H2, H4, H5, L1, L2 |
| **Đáng ngờ** | **4** — H3, H6, H9, H10 |
| **Nên sửa** | **9** — H7, H8, L3, L4, L5, L6, G5, G6, G7 |
| **Ghi chú biên tập lỗi thời** | **4** — G1, G2, G3, G4 |

**Ba hạng mục nghiêm trọng nhất**

1. **L1** — `CH90-CE01_09-01` Trưng Trắc ghi "Ảnh hưởng tới: **CH90-CE01_09-04**" (Tì-ni-đa-lưu-chi, tăng sĩ Nam Ấn, hoạt động 580). Gần như chắc chắn là lỗi gõ `-04` thay cho `-05` (Lý Nam Đế), vì Lý Nam Đế **đang ghi Trưng Trắc trong "Kế thừa từ"** mà không có chiều ngược lại. Lint **không bắt được** vì nó chỉ kiểm chiều `Kế thừa từ`.
2. **H1** — con số "sáu mươi lăm thành" vẫn được gắn với *Hậu Hán thư, Mã Viện truyện*, nơi nguyên văn là 六十餘城. Vòng 1 đã báo đúng ở `review-ch90.md` (S8) nhưng `review-ch90-CE01_09.md` lại "xác minh" ngược bằng cách dán nguyên văn quyển 86 vào tên quyển 24 — và bản vá đã nghe báo cáo sai.
3. **H2** — trường `năm` của Triệu Đà, viết tay, ghi "ĐVSKTT: 207–136 TCN". ĐVSKTT chép 甲午元年 → 甲辰七十一年, tức **207–137 TCN**. Không có biến thể 136 nào, và nhãn "ĐVSKTT" còn bị dán vào nhầm vế.

**Trung lập:** tự mô tả của file về giai đoạn 1954–1975 nay **chính xác** — tôi kiểm lại từng tên trong danh sách bị loại và xác nhận không có nhân vật Việt Nam Cộng hoà nào, Trần Trọng Kim và Ngô Đình Diệm không xuất hiện ở bất kỳ đâu, Đổi mới 1986 chỉ có trong Bối cảnh. `atlaslib/render.py:475` khớp với ghi chú. Nhưng file **im lặng** về một bất đối xứng khác mà vòng 1 đã nêu (TL3) và vẫn còn nguyên — xem mục *Trung lập*.

---

## Hồi quy

### H1 · CH90-CE01_09-01 Trưng Trắc — lỗi S8 **chưa được sửa**, và vòng 1 đã "xác minh" ngược
**Mức: Sai.**

> "…khởi binh năm 40 chống thái thú Tô Định, **chiếm được sáu mươi lăm thành** và xưng vương ở Mê Linh…"
> "**Nguồn:** Keith W. Taylor, The Birth of Vietnam (1983), chương 1; **Hậu Hán thư, Mã Viện truyện**."

**Sai ở đâu:** Con số 65 **không** nằm trong Mã Viện truyện. Tôi tra trực tiếp hai thiên:

- *Hậu Hán thư* **quyển 24 · Mã Viện truyện**: 「**寇略嶺外六十餘城**」 — "hơn sáu mươi thành", không có con số 65.
- *Hậu Hán thư* **quyển 86 · Nam Man Tây Nam Di liệt truyện**: 「交阯女子徵側及其妹徵貳反，攻郡。徵側者，麊泠縣雒將之女也…交阯太守蘇定以法繩之，側忿，故反。於是九眞、日南、合浦蠻里皆應之，**凡略六十五城**，自立爲王。」 — đây mới là chỗ chép 65, và cũng là chỗ chép đủ các chi tiết tiểu sử mà mục này dùng (con Lạc tướng Mê Linh, Tô Định "lấy pháp luật ràng buộc").

**Vì sao chỗ này lọt lưới:** `reports/review-ch90.md` (S8) đã nêu đúng, nhưng `reports/review-ch90-CE01_09.md` mục "ĐÃ KIỂM, ĐÚNG" lại ghi ngược — *"**'sáu mươi lăm thành'** ✓ — Hậu Hán thư, Mã Viện truyện: 凡略六十五城，自立為王"* — tức dán nguyên văn của **quyển 86** vào tên thiên **quyển 24**. Hai báo cáo vòng 1 mâu thuẫn nhau, và bản vá đã theo báo cáo sai. Đây là một "xác minh dương tính giả", nguy hiểm hơn một lỗi chưa ai thấy.

**Sửa thế nào (chọn một):**
- giữ "sáu mươi lăm thành" → đổi Nguồn thành "Hậu Hán thư, **Nam Man Tây Nam Di liệt truyện (quyển 86)**"; hoặc
- giữ Mã Viện truyện → đổi số thành "**hơn sáu mươi thành**".

**Bằng chứng:** zh.wikisource.org/wiki/後漢書/卷24 ; zh.wikisource.org/wiki/後漢書/卷86 (tra trực tiếp 31/10/2026).

---

### H2 · CH90-BCE03_01-02 Triệu Đà — trường `năm` mới viết tay ghi sai chính ĐVSKTT
**Mức: Sai.** Đây là một trong các trường do biên tập viên tự viết, không qua bản vá JSON.

> `năm: trị vì 207–137 TCN (**ĐVSKTT: 207–136 TCN**; năm sinh không rõ)`

**Sai ở đâu:** ĐVSKTT **không** chép 136. *Đại Việt sử ký toàn thư, Ngoại kỷ quyển 2, Kỷ nhà Triệu*, Vũ Đế: 「在位七十一年，壽一百二十一歲」, niên biểu mở bằng **甲午元年** và đóng bằng **甲辰七十一年**. Quy đổi can chi: 甲午 = **207 TCN**, 甲辰 = **137 TCN** (甲午 +70 năm; 甲午 là vị trí 31, 甲辰 là vị trí 41 trong lục thập hoa giáp). Tức ĐVSKTT cho **207–137 TCN**, đúng bằng con số đặt ở vế chính — không có biến thể 136 nào.

**Hệ quả thứ hai, nặng hơn:** cấu trúc "X (ĐVSKTT: Y)" ngụ ý vế chính là niên đại **sử học hiện đại** và vế trong ngoặc là niên đại **ĐVSKTT**. Thực tế ngược: **207** mới là mốc của ĐVSKTT (theo lập trường Lê Văn Hưu lấy 207 TCN làm khởi điểm quốc thống), còn sử học hiện đại dựa vào *Sử ký* – *Hán thư* đặt việc lập Nam Việt vào khoảng **204 TCN** (vi.wikipedia ghi dải "208 hoặc 205 hoặc 204 – 137 TCN"). Chỉ **năm mất 137 TCN** là nơi mọi nguồn đồng thuận. Trường hiện tại vừa sai một con số vừa dán nhãn ngược cho con số còn lại.

**Sửa thế nào:** `năm: trị vì k. 204–137 TCN (ĐVSKTT: 207–137 TCN, "ở ngôi 71 năm"; năm sinh không rõ)` — hoặc bỏ hẳn vế ngoặc nếu không muốn mở tranh luận mốc đầu, nhưng **phải bỏ con số 136**.

**Lưu ý nhất quán:** phần văn xuôi viết "cai trị **bảy mươi năm**" — đúng theo số năm trôi qua (207→137), trong khi ĐVSKTT đếm gộp là 71 năm. Không sai, nhưng nếu trường `năm` sửa theo hướng trên thì nên đồng bộ cách đếm.

**Bằng chứng:** zh.wikisource.org — ĐVSKTT, Ngoại kỷ quyển 2 (tra trực tiếp); vi.wikipedia.org/wiki/Triệu_Vũ_Vương ("Năm mất của Triệu Đà được các nguồn sử liệu thống nhất là 137 TCN").

---

### H3 · CH90-BCE03_01-01 An Dương Vương — câu Cổ Loa mới viết: khuôn đúc **không** ở Cầu Vực
**Mức: Đáng ngờ, nghiêng về Sai.**

> "Khảo cổ xác nhận toà thành ba vòng dời hơn hai triệu mét khối đất, **kho một vạn mũi tên đồng và khuôn đúc tại chỗ ở Cầu Vực** (Kim, Lai và Trinh, 2010)"

**Vấn đề:** Câu gộp hai phát hiện ở **hai địa điểm khác nhau** rồi đặt chung một định ngữ nơi chốn:
- **Cầu Vực** (ngoài cửa nam thành, phát hiện **tháng 6/1959** khi làm đường): hố vuông ~1 m, sâu ~1,2 m, chứa **93 kg** mũi tên đồng, ước gần **một vạn** chiếc. ✓ đúng với "kho một vạn mũi tên đồng".
- **Khuôn đúc**: bộ sưu tập **11 khuôn đá sa thạch** (10 khuôn mũi tên ba cạnh + 1 khuôn mũi giáo cánh én), cùng dấu vết **lò đúc**, khai quật ở **Đền Thượng** — khu tây nam Thành Nội — trong các mùa **2004–2007**, nay là Bảo vật quốc gia. Không phải ở Cầu Vực, và muộn hơn phát hiện Cầu Vực gần nửa thế kỷ.

Cụm "**tại chỗ ở Cầu Vực**" vì thế gán sai nơi tìm được khuôn đúc, đồng thời làm mất đi chính luận điểm mạnh hơn: xưởng đúc nằm **bên trong** Thành Nội, tức sản xuất vũ khí được tổ chức ngay trong trung tâm quyền lực — bằng chứng về nhà nước còn rõ hơn một kho chôn ngoài thành.

**Sửa thế nào:** "…kho gần một vạn mũi tên đồng ở Cầu Vực và khuôn đúc cùng lò đúc tại Đền Thượng trong Thành Nội".

**Mức tin cậy của phát hiện này:** tôi **không đọc được toàn văn** Kim, Lai & Trịnh 2010 (os.pennds.org từ chối kết nối, Cambridge Core trả 429, bản ResearchGate/Academia cần đăng nhập). Một bản tóm lược thứ cấp có nhắc tới khuôn đúc ở khu Cầu Vực, nên không loại trừ bài báo có nói tới cả hai. Nhưng các nguồn Việt Nam chuyên trách (thanhcoloa.vn — ban quản lý di tích; kinhtedothi.vn về hồ sơ Bảo vật quốc gia) đều quy bộ khuôn về **Đền Thượng 2004–2007**. Cần đối chiếu trang in trước khi coi là đã khép.

**Đã kiểm và ĐÚNG trong cùng câu:** "hơn hai triệu mét khối đất" ✓ ("over two million cubic metres of material were moved"); trích dẫn **Antiquity 84 (2010)** ✓ — chính xác là Antiquity **84 (326), 12/2010, tr. 1011–1027**, ba tác giả đúng tên và đúng thứ tự. Mệnh đề "lớp luỹ sớm nhất có thể có trước niên đại truyền thống của ông" ✓ — luỹ trong được định niên 400–350 TCN, sớm hơn mốc 257 TCN của ĐVSKTT.

**Nhặt sạn:** văn xuôi ghi "Kim, Lai và **Trinh**, 2010" (không dấu) trong khi dòng Nguồn ghi "**Trịnh** Hoàng Hiệp". Nên thống nhất một lối.

---

### H4 · CH90-CE19_20-04 Trương Vĩnh Ký — bản vá **nhân đôi** một lỗi chức danh thay vì sửa nó
**Mức: Sai. Hồi quy rõ nhất trong cả file.**

> "…ông làm **chủ bút** Gia Định báo từ 1869, tờ báo chữ Quốc ngữ đầu tiên…"
> "**Nguồn:** Gia Định báo (1865–1909), giai đoạn ông làm **chủ bút** 1869–k. 1872; …"

**Sai ở đâu:** Theo nghị định được Đô đốc Ohier duyệt ngày **16/9/1869**, Trương Vĩnh Ký giữ chức **chánh tổng tài** (*rédacteur en chef*, tương đương giám đốc); **"chủ bút" là chức của Huỳnh Tịnh Của** — chính là người được nêu làm ứng viên bị loại **trong cùng mục này** ("Ứng viên cùng vai trò là Huỳnh Tịnh Của").

**Vì sao đây là hồi quy chứ chỉ là lỗi tồn đọng:** vòng 1 đã nêu chính xác (N15) cả hai nửa — sai chức danh **và** sai khoảng năm của tờ báo. Bản vá chỉ áp nửa sau (1869–1897 → 1865–1909, đúng) và khi viết lại dòng Nguồn đã **chép thêm chữ "chủ bút" vào đó**. Trước khi vá, lỗi chỉ ở một chỗ (văn xuôi); sau khi vá, nó ở hai chỗ.

**Sửa thế nào:** văn xuôi → "…ông được bổ làm **chánh tổng tài** (giám đốc) Gia Định báo từ 1869, với **Huỳnh Tịnh Của làm chủ bút**…"; Nguồn → "…giai đoạn ông làm **chánh tổng tài** 1869–k. 1872". Sửa xong thì đoạn "Vì sao chọn" còn mạnh lên: hai người cùng một toà soạn, không chỉ "cùng vai trò".

**Bằng chứng:** vi.wikipedia.org/wiki/Gia_Định_báo — tra trực tiếp: "Trương Vĩnh Ký" làm *chánh tổng tài*, "Huỳnh Tịnh Của" làm *chủ bút*; số đầu 15/4/1865, đình bản 1897 theo một dòng tư liệu và 31/12/1909 theo khảo cứu Lê Nguyễn (khoảng "1865–1909" trong file là chấp nhận được).

---

### H5 · Hai chỗ bản vá mới đưa chữ "**đương thời**" vào sai — CH90-CE01_09-01 và CH90-CE01_09-07
**Mức: Sai.** Cùng một kiểu lỗi, ở hai câu đều do bản vá vòng 1 viết mới.

> Trưng Trắc: "Đây là cuộc nổi dậy có tổ chức sớm nhất chống ách đô hộ phương Bắc được **Hậu Hán thư đương thời** chép; phía Việt, bản chép sớm nhất còn lại là Toàn thư thế kỷ 15."
> Phùng Hưng: "**sử Đường đương thời** chỉ chép thủ lĩnh Đỗ Anh Hàn, không nhắc tên ông."

**Sai ở đâu:** Không bộ nào trong hai bộ là *đương thời*.
- *Hậu Hán thư* do **Phạm Diệp (398–445)** soạn đời Lưu Tống, hoàn thành trước khi ông mất năm **445** — tức sau khởi nghĩa Hai Bà Trưng (40–43) **khoảng bốn trăm năm**, và không phải sử của chính triều Hán.
- Các bộ chép Đỗ Anh Hàn là **Cựu Đường thư (945)**, **Tân Đường thư (1060)** và **Tư trị thông giám (k. 1084)** — đều là biên soạn hậu Đường, cách sự kiện 791 từ 150 tới gần 300 năm.

**Vì sao nó quan trọng chứ không phải bắt bẻ chữ:** cả hai câu được viết ra để **so sánh độ gần của chứng cứ** ("đương thời" vs "Toàn thư thế kỷ 15"). Luận điểm đúng và đáng giữ — nguồn Hán vẫn sớm hơn nguồn Việt rất nhiều — nhưng nó đang được chống bằng một tính từ sai. Nếu người đọc kiểm, mệnh đề sụp, và kéo theo cả so sánh.

**Sửa thế nào:** Trưng Trắc → "…được *Hậu Hán thư* (TK 5) chép, sớm hơn bản chép Việt sớm nhất còn lại là Toàn thư TK 15 tới một nghìn năm"; Phùng Hưng → "…**sử Đường** chỉ chép thủ lĩnh Đỗ Anh Hàn…" (bỏ "đương thời").

**Bằng chứng:** niên đại Phạm Diệp và *Hậu Hán thư*; vi.wikipedia.org/wiki/Bố_Cái_Đại_Vương và en.wikipedia.org/wiki/Đỗ_Anh_Hàn — "the Old Book of Tang (945), New Book of Tang (1054) and Comprehensive Mirror (c. 1084) do not mention Phùng Hưng but only a local chief named Đỗ Anh Hàn".

**Phần còn lại của hai câu thì ĐÚNG và là bản vá tốt:** Tân/Cựu Đường thư quả thật không nhắc tên Phùng Hưng ✓; nhà Đường thu hồi An Nam năm **791** ✓; niên hiệu **Đại Lịch = 766–779** ✓; trường `năm: hoạt động k. 766–791` nay bao đúng cả hai cách dựng (Việt điện u linh từ Đại Lịch, Toàn thư dồn vào 791) ✓.

---

### H6 · CH90-CE15_18-04 Nguyễn Bỉnh Khiêm — bản vá thay một lỗi bằng một truyền thống đang tranh luận
**Mức: Đáng ngờ.**

> "Ứng viên cùng thời là Nguyễn Dữ, tác giả Truyền kỳ mạn lục **và là học trò ông**, và Phùng Khắc Khoan, học trò khác đi theo nhà Lê."

**Vấn đề:** Vòng 1 (S15) đúng khi loại **Lương Thế Vinh** (1441–1496) khỏi chỗ này — đó là lỗi cứng và bản vá đã xử lý tốt. Nhưng câu thay thế lại **khẳng định như sự thật** một quan hệ mà giới nghiên cứu đang cãi nhau. Theo **Trần Khánh Hạo** (dẫn qua Trần Ích Nguyên), Nguyễn Dữ **không phải học trò** Nguyễn Bỉnh Khiêm mà là người cùng lứa, thậm chí có thể thuộc **thế hệ trước**; một dòng nghiên cứu khác còn bác luôn chuyện Nguyễn Bỉnh Khiêm "phủ chính" *Truyền kỳ mạn lục*. Truyền thống "học trò + bạn đồng môn Phùng Khắc Khoan" đến từ phả ký đời sau.

Chỗ này đáng chú ý vì **chính file ở nơi khác rất kỷ luật** về đúng kiểu mệnh đề này: mục này tự gạt sấm ký ("phần lớn là do đời sau thêm vào"), tự dán nhãn giai thoại Hoành Sơn là "chỉ chép trong Đại Nam thực lục tiền biên hai thế kỷ rưỡi sau". Rồi ngay bên dưới lại nhận một truyền thống muộn khác không hedge.

**Sửa thế nào:** "…Nguyễn Dữ, tác giả Truyền kỳ mạn lục **mà truyền thống coi là học trò ông** (quan hệ này còn tranh luận), và Phùng Khắc Khoan…". Riêng **Phùng Khắc Khoan (1528–1613)** là học trò thì vững, không cần hedge.

**Bằng chứng:** mactoc.com, "Đoán định lại thân thế Nguyễn Dữ và thời điểm sáng tác Truyền kì mạn lục"; taodan.com.vn, "Nguyễn Dữ và Truyền kỳ mạn lục".

---

### H7 · CH90-CE10_14-07 Trần Hưng Đạo — bản vá cắt mất hai chữ mang toàn bộ luận điểm của bài báo
**Mức: Nên sửa.**

> "**Nguồn:** … Ngô Đức Thọ, "Đi tìm nguồn gốc và năm xuất hiện của văn bản Binh thư yếu lược" (1986)."

**Vấn đề:** Nhan đề thật kết thúc bằng hai chữ **"hiện có"**: *"Đi tìm nguồn gốc và năm xuất hiện của văn bản Binh thư yếu lược **hiện có**"*, *Tạp chí Hán Nôm* số 2/1986. Hai chữ ấy chính là luận điểm: bài khảo của Ngô Đức Thọ nói về **văn bản đang lưu hành**, không về *Binh thư yếu lược* nói chung. Bỏ chúng đi thì nhan đề đọc như một bài về nguồn gốc tác phẩm của Trần Quốc Tuấn — đúng cái hiểu mà bài báo bác bỏ, và đúng cái lỗi (S3) mà bản vá này sinh ra để sửa.

**Sửa thế nào:** `Ngô Đức Thọ, "Đi tìm nguồn gốc và năm xuất hiện của văn bản Binh thư yếu lược hiện có", Tạp chí Hán Nôm 2/1986.`

**Bằng chứng:** baotanglichsu.vn/vi/Articles/3096/7417/ — đăng lại nguyên bài, nhan đề viết hoa đủ "…BINH THƯ YẾU LƯỢC HIỆN CÓ".

**Phần vá thì ĐÚNG:** *Binh thư yếu lược* đã được gỡ khỏi dòng Nguồn ✓ và câu văn xuôi nay ghi rõ "văn bản mang tên Binh thư yếu lược lưu hành ngày nay được khảo cứu xác định là soạn muộn, không sớm hơn 1869" ✓.

---

### H8 · CH90-CE19_20-03 Hồ Xuân Hương — một mục **Sai** của vòng 1 chưa vá
**Mức: Nên sửa (vòng 1 xếp Sai).**

> "Ứng viên cùng thời là Bà Huyện Thanh Quan và **Đoàn Thị Điểm**, hai nữ sĩ có danh phận rõ hơn."

**Vấn đề:** Đoàn Thị Điểm **1705–1748**, mất **24 năm trước** khi Hồ Xuân Hương (k. 1772) sinh; Bà Huyện Thanh Quan **1805–1848**, nổi danh sau khi Hồ Xuân Hương đã mất. Chữ "**cùng thời**" làm câu này thành một **phát biểu sai sự thật**, không chỉ là lỗi phương pháp — đó là lý do vòng 1 xếp S15 vào *Sai*. Bản vá nhóm CE19_20 không đụng tới (12 patch của nhóm đều từ báo cáo nhóm, không từ S15 của báo cáo toàn file).

**Sửa thế nào:** bỏ chữ "cùng thời", ví dụ "Hai nữ sĩ thường được đặt cạnh bà là Đoàn Thị Điểm (thế hệ trước) và Bà Huyện Thanh Quan (thế hệ sau), đều có danh phận rõ hơn." Cùng kiểu, **CH90-CE15_18-03** Lê Thánh Tông ("Lê Thái Tổ và Minh Mạng ở thế kỷ 19") và **CH90-CE01_09-07** Phùng Hưng ("Dương Thanh… và Khúc Thừa Dụ đầu thế kỷ 10") vẫn chưa nêu được ứng viên thật sự cùng thời.

---

### H9 · CH90-CE01_09-03 Sĩ Nhiếp — câu mới viết **mâu thuẫn với liên kết ngay bên dưới nó**
**Mức: Đáng ngờ.**

> *Vì sao chọn:* "…còn **Khương Tăng Hội** tuy sinh ở Giao Chỉ nhưng dịch kinh ở Kiến Nghiệp từ năm 247, **sau khi Sĩ Nhiếp mất**."
> *Ảnh hưởng tới:* "- **Khương Tăng Hội (康僧會) · kế thừa · trực tiếp**"

**Vấn đề:** Bản vá sửa đúng một lỗi của vòng 1 (Mâu Tử không phải tăng sĩ; Khương Tăng Hội không "cùng hoạt động" thời Sĩ Nhiếp) — nhưng khi thêm mệnh đề "sau khi Sĩ Nhiếp mất" thì nó **phủ định mức bằng chứng "trực tiếp"** của chính liên kết nằm cách đó bốn dòng. Trong file, "trực tiếp" dành cho quan hệ có tiếp xúc; mục này vừa tự khai là không có.

Quan hệ vẫn **có thể** đứng — Khương Tăng Hội lớn lên ở Giao Chỉ trong môi trường Phật giáo mà Sĩ Nhiếp tạo điều kiện — nhưng đó đúng là nghĩa của "**qua trường phái**".

**Sửa thế nào:** đổi thành `Khương Tăng Hội (康僧會) · kế thừa · qua trường phái`.

---

### H10 · CH90-CE19_20-09 Tôn Thất Tùng — "thời gian mổ" (N18) chưa vá
**Mức: Đáng ngờ.**

> "Phương pháp công bố năm 1963 rút **thời gian mổ** từ hàng giờ xuống vài phút…"

**Vấn đề:** Con số vài phút là **thì cắt nhu mô gan**, không phải thời lượng cả cuộc mổ. Bản vá nhóm CE19_20 đã sửa rất tốt dòng Nguồn của mục này (The Lancet 281, 1963, tr. 192–193, thêm đồng tác giả Nguyễn Dương Quang — tôi xác nhận ở *Đã kiểm, đúng*) nhưng để nguyên mệnh đề văn xuôi mà vòng 1 đã nêu ở N18. Kết quả: dòng Nguồn nay chuẩn xác, còn câu nó chống đỡ thì vẫn phóng đại — một thành tựu vốn không cần phóng đại.

**Sửa thế nào:** "…rút **thì cắt nhu mô gan** từ hàng giờ xuống còn vài phút…"

---

### H11 · CH90-CE01_09-06 Mai Hắc Đế — "sử Đường" nói nhiều hơn nguồn được dẫn
**Mức: Nên sửa (nhẹ).**

> "**sử Đường và Toàn thư đều đặt** việc Dương Tư Húc dẹp ông **vào năm 722**"

**Vấn đề:** Bản vá này là một trong những bản vá tốt nhất của cả file — nó thay mệnh đề "giữ được khoảng mười năm" (vô căn cứ) bằng đúng cách đặt vấn đề, và quy đích danh mốc 713 cho tái dựng của Phan Huy Lê. Chỉ một chỗ hơi quá: **Tân Đường thư — bộ duy nhất được dẫn ở dòng Nguồn — không cho năm 722**, nó chỉ chép 「開元初」. Năm 722 (Khai Nguyên 10) đến từ **Tư trị thông giám quyển 212**, một bộ đời Tống, và từ ĐVSKTT Ngoại kỷ q.5 (năm Nhâm Tuất).

**Sửa thế nào:** "…**Tư trị thông giám và Toàn thư** đều đặt việc Dương Tư Húc dẹp ông vào năm 722, còn Tân Đường thư chỉ ghi 'đầu niên hiệu Khai Nguyên'…" — hoặc bổ sung Tư trị thông giám q.212 vào dòng Nguồn.

**Lưu ý:** chính kiểm toán nguồn (`audit-nguon-ch90.md`) đã cảnh báo đúng điều này ở dòng Tân Đường thư — cảnh báo chưa được áp.

## Liên kết

**Phạm vi đã quét:** toàn bộ 80 khối `Kế thừa từ` / `Ảnh hưởng tới` của 40 mục — **126 dòng liên kết**, trong đó **88 trỏ tới ID nội bộ** — kiểm bằng script trên bốn trục brief yêu cầu: (a) bất khả về niên đại, (b) đối ứng đúng chiều, (c) từ vựng hợp lệ, (d) quá 3 mục.

**Kết quả tổng:**
- **Bất khả về niên đại: KHÔNG CÓ.** Không mục nào ảnh hưởng tới người đã mất trước khi mình bắt đầu hoạt động. Tôi quét thêm một trục chặt hơn brief: trong **34 dòng** ghi mức bằng chứng **"trực tiếp"**, mọi dòng trỏ tới ID nội bộ đều có **giao nhau về đời sống** giữa hai phía — đạt hết.
- **Quá 3 mục: KHÔNG CÓ.** Dài nhất là 3 (Phan Châu Trinh `Kế thừa từ`, Võ Nguyên Giáp `Kế thừa từ`).
- **Từ vựng: hợp lệ 100%.** Mọi loại quan hệ nằm trong {kế thừa, tổng hợp, phản bác, tương đồng độc lập} và mọi mức bằng chứng trong {trực tiếp, qua trường phái, suy đoán học giả}. Không có ID trỏ tới mục không tồn tại, không có mục tự trỏ vào mình.
- **Đối ứng: 8 liên kết một chiều**, trong đó **4 cái lint nhìn thấy** (INFO) và **4 cái lint mù** — xem L3.

---

### L1 · CH90-CE01_09-01 Trưng Trắc — "Ảnh hưởng tới" trỏ **nhầm số mục**
**Mức: Sai. Hạng mục nghiêm trọng nhất của vòng này.**

> **Ảnh hưởng tới:**
> - CH90-CE01_09-02 · tương đồng độc lập · suy đoán học giả
> - **CH90-CE01_09-04 · kế thừa · qua trường phái**

**Sai ở đâu:** `CH90-CE01_09-04` là **Tì-ni-đa-lưu-chi (Vinītaruci)** — tăng sĩ gốc Nam Ấn, hoạt động 580–594, mục về Thiền tông. Mệnh đề "Trưng Trắc **kế thừa qua trường phái** tới Tì-ni-đa-lưu-chi" không có nghĩa theo bất kỳ cách đọc nào: không cùng lĩnh vực (Quân sự → Tôn giáo), không cùng mạch, và mục `-04` **không hề ghi Trưng Trắc** trong "Kế thừa từ" (nó ghi Sĩ Nhiếp và Thiền Trung Hoa — Tăng Xán).

**Đâu là cái đúng — bằng chứng nội tại rất mạnh:** `CH90-CE01_09-05` **Lý Nam Đế** đang ghi:
> **Kế thừa từ:** `- CH90-CE01_09-01 · kế thừa · qua trường phái`

…**đúng loại quan hệ, đúng mức bằng chứng, đúng chiều** — và không có vế đối ứng. Lint báo đúng việc đó:
> `[INFO] CH90-CE01_09-05: kế thừa từ CH90-CE01_09-01 nhưng CH90-CE01_09-01 không ghi 'Ảnh hưởng tới' CH90-CE01_09-05`

Tức đây là một **lỗi gõ `-04` thay cho `-05`**: một liên kết lẽ ra đối ứng bị tách thành một INFO giả ở một đầu và một liên kết vô nghĩa ở đầu kia. Nội dung cũng khớp: Lý Bí là mắt tiếp theo của mạch khởi nghĩa mà Hai Bà Trưng mở, đúng như mục Lý Nam Đế lập luận.

**Sửa thế nào:** đổi `CH90-CE01_09-04` thành `CH90-CE01_09-05` trong khối "Ảnh hưởng tới" của Trưng Trắc. Một dòng sửa xong hai vấn đề và dọn luôn một INFO của lint.

**Vì sao lint không bắt được:** `atlaslib/lint.py` chỉ quét một chiều —
```python
for l in p["inherits"]:
    if t in all_persons and not any(x["target"] == p["id"] for x in all_persons[t]["influences"]):
        rep.info(...)
```
— tức chỉ hỏi "ai kế thừa mà đầu kia không ghi ảnh hưởng", **không bao giờ hỏi ngược lại**. Mọi `Ảnh hưởng tới` trỏ sai đích đều đi lọt, miễn ID đó tồn tại. Đề nghị bổ sung vòng đối xứng ở P4.

---

### L2 · CH90-CE19_20-10 Thích Nhất Hạnh — nhãn quan hệ **tự mâu thuẫn** (N19 chưa vá)
**Mức: Sai.**

> **Ảnh hưởng tới:** `- Martin Luther King Jr. · tương đồng độc lập · trực tiếp`

**Sai ở đâu:** Hai trường phủ định nhau **trong cùng một dòng**. Theo chính `prompts/atlas-prompt.md`, "tương đồng độc lập" là nhãn dùng **khi không có bằng chứng tiếp xúc**; "trực tiếp" là mức bằng chứng **có tiếp xúc**. Và ở đây tiếp xúc là chắc chắn: hai người gặp nhau năm **1966**, King **đề cử ông giải Nobel Hoà bình năm 1967**.

**Vì sao vẫn chưa vá, và đề xuất của vòng 1 cũng không dùng được:** `review-ch90.md` (N19) đề nghị đổi thành `"ảnh hưởng · trực tiếp"` — nhưng **"ảnh hưởng" không nằm trong từ vựng** {kế thừa | tổng hợp | phản bác | tương đồng độc lập}. Áp nguyên văn đề xuất đó sẽ sinh **ERROR lint** (`loại quan hệ '…' ngoài từ vựng`). Nhiều khả năng đây là lý do bản vá bỏ qua mục này thay vì sửa.

**Sửa thế nào (nằm trong từ vựng):** `Martin Luther King Jr. · kế thừa · trực tiếp`. Chiều đúng: TNH đang ở khối "Ảnh hưởng tới", và King là người tiếp nhận — ông công khai chống chiến tranh Việt Nam sau cuộc gặp 1966.

---

### L3 · Bốn liên kết một chiều mà lint **không thể thấy**
**Mức: Nên sửa.** Lint chỉ cảnh báo chiều `Kế thừa từ` (4 INFO hiện có). Bốn liên kết dưới đây nằm ở chiều `Ảnh hưởng tới` và **không sinh cảnh báo nào**:

| Nguồn | Đích | Dòng | Chẩn đoán |
|---|---|---|---|
| `BCE03_01-01` An Dương Vương | `BCE03_01-02` Triệu Đà | `phản bác · trực tiếp` | Triệu Đà chỉ ghi "Thiết chế quận huyện nhà Tần" trong *Kế thừa từ* (1/3 chỗ, còn trống). Quan hệ đối kháng quan trọng nhất của cả nhóm chỉ hiện một chiều trên graph. |
| `CE01_09-01` Trưng Trắc | `CE01_09-04` Tì-ni-đa-lưu-chi | `kế thừa · qua trường phái` | **Lỗi thật** — xem L1. |
| `CE10_14-06` Trần Thủ Độ | `CE10_14-07` Trần Hưng Đạo | `kế thừa · qua trường phái` | Nội dung đúng (bộ khung thiết chế Trần là điều kiện cho chỉ huy thống nhất). Trần Hưng Đạo đang có 2/3 mục *Kế thừa từ*, còn chỗ. |
| `CE19_20-01` Nguyễn Du | `CE19_20-04` Trương Vĩnh Ký | `kế thừa · qua trường phái` | Nội dung đúng và được chính văn xuôi mục Trương Vĩnh Ký chống đỡ ("phiên âm… Truyện Kiều… sang Quốc ngữ"). Trương Vĩnh Ký đang có 2/3 mục, còn chỗ. |

Ba cái sau **không sai về nội dung** — chỉ là bất đối xứng mà P4 sẽ đồng bộ. Nêu ra vì chúng chứng minh một điều: **lint hiện không bảo vệ được chiều này**, nên L1 có thể tồn tại mà không ai thấy.

Để tham chiếu, 4 INFO lint đang báo (chiều ngược lại, đều là bất đối xứng lành tính trừ cái thứ nhất): `CE01_09-05 ← CE01_09-01` (chính là L1), `CE01_09-06 ← CE01_09-05`, `CE01_09-08 ← CE01_09-03`, `CE15_18-10 ← CE10_14-10`.

---

### L4 · CH90-CE01_09-03 Sĩ Nhiếp → Khương Tăng Hội: mức bằng chứng mâu thuẫn với văn xuôi mới
Xem **H9**. Tóm tắt: `trực tiếp` → nên là `qua trường phái`.

---

### L5 · CH90-CE15_18-10 Quang Trung ← CH90-CE10_14-10 Hồ Quý Ly — nhãn so với văn xuôi
**Mức: Nên sửa (nhẹ).**

> Quang Trung, *Kế thừa từ:* `- CH90-CE10_14-10 · tương đồng độc lập · suy đoán học giả`

**Vấn đề:** "Tương đồng độc lập" nghĩa là hai bên đi tới cùng chỗ **mà không biết nhau**. Nhưng văn xuôi hai mục nay nói mạnh hơn thế, và nói có chủ ý: mục Hồ Quý Ly viết "bước ấy phải đợi **Quang Trung** gần bốn thế kỷ sau, nhưng ý định dùng tiếng bản địa làm phương tiện học thuật **bắt đầu từ đây**"; mục Quang Trung viết "nỗ lực mà **Hồ Quý Ly từng thử và thất bại**". Cả hai dựng một **mạch kế tục có ý thức**, không phải hai phát minh song song.

Ghi chú bản vá (`patch-ch90-CE10_14-notes.md` mục F) nói rõ hai mục được cố ý khớp với nhau — nhưng cái nhãn thì không được chỉnh theo.

**Sửa thế nào:** `kế thừa · suy đoán học giả` (giữ nguyên mức bằng chứng, vốn đã thận trọng đúng mức). Hoặc giữ nhãn và nới văn xuôi — nhưng không nên giữ cả hai như hiện nay.

---

### L6 · Liên kết thiếu sau khi vá: Hồ Chí Minh ↔ Phan Châu Trinh
**Mức: Nên sửa (nhẹ).** Bản vá D1 đưa vào mục `CE19_20-07` một câu mới rất tốt: *"Năm 1919, ông cùng **Phan Châu Trinh**, Phan Văn Trường soạn Yêu sách của nhân dân An Nam…"*. Phan Châu Trinh là `CH90-CE19_20-06`, có mục riêng trong cùng nhóm. Nhưng **không có liên kết nào giữa hai mục** — Hồ Chí Minh chỉ ghi `Kế thừa từ: CE19_20-05 (Phan Bội Châu)` và Lenin.

Quan hệ nay được chính văn xuôi chứng thực ở mức "trực tiếp" (đồng tác giả một văn bản), tức mạnh hơn cả liên kết Lenin đang có. Phan Châu Trinh còn trống 1/3 chỗ ở `Ảnh hưởng tới`. Không phải lỗi, nhưng là chỗ bản vá tạo ra nội dung mà graph chưa theo kịp.

## Nhất quán / Ghi chú biên tập

Tôi đối chiếu **từng con số và từng mệnh đề** của mục "## Ghi chú biên tập" với 40 mục hiện tại. Bốn chỗ đã lỗi thời so với chính các bản vá.

---

### G1 · "**bốn chỗ không xác minh được**" — câu tự mâu thuẫn, con số đúng là **ba**
**Mức: Ghi chú lỗi thời.**

> "Kiểm toán nguồn độc lập (95 trích dẫn) còn **bốn chỗ không xác minh được nội dung**, chỉ xác minh được tác phẩm và phạm vi: Trần Văn Giáp cho Chu Văn An (chưa tra được tập/trang); Bản kỷ tục biên năm 1585 cho Nguyễn Bỉnh Khiêm; Li Tana cho Đào Duy Từ (không đọc được toàn văn); và báo cáo Cổ Loa vô danh của An Dương Vương — **chỗ này đã thay bằng công bố có tên**."

**Vấn đề:** Câu vừa khẳng định "còn bốn chỗ **không xác minh được**" vừa, trong cùng một câu, **giải quyết một trong bốn**. Tôi xác nhận chỗ thứ tư đã thật sự được xử lý: dòng Nguồn của `CH90-BCE03_01-01` nay là *Nam C. Kim, Lai Văn Tới và Trịnh Hoàng Hiệp, "Co Loa: an investigation of Vietnam's ancient capital", Antiquity 84 (2010)* — một công bố bình duyệt định danh được, mà tôi đã kiểm là **có thật và trích đúng** (Antiquity 84 (326), 12/2010, tr. 1011–1027). "Báo cáo khai quật di chỉ Cổ Loa, Viện Khảo cổ học" vô danh không còn trong file.

Nên **ba**, không phải bốn. Và vì câu kết của đoạn ("Cần đối chiếu trên bản in trước khi coi là đã kiểm") đọc như áp cho cả bốn, người đọc sẽ đi tìm một nghĩa vụ không còn tồn tại.

**Sửa thế nào:** "…còn **ba chỗ** không xác minh được nội dung…: Trần Văn Giáp cho Chu Văn An; Bản kỷ tục biên năm 1585 cho Nguyễn Bỉnh Khiêm; Li Tana cho Đào Duy Từ. (Chỗ thứ tư — báo cáo Cổ Loa vô danh — đã được thay bằng Kim, Lai và Trịnh 2010 và không còn là vấn đề.)"

**Lưu ý kèm theo:** bản vá mới đã **đúng về trích dẫn** nhưng **sai một dữ kiện bên trong câu** mà nó chống đỡ — xem **H3** (khuôn đúc không ở Cầu Vực). Gỡ được một KHÔNG KIỂM ĐƯỢC thì tốt, nhưng câu văn xuôi đi kèm cần sửa trước khi coi mục này là khép.

---

### G2 · Ghi chú về Triệu Đà **lỗi thời so với chính mục Triệu Đà vừa được vá**
**Mức: Ghi chú lỗi thời.**

> *Ghi chú biên tập:* "Triệu Đà (CH90-BCE03_01-02): việc xếp nhà Triệu vào quốc thống Việt Nam là vấn đề sử học chưa khép lại, **từ Đại Việt sử ký toàn thư qua Ngô Thì Sĩ tới nay**."

**Vấn đề:** Bản vá đã **sửa đúng** mục Triệu Đà theo khuyến nghị N5 — văn xuôi nay ghi đích danh người khởi đầu lập trường ấy:
> "việc **Lê Văn Hưu** xếp nhà Triệu vào quốc thống **từ thế kỷ 13**, rồi Ngô Thì Sĩ năm 1775 và dòng chính thống hiện nay phản bác…"

…và dòng Nguồn cũng được chỉnh thành "Đại Việt sử ký toàn thư, Kỷ nhà Triệu **(kế thừa lập trường của Lê Văn Hưu)**". Nhưng ghi chú biên tập **vẫn giữ nguyên cách kể cũ**, bỏ mất Lê Văn Hưu và quy khởi điểm cho Toàn thư — tức đúng cái lỗi mà bản vá đã sửa ở thân bài. Hai chỗ trong cùng một file nay kể hai phả hệ sử học khác nhau.

**Sửa thế nào:** "…chưa khép lại, **từ Lê Văn Hưu (TK 13) qua Đại Việt sử ký toàn thư và Ngô Thì Sĩ (1775) tới nay**."

---

### G3 · "Lê Văn Hưu … **bị Lê Quý Đôn lấn chỗ**" — lý do loại xuyên nhóm, N5 chưa vá
**Mức: Ghi chú lỗi thời / Nên sửa.**

> "Lê Văn Hưu, Ngô Sĩ Liên, Phan Huy Chú: ba sử gia lớn, **bị Lê Quý Đôn lấn chỗ ở lĩnh vực Sử học**."

**Vấn đề:** Lê Văn Hưu (1230–1322) thuộc nhóm **CE10_14**; Lê Quý Đôn (1726–1784) thuộc nhóm **CE15_18**. Loại một người ở nhóm này vì một người ở nhóm khác "lấn chỗ" phá vỡ chính nguyên tắc chia nhóm mà file dựa vào — và mâu thuẫn trực tiếp với lý do "nhóm đã đủ 10 người" dùng ở dòng ngay bên dưới, vốn chỉ có nghĩa nếu hạn ngạch **tính trong nhóm**.

Điều này nay **chói hơn sau bản vá**, vì mục Triệu Đà vừa được bổ sung để tôn Lê Văn Hưu lên vai người đặt ra một trong những lập trường sử học bền nhất của Việt Nam. File đồng thời nói ông quan trọng đến thế và loại ông bằng một lý do thuộc nhóm khác.

**Sửa thế nào:** hoặc đổi lý do loại sang một lý do **trong nhóm CE10_14** (ví dụ: so với Chu Văn An ở tiêu chí (b), hoặc so với chính Trần Nhân Tông / Hồ Quý Ly về số chỗ), hoặc tách Lê Văn Hưu ra một dòng riêng với lý do riêng. Không giữ công thức "lấn chỗ" xuyên nhóm.

---

### G4 · "nhóm CE19_20 **đã có hai mục văn học**" — đếm thiếu
**Mức: Ghi chú lỗi thời (nhẹ).**

> "Nguyễn Công Trứ, Cao Bá Quát, Nguyễn Đình Chiểu, Bà Huyện Thanh Quan, Đoàn Thị Điểm: **nhóm CE19_20 đã có hai mục văn học**; thêm nữa sẽ lệch khỏi yêu cầu đa dạng lĩnh vực."

**Vấn đề:** Ở trạng thái hiện tại, **bốn** mục của nhóm mang lĩnh vực **Văn học**:

| ID | Tên | `lĩnh vực` |
|---|---|---|
| CE19_20-01 | Nguyễn Du | **Văn học** |
| CE19_20-03 | Hồ Xuân Hương | **Văn học** |
| CE19_20-04 | Trương Vĩnh Ký | Ngôn ngữ học, **Văn học** |
| CE19_20-05 | Phan Bội Châu | Chính trị/Nhà nước, **Văn học** |

Đọc theo "lĩnh vực chính" thì "hai mục" bảo vệ được; nhưng lập luận của ghi chú là về **đa dạng lĩnh vực**, mà lint đếm theo `Counter(f for p in g["persons"] for f in p["fields"])` — tức đếm **cả lĩnh vực thứ hai**. Nói "hai" trong một câu về hạn ngạch lĩnh vực là nói nhẹ hơn thực tế gấp đôi, và nó làm yếu chính lý do loại năm người.

**Sửa thế nào:** "…nhóm CE19_20 đã có **hai mục lấy Văn học làm lĩnh vực chính và hai mục nữa mang Văn học làm lĩnh vực phụ**…"

---

### G5 · Con số "95 trích dẫn" không còn tái dựng được từ file hiện tại
**Mức: Nên sửa.** `audit-nguon-ch90.md` giải thích rõ con số: 90 trích dẫn lúc bắt đầu + 5 thêm trong lúc kiểm (Taylor 1986, Nhung Tuyet Tran 2018, Yao Takao 2013, *Bạch Vân quốc ngữ thi tập*, Windrow 2004) = 95. Nhưng **sau** khi kiểm toán chốt, các bản vá nhóm CE10_14 và CE19_20 còn đổi tiếp vài dòng Nguồn (gỡ *Binh thư yếu lược*, thêm Ngô Đức Thọ 1986; đổi *Đại Nam thực lục chính biên* → *Đại Nam chính biên liệt truyện sơ tập* q.30 cho Quang Trung). Đếm máy móc trên file hôm nay cho **~92 đoạn** tách bằng dấu chấm phẩy trên 40 dòng Nguồn — không khớp 95 và cũng không nên khớp, vì hai cách đếm khác nhau.

Ghi chú không sai, nhưng nó đọc như một chứng chỉ bao phủ **file hiện tại**, trong khi thực tế nó bao phủ một **ảnh chụp** của file. Nên viết rõ: "Kiểm toán nguồn độc lập ngày 30/10/2026 đã kiểm 95 trích dẫn **ở bản thời điểm đó**; một số dòng Nguồn được sửa sau đó (xem reports/audit-nguon-ch90.md)."

---

### G6 · Nhãn `[Tranh cãi lịch sử]` vẫn bất đối xứng (TL1 phần 2 chưa vá)
**Mức: Nên sửa.** Bản vá đã xử lý **rất tốt** phần 1 của TL1: Bối cảnh nhóm BCE03_01 nay viết "Lấy mốc nào làm khởi điểm Bắc thuộc — 179 hay 111 TCN — tuỳ thuộc câu hỏi nhà Triệu có thuộc quốc thống Việt Nam hay không", thay cho mệnh đề cũ đã âm thầm chọn phe. Nhưng phần 2 còn nguyên: **An Dương Vương mang nhãn `[Tranh cãi lịch sử]`, Triệu Đà thì không** — dù chính mục Triệu Đà gọi vấn đề của mình là "một trong những tranh luận sử học kéo dài nhất của Việt Nam", và dù An Dương Vương nay có hẳn bằng chứng khảo cổ có bình duyệt chống đỡ. Nếu chỉ một mục được mang nhãn, lẽ ra là mục kia.

---

### G7 · Ba mục vẫn không nêu được ứng viên bị loại (N4), ghi chú không thừa nhận
**Mức: Nên sửa.** N4 nêu ba mục; **một đã vá tốt** — `BCE03_01-02` Triệu Đà nay có "Ứng viên cùng giai đoạn là **Lữ Gia**, tể tướng cầm đầu cuộc kháng cự khi nhà Hán diệt Nam Việt năm 111 TCN", kèm lý do theo counterfactual (d). Hai mục còn lại giữ nguyên:
- `CE10_14-10` Hồ Quý Ly — "**Ứng viên thay thế không có** — không ai cùng thời làm điều tương tự." (Hồ Nguyên Trừng và Trần Nguyên Đán đều là ứng viên nêu được.)
- `CE15_18-07` Alexandre de Rhodes — nêu Pina, Amaral, Barbosa, nhưng đó là **cộng sự bị chia công**, không phải ứng viên cạnh tranh bị loại theo tiêu chí.

Cộng với H8 (Hồ Xuân Hương, Lê Thánh Tông, Phùng Hưng nêu người không cùng thời), đây là **5/40 mục** chưa đạt thể thức "Vì sao chọn". Mục *Ghi chú biên tập* hiện không ghi nhận khoảng trống này ở bất kỳ đâu — trong khi nó đã chịu ghi nhận khoảng trống 1954–1975 và khoảng trống lĩnh vực của nhóm BCE03_01. Nên nhất quán: hoặc vá, hoặc ghi.

---

### Các con số và mệnh đề khác của Ghi chú biên tập — **đã kiểm, đúng**

| Mệnh đề | Kết quả |
|---|---|
| "Nhóm BCE03_01 chỉ có 2 nhân vật và 2 lĩnh vực nên bị lint cảnh báo" | ✅ khớp `reports/lint-ch90.txt` (`[WARN] ch90/BCE03_01: chỉ 2 lĩnh vực`); hai lĩnh vực là Chính trị/Nhà nước và Quân sự |
| "nhóm CE19_20 đã có 10 người; trần nay là 12" | ✅ đếm được đúng 10 mục; `max_per_group` không bị vượt (lint 0 ERROR) |
| "Hồ Chí Minh (CH90-CE19_20-07) và Thích Nhất Hạnh (CH90-CE19_20-10)" | ✅ hai ID đúng người |
| "Wikidata xếp 'Trung sisters' (Q1207428) là một cặp… dùng Q-ID của Trưng Trắc (Q25418142)" | ✅ khớp trường `wikidata:` của mục |
| "Khúc Thừa Dụ: giành quyền tự chủ thực tế từ 905" | ✅ khớp mục Ngô Quyền ("từ năm 905") |
| "Owner đã bổ sung hai lĩnh vực **Giáo dục** và **Ngôn ngữ học**, nên ba mục này nay ghi đúng chuyên môn" | ✅ Chu Văn An = `Giáo dục, Triết học`; Trương Vĩnh Ký và de Rhodes = `Ngôn ngữ học, …`; cả ba hợp từ vựng `C.FIELDS` (lint 0 ERROR) |
| "Tuệ Tĩnh… trước tác thất lạc gần hết nên không đánh giá được theo (b)" | ✅ khớp lý do nêu trong mục Lê Hữu Trác |
| "Áp đúng thang [toàn cầu] thì gần như chỉ còn Hồ Chí Minh và Thích Nhất Hạnh" | ✅ nhất quán với hai mục đó và với `render.py` |
| Toàn bộ 40 mục, 5 nhóm, phân bố 2/8/10/10/10 | ✅ đếm bằng script |

**Lint hiện tại:** `ERROR 0 · WARN 1 · INFO 4` — WARN duy nhất đã được Ghi chú biên tập giải thích và chấp nhận; 4 INFO là bất đối xứng liên kết (xem L1, L3).

## Trung lập

### T1 · Tự mô tả về giai đoạn 1954–1975 nay **chính xác** — đã kiểm từng mệnh đề

Đoạn "Giai đoạn 1954–1975 và sau đó" đưa ra bốn khẳng định kiểm được. Tôi kiểm cả bốn trên file hiện tại:

| Khẳng định trong ghi chú | Kiểm trên file | Kết quả |
|---|---|---|
| "**Câu đó chưa kiểm chứng và thiếu chứng cứ**" (câu "cả hai miền" của bản thảo đầu) | Chuỗi "cả hai miền" không còn ở dạng khẳng định; câu cũ đã bị thay | ✅ |
| "không một nhân vật Việt Nam Cộng hoà nào được nêu tên, **kể cả trong danh sách bị loại**" | Tôi liệt kê đủ 22 tên trong "Ứng viên mạnh đã bị loại": Lê Hoàn, Lý Thánh Tông, Minh Mạng, Trần Thái Tông, Khúc Thừa Dụ, Tuệ Tĩnh, Lương Thế Vinh, Vũ Hữu, Nguyễn Công Trứ, Cao Bá Quát, Nguyễn Đình Chiểu, Bà Huyện Thanh Quan, Đoàn Thị Điểm, Huỳnh Thúc Kháng, Nguyễn Văn Vĩnh, Phạm Quỳnh, Nguyễn Thái Học, Trương Định, Nguyễn Trung Trực, Lê Văn Hưu, Ngô Sĩ Liên, Phan Huy Chú — **không ai thuộc VNCH** | ✅ |
| "**Trần Trọng Kim và Ngô Đình Diệm chưa từng được cân**" | `grep` toàn file: mỗi tên xuất hiện **đúng một lần, và chỉ ở chính câu ghi chú này**. Không ai trong hai người xuất hiện trong bất kỳ mục nào, bất kỳ đoạn "Vì sao chọn" nào, hay danh sách bị loại. Cụm "Việt Nam Cộng hoà" cũng chỉ có **một lần duy nhất**, cũng ở chính câu đó | ✅ |
| "**Đổi mới 1986 được nêu ở Bối cảnh nhưng không có mục đại diện**" | Bối cảnh CE19_20 có "thống nhất và đổi mới kinh tế từ 1986"; không mục nào trong 40 mục đại diện cho giai đoạn này | ✅ |

**Và `overview.html` khớp.** `atlaslib/render.py:475` viết: *"với giai đoạn 1954–1975, phụ lục hiện phản ánh một góc nhìn: đánh giá độc lập cho thấy nhân vật phía Việt Nam Cộng hoà và giai đoạn Đổi mới chưa được cân nhắc, và điều đó được ghi rõ trong Ghi chú biên tập thay vì che đi."* Không có lệch giữa trang Overview và file.

**Phán xét:** đây là cách xử lý **đúng** và là chỗ mạnh nhất của vòng vá. File không còn tự nhận một việc chưa làm; nó nói thẳng phạm vi của mình và đặt việc cân lại cho Owner ở P4. Một phụ lục có quyền chọn phạm vi hẹp — điều không được phép là mô tả sai việc mình đã làm, và lỗi đó đã được gỡ.

---

### T2 · Nhưng file **im lặng** về bất đối xứng TL3, vốn vẫn còn nguyên
**Mức: Nên sửa.**

Vòng 1 nêu **hai** vấn đề trung lập ở thế kỷ 20, không phải một:
- **TL2** — tuyên bố "cả hai miền" không có chứng cứ → **đã xử lý**, và được ghi rõ (T1).
- **TL3** — Trần Thủ Độ, Gia Long, Triệu Đà, Hồ Quý Ly, Trương Vĩnh Ký đều có ít nhất một câu ghi mặt trái; **Hồ Chí Minh và Võ Nguyên Giáp không có câu nào** → **chưa xử lý**, và *Ghi chú biên tập* **không nhắc tới ở bất kỳ đâu**.

Tôi xác nhận TL3 vẫn đúng với file hôm nay. Mẫu câu mà file dùng — Trần Thủ Độ, *Vì sao chọn*:
> "Các biện pháp tàn khốc với tông thất nhà Lý **cũng là của ông**, phụ lục ghi cả hai mặt."

…không có đối ứng ở hai mục thế kỷ 20. Và đó là điều duy nhất file **không** chịu nói ra, trong khi nó đã chịu nói ra khoảng trống VNCH, khoảng trống Đổi mới, khoảng trống lĩnh vực nhóm BCE03_01, và ca ranh giới Võ Nguyên Giáp.

**Hệ quả cho câu hỏi của brief — "tự mô tả hiện tại có chính xác không":** chính xác **về những gì nó nói**, nhưng **chưa đầy đủ**. Nếu Owner chọn không áp hai câu `trunglap`, thì ghi chú nên nói ra điều đó, đúng cách file đã làm với giai đoạn 1954–1975 — ví dụ một dòng ở "Điểm cần kiểm chứng thêm": *"Chuẩn ghi mặt trái (mẫu: Trần Thủ Độ) hiện chưa được áp cho CH90-CE19_20-07 và -08; để Owner quyết ở P4."* Giữ im lặng là lặp lại đúng kiểu sai mà TL2 vừa được sửa: file làm một việc và mô tả một việc khác.

---

### T3 · Hai câu `trunglap` chưa áp — chúng có đạt chuẩn Trần Thủ Độ không?

Brief hỏi riêng về việc này. Hai câu nằm ở `reports/patch-ch90-CE19_20.json`, **không được áp** theo đúng yêu cầu — **việc không áp tự nó không phải lỗi**, đây là quyết định dành cho Owner. Đánh giá bản thảo:

**Chuẩn mà mục Trần Thủ Độ đặt ra**, tách thành bốn yêu cầu: (i) đặt ở cuối "Vì sao chọn"; (ii) nêu **đích danh sự việc**; (iii) **quy trách nhiệm trực tiếp** cho nhân vật; (iv) **không bình luận**, không định tính, không con số đang tranh cãi.

**Hồ Chí Minh — `CH90-CE19_20-07`:**
> "Cải cách ruộng đất 1953–1956 **dưới chính phủ do ông đứng đầu** gây hàng loạt án oan; **ông công khai nhận sai tháng 8/1956**."

- (i) ✅ gắn sau "…với góc nhìn phi thực dân hoá." — đúng vị trí.
- (ii) ✅ sự việc đích danh, có niên đại.
- (iii) ⚠️ **nhẹ hơn chuẩn.** Trần Thủ Độ: "cũng là của ông". Ở đây: "dưới chính phủ do ông đứng đầu" — quy cho thiết chế, không cho người. Có thể bảo vệ được (trách nhiệm chính trị là trách nhiệm thật), nhưng nó **không phải cùng mức** với câu mẫu.
- (iv) ⚠️ nửa sau là một **mệnh đề giảm nhẹ** ("ông công khai nhận sai") mà câu Trần Thủ Độ không có đối ứng. Chi tiết có thật và kiểm được (thư gửi đồng bào nông thôn 18/8/1956), nhưng đưa vào **trong cùng một câu** thì nó đóng vai trò cân bằng ngay tại chỗ — một ưu đãi mà mục Trần Thủ Độ, Gia Long hay Trương Vĩnh Ký không được hưởng.

→ **Đạt về hình thức, dưới chuẩn một bậc về độ nghiêm khắc.** Muốn ngang chuẩn: *"Cải cách ruộng đất 1953–1956, với luật do ông ký tháng 12/1953, gây hàng loạt án oan; phụ lục ghi cả hai mặt."* — và nếu muốn giữ chi tiết nhận sai thì để nó ở phần "Tư tưởng / đóng góp chính", không trong chính câu ghi mặt trái.

**Võ Nguyên Giáp — `CH90-CE19_20-08`:**
> "Ba đợt tấn công đồng bằng Bắc Bộ năm 1951 (Vĩnh Yên, Mạo Khê, sông Đáy) đều thất bại, tổn thất nặng; mức thương vong ông chấp nhận **là điểm tranh luận nhất**."

- (i) ✅ gắn sau "…Algérie và châu Phi."
- (ii) ✅ ba trận đích danh, có năm — chặt hơn cả câu Trần Thủ Độ.
- (iii) ✅ "mức thương vong **ông** chấp nhận" — quy trực tiếp, đúng mức.
- (iv) ❌ **"là điểm tranh luận nhất" là một mệnh đề tối cao không quy thuộc** — đúng loại văn mà vòng 1 đã dựng riêng một mục (TL4) để phản đối, và đúng loại mà `prompts/atlas-prompt.md` cấm ("văn phong trung lập, không tô vẽ"). Nó cũng không kiểm chứng được: tranh luận nhất so với cái gì, theo ai?

→ **Ba phần tư đạt, một phần tư tự phá.** Đáng chú ý: `patch-ch90-CE19_20-notes.md` mô tả câu này là *"mức thương vong ông chấp nhận **là điểm Fall và Windrow đều bàn**"* — bản trong ghi chú **có quy thuộc** và đạt chuẩn; bản trong JSON thì không. **Hai bản không khớp nhau.** Nếu Owner áp, nên áp **bản của ghi chú** (và hai tên đó đều đã có trong dòng Nguồn của mục).

**Về kỹ thuật:** cả hai patch đưa "Vì sao chọn" lên **103 chữ**. Ngưỡng cảnh báo lint là `abs(n - 80) > 0.3 × 80`, tức WARN từ **105 chữ**. Áp cả hai vẫn **0 cảnh báo mới** — nhưng chỉ còn dư **1 chữ**, nên nếu sửa câu theo đề xuất của tôi ở trên thì phải đếm lại bằng đúng `atlaslib.lint.words()`.

---

### T4 · Những chỗ trung lập **đã được vá tốt** (ghi nhận)

- **Bối cảnh BCE03_01** — mốc Bắc thuộc nay nêu cả 179 và 111 TCN kèm lý do vì sao mốc khác nhau, thay cho việc âm thầm chọn mốc 111. Đây là bản vá gọn nhất của cả vòng (TL1 phần 1).
- **Quang Trung** — dòng Nguồn nay ghi rõ *"Đại Nam chính biên liệt truyện sơ tập, quyển 30 'Nguỵ Tây liệt truyện' (sử triều Nguyễn, thù địch với Tây Sơn — **đọc có đối chiếu**)"*. Đây là mẫu mực: không gỡ nguồn thiên kiến mà dán nhãn nó (N20).
- **Lê Thánh Tông** — nay nêu **cả hai phía** của tranh luận quyền phụ nữ (Insun Yu / Tạ Văn Tài ↔ Nhung Tuyet Tran 2018) thay vì trình bày như đã ngã ngũ, và thêm Yao Takao cho nghi vấn niên đại bộ luật (D4).
- **Võ Nguyên Giáp** — mệnh đề "lần đầu" nay được rào bằng chính ca ngoại lệ ("Adwa 1896 là chiến thắng của Ethiopia, một nước độc lập") thay vì bỏ lửng (D2).
- **Hồ Chí Minh** — bản Yêu sách 1919 nay quy cho nhóm soạn chung và nói rõ Hội nghị Versailles **không tiếp nhận** (D1).

**Còn tồn (TL4):** các mệnh đề tối cao không kiểm chứng được vẫn rải rác — "một trong những tranh luận sử học kéo dài nhất của Việt Nam" (Triệu Đà), "hiếm gặp ở Đông Á đương thời" (Lý Thường Kiệt), "không có tiền lệ trong văn học Đông Á" (Hồ Xuân Hương), "trường hợp hiếm trong lịch sử thế giới" (Trần Nhân Tông), "quyết định quy hoạch có hệ quả dài nhất trong lịch sử Việt Nam" (Lý Thái Tổ). Vòng 1 xếp đây là vấn đề trung lập; bản vá không đụng tới, và *Ghi chú biên tập* không ghi nhận.

## Đã kiểm, đúng

Đây là phạm vi tôi **thực sự tra tới nguồn** và thấy bản vá đứng vững — không phải "không tìm thấy lỗi".

### Các bản vá viết tay (brief yêu cầu soi kỹ nhất)

| Bản vá | Kết quả | Bằng chứng |
|---|---|---|
| **An Dương Vương, `năm` mới: "trị vì 257–208 TCN theo ĐVSKTT (sử học hiện đại: Âu Lạc k. 208–179 TCN)"** | ✅ **Đúng cả hai vế.** ĐVSKTT Ngoại kỷ q.1 chép An Dương Vương "ở ngôi 50 năm", **甲辰 (257 TCN) → 癸巳 (208 TCN)** — 257–208 đúng 50 năm đếm gộp. Mốc hiện đại 208–179 khớp Bối cảnh nhóm ("thôn tính khoảng năm 179 TCN"). Cấu trúc "X theo ĐVSKTT (hiện đại: Y)" dán nhãn **đúng chiều** — ngược hẳn với mục Triệu Đà (H2) | quy đổi can chi; ĐVSKTT Ngoại kỷ q.1 |
| **An Dương Vương, "hơn hai triệu mét khối đất"** | ✅ khớp "over two million cubic metres of material were moved" | en.wikipedia "Citadel of Cổ Loa" |
| **An Dương Vương, trích dẫn Kim/Lai/Trịnh 2010** | ✅ **Chính xác tuyệt đối.** *Antiquity* **84 (326)**, 12/2010, tr. **1011–1027**; ba tác giả Nam C. Kim (UW–Madison), Lai Van Toi, Trinh Hoang Hiep (Viện Khảo cổ học) — đúng tên, đúng thứ tự, đúng tập, đúng năm | Cambridge Core; Gale OneFile |
| **An Dương Vương, "lớp luỹ sớm nhất có thể có trước niên đại truyền thống của ông"** | ✅ luỹ trong định niên **400–350 TCN**, sớm hơn mốc 257 TCN của ĐVSKTT | en.wikipedia "Citadel of Cổ Loa", ref. [7] |
| **Phùng Hưng, `năm: hoạt động k. 766–791` + câu Đỗ Anh Hàn** | ✅ Niên hiệu **Đại Lịch = 766–779** đúng; Toàn thư dồn vào **Tân Mùi 791** đúng; nhà Đường thu hồi An Nam **791** đúng; **sử Đường chỉ chép Đỗ Anh Hàn**, không nhắc Phùng Hưng — đúng. (Chỉ chữ "đương thời" sai — H5) | en.wikipedia "Đỗ Anh Hàn"; vi.wikipedia "Bố Cái Đại Vương" |
| **Tì-ni-đa-lưu-chi, "thư tịch Hán ghi ông dịch kinh ở Trường An năm 582"** | ✅ **Đúng, và là bản vá sắc nhất của cả vòng.** *Lịch đại tam bảo ký* chép 毘尼多流支 dịch **象頭精舍經** và **大乘方廣總持經** tại **大興善寺, Trường An, 開皇二年 (582)**. Câu này còn làm lộ đúng chỗ căng: nếu ông còn ở Trường An năm 582 thì mốc "sang Giao Châu 580" của *Thiền uyển tập anh* có vấn đề — và mục đã nói ra điều đó | zh.wikipedia 毘尼多流支; Lịch đại tam bảo ký |
| **Tì-ni-đa-lưu-chi, "Cuong Tu Nguyen (1997) cho là dựng hồi cố"** | ✅ khớp *Zen in Medieval Vietnam* (Hawai'i, 1997); mục nay phòng cả **tính có thật của dòng phái**, không chỉ niên đại (D5) | kiểm toán nguồn đã xác nhận tồn tại |
| **Mai Thúc Loan, "722" + quy Phan Huy Lê** | ✅ ĐVSKTT Ngoại kỷ q.5 chép năm **Nhâm Tuất (722)**; Tư trị thông giám q.212 định niên Khai Nguyên 10; mốc 713 đúng là tái dựng hiện đại của Phan Huy Lê và **đang tranh luận**. `năm` sửa từ 713–**723** sang k. 713–**722** ✅ | zh.wikisource 新唐書 q.207, 資治通鑑 q.212 |
| **Sĩ Nhiếp, câu Mâu Tử / Khương Tăng Hội** | ✅ Mâu Tử là **nho sĩ cư sĩ**, tác giả *Lý hoặc luận* tại Giao Chỉ — đúng; Khương Tăng Hội dịch kinh ở **Kiến Nghiệp từ 247**, sau khi Sĩ Nhiếp mất **226** — đúng. (Chỉ nhãn liên kết lệch — H9/L4) | kiểm chéo báo cáo nhóm CE01_09 |
| **Sĩ Nhiếp, "hai mươi tháp, năm trăm tăng, mười lăm quyển kinh dịch chỉ có trong Thiền uyển tập anh TK 14"** | ✅ đúng cả ba con số và đúng xuất xứ (lời Đàm Thiên tâu Tuỳ Văn Đế) | báo cáo nhóm CE01_09 mục 8 |
| **Lý Nam Đế, "542 đuổi Tiêu Tư / 544 xưng đế"** | ✅ tách đúng hai mốc mà bản cũ gộp làm một | ĐVSKTT Ngoại kỷ q.4 |
| **Lý Nam Đế, "Lý Phật Tử (Hậu Lý Nam Đế)"** | ✅ sửa đúng chỗ dễ gây nhầm với nhà Lý 1009–1225; "gần sáu mươi năm" (544→602 = 58) ✅ | |
| **Lý Nam Đế, chùa Khai Quốc "chỉ có trong bia và truyền thống đời sau, không có trong Toàn thư"** | ✅ đúng — chứng cứ sớm nhất là *Trấn Quốc tự bi ký* (1639) | |
| **Lê Thánh Tông, Yao Takao** | ✅ Bài có thật, trong *Việt Nam học — Kỷ yếu Hội thảo quốc tế lần thứ tư* (2013), và luận điểm được tóm **đúng**. ⚠️ nhan đề bài là **"Nguồn gốc của Quốc triều hình luật không phải là luật Hồng Đức"**; "Luật Quang Thuận đã từng tồn tại?" là **tên một tiểu mục** bên trong. Nên dẫn nhan đề bài | dulieu.itrithuc.vn, kỷ yếu bản PDF |
| **Lê Thánh Tông, "dựa chủ yếu vào Đường luật chứ không phải luật Minh"** | ✅ theo chính bảng đối chiếu của Insun Yu: ~261/722 điều từ Đường luật, chỉ **53** từ Đại Minh luật | Insun Yu (1990) |
| **Lê Thánh Tông, "Insun Yu và Tạ Văn Tài đọc đó là quyền ngang bằng, Nhung Tuyet Tran (2018) phản bác"** | ✅ **Đúng cả nội dung lẫn chiều tranh luận.** *Familial Properties: Gender, State, and Society in Early Modern Vietnam, 1463–1778*, University of Hawai'i Press, **2018** — Tran bác cách đọc "con gái thừa kế ngang con trai", và Insun Yu (cùng Sun Laichen, Miyazawa Chihiro) phản biện lại | uhpress.hawaii.edu; H-Net review |
| **Lê Thánh Tông, "hơn ba thế kỷ, tới Hoàng Việt luật lệ 1812–1815"** | ✅ sửa đúng "gần bốn thế kỷ" của bản cũ (1483→1812 = 329 năm); "gần ba mươi bảy năm" trị vì ✅ (6/1460–2/1497); "mười hai rồi mười ba đạo thừa tuyên (1466, 1471)" ✅ | |
| **Nguyễn Bỉnh Khiêm, "khả dĩ dung thân" + "bản 'vạn đại' có lẽ là chữ đời Nguyễn sửa"** | ✅ **Đúng, và đúng cả phần tinh tế.** Bản sớm là 「可以容身」; 「萬代容身」 là dạng đời Nguyễn sửa để khẳng định nghiệp lâu dài của dòng họ | danviet.vn; vanhoavaphattrien.vn |
| **de Rhodes, "khoảng chín năm"** | ✅ en.wikipedia tổng kết "approximately 9 years" (Đàng Ngoài 3/1627–1630 ≈ 3 năm + Đàng Trong ≈ 6 năm), và xác nhận 1630–1640 ông ở Ma Cao. Sửa đúng "hai mươi năm" của bản cũ (N8) | en.wikipedia "Alexandre de Rhodes" |
| **Lê Lợi, "hơn tám vạn quân Minh… (Minh thực lục ghi 84.640 người)"** | ✅ **Đúng con số và đúng nguồn.** Minh thực lục chép **84.640** quan quân được Lê Lợi cấp thuyền, ngựa, lương cho về nước, ngày 29/12/1427. Các mốc khác cũng khớp: Minh cai trị từ 1407 → "gần mười một năm" ✅; Hậu Trần 1407–1414 = "bảy năm" ✅; "sáu năm đầu" 1418–1424 ✅ | danviet.vn; hoangthanhthanglong.vn |
| **Quang Trung, "ba mươi chín ngày" + "Tam Điệp chỉ năm sáu ngày"** | ✅ 22/12/1788 (25 tháng 11 Mậu Thân, rời Phú Xuân) → 30/1/1789 (mồng 5 Tết, vào Thăng Long) = **đúng 39 ngày**; chặng Tam Điệp (30 Tết) → Thăng Long (mồng 5) = 5 ngày ✅. "mười tám năm" (1771→1789) ✅; "tuổi ba mươi chín" (1753→1792) ✅; "sụp sau đó mười năm" (1792→1802) ✅; nguồn *Tạ Chí Đại Trường, Lịch sử nội chiến ở Việt Nam **1771–1802** (1973)* — đúng nhan đề và đúng khung năm khớp mốc 1771 của văn xuôi | đối chiếu âm–dương lịch; vi.wikipedia "Trận Ngọc Hồi – Đống Đa" |
| **Vạn Hạnh, `năm: k. 938–1025 (bản hiệu đính Trần Văn Giáp: 1018)`** | ✅ **Đúng và xử lý khéo.** *Thiền uyển tập anh* truyền bản chép **Thuận Thiên 16 = 1025**; Trần Văn Giáp hiệu đính thành Thuận Thiên 9 = **1018**, trùng ĐVSKTT (Mậu Ngọ 1018). Trường giữ 1025 để khớp Wikidata Q1076219, ngoặc nêu bản hiệu đính kèm **tên người hiệu đính** — giải đúng chỗ báo cáo vòng 1 từng ghi ngược (N14) | ghi chú bản vá mục C; đối chiếu niên hiệu |
| **Vạn Hạnh, "sau Quốc tộ của Đỗ Pháp Thuận và Vương lang quy của Khuông Việt"** | ✅ gỡ đúng mâu thuẫn N6 (không còn gọi bài kệ là "sớm nhất" ngay trên hai tác giả sớm hơn) | |
| **Lý Thường Kiệt, `lĩnh vực: Quân sự, Chính trị/Nhà nước`** | ✅ **Lựa chọn đúng.** Bỏ "Văn học" gỡ được việc ngầm nhận tác quyền *Nam quốc sơn hà* (N3); thay bằng Chính trị/Nhà nước là có căn cứ — ông làm Thái uý, cầm triều chính, chủ trì bang giao với Tống, đúng với chính nguồn đang dẫn (Hoàng Xuân Hãn 1949). Nhóm CE10_14 vẫn đủ lĩnh vực, lint **không sinh cảnh báo mới** | lint-ch90.txt: 0 ERROR, WARN duy nhất ở BCE03_01 |
| **Lý Thường Kiệt, "không thư tịch cổ nào ghi tác giả"** | ✅ đúng mức — nêu tình trạng **khuyết danh**, không khẳng định ngược rằng ông không viết | |
| **Tôn Thất Tùng, dòng Nguồn** | ✅ *The Lancet* **281** (1963), tr. **192–193**, đồng tác giả **Nguyễn Dương Quang** — thay đúng một trích dẫn **không tồn tại** (S10). Bài *Presse Médicale* thật của ông là 1965, không phải 1963 | Crossref 10.1016/S0140-6736(63)91210-8 |
| **Võ Nguyên Giáp, "chuẩn bị thêm gần bảy tuần"** | ✅ đổi phương châm 26/1/1954 → nổ súng 13/3/1954 = 46 ngày ≈ 6,6 tuần. "chỉ huy quân đội từ 1944" ✅ | nhandan.vn, vnexpress.net |
| **Thích Nhất Hạnh, "ba mươi chín năm"** | ✅ 1966–2005 | plumvillage.org |
| **Triệu Đà, "Ứng viên cùng giai đoạn là Lữ Gia"** | ✅ vá đúng N4 — nêu được ứng viên đích danh kèm lý do counterfactual (d) | |
| **Triệu Đà, "cai trị bảy mươi năm"** | ✅ 207→137 = 70 năm trôi qua (ĐVSKTT đếm gộp 71). Sửa đúng "gần một thế kỷ" của bản cũ (N12) | |

### Kiểm toàn file bằng script (không chỉ đọc)
- **40 mục / 5 nhóm**, phân bố **2 · 8 · 10 · 10 · 10** — khớp mọi con số trong Ghi chú biên tập.
- **126 dòng liên kết** (88 trỏ ID nội bộ): 0 ID không tồn tại, 0 liên kết tự trỏ, 0 khối quá 3 mục, 0 giá trị ngoài từ vựng, 0 bất khả niên đại, 0 liên kết "trực tiếp" không giao đời sống.
- **40 dòng Nguồn**: không dòng nào rỗng; mọi mục có đủ `Kế thừa từ` và `Ảnh hưởng tới`.
- **35 bản vá trong hai file JSON**: tôi kiểm từng cặp `old`/`new` trên file hiện tại — **33/33 patch nội dung đã áp sạch** (không còn chuỗi `old` nào sót), và **2 patch `trunglap` chưa áp**, đúng như brief mô tả. Không có patch nào áp nửa vời hay áp hai lần.
- **Lint hiện tại**: `ERROR 0 · WARN 1 · INFO 4`.

---

## Không kiểm chứng được

**1. Toàn văn Kim, Lai & Trịnh 2010.** Đây là lỗ hổng ảnh hưởng trực tiếp tới **H3**. `os.pennds.org` từ chối kết nối (ECONNREFUSED), Cambridge Core trả **429**, ResearchGate và Academia.edu cần đăng nhập. Tôi kết luận về vị trí khuôn đúc Cổ Loa dựa vào nguồn Việt Nam chuyên trách (thanhcoloa.vn — ban quản lý di tích; kinhtedothi.vn — hồ sơ Bảo vật quốc gia), đều quy bộ 11 khuôn đá về **Đền Thượng, 2004–2007**. Một bản tóm lược thứ cấp lại nhắc tới khuôn đúc ở khu Cầu Vực. **Cần mở trang in bài báo** trước khi chốt H3 là Sai hay chỉ là câu viết mơ hồ.

**2. Ba mục KHÔNG KIỂM ĐƯỢC của kiểm toán nguồn — tôi gỡ được 0/3.**
- *Trần Văn Giáp, Tìm hiểu kho sách Hán Nôm* cho Chu Văn An: vẫn không tra được mục lục chi tiết để xác nhận có mục khảo *Tứ thư thuyết ước* / *Tiều ẩn thi tập*. Phải mở bản in tập I (1970) hoặc bản 2003.
- *ĐVSKTT, Bản kỷ tục biên* năm Ất Dậu 1585 cho Nguyễn Bỉnh Khiêm: zh.wikisource trả **404** cho quyển tương ứng; tìm 阮秉謙 trong bản Hán văn trực tuyến không ra. Xác nhận được **năm mất 1585** và tước **Trình Quốc công** từ nguồn thứ cấp, nhưng **không** xác nhận được chính Bản kỷ tục biên có chép.
- *Li Tana, Nguyễn Cochinchina* (1998) cho Đào Duy Từ: không mở được toàn văn.

Tôi **chỉ gỡ được chỗ thứ tư** (báo cáo Cổ Loa vô danh) — và chính vì nó đã được thay bằng một công bố định danh được, nên G1 ở trên đề nghị hạ con số xuống **ba**.

**3. Nguồn gốc câu "Hoành Sơn nhất đái" có thật sự **lần đầu** xuất hiện ở Đại Nam thực lục tiền biên hay không.** Nội dung câu và lịch sử dị bản "khả dĩ" / "vạn đại" thì tôi xác nhận được. Nhưng mệnh đề "**chỉ** chép trong Đại Nam thực lục tiền biên hai thế kỷ rưỡi sau" đòi chứng minh **không** có bản chép sớm hơn (*Trịnh–Nguyễn diễn chí*, *Việt Nam khai quốc chí truyện*…), và tôi không kiểm được điều đó. Thêm: 1558 → *Tiền biên* soạn k. 1821–1844 là **gần ba thế kỷ**, không hẳn "hai thế kỷ rưỡi" — sai số nằm trong mức chấp nhận được nhưng nghiêng về phía nói nhẹ.

**4. Tôi không kiểm lại Q-ID Wikidata, và không kiểm lại trường `độ tin cậy niên đại`.** Brief hướng tôi vào hồi quy; vòng 1 đã duyệt các trường này. Ngoại lệ duy nhất là ba trường `năm` mà brief nêu đích danh (An Dương Vương, Triệu Đà, Vạn Hạnh) — đã kiểm, kết quả ở trên.

**5. Bốn mục mà vòng 1 tự khai chỉ soát nội tại, tôi cũng không tra độc lập** (ngân sách dồn vào các bản vá viết tay): `CE15_18-05` Nguyễn Hoàng, `CE15_18-06` Đào Duy Từ, `CE15_18-08` Lê Quý Đôn, `CE15_18-09` Lê Hữu Trác. Tôi chỉ đối chiếu được vài mốc rời (Nam tiến "bắt đầu từ 1069" ✅; luỹ Thầy và khung giao tranh 1631–1672 ✅). **Bốn mục này vẫn là vùng tối sau hai vòng rà soát** — nên được ưu tiên ở vòng sau.

**6. Lỗ hổng đối chiếu thư mục mà vòng 1 nêu vẫn chưa được lấp.** Danh sách ~22 công trình hiện đại chưa kiểm tồn tại (Hoàng Xuân Hãn 1949, Li Tana 1998, Choi Byung Wook 2004, Vĩnh Sính 2009, Duiker 2000, Fall 1966, Marr 1971, Nguyễn Lang, Lê Mạnh Thát, Trần Đình Sử 2002, Đỗ Lai Thuý 1999, Nguyễn Văn Trung 1993…) vẫn **chưa ai chạy**. Tôi chỉ bổ sung được bốn cái trong vòng này (Kim/Lai/Trịnh 2010, Nhung Tuyet Tran 2018, Yao Takao 2013, Ngô Đức Thọ 1986 — tất cả **tồn tại và đúng**). Với tỷ lệ hỏng từng tìm thấy ở phần đã kiểm, đây vẫn là rủi ro xuất bản lớn nhất còn lại của file, lớn hơn mọi phát hiện trong báo cáo này.

**7. Hai chỗ tôi cố ý không phán:** (a) mốc khởi đầu "đúng" của triều Triệu (204 hay 207 TCN) — tôi chỉ chứng minh được **136 là sai** và **137 là mốc đồng thuận**, việc chọn mốc đầu là quyết định biên tập; (b) *Thất trảm sớ* năm nào — mục hiện viết "ĐVSKTT không ghi năm, niên đại thường dẫn là 1358", đúng theo khuyến nghị vòng 1, và tôi không tìm được gì mới.

---

## Thứ tự việc cần làm

1. **Sáu chỗ Sai, vá trước khi in:** H1 (Hậu Hán thư q.86), H2 (bỏ "136"), H4 (chánh tổng tài, hai chỗ), H5 (bỏ "đương thời", hai chỗ), **L1 (đổi `-04` thành `-05`)**, L2 (`kế thừa · trực tiếp` cho MLK).
2. **Bốn ghi chú biên tập lỗi thời:** G1 (bốn→ba), G2 (thêm Lê Văn Hưu), G3 (lý do loại xuyên nhóm), G4 (đếm lĩnh vực Văn học).
3. **Kiểm H3 trên bản in Kim/Lai/Trịnh 2010** rồi sửa câu Cổ Loa theo kết quả.
4. **Bổ sung vòng đối xứng liên kết vào `atlaslib/lint.py`** — hiện chỉ quét chiều `Kế thừa từ`, nên mọi `Ảnh hưởng tới` trỏ sai đích đều đi lọt (L1 là bằng chứng).
5. **Quyết TL3** (T2/T3): hoặc áp hai câu `trunglap` — với Võ Nguyên Giáp dùng **bản của file ghi chú**, không phải bản JSON — hoặc ghi rõ trong Ghi chú biên tập rằng chuẩn chưa được áp.
6. **Chạy vòng đối chiếu thư mục riêng** cho ~22 công trình hiện đại chưa kiểm (mục 6 ở trên).
