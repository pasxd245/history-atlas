# Bình duyệt mức bằng chứng `trực tiếp` — 39 cạnh đích-là-văn-bản-tự-do, Chapter 1–3

Phạm vi: 39 cạnh đang mang `trực tiếp` mà đích **không** phải ID mục trong atlas
mà là văn bản tự do nêu tên người, thuộc chapter 1, 2, 3.
Nguồn danh sách: `scratchpad/tructiep-A.md`.

Tiêu chí áp dụng: `CONTRIBUTING.md` quy tắc 9 + khối "Quy ước mức bằng chứng".
- `trực tiếp` = tiếp xúc người với người chứng minh được bằng nguồn **VÀ** đời hai người chồng lấn.
- `qua trường phái` = mặc định cho mọi cặp không chồng đời, **và cho mọi đích không phải một con người**.
- `suy đoán học giả` = không có đường truyền chứng minh được.

Phương pháp: tra Wikidata qua `wbgetentities` (P569 sinh / P570 mất / P22 cha / P25 mẹ /
P40 con / P3373 anh chị em / P39 chức vụ kèm P580–P582), đối chiếu với trường `năm:` của
mục nguồn trong `content/chNN.md`; khi cần thì đọc thêm phần mở đầu bài Wikipedia tiếng Anh
qua `action=query&prop=extracts`. Mọi lời gọi mạng dùng User-Agent `history-atlas/0.1 (research)`.

**Cảnh báo phương pháp đọc trước khi dùng báo cáo này.** Phần lớn các cạnh dưới đây là quan hệ
**cha–con / anh–em / vua trước–vua sau**. Quan hệ huyết thống trên Wikidata (P22/P25/P40) chứng
minh được *có chồng đời*, nhưng tự nó **chưa** chứng minh "tiếp xúc chứng minh được bằng nguồn"
theo nghĩa hẹp nhất — nó chỉ khiến tiếp xúc gần như chắc chắn. Tôi ghi `GIỮ` cho những ca này
và nói rõ cơ sở, để chủ dự án biết đang chấp nhận suy luận nào.

**Bẫy trường `năm:`.** Rất nhiều mục ở Chapter 1 ghi `trị vì …` hoặc `hoạt động …` chứ không
phải sinh–mất. Khi gặp, tôi **không** trừ năm trực tiếp mà nói rõ, rồi chuyển sang chứng cứ khác
(huyết thống, văn bản kế vị). Ca nào không còn chứng cứ nào khác thì ghi `[KHÔNG KIỂM ĐƯỢC]`.

---

## Ca 1 — Chapter 1 (8 cạnh)

### 1.1 `CH01-BCE11_9-02` Chu Vũ Vương → **Chu Văn Vương** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Chu Văn Vương, Q698909 (nhãn en "King Wen of Zhou").
2. **Chồng đời?** Trường `năm:` của mục nguồn là `trị vì k. 1046–1043 TCN` — **đây là niên đại trị vì,
   không phải sinh–mất, nên không trừ năm trực tiếp được** (bẫy đã nêu). Chứng cứ thay thế:
   Wikidata Q698909 `P40 con` có Q1061289 (Chu Vũ Vương), và Q1061289 `P22 cha` = Q698909 — quan hệ
   cha–con hai chiều khớp. Văn Vương mất k. 1050 TCN (Q698909 P570, prec 9), Vũ Vương lên ngôi k. 1046.
   Cha–con thì chồng đời theo định nghĩa. **Có chồng đời.**
3. **Tiếp xúc chứng thực được?** Trong hệ truyền thống mà chính mục này dẫn (Thượng thư; Shaughnessy,
   *Sources of Western Zhou History*, 1991), Vũ Vương kế tục sự nghiệp của cha và tự dẫn chiếu "mệnh"
   cha đã nhận. Lưu ý thẳng: đây là **truyền thống văn bản đời sau**, không phải văn khắc đương thời;
   mục đã tự để `độ tin cậy niên đại: Thấp`. Trong khung ấy, tiếp xúc cha–con là chứng thực được.

**→ GIỮ `trực tiếp`.**

### 1.2 `CH01-BCE14_12-02` Akhenaten → **Amenhotep III** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Amenhotep III, Q42606.
2. **Chồng đời?** `năm:` mục nguồn là `trị vì k. 1353–1336 TCN` — **niên đại trị vì, không so trực tiếp được.**
   Chứng cứ thay thế: Q81794 (Akhenaten) `P22 cha` = Q42606; Q42606 `P570 mất` = −1351 (prec 9),
   tức sau khi Akhenaten lên ngôi k. 1353 theo chính trường `năm:` của mục. **Có chồng đời**, và còn
   có khả năng đồng trị (coregency) — một tranh luận chưa ngã ngũ trong Ai Cập học, không cần giải ở đây.
3. **Tiếp xúc chứng thực được?** Cha–con, cùng một triều đình Thebes; mục tự viết Amenhotep III
   "đã nâng Aten lên trước đó", tức đường truyền đi qua chính triều đình ấy.

**→ GIỮ `trực tiếp`.**

### 1.3 `CH01-BCE14_12-04` Tukulti-Ninurta I → **Shalmaneser I** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Shalmaneser I, Q310142.
2. **Chồng đời?** `năm:` mục nguồn là `trị vì k. 1243–1207 TCN` — **niên đại trị vì.** Wikidata cho cả hai
   chỉ có độ chính xác **thế kỷ** (Q310142 P569 −1400 / P570 −1300 prec 7; Q299013 P569/P570 −1300 prec 7),
   **không dùng để trừ năm được.** Chứng cứ thay thế: Q310142 `P40 con` = Q299013 và Q299013 `P22 cha`
   = Q310142 — cha–con, hai chiều khớp. **Có chồng đời.**
3. **Tiếp xúc chứng thực được?** Cha truyền con nối trực tiếp trên ngai Assyria; danh sách vua Assyria
   và văn khắc hoàng gia (Grayson, *Assyrian Rulers of the Third and Second Millennia BC*, 1987 — đúng
   nguồn mục đang dẫn) ghi Tukulti-Ninurta I là con và người kế vị liền kề.

**→ GIỮ `trực tiếp`.**

### 1.4 `CH01-BCE14_12-06` Ramesses II → **Seti I** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Seti I, Q157918.
2. **Chồng đời?** Đây là ca **so được trực tiếp**: mục nguồn ghi `k. 1303–1213 TCN` (sinh–mất thật),
   Q157918 Seti I sinh −1323 / mất −1279 (prec 9). Chồng lấn k. 1303–1279, **24 năm**.
3. **Tiếp xúc chứng thực được?** Q1523 `P22 cha` = Q157918. Ngoài huyết thống còn có tiếp xúc công vụ:
   Ramesses II được đặt làm hoàng tử nhiếp chính và đi theo cha trong các chiến dịch Levant — đúng điều
   mục "Vì sao chọn" đang viện (Kitchen, *Pharaoh Triumphant*, 1982, là nguồn mục đang dẫn).

**→ GIỮ `trực tiếp`.** Ca mạnh nhất trong Chapter 1.

### 1.5 `CH01-BCE17_15-02` Khyan → **Apophis và giai đoạn Hyksos muộn** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** **Không hẳn — cụm hỗn hợp.** Vế một là một con người (Apophis/Apepi,
   Q322169); vế hai, "giai đoạn Hyksos muộn", là một **giai đoạn lịch sử**, không phải người. Theo quy ước,
   riêng vế hai đã đủ đẩy cạnh về mức mặc định `qua trường phái`.
2. **Chồng đời?** **Không chứng minh được, và nhiều khả năng là không.** `năm:` mục nguồn là
   `trị vì k. 1650–1620 TCN` — **niên đại trị vì.** Wikidata Q440496 (Khyan) chỉ có độ chính xác thế kỷ
   (−1700/−1600 prec 7), vô dụng. Dùng nguồn chữ: Wikipedia en "Khyan" ghi ông trị vì *nửa sau thế kỷ 17 TCN*;
   Wikipedia en "Apepi" ghi Apepi trị vì 40 năm trong *nửa đầu thế kỷ 16 TCN* theo Turin Canon. Hai khoảng
   ấy **không giao nhau**. Thêm nữa, chính mục này ghi khai quật Tell Edfu (Moeller & Marouard 2011) đẩy
   Khyan **sớm hơn** tới k. 1700 — tức càng đẩy xa Apophis, không kéo lại gần.
3. **Tiếp xúc chứng thực được?** Không có. Không nguồn nào đặt hai người trong cùng một khung thời gian,
   nói gì tới một cuộc gặp.

**→ HẠ xuống `qua trường phái`.** Hai lý do độc lập, mỗi lý do đủ một mình: đích là cụm hỗn hợp,
và hai đời không chồng lấn.

> **Văn bản thay thế đề xuất** (dòng trong mục `Ảnh hưởng tới`):
> `- Apophis và giai đoạn Hyksos muộn · kế thừa · qua trường phái`
>
> Tự soi lại câu thay thế của mình: dòng này **vẫn** để nguyên cụm hỗn hợp "Apophis và giai đoạn
> Hyksos muộn" — nó chỉ sửa mức bằng chứng, không sửa cái khiến mức ấy sai. Nếu chủ dự án muốn dọn
> triệt để thì tách làm hai dòng, nhưng **tôi không đề xuất tách**: vế "Apophis" đứng một mình vẫn
> không chồng đời, nên tách ra cũng vẫn là `qua trường phái`, chỉ thêm một dòng mà không thêm thông tin.

### 1.6 `CH01-BCE17_15-03` Ahmose I → **Apophis và Khamudi, hai vua Hyksos cuối** · Kế thừa từ · `phản bác`

1. **Đích có phải một con người?** **Hai con người**, không lẫn thể chế: Apophis/Apepi (Q322169) và
   Khamudi (Q879157). Cụm nhiều người nhưng không hỗn hợp, nên không rơi vào mệnh đề "đích không phải
   một con người".
