# Bình duyệt độc lập — nhóm CE07, `content/ch05.md` dòng 209–411

Vòng rà soát do một agent **không viết** nhóm này thực hiện, ngày 2026-11-02.
Phạm vi: 12 mục `CH05-CE07-01` … `CH05-CE07-12` cộng dòng **Bối cảnh** của nhóm.

**Đã đọc trước khi bắt đầu:** `CONTRIBUTING.md` (đặc biệt quy tắc 5, 6, 7, 8 và quy ước `vùng:`),
`README.md`, `prompts/atlas-prompt.md` (§5 template), `atlaslib/lint.py`, `atlaslib/common.py`,
và các khối 14–23 của `## Ghi chú biên tập` ở `content/ch05.md` (dòng 1110–1143), vốn nói về chính nhóm này.

**Xếp hạng:** **BẮT BUỘC** (phải sửa) · **NÊN** · **CÂN NHẮC** · `[KHÔNG KIỂM ĐƯỢC]` đánh dấu riêng.

---

## Kiểm ở tầng nhóm (trước khi vào từng mục)

**Đã kiểm được (không có phát hiện):**

- **Trần chữ.** Đếm bằng `len([w for w in s.split() if w])` đúng như `atlaslib/lint.py`.
  Không mục nào vượt trần: `ideas` cao nhất là `CH05-CE07-02` với **130/130** (sát trần, xem cảnh báo dưới),
  thấp nhất `CH05-CE07-07` với 91. `why` cao nhất `CH05-CE07-07` với **99/104**, thấp nhất 78.
  `Bối cảnh` **56/78 chữ**. Không có cảnh báo lệch > 30% nào.
- **Mười hai Q-ID đều trỏ đúng người.** Tra bằng `wbgetentities` một lượt:
  Q9458 Muhammad · Q8467 Umar ibn Al-Khattāb · Q39619 Alī ibn Abī Ṭālib · Q9701 Emperor Taizong of Tang ·
  Q9738 Wu Zetian · Q42063 Xuanzang · Q345012 Huineng · Q202943 Brahmagupta · Q166876 Isidore of Seville ·
  Q457990 Dharmakirti · Q320122 Songtsän Gampo · Q371384 K'inich Janaab' Pakal. Cả 12 đều `P31 = Q5`.
  Không tái diễn ca `Q311215` (chi bướm *Colias*) mà khối 15 ghi lại.
- **Mười hai liên kết ID đều tồn tại VÀ trỏ đúng người** (mở từng mục đích ra đọc tên, không chỉ kiểm tồn tại
  như `atlaslib/lint.py:151-152` làm): CH05-CE06-03 = Khosrow I · CH05-CE06-04 = Varāhamihira ·
  CH05-CE06-05 = Trần-na · CH05-CE06-06 = Tùy Văn Đế · CH05-CE06-08 = Bồ-đề-đạt-ma · CH04-CE04-10 = Asaṅga ·
  CH04-CE04-11 = Vasubandhu · CH04-CE04-12 = Pháp Hiển · CH04-CE05-01 = Augustinô · CH04-CE05-09 = Āryabhaṭa ·
  CH05-CE09-04 = Al-Khwarizmi · CH05-CE08-10 = Trisong Detsen. **Không có ca trỏ sai người nào** —
  khác hẳn bảy ca của vòng trước. Chi tiết nhãn quan hệ xem từng mục.
- **Quy tắc 6, quét toàn bộ `content/*.md` (285 mục, kể cả phụ lục `ch90.md`).** Mọi cái tên bị nêu
  làm ứng viên bị loại / ứng viên cùng thời đều **không có mục riêng ở bất kỳ chapter nào**:
  Abu Bakr (caliph), Khalid ibn al-Walid, Uthman, Mu'awiya, Đường Cao Tổ, Ngụy Trưng, Đường Cao Tông,
  Địch Nhân Kiệt, Nghĩa Tịnh, Thần Tú, Thần Hội, Bhāskara I, Gregorius thành Tours, Kumārila Bhaṭṭa,
  Gar Tongtsen, Yuknoom Chʼeen II, Thönmi Sambhoṭa. Hai ca `grep` trúng mà **không** phải va chạm:
  `CH05-CE10-02 · Abu Bakr al-Rāzī` (người khác) và `CH05-CE08-05 · Sibawayh (Amr ibn Uthman)` (tên đệm).
  Bốn ca đã khai sẵn đúng câu chữ `CONTRIBUTING.md:51` — Pháp Hiển, Āryabhaṭa, Trần-na, Trisong Detsen —
  đều được xác nhận là có mục thật ở đúng ID được nêu. **Ca Trisong Detsen đã được vá, không còn hở.**
- **Trường `năm:`.** Không mục nào dùng tiền tố "trị vì"/"hoạt động", nên `NON_BIO_YEARS_RE`
  (`common.py:133`) không áp dụng; cả 12 đều ở dạng `sinh–mất` parser đọc được, không mục nào dạng `TK 6 CN`.
- **Đối chiếu niên đại theo `DATE_TOLERANCE` (`common.py:82`).** 12/12 sạch. Ba ca đáng ghi:
  (1) `Q457990` Pháp Xứng `P569 = +0700/p7` là **khoảng 601–700**, không phải điểm 700 — đọc đúng theo
  `year_in_bucket`, khớp khối 16; mục để `Thấp` nên `DATE_TOLERANCE = None`, không đối chiếu.
  (2) `Q320122` Tùng Tán Cán Bố có **hai** giá trị `P569` cùng rank `normal` (+0604 và +0617); mục lấy 617,
  nằm trong dung sai ±25 của `Trung bình` so với cả hai.
  (3) `Q371384` Pakal `P569 = 603-03-23`, `P570 = 683-08-28` ở `precision 11` — **khớp chính xác** ngày
  mà khối 17 ghi, và khối 17 nói đúng: `precision 11` chỉ khai độ chính xác, không khai độ tin cậy.
- **Độ phủ (lint `lint_chapter`).** 5 vùng (Trung Đông/Bắc Phi 3 · Đông Á 5 · Nam Á 2 · Châu Âu 1 · Châu Mỹ 1)
  ≥ 3, và 11 lĩnh vực ≥ 4. Không cảnh báo.
- **URL trong `**Nguồn:**`.** `grep "http"` trên dòng 209–411 trả về **rỗng** — nhóm CE07 **không có URL nào**.
  §5 của `prompts/atlas-prompt.md` chỉ đòi "kèm link nếu có", nên đây không phải lỗi; hệ quả là
  danh mục bẫy URL (202/0 byte, 429 Varnish, 403 Cloudflare) **không áp dụng cho nhóm này**.
  Đổi lại, mọi nguồn đều là sách/tạp chí nên phải kiểm theo quy tắc 7 và quy tắc "không ghi số quyển nếu chưa mở mục lục" — xem từng mục.
- **Tỉ lệ phần trăm rữa (`content/ch05.md:1271`).** Không mục nào trong CE07 nêu một con số phần trăm.
  Các con số có mặt đều là niên đại hoặc số đếm tuyệt đối. Hai con số **không** phải phần trăm nhưng vẫn
  là mệnh đề định lượng không tự khai mốc đo — xem `CH05-CE07-10` (tám thế kỷ) và `CH05-CE07-09` (gần một nghìn bản chép tay).

### Phát hiện ở tầng nhóm

**[NÊN] G-1 — `Bối cảnh`: "Trường An thành đô thị lớn nhất thế giới" là một mệnh đề so sánh toàn cầu không có mốc đo và không có nguồn.**

Nguyên văn câu sai:
> Nhà Đường mở thời Trinh Quán và Trường An thành đô thị lớn nhất thế giới.

Vấn đề: mệnh đề "lớn nhất thế giới" cần một mốc năm và một phép đếm. Con số dân cư Trường An thường
được trích (≈1 triệu kể cả ngoại vi) là ước lượng cho **đỉnh thời Huyền Tông, giữa thế kỷ 8** — tức nhóm CE08,
không phải nhóm này. Trong thế kỷ 7 thì đối thủ Constantinopolis chưa bị loại khỏi cuộc so. Đây đúng
hình dạng lỗi mà quy ước ở `content/ch05.md:1271` muốn chặn: một con số/thứ hạng viết ở thì hiện tại
mà không tự khai nó đo ở đâu.

Câu thay thế đề xuất, nguyên văn:
> Nhà Đường mở thời Trinh Quán, và Trường An được quy hoạch lại thành kinh đô có mặt bằng lớn nhất Đông Á.

Soi lại chính câu thay thế: "mặt bằng lớn nhất Đông Á" vẫn là một mệnh đề so sánh — nhưng nó đo **diện tích
thành quách quy hoạch**, thứ có bản đồ khảo cổ, và giới hạn phạm vi so sánh về Đông Á thay vì toàn cầu.
`[KHÔNG KIỂM ĐƯỢC]` — vòng này **không truy được tới một nguồn khảo cổ cho con số diện tích**, chỉ loại trừ
được mệnh đề toàn cầu. Nếu không muốn mang theo một mệnh đề chưa truy nguồn, **cắt hẳn vế so sánh**;
câu vẫn đứng được: "Nhà Đường mở thời Trinh Quán và quy hoạch lại kinh đô Trường An."
Đếm: bản gốc `Bối cảnh` 56 chữ; bản cắt hẳn 55 chữ; bản thay thế 57 chữ — cả ba đều dưới trần 78.

---
## `CH05-CE07-01` · Muhammad — dòng 212–228

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q9458` → nhãn en `Muhammad`, vi `Muhammad`, `P31 = Q5`. Đúng người.
- Niên đại `k. 570–632 CN`, `độ tin cậy: Trung bình` (dung sai ±25). Wikidata `P569` rank `preferred`
  `+0571-04-20/p11`, và một giá trị `normal` `+0570/p9`; `P570` `+0632-06-08/p11`. Khớp cả hai đầu.
- "Từ khoảng năm 610 ông bắt đầu đọc ra những lời…" — mốc 610 là niên đại truyền thống, và câu đã rào
  bằng "khoảng" cộng "mà tín đồ coi là mặc khải". Không khẳng định thay người đọc.
- "Năm 622 ông rời Mecca ra Yathrib, mốc khởi đầu lịch Hồi giáo" — đúng, và `CH05-CE07-02` trong cùng nhóm
  rào thêm rằng việc *đặt* mốc ấy là quy gán muộn. Hai mục nhất quán với nhau.
- "tiểu sử đầy đủ sớm nhất là của Ibn Ishaq, soạn hơn một thế kỷ sau" — Ibn Ishaq k. 699–767, Muhammad mất 632;
  phần Sīra soạn ở Baghdad dưới al-Manṣūr, tức khoảng 120–135 năm sau. "Hơn một thế kỷ" đúng.
- Nguồn 1 tồn tại và đúng thể loại: A. Guillaume, *The Life of Muhammad: A Translation of Isḥāq's Sīrat Rasūl Allāh*,
  Oxford University Press, 1955. Đúng nhà xuất bản, đúng năm, và đúng là **bản dịch** chứ không bị ghi nhầm thành chuyên khảo
  (loại lỗi Fried & Unguru mà quy tắc 7 nêu).
- Nguồn 2 tồn tại: Fred M. Donner, *Muhammad and the Believers: At the Origins of Islam*, Harvard University Press, 2010.
  Đúng nhà xuất bản, đúng năm. (Luận điểm của nó thì có vấn đề — xem phát hiện 01-2.)
- Hai dòng `Ảnh hưởng tới` trỏ `CH05-CE07-02` và `CH05-CE07-03`: mở ra đọc, đúng là Umar và Ali, cả hai
  là bạn đồng hành đương thời, nên `trực tiếp` ở đây là nghĩa **người–người** thật, không phải nghĩa văn bản.
  Đây là hai trong số ít dòng `trực tiếp` của nhóm dùng đúng nghĩa.
- Quy tắc 6: mục này không nêu tên ai làm ứng viên bị loại, nên không có gì để va chạm.
- `ideas` 112 chữ (≤ 130), `why` 83 chữ (≤ 104).

### Phát hiện

**[BẮT BUỘC] 01-1 — Donner 2010 bị dẫn ngược luận điểm trung tâm của chính nó (quy tắc 7).**

Nguyên văn câu được nguồn đỡ:
> Việc tôn giáo và nhà nước khởi sinh cùng lúc trong một đời người là điều phân biệt trường hợp này.

Luận điểm trung tâm của Donner trong đúng cuốn được dẫn là ngược lại ở nửa "tôn giáo": phong trào khởi đầu
là một **phong trào "Người tin" (Believers) độc thần bao gồm cả Kitô hữu và người Do Thái ngay thẳng**, và
nó **chỉ tách ra thành một tôn giáo riêng biệt dưới thời Abd al-Malik (685–705)**, tức hơn nửa thế kỷ sau
khi Muhammad mất. Dẫn Donner để đỡ cho "tôn giáo … khởi sinh … trong một đời người" là đúng loại lỗi mà
`CONTRIBUTING.md` quy tắc 7 mô tả bằng ca Hansen: nguồn tồn tại, đúng chủ đề, mà luận điểm thì chống lại
câu nó đang đỡ. Lưu ý Donner vẫn đỡ được vế **nhà nước** và vế sự sớm của văn bản Qur'an (ông phản bác
Wansbrough về niên đại muộn), nên nguồn không phải bỏ — chỉ phải sửa câu.

Câu thay thế đề xuất, nguyên văn:
> Việc một cộng đồng tín ngưỡng và một bộ máy cai trị khởi sinh cùng lúc trong một đời người là điều phân biệt trường hợp này; còn việc cộng đồng ấy tách hẳn khỏi Kitô hữu và người Do Thái thành một tôn giáo riêng thì theo Donner phải tới đời Abd al-Malik.

Soi lại chính câu thay thế: (a) "cộng đồng tín ngưỡng và bộ máy cai trị khởi sinh cùng lúc" — đoạn văn ngay
trên đã dẫn chứng cho vế này ("ông không chỉ giảng mà còn cầm quyền, xử kiện và chỉ huy quân"), nên không
mượn mệnh đề mới. (b) Vế Abd al-Malik được **quy thẳng cho Donner** chứ không viết như sự thật đã chốt —
cần thiết, vì luận điểm này bị phản bác công khai (Patricia Crone chê rằng bằng chứng trực tiếp chỉ gồm
vài câu Qur'an, phần còn lại là suy đoán). Cách quy nguồn ấy làm câu đứng được bất kể tranh luận ngả về đâu.
(c) Đếm: thay câu cũ (23 chữ) bằng câu mới (45 chữ) đưa `ideas` từ 112 lên **134 chữ, VƯỢT trần 130**.
Nên dùng bản rút gọn sau, 112 + 10 = **122 chữ**:
> Việc một cộng đồng tín ngưỡng và một bộ máy cai trị khởi sinh cùng lúc trong một đời người là điều phân biệt trường hợp này; theo Donner, việc cộng đồng ấy tách thành một tôn giáo riêng thì muộn hơn nhiều.

**[NÊN] 01-2 — "nay chỉ còn qua bản hiệu đính của Ibn Hisham" là sai: Sīra còn qua nhiều đường truyền, không chỉ một.**

Nguyên văn câu sai:
> Niên đại để Trung bình vì tiểu sử đầy đủ sớm nhất là của Ibn Ishaq, soạn hơn một thế kỷ sau và nay chỉ còn qua bản hiệu đính của Ibn Hisham; các mốc năm sinh do truyền thống dựng ngược.

Chữ **"chỉ"** là chỗ sai. Sīra của Ibn Ishaq còn lại qua **nhiều** bản truyền (recension), không riêng
bản Ibn Hisham: al-Ṭabarī truyền một mạch riêng, và bản của Yūnus ibn Bukayr còn lại từng phần. Điều này
quan trọng về phương pháp chứ không phải chi tiết vụn — chính việc có nhiều mạch truyền độc lập là cơ sở để
so chéo, và câu hiện tại xoá mất cơ sở ấy. Mỉa mai là mục `CH05-CE07-02` và `CH05-CE07-03` cùng nhóm đều
dẫn al-Ṭabarī, tức atlas đã dùng chính cái mạch truyền mà câu này phủ nhận.

Câu thay thế đề xuất, nguyên văn:
> Niên đại để Trung bình vì tiểu sử đầy đủ sớm nhất là của Ibn Ishaq, soạn hơn một thế kỷ sau và nay chỉ còn qua các bản truyền đời sau, quen thuộc nhất là bản Ibn Hisham; các mốc năm sinh do truyền thống dựng ngược.

Soi lại chính câu thay thế: "chỉ còn qua các bản truyền đời sau" là mệnh đề đã kiểm (không có bản gốc
Ibn Ishaq nào còn); "quen thuộc nhất là bản Ibn Hisham" cũng đã kiểm. Câu thay thế **không nêu tên mạch
truyền thứ hai**, cố ý — nêu tên al-Ṭabarī hay Yūnus ibn Bukayr sẽ kéo theo chi tiết mà vòng này chưa mở
tới bản in để xác nhận phạm vi từng mạch. `why` đi từ 83 lên **86 chữ**, vẫn dưới trần 104.

**[CÂN NHẮC] 01-3 — "Không có ứng viên cùng chỗ" là hợp lệ theo quy tắc 5 nhưng hai mục kế bên làm nó đọc như tự mâu thuẫn.**

Nguyên văn:
> Không có ứng viên cùng chỗ: không nhân vật nào khác trong vùng ở thế kỷ 7 có phạm vi gần tương đương.

`CONTRIBUTING.md` quy tắc 5 cho phép viết thẳng là không có ai — đó là một phát hiện về tư liệu.
Nhưng `CH05-CE07-02` (Umar) và `CH05-CE07-03` (Ali) **cùng vùng, cùng thế kỷ, cùng lĩnh vực**, nên câu
"không nhân vật nào khác trong vùng ở thế kỷ 7" đọc như bị hai mục sau nó bác, dù ý thật là "không ai
tranh suất này". Ghi chú biên tập đo CE07 là **12/12** về thể thức nêu đích danh ứng viên bị loại; theo
cách đếm chặt thì mục này **không nêu tên ai**, nên con số ấy nên được đọc lại là 11/12.

Câu thay thế đề xuất, nguyên văn:
> Không có ứng viên tranh suất này: ba mục Trung Đông của nhóm — Umar và Ali là hai mục kia — đều quy về ông, và không nhân vật nào khác trong vùng ở thế kỷ 7 có phạm vi gần tương đương.

Soi lại chính câu thay thế: nó **không** nêu Umar và Ali làm "ứng viên bị loại" (hai người đã có mục riêng,
làm vậy sẽ vi phạm đúng quy tắc 6); nó nêu họ làm hai mục song song, đúng tinh thần câu mẫu ở
`CONTRIBUTING.md:51`. Mệnh đề "không ai khác trong vùng ở thế kỷ 7 có phạm vi gần tương đương" được giữ
nguyên từ bản gốc vì nó là **phán đoán đánh giá theo bốn tiêu chí**, không phải mệnh đề sự kiện cần kiểm.
`why` đi từ 83 lên **94 chữ**, vẫn dưới trần 104. Nếu muốn ngắn, cắt vế "và không nhân vật nào … tương đương"
thì câu vẫn đứng được (85 chữ).

**[CÂN NHẮC] 01-4 — `trực tiếp` dùng cho một đích không phải người.**

Nguyên văn:
> - Tục lệ bộ lạc Quraysh ở Mecca · phản bác · trực tiếp

Đích là một **tập tục**, không phải một người. Đây đúng ca mà khối ghi chú chapter (`content/ch05.md:1270`)
nói lint mù: `trực tiếp` đang mang hai nghĩa. Nhóm CE07 có **13 dòng `trực tiếp`**, trong đó chỉ **4**
chỉ quan hệ người–người thật (CE07-01→02, CE07-01→03, CE07-04→05, CE07-12→Kan Bahlam II).
Tôi **không đề xuất sửa từng dòng ở vòng này**: ghi chú chapter đã kết luận đúng rằng đây phải xử ở tầng
`CONTRIBUTING.md` chứ không vá từng mục. Ghi ở đây để nhóm CE07 có con số của riêng nó: **4/13**.

---
> **Đính chính cho chính báo cáo này (ghi ngay khi phát hiện, không sửa ngược lên trên).**
> Con số "13 dòng `trực tiếp`" ở phát hiện 01-4 là **sai** — tôi đếm bằng mắt thay vì bằng `grep`.
> Số đúng: `sed -n '209,411p' content/ch05.md | grep -c "· trực tiếp$"` → **29 dòng**. Phân loại lại:
> - **7 dòng là quan hệ người–người thật** (hai bên có tiếp xúc trong đời): CE07-01→02, CE07-01→03,
>   CE07-02←01, CE07-03←01, CE07-04→05, CE07-05←04, CE07-12→Kʼinich Kan Bahlam II.
> - **19 dòng có đích KHÔNG phải người** (tập tục, chế độ, lịch, phái, tầng quan lại, nghệ thuật, tông phái,
>   ngành khảo cổ, chương trình học, truyền thống, đế quốc, vương triều, thành bang).
> - **3 dòng có đích là người nhưng hai bên chưa bao giờ gặp nhau**: CE07-04 ← `CH05-CE06-06` (Tùy Văn Đế mất 604,
>   Thái Tông khi ấy 6 tuổi), CE07-08 → `CH04-CE05-09` (Āryabhaṭa 476–550 so với Brahmagupta k. 598–668),
>   CE07-10 ← `CH05-CE06-05` (Trần-na so với Pháp Xứng). Ca thứ ba là ca nặng nhất và được tách ra
>   thành phát hiện riêng ở mục `CH05-CE07-10` bên dưới, vì `CONTRIBUTING.md` quy tắc 8 nêu đích danh
>   hình dạng này ("`trực tiếp` giữa hai người cách nhau 130 năm mà vẫn đúng thứ tự").
>
> Tỉ lệ đúng của nhóm CE07 vì vậy là **7/29**, không phải 4/13. Để so: ghi chú chapter đo nhóm CE10
> được "khoảng ba trong 19 dòng". Mốc đo của con số này: **nhóm CE07 như đang nằm ở `content/ch05.md`
> dòng 209–411, ngày 2026-11-02** — ghi mốc theo đúng quy ước `content/ch05.md:1271`.

---
## `CH05-CE07-02` · Umar ibn al-Khattab — dòng 229–245

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q8467` → nhãn en `Umar ibn Al-Khattāb`, `P31 = Q5`. Đúng người (không phải Umar II `Q314914`).
- `k. 586–644 CN`, `Trung bình` (±25). Wikidata `P569 +0586/p9`, `P570` rank `preferred` `+0644-11-03/p11`. Khớp.
- "Trong mười năm làm caliph từ 634" — 634–644, đúng mười năm.
- "Sasanian … sụp hẳn năm 651, sau khi ông đã chết" — đúng, và đây chính là chỗ khối 20 ghi là đã sửa
  (bản thảo đầu quy việc ấy cho nhiệm kỳ Umar và tự mâu thuẫn với `CH05-CE06-03`). **Bản hiện tại đã đúng**,
  và tôi đã mở `CH05-CE06-03` ra đối chiếu: mục Khosrow I cũng ghi 651. Hai mục nay nhất quán.
