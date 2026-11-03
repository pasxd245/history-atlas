# Bình duyệt độc lập — VÒNG 2 — Chapter 5, nhóm CE08 (TK 8, 701–800 CN)

Phạm vi: `content/ch05.md` dòng 412–627 (12 mục `CH05-CE08-01`…`-12` + dòng **Bối cảnh** của nhóm).
Người rà **không** viết nhóm này và **không** thực hiện vòng 1.
Báo cáo ghi **tăng dần**: mỗi mục kiểm xong ghi ngay, không gom cuối.

## Vì sao có vòng 2, và nó đổi cách làm thế nào

Vòng 1 (`reports/ch05-ce08-review.md`) **đã ký ✓ cho một mệnh đề sai** (§B-14, câu "Khương Công Phụ đỗ đầu kỳ thi nhà Đường năm 780", trong khi *Tân Đường thư* q.152 chỉ chép 「第進士」 và 「以制策異等」). Vì vậy vòng này **không mượn chữ ký nào của vòng 1**: mọi mệnh đề đều được mở lại từ nguồn, kể cả những chỗ vòng 1 đánh ✓. Phần cuối báo cáo có một mục riêng liệt kê những chỗ vòng 1 ký ✓ mà vòng này thấy sai hoặc không kiểm được.

Lưu ý về trạng thái văn bản: **nhiều đề nghị của vòng 1 đã được áp dụng vào `content/ch05.md`** (Sibawayh "bộ mô tả cổ nhất", Đền IV "kim tự tháp cao nhất", lịch Đại Diễn "suốt phần còn lại của nhà Đường", "tổ tiên của mọi đồng hồ cơ", Charles Martel "không để lại thiết chế nào", "bốn phương án" → "ba phương án", `k. 683`, `k. 766`, trụ đá Kar-cun "con ông", tranh biện Samye hai chiều). Vòng này rà **văn bản hiện tại**, không rà bản vòng 1 đã đọc.

## Quy ước đánh dấu

- **BẮT BUỘC** — sai sự kiện, vi phạm quy tắc `CONTRIBUTING.md`, liên kết trỏ sai người, nguồn bị dẫn ngược, hoặc mâu thuẫn chéo trong cùng file.
- **NÊN** — đúng nhưng nói quá, thiếu chính xác, hoặc dễ gây hiểu nhầm.
- **CÂN NHẮC** — vấn đề quy ước / diễn đạt, không chặn.
- **[KHÔNG KIỂM ĐƯỢC]** — nêu rõ lý do, không đoán.

Mọi request mạng dùng `curl -A 'history-atlas/0.1 (research)'`. Không có thông tin cá nhân trong header/URL/payload/báo cáo.

---

## §0 · Bốn phép kiểm chạy một lần cho cả nhóm

### §0.1 · Trần chữ (`atlaslib/lint.py` WORD_TARGET: ideas ≤130, why ≤104, context ≤78)

Đếm bằng `len([w for w in s.split() if w])` trên đúng dải dòng 412–627. **Không mục nào vượt trần.**

| Mục | ideas | why |
|---|---|---|
| Bối cảnh nhóm | context = **58** / 78 | — |
| -01 Abu Muslim | 108 | 75 |
| -02 Al-Mansur | 95 | 77 |
| -03 Jaʿfar al-Sadiq | 107 | 76 |
| -04 Abu Hanifa | **126** | 81 |
| -05 Sibawayh | **127** | 84 |
| -06 Charlemagne | 119 | 88 |
| -07 Bêđa | 102 | 70 |
| -08 Tăng Nhất Hạnh | **129** | 72 |
| -09 Đỗ Phủ | 108 | 75 |
| -10 Trisong Detsen | 121 | **98** |
| -11 Ādi Shankara | 107 | 92 |
| -12 Yikʼin Chan Kʼawiil | 107 | 79 |

**CÂN NHẮC toàn nhóm — ba mục sát trần.** `-08` còn **1 chữ** dư, `-05` còn 3, `-04` còn 4. Mọi câu thay thế đề xuất bên dưới cho ba mục này đều được đếm lại và viết **ngắn hơn hoặc bằng** câu nó thay; chỗ nào không thể, tôi nói rõ phải cắt gì.

### §0.2 · Cổng Q-ID — tự chạy lại, không chép vòng 1

`wbgetentities&props=labels|claims&languages=en|vi`, HTTP 200.

| Mục | Q-ID | Nhãn en | P31 | P569 (rank/refs) | P570 (rank/refs) |
|---|---|---|---|---|---|
| -01 | Q335210 | Abu Muslim al Khorasani | Q5 | 718 p9 (1 ref) | 755-02 p10 (**0 ref**) |
| -02 | Q31066 | Al-Mansur | Q5 | 713-11 p10 **preferred**; 714 p9 | 775-10-07 p11 pref; 775-10-18 p11 |
| -03 | Q170046 | Jaafar Al-Sadiq | Q5 | 702-04-20 p11; 699 p9 | 765-12-16 p11 (0 ref); 765 p9 |
| -04 | Q190896 | Abū Ḥanīfa | Q5 | 699-09-05 p11 pref; 699 p9 | 767 p9 ×2 |
| -05 | Q983355 | Sibawayh | Q5 | 760 p9 | **797** p9 |
| -06 | Q3044 | (không có nhãn en) | Q5 | **5 phát biểu / 3 năm**: 748-04-02, 742, 747, 742-04-02, 742-04-10 | 814-01-28; 814-02-01 *deprecated* |
| -07 | Q154938 | Bede (vi: Bêđa) | Q5 | 672 p9 pref; 672; 673 | **735-05-25 p11 preferred, 2 refs**; 735; 734 |
| -08 | Q710705 | Yi Xing (vi: **Nhất Hạnh**) | Q5 | 683 p9 | 727 p9 |
| -09 | Q33772 | Du Fu (vi: Đỗ Phủ) | Q5 | 712 p9 (7 refs) | 770 p9 (7 refs) |
| -10 | Q366661 | Tri Songdetsen | Q5 | 742 ×2 | **4 giá trị**: 798, 797 pref (0 ref), 800, 797 |
| -11 | Q180967 | Ādi Shankara | Q5 | 788 p9 (4 refs) | 820 ×2 |
| -12 | Q2620151 | Yik'in Chan K'awiil | Q5 | (không có) | `somevalue` |

**Cả 12 Q-ID trỏ đúng người, cả 12 có `P31 = Q5`.** Không có ca "chi bướm". Kết luận này trùng vòng 1 nhưng được chạy lại độc lập, không chép.

Hai điểm bẫy Wikidata xác nhận được đúng như đề bài mô tả: `Q154938` (Bêđa) có `P570 = +0735-05-25` **precision 11, rank preferred, 2 tham chiếu** — tức `precision 11` ở đây đi cùng mục được chấm `Cao`; còn `Q2620151` khai `P570 = somevalue`, tức Wikidata **khẳng định có năm mất nhưng không biết là năm nào** — khớp với việc mục ghi `k. 766`.

### §0.3 · Quy tắc 6 — đối chiếu mọi tên trong thân mục CE08 với toàn bộ `content/*.md`

Tôi trích 285 dòng `### ` của cả 6 file (`ch01`–`ch05`, `ch90`), lấy tên chính trước dấu ngoặc, rồi dò ngược vào dải dòng 412–627. **Năm tên khớp, và không tên nào bị gọi là "ứng viên bị loại":**

| Tên có mục riêng | Xuất hiện ở | Cách gọi | Hợp quy tắc 6? |
|---|---|---|---|
| Muhammad (`CH05-CE07-01`) | -03 | "dòng dõi Muhammad" | ✔ không phải ứng viên bị loại |
| Pháp Xứng (`CH05-CE07-10`) | -11 | "ông trích Pháp Xứng", và có ID ở `Kế thừa từ:` | ✔ |
| Kʼinich Janaabʼ Pakal (`CH05-CE07-12`) | -12 | "**có mục riêng ở nhóm CE07**" | ✔ đúng câu chữ `CONTRIBUTING.md:51` |
| Vācaspati Miśra (`CH05-CE10-07`) | -11 | dẫn kèm ID | ✔ |
| Thích Nhất Hạnh (`CH90-CE19_20-10`) | -08 | "**người có mục riêng ở phụ lục**" | ✔ |

Và ngược lại: **cả 5 cái tên được nêu đích danh là "ứng viên bị loại" trong thân mục CE08 đều không có mục ở bất kỳ chapter nào, kể cả `ch90.md`** — kiểm bằng `grep '^### '` trên cả 6 file:

- Divashtich / Ḏēwaštīč (-01) — 0 mục
- Charles Martel (-06) — 0 mục
- Alcuin xứ York (-07) — 0 mục
- Lý Bạch (-09) — 0 mục; và mục viết ông ở dạng **chữ tự do**, không giả vờ có ID
- Liên Hoa Sinh / Padmasambhava (-10) — 0 mục

**Quy tắc 6 sạch ở tầng thân mục.** Ca Jayavarman II mà đề bài nêu nằm ở **ghi chú biên tập**, không ở thân mục, và đã được sửa ở đó ("Mười lăm ứng viên bị loại khi ấy, nay còn **mười bốn**…"). Tôi xác nhận `CH05-CE09-01` tồn tại và đúng là Jayavarman II.

### §0.4 · Mọi ID liên kết — mở đích ra đọc tên (lint chỉ kiểm tồn tại, `lint.py:151-152`)

| Mục | Liên kết | ID trỏ tới | Đúng người? |
|---|---|---|---|
| -01 Ảnh hưởng | `CH05-CE08-02` | Al-Mansur | ✔ |
| -02 Kế thừa | `CH05-CE08-01` | Abu Muslim al-Khurasani | ✔ |
| -03 Kế thừa | `CH05-CE07-03` | Ali ibn Abi Talib | ✔ (tổ bốn đời) |
| -03 Ảnh hưởng | `CH05-CE08-04` | Abu Hanifa | ✔ |
| -04 Kế thừa | `CH05-CE08-03` | Jaʿfar al-Sadiq | ✔ |
| -05 Kế thừa | `CH02-BCE05-08` | **Pāṇini** | ✔ |
| -06 Kế thừa | `CH04-CE05-01` | Augustinô thành Hippo | ✔ |
| -06 Kế thừa | `CH04-CE04-01` | **Constantinus I** | ✔ |
| -07 Kế thừa | `CH05-CE07-09` | Isiđôrô thành Seville | ✔ |
| -07 Kế thừa | `CH04-CE05-01` | Augustinô thành Hippo | ✔ |
| -09 Ảnh hưởng | `CH90-CE19_20-01` | **Nguyễn Du** | ✔ |
| -10 Kế thừa | `CH05-CE07-11` | Tùng Tán Cán Bố | ✔ |
| -11 Kế thừa | `CH05-CE07-10` | Pháp Xứng | ✔ |
| -11 (trong văn xuôi) | `CH05-CE10-07` | Vācaspati Miśra | ✔ |

**Không có ca trỏ sai người.** Đây là điểm vòng 1 cũng kết luận vậy; tôi mở lại từng đích và xác nhận độc lập.

---
## §A · Từng mục

### §A-00 · Dòng **Bối cảnh** của nhóm CE08 — dòng 413

**Đã kiểm được (không có phát hiện)**
- `context = 58 chữ` ≤ 78 ✔.
- "Một cuộc nổi dậy khởi từ Khurasan lật nhà Umayyad và dời trọng tâm thế giới Hồi giáo về Baghdad" ✔ (747–750; Baghdad 762).
- "Loạn An Lộc Sơn chặt đôi nhà Đường" ✔ (755–763).
- "Thổ Phồn lên đỉnh" ✔ (Trường An 763, hiệp ước 783).
- "ở Tây Âu người Frank dựng lại một ngôi hoàng đế" ✔ (25-12-800, nằm **trong** `group_range('CE08') = (701, 800)`).

**BẮT BUỘC — "Hai trường phái luật Sunni đầu tiên … thành hình" bị chính nguồn của mục `-04` bác, và mâu thuẫn với ghi chú biên tập của chính file.**

Nguyên văn câu sai (dòng 413):
> "Hai trường phái luật Sunni đầu tiên và ngữ pháp Ả Rập thành hình."

Ba chỗ cùng chỉ vào một kết luận:
1. **Nguồn**: Melchert, *The Formation of the Sunni Schools of Law, **9th–10th Centuries C.E.*** (Brill, 1997) — nguồn thứ nhất của `CH05-CE08-04` — lập luận rằng các trường phái **mang tên** các luật gia thế kỷ 8–9 **nhưng chưa vận hành sớm như vậy**; ông định niên các madhhab "cổ điển" Shāfiʿī, Ḥanafī, Ḥanbalī vào thời Ibn Surayj, al-Karkhī và al-Khallāl, tức **cuối thế kỷ 3 AH / 9 CN tới giữa thế kỷ 4 AH / 10 CN**. (Xác minh qua trang Brill của chính sách và mô tả nhà xuất bản; nhan đề và năm khớp đúng dòng `**Nguồn:**` của mục.)
2. **Ghi chú biên tập của chính file** (khối "Hình dạng của thế kỷ…") đã viết đúng điều đó: *"Bản thân các **trường phái** thì Melchert — nguồn mà `CH05-CE08-04` dẫn — đặt ở thế kỷ 9–10."*
3. Nên dòng Bối cảnh đang nói **ngược** cả nguồn lẫn ghi chú — đúng hình dạng quy tắc 7, và đồng thời là một mâu thuẫn chéo trong cùng file.

Vòng 1 **không kiểm dòng Bối cảnh ở đâu cả** (báo cáo vòng 1 không có mục nào cho nó: §A chỉ có A-01…A-12, §B chỉ về ghi chú biên tập). Đây là lỗ hổng phạm vi, không phải một chữ ký sai.

**Câu thay thế đề xuất (nguyên văn, đã đếm: 77 chữ ≤ 78):**
> "Một cuộc nổi dậy khởi từ Khurasan lật nhà Umayyad và dời trọng tâm thế giới Hồi giáo về Baghdad. Những người về sau được lấy tên đặt cho hai trường phái luật Sunni đầu tiên đang dạy ở Kufa và Medina; ngữ pháp Ả Rập thì thành hình trong thế kỷ này. Loạn An Lộc Sơn chặt đôi nhà Đường, Thổ Phồn lên đỉnh, và ở Tây Âu người Frank dựng lại một ngôi hoàng đế."

