# Cổng chọn người — Chapter 5, nhóm CE08 (TK 8, 701–800 CN)

Bình duyệt độc lập. Người rà **không** viết nhóm CE06/CE07.
Ngày rà: 2026-10-31. Trạng thái: **HOÀN TẤT** — báo cáo được viết tăng dần, mỗi phần lưu ngay khi xong; năm vấn đề, danh sách 12 người, danh sách bị loại, D5 và câu hỏi cỡ nhóm đều đã có kết luận.

**Đường đi nhanh:** §1 cổng Wikidata · §2 năm vấn đề phải quyết (viết theo thứ tự quyết xong, nên §2.4 đứng trước §2.1 — nội dung không phụ thuộc thứ tự) · §3 khảo sát năm vùng trống · **§4 danh sách 12 người đề xuất** · §5 ứng viên bị loại · §6 D5 Việt Nam · §7 cỡ nhóm, phương pháp, và ghi chú quyền riêng tư.

**Quy ước đánh dấu trong báo cáo này**
- `[KIỂM ĐƯỢC]` — đã tự mở nguồn, có mã HTTP + kích thước + nội dung thật.
- `[KHÔNG KIỂM ĐƯỢC]` — không mở được / không tìm được nguồn gốc; **không** được viết vào atlas như sự kiện.
- `[SUY LUẬN HIỆN ĐẠI]` — kết luận của học giới, không phải nguồn đương thời.
- `[NIÊN ĐẠI QUY ƯỚC]` — mốc dựng ngược từ truyền thống muộn, không có chứng cứ đương thời.

**User-Agent dùng cho mọi lệnh mạng trong vòng này:** `history-atlas/0.1 (research)`.
Ghi chú kỹ thuật cho Owner: `atlaslib/common.py` dòng `PROJECT["user_agent"]` đang nhúng **địa chỉ email cá nhân** vào User-Agent của mọi request build. Vòng rà này cố ý **không** dùng chuỗi đó. Xem §7.3.

---

## §0 · Việc đã làm trước khi kết luận

Đọc trước khi tra mạng: `CONTRIBUTING.md` (toàn bộ, đặc biệt quy tắc 6, 7, 8 và bốn quy ước `vùng:` ở dòng 66–71), `content/ch05.md` (hai nhóm CE06/CE07 đã viết + toàn bộ `## Ghi chú biên tập`), `atlaslib/common.py` (`FIELDS`, `REGIONS`, `CONFIDENCE`, `DATE_TOLERANCE`), `content/ch90.md` (phụ lục Việt Nam), `data/persons.json` (248 bản ghi).

**Kiểm chéo quy tắc 6 — đã chạy bằng script, không dò tay.** Đối chiếu 20 Q-ID ứng viên CE08 với toàn bộ `data/persons.json`: **không ai trong 20 người đã có mục ở nơi khác trong atlas**. Nghĩa là mọi người bị loại ở §3 đều là ứng viên bị loại thật, và danh sách ở §3 dùng được thẳng cho mục "Ứng viên mạnh đã bị loại" mà không vi phạm quy tắc 6.

**Thống kê nền (tự tính lại từ `data/persons.json`, không chép từ `reports/stats.txt`):** 208 người ở track chính (ch90 đã loại trừ đúng).

| Vùng | Số | % |
|---|---|---|
| Trung Đông/Bắc Phi | 69 | 33,2% |
| Châu Âu | 56 | 26,9% |
| Đông Á | 51 | 24,5% |
| Nam Á | 25 | 12,0% |
| Châu Phi hạ Sahara | 4 | 1,9% |
| Trung Á | 1 | 0,5% |
| Đông Nam Á | 1 | 0,5% |
| Châu Mỹ | 1 | 0,5% |
| Châu Đại Dương | 0 | 0,0% |

Con số khớp với đề bài. Một chi tiết đáng nói ngay: **người Trung Á duy nhất của atlas là Zarathustra** (`CH02-BCE06-09`), mà chính trường `nơi:` của mục ấy ghi "đông Iran **hoặc** Trung Á" — tức ô Trung Á của atlas đang đứng trên một người mà vị trí địa lý còn là câu hỏi mở. Điều này làm cho §2.5 (vùng của Tây Tạng) và §6.4 (ứng viên Trung Á) nặng hơn bình thường: Trung Á không chỉ ít người, nó gần như chưa có người nào chắc chắn.

---

## §1 · Cổng Wikidata: 20 ứng viên, tự mở kiểm

Gọi `wbgetentities` (props=labels|claims, languages=vi|en) qua 3 request, User-Agent `history-atlas/0.1 (research)`. **HTTP 200**, kích thước lần lượt **440.172 B**, **898.417 B**, **365.049 B** — tức nội dung thật, không phải trang chặn.

Cột "độ chính xác" là `precision` của Wikidata: `9` = năm, `10` = tháng, `11` = ngày.
Cột "ref" đếm reference **thật**; `P143` (imported from Wikimedia project) và `P2477`/`P214` (BnF/VIAF) được đánh dấu riêng vì chúng **không phải** chứng cứ sử học — chúng là bản ghi thư mục hoặc import từ Wikipedia.

| Q-ID | nhãn en | nhãn vi | P31 | P569 (sinh) | P570 (mất) | chất lượng ref |
|---|---|---|---|---|---|---|
| Q190896 | Abū Ḥanīfa | Abu Hanifa | Q5 | 699-09-05 (prec 11, preferred) / 699 (prec 9) | 767 (prec 9) | tốt — P248 nhiều nguồn |
| Q170046 | Jaafar Al-Sadiq | Ja'far al-Sadiq | Q5 | 702-04-20 (prec 11) / 699 (prec 9) | 765-12-16 (prec 11, **0 ref**) / 765 (prec 9) | trung bình, hai mạch sinh lệch 3 năm |
| Q31066 | Al-Mansur | **(không có nhãn vi)** | Q5 | 713-11 (prec 10, preferred) / 714 | 775-10-07 (preferred, ref = P854 URL) / 775-10-18 | trung bình |
| Q312299 | Malik ibn Anas | Malik ibn Anas | Q5 | 711 (preferred) / 712 / 709 | 795-06-07 (preferred); **796 và 812 bị deprecated** | tốt |
| Q334847 | Ibn Ishaq | **(không có nhãn vi)** | Q5 | 704 (prec 9) | 768 (prec 9) | tốt |
| Q983355 | Sibawayh | **(không có nhãn vi)** | Q5 | 760 (prec 9, ref = P143) | 797 (prec 9) | **yếu** — sinh chỉ có import |
| Q131002 | Harun al-Rashid | Harun Al-Rashid | Q5 (**0 ref**) | 766-02-19 (preferred) / 766-03-07 | **809-03-24** | trung bình |
| Q167852 | Jabir ibn Hayyan | Jabir ibn Hayyan | Q5 | 721 (prec 9) | 815 (prec 9) | **xem §2.2 — ref là hồ sơ thư mục, không phải nghiên cứu** |
| Q154938 | Bede | **Bêđa** | Q5 | 672 (preferred) / 673 | 735-05-25 (preferred) | **tốt nhất nhóm** |
| Q154332 | Alcuin | Alcuin | Q5 | **740 (preferred) / 735 / 724 — ba giá trị, lệch 16 năm** | 804-05-19 | tốt cho P570, yếu cho P569 |
| Q3044 | Charlemagne | Charlemagne | Q5 | 748-04-02 / 742-04-02 / 742-04-10 / 747 — **bốn giá trị, ba cùng rank preferred** | 814-01-28 | P570 rất tốt, P569 hỗn loạn |
| Q3301 | Charles Martel | Charles Martel | Q5 (**0 ref**) | 688-08-23 (prec 11) | 741-10-22 (prec 11, **0 ref**) | yếu so với độ chính xác được khai |
| Q180967 | Ādi Shankara | Adi Shankara | Q5 | **788** (prec 9) | **820** (prec 9) | xem §2.1 — ref là bách khoa thư, không phải Ấn Độ học |
| Q231582 | Padmasambhava | **Liên Hoa Sinh** | Q5 | 717 (ref = **P214 VIAF**) | 762 (ref = **P214 VIAF**) | **rất yếu** — xem §2.5b |
| Q366661 | Tri Songdetsen | Trisong Detsen | Q5 | 742 | **797 (preferred, 0 ref)** / 798 / 800 / 797 | yếu |
| Q7071 | Li Bai | **Lý Bạch** | Q5 | 701-05-19 (prec 11) | 762-11-30 (prec 11) | tốt |
| Q33772 | Du Fu | **Đỗ Phủ** | Q5 | 712 (prec 9, **7 ref**) | 770 (prec 9, **7 ref**) | **tốt nhất nhóm Đông Á** |
| Q710705 | Yi Xing | **Nhất Hạnh** ⚠ | Q5 | 683 (ref = P143) | 727 (ref = P143) | **yếu** — xem §2.4 |
| Q360559 | An Lushan | An Lộc Sơn | Q5 | 703 (ref = P854 URL) | 757-01-29 | yếu–trung bình |
| Q349263 | Shōmu | Shōmu | Q5 | 701-09-18 | 756-06-04 | yếu (chỉ P143) nhưng khớp sử Nhật |

**Ba kết luận rút từ bảng này:**

1. **Tất cả 20 đều P31 = Q5.** Cổng Q-ID của vòng trước đứng vững; không có ca "chi bướm Colias" nào ở đây.
2. **Độ chính xác ngày tháng không đo độ tin cậy.** Charles Martel được ghi tới từng ngày (688-08-23, 741-10-22) mà **P570 không có reference nào** và P31 cũng không. Padmasambhava có ngày sinh–mất tròn trịa 717–762 mà nguồn duy nhất là **VIAF** — một bản ghi thư mục thư viện, không phải một mệnh đề sử học. Đây đúng là quy luật mà Ghi chú biên tập CE06 đã ghi ("năm sinh Wikidata rất hay là suy diễn không nguồn"), nay thêm một biến thể: **niên đại có thể có nguồn mà nguồn ấy lại là catalog thư viện**.
3. **Năm giá trị phải tự chặn, không được chép thẳng:** Sibawayh P569=760 (chỉ import), Alcuin P569 (ba giá trị lệch 16 năm), Charlemagne P569 (bốn giá trị, ba cùng rank `preferred` — Wikidata ở đây tự mâu thuẫn), Padmasambhava 717–762, Trisong Detsen P570 (bốn giá trị 797/798/800).

---

## §2.4 · [ĐÃ QUYẾT] Bẫy nhãn Wikidata: Q710705 "Nhất Hạnh"

**Xác nhận trực tiếp trên Wikidata — bẫy có thật và nặng hơn mô tả trong đề bài.**

Gọi `wbgetentities` cho Q710705 (props=labels|aliases|descriptions|sitelinks): **HTTP 200, 2.314 B**, nội dung thật.

```
labels:    en = "Yi Xing"   |  vi = "Nhất Hạnh"   |  zh = "一行"
aliases:   vi = ["Trương Toại"]
           zh = ["僧一行", "唐一行", "张遂", "一行禅师"]
descriptions: en = "8th-century Buddhist monk and astronomer"
              zh = "中国唐朝天文学家、佛学家、禅师（683-727）"
              vi = (KHÔNG CÓ)
sitelinks: enwiki = "Yi Xing"  |  viwiki = "Nhất Hạnh"  |  zhwiki = "一行"
```

Tra `wbsearchentities` với từ khoá "Nhất Hạnh", ngôn ngữ vi (**HTTP 200**) trả về đúng hai kết quả đầu bảng:

```
Q710705  Nhất Hạnh         — 8th-century Buddhist monk and astronomer
Q310913  Thích Nhất Hạnh   — thiền sư, giảng viên, nhà văn, nhà thơ người Việt Nam (1926–2022)
```

**Vì sao bẫy này nặng hơn một lỗi nhãn thường:**

- Nó **không phải lỗi Wikidata**. 一行 đọc Hán–Việt đúng là "Nhất Hạnh", và Wikipedia tiếng Việt đặt tên bài đúng như vậy. Thiền sư hiện đại 釋一行 Thích Nhất Hạnh lấy pháp hiệu trùng chữ. Hai người **thật sự trùng tên trong tiếng Việt** — không có cách phiên âm nào tránh được.
- Q710705 **không có description tiếng Việt**. Mọi công cụ hiển thị theo ngôn ngữ vi sẽ in ra đúng hai chữ "Nhất Hạnh" trần, không kèm gì để phân biệt. Đây là chỗ một vòng biên tập sau rất dễ "sửa" nhầm.
- Độc giả tiếng Việt gặp Thích Nhất Hạnh (1926–2022) trước nhà sư thế kỷ 8 với xác suất gần như tuyệt đối.

**KHUYẾN NGHỊ DỨT KHOÁT.** Viết trường tên trong atlas là:

> `### CH05-CE08-nn · Tăng Nhất Hạnh (僧一行 Yi Xing, tục danh Trương Toại 張遂)`

Bốn lý do: (a) `僧一行` là **alias có thật trên Wikidata** (zh aliases), không phải tên do atlas bịa ra — chữ 僧 "tăng" là cách thư tịch Hán phân biệt ông; (b) nó giữ đúng âm Hán–Việt mà atlas đang dùng nhất quán cho Trí Di, Huyền Trang, Huệ Năng; (c) tục danh **Trương Toại** là alias tiếng Việt có sẵn trên Wikidata, chặn nhầm lẫn ở lớp thứ hai; (d) không vi phạm quy ước nào — mẫu `Tên (nguyên ngữ, biệt danh)` đã dùng ở `CH05-CE06-07 · Trí Di (智顗 Zhìyǐ, Thiên Thai đại sư)`.

**Kèm theo, bắt buộc:** một câu trong phần văn xuôi của mục nói thẳng ông **không** liên quan tới Thích Nhất Hạnh (1926–2022, `Q310913`), và một dòng trong `## Ghi chú biên tập` ghi lại bẫy này. Lý do phải ghi vào Ghi chú biên tập chứ không chỉ trong mục: quy tắc 8 của `CONTRIBUTING.md` là về **liên kết trỏ đúng ID nhưng sai người** — ở đây rủi ro ngược lại nhưng cùng cơ chế, một vòng sau thấy nhãn Wikidata là "Nhất Hạnh" sẽ tưởng atlas ghi sai tên và "sửa" lại thành nhãn trần.

**Niên đại:** Wikidata ghi 683–727 nhưng cả hai đều chỉ có `P143` (import từ Wikipedia), **không có reference thật** → `độ tin cậy niên đại: Trung bình`, không phải Cao.

---

## §2.1 · [ĐÃ QUYẾT] Adi Shankara — và một đính chính cho chính đề bài

### Nguồn đã tự mở kiểm