- "dīwān, sổ lương xếp theo thâm niên theo đạo và quan hệ với nhà tiên tri chứ không theo công trạng chiến trận"
  — đúng, và đúng là rào mà khối 20 yêu cầu (*sābiqa* / *qarāba*, không phải công trạng).
- "đặt Kufa, Basra và Fustat làm trung tâm cai trị" — ba *amṣār* đúng, đều lập dưới thời ông.
- "Việc lấy năm 622 làm năm gốc cho lịch Hồi giáo là do truyền thống quy cho ông, không phải do chứng cứ
  đương thời" — rào đúng theo khối 20 (giấy cói PERF 558 năm 643 không nhắc hijra lẫn người đặt ra nó).
- **Số quyển al-Ṭabarī đã tra tới nhan đề, không đoán** (quy tắc "không ghi số quyển nếu chưa mở mục lục").
  Tra OpenLibrary: vol. **XII** = *The Battle of al-Qādisiyyah and the Conquest of Syria and Palestine*;
  vol. **XIII** = *The Conquest of Iraq, Southwestern Persia, and Egypt*; vol. **XIV** = *The Conquest of Iran,
  A.D. 641–643/A.H. 21–23*. Cả ba đúng chủ đề mục đang dẫn, và đúng là bản SUNY Press. Không có ca lệch +1
  như sáu số chương Keith Taylor mà `CONTRIBUTING.md:48` mô tả.
- Nguồn 2 tồn tại và đúng: Hugh Kennedy, *The Great Arab Conquests*, Da Capo Press, 2007 (bản Anh là
  Weidenfeld & Nicolson cùng năm). Quy tắc 7: luận điểm của Kennedy — các cuộc chinh phục có thật, nhanh,
  và bộ máy cũ phần lớn được giữ lại — **đỡ đúng** câu mục đang viết, không bị dẫn ngược.
- Quy tắc 6: Abu Bakr (caliph đầu tiên) và Khalid ibn al-Walid đều **không có mục ở bất kỳ chapter nào**.
  `grep` trúng `CH05-CE10-02 · Abu Bakr al-Rāzī` là một người hoàn toàn khác (thầy thuốc Ba Tư thế kỷ 10).
  Cả hai đều thật sự cùng thời với Umar (quy tắc 5): Abu Bakr mất 634, Khalid mất 642, Umar 586–644 — chồng lấn thật.
- `ideas` **130 chữ — đúng bằng trần 130**. `why` 79 chữ. Hệ quả thực hành: **mọi đề xuất sửa cho mục này
  phải là trao đổi chữ, không được thêm ròng.** Các câu thay thế dưới đây đều tuân thủ điều đó.

### Phát hiện

**[BẮT BUỘC] 02-1 — Dòng quan hệ "Lịch Hijri · kế thừa · trực tiếp" bác chính câu rào trong phần văn xuôi của mục.**

Nguyên văn hai chỗ đá nhau:
> Việc lấy năm 622 làm năm gốc cho lịch Hồi giáo là do truyền thống quy cho ông, không phải do chứng cứ đương thời.

> - Lịch Hijri · kế thừa · trực tiếp

Mục bỏ công rào rằng việc đặt lịch **chỉ là quy gán của truyền thống**, rồi dòng quan hệ lại khai mức bằng
chứng cao nhất, `trực tiếp`, cho đúng mệnh đề vừa rào. Hai dòng không thể cùng đúng. Đây không phải chuyện
`trực tiếp` mang hai nghĩa (vấn đề ở tầng chapter) mà là một mâu thuẫn nội tại trong một mục, và nó **sửa
được ngay ở tầng mục** mà không cần đợi `CONTRIBUTING.md` định nghĩa lại từ vựng.

Dòng thay thế đề xuất, nguyên văn:
> - Lịch Hijri · kế thừa · suy đoán học giả

Soi lại chính dòng thay thế: `suy đoán học giả` nằm trong `EVIDENCE_LEVELS` của `atlaslib/common.py` nên
lint nhận; và nó là mức duy nhất trong ba mức khớp với trạng thái bằng chứng mà mục tự mô tả (quy gán
truyền thống, chứng cứ đương thời sớm nhất không nhắc tới người đặt). Không thêm chữ nào vào `ideas`,
nên trần 130 không bị động tới.

**[NÊN] 02-2 — Lĩnh vực `Luật` không có một chữ nào trong mục đỡ.**

Nguyên văn dòng metadata:
> `năm: k. 586–644 CN | nơi: Medina | vùng: Trung Đông/Bắc Phi | lĩnh vực: Chính trị/Nhà nước, Luật | …`

Đọc hết 130 chữ của `ideas` và 79 chữ của `why`: mục nói về **biên giới, dīwān, bộ máy hành chính địa phương,
ba thành trấn, và lịch**. Không có một mệnh đề nào về luật — không chế định, không toà, không *qāḍī*.
Lint không bắt được vì `Luật` nằm trong `FIELDS` và tổng số lĩnh vực là 2 (≤ 2). Nhưng thống kê lĩnh vực
toàn atlas đang được đọc như một phép đo nội dung (xem các khối 24, 33, 38 của Ghi chú biên tập), nên một
nhãn không có nội dung đỡ sẽ làm hỏng chính phép đo ấy. Hai cách sửa, và tôi đề xuất cách (b):

(a) Đổi nhãn: `lĩnh vực: Chính trị/Nhà nước, Kinh tế` — `Kinh tế` thì có nội dung đỡ thật (dīwān là sổ lương,
cộng chế độ thuế đất ở dòng `Ảnh hưởng tới`).

(b) Giữ nhãn `Luật` và đưa nội dung đỡ vào mục, bằng cách **trao đổi chữ** chứ không thêm ròng.
Câu thay thế đề xuất, nguyên văn — thay câu:
> Phần bền hơn là cách tổ chức.

bằng:
> Phần bền hơn là cách tổ chức, kể cả việc tách người xử kiện khỏi người cầm quân ở các tỉnh.

Soi lại chính câu thay thế: đây là chỗ **tôi phải tự khai**. `[KHÔNG KIỂM ĐƯỢC]` — vòng này **không truy
được tới nguồn gốc** cho mệnh đề Umar là người đặt ra chế độ *qāḍī* tách khỏi tổng trấn; đó là một quy gán
rất phổ biến trong sách phổ thông, và nó mang **đúng hình dạng** của những quy gán muộn mà chính mục này
đã phải rào hai lần (lịch Hijri, dīwān). Tôi không mở được bản in Kennedy 2007 để xác nhận. Vì vậy:
**đừng dùng phương án (b) trừ khi có người mở được nguồn.** Phương án đứng được mà không cần kiểm thêm là
**(a) đổi `Luật` thành `Kinh tế`**, hoặc bỏ hẳn lĩnh vực thứ hai và để một mình `Chính trị/Nhà nước` —
lint cho phép một lĩnh vực (`CH05-CE07-05` trong cùng nhóm đang làm đúng vậy).

**[CÂN NHẮC] 02-3 — `Kế thừa từ CH05-CE06-03` (Khosrow I) đúng người nhưng không có một chữ nào trong mục nối hai cái tên lại.**

Nguyên văn:
> - CH05-CE06-03 · kế thừa · qua trường phái

Tôi đã mở đích ra đọc: `CH05-CE06-03` là **Khosrow I (Anushirvan)**, đúng người mà một dòng "kế thừa bộ máy
hành chính" phải trỏ tới — nên **đây không phải ca trỏ sai người**. Mức `qua trường phái` cũng đúng, không
thổi phồng. Vấn đề nhỏ hơn: phần văn xuôi chỉ viết "giữ nguyên bộ máy hành chính địa phương thay vì thay thế",
không nói bộ máy ấy là **bộ máy Sasanian do Khosrow I cải tổ**, nên người đọc không có cách nào nối được
dòng quan hệ với nội dung. Lint ghi dòng này ở mức `INFO` (bất đối xứng — `CH05-CE06-03` không ghi chiều ngược),
và P4 sẽ đồng bộ, nên không cần làm gì ở vòng này; ghi để P4 biết nối về đâu.

Câu thay thế đề xuất, nguyên văn — thay:
> giữ nguyên bộ máy hành chính địa phương thay vì thay thế;

bằng:
> giữ nguyên bộ máy thuế khoá Sasanian và Byzantine ở địa phương thay vì thay thế;

Soi lại chính câu thay thế: mệnh đề "giữ nguyên bộ máy thuế khoá địa phương của hai đế chế cũ" là **luận điểm
trung tâm của Kennedy 2007**, tức nguồn đã dẫn đỡ đúng cho nó — không phải một mệnh đề mới chưa kiểm.
Đếm: câu cũ 10 chữ, câu mới 13 chữ → `ideas` đi từ 130 lên **133, VƯỢT trần 130**. Để bù, cắt ba chữ ở chỗ
thừa nhất trong cùng câu: "còn Sasanian bị đánh gãy xương sống rồi sụp hẳn năm 651" → "còn Sasanian sụp hẳn
năm 651" (−4 chữ), đưa tổng về **129**. Lưu ý phép cắt này **không** làm mất mệnh đề nào đã kiểm.

---
## `CH05-CE07-03` · Ali ibn Abi Talib — dòng 246–261

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q39619` → nhãn en `Alī ibn Abī Ṭālib`, `P31 = Q5`. Đúng người.
- `k. 599–661 CN`, `Trung bình`. Wikidata `P569 +0599-03-17/p11`, `P570 +0661/p9`. Khớp cả hai đầu.
- "Em họ và con rể nhà tiên tri" — đúng: anh em họ bên nội, và chồng Fatima.
- "làm caliph từ năm 656" — đúng (sau khi Uthman bị giết tháng 6 năm 656).
- Thứ tự hai trận **đúng**: Lạc Đà (cuối 656) trước Siffin (657). Đây là loại lỗi rất dễ mắc và mục không mắc.
- "việc ông chấp nhận phân xử khiến một bộ phận quân mình ly khai thành phái Khawarij — và chính một người
  trong số đó giết ông năm 661" — đúng chuỗi nhân quả, và đúng năm.
- "Nahj al-Balāgha gán cho ông được biên soạn thế kỷ 10 nên không dùng làm nguồn tiểu sử" — kiểm được:
  người biên soạn là al-Sharīf al-Raḍī (970–1015), và niên đại biên soạn được mô tả rộng rãi là thế kỷ 10.
  Việc **chủ động loại một văn bản khỏi vai trò nguồn tiểu sử** vì niên đại là đúng tinh thần quy tắc 7.
- **Số quyển al-Ṭabarī đã tra tới nhan đề:** vol. **XVI** = *The Community Divided: The Caliphate of ʿAlī,
  A.D. 656–657/A.H. 35–36*; vol. **XVII** = *The First Civil War*. Cả hai khớp chính xác khoảng thời gian
  và chủ đề mục đang dẫn. Không đoán số quyển.
- Nguồn 1 tồn tại: Wilferd Madelung, *The Succession to Muhammad: A Study of the Early Caliphate*,
  Cambridge University Press (bản bìa cứng 1996, bản thường dẫn 1997). Đúng tác giả, đúng nhà xuất bản.
- Quy tắc 7, phần làm **đúng**: mục tự khai rằng nguồn chính của nó nghiêng một phía, và tự khai rằng nó
  không chọn phía. Đây là cách xử lý đúng chứ không phải lỗi — ghi nhận riêng vì nó hiếm.
- Quy tắc 6: **Uthman** và **Mu'awiya** đều không có mục ở bất kỳ chapter nào (`grep` 285 mục; ca trúng
  `CH05-CE08-05 · Sibawayh (Amr ibn Uthman)` chỉ là tên đệm của một người khác). Quy tắc 5: cả hai thật sự
  cùng thời — Uthman mất 656, Mu'awiya 602–680, Ali k. 599–661. Chồng lấn thật, không phải ca lệch thế kỷ.
- `ideas` 103 chữ, `why` 94 chữ. Cả hai dưới trần.

### Phát hiện

**[NÊN] 03-1 — Trường "Tư tưởng / đóng góp chính" không chứa một đóng góp nào của nhân vật.**

Nguyên văn cả trường (103 chữ) kể: ông làm caliph, hai trận đánh xảy ra, một phái ly khai, ông bị giết, và
một **câu hỏi** mở ra. Không có một ý tưởng, một văn bản, hay một thiết chế nào do ông tạo. Chính mục cũng
thừa nhận điều này ở trường kế bên:
> kết cục quân sự thuộc về Mu'awiya, nhưng câu hỏi mở ra quanh Ali mới là thứ sống tiếp.

Tức mục chọn một người vì ông là **dịp** của một câu hỏi chứ không phải tác giả của nó. Template §5 đòi
trường này nêu "ý tưởng cốt lõi, tác phẩm hoặc thành tựu tiêu biểu". Lint không bắt được vì nó chỉ đếm chữ.
Đáng nói là atlas đã có tiền lệ xử đúng ca này: `CH05-CE07-12` trong cùng nhóm **tự khai thẳng** một khuyết
tật của tiêu chí phạm vi thay vì giấu nó. Mục này nên làm cùng một việc, hoặc nêu được một đóng góp thật.

Câu thay thế đề xuất, nguyên văn — thêm vào cuối trường `Vì sao chọn`:
> Phải nói thẳng một chỗ yếu: mục này chọn theo (b) chứ không theo (c), vì cái sống tiếp là câu hỏi mở ra quanh ông, không phải một văn bản hay thiết chế do ông lập.

Soi lại chính câu thay thế: nó **không mang theo mệnh đề sự kiện mới nào** — chỉ phát biểu lại điều mục
đã viết, nên không có gì phải kiểm thêm. Đếm: `why` đi từ 94 lên **124 chữ, VƯỢT trần 104**. Để nằm trong
trần, dùng bản ngắn (+9 chữ → **103**):
> Chỗ yếu phải nói thẳng: chọn theo (b), không theo (c) — cái sống tiếp là câu hỏi, không phải văn bản của ông.

**[NÊN] 03-2 — Một đích tự do nay đã giải được thành ID, đúng hình dạng mà ghi chú chapter mô tả.**

Nguyên văn:
> - Phái Shia và chế độ imam · kế thừa · trực tiếp

`CH05-CE08-03` trong cùng chapter là **Jaʿfar al-Sadiq** — tôi đã mở ra đọc tên để xác nhận — và mục ấy
**đã ghi chiều ngược rồi**: `reports/lint-ch05.txt` có dòng
`[INFO] CH05-CE08-03: kế thừa từ CH05-CE07-03 nhưng CH05-CE07-03 không ghi 'Ảnh hưởng tới' CH05-CE08-03`.
Tức liên kết đã tồn tại một chiều và chỉ thiếu chiều này. Đây đúng ca mà khối 43 của Ghi chú biên tập
(`content/ch05.md:1243`) gọi là "đích tự do nay giải được". Nâng nó lên ID vừa xoá một dòng `INFO`,
vừa thay một đích trừu tượng bằng một người thật.

Dòng thay thế đề xuất, nguyên văn:
> - CH05-CE08-03 · kế thừa · qua trường phái

Soi lại chính dòng thay thế: (a) đích đã **mở ra đọc tên**, đúng là Jaʿfar al-Sadiq, không phải ca trỏ sai
người. (b) Mức bằng chứng để `qua trường phái` chứ **không** giữ `trực tiếp`: Ali mất 661, Jaʿfar sinh k. 702 —
hai người **chưa bao giờ gặp nhau**, nên `trực tiếp` ở đây sẽ tái lập đúng cái lỗi mà `CONTRIBUTING.md`
quy tắc 8 nêu đích danh và mà tôi đang chẩn ở `CH05-CE07-10`. Tôi cố ý không lặp lại lỗi mình vừa chẩn.
(c) Dòng này **thay** dòng cũ chứ không thêm, nên vẫn trong trần 3 mục của `Ảnh hưởng tới`.

**[CÂN NHẮC] 03-3 — Một so sánh cấp nhất về giới nghiên cứu, phát biểu như sự kiện, không có gì đỡ.**

Nguyên văn:
> Madelung 1997, nguồn chính của mục, nghiêng về phía Alid rõ nhất trong giới hiện đại.

Việc Madelung nghiêng về phía Alid là nhận định phổ biến và mục nêu nó là đúng tinh thần quy tắc 7.
Chỗ vượt quá là hai chữ **"rõ nhất"**: đó là một xếp hạng trên toàn bộ giới nghiên cứu hiện đại, phát biểu
ở thì hiện tại, không kèm ai đã xếp hạng và theo thước nào — cùng họ với loại mệnh đề mà quy ước ở
`content/ch05.md:1271` muốn chặn. `[KHÔNG KIỂM ĐƯỢC]` — vòng này **không truy được tới một bài điểm sách
hay khảo luận sử học nào xếp hạng như vậy**; chỉ xác nhận được rằng sách tồn tại và tác giả đúng.

Câu thay thế đề xuất, nguyên văn:
> Madelung 1997, nguồn chính của mục, đọc chuỗi biến cố nghiêng về phía các yêu sách của dòng Ali.

Soi lại chính câu thay thế: đã **bỏ hẳn xếp hạng cấp nhất** — thứ tôi không kiểm được — và giữ lại đúng
phần kiểm được, là chiều nghiêng của cuốn sách. Không mệnh đề nào trong câu thay thế còn cần kiểm thêm.
Đếm: câu cũ 16 chữ, câu mới 18 chữ → `why` từ 94 lên **96**, vẫn dưới trần 104. Nếu đồng thời áp cả
03-1 (bản ngắn, +9) thì tổng là **105 chữ, VƯỢT trần 104 đúng một chữ**; khi ấy bỏ hai chữ "nguồn chính của mục"
→ **102**, và câu vẫn đứng được vì trường `Nguồn` đã nói Madelung đứng đầu danh sách.

---
## `CH05-CE07-04` · Đường Thái Tông — dòng 262–277

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q9701` → nhãn en `Emperor Taizong of Tang`, vi `Đường Thái Tông`, `P31 = Q5`. Đúng người.
- `598–649 CN`, `độ tin cậy: Cao` (dung sai ±5, chặt nhất). Wikidata `P569 +0598-01-28/p11`,
  `P570 +0649-07-10/p11`. Khớp chính xác tới năm; `Cao` đứng được.