Soi lại chính câu thay thế: (a) "đang dạy ở Kufa và Medina" — Abu Hanifa dạy ở Kufa, Malik ibn Anas ở Medina, cả hai mất trong thế kỷ 8 (767 và 795); đây là mệnh đề về **người dạy**, không phải về **trường phái thành hình**, nên không còn đụng Melchert. (b) "ngữ pháp Ả Rập thì thành hình trong thế kỷ này" — `al-Kitāb` của Sibawayh soạn cuối thế kỷ 8, đúng mục `-05`, nên vế này đứng được. (c) Nếu Owner muốn ngắn hơn nữa, cắt mệnh đề "đang dạy ở Kufa và Medina" thì câu vẫn đứng.

---

### §A-01 · `CH05-CE08-01` Abu Muslim al-Khurasani — dòng 415–431

**Đã kiểm được (không có phát hiện)**
- `Q335210` = "Abu Muslim al Khorasani", `P31 = Q5` ✔ đúng người.
- `năm: k. 718–755 CN`; Wikidata `P569 = 718` (p9), `P570 = 755-02` (p10, **0 tham chiếu**). `độ tin cậy niên đại: Trung bình` (±25) hấp thụ được biên độ 718/719 vs 723/727 của nguồn cổ điển ✔.
- Trường `năm:` đúng dạng sinh–mất, không rơi vào `NON_BIO_YEARS_RE` ✔.
- "Năm 745 ông được phái từ Iraq về Khurasan" ✔ (745, đi cùng Qaḥṭaba ibn Shabīb).
- "Năm 747 ông giương cờ đen công khai" ✔ (pha công khai của cách mạng Abbasid khởi trong 747).
- "cuối năm ấy chiếm Merv, đánh bật tổng đốc Umayyad Nasr ibn Sayyar" ✔ — Merv rơi **tháng 12-747 (hoặc tháng 1-748)**; "cuối năm ấy" nằm trong khung ấy. (Một dòng khác ghi 14-02-748 / Jumādā II 130; xem CÂN NHẮC.)
- "Divashtich thua trận năm 722" ✔, nhất quán với khối ghi chú Divashtich.
- "trọng tâm chính trị của thế giới Hồi giáo dịch vĩnh viễn từ Syria về Iraq" ✔.
- `lĩnh vực: Chính trị/Nhà nước, Quân sự` — 2 giá trị, đều trong `FIELDS` ✔. `vùng: Trung Á` — Merv/Khurasan, đúng quy ước `vùng:` 1 (nơi hoạt động chính) ✔. `câu hỏi lớn: Không áp dụng` ✔.
- Quy tắc 6: **Divashtich không có mục ở bất kỳ chapter nào, kể cả `ch90.md`** ✔ (grep `^### ` trên cả 6 file).
- Liên kết `CH05-CE08-02` trỏ đúng **Al-Mansur** ✔.
- Nguồn 1: Moshe Sharon, *Black Banners from the East: The Establishment of the ʿAbbāsid State* (Magnes Press, 1983) — **có thật**, đúng tác giả, đúng nhà xuất bản, đúng năm; nhan đề đầy đủ còn có đuôi "—Incubation of a Revolt" (Max Schloessinger Memorial Series, monograph 2). Nguồn 2: Elton L. Daniel, *The Political and Social History of Khurasan under Abbasid Rule, 747–820* (Bibliotheca Islamica, 1979) — có thật, và **khung niên đại trong nhan đề (747–820) phủ đúng mệnh đề nó đỡ** ✔ (phép thử quy tắc 7).

**CÂN NHẮC (1) — "cuối năm ấy chiếm Merv" chọn một trong hai dòng niên đại mà không nói là có hai.**
> "Năm 747 ông giương cờ đen công khai, và cuối năm ấy chiếm Merv, đánh bật tổng đốc Umayyad Nasr ibn Sayyar."

Hai dòng cùng lưu hành: tháng 12-747 / tháng 1-748, và 14-02-748 (Jumādā II 130). Không sai, nhưng là một lựa chọn im lặng. Vì `ideas` của mục chỉ dùng 108/130 chữ nên có chỗ nói ra.

**Câu thay thế đề xuất:** *"Năm 747 ông giương cờ đen công khai, và trong vòng vài tháng chiếm Merv, đánh bật tổng đốc Umayyad Nasr ibn Sayyar."* — "trong vòng vài tháng" đúng với **cả hai** dòng niên đại, nên không phải chọn phe. (+1 chữ; `ideas` 108 → 109, còn xa trần 130.)

**CÂN NHẮC (2) — "Trong ba năm" đếm từ mốc không được nêu.**
> "Trong ba năm, một cuộc nổi dậy ở rìa đông lật được triều đình ở trung tâm"

Đếm từ cờ đen (747) tới khi Marwan II đổ (750) là đúng ba năm; nhưng câu đứng ngay sau mệnh đề về Merv, nên dễ đọc thành "ba năm kể từ 745", khi đó là năm năm. Vòng 1 đã nêu và **mục chưa sửa**. Đề xuất: *"Từ lúc giương cờ tới khi nhà Umayyad sụp năm 750 là chưa đầy ba năm."*

**CÂN NHẮC (3) — `trực tiếp` cho một quan hệ không phải người-với-người.**
> "Cuộc vận động ngầm Hāshimiyya của dòng Abbas ở Kufa · kế thừa · trực tiếp"

Đích là một **phong trào**, không phải một người. Đây đúng loại "mức bằng chứng thổi phồng" mà lint mù. Không sai từ vựng (`EVIDENCE_LEVELS` không nói gì về chủ thể), nhưng nếu Owner muốn giữ `trực tiếp` chỉ cho quan hệ có bằng chứng văn bản cụ thể thì ca này phải xuống `qua trường phái`. Cùng hình dạng: `-04` "…và bộ luật Hanafī · trực tiếp", `-10` "Chương trình dịch kinh điển Phật giáo sang tiếng Tạng · trực tiếp", `-12` "Calakmul, qua thế đối đầu kéo dài · phản bác · trực tiếp". Xem §C-2.

---
### §A-02 · `CH05-CE08-02` Al-Mansur — dòng 432–448

**Đã kiểm được (không có phát hiện)**
- `Q31066` = "Al-Mansur", `P31 = Q5` ✔.
- "Al-Saffah lên ngôi trước" ✔ (749–754, anh ông).
- "Hai mươi mốt năm cầm quyền" ✔ (754–775).
- "một quyết định năm 762: dựng kinh đô mới Madinat al-Salam" ✔; "thành tròn xây từ đất trống" ✔.
- "Abu Muslim bị ông xử tử năm 755" ✔.
- `lĩnh vực: Chính trị/Nhà nước` (1) ✔; `vùng: Trung Đông/Bắc Phi` ✔ (Kufa/Baghdad, quy ước 1); `câu hỏi lớn: Không áp dụng` ✔.
- Liên kết `CH05-CE08-01` trỏ đúng **Abu Muslim** ✔.
- Quy tắc 6: mục **không nêu ứng viên bị loại nào** — không có gì để vi phạm ✔.
- Nguồn 1: Hugh Kennedy, *The Early Abbasid Caliphate: A Political History* (Croom Helm, 1981) — có thật, đúng tác giả/nhà xuất bản/năm, và **khung chủ đề phủ đúng al-Mansur** ✔.

**BẮT BUỘC — "Abu Hanifa chết năm 767 khi đang bị ông giam" mâu thuẫn trực tiếp với mục `-04` trong cùng nhóm.**

Nguyên văn câu sai (dòng 438):
> "Abu Hanifa chết năm 767 khi đang bị ông giam."

Mục `CH05-CE08-04`, cách đó **29 dòng**, viết về đúng sự việc ấy:
> "…và **truyền thống chép** ông chết trong ngục Baghdad — Melchert đọc chi tiết ấy là truyền thuyết thánh hoá đời sau."

Tức cùng một file, cùng một nhóm: mục `-04` đánh dấu đây là **tường thuật truyền thống bị học giới đọc lại**, mục `-02` khẳng định nó như **dữ kiện**. Một trong hai phải nhường. Vì hướng thận trọng nằm ở `-04`, `-02` là chỗ phải sửa.

**Câu thay thế đề xuất (nguyên văn):**
> "Ba mục trong nhóm này nối với nhau bằng một người: Abu Muslim bị ông xử tử năm 755, Abu Hanifa chết ở Baghdad năm 767, theo truyền thống là trong ngục của ông."

Soi lại câu thay thế: "chết ở Baghdad năm 767" là phần không ai tranh cãi; "theo truyền thống là trong ngục của ông" đánh dấu đúng tầng tư liệu. (`why` 77 → 79 chữ, còn xa trần 104.) Nếu muốn ngắn hơn, cắt mệnh đề sau dấu phẩy thì câu vẫn đứng và vẫn đúng.

**BẮT BUỘC — năm sinh "709" không kiểm được, và nó được nhập nguyên từ câu thay thế của vòng 1.**

Nguyên văn câu (dòng 438):
> "Niên đại ghi Trung bình vì các nguồn cho ba năm sinh khác nhau: 709, 713 và 714."

Kiểm được: `Q31066` có `P569 = 713-11` (p10, **preferred**) và `714` (p9) — tức **hai** giá trị, cả hai quy đổi từ **95 AH** (Ṣafar 95 = tháng 11-713; 95 AH chạy từ tháng 10-713 tới tháng 9-714). Nguồn tham chiếu phổ thông và nguồn chuyên ngành tôi mở được đều chỉ cho 95/713–4.

**[KHÔNG KIỂM ĐƯỢC] — con số 709.** Tôi tìm bằng ba truy vấn khác nhau (kể cả truy theo "101 AH" và "c. 709") và không thấy dòng học thuật nào cho 709. Không loại trừ nó có trong một nguồn cổ điển tôi không mở được; nhưng nó **chưa được dẫn nguồn ở đâu trong repo**.

Đáng ghi về quy trình: câu này không phải của người viết mục. Vòng 1 (§A-02) đề nghị nguyên văn *"Niên đại ghi Trung bình vì năm sinh không chắc — các nguồn cho 709, 713 và 714"* trong khi **chính vòng 1 vừa đánh dấu `[KHÔNG KIỂM ĐƯỢC]` cho con số "ba" ở câu cũ**; rồi tự nó đưa ra một bộ ba mới, trong đó phần tử "709" không kèm nguồn. Mục đã chép nguyên câu ấy vào. Đây đúng là cái mà đề bài gọi là *"câu thay thế còn mang đúng cái lỗi nó vừa chẩn"*.

**Câu thay thế đề xuất (nguyên văn):**
> "Niên đại ghi Trung bình vì năm sinh 95 AH được quy đổi khi thì 713, khi thì 714."

Soi lại câu thay thế: mệnh đề duy nhất trong đó — 95 AH ↔ 713/714 — là phép quy đổi lịch kiểm được, và khớp đúng hai giá trị `P569` của `Q31066`. Nó **không** còn mang con số chưa kiểm được nào. (`why` giữ trong trần: 77 → 79 nếu áp cả hai câu thay thế ở mục này.)

**NÊN — nguồn thứ hai gần như chắc chắn không nói về nhân vật của mục, và lập trường của nó ngược chiều cách mục dùng nó (quy tắc 7).**

> "**Nguồn:** … Tayeb El-Hibri, Reinterpreting Islamic Historiography (Cambridge University Press, 1999)."

Hai vấn đề chồng lên nhau:
1. **Phạm vi.** Nhan đề đầy đủ là *Reinterpreting Islamic Historiography: **Hārūn al-Rashīd and the Narrative of the ʿAbbāsid Caliphate***, và mục lục mà nhà xuất bản công bố là: 1. Historical background and introduction · 2. **Harun al-Rashid** · 3. **Al-Amin** · 4. **Al-Ma'mun** · 5. The structure of civil war narratives. **Không chương nào về al-Mansur.** Đây là đúng cái mà `CONTRIBUTING.md` mục 2 của "hai việc bắt buộc" cảnh báo: nguồn tồn tại, đúng chủ đề rộng, nhưng chưa chắc **nói về nhân vật**.
2. **Lập trường.** Luận điểm trung tâm của El-Hibri là các tường thuật Abbasid **không phải ghi chép sự kiện** mà là văn bản văn chương/đạo lý. Mục `-02` lại dùng nó để đỡ một chuỗi mệnh đề sự kiện (21 năm cầm quyền, quyết định 762, vị trí địa lý). Dùng một công trình hoài nghi tường thuật để chứng thực tường thuật là hình dạng quy tắc 7.

**[KHÔNG KIỂM ĐƯỢC]** — trang Cambridge của sách trả **HTTP 403**, nên tôi **không mở được mục lục đầy đủ**; danh sách chương trên lấy từ mô tả nhà xuất bản được trích lại. Vì vậy tôi **không khẳng định** El-Hibri hoàn toàn không nhắc al-Mansur (chương 1 là "Historical background"), chỉ khẳng định **không có chương nào dành cho ông**.

**Đề xuất (nguyên văn dòng `**Nguồn:**`):**
> "**Nguồn:** Hugh Kennedy, The Early Abbasid Caliphate: A Political History (Croom Helm, 1981); Jacob Lassner, The Shaping of ʿAbbāsid Rule (Princeton University Press, 1980)."

Soi lại chính đề xuất này: **[KHÔNG KIỂM ĐƯỢC]** — tôi xác minh được Lassner là tác giả đúng chủ đề (ông cũng viết *Islamic Revolution and Historical Memory*, American Oriental Society, 1986, mà tôi mở được thư mục), nhưng **chưa mở được trang thư mục xác nhận nhan đề/nhà xuất bản/năm của *The Shaping of ʿAbbāsid Rule***. **Đừng chép đề xuất này vào file khi chưa tra.** Phương án an toàn tuyệt đối, không cần tra thêm gì: **giữ nguyên Kennedy 1981 và bỏ El-Hibri**, vì Kennedy một mình đã đỡ được mọi mệnh đề sự kiện của mục.

**CÂN NHẮC — "giữ vai trung tâm của thế giới Hồi giáo suốt năm thế kỷ".**
762–1258 đúng là ~5 thế kỷ nếu đo bằng danh nghĩa caliph, nhưng quyền lực chính trị thật của Baghdad mất từ 945 (Buyid vào thành). Không sai, là cách đọc rộng tay. Vòng 1 cũng ghi nhận và mục chưa đổi.