2. **Chồng đời?** **Có.** Mục nguồn ghi `k. 1560–1525 TCN` (sinh–mất thật, so được). Wikipedia en "Apepi"
   nói thẳng: Apepi *sống lâu hơn Kamose nhưng không lâu hơn Ahmose I* — tức hai đời chồng lấn, không cần
   suy luận. Khamudi là vua Hyksos cuối, bị chính Ahmose I đánh đổ, nên chồng đời là hệ quả hiển nhiên.
   (Ghi chú chất lượng dữ liệu, không ảnh hưởng kết luận: Q879157 Khamudi có P569 sinh −1549 **sau** P570
   mất −1600 — Wikidata ở đây tự mâu thuẫn, cả hai đều prec 7. Tôi **không** dùng cặp số này.)
3. **Tiếp xúc chứng thực được?** Có, dạng đối đầu quân sự có tên hai bên: chiến dịch chiếm Avaris rồi
   truy kích Sharuhen, chép trong tiểu sử mộ Ahmose con bà Ibana (El-Kab) — đúng nguồn mục đang dẫn.
   Lưu ý diễn giải: CONTRIBUTING liệt kê "thầy–trò, đồng sự, thư từ, cùng một hội đồng/triều đình" như
   **ví dụ**, không phải danh sách đóng. Hai chủ soái đối địch trong một cuộc chiến có sử liệu là tiếp
   xúc người với người theo nghĩa chặt nhất. Nếu chủ dự án muốn đọc danh sách ấy là **đóng**, thì ca này
   phải hạ — nên tôi nêu rõ chỗ rẽ thay vì giấu nó.

**→ GIỮ `trực tiếp`.**

### 1.7 `CH01-BCE17_15-03` Ahmose I → **Kamose và Ahhotep** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Hai con người: Kamose (Q19327) và Ahhotep I (Q239678).
2. **Chồng đời?** **Có, với một vết nứt nhỏ ở vế Kamose.** Mục nguồn `k. 1560–1525 TCN`.
   - Ahhotep I: Q239678 sinh −1560 / mất −1530 (prec 9) → chồng lấn k. 1560–1530, **30 năm**.
     Q7222 `P25 mẹ` = Q239678 xác nhận quan hệ mẹ–con.
   - Kamose: Q19327 mất −1549 (prec 9), sinh chỉ có prec 7 (−1600, tức "thế kỷ 17 TCN", không dùng được).
     Ahmose I sinh k. 1560 → chồng lấn k. 1560–1549, **khoảng 11 năm**, và Ahmose còn rất nhỏ trong
     khoảng đó. Q7222 `P3373 anh chị em` có Q19327, và cả hai cùng `P22 cha` = Q31526 (Seqenenre Tao).
     Quan hệ anh em là chắc; **"tiếp xúc" ở đây là tiếp xúc giữa một người lớn và một đứa trẻ**, không
     phải trao truyền giữa hai người trưởng thành.
3. **Tiếp xúc chứng thực được?** Cùng một gia tộc Thebes, cùng một triều đình — khớp đúng ví dụ
   "cùng ngồi một triều đình" của CONTRIBUTING. Vế Ahhotep còn mạnh hơn: bà được ghi công nhiếp chính
   giữ miền nam trong thời Ahmose I còn nhỏ, tức tiếp xúc là quan hệ cai trị thực tế, không chỉ huyết thống.

**→ GIỮ `trực tiếp`.** Nhưng nói thẳng: cạnh này đứng được **nhờ vế Ahhotep**. Nếu tách riêng, vế
Kamose là ca yếu nhất trong Chapter 1 — ảnh hưởng của Kamose lên Ahmose I trên thực tế truyền qua
**sự nghiệp để lại**, không qua dạy dỗ, vì Kamose mất khi Ahmose còn là trẻ con.

### 1.8 `CH01-BCE17_15-06` Mursili I → **Hattusili I** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Hattusili I, Q299472 (nhãn en "Hattusili I", mô tả "Hittite king").
2. **Chồng đời?** **Có, nhưng không chứng minh bằng phép trừ năm được.** `năm:` mục nguồn là
   `trị vì k. 1620–1590 TCN` — **niên đại trị vì.** Q222536 (Mursili I) sinh chỉ prec 7 (−1700). Phép trừ
   bất khả. Chứng cứ thay thế là **thứ tự kế vị liền kề**: Q299472 Hattusili I mất −1620 (prec 9), đúng
   năm Mursili I lên ngôi theo trường `năm:`. Kế vị liền kề đòi hai người cùng sống tại thời điểm chuyển giao.
3. **Tiếp xúc chứng thực được?** Có, và bằng một văn bản Hittite cụ thể: **Sắc lệnh Telipinu** — đúng
   nguồn mục này đang dẫn — chép việc Hattusili I truất những người thừa kế trước rồi chỉ định Mursili
   làm người nối ngôi trước khi mất. Đó là tiếp xúc người với người có văn bản.
   **Đính chính một chi tiết trong thân mục, không liên quan tới mức bằng chứng:** mục "Vì sao chọn"
   gọi Hattusili I là **"cha nuôi"** của Mursili I. Wikidata ghi Q222536 `P22 cha` = Q1164824 (Marattisz),
   và Q1164824 `P22 cha` = Q695778, vốn là **anh chị em** (P3373) của Hattusili I — tức theo phả hệ ấy
   Hattusili I là ông/chú-ông, không phải cha đẻ. Chữ "cha nuôi" khớp với việc **nhận làm người thừa kế**
   trong Sắc lệnh Telipinu, nên không sai; nhưng nếu chủ dự án muốn chặt chữ thì "người chỉ định ông
   làm thừa kế" chính xác hơn "cha nuôi". Đây là **gợi ý tuỳ chọn**, không phải lỗi chặn.

**→ GIỮ `trực tiếp`.**

**Tiểu kết Ca 1:** GIỮ 7 · HẠ 1 (`CH01-BCE17_15-02` → Apophis và giai đoạn Hyksos muộn) · [KHÔNG KIỂM ĐƯỢC] 0.

---

## Ca 2 — Chapter 2, nhóm BCE05 (11 cạnh)

Niên đại mục nguồn ở nhóm này **đều là sinh–mất thật**, không phải `trị vì`/`hoạt động`
(trừ ca Pāṇini, xem 2.8), nên phép trừ năm dùng được — khác hẳn Ca 1.

### 2.1 `CH02-BCE05-01` Socrates [k. 470–399 TCN] → **Plato (Πλάτων)** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Plato, Q859.
2. **Chồng đời?** Có. Q859 sinh k. −428/−427, mất −347. Socrates k. 470–399. Chồng lấn **k. 428–399,
   khoảng 29 năm**.
3. **Tiếp xúc chứng thực được?** Có, loại mạnh nhất: Q913 `P802 học trò` có Q859; Q859 `P1066 học trò của`
   có Q913 — hai chiều khớp. Plato tự đặt mình trong nhóm có mặt tại phiên xử (Apologia 34a, 38b) — đúng
   nguồn mục đang dẫn.

**→ GIỮ `trực tiếp`.**

> **Phát hiện ngoài phạm vi, cần chủ dự án xử lý riêng:** Plato **đã có mục trong atlas**,
> `CH03-BCE04-01` (`k. 427–347 TCN`). Cạnh này lẽ ra là liên kết theo ID chứ không phải văn bản tự do.
> Đây là lỗi *loại khác* với lỗi mức bằng chứng tôi được giao, nên tôi **không** đề xuất sửa ở đây —
> nhưng nó giải thích vì sao cạnh lọt vào danh sách "đích là văn bản tự do" ngay từ đầu.
> Nâng lên ID sẽ kéo theo yêu cầu đối xứng hai chiều, nên là một thay đổi riêng, phải cân nhắc riêng.

### 2.2 `CH02-BCE05-01` Socrates → **Antisthenes** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Antisthenes, Q179149.
2. **Chồng đời?** Có. Q179149 sinh −445, mất −365 (cả hai prec 9). Chồng lấn với Socrates
   **k. 445–399, khoảng 46 năm**.
3. **Tiếp xúc chứng thực được?** Có. Q179149 `P1066 học trò của` = Q913. Antisthenes được kể là có mặt
   bên Socrates lúc ông chết (Plato, *Phaedo* 59b).

**→ GIỮ `trực tiếp`.** Không có mục atlas trùng tên, nên đây đúng là một đích văn bản tự do hợp lệ.

### 2.3 `CH02-BCE05-02` Parmenides [k. 515–450 TCN] → **Zeno xứ Elea** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Zeno xứ Elea, Q132157 — **không** nhầm với Zeno xứ Citium
   (Q48305), người đã có mục riêng `CH03-BCE03-07`. Hai Zeno khác nhau; mục này trỏ đúng người.
2. **Chồng đời?** Có. Q132157 sinh −490, mất −425. Chồng lấn với Parmenides **k. 490–450, khoảng 40 năm**.
3. **Tiếp xúc chứng thực được?** Có. Q132157 `P1066 học trò của` = Q125551, và Q125551 `P802 học trò`
   có Q132157 — hai chiều khớp. Chính mục "Vì sao chọn" cũng viết "Zeno chỉ xây nghịch lý để bảo vệ
   lập luận đã có của thầy".

**→ GIỮ `trực tiếp`.**

### 2.4 `CH02-BCE05-03` Herodotus [k. 484–425 TCN] → **Hecataeus xứ Miletus** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Hecataeus xứ Miletus, Q242270.
2. **Chồng đời?** **Trên giấy thì có, nhưng chồng lấn rỗng.** Q242270 mất −475 (prec 9); sinh chỉ prec 7
   (−600, tức "thế kỷ 6 TCN", không dùng được). Herodotus sinh k. 484 (Q26825, prec 9). Chồng lấn danh
   nghĩa **k. 484–475, khoảng 9 năm — và Herodotus là một đứa trẻ dưới mười tuổi suốt quãng đó.**