- "lên ngôi năm 626 sau khi giết hai anh em ở cửa Huyền Vũ rồi ép cha thoái vị" — đúng cả ba vế và đúng năm.
- **Mệnh đề hai bộ luật, kiểm riêng vì đây là chỗ khối 20 ghi là đã sửa một lần.** Bản hiện tại đúng:
  Trinh Quán luật là bản chỉnh năm **637** dưới triều ông; *Đường luật sớ nghị* (唐律疏議) là phần **sớ nghị
  năm 653**, dưới triều Cao Tông. Kiểm chéo cho thấy mục còn **thận trọng hơn mức cần thiết** theo hướng tốt:
  bộ luật được ban năm 652 và sớ nghị thêm năm 653, nên con số 653 của mục là con số của phần sớ nghị, đúng
  như tên gọi mục dùng. **Không đề nghị sửa chỗ này.**
- "sau khi đánh bại Đông Đột Quyết năm 630 thì nhận hiệu Thiên Khả Hãn" — đúng năm, đúng danh hiệu.
- "ông duy trì ban gián quan có quyền phản bác hoàng đế" — đúng, và đây là đúng vế mà nguồn Wechsler đỡ được.
- Quy tắc 7 làm **đúng**: mục tự ghi "lưu ý đây là chuyên khảo về Ngụy Trưng và chế độ gián quan, dùng cho
  vế ấy chứ không dùng cho vế bộ luật", rồi bổ sung Wallace Johnson cho vế luật. Đã xác nhận
  **Wallace Johnson, *The T'ang Code*, Princeton University Press, 1979** tồn tại đúng như ghi (tập I;
  tập II ra 1997). Đây là cách xử đúng loại lỗi "nguồn đúng chủ đề nhưng sai phạm vi".
- "việc ông can thiệp vào khởi cư chú được chép lại" — mục **không khẳng định** chính sử đã bị sửa, chỉ nói
  "có dấu hiệu đã được sửa" và việc can thiệp "được chép lại". Rào đúng mức.
- Quy tắc 6: **Đường Cao Tổ** và **Ngụy Trưng** đều không có mục ở bất kỳ chapter nào (quét 285 mục).
  Quy tắc 5: cả hai thật sự cùng thời (Cao Tổ 566–635, Ngụy Trưng 580–643, Thái Tông 598–649).
- `ideas` 124 chữ, `why` 82 chữ. Dưới trần.
- Nguồn Wechsler: tồn tại, đúng tác giả, đúng nhà xuất bản Yale University Press. **Ghi chú không thành
  phát hiện:** năm in xuất hiện ở cả **1974 và 1975** trong các bản ghi thư mục tra được (Internet Archive
  có cả hai; OpenLibrary chỉ có 1975). Mục ghi 1974, nằm trong vùng hợp lệ. `[KHÔNG KIỂM ĐƯỢC]` phần phân
  biệt lần in đầu — Library of Congress trả **HTTP 403** (đúng loại bẫy mà khối 13 liệt kê), và tôi không
  mở được trang bản quyền của sách.

### Phát hiện

**[BẮT BUỘC] 04-1 — Câu "Vì sao chọn" lấy lại đúng mệnh đề mà phần "Tư tưởng" của chính nó vừa đính chính.**

Nguyên văn câu sai:
> Thái Tông được chọn theo phạm vi (a): khuôn triều đình, bộ luật và chế độ khảo hạch thời ông được Nhật Bản, Triều Tiên và Việt Nam mô phỏng trực tiếp, nên ảnh hưởng vượt hẳn ra ngoài Trung Hoa.

Hai lỗi chồng lên nhau:

(1) **Bộ luật được Đông Á mô phỏng không phải bộ luật "thời ông".** Chính mục, cách đó bốn dòng, đã bỏ công
đính chính rằng bộ quen thuộc là *Đường luật sớ nghị* năm 653 dưới triều Cao Tông, chứ không phải Trinh Quán
luật 637. Rồi `Vì sao chọn` quy toàn bộ sức nặng "mô phỏng trực tiếp" về "bộ luật … thời ông". Khối 20 của
Ghi chú biên tập ghi rõ mệnh đề này đã bị vòng kiểm sự kiện bác một lần; nó đã được sửa ở trường `ideas`
nhưng **sót lại ở trường `why`**. Lint không thể bắt được vì nó không đọc nghĩa.

(2) **"Việt Nam mô phỏng trực tiếp" sai ở cả chủ thể lẫn thời điểm.** Thế kỷ 7–9 Việt Nam nằm **trong**
nhà Đường với tư cách An Nam đô hộ phủ (từ năm 679) — đây là điều chính Ghi chú biên tập của chapter ghi ở
khối 22 (`content/ch05.md:1138`). Một đơn vị hành chính bị áp luật không phải một nhà nước "mô phỏng".
Mục vì vậy tự mâu thuẫn với ghi chú của chính chapter mình.

Câu thay thế đề xuất, nguyên văn:
> Thái Tông được chọn theo phạm vi (a): khuôn triều đình và chế độ khảo hạch định hình ở thời ông, rồi bộ Đường luật hoàn chỉnh ngay sau đó, thành mẫu mà Nhật Bản và Triều Tiên dựng lại thể chế theo, nên ảnh hưởng vượt hẳn ra ngoài Trung Hoa.

Soi lại chính câu thay thế: (a) đã **bỏ Việt Nam** — đó là vế sai, và bỏ nó làm câu đúng lên chứ không yếu đi.
(b) Đã tách "bộ Đường luật hoàn chỉnh ngay sau đó" khỏi "thời ông", nên không tái phạm lỗi (1).
(c) `[KHÔNG KIỂM ĐƯỢC]` — vòng này xác nhận được rằng bộ luật Đường trở thành nền cho các bộ luật đời sau
"không chỉ ở Trung Hoa mà cả nơi khác ở Đông Á", nhưng **không mở được tới văn bản bộ Taihō (701) của
Nhật hay bộ luật Silla để xác nhận chúng mô phỏng bản 653 chứ không phải bản 637**. Nếu không muốn mang
mệnh đề chưa truy được, **cắt hẳn mệnh đề về bộ luật**; câu vẫn đứng được trên hai vế còn lại:
> Thái Tông được chọn theo phạm vi (a): khuôn triều đình và chế độ khảo hạch định hình ở thời ông thành mẫu mà Nhật Bản và Triều Tiên dựng lại thể chế theo, nên ảnh hưởng vượt hẳn ra ngoài Trung Hoa.

Đếm: bản gốc `why` 82 chữ; bản đầy đủ 89 chữ; bản cắt 83 chữ. Cả hai dưới trần 104.

**[NÊN] 04-2 — "mở rộng khoa cử" được gán cho hai người khác nhau trong cùng một nhóm, và chỉ một trong hai có thể là mệnh đề chính.**

Nguyên văn ở `CH05-CE07-04`:
> mở rộng khoa cử

Nguyên văn ở `CH05-CE07-05`, cách đó mười sáu dòng:
> Bà mở rộng khoa cử và lấy người từ tầng lớp thấp hơn, làm suy yếu các dòng họ quý tộc tây bắc.

Hai mục trong cùng nhóm cùng nhận một công lao, không mục nào nhắc mục kia, và người đọc không có cách nào
biết hai lần "mở rộng" ấy khác nhau ở chỗ nào. Điều này quan trọng vì `CH05-CE07-05` dùng chính khoa cử
làm một trong hai chân của lập luận chọn người. Nền sử học thì đặt khởi điểm ở nhà **Tuỳ** và nói việc thi
cử trở thành kênh tuyển dụng **thường xuyên** trong suốt đời Đường — tức một quá trình nhiều triều, không
phải một hành động của một người.

Câu thay thế đề xuất, nguyên văn — thay "mở rộng khoa cử" ở `CH05-CE07-04` bằng:
> giữ khoa cử do nhà Tuỳ mở làm một kênh tuyển người thường xuyên

Soi lại chính câu thay thế: (a) mệnh đề "khoa cử khởi từ nhà Tuỳ" đã kiểm được và **nhất quán với
`CH05-CE06-06` Tùy Văn Đế** trong cùng chapter, vốn là đích của dòng `Kế thừa từ` ngay dưới. (b) Nó
**không** gán cho Thái Tông việc mở rộng, nên không còn va với `CH05-CE07-05`. (c) `[KHÔNG KIỂM ĐƯỢC]`:
tôi **không** kiểm được quy mô tuyệt đối (số người đỗ mỗi năm dưới triều ông) nên câu thay thế cố ý
**không nêu con số nào** — nêu một con số ở đây sẽ tái lập đúng lỗi "số không tự khai mốc đo".
Đếm: thay 3 chữ bằng 10 chữ → `ideas` từ 124 lên **131, VƯỢT trần 130 đúng một chữ**. Bỏ chữ "thường xuyên"
→ **129**, và câu vẫn đứng được.

**[CÂN NHẮC] 04-3 — "sử do chính triều ông soạn" không mô tả đúng nguồn đang được dẫn.**

Nguyên văn:
> Nguồn chính về ông là sử do chính triều ông soạn, và việc ông can thiệp vào khởi cư chú được chép lại.

Trường `Nguồn` của mục liệt kê *Cựu Đường thư* (945) và *Trinh Quán chính yếu*. *Cựu Đường thư* được soạn
dưới **Hậu Tấn**, gần ba thế kỷ sau khi ông mất — không phải "triều ông". Ý thật của câu hẳn là lớp thực lục
và quốc sử đương triều nằm **bên dưới** *Cựu Đường thư*, và ý ấy đúng; nhưng câu như đang viết thì mô tả sai
chính hai nguồn mà mục dẫn, và một người đọc đối chiếu sẽ thấy vênh ngay.

Câu thay thế đề xuất, nguyên văn:
> Nguồn chính về ông dựng trên lớp thực lục do triều đình đương thời soạn, và việc ông can thiệp vào khởi cư chú được chép lại.

Soi lại chính câu thay thế: nó **không** khẳng định *Cựu Đường thư* là sử đương triều (lỗi cũ), cũng
**không** khẳng định mức độ lớp thực lục ấy đã bị sửa — vế đó mục đã rào riêng ở trường `ideas` bằng
"có dấu hiệu đã được sửa", và tôi giữ nguyên cách rào ấy thay vì làm chặt thêm, vì `[KHÔNG KIỂM ĐƯỢC]`:
vòng này không mở được tới một khảo luận sử liệu xác định phần nào của khởi cư chú đã bị sửa.
Đếm: `why` từ 82 lên **84**; nếu áp cùng 04-1 bản cắt thì tổng là **85**, vẫn dưới trần 104.

---
## `CH05-CE07-05` · Võ Tắc Thiên — dòng 278–293

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q9738` → nhãn en `Wu Zetian`, vi `Võ Tắc Thiên`, `P31 = Q5`. Đúng người.
- `624–705 CN`, `Cao` (±5). Wikidata `P569 +0624-02-17/p11`, `P570 +0705-12-16/p11`. Khớp chính xác.
- "lập triều Chu năm 690 sau nhiều năm cầm quyền thực tế qua chồng rồi qua con" — đúng cả mốc và cả chuỗi.
- **Mệnh đề Đại Vân kinh, kiểm riêng vì khối 20 ghi đây là chỗ đã bị bác một lần.** Bản hiện tại **đúng**:
  mục gọi thứ lưu hành năm 690 là "một **bản sớ**, Đại Vân kinh Thần Hoàng thụ ký nghĩa sớ", và gọi
  Đại Vân kinh là "một kinh Ấn Độ **có thật**". Đây đúng công thức mà khối 20 chốt, và nó làm luận điểm
  chính danh của mục mạnh lên chứ không yếu đi. **Không đề nghị sửa.**
- "bà bảo trợ việc tạc tượng ở Long Môn" — đúng, và câu dùng chữ "bảo trợ" chứ không nói bà khởi xướng.
- Nguồn 2 tồn tại và đúng: R.W.L. Guisso, *Wu Tse-T'ien and the Politics of Legitimation in T'ang China*,
  Western Washington University, 1978. Đúng tên, đúng nơi in, đúng năm, và **đúng chủ đề** mệnh đề trung tâm
  của mục (chính danh) — không phải ca nguồn đúng chủ đề mà ngược luận điểm.
- Quy tắc 6: **Đường Cao Tông** (`Q9703`, 628–683) và **Địch Nhân Kiệt** (`Q445747`, 630–700) đều không có
  mục ở bất kỳ chapter nào. Quy tắc 5: cả hai chồng lấn thật với bà (624–705) — không phải ca lệch thế kỷ
  kiểu Tử Sản / Quản Trọng mà `CONTRIBUTING.md:50` mô tả.
- `Kế thừa từ CH05-CE07-04`: mở đích ra đọc, đúng là Đường Thái Tông, và hai người **có tiếp xúc thật**
  (bà vào cung ông làm tài nhân). Đây là một trong 7 dòng `trực tiếp` dùng đúng nghĩa người–người của nhóm.
- `ideas` 122 chữ, `why` 84 chữ. Dưới trần.
- Lĩnh vực chỉ một (`Chính trị/Nhà nước`) — hợp lệ, lint cho phép 1–2.

### Phát hiện

**[BẮT BUỘC] 05-1 — Mục tuyên bố đã tách nguồn đương thời khỏi lớp đánh giá đời sau, nhưng trường `Nguồn` không có một nguồn đương thời nào.**

Nguyên văn câu sai:
> Hình ảnh tàn bạo gắn với bà phần lớn do sử gia Nho giáo đời sau xây, nên mục này tách nguồn đương thời khỏi lớp đánh giá về sau.

Nguyên văn trường `Nguồn`:
> Lưu Hú và nhóm biên soạn, Cựu Đường thư (945); R.W.L. Guisso, Wu Tse-T'ien and the Politics of Legitimation in T'ang China (Western Washington University, 1978).

Hai nguồn, không nguồn nào đương thời: *Cựu Đường thư* soạn năm **945**, tức 240 năm sau khi bà mất và
dưới một triều khác (Hậu Tấn) — nó **chính là** lớp sử học đời sau mà câu nói nó đang tách ra; Guisso là
chuyên khảo năm 1978. Mục vì vậy hứa một thao tác phương pháp mà danh mục nguồn của nó không thực hiện được.
Đây không phải chuyện nguồn sai — cả hai đều tồn tại và đúng chủ đề — mà là **mệnh đề về phương pháp
không có gì đỡ**, đúng loại lỗi quy tắc 7 nhắm tới: phải biết nguồn **là gì**, không chỉ nó nói về ai.

Câu thay thế đề xuất, nguyên văn:
> Hình ảnh tàn bạo gắn với bà phần lớn do sử gia Nho giáo đời sau xây, nên mục này chỉ lấy ở chính sử phần sự kiện có mốc, và để phần đánh giá cho chuyên khảo hiện đại.

Soi lại chính câu thay thế: (a) Nó mô tả đúng cái mục **thật sự làm được** với hai nguồn đang có — lấy mốc
sự kiện ở *Cựu Đường thư*, lấy khung diễn giải ở Guisso — thay vì hứa một việc cần nguồn thứ ba.
(b) Nó **không** khẳng định *Cựu Đường thư* trung lập về sự kiện; chỉ nói mục dùng nó ở tầng nào.
(c) `[KHÔNG KIỂM ĐƯỢC]` — tôi **không** kiểm được mệnh đề "phần lớn do sử gia Nho giáo đời sau xây" tới
một khảo luận sử học cụ thể; nó được giữ nguyên từ bản gốc, không phải tôi thêm vào. Nếu muốn câu không
mang mệnh đề chưa truy nguồn nào, cắt vế đầu: "Mục này chỉ lấy ở chính sử phần sự kiện có mốc, và để phần
đánh giá cho chuyên khảo hiện đại." — câu vẫn đứng được và vẫn làm đúng việc rào.
Đếm: `why` từ 84 lên **90** (bản đầy đủ) hoặc **75** (bản cắt). Cả hai trong khoảng hợp lệ của trần 104
và không rơi dưới ngưỡng cảnh báo lệch 30% (56 chữ).

**[NÊN] 05-2 — Mệnh đề "làm suy yếu các dòng họ quý tộc tây bắc" được phát biểu như kết quả đã chốt.**

Nguyên văn:
> Bà mở rộng khoa cử và lấy người từ tầng lớp thấp hơn, làm suy yếu các dòng họ quý tộc tây bắc.

Đây là một mệnh đề **nhân quả về cấu trúc xã hội**, không phải một sự kiện có mốc, và nó là mệnh đề duy
nhất trong mục đỡ cho vế "counterfactual (d)" ở `Vì sao chọn`. Nó cũng là mệnh đề bị tranh luận nhiều nhất
trong sử học Đường hiện đại. Ngoài ra nó va với `CH05-CE07-04` — xem phát hiện 04-2: hai mục trong cùng
nhóm cùng nhận công "mở rộng khoa cử", không mục nào nhắc mục kia.

Câu thay thế đề xuất, nguyên văn:
> Bà đẩy mạnh khoa cử và lấy người từ tầng lớp thấp hơn, điều mà sử học hiện đại đọc là một đòn vào thế của các dòng họ quý tộc tây bắc.

Soi lại chính câu thay thế: (a) Nó **quy mệnh đề nhân quả cho người đọc nó** ("sử học hiện đại đọc là")
thay vì phát biểu như sự kiện — đúng cách mà mục `CH05-CE07-11` cùng nhóm xử lý Thönmi Sambhoṭa.
(b) `[KHÔNG KIỂM ĐƯỢC]` — vòng này **không** xác định được mức độ đồng thuận của "sử học hiện đại" về
mệnh đề này, chỉ xác định được rằng nó không phải một kết quả đo đếm. Nếu không muốn mang theo một mệnh đề
về trạng thái học giới, cắt vế sau: "Bà đẩy mạnh khoa cử và lấy người từ tầng lớp thấp hơn." — câu vẫn
đứng được, và khi ấy lập luận (d) ở `Vì sao chọn` phải chuyển sang dựa hẳn vào vế chính danh Phật giáo,
vốn là vế mục có nguồn chuyên khảo đỡ (Guisso).
Đếm: câu cũ 17 chữ, câu mới 25 chữ → `ideas` từ 122 lên **130, đúng bằng trần**. Bản cắt: **115**.

**[CÂN NHẮC] 05-3 — Một lĩnh vực có nội dung đỡ nhưng không được khai.**

Gần một phần ba trường `ideas` nói về **chính danh Phật giáo** (bản sớ Đại Vân kinh) và **bảo trợ tạc tượng
Long Môn**, nhưng `lĩnh vực:` chỉ khai `Chính trị/Nhà nước`. Lint không báo gì (1 ≤ 2). Ngược lại với ca
`CH05-CE07-02`, nơi một nhãn **không** có nội dung đỡ — ở đây là nội dung **có** mà nhãn thiếu. Hai ca cộng
lại cho thấy thống kê lĩnh vực của nhóm đang lệch theo cả hai chiều.

Đề xuất, nguyên văn: `lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh`

Soi lại chính đề xuất: (a) `Tôn giáo/Tâm linh` nằm trong `FIELDS` của `atlaslib/common.py`, tổng 2 ≤ 2,
nên lint nhận. (b) Tôi **cố ý không đề xuất `Nghệ thuật/Kiến trúc`**, dù vế Long Môn có vẻ đỡ được:
`CH05-CE07-12` trong cùng nhóm đã giữ ô ấy và vai trò của bà ở Long Môn là **bảo trợ**, không phải tạo tác —
đổi nhãn vì nó làm đẹp một ô thống kê là đúng cái việc mà `CONTRIBUTING.md` quy ước `vùng:` mục 4 cấm,
và nguyên tắc ấy không có lý do gì chỉ áp cho `vùng:`.

---
## `CH05-CE07-06` · Huyền Trang — dòng 294–310

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q42063` → nhãn en `Xuanzang`, vi `Huyền Trang`, `P31 = Q5`. Đúng người.
- "về năm 645 với **657 bộ kinh**" — con số 657 kiểm được và khớp.
- "riêng Nālandā chừng **năm năm**" — đúng theo đính chính ở khối 20; con số "hơn mười năm" được giữ đúng
  chỗ của nó, là **tổng thời gian ở Ấn Độ**. Hai con số không còn lẫn nhau như bản thảo đầu.