---
> **Đính chính của chính vòng này, ghi ngay thay vì sửa lùi:** sau khi viết đoạn trên tôi đã tra được Lassner. **Jacob Lassner, *The Shaping of ʿAbbāsid Rule*, Princeton University Press, 1980** (Princeton Studies on the Near East, xvii+328 tr., ISBN 0-691-05281-6) — **tồn tại, đúng tác giả, đúng nhà xuất bản, đúng năm**, và nội dung là quá trình phong trào cách mạng Abbasid biến thành chính quyền đế chế trong những năm định hình, tức **đúng mệnh đề mục `-02` cần đỡ**. Dấu `[KHÔNG KIỂM ĐƯỢC]` ở đoạn trên vì vậy được **gỡ**: đề xuất thay El-Hibri bằng Lassner 1980 nay đã kiểm được đầy đủ.

---
### §A-03 · `CH05-CE08-03` Jaʿfar al-Sadiq — dòng 449–466

**Đã kiểm được (không có phát hiện)**
- `Q170046` = "Jaafar Al-Sadiq" (nhãn vi "Ja'far al-Sadiq"), `P31 = Q5` ✔.
- `năm: k. 702–765 CN`; `P569` 702-04-20 và 699; `P570` 765-12-16 và 765. Biên độ sinh 699–702 ⇒ `Trung bình` (±25) ✔.
- "người Shiʿa Twelver và Ismaʿili coi ông là Imam thứ sáu" ✔.
- "giới Sunni coi ông là người truyền hadith đáng tin" ✔.
- "cả Abu Hanifa lẫn Malik ibn Anas đều được ghi là học trò ông" ✔ — xác minh được: ông được chép là người truyền cho cả hai, đúng cách mục viết ("**được ghi là**", không viết "là").
- "Số truyền ngôn quy cho Jaʿfar nhiều hơn tổng các Imam khác cộng lại, nhưng chính việc quy ấy đang bị giới nghiên cứu đặt dấu hỏi" ✔ — **cả hai vế** kiểm được, kể cả vế hoài nghi. Đây là chỗ viết đúng tầng tư liệu.
- "giữa một thế kỷ đầy khởi nghĩa nhân danh dòng dõi Muhammad, ông đứng ngoài tất cả" ✔ (Zayd 740, al-Nafs al-Zakiyya 762).
- "các bộ rijāl Shiʿa thì không bộ nào nhắc tới Jabir" ✔ — nhất quán với khối ghi chú Jabir (al-Barqī, al-Kashshī, al-Najāshī, al-Ṭūsī).
- `lĩnh vực: Tôn giáo/Tâm linh, Luật` (2) ✔; `vùng: Trung Đông/Bắc Phi` ✔; `câu hỏi lớn: Con người` ✔; `Ảnh hưởng tới:` 3 mục = đúng trần ✔.
- Liên kết: `CH05-CE07-03` → **Ali ibn Abi Talib** ✔ đúng người; `CH05-CE08-04` → **Abu Hanifa** ✔.
- Quy tắc 6: mục không nêu ứng viên bị loại nào ✔. Muhammad (`CH05-CE07-01`) được nhắc nhưng ở cụm "dòng dõi Muhammad", không phải tư cách ứng viên ✔.
- Nguồn 1: Robert Gleave, "Jaʿfar al-Ṣādiq", *Encyclopaedia of Islam THREE* (Brill) — tác giả, mục từ và bộ bách khoa đều có thật, đúng chuyên môn (Gleave là chuyên gia luật học Shiʿa). Nguồn 2: Amir-Moezzi, *The Divine Guide in Early Shiʿism* (SUNY Press, 1994) — có thật, và **lập trường của nó (truyền thống Imam sơ kỳ là tầng bí truyền được dựng về sau) cùng chiều với cách mục dùng nó**, không ngược ✔.

**NÊN — mục tự đặt một kỷ luật rồi hai liên kết của chính nó phá kỷ luật ấy.**

Nguyên văn (dòng 455 và 464):
> "…nên không viết 'Jaʿfar dạy rằng X' từ các tuyển tập hadith."
> "Malik ibn Anas và trường phái Medina · kế thừa · **trực tiếp**"

Quan hệ thầy–trò Jaʿfar → Malik **chính là** một mệnh đề của truyền thống, cùng tầng tư liệu với những truyền ngôn mà mục vừa từ chối dùng. Gắn `trực tiếp` cho nó là nâng một mệnh đề truyền thống lên mức bằng chứng cao nhất của atlas, trong khi câu văn xuôi ngay trên đó nói không được làm vậy. Vòng 1 đã nêu (CÂN NHẮC) và mục chưa đổi; tôi xếp nặng hơn vì nó là **mâu thuẫn nội tại của chính mục**, không phải một lựa chọn từ vựng.

**Đề xuất (nguyên văn dòng liên kết):**
> "- Malik ibn Anas và trường phái Medina · kế thừa · qua trường phái"

Soi lại đề xuất: `qua trường phái` nằm trong `EVIDENCE_LEVELS` ✔, không đổi số liên kết (vẫn 3 ≤ 3) ✔, không đụng trần chữ (dòng liên kết không tính vào `ideas`/`why`) ✔, và nó mô tả đúng cái ta có — một mối liên hệ do truyền thống trường phái ghi lại.

**CÂN NHẮC — `Ali ibn Abi Talib · kế thừa · trực tiếp`, hình dạng quy tắc 8.**
Ali mất **661**, Jaʿfar sinh **k. 702**: hai người cách nhau 41 năm, không thể gặp nhau; `trực tiếp` ở đây nghĩa là "dòng truyền Imam", không phải tiếp xúc. `CONTRIBUTING.md` quy tắc 8 cảnh báo đúng hình dạng này và lint không bắt được. Nhóm CE08 dùng `trực tiếp` cho **ít nhất bốn cặp không cùng thời** (Ali→Jaʿfar, Isiđôrô→Bêđa, Gauḍapāda→Shankara, Pháp Xứng→Shankara). Vòng 1 đã đề nghị Owner viết quy ước này thành văn; **đề nghị ấy vẫn chưa có trong `CONTRIBUTING.md`** (tôi đọc lại toàn file: mục 8 chỉ cảnh báo, không định nghĩa `trực tiếp`). Xem §C-2.

**CÂN NHẮC — "Chính lựa chọn ấy biến Shiʿa giáo thành một truyền thống học thuật sống được dưới các triều đại thù địch" là diễn giải, viết như kết quả.**
Mệnh đề nền (Jaʿfar không tham gia khởi nghĩa) kiểm được; mệnh đề nhân quả thì là một cách đọc của học giới, không phải dữ kiện. Mục đã rất kỷ luật ở phần "Vì sao chọn" nên chỗ này lệch tông. Không chặn.

---

### §A-04 · `CH05-CE08-04` Abu Hanifa — dòng 467–483

**Đã kiểm được (không có phát hiện)**
- `Q190896` = "Abū Ḥanīfa" (nhãn vi "Abu Hanifa"), `P31 = Q5` ✔.
- `năm: k. 699–767 CN`; `P569` 699-09-05 (preferred) và 699; `P570` 767 ×2 ✔. `Trung bình` ✔.
- "ông chưa bao giờ làm quan toà" ✔ — đây là phần không bị tranh cãi.
- Ba thuật ngữ `qiyās` / `istiḥsān` / `raʾy` định nghĩa đúng; mô tả `istiḥsān` ("chọn giải pháp hợp lý hơn khi loại tỷ cho kết quả cứng nhắc") là định nghĩa chuẩn ✔.
- "Trường phái Hanafī … trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi" ✔.
- `vùng: Trung Đông/Bắc Phi` ✔ đúng quy ước 1, **và mục tự viết ra lý do** — cách xử lý mẫu mực. Mệnh đề "nguồn nói ông **gốc** Trung Á" khớp đúng khối ghi chú biên tập ("gốc gác Trung Á nhưng sinh và hoạt động cả đời ở Kufa") — **không còn mâu thuẫn chéo** mà vòng 1 từng báo (vòng 1 đọc bản ghi chú cũ ghi "sinh ở Trung Á"; bản hiện tại đã sửa).
- "Niên đại Trung bình vì các nguồn cổ điển cho nhiều năm sinh khác nhau" ✔ — viết "nhiều" thay vì một con số là cách đúng khi chưa tra được bảng; đối lập với ca "709" ở `-02`.
- `lĩnh vực: Luật, Tôn giáo/Tâm linh` (2) ✔; `câu hỏi lớn: Con người` ✔.
- Liên kết `CH05-CE08-03` → **Jaʿfar al-Sadiq** ✔.
- Quy tắc 6: mục không nêu ứng viên bị loại nào ✔.
- Nguồn 2: Wael B. Hallaq, *The Origins and Evolution of Islamic Law* (Cambridge University Press, 2005) — có thật, đúng tác giả/nhà xuất bản/năm ✔.

**NÊN + [KHÔNG KIỂM ĐƯỢC] — mục gán cho Melchert một cách đọc cụ thể mà không vòng nào mở sách ra xác nhận.**

Nguyên văn câu (dòng 471):
> "…và truyền thống chép ông chết trong ngục Baghdad — **Melchert đọc chi tiết ấy là truyền thuyết thánh hoá đời sau**."

Tôi tra bốn truy vấn khác nhau và **không tìm được đoạn nào của Melchert đọc chuyện ngục tù / cái chết trong ngục như thánh truyện**. Cái tôi xác minh được chỉ là lập trường chung của Melchert 1997 — rằng các madhhab chưa vận hành ở thế kỷ 8 — chứ **không** phải một phán đoán về mạch truyện tử đạo. *Encyclopaedia Iranica* (mục ABŪ ḤANĪFA), nơi có thể chốt việc này, trả **HTTP 403** cả qua `curl` lẫn qua fetch, nên **[KHÔNG KIỂM ĐƯỢC]**.

Về xuất xứ: câu này cũng **không phải của người viết mục**. Vòng 1 (§A-04) đề nghị nguyên văn *"giới nghiên cứu hiện nay đọc mạch truyện ấy như lớp thánh truyện của trường phái"* và nêu đích danh Melchert làm chỗ dựa — trong khi **chính vòng 1 ghi rằng nó không có bản Melchert để mở** (§A-11 vòng 1 thừa nhận cùng kiểu giới hạn với Nakamura). Đây là `CONTRIBUTING.md` mục 3 ở dạng khác: **đừng ghi một phán đoán cụ thể cho một tác giả cụ thể nếu chưa mở sách**.

**Câu thay thế đề xuất (nguyên văn, đã đếm: 39 chữ, thay cho 42 chữ ⇒ `ideas` 126 → 123):**
> "Ông chưa bao giờ làm quan toà: truyền thống chép ông bị tù dưới cả Umayyad lẫn Abbasid vì từ chối chức qāḍī và chết trong ngục Baghdad — một mạch tường thuật không có nguồn đương thời đỡ."

Soi lại câu thay thế: (a) nó **không gán phán đoán cho ai**, nên không lặp lại lỗi vừa chẩn; (b) "không có nguồn đương thời đỡ" là mệnh đề âm tính kiểm được — nguồn sớm nhất cho mạch truyện này là các từ điển tiểu sử thế kỷ 9 trở đi, không có văn bản thế kỷ 8; (c) nó **mở rộng dấu hiệu "truyền thống chép" ra cả hai lần tù**, chứ bản gốc chỉ hedge cái chết mà khẳng định hai lần tù như dữ kiện. Nếu Owner thấy vế cuối vẫn nặng, cắt từ dấu gạch ngang trở đi thì câu vẫn đứng và vẫn đúng (28 chữ).

**NÊN — quy tắc 7: chuỗi nhân quả của mục gán cho người được lấy tên đúng cái mà nguồn của mục gán cho thế hệ sau.**

Nguyên văn (dòng 471 và 473):
> "Nhưng cách làm luật ông để lại … cho phép một hệ luật sinh ra ở Ả Rập làm việc được trong những xã hội không Ả Rập. **Trường phái Hanafī vì thế trải từ** Trung Á và Nam Á tới Anatolia, Balkan và châu Phi."
> "…người bị caliph bỏ tù lại **định khuôn luật** cho phần lớn thần dân của các caliph về sau."

Melchert 1997 — **nguồn thứ nhất của chính mục** — lập luận rằng các trường phái mang tên các luật gia thế kỷ 8 **chưa vận hành** khi ấy, và định hình trường phái Ḥanafī "cổ điển" vào thời **al-Karkhī** (cuối thế kỷ 3 AH / 9 CN – giữa thế kỷ 4 AH / 10 CN). Chữ "vì thế" và chữ "định khuôn" đang nối thẳng người được lấy tên với một thiết chế mà nguồn đặt ở hai thế kỷ sau. Mức độ nhẹ hơn dòng Bối cảnh (§A-00) vì mục nói về **cách làm luật** chứ không nói trường phái thành hình ở thế kỷ 8 — nhưng cùng một hướng lệch.

**Câu thay thế đề xuất (nguyên văn, thay đúng một câu, 24 chữ thay cho 20 ⇒ `ideas` 123 → 127 nếu áp **cùng lúc** với câu trên; vẫn ≤ 130):**
> "Trường phái Hanafī mang tên ông — dù chính nó chỉ thành hình ở thế kỷ 9–10 — trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi."

Soi lại câu thay thế: mệnh đề chèn vào ("chỉ thành hình ở thế kỷ 9–10") **là mệnh đề của chính nguồn mục đang dẫn**, nên nó sửa lỗi quy tắc 7 bằng chính Melchert chứ không bằng một nguồn mới chưa kiểm. **Cảnh báo trần chữ:** nếu Owner áp **cả hai** câu thay thế của mục này thì `ideas` = 127/130 — còn 3 chữ. Nếu muốn an toàn hơn, bỏ cụm "mang tên ông" (⇒ 125).