3. **Tiếp xúc chứng thực được?** **Không.** Herodotus biết Hecataeus qua **tác phẩm**: ông trích dẫn,
   dùng lại và bác bỏ Hecataeus trong *Historíai* (II.143; V.36; V.125; VI.137). Ở V.36 Hecataeus xuất
   hiện với tư cách **nhân vật trong trình thuật** — người khuyên dân Ionia năm 499 TCN — chứ không phải
   người Herodotus gặp. Không nguồn nào đặt hai người trong cùng một phòng.

**→ HẠ xuống `qua trường phái`.** Đây là ca mẫu của định nghĩa: đường truyền là **văn bản**, đúng nghĩa
đen. Chồng đời tồn tại về số học nhưng không đỡ nổi `trực tiếp`, vì điều kiện chồng đời là **cần**,
không phải **đủ** — vế "tiếp xúc chứng minh được bằng nguồn" mới là vế quyết định, và nó trống.

> **Văn bản thay thế đề xuất:** `- Hecataeus xứ Miletus · kế thừa · qua trường phái`
>
> Tự soi lại: dòng này không khẳng định gì mới ngoài mức bằng chứng, nên không mang theo lỗi nào.
> Tôi **cố ý không** viết "Hecataeus xứ Miletus (qua *Períodos gês*)" dù đó là đường truyền thật:
> thêm tên tác phẩm vào đây là thêm một khẳng định về **thể loại và nhan đề** mà tôi chưa mở mục lục
> để kiểm — đúng loại lỗi quy tắc 3 và 7 của CONTRIBUTING cảnh báo. Để trống an toàn hơn.

### 2.5 `CH02-BCE05-03` Herodotus → **Thucydides (Θουκυδίδης)** · Ảnh hưởng tới · `phản bác`

1. **Đích có phải một con người?** Có. Thucydides, Q41683.
2. **Chồng đời?** Có, và rộng. Q41683 sinh −460 (prec 8), mất −395. Chồng lấn với Herodotus
   **k. 460–425, khoảng 35 năm**. Điều kiện cần **đạt**.
3. **Tiếp xúc chứng thực được?** **Không.** Hai dữ kiện ngược chiều nhau và dữ kiện phủ định thắng:
   - Giai thoại Thucydides thiếu niên nghe Herodotus diễn giảng rồi bật khóc, và Herodotus quay sang
     nói với cha cậu, **là nguồn duy nhất cho một cuộc gặp** — và chính nó bị xếp là *disputed*,
     "most likely from a later Greek or Roman account of his life" (Wikipedia en, mục "Thucydides",
     phần "Evidence from the classical period"; gốc là Marcellinus, *Vita Thucydidis*). Dùng nó làm
     bằng chứng là dựng `trực tiếp` trên một giai thoại hậu kỳ.
   - **Thucydides không hề nhắc tên Herodotus** trong toàn bộ tác phẩm; chỗ được cho là ám chỉ ông
     chỉ là câu mở I.22 về "không xen chuyện hoang đường" (cùng nguồn, mục "Comparison with Herodotus").
     Tức sự `phản bác` có thật, nhưng nó diễn ra **giữa hai văn bản**, không giữa hai người.

**→ HẠ xuống `qua trường phái`.**

> **Văn bản thay thế đề xuất:** `- Thucydides (Θουκυδίδης) · phản bác · qua trường phái`
>
> Tự soi lại: giữ nguyên `phản bác` là **đúng** và không được đổi — quan hệ vẫn là phản bác, chỉ có
> đường truyền là văn bản. Hai trường này độc lập nhau; đổi cả hai sẽ là sửa quá tay.

### 2.6 `CH02-BCE05-05` Democritus [k. 460–370 TCN] → **Leucippus (Λεύκιππος)** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có — **với một dè dặt nên nói ra.** Leucippus, Q165589. Chính sự tồn
   tại của ông từng bị nghi ngờ trong cổ đại (Diogenes Laertius X.13 dẫn Epicurus nói "không có triết
   gia nào tên Leucippus"); giới nghiên cứu hiện nay đa số bác lời ấy và coi ông là người thật.
2. **Chồng đời?** **Không kiểm được bằng số.** Q165589 **chỉ có độ chính xác thế kỷ** cho cả P569 và
   P570 (−0500 prec 7 cả hai) — tức Wikidata thực chất không biết năm nào. Phép trừ bất khả. Chứng cứ
   thay thế là quan hệ thầy–trò (xem dưới), vốn hàm ý chồng đời.
3. **Tiếp xúc chứng thực được?** Có, theo truyền thống cổ đại nhất quán: Q41980 `P1066 học trò của`
   = Q165589 và Q165589 `P802 học trò` = Q41980 — hai chiều khớp; Diogenes Laertius IX.34 ghi Democritus
   là học trò Leucippus. Chính thân mục cũng mở đầu bằng "Cùng thầy là Leucippus".

**→ GIỮ `trực tiếp`.** Nhưng ghi rõ mức chắc chắn: cạnh này đứng trên **truyền thống tiểu sử cổ đại**,
không trên niên đại kiểm được. Nếu chủ dự án muốn chuẩn "số phải tự đứng được", đây là ca đầu tiên rụng.

### 2.7 `CH02-BCE05-06` Aeschylus [k. 525–456 TCN] → **Sophocles (Σοφοκλῆς)** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Sophocles, Q7235.
2. **Chồng đời?** Có. Q7235 sinh −496, mất −406 (prec 9). Chồng lấn với Aeschylus **k. 496–456,
   khoảng 40 năm**.
3. **Tiếp xúc chứng thực được?** Có, và là loại rất cụ thể: hai người **dự thi cùng một giải** tại
   Đại Dionysia Athens; Sophocles thắng giải đầu tiên năm 468 TCN trong cuộc thi có Aeschylus dự
   (Plutarch, *Cimon* 8). Cùng một cuộc thi, cùng một thành bang, cùng mấy chục năm — khớp đúng tinh
   thần "đồng sự / cùng một định chế" của CONTRIBUTING.

**→ GIỮ `trực tiếp`.**

### 2.8 `CH02-BCE05-07` Mặc Tử [k. 470–391 TCN] → **Mạnh Tử (孟子)** · Ảnh hưởng tới · `phản bác`

1. **Đích có phải một con người?** Có. Mạnh Tử, Q188903.
2. **Chồng đời?** **KHÔNG.** Q188903 sinh −372, mất −289 (cả hai prec 9). Mặc Tử mất k. 391 TCN
   (Q272411 P570 −391, prec 9; khớp trường `năm:` của mục). **Mạnh Tử sinh sau khi Mặc Tử mất 19 năm.**
   Không có một ngày nào hai người cùng sống.
3. **Tiếp xúc chứng thực được?** Không thể có. Mạnh Tử công kích Mặc gia trong văn bản (*Mạnh Tử* 3B.9,
   7A.26 — công thức "Dương Chu, Mặc Địch"), tức ông phản bác **học phái và văn bản**, không phản bác
   con người.

**→ HẠ xuống `qua trường phái`.** Đây là lỗi quy tắc 9 ở dạng sạch nhất, và lint **không** bắt được nó
vì thứ tự niên đại vẫn "đúng chiều" (người tác động sinh trước).

> **Văn bản thay thế đề xuất:** `- Mạnh Tử (孟子) · phản bác · qua trường phái`
>
> Tự soi lại: tôi **không** đổi `phản bác` thành thứ khác — sự phản bác là có thật và được chính mục
> "Vì sao chọn" lập luận ("sức ép từ Mặc gia buộc Mạnh Tử và Tuân Tử phải biện minh có hệ thống").
> Lập luận đó vẫn đúng nguyên vẹn sau khi hạ mức: nó nói về **sức ép của học phái**, không hề khẳng
> định hai người từng gặp nhau. Tức phần văn xuôi **không cần sửa theo** — hiếm khi được vậy, nên
> nói rõ để chủ dự án khỏi sửa thừa.
>
> **Phát hiện ngoài phạm vi:** Mạnh Tử đã có mục `CH03-BCE04-04` (`k. 372–289 TCN`) — lại là một đích
> văn bản tự do lẽ ra nên là ID. Cùng loại với 2.1.

### 2.9 `CH02-BCE05-08` Pāṇini [k. 520–460 TCN] → **Yāska** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Yāska, Q993504 (nhãn en "Yāska", mô tả "Indian linguist").
2. **Chồng đời?** **[KHÔNG KIỂM ĐƯỢC] riêng cho câu hỏi này.** Q993504 **chỉ có P569 ở độ chính xác thế kỷ**
   (−0500 prec 7) và **không có P570** — Wikidata không biết ông sống năm nào, càng không biết mất năm nào.
   Niên đại Pāṇini cũng tự nó rất lỏng (mục để `độ tin cậy niên đại: Thấp`; giới nghiên cứu xếp ông đâu đó
   từ TK 6 tới TK 4 TCN). Hai khoảng bất định chồng lên nhau thì **không kết luận chồng đời được theo
   chiều nào**.
3. **Tiếp xúc chứng thực được?** **Không.** Không có nguồn nào ghi một cuộc gặp, một quan hệ thầy–trò,
   hay bất kỳ tiếp xúc nào giữa hai người. Quan hệ được biết là **quan hệ giữa hai văn bản**: *Nirukta*
   được coi là tiền-Pāṇini và nằm trong lớp tư liệu mà *Aṣṭādhyāyī* kế thừa.

**→ HẠ xuống `qua trường phái`.** Lưu ý cách đọc kết luận: câu 2 là `[KHÔNG KIỂM ĐƯỢC]`, nhưng **kết
luận cạnh vẫn là HẠ**, không phải `[KHÔNG KIỂM ĐƯỢC]`. Lý do: `trực tiếp` đòi **cả hai** điều kiện;
vế tiếp xúc đã trống chắc chắn, nên không cần giải quyết vế niên đại thì cạnh đã rụng. Và
`qua trường phái` chính là mức mặc định CONTRIBUTING chỉ định cho đúng tình huống này.

### 2.10 `CH02-BCE05-08` Pāṇini → **Patañjali** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Patañjali — và **ông đã có mục riêng trong atlas:
   `CH03-BCE02-06`, `hoạt động k. 160–140 TCN`.** Q231680 cho P569/P570 là `novalue` nhưng
   P1317 floruit = −200 (prec 7, tức TK 2 TCN) — khớp mục atlas.
2. **Chồng đời?** **KHÔNG, và cách xa.** Pāṇini k. 520–460 TCN so với Patañjali hoạt động k. 160–140 TCN:
   **cách khoảng ba thế kỷ.** Đây không phải ca biên; không có cách đọc niên đại nào kéo lại gần được.
3. **Tiếp xúc chứng thực được?** Không thể có. Patañjali là **người viết bình chú** cho Aṣṭādhyāyī
   (*Mahābhāṣya*) — chính thân mục đã nói vậy: "Patañjali, người viết đại bình chú **sau này**", và
   "Patañjali chỉ chú giải". Thân mục và nhãn `trực tiếp` **mâu thuẫn nhau ngay trong cùng một mục**.

**→ HẠ xuống `qua trường phái`.** Đường truyền là bình chú — tức đúng định nghĩa "truyền qua văn bản".

> **Văn bản thay thế đề xuất:** `- Patañjali · kế thừa · qua trường phái`
>
> Tự soi lại: tôi **không** đề xuất nâng thành `CH03-BCE02-06 · kế thừa · qua trường phái` trong cùng
> một nhát, dù ID tồn tại và trỏ đúng người. Lý do: nâng lên ID kéo theo ràng buộc đối xứng hai chiều
> (P2) và làm đổi thống kê mạng lưới — ngoài phạm vi việc tôi được giao, và đáng là một quyết định riêng.
> Nếu chủ dự án áp cả hai cùng lúc thì nhớ thêm cạnh ngược ở `CH03-BCE02-06`.

### 2.11 `CH02-BCE05-09` Tôn Tử [k. 544–496 TCN theo truyền thống] → **Tào Tháo (曹操)** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Tào Tháo, Q204077.
2. **Chồng đời?** **KHÔNG, và đây là khoảng cách lớn nhất trong cả 39 cạnh.** Q204077 sinh **+155**,
   mất **+220 CN** (prec 9, khớp nhau ở hai giá trị). Tôn Tử k. 544–496 **TCN**. **Cách nhau khoảng
   650 năm.** Trường `năm:` mục nguồn còn tự ghi "(theo truyền thống)" và `độ tin cậy niên đại: Thấp`,
   nhưng điều đó không cứu được gì: kể cả dời Tôn Tử sang thời Chiến Quốc như nhãn [Tranh cãi lịch sử]
   gợi ý, khoảng cách vẫn còn hơn bốn thế kỷ.
3. **Tiếp xúc chứng thực được?** Không thể có. Đường truyền thì rất rõ và rất mạnh — Tào Tháo là người
   viết **bản chú Binh pháp Tôn Tử** (*Ngụy Vũ Đế chú Tôn Tử*), bản chú sớm nhất còn giữ được và là
   khung cho mọi bản truyền đời sau. Nhưng đó đúng là định nghĩa của `qua trường phái`: truyền qua
   văn bản và chú giải.

**→ HẠ xuống `qua trường phái`.**

> **Văn bản thay thế đề xuất:** `- Tào Tháo (曹操) · kế thừa · qua trường phái`
>
> Tự soi lại: dòng ngay dưới nó trong cùng mục đã là `- Mao Trạch Đông (毛澤東) · kế thừa · qua trường phái`
> — tức cùng một loại đường truyền (đọc và vận dụng văn bản) đang được ghi hai mức khác nhau trong
> cùng một mục. Sau khi hạ, hai dòng nhất quán. Tôi **không** đề xuất thêm chữ "(người chú giải sớm nhất)"
> vào dòng: đó là một khẳng định về thứ tự các bản chú mà tôi chưa mở mục lục để kiểm, nên theo quy tắc 3
> thà bỏ còn hơn ghi đoán. Nếu muốn nêu điều đó, chỗ của nó là thân mục kèm nguồn, không phải dòng quan hệ.

**Tiểu kết Ca 2:** GIỮ 5 (2.1, 2.2, 2.3, 2.6, 2.7) · HẠ 6 (2.4, 2.5, 2.8, 2.9, 2.10, 2.11) · [KHÔNG KIỂM ĐƯỢC] 0.

---

## Ca 3 — Chapter 2, nhóm BCE06 / BCE07 / BCE08 (9 cạnh)

### 3.1 `CH02-BCE06-03` Đức Phật → **Āḷāra Kālāma và Uddaka Rāmaputta** · Kế thừa từ · `phản bác`

1. **Đích có phải một con người?** **Hai con người**, không lẫn thể chế. Āḷāra Kālāma = Q2500007;
   Uddaka Rāmaputta = Q7876891. Mô tả Wikidata của cả hai đều ghi thẳng "teacher of yogic meditation
   and … teacher of Gautama Buddha". (Chi tiết lệch, không ảnh hưởng kết luận: Wikidata gọi Āḷāra là
   thầy **thứ hai** và Uddaka là thầy **thứ nhất**, **ngược** với trình tự trong *Ariyapariyesanā Sutta*
   MN 26, nơi Āḷāra đến trước. Thứ tự dòng trong mục atlas khớp kinh, không khớp Wikidata — và mục
   atlas đúng.)