- **Chỗ mục làm tốt hơn cả nguồn phổ thông, ghi nhận riêng.** Về chiếu chỉ cấm xuất cảnh, mục viết:
  "tiểu sử môn đồ soạn sau khi ông mất nói là trái lệnh cấm, còn chính Tây Vực ký không kể". Nguồn bách khoa
  phổ thông thì khẳng định thẳng rằng ông vi phạm lệnh cấm. Công thức của mục — quy cho nguồn **và** nêu
  chỗ nguồn im lặng — đúng như khối 20 dặn, và **không được rút gọn thành một khẳng định**.
- "Cunningham ở thế kỷ 19 dùng Tây Vực ký song song với ký sự Pháp Hiển để định vị di chỉ" — đúng.
- "Nghĩa Tịnh, người cũng đi Ấn Độ bằng đường biển và để lại ký sự" — `Q457629`, **635–713**. Quy tắc 5:
  chồng lấn thật với Huyền Trang (602–664), 29 năm. Quy tắc 6: **không có mục** ở bất kỳ chapter nào.
  Cả hai cổng đều qua.
- "Pháp Hiển **có mục riêng** ở `CH04-CE04-12` nên không phải ứng viên bị loại" — mở ra đọc:
  `### CH04-CE04-12 · Pháp Hiển (法顯 Fǎxiǎn)`. **Đúng người, đúng ID**, và dùng đúng câu chữ
  `CONTRIBUTING.md:51` yêu cầu. Quy tắc 6 được áp đúng.
- Hai dòng `Kế thừa từ` mở ra đọc tên: `CH04-CE04-11` = **Vasubandhu**, `CH04-CE04-10` = **Asaṅga**.
  Đúng hai người của mạch Du-già hành, đúng mạch mà Huyền Trang mang về và lập thành tông Pháp tướng.
  Mức `qua trường phái` ở cả hai dòng là **đúng, không thổi phồng** (hai bên cách nhau hai thế kỷ, quan hệ
  là văn bản). Đây là hai dòng mẫu mực của cả nhóm về chuyện khai đúng mức bằng chứng.
- `vùng: Đông Á` dù `nơi:` liệt kê ba nơi — **đúng quy ước** `CONTRIBUTING.md` mục `vùng:` điều 1:
  nơi hoạt động chính, không phải nơi đi qua. Toàn bộ sự nghiệp dịch thuật diễn ra ở Trường An.
- Nguồn 1 tồn tại và **đúng thể loại**: Samuel Beal, *Si-Yu-Ki: Buddhist Records of the Western World*, 1884
  — là **bản dịch**, và mục ghi đúng là "bản dịch", không ghi nhầm thành chuyên khảo.
- `ideas` 115 chữ, `why` 78 chữ. Dưới trần.

### Phát hiện

**[NÊN] 06-1 — "Năm 629 ông rời Trung Hoa" được viết như một mốc chắc, trong khi đây là một tranh luận niên đại có tên và có lý do nội tại.**

Nguyên văn câu:
> Năm 629 ông rời Trung Hoa — tiểu sử môn đồ soạn sau khi ông mất nói là trái lệnh cấm, còn chính Tây Vực ký không kể — đi qua Trung Á tới Ấn Độ…

Năm khởi hành được chép theo **hai hệ**: bản 627 có trong *Quảng hoằng minh tập* và trong các văn bản Nhật,
Triều Tiên; bản 629 có trong mạch Trung Hoa và các bản phương Tây. Và mâu thuẫn không phải chuyện chép lệch:
một trong ba bản tiểu sử (của Huệ Lập) kể ông gặp **Yabghu Qaghan**, người theo ghi chép Ba Tư và Thổ đã
chết năm **628** — tức nếu chi tiết ấy đúng thì ông phải đi trước 628. Mục dùng 629 (lựa chọn đa số, hợp lệ)
nhưng viết nó trần trụi, và chính câu ấy lại là câu mục bỏ công rào ở **vế khác** (lệnh cấm). Rào một vế
mà để trần vế kia trong cùng một câu là chỗ dễ sửa.

Câu thay thế đề xuất, nguyên văn:
> Ông rời Trung Hoa năm 629 theo mạch chép Trung Hoa, năm 627 theo mạch Nhật – Triều Tiên — tiểu sử môn đồ soạn sau khi ông mất nói là trái lệnh cấm, còn chính Tây Vực ký không kể — đi qua Trung Á tới Ấn Độ…

Soi lại chính câu thay thế: (a) Cả hai con số và cả hai mạch chép đều **đã kiểm được**, không phải tôi suy ra.
(b) Tôi **cố ý không đưa lập luận Yabghu Qaghan vào mục** — nó cần tới ghi chép Ba Tư/Thổ mà vòng này
`[KHÔNG KIỂM ĐƯỢC]` tới nguồn gốc, và nó sẽ ngốn khoảng 25 chữ. Chỗ của nó là Ghi chú biên tập, không phải mục.
(c) Giữ nguyên công thức rào về lệnh cấm, không rút gọn — đúng như khối 20 dặn.
Đếm: +11 chữ → `ideas` từ 115 lên **126**, vẫn dưới trần 130.

**[NÊN] 06-2 — `độ tin cậy niên đại: Cao` đứng cạnh một năm sinh tự ghi là "khoảng"; chapter này đã có tiền lệ xử đúng ca ấy theo chiều ngược lại.**

Nguyên văn dòng metadata:
> `năm: k. 602–664 CN | … | độ tin cậy niên đại: Cao | …`

`CH05-CE07-06` là **mục duy nhất trong nhóm CE07** để `Cao` mà vẫn mang tiền tố `k.`; ba mục `Cao` còn lại
(`-04` 598–649, `-05` 624–705, `-12` 603–683) đều ghi năm trần. Tiền tố `k.` nói "không chắc", nhãn `Cao`
nói "chắc trong ±5 năm" — hai tín hiệu ngược nhau trên cùng một dòng, và `_APPROX_RE` của
`atlaslib/common.py` có nhận ra `k.` nhưng lint không đối chiếu nó với `CONFIDENCE`, nên không ai báo.

Quan trọng hơn: **chapter này đã phát biểu nguyên tắc cho đúng tình huống đó**, ở khối 11
(`content/ch05.md:1099`), khi quyết không để Boethius ở `Cao`: "mức Cao sẽ là một tuyên bố chắc chắn mà
nguồn không cho phép". Nguyên tắc ấy không có lý do gì chỉ áp cho một mục.

Hai cách sửa, và tôi đề xuất cách (a):

(a) Bỏ tiền tố: `năm: 602–664 CN … độ tin cậy niên đại: Cao`.
(b) Hạ nhãn: `năm: k. 602–664 CN … độ tin cậy niên đại: Trung bình`.

Soi lại chính đề xuất: cách (a) đứng được vì năm sinh 602 được chép tới **từng ngày** (6-4-602) và năm mất
tới 5-2-664, khớp `P569 +0602-04-06/p11` rank `preferred` và `P570 +0664-03-07/p11` của `Q42063`; dung sai
`Cao` là ±5 nên cả hai đầu vẫn sạch sau khi bỏ `k.`. Cách (b) **an toàn hơn về mặt tri thức** nhưng có một
hệ quả tôi phải nói thẳng: hạ xuống `Trung bình` nới dung sai lên ±25, tức **nới lỏng cổng lint** cho một
mục mà niên đại thực ra khá chắc — đó là trả giá sai chiều. Vì vậy tôi đề xuất (a), không đề xuất (b).
`[KHÔNG KIỂM ĐƯỢC]`: tôi không truy được tới nguồn gốc các dị bản 596/600 đôi khi gặp cho năm sinh ông,
nên không khẳng định được rằng 602 là **không** tranh luận — chỉ khẳng định được rằng mục không thể vừa
ghi `k.` vừa ghi `Cao`.

**[CÂN NHẮC] 06-3 — Một dòng `trực tiếp` nối ông với một ngành học ra đời sau ông 1.200 năm.**

Nguyên văn:
> - Khảo cổ học Ấn Độ thế kỷ 19 · kế thừa · trực tiếp

Đích không phải người, và khoảng cách là **khoảng 1.200 năm** — xa hơn cả ca mà Ghi chú biên tập gọi là
"ca xa nhất" của nhóm CE10 (`CH05-CE10-12 · Gerbert` kế thừa Boethius qua 420 năm). Nội dung thì đúng:
Cunningham dùng Tây Vực ký làm bản đồ thực địa. Nhưng mức bằng chứng thì không thể là `trực tiếp` theo bất
kỳ nghĩa người–người nào.

Dòng thay thế đề xuất, nguyên văn:
> - Khảo cổ học Ấn Độ thế kỷ 19 · kế thừa · qua trường phái

Soi lại chính dòng thay thế: `qua trường phái` nằm trong `EVIDENCE_LEVELS` nên lint nhận; và nó mô tả đúng
quan hệ thật (một ngành học thế kỷ 19 dùng một văn bản thế kỷ 7 làm nguồn). Tôi **không** đề xuất
`suy đoán học giả` vì việc Cunningham dùng Tây Vực ký không phải suy đoán — nó được chính ông ghi.
Lưu ý thủ tục: đây là một trong 19 dòng cùng họ của nhóm, và ghi chú chapter đã kết luận đúng rằng phải xử
ở tầng `CONTRIBUTING.md`. Tôi nêu riêng dòng này vì khoảng cách của nó là cực trị, không phải để vá lẻ.

---
## `CH05-CE07-07` · Huệ Năng — dòng 311–326

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q345012` → nhãn en `Huineng`, vi `Huệ Năng`, `P31 = Q5`. Đúng người.
- `638–713 CN`, `Trung bình`. Wikidata `P569 +0638/p9`, `P570 +0713/p9`. Khớp. Và nhãn `Trung bình`
  ở đây là **lựa chọn đúng**, không phải lựa chọn an toàn: nền sử học hiện đại gọi ông là một nhân vật
  "bán truyền thuyết" và coi hai con số ấy là niên đại truyền thống. So với `CH05-CE07-06` (xem 06-2),
  mục này khai đúng mức không chắc chắn của mình.
- "nghe một câu Kinh Kim Cương mà ngộ" — đúng theo tường thuật của Đàn kinh, và mục đã rào bằng "kể ông là".
- **Cách rào vế Thần Tú là đúng và không được làm chặt thêm.** Mục viết: lập trường đốn ngộ "được dựng thành
  thế đối lập với 'tiệm tu' **gán cho** Thần Tú". Hai chữ "gán cho" là chỗ quan trọng: chính McRae — nguồn 2
  của mục — lập luận rằng bài kệ gán cho Thần Tú **không** nói về tu tiệm tiến, và cách đọc đối lập
  đốn/tiệm là một **phóng đại luận chiến** đời sau. Mục rào đúng chỗ ấy. **Không đề nghị sửa.**
- "phần lớn tường thuật về ông do Thần Hội dựng ở thế kỷ 8 để tranh chính thống — luận điểm Hồ Thích nêu,
  mà McRae tuy nhận phần sử liệu vẫn phản đối cách Hồ Thích quy giản Thiền tông thành chuyện tranh quyền"
  — kiểm được cả ba vế, và khớp đúng cảnh báo quy tắc 7 mà khối 21 đặt ra cho McRae. Đây là ca **dùng nguồn
  đúng chiều**: McRae không bị dẫn như người đồng tình với Hồ Thích.
- Quy tắc 5 và 6 cho cả hai ứng viên: **Thần Tú** `Q704016` **606–706**, **Thần Hội** **684–758**.
  Chồng lấn với Huệ Năng (638–713) là 68 năm và 29 năm — cùng thời thật. Không ai có mục ở bất kỳ chapter nào.
- `Kế thừa từ CH05-CE06-08`: mở ra đọc, đúng là **Bồ-đề-đạt-ma**, và mức `qua trường phái` là đúng —
  hai người cách nhau hơn một thế kỷ, quan hệ là phả hệ truyền thừa chứ không phải tiếp xúc. Dòng này
  **không** mắc lỗi thổi phồng mà `CH05-CE07-10` mắc.
- Nguồn 1: Philip B. Yampolsky, *The Platform Sutra of the Sixth Patriarch*, Columbia University Press, 1967
  — tồn tại, đúng tác giả, đúng nhà xuất bản, đúng năm; và mục ghi đúng rằng đây là **bản Đôn Hoàng**,
  tức bản cổ nhất, chứ không phải bản thông hành đời sau.
- Nguồn 2: John McRae, *Seeing Through Zen*, University of California Press, 2003 — tồn tại, đúng cả ba.
- `ideas` 91 chữ (dưới ~100 nhưng lệch 9%, không chạm ngưỡng cảnh báo 30%), `why` 99 chữ (≤ 104).

### Phát hiện

**[NÊN] 07-1 — Mệnh đề "bộ duy nhất" đúng trong một phạm vi, nhưng mục đã bỏ mất phạm vi ấy.**

Nguyên văn câu sai:
> Pháp bảo đàn kinh — bộ duy nhất do người Trung Hoa soạn mà được gọi là "kinh" — kể ông là một người đốn củi mù chữ…

Không có ngữ cảnh giới hạn, câu này sai. **Nhiều** văn bản soạn ở Đông Á mang chữ 經 trong nhan đề:
*Viên Giác kinh* (圓覺經) được soạn ở Trung Hoa; *Phạm Võng kinh* (梵網經) được giới nghiên cứu xếp là soạn
ở Đông Á giữa thế kỷ 5 chứ không phải bản dịch của Cưu-ma-la-thập như truyền thống ghi; và cả một lớp
"nguỵ kinh" (Buddhist apocrypha) nữa. Dạng đúng của mệnh đề là có **giới hạn trong Thiền tông**: trong
Thiền tông, đây là văn bản Trung Hoa duy nhất được gọi thẳng là "kinh". Lỗi ở đây là lỗi **mất điều kiện**,
cùng họ với ca Hansen ở quy tắc 7 — một mệnh đề đúng trong khung hẹp bị trích ra khỏi khung.

Câu thay thế đề xuất, nguyên văn:
> Pháp bảo đàn kinh — trong Thiền tông là văn bản Trung Hoa duy nhất được gọi thẳng là "kinh" — kể ông là một người đốn củi mù chữ…

Soi lại chính câu thay thế: (a) Giới hạn "trong Thiền tông" là **chính giới hạn** mà các mô tả quy chuẩn
dùng, không phải giới hạn tôi tự đặt thêm cho an toàn. (b) Tôi **không** viết "bộ kinh duy nhất không do
người Ấn soạn" — đó sẽ là đúng cái lỗi vừa chẩn, vì lớp nguỵ kinh Đông Á phá nó ngay.
(c) `[KHÔNG KIỂM ĐƯỢC]` — vòng này **không** mở được tới phần dẫn nhập của Yampolsky 1967 để xem ông phát
biểu mệnh đề ấy với giới hạn nào; nếu bản in của ông cũng viết không giới hạn thì mục nên nói rõ "theo
Yampolsky". Nếu không muốn mang bất kỳ mệnh đề so sánh nào, cắt hẳn cụm trong gạch ngang — câu vẫn đứng
được và không mất gì về nội dung của chính Huệ Năng.
Đếm: +2 chữ → `ideas` từ 91 lên **93**; bản cắt hẳn còn **80 chữ**, lệch 20% so với ~100, vẫn dưới ngưỡng
cảnh báo 30% của lint.

**[CÂN NHẮC] 07-2 — Người truyền y bát không được nêu tên, nên mệnh đề trung tâm của tường thuật treo lơ lửng.**

Nguyên văn:
> rồi được truyền y bát vượt qua các học trò có học

Người truyền là **Hoằng Nhẫn**, tổ thứ năm, và việc ông chọn Huệ Năng thay vì Thần Tú chính là biến cố mà
cả `ideas` lẫn `why` xoay quanh. Mục nêu tên Thần Tú (ở `why`) nhưng không nêu tên người quyết định.
Hoằng Nhẫn không có mục trong atlas nên không vướng quy tắc 6, và đích tự do là hợp lệ theo §5.

Câu thay thế đề xuất, nguyên văn:
> rồi được tổ thứ năm Hoằng Nhẫn truyền y bát vượt qua các học trò có học

Soi lại chính câu thay thế: (a) Mệnh đề này nằm **trong cùng tường thuật** mà câu đang thuật lại, và câu đã
mở bằng "kể ông là", nên nó vẫn được rào bởi cùng một mệnh đề dẫn — tôi **không** biến tường thuật thành
khẳng định lịch sử. Đây là chỗ dễ trượt nhất và tôi cố ý không trượt: nền sử học hiện đại coi chính việc
truyền thừa này là thứ do Thần Hội dựng, và `why` của mục đã nói đúng như vậy.
(b) Đếm: +4 chữ → `ideas` **95** (hoặc **97** nếu áp cùng 07-1). Dưới trần 130.

**[CÂN NHẮC] 07-3 — Hai dòng `Ảnh hưởng tới` cùng trỏ về một mạch, nên mục dùng hết suất mà không mở ra chiều nào mới.**

Nguyên văn:
> - Thiền tông Nam phái và các dòng Lâm Tế, Tào Động · kế thừa · trực tiếp
> - Zen Nhật Bản và Thiền Việt Nam · kế thừa · qua trường phái

Hai dòng là cùng một cây phả hệ ở hai độ xa khác nhau, và dòng đầu khai `trực tiếp` cho hai dòng phái ra
đời ở thế kỷ 9 — tức sau ông gần hai thế kỷ. Mục còn **một suất trống** (§5 cho tối đa 3).
Ghi lại cho P4: `CH05-CE08-xx` và các chapter sau chưa có mục Thiền tông nào để nâng đích tự do này lên ID,
nên **vòng này không đề xuất thay bằng ID** — khác với ca `CH05-CE07-03` ở trên, nơi đích đã có người thật.
Đề xuất duy nhất ở đây là hạ mức dòng đầu xuống `qua trường phái`, cùng lý do với 06-3.

---
## `CH05-CE07-08` · Brahmagupta — dòng 327–343

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q202943` → nhãn en/vi `Brahmagupta`, `P31 = Q5`. Đúng người.
- `k. 598 – k. 668 CN`, `Trung bình` (±25). Wikidata `P569 +0598/p9`; `P570` rank `preferred` `+0670/p9`
  và một giá trị `normal` `+0665/p9`. Cả hai nằm trong dung sai. Và 598 là con số **chính ông khai**
  trong văn bản, nên đầu sinh vững hơn đa số ca cùng thời.