---
> **Đính chính của chính vòng này, §A-04 — tôi vừa suýt mắc đúng lỗi mình đang bắt.** Phép đếm trong đoạn trên **sai**: câu gốc "Trường phái Hanafī vì thế trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi." là **18 chữ**, không phải 20; và câu thay thế tôi đề xuất là **31 chữ**, không phải 24. Áp **cả hai** câu thay thế của mục `-04` sẽ cho `ideas` = 126 − 3 + 13 = **136 chữ, VƯỢT TRẦN 130** và lint sẽ cảnh báo. Đếm lại bằng `len([w for w in s.split() if w])`:
>
> | phương án câu cuối | số chữ | `ideas` nếu áp cùng câu mở mới |
> |---|---|---|
> | giữ nguyên câu gốc | 18 | **123** ✔ |
> | "Trường phái Hanafī mang tên ông — dù chính nó chỉ thành hình ở thế kỷ 9–10 — trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi." | 31 | **136** ✗ vượt trần |
> | **"Trường phái Hanafī, thành hình ở thế kỷ 9–10, trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi."** | 22 | **127** ✔ |
> | "Trường phái mang tên ông, thành hình ở thế kỷ 9–10, trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi." | 24 | **129** ✔ (sát trần) |
>
> **Câu thay thế được rút lại và thay bằng (nguyên văn):**
> > "Trường phái Hanafī, thành hình ở thế kỷ 9–10, trải từ Trung Á và Nam Á tới Anatolia, Balkan và châu Phi."
>
> Phương án này giữ nguyên mệnh đề của Melchert, bỏ chữ "vì thế" (chính là chữ tạo ra chuỗi nhân quả sai), và để `ideas` ở **127/130**. Nếu Owner muốn biên an toàn hơn, chỉ áp câu mở mới và bỏ riêng hai chữ "vì thế" ở câu cuối ⇒ `ideas` = **121**.

---
### §A-05 · `CH05-CE08-05` Sibawayh — dòng 484–501

**Đã kiểm được (không có phát hiện)**
- `Q983355` = "Sibawayh", `P31 = Q5` ✔.
- `năm: k. 760 – k. 796 CN`, `độ tin cậy niên đại: Thấp` ⇒ `DATE_TOLERANCE["Thấp"] = None`, lint không đối chiếu ✔. Lựa chọn `Thấp` **đúng vì lý do đúng**: hai khung chết thực sự loại trừ nhau — **161 AH / 777 CN ở Basra** so với **177–180 AH / 793–796 CN ở làng al-Bayḍāʾ gần Shiraz**, lệch 19 năm **và khác nơi chết**. Xác minh được. "k. 796" khớp dòng 180 AH.
- "Al-Kitāb … mô tả tiếng Ả Rập một cách hệ thống — âm, hình thái, cú pháp, và cả biến thể vùng miền" ✔.
- "vào đúng lúc thứ tiếng ấy đang thành ngôn ngữ hành chính và học thuật của một đế quốc trải từ Iberia tới Sindh" ✔.
- "Sách không mang tên do chính ông đặt; đời sau gọi nó là 'Quyển sách'" ✔.
- Chân dung tiểu sử nghèo nàn (tên ʿAmr ibn ʿUthmān, tới Baghdad, cãi nhau, bị làm nhục, về một thị trấn Ba Tư, chết trẻ) ✔ khớp mạch *al-masʾala al-zunbūriyya*.
- `lĩnh vực: Ngôn ngữ học` (1) ✔; `vùng: Trung Đông/Bắc Phi` ✔ — và trường `nơi:` ghi "gốc vùng Shiraz, Iran" mà **không** để gốc gác kéo `vùng:` đi, đúng quy ước 1.
- Liên kết `CH02-BCE05-08` → **Pāṇini** ✔ đúng người; `tương đồng độc lập · suy đoán học giả` — mức bằng chứng thấp nhất, đúng với tình trạng tranh luận về môi giới Ba Tư.
- Al-Khalil ibn Ahmad al-Farahidi · `trực tiếp` ✔ (thầy thật của ông); Yunus ibn Habib · `trực tiếp` ✔.
- Quy tắc 6: mục không nêu ứng viên bị loại nào ✔.
- Nguồn 1: M.G. Carter, *Sībawayhi* (I.B. Tauris, 2004) — **có thật**, Makers of Islamic Civilization, viii+159 tr., London/New York, I.B. Tauris & Oxford University Press, 2004 ✔. Nguồn 2: Kees Versteegh, *The Arabic Linguistic Tradition* (Routledge, 1997) ✔.

**CÂN NHẮC — phép so sánh với ngữ pháp Hy Lạp–Latin là một mệnh đề mới chưa được kiểm, và nó do vòng 1 đưa vào.**

Nguyên văn (dòng 488):
> "…khác các sách ngữ pháp Hy Lạp và Latin còn lại, al-Kitāb không bị công trình nào trong truyền thống của nó thay thế, mà thành văn bản mọi nhà ngữ pháp Ả Rập về sau phải chú giải hoặc phản bác."

Vế "al-Kitāb không bị thay thế" ✔ đúng. Vế so sánh thì không chắc: *Ars minor/Ars maior* của Donatus và *Institutiones grammaticae* của Priscianus **cũng** không bị thay thế trong truyền thống của chúng — chúng là sách giáo khoa chuẩn của châu Âu Latin suốt gần một nghìn năm, tới tận các ngữ pháp nhân văn chủ nghĩa thời Phục hưng. Nói "khác các sách ngữ pháp Hy Lạp và Latin còn lại" vì thế dựng một tương phản mà bản thân nó phải được chứng minh.

Đáng ghi về quy trình: đây **chính là câu thay thế của vòng 1**. Vòng 1 bắt đúng một superlative sai ("bộ mô tả ngôn ngữ còn nguyên vẹn cổ nhất ngoài truyền thống Pāṇini") và nêu đích danh Donatus, Priscianus, Dionysius Thrax để bác — rồi **câu thay thế của nó lại dùng chính ba tác phẩm ấy làm vế đối lập**, theo chiều ngược với dữ kiện nó vừa trình bày. Mục đã chép nguyên câu ấy vào file.

**Câu thay thế đề xuất (nguyên văn, 47 chữ thay cho 58 ⇒ `ideas` 127 → 116):**
> "Nó vẫn là mốc quy chiếu của ngữ pháp Ả Rập sau mười hai thế kỷ: al-Kitāb không bị công trình nào trong truyền thống của nó thay thế, mà thành văn bản mọi nhà ngữ pháp Ả Rập về sau phải chú giải hoặc phản bác."

Soi lại câu thay thế: nó **bỏ hẳn phép so sánh liên truyền thống** thay vì đảo chiều nó — tức không thay một mệnh đề chưa kiểm bằng một mệnh đề chưa kiểm khác. Mọi vế còn lại đều là mệnh đề về chính truyền thống Ả Rập, kiểm được qua Carter và Versteegh. Và nó nới `ideas` từ 127 xuống 116, tức trả lại 11 chữ cho mục sát trần thứ hai của nhóm.

**CÂN NHẮC — "Al-Mubarrad và toàn bộ ngữ pháp Ả Rập về sau · kế thừa · trực tiếp".**
Al-Mubarrad (mất 898) chú giải *al-Kitāb*, nên `trực tiếp` đúng cho vế đầu; nhưng vế "**toàn bộ** ngữ pháp Ả Rập về sau" là một đích không xác định, và `trực tiếp` gánh cả nó. Nếu tách thành hai dòng thì `Ảnh hưởng tới:` lên 3 mục, vẫn trong trần.

---

### §A-06 · `CH05-CE08-06` Charlemagne — dòng 502–520

**Đã kiểm được (không có phát hiện)**
- `Q3044`, `P31 = Q5` ✔ (entity không có nhãn `en`/`vi`, nhưng là đúng thực thể Charlemagne — xác minh qua `P22 → Q81212` Pepin Lùn).
- `năm: k. 748–814 CN` + `Trung bình`: `P569` có **5 phát biểu / 3 năm phân biệt (742, 747, 748)**, biên độ 6 năm > `DATE_TOLERANCE["Cao"] = 5` và ≪ 25 ⇒ nấc `Trung bình` đúng ✔. Con số hiển thị 748 khớp phát biểu `preferred` 748-04-02.
- "Vua người Frank từ năm 768" ✔; "diệt vương quốc Lombard năm 774" ✔; "thu phục Bavaria năm 788" ✔ (phế Tassilo III); "phá liên minh Avar trong các chiến dịch 791–796" ✔.
- "Ngày 25 tháng 12 năm 800, giáo hoàng Lêô III phong ông làm hoàng đế" ✔ — và 800 **nằm trong** `group_range('CE08') = (701, 800)`, nên lập luận xếp nhóm của mục đứng vững.
- "Charles Martel, ông nội ông" ✔ (Martel → Pepin Lùn → Charlemagne).
- `lĩnh vực: Chính trị/Nhà nước, Giáo dục` (2) ✔; `vùng: Châu Âu` ✔; `Kế thừa từ:` 3, `Ảnh hưởng tới:` 3 — đúng trần ✔.
- Liên kết `CH04-CE05-01` → **Augustinô thành Hippo** ✔; `CH04-CE04-01` → **Constantinus I** ✔; cả hai `qua trường phái`, đúng mức cho hai mối liên hệ mô hình chứ không phải tiếp xúc.
- Quy tắc 6: **Charles Martel không có mục ở bất kỳ chapter nào** ✔.
- Nguồn: McKitterick, *Charlemagne: The Formation of a European Identity* (CUP, 2008) ✔; Einhard, *Vita Karoli Magni*, k. 830 — niên đại soạn còn tranh luận (817–833) nên "k. 830" hợp lệ ✔.

**NÊN — "33 trong 46 năm trị vì" trộn hai cách đếm, và lệch với ghi chú biên tập của chính file.**

Nguyên văn (dòng 508):
> "…vì atlas xếp người theo giai đoạn ảnh hưởng: **33 trong 46 năm trị vì**, toàn bộ việc dựng đế quốc, và cả lễ đăng quang đều nằm trước năm 801."

Con số **33** là đếm **năm dương lịch trọn** (768…800 = 33 năm), còn **46** là **thời lượng** (768→814). Trộn hai đơn vị trong cùng một phân số. Đếm nhất quán thì phải là **33 / 47** (768…814 = 47 năm dương lịch) hoặc **32 / 46** (thời lượng). Ghi chú biên tập của chính file đã viết đúng: *"33 trong **47 năm dương lịch** mà triều ông chạm tới"* — nên đây cũng là một lệch chéo trong cùng file.

Vòng 1 **ký ✓ cho con số này** (§B-01: *"33/46 năm trị vì (768–814, trong đó 768–800 là 33 năm) ✓"*). Phép kiểm ấy không phát hiện việc hai vế dùng hai đơn vị khác nhau.

**Câu thay thế đề xuất (nguyên văn, 54 chữ thay cho 49 ⇒ `why` 88 → 93, vẫn ≤ 104):**
> "Ông được xếp vào nhóm thế kỷ 8 chứ không phải thế kỷ 9 dù mất năm 814, vì atlas xếp người theo giai đoạn ảnh hưởng: 33 trong 47 năm dương lịch mà triều ông chạm tới, toàn bộ việc dựng đế quốc, và cả lễ đăng quang đều nằm trước năm 801."

Soi lại câu thay thế: "47 năm dương lịch mà triều ông chạm tới" = 768…814 kể cả hai đầu ✔, và "33" = 768…800 kể cả hai đầu ✔ — hai vế nay cùng một đơn vị. Câu này **trùng đúng chữ dùng trong ghi chú biên tập**, nên sửa xong hai chỗ sẽ nói một tiếng.

**NÊN — "các bản chép thời ông" lệch khoảng một thế hệ.**

Nguyên văn (dòng 506):
> "…và bảo trợ một lối chữ mới dễ đọc đến mức phần lớn tác phẩm Latin cổ điển còn tới nay là còn qua **các bản chép thời ông**."

Mệnh đề nền đúng (bản chép cổ nhất còn lại của phần lớn tác gia Latin cổ điển là bản Carolingian), nhưng phần lớn những bản ấy là **thế kỷ 9**, tức sau khi ông mất năm 814 — sản phẩm của chương trình ông khởi động, không phải của "thời ông". Vòng 1 đã nêu đúng điều này và **mục chưa sửa**.

**Câu thay thế đề xuất (nguyên văn, 31 chữ thay cho 29 ⇒ `ideas` 119 → 121):**
> "…và bảo trợ một lối chữ mới dễ đọc đến mức phần lớn tác phẩm Latin cổ điển còn tới nay là còn qua phong trào chép sách ông khởi động."

Soi lại câu thay thế: "phong trào chép sách ông khởi động" không khẳng định các bản chép thuộc đời ông, nên bỏ được lỗi niên đại mà không thêm mệnh đề mới nào phải kiểm. **Một hạn chế phải nói:** mệnh đề "ông **bảo trợ** lối chữ mới" vẫn còn trong câu, và mức độ chủ động của triều đình trong việc hình thành chữ nhỏ Caroline (Corbie, Tours) là điều học giới còn bàn — **[KHÔNG KIỂM ĐƯỢC]** ở tầng "ai bảo trợ". Nếu cắt "bảo trợ một lối chữ mới dễ đọc đến mức" và viết thẳng "dưới triều ông, lối chữ nhỏ Caroline lan ra, đến mức…" thì câu vẫn đứng mà không gánh mệnh đề ấy.

**CÂN NHẮC — Einhard đứng cùng dòng `**Nguồn:**` với McKitterick.**
*Vita Karoli Magni* là tụng ca đương thời, còn McKitterick 2008 là công trình **đọc lại hình ảnh Charlemagne một cách hoài nghi**, trong đó Einhard là đối tượng phê bình. Để hai thứ cạnh nhau không sai (một là nguồn sơ cấp, một là nghiên cứu), nhưng dòng `**Nguồn:**` không phân biệt hai hạng, nên người đọc không thấy rằng nguồn thứ hai đang tranh luận với nguồn thứ nhất.

---
### §A-07 · `CH05-CE08-07` Bêđa — dòng 521–539