2. **Chồng đời?** **Không kiểm được bằng số, nhưng không cần.** Cả Q2500007 lẫn Q7876891 **không có
   P569 cũng không có P570** — Wikidata không biết năm nào. Trường `năm:` mục nguồn cũng tự khai hai
   niên đại cách nhau gần tám mươi năm (`k. 563–483 TCN` dài / `k. 480–400 TCN` ngắn) và để
   `độ tin cậy niên đại: Thấp`. Phép trừ bất khả theo cả hai chiều. Chồng đời ở đây được thiết lập
   **bởi chính trình thuật thầy–trò**, không bởi niên biểu: một người học dưới một người thì hai người
   cùng sống.
3. **Tiếp xúc chứng thực được?** Có, trong hệ nguồn của chính chủ đề: kinh tạng Pāli kể Siddhattha
   theo học thiền dưới Āḷāra Kālāma rồi Uddaka Rāmaputta, đạt tới tầng chứng của mỗi người, rồi bỏ đi
   vì thấy chưa phải giải thoát (*Ariyapariyesanā Sutta* MN 26; *Mahāsaccaka Sutta* MN 36). Đó đúng là
   thầy–trò, và cũng giải thích vì sao loại quan hệ ghi `phản bác` chứ không `kế thừa`.

**→ GIỮ `trực tiếp`.** Kèm dè dặt phải nói ra: toàn bộ bằng chứng nằm trong **kinh điển Phật giáo**,
không có chứng thực ngoại vi; tính lịch sử của hai vị thầy đứng hay đổ cùng với độ tin cậy ta đặt vào
tầng tư liệu ấy. Trong atlas này điều đó nhất quán — mục Đức Phật vốn đã được viết trên cùng tầng
tư liệu đó — nên tôi không coi là lý do hạ.

### 3.2 `CH02-BCE06-11` Sappho [k. 630–570 TCN] → **Catullus** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Catullus, Q163079.
2. **Chồng đời?** **KHÔNG.** Q163079 sinh −84, mất −54 (prec 9). Sappho mất k. 570 TCN.
   **Cách nhau khoảng 486 năm.**
3. **Tiếp xúc chứng thực được?** Không thể có. Đường truyền là **bản dịch** — và chính mục đã viết ra
   điều đó trong "Vì sao chọn": *"mảnh 31 được Catullus dịch thành bài 51"*. Dịch một văn bản là ví dụ
   đầu tiên CONTRIBUTING nêu cho `qua trường phái`.

**→ HẠ xuống `qua trường phái`.** Mục này **tự mâu thuẫn trong chính nó**: phần văn xuôi mô tả một
đường truyền qua văn bản, dòng quan hệ lại ghi `trực tiếp`.

### 3.3 `CH02-BCE06-11` Sappho → **Horace** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Horace, Q6197.
2. **Chồng đời?** **KHÔNG.** Q6197 sinh −65, mất −8 (prec 9/11). **Cách Sappho khoảng 505 năm.**
3. **Tiếp xúc chứng thực được?** Không thể có. Đường truyền là **khổ thơ Sapphic** đi qua văn bản —
   lại chính mục nói: *"khổ thơ mang tên bà đi tiếp qua Horace vào thánh ca Latin"*.

**→ HẠ xuống `qua trường phái`.**

> **Văn bản thay thế đề xuất cho 3.2 và 3.3:**
> `- Catullus (Gaius Valerius Catullus) · kế thừa · qua trường phái`
> `- Horace (Quintus Horatius Flaccus) · kế thừa · qua trường phái`
>
> Tự soi lại: dòng thứ ba trong cùng khối, `- Thánh ca Latin trung cổ theo khổ Sapphic · kế thừa ·
> qua trường phái`, **đã** ở mức này sẵn. Tức sau khi hạ, cả ba dòng trong khối "Ảnh hưởng tới" cùng
> mức — và đó là kết quả đúng, vì cả ba đều là cùng một đường truyền văn bản, chỉ khác độ xa.
> Phần văn xuôi **không cần sửa**: nó vốn đã mô tả đúng đường truyền, chỉ dòng quan hệ ghi sai mức.