- "Brāhmasphuṭasiddhānta, soạn năm **628**" — đúng, và đúng là năm ông 30 tuổi theo chính lời ông.
- "quy tắc dấu cho số âm, diễn giải chúng là 'nợ'" — đúng.
- "công thức diện tích tứ giác nội tiếp mang tên ông" — đúng (công thức Brahmagupta).
- "**ông cho rằng không chia cho không bằng không**" — đúng, và đây là chỗ dễ chép sai nhất trong cả mục.
  Văn bản BSS 18.34 ghi đúng rằng **không chia cho không bằng không**; câu kế (18.35) thì để ngỏ trường hợp
  một số dương hay âm chia cho không. Mục nêu đúng mệnh đề 18.34 và **không** gán nhầm cho ông mệnh đề 18.35.
- "Chuyện bộ này tới Baghdad năm 772/773 chỉ được chép rất muộn, qua Ibn al-Adamī rồi al-Qifṭī, nên đọc như
  giai thoại" — rào đúng theo khối 20, và đúng chuỗi truyền.
- `Kế thừa từ CH05-CE06-04`: mở ra đọc, đúng là **Varāhamihira**, và nhãn `kế thừa` là **đúng chứ không phải
  gượng** — hồ sơ ghi Brahmagupta đã nghiên cứu công trình của Varāhamihira cùng với Āryabhaṭa I, Lāṭadeva,
  Pradyumna, Siṃha, Śrīṣeṇa, Vijayanandin, Viṣṇucandra. Mức `qua trường phái` cũng đúng (hai người cách nhau
  một thế hệ, không tiếp xúc).
- `Ảnh hưởng tới CH05-CE09-04`: mở ra đọc, đúng là **Al-Khwarizmi**, đúng người mà một dòng về đường truyền
  siddhānta sang toán học Ả Rập phải trỏ tới. Mức `qua trường phái` là **đúng, không thổi phồng**.
- "Āryabhaṭa **có mục riêng** ở `CH04-CE05-09` nên không phải ứng viên bị loại — và chính Brahmagupta công
  kích ông, nên quan hệ giữa hai mục là phản bác" — mở ra đọc: `### CH04-CE05-09 · Āryabhaṭa (आर्यभट)`.
  **Đúng người, đúng ID, đúng câu chữ quy tắc 6**, và phần giải thích thêm ("chính Brahmagupta công kích ông")
  làm rõ vì sao nhãn quan hệ là `phản bác` chứ không phải `kế thừa` — đây là cách áp quy tắc 6 tốt nhất
  trong cả nhóm, vì nó không chỉ khai mà còn nối.
- Quy tắc 5 và 6 cho **Bhāskara I**: ông chú giải *Āryabhaṭīya* năm **629**, tức đúng một năm sau BSS —
  cùng thời thật, không phải ca lệch thế kỷ. Và ông **không có mục** ở bất kỳ chapter nào.
- Nguồn 1 tồn tại và đúng: Kim Plofker, *Mathematics in India*, Princeton University Press, 2009.
- Nguồn 2 **ghi đúng thể loại và không bịa số chương**: "Brahmagupta, Brāhmasphuṭasiddhānta, **các chương
  toán học** trong bản dịch H.T. Colebrooke (1817)". Colebrooke 1817 đúng là một **bản dịch** (không phải
  chuyên khảo — không mắc lỗi Fried & Unguru), và việc viết "các chương toán học" thay vì ghi số chương
  là đúng chỉ dẫn `CONTRIBUTING.md:48`. Ghi nhận riêng: đây là cách xử đúng.
- `ideas` 118 chữ, `why` 78 chữ. Dưới trần.

### Phát hiện

**[NÊN] 08-1 — `Vì sao chọn` dựng lập luận trên một mắt xích mà chính `Tư tưởng` của nó vừa hạ xuống hàng giai thoại.**

Nguyên văn hai chỗ đá nhau, cách nhau ba dòng:
> Chuyện bộ này tới Baghdad năm 772/773 chỉ được chép rất muộn, qua Ibn al-Adamī rồi al-Qifṭī, nên đọc như giai thoại; chắc hơn là văn bản của ông có mặt trong mạch toán học Ả Rập.

> Brahmagupta được chọn theo phạm vi (a): bộ của ông là văn bản Ấn Độ thật sự được dịch sang tiếng Ả Rập, nên đây là mắt xích có chứng cứ chứ không phải mắt xích giả định.

Trường `ideas` hạ mệnh đề truyền bá xuống mức "giai thoại" và chỉ giữ lại dạng yếu ("có mặt trong mạch").
Rồi `why` nâng nó lên thành "**thật sự được dịch**" và "**mắt xích có chứng cứ**", tức đúng mức mà câu trước
vừa bác. Vì toàn bộ lập luận chọn người của mục đứng trên mệnh đề này, chỗ vênh không phải tiểu tiết.

Câu thay thế đề xuất, nguyên văn:
> Brahmagupta được chọn theo phạm vi (a): trong các tác giả siddhānta, ông là người mà dấu vết trong mạch toán học Ả Rập đời sau rõ nhất, nên đây là mắt xích đọc được chứ không phải mắt xích giả định.

Soi lại chính câu thay thế: (a) Nó dùng **đúng dạng yếu** mà `ideas` đã chốt ("có mặt trong mạch"), nên
hai trường thôi đá nhau. (b) Tôi **bỏ chữ "thật sự được dịch"** — đó là mệnh đề mà `[KHÔNG KIỂM ĐƯỢC]`:
vòng này không truy được tới một chứng cứ đương thời cho bản dịch Ả Rập của BSS; mọi đường đều quay về
đúng chuỗi al-Qifṭī mà mục đã gọi là giai thoại. (c) Cụm "rõ nhất" là một so sánh — nhưng nó được giới hạn
trong một tập hợp hẹp và xác định ("các tác giả siddhānta"), khác với ca 03-3 nơi "rõ nhất" trùm cả một
ngành học. Nếu vẫn muốn bỏ mọi so sánh, cắt thành: "ông là người có dấu vết trong mạch toán học Ả Rập đời sau"
— câu vẫn đứng được. Đếm: `why` từ 78 lên **84** (hoặc **80** bản cắt), dưới trần 104.

**[NÊN] 08-2 — Mục khai `Khoa học tự nhiên` và câu hỏi lớn `Vũ trụ`, nhưng không có một chữ nào về thiên văn.**

Nguyên văn dòng metadata:
> `… | lĩnh vực: Toán học, Khoa học tự nhiên | … | câu hỏi lớn: Vũ trụ`

Đọc hết 118 chữ `ideas`: số không, quy tắc dấu số âm, công thức tứ giác nội tiếp, phép chia cho không,
đường truyền sang Baghdad. **Không một mệnh đề nào về thiên văn.** Nhưng Brāhmasphuṭasiddhānta là một
**chuyên luận thiên văn**, trong đó các chương toán là một phần; ông thuộc trường phái Brāhmapakṣa và về
sau soạn *Khaṇḍakhādyaka* (665), một sổ tay thiên văn thực hành. Cả nhãn `Khoa học tự nhiên` lẫn câu hỏi lớn
`Vũ trụ` **chỉ có nghĩa qua vế thiên văn**, mà vế ấy vắng mặt. Đây là ca ngược với `CH05-CE07-02`
(nhãn không có nội dung đỡ) và giống ca `CH05-CE07-05` (nội dung có mà nhãn thiếu) — lần này là nhãn có
mà nội dung thiếu. So sánh với `CH05-CE06-04` Varāhamihira trong cùng chapter, vốn khai cùng bộ nhãn
`Toán học, Khoa học tự nhiên | Vũ trụ` và **có** nội dung thiên văn đỡ, thì chỗ hổng của mục này hiện rõ.

Câu thay thế đề xuất, nguyên văn — thay cụm mở đầu:
> Brāhmasphuṭasiddhānta, soạn năm 628, cho tới nay vẫn được coi là văn bản sớm nhất còn lại xử lý số không như một số có quy tắc tính chứ không chỉ là ký hiệu đánh dấu chỗ trống:

bằng:
> Brāhmasphuṭasiddhānta, chuyên luận thiên văn ông soạn năm 628, cho tới nay vẫn được coi là văn bản sớm nhất còn lại xử lý số không như một số có quy tắc tính chứ không chỉ là ký hiệu đánh dấu chỗ trống;

Soi lại chính câu thay thế: (a) "chuyên luận thiên văn" là mệnh đề đã kiểm, và nó **làm mệnh đề về số không
mạnh lên** chứ không yếu đi — số không xuất hiện trong các chương toán của một bộ thiên văn, đúng như
Colebrooke dịch. (b) Tôi **cố ý không thêm *Khaṇḍakhādyaka* (665)**: thêm nó sẽ tốn ~8 chữ và kéo theo một
mốc năm nữa phải rào, mà vế thiên văn đã đủ đỡ cho nhãn chỉ với bốn chữ. (c) Đã sửa luôn dấu hai chấm
thành chấm phẩy — xem 08-3. Đếm: +4 chữ → `ideas` **122**, dưới trần 130.

**[CÂN NHẮC] 08-3 — Lỗi dấu câu làm gãy một câu dài.**

Nguyên văn:
> …chứ không chỉ là ký hiệu đánh dấu chỗ trống: Ông cũng nêu quy tắc dấu cho số âm…

Dấu hai chấm đứng trước một câu mới viết hoa ("Ông"). Hoặc là dấu chấm, hoặc là chấm phẩy, không phải hai chấm.
Đây là lỗi duy nhất thuộc loại này tôi tìm thấy trong 203 dòng của nhóm; ghi vì nó nằm đúng ở câu mang
mệnh đề nổi bật nhất của mục. Sửa gộp vào câu thay thế của 08-2 ở trên (đổi `:` thành `;`).

---
## `CH05-CE07-09` · Isiđôrô thành Seville — dòng 344–360

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q166876` → nhãn en `Isidore of Seville`, vi `Isiđôrô`, `P31 = Q5`. Đúng người.
- `k. 560–636 CN`, `Trung bình`. Wikidata `P569 +0560/p9`, `P570` rank `preferred` `+0636-04-04/p11`. Khớp.
- "**việc chia thành hai mươi quyển là do Braulio … làm sau**" — kiểm được và **đúng**: Braulio, người Isiđôrô
  đề tặng và gửi bản cho hiệu đính, là người chia bộ thành hai mươi quyển. Đây là một đính chính thật
  so với cách kể phổ thông, và mục giữ đúng.
- "**Gần một nghìn bản chép tay còn lại**" — kiểm được: mô tả quy chuẩn nói số bản chép tay còn lại là
  "trên dưới một nghìn". Con số của mục nằm đúng trong khoảng ấy. (Xem 09-3 về chuyện ghi chú chapter
  lại dặn **không** viết con số này vào mục.)
- "Truyền thống bách khoa Latin từ **Pliny Cả**" — kiểm được và đúng: ba quyển của bộ lấy phần lớn từ
  *Naturalis Historia*, và Isiđôrô **có** ghi nhận Pliny (trong khi ông không ghi nhận phần lớn nguồn khác).
  Đây là một trong những dòng `Kế thừa từ` dạng tự do có nền vững nhất của nhóm.
- "Phương pháp đó sai" — đúng, và việc mục nói thẳng điều đó thay vì khen là đúng tinh thần `README.md`.
- Nguồn 1 tồn tại và **đúng thể loại**: Stephen A. Barney, W.J. Lewis, J.A. Beach, Oliver Berghof,
  *The Etymologies of Isidore of Seville*, Cambridge University Press (các lần in 2002 / 2006 / 2010;
  mục ghi 2006, nằm trong khoảng). Là **bản dịch**, và mục ghi đúng là "bản dịch".
- Nguồn 2 tồn tại và đúng cả ba: Jacques Fontaine, *Isidore de Séville*, Brepols, **2000**.
  (Fontaine còn một chuyên khảo 1959 về cùng chủ đề; mục dẫn đúng cuốn 2000, không lẫn.)
- `Kế thừa từ CH04-CE05-01`: mở ra đọc, đúng là **Augustinô thành Hippo** — không phải ca trỏ sai người.
- `ideas` 123 chữ, `why` 78 chữ. Dưới trần.

### Phát hiện

**[BẮT BUỘC] 09-1 — Mục viện một tiền lệ của chính atlas, và một nửa tiền lệ ấy không đúng như mục mô tả.**

Nguyên văn câu sai:
> Isiđôrô được chọn theo tính nguyên bản (c) hiểu theo nghĩa tư liệu — cùng tiêu chuẩn atlas đã dùng cho Pappus và Wulfila: nhiều đoạn của tác giả cổ điển ngày nay còn lại chỉ vì ông chép.

Tôi mở cả hai mục đích ra đọc:

- `CH04-CE04-03 · Wulfila` — `Vì sao chọn` ghi: "Wulfila được chọn theo **tính nguyên bản (c) và phạm vi (a)
  của tư liệu**". **Khớp.**
- `CH04-CE04-06 · Pappus xứ Alexandria` — `Vì sao chọn` ghi: "Pappus được chọn theo **counterfactual (d)**:
  bài toán quỹ tích của ông là chỗ cụ thể mà Descartes dùng để chứng minh rằng cần một phương pháp mới".
  **Không khớp.** Mục Pappus không viện (c), và lý do nó đưa ra không phải lý do tư liệu mà là một mắt xích
  nhân quả cụ thể tới Descartes.

Đây đúng loại lỗi mà `CONTRIBUTING.md` quy tắc 8 mô tả ở tầng liên kết, nhưng ở tầng **viện dẫn tiền lệ**:
cái tên tồn tại, mục tồn tại, mà nội dung ở đầu kia không nói điều đang được dẫn. Lint hoàn toàn mù —
đây thậm chí không phải một dòng quan hệ nên cả `lint.py:151-152` lẫn vòng đối xứng đều không chạm tới.

Cần ghi thêm một việc **ngoài phạm vi nhóm CE07**: `CH05-CE06-04 · Varāhamihira` trong cùng chapter mắc
**đúng cùng một lỗi**, nguyên văn "Đây đúng là tiêu chuẩn atlas đã dùng cho Pappus và Wulfila". Tức đây là
một công thức đang lan, không phải một ca lẻ. Vòng sau nên `grep` cụm "Pappus và Wulfila" trên toàn kho.

Câu thay thế đề xuất, nguyên văn:
> Isiđôrô được chọn theo tính nguyên bản (c) hiểu theo nghĩa tư liệu — cùng tiêu chuẩn atlas đã dùng cho Wulfila: nhiều đoạn của tác giả cổ điển ngày nay còn lại chỉ vì ông chép.

Soi lại chính câu thay thế: tôi **không** thay Pappus bằng một cái tên khác, vì làm vậy sẽ là đoán — cách
duy nhất an toàn là **bỏ cái tên không khớp** và giữ cái tên đã mở ra đọc và xác nhận khớp. Mệnh đề
"nhiều đoạn của tác giả cổ điển ngày nay còn lại chỉ vì ông chép" giữ nguyên từ bản gốc, và nó có nền:
hồ sơ ghi rằng bộ của ông được đọc thay cho chính các bản cổ điển mà nó tóm tắt, khiến một số bản ấy
thôi được chép và mất hẳn. Đếm: −1 chữ → `why` **77 chữ**, vẫn trong khoảng hợp lệ.

**[NÊN] 09-2 — Ứng viên được nêu thuộc về nhóm thế kỷ 6, và chapter này đã xử ông ở đúng nhóm ấy rồi.**

Nguyên văn câu sai:
> Ứng viên cùng thời là Gregorius thành Tours, người viết sử người Frank.

Gregory xứ Tours là `Q67841`, **538 – 17-12-594**. Hai điều:

(1) **Ông chết năm 594, tức ngoài khoảng nhóm.** `group_range('CE07')` của `atlaslib/common.py` trả về
(601, 700); `group_range('CE06')` trả về (501, 600). Theo quy tắc 3 của `prompts/atlas-prompt.md` —
xếp theo giai đoạn ảnh hưởng chính — toàn bộ sự nghiệp của ông (giám mục Tours từ 573, *Historia Francorum*
soạn tới 594) nằm trong nhóm **CE06**. Về tuổi thọ thì ông và Isiđôrô có chồng lấn 34 năm, nên mục **không**
vi phạm chữ của quy tắc 5; nhưng ông không phải ứng viên tranh suất ở nhóm này.

(2) **Chapter này đã chấm ông ở nhóm CE06 và đã công bố kết quả.** Khối 10 của Ghi chú biên tập
(`content/ch05.md:1095`) ghi: Boethius được 18 điểm, "hơn người hạng hai, **Gregory xứ Tours**, hai điểm",
ở vòng chọn suất thứ mười hai của nhóm **CE06**. Nêu lại ông làm ứng viên bị loại ở CE07 nghĩa là cùng một
người bị loại hai lần ở hai nhóm khác nhau vì hai lý do khác nhau, mà không mục nào biết mục kia.

Câu thay thế đề xuất, nguyên văn:
> Ứng viên cùng ô là Ildefonsus thành Toledo, người kế tục công việc của ông ở Tây Ban Nha Visigoth; Gregorius thành Tours thì đã được chấm ở nhóm CE06 nên không phải ứng viên bị loại của nhóm này.

Soi lại chính câu thay thế — **đây là chỗ tôi phải tự khai rõ nhất**: (a) Vế thứ hai (Gregorius) hoàn toàn
kiểm được: niên đại 538–594 lấy từ Wikidata, và việc ông được chấm ở CE06 lấy từ chính Ghi chú biên tập
của chapter. Vế ấy cũng dùng đúng dạng câu `CONTRIBUTING.md:51`. (b) Vế thứ nhất `[KHÔNG KIỂM ĐƯỢC]` —
tôi **không** tra Q-ID, niên đại hay tác phẩm của Ildefonsus thành Toledo trong vòng này, và
`CONTRIBUTING.md` quy tắc 1 cấm viết một cái tên vào atlas mà chưa tra Wikidata. **Đừng dùng vế đó như đang
viết.** Phương án đứng được ngay mà không cần kiểm thêm là **bỏ hẳn vế một**:
> Gregorius thành Tours đã được chấm ở nhóm CE06 nên không phải ứng viên bị loại của nhóm này; mục này không nêu được ứng viên cùng ô nào khác trong thế kỷ 7.

Dạng ấy hợp lệ theo quy tắc 5 ("nếu giai đoạn đó thật sự không có ai để so, viết thẳng là không có"), và
atlas đã có tiền lệ dùng đúng công thức ấy ở `CH04-CE04-03 · Wulfila` ("Không nêu được ứng viên cùng thời").
Đếm: `why` từ 78 → **86** (bản bỏ vế một) hoặc **96** (bản đầy đủ). Cả hai dưới trần 104; cộng với 09-1 (−1)
thì còn **85** / **95**.

**[NÊN] 09-3 — Mục mô tả cách tổ chức của bộ sách không đúng cách nó được tổ chức.**

Nguyên văn câu sai:
> Etymologiae gom những gì ông còn với tới được của học thuật cổ điển thành **một bộ sắp xếp theo lối truy nguyên từ**

Bộ **không** được sắp xếp theo truy nguyên từ. Nó được sắp theo **chủ đề** — và chính mục nói đúng điều đó
ở câu sau ("bao trùm ngữ pháp, y học, luật, địa lý và nông nghiệp"). Truy nguyên từ là **phương pháp** áp
vào bên trong các mục, và nó là **chủ đề riêng của đúng một quyển trong hai mươi** (quyển X), dù lối liên hệ
theo âm gần thì thấm khắp bộ. Câu hiện tại vì vậy mô tả sai cấu trúc, và lại làm yếu chính luận điểm kế
tiếp của mục: cái khiến bộ này thành "chỗ gần nhất với một thư viện" là **độ phủ chủ đề**, không phải lối
truy nguyên.

Câu thay thế đề xuất, nguyên văn:
> Etymologiae gom những gì ông còn với tới được của học thuật cổ điển thành một bộ sắp theo chủ đề, mà lối giải thích xuyên suốt là truy nguyên từ

Soi lại chính câu thay thế: cả hai vế đều đã kiểm — sắp theo chủ đề, và truy nguyên là lối giải thích
thấm khắp bộ. Tôi **cố ý không viết "chỉ một trong hai mươi quyển bàn về từ nguyên"**: con số ấy đúng
nhưng sẽ mâu thuẫn với câu kế tiếp của mục ("ông tin rằng biết gốc một từ là biết bản chất của vật"),
vốn mô tả **niềm tin phương pháp luận**, không phải tỉ trọng trang sách. Đếm: +1 chữ → `ideas` **124**,
dưới trần 130.

**[CÂN NHẮC] 09-4 — "Braulio, học trò ông" là một quan hệ hẹp hơn cái mà hồ sơ ghi.**

Nguyên văn:
> việc chia thành hai mươi quyển là do Braulio, **học trò ông**, làm sau

Braulio (`Q849117`, **590–651**) là giám mục Zaragoza, người Isiđôrô đề tặng bộ sách và gửi bản cho hiệu đính;
mô tả quy chuẩn gọi ông là **bạn** và người trao đổi thư từ. Cách gọi "học trò" xuất hiện trong một mạch
mô tả nhưng không phải cách gọi chiếm ưu thế. `[KHÔNG KIỂM ĐƯỢC]` — vòng này **không** mở được tới tập thư
từ Braulio–Isiđôrô để xác định quan hệ ấy được hai người tự mô tả thế nào.

Câu thay thế đề xuất, nguyên văn:
> việc chia thành hai mươi quyển là do Braulio, giám mục Zaragoza, người ông gửi bản cho hiệu đính, làm sau

Soi lại chính câu thay thế: cả chức vị lẫn vai trò hiệu đính đều **đã kiểm được**, và vai trò hiệu đính
giải thích luôn **vì sao** Braulio là người chia quyển — câu vì vậy chặt hơn chứ không chỉ an toàn hơn.
Đếm: +7 chữ → `ideas` **130, đúng bằng trần**; nếu áp cùng 09-3 (+1) thì **131, VƯỢT trần một chữ**.
Khi ấy rút thành "do Braulio, người ông gửi bản cho hiệu đính, làm sau" (+4) → **128**.

---
## `CH05-CE07-10` · Pháp Xứng — dòng 361–377

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q457990` → nhãn en `Dharmakirti`, vi `Pháp Xứng`, `P31 = Q5`. Đúng người.
- **Bẫy Wikidata của mục này đã được đọc đúng.** `Q457990` ghi `P569 = +0700-01-01/p7` và `P570 = +0660/p9`.
  Theo `year_in_bucket` của `atlaslib/common.py`, `p7` là **thế kỷ**, tức khoảng **601–700**, không phải
  điểm 700 — đọc đúng thì không có nghịch lý sinh-sau-mất. Mục để `độ tin cậy: Thấp`, nên
  `DATE_TOLERANCE["Thấp"] = None` và lint bỏ qua đối chiếu. Khối 16 ghi đúng, và mục khai đúng.