**Đã kiểm được (không có phát hiện)**
- `Q154938` = "Bede", nhãn vi **"Bêđa"** khớp đúng tên mục, `P31 = Q5` ✔.
- `năm: k. 672–735 CN` + `độ tin cậy niên đại: Cao`. Wikidata: `P569` 672 (preferred) / 672 / 673 — biên độ **1 năm**, nằm sâu trong `DATE_TOLERANCE["Cao"] = 5` ✔; `P570` **735-05-25, precision 11, rank preferred, 2 tham chiếu**. Đây đúng là ca mà đề bài nêu: `precision 11` ở đây **đi cùng** mục được chấm `Cao`, nên `precision` không nói gì về độ tin cậy theo cả hai chiều — và mục chấm `Cao` theo **lý do đúng** (lời tự khai ở chương cuối bộ sử), không theo `precision`.
- "Historia ecclesiastica gentis Anglorum, hoàn tất khoảng năm 731" ✔.
- "bộ sử đầu tiên coi 'người Anh' là một dân tộc chứ không phải một tập hợp vương quốc tranh nhau" ✔ — luận điểm chuẩn của học giới về *gens Anglorum*.
- "Dionysius Exiguus nghĩ ra niên lịch Anno Domini từ thế kỷ 6" ✔ (bảng Phục sinh 525), "nhưng chính Bêđa … biến nó thành mặc định" ✔ — mục **không** gán việc phát minh cho Bêđa, đó là chỗ dễ sai nhất và mục tránh được.
- Xếp nhóm CE08 đúng theo §3: sinh 672 (TK 7), nhưng *De temporum ratione* 725 và *Historia* 731 đều ở TK 8 ✔.
- `lĩnh vực: Sử học, Tôn giáo/Tâm linh` (2) ✔; `vùng: Châu Âu` ✔; `Kế thừa từ:` 3, `Ảnh hưởng tới:` 3 ✔.
- Liên kết `CH05-CE07-09` → **Isiđôrô thành Seville** ✔; `CH04-CE05-01` → **Augustinô thành Hippo** ✔.
- Quy tắc 6: **Alcuin xứ York không có mục ở bất kỳ chapter nào, kể cả `ch90.md`** ✔ — nên nêu ông làm ứng viên bị loại là hợp lệ. Và mục khớp với khối ghi chú "Alcuin: người lẽ ra phải ở nhóm này" ✔, khớp cả với `Ảnh hưởng tới:` của mục Charlemagne ✔.
- Nguồn 1: McClure & Collins (chủ biên), *Bede: The Ecclesiastical History of the English People* (Oxford University Press, 1994) ✔. Nguồn 2: George Hardin Brown, *A Companion to Bede* (Boydell Press, 2009) — **có thật**, Woodbridge/Rochester, 167 tr. ✔. Cả hai đều đúng chủ đề và đúng chiều với mệnh đề chúng đỡ.

**CÂN NHẮC — "Thói quen ghi 'năm 2026' bắt đầu ở một tu viện Northumbria" là tu từ đè lên một mệnh đề mục vừa viết đúng.**
Câu ngay trên đó ghi rõ Dionysius Exiguus mới là người nghĩ ra AD; câu kết lại nói thói quen ấy "bắt đầu" ở Northumbria. Đọc liền hai câu thì hiểu đúng (Bêđa phổ biến, không phát minh), nhưng câu kết đứng một mình thì nói sai. Nếu đổi "bắt đầu" thành "lan ra", câu giữ nguyên sức mà không còn mâu thuẫn với câu trước. (`ideas` 102/130, dư chỗ.)

**CÂN NHẮC — Bêđa và Alcuin không hề cùng thời, và cả quan hệ `trực tiếp` lẫn tư cách "ứng viên bị loại" đều dựa trên điều đó.**
Bêđa mất **735**; `Q154332` cho Alcuin ba `P569` lệch nhau 16 năm (**740 preferred / 735 / 724**) — tức ở phương án phổ biến nhất, Alcuin **sinh sau khi Bêđa mất**. Hai người không bao giờ gặp nhau. Hệ quả hai tầng:
1. `Ảnh hưởng tới: Alcuin xứ York và trường học York · kế thừa · trực tiếp` — `trực tiếp` ở đây chỉ có thể nghĩa là **ảnh hưởng qua văn bản**, không phải tiếp xúc. Cùng vấn đề quy ước với §A-03; xem §C-2.
2. Mục gọi Alcuin là "ứng viên bị loại **cùng vùng**" — chữ **"cùng vùng"** là chính xác và tránh được bẫy; template §5 thì đòi "cùng lĩnh vực, **cùng thời**". Xem §C-1 về việc nhóm này đọc "cùng thời" là "cùng nhóm thế kỷ".

---

### §A-08 · `CH05-CE08-08` Tăng Nhất Hạnh (Yi Xing) — dòng 540–556

**Đã kiểm được (không có phát hiện)**
- `Q710705` = "Yi Xing", nhãn vi **"Nhất Hạnh"** trần, `P31 = Q5` ✔. Alias trường `zh` của chính `Q710705` có **僧一行** ✔ (cùng với 唐一行, 张遂, 一行禅师) — tức tên mục **không phải atlas tự đặt**, đúng như khối ghi chú khẳng định. Alias `vi` có "Trương Toại" ✔, khớp phần "tục danh Trương Toại 張遂".
- `năm: k. 683–727 CN` + `Trung bình`. Kiểm được: **683 là niên đại truyền thống**, còn Chen (2000) lập luận **673** khả dĩ hơn — một bài trên *Religions* 13(6):543 (2022) thậm chí đặt tiêu đề là "Yixing 一行 (673–727)". Biên độ 10 năm ⇒ vượt `Cao = 5`, trong `Trung bình = 25` ✔, và chữ "k." ở năm sinh nay khớp với lý do hạ nấc ✔.
- "Năm 724–725 triều Đường cho đo bóng nắng giữa trưa và độ cao sao Bắc Cực ở chuỗi trạm trải bắc–nam" ✔.
- "Người chủ trì là một tăng sĩ Mật tông" ✔.
- "ông và Lương Lệnh Toản (梁令瓚) lắp vào thiên cầu thuỷ lực một cơ cấu hồi" ✔.
- "Needham coi đây là tiền thân của cơ cấu hồi đồng hồ cơ, tuy đường truyền sang châu Âu chưa chứng minh được" ✔ — **gán luận điểm cho đúng người và đánh dấu đúng tình trạng**; đây là cách viết mà §A-04 còn thiếu.
- "Lịch Đại Diễn của ông ban hành năm 729 và dùng hơn ba mươi năm" ✔ — kiểm được: Đại Diễn lịch được dùng chính thức **729–761**, tức 33 năm.
- "chính nguồn ghi rằng Nhất Hạnh không cho rằng Trái Đất hình cầu, nên không được viết ông 'đo chu vi Trái Đất'" ✔ — và việc tách hai tầng (phép đo có thật / cách gọi là diễn giải hiện đại) là chỗ mạnh nhất nhóm.
- "Ông không liên quan gì tới Thích Nhất Hạnh (1926–2022), **người có mục riêng ở phụ lục**" ✔ — `CH90-CE19_20-10` tồn tại và đúng là Thích Nhất Hạnh; câu chữ đúng quy tắc 6.
- `lĩnh vực: Toán học, Khoa học tự nhiên` (2) ✔; `vùng: Đông Á` ✔; `câu hỏi lớn: Vũ trụ` ✔.
- Nguồn: Needham, *SCC* tập 3 (CUP, 1959) ✔; Needham, Wang Ling & Derek J. de Solla Price, *Heavenly Clockwork* (CUP, 1960) ✔ — đúng ba tác giả, đúng năm.

**CÂN NHẮC — `ideas` = 129/130, chỉ còn một chữ.**
Mọi sửa đổi về sau ở mục này đều phải **trừ chữ trước khi cộng**. Tôi không đề nghị sửa gì ở mục này; ghi lại con số để vòng sau không vô tình làm vỡ trần.

**NÊN — "Vì sao chọn" không nêu đích danh ứng viên bị loại nào, trái template §5.**
`prompts/atlas-prompt.md:45` đòi: *"nêu ĐÍCH DANH 1–2 người cùng lĩnh vực, cùng thời đã được cân nhắc"*. Phần "Vì sao chọn" của mục này dùng toàn bộ 72 chữ cho (a) việc tách hai tầng diễn giải và (b) việc phân biệt tên với Thích Nhất Hạnh — **không có ứng viên bị loại nào**. Lint không kiểm điều này. Đây không phải lỗi riêng mục `-08`: xem §C-1, **7 trong 12 mục của nhóm** cùng thiếu. Mục còn **57 chữ** dư dưới trần `why` (72/104), nên chỗ để thêm là có sẵn.

---

### §A-09 · `CH05-CE08-09` Đỗ Phủ — dòng 557–574

**Đã kiểm được (không có phát hiện)**
- `Q33772` = "Du Fu", nhãn vi "Đỗ Phủ", `P31 = Q5` ✔. `P569 = 712` và `P570 = 770`, **mỗi giá trị 7 tham chiếu, không có giá trị cạnh tranh** ⇒ `độ tin cậy niên đại: Cao` đúng ✔.
- "Gần 1.500 bài thơ của ông còn lại" ✔ (con số thường dẫn 1.400–1.500).
- "ông đẩy thể luật thi tới chỗ chặt nhất mà nó đạt được" ✔.
- "loạn An Lộc Sơn từ năm 755" ✔.
- "Đời sau gọi ông là Thi sử và Thi thánh" ✔ (詩史, 詩聖).
- "gần như tất cả những gì ta biết về đời ông đều rút từ chính thơ ông" ✔ (William Hung 1952).
- `lĩnh vực: Văn học` (1) ✔; `vùng: Đông Á` ✔; `câu hỏi lớn: Con người` ✔; `Ảnh hưởng tới:` 3 ✔.
- Liên kết `CH90-CE19_20-01` → **Nguyễn Du** ✔ đúng người.
- Quy tắc 6: **Lý Bạch không có mục ở bất kỳ chapter nào** ✔, và mục viết ông ở **dạng chữ tự do chứ không phải ID** — đúng cách, vì viết ID mới là giả vờ ông có mục.
- **Quy tắc 5 — đây là ca duy nhất trong nhóm mà "ứng viên bị loại" thật sự cùng thời.** Lý Bạch 701–762, Đỗ Phủ 712–770: hai đời chồng lên nhau 50 năm, hai người gặp nhau năm 744. `Lý Bạch, bạn và người cùng thời · kế thừa · trực tiếp` vì vậy là ca `trực tiếp` **không** vướng hình dạng quy tắc 8.
- Nguồn: Stephen Owen (dịch), *The Poetry of Du Fu*, **6 tập** (De Gruyter, 2016) ✔ — bản dịch trọn vẹn đầu tiên, 6 tập / ~3.000 trang, De Gruyter, mở truy cập; William Hung, *Tu Fu: China's Greatest Poet* (Harvard University Press, 1952) ✔.

**CÂN NHẮC — "biến cố lớn nhất thế kỷ 8 ở Đông Á" là superlative, không phải dữ kiện.**
Bảo vệ được (loạn An Lộc Sơn làm sụp quân điền và phủ binh, đổi cơ cấu thuế khoá, và sử học Trung Quốc coi là mốc chia đôi nhà Đường), nhưng vẫn là một tuyệt đối hoá. Khối ghi chú "An Lộc Sơn" của chính file viết thận trọng hơn — *"**có lẽ** là biến cố đơn lẻ có hệ quả lớn nhất thế kỷ 8 ở lục địa Á–Âu"* — tức ghi chú có chữ "có lẽ" mà thân mục thì không. Chênh nhẹ giữa hai chỗ; nếu muốn một tiếng, thêm "có lẽ" vào thân mục (`ideas` 108/130, dư chỗ).

**CÂN NHẮC — liên kết từ track chính sang track phụ lục.**
`Ảnh hưởng tới: CH90-CE19_20-01` trỏ sang phụ lục Việt Nam, vốn theo thiết kế **cô lập khỏi thống kê chính** (`atlaslib/common.py` khối `APPENDICES`: *"track riêng, KHÔNG tính vào thống kê/độ phủ toàn cục"*). Quan hệ là có thật (Nguyễn Du viết *Lỗi Dương Đỗ Thiếu Lăng mộ*), và lint không chặn. Nhưng hướng liên kết chính → phụ lục là **câu hỏi quy ước chưa được viết ra ở đâu**; vòng 1 đã nêu và vẫn chưa có câu trả lời trong `CONTRIBUTING.md`. Đây là việc của Owner, không phải lỗi sự kiện.

---
### §A-10 · `CH05-CE08-10` Trisong Detsen — dòng 575–591

**Đã kiểm được (không có phát hiện)**
- `Q366661` = "Tri Songdetsen", nhãn vi "Trisong Detsen", `P31 = Q5` ✔.
- `năm: trị vì 755–797 CN` — khớp `NON_BIO_YEARS_RE` (`common.py:133`): chuỗi **bắt đầu** bằng "trị vì" ✔, nên lint bỏ qua đối chiếu P569/P570 đúng như thiết kế.
- "năm 763 quân Tây Tạng vào Trường An và lập một hoàng đế của riêng họ" ✔.
- "năm 783 buộc nhà Đường ký lại đường biên" ✔ (hiệp ước Thanh Thuỷ).
- "Samye — tu viện đầu tiên của Tây Tạng" ✔.
- "tổ chức cuộc tranh biện Samye khoảng 792–794" ✔.
- "Truyền thống Tây Tạng chép phía Ấn Độ thắng, văn bản Hán ở Đôn Hoàng chép ngược lại; điều kiểm được là dòng Ấn Độ thành dòng định hình Phật giáo Tây Tạng về sau" ✔ — **hai chiều đều được nêu và chỉ mệnh đề kiểm được mới được khẳng định**. Đây là mẫu đúng cho cả nhóm.
- "Niên đại sắc chỉ quốc giáo thì khi được dẫn là 779, khi là 791, vì trụ đá Samye ghi việc ấy không mang niên đại" ✔ — cùng kỷ luật.
- "Biên niên Tây Tạng cổ ở Đôn Hoàng cho khung sự kiện" ✔ (Dotson 2009 là bản hiệu đính của chính văn bản ấy — nguồn **đúng thể loại** cho mệnh đề nó đỡ, phép thử quy tắc 7 qua được).
- Lý do loại **Liên Hoa Sinh**: "các bản Đôn Hoàng có nhắc một đạo sư kīlaya cùng tên nhưng không gắn ông với Trisong Detsen, còn tiểu sử đầu tiên ra đời khoảng bốn thế kỷ sau" ✔ — khớp khối ghi chú (*Zangling-ma*, Nyangral Nyima Özer 1124–1192).
- Quy tắc 6: **Padmasambhava / Liên Hoa Sinh không có mục ở bất kỳ chapter nào** ✔.
- `lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh` (2) ✔; `vùng: Đông Á` ✔ đúng quy ước `vùng:` 3 và **nhất quán** với `CH05-CE07-11` Tùng Tán Cán Bố.
- Liên kết `CH05-CE07-11` → **Tùng Tán Cán Bố** ✔.
- Nguồn: Kapstein, *The Tibetan Assimilation of Buddhism* (OUP, 2000) ✔; Dotson, *The Old Tibetan Annals* (Verlag der ÖAW, 2009) ✔.