| URL | HTTP | Kích thước | Nội dung thật? |
|---|---|---|---|
| `https://plato.stanford.edu/entries/shankara/` | **200** | **111.114 B** | **Có** — bài SEP đầy đủ, mục "1. Life and Works" bàn thẳng niên đại |
| `https://plato.stanford.edu/entries/advaita-vedanta/` | **404** | 9.908 B | **Không** — slug này **không tồn tại**; chỉ `shankara` mới có |
| `https://www.advaita-vedanta.org/avhp/dating-Sankara.html` | **200** | **21.831 B** | **Có** — 18.270 ký tự văn bản, khảo luận riêng về niên đại |
| `https://en.wikipedia.org/w/api.php?...titles=Adi%20Shankara` | **200** | **59.922 B** | **Có** — extract đầy đủ, có mục "Dating" |

Ghi lại cái 404 vì nó xác nhận đúng cảnh báo ở `CONTRIBUTING.md` mục 2: slug SEP **phải mở mới biết**. `shankara` có thật; `advaita-vedanta` không.

### Gốc của từng khung niên đại

**(1) 788–820 CN — và đây là chỗ đề bài ghi sai.**
Đề bài mô tả khung này là "truyền thống Śṛṅgeri". **Không đúng, theo cả hai nguồn đã mở.** Thực tế:

- Wikipedia mục "Scholarly datings" ghi rõ: 788–820 **do giới học thuật cuối TK 19 – đầu TK 20 đề xuất, theo sau K.P. Tiele**, rồi được Max Müller, Macdonell, Pathak, Deussen và Radhakrishnan chấp nhận theo lệ. Đây là một **khung của Đông phương học châu Âu**, không phải của maṭha.
- Truyền thống Śṛṅgeri ghi **ngược lại**: niên đại truyền thống của chính Śṛṅgeri là **483 TCN**, và các maṭha lớn đều đặt ông ở **thế kỷ 5 TCN** (Kanchipuram 509 TCN, Govardhan 507 TCN, Dvārakā 491 TCN, Jyotirmath 485 TCN, Puri 484 TCN).
- Bản ghi Śṛṅgeri thật sự nói gì: Śaṅkara sinh vào **năm thứ 14 đời một vua tên Vikramāditya**, mà bản ghi **không cho biết là Vikramāditya nào**. Giới nghiên cứu hiện đại đọc đó là Vikramāditya của triều Cālukya ở Bādāmi — nhiều khả năng **Vikramāditya II (733–746)**. Tức bản ghi Śṛṅgeri, đọc theo cách được chấp nhận hiện nay, **ủng hộ khung sớm**, không ủng hộ 788–820.

→ Phải sửa tiền đề này trước khi viết, nếu không mục sẽ dẫn ngược nguồn đúng kiểu quy tắc 7.

**(2) k. 700–750 CN — khung của học giới hiện nay.** Đây là một **lập luận chặn hai đầu**, không phải một con số truyền lại:
- *Chặn đầu sớm (k. 650):* tác phẩm của Śaṅkara mang dấu vết tranh biện với các tác giả Phật giáo và Mīmāṃsā thế kỷ 5–7. Lập luận mạnh nhất, nêu ở cả hai nguồn: Śaṅkara **trích nguyên văn Dharmakīrti** — và Sureśvara xác nhận việc trích này. Dharmakīrti được định niên qua lời chứng của Huyền Trang, người sang Ấn Độ thời Harṣa (606–647). Vậy Śaṅkara **sau Dharmakīrti**, nhiều khả năng sau cả Huyền Trang.
- *Chặn đầu muộn (k. 800):* Vācaspati Miśra viết sớ cho tác phẩm của Śaṅkara, và sớ ấy được định niên vào nửa đầu thế kỷ 9.
- Người lập luận dài nhất cho khung này: **Nakamura 1983: 48–88** (*A History of Early Vedānta Philosophy: Part One*, Motilal Banarsidass) — SEP dẫn đích danh kèm số trang và ghi rằng ông "bàn các thuyết định niên khác nhau một cách chi tiết".

**(3) Cuối TK 7 – đầu TK 8 — Potter 1981: 14–15, 116–119**, dựa trên niên đại của Maṇḍanamiśra, một người Advaita cùng thời (xem Thrasher 1979 về niên đại Maṇḍanamiśra).

**(4) Các khung bị bác:** 44–12 TCN (Ānandagiri); TK 5 TCN (các maṭha) — trang advaita-vedanta.org chỉ ra khung TK 5 TCN "thực ra không đến từ truyền thống cổ nào", mà mới được nêu trong khoảng hai thế kỷ gần đây; 805–897 (Venkiteswara); 680 (Bhandarkar).

### Chốt: cả hai khung chính đều đặt ông ở thế kỷ 8

Câu mở đầu của SEP, nguyên văn: Śaṅkara *"flourished during the eighth century CE"*. Khung 788–820 là khung **duy nhất** đẩy phần hoạt động của ông sang thế kỷ 9 — và đó đúng là khung mà học giới gần đây đã đặt dấu hỏi. Nói cách khác, nếu atlas xếp ông vào CE09 thì nó đang theo **một khung thiểu số đang bị bác**, chứ không phải theo một lựa chọn trung lập.

### KHUYẾN NGHỊ DỨT KHOÁT

| Trường | Giá trị |
|---|---|
| nhóm | **CE08** (thế kỷ 8) |
| `năm:` | **`k. 700 – k. 750 CN`** |
| `độ tin cậy niên đại:` | **`Thấp`** |
| `vùng:` | Nam Á |
| `lĩnh vực:` | Triết học, Tôn giáo/Tâm linh |

**Vì sao `Thấp` giải quyết trọn vấn đề cảnh báo lint — đã đọc code, không đoán.** `atlaslib/lint.py` dòng 289–292:

```python
tol = C.DATE_TOLERANCE.get(p["confidence"])
if tol is None:
    rep.info(pw, "độ tin cậy Thấp — bỏ qua đối chiếu niên đại")
    continue
```

`DATE_TOLERANCE["Thấp"] is None` (`common.py` dòng 82), nên nhánh này **`continue` trước khi tới vòng so P569/P570**, và chỉ ghi một dòng `info`, **không phải `warn`**. Tức viết `k. 700 – k. 750 CN` với độ tin cậy `Thấp` sẽ **không sinh cảnh báo lệch năm nào** dù Wikidata ghi 788–820. Hai vế của thế lưỡng nan trong đề bài **không thật sự xung đột** — cơ chế để thoát đã có sẵn trong lint.

Lưu ý: vòng kiểm nhãn (`nhãn Wikidata ... không khớp tên`) chạy **trước** nhánh này và vẫn chạy bình thường — nhãn vi là "Adi Shankara", khớp, nên cũng không có cảnh báo.

**`Thấp` ở đây là mô tả đúng chứ không phải mẹo né lint.** SEP viết thẳng: *"There are no dependable historical records of Śaṅkara's life beyond his written works which provide few biographical clues."* Các tiểu sử *Śaṅkaravijaya* được soạn **nhiều thế kỷ sau khi ông mất** (bản Mādhavīya thường đặt ở TK 14). Đây là `[NIÊN ĐẠI QUY ƯỚC]` đúng nghĩa: không có bi ký, không có tiền đúc, không có văn bản đương thời định danh ông — chỉ có chặn hai đầu bằng văn bản của người khác.

**Hai việc bắt buộc khi viết mục:**
1. Nêu thẳng trong phần văn xuôi rằng niên đại của ông là tranh luận mở, và rằng 788–820 là khung cũ của Đông phương học chứ **không** phải truyền thống maṭha.
2. Liên kết **Kế thừa từ: `CH05-CE07-10` (Pháp Xứng / Dharmakīrti) · phản bác · trực tiếp**. Đây là liên kết có giá trị thật: chính việc Śaṅkara trích nguyên văn Dharmakīrti là chứng cứ định niên mạnh nhất, và quan hệ tư tưởng giữa hai người đúng là **phản bác**. Kiểm nghịch niên đại: Pháp Xứng ghi `k. 600 – k. 660`, Śaṅkara `k. 700 – k. 750` → đúng thứ tự, cách nhau khoảng một thế kỷ, không vi phạm quy tắc 5 về "ứng viên cùng thời" vì đây là quan hệ kế thừa chứ không phải so sánh đồng đại. **Mở mục đích đã đọc tên** (quy tắc 8): `CH05-CE07-10 · Pháp Xứng (धर्मकीर्ति Dharmakīrti)` — đúng người.

---

## §2.2 · [ĐÃ QUYẾT] Jabir ibn Hayyan — LOẠI khỏi CE08

### Câu hỏi của đề bài: có công trình sau 2010 đảo lại Kraus không?

**Không. Công trình sau 2010 củng cố Kraus, và còn rút mất cái chân chống cuối cùng của "Jabir thế kỷ 8".**

Hai công trình sau 2010 đã kiểm được sự tồn tại qua **Crossref API** (vì cả hai nhà xuất bản đều chặn bot — xem phần kiểm URL bên dưới):

| | Delva 2017 | Capezzone 2020 |
|---|---|---|
| DOI | `10.1163/22142371-12340030` | `10.1017/S0041977X20000014` |
| Crossref | **HTTP 200, 28.897 B** | **HTTP 200, 15.783 B** |
| Tác giả | Thijs Delva | Leonardo Capezzone |
| Nhan đề | "The Abbasid Activist Ḥayyān al-ʿAṭṭār as the Father of Jābir b. Ḥayyān: An Influential Hypothesis Revisited" | "The solitude of the Orphan: Ǧābir b. Ḥayyān and the Shiite heterodox milieu of the third/ninth–fourth/tenth centuries" |
| Tạp chí | *Journal of Abbasid Studies* 4(1): 35–61 | *BSOAS* 83(1): 51–73 |
| Năm | 2017-06-15 | 2020-02 |

> **Cảnh báo kỹ thuật cho vòng sau — đúng loại bẫy mà Ghi chú biên tập CE06 đã ghi.**
> `https://doi.org/10.1163/22142371-12340030` → chuyển hướng tới `brill.com/view/journals/jas/4/1/article-p35_2.xml` và trả **HTTP 202 với 0 byte**. Đây chính là mẫu "thread diễn đàn trả 202" của vòng trước: mã không phải lỗi, nhưng **không có nội dung**.
> `https://doi.org/10.1017/S0041977X20000014` → `cambridge.org` trả **HTTP 429, 1.478 B**, nội dung là trang "Too many automated requests from this network" của Varnish.
> **Không được dẫn hai URL ấy như nguồn đã đọc.** Dẫn theo thư mục (tạp chí, tập, số, trang) đã xác minh qua Crossref.
> Thêm một chi tiết để vòng sau khỏi "sửa" nhầm: Crossref ghi publisher của Delva 2017 là **Walter de Gruyter GmbH**, không phải Brill — *Journal of Abbasid Studies* đã đổi nhà xuất bản sau khi bài ra đời. Cả hai cách ghi đều không sai.

### Delva 2017 làm gì

Giả thuyết khiến "Jabir thế kỷ 8" nghe hợp lý là của **Holmyard (1927)**: cha Jabir là **Ḥayyān al-ʿAṭṭār**, một nhà hoạt động proto-Shi'a vận động cho nhà Abbas đầu thế kỷ 8, bị hành quyết không lâu sau năm 721 — từ đó **suy ra năm sinh Jabir k. 721**. Delva 2017 bác giả thuyết này trên hai điểm: Ḥayyān al-ʿAṭṭār nhiều khả năng **sống ít nhất tới k. 744**, và với tư cách *mawlā* của bộ tộc **Nakhaʿ**, ông rất khó là cha của Jabir, người được cho là thuộc bộ tộc **Azd**.

**Hệ quả trực tiếp lên Wikidata, và đây là điểm phải ghi:** `Q167852` ghi **P569 = 721**. Con số 721 ấy **chính là** suy diễn từ giả thuyết Holmyard mà Delva 2017 đã tháo. Wikidata đang chở một niên đại mà công trình chuyên ngành gần nhất đã rút nền. Đây là ca "khớp Wikidata không đồng nghĩa với đúng" ở dạng rõ nhất của cả Chapter 5.

### Vì sao không thể viết ông như "nhà giả kim thế kỷ 8"

Bằng chứng, xếp theo loại — không trộn:

- `[NGUỒN ĐƯƠNG THỜI]` — **không có.** Jabir **không được nhắc trong bất kỳ nguồn sử nào trước k. 900**.
- `[NGUỒN MUỘN]` — người đầu tiên viết tiểu sử về ông là nhà thư mục Baghdad **Ibn al-Nadīm** trong *Fihrist*, **năm 987**, tức khoảng **hai thế kỷ** sau đời ông theo truyền thống. Ngay thời Ibn al-Nadīm đã có người khẳng định Jabir **chưa từng tồn tại**.
- **Lập luận từ im lặng, và nó rất mạnh:** các nhà viết tiểu sử Shi'a sớm — al-Barqī (mất k. 893), al-Kashshī (nửa đầu TK 10), al-Najāshī (983–1058), al-Ṭūsī (995–1067) — soạn những bộ dày về các *môn đồ của Ja'far al-Sadiq*, và **không ai nhắc tới Jabir**. Nếu Jabir là môn đồ nổi bật của Ja'far như truyền thống kể, sự vắng mặt này rất khó giải thích.
- `[SUY LUẬN HIỆN ĐẠI]` — ba lập luận định niên văn bản: phần lớn **thuật ngữ triết học** trong tập Jābir chỉ được đặt ra khoảng **giữa thế kỷ 9**; một số **văn bản triết học Hy Lạp được trích** trong tập chỉ được dịch sang tiếng Ả Rập vào **cuối thế kỷ 9**; và một phần quan trọng của tập bàn **triết học tôn giáo Shi'a sơ kỳ** chỉ thấy ở nguồn **cuối TK 9 – đầu TK 10**. → Niên đại **k. 850–950** cho tập Jābir "đã được chấp nhận rộng rãi trong giới nghiên cứu hiện đại".
- **Mạch phản biện, ghi cho công bằng:** Fuat Sezgin (1971) bác Kraus và quy toàn bộ tập cho một nhân vật lịch sử thế kỷ 8. Và ngay trong cách đọc chủ lưu vẫn để ngỏ rằng tập "có thể dựa trên một lõi thế kỷ 8 sớm hơn", đã bị san định nhiều lần. Nhưng **Sezgin 1971 là công trình trước 2010**, và không có công trình sau 2010 nào mà vòng này tìm được đứng về phía ông.

### KHUYẾN NGHỊ DỨT KHOÁT: loại khỏi CE08

**Loại.** Ba lý do, lý do thứ hai là lý do cứng:

1. **Tiền lệ của chính atlas.** Ghi chú biên tập CE06 đã loại Yajaw Teʼ Kʼinich II với đúng câu này: *"lý do duy nhất để đưa ông vào là một mệnh đề mà chính chuyên gia hàng đầu đang bác"*. Ở đây mệnh đề bị bác còn nặng hơn — không phải "ông có phải tác nhân của sự kiện X không", mà "ông có tồn tại ở thế kỷ 8 không".
2. **Quy tắc §3 tự nó loại ông, không cần xét gì thêm.** Atlas xếp người theo **giai đoạn ảnh hưởng chính**. Giai đoạn ảnh hưởng của tập Jābir là **thế kỷ 9–10** — đó là lúc nó được soạn, san định và bắt đầu lưu hành. Kể cả nếu một Jabir lịch sử thế kỷ 8 có thật, **ảnh hưởng của ông không diễn ra ở thế kỷ 8**. Đây đúng là cùng một lỗi mà Ghi chú biên tập đã ghi với Āryabhaṭa: *"danh sách nháp xét nhân vật theo năm sinh, còn atlas xếp theo giai đoạn ảnh hưởng"*.
3. **Viết "chính cuộc tranh luận" làm nội dung mục thì mục ấy không còn là mục về một người.** Template §5 đòi `năm:`, `nơi:`, `lĩnh vực:`, quan hệ kế thừa — tất cả đều giả định một cá nhân định vị được. Một mục mà trường `năm:` phải ghi "không xác định được là người hay là tập văn bản" thì đã hỏng ở cấp cấu trúc, chứ không phải ở cấp văn phong.

**Nhưng đừng để mất nội dung này — hai chỗ đặt nó, cả hai đều tốt hơn một mục CE08:**

- **(a) Viết vào `## Ghi chú biên tập` của Chapter 5** thành một khối riêng, song song với khối Yajaw Teʼ Kʼinich II của CE06. Nó dạy đúng bài học mà atlas đang tích lũy, và nó chặn vòng sau khỏi "phát hiện lại" Jabir như một ô trống dễ lấp.
- **(b) Nhắc một câu trong mục `Ja'far al-Sadiq`** (đã chọn, xem §4). Truyền thống gắn Jabir làm môn đồ của Ja'far, nên chỗ tự nhiên nhất để nói "và truyền thống ấy không có chứng cứ sớm" chính là mục Ja'far. Một câu, không rào dài.
- **(c) Nếu Owner vẫn muốn tập Jābir có mặt trong atlas**, chỗ đúng là **CE09 hoặc CE10**, với nhãn `[Tranh cãi lịch sử]` (`LABELS` trong `common.py` có sẵn giá trị này, và `lint.py` dòng 286–288 cho nhãn ấy triệt tiêu cảnh báo P31) và `độ tin cậy niên đại: Thấp`. Đó là quyết định của nhóm CE09/CE10, **không** phải của CE08. Vòng này không khuyến nghị thêm vì chưa rà nhóm đó.

---

## §2.3 · [ĐÃ QUYẾT] Charlemagne — **CE08**, không phải CE09 (tôi không đồng ý với tiền đề của đề bài)

Đề bài viết "Theo §3 thì CE09 có lý hơn CE08". Sau khi đọc §3, đọc code định nghĩa nhóm, và kiểm lại niên đại, **tôi kết luận ngược lại**, và đây là lập luận.

### Dữ kiện đã kiểm

Wikipedia `Charlemagne` (**HTTP 200, 63.310 B**, extract đầy đủ 62.790 ký tự):
- Vua người Frank **từ 768**; vua người Lombard **từ 774**; hoàng đế **từ 800**; mất **28-01-814**.
- Lễ đăng quang: *"[at St.] Peter's Basilica on **Christmas Day 800**, Leo proclaimed Charlemagne 'emperor of the Romans' (Imperator Romanorum) and crowned him."* → **25-12-800**.
- Ông trao đổi sứ giả với **Harun al-Rashid** trong **thập niên 790** vì lợi ích chung ở bán đảo Iberia.

### Lập luận 1 — lễ đăng quang nằm TRONG nhóm CE08, không phải ngoài

Chạy `atlaslib.common.group_range` (không đoán):

```
CE07 (601, 700)      CE08 (701, 800)      CE09 (801, 900)
```

Nhóm CE08 kết thúc ở **năm 800 bao gồm cả năm 800**. Lễ đăng quang ngày **25-12-800** rơi vào **tuần cuối cùng của nhóm CE08** — sớm hơn ranh giới đúng **sáu ngày**. Nghĩa là "hành vi định nghĩa" mà đề bài nêu **không** đẩy ông sang CE09; nó là sự kiện gần như cuối cùng của CE08.

### Lập luận 2 — đếm theo giai đoạn ảnh hưởng thì CE08 thắng áp đảo

| | thuộc CE08 (701–800) | thuộc CE09 (801–900) |
|---|---|---|
| Số năm trị vì | **33 năm** (768–800) | 14 năm (801–814) |
| Diệt vương quốc Lombard | **774** | |
| Chiến tranh Saxon | **từ 772** | |
| Thu phục Bavaria | **788** | |
| Chiến dịch Avar | **791–796** | |
| Alcuin tới triều đình | **782** | |
| Sứ bộ với Harun al-Rashid | **thập niên 790** | |
| Đăng quang hoàng đế | **25-12-800** | |
| Mang tước hiệu hoàng đế | | 801–814 |

Toàn bộ việc **tạo ra** đế quốc, và cả việc **được phong** đế, nằm trong thế kỷ 8. Thế kỷ 9 chỉ chứa phần ông **giữ** tước hiệu đã có.

### Lập luận 3 — xếp ông vào CE09 chính là lỗi mà §3 sinh ra để chặn

Ghi chú biên tập của chính Chapter 5 đã ghi, trong ca Āryabhaṭa: *"danh sách nháp xét nhân vật theo **năm sinh**, còn atlas xếp theo **giai đoạn ảnh hưởng**."* Đẩy Charlemagne sang CE09 là xếp ông theo **năm mất (814)** — cùng một lỗi, chỉ đổi đầu. Āryabhaṭa được giữ ở CE05 vì *Āryabhaṭīya* hoàn thành năm 499, dù ông mất năm 550 tức thế kỷ 6. **Cùng nguyên tắc ấy, Charlemagne thuộc CE08.**

### Lập luận 4 — lint không ép bên nào, nên đây thuần là quyết định nội dung

`atlaslib/lint.py` dòng 125 chỉ cảnh báo khi **đời sống không giao** với khoảng nhóm:

```python
rep.warn(pw, f"đời sống ... không giao với nhóm {g['id']} ...")
```

748–814 giao với CE08 (701–800) **và** giao với CE09 (801–900). Lint im lặng ở cả hai phương án. Không có sức ép kỹ thuật nào; chọn theo §3 là chọn duy nhất phải làm.

### KHUYẾN NGHỊ DỨT KHOÁT

| Trường | Giá trị |
|---|---|
| nhóm | **CE08** |
| `năm:` | **`k. 748–814 CN`** |
| `độ tin cậy niên đại:` | **`Trung bình`** |
| `vùng:` | Châu Âu |
| `lĩnh vực:` | Chính trị/Nhà nước, Giáo dục |

**Vì sao `k. 748` chứ không phải `748`, và vì sao `Trung bình`:** Wikidata `Q3044` có **bốn** giá trị P569 (748-04-02, 742-04-02, 742-04-10, 747), trong đó **ba** cùng mang rank `preferred` — tức Wikidata tự mâu thuẫn và không chỉ ra được giá trị nào thắng. Năm sinh Charlemagne là vấn đề mở thật sự trong sử học Carolingian, không phải lỗi dữ liệu. Với `Trung bình` (dung sai ±25 năm) mọi giá trị trong khoảng 742–748 đều qua lint; với `Cao` (±5) thì vẫn qua, nhưng `Cao` sẽ là một tuyên bố sai về chất lượng bằng chứng. **P570 = 814-01-28 thì rất chắc** — nhưng độ tin cậy là một trường cho cả cặp, nên phải lấy theo vế yếu hơn.

**Hệ quả dây chuyền phải xử lý cùng lúc:** nếu Charlemagne ở CE08 thì **Alcuin (mất 804)** cũng ở CE08 theo đúng lập luận ấy — công việc của Alcuin ở triều đình Aachen là **782–796**, và nhiệm kỳ Tours **796–804**; phần thế kỷ 9 chỉ là bốn năm cuối. Hai mục này phải cùng nhóm, nếu không atlas sẽ tách một cặp thầy–trò cùng một chương trình cải cách ra hai chương.

---

## §2.5 · [ĐÃ QUYẾT] Vùng của Padmasambhava và Trisong Detsen — **Đông Á**, và một khuyến nghị kèm theo

### Kết luận về `vùng:` — không có chỗ cho do dự

**Cả hai ghi `vùng: Đông Á`.** Bản nháp xếp "Trung Á" là **sai**, và nó sai theo đúng một lỗi mà atlas đã bác hai lần.

Chuỗi tiền lệ, đã mở từng mục ra đọc:

1. `CONTRIBUTING.md` dòng 70, nguyên văn: *"`REGIONS` không có ô nào cho Nội Á / thế giới thảo nguyên. Hệ quả: cao nguyên Mông Cổ ghi **Đông Á** (Mặc Đốn thiền vu, `CH03-BCE02-12`), còn 'Trung Á' trên thực tế chỉ còn dùng cho vành đai Transoxiana–Iran đông."*
2. `CH05-CE07-11` **Tùng Tán Cán Bố** — `nơi: thung lũng Yarlung và Lhasa, cao nguyên Tây Tạng | vùng: Đông Á`. Cùng cao nguyên, cùng triều đại, **cùng quốc gia** với hai người đang xét.
3. Ghi chú biên tập CE07 đã ghi thẳng cám dỗ này và từ chối nó: *"Ghi 'Trung Á' sẽ nâng con số Trung Á từ 0,5% lên khoảng 1%, và đó chính là lý do không được làm."*
4. `CONTRIBUTING.md` dòng 71 — tiền lệ Kanishka: đề xuất chuyển Nam Á → Trung Á đã bị **bác**.

Padmasambhava và Trisong Detsen hoạt động ở **cùng cao nguyên Tây Tạng, trong cùng Đế quốc Thổ Phồn**, chỉ cách Tùng Tán Cán Bố hơn một thế kỷ. Ghi họ là "Trung Á" trong khi người sáng lập triều đại ấy ghi "Đông Á" sẽ tạo ra **mâu thuẫn nội bộ ngay trong một chapter** — đúng loại lỗi mà bản thảo CE07 từng mắc khi `CH05-CE06-03` ghi Sasanian sụp năm 651 còn mục Umar ghi khác.

**Với Padmasambhava có thêm một bẫy riêng phải chặn:** truyền thống cho ông là người **Oḍḍiyāna** (thường định vị ở thung lũng Swat, nay thuộc Pakistan). Một vòng biên tập sau rất dễ lấy nơi sinh ấy để ghi "Nam Á" hoặc "Trung Á". `CONTRIBUTING.md` dòng 68 quy ước 1 chặn việc đó: **vùng là nơi hoạt động chính, không phải nơi sinh** — như Plotinus sinh ở Ai Cập mà ghi Châu Âu. Hoạt động của Padmasambhava, theo mọi nguồn, là **ở Tây Tạng**.

### Tôi có cho rằng tiền lệ ấy sai không? — Không, nhưng nó đang che một khuyết tật phải ghi ra

Đề bài mời tôi nói thẳng nếu thấy tiền lệ sai. **Tiền lệ đúng, với từ vựng hiện có.** Trong khuôn khổ 9 giá trị `REGIONS`, không có lựa chọn nào tốt hơn cho cao nguyên Tây Tạng, và việc đổi nhãn để lấy con số đẹp đã bị cấm minh thị.

Nhưng khuyết tật thì phải ghi, và vòng này tìm được một dữ kiện làm nó rõ hơn trước: **người "Trung Á" duy nhất của atlas là Zarathustra** `CH02-BCE06-09`, mà trường `nơi:` của chính mục ấy ghi **"đông Iran hoặc Trung Á"**. Nghĩa là con số *Trung Á = 0,5%* hiện đang đứng trên **một người mà vị trí địa lý còn là câu hỏi mở**. Cộng với việc Tây Tạng và thảo nguyên Mông Cổ đều bị dồn vào Đông Á, kết luận phải viết vào Ghi chú biên tập là:

> Con số Trung Á của atlas **không đo lịch sử Nội Á**; nó đo một từ vựng chín ô không có chỗ cho Nội Á. Sau Chapter 5, "Trung Á" trong atlas thực tế chỉ còn nghĩa **Transoxiana–Iran đông**, và ngay cả ô ấy cũng chưa có người nào chắc chắn. Mọi so sánh tỷ lệ vùng phải đọc kèm giới hạn này.

Đây là lựa chọn đúng thứ hai mà `CONTRIBUTING.md` dòng 71 cho phép: *"ghi vào Ghi chú biên tập rằng vùng ấy trống và vì sao."*

### Khuyến nghị kèm theo: giữ Trisong Detsen, **loại Padmasambhava**

Hai người này không ngang nhau về bằng chứng, và chênh lệch đủ lớn để quyết định suất.

**Trisong Detsen — bằng chứng vững** (Wikipedia `Trisong Detsen`, **HTTP 200, 7.731 B**):
- `[NGUỒN GẦN ĐƯƠNG THỜI]` **Trụ đá Kar-cun** do người kế vị **Tridé Songtsen (trị vì 800–815)** dựng, chép rằng dưới triều Trisong Detsen "các điện thờ Tam Bảo được lập bằng việc xây chùa ở trung tâm và ở biên giới, Samye (Bsam-yas) ở Brag-mar, v.v." — tức bi ký do **thế hệ kế tiếp** dựng, không phải truyền thống muộn hàng thế kỷ.
- `[NGUỒN ĐƯƠNG THỜI]` Old Tibetan Annals / Old Tibetan Chronicle (bản chép Đôn Hoàng) — cùng khối tư liệu mà mục Tùng Tán Cán Bố đã dùng.
- Mốc tuyệt đối, kiểm được: **763** chiếm Trường An, buộc Đường Đại Tông bỏ kinh thành; **783** định lại biên giới với nhà Đường; **791** sắc chỉ lấy Phật giáo làm quốc giáo; **792–794** cuộc tranh biện Samye.