### 3.4 `CH02-BCE06-12` Croesus [k. 595 – sau 546 TCN] → **Alyattes xứ Lydia** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Alyattes xứ Lydia, Q299551.
2. **Chồng đời?** Có, và so được. Q299551 sinh −640, mất −560 (prec 9). Croesus sinh k. 596
   (Q184462 P569 −596, khớp trường `năm:`). Chồng lấn **k. 596–560, khoảng 36 năm**.
   (Lưu ý niên đại: trường `năm:` mục nguồn đã tự ghi Wallace 2016 đẩy năm lên ngôi về thập niên 580 —
   nếu theo Wallace thì Croesus lên ngôi **khi cha còn sống**, tức chồng lấn còn chắc hơn, không yếu đi.)
3. **Tiếp xúc chứng thực được?** Có. Q299551 `P40 con` có Q184462 và Q184462 `P22 cha` = Q299551 —
   cha–con, hai chiều khớp; cùng một triều đình Sardis, con kế vị cha trực tiếp. Và tiếp xúc ở đây
   **đúng chính nội dung quan hệ**: mục mô tả Croesus thay hệ tiền electrum của cha bằng hệ lưỡng kim,
   tức ông thao tác trên chính xưởng đúc cha để lại.

**→ GIỮ `trực tiếp`.** Mục này cũng đáng khen về kỷ luật nguồn ở chỗ khác: nó tự gạt truyện Croesus gặp
Solon là "tiếp nhận văn học, không phải sử liệu" — đúng loại phân biệt mà quy tắc 9 đòi.

### 3.5 `CH02-BCE07-04` Archilochus [k. 680–645 TCN] → **Horace** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Horace, Q6197.
2. **Chồng đời?** **KHÔNG.** Horace −65 đến −8. Archilochus mất k. 645 TCN (Q201323 P570 −645, prec 9).
   **Cách nhau khoảng 580 năm.**
3. **Tiếp xúc chứng thực được?** Không thể có. Horace tự mô tả đường truyền là **đọc và mô phỏng văn bản**
   (*Epistulae* I.19.23–25, nơi ông nhận đã đem nhịp iambus của Paros vào Latium). Mục cũng tự viết
   "Horace, Catullus rồi cả truyền thống thơ trữ tình châu Âu đều nhận ảnh hưởng".

**→ HẠ xuống `qua trường phái`.**

> Ghi chú nhất quán giữa hai mục: sau khi áp 3.3 và 3.5, **cả hai** cạnh trỏ tới Horace (từ Sappho và
> từ Archilochus) cùng ở `qua trường phái`. Trước khi sửa, atlas đang gọi cùng một người La Mã là
> "tiếp xúc trực tiếp" của hai nhà thơ Hy Lạp cổ phong sống trước ông năm thế kỷ — hai lần, ở hai mục
> khác nhau. Đó là dấu hiệu lỗi hệ thống chứ không phải sơ suất lẻ.

### 3.6 `CH02-BCE07-08` Sennacherib [k. 745–681 TCN] → **Sargon II (chương trình xây Dur-Sharrukin)** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có — Sargon II, Q208336. Phần trong ngoặc là **định ngữ chỉ rõ mặt
   nào của ông**, không phải một đích thứ hai nối bằng "và". Khác với ca 1.5, đây **không** phải cụm hỗn hợp.
2. **Chồng đời?** Có, rộng và so được. Q208336 sinh −765, mất −705 (prec 9). Sennacherib k. 745–681
   (Q207140 P569 −745 / P570 −681, khớp trường `năm:`). Chồng lấn **k. 745–705, khoảng 40 năm**.
3. **Tiếp xúc chứng thực được?** Có, và thuộc loại CONTRIBUTING nêu đích danh — **thư từ qua lại**.
   Q207140 `P22 cha` = Q208336 và Q208336 `P40 con` = Q207140 (hai chiều khớp); ngoài huyết thống còn
   có khối thư Sennacherib gửi Sargon II thời ông làm thái tử, nằm trong văn khố hoàng gia Nineveh.

**→ GIỮ `trực tiếp`.**

> **Quan sát ngoài phạm vi mức bằng chứng, nêu để chủ dự án cân nhắc:** loại quan hệ ghi `kế thừa`
> nhưng định ngữ lại là "chương trình xây Dur-Sharrukin" — mà chính mục "Vì sao chọn" viết
> *"Dur-Sharrukin bị bỏ ngay khi Sargon chết"*. Sennacherib **không** kế thừa công trình ấy; ông bỏ nó
> và dựng Nineveh thay thế. Cái ông kế thừa là **tập quán vua mới lập kinh đô mới**. Tôi **không** đề
> xuất chữ thay thế cụ thể: sửa định ngữ này là một khẳng định mới về ý đồ xây dựng, cần người đọc
> Jacobsen–Lloyd và Russell (hai nguồn mục đang dẫn) xác nhận, và tôi chưa mở hai sách đó. Nêu ra để
> không im lặng, không để tự sửa.

### 3.7 `CH02-BCE07-08` Sennacherib → **Esarhaddon (tái thiết Babylon)** · Ảnh hưởng tới · `phản bác`

1. **Đích có phải một con người?** Có. Esarhaddon, Q193912 (nhãn en trống trong kết quả API, mô tả
   "King of Assyria (8th century BCE – 669 BCE)"; định danh chắc nhờ `P22 cha` = Q207140 Sennacherib).
   Phần ngoặc lại là định ngữ, không phải đích thứ hai.
2. **Chồng đời?** Có. Q193912 mất −669 (prec 11, tức chính xác tới ngày: 26/10/669 TCN); P569 chỉ prec 7
   (−800) nên **năm sinh không dùng được**. Nhưng ông kế vị Sennacherib năm 681 (Q193912 `P39` ghi
   −681 → −669) ngay sau khi cha bị ám sát — kế vị liền kề đòi hai người cùng sống.
3. **Tiếp xúc chứng thực được?** Có. Cha–con, cùng một triều đình Assyria; Sennacherib đã chính thức
   lập ông làm thái tử (lăng trụ Nineveh A của chính Esarhaddon kể việc cha chọn ông vượt các anh).
   Và `phản bác` ở đây đúng nghĩa đen: cha phá Babylon năm 689, con dựng lại — một sự đảo chính sách
   giữa hai người đã từng sống chung một triều.

**→ GIỮ `trực tiếp`.**

### 3.8 `CH02-BCE07-09` Taharqa [trị vì 690–664 TCN] → **Tanwetamani** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Tanwetamani/Tanutamani, Q434535 ("last Egyptian pharaoh of the
   25th dynasty"). Phần ngoặc "(mất quyền kiểm soát Ai Cập năm 663 TCN)" là định ngữ về sự kiện, không
   phải đích thứ hai; và nó **đúng** — Ashurbanipal cướp phá Thebes năm 663 TCN, đẩy ông về Nubia.
2. **Chồng đời?** **Có, nhưng phải nói rõ là không chứng minh bằng phép trừ.** Hai lớp bẫy chồng nhau:
   trường `năm:` mục nguồn là `trị vì 690–664 TCN` — **niên đại trị vì**; và Q434535 P569 chỉ prec 7
   (−800, "thế kỷ 8 TCN"), vô dụng. Chứng cứ thay thế: Q315714 Taharqa mất −664 (prec 9) và Tanwetamani
   kế vị **ngay năm đó**, mất −653 (prec 9). Kế vị liền kề đòi hai người cùng sống.
3. **Tiếp xúc chứng thực được?** Có. Hai người cùng hoàng tộc Kush vương triều 25 (Q434535 `P22 cha`
   = Q365929 Shabaka, tức Tanwetamani là **cháu gọi Taharqa bằng bác/chú**, không phải con — một chi
   tiết mục atlas không khẳng định sai vì nó chỉ ghi "người kế vị"), cùng một triều đình Napata–Memphis,
   và Tanwetamani kế vị trực tiếp.

**→ GIỮ `trực tiếp`.**

### 3.9 `CH02-BCE08-07` Hezekiah [k. 741–687 TCN] → **Ahaz (vua Judah, cha ông)** · Kế thừa từ · `phản bác`

1. **Đích có phải một con người?** Có. Ahaz, Q30914 ("king of Judah"). Phần ngoặc là định ngữ xác định
   thân phận, không phải đích thứ hai.
2. **Chồng đời?** Có. Q30914 sinh −763, mất −727 (prec 9); `P40 con` = Q244912, đúng Q-ID của mục nguồn.
   Hezekiah k. 741–687. Chồng lấn **k. 741–727, khoảng 14 năm** theo Wikidata.
   **Một lệch nội bộ cần ghi, tuy không đổi kết luận:** chính mục "Vì sao chọn" viết Ahaz là
   "vua Judah **k. 732–716 TCN**", tức theo một niên biểu khác (dòng Thiele) muộn hơn Wikidata khoảng
   mười năm. Hai niên biểu **đều** cho chồng đời, nên kết luận không đổi; nhưng mục đang mang hai hệ
   niên đại không khớp nhau mà không nói ra.
3. **Tiếp xúc chứng thực được?** Có. Cha–con, kế vị trực tiếp trên ngai Judah, cùng một triều đình
   Jerusalem. Và `phản bác` khớp nội dung: mục lập luận Ahaz thần phục Assyria còn Hezekiah đảo ngược,
   tức một sự đảo chính sách giữa hai người từng cùng triều.

**→ GIỮ `trực tiếp`.** Dè dặt phải nói: cả hai nhân vật được biết chủ yếu qua trình thuật Kinh Thánh,
có hậu thuẫn ngoại vi đáng kể cho Hezekiah (bulla Ophel, bi ký Siloam, lăng trụ Sennacherib) nhưng
**mỏng hơn nhiều cho Ahaz**. Quan hệ cha–con cụ thể là từ 2 Các Vua, không từ văn khắc.

**Tiểu kết Ca 3:** GIỮ 6 (3.1, 3.4, 3.6, 3.7, 3.8, 3.9) · HẠ 3 (3.2, 3.3, 3.5) · [KHÔNG KIỂM ĐƯỢC] 0.