**CÂN NHẮC — chọn dạng `trị vì` làm tắt phép kiểm niên đại duy nhất chạy tự động, ở đúng một mục mà Wikidata khai bốn năm mất.**
`Q366661` có `P569 = 742` (hai phát biểu) và **`P570` bốn giá trị: 798, 797 (rank preferred, 0 tham chiếu), 800, 797**. Vì trường `năm:` dùng dạng `trị vì`, `NON_BIO_YEARS_RE` làm lint **bỏ qua hoàn toàn** việc đối chiếu — tức mục khai `độ tin cậy niên đại: Trung bình` mà không có phép kiểm nào chạm vào. Quy ước `CONTRIBUTING.md` cho phép dạng `trị vì` với "**vua không có năm sinh**"; ở đây Wikidata **có** năm sinh (742 ×2). Không phải lỗi — khung trị vì nói nhiều hơn về một ông vua — nhưng nếu Owner muốn phép kiểm chạy, dạng `k. 742–797 CN` cũng hợp lệ và được Wikidata đỡ. Ghi lại để quyết một lần cho mọi mục vua.

**CÂN NHẮC — `trực tiếp` cho một đích không phải người.**
> "Chương trình dịch kinh điển Phật giáo sang tiếng Tạng · kế thừa · trực tiếp"

Đích là một **chương trình**, không phải người. Cùng hình dạng với §A-01. Xem §C-2.

**[KHÔNG KIỂM ĐƯỢC] — trụ đá Kar-cun "xác nhận việc lập chùa Samye".**
> "trụ đá Kar-cun do con ông dựng xác nhận việc lập chùa Samye"

Tôi xác minh được: trụ đá sKar-chung do **Tride Songtsen (Sadnalegs)**, con Trisong Detsen, dựng ✔ — nên chữ "con ông" đúng (bản vòng 1 đọc là "người kế vị ông", đã được sửa). Nhưng tôi **không mở được bản dịch hay bản chép minh văn sKar-chung** để xác nhận nó **nhắc đích danh việc lập Samye** (khác với việc nó tái khẳng định các sắc chỉ hộ pháp của Trisong Detsen). Nguồn duy nhất đủ thẩm quyền là Kapstein 2000 hoặc Richardson, *A Corpus of Early Tibetan Inscriptions*, mà tôi không có bản. **Không đoán.** Nếu Owner muốn câu an toàn tuyệt đối mà không phải tra: *"trụ đá Kar-cun do con ông dựng tái khẳng định các sắc chỉ hộ pháp của ông"* — mệnh đề này là phần ai cũng dẫn về minh văn ấy; nhưng **nó cũng chưa được vòng này mở nguồn**, nên đừng chép vào trước khi tra Richardson.

---

### §A-11 · `CH05-CE08-11` Ādi Shankara — dòng 592–610

**Đã kiểm được (không có phát hiện)**
- `Q180967` = "Ādi Shankara", `P31 = Q5` ✔. `P569 = 788` (4 tham chiếu), `P570 = 820` ×2 — tức Wikidata khai đúng cái khung mà mục **từ chối dùng**, và `độ tin cậy niên đại: Thấp` ⇒ `DATE_TOLERANCE["Thấp"] = None` nên lint không báo lệch ✔. Đây là cách dùng nấc `Thấp` đúng mục đích.
- `năm: k. 700 – k. 750 CN` — khớp Nakamura (1983: 48–88), và **SEP, nguồn thứ hai của chính mục, xác nhận được điều này**: tôi mở `https://plato.stanford.edu/entries/shankara/` (**HTTP 200, 111 KB, nội dung thật về Śaṅkara**) và đọc đúng câu: *"Nakamura (1983: 48–88) argues for an earlier date of 700–750 CE"*.
- "ông trích Pháp Xứng, nên sau giữa thế kỷ 7" ✔ — SEP có đoạn Śaṅkara phê phán "Vasubandhu and Dharmakīrti" (BrSūBh 2.2.28), nên mệnh đề này được **chính nguồn được dẫn** đỡ.
- "các *Śaṅkaravijaya* đều được soạn nhiều thế kỷ sau" ✔ — SEP: các bản thánh truyện "were composed several centuries after his death".
- `nơi: Kerala` ✔ — SEP: sinh ở Kalaḍi, Kerala ngày nay.
- Ba luận điểm Advaita được tóm đúng, và cách phân biệt *"không phải ảo giác mà là một cách nhìn sai do vô minh"* là cách tránh đúng hiểu lầm phổ biến nhất về *māyā* ✔.
- "các maṭha đặt ông ở thế kỷ 5 trước Công nguyên" ✔ — khớp khối ghi chú (Śṛṅgeri 483 TCN, Kanchipuram 509 TCN, Dvārakā 491 TCN).
- `lĩnh vực: Triết học, Tôn giáo/Tâm linh` (2) ✔; `vùng: Nam Á` ✔; `câu hỏi lớn: Thực tại` ✔; `Kế thừa từ:` 3, `Ảnh hưởng tới:` 3 ✔.
- Liên kết `CH05-CE07-10` → **Pháp Xứng** ✔; ID `CH05-CE10-07` trong văn xuôi → **Vācaspati Miśra** ✔.
- Quy tắc 6: mục không nêu ứng viên bị loại nào ✔ (xem §C-1 về mặt trái của điều đó).
- Nguồn 1: Nakamura, *A History of Early Vedānta Philosophy, Part One* (Motilal Banarsidass, 1983) — **năm 1983 khớp đúng cách SEP trích dẫn chính sách ấy** ✔.

**BẮT BUỘC — "đề xuất của Đông phương học châu Âu" bị chính ghi chú biên tập của file này bác, bằng nguyên một đoạn.**

Nguyên văn câu sai (dòng 598):
> "…khung 788–820 hay được chép lại không phải truyền thống của các maṭha mà là **đề xuất của Đông phương học châu Âu cuối thế kỷ 19**; các maṭha đặt ông ở thế kỷ 5 trước Công nguyên."

Khối ghi chú "Khung 788–820 của Shankara không phải truyền thống của các maṭha" trong **cùng file** viết ngược lại ở đúng chỗ then chốt:
> "…C.P. Tiele … lấy nó từ chuyên luận *Āryavidyā-sudhākara* của Yajñeśvara Śāstrī, vốn dẫn lại *Śaṅkara-mandāra-saurabha* của Bhaṭṭa Nīlakaṇṭha … Tức đóng góp của giới Đông phương học là **chọn và phổ biến** một niên đại vốn có nguồn Ấn Độ, **không phải chế ra nó**."

Chữ "đề xuất" trong thân mục khẳng định đúng cái mà ghi chú đã bác. Và SEP — nguồn thứ hai của chính mục — cũng chỉ viết trung tính *"Early scholars placed him from 788–820 CE"*, không nói ai đề xuất.

**Câu thay thế đề xuất (nguyên văn, 55 chữ thay cho 47):**
> "Niên đại của ông là tranh luận mở, và khung 788–820 hay được chép lại không phải truyền thống của các maṭha mà là một niên đại nguồn Ấn Độ được Đông phương học châu Âu cuối thế kỷ 19 chọn và phổ biến; các maṭha đặt ông ở thế kỷ 5 trước Công nguyên."

Soi lại câu thay thế: mỗi mệnh đề trong đó đều có chỗ dựa **trong chính repo** — "nguồn Ấn Độ" và "chọn và phổ biến" lấy nguyên từ khối ghi chú đã được kiểm, "các maṭha đặt ở thế kỷ 5 TCN" cũng vậy. Nó **không** thêm mệnh đề mới nào phải tra. Xem cảnh báo trần chữ ở phát hiện tiếp theo.

**NÊN — mỏ neo Vācaspati mâu thuẫn với quyết định mà chính atlas đã ra ở `CH05-CE10-07`.**

Nguyên văn (dòng 598):
> "…còn mỏ neo Vācaspati Miśra (`CH05-CE10-07`) thì lỏng hơn vẻ ngoài, vì niên đại của chính Vācaspati có hai cách đọc cách nhau 135 năm."

Mục `CH05-CE10-07` **đã chọn** rồi: `năm: hoạt động k. 950–1000 CN`, và phần "Vì sao chọn" của nó viết thẳng *"mục này chọn khung 950–1000 theo cách đọc Śaka"*. Trong hệ quy chiếu của chính atlas, Vācaspati ở **cuối thế kỷ 10** — tức cách Śaṅkara hơn hai thế kỷ, và **không còn là mỏ neo gì cả**, chứ không phải "lỏng hơn vẻ ngoài". Mục `-11` đang mô tả tranh luận như còn mở trong khi file đã khép nó về một phía.
Thêm một chi tiết: **cả hai nguồn được dẫn của mục `-11` đều không đỡ mỏ neo này.** SEP không nhắc Vācaspati Miśra **một lần nào** trong toàn bài (tôi `grep` toàn văn: 0 lần); chỗ chặn đầu trên mà SEP thật sự dùng là **Maṇḍanamiśra** (Potter 1981: 14–15, 116–119; Thrasher 1979). Việc Nakamura 1983 có dùng Vācaspati làm hạn trên hay không thì **[KHÔNG KIỂM ĐƯỢC]** — tôi không có bản sách.

**Câu thay thế đề xuất (nguyên văn, 24 chữ thay cho 25):**
> "…còn mỏ neo Vācaspati Miśra (`CH05-CE10-07`) thì atlas đã bỏ: vòng CE10 đọc niên hiệu theo lịch Śaka và xếp ông ở k. 950–1000."

Soi lại câu thay thế: cả hai mệnh đề đều đọc thẳng được từ `content/ch05.md` (trường `năm:` và phần "Vì sao chọn" của `CH05-CE10-07`), nên không có gì phải tra ngoài. Nó cũng **không** khẳng định cách đọc Śaka là đúng — chỉ ghi rằng atlas đã chọn nó, đúng mức độ ta biết.

**Trần chữ, đã đếm:** `why` hiện 92. Áp **cả hai** câu thay thế ⇒ 92 + 8 − 1 = **99/104** ✔. Nếu Owner muốn biên rộng hơn, bỏ cụm "nguồn Ấn Độ" ở câu đầu (⇒ 97) — câu vẫn đứng vì vế quan trọng là "chọn và phổ biến", không phải "nguồn Ấn Độ".

---

### §A-12 · `CH05-CE08-12` Yikʼin Chan Kʼawiil — dòng 611–627

**Đã kiểm được (không có phát hiện)**
- `Q2620151` = "Yik'in Chan K'awiil", `P31 = Q5` ✔. `P569` **không có**; `P570 = somevalue` — Wikidata khẳng định có năm mất nhưng không biết là năm nào, khớp đúng việc mục ghi `k. 766` và giải thích "năm mất còn để ngỏ" ✔.
- `năm: trị vì 734 – k. 766 CN` — khớp `NON_BIO_YEARS_RE` ✔ ("trị vì" ở đầu trường).
- "lên ngôi ngày 8 tháng 12 năm 734" ✔.
- "đánh bại Calakmul năm 736, rồi hai đồng minh của Calakmul là El Perú năm 743 và Naranjo năm 744" ✔.
- "các rầm gỗ chạm ghi chính những chiến dịch ấy" ✔ (rầm 2 và 3, Đền IV).
- "Trong hai thế kỷ, chính trị Maya Cổ điển xoay quanh thế đối đầu giữa Tikal và Calakmul" ✔ — cách đọc chuẩn của Martin & Grube.
- "năm sinh của Charlemagne cùng thế kỷ vẫn còn **ba phương án cạnh tranh là 742, 747 và 748**" ✔ — **khớp chính xác** `P569` của `Q3044` (5 phát biểu, 3 năm phân biệt). Con số "bốn" mà vòng 1 bắt đã được sửa, và bản sửa đúng.
- "Kʼinich Janaabʼ Pakal **có mục riêng ở nhóm CE07**" ✔ — `CH05-CE07-12` tồn tại, đúng người; câu chữ đúng `CONTRIBUTING.md:51`.
- `lĩnh vực: Chính trị/Nhà nước, Nghệ thuật/Kiến trúc` (2) ✔; `vùng: Châu Mỹ` ✔.
- "Jasaw Chan Kʼawiil I, cha ông" ✔; "Yaxʼ Nuun Ahiin II" ✔ đúng người kế vị.
- Nguồn: Martin & Grube, *Chronicle of the Maya Kings and Queens*, tái bản lần 2 (Thames & Hudson, 2008) ✔; Harrison, *The Lords of Tikal: Rulers of an Ancient Maya City* (Thames & Hudson, 1999) ✔ — có thật, New Aspects of Antiquity, 208 tr.

**BẮT BUỘC — "cao nhất thế giới Maya thời Cổ điển" vẫn sai, và đây là câu thay thế của vòng 1.**

Nguyên văn câu sai (dòng 615):
> "…và chuyển chiến thắng thành đá — Đền IV, cao 70 mét, công trình cao nhất Tikal và **cao nhất thế giới Maya thời Cổ điển**, với các rầm gỗ chạm ghi chính những chiến dịch ấy."

Vòng 1 bắt đúng rằng "kim tự tháp cao nhất thế giới Maya" sai (La Danta ở El Mirador cao hơn), rồi đề nghị hạ xuống "cao nhất thế giới Maya **thời Cổ điển**" — và mục đã chép nguyên văn. Nhưng mệnh đề mới **cũng sai**, vì La Danta không phải đối thủ duy nhất:

- **Đền IV ở Tikal: 70 m.**
- **Đại kim tự tháp / Acropolis ở Toniná (Chiapas): 74 m** — công trình Maya **thời Cổ điển**, và là **công trình tiền Columbus còn đứng cao nhất Tân thế giới**; Đền IV được xếp **thứ hai**, ngay sau nó.

Tức cái bị "thời Cổ điển" loại bỏ chỉ là La Danta (Tiền Cổ điển, k. 300 TCN – 150 CN); Toniná thì vẫn đứng đó và vẫn cao hơn. Đây đúng hình dạng mà đề bài cảnh báo: **câu thay thế của vòng trước mang theo đúng loại lỗi nó vừa chẩn** — một superlative được thu hẹp vừa đủ để né phản ví dụ đã biết, chứ không được kiểm lại từ đầu.
*(Một lưu ý trung thực: Acropolis Toniná là quần thể bậc thang dựng trên sườn đồi tự nhiên, nên có người không xếp nó cùng hạng với một kim tự tháp đứng tự do. Nhưng câu của mục dùng chữ "**công trình**", không phải "kim tự tháp" — và ở hạng "công trình" thì Toniná thắng.)*

**Câu thay thế đề xuất (nguyên văn, 36 chữ thay cho 37 ⇒ `ideas` 107 → 106):**
> "…và chuyển chiến thắng thành đá — Đền IV, cao 70 mét, công trình cao nhất Tikal và thuộc hàng cao nhất thế giới Maya, với các rầm gỗ chạm ghi chính những chiến dịch ấy."