- `k. 600 – k. 660 CN` theo Frauwallner — **kiểm được tới nguồn**: SEP ghi "Erich Frauwallner came out
  strongly for 600–660 C.E. as Dharmakīrti's dates, using an argumentum ex silentio that is short of
  conclusive". Tức con số đúng là của Frauwallner, **và** chính nguồn của mục gọi lập luận ấy là chưa chốt —
  nên `độ tin cậy: Thấp` là nhãn đúng, không phải nhãn né. SEP cũng xác nhận "một mạch gần đây đẩy ông sớm
  hơn" mà khối 16 nhắc: Krasser (2012) đẩy về giữa thế kỷ 6, Balcerowicz (2016) đề nghị 550–610.
- `nơi: Nam Ấn Độ và vùng Nālandā` — khớp mô tả nguồn ("born in South India and then to have moved to …
  Nālandā"), và mục không biến truyền thống Tây Tạng thành sự kiện chắc.
- "Pramāṇavārttika chỉ thừa nhận hai nguồn tri thức đúng — tri giác trực tiếp và suy luận" — đúng.
- "đòi suy luận chỉ có giá trị khi dựa trên một quan hệ tất yếu: hoặc đồng nhất bản chất, hoặc nhân quả"
  — đúng (*svabhāva* và *tadutpatti*), và diễn đạt tiếng Việt không làm sai nghĩa.
- "hệ của ông vẫn sống ở Tây Tạng như một môn học bắt buộc tới tận nay" — khớp nguồn: trường phái này
  "had an enormous influence on Mahāyāna Buddhism in Central Asia, especially in Tibet".
- **Nguồn 1 tồn tại, đúng tác giả, đúng chuyên trang.** `https://plato.stanford.edu/entries/dharmakiirti/`
  trả **HTTP 200, 145.892 byte**, nội dung thật (không phải trang chặn bot 2–3 KB như ca `ctext.org` hay
  "Client Challenge" của JSTOR mà khối 13 liệt kê), và thẻ `meta author` ghi **"Tillemans, Tom"**.
  Mục ghi "Tom J.F. Tillemans" — đúng người. Đây **không** phải ca slug SEP ma như `mozi` / `thales`
  mà `CONTRIBUTING.md:47` cảnh báo.
- Nguồn 2 tồn tại và đúng: John Dunne, *Foundations of Dharmakīrti's Philosophy*, Wisdom Publications, 2004.
- "Trần-na **có mục riêng** ở `CH05-CE06-05` nên không phải ứng viên bị loại" — mở ra đọc:
  `### CH05-CE06-05 · Trần-na (दिग्नाग Dignāga, Trần Na)`. Đúng người, đúng ID, đúng câu chữ quy tắc 6.
- `Kế thừa từ CH04-CE04-11`: mở ra đọc, đúng là **Vasubandhu**; mức `qua trường phái` đúng.
- Quy tắc 6 cho **Kumārila Bhaṭṭa**: không có mục ở bất kỳ chapter nào.
- `ideas` 112 chữ, `why` 83 chữ. Dưới trần.

### Phát hiện

**[BẮT BUỘC] 10-1 — Mục gán cho ông việc dựng lý thuyết apoha; nguồn số 1 của chính mục nói ngược, và `CH05-CE06-05` của chính atlas cũng nói ngược.**

Nguyên văn câu sai:
> Từ đó ông dựng lý thuyết apoha: từ ngữ không chỉ ra cái phổ quát có thật, chúng chỉ loại trừ cái khác, nên "bò" có nghĩa là "không phải cái không-bò".

Hai chứng cứ độc lập cùng bác:

(1) **Nguồn 1 của mục.** SEP, "Dharmakīrti", mục 2.2: "To solve this problem of 'aboutness' **Dignāga had
devised** the theory of concepts, i.e., apoha ('exclusions'). **Dharmakīrti reinterpreted this theory**,
once again, in terms of causal relations." Mục SEP còn có hẳn hai tiểu mục tách bạch —
*2.2.1 Dignāga's apoha* và *2.2.2 Dharmakīrti's causal version of apoha*. Đây đúng ca quy tắc 7:
nguồn tồn tại, đúng chủ đề, mà luận điểm thì chống lại câu nó đang đỡ.

(2) **Chính atlas này.** `CH05-CE06-05 · Trần-na` viết, nguyên văn: "**Lý thuyết apoha** giải nghĩa của từ
theo lối phủ định: '**bò**' nghĩa là '**không phải cái không-bò**'." Tức hai mục trong cùng một chapter
gán cùng một lý thuyết cho hai người, **bằng đúng một ví dụ minh hoạ**. Lint không có cách nào bắt được.

Điều đáng nói: phần đóng góp thật của Pháp Xứng ở đây — đọc lại apoha theo **quan hệ nhân quả** — vừa
đúng, vừa nối liền với mệnh đề ngay trước đó của mục về hai loại quan hệ tất yếu. Sửa đúng làm mục
**mạch lạc hơn**, không phải mất mát.

Câu thay thế đề xuất, nguyên văn:
> Trên nền đó ông đọc lại lý thuyết apoha của Trần-na theo quan hệ nhân quả: từ ngữ không chỉ ra cái phổ quát có thật, chúng chỉ loại trừ cái khác.

Soi lại chính câu thay thế: (a) "của Trần-na" và "đọc lại … theo quan hệ nhân quả" đều lấy thẳng từ SEP,
đã kiểm. (b) Tôi **bỏ ví dụ "bò" / "không phải cái không-bò"** — không phải vì nó sai, mà vì nó đang là
**bản sao nguyên văn** của một câu ở `CH05-CE06-05`; giữ lại sẽ để nguyên chỗ trùng. Đây đúng chỗ mà một
câu thay thế dễ mang theo cái lỗi nó vừa chẩn, và tôi cắt nó đi. (c) `[KHÔNG KIỂM ĐƯỢC]`: tôi không kiểm
được rằng cách đọc nhân quả ấy là **của riêng** Pháp Xứng chứ không có ai trước — SEP nói "such reliance on
causality seems to be entirely absent in Dignāga", đủ để loại Trần-na nhưng không đủ để loại mọi người khác.
Câu thay thế vì vậy viết "ông đọc lại", không viết "ông là người đầu tiên".
Đếm: −6 chữ → `ideas` **106 chữ**, lệch 6% so với ~100, dưới ngưỡng cảnh báo 30%.

**[BẮT BUỘC] 10-2 — Dòng `trực tiếp` nối hai người cách nhau khoảng sáu mươi năm và chưa từng gặp nhau — đúng hình dạng mà `CONTRIBUTING.md` quy tắc 8 nêu đích danh.**

Nguyên văn dòng sai:
> - CH05-CE06-05 · kế thừa · trực tiếp

Mở đích ra đọc: `CH05-CE06-05 · Trần-na`, metadata `năm: k. 480 – k. 540 CN`. Mục đang xét ghi
`k. 600 – k. 660 CN`. Tức **Trần-na mất khoảng sáu mươi năm trước khi Pháp Xứng sinh** — và SEP gọi thẳng
Dignāga là "**his predecessor**", đồng thời cho biết truyền thống Tây Tạng đặt một người trung gian
(Īśvarasena, học trò của Dignāga) giữa hai người.

Đây là **đích đúng người** — không phải ca trỏ sai — nhưng **sai mức bằng chứng**, và là đúng trường hợp
mà `CONTRIBUTING.md` quy tắc 8 mô tả bằng chữ: "nó không bắt được `trực tiếp` giữa hai người cách nhau
130 năm mà vẫn 'đúng thứ tự'". Lint im lặng vì thứ tự niên đại hợp lệ (người sau sinh sau người trước mất).
Đây là ca `trực tiếp` **sai nhất** của nhóm CE07, và là lý do tôi tách nó khỏi khối "19 dòng đích không phải
người" ở phần đính chính tầng nhóm: 18 dòng kia là tranh luận về **định nghĩa từ vựng** đang chờ
`CONTRIBUTING.md`; dòng này thì sai theo **cả hai** cách đọc của từ `trực tiếp`.

Dòng thay thế đề xuất, nguyên văn:
> - CH05-CE06-05 · kế thừa · qua trường phái

Soi lại chính dòng thay thế: (a) `qua trường phái` nằm trong `EVIDENCE_LEVELS`, lint nhận. (b) Nó mô tả
đúng quan hệ thật — một truyền thừa học phái có người trung gian, không phải thầy trò trực tiếp.
(c) Tôi **không** chọn `suy đoán học giả`: việc Pháp Xứng chú giải và phát triển Trần-na là điều chính
văn bản của ông làm, không phải một suy đoán. (d) So chiếu: `CH05-CE07-07` trong cùng nhóm đã khai
`qua trường phái` cho đúng loại quan hệ này (Huệ Năng ← Bồ-đề-đạt-ma), nên sửa này **đưa mục về đúng
chuẩn mà nhóm đã tự đặt**, không phải áp một chuẩn từ ngoài.

**[NÊN] 10-3 — "tám thế kỷ" là một con số không tự khai mốc đo và không khớp với khung mà chính câu ấy dựng.**

Nguyên văn câu sai:
> Pháp Xứng được chọn theo độ bền (b): cuộc tranh luận ông mở ra chi phối triết học Ấn Độ suốt tám thế kỷ, và khi Phật giáo gần như biến mất khỏi Ấn Độ thì hệ của ông vẫn sống ở Tây Tạng…

Tám thế kỷ tính từ k. 660 là tới khoảng **1460**. Nhưng vế sau của chính câu ấy lấy mốc "khi Phật giáo gần
như biến mất khỏi Ấn Độ" làm bản lề — mốc ấy rơi vào khoảng thế kỷ 12–13, tức khoảng **năm tới sáu** thế kỷ,
không phải tám. Câu vì vậy tự mâu thuẫn ở hai vế liền nhau. Quy ước `content/ch05.md:1271` được đặt ra cho
phần trăm, nhưng lý do của nó — con số phải tự khai nó đo cái gì tới đâu — áp y hệt cho một khoảng thời gian.

Câu thay thế đề xuất, nguyên văn:
> Pháp Xứng được chọn theo độ bền (b): cuộc tranh luận ông mở ra chi phối triết học Ấn Độ cho tới khi Phật giáo gần như biến mất khỏi tiểu lục địa, rồi hệ của ông vẫn sống tiếp ở Tây Tạng…

Soi lại chính câu thay thế: (a) Nó **bỏ hẳn con số** thay vì thay bằng một con số khác — vì
`[KHÔNG KIỂM ĐƯỢC]`: tôi không truy được tới một khảo luận đặt mốc kết thúc cho tranh luận pramāṇa ở Ấn Độ,
chỉ loại được con số tám. (b) Nó biến hai vế đang mâu thuẫn thành một mốc **duy nhất** dùng cho cả hai,
nên không còn chỗ để vênh. (c) Mệnh đề "vẫn sống tiếp ở Tây Tạng" giữ nguyên và đã kiểm được qua SEP.
Đếm: +1 chữ → `why` **84**, dưới trần 104.

**[CÂN NHẮC] 10-4 — Nguồn SEP không có URL, trong một chapter mà bốn mục khác có.**

Nguyên văn:
> **Nguồn:** Tom J.F. Tillemans, "Dharmakīrti", Stanford Encyclopedia of Philosophy; …

§5 của `prompts/atlas-prompt.md` chỉ đòi "kèm link nếu có", nên đây **không phải lỗi**. Nhưng `CH05-CE06-12`
trong cùng chapter dẫn SEP **kèm URL đầy đủ**, và slug của mục này thuộc dạng dễ viết sai —
đúng là `/entries/dharmakiirti/` với **hai chữ i**. `CONTRIBUTING.md:47` ghi rằng slug SEP là một nguồn lỗi
đã biết. Ghi URL vào là cách rẻ nhất để vòng sau khỏi phải đoán.

Dòng thay thế đề xuất, nguyên văn:
> **Nguồn:** Tom J.F. Tillemans, "Dharmakīrti", Stanford Encyclopedia of Philosophy, <https://plato.stanford.edu/entries/dharmakiirti/>; John Dunne, Foundations of Dharmakīrti's Philosophy (Wisdom Publications, 2004).

Soi lại chính dòng thay thế: URL này **đã được mở trong vòng này** và trả HTTP 200 với 145.892 byte nội dung
thật — không phải một URL tôi dựng từ quy luật đặt tên. Trường `Nguồn` không nằm trong phạm vi đếm chữ
của `WORD_TARGET` nên không động tới trần nào.

---
## `CH05-CE07-11` · Tùng Tán Cán Bố — dòng 378–394

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q320122` → nhãn en `Songtsän Gampo`, vi `Tùng Tán Cán Bố`, `P31 = Q5`. Đúng người.
- "chỉ hơn một thế kỷ sau quân Tây Tạng có lúc chiếm được Trường An" — ông mất 650, Trường An bị chiếm 763:
  **113 năm**. "Hơn một thế kỷ" đúng, và cách viết "có lúc chiếm được" không thổi phồng thành chiếm đóng lâu dài.
- "một hệ chữ Tây Tạng được tạo theo mẫu Brāhmī của Ấn Độ — **truyền thống quy cho** Thönmi Sambhoṭa"
  — rào đúng, và rào đúng chỗ: sự tồn tại lịch sử của Thönmi Sambhoṭa khó xác minh, và chính truyền thuyết
  ông chế ra chữ viết là thứ bị nghi ngờ. Mục **không** biến truyền thống thành sự kiện. Thönmi Sambhoṭa
  cũng không có mục ở chapter nào nên không vướng quy tắc 6.
- "Bộ luật và khung hành chính đầu tiên của Tây Tạng cũng **được quy cho** thời ông" — rào đúng cùng kiểu.
- **`vùng: Đông Á`, và đây là một quyết định đúng đã được ghi lại.** Khối 19 (`content/ch05.md:1127`) ghi
  rõ lý do: `REGIONS` không có ô Nội Á, nên theo tiền lệ Mặc Đốn thiền vu `CH03-BCE02-12`; và ghi "Trung Á"
  sẽ là đổi vùng để làm đẹp thống kê, đúng điều `CONTRIBUTING.md` quy ước `vùng:` mục 4 cấm. Tôi đã đối chiếu
  `CH03-BCE02-12` và tiền lệ có thật. **Không đề nghị đổi.**
- "**Trisong Detsen có mục riêng ở `CH05-CE08-10` nên không phải ứng viên bị loại**" — mở ra đọc:
  `### CH05-CE08-10 · Trisong Detsen (ཁྲི་སྲོང་ལྡེ་བཙན་)`. **Đúng người, đúng ID, đúng câu chữ
  `CONTRIBUTING.md:51`.** Đây là ca quy tắc 6 phát sinh theo thời gian mà đề bài nêu đích danh — nó
  **đã được vá rồi**, và vá đúng. Không còn hở.
- Quy tắc 5 và 6 cho **Gar Tongtsen**: `Q843378`, **590–667**. Chồng lấn thật với ông (k. 617–650).
  Không có mục ở bất kỳ chapter nào.
- Nguồn 1 tồn tại và đúng: Brandon Dotson, *The Old Tibetan Annals*, Verlag der Österreichischen Akademie
  der Wissenschaften, 2009 — đúng tác giả, đúng nhà xuất bản, đúng năm. (Phạm vi niên đại của nó thì có
  vấn đề — xem 11-2.)
- Nguồn 2 tồn tại và đúng: Christopher I. Beckwith, *The Tibetan Empire in Central Asia*,
  Princeton University Press, 1987.
- `ideas` 114 chữ, `why` 90 chữ. Dưới trần.

### Phát hiện

**[BẮT BUỘC] 11-1 — `Tư tưởng` dùng chính tường thuật mà `Vì sao chọn` tuyên bố là không dùng, và nửa bị tuyên bố loại lại là nửa yếu bằng chứng nhất.**

Nguyên văn hai chỗ đá nhau:
> Ông hợp nhất các thế lực trên cao nguyên thành một đế quốc đủ mạnh để **buộc cả nhà Đường lẫn Nepal gả công chúa**…

> Phần tiểu sử tôn giáo — **hai công chúa** cảm hoá ông — đến từ biên niên Phật giáo soạn muộn hơn nhiều, nên **mục này không dùng**.

Mục tuyên bố loại tường thuật hai công chúa, rồi dùng đúng tường thuật ấy làm **bằng chứng chính** cho
mệnh đề về sức mạnh đế quốc. Và nửa Nepal là nửa yếu nhất: tính lịch sử của công chúa Bhrikuti **không
chắc chắn**, và **không có một tham chiếu nào tới bà trong khối văn bản Đôn Hoàng** — tức không có trong
chính nguồn số 1 của mục. Nửa Đường (Văn Thành công chúa) thì có nền vững hơn nhiều.

Có thể mục định tách "sự kiện hôn nhân chính trị" khỏi "tường thuật cảm hoá tôn giáo". Nhưng câu như đang
viết không làm được phép tách ấy, vì nó khẳng định **cả hai** cuộc hôn nhân, trong đó một cuộc là thứ chỉ
biết qua đúng lớp biên niên muộn mà câu kia vừa loại.

Câu thay thế đề xuất, nguyên văn:
> Ông hợp nhất các thế lực trên cao nguyên thành một đế quốc đủ mạnh để nhà Đường phải gả công chúa Văn Thành về Lhasa…

Soi lại chính câu thay thế: (a) Đã **bỏ vế Nepal** — vế không có chứng cứ đương thời. Bỏ nó làm câu vững
lên, và làm `ideas` thôi mâu thuẫn với `why`. (b) Việc gả Văn Thành thì có trong cả nguồn Hán lẫn nguồn
Tây Tạng, nên nó không nằm trong phần `why` loại trừ. (c) `[KHÔNG KIỂM ĐƯỢC]` và đây là chỗ phải nói thẳng:
tôi **không** kiểm được chữ "buộc" / "phải" — chiều cưỡng ép. Hồ sơ cho thấy quan hệ phức tạp hơn một chiều:
trong thư gửi hoàng đế Đường, chính ông tự xưng là **bề tôi của nhà Đường**, và năm 649 Đường Cao Tông
phong tước cho ông; Tây Tạng là phiên thuộc trên danh nghĩa cho tới 670. Nếu không muốn mang mệnh đề về
chiều cưỡng ép, bỏ chữ "phải": "…một đế quốc đủ mạnh để nhà Đường gả công chúa Văn Thành về Lhasa" — câu
vẫn đứng được trên sự kiện, và **đó là bản tôi khuyến nghị**.
Đếm: −2 chữ → `ideas` **112**, dưới trần 130.

**[BẮT BUỘC] 11-2 — Nguồn số 1 bắt đầu đúng vào năm ông mất (quy tắc 7, kiểm khung niên đại của nguồn).**

Nguyên văn trường `Nguồn`:
> Old Tibetan Annals, bản chép Đôn Hoàng, trong Brandon Dotson, The Old Tibetan Annals (…, 2009); …

*Old Tibetan Annals* gồm hai bản chép: bản "dân sự" (IOL Tib J 750 + Pelliot tibétain 1288) phủ các năm
**650–748**, bản "quân sự" (Or.8212/187) phủ **743–765**. Tùng Tán Cán Bố **mất năm 650**. Tức nguồn sơ cấp
duy nhất của mục bắt đầu ghi chép đúng vào năm cuối đời ông, và **không phủ** bất kỳ mệnh đề nào mà mục
dựa vào: hợp nhất cao nguyên, hôn nhân với Đường và Nepal, tạo chữ viết, bộ luật đầu tiên.

Đây là quy tắc 7 áp ở dạng **khung niên đại** chứ không phải dạng luận điểm — đúng như đề bài yêu cầu kiểm:
"nhan đề/khung niên đại của nguồn so với mệnh đề nó đang đỡ". Nguồn tồn tại, đúng chủ đề, đúng nhà xuất bản,
mà vẫn không đỡ được điều nó đang đỡ. Và điều này **làm nặng thêm phát hiện 11-1**: khi mục nói tường thuật
hai công chúa "đến từ biên niên Phật giáo soạn muộn hơn nhiều", nó ngụ ý rằng phần nó **giữ** thì có nguồn
sớm — nhưng nguồn sớm ấy không nói về thời ông.

Dòng thay thế đề xuất, nguyên văn:
> **Nguồn:** Old Tibetan Annals, bản chép Đôn Hoàng, trong Brandon Dotson, The Old Tibetan Annals (Verlag der Österreichischen Akademie der Wissenschaften, 2009) — lưu ý bản chép này bắt đầu ở năm 650, tức năm ông mất, nên dùng cho khung triều đại kế tiếp chứ không dùng cho các mệnh đề về chính thời ông; Christopher I. Beckwith, The Tibetan Empire in Central Asia (Princeton University Press, 1987).

Soi lại chính dòng thay thế: (a) Dạng câu này **đã có tiền lệ trong chính nhóm** — `CH05-CE07-04` dùng đúng
công thức "lưu ý đây là chuyên khảo về Ngụy Trưng …, dùng cho vế ấy chứ không dùng cho vế bộ luật".
Tôi dùng lại khuôn ấy thay vì bịa khuôn mới. (b) Con số 650 **đã kiểm được**. (c) `[KHÔNG KIỂM ĐƯỢC]`:
tôi **không** xác định được rằng Beckwith 1987 đỡ đủ cho toàn bộ các mệnh đề còn lại của mục — tôi chỉ xác
nhận sách tồn tại và đúng chủ đề (đế quốc Tây Tạng ở Trung Á thời Trung cổ sớm). Nếu vòng sau muốn một
nguồn sơ cấp thật cho thời Tùng Tán Cán Bố thì phải tìm nguồn khác, và **ghi chú này không thay thế được
việc đó** — nó chỉ ngăn người đọc tưởng rằng nguồn hiện có đã đỡ.

**[BẮT BUỘC] 11-3 — Dòng quan hệ khai "tương đồng độc lập · suy đoán học giả" cho một cặp mà chính mục mô tả là có tiếp xúc ngoại giao trực tiếp.**

Nguyên văn dòng sai:
> - CH05-CE07-04 · tương đồng độc lập · suy đoán học giả

`CH05-CE07-04` là **Đường Thái Tông** — đích đúng người. Nhưng nhãn thì ngược với nội dung của chính mục:
câu đầu `ideas` nói nhà Đường gả công chúa cho ông, tức có **quan hệ triều đình với triều đình**.
Hồ sơ còn cho thấy nhiều hơn: ông tự xưng bề tôi của nhà Đường trong thư, và năm 649 được triều Đường
phong tước. `prompts/atlas-prompt.md` §5 nói rõ về loại quan hệ này: "'tương đồng độc lập' là hợp lệ và
**nên dùng khi không có bằng chứng tiếp xúc**". Ở đây bằng chứng tiếp xúc là thứ mục tự đưa ra ở dòng đầu.

Đây là ca **ngược chiều** với 10-2: ở `CH05-CE07-10`, mức bằng chứng bị thổi lên; ở đây nó bị dìm xuống
tới mức phủ nhận một quan hệ có thật. Cả hai lint đều không bắt được, vì cả hai nhãn đều nằm trong từ vựng.

Dòng thay thế đề xuất, nguyên văn:
> - CH05-CE07-04 · kế thừa · trực tiếp

Soi lại chính dòng thay thế — **tôi phải soi dòng này kỹ nhất trong cả báo cáo, vì nó là dòng duy nhất tôi
đề xuất NÂNG lên `trực tiếp`, trong khi phần lớn báo cáo đang hạ các dòng khác xuống.** (a) Hai người
**sống cùng thời và hai triều đình có tiếp xúc được ghi chép** (hôn nhân 641, phong tước 649) — đây là
nghĩa người–người, không phải nghĩa văn bản, nên `trực tiếp` đúng theo **cả hai** cách đọc đang tranh luận
ở tầng chapter. (b) Nhãn `kế thừa`: `[KHÔNG KIỂM ĐƯỢC]` — tôi **không** truy được tới nguồn cho mệnh đề
rằng khung hành chính Tây Tạng chép theo mẫu Đường; ngược lại, một mạch tường thuật truyền thống quy
"mô hình luật lệ và hành chính" cho phía **Đột Quyết** chứ không phải Đường. Vì vậy, nếu không muốn khẳng
định chiều kế thừa thể chế, phương án an toàn là giữ nguyên loại quan hệ hiện có và **chỉ sửa mức bằng chứng**:
> - CH05-CE07-04 · tương đồng độc lập · trực tiếp

Dạng ấy nói đúng điều kiểm được (hai nhà nước hình thành song song, có tiếp xúc được ghi chép) mà không
khẳng định chiều vay mượn nào. **Đó là bản tôi khuyến nghị.**

**[CÂN NHẮC] 11-4 — `Trung bình` cho một năm sinh có độ tán rộng hơn cả ca mà nhóm này đã để `Thấp`.**

Nguyên văn:
> `năm: k. 617–650 CN | … | độ tin cậy niên đại: Trung bình | …`

Năm mất 650 thì vững. Năm sinh thì không: `Q320122` khai **hai** giá trị `P569` cùng rank `normal`
(+0604 và +0617), và các con số khác cũng được đề nghị — 569, 593, 605 — vì niên đại được dựng ngược từ
tục lệ vua Tạng lên ngôi quanh tuổi mười ba. Độ tán thực tế vượt xa dung sai ±25 của `Trung bình`.

So trong cùng nhóm: `CH05-CE07-10` để **`Thấp`** cho một độ tán hẹp hơn (Frauwallner 600–660 so với
Balcerowicz 550–610, tức 50 năm), và khối 16 giải thích vì sao. Hai mục đang dùng hai thước khác nhau.

Đề xuất, nguyên văn: `năm: k. 617–650 CN | … | độ tin cậy niên đại: Thấp | …`

Soi lại chính đề xuất — và đây là chỗ phải cân nhắc thật chứ không phải đổi cho an toàn: hạ xuống `Thấp`
làm `DATE_TOLERANCE` thành `None`, tức **tắt hẳn** đối chiếu Wikidata cho mục này. Với `CH05-CE07-06` tôi đã
**từ chối** đề xuất hạ nhãn đúng vì lý do ấy. Khác biệt ở đây: niên đại Huyền Trang được chép tới từng ngày
và chỉ vướng một tiền tố `k.` thừa, còn năm sinh ở đây **thật sự không chốt được** và Wikidata tự khai hai
giá trị ngang hàng — tức phép đối chiếu vốn đã không phán được gì, tắt nó không mất thêm lớp bảo vệ nào.
Nếu Owner muốn giữ lớp đối chiếu, phương án thay thế là giữ `Trung bình` và ghi lý do vào Ghi chú biên tập,
như khối 19 đã làm cho trường `vùng:` của chính mục này.

---
## `CH05-CE07-12` · Kʼinich Janaabʼ Pakal — dòng 395–411

**Đã kiểm được (không có phát hiện):**

- `wikidata: Q371384` → nhãn en/vi `K'inich Janaab' Pakal`, `P31 = Q5`. **Đúng người**, và đây là ca mà
  khối 15 ghi lại: bản nháp từng ghi `Q311215`, vốn là **Colias**, một chi bướm. Bản hiện tại đã đúng.
  Tôi cũng kiểm hai bẫy kề bên mà khối ấy nêu — `Q641749` (một Janaabʼ Pakal khác, mất 612) và `Q4017694`
  (Janaab Pakal III) — mục **không** dính cái nào.
- `603–683 CN`, `Cao` (±5). `Q371384` khai `P569 = +0603-03-23/p11`, `P570 = +0683-08-28/p11`.
  Khớp tới ngày với bi ký (24-3-603 và 29-8-683 theo quy ước lịch khác), và `Cao` là nhãn đúng.
  Đây là mục có niên đại vững nhất nhóm CE07.
- "Lên ngôi năm **615** lúc **mười hai tuổi** và trị vì **sáu mươi tám năm**" — cả ba con số đều kiểm được
  và khớp chính xác. Ba con số trong một câu, không con số nào lệch — hiếm.
- "một thành **từng** bị Calakmul đánh bại **hai lần**" — đúng: Palenque bị Calakmul cướp phá năm **599**
  (bốn năm trước khi ông sinh) và bị đánh lần nữa năm **611**. Chữ "từng" đặt đúng chỗ, vì cả hai lần đều
  xảy ra **trước** khi ông lên ngôi; mục không gán hai thất bại ấy cho triều ông.
- "Đền Bi ký do **con ông** hoàn tất" — đúng: Kʼinich Kan Bahlam II hoàn thành công trình sau 683.
- "khối văn bản tượng hình **thuộc loại** dài nhất châu Mỹ tiền Columbus" — rào đúng bằng hai chữ
  "thuộc loại": ba tấm bi ký của Đền Bi ký gồm **617 ô chữ** và được mô tả là "một trong những bi văn Maya
  dài nhất", không phải dài nhất tuyệt đối. Nếu mục viết "dài nhất" trần trụi thì đã sai; nó không viết vậy.
- "tính thời gian xuôi tới tận **năm 4772**" — kiểm được: bi ký trỏ tới ngày **21-10-4772**, hơn bốn nghìn
  năm sau thời ông. Con số đúng.
- "`Kʼinich Kan Bahlam II và Đền Bi ký · kế thừa · trực tiếp`" — đích là **con ruột và người kế vị**,
  quan hệ người–người thật. Một trong 7 dòng `trực tiếp` dùng đúng nghĩa của nhóm.
- Quy tắc 5 và 6 cho **Yuknoom Chʼeen II**: trị vì Calakmul 636–686, chồng lấn thật với Pakal (603–683);
  không có mục ở bất kỳ chapter nào.
- **Mục tự khai khuyết tật tiêu chí, và đó là chỗ làm tốt nhất của cả nhóm.** Nguyên văn: "Phải nói thẳng
  một khuyết tật của tiêu chí phạm vi (a): trước 1492 không tồn tại đường vật lý nào để ảnh hưởng ra khỏi
  bán cầu." Đây là cách xử đúng mà `CH05-CE07-03` nên học theo (xem 03-1).
- Nguồn 2 tồn tại và đúng cả ba: David Stuart và George Stuart, *Palenque: Eternal City of the Maya*,
  Thames & Hudson, **2008**.
- `ideas` 115 chữ, `why` 90 chữ. Dưới trần.

### Phát hiện

**[NÊN] 12-1 — Mô tả nắp quan tài đặt ông sai chỗ trong chính bức chạm.**

Nguyên văn câu sai:
> Nắp quan tài chạm hình ông **rơi vào cây vũ trụ** là một trong những hình ảnh Maya được biết nhiều nhất.

Bố cục của nắp là: Pakal **rơi xuống** — vào hàm của cõi dưới, hoặc theo cách đọc của Linda Schele là rơi
dọc dải Ngân Hà về chân trời nam — **bên dưới** cây vũ trụ, vốn vươn lên phía trên ông. Ông không rơi *vào*
cây; cây là trục đứng của bố cục, còn ông là chuyển động đi xuống dọc trục ấy. Chi tiết này không vụn:
chính cấu trúc "rơi xuống dưới cây" là thứ làm bức chạm thành một tuyên bố vũ trụ học về tái sinh, và cũng
chính chỗ này là chỗ thuyết phi hành gia của von Däniken bám vào — tức một mô tả lệch ở đây mở đúng cánh
cửa mà khối 17 của Ghi chú biên tập dặn phải chặn.

Câu thay thế đề xuất, nguyên văn:
> Nắp quan tài chạm hình ông rơi xuống cõi dưới ở gốc cây vũ trụ là một trong những hình ảnh Maya được biết nhiều nhất.

Soi lại chính câu thay thế: (a) Cả hai yếu tố — chuyển động rơi xuống, và cây vũ trụ ở trên — đều kiểm được.
(b) Tôi **cố ý không viết "rơi dọc dải Ngân Hà"**: đó là cách đọc **của Linda Schele**, một cách đọc cụ thể
có tên tác giả, nên viết nó như mô tả trung lập sẽ là gán một diễn giải thành sự kiện. (c) `[KHÔNG KIỂM
ĐƯỢC]` — tôi không truy được tới một bản giải mã từng ký hiệu của nắp quan tài, chỉ tới các mô tả tổng hợp;
nếu muốn câu hoàn toàn không mang diễn giải nào, cắt thành "Nắp quan tài chạm hình ông cùng cây vũ trụ…"
— nhưng bản ấy **mất** chính yếu tố làm bức chạm đáng nói, nên tôi không khuyến nghị.
Đếm: +2 chữ → `ideas` **117**, dưới trần 130.

**[NÊN] 12-2 — Nguồn số 1 được dẫn cho tiểu sử chung, trong khi đóng góp thật của nó là một tranh luận mà mục cố ý không nhắc (quy tắc 7).**

Nguyên văn trường `Nguồn`:
> Vera Tiesler và Andrea Cucina (chủ biên), Janaab' Pakal of Palenque: Reconstructing the Life and Death of a Maya Ruler (University of Arizona Press, 2006); …

Sách này là một tập chuyên đề **giám định lại bộ xương** — nó tồn tại là để trả lời tranh luận tuổi thọ
mở ra từ giám định năm 1952 (bộ xương cho tuổi 40–50, trong khi bi ký cho 80). Mục thì để
`độ tin cậy: Cao` theo bi ký rồi dừng, **không nhắc tranh luận**. Khối 17 của Ghi chú biên tập
(`content/ch05.md:1119`) đã nhận ra chính xác điều này và ghi: "Tiesler và Cucina 2006 chỉ xuất hiện ở
trường `Nguồn` **như nhan đề sách**." Tức vấn đề đã được chẩn ở tầng ghi chú nhưng **chưa được xử ở tầng mục**.

Đây không phải ca dẫn ngược luận điểm (sách **ủng hộ** phía bi ký, nên nó đỡ đúng chiều cho nhãn `Cao`).
Nó là ca **dẫn một chuyên khảo cho mệnh đề nằm ngoài chuyên đề của nó** — cùng họ với ca Wechsler mà
`CH05-CE07-04` đã phải rào, và atlas đã có sẵn công thức rào.

Dòng thay thế đề xuất, nguyên văn:
> **Nguồn:** Vera Tiesler và Andrea Cucina (chủ biên), Janaab' Pakal of Palenque: Reconstructing the Life and Death of a Maya Ruler (University of Arizona Press, 2006) — tập chuyên đề giám định lại bộ xương, dùng cho vế niên đại chứ không dùng cho vế tiểu sử chính trị; David Stuart và George Stuart, Palenque: Eternal City of the Maya (Thames & Hudson, 2008).

Soi lại chính dòng thay thế: (a) Dùng lại đúng khuôn mà `CH05-CE07-04` đã dùng, không bịa khuôn mới.
(b) "giám định lại bộ xương" là mô tả đã kiểm được từ nhan đề phụ của chính sách.
(c) Tôi **không** đề xuất đưa tranh luận tuổi thọ vào trường `ideas`: khối 17 đã nêu công thức đúng cho
việc ấy ("nghiêng về phía bi ký", không phải "đã chứng minh") và ghi rằng đó là quyết định để ngỏ cho
vòng sau. Việc rào nguồn ở đây **không** thay cho quyết định ấy; nó chỉ ngăn người đọc hiểu nhầm phạm vi
của nguồn trong lúc chờ.
(d) Trường `Nguồn` không nằm trong `WORD_TARGET` nên không chạm trần nào.

**[CÂN NHẮC] 12-3 — Một so sánh cấp nhất trên toàn bán cầu, phát biểu như sự kiện.**

Nguyên văn:
> …khiến ông là **cá nhân châu Mỹ tiền Columbus mà ngày nay biết rõ nhất**.

Mệnh đề nền ("hồ sơ văn bản và kiến trúc Palenque chi tiết hơn bất cứ nơi nào khác ở vùng Maya") thì đo
được và nhiều khả năng đúng. Mệnh đề dẫn xuất thì trùm cả **hai lục địa và mọi nền văn minh tiền 1492** —
không có thước, không có mốc, không có nguồn. Cùng họ với ca 03-3 và với loại mệnh đề mà quy ước ở
`content/ch05.md:1271` muốn chặn. `[KHÔNG KIỂM ĐƯỢC]` — vòng này không truy được tới bất kỳ khảo luận nào
xếp hạng như vậy; chỉ loại được tính hiển nhiên của nó.

Câu thay thế đề xuất, nguyên văn:
> …khiến ông là người cai trị Maya cổ điển mà đời sống được ghi chép dày nhất.

Soi lại chính câu thay thế: (a) Đã **thu phạm vi so sánh** từ "châu Mỹ tiền Columbus" về "Maya cổ điển",
tức đúng phạm vi mà mệnh đề nền của chính mục đo được. (b) Đã đổi "biết rõ nhất" (một mệnh đề về trạng
thái tri thức hiện nay, không đo được) thành "được ghi chép dày nhất" (một mệnh đề về khối tư liệu, đo được).
(c) `[KHÔNG KIỂM ĐƯỢC]` phần còn lại: tôi **không** đối chiếu khối bi ký Palenque với Copán, Tikal hay
Yaxchilán để xác nhận "dày nhất". Nếu không muốn giữ bất kỳ cấp nhất nào, cắt thành "…khiến đời sống của
ông được ghi chép dày hơn hẳn phần lớn người cai trị Maya cổ điển" — câu vẫn đỡ được lập luận (c) của mục.
Đếm: −3 chữ → `why` **87**, dưới trần 104.

**[CÂN NHẮC] 12-4 — Năm in của nguồn 1 có hai giá trị trong các bản ghi thư mục.**

Mục ghi **2006**; bản ghi thư mục tra được ghi **2005** cho bản University of Arizona Press, và **2004**
cho bản tiếng Tây Ban Nha (*Janaab' Pakal de Palenque*, Universidad Autónoma de Yucatán / UNAM).
Không đề xuất sửa — 2006 là năm thường được dẫn và nằm trong vùng hợp lý. `[KHÔNG KIỂM ĐƯỢC]` phần phân
biệt lần in: tôi không mở được trang bản quyền. Ghi lại để vòng sau khỏi "sửa" thành 2005 mà tưởng là đính chính.
(Ca cùng loại: Wechsler 1974/1975 ở `CH05-CE07-04`, và Madelung 1996/1997 ở `CH05-CE07-03`. Ba ca trong
một nhóm cho thấy đây là một nguồn nhiễu hệ thống của bản ghi thư mục, không phải lỗi của người viết.)

---
## Bảng tổng

| Mục | Dòng | BẮT BUỘC | NÊN | CÂN NHẮC | Tổng |
|---|---|---|---|---|---|
| *Tầng nhóm* (Bối cảnh + rà chéo) | 209–411 | 0 | 1 | 0 | 1 |
| `CH05-CE07-01` Muhammad | 212–228 | 1 | 1 | 2 | 4 |
| `CH05-CE07-02` Umar ibn al-Khattab | 229–245 | 1 | 1 | 1 | 3 |
| `CH05-CE07-03` Ali ibn Abi Talib | 246–261 | 0 | 2 | 1 | 3 |
| `CH05-CE07-04` Đường Thái Tông | 262–277 | 1 | 1 | 1 | 3 |
| `CH05-CE07-05` Võ Tắc Thiên | 278–293 | 1 | 1 | 1 | 3 |
| `CH05-CE07-06` Huyền Trang | 294–310 | 0 | 2 | 1 | 3 |
| `CH05-CE07-07` Huệ Năng | 311–326 | 0 | 1 | 2 | 3 |
| `CH05-CE07-08` Brahmagupta | 327–343 | 0 | 2 | 1 | 3 |
| `CH05-CE07-09` Isiđôrô thành Seville | 344–360 | 1 | 2 | 1 | 4 |
| `CH05-CE07-10` Pháp Xứng | 361–377 | 2 | 1 | 1 | 4 |
| `CH05-CE07-11` Tùng Tán Cán Bố | 378–394 | 3 | 0 | 1 | 4 |
| `CH05-CE07-12` Kʼinich Janaabʼ Pakal | 395–411 | 0 | 2 | 2 | 4 |
| **Tổng** | | **10** | **17** | **15** | **42** |

### Ba mục nặng nhất, và hình dạng chung của chúng

1. **`CH05-CE07-11` Tùng Tán Cán Bố — 3 BẮT BUỘC.** Cả ba đều là **mâu thuẫn nội tại**: `ideas` dùng
   tường thuật mà `why` tuyên bố loại; nguồn sơ cấp bắt đầu ở năm ông mất; dòng quan hệ khai "không có
   tiếp xúc" cho một cặp mà chính mục mô tả là có hôn nhân triều đình. Nghịch lý đáng ghi: đây lại là mục
   **duy nhất** của nhóm có ca quy tắc 6 phát sinh theo thời gian (Trisong Detsen), và ca ấy **đã được vá
   đúng**. Vòng trước sửa đúng chỗ được nhắm, và ba chỗ không được nhắm thì còn nguyên.
2. **`CH05-CE07-10` Pháp Xứng — 2 BẮT BUỘC.** Cả hai là ca sách giáo khoa cho hai quy tắc khác nhau:
   quy tắc 7 (SEP nói Trần-na dựng apoha, mục nói Pháp Xứng dựng) và quy tắc 8 (`trực tiếp` giữa hai người
   cách nhau sáu mươi năm). Cả hai đều bị bác bởi **chính nguồn của mục** và bởi **chính một mục khác của
   atlas**, không cần tri thức ngoài.
3. **`CH05-CE07-09` Isiđôrô — 1 BẮT BUỘC nhưng là ca lan rộng nhất.** Việc viện "tiêu chuẩn atlas đã dùng
   cho **Pappus** và Wulfila" không đứng được ở nửa Pappus, và công thức ấy **đã được chép sang
   `CH05-CE06-04 · Varāhamihira`** trong cùng chapter. Khuyến nghị thủ tục: `grep -n "Pappus và Wulfila"
   content/*.md` trên toàn kho trước khi sửa, vì đây là lỗi của một **khuôn câu**, không của một mục.

### Hai nhận xét ở tầng nhóm, ngoài bảng

- **Thể thức nêu ứng viên bị loại của CE07 không phải 12/12.** Khối 44 của Ghi chú biên tập
  (`content/ch05.md:1268`) đo CE07 là **12/12** và gọi đó là "một đỉnh". Đếm lại chặt: `CH05-CE07-01`
  **không nêu tên ai** (viết "Không có ứng viên cùng chỗ" — hợp lệ theo quy tắc 5, nhưng không phải nêu tên),
  và `CH05-CE07-09` nêu một người **thuộc nhóm CE06** mà chapter đã chấm ở nhóm ấy. Con số đúng là
  **11/12** theo cách đếm rộng, **10/12** theo cách đếm chặt. Mốc đo: nhóm CE07 ở `content/ch05.md`
  dòng 209–411, ngày **2026-11-02**. Điều này **không** phá kết luận của khối 44 (CE07 vẫn cao hơn hẳn
  bốn nhóm sau), nhưng nó làm "đỉnh" thấp đi một bậc.
- **Quy tắc 6 sạch, quy tắc 7 và 8 thì không.** Đây là kết quả đáng chú ý nhất của vòng này: **0 ca**
  quy tắc 6 còn hở (17 cái tên bị loại, đối chiếu với toàn bộ 285 mục ở `content/*.md` kể cả `ch90.md`),
  **0 ca** Q-ID trỏ sai người, **0 ca** liên kết ID trỏ sai người, **0 ca** vượt trần chữ,
  **0 URL chết** (vì nhóm không dùng URL nào). Toàn bộ 10 phát hiện BẮT BUỘC nằm ở hai chỗ mà **không
  script nào kiểm được**: nguồn bị dẫn sai chiều hoặc sai phạm vi (quy tắc 7), và mức bằng chứng sai
  (quy tắc 8). Cổng tự động của repo đang đứng vững ở đúng chỗ nó được thiết kế để đứng.

---

## Mọi `[KHÔNG KIỂM ĐƯỢC]` của vòng này

Liệt kê đầy đủ, kể cả những chỗ nằm trong **câu thay thế của chính tôi** — theo yêu cầu soi câu thay thế
nghiêm như bản gốc. Mỗi dòng ghi: điều không kiểm được · vì sao · cắt gì thì câu vẫn đứng.

**A. Trong phần chẩn (mệnh đề của bản gốc mà tôi không phán được đúng/sai)**

1. **G-1** · Trường An có phải "đô thị lớn nhất thế giới" thế kỷ 7 · không truy được tới một phép đếm dân cư
   hay diện tích có mốc năm · bỏ hẳn vế so sánh.
2. **04-3** · Phần nào của khởi cư chú thời Đường Thái Tông đã bị sửa · không mở được tới khảo luận sử liệu ·
   giữ nguyên cách rào hiện có của mục ("có dấu hiệu đã được sửa"), đừng làm chặt thêm.
3. **05-1** · "Hình ảnh tàn bạo … phần lớn do sử gia Nho giáo đời sau xây" · không truy được tới khảo luận
   cụ thể · cắt vế này, phần còn lại của câu thay thế vẫn đứng.
4. **06-2** · Các dị bản 596 / 600 cho năm sinh Huyền Trang · không truy được tới nguồn gốc · không ảnh
   hưởng tới kết luận, vì kết luận chỉ là "không thể vừa ghi `k.` vừa ghi `Cao`".
5. **07-1** · Yampolsky 1967 phát biểu mệnh đề "bộ duy nhất được gọi là kinh" **với giới hạn nào** ·
   không mở được bản in · nếu bản in cũng viết không giới hạn thì mục phải ghi "theo Yampolsky".
6. **09-4** · Braulio là "học trò" hay "bạn/người hiệu đính" theo cách hai người tự mô tả · không mở được
   tập thư từ · câu thay thế đã né bằng cách chỉ dùng chức vị và vai trò hiệu đính, cả hai đều kiểm được.
7. **10-3** · Mốc kết thúc của tranh luận pramāṇa ở Ấn Độ · không truy được tới khảo luận đặt mốc ·
   câu thay thế **bỏ hẳn con số** thay vì thay bằng con số khác.
8. **11-1** · Chiều cưỡng ép trong hôn nhân Đường–Tạng (chữ "buộc") · hồ sơ cho thấy quan hệ hai chiều
   (ông tự xưng bề tôi nhà Đường, được phong tước 649) · bỏ chữ "phải"/"buộc", câu vẫn đứng trên sự kiện.
9. **12-1** · Bản giải mã từng ký hiệu nắp quan tài Pakal · chỉ tới được mô tả tổng hợp · cắt thành
   "ông cùng cây vũ trụ" thì an toàn tuyệt đối nhưng **mất** yếu tố đáng nói, nên tôi không khuyến nghị.
10. **12-3** · Khối bi ký Palenque có "dày nhất" so với Copán, Tikal, Yaxchilán không · không đối chiếu ·
    cắt thành "dày hơn hẳn phần lớn người cai trị Maya cổ điển".
11. **03-3** · Madelung có phải người "nghiêng về phía Alid rõ nhất trong giới hiện đại" · không truy được
    tới một bài điểm sách nào xếp hạng như vậy · câu thay thế đã bỏ hẳn xếp hạng cấp nhất.
12. **08-1** · Chứng cứ đương thời cho việc Brāhmasphuṭasiddhānta được dịch sang tiếng Ả Rập · mọi đường
    đều quay về chuỗi Ibn al-Adamī → al-Qifṭī mà chính mục đã gọi là giai thoại · câu thay thế dùng dạng
    yếu ("có dấu vết trong mạch"), và cắt thêm cụm "rõ nhất" thì vẫn đứng.

**B. Trong câu thay thế của chính tôi (phần người sửa phải tự quyết trước khi dùng)**

13. **02-2 (b)** · Việc Umar đặt chế độ *qāḍī* tách khỏi tổng trấn · không mở được bản in Kennedy 2007,
    và mệnh đề mang **đúng hình dạng** của những quy gán muộn mà chính mục đã phải rào hai lần ·
    **ĐỪNG DÙNG phương án (b).** Phương án đứng được là (a): đổi `Luật` thành `Kinh tế`, hoặc bỏ lĩnh vực thứ hai.
14. **04-1** · Bộ Taihō (701) của Nhật và luật Silla mô phỏng bản Đường luật **653** hay bản **637** ·
    không mở được tới văn bản hai bộ ấy · dùng bản cắt (bỏ hẳn mệnh đề về bộ luật); câu vẫn đứng trên
    khuôn triều đình và chế độ khảo hạch.
15. **04-2** · Quy mô tuyệt đối của khoa cử dưới triều Thái Tông · không tra được số người đỗ mỗi năm ·
    câu thay thế **cố ý không nêu con số nào** — nêu một con số ở đây sẽ tái lập chính lỗi vừa chẩn.
16. **05-2** · Mức độ đồng thuận của "sử học hiện đại" về việc quý tộc tây bắc suy yếu · không xác định được ·
    cắt vế sau; khi ấy lập luận (d) của mục phải dựa hẳn vào vế chính danh Phật giáo, vốn có Guisso đỡ.
17. **09-2** · **Ildefonsus thành Toledo** — Q-ID, niên đại, tác phẩm · **tôi không tra Wikidata cho tên này**,
    và `CONTRIBUTING.md` quy tắc 1 cấm viết một cái tên vào atlas khi chưa tra · **ĐỪNG DÙNG vế đó như
    đang viết.** Bản đứng được là bỏ hẳn vế một và viết thẳng là không nêu được ứng viên cùng ô nào khác,
    theo đúng tiền lệ `CH04-CE04-03 · Wulfila`.
18. **10-1** · Cách đọc apoha theo quan hệ nhân quả có phải **của riêng** Pháp Xứng · SEP chỉ nói lối dựa
    vào nhân quả "seems to be entirely absent in Dignāga", đủ loại Trần-na nhưng không đủ loại mọi người khác ·
    câu thay thế viết "ông đọc lại", **không** viết "ông là người đầu tiên".
19. **11-3** · Chiều kế thừa thể chế Tạng ← Đường · không truy được nguồn; ngược lại một mạch truyền thống
    quy mô hình luật lệ và hành chính cho phía **Đột Quyết** · **bản khuyến nghị là chỉ sửa mức bằng chứng**
    (`tương đồng độc lập · trực tiếp`), không đổi loại quan hệ thành `kế thừa`.
20. **11-2** · Beckwith 1987 có đỡ đủ các mệnh đề còn lại của mục không · chỉ xác nhận được sách tồn tại và
    đúng chủ đề · dòng rào tôi đề xuất **không thay thế** việc tìm một nguồn sơ cấp thật cho thời ông.

**C. Nhiễu thư mục (ba ca, không ca nào thành phát hiện phải sửa)**

21. **Wechsler** *Mirror to the Son of Heaven* — mục ghi **1974**; bản ghi tra được có cả **1974** và **1975**.
    Library of Congress trả **HTTP 403** (đúng loại bẫy khối 13 liệt kê), không mở được trang bản quyền.
22. **Madelung** *The Succession to Muhammad* — mục ghi **1997**; bản ghi tra được có cả **1996** và **1997**.
23. **Tiesler & Cucina** *Janaab' Pakal of Palenque* — mục ghi **2006**; bản ghi tra được ghi **2005**
    (bản tiếng Tây Ban Nha **2004**). Ghi lại để vòng sau khỏi "sửa" thành 2005 mà tưởng là đính chính.

**D. Giới hạn của chính vòng rà này — phải đọc kèm mọi kết luận ở trên**

24. **Không mở được bất kỳ cuốn sách in nào.** Mọi kiểm nguồn dạng sách chỉ ở tầng **thư mục**
    (tồn tại · đúng tác giả · đúng nhà xuất bản · đúng năm · **đúng thể loại**) cộng với mô tả luận điểm
    ở những chỗ có tư liệu mở. Nguồn **duy nhất** được đọc tới nội dung là SEP "Dharmakīrti"
    (`CH05-CE07-10`), và đó cũng là nơi vòng này bắt được ca quy tắc 7 chắc chắn nhất. Hệ quả phải nói thẳng:
    **nếu còn ca quy tắc 7 nào khác trong nhóm CE07, vòng này nhiều khả năng không thấy nó** — vì để thấy
    phải biết sách đó lập luận gì, không chỉ nó nói về cái gì.
25. **Không chạy `build.py`.** Mọi kết luận về lint được rút từ việc đọc `atlaslib/lint.py`,
    `atlaslib/common.py` và `reports/lint-ch05.txt` đã có sẵn, cộng với việc tự đếm chữ bằng đúng công thức
    `len([w for w in s.split() if w])` của `lint.py`. Vòng Wikidata thì **có** chạy thật, qua
    `wbgetentities` cho cả 12 Q-ID.
26. **Không rà `## Ghi chú biên tập`.** Các khối 14–23 được đọc **làm đầu vào**, không làm đối tượng rà.
    Chỗ duy nhất tôi phán về chúng là khối 44 (con số 12/12) và khối 20 (dòng về số bản chép tay
    Etymologiae dặn "không được viết vào mục" trong khi mục **có** viết, và con số ấy lại kiểm được) —
    cả hai đều là **vênh giữa ghi chú và mục**, không phải lỗi của riêng bên nào, và cả hai nằm ngoài
    dòng 209–411 nên không vào bảng tổng.