---

## Ca 4 — Chapter 3 (11 cạnh)

### 4.1 `CH03-BCE01-06` Tư Mã Thiên [k. 145–86 TCN] → **Tư Mã Đàm** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Tư Mã Đàm, Q2401828 ("Chinese astrologer and historian,
   c. 165–110 BCE").
2. **Chồng đời?** Có, so được bằng số. Q2401828 sinh −165, mất −110 (prec 9). Tư Mã Thiên k. 145–86
   (Q9372 P569 −145 / P570 −86, khớp trường `năm:`). Chồng lấn **k. 145–110, khoảng 35 năm**.
3. **Tiếp xúc chứng thực được?** Có, loại mạnh nhất có thể có cho một cặp Trung Hoa cổ: Q9372 `P22 cha`
   = Q2401828 và Q2401828 `P40 con` = Q9372 (hai chiều khớp); và *Sử ký* quyển 130 (phần tự tự) chép
   chính lời trăng trối Tư Mã Đàm dặn con hoàn thành bộ sử — tức tiếp xúc được ghi bởi **chính người
   trong cuộc**, trong **chính tác phẩm** mà mục này nói về.

**→ GIỮ `trực tiếp`.** Cạnh được chứng minh tốt nhất trong cả 39 cạnh.

### 4.2 `CH03-BCE01-07` Hillel Trưởng lão → **Shemaiah và Avtalyon** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** **Hai con người**, không lẫn thể chế: Shemaiah/Shmaya = Q2907313
   ("Rabbinic sage"); Avtalyon/Abtalion = Q2750624 ("pharisee leader").
2. **Chồng đời?** **[KHÔNG KIỂM ĐƯỢC] riêng cho câu hỏi này.** Hai lớp bẫy: trường `năm:` mục nguồn là
   `hoạt động k. 30 TCN – 10 CN` — **khoảng hoạt động, không phải sinh–mất**; và **cả Q2907313 lẫn
   Q2750624 đều không có P569 cũng không có P570** — Wikidata không có một con số nào cho hai người này.
   Không có gì để trừ. (Q319219 Hillel có P569/P570 nhưng mang hai bộ giá trị mâu thuẫn nhau: −50/+8
   prec 9 và −100/+100 prec 7. Tôi không dựa vào chúng.)
3. **Tiếp xúc chứng thực được?** Có, trong hệ nguồn của chính chủ đề, và khớp hai chiều trên Wikidata:
   Q319219 `P1066 học trò của` = Q2907313 **và** Q2750624; ngược lại cả Q2907313 lẫn Q2750624 đều có
   `P802 học trò` = Q319219. Nền văn bản là chuỗi truyền thừa trong Mishnah *Avot* 1:10–12 — đúng nguồn
   mục đang dẫn — và truyện Hillel leo lên mái nhà học để nghe hai ông giảng (*Yoma* 35b).

**→ GIỮ `trực tiếp`.** Nhưng mức chắc chắn thấp hơn 4.1 một bậc rõ rệt, và **mục đã tự nói ra điều đó**:
"Niên đại và cả việc quy bảy quy tắc cho ông đều dựa vào nguồn rabbi muộn, nên để độ tin cậy Thấp".
Quan hệ thầy–trò cũng đến từ đúng tầng nguồn ấy. Tôi giữ vì CONTRIBUTING đòi "chứng minh được bằng
nguồn", không đòi nguồn đương thời — nhưng nếu chủ dự án muốn siết thành "nguồn đương thời", đây là
ca rụng cùng với 1.1 (Chu Vũ Vương) và 3.1 (Đức Phật).

### 4.3 `CH03-BCE01-12` Posidonius [k. 135–51 TCN] → **Panaetius** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Panaetius, Q297420.
2. **Chồng đời?** Có, so được. Q297420 sinh −185/−183/−180 (ba giá trị, đều prec 9), mất −110/−109.
   Posidonius k. 135–51 (Q185770 P569 −135 / P570 −51, khớp trường `năm:`). Chồng lấn
   **k. 135–110, khoảng 25 năm**.
3. **Tiếp xúc chứng thực được?** Có. Q185770 `P1066 học trò của` = Q297420 **và** Q297420 `P802 học trò`
   có Q185770 — hai chiều khớp; Posidonius học dưới Panaetius ở Athens trước khi mở trường riêng ở Rhodes.
   Chính mục "Vì sao chọn" cũng gọi thẳng Panaetius là "thầy ông".

**→ GIỮ `trực tiếp`.**

### 4.4 `CH03-BCE02-03` Hipparchus [k. 190–120 TCN] → **Ptolemy và Almagest** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** **Không hẳn — cụm hỗn hợp**, cùng dạng với ca 1.5. Vế một là người
   (Claudius Ptolemy, Q34943); vế hai, *Almagest*, là một **tác phẩm**. Riêng vế hai đã đủ đưa cạnh về
   mức mặc định.
2. **Chồng đời?** **KHÔNG.** Q34943 sinh +100 (cũng có biến thể +87, +85), mất +170 (hoặc +165) — thế kỷ
   2 **CN**. Hipparchus k. 190–120 **TCN** (Q159905 P569 −190 / P570 −120 prec 9, khớp trường `năm:`).
   **Cách nhau khoảng 220 năm** tính từ năm Hipparchus mất tới năm Ptolemy sinh.
3. **Tiếp xúc chứng thực được?** Không thể có. Đường truyền được chính mục mô tả đúng ở văn xuôi —
   *"vì Almagest giữ lại phương pháp của ông"* — tức Ptolemy **đọc và bảo tồn** công trình Hipparchus
   qua văn bản, hai thế kỷ sau. Mục còn dẫn chính *Almagest* q. III và VII làm nguồn, tức thừa nhận
   đường truyền là văn bản.

**→ HẠ xuống `qua trường phái`.** Hai lý do độc lập: cụm hỗn hợp, và lệch hơn hai thế kỷ.

> **Văn bản thay thế đề xuất:** `- Ptolemy và Almagest · kế thừa · qua trường phái`
>
> Tự soi lại: như ca 1.5, dòng này **giữ nguyên cụm hỗn hợp** — chỉ sửa mức, không sửa hình dạng đích.
> Tôi không tách làm hai dòng vì cả hai vế tách ra đều vẫn là `qua trường phái`, nên tách chỉ tốn dòng.
>
> **Phát hiện ngoài phạm vi:** Claudius Ptolemy **đã có mục trong atlas**, `CH04-CE02-05` (`k. 100–170 CN`).
> Như 2.1 / 2.8 / 2.10, đây lẽ ra là liên kết theo ID. Cùng loại, xử lý riêng.

### 4.5 `CH03-BCE02-06` Patañjali [hoạt động k. 160–140 TCN] → **Kātyāyana** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có, nhưng **định danh không sạch**. Tìm trên Wikidata không ra mục
   nào dành riêng cho **Kātyāyana nhà văn phạm** (người soạn vārttika). Ứng viên gần nhất là Q1196778,
   nhãn "Kātyāyana", mô tả **"Sanskrit mathematician"** — tức mục ấy định danh ông theo
   Śulbasūtra, không theo vārttika. Còn Q44277 là một Kātyāyana khác hẳn (đệ tử Đức Phật). Ghi thẳng:
   **tôi không xác nhận được Q-ID nào trỏ đúng người mục này muốn nói.**
2. **Chồng đời?** **[KHÔNG KIỂM ĐƯỢC] — và hai nguồn mâu thuẫn nhau theo đúng hai chiều ngược.**
   - Q1196778 ghi sinh −190 / mất −159, **cả hai prec 7** (độ chính xác thế kỷ, tức con số lẻ không
     mang nghĩa). Đọc theo đó thì **có** chồng lấn với Patañjali (hoạt động k. 160–140 TCN).
   - Wikipedia en, mục "Kātyāyana", ghi ông sống **"c. 3rd–4th century BCE"** — đọc theo đó thì
     **không** chồng lấn, cách Patañjali ít nhất một thế kỷ.
   Tôi **không chọn con số có lợi cho kết luận nào**: hai nguồn chỏi nhau và cả hai đều ở độ phân giải
   thế kỷ. Câu này để ngỏ.
3. **Tiếp xúc chứng thực được?** **Không — và câu này mới là câu quyết định.** Quan hệ giữa hai người là
   **bình chú trên văn bản**: Mahābhāṣya của Patañjali bình giải các vārttika của Kātyāyana. Chính mục
   viết ra điều đó hai lần: *"Kātyāyana, người soạn các vārttika mà ông bình giải"* và *"không có
   Mahābhāṣya thì các vārttika chỉ là ghi chú rời"*. Không nguồn nào ghi một cuộc gặp, một quan hệ
   thầy–trò, hay bất kỳ tiếp xúc người với người nào.

**→ HẠ xuống `qua trường phái`.** Cách đọc kết luận giống ca 2.9: câu 2 là `[KHÔNG KIỂM ĐƯỢC]`, nhưng
cạnh vẫn **HẠ**, vì `trực tiếp` đòi cả hai điều kiện và vế tiếp xúc trống chắc chắn. Không cần giải
xong câu niên đại thì cạnh đã rụng.

> **Văn bản thay thế đề xuất:** `- Kātyāyana · kế thừa · qua trường phái`
>
> Tự soi lại: tôi **cố ý không** viết "Kātyāyana (tác giả các vārttika)" dù định ngữ ấy sẽ giúp phân
> biệt với Kātyāyana đệ tử Phật và Kātyāyana nhà toán học. Lý do: thêm nó là khẳng định một **định danh
> mà tôi vừa nói là chưa xác minh được** — đúng cái lỗi tôi đang chẩn ở câu 1. Nếu chủ dự án muốn thêm
> định ngữ, phải mở Cardona (1976, nguồn mục đang dẫn) xác nhận trước; đó không phải việc tôi làm thay
> được ở đây.