Soi lại câu thay thế: tôi **bỏ hẳn superlative tuyệt đối** thay vì thu hẹp nó thêm một nấc — vì mọi nấc thu hẹp đều cần một phép kiểm toàn bộ danh mục công trình Maya mà không vòng nào làm được. "cao nhất Tikal" là mệnh đề kiểm được và không ai tranh cãi; "thuộc hàng cao nhất thế giới Maya" đúng với cả bảng xếp hạng mà tôi mở được (Đền IV đứng thứ hai trong số công trình tiền Columbus còn đứng). Nếu Owner muốn tuyệt đối an toàn, cắt luôn vế sau: *"Đền IV, cao 70 mét, công trình cao nhất Tikal"* (−6 chữ) — câu vẫn đứng.

**CÂN NHẮC — `Calakmul, qua thế đối đầu kéo dài · phản bác · trực tiếp`.**
`phản bác` trong `RELATION_TYPES` được hiểu là bác bỏ **tư tưởng**; dùng cho một cuộc đối đầu **quân sự** giữa một người và một **thành bang** là co giãn, và `trực tiếp` lại là mức bằng chứng cho quan hệ người-với-người. Không sai từ vựng, nhưng là ca thứ tư cùng hình dạng trong nhóm. Xem §C-2.

---
## §B · Hai phép kiểm chạy riêng

### §B-1 · URL trong dòng `**Nguồn:**` — toàn nhóm có đúng một

`grep -o 'https\?://[^ )]*'` trên dải 412–627 trả về **đúng một URL**:

| URL | HTTP | Byte | Có nói về nhân vật không? |
|---|---|---|---|
| `https://plato.stanford.edu/entries/shankara/` | **200** | 111.114 | **Có.** Tôi tải toàn văn và `grep` được: "Nakamura (1983: 48–88) argues for an earlier date of 700–750 CE"; "Śaṅkara also critiques … Vasubandhu and Dharmakīrti"; "Hagiographical accounts … the Śaṅkaravijayas … were composed several centuries after his death"; "born in Kalaḍi, located in modern day Kerala". |

Ba bẫy mà đề bài nêu (202 + 0 byte, 429 Varnish, 403) **không xảy ra ở URL này**. Tôi gặp chúng ở nơi khác trong quá trình rà, và ghi lại vì chúng là tư liệu về quy trình chứ không phải lỗi của nhóm: `cambridge.org` (trang sách El-Hibri) trả **403**, và `iranicaonline.org` (mục ABŪ ḤANĪFA) trả **403** cả qua `curl` lẫn qua fetch — đó là lý do hai mệnh đề ở §A-02 và §A-04 phải nhận `[KHÔNG KIỂM ĐƯỢC]`.

Nhận xét: **11/12 mục không có URL nào**, chỉ có sách. Điều đó làm phép kiểm "nguồn có nói điều được dẫn không" phụ thuộc hoàn toàn vào việc tra thư mục bên ngoài — và đó là chỗ cả hai vòng đều mỏng nhất (xem mọi dấu `[KHÔNG KIỂM ĐƯỢC]` ở §D).

### §B-2 · Lint hiện tại

`.venv/bin/python build.py --offline`: **0 lỗi · 3 cảnh báo** (không cảnh báo nào thuộc ch05) · `reports/lint-ch05.txt` ghi **ERROR 0 · WARN 0 · INFO 62**. Mọi dòng INFO liên quan CE08 đều là **bất đối xứng liên kết** đã được hoãn sang P4 (13 dòng), không phải lỗi. Không có cảnh báo trần chữ, không có cảnh báo từ vựng. Tức **mọi phát hiện trong báo cáo này đều nằm ngoài tầm với của lint** — đúng như thiết kế của vòng bình duyệt.

---

## §C · Ba hình dạng lỗi ở tầng nhóm

### §C-1 · NÊN — 7 trong 12 mục không nêu đích danh ứng viên bị loại, trái template §5

`prompts/atlas-prompt.md:45` (từ vựng bắt buộc của template):
> "**Vì sao chọn (~80 chữ):** nêu ĐÍCH DANH 1–2 người cùng lĩnh vực, cùng thời đã được cân nhắc, và lý do người này vượt trội theo tiêu chí (a)–(d). Không viết chung chung."

| Mục | Nêu đích danh ai? | Đạt? | `why` còn dư |
|---|---|---|---|
| -01 Abu Muslim | Divashtich xứ Panjikant | ✔ | 29 |
| -02 Al-Mansur | — (al-Saffah chỉ xuất hiện trong một phản thực, không phải tư cách ứng viên) | ✗ | 27 |
| -03 Jaʿfar al-Sadiq | — | ✗ | 28 |
| -04 Abu Hanifa | — | ✗ | 23 |
| -05 Sibawayh | — | ✗ | 20 |
| -06 Charlemagne | Charles Martel | ✔ | 16 |
| -07 Bêđa | Alcuin xứ York | ✔ | 34 |
| -08 Tăng Nhất Hạnh | — (Thích Nhất Hạnh là phân biệt tên, không phải ứng viên) | ✗ | 32 |
| -09 Đỗ Phủ | Lý Bạch | ✔ | 29 |
| -10 Trisong Detsen | Liên Hoa Sinh | ✔ | 6 |
| -11 Ādi Shankara | — | ✗ | 12 |
| -12 Yikʼin Chan Kʼawiil | — (Pakal được nêu đúng cách là người **đã có mục**, không phải ứng viên bị loại) | ✗ | 25 |

Lint không kiểm điều này, và `CONTRIBUTING.md` bước 8 lại liệt nó vào danh sách bắt buộc của đánh giá độc lập (*"mục 'Vì sao chọn' có nêu đích danh ứng viên bị loại không"*). **Vòng 1 không nêu thiếu sót này ở mục nào** — trái lại, §A-03 vòng 1 khen phần "Vì sao chọn" của mục `-03` là "điểm mạnh đáng ghi nhận" mà không nhận ra nó không có ứng viên bị loại nào.

Chi phí sửa thấp: ghi chú biên tập **đã có sẵn** tên cho ít nhất hai mục Trung Đông — khối "Nhóm chật nhất Chapter 5" nêu **Malik ibn Anas** và **Ibn Ishaq** bị loại thuần vì hết suất. Cả hai đều **không có mục ở bất kỳ chapter nào** (tôi đã kiểm), nên quy tắc 6 cho phép nêu họ. Mọi mục thiếu đều còn ≥ 12 chữ dư dưới trần `why`.

### §C-2 · NÊN — `trực tiếp` đang gánh hai nghĩa khác nhau, và nhóm này dùng cả hai mà không phân biệt

Đếm trên 12 mục, `trực tiếp` được dùng cho **ba loại đích khác nhau**:

1. **Người ↔ người, có tiếp xúc thật** — Al-Khalil → Sibawayh; Muhammad al-Baqir → Jaʿfar; Lý Bạch ↔ Đỗ Phủ; Jasaw Chan Kʼawiil I → Yikʼin; Śāntarakṣita → Trisong Detsen. **Không vấn đề.**
2. **Người ↔ người, không cùng thời, ảnh hưởng qua văn bản** — Ali (mất 661) → Jaʿfar (sinh k. 702); Isiđôrô (mất 636) → Bêđa; Pháp Xứng → Shankara; Gauḍapāda → Shankara; Bêđa (mất 735) → Alcuin (sinh k. 735/740). Đây chính là hình dạng `CONTRIBUTING.md` quy tắc 8 nói lint không bắt được.
3. **Đích không phải một con người** — "Cuộc vận động ngầm Hāshimiyya" (-01); "Abu Yusuf, Muhammad al-Shaybani **và bộ luật Hanafī**" (-04); "Al-Mubarrad **và toàn bộ ngữ pháp Ả Rập về sau**" (-05); "Pepin Lùn **và liên minh Frank–giáo hoàng**" (-06); "Alcuin xứ York **và trường học York**" (-07); "Thiện Vô Uý **và Mật tông đời Đường**" (-08); "**Chương trình dịch kinh điển** Phật giáo sang tiếng Tạng" (-10); "**Calakmul**, qua thế đối đầu kéo dài" (-12). Đây là "mức bằng chứng thổi phồng" mà đề bài nêu: `trực tiếp` áp cho quan hệ người–thiết chế / người–phong trào.

Loại (2) và (3) không vi phạm `EVIDENCE_LEVELS` (từ vựng không nói gì về chủ thể của đích), nên **lint mù hoàn toàn**. Vòng 1 đã đề nghị Owner viết quy ước này thành văn; tôi đọc lại toàn bộ `CONTRIBUTING.md` hiện tại và **quy ước ấy vẫn chưa được viết**. Đây đúng tình huống mà mục `vùng:` của `CONTRIBUTING.md` đã từng gặp — *"quy tắc này trước nay chưa từng được viết ra"* — và cách xử lý đã được chứng minh là đúng: viết nó thành văn, rồi áp lại. Trước khi có quy ước, tôi **không** đề nghị sửa từng dòng liên kết: sửa lẻ sẽ làm nhóm CE08 lệch khỏi mọi chapter khác.

### §C-3 · CÂN NHẮC — nhóm đọc "cùng thời" của template là "cùng nhóm thế kỷ", và điều đó cũng chưa thành văn

Template §5 đòi ứng viên bị loại phải "cùng lĩnh vực, **cùng thời**". Kiểm 5 ca có nêu tên:

| Mục | Người được chọn | Ứng viên bị loại | Có thật sự cùng thời? |
|---|---|---|---|
| -09 | Đỗ Phủ 712–770 | Lý Bạch 701–762 | **Có** — chồng 50 năm, gặp nhau 744 |
| -10 | Trisong Detsen trị vì 755–797 | Liên Hoa Sinh (truyền thống TK 8) | Có, theo truyền thống |
| -01 | Abu Muslim k. 718–755 | Divashtich mất **722** | Chồng về mặt sinh học (Abu Muslim ~4 tuổi), **sự nghiệp không chồng một ngày nào** |
| -06 | Charlemagne k. 748–814 | Charles Martel 688–**741** | **Martel mất 7 năm trước khi Charlemagne sinh** |
| -07 | Bêđa k. 672–**735** | Alcuin sinh **k. 735/740** | **Alcuin sinh vào hoặc sau năm Bêđa mất** |

Ba ca cuối có đúng hình dạng mà `CONTRIBUTING.md` quy tắc 5 mô tả ("Lương Thế Vinh mất 5 năm trước khi Nguyễn Bỉnh Khiêm sinh"). **Nhưng tôi không xếp chúng là lỗi**, vì ba điều: (a) cả ba ứng viên bị loại đều thuộc **cùng nhóm thế kỷ CE08** theo chính tiêu chí giai đoạn ảnh hưởng mà atlas dùng — Martel hoạt động 718–741, Alcuin 782–804, Divashtich tới 722; (b) đánh đổi ở đây là **một suất trong nhóm 12 người**, tức một đánh đổi có thật, không phải một so sánh mượn tạm; (c) mục `-06` và `-07` **tự khai quan hệ** ("ông nội ông", "cùng vùng"), nên không giấu gì.

Điều cần làm là **viết ra** rằng "cùng thời" trong template nghĩa là "cùng nhóm thế kỷ theo giai đoạn ảnh hưởng", đúng như `vùng:` đã được viết ra sau hai vòng Chapter 4. Nếu không, vòng sau sẽ đọc quy tắc 5 theo nghĩa đen và báo ba lỗi không tồn tại — hoặc tệ hơn, "sửa" bằng cách thay bằng một cái tên thật sự cùng năm sinh nhưng không cạnh tranh suất nào.

---
## §D · Mọi `[KHÔNG KIỂM ĐƯỢC]` của vòng này

| # | Ở đâu | Mệnh đề không kiểm được | Vì sao | Cắt gì thì câu vẫn đứng |
|---|---|---|---|---|
| D-1 | §A-02, thân mục `-02` | Năm sinh **709** của al-Mansur | Ba truy vấn khác nhau (kể cả "101 AH", "c. 709") không ra dòng học thuật nào; `Q31066` chỉ có 713-11 và 714, cả hai = 95 AH | Bỏ "709", chỉ giữ 713 và 714 |
| D-2 | §A-02, dòng `**Nguồn:**` | El-Hibri 1999 **có bàn tới al-Mansur hay không** | `cambridge.org` trả **HTTP 403**; mục lục đầy đủ không mở được. Xác minh được: 4 chương chính là Harun al-Rashid, al-Amin, al-Ma'mun, cấu trúc tường thuật nội chiến — **không chương nào về al-Mansur** | Bỏ El-Hibri; Kennedy 1981 (và Lassner 1980, đã kiểm) đủ đỡ mọi mệnh đề của mục |
| D-3 | §A-04, thân mục `-04` | **"Melchert đọc chi tiết ấy là truyền thuyết thánh hoá đời sau"** | Không mở được văn bản Melchert 1997 ở đoạn liên quan; `iranicaonline.org` (ABŪ ḤANĪFA) trả **HTTP 403** qua cả `curl` lẫn fetch. Chỉ xác minh được lập trường **chung** của Melchert (các madhhab chưa vận hành ở TK 8), không phải phán đoán về mạch truyện tử đạo | Bỏ hẳn việc gán cho Melchert; dùng câu thay thế ở §A-04 |
| D-4 | §A-06, thân mục `-06` | Mức độ **"bảo trợ"** của triều đình với chữ nhỏ Caroline | Việc chữ nhỏ Caroline hình thành ở Corbie/Tours dưới triều ông là đồng thuận; việc ai **bảo trợ** nó thì tôi không mở được công trình nào chốt | Viết "dưới triều ông, lối chữ nhỏ Caroline lan ra" thay vì "ông bảo trợ" |
| D-5 | §A-10, thân mục `-10` | Trụ đá **Kar-cun (sKar-chung) có nhắc việc lập Samye** hay không | Không có bản dịch/bản chép minh văn; nguồn đủ thẩm quyền là Kapstein 2000 hoặc Richardson, *A Corpus of Early Tibetan Inscriptions*, tôi không có bản. Xác minh được **người dựng** là Tride Songtsen, con ông ✔ | Nếu bỏ "xác nhận việc lập chùa Samye" thì mất chính luận cứ của câu — nên đây là chỗ **phải tra**, không phải chỗ cắt |
| D-6 | §A-11, thân mục `-11` | Nakamura 1983 có dùng **Vācaspati Miśra** làm hạn trên cho Śaṅkara hay không | Không có bản sách. Xác minh được chiều ngược: **SEP không nhắc Vācaspati một lần nào** (0 lần trong toàn văn), và hạn trên mà SEP dùng là **Maṇḍanamiśra** (Potter 1981; Thrasher 1979) | Dùng câu thay thế ở §A-11, nó không còn phụ thuộc vào việc ai dùng mỏ neo nào |
| D-7 | §A-10, **trong chính đề xuất của tôi** | Câu dự phòng *"trụ đá Kar-cun … tái khẳng định các sắc chỉ hộ pháp của ông"* | Cùng lý do D-5 — tôi **không** mở được minh văn. Ghi ngay trong phần đề xuất, đúng yêu cầu | **Đừng chép câu dự phòng ấy vào file trước khi tra Richardson** |