**Padmasambhava — bằng chứng yếu, và yếu theo đúng kiểu atlas đã từng từ chối** (Wikipedia `Padmasambhava`, **HTTP 200, 39.512 B**):
- Lewis Doney: tính lịch sử của ông từng bị các nhà Tạng học trước đây đặt vấn đề, **nay được chấp nhận một cách "thận trọng" (cautiously accepted)** — chấp nhận thận trọng, không phải xác lập.
- Nguồn biên niên sớm nhất: **Testament of Ba (Dba' bzhed), k. TK 9–12** — một khoảng rộng ba thế kỷ.
- Các bản chép Đôn Hoàng có nhắc một tantrika tên Padmasambhava gắn với nghi quỹ kīlaya, **nhưng không gắn ông với Trisong Detsen**. Đây là chi tiết quyết định: bằng chứng sớm nhất **không** chống đỡ cho chính mệnh đề mà một mục CE08 sẽ cần.
- Tiểu sử đầu tiên là **Zangling-ma** của **Nyangral Nyima Özer (1124–1192)** — tức **khoảng bốn thế kỷ sau**. Khối "tám hoá thân", terma, hàng phục quỷ thần đều hình thành **từ khoảng thế kỷ 12**.

**Hai lý do loại, cả hai đều là tiền lệ của chính atlas:**

1. **Quy tắc §3 đặt ông ở thế kỷ 12, không phải thế kỷ 8.** Giai đoạn ảnh hưởng chính của Padmasambhava — với tư cách nhân vật định hình phái Nyingma, hệ terma và guru yoga — **bắt đầu từ TK 12 với Nyangral Nyima Özer**. Đây **cùng một lập luận** đã dùng để loại Jabir ở §2.2, và phải áp dụng nhất quán, nếu không atlas sẽ loại Jabir vì một lý do mà nó tha cho Padmasambhava.
2. **Tiền lệ Tì-ni-đa-lưu-chi.** Ghi chú biên tập CE06 giữ Tì-ni-đa-lưu-chi ở phụ lục chứ không đưa lên atlas chính vì *"tiểu sử ông phụ thuộc gần hoàn toàn vào Thiền uyển tập anh, bộ sách soạn thế kỷ 13–14, tức sau ông bảy thế kỷ."* Padmasambhava đứng ở đúng vị trí ấy — tiểu sử phụ thuộc một bộ soạn sau bốn thế kỷ — mà lại là ứng viên cho **atlas chính**, nơi thanh chắn phải **cao hơn** phụ lục chứ không thấp hơn.

**Suất Tây Tạng vì vậy là một, không phải hai: Trisong Detsen.** Xem §4 để biết suất còn lại đi đâu.

> **Ghi chú kiểm nguồn — một URL phải đánh dấu `[KHÔNG KIỂM ĐƯỢC]`.**
> `https://ocbs.org/.../Cantwell-Mayer-Early-Representations-of-Padmasambhava-copy.pdf` trả **HTTP 200, 4.343.149 B, `application/pdf` hợp lệ (PDF 1.3)** — file có thật, kích thước thật. Nhưng đây là **bản quét ảnh**, không rút được lớp văn bản, nên vòng này **không xác minh được bài ấy lập luận gì**. Theo quy tắc 7 (phải biết nguồn *lập luận gì*, không chỉ nó nói *về cái gì*), **không được dẫn bài này** cho tới khi có người đọc được nội dung. Tương tự `https://austriaca.at/0xc1aa5572%200x001bccee.pdf` (**HTTP 200, 725.746 B, PDF 1.4, 27 trang**) về Pelliot tibétain 44 — file thật, nội dung **chưa đọc được**, chưa dẫn.

---

# §3 · Khảo sát năm vùng trống

Nguyên tắc trả lời, theo đúng yêu cầu: mỗi vùng kết thúc bằng **một ứng viên có tên + Q-ID tôi tự mở + niên đại tuyệt đối + luận điểm viết được**, hoặc bằng **`KHOẢNG TRỐNG TƯ LIỆU` kèm lý do tư liệu cụ thể**. Không có ô nào kết thúc bằng một câu bỏ lửng.

Mọi Q-ID dưới đây tôi **tự gọi `wbsearchentities` + `wbgetentities`** trong vòng này, không lấy từ trí nhớ (tiền lệ con bướm Colias ở Ghi chú biên tập CE07).

## §3.1 · Châu Mỹ — **CÓ ỨNG VIÊN**, và là ứng viên mạnh

**Yikʼin Chan Kʼawiil** (còn gọi *Ruler B*), ajaw của Tikal.

| | |
|---|---|
| Q-ID | **Q2620151** — tự kiểm: `P31 = Q5`, nhãn en `Yik'in Chan K'awiil`, **không có nhãn vi** (không có bẫy đồng âm) |
| Wikidata P569 | **không có** |
| Wikidata P570 | **`somevalue`** — tức Wikidata khai thẳng "có giá trị nhưng không biết" |
| `năm:` đề xuất | **`trị vì 734–766 CN`** |
| `độ tin cậy niên đại:` | **`Trung bình`** |

**Vì sao `trị vì` chứ không phải năm sinh–mất.** Đây là ca mà quy ước `năm:` của CONTRIBUTING được viết ra để xử lý: *"vua không có năm sinh → `trị vì 745–727 TCN`"*. Dạng này còn có một tác dụng kỹ thuật phải nói rõ: `atlaslib/common.py` dòng 133 có `NON_BIO_YEARS_RE = re.compile(r"^(trị vì|hoạt động)\b", re.I)`, nên lint **bỏ qua** đối chiếu P569/P570 cho mục này. Điều đó ở đây **không phải mẹo lách**, mà là cách ghi trung thực duy nhất: Wikidata **không có** năm sinh và khai năm mất là `somevalue`.

**Niên đại tuyệt đối, từ bi ký đương thời.** `[BI KÝ ĐƯƠNG THỜI]` Wikipedia `Yik'in Chan K'awiil` (**HTTP 200, 1.997 B**, extract 1.708 ký tự):
- Lên ngôi **8 tháng 12 năm 734** — ngày chính xác đến từng ngày, vì Long Count của Maya là **lịch đếm ngày tuyệt đối**, không phải niên đại quy ước dựng ngược.
- Đánh bại **Calakmul năm 736**, **El Perú năm 743**, **Naranjo năm 744**.
- Tư liệu gắn với ông: *"Stelae 5, 20? and 3?; Temple 4 Lintels 2 and 3; Lintel from Structure 5D-52"*.
- Năm mất không chắc: *"before 734 – c. 746/766?"*. Vì vậy `Trung bình`, không phải `Cao`.

**Luận điểm trung tâm viết được:** *Trong hai thế kỷ, chính trị Maya Cổ điển được tổ chức quanh thế đối đầu Tikal–Calakmul. Yikʼin Chan Kʼawiil là người phá vỡ nó: trong tám năm (736–744) ông lần lượt hạ Calakmul rồi hai đồng minh El Perú và Naranjo, và chuyển chiến thắng thành đá — Đền IV, kim tự tháp cao nhất thế giới Maya. Niên đại của toàn bộ chuỗi ấy không do người đời sau dựng lại: nó được chính triều đình ông khắc bằng Long Count, hệ đếm ngày tuyệt đối, nên ngày lên ngôi của ông xác định đến từng ngày trong khi năm sinh của Charlemagne cùng thế kỷ vẫn còn bốn phương án.*

Câu cuối là một **cặp so sánh có thật trong cùng nhóm CE08** — đúng loại liên kết mà quy tắc 5 đòi hỏi (kiểm cả hai vế: Charlemagne k. 748–814, Yikʼin trị vì 734–766, hai người **thật sự cùng thời**).

> Lưu ý rule 6: `CH05-CE07-12 · Kʼinich Janaabʼ Pakal` (Palenque, 603–683) **đã có mục riêng**, nên khi viết mục Yikʼin **không được** nêu Pakal như "ứng viên bị loại"; phải ghi rõ *"có mục riêng ở nhóm CE07"*.

## §3.2 · Đông Nam Á — **CÓ ỨNG VIÊN** (nhưng xem §4 về việc tôi không xếp được vào 12 suất)

**Lưu ý đầu tiên, theo đúng cảnh báo của đề bài:** `Q42798` **Borobudur là một công trình, không phải người** — `P31` của nó không phải `Q5`. Không được đưa vào atlas. Bẫy này có thật vì tên "Borobudur" nổi hơn tên mọi cá nhân liên quan.

Hai ứng viên có bi ký đương thời, niên đại tuyệt đối:

| | Sanjaya | Panangkaran |
|---|---|---|
| Q-ID (tự kiểm) | **Q3107477**, `P31 = Q5` | **Q7130030**, `P31 = Q5` |
| Wikidata P569/P570 | **không có giá trị nào** | **không có giá trị nào** |
| Bi ký | **Bia Canggal**, Sanskrit, **732 CN** | **Bia Kalasan**, **700 Śaka = 778 CN** |
| Nguồn kiểm | WP `Canggal inscription` (**HTTP 200, 2.619 B**) | WP `Kalasan inscription` (**HTTP 200, 6.177 B**) |
| `năm:` đề xuất | `hoạt động 732 CN` | `hoạt động 778 CN` |
| độ tin cậy | `Thấp` | `Thấp` |

`[BI KÝ ĐƯƠNG THỜI]` Bia Canggal 732 ghi việc dựng một *lingam* theo lệnh Sanjaya, *"con của Sannaha (em gái của Sanna)"*, và ông tự xưng vua toàn cõi Mataram. `[SUY LUẬN HIỆN ĐẠI / NGUỒN MUỘN]` Tên Sanjaya, Sanna, Sannaha cũng xuất hiện trong *Carita Parahyangan*, **soạn khoảng thế kỷ 16** — **không được dùng làm nguồn tiểu sử**; đó là khoảng cách tám thế kỷ.

`[BI KÝ ĐƯƠNG THỜI]` Bia Kalasan 778 là **bi ký đầu tiên ở Indonesia nêu tên dòng họ Śailendra** (*Sailendravamça*), ghi việc Maharaja *Tejapurnapana Panangkaran* / *Dyah Pancapana Panamkarana* cho dựng đền thờ Tārā (đền Kalasan) và một *vihāra* cho tăng chúng, cùng việc cúng làng Kalaça cho Tăng-già.

**Luận điểm trung tâm viết được (Panangkaran):** *Bia Kalasan 778 là mốc đầu tiên có niên đại tuyệt đối cho cái tên Śailendra, và nó ghi một ông vua Java chuyển bảo trợ hoàng gia từ Śiva sang Phật giáo Đại thừa — bước mở đầu của chương trình xây đền sẽ kết thúc ở Borobudur. Nhưng bia ấy cũng cho thấy giới hạn của tư liệu: ta biết ông ra lệnh gì vào năm nào, mà không biết ông sinh hay mất năm nào.*

**Vì sao `Thấp` và vì sao `hoạt động`:** Wikidata **không có P569 lẫn P570** cho cả hai người. `hoạt động` kích hoạt `NON_BIO_YEARS_RE`, và `Thấp` thì `DATE_TOLERANCE["Thấp"] is None` khiến `lint.py` `continue` trước vòng so niên đại. Cả hai đều là cách ghi trung thực, không phải lách.

**Ứng viên thứ ba đã xét và loại — Jayavarman II:** lễ ở Phnom Kulen thường được quy ước là **802 CN**, tức **nhóm CE09, không phải CE08**; hơn nữa niên đại ấy đến từ **bia Sdok Kok Thom, dựng năm 1052**, tức **250 năm sau**. Đây là `[NIÊN ĐẠI QUY ƯỚC]`, không phải bi ký đương thời.

## §3.3 · Trung Á (nghĩa hẹp Transoxiana–Iran đông) — **CÓ ỨNG VIÊN**, và vùng này không hề trống như con số 0,5% gợi ý

Đây là phát hiện có hệ quả lớn nhất của §3. Thế kỷ 8 **chính là** thế kỷ mà vành đai Transoxiana–Khurasan quyết định lịch sử Á–Âu, và nó có **hai** ứng viên đạt chuẩn, không phải không có ai.

### Ứng viên A — **Abu Muslim al-Khurasani** (đề xuất lấy suất, xem §4)

| | |
|---|---|
| Q-ID (tự kiểm) | **Q335210** — `P31 = Q5` (ref: P143) |
| P569 | **718** (prec 9, ref = P143) |
| P570 | **755-02** (prec 10, **0 ref**) |
| `năm:` đề xuất | **`k. 718–755 CN`** |
| `độ tin cậy niên đại:` | **`Trung bình`** |

Nguồn kiểm: WP `Abu Muslim` (**HTTP 200, 12.839 B**, extract 12.221 ký tự). Bản thân bài ghi khoảng sinh **"718 to 727"** — biên độ 9 năm, nằm gọn trong dung sai ±25 của `Trung bình`, vượt dung sai ±5 của `Cao`. Vì vậy **không được ghi `Cao`**.

Mốc tuyệt đối: được phái về Khurasan **745/6**; phát động giai đoạn công khai của cách mạng **747**; chiếm **Merv tháng 12-747 (hoặc tháng 1-748)**, đánh bại tổng đốc Umayyad Nasr ibn Sayyar; làm tổng đốc Khurasan sau 750; bị **al-Mansur xử tử năm 755** tại al-Madaʾin.

**Vấn đề `vùng:` phải xử lý thẳng, vì nó đụng đúng điều cấm của CONTRIBUTING dòng 71.**
Nơi hoạt động chính của Abu Muslim là **Merv và Khurasan** — nằm trong vành đai Transoxiana–Iran đông, tức **đúng định nghĩa còn lại của "Trung Á"** theo CONTRIBUTING dòng 70. Theo quy ước 1 (*vùng là nơi hoạt động chính, không phải nơi sinh* — và cũng không phải nơi chết), ông ghi **`vùng: Trung Á`**.

Tôi ý thức rằng kết luận này **cũng** làm giảm áp lực 8-ứng-viên-Trung-Đông. Vì vậy phải nói rõ: **đây không phải lý do**. Nếu Abu Muslim hoạt động ở Damascus hay Kufa thì ông là Trung Đông/Bắc Phi, và tôi vẫn đề xuất ông. Phép thử để Chủ dự án tự kiểm: **đảo ngược lợi ích**. Giả sử atlas đang thừa người Trung Á và thiếu người Trung Đông — lập luận "nơi hoạt động chính là Merv" có đổi không? Không. Đó là dấu hiệu nó là lập luận địa lý chứ không phải lập luận thống kê. Tiền lệ Kanishka bị bác vì kinh đô Purushapura **thật sự** ở Nam Á; ở đây Merv **thật sự** ở Trung Á.

**Luận điểm trung tâm viết được:** *Cách mạng Abbasid không nổ ra ở trung tâm Ả Rập mà ở rìa đông của caliphate, và nó thắng. Abu Muslim là người tổ chức cuộc nổi dậy ấy ở Khurasan — một tỉnh biên giới nơi người Ả Rập định cư và người Iran bản địa đã hoà vào nhau qua mấy thế hệ chiến tranh, và cùng ghét Damascus. Kết quả là trọng tâm chính trị của thế giới Hồi giáo dịch từ Syria về Iraq, và trọng tâm văn hoá dịch về phía Iran. Phần thưởng của ông là bị chính caliph mà ông dựng lên xử tử năm 755 — và chuỗi khởi nghĩa mang tên ông ở Iran suốt một thế kỷ sau cho thấy việc giết ông đã không xoá được ông.*

### Ứng viên B — **Divashtich** (không lấy suất; lý do ở §5)

| | |
|---|---|
| Q-ID (tự kiểm) | **Q753663** — `P31 = Q5` |
| P569 | `+0650` nhưng **precision 7 (thế kỷ)** — tức Wikidata khai "thế kỷ 7", con số 650 là chỗ giữ chỗ |
| P570 | **722** (prec 9) |

**Bằng chứng ở đây thuộc hạng cao nhất mà atlas từng gặp cho một nhân vật Trung Á: văn khố cá nhân của chính ông còn nguyên.**
`[VĂN KIỆN ĐƯƠNG THỜI]` Kiểm trực tiếp hai nguồn:
- UNESCO *Memory of the World*, `https://www.unesco.org/en/memory-world/collection-documents-mount-mugh` — **HTTP 200, 261.407 B**, văn bản thật 1.894 ký tự: *"The documents show the life of Dewashtich, the ruler of Penjikent principality, until his defeat by Arab forces in 722. The collection includes everyday business records, letters, contracts, diplomatic exchange and spy reports."* Năm ghi danh: **2025**.
- Sasanika (UC Irvine), `https://sites.uci.edu/sasanika/mount-mugh-documents/` — **HTTP 200, 71.920 B**, văn bản thật 914 ký tự: *"approximately 80 documents … the most comprehensive corpus of Sogdian texts ever found within Sogdiana"*, từ văn khố riêng của Ḏēwaštīč. Công bố gốc: Freiman, Livšic, Bogolyubov & Smirnova, *Sogdiiskie dokumenty s gory Mug*, 3 tập, Moskva 1962–63.

Mốc tuyệt đối: cai trị Panjikant **từ k. 706**; thần phục Umayyad **712** sau cuộc xâm lăng của Qutayba ibn Muslim; cầm đầu khởi nghĩa chống Ả Rập **720**; thua trận **722**; bị al-Harashi **đóng đinh trên một tháp im lặng Hoả giáo**, đầu gửi về Iraq.

**Vì sao vẫn không lấy suất:** xem §5. Tóm tắt: ông đạt rất cao ở **bằng chứng** nhưng thấp ở **(a) phạm vi** và **(d) counterfactual** — ông thua, triều đại ông chấm dứt, và Transoxiana vẫn Hồi giáo hoá đúng như khi ông không tồn tại. Bốn tiêu chí của CONTRIBUTING đo **ảnh hưởng**, không đo **mức độ được ghi chép**. Đây là phân biệt phải giữ cho chặt, nếu không atlas sẽ dần biến thành bản đồ các văn khố còn sót.

## §3.4 · Châu Phi hạ Sahara — **có một tên, nhưng kết luận là KHOẢNG TRỐNG TƯ LIỆU**

Đây là vùng duy nhất tôi phải trả lời bằng cả hai nửa, và tôi ghi rõ cả hai thay vì chọn nửa gọn hơn.

### Nửa thứ nhất: có đúng một cá nhân có tên và có niên đại

**Kyriakos xứ Makuria** — **Q1148493** (tự kiểm, nhãn en `Kyriakos of Makuria`, mô tả `monarch`). WP `Kyriakos of Makuria` (**HTTP 200, 1.978 B**, extract **chỉ 1.772 ký tự** — độ dài ấy tự nó là một dữ kiện).

- `fl. c. 748`. Tên có dạng Old Nubian ⲕⲩⲣⲓⲁⲕⲟⲥ.
- Sự kiện chính: **đem quân vào Ai Cập Umayyad** để cứu giáo hoàng Alexandria Michael I đang bị giam, k. **748**, tiến tới tận **Fustat**, buộc tổng đốc thả Michael I. Đây là một hành vi vi phạm hiệp ước **Baqt** giữa Nubia và Ả Rập.
- Con số "100.000 quân" bài viết tự bác: *"this figure is highly unlikely"*. `[SUY LUẬN HIỆN ĐẠI]`

**Theo tiền lệ của chính atlas, vùng của ông sẽ là `Châu Phi hạ Sahara`:** `CH02-BCE08-06` Piye (Napata) và `CH02-BCE07-09` Taharqa (Napata–Memphis) đều ghi `Châu Phi hạ Sahara`, và Makuria nằm trên cùng khúc sông Nile ấy. Không có mâu thuẫn vùng ở đây.

### Nửa thứ hai: vì sao tôi vẫn kết luận **KHOẢNG TRỐNG TƯ LIỆU**

Lý do là **tư liệu**, không phải cảm tính, và là cả bốn loại mà đề bài liệt kê:

1. **Kyriakos chỉ tồn tại qua một nguồn muộn, và nguồn ấy tự mâu thuẫn với các nguồn khác về chính vị trí của ông trong danh sách vua.** Bài viết ghi: *History of the Patriarchs of Alexandria* xếp triều ông sau Markos, *"other authorities place it between Merkurios and his son Zacharias I"*. Khi hai hệ thống không thống nhất nổi ông đứng ở đâu trong danh sách vua, niên đại `c. 748` là `[NIÊN ĐẠI QUY ƯỚC]` dựng ngược từ triều giáo hoàng Michael I (743–767), **không** phải từ bi ký Nubia. Với bốn tiêu chí (a)(b)(c)(d), ông không qua nổi (c) và (d).
2. **Aksum: thế kỷ 8 đúng là khoảng tối tư liệu, và lý do đo được.** WP `Kingdom of Aksum` (**HTTP 200, 45.751 B**): *"ceased production of coins in the early eighth century"*. Tiền đúc là **nguồn đương thời chính** mà atlas đã dùng cho Ezana (`CH04-CE04-09`) và Kaleb (`CH05-CE06-09`) — *"Ezana's coins and inscriptions make the change from pre-Christian imagery to Christian symbolism around 340"*. Thế kỷ 8 là đúng thế kỷ **nguồn ấy tắt**. Vua có tên tiếp theo, Degna Djan, thuộc **thế kỷ 9** và đến qua truyền thống muộn.
3. **Kanem và Sahel: có nhà nước, chưa có cá nhân có tên.** WP `Kanem–Bornu Empire` (**HTTP 200, 51.056 B**): *"The earliest known written record of Kanem comes from the Arab geographer Al-Ya'qubi in **872**"* — tức **thế kỷ 9**, và là nguồn **ngoại lai**, không phải bản địa. *"Later tradition identifies mai Susam as the first ruler"* — **truyền thống muộn**. Vua Hồi giáo đầu tiên là **mai Hu thế kỷ 11**. Nghĩa là: ở thế kỷ 8 có **thực thể chính trị**, không có **cá nhân được ghi tên bởi nguồn đương thời**.
4. **Bờ Đông Phi: chữ viết đến muộn hơn ba thế kỷ.** Bi ký Hồi giáo có niên đại cổ nhất vùng này là **bia Kufic ở nhà thờ Kizimkazi Dimbani, Zanzibar, 1107 CN** — WP `Kizimkazi Mosque` (**HTTP 200, 1.159 B**): *"According to a preserved kufic inscription, the mosque was built in 1107 CE."* Đó là **ba thế kỷ sau** khung CE08. Khảo cổ ở các cảng Swahili sớm cho **niên đại**, không cho **tên người**.

> **Một URL phải ghi `[KHÔNG KIỂM ĐƯỢC]`:** truy vấn Wikipedia `Shanga, Kenya` trả **HTTP 200, 91 B, không có extract, `pageid = -1`** — tức **trang không tồn tại** dù mã là 200. Lại đúng cái bẫy đề bài cảnh báo. Không được dẫn di chỉ Shanga qua slug này.

**Kết luận viết vào Ghi chú biên tập:** *Châu Phi hạ Sahara ở thế kỷ 8 không thiếu lịch sử; nó thiếu **nguồn viết đương thời nêu tên cá nhân**. Ba hệ chữ viết từng phục vụ vùng này — tiền đúc và bi ký Ge'ez ở Aksum, tiếng Hy Lạp và Old Nubian ở Nubia, tiếng Ả Rập ở Sahel và bờ Đông — thì hệ thứ nhất **tắt** đúng vào thế kỷ 8, hệ thứ hai chỉ còn vọng lại qua một biên niên Ai Cập soạn muộn và tự mâu thuẫn, hệ thứ ba **chưa tới** (872 cho Kanem qua nguồn ngoại lai, 1107 cho bờ Đông). Bốn mục Châu Phi hạ Sahara hiện có của atlas đều rơi vào các thế kỷ mà **tiền đúc hoặc bi ký còn hoạt động**. Đó không phải trùng hợp: nó là hình dạng của tư liệu, và con số 1,9% đo điều đó.*

## §3.5 · Châu Đại Dương — **KHOẢNG TRỐNG TƯ LIỆU**, và đây là ca rõ ràng nhất trong năm ca

Lý do tư liệu gồm ba tầng, tầng nào cũng đủ một mình.

**Tầng 1 — ở thế kỷ 8, phần lớn Đông Polynesia chưa có người ở.**
`[NGHIÊN CỨU HIỆN ĐẠI, ĐÃ KIỂM]` Wilmshurst, Hunt, Lipo & Anderson, *"High-precision radiocarbon dating shows recent and rapid initial human colonization of East Polynesia"*, **PNAS 108(5): 1815–1820**, công bố **27-12-2010**. Kiểm qua **Crossref API: HTTP 200, 9.982 B** — tên bài, tạp chí, tập/số/trang, 4 tác giả, `type: journal-article`, tất cả khớp. Phân tích lại **1.434 niên đại carbon phóng xạ** cho kết quả: quần đảo Society được định cư **k. 1200–1290 CN**, và toàn Đông Polynesia lan toả cực nhanh trong **thế kỷ 13**.

Nghĩa là Hawaiʻi, Aotearoa và Rapa Nui ở **thế kỷ 8 chưa có cư dân**. Không thể có ứng viên từ nơi chưa có người. Đây là dạng khoảng trống mạnh nhất có thể có.

> Ghi chú về quy tắc 7 — **không được giấu tranh luận**: niên đại rút ngắn này **bị phản biện** ngay trên cùng tạp chí (Mulrooney et al.; và bài *"Recalibrating Polynesian prehistory"*, cùng PNAS 2011). Tôi **không kiểm được nội dung** hai bài phản biện trong vòng này → `[KHÔNG KIỂM ĐƯỢC]` cho chi tiết của chúng. Nhưng điều đó **không đổi kết luận**: phe phản biện đòi niên đại **sớm hơn**, và ngay cả khung dài nhất cũng không tạo ra **nguồn viết** nào — các tầng 2 và 3 dưới đây độc lập hoàn toàn với tranh luận này.

**Tầng 2 — không có hệ chữ viết nào ở Châu Đại Dương trước tiếp xúc châu Âu.**
Ứng viên duy nhất là **rongorongo** ở Rapa Nui. WP `Rongorongo` (**HTTP 200, 35.733 B**, extract 35.001 ký tự): *"a system of glyphs discovered in the 19th century … that has the appearance of writing or proto-writing"*; *"Numerous attempts at decipherment have been made, but **none have been successful**"*; *"**If** rongorongo does prove to be writing and to be an independent invention…"* — tức ngay cả **tư cách chữ viết** của nó cũng còn là giả thiết. Hiện vật được thu thập **cuối thế kỷ 19**. Và theo tầng 1, Rapa Nui thế kỷ 8 chưa có người. Vậy rongorongo không cứu được ô CE08 dù giải mã được ngày mai.

**Tầng 3 — gia phả truyền miệng không phải nguồn đương thời.**
Tây Polynesia (Tonga, Samoa), Melanesia và Micronesia **đã có người ở** từ lâu trước thế kỷ 8 — nên đây **không** phải khoảng trống dân cư. Nhưng tên người ở các xã hội ấy truyền qua **gia phả truyền khẩu**, chỉ được chép thành văn **từ thế kỷ 19** bởi người sưu tầm châu Âu và bản địa. Khoảng cách **hơn một nghìn năm** giữa sự kiện và lần chép đầu tiên xa hơn mọi ca atlas từng chấp nhận — xa hơn cả hai ca atlas đã **từ chối**: *Thiền uyển tập anh* cách Tì-ni-đa-lưu-chi **bảy thế kỷ** (giữ ở phụ lục) và *Zangling-ma* cách Padmasambhava **bốn thế kỷ** (loại ở §2.5). Áp đúng thanh chắn ấy, không có cái tên Châu Đại Dương nào thế kỷ 8 qua được.

**Kết luận viết vào Ghi chú biên tập:** *Châu Đại Dương giữ con số 0,0% ở Chapter 5, và lý do là tư liệu chứ không phải thiếu tìm: ở thế kỷ 8, nửa đông của vùng này **chưa có cư dân**, còn nửa tây **có cư dân nhưng không có chữ viết**, và tên người ở đó chỉ tới tay ta qua gia phả truyền khẩu chép muộn hơn một nghìn năm. Ô 0,0% này sẽ **chỉ** được lấp ở các chapter sau — và kể cả khi ấy cũng phải lấp bằng nguồn, không bằng thiện chí.*

---

# §4 · Danh sách 12 người đề xuất cho CE08

Mọi Q-ID dưới đây đã qua `wbgetentities` trong vòng này (bảng §1 và §3). Mọi `độ tin cậy niên đại:` được chọn theo **biên độ thật của các giá trị cạnh tranh**, không theo `precision` mà Wikidata khai — kết luận §1.2.

| # | Tên | Q-ID | `năm:` | `vùng:` | `lĩnh vực:` | độ tin cậy |
|---|---|---|---|---|---|---|
| 1 | Abu Muslim al-Khurasani | **Q335210** | `k. 718–755 CN` | **Trung Á** | Chính trị/Nhà nước, Quân sự | Trung bình |
| 2 | Al-Mansur | **Q31066** | `k. 714–775 CN` | Trung Đông/Bắc Phi | Chính trị/Nhà nước | Trung bình |
| 3 | Jaʿfar al-Sadiq | **Q170046** | `k. 702–765 CN` | Trung Đông/Bắc Phi | Tôn giáo/Tâm linh, Luật | Trung bình |
| 4 | Abu Hanifa | **Q190896** | `k. 699–767 CN` | Trung Đông/Bắc Phi | Luật, Tôn giáo/Tâm linh | Trung bình |
| 5 | Sibawayh | **Q983355** | `k. 760 – k. 796 CN` | Trung Đông/Bắc Phi | Ngôn ngữ học | **Thấp** |
| 6 | Charlemagne | **Q3044** | `k. 748–814 CN` | Châu Âu | Chính trị/Nhà nước, Giáo dục | Trung bình |
| 7 | Bêđa (Bede) | **Q154938** | `k. 672–735 CN` | Châu Âu | Sử học, Tôn giáo/Tâm linh | **Cao** |
| 8 | Tăng Nhất Hạnh (Yi Xing) | **Q710705** | `683–727 CN` | Đông Á | Toán học, Khoa học tự nhiên | Trung bình |
| 9 | Đỗ Phủ | **Q33772** | `712–770 CN` | Đông Á | Văn học | **Cao** |
| 10 | Trisong Detsen | **Q366661** | `trị vì 755–797 CN` | **Đông Á** (Tây Tạng) | Chính trị/Nhà nước, Tôn giáo/Tâm linh | Trung bình |
| 11 | Ādi Shankara | **Q180967** | `k. 700 – k. 750 CN` | Nam Á | Triết học, Tôn giáo/Tâm linh | **Thấp** |
| 12 | Yikʼin Chan Kʼawiil | **Q2620151** | `trị vì 734–766 CN` | **Châu Mỹ** | Chính trị/Nhà nước, Nghệ thuật/Kiến trúc | Trung bình |

## §4.1 · Luận điểm trung tâm viết được, từng người

**1. Abu Muslim al-Khurasani** — xem §3.3. *Cách mạng Abbasid thắng từ rìa đông, không từ trung tâm Ả Rập; và người tổ chức nó bị chính caliph mình dựng lên xử tử năm 755.*

**2. Al-Mansur** — `[ĐÃ KIỂM]` WP `Al-Mansur` (**HTTP 200, 23.424 B**): sinh **714** tại Humayma (nay thuộc Jordan), caliph **754–775**, mất **6-10-775**; *"He founded the Round City of Madinat al-Salam in **762**, which became the core of imperial Baghdad and the capital of the caliphate."*
*Luận điểm:* *Al-Saffah lên trước, nhưng người **biến** một cuộc đảo chính thành một nhà nước là al-Mansur: 21 năm cầm quyền, và một quyết định đặt đô mới ở ngã ba Tigris năm 762 đã dời trọng tâm thế giới Hồi giáo khỏi Syria vĩnh viễn. Cái giá của việc dựng nhà nước ấy cũng do chính ông ra lệnh: Abu Muslim bị giết năm 755, Abu Hanifa chết trong ngục Baghdad năm 767 — ba mục trong cùng nhóm CE08 này nối với nhau bằng một người.*
*Vì sao `Trung bình`:* P569 có hai mạch (713-11 preferred / 714) và P570 có hai (775-10-07 có ref P854 / 775-10-18), còn Wikipedia ghi 6-10-775 — **ba ngày mất khác nhau**. `Cao` sẽ là lời khai sai.

**3. Jaʿfar al-Sadiq** — `[ĐÃ KIỂM]` WP `Ja'far al-Sadiq` (**HTTP 200, 50.168 B**): *"born in Medina around 700, and 702 is given in most sources, according to Gleave"*; Imam thứ sáu của cả Twelver lẫn Ismaʿili; *"a transmitter to the Sunni scholars Abu Hanifa and Malik ibn Anas"*.
*Luận điểm:* *Jaʿfar là điểm mà hai nhánh lớn của Hồi giáo vẫn còn chung nhau: người Shiʿa Twelver và Ismaʿili coi ông là Imam, người Sunni coi ông là người truyền hadith đáng tin — và cả Abu Hanifa lẫn Malik ibn Anas đều nhận là học trò ông. Ông cũng là người chọn **đứng ngoài** mọi cuộc nổi dậy của thời mình, kể cả khi được mời; chính lựa chọn ấy, chứ không phải một cuộc khởi nghĩa, định hình Shiʿa giáo thành một truyền thống học thuật sống sót được qua các triều đại thù địch.*
> **`[CẢNH BÁO QUY TẮC 7 — PHẢI VIẾT VÀO MỤC]`** Chính bài Wikipedia ghi: *"more traditions are cited from Jaʿfar than that of the other Imams combined, **although their attribution to him is questionable, making it hard to determine his actual teachings**."* Nghĩa là **không được** viết "Jaʿfar dạy rằng X" từ các tuyển tập hadith. Mục phải nói về **vị trí** của ông, không về **nội dung** gán cho ông. Bỏ qua điểm này là lặp lại lỗi Hansen.

**4. Abu Hanifa** — `[ĐÃ KIỂM]` WP `Abu Hanifa` (**HTTP 200, 27.511 B**): **5-9-699 – 18-6-767**; *"the Hanafi school remains the most widely practised of the Sunni schools"*; dùng **qiyās, istiḥsān, raʾy**; *"he never held an official post as qadi"*; *"died in prison in Baghdad in 767"*.
*Luận điểm:* *Abu Hanifa chưa bao giờ làm quan toà — ông bị tù dưới **cả** Umayyad **và** Abbasid vì từ chối chức qāḍī, và chết trong ngục. Nhưng chính trường phái ông xây bằng suy lý (qiyās, istiḥsān, raʾy) lại trở thành hệ luật được áp dụng rộng nhất trong thế giới Sunni, từ Trung Á và Nam Á tới Thổ Nhĩ Kỳ, Balkan và châu Phi. Đây là ca mẫu mực cho thấy ảnh hưởng lâu dài và quyền lực đương thời là hai thứ khác nhau.*
*Vì sao `Trung bình` dù Wikidata khai `precision 11`:* các nguồn cổ điển cho **bốn** năm sinh — 699 (đa số), 696, 689, 680. Biên độ 19 năm. `Cao` (±5) là khai man.
> **Ghi chú vùng — phép thử đối xứng với Abu Muslim.** Bài viết ghi *"Abu Hanifa came from Central Asia"* và liệt kê Kabul, Nasa, Termez trong các nơi sinh có thể. Nhưng nơi hoạt động chính của ông là **Kufa** (và chết ở Baghdad), nên ông ghi **Trung Đông/Bắc Phi**, theo đúng quy ước 1. Hai mục này là cặp kiểm chứng của nhau: Abu Muslim sinh ở Kufa mà hoạt động ở Merv → **Trung Á**; Abu Hanifa có thể sinh ở Trung Á mà hoạt động ở Kufa → **Trung Đông/Bắc Phi**. Quy tắc được áp **cùng một chiều** cho cả hai, và nó đẩy hai người về **hai phía ngược nhau**. Đó là bằng chứng nội tại rằng §3.3 không phải thao tác thống kê.

**5. Sibawayh** — `[ĐÃ KIỂM]` WP `Sibawayh` (**HTTP 200, 14.158 B**): người Ba Tư, nhà ngữ pháp hàng đầu của trường phái Basra; học trò của Yunus ibn Habib và **al-Khalil ibn Ahmad al-Farahidi**; cuộc tranh luận *al-Masʾalah al-Zunbūrīyah* với al-Kisaʾi trước tể tướng Yahya ibn Khalid.
*Luận điểm:* *Quyển **al-Kitāb** của Sibawayh mô tả tiếng Ả Rập một cách hệ thống vào đúng lúc thứ tiếng ấy đang trở thành ngôn ngữ hành chính và học thuật của một đế quốc trải từ Iberia tới Sindh — và nó vẫn là sách quy chiếu sau 1.200 năm. Nghịch lý đáng viết nằm ở chỗ: quyển sách sống sót gần như nguyên vẹn, còn con người thì hầu như không. Nguồn tiểu sử sớm nhất còn lại, Ibn Qutaybah, chỉ viết được chừng này về ông: ông là Amr ibn Uthman, chủ yếu là nhà ngữ pháp, tới Baghdad, cãi nhau với các nhà ngữ pháp ở đó, bị làm nhục, về lại một thị trấn Ba Tư và chết ở đó khi còn trẻ.*
*Vì sao `Thấp` — và đây là chỗ phải sửa so với bảng §1:* bài viết cho **hai khung chết loại trừ nhau** — *"died there between 177/793 and 180/796"* **hoặc** *"he died in Basra in 161/777"*. Biên độ **19 năm**, và hai khung còn khác **cả nơi chết**. Wikidata ghi 797, lại là một giá trị thứ ba. Thêm nữa P569 của ông **chỉ có ref P143** (import từ Wikipedia) — tức không có nguồn nào cả. Với biên độ ấy, `Trung bình` (±25) **vẫn qua lint**, nhưng `Thấp` mới là lời khai đúng, và `Thấp` khiến `lint.py` `continue` trước vòng so niên đại nên cũng không sinh cảnh báo. **Chọn `Thấp`.**

**6. Charlemagne** — xem §2.3 đầy đủ. *Hành vi định nghĩa của ông — lễ đăng quang 25-12-800 — rơi vào sáu ngày cuối cùng của nhóm CE08.*

**7. Bêđa (Bede)** — `[ĐÃ KIỂM]` WP `Bede` (**HTTP 200, 49.369 B**): *Historia ecclesiastica gentis Anglorum* hoàn thành **k. 731**; *"Bede implies that he was then in his fifty-ninth year, which would give a birth date in 672 or 673"*; *"He also helped to popularise the practice of dating forward from the birth of Christ (Anno Domini)"*; mất **26-5-735** tại Jarrow.
*Luận điểm:* *Thói quen ghi "năm 2026" bắt nguồn từ một tu sĩ ở một tu viện Northumbria. Dionysius Exiguus nghĩ ra cách tính Anno Domini từ thế kỷ 6, nhưng chính Bede — bằng việc dùng nó xuyên suốt một bộ sử được đọc khắp châu Âu Latin — đã biến nó thành mặc định. Và ông làm điều đó trong lúc viết bộ sử đầu tiên coi "người Anh" là một dân tộc. Đây là mục hiếm hoi trong nhóm mà **mọi niên đại đều kiểm được**, vì phần lớn thông tin về đời ông do chính ông viết ra ở chương cuối bộ sử ấy.*
*Vì sao `Cao`, và một khác biệt phải ghi:* Wikidata P570 = **735-05-25**, Wikipedia ghi **26-5-735** (lễ Thăng Thiên). Lệch **một ngày**, cùng năm — trong dung sai ±5 của `Cao` một cách thoải mái. Niên đại sinh 672/673 đến từ **lời tự khai của chính Bede**, loại bằng chứng tốt nhất nhóm này có. Đây là mục duy nhất tôi cấp `Cao` cho một người châu Âu thế kỷ 8.

**8. Tăng Nhất Hạnh (僧一行 Yi Xing, tục danh Trương Toại 張遂)** — cách ghi tên bắt buộc và lý do ở **§2.4**; **không được** rút gọn thành "Nhất Hạnh".
`[ĐÃ KIỂM]` WP `Yi Xing` (**HTTP 200, 16.565 B**, extract 15.952 ký tự): **683–727**; chủ trì cuộc **khảo trắc thiên-địa** của triều Đường; cùng **Lương Lệnh Toản** chế thiên cầu chạy bằng nước có **cơ cấu hồi (escapement)** — Needham: *"the first escapement came, in +725"*; mất năm **727** khi đang đi cùng hoàng đế.
*Luận điểm:* *Năm 724–725, triều Đường cho đo bóng nắng ở một chuỗi trạm trải dài bắc–nam hàng nghìn cây số; giới nghiên cứu hiện đại đọc đó là phép đo cung kinh tuyến đầu tiên trong lịch sử, và kết quả cho độ dài một độ kinh tuyến khá sát số hiện đại. Người chủ trì là một tăng sĩ Mật tông. Cùng năm ấy, ông và Lương Lệnh Toản lắp vào thiên cầu chạy nước một cơ cấu hồi — tổ tiên của mọi đồng hồ cơ.*
> **`[CẢNH BÁO QUY TẮC 7]`** Không được viết rằng Nhất Hạnh "đo chu vi Trái Đất". Chính bài viết bác: *"Yi Xing, **who did not know the Earth was spherical**, did not conceptualize his measurements in these terms."* Phép đo là có thật, cách diễn giải "đo cung kinh tuyến" là **`[SUY LUẬN HIỆN ĐẠI]`** đặt lên trên nó. Mục phải tách hai tầng ấy ra.
*Vì sao `Trung bình`:* P569 và P570 của Q710705 **chỉ có ref P143**. Dù 683/727 khớp sử Đường, chất lượng tham chiếu Wikidata ở mức thấp nhất, nên không cấp `Cao`.

**9. Đỗ Phủ** — `[ĐÃ KIỂM]` WP `Du Fu` (**HTTP 200, 28.083 B**): **712–770**; *"Nearly 1,500 poems attributed to him survive"*; *"The An Lushan rebellion, which began in 755, displaced him and his family and shaped much of his later writing"*; *"Most of what is known of Du Fu's life comes from his poems"*; đời sau gọi ông là **Thi sử** và **Thi thánh**.
*Luận điểm:* *Đỗ Phủ là ca hiếm khi danh hiệu "Thi sử" đúng theo nghĩa đen về tư liệu: gần như tất cả những gì ta biết về đời ông đều rút từ chính thơ ông, và loạn An Lộc Sơn — biến cố lớn nhất của thế kỷ 8 ở Đông Á — đến với hậu thế một phần qua con mắt của một viên quan nhỏ bị nó đẩy đi lưu lạc. Ảnh hưởng của ông lên thơ chữ Hán, kể cả thơ Việt Nam, kéo dài hơn một nghìn năm.*
*Vì sao `Cao`:* P569 712 và P570 770 đều có **7 tham chiếu** — hồ sơ tốt nhất của cả nhóm Đông Á (kết luận §1).
> Rule 6: `CH90-CE19_20-01 · Nguyễn Du` **có mục riêng** ở phụ lục. Nếu mục Đỗ Phủ nhắc tới ảnh hưởng lên thơ Việt, phải ghi rõ Nguyễn Du *"có mục riêng ở phụ lục"*, không được nêu như ứng viên bị loại.

**10. Trisong Detsen** — bằng chứng và vùng ở **§2.5**. `[ĐÃ KIỂM]` WP `Trisong Detsen` (**HTTP 200, 7.731 B**): vua thứ 38 của Tây Tạng, **755–797**, lên ngôi năm 755 lúc 13 tuổi (khớp P569 = 742), **thoái vị năm 797** nhường ngôi cho Muné Tsenpo.
*Luận điểm:* *Năm 763, quân Tây Tạng vào Trường An và lập một hoàng đế của riêng họ; năm 783 họ buộc nhà Đường ký lại đường biên. Cùng người ấy, cùng triều ấy, đưa Phật giáo lên thành quốc giáo bằng sắc chỉ năm 791 và cho tổ chức cuộc tranh biện Samye 792–794 để chọn giữa đường tu Ấn Độ và đường tu Thiền Trung Hoa — lựa chọn ấy định hình Phật giáo Tây Tạng cho đến hôm nay. Trụ đá Kar-cun do chính người kế vị ông dựng xác nhận việc lập chùa Samye, nên đây không phải truyền thống muộn.*
*Vì sao `trị vì` và `Trung bình`:* P570 của Q366661 có **bốn** giá trị (797 preferred nhưng **0 ref**, 798, 800, 797). Dạng `trị vì` kích hoạt `NON_BIO_YEARS_RE` nên lint bỏ qua đối chiếu — và đó là cách ghi trung thực, vì cái chắc chắn ở đây là **khoảng trị vì**, không phải khoảng sống.

**11. Ādi Shankara** — toàn bộ lập luận ở **§2.1**. *Khung 788–820 không phải "truyền thống Śṛṅgeri"; nó là sản phẩm của học thuật cuối TK 19.*

**12. Yikʼin Chan Kʼawiil** — xem **§3.1**.

## §4.2 · Bảng phân bố vùng

| Vùng | CE08 | Atlas trước CE08 | Atlas sau CE08 |
|---|---|---|---|
| Trung Đông/Bắc Phi | **4** | 69 (33,2%) | 73 (**33,2%**) |
| Châu Âu | **2** | 56 (26,9%) | 58 (26,4%) |
| Đông Á | **3** | 51 (24,5%) | 54 (24,5%) |
| Nam Á | **1** | 25 (12,0%) | 26 (11,8%) |
| Trung Á | **1** | 1 (0,5%) | 2 (**0,9%**) |
| Châu Mỹ | **1** | 1 (0,5%) | 2 (**0,9%**) |
| Châu Phi hạ Sahara | 0 | 4 (1,9%) | 4 (1,8%) |
| Đông Nam Á | 0 | 1 (0,5%) | 1 (0,5%) |
| Châu Đại Dương | 0 | 0 (0,0%) | 0 (0,0%) |
| **Tổng** | **12** | **208** | **220** |

Ba điều đáng đọc từ bảng này:

1. **Trung Đông/Bắc Phi giữ nguyên 33,2%.** Đề bài lo rằng 8 ứng viên Trung Đông trên 12 suất sẽ làm lệch — đúng: 8/12 = 67%, gấp đôi tỷ lệ hiện hành. **4/12 = 33,3%** trùng khít tỷ lệ atlas đang có. Nghĩa là cắt từ 8 xuống 4 không phải là trừng phạt vùng ấy; nó là giữ nguyên trạng. Và với Abu Muslim tính là Trung Á, thế giới Hồi giáo vẫn chiếm **5/12** số mục của nhóm — tương xứng với một thế kỷ mà cách mạng Abbasid, bốn trường phái luật và ngữ pháp Ả Rập cùng định hình.
2. **Trung Á và Châu Mỹ cùng tăng gấp đôi — từ 1 lên 2.** Con số vẫn thảm, nhưng đây là lần đầu hai ô ấy nhúc nhích, và nhúc nhích bằng **hai người có nguồn đương thời** (văn khố Mugh / bi ký Long Count), không bằng hạ thanh chắn.
3. **Ba ô vẫn đứng yên, và §3 đã ghi lý do tư liệu cho từng ô**, không bỏ lửng ô nào.

## §4.3 · Bảng phân bố lĩnh vực

| Lĩnh vực | CE08 | Ai |
|---|---|---|
| Chính trị/Nhà nước | **5** | Abu Muslim, Al-Mansur, Charlemagne, Trisong Detsen, Yikʼin |
| Tôn giáo/Tâm linh | **5** | Jaʿfar, Abu Hanifa, Bede, Trisong Detsen, Shankara |
| Luật | **2** | Jaʿfar, Abu Hanifa |
| Quân sự | 1 | Abu Muslim |
| Sử học | 1 | Bede |
| Giáo dục | 1 | Charlemagne |
| Văn học | 1 | Đỗ Phủ |
| Toán học | 1 | Tăng Nhất Hạnh |
| Khoa học tự nhiên | 1 | Tăng Nhất Hạnh |
| Triết học | 1 | Shankara |
| Ngôn ngữ học | 1 | Sibawayh |
| Nghệ thuật/Kiến trúc | 1 | Yikʼin |
| **Tổng ô lĩnh vực** | **21** | trần là 24 (12 × 2) |

Đối chiếu với toàn atlas (208 người): Chính trị/Nhà nước 39,4% · Tôn giáo/Tâm linh 27,4% · Triết học 23,6%. Nhóm CE08 ở mức **41,7%** cho Chính trị và **41,7%** cho Tôn giáo — cao hơn mức nền. Điều này **không** cần sửa: thế kỷ 8 đúng là thế kỷ nhà nước mới (Abbasid, Carolingian, Thổ Phồn) và tôn giáo được thể chế hoá (bốn trường phái luật, quốc giáo Tây Tạng, Advaita). Nhưng phải ghi vào Ghi chú biên tập rằng đây là **hình dạng của thế kỷ**, không phải thiên lệch của người chọn.

**Một kiểm tra chéo đáng làm trước khi viết:** `Toán học` và `Khoa học tự nhiên` trong atlas từ CH04 đến nay đi theo một chuỗi liên tục — Āryabhaṭa (CE05), Tổ Xung Chi (CE05), Varāhamihira (CE06), Brahmagupta (CE07). **Nếu CE08 không có ai, chuỗi ấy đứt ở đúng thế kỷ của Nhất Hạnh và của *Zīj al-Sindhind*.** Đó là lý do mục #8 không thể bỏ, dù Q710705 có hồ sơ Wikidata yếu nhất nhóm.

---

# §5 · Ứng viên mạnh đã bị loại — bản thảo cho mục Ghi chú biên tập

**Kiểm quy tắc 6 trước khi viết mục này.** Tôi chạy script đối chiếu **cả 15 tên dưới đây** (ở cả hai trường `name_vi` và `name_orig`) với toàn bộ `data/persons.json`: **không tên nào trong 15 người bị loại đã có mục riêng ở bất kỳ đâu trong atlas.** Vậy mọi dòng dưới đây là một đánh đổi **có thật**, không rơi vào lỗi Ch3 mắc 11 lần.

Cùng script bắt được **sáu tên đã có mục riêng** mà các mục CE08 rất dễ nhắc tới. Khi nhắc, **bắt buộc** ghi kèm *"có mục riêng ở nhóm X"*, không được xếp vào diện bị loại:

| Tên | ID | Mục CE08 có nguy cơ nhắc tới |
|---|---|---|
| **Thích Nhất Hạnh** | `CH90-CE19_20-10` | mục Tăng Nhất Hạnh (§2.4) — **nguy cơ cao nhất** |
| Kʼinich Janaabʼ Pakal | `CH05-CE07-12` | mục Yikʼin Chan Kʼawiil |
| Tùng Tán Cán Bố | `CH05-CE07-11` | mục Trisong Detsen |
| Mặc Đốn thiền vu | `CH03-BCE02-12` | ghi chú vùng Nội Á |
| Zarathustra | `CH02-BCE06-09` | mục Abu Muslim (vùng Trung Á) |
| Nguyễn Du | `CH90-CE19_20-01` | mục Đỗ Phủ |

> **Cập nhật bắt buộc cho §2.4.** Khi viết §2.4 tôi mới chỉ biết Q310913 tồn tại trên Wikidata. Script lần này cho thêm một dữ kiện làm vấn đề **nặng hơn**: **Thích Nhất Hạnh đã là một mục của chính atlas này** (`CH90-CE19_20-10`, 1926–2022, phụ lục Việt Nam). Nghĩa là nếu mục CE08 ghi tên là "Nhất Hạnh", atlas sẽ có **hai mục cùng tên** cách nhau **1.200 năm**, và trang chỉ mục sẽ tự sinh ra một cú va chạm mà không lint nào bắt được. Khuyến nghị §2.4 — viết là **`Tăng Nhất Hạnh (僧一行 Yi Xing, tục danh Trương Toại 張遂)`** kèm câu phân biệt bắt buộc — vì vậy chuyển từ "nên làm" thành **"phải làm"**.

## §5.1 · Bị loại vì giai đoạn ảnh hưởng không thuộc thế kỷ 8 (quy tắc §3)

**Jabir ibn Hayyan** (Q167852) — lập luận đầy đủ ở §2.2. Khối *Jābirian* hình thành ở **cuối TK 9 – TK 10**; P569 = 721 của Wikidata truy ngược về giả thuyết Holmyard 1927 mà **Delva 2017** (kiểm qua Crossref, HTTP 200, 28.897 B) đã tháo rời. Giữ ông ở CE08 là đặt một tập thể tác giả thế kỷ 10 vào thế kỷ 8.

**Padmasambhava** (Q231582) — lập luận đầy đủ ở §2.5. Tiểu sử đầu tiên (*Zangling-ma*) cách ông **bốn thế kỷ**; các bản Đôn Hoàng có nhắc một tantrika cùng tên nhưng **không** gắn ông với Trisong Detsen. P569/P570 của Wikidata (717/762) có tham chiếu là **P214 VIAF** — hồ sơ thư viện, không phải nghiên cứu lịch sử. Áp đúng tiêu chuẩn đã dùng cho Jabir.

**Harun al-Rashid** (Q131002) — **đây là ca loại gây tiếc nhất và cần nói rõ nhất.** Ông trị vì **786–809**: 14 năm thuộc CE08, 9 năm thuộc CE09. Nhưng hai thứ làm nên danh tiếng ông đều **không** thuộc về ông: *Nghìn lẻ một đêm* là **tác phẩm văn học lấy ông làm nhân vật**, không phải tư liệu về ông (`[TRUYỀN THUYẾT]`); còn Bayt al-Ḥikma với tư cách một trung tâm dịch thuật có tổ chức thì gắn với **al-Maʾmun, thế kỷ 9**. Bỏ ông khỏi CE08 không có nghĩa bỏ ông khỏi atlas — **CE09 là chỗ đúng hơn**, và ở đó ông đứng cạnh al-Maʾmun, nơi câu chuyện dịch thuật kể được trọn vẹn. *Ghi chú cho vòng CE09: không được để Harun rơi qua khe giữa hai nhóm.*

## §5.2 · Bị loại vì có người cùng vai mạnh hơn trong nhóm

**Alcuin** (Q154332) — mất 804; hoạt động ở triều Aachen 782–796, Tours 796–804, tức **chủ yếu thế kỷ 8**. Ông bị loại **không phải vì niên đại** mà vì trùng vai với Charlemagne ở ô `Giáo dục`: cải cách giáo dục Carolingian được kể trọn trong một mục. **Nhưng xem cảnh báo ở §2.3** — nếu Chủ dự án quyết đưa Alcuin vào, thì ông và Charlemagne **phải cùng nhóm**, và người tôi đề nghị nhường chỗ là **Sibawayh** (mục #5), không phải ai khác.
*Dữ kiện dùng được:* P569 của Q154332 có **ba giá trị lệch nhau 16 năm** (740 preferred / 735 / 724) — nếu viết, phải ghi `độ tin cậy: Thấp`.

**Malik ibn Anas** (Q312299) và **Ibn Ishaq** (Q334847) — cả hai đều là mất mát thật. Malik: *al-Muwaṭṭaʾ*, bộ luật thành văn sớm nhất còn lại của Hồi giáo; hồ sơ Wikidata **tốt** (P570 795-06-07 preferred, hai giá trị 796 và 812 **bị deprecated** — dấu hiệu dữ liệu đã được dọn). Ibn Ishaq: *Sīra*, tiểu sử Muhammad đầu tiên, và là **nguồn mà mọi tiểu sử sau đều phải đi qua** — kể cả khi bản gốc chỉ còn qua bản hiệu đính của Ibn Hisham.
*Lý do loại:* với 4 suất Trung Đông, ô `Luật` đã có Abu Hanifa (trường phái rộng nhất) và Jaʿfar (nhánh Shiʿa), còn ô `Sử học` đã có Bede. Lấy thêm Malik hoặc Ibn Ishaq sẽ đẩy Trung Đông lên 5–6/12, tức **vượt tỷ lệ nền 33,2%** mà §4.2 vừa giữ được. **Nếu Chủ dự án muốn Ibn Ishaq, người phải nhường là Bede** — và khi ấy ô `Sử học` chuyển từ châu Âu sang Trung Đông, một đánh đổi đáng cân nhắc nghiêm túc chứ không phải câu nói cho đủ.

**Lý Bạch** (Q7071) — hồ sơ niên đại **tốt** (701-05-19 / 762-11-30, precision 11). Loại vì trùng ô `Văn học` với Đỗ Phủ, và giữa hai người, Đỗ Phủ nối được với biến cố trung tâm của thế kỷ (loạn An Lộc Sơn) theo cách Lý Bạch không nối được. *Dữ kiện hỗ trợ:* WP `Du Fu` ghi *"We have twelve poems to or about Li Bai from the younger poet, but only one in the other direction"* — quan hệ hai người **không đối xứng**, và mục Đỗ Phủ có thể kể điều đó. **Cảnh báo quy tắc 8:** nếu đặt liên kết Lý Bạch ↔ Đỗ Phủ thì phải **mở mục đích ra đọc tên**; nhưng vì Lý Bạch không có mục, **không được** tạo liên kết trỏ tới ông.

## §5.3 · Bị loại vì bốn tiêu chí (a) phạm vi · (b) độ bền · (c) nguyên bản · (d) counterfactual

**An Lộc Sơn** (Q360559) — **ca khó nhất của toàn vòng này, và tôi muốn Chủ dự án đọc kỹ đoạn này.** Loạn An Lộc Sơn (755–763) có lẽ là biến cố đơn lẻ có hệ quả lớn nhất thế kỷ 8 ở lục địa Á–Âu: nó chấm dứt đỉnh cao nhà Đường, mở đường cho Tây Tạng vào Trường An **năm 763** (xem mục Trisong Detsen) và cho Nam Chiếu tách ra.
Nhưng bốn tiêu chí đo **con người**, không đo **biến cố**. Theo (c) **tính nguyên bản** và (d) **counterfactual**, An Lộc Sơn là **triệu chứng** của một cấu trúc — chế độ tiết độ sứ biên trấn tích luỹ binh quyền — chứ không phải người tạo ra nó; nếu không có ông, một tiết độ sứ khác rất có thể đã làm điều tương tự, và đó chính là điều các sử gia vẫn lập luận. Biến cố ấy **vẫn vào atlas**, nhưng qua **mục Đỗ Phủ** (người chứng) và **mục Trisong Detsen** (người hưởng lợi) — hai góc nhìn, không mất gì.
*Nếu Chủ dự án không đồng ý:* người tôi đề nghị nhường chỗ là **Sibawayh**, và khi ấy Đông Á lên 4/12 còn Trung Đông xuống 3/12.

**Shōmu** (Q349263) — Đại Phật chùa Tōdai-ji khai nhãn **752**, và sắc lệnh dựng *kokubunji* khắp các tỉnh là một bước thể chế hoá Phật giáo nhà nước có thật. Loại vì (a) **phạm vi** giới hạn trong quần đảo Nhật ở thời điểm ấy, và vì ô `Tôn giáo/Tâm linh` của nhóm đã có **5 người**. *Ứng viên nên xem lại ở các chapter sau, không phải ứng viên yếu.*

**Charles Martel** (Q3301) — trận Tours **732**. Loại vì luận điểm "cứu châu Âu khỏi Hồi giáo" là một **`[SUY LUẬN HIỆN ĐẠI]` thế kỷ 18–19** (Gibbon) mà sử học hiện nay phần lớn đã hạ cấp; viết mục cho ông đòi hỏi mục ấy chủ yếu đi **bác** luận điểm làm ông nổi tiếng — đúng cấu hình mà Ghi chú biên tập CE07 đã dùng để loại Yajaw Teʼ Kʼinich II: *"lý do duy nhất để đưa ông vào là một mệnh đề mà chính chuyên gia hàng đầu đang bác"*. Thêm nữa, vai trò thật của ông — dựng nền cho nhà Carolingian — **đã nằm trong mục Charlemagne**.
*Dữ kiện phải ghi nếu Chủ dự án vẫn muốn ông:* Q3301 có `P31 = Q5` với **0 tham chiếu**, và P570 (741-10-22, precision 11) cũng **0 tham chiếu** — độ chính xác được khai cao hơn hẳn bằng chứng đỡ cho nó.

**Divashtich** (Q753663) — xem §3.3. Bằng chứng hạng nhất (văn khố Mugh, UNESCO 2025), nhưng (a) phạm vi chỉ là Panjikant và (d) counterfactual gần bằng không: ông thua, bị đóng đinh năm 722, và Transoxiana Hồi giáo hoá đúng như khi ông không tồn tại. **Bài học phải viết thành câu trong Ghi chú biên tập:** *bốn tiêu chí đo ảnh hưởng, không đo mức độ được ghi chép; nếu lẫn hai thứ, atlas sẽ dần thành bản đồ các văn khố còn sót chứ không phải bản đồ ảnh hưởng.*

**Sanjaya** (Q3107477) và **Panangkaran** (Q7130030) — xem §3.2. Cả hai có bi ký đương thời với niên đại tuyệt đối (732; 778), nhưng theo (c) **tính nguyên bản** và (d) **counterfactual** họ là **người bảo trợ** chứ không phải người khởi tạo: chương trình đền tháp Śailendra là hiện tượng của cả một triều đại, và không bi ký nào cho biết điều gì thuộc về quyết định riêng của họ. **Đây là lý do duy nhất khiến Đông Nam Á ở lại mức 0,5%, và nó phải được ghi thẳng** — không phải vì không tìm, mà vì hai ứng viên tìm được không qua nổi hai trong bốn tiêu chí.

**Kyriakos xứ Makuria** (Q1148493) — xem §3.4. Loại vì nguồn duy nhất là một biên niên Ai Cập soạn muộn, và các hệ thống sử liệu **không thống nhất nổi ông đứng ở đâu trong danh sách vua Makuria**.

**Jayavarman II** — loại vì nhóm sai (**802 thuộc CE09**) **và** vì niên đại ấy đến từ bia Sdok Kok Thom **dựng năm 1052**, tức `[NIÊN ĐẠI QUY ƯỚC]` cách sự kiện 250 năm. *Ghi chú cho vòng CE09: ông là ứng viên Đông Nam Á của nhóm ấy, và vấn đề nguồn phải được nêu ngay trong mục.*

---

# §6 · D5 — Ứng viên Việt Nam thế kỷ 8

## §6.1 · Kết luận: không đưa ai lên track chính, và **không được** nêu ba người này như "ứng viên bị loại"

Ba nhân vật Việt Nam thế kỷ 8 **đều đã có mục riêng trong `content/ch90.md`**:

| Tên | ID | `năm:` hiện có | `nơi:` |
|---|---|---|---|
| **Mai Hắc Đế** (Mai Thúc Loan) | `CH90-CE01_09-06` | `hoạt động k. 713–722` | Hoan Châu, nay thuộc Nghệ An |
| **Phùng Hưng** | `CH90-CE01_09-07` | `hoạt động k. 766–791` | Đường Lâm, nay thuộc Hà Nội |
| **Khương Công Phụ** | `CH90-CE01_09-08` | `731–805` | Ái Châu, nay thuộc Thanh Hoá; làm quan tại Trường An |

**Hệ quả quy tắc 6 là bắt buộc và tuyệt đối:** vì cả ba **đã được chọn ở chỗ khác trong atlas**, mục "Ứng viên mạnh đã bị loại" của CE08 **không được nêu tên họ**. Nếu muốn nhắc để so sánh, câu văn phải là *"có mục riêng ở phụ lục Việt Nam"*. Đây đúng là hình dạng lỗi mà Ch3 mắc 11 lần: nêu một người đã có mục riêng như một đánh đổi, trong khi **không có đánh đổi nào xảy ra**.

## §6.2 · Vì sao track chính vẫn là "không", xét theo bốn tiêu chí

- **Mai Thúc Loan** — khởi nghĩa k. 713–722, xưng đế. `[NGUỒN MUỘN]` Tư liệu đến qua *Đại Việt sử ký toàn thư* (TK 15) và các bộ sử Đường (TK 10–11), đều **sau sự kiện nhiều thế kỷ**; ngay `năm:` ở ch90 cũng đã phải dùng dạng `hoạt động k.` Theo (a) phạm vi và (d) counterfactual: khởi nghĩa bị dập, cấu trúc đô hộ không đổi.
- **Phùng Hưng** — k. 766–791, hiệu *Bố Cái Đại Vương*. Cùng hình dạng tư liệu, cùng kết cục.
- **Khương Công Phụ** — `[ĐÃ KIỂM]` Wikipedia tiếng Việt `Khương Công Phụ` (**HTTP 200, 15.128 B**, extract 7.089 ký tự): **731–805**, tự Đức Văn, đỗ đầu kỳ thi nhà Đường năm **780**, thăng dần tới **Đồng trung thư môn hạ bình chương sự** (tể tướng) dưới **Đường Đức Tông** — bài viết gọi ông là *"người Việt duy nhất đỗ trạng nguyên rồi làm tể tướng Trung Hoa"*.
  Đây là người có hồ sơ **tốt nhất trong ba người**, vì ông xuất hiện trong **bộ máy quan chức nhà Đường**, tức nguồn gần đương thời chứ không phải truyền thuyết khởi nghĩa. Nhưng vẫn không đủ cho track chính theo (c) và (d): ông thành công **bên trong** một hệ thống do người khác dựng, và việc ông làm tể tướng không đổi điều gì ngoài chính sự nghiệp ông.
  > **Hai cảnh báo nguồn nếu vòng sau viết lại mục này:** (1) chi tiết gia thế (ông nội Khương Thần Dực, cha Khương Văn Đĩnh) trong bài đến từ *"tộc phả của họ Khương ở Thạch Thất"* — **gia phả, nguồn muộn**, không được viết như sự kiện; (2) từ **"trạng nguyên"** là thuật ngữ khoa cử Việt Nam đời sau, áp ngược lên kỳ thi nhà Đường năm 780 — `[NIÊN ĐẠI/THUẬT NGỮ QUY ƯỚC]`, nên viết là "đỗ đầu kỳ thi" kèm chú.

## §6.3 · Một đính chính phải giữ: `ch90.md` là phụ lục **Việt Nam**, không phải phụ lục Đông Nam Á

Ghi chú biên tập CE07 đã sửa nhầm lẫn này một lần. Nó có hệ quả trực tiếp cho vòng CE08: **Sanjaya và Panangkaran không thể "đẩy xuống ch90"**. Nếu họ không vào track chính thì họ **không vào đâu cả** — và đó chính là nội dung phải ghi vào Ghi chú biên tập, thay vì để người đọc tưởng vùng Đông Nam Á đã được phục vụ bởi phụ lục. Phụ lục Việt Nam **nằm ngoài thống kê chính**, nên 1 người Đông Nam Á trong bảng §4.2 là con số thật, không phải con số thiếu sót kỹ thuật.

---

# §7 · Ba việc còn lại

## §7.1 · Cỡ nhóm: **12 là đúng, và CE08 là một trong số ít nhóm mà con số ấy thật sự chật**

Đề bài hỏi thẳng nên tôi trả lời thẳng, kèm một đính chính về cách đọc quy tắc.

**Đính chính:** `CONTRIBUTING.md` viết *"mỗi nhóm **trần** 12 người"*, và lint chặn build khi *"nhóm quá 12 người"*. Vậy 12 là **trần**, không phải **định mức**. Một nhóm hoàn toàn được phép có **ít hơn** 12 — và với các nhóm nghèo tư liệu thì ít hơn mới là câu trả lời đúng.

**Nhưng CE08 là trường hợp ngược lại.** Thế kỷ 8 dồn vào một chỗ: cách mạng Abbasid và việc dời đô về Baghdad; sự kết tinh của bốn trường phái luật Hồi giáo và của ngữ pháp Ả Rập; loạn An Lộc Sơn và điểm gãy của nhà Đường; đế quốc Thổ Phồn ở đỉnh cao, chiếm Trường An và chọn đường tu cho Tây Tạng; sự hình thành đế quốc Carolingian và lễ đăng quang năm 800; Advaita Vedānta; Tikal ở đỉnh Hậu Cổ điển; và các bi ký có niên đại đầu tiên của Java. **Vấn đề của nhóm này không phải thừa suất mà là thiếu suất** — §5 phải loại **mười lăm** ứng viên, trong đó ít nhất bốn người (Harun al-Rashid, Malik ibn Anas, Ibn Ishaq, An Lộc Sơn) sẽ chắc chắn vào atlas nếu trần là 16.

**Vì vậy tôi khuyến nghị giữ nguyên 12, và nêu rõ lý do không phải vì 12 là con số đúng cho thế kỷ này, mà vì:**
1. **Tính so sánh được xuyên chapter.** Trần 12 là thứ làm cho các bảng phân bố vùng và lĩnh vực đọc được giữa các nhóm. Nới trần cho riêng một nhóm sẽ biến mọi so sánh tỷ lệ thành vô nghĩa — và chính các bảng ấy là thứ atlas dùng để tự phê bình (xem toàn bộ §4.2).
2. **Nới trần là thay đổi hạ tầng, không phải thay đổi nội dung.** Nó đòi sửa `atlaslib/common.py` **và** `prompts/atlas-prompt.md` cùng lúc (CONTRIBUTING nói rõ: sửa một nơi thôi thì các chapter sau sẽ sinh lỗi), rồi kéo theo câu hỏi có nên hồi tố cho CE06, CE07 và cả Chapter 3–4 hay không. Đó là quyết định kiến trúc, không nên đi kèm một vòng duyệt nội dung.
3. **Chỗ đúng cho sức ép này là Ghi chú biên tập, không phải trần nhóm.** Danh sách 15 người bị loại ở §5, kèm lý do từng người, **giữ lại được toàn bộ thông tin** mà việc nới trần định cứu — và còn giữ thêm thứ mà việc nới trần sẽ xoá: **bản ghi về việc atlas đã phải chọn gì**.

*Đề nghị kèm theo:* ghi vào Ghi chú biên tập CE08 một câu thẳng thắn rằng **nhóm này là nhóm chật nhất Chapter 5**, và rằng bốn cái tên nêu trên bị loại **vì trần, không vì chất lượng**. Đó là thông tin cho người đọc, và cũng là ghi chú cho chính vòng CE09 (Harun al-Rashid phải được nhặt lại ở đó).

## §7.2 · Một kết luận về phương pháp mà vòng này rút ra

Bốn ca trong vòng này có cùng một hình dạng, và nên được viết thành một dòng trong Ghi chú biên tập:

| Người | Wikidata khai | Nguồn thật của con số ấy |
|---|---|---|
| Ādi Shankara | 788–820 | học thuật cuối TK 19 theo K.P. Tiele — **không phải** truyền thống Śṛṅgeri (§2.1) |
| Jabir ibn Hayyan | 721–815 | giả thuyết Holmyard **1927**, đã bị Delva 2017 tháo rời (§2.2) |
| Padmasambhava | 717–762 | tham chiếu là **P214 VIAF**, một hồ sơ thư viện (§2.5) |
| Charles Martel | 741-10-22 (prec 11) | **0 tham chiếu** cho cả P31 lẫn P570 (§5.3) |

> **Dòng để viết vào Ghi chú biên tập:** *Wikidata khai `precision` chứ không khai **độ tin cậy**. Trong nhóm CE08, bốn niên đại được khai ở độ chính xác cao nhất lại là bốn niên đại yếu nhất, vì con số đằng sau chúng là một giả thuyết hiện đại, một hồ sơ thư viện, hoặc không gì cả. `độ tin cậy niên đại:` của atlas phải được chấm theo **biên độ giữa các giá trị cạnh tranh trong học thuật**, không theo trường `precision`.*

## §7.3 · Ghi chú riêng gửi Chủ dự án — quyền riêng tư trong `atlaslib/common.py`

(Đây là mục mà phần đầu báo cáo tham chiếu tới.)

`atlaslib/common.py` đặt:

```python
PROJECT["user_agent"] = "history-atlas/0.1 (personal research project; <email Chủ dự án — che khi đưa vào git>) python-urllib"
```

Nghĩa là **mọi lần chạy `build.py` không có `--offline` đều gửi địa chỉ email cá nhân của Chủ dự án tới Wikidata và tới mọi máy chủ mà build gọi**, kèm cả tên miền nơi làm việc.

Theo yêu cầu của đề bài — *"tuyệt đối không đưa thông tin cá nhân nào (email, tên người dùng) vào header, URL hay payload"* — **toàn bộ** lời gọi mạng trong vòng duyệt này dùng `User-Agent: history-atlas/0.1 (research)` và **không** dùng chuỗi trong `common.py`. Không có email hay tên người dùng nào xuất hiện trong bất kỳ header, URL hay payload nào tôi gửi.

**Đây là báo cáo, không phải thay đổi.** Tôi **không** sửa `common.py`, vì (a) đề bài giao việc bình duyệt nội dung, không giao sửa cấu hình, và (b) quy ước User-Agent của Wikimedia khuyến khích một địa chỉ liên hệ, nên đây có thể là lựa chọn có chủ ý. Nhưng nếu kho này từng được công khai, chuỗi ấy nằm trong lịch sử git. Quyết định thuộc về Chủ dự án; một phương án trung dung là dùng URL kho thay cho email cá nhân.