### 4.6 `CH03-BCE02-11` Judah Maccabee [hoạt động k. 167–160 TCN] → **Mattathias** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Mattathias, Q75048.
2. **Chồng đời?** Có, dù phải đi đường vòng. Bẫy: trường `năm:` mục nguồn là `hoạt động k. 167–160 TCN`
   — **khoảng hoạt động**; và Q111559 (Judah) có P569 = −500 **prec 6** (độ chính xác thiên niên kỷ —
   rác, không dùng được; chính Ghi chú biên tập của chapter cũng đã ghi nhận chỗ này). Chứng cứ dùng
   được: Q75048 mất −166 (prec 9), nằm **bên trong** khoảng hoạt động 167–160 của Judah; và Q111559
   `P22 cha` = Q75048, Q75048 `P40 con` có Q111559 — hai chiều khớp. **Có chồng đời.**
3. **Tiếp xúc chứng thực được?** Có. Cha–con, cùng khởi nghĩa: 1 Maccabee 2 chép Mattathias lúc hấp hối
   giao quyền chỉ huy quân sự cho Judah — đúng nguồn mục đang dẫn ("Sách Maccabee thứ nhất").

**→ GIỮ `trực tiếp`.**

### 4.7 `CH03-BCE02-12` Mặc Đốn thiền vu [k. 234–174 TCN] → **Đầu Mạn thiền vu** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Đầu Mạn/Touman, Q719747 ("Xiongnu chanyu"). Phần ngoặc
   "(liên minh bộ lạc Hung Nô trước khi hợp nhất)" là định ngữ về bối cảnh, không phải đích thứ hai.
2. **Chồng đời?** Có. Bẫy dữ liệu: Q719747 có P569 prec 7 (−250, "thế kỷ 3 TCN") và **không có P570**
   — Wikidata không ghi năm Đầu Mạn mất. Chứng cứ dùng được: Q382816 `P22 cha` = Q719747 và Q719747
   `P40 con` = Q382816 (hai chiều khớp); Mặc Đốn k. 234–174 và lên ngôi năm 209 TCN (Q382816 `P39`
   ghi −209 → −174). Cha–con, con kế vị cha. **Có chồng đời.**
3. **Tiếp xúc chứng thực được?** Có, và là ca cực đoan nhất về mức "trực tiếp" trong cả 39 cạnh:
   *Sử ký* quyển 110 "Hung Nô liệt truyện" — **đúng nguồn mục đang dẫn, kèm cả bản dịch Watson 1993** —
   chép Mặc Đốn bắn chết chính cha mình năm 209 TCN để đoạt ngôi.

**→ GIỮ `trực tiếp`.**

### 4.8 `CH03-BCE02-12` Mặc Đốn thiền vu → **Lão Thượng thiền vu** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Lão Thượng/Laoshang, Q2593729 ("chanyu of the Xiongnu").
   Phần ngoặc "(hoàn tất việc đuổi Nguyệt Chi khỏi Trung Á)" là định ngữ về sự kiện, và nó khớp
   *Sử ký* 110.
2. **Chồng đời?** Có. Bẫy dữ liệu: Q2593729 có `P569 novalue` — Wikidata **khẳng định không biết**
   năm sinh. Chứng cứ dùng được: Q2593729 `P22 cha` = Q382816 và Q382816 `P40 con` = Q2593729
   (hai chiều khớp); Mặc Đốn mất −174 và Lão Thượng kế vị ngay năm đó, mất −161 (prec 9). Cha–con,
   kế vị liền kề. **Có chồng đời.**
3. **Tiếp xúc chứng thực được?** Có. Cha–con trong cùng một vương đình Hung Nô, con kế vị cha trực tiếp;
   *Sử ký* 110 chép cả hai trong một mạch trình thuật liên tục.

**→ GIỮ `trực tiếp`.**

### 4.9 `CH03-BCE03-12` Hannibal Barca [k. 247–183 TCN] → **Hamilcar Barca** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Hamilcar Barca, Q185101.
2. **Chồng đời?** Có, so được. Q185101 sinh −275, mất −228 (prec 9). Hannibal k. 247–183 (Q36456
   P569 −247 / P570 −183, khớp trường `năm:`). Chồng lấn **k. 247–228, khoảng 19 năm**.
3. **Tiếp xúc chứng thực được?** Có. Q36456 `P22 cha` = Q185101 và Q185101 `P40 con` có Q36456
   (hai chiều khớp). Ngoài huyết thống còn có tiếp xúc công vụ: Hannibal theo cha sang Hispania từ nhỏ,
   và Polybius III.11 — **đúng nguồn mục đang dẫn ("Polybius, Lịch sử, q. III")** — chép lời thề trước
   bàn thờ mà Hamilcar bắt con tuyên.

**→ GIỮ `trực tiếp`.**

### 4.10 `CH03-BCE03-12` Hannibal Barca → **Scipio Africanus** · Ảnh hưởng tới · `kế thừa`

1. **Đích có phải một con người?** Có. Scipio Africanus, Q2253.
2. **Chồng đời?** Có, rất rộng. Q2253 sinh −235, mất −183 (prec 9). Hannibal k. 247–183. Chồng lấn
   **k. 235–183, khoảng 52 năm** — và hai người **mất cùng năm**.
3. **Tiếp xúc chứng thực được?** Có, loại đối đầu có tên hai bên, mạnh hơn hẳn ca 1.6: hai người chỉ huy
   hai bên ở Zama năm 202 TCN, và Polybius XV.6–8 chép cả **một cuộc hội đàm mặt đối mặt giữa hai người
   trước trận**. Polybius q. III là nguồn mục đang dẫn, nên bước sang q. XV không phải bước ra ngoài
   tầng nguồn của mục.

**→ GIỮ `trực tiếp`.**

> Ghi chú quan hệ, không phải mức bằng chứng: loại ghi là `kế thừa` ("Hannibal ảnh hưởng tới Scipio"),
> và điều đó **khớp** lập luận của mục ("Scipio phần lớn là học và áp dụng lại chính cách đánh ấy")
> cũng như Ghi chú biên tập của chapter ("phần lớn cách đánh là học lại từ chính đối thủ").
> Nhất quán, không cần sửa.

### 4.11 `CH03-BCE04-03` Alexander Đại đế [356–323 TCN] → **Philip II của Macedonia** · Kế thừa từ · `kế thừa`

1. **Đích có phải một con người?** Có. Philip II, Q130650 ("King of Macedon from 359 to 336 BC").
2. **Chồng đời?** Có, so được, và đây là mục duy nhất trong 39 ca có `độ tin cậy niên đại: Cao` cùng
   niên đại **không** có chữ "k.". Q130650 sinh −383/−382, mất −336 (prec 9; một giá trị prec 10 ghi
   tháng 8). Alexander 356–323. Chồng lấn **356–336, đúng 20 năm**.
3. **Tiếp xúc chứng thực được?** Có. Q130650 `P40 con` có Q8409; cha–con, Alexander nhiếp chính khi cha
   vắng mặt và chỉ huy cánh kỵ binh Companion ở Chaeronea năm 338 TCN dưới quyền cha — tức tiếp xúc
   vừa gia đình vừa công vụ vừa chiến trường. Arrian, *Anabasis*, là nguồn mục đang dẫn.

**→ GIỮ `trực tiếp`.**

**Tiểu kết Ca 4:** GIỮ 9 (4.1, 4.2, 4.3, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11) · HẠ 2 (4.4, 4.5) ·
[KHÔNG KIỂM ĐƯỢC] 0.

---

## Tổng kết

| Kết luận | Số cạnh | Tỷ lệ |
|---|---:|---:|
| **GIỮ `trực tiếp`** | **27** | 69,2 % |
| **HẠ xuống `qua trường phái`** | **12** | 30,8 % |
| **`[KHÔNG KIỂM ĐƯỢC]`** | **0** | 0 % |
| Tổng | 39 | 100 % |

Phân rã theo ca:

| Ca | Phạm vi | Tổng | GIỮ | HẠ | [KHÔNG KIỂM ĐƯỢC] |
|---|---|---:|---:|---:|---:|
| 1 | Chapter 1 | 8 | 7 | 1 | 0 |
| 2 | Ch2 nhóm BCE05 | 11 | 5 | 6 | 0 |
| 3 | Ch2 nhóm BCE06/07/08 | 9 | 6 | 3 | 0 |
| 4 | Chapter 3 | 11 | 9 | 2 | 0 |
| | **Tổng** | **39** | **27** | **12** | **0** |

### Vì sao không có ca nào là `[KHÔNG KIỂM ĐƯỢC]`

Ba lần tôi gặp bất định thật và đã ghi `[KHÔNG KIỂM ĐƯỢC]` **ở cấp câu hỏi**: câu "chồng đời?" của
2.9 (Yāska), 4.2 (Shemaiah và Avtalyon) và 4.5 (Kātyāyana). Không ca nào trong ba ca ấy lan thành
`[KHÔNG KIỂM ĐƯỢC]` ở **cấp kết luận**, vì `trực tiếp` đòi **cả hai** điều kiện: khi vế "tiếp xúc"
đã ngã dứt khoát (2.9, 4.5) thì không cần giải vế niên đại nữa, và khi vế tiếp xúc đứng vững bằng
nguồn (4.2) thì niên đại mờ không đủ để lật. Nói cách khác: con số 0 ở cột này **không** có nghĩa là
mọi thứ đều kiểm được — nó có nghĩa là cấu trúc hai-điều-kiện của định nghĩa đã chặn bất định lại
trước khi nó chạm tới kết luận. Chi tiết bất định nằm ở từng ca, không bị nuốt mất.

### 12 cạnh cần hạ, gom theo mục để tiện áp