Ngoài ra: §A-02 từng mang một `[KHÔNG KIỂM ĐƯỢC]` cho thư mục Lassner 1980 và **đã được gỡ trong chính báo cáo này** sau khi tra xong (Princeton University Press, 1980, Princeton Studies on the Near East, xvii+328 tr.).

---

## §E · Những chỗ vòng 1 ký ✓ mà vòng này thấy sai hoặc không kiểm được

### E-1 · Ký ✓ cho mệnh đề sai

| # | Vòng 1 | Nó ký gì | Vòng này tìm được gì |
|---|---|---|---|
| E-1.1 | §B-14 | "Khương Công Phụ đỗ đầu kỳ thi nhà Đường năm 780" — **✓** | Sai, như đề bài nêu. *Tân Đường thư* q.152 chỉ chép 「第進士」 và 「以制策異等」: **không thứ hạng, không năm**. Ghi chú biên tập hiện tại **đã sửa** và còn viết thêm một câu chặn: *"Không được thay nó bằng 'đỗ đầu kỳ thi' — đó là cùng một mệnh đề thứ hạng, chỉ đổi chữ."* Tôi đọc lại khối ấy và xác nhận bản hiện tại đúng. |
| E-1.2 | §B-01 | "**33/46 năm trị vì** (768–814, trong đó 768–800 là 33 năm) **✓**" | Phép kiểm này không nhận ra hai vế dùng **hai đơn vị khác nhau**: 33 là năm dương lịch trọn, 46 là thời lượng. Nhất quán phải là 33/47 hoặc 32/46. Ghi chú biên tập của chính file viết "33 trong **47** năm dương lịch" — nên vòng 1 đã ký ✓ cho một con số lệch với ghi chú mà nó cũng đang rà. Xem §A-06. |
| E-1.3 | §A-12 | "tôi tự truy `Q2620151` — Wikidata ghi **`P570 = no value`**, tức không có năm mất nào được khẳng định **✓**" | Đọc sai `snaktype`. Giá trị thật là **`somevalue`** (*unknown value*), không phải `novalue`. Hai thứ ngược nghĩa nhau: `somevalue` nghĩa là Wikidata **khẳng định có** một năm mất nhưng không biết là năm nào; `novalue` nghĩa là khẳng định **không có**. Kết luận cuối (ghi `k. 766`) vẫn đúng, nhưng lý do thì ngược. |

### E-2 · Câu thay thế của vòng 1 đã được chép vào file, và mang theo lỗi cùng loại

Đây là nhóm nghiêm trọng nhất, vì những câu này **đã nằm trong `content/ch05.md`** và trông như đã qua bình duyệt.

| # | Vòng 1 chẩn đúng điều gì | Câu thay thế nó đưa ra | Lỗi còn lại |
|---|---|---|---|
| E-2.1 | `-12`: "kim tự tháp cao nhất thế giới Maya" sai vì **La Danta** cao hơn | "công trình cao nhất Tikal và **cao nhất thế giới Maya thời Cổ điển**" | **Vẫn sai.** Acropolis / Đại kim tự tháp **Toniná** (Chiapas) cao **74 m**, thuộc **thời Cổ điển**, và Đền IV (70 m) được xếp **thứ hai** sau nó trong số công trình tiền Columbus còn đứng. Chữ "thời Cổ điển" chỉ loại được La Danta. Xem §A-12. **BẮT BUỘC.** |
| E-2.2 | `-05`: "bộ mô tả ngôn ngữ còn nguyên vẹn cổ nhất ngoài truyền thống Pāṇini" sai, và nêu đích danh Donatus, Priscianus, Dionysius Thrax để bác | "**khác các sách ngữ pháp Hy Lạp và Latin còn lại**, al-Kitāb không bị công trình nào trong truyền thống của nó thay thế" | Dùng chính ba tác phẩm vừa viện dẫn làm **vế đối lập**, theo chiều ngược với dữ kiện: Donatus và Priscianus cũng **không** bị thay thế trong truyền thống của chúng — chúng là sách giáo khoa chuẩn của châu Âu Latin gần một nghìn năm. Xem §A-05. **CÂN NHẮC.** |
| E-2.3 | `-02`: con số "ba ngày mất" không kiểm được — vòng 1 **tự đánh dấu `[KHÔNG KIỂM ĐƯỢC]`** | "các nguồn cho **709**, 713 và 714" | Thay một con số chưa kiểm bằng một **bộ ba** trong đó phần tử "709" cũng chưa kiểm, và lần này **không** kèm dấu `[KHÔNG KIỂM ĐƯỢC]`. Xem §A-02 và D-1. **BẮT BUỘC.** |
| E-2.4 | `-04`: viết chuyện ngục tù như dữ kiện là dùng nguồn ngược luận điểm của nó | "**Melchert đọc chi tiết ấy là truyền thuyết thánh hoá đời sau**" | Gán một phán đoán **cụ thể** cho một tác giả **cụ thể** mà không mở sách — trong khi chính vòng 1 ở §A-11 thừa nhận nó không có bản sách của nguồn tương đương. `CONTRIBUTING.md` mục 3 cấm đúng hình dạng này (ghi số chương khi chưa mở mục lục). Xem §A-04 và D-3. **NÊN + `[KHÔNG KIỂM ĐƯỢC]`.** |

### E-3 · Vòng 1 ký ✓ nhưng phép kiểm không phủ tới

| # | Chỗ | Vấn đề |
|---|---|---|
| E-3.1 | Toàn §A vòng 1 | **Không mục nào** nêu việc 7/12 mục không có ứng viên bị loại đích danh, dù `CONTRIBUTING.md` bước 8 liệt nó vào danh sách bắt buộc. §A-03 vòng 1 còn **khen** phần "Vì sao chọn" của `-03` là "điểm mạnh đáng ghi nhận" — mục ấy không nêu ứng viên nào. Xem §C-1. |
| E-3.2 | Phạm vi vòng 1 | Dòng **Bối cảnh** của nhóm **không được kiểm ở đâu cả** (§A chỉ có A-01…A-12, §B chỉ về ghi chú biên tập). Đó là chỗ chứa phát hiện **BẮT BUỘC** nặng nhất của vòng này (§A-00). Lỗ hổng phạm vi, không phải chữ ký sai. |
| E-3.3 | §A-10 vòng 1 | Ký ✓ cho `trị vì 755–797` + `Trung bình` với lý do "năm mất có dòng cạnh tranh, độ chênh dưới 10 năm". Nhưng vì trường `năm:` dùng dạng `trị vì`, `NON_BIO_YEARS_RE` làm lint **bỏ qua hoàn toàn** phép đối chiếu — nên `Trung bình` ở đây **không được phép kiểm nào chạm tới**, và `Q366661` khai **bốn** giá trị `P570` chứ không phải hai. Xem §A-10. |

### E-4 · Những chỗ vòng 1 ký ✓ mà vòng này **chạy lại độc lập và xác nhận đúng**

Ghi ra để Owner biết phần nào của vòng 1 vẫn đứng:
- **Cả 12 Q-ID** trỏ đúng người và đều `P31 = Q5` (tôi tự gọi `wbgetentities`, không chép bảng vòng 1).
- **Quy tắc 6 sạch ở tầng thân mục**: 5 ứng viên bị loại được nêu đích danh đều không có mục ở đâu, kể cả `ch90.md`; 5 tên có mục riêng xuất hiện trong nhóm đều được gọi đúng cách.
- **Mọi ID liên kết trỏ đúng người** — tôi mở từng đích đọc tên.
- **Charlemagne thuộc CE08**, với `group_range('CE08') = (701, 800)` bao gồm cả năm 800.
- **Sibawayh `Thấp`** là nấc đúng (161/777 Basra vs 177–180/793–796 gần Shiraz, lệch 19 năm **và** khác nơi chết).
- **Bêđa `Cao`** là nấc đúng, và `P570 = 735-05-25` precision 11 preferred 2 tham chiếu — xác nhận đúng ví dụ mà ghi chú biên tập dùng.
- **Đỗ Phủ `Cao`**: `P569`/`P570` mỗi bên 7 tham chiếu, không có giá trị cạnh tranh.
- **Melchert đặt các trường phái Sunni ở TK 9–10** — mệnh đề mà ghi chú biên tập khẳng định, tôi tra được qua mô tả của Brill/nhà xuất bản.

### E-5 · Một `[KHÔNG KIỂM ĐƯỢC]` của vòng 1 nay **đã giải được**

Vòng 1 §A-12 ghi: *"Tôi không tìm được chỗ nào xác nhận con số **766** — [KHÔNG KIỂM ĐƯỢC] … các nguồn mở được thì cho 746/755."* Vòng này tra được: triều Yikʼin Chan Kʼawiil **được dẫn là 734–766** (với một dòng khác ghi "k. 746/766"), nên `trị vì 734 – k. 766 CN` **có chỗ dựa**, và chữ "k." đã được thêm đúng. Dấu `[KHÔNG KIỂM ĐƯỢC]` ấy **gỡ được**.

---

## §F · Bảng tổng

### F-1 · Theo mục

| Mục | Dòng | BẮT BUỘC | NÊN | CÂN NHẮC | `[KKĐ]` |
|---|---|---|---|---|---|
| **Bối cảnh** nhóm CE08 | 413 | **1** | 0 | 0 | 0 |
| -01 Abu Muslim al-Khurasani | 415–431 | 0 | 0 | 3 | 0 |
| -02 Al-Mansur | 432–448 | **2** | 1 | 1 | 2 |
| -03 Jaʿfar al-Sadiq | 449–466 | 0 | 1 | 2 | 0 |
| -04 Abu Hanifa | 467–483 | 0 | 2 | 0 | 1 |
| -05 Sibawayh | 484–501 | 0 | 0 | 2 | 0 |
| -06 Charlemagne | 502–520 | 0 | 2 | 1 | 1 |
| -07 Bêđa | 521–539 | 0 | 0 | 2 | 0 |
| -08 Tăng Nhất Hạnh | 540–556 | 0 | 1 | 1 | 0 |
| -09 Đỗ Phủ | 557–574 | 0 | 0 | 2 | 0 |
| -10 Trisong Detsen | 575–591 | 0 | 0 | 2 | 2 |
| -11 Ādi Shankara | 592–610 | **1** | 1 | 0 | 1 |
| -12 Yikʼin Chan Kʼawiil | 611–627 | **1** | 0 | 1 | 0 |
| **Tầng nhóm (§C)** | — | 0 | 2 | 1 | 0 |
| **Tổng** | | **5** | **10** | **18** | **7** |

### F-2 · Năm phát hiện BẮT BUỘC, gom lại

1. **Bối cảnh, dòng 413** — "Hai trường phái luật Sunni đầu tiên … thành hình" bị Melchert (nguồn của `-04`) và ghi chú biên tập của chính file bác. Quy tắc 7 + mâu thuẫn chéo.
2. **`-02`, dòng 438** — "Abu Hanifa chết năm 767 **khi đang bị ông giam**" mâu thuẫn với `-04` cách đó 29 dòng.
3. **`-02`, dòng 438** — năm sinh "**709**" không có nguồn; nhập nguyên từ câu thay thế của vòng 1.
4. **`-11`, dòng 598** — "**đề xuất** của Đông phương học châu Âu" bị ghi chú biên tập của chính file bác ("chọn và phổ biến … không phải chế ra nó").
5. **`-12`, dòng 615** — "cao nhất thế giới Maya **thời Cổ điển**" vẫn sai (Toniná 74 m > Đền IV 70 m); là câu thay thế của vòng 1.

**Bốn trong năm là mâu thuẫn chéo trong cùng file hoặc nguồn bị dẫn ngược** — tức đúng hai loại lỗi mà đề bài dự đoán, và **không loại nào bị lint chạm tới** (`build.py --offline`: ch05 ERROR 0 · WARN 0).

### F-3 · Ba ca "mâu thuẫn chéo cùng hình dạng" ngoài ca Shankara/Vācaspati mà đề bài đã biết

Đề bài yêu cầu tìm thêm ca cùng hình dạng với `CH05-CE08-11` ↔ `CH05-CE10-07`. Bốn ca:

| Ca | Thân mục nói | Chỗ khác trong cùng file nói |
|---|---|---|
| **Bối cảnh ↔ ghi chú "Hình dạng của thế kỷ"** | trường phái luật Sunni "thành hình" ở TK 8 | "Melchert … đặt ở thế kỷ 9–10" |
| **`-02` ↔ `-04`** | Abu Hanifa "chết … khi đang bị ông giam" | "**truyền thống chép** ông chết trong ngục" |
| **`-06` ↔ ghi chú "Charlemagne ở nhóm thế kỷ 8"** | "33 trong **46** năm trị vì" | "33 trong **47** năm dương lịch mà triều ông chạm tới" |
| **`-11` ↔ ghi chú "Khung 788–820"** | 788–820 là "**đề xuất** của Đông phương học" | "**chọn và phổ biến** một niên đại vốn có nguồn Ấn Độ, **không phải chế ra nó**" |

Thêm một ca nhẹ hơn, cùng hướng: **`-09` ↔ ghi chú "An Lộc Sơn"** — thân mục viết "biến cố lớn nhất thế kỷ 8 ở Đông Á" (khẳng định), ghi chú viết "**có lẽ** là biến cố đơn lẻ có hệ quả lớn nhất" (dè dặt).

Hình dạng chung đủ rõ để nói thành một quy tắc cho vòng sau: **khi một khối ghi chú biên tập được sửa, phải dò lại mọi thân mục đã mượn chữ của khối ấy.** Cả bốn ca trên đều sinh ra đúng theo cách đó — ghi chú được siết lại, thân mục thì giữ nguyên câu cũ.