| Mục | Dòng hiện tại | Sửa thành |
|---|---|---|
| `CH01-BCE17_15-02` | `Apophis và giai đoạn Hyksos muộn · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE05-03` | `Hecataeus xứ Miletus · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE05-03` | `Thucydides (Θουκυδίδης) · phản bác · trực tiếp` | `… · phản bác · qua trường phái` |
| `CH02-BCE05-07` | `Mạnh Tử (孟子) · phản bác · trực tiếp` | `… · phản bác · qua trường phái` |
| `CH02-BCE05-08` | `Yāska · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE05-08` | `Patañjali · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE05-09` | `Tào Tháo (曹操) · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE06-11` | `Catullus (Gaius Valerius Catullus) · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE06-11` | `Horace (Quintus Horatius Flaccus) · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH02-BCE07-04` | `Horace (Quintus Horatius Flaccus) · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH03-BCE02-03` | `Ptolemy và Almagest · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |
| `CH03-BCE02-06` | `Kātyāyana · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` |

Chạm **10 mục** trong 3 file (`content/ch01.md`, `ch02.md`, `ch03.md`).
**Loại quan hệ (`kế thừa` / `phản bác`) không đổi ở bất kỳ dòng nào** — chỉ đổi trường thứ ba.
Hai trường này đo hai thứ khác nhau; đổi kèm là sửa quá tay.
**Không cần sửa một chữ nào trong phần văn xuôi** của 10 mục đó: ở các ca 2.8, 3.2, 3.3, 4.4, 4.5 phần
"Vì sao chọn" đã mô tả **đúng** đường truyền qua văn bản sẵn rồi — chính dòng quan hệ mới là chỗ lệch
khỏi văn xuôi. Vì vậy trần chữ (`Tư tưởng / đóng góp chính` 130, `Vì sao chọn` 104) **không bị động tới**.

### Hình dạng của lỗi — 12 cạnh này không phân bố ngẫu nhiên

- **7/12 là lệch quá một thế kỷ**, và 5 trong đó **quá bốn thế kỷ**: Tôn Tử→Tào Tháo (~650 năm),
  Archilochus→Horace (~580), Sappho→Horace (~505), Sappho→Catullus (~486), Hipparchus→Ptolemy (~220).
  Lint để lọt sạch vì thứ tự niên đại vẫn "đúng chiều" — đúng chỗ mù mà `CONTRIBUTING.md` quy tắc 9 mô tả.
- **5/12 nằm trong mục mà chính phần văn xuôi đã mô tả đúng đường truyền là văn bản** (bản dịch, khổ thơ,
  bình chú, *Almagest* giữ lại phương pháp). Tức lỗi không phải do không biết, mà do **dòng quan hệ được
  điền tách rời khỏi đoạn văn ngay phía trên nó**.
- **2/12 là cụm hỗn hợp người + không-phải-người** (1.5 "Apophis và giai đoạn Hyksos muộn";
  4.4 "Ptolemy và Almagest"). Dạng này đáng dò bằng script: đích chứa " và " rồi một danh từ chỉ
  giai đoạn / tác phẩm / thể chế là dấu hiệu gần như chắc chắn.
- **Chỉ 1/12 thuộc Chapter 1** — và 27 ca GIỮ phần lớn là quan hệ cha–con / kế vị, loại mà atlas đang
  ghi `trực tiếp` **đúng**. Nói cách khác, vấn đề không nằm ở Chapter 1 mà tập trung ở **nhóm BCE05 của
  Chapter 2 (6/11 cạnh phải hạ)**, nơi đích hay là một tên La Mã hoặc một nhà bình chú đời sau.

### Bốn ca GIỮ mà chủ dự án nên biết là mình đang chấp nhận điều gì

Bốn cạnh dưới đây **đạt chuẩn hiện hành** nhưng đứng trên **nguồn hậu kỳ** chứ không trên tư liệu
đương thời. Nếu sau này CONTRIBUTING siết thêm một vế ("nguồn phải đương thời hoặc gần đương thời"),
đây là bốn ca rụng đầu tiên — nêu ra để lần rà sau không phải tìm lại:

| Ca | Cạnh | Nguồn duy nhất cho tiếp xúc |
|---|---|---|
| 1.1 | Chu Vũ Vương ← Chu Văn Vương | Thượng thư, truyền thống văn bản đời sau |
| 2.6 | Democritus ← Leucippus | Diogenes Laertius IX.34; Wikidata không có niên đại dùng được |
| 3.1 | Đức Phật ← Āḷāra Kālāma, Uddaka Rāmaputta | kinh tạng Pāli, không có chứng thực ngoại vi |
| 4.2 | Hillel ← Shemaiah, Avtalyon | Mishnah *Avot* 1:10–12, *Yoma* 35b — nguồn rabbi muộn |

Thêm một ca nửa vời đáng ghi: **1.7 (Ahmose I ← Kamose và Ahhotep)** được GIỮ **nhờ vế Ahhotep**;
vế Kamose nếu tách riêng thì không đứng được, vì Kamose mất khi Ahmose I còn là trẻ con.

### Phát hiện ngoài phạm vi — chuyển cho chủ dự án, tôi không đề xuất sửa

**(A) Bốn đích văn bản tự do đã có mục riêng trong atlas.** Dò bằng cách đối chiếu tên đích với
`data/persons.json` (285 mục):

| Mục nguồn | Đích văn bản tự do | Đã có ID |
|---|---|---|
| `CH02-BCE05-01` | Plato (Πλάτων) | `CH03-BCE04-01` |
| `CH02-BCE05-07` | Mạnh Tử (孟子) | `CH03-BCE04-04` |
| `CH02-BCE05-08` | Patañjali | `CH03-BCE02-06` |
| `CH03-BCE02-03` | Ptolemy và Almagest | `CH04-CE02-05` (Claudius Ptolemy) |

Đây là **lỗi loại khác** với việc tôi được giao, nên tôi không gộp vào. Nâng lên ID kéo theo ràng buộc
đối xứng hai chiều (P2) và làm đổi thống kê mạng lưới — phải là một quyết định riêng. Nếu áp, nhớ
thêm cạnh ngược ở mục đích. Lưu ý ba trong bốn ca này **đồng thời** nằm trong danh sách HẠ của tôi;
nếu áp cả hai thay đổi một lượt thì dòng cuối là ví dụ `- CH03-BCE02-06 · kế thừa · qua trường phái`.

**(B) `CH02-BCE07-08` Sennacherib — định ngữ "(chương trình xây Dur-Sharrukin)" mâu thuẫn với thân mục.**
Loại quan hệ là `kế thừa`, nhưng chính "Vì sao chọn" viết *"Dur-Sharrukin bị bỏ ngay khi Sargon chết"*.
Sennacherib bỏ công trình ấy và dựng Nineveh thay. Mức bằng chứng `trực tiếp` **đúng** và tôi giữ;
cái lệch là định ngữ. Cần người mở Jacobsen–Lloyd (1935) và Russell (1991) rồi sửa, không sửa mò.

**(C) `CH02-BCE08-07` Hezekiah mang hai hệ niên đại không khớp nhau.** Trường `năm:` và Wikidata cho
Ahaz mất −727; phần "Vì sao chọn" lại ghi Ahaz là "vua Judah k. 732–716 TCN". Hai niên biểu khác nhau
(Thiele và dòng còn lại), lệch khoảng mười năm, không được nói ra. Không đổi kết luận 3.9, nhưng là
chỗ người đọc sẽ vấp.

**(D) `CH02-BCE06-03` — thứ tự hai vị thầy của Đức Phật.** Mục atlas ghi "Āḷāra Kālāma và Uddaka
Rāmaputta", khớp *Ariyapariyesanā Sutta* MN 26. Wikidata **ghi ngược** (Q2500007 Āḷāra là "second
teacher", Q7876891 Uddaka là "first teacher"). **Atlas đúng, Wikidata sai** — ghi ra để lần đối chiếu
Wikidata sau không "sửa" nhầm theo chiều ngược.

**(E) Ba mục dữ liệu Wikidata hỏng, gặp trong lúc rà.** Nêu để không ai dùng lại chúng mà không biết:
Q879157 (Khamudi) có P569 sinh −1549 **muộn hơn** P570 mất −1600; Q111559 (Judah Maccabee) có P569 ở
**prec 6** (thiên niên kỷ); Q1196778 (Kātyāyana) có P569/P570 ở prec 7 nhưng **chỏi với** chính bài
Wikipedia en cùng chủ đề (TK 2 TCN so với TK 3–4 TCN).

### Giới hạn của chính bản bình duyệt này

- Tôi kiểm **mức bằng chứng**, không kiểm lại Q-ID của mục nguồn, không kiểm lại nguồn trong mục
  "Nguồn", không kiểm phần văn xuôi. Những việc đó thuộc `reviews/review-chNN.md`.
- Nền niên đại chủ yếu là **Wikidata**, vốn là **sàn chứ không phải trần** (CONTRIBUTING quy tắc 4).
  Ở các ca nhân vật cổ đại, Wikidata nhiều khi chỉ có độ chính xác thế kỷ hoặc thiên niên kỷ; mỗi lần
  gặp tôi đã nói rõ thay vì lặng lẽ dùng con số lẻ.
- Những tiếp xúc tôi viện bằng trí nhớ chuyên ngành mà **không** mở nguồn ra kiểm trong lượt này —
  thư thái tử Sennacherib gửi Sargon II, lăng trụ Nineveh A, Polybius III.11 và XV.6–8, Plutarch
  *Cimon* 8, Diogenes Laertius IX.34, *Sử ký* 110 và 130, 1 Maccabee 2, *Yoma* 35b, Horace
  *Epistulae* I.19 — đều là tư liệu phổ biến, nhưng chúng **chưa được tôi mở mục lục xác nhận**, nên
  theo tinh thần quy tắc 3 chúng được nêu **không kèm số trang**. Mọi kết luận GIỮ dựa vào nhóm này
  đều còn chỗ cho một vòng kiểm thứ hai; không kết luận HẠ nào dựa vào chúng.
