# Cổng chọn người — Chapter 5, nhóm CE09 (TK 9, 801–900 CN)

**Vòng độc lập.** Báo cáo này không viết `content/ch05.md`. Nó khảo sát ứng viên, mở từng Q-ID ra kiểm, và đề xuất một roster có thể bảo vệ được cho người viết mục.

**Quy ước ký hiệu dùng xuyên báo cáo**
- `[KHÔNG KIỂM ĐƯỢC]` — tôi đã thử và thất bại; lý do ghi ngay sau.
- `[NIÊN ĐẠI QUY ƯỚC]` — con số được học giới dùng như mốc quy ước, không đến từ nguồn đương thời.
- `[SUY LUẬN HIỆN ĐẠI]` — kết luận của học thuật hiện đại, không phải lời của nguồn cổ.

---

## §0 · Việc đã làm trước khi kết luận

Đọc, theo thứ tự:

1. `CONTRIBUTING.md` toàn bộ — bốn tiêu chí (a) phạm vi · (b) độ bền · (c) tính nguyên bản · (d) counterfactual; tám quy tắc nội dung đánh số; bốn quy ước trường `vùng:`.
2. `atlaslib/common.py` dòng 72–82 — từ vựng cố định. Mọi giá trị đề xuất trong báo cáo này đã đối chiếu với `FIELDS` (16), `REGIONS` (9), `BIG_QUESTIONS` (4), `CONFIDENCE` (3).
3. `content/ch05.md` toàn bộ 36 mục CE06/CE07/CE08 + toàn bộ `## Ghi chú biên tập` (43 khối), trong đó 13 khối cuối là của vòng CE08 và chứa các cam kết ràng buộc nhóm này.
4. `reports/ch05-ce08-gate.md` — phương pháp của vòng trước và danh sách ứng viên hoãn sang CE09.
5. `reports/stats.txt` — phân bố vùng/lĩnh vực hiện tại (221 người track chính).

**Bốn ràng buộc tôi tự áp, rút từ ghi chú CE08:**

- Trần 12 là **trần**, không phải định mức. Nếu bằng chứng không đỡ nổi 12, tôi nộp ít hơn.
- Vùng trống chỉ có hai câu trả lời đúng: tìm được người thật, hoặc ghi rõ vùng ấy trống **và vì sao** (quy ước `vùng:` số 4). Không đổi nhãn vùng để chữa thống kê.
- `độ tin cậy niên đại:` chấm theo **biên độ giữa các giá trị cạnh tranh trong học thuật**, không theo trường `precision` của Wikidata (ghi chú CE08, khối "Wikidata khai độ chính xác, nó không khai độ tin cậy").
- Quy tắc 6: không nêu tên ai làm "ứng viên bị loại" nếu người ấy đã có mục ở nơi khác trong atlas, kể cả `ch90.md`.

---

# §1 · Cổng Wikidata — 60 ứng viên, tự mở kiểm

Tôi tra **toàn bộ** ứng viên qua `wbgetentities` (enwiki titles rồi Q-ID), và với nhóm lọt vòng trong thì mở thêm **tham chiếu của từng giá trị P569/P570** — vì đây đúng là chỗ vòng CE08 đã rút ra bài học: `precision` cao không có nghĩa là niên đại chắc.

**Kết quả trùng lặp (việc 4 của đề bài):** không một Q-ID nào trong danh sách ứng viên trùng với 261 Q-ID đang có trong `content/` (`grep` đối chiếu toàn bộ). Không ai trong danh sách đã có mục riêng.

## §1.1 · Bốn ca `P31 ≠ Q5` — không có đường vào atlas

Cùng loại lỗi mà ghi chú CE08 đã ghi với `Q42798` Borobudur ("là một công trình, không phải người"):

| Q-ID | Nhãn | `P31` thật | Hệ quả |
|---|---|---|---|
| `Q423210` | Banū Mūsā | `Q109288756`, `Q16017119` | **Không phải `Q5`.** Đây là mục cho *ba anh em* như một tập thể. Muốn đưa khối Banū Mūsā vào atlas thì phải chọn **một** anh em (Muḥammad ibn Mūsā ibn Shākir) và dùng Q-ID riêng của người ấy — không dùng `Q423210`. |
| `Q27793406` | Devapala | `Q4167410` (**trang định hướng Wikimedia**) | Tra "Devapala" bằng tiêu đề enwiki trả về một **trang định hướng**, không phải vua Pala. Bẫy sạch sẽ: `P31` là thứ duy nhất phát hiện ra. |
| `Q7488718` | Shankaranarayana | `Q56436498` | Không phải `Q5`. |
| `Q42798` | Borobudur | (đã ghi ở CE08) | nhắc lại vì nó vẫn là ứng viên "nổi tiếng hơn mọi cá nhân liên quan". |

## §1.2 · Ba bẫy nhãn (việc 3 của đề bài)

**(1) `Q2269861` — nhãn `en` là "Mahāvīra", và atlas ĐÃ CÓ một Mahāvīra khác.**
Đây là ca nghiêm trọng nhất của vòng này, nặng hơn ca `Q710705` "Nhất Hạnh" của CE08. `CH02-BCE06-04 · Mahāvīra (महावीर, Vardhamāna)` là **tổ thứ 24 của Jaina giáo, thế kỷ 6 TCN**. `Q2269861` là **nhà toán học Ấn Độ thế kỷ 9** ở triều Rāṣṭrakūṭa. Hai người cách nhau **mười bốn thế kỷ** và `Q2269861` không có nhãn `vi` nào để làm hàng rào.
*Dạng viết tên an toàn đề xuất:* **Mahāvīrācārya (महावीराचार्य, Mahāvīra nhà toán học)**. Hậu tố `-ācārya` không phải tên atlas tự đặt: nó là cách giới sử toán học Ấn Độ quy chiếu ông và là cách phân biệt chuẩn với tổ Jaina. Người viết mục **phải** dùng dạng này, và Ghi chú biên tập phải ghi lại lý do, nếu không một vòng sau sẽ "sửa" cho khớp nhãn Wikidata — đúng cơ chế mà ghi chú CE08 đã cảnh báo.

**(2) `Q194442` — nhãn `vi` là "Hanbal" trần.**
Tên đầy đủ là Aḥmad ibn Ḥanbal; "Ḥanbal" một mình là tên **ông cố** của ông, không phải tên ông. Nhãn `vi` trần ấy vừa sai vừa dễ bị chép thẳng vào trường tiêu đề. *Dạng viết tên đề xuất:* **Ahmad ibn Hanbal (أحمد بن حنبل)**.

**(3) `Q61056` — nhãn `vi` là "Al-Mamun", alias `vi` là "Al-Ma'mun".**
Không va chạm với ai, nhưng hai dạng khác nhau tồn tại song song trên chính Wikidata. Ghi chú biên tập CE08 đã dùng dạng **al-Maʾmun**; nếu vòng này đưa ông vào thì phải giữ **đúng một** dạng xuyên chapter.

## §1.3 · Niên đại: `precision` cao nhất lại là niên đại yếu nhất — mẫu hình CE08 lặp lại nguyên vẹn

Tôi đọc tham chiếu của từng giá trị. Bảng dưới là **bằng chứng thật so với hồ sơ thư mục**:

| Ứng viên | Giá trị `preferred` | Tham chiếu của nó | Đọc |
|---|---|---|---|
| Harun al-Rashid `Q131002` | sinh 19-02-766 (`p11`), mất 24-03-809 (`p11`) | **toàn bộ là `P143` imported from Wikimedia project** | Ngày tới từng ngày, bằng chứng bằng không. Không phải mệnh đề sử học. |
| Ahmad ibn Hanbal `Q194442` | sinh 23-11-780 (`p11`), mất 02-08-855 (`p11`) | **KHÔNG CÓ THAM CHIẾU** ở cả hai | Hình dạng y hệt ca Charles Martel của CE08. (Các giá trị `normal` cấp năm thì *có* nguồn.) |
| Jayavarman II `Q379239` | sinh +0800 (`p7` = **thế kỷ**), mất +0900 (`p7`) | **KHÔNG CÓ THAM CHIẾU** | Đúng như ghi chú CE07 đã cảnh báo: "giá trị độn, không được chép". |
| Sugawara no Michizane `Q382005` | 01-08-845 → 26-03-903 (`p11`) | `P143` imported from jawiki | Ngày chính xác, nguồn là một bản dịch Wikipedia. |
| Đường Vũ Tông `Q9801` | 02-07-814 → 22-04-846 (`p11`) | `P143` imported from zhwiki | như trên. |
| Kūkai `Q222227` | sinh 27-07-774 (`p11`, preferred) | **KHÔNG CÓ THAM CHIẾU**; giá trị 774 cấp năm thì có GND + Getty + ở mức `normal` | Ngày sinh là ngày truyền thống tông Chân Ngôn, không phải tư liệu đương thời. |
| al-Bukhari `Q241026` | mất 31-08-870 (`p11`) | `stated in Q76499581` | Niên đại Hijrī 13 Shawwāl 194 / đêm Eid al-Fiṭr 256 có trong chính truyền thống tiểu sử Hồi giáo — đây là ca hiếm mà `p11` **có** cơ sở. |
| Photios I `Q243187` | mất +0900 (`p7`) preferred, nhưng có **năm giá trị cạnh tranh** 891 / 893 / 895 / 896 / 900 | nhiều nguồn khác nhau | Biên độ 9 năm cho năm mất của một thượng phụ Constantinopolis. |
| al-Khwarizmi `Q9038` | sinh 780 preferred, nhưng còn 750 (`p7`); mất 850 preferred, còn 846 | DSB (`Q656742`) ghi nguyên văn *"(b. before 800; d. after 847)"* | **Biên độ sinh ~30 năm.** |
| Mahāvīrācārya `Q2269861` | sinh 817 preferred / 800; mất 875 | Google Books tr. 231 | Thực chất mốc duy nhất chắc là: *Gaṇitasārasaṅgraha* soạn dưới triều Amoghavarsha I. |

**Hệ quả cho trường `độ tin cậy niên đại:` — đề xuất theo biên độ học thuật, không theo `precision`:**

| Ứng viên | Đề xuất | Lý do (biên độ giữa các giá trị cạnh tranh) |
|---|---|---|
| al-Bukhari | **Cao** | Niên đại Hijrī tới từng ngày, truyền thống tiểu sử nội tại nhất quán. |
| Ahmad ibn Hanbal | **Cao** | 780–855 không bị tranh cãi trong học thuật (chỉ các *ngày* mới vô nguồn). |
| Hunayn ibn Ishaq | **Cao** | 808/809–873; biên độ 1 năm. |
| al-Kindi | **Trung bình** | sinh 796 / 800 / 801, mất 870 / 873 — biên độ 5 và 3 năm, nhưng mọi con số đều mang tiền tố "k." trong chính học thuật. |
| Hàn Dũ, Bạch Cư Dị | **Cao** | Niên đại Đường thư, nhất quán, và cả hai có văn tập tự định niên. |
| Alfred Đại đế | **Cao** | 848/9–26-10-899; biên độ 1 năm, có *Asser* và *Anglo-Saxon Chronicle*. |
| al-Khwarizmi | **Thấp** | Biên độ sinh ~30 năm (DSB: "b. before 800"). Vượt dung sai `Trung bình` (±25). |
| Mahāvīrācārya | **Thấp** | Không có niên đại độc lập; khung duy nhất là triều Amoghavarsha I. Nên viết `hoạt động k. 850 CN`. |
| Photios I | **Thấp** | Năm mất có 5 giá trị cạnh tranh, biên độ 9 năm. |
| Jayavarman II | **Thấp** | Mọi niên đại đến từ bia dựng năm 1052. |
| Trương Bảo Cao (Jang Bogo) | **Thấp** | Năm mất 841 (nhật ký Ennin, đương thời) **chống lại** 846 (*Tam quốc sử ký*, thế kỷ 12). Wikidata để 841 ở hạng `deprecated` và 846 ở `preferred` — tức Wikidata đã **chọn phe**, và chọn phe nguồn **muộn hơn**. Đừng chép mà không nói. |
| Eriugena | **Thấp** | `P569` khai ở `p8` = độ chính xác **thập kỷ**. |
| Kʼakʼupakal | **Thấp**→xem §3.1 | Wikidata không có `P569`/`P570` nào; chỉ có niên đại bi ký. |


---

# §2 · Ba việc CE08 giao lại — đã quyết

Ghi chú biên tập của CE08 để lại ba món nợ cho vòng này. Tôi xử cả ba, và với mỗi món tôi nói rõ mình **đồng ý hay không đồng ý** với lập luận cũ.

## §2.1 · Harun al-Rashid `Q131002` — **VẪN LOẠI**, nhưng vì lý do mạnh hơn lý do của CE08

CE08 cắt ông vì hết trần 12 người, rồi dặn "vòng CE09 phải nhặt ông lại". Tôi đã đánh giá lại độc lập và kết luận ngược: **không nhặt**. Ba lớp lý do, xếp theo độ mạnh tăng dần.

**(1) Hai thứ làm ông nổi tiếng đều không phải của ông.** Điểm này CE08 đã nêu và tôi xác nhận: *Nghìn lẻ một đêm* dùng ông làm **nhân vật**, không phải tác phẩm của ông — đúng như bài Wikipedia tiếng Anh về ông thừa nhận, nhiều truyện "đặt bối cảnh ở triều đình Harun và một số truyện có ông tham gia". Một người được viết về không phải một người sản xuất ra tư tưởng. Theo tiêu chí (c) *tính nguyên bản*, đây là số không.

**(2) Bayt al-Ḥikma: không chỉ "thuộc về al-Maʾmūn" — mà có lẽ chưa bao giờ là một thiết chế.** Đây là chỗ tôi đi xa hơn CE08. CE08 nói công lao nhà dịch thuật có tổ chức thuộc về al-Maʾmūn. Nhưng học thuật gần đây đi thêm một bước: Ekmeleddin İhsanoğlu, *The Abbasid House of Wisdom: Between Myth and Reality* (Routledge, 2023) lập luận rằng hình ảnh Bayt al-Ḥikma như **một học viện có khoa, có ban, có tranh luận học thuật tổ chức** là sản phẩm **được dựng lên trong thế kỷ 19 – đầu thế kỷ 20** bởi học giả Đông phương học, qua lỗi dịch và phép phóng chiếu ngược, rồi được truyền tiếp vào học thuật đời sau. Dimitri Gutas, *Greek Thought, Arabic Culture* (1998) từ lâu đã mô tả phong trào dịch thuật như một **hiện tượng xã hội rộng** chứ không phải sản phẩm của một toà nhà.

> **Hệ quả cho atlas, và đây là phần quan trọng:** nếu "sáng lập Nhà Trí tuệ" là một mệnh đề đang bị học thuật tháo dỡ, thì nó **không cứu được Harun mà cũng không cứu được al-Maʾmūn**. Cách đúng để đưa phong trào dịch thuật vào atlas là đi qua **người dịch**, không qua người chi tiền. Vì vậy §4 có Hunayn ibn Isḥāq, và §5 loại al-Maʾmūn.

**(3) Niên đại của ông trên Wikidata rỗng bằng chứng.** Xem §1.3: `P569` 19-02-766 và `P570` 24-03-809 đều ở `precision` **tới từng ngày**, và tham chiếu của cả hai **chỉ là `P143` imported from Wikimedia project**. Đây không phải lý do chính để loại — niên đại yếu không loại một người thật sự quan trọng, nó chỉ hạ `độ tin cậy niên đại:`. Nhưng nó cho thấy cái vẻ chắc chắn quanh Harun là vẻ chắc chắn **vay mượn**.

**Đối chứng công bằng — những gì ông thật sự làm, và vì sao vẫn không đủ.** Ông trị vì 786–809; ông thanh trừng nhà Barmakid năm 803; ông chia đế quốc cho al-Amin và al-Maʾmūn, và chính sự sắp xếp kế vị đó dẫn thẳng tới **nội chiến 811–813**. Nếu xét tiêu chí (d) *phản thực*, di sản chính trị trực tiếp nhất của Harun là **một cuộc nội chiến**, tức một hậu quả tiêu cực chứ không phải một đóng góp. Ông cũng trao đổi sứ bộ với Charlemagne (con voi Abul-Abbas, 802) — một giai thoại đẹp, nhưng là một sự kiện ngoại giao, không phải một ý tưởng.

**Kết luận §2.1.** Harun al-Rashid **không vào CE09**. Ông đã có mặt trong `content/ch05.md` ở dạng **đích quan hệ bằng văn bản tự do** (dòng 444, trong mục `CH05-CE08-02 · Al-Mansur`) — đó là vị trí đúng của ông trong atlas này: một cái tên mà thế kỷ 9 đi qua, không phải một người mà thế kỷ 9 nhận ý tưởng từ đó.
*Ghi chú cho người viết mục: vì ông **không** có mục riêng, ông **được phép** xuất hiện trong danh sách bị loại (§5) theo quy tắc 6.*

## §2.2 · Khối văn bản Jābirian `Q167852` — **KHÔNG vào CE09**, và nhãn `[Tranh cãi lịch sử]` không cứu được

CE08 loại Jābir ibn Ḥayyān vì niên đại văn bản là k. 850–950, và nói chỗ đúng của ông, nếu có, là CE09 hoặc CE10 kèm nhãn `[Tranh cãi lịch sử]`. Tôi đã đọc lại và **không đồng ý với phần "nếu có"**.

**Tình trạng học thuật, đã kiểm.** Jābir ibn Ḥayyān lịch sử (nếu có) **mất khoảng 806–816**. Khối văn bản mang tên ông — khoảng **215 chuyên luận còn lại** — được định niên **k. 850–950**, niên đại do Paul Kraus (*Jābir ibn Ḥayyān*, 1942–1943, tập I, tr. lxv) đề xuất và "đã được chấp nhận rộng rãi trong học thuật hiện đại". Ba chứng cứ nội tại dẫn tới niên đại ấy: (a) phần lớn **thuật ngữ triết học** dùng trong các chuyên luận chỉ mới được đặt ra vào **giữa thế kỷ 9**; (b) một số **bản dịch Hy Lạp** mà khối văn bản trích dẫn chỉ được dịch sang tiếng Ả Rập vào **cuối thế kỷ 9**; (c) phần Shiʿa trong khối văn bản chỉ thấy ở các nguồn **cuối thế kỷ 9 – đầu thế kỷ 10**. Có phản biện — Fuat Sezgin (1971) và Syed Nomanul Haq (1994) chống lại niên đại Kraus — nhưng Gannagé (1998) đã bác luận cứ chính của Nomanul Haq.

**Vì sao nhãn `[Tranh cãi lịch sử]` không phải lời giải.** Nhãn ấy đánh dấu **một con người có tồn tại gây tranh cãi**. Ca Jābir không có hình dạng đó. Ở đây ta có **hai vật thể tách rời nhau**:

| Vật thể | Niên đại | Tình trạng |
|---|---|---|
| Con người Jābir ibn Ḥayyān | mất k. 806–816 (tức thuộc nhóm **CE08**) | Tồn tại có thể có, nhưng **không có tác phẩm nào quy được cho ông** |
| Khối văn bản Jābirian | k. 850–950 (**CE09 + CE10**) | Tác phẩm có thật, nhưng là của **nhiều tác giả ẩn danh qua nhiều lớp hiệu đính** |

Atlas này là bản đồ **con người**, và đơn vị của nó là "một người, một mục, có đóng góp quy được cho người đó". Ca Jābir làm đơn vị ấy **gãy**: hoặc ta có một con người không có tác phẩm, hoặc ta có một tác phẩm không có con người. Đặt nhãn `[Tranh cãi lịch sử]` lên một mục tên "Jābir ibn Ḥayyān, CE09" sẽ **ngầm khẳng định** điều học thuật đang phủ nhận — rằng có một cá nhân thế kỷ 9 viết khối ấy. Đó chính là kiểu dùng nguồn ngược mà **quy tắc 7** cấm: nguồn có thật, đúng chủ đề, và bị dùng ngược chiều luận điểm trung tâm của nó.

**Kết luận §2.2.** Khối Jābirian **không có mục riêng ở CE09**, và tôi khuyến nghị **cũng không có ở CE10** — xem §7 để biết chỗ đúng của nó: một khối trong `## Ghi chú biên tập`, không phải một mục. Nếu ai đó ở vòng CE10 muốn lật lại, gánh nặng chứng minh là phải chỉ ra **một chuyên luận cụ thể** quy được cho **một cá nhân cụ thể** sống trong 801–900.

## §2.3 · Alcuin `Q154332` — **giữ nguyên quyết định CE08, không chuyển sang CE09**

CE08 loại Alcuin vì **trùng vai với Charlemagne ở lĩnh vực `Giáo dục`**, *không phải* vì niên đại. Tôi đã kiểm và **không bác được lập luận đó**, nên theo đúng yêu cầu của đề bài, tôi **không đề xuất lại ông**.

Thêm hai lý do riêng của vòng này củng cố quyết định cũ:
1. **Niên đại đặt ông vào CE08, không phải CE09.** Alcuin mất **804**. Theo §3/§5.3 của `CONTRIBUTING.md`, xếp nhóm theo **thời kỳ ảnh hưởng chính**: thời kỳ ảnh hưởng chính của Alcuin là trường cung đình Aachen **782–796** và Tours **796–804** — tuyệt đại bộ phận nằm trong thế kỷ 8. Chuyển ông sang CE09 sẽ là **lách niên đại để lấp chỗ**, đúng thứ mà CE08 đã cảnh báo.
2. **Nếu bao giờ thêm ông, `độ tin cậy niên đại:` phải là `Thấp`** — `Q154332` `P569` có **ba giá trị trải 16 năm**. Ghi chú CE08 đã ghi điều này; tôi xác nhận nó vẫn đúng.

**Kết luận §2.3.** Alcuin ở lại ngoài, và ở lại **ngoài nhóm CE08**, không rơi sang CE09. Vì ông **không có mục riêng**, ông được phép đứng trong §5.

---

# §3 · Khảo sát đủ chín vùng của `REGIONS` (việc 1 của đề bài)

Nguyên tắc tôi tự áp: **tìm kỹ hơn ở vùng mỏng, không hạ chuẩn ở vùng mỏng.** Mỗi tiểu mục dưới đây nói rõ: thế kỷ 9 ở vùng đó có **ai**, nguồn **thuộc loại nào**, và nếu để trống thì trống **vì sự thật lịch sử** hay vì **điều kiện lưu trữ**. Danh sách ứng viên là **mở**, không phải đóng.

## §3.1 · Châu Mỹ — **có một người, và người ấy đứng vững**

**Kʼakʼupakal `Q26904572`** (`P31 = Q5`, **không có** `P569`/`P570`, không có `P18`), Chichén Itzá.

Những gì tôi đọc được trực tiếp từ văn bản nguồn của Wikipedia tiếng Anh (bài `Chichen Itza` và bài `Kʼakʼupakal`, cả hai tôi tự tải về bằng `curl`, HTTP 200):
- Tên ông là **tên người riêng được nhắc nhiều nhất** trong các bi ký Maya còn lại ở Chichén Itzá, và còn xuất hiện ở **Uxmal** — tức ảnh hưởng của ông vượt khỏi một thành phố.
- Bi ký **Casa Colorada** mang một niên đại quy đổi ra **869 CN**.
- Niên đại chữ viết sớm nhất ở Chichén Itzá là **832**, muộn nhất là **998** — nên khung hoạt động của ông nằm gọn trong 801–900.

**Đề xuất:** `năm: hoạt động k. 869–890 CN`, `độ tin cậy niên đại: Thấp`. Lý do `Thấp` **không phải** vì nguồn kém — bi ký Maya là nguồn đương thời, chính xác hơn nhiều sử ký đời sau — mà vì **Wikidata không có `P569`/`P570` nào để đối chiếu** và vì khung năm phụ thuộc hoàn toàn vào việc quy đổi Lịch Đếm Dài, một phép quy đổi có hai hệ số tương quan GMT cạnh tranh.

> **Lưu ý quan trọng cho người viết mục:** đây là người thứ **ba** của Châu Mỹ trong atlas, sau `CH05-CE07-12 · Kʼinich Janaabʼ Pakal` (Palenque) và `CH05-CE08-12 · Yikʼin Chan Kʼawiil` (Tikal). Cả ba đều là Maya. Phải nói thẳng điều đó trong `## Ghi chú biên tập`: **"Châu Mỹ" trong atlas này hiện nghĩa là "Maya vùng đất thấp"** — Teotihuacan đã sụp, Moche đã tàn, Wari và Tiwanaku đang ở đỉnh trong thế kỷ 9 nhưng **không để lại chữ viết ghi tên người**. Đó là một giới hạn của tư liệu, và nó phải được khai báo chứ không được che.

## §3.2 · Châu Đại Dương — **vẫn trống, nhưng lý do của CE08 cần được chỉnh lại cho đúng**

CE08 lập luận Châu Đại Dương trống vì Đông Polynesia chỉ được định cư khoảng 1200–1290, dẫn Wilmshurst và cộng sự trên *PNAS*. Tôi đã **tự kiểm lại trích dẫn ấy qua Crossref** (DOI `10.1073/pnas.1015876108`) và phải báo hai điều:

**(a) Trích dẫn CE08 ghi năm sai.** Bài là Wilmshurst, Hunt, Lipo, Anderson, *"High-precision radiocarbon dating shows recent and rapid initial human colonization of East Polynesia"*, **PNAS 108(5): 1815–1820**, bản in **tháng 2 năm 2011**; **27-12-2010** chỉ là ngày đăng trực tuyến trước. Ghi chú CE08 ghi "(2010)". Nên sửa thành **2011** (hoặc "2011, trực tuyến 27-12-2010").

**(b) Lập luận của CE08 đúng kết luận nhưng sai phạm vi, và phải được mở rộng.** Nói "Châu Đại Dương chưa có người ở thế kỷ 9" là **sai**: thế kỷ 9 Úc đã có người ở hàng chục nghìn năm, Melanesia và Micronesia đã có người, và **Tây Polynesia (Tonga, Samoa, Fiji) đã được định cư từ thời Lapita**, trước đó khoảng 2.800 năm. Cái mà bài *PNAS* chứng minh là **Đông** Polynesia (Society, Hawaiʻi, Aotearoa, Rapa Nui) mới được định cư muộn.

**Vậy lý do thật sự khiến vùng này trống là lý do thứ hai, không phải lý do thứ nhất:** toàn Châu Đại Dương tiền tiếp xúc **không có hệ chữ viết nào ghi được tên người** (rongorongo của Rapa Nui, nếu là chữ viết, cũng muộn hơn nhiều và chưa giải mã), và các **gia phả truyền miệng** chỉ được ghi lại từ thế kỷ 19.

Tôi đã kiểm trường hợp **gần nhất** có thể phản bác: triều **Tuʻi Tonga**, mà truyền thống Tonga cho là bắt đầu với **ʻAhoʻeitu** — và nó **không phản bác**, vì hai lẽ độc lập: (i) niên đại truyền thống là **k. 950**, tức **thế kỷ 10**, không phải thế kỷ 9; (ii) ʻAhoʻeitu trong chính truyền thống ấy là **con của thần bầu trời Tangaloa ʻEitumātupuʻa**, bị các anh cùng cha giết và ăn thịt rồi được hồi sinh trong một cái `kumete` — tức một nhân vật **thần thoại**, mà ngay cả nhãn `Truyền thuyết` cũng chỉ hợp nếu atlas muốn một mục không có gì để nói về thế kỷ 9.

**Kết luận §3.2: Châu Đại Dương trống ở CE09, và sẽ còn trống ít nhất tới CE10.** Đây là một kết quả **có giá trị**, không phải một thất bại: nó cho biết atlas đang đo **phạm vi của chữ viết**, không phải phạm vi của lịch sử.

## §3.3 · Đông Nam Á — **một người lục địa, và đảo thì vẫn trống (ghi chú CE07 đúng)**

Ghi chú CE07 dự đoán: Jayavarman II chỉ phủ Khmer lục địa, nên **Đông Nam Á hải đảo vẫn trống sau CE09**. Tôi đã thử **phản bác** dự đoán ấy bằng hai ứng viên hải đảo và **thất bại**. Báo cáo lại việc thử:

**Ứng viên hải đảo 1 — Balaputradeva `Q4199265`.** Lý do hấp dẫn: ông được nêu tên trong **bia đồng Nālandā** do Devapala ban, tức một bi ký **đương thời ở ngoài khu vực**, loại bằng chứng mạnh hiếm có cho Đông Nam Á. Lý do loại: (i) **ông là người bảo trợ**, công trạng được ghi là **ra lệnh xây một tu viện Phật giáo ở Nālandā** — đúng dạng mà CE08 đã loại với Sanjaya và Panangkaran; (ii) phần "quan trọng" của ông — chuyện ông thua Rakai Pikatan năm 856 rồi chạy sang Srivijaya, biến Srivijaya thành cường quốc hàng hải Sailendra — **là giả thuyết của J. G. de Casparis (1956), không phải nội dung bi ký**. Bia Shivagrha chỉ nói tới "kẻ nổi loạn" dựng pháo đài bằng hàng trăm khối đá; việc đồng nhất kẻ ấy với Balaputra **đã bị học thuật xét lại**, với Rakai Walaing pu Kumbayoni nay được coi là ứng viên khả dĩ hơn. (iii) Bài Wikipedia tự thừa nhận "ghi chép về Balaputra thì ít ỏi".

**Ứng viên hải đảo 2 — Rakai Pikatan `Q7286535`.** Lý do hấp dẫn: người cho dựng **Prambanan**; bia **Shivagrha** niên đại **856 CN** (778 Śaka) là bi ký đương thời, hiện ở Bảo tàng Quốc gia Indonesia, số kiểm kê D.28. Lý do loại: (i) **lại là người bảo trợ công trình**; (ii) bài Wikipedia nói thẳng: *"The circumstances of Salaḍū's reign are highly conjectural, due to the limited amount of primary source material available"*; (iii) ngay bia Shivagrha cũng được khắc theo lệnh **người kế vị** ông ngay sau khi ông thoái vị.

**Người được chọn — Jayavarman II `Q379239`**, và phải nói rõ ông yếu ở đâu. Ông vào vì (b) và (d): ông đặt nền cho **đế quốc Khmer** và cho thời kỳ Angkor kéo dài tới giữa thế kỷ 15, qua lễ `devarāja` năm **802** trên núi Mahendraparvata (Phnom Kulen). Nhưng bằng chứng của ông là loại yếu nhất trong cả nhóm CE09, và bài Wikipedia tiếng Anh nói một câu không thể bỏ qua: **"No inscriptions securely identified with Jayavarman II have been found."** Mọi thứ ta biết đến từ bia **Sdok Kak Thom năm 1052**, tức **250 năm sau**, cộng với bia Baksei Chamkrong năm 947. Ngay cả chữ "Java" trong bia ấy — nơi ông tuyên bố độc lập khỏi — cũng đang bị tranh cãi là đảo Java, bán đảo Mã Lai, hay Kedah (Griffiths, *Archipel* 85/1, 2013).

**Đề xuất:** `độ tin cậy niên đại: Thấp`, và `P569 +0800/p7`, `P570 +0900/p7` trên Wikidata **không có tham chiếu** (§1.3) — **không được chép**. Viết `năm: trị vì k. 802–850 CN`.

## §3.4 · Châu Phi hạ Sahara — **có một người, và tiền lệ vùng đã có sẵn trong atlas**

**Câu hỏi vùng, giải trước.** Makuria đóng đô ở **Dongola**, nay thuộc Sudan. Atlas đã có tiền lệ: `ch02` xếp **hai vua Kush ở Napata (nay thuộc Sudan)** vào `Châu Phi hạ Sahara`. Vậy Makuria vào `Châu Phi hạ Sahara` là **theo tiền lệ sẵn có**, không phải một thao tác thống kê.

**Georgios I của Makuria `Q1525584`** (`P31 = Q5`, không `P18`).

Điều tôi đọc được: ông xuất hiện lần đầu trong sử liệu năm **835**, khi ở tuổi 20 được cha là Zacharias III phong đồng trị và **cử đi Baghdad** giải quyết tranh chấp về khoản *baqt* mà Makuria đã ngừng nộp trong thời Fitna thứ tư. Chuyến đi dẫn tới một **hiệp ước mới: xoá nợ tồn đọng và đổi *baqt* từ hàng năm thành ba năm một lần**. Ông về Dongola đầu **837**, trị vì một mình từ trước **856** tới khoảng **887**.

**Chất lượng bằng chứng — phải nói cả hai mặt.** Phần tự sự đến từ các sử gia Ai Cập **al-Maqrīzī, al-Balawī, Ibn Taghrībirdī**, tức **muộn hàng thế kỷ**, và bài Wikipedia tự cảnh báo rằng họ "mâu thuẫn nhau ở vài điểm". Nhưng khác với Jayavarman II, ca này **có một mỏ neo đương thời**: bi ký mộ chí của viên *tetrarch* Mariankouda, **tháng 6 năm 887**, nhắc tới Georgios **đã mất** — tức năm mất được một bi ký đương thời chặn lại.

**Niên đại trên Wikidata có hai giá trị rác, phải loại bỏ bằng tay:**

| Giá trị | Tham chiếu | Xử lý |
|---|---|---|
| `P569 +0815/p9` | `stated-in Q46002746` | **dùng** |
| `P569 +0900/p7` | `imported-from-wikimedia Q48183` | **bỏ** |
| `P570 +0887/p9` | `stated-in Q46002746` | **dùng** |
| `P570 +0920/p9` | **KHÔNG CÓ THAM CHIẾU** | **bỏ** |

**Đề xuất:** `năm: k. 815 – k. 887 CN, trị vì k. 856–887` và `độ tin cậy niên đại: Trung bình` — biên độ giữa các giá trị **học thuật** (không phải giữa các giá trị Wikidata) nằm trong ±25, và năm mất có mỏ neo bi ký. Người viết mục phải nêu rằng hai giá trị 900/920 là rác.

**Đã khảo sát và loại, để người sau khỏi làm lại:** Kanem — al-Yaʿqūbī **872** là ghi chép viết sớm nhất về vương quốc này, nhưng **không nêu tên một cá nhân nào**; Ghana — tương tự, có vương quốc, không có tên người; Igbo-Ukwu — đồ đồng niên đại phóng xạ quanh thế kỷ 9, nhưng **thợ đúc vô danh**; bờ Swahili — bi ký Kufic ở Kizimkazi niên đại **1107**, quá muộn; Aksum — đã ngừng đúc tiền từ đầu thế kỷ 8, không còn tên vua chắc chắn. **Kết luận: Châu Phi hạ Sahara thế kỷ 9 chỉ có Nubia Kitô giáo là nêu được tên người, và đó là vì Nubia nằm trong tầm viết của thư lại Ai Cập — lại là một dữ kiện về văn khố, không về lịch sử.**

## §3.5 · Trung Á — **một người, và tôi phải tự khai một xung đột lợi ích**

**Người đề xuất: Muḥammad al-Bukhārī `Q241026`.**

**Xung đột lợi ích, khai trước khi lập luận.** Trung Á đang ở **0,9% toàn atlas (2 người)**. Tôi **có động cơ** xếp al-Bukhārī vào Trung Á thay vì Trung Đông/Bắc Phi. `CONTRIBUTING.md` cấm đổi `vùng:` để cải thiện thống kê. Nên tôi áp một phép thử: **nếu thống kê không thành vấn đề, tôi có xếp ông vào Trung Á không?**

**Trả lời: có, và có tiền lệ ngay trong chính chương này.** `CH05-CE08-01 · Abu Muslim al-Khurasani` ghi `nơi: Merv và Khurasan` → `vùng: Trung Á`. Tức atlas **đã** quyết rằng một nhân vật trong thế giới Abbasid mà hoạt động ở Khurasan thì thuộc Trung Á, không thuộc Trung Đông. al-Bukhārī sinh ở **Bukhara**, mất ở **Khartank gần Samarkand**, và tên ông theo đúng nghĩa đen là "người Bukhara". Quy ước §5.3 nói `Trung Á` trong atlas này trên thực tế là **Transoxiana – đông Iran**; Bukhara và Samarkand là **trung tâm** của cái hộp đó, không phải rìa.

**Phản biện công bằng, phải ghi vào mục:** mười sáu năm thu thập ḥadīth của ông diễn ra **khắp Hijaz, Iraq, Ai Cập, Syria** — tức "nơi hoạt động chính" của ông, nếu hiểu là nơi làm việc nghiên cứu, **trải khắp thế giới Hồi giáo**. Tôi vẫn chọn Trung Á vì nơi ông **soạn, giảng, và chết** là Khurasan–Transoxiana, nhưng người viết mục phải nêu sự lưỡng nghĩa này chứ không được giấu.

**Niên đại (xem §1.3):** `P570` 31-08-870 ở `precision` tới ngày, và đây là **ca hiếm mà `p11` có cơ sở thật** — niên đại Hijrī (sinh 13 Shawwāl 194, mất đêm Eid al-Fiṭr 256) nằm trong chính truyền thống tiểu sử Hồi giáo. → `độ tin cậy niên đại: Cao`.

**Các ứng viên Trung Á khác đã khảo sát** (giữ lại để CE10 dùng, hoặc để ai đó lật lại tôi): **al-Tirmidhī `Q293578`** (824–892, Termez) — mạnh, nhưng là **học trò** của al-Bukhārī và đóng góp cùng loại, trùng vai; **Yaʿqūb ibn al-Layth al-Ṣaffār `Q45261`** (mất 879, Sistan) — chấm dứt độc quyền chính trị của người Ả Rập ở Iran, nhưng là một lãnh chúa quân sự, yếu ở (c); **Ismāʿīl Samānī `Q862648`** (mất **907**) — **thời kỳ ảnh hưởng chính rơi sang thế kỷ 10, phải để CE10**. Và một cảnh báo quy ước: **al-Khwārizmī, al-Farghānī, Abū Maʿshar al-Balkhī đều mang nisba Trung Á nhưng hoạt động ở Baghdad** — theo quy ước "nơi hoạt động chính, không phải nơi sinh", cả ba là **Trung Đông/Bắc Phi**. Không được dùng nisba để kéo thống kê.

## §3.6 · Nam Á — **hai ứng viên lý thuyết gia; một vào roster, một bị trần 12 cắt**

**Mahāvīrācārya `Q2269861`** (xem bẫy nhãn ở §1.2 — **bắt buộc** không được viết trần là "Mahāvīra"). Soạn ***Gaṇitasārasaṅgraha* năm 850 CN**, dưới triều Rāṣṭrakūṭa **Amoghavarsha I**. Điểm then chốt cho tiêu chí (c): đây là **văn bản Ấn Độ sớm nhất dành riêng hoàn toàn cho toán học** — trước đó toán học luôn là một chương phụ trong sách thiên văn. Ông **tách chiêm tinh khỏi toán học**, đặt thuật ngữ cho tam giác đều, tam giác cân, hình thoi, hình tròn, bán nguyệt, cho quy tắc hệ thống để phân tích phân số thành tổng các phân số đơn vị, và nêu rằng **căn bậc hai của số âm không tồn tại**. Sách được dịch sang **tiếng Telugu** bởi Pāvulūri Mallana — tức ảnh hưởng vượt khỏi vùng ngôn ngữ gốc. *Phải ghi cả chỗ ông sai:* ông khẳng định một số chia cho **không** thì không đổi — một bước **lùi** so với Brahmagupta. Ghi cả hai mặt là cách giữ tiêu chí (c) trung thực.
→ `năm: hoạt động k. 850 CN`, `độ tin cậy niên đại: Thấp` (không có niên đại độc lập; khung duy nhất là triều Amoghavarsha I).
**Nhưng ông KHÔNG vào roster** — ông là người thứ 13 và bị trần 12 cắt. Lý do và lập luận đầy đủ ở **§5.1**. Tôi để nguyên phần khảo sát ở đây vì vòng duyệt cần thấy ông đã được cân nhắc nghiêm túc, không phải bị bỏ sót.

**Ānandavardhana `Q2551244`** (`P31 = Q5`, không `P18`), Kashmir. Soạn ***Dhvanyāloka*** dưới triều **Avantivarman** (trị vì 855–883), được phong tước *Rājānaka*; được **Kalhaṇa nhắc tên trong *Rājataraṅgiṇī***. Đóng góp: lý thuyết ***dhvani*** — "gợi" (*vyañjanā*) là **linh hồn** (*ātman*) của thơ — và phép phân loại thơ làm ba hạng theo mức độ gợi. Tiêu chí (d) rất mạnh: **Abhinavagupta (k. 950–1016) viết bình chú *Locana* lên chính tác phẩm này**, và từ đó dhvani thành khung thẩm mỹ chủ đạo của toàn bộ thi học Sanskrit về sau. Bản dịch Anh ngữ đầy đủ kèm *Locana* do Daniel H. H. Ingalls và cộng sự thực hiện trong **Harvard Oriental Series**.
→ `năm: hoạt động k. 855–890 CN`, `độ tin cậy niên đại: Thấp`. Wikidata ghi 820–890 nhưng chỉ dựa vào **một nguồn cấp ba duy nhất** (`Q6023365`) và `P569` còn mang `imported-from-wikimedia`; mỏ neo chắc duy nhất là triều Avantivarman.

**Đã khảo sát và không chọn:** **Devapala** nhà Pāla — `Q27793406` là **trang định hướng Wikimedia (`P31 = Q4167410`)**, không phải người (§1.1); và dù giải được Q-ID đúng, ông vẫn là một vị vua bảo trợ. **Vācaspati Miśra** — niên đại dao động giữa **841 và 976**, một biên độ **135 năm**: không thể xếp nhóm thế kỷ, phải để CE10 quyết. **Śaṅkaranārāyaṇa** `Q7488718` → `P31 = Q56436498`, không phải `Q5` (§1.1). **Sureśvara** — không giải được Q-ID ổn định, và trùng vai với `CH05-CE08-11 · Ādi Shankara`. **Amoghavarsha I** — người bảo trợ, cùng dạng đã loại ở CE08.

## §3.7 · Đông Á — **ba người, chọn từ nhóm ứng viên đông nhất và cũng chật nhất**

Đông Á đang ở **24,4% toàn atlas** và **33,3% riêng ch05**. Thế kỷ 9 lại là một thế kỷ dày đặc ở Đông Á. Nên đây là vùng tôi phải **cắt**, không phải vùng tôi phải tìm. Tôi giữ **ba**, và nói rõ ai bị cắt (§5).

1. **Kūkai `Q222227`** (vi-label Wikidata: **"Không Hải"**), Nhật Bản, 774–835. Thời kỳ ảnh hưởng chính **806–835** nằm gọn trong thế kỷ 9, nên ông thuộc CE09 chứ không phải CE08. Sáng lập **Chân Ngôn tông (Shingon)**, lập **Kim Cương Phong tự** trên núi Kōya **816**, nhận **Đông tự (Tōji)** **823**. → §4 cho luận đề đầy đủ. Niên đại: `độ tin cậy niên đại: Cao` (774–835 không bị tranh cãi), **nhưng** giá trị `preferred` 27-07-774 ở `precision` tới ngày **không có tham chiếu** — đó là ngày truyền thống của tông Chân Ngôn, không phải tư liệu đương thời (§1.3). Viết `năm: 774–835 CN`, đừng chép ngày.
2. **Hàn Dũ `Q318998`** (vi-label đã có sẵn **"Hàn Dũ"**, alias vi "Hàn Thoái Chi", "Hàn Xương Lê"), 768–824. → §4.
3. **Trương Bảo Cao `Q493856`** (Jang Bogo / Chang Pogo), **k. 787–841**, Silla. → §4, và một đính chính niên đại ở §3.7.1 ngay dưới.

### §3.7.1 · Đính chính đề xuất của chính tôi ở §1.3 — Trương Bảo Cao: `Thấp` → **`Trung bình`**

Ở §1.3 tôi đã đề xuất `Thấp` **trước khi đọc nguồn**. Sau khi đọc, tôi nâng lên **`Trung bình`**, và ghi lại việc đổi ý thay vì sửa lặng lẽ.

Lý do: cuộc tranh chấp 841 vs 846 **không cân**. Phía **841** có **ba** chứng cứ độc lập và gần như đương thời: (i) ***Shoku Nihon Kōki*** (869) chép "Bogo mất vào tháng mười một năm ngoái"; (ii) nhật ký ***Nittō Guhō Junrei Kōki*** của **Ennin**, ghi rằng tháng 7 năm **845** viên "nguyên Kỵ binh Đô uý Thanh Hải trấn" đang lưu vong ở Liên Thuỷ, Trung Quốc sau một biến cố quốc gia; (iii) ***Tân Đường thư*** ghi các sứ bộ triều cống của Silla do Trương Bảo Cao dẫn **chấm dứt sau niên hiệu Hội Xương (841–846)**. Phía **846** chỉ có ***Tam quốc sử ký*** (thế kỷ 12). **Uỷ ban Biên soạn Quốc sử Hàn Quốc** theo 841.

**Hệ quả, và đây là điểm phải ghi vào `## Ghi chú biên tập`:** Wikidata để **841 ở hạng `deprecated`** và **846 ở hạng `preferred`**. Tức Wikidata đã **chọn phe**, và chọn **phe yếu hơn**. Đây là ví dụ sạch nhất tôi tìm được cho luận điểm của CE08 rằng "Wikidata khai độ chính xác, nó không khai độ tin cậy" — ở đây nó còn khai cả **thứ hạng**, và thứ hạng ấy sai. **Người viết mục phải ghi `841`, không được chép giá trị `preferred`.**

## §3.8 · Châu Âu — **một người, và đây là chỗ tôi cố tình cắt sâu nhất**

Châu Âu đang ở **26,7% toàn atlas**. Thế kỷ 9 ở châu Âu có **nhiều** ứng viên qua được cổng: Alfred Đại đế, Photios I, Constantinus–Cyrillus và Methodius, Rabanus Maurus, Hincmar xứ Reims, Gottschalk xứ Orbais, ʿAbd al-Raḥmān II ở Córdoba, Ziryāb. Tôi **chỉ lấy một**, và lấy người mạnh nhất ở tiêu chí **(c) tính nguyên bản**, không phải người nổi tiếng nhất.

**Johannes Scotus Eriugena `Q184500`** (`P31 = Q5`), Ireland, hoạt động tại triều Charles Hói. Lý do: ông là **nhà siêu hình học Latin nguyên bản duy nhất** giữa Augustinus và Anselmus, là người **đọc được tiếng Hy Lạp** trong một Tây Âu gần như không ai đọc được, và ông **dịch Pseudo-Dionysius Areopagita sang tiếng Latin** — một hành vi truyền tải có hệ quả kéo dài tới Nicolaus Cusanus và chủ nghĩa thần bí Rhineland. *Periphyseon* là một hệ thống, không phải một bộ sưu tập.

**Niên đại: `Thấp`.** `P569` khai ở `p8` = **độ chính xác thập kỷ** (k. 800); `P570` 877 mang `imported-from-wikimedia` cộng một nguồn tiểu sử. Không có năm sinh hay năm mất nào được chứng thực.

Ai bị cắt và vì sao — ở §5. Nhưng nói ngay ở đây một điều để người viết mục khỏi hiểu lầm: **Alfred Đại đế bị cắt vì trần 12 và vì cân vùng, không phải vì ông không đủ chuẩn.** Ông đủ chuẩn, và niên đại của ông là loại **tốt nhất** trong cả nhóm (848/9 – 26-10-899, có *Asser* và *Anglo-Saxon Chronicle*, `độ tin cậy niên đại: Cao`). Ông là **một trong hai người dự bị** của nhóm này, cùng với Mahāvīrācārya (§5.1). Nếu vòng duyệt muốn đảo, hãy đảo với một trong **ba** người Đông Á hoặc **ba** người Trung Đông — **không** được đảo với bốn người ở vùng mỏng, vì đảo như thế là xoá một vùng khỏi bản đồ.

## §3.9 · Trung Đông/Bắc Phi — **ba người, cắt từ một danh sách mà tám người đều qua cổng**

Vùng này đang ở **33,0% toàn atlas**, cao nhất. Và thế kỷ 9 **đúng là** thế kỷ Abbasid. Hai sự thật ấy xung đột, và tôi giải bằng cách **giữ ba, không giữ tám**, chọn theo nguyên tắc: **ưu tiên người làm ra tri thức, loại người chi tiền cho tri thức; ưu tiên người lấp được lĩnh vực đang trống.**

1. **Muḥammad ibn Mūsā al-Khwārizmī `Q9038`** — `Toán học`. Không thể bỏ: đại số như một **môn học có đối tượng riêng**, thuật toán, và kênh truyền chữ số Ấn–Ả Rập. `độ tin cậy niên đại: Thấp` — *Dictionary of Scientific Biography* ghi nguyên văn **"(b. before 800; d. after 847)"**, biên độ sinh ~30 năm, vượt dung sai của `Trung bình` (±25).
2. **Ḥunayn ibn Isḥāq `Q503130`** — `Y học`. **Đây là mục lấp ô `Y học`**, lĩnh vực mỏng nhất atlas (**1,1%**), và là **cách đúng để đưa phong trào dịch thuật vào atlas** sau khi §2.1 đã tháo bỏ huyền thoại Bayt al-Ḥikma. `độ tin cậy niên đại: Cao` (808/809–873, biên độ 1 năm, có nhiều nguồn bách khoa độc lập).
3. **Aḥmad ibn Ḥanbal `Q194442`** — `Luật` + `Tôn giáo/Tâm linh`. Phía **thắng** của cuộc *Miḥna*, và là phía **tồn tại lâu dài**. `độ tin cậy niên đại: Cao` (780–855 không bị tranh cãi; chỉ các **ngày** mới vô nguồn — §1.3). **Bẫy nhãn: vi-label Wikidata là "Hanbal" trần**, mà Ḥanbal là tên **cụ cố** của ông. Phải viết đầy đủ (§1.2).

**Bị cắt từ vùng này, với lý do ở §5:** al-Maʾmūn, al-Kindī, al-Ṭabarī, Ibn Khordādbeh, anh em Banū Mūsā, Harun al-Rashid (§2.1).

---

# §4 · Roster đề xuất — 12 người

**Thứ tự đánh số theo `CONTRIBUTING.md` §3/§5.3: xếp theo *thời kỳ ảnh hưởng chính*, không theo năm sinh.** Vì vậy Hàn Dũ (sinh 768) đứng trước Kūkai (sinh 774) nhưng sau Jayavarman II (sinh không rõ), và Ḥunayn (sinh 808) đứng trước Aḥmad ibn Ḥanbal (sinh 780) — vì mốc neo của Ibn Ḥanbal là *Miḥna* 833, còn Ḥunayn đã dịch từ khoảng 830.

**Quy ước của §4 này:**
- Dòng metadata viết đúng dạng sẽ dán vào `content/ch05.md`. Người viết mục **vẫn phải tự kiểm lại**, đây là đề xuất chứ không phải bản chốt.
- `Ảnh hưởng tới:` chỉ dùng **ID đã tồn tại** khi có; mọi đích ở sau thế kỷ 9 viết **mô tả tự do**, vì quy tắc 8 cấm trỏ tới ID chưa có. Các liên kết **trong nội bộ CE09** (ví dụ Ibn Ḥanbal → al-Bukhārī, vốn là thầy–trò thật) cũng viết **mô tả tự do**, kèm ghi chú rằng khi cả hai mục đã tồn tại thì có thể chuyển thành ID.
- Mỗi người có **2–3 nguồn, mỗi URL do tôi tự `curl` kiểm** (User-Agent trung tính). Mã HTTP ghi ngay sau. Nguồn nào tôi **không** mở được thì ghi `[KHÔNG KIỂM ĐƯỢC]` kèm lý do, và **không** dùng nó làm chỗ dựa cho luận điểm.

---

## CH05-CE09-01 · Jayavarman II (ជ័យវរ្ម័នទី២)

`năm: trị vì k. 802–850 CN | nơi: Mahendraparvata (Phnom Kulen) và Hariharalaya, Campuchia | vùng: Đông Nam Á | lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh | độ tin cậy niên đại: Thấp | wikidata: Q379239 | câu hỏi lớn: Không áp dụng`

**Luận đề cho "Tư tưởng / đóng góp chính":** Nghi lễ *devarāja* năm 802 trên Phnom Kulen không phải một lễ đăng quang mà là một **phát minh thể chế** — nó gắn vương quyền Khmer vào một nghi quỹ Shaiva khiến ngai vàng trở thành một vị trí vũ trụ luận chứ không chỉ một vị trí chính trị, và chính cái khung ấy đỡ cả thời kỳ Angkor suốt sáu thế kỷ rưỡi.

**Luận đề cho "Vì sao chọn":** Ông vào atlas vì tiêu chí (b) độ bền và (d) phản thực — bỏ ông đi thì không còn giải thích được vì sao một vùng vốn phân mảnh thành các *muang* lại sinh ra một nhà nước tập quyền kéo dài tới 1431 — **nhưng** ông cũng là mục có bằng chứng yếu nhất nhóm, và mục phải nói thẳng điều đó.

**Kế thừa từ:** `CH05-CE06-11 · kế thừa · suy đoán học giả` (đường nối Chenla → Khmer là tái dựng của học giả, không phải lời bia).
**Ảnh hưởng tới:** `Thể chế devarāja và toàn bộ thời kỳ Angkor tới 1431 · kế thừa · suy đoán học giả`; `Yaśovarman I và việc dời đô về Yaśodharapura 889 · kế thừa · suy đoán học giả`.

**Nguồn (đã tự mở kiểm):**
1. Arlo Griffiths, "The Problem of the Ancient Name Java and the Role of Satyavarman in Southeast Asian International Relations around the Turn of the Ninth Century CE", *Archipel* 85 (2013), tr. 43–81 — `https://www.persee.fr/doc/arch_0044-8613_2013_num_85_1_4384` (**HTTP 200**). Dùng cho: chữ "Java" trong bia Sdok Kak Thom đang bị tranh cãi.
2. Bản toàn văn mở của cùng bài — `https://hal.science/hal-01958103/document` (**HTTP 200**).
3. G. Cœdès, *The Indianized States of Southeast Asia* — `https://archive.org/details/vxuz-the-indianized-states-of-southeast-asia-by-g-coede` (**HTTP 200**). Dùng cho: tự sự chuẩn về 802 và Hariharalaya; **phải đọc như nguồn cấp hai cũ**, vì chính tự sự này là cái mà Griffiths đang xét lại.

> **Cảnh báo bắt buộc ghi vào mục:** *"No inscriptions securely identified with Jayavarman II have been found."* Mọi niên đại đến từ bia **Sdok Kak Thom năm 1052** (250 năm sau) và bia Baksei Chamkrong năm 947. Wikidata `P569 +0800/p7` và `P570 +0900/p7` là **giá trị độn, không tham chiếu — không được chép** (§1.3).

---

## CH05-CE09-02 · Hàn Dũ (韓愈 Hán Yù, Hàn Xương Lê)

`năm: 768–824 CN | nơi: Trường An và Triều Châu, nhà Đường | vùng: Đông Á | lĩnh vực: Văn học, Triết học | độ tin cậy niên đại: Cao | wikidata: Q318998 | câu hỏi lớn: Con người`

**Luận đề cho "Tư tưởng / đóng góp chính":** Hàn Dũ làm hai việc cùng một lúc và chúng là một việc — ông đòi bỏ lối biền ngẫu để trở về **cổ văn**, và ông dựng khái niệm **đạo thống**: một chuỗi truyền thừa Nghiêu → Thuấn → Vũ → Thang → Văn → Vũ → Chu Công → Khổng Tử → Mạnh Tử rồi **đứt**, mà hệ quả của chữ "đứt" ấy là một lời mời: có chỗ trống để ai đó nối.

**Luận đề cho "Vì sao chọn":** Tiêu chí (d) rất mạnh — *Nguyên đạo* và *Luận Phật cốt biểu* (819) là nơi Nho giáo lần đầu tự định nghĩa bằng cách **loại trừ** Phật và Lão thay vì hấp thụ chúng, và toàn bộ Tân Nho học đời Tống về sau tự nhận là người nối vào chỗ đứt mà ông chỉ ra.

**Kế thừa từ:** `CH02-BCE06-01 · kế thừa · qua trường phái`; `CH03-BCE04-04 · kế thừa · trực tiếp` (ông nâng Mạnh Tử lên làm người cuối cùng của đạo thống — một thao tác **chọn lựa**, không phải một sự thật có sẵn).
**Ảnh hưởng tới:** `CH02-BCE06-03 · phản bác · trực tiếp` (Luận Phật cốt biểu 819 công kích thẳng việc rước xá-lợi vào cung); `Tân Nho học đời Tống, đặc biệt Chu Hy và khái niệm đạo thống · kế thừa · qua trường phái`; `Phong trào cổ văn đời Tống (Âu Dương Tu, Tô Thức) · kế thừa · qua trường phái`.

**Nguồn (đã tự mở kiểm — cả hai là *văn bản gốc*, không phải diễn giải):**
1. 韓愈, 《原道》, trong 全唐文 卷0558 — `https://zh.wikisource.org/wiki/原道` (**HTTP 200**). Mở đầu "博愛之謂仁…"; chứa nguyên văn chuỗi đạo thống và đoạn công kích Lão–Phật.
2. 韓愈, 《論佛骨表》 (819) — `https://zh.wikisource.org/wiki/論佛骨表` (**HTTP 200**). Bản tấu khiến ông bị đày xuống Triều Châu.
3. 韓愈, 《師說》 — `https://zh.wikisource.org/wiki/師說` (**HTTP 200**). Dùng cho phần "thầy–đạo", nếu mục muốn chạm `Giáo dục`.

> **Ghi chú nguồn:** `ctext.org` **[KHÔNG KIỂM ĐƯỢC]** — trả về thông báo chống thu thập dữ liệu thay vì văn bản, với User-Agent trung tính bắt buộc. Tôi **không** giả mạo User-Agent trình duyệt, nên chuyển sang Wikisource, vốn ghi rõ xuất xứ 全唐文/卷0558.

---

## CH05-CE09-03 · Kūkai (空海, Không Hải; thuỵ hiệu Kōbō Daishi)

`năm: 774–835 CN | nơi: Trường An; núi Kōya và Tōji, Nhật Bản | vùng: Đông Á | lĩnh vực: Tôn giáo/Tâm linh, Triết học | độ tin cậy niên đại: Cao | wikidata: Q222227 | câu hỏi lớn: Thực tại, Vũ trụ`

**Luận đề cho "Tư tưởng / đóng góp chính":** Kūkai lật ngược quan hệ giữa ngôn ngữ và thực tại — với ông, Pháp thân Đại Nhật **đang thuyết pháp** bằng chính hiện tượng của vũ trụ (*hosshin seppō*), nên âm thanh, chữ viết và nghĩa không phải ba tầng tách rời mà là một cấu trúc cộng hưởng duy nhất; từ đó ông rút ra *sokushin jōbutsu*, thành Phật **ngay trong thân này**, chứ không sau vô lượng kiếp.

**Luận đề cho "Vì sao chọn":** Tiêu chí (c) — SEP gọi ông là một trong những nhà tư tưởng Phật giáo **hệ thống và triết học nhất** của Nhật Bản và có lẽ của cả Đông Á, và *Thập trụ tâm luận* là một phép phân hạng toàn bộ tư tưởng đương thời thành mười bậc, tức một siêu-lý-thuyết chứ không phải một tông phái thêm vào.

**Kế thừa từ:** `Huệ Quả (惠果) ở chùa Thanh Long, Trường An · kế thừa · trực tiếp` (ông thụ pháp và thành tổ thứ tám của Mật giáo trong vòng chưa tới hai năm); `CH04-CE02-08 · kế thừa · qua trường phái`; `CH05-CE07-06 · kế thừa · qua trường phái` (kênh Hán dịch mà ông dựa vào).
**Ảnh hưởng tới:** `Chân Ngôn tông và toàn bộ Mật giáo Nhật Bản · kế thừa · trực tiếp`; `Khung honji-suijaku hoà Thần đạo vào Phật giáo · kế thừa · qua trường phái`; `Mỹ học và thư pháp cung đình Heian · kế thừa · qua trường phái`.

**Nguồn (đã tự mở kiểm):**
1. "Kūkai", *Stanford Encyclopedia of Philosophy* — `https://plato.stanford.edu/entries/kukai/` (**HTTP 200**). Nguyên văn: Kūkai (774–835 CE) "is one of the intellectual giants of Japan"; mục lục có các tiết *Hosshin Seppō*, *Sokushinjōbutsu*, *Sanmitsu*, *Ten States*.
2. "Japanese Philosophy", *Stanford Encyclopedia of Philosophy* — `https://plato.stanford.edu/entries/japanese-philosophy/` (**HTTP 200**). Nguyên văn: Shingon "founded by Kūkai, 774–835"; Kūkai là "the pioneering figure and the more sophisticated philosopher".

> **Cảnh báo niên đại (§1.3):** giá trị `preferred` **27-07-774** trên Wikidata ở `precision` tới ngày và **không có tham chiếu** — đó là ngày truyền thống của tông Chân Ngôn. Viết `năm: 774–835 CN`, **đừng chép ngày**. `độ tin cậy niên đại: Cao` là chấm cho **khung năm**, không cho ngày.

---

## CH05-CE09-04 · Al-Khwarizmi (محمد بن موسى الخوارزمي)

`năm: hoạt động k. 813–847 CN | nơi: Baghdad, Iraq | vùng: Trung Đông/Bắc Phi | lĩnh vực: Toán học, Khám phá/Địa lý | độ tin cậy niên đại: Thấp | wikidata: Q9038 | câu hỏi lớn: Không áp dụng`

**Luận đề cho "Tư tưởng / đóng góp chính":** *Al-kitāb al-mukhtaṣar fī ḥisāb al-jabr wa-l-muqābala* không giải các bài toán khó hơn người đi trước — nó làm một việc khác hẳn: **phân loại mọi phương trình bậc hai thành sáu dạng chuẩn** rồi đưa thuật giải phổ quát cho từng dạng, tức biến "giải phương trình" từ một tập hợp mẹo thành **một môn học có đối tượng riêng**; cuốn *Kitāb Ṣūrat al-Arḍ* (833) thì hiệu chỉnh toạ độ của Ptolemy cho vùng Hồi giáo và Địa Trung Hải.

**Luận đề cho "Vì sao chọn":** Hai danh từ chung trong mọi ngôn ngữ khoa học hiện nay — *algebra* và *algorithm* — là tên ông và tên sách ông; ít người trong atlas đáp ứng tiêu chí (b) độ bền một cách thô bạo đến thế.

**Kế thừa từ:** `CH05-CE07-08 · kế thừa · qua trường phái` (hệ thập phân vị trí và số không, truyền qua *Sindhind*); `CH04-CE02-05 · phản bác · trực tiếp` (*Ṣūrat al-Arḍ* sửa toạ độ *Geographia*); `CH04-CE03-08 · tương đồng độc lập · suy đoán học giả`.
**Ảnh hưởng tới:** `Bản dịch Latin TK 12 (Robert xứ Chester, Gerard xứ Cremona) và từ "algebra" · kế thừa · qua trường phái`; `Chữ số Ấn–Ả Rập trong tính toán châu Âu · kế thừa · qua trường phái`.

**Nguồn (đã tự mở kiểm):**
1. "Al-Khwarizmi", *MacTutor History of Mathematics* — `https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/` (**HTTP 200**). Dùng cho: "Born about 780 … Died about 850"; tranh luận Toomer–Rashed về nisba; và **al-Ṭabarī gọi ông là "al-Qutrubbulli"**, tên một quận gần Baghdad — tức chính nguồn Ả Rập sớm neo ông vào Iraq.
2. F. Rosen (dịch), *The Algebra of Mohammed ben Musa* (London, 1831) — `https://archive.org/details/algebraofmohamme00khuwrich` (**HTTP 200**). Bản dịch Anh ngữ đầy đủ kèm nguyên bản Ả Rập; dùng cho sáu dạng chuẩn.
3. Encyclopaedia Britannica và *Encyclopædia Iranica* — **[KHÔNG KIỂM ĐƯỢC — HTTP 403 với User-Agent trung tính bắt buộc]**. Không dùng làm chỗ dựa.

> **Quyết định vùng, nói rõ để khỏi bị hiểu lầm:** nisba "al-Khwārizmī" trỏ về Khwarezm (Trung Á), và Trung Á đang là vùng mỏng (0,9%). Tôi **vẫn** xếp ông `Trung Đông/Bắc Phi` theo quy ước "nơi hoạt động chính, không phải nơi sinh" (§5.3), và MacTutor đưa một chứng cứ độc lập ủng hộ: biệt danh al-Ṭabarī đặt cho ông neo vào vùng Baghdad. **Không dùng nisba để kéo thống kê.**
> **Niên đại `Thấp`:** *Dictionary of Scientific Biography* ghi nguyên văn "(b. before 800; d. after 847)" — biên độ sinh ~30 năm, vượt dung sai của `Trung bình` (±25). Nên viết dạng `hoạt động k. …`, không viết năm sinh–năm mất.

---

## CH05-CE09-05 · Trương Bảo Cao (張保皐, Jang Bogo / Chang Pogo)

`năm: k. 787–841 CN | nơi: Thanh Hải trấn (Cheonghaejin), đảo Wando, Silla | vùng: Đông Á | lĩnh vực: Kinh tế, Quân sự | độ tin cậy niên đại: Trung bình | wikidata: Q493856 | câu hỏi lớn: Không áp dụng`

**Luận đề cho "Tư tưởng / đóng góp chính":** Ông biến một đồn quân trấn hải tặc thành **trung tâm điều phối của cả một hệ thương mại ba bên Silla – Đường – Nhật Bản**: Thanh Hải trấn (lập 828) vừa là hải quân vừa là nhà băng vừa là bến trung chuyển, dựa trên mạng lưới kiều dân Silla ở Sơn Đông và Giang Tô — tức một mô hình **quyền lực phi-triều-đình dựa trên kiểm soát tuyến đường biển**, khác hẳn mọi dạng quyền lực mà Đông Á thế kỷ 9 công nhận.

**Luận đề cho "Vì sao chọn":** Mục này lấp ô `Kinh tế` — lĩnh vực đang ở **1,7%** toàn atlas — bằng một người mà đóng góp **thật sự là kinh tế**, không phải một ông vua được gán nhãn kinh tế; và tiêu chí (d) rất rõ: sau khi ông bị ám sát, hệ thống ấy sụp và Silla mất quyền kiểm soát biển.

**Kế thừa từ:** `Mạng lưới kiều dân Silla ở Sơn Đông – Giang Tô và các Tân La phường · kế thừa · trực tiếp`; `Chế độ phiên trấn nhà Đường mà ông từng phục vụ với tư cách võ quan · kế thừa · trực tiếp`.
**Ảnh hưởng tới:** `Thương mại biển Hoàng Hải – Đông Hải thế kỷ 9 và các chuyến đi của tăng nhân Nhật Bản · kế thừa · trực tiếp`; `Việc Silla mất quyền kiểm soát hải lộ sau 851 · phản bác · suy đoán học giả`.

**Nguồn (đã tự mở kiểm):**
1. 국사편찬위원회, *신편 한국사* 권11 — `https://contents.history.go.kr/front/nh/view.do?levelId=nh_011_0030_0030` (**HTTP 200**). Chứa tiết "3. 장보고와 청해진"; đây là lập trường của **Uỷ ban Biên soạn Quốc sử Hàn Quốc**.
2. 한국 고대 사료 DB (국사편찬위원회), *三國史記* 권44 — `https://db.history.go.kr/ancient/level.do?levelId=sg_044r_0020_0010` (**HTTP 200**). **Đây là nguồn quan trọng nhất của mục này**, vì chú giải của chính cơ quan ấy nói rằng 張保皐列傳 "국내 기록은 전혀 참조하지 않고" — **không tham khảo một ghi chép trong nước nào** — mà chủ yếu **chép lại** 張保皐鄭年傳 trong 樊川文集 của **Đỗ Mục** (dẫn 전덕재, 2021).

> **Đây là lý do niên đại, và phải ghi vào mục:** nếu *Tam quốc sử ký* (TK 12) ở chỗ này chỉ là bản sao một tiểu truyện văn chương Trung Hoa TK 9, thì con số **846** của nó **không phải** một chứng cứ độc lập. Phía **841** có ba chỗ dựa gần đương thời: *Shoku Nihon Kōki* (869), nhật ký Ennin (tháng 7 năm 845), và *Tân Đường thư* về việc sứ bộ chấm dứt. **Viết 841.**
> **Cảnh báo Wikidata (§3.7.1):** Wikidata để **841 ở hạng `deprecated`** và **846 ở `preferred`** — tức nó đã chọn phe, và chọn phe yếu hơn. **Không được chép giá trị `preferred`.**

---

## CH05-CE09-06 · Hunayn ibn Ishaq (حنين بن إسحاق)

`năm: 808–873 CN | nơi: al-Hira và Baghdad, Iraq | vùng: Trung Đông/Bắc Phi | lĩnh vực: Y học, Ngôn ngữ học | độ tin cậy niên đại: Cao | wikidata: Q503130 | câu hỏi lớn: Con người`

**Luận đề cho "Tư tưởng / đóng góp chính":** Ḥunayn không chỉ dịch Galen — ông **phát minh ra một phương pháp dịch**: đối chiếu nhiều thủ bản Hy Lạp để dựng bản nền, dịch theo **nghĩa** chứ không theo từng chữ, rồi tự kiểm kê công việc của chính mình trong một bức thư liệt kê **129 tác phẩm Galen** cùng tình trạng từng bản; cuốn *Kitāb al-Masāʾil fī al-ṭibb li-l-mutaʿallimīn* của ông, vào châu Âu dưới tên *Isagoge*, trở thành sách nhập môn y học của phương Tây suốt nhiều thế kỷ.

**Luận đề cho "Vì sao chọn":** Mục này lấp ô `Y học` — lĩnh vực **mỏng nhất atlas (1,1%)** — và nó là **cách đúng để đưa phong trào dịch thuật Abbasid vào atlas** sau khi §2.1 đã tháo bỏ huyền thoại Bayt al-Ḥikma: atlas ghi **người dịch**, không ghi người chi tiền.

**Kế thừa từ:** `CH04-CE02-06 · kế thừa · trực tiếp`; `CH02-BCE05-04 · kế thừa · qua trường phái`; `Truyền thống y học Syriac ở Jundishapur và Yuhanna ibn Masawayh · kế thừa · trực tiếp`.
**Ảnh hưởng tới:** `Y học Latin TK 11–13 qua Isagoge trong tuyển tập Articella · kế thừa · qua trường phái`; `Thuật ngữ y học và triết học Ả Rập về sau · kế thừa · trực tiếp`.

**Nguồn (đã tự mở kiểm):**
1. U.S. National Library of Medicine, "Islamic Culture and the Medical Arts — Ḥunayn ibn Isḥāq al-ʿIbādī" — `https://www.nlm.nih.gov/hmd/arabic/bioH.html` (**HTTP 200**). Dùng cho: ông là **Kitô hữu Nestorian** gốc nam Iraq làm việc ở Baghdad; **95 bản Syriac + 34 bản Ả Rập** các tác phẩm Galen; và *Kitāb al-Masāʾil* → *Isagoge*.
2. "Hunayn ibn Ishaq", *MacTutor History of Mathematics* — `https://mathshistory.st-andrews.ac.uk/Biographies/Hunayn/` (**HTTP 200**). Dùng cho khung niên đại **808 (al-Hira) – 873 (Baghdad)** và địa vị "the leading translator".

> **Bẫy nguồn, phải xử trong mục:** NLM ghi ông mất **"873 hoặc 877"** — tức rộng hơn "biên độ 1 năm" mà §1.3 của chính tôi đã viết. Tôi sửa lại ở đây thay vì để nguyên: biên độ thật là **4 năm**. `Cao` vẫn đúng (dung sai ±5), nhưng lý do phải ghi cho đúng.
> **Bẫy nguồn thứ hai:** MacTutor gọi ông là dịch giả hàng đầu **"in the House of Wisdom"**. Đó đúng là mệnh đề mà §2.1 đã chỉ ra là đang bị học thuật tháo dỡ (İhsanoğlu 2023). Dùng MacTutor cho **niên đại và địa vị**, **không** dùng nó cho mệnh đề thiết chế.

---

## CH05-CE09-07 · Ahmad ibn Hanbal (أحمد بن حنبل)

`năm: 780–855 CN | nơi: Baghdad, Iraq | vùng: Trung Đông/Bắc Phi | lĩnh vực: Luật, Tôn giáo/Tâm linh | độ tin cậy niên đại: Cao | wikidata: Q194442 | câu hỏi lớn: Con người`

**Luận đề cho "Tư tưởng / đóng góp chính":** Khi al-Maʾmūn áp *Miḥna* từ năm 833, buộc giới học giả công khai thừa nhận Qurʾān là **được tạo ra**, Ibn Ḥanbal chịu tù và đòn roi thay vì ký — và thắng lợi cuối cùng của ông không phải là một luận chứng thần học mà là một **nguyên tắc về nguồn quyền uy**: giáo lý do *ḥadīth* và cộng đồng học giả xác lập, không do caliph ban bố.

**Luận đề cho "Vì sao chọn":** Tiêu chí (d) ở dạng mạnh nhất có thể — *Miḥna* là lần duy nhất quyền lực chính trị Hồi giáo thử nắm quyền định tín điều, và việc nó **thất bại** đã định hình quan hệ giữa nhà nước và *ʿulamāʾ* trong toàn bộ lịch sử Sunni về sau; thêm nữa *Musnad* của ông, khoảng 28.000 ḥadīth, là một trong những bộ sưu tập lớn nhất còn lại.

**Kế thừa từ:** `CH05-CE07-01 · kế thừa · qua trường phái`; `CH05-CE08-04 · phản bác · suy đoán học giả` (ông đứng ở cực đối lập với lối *raʾy*, suy lý cá nhân, của trường phái Kufa); `al-Shafiʿi · kế thừa · trực tiếp`.
**Ảnh hưởng tới:** `Trường phái luật Ḥanbalī, một trong bốn madhhab Sunni · kế thừa · trực tiếp`; `Ibn Taymiyya và các phong trào phục cổ về sau · kế thừa · qua trường phái`; `Người soạn ḥadīth thế hệ kế tiếp ở Khurasan — xem CH05-CE09-08 · kế thừa · trực tiếp`.

**Nguồn (đã tự mở kiểm):**
1. Walter M. Patton, *Aḥmed Ibn Ḥanbal and the Miḥna* (Leiden: Brill, 1897) — `https://archive.org/details/ahmedibnhanbalan00pattuoft` (**HTTP 200**). Chuyên khảo toàn văn, phạm vi công cộng; nhan đề phụ ghi rõ là tiểu sử kèm trần thuật về *Miḥna*. **Cũ (1897) — dùng cho tự sự sự kiện, không dùng cho diễn giải.**
2. John A. Nawas, "A Reexamination of Three Current Explanations for al-Maʾmūn's Introduction of the Miḥna", *International Journal of Middle East Studies* (tháng 11, 1994), DOI `10.1017/S0020743800061134` — **siêu dữ liệu xác minh qua Crossref API, HTTP 200**. **[KHÔNG KIỂM ĐƯỢC phần toàn văn — trang JSTOR/Cambridge trả 403 với User-Agent trung tính bắt buộc.]** Nêu ra để người viết mục biết có một bài **xét lại ba cách giải thích thông dụng** về động cơ của *Miḥna*; đừng trình bày động cơ ấy như đã ngã ngũ.

> **Bẫy nhãn (§1.2), bắt buộc:** nhãn `vi` trên Wikidata là **"Hanbal" trần**, mà Ḥanbal là tên **ông cố** của ông. Phải viết đầy đủ **Ahmad ibn Hanbal**.
> **Niên đại:** `P569` 23-11-780 và `P570` 02-08-855 ở `precision` tới ngày và **không có tham chiếu nào** — đúng hình dạng ca Charles Martel của CE08. Các giá trị cấp **năm** thì có nguồn. Viết `780–855 CN`.

---

## CH05-CE09-08 · Georgios I của Makuria (ⲅⲉⲱⲣⲅⲓⲟⲥ)

`năm: k. 815 – k. 887 CN, trị vì k. 856–887 | nơi: Dongola, Makuria (nay thuộc Sudan) | vùng: Châu Phi hạ Sahara | lĩnh vực: Chính trị/Nhà nước, Kinh tế | độ tin cậy niên đại: Trung bình | wikidata: Q1525584 | câu hỏi lớn: Không áp dụng`

**Luận đề cho "Tư tưởng / đóng góp chính":** Năm 835, ở tuổi hai mươi, ông được cha cử tới Baghdad để gỡ món nợ *baqt* mà Makuria đã ngừng nộp trong thời Fitna thứ tư — và ông mang về một **hiệp ước viết lại điều khoản**: xoá nợ tồn đọng, đổi *baqt* từ hàng năm sang **ba năm một lần**; đó là một vương quốc Kitô giáo ở ngoài rìa thế giới Hồi giáo **đàm phán lại luật chơi** với trung tâm của nó, không phải một nước triều cống.

**Luận đề cho "Vì sao chọn":** Đây là **nhân vật duy nhất ở Châu Phi hạ Sahara thế kỷ 9 mà ta nêu được tên, nêu được việc làm, và neo được năm mất vào một bi ký đương thời** — và sự duy nhất ấy tự nó là dữ kiện phải ghi: Kanem, Ghana, Igbo-Ukwu, bờ Swahili đều có vương quốc hoặc có hiện vật, nhưng **không có tên người**.

**Kế thừa từ:** `CH04-CE04-02 · kế thừa · qua trường phái` (Kitô giáo Nubia đi qua toà Alexandria); `Zacharias III, cha ông, người phong ông làm đồng trị năm 835 · kế thừa · trực tiếp`.
**Ảnh hưởng tới:** `Makuria Kitô giáo duy trì tới thế kỷ 14 · kế thừa · suy đoán học giả`; `Khung quan hệ baqt giữa Nubia và Ai Cập Hồi giáo · kế thừa · trực tiếp`.

**Nguồn (đã tự mở kiểm — cả hai là *bi ký*, không phải sử ký muộn):**
1. *Database of Medieval Nubian Texts* (Đại học Warszawa), văn bản số 12 — `https://dbmnt.uw.edu.pl/texts/12/` (**HTTP 200**). Mộ chí Hy ngữ trên bia đá cẩm thạch của **Mariankouda, tetrarch của Makuria**, tìm thấy ở **Hambukol**, hiện ở Bảo tàng Quốc gia Sudan số **SNM 30149**, niên đại **5 tháng 6 năm 887**, có nhắc tới **vua Georgios**.
2. *Database of Medieval Nubian Texts*, văn bản số 33 — `https://dbmnt.uw.edu.pl/texts/33/` (**HTTP 200**).

> **Phải nói cả hai mặt trong mục:** phần tự sự (chuyến đi Baghdad, hiệp ước) đến từ **al-Maqrīzī, al-Balawī, Ibn Taghrībirdī** — sử gia Ai Cập **muộn hàng thế kỷ** và **mâu thuẫn nhau ở vài điểm**. Cái neo chắc là bi ký 887, chứ không phải tự sự.
> **Dọn rác Wikidata (§3.4):** chỉ dùng `P569 +0815/p9` và `P570 +0887/p9` (cùng có `stated-in Q46002746`). **Bỏ** `P569 +0900/p7` (imported-from-wikimedia) và `P570 +0920/p9` (**không tham chiếu**).
> **Quyết định vùng:** theo **tiền lệ sẵn có trong atlas** — `ch02` đã xếp hai vua Kush ở Napata (nay thuộc Sudan) vào `Châu Phi hạ Sahara`. Không phải thao tác thống kê.
> **Lĩnh vực:** tôi đề xuất `Kinh tế` làm lĩnh vực thứ hai vì nội dung cụ thể của việc ông làm là **đàm phán lại một nghĩa vụ cống nạp – thương mại**. Nếu người viết mục thấy quá mạnh tay, lựa chọn thay thế hợp lý là `Tôn giáo/Tâm linh` (vương quyền Kitô giáo Nubia). **Tôi ghi cả hai để vòng duyệt chọn, chứ không giấu lựa chọn.**

---

## CH05-CE09-09 · Al-Bukhari (محمد بن إسماعيل البخاري)

`năm: 810–870 CN | nơi: Bukhara và Khartank gần Samarkand, Transoxiana | vùng: Trung Á | lĩnh vực: Tôn giáo/Tâm linh, Sử học | độ tin cậy niên đại: Cao | wikidata: Q241026 | câu hỏi lớn: Con người`

**Luận đề cho "Tư tưởng / đóng góp chính":** Vấn đề mà al-Bukhārī đối mặt không phải thiếu tư liệu mà **thừa**: hàng trăm nghìn lời truyền được gán cho Muhammad, nhiều lời mâu thuẫn nhau, nhiều lời bịa ra để phục vụ phe phái — và ông trả lời bằng một **phương pháp phê phán nguồn**: truy từng mắt xích *isnād*, lập tiểu sử người truyền, đòi người truyền phải **thật sự gặp nhau**, rồi chỉ giữ lại một phần rất nhỏ trong *al-Jāmiʿ al-Ṣaḥīḥ*.

**Luận đề cho "Vì sao chọn":** Tiêu chí (c) — *ʿilm al-rijāl* mà ông đẩy tới mức hệ thống là **một trong những bộ máy phê phán nguồn sớm nhất và quy mô nhất của lịch sử nhân loại**, áp dụng cho chính văn bản thiêng của cộng đồng mình; và tiêu chí (b) — bộ sưu tập ấy vẫn là văn bản đứng thứ hai sau Qurʾān trong Hồi giáo Sunni sau mười hai thế kỷ.

**Kế thừa từ:** `CH05-CE07-01 · kế thừa · qua trường phái`; `Người soạn ḥadīth thế hệ trước ở Baghdad — xem CH05-CE09-07, vốn là thầy ông · kế thừa · trực tiếp`; `Yahya ibn Maʿin và Ali ibn al-Madini · kế thừa · trực tiếp`.
**Ảnh hưởng tới:** `Hệ Kutub al-Sittah, sáu bộ ḥadīth chính điển Sunni · kế thừa · trực tiếp`; `Muslim ibn al-Hajjaj và al-Tirmidhi · kế thừa · trực tiếp`; `Khoa phê phán tiểu sử người truyền (ʿilm al-rijāl) về sau · kế thừa · trực tiếp`.

**Nguồn (đã tự mở kiểm):**
1. Jonathan A. C. Brown, *The Canonization of al-Bukhārī and Muslim: The Formation and Function of the Sunnī Ḥadīth Canon* — `https://archive.org/details/TheCanonizationOfAlBukhariAndMuslimByJonathanBrown` (**HTTP 200**). Dùng cho: bộ sưu tập **trở thành chính điển qua một quá trình lịch sử**, không phải được công nhận ngay — đây chính là điểm mà mục cần nói để tránh viết theo giọng hộ giáo.
2. Wikidata `Q241026`, tham chiếu `stated in Q76499581` cho `P570` — **tôi tự mở qua `wbgetentities`**. Dùng cho: đây là ca hiếm mà `precision` tới ngày **có** cơ sở, vì niên đại Hijrī (sinh 13 Shawwāl 194; mất đêm Eid al-Fiṭr 256) nằm trong chính truyền thống tiểu sử.
3. `sunnah.com` — **[KHÔNG KIỂM ĐƯỢC — HTTP 403 với User-Agent trung tính bắt buộc]**.

> **Quyết định vùng, kèm xung đột lợi ích đã khai ở §3.5:** Trung Á đang ở **0,9%**, nên tôi **có động cơ** xếp ông vào đó. Phép thử tôi tự áp: tiền lệ **`CH05-CE08-01 · Abu Muslim al-Khurasani`** (Merv/Khurasan → `Trung Á`) đã tồn tại **trước** khi tôi đến. Bukhara và Samarkand là **trung tâm** của hộp "Transoxiana – đông Iran", không phải rìa. **Phản biện phải ghi vào mục:** mười sáu năm thu thập ḥadīth của ông trải khắp Hijaz, Iraq, Ai Cập, Syria.
> **Lĩnh vực:** `Sử học` là một đề xuất **có chủ ý và có thể bị bác**. Lập luận: *ʿilm al-rijāl* là phê phán nguồn, cùng loại thao tác với sử học. Lựa chọn thay thế hợp lý: `Luật`. Người viết mục chọn, nhưng phải chọn **có lý do viết ra**, không chọn vì `Sử học` đang ở 2,8%.

---

## CH05-CE09-10 · Johannes Scotus Eriugena (Iohannes Scottus Eriugena)

`năm: hoạt động k. 845–877 CN | nơi: triều đình Charles Hói, Tây Frank | vùng: Châu Âu | lĩnh vực: Triết học, Tôn giáo/Tâm linh | độ tin cậy niên đại: Thấp | wikidata: Q184500 | câu hỏi lớn: Thực tại, Vũ trụ`

**Luận đề cho "Tư tưởng / đóng góp chính":** *Periphyseon* chia "tự nhiên" thành bốn hạng — cái tạo mà không được tạo, cái được tạo và tạo, cái được tạo mà không tạo, cái không tạo cũng không được tạo — và dùng chính sơ đồ ấy để nói rằng Thượng đế không phải một hữu thể trong số các hữu thể, nên **không thể biết được ngay cả với chính Ngài**; đó là một hệ thống siêu hình hoàn chỉnh, không phải một tuyển tập chú giải.

**Luận đề cho "Vì sao chọn":** Tiêu chí (c) ở mức cao nhất mà châu Âu thế kỷ 9 đạt tới: SEP gọi ông là nhà triết học **nguyên bản nhất** của thời Carolingian **và của cả quãng triết học Latin từ Boethius tới Anselmus**; thêm vào đó ông đọc được tiếng Hy Lạp ở một Tây Âu gần như không ai đọc được, và **bản dịch Latin toàn bộ corpus Dionysius hoàn thành năm 862** của ông là một hành vi truyền tải có hệ quả kéo dài nhiều thế kỷ.

**Kế thừa từ:** `CH04-CE05-03 · kế thừa · qua trường phái` (SEP ghi rằng Pseudo-Dionysius là "a follower of Proclus" — tức Tân Platon vào châu Âu Latin **qua** Eriugena); `CH04-CE05-01 · kế thừa · trực tiếp`; `CH05-CE06-12 · kế thừa · qua trường phái`.
**Ảnh hưởng tới:** `Chủ nghĩa thần bí Rhineland và Nicolaus Cusanus · kế thừa · qua trường phái`; `Truyền thống Dionysius ở Tây Âu — Grosseteste, Bonaventura · kế thừa · trực tiếp`.

**Nguồn (đã tự mở kiểm):**
1. "John Scottus Eriugena", *Stanford Encyclopedia of Philosophy* — `https://plato.stanford.edu/entries/scottus-eriugena/` (**HTTP 200**). Nguyên văn dùng cho luận đề: ông là "the most outstanding philosopher (in terms of originality)" của thời Carolingian và của cả quãng từ Boethius tới Anselmus.
2. "Pseudo-Dionysius the Areopagite", *Stanford Encyclopedia of Philosophy* — `https://plato.stanford.edu/entries/pseudo-dionysius-areopagite/` (**HTTP 200**). Dùng cho **niên đại chính xác của việc dịch**: bản dịch của Hilduin khó hiểu tới mức **Charles Hói yêu cầu Eriugena dịch lại**, ông **hoàn thành năm 862** và **hiệu đính năm 875**; và cho chuỗi ảnh hưởng tới Grosseteste và Bonaventura.
3. *Internet Encyclopedia of Philosophy* mục Eriugena — **[KHÔNG KIỂM ĐƯỢC — HTTP 404; URL `iep.utm.edu/eriugena/` không còn tồn tại]**. Đã thay bằng SEP.

> **Niên đại `Thấp`, lý do cụ thể:** `P569` khai ở `p8` = **độ chính xác thập kỷ**; `P570` 877 mang `imported-from-wikimedia`. **Không có năm sinh hay năm mất nào được chứng thực.** Nhưng hai mốc **hoạt động** thì chắc và nên dùng làm xương sống của mục: **862** (dịch xong Dionysius) và **875** (hiệu đính). Vì vậy viết `hoạt động k. 845–877 CN`, không viết `k. 800 – k. 877`.

---

## CH05-CE09-11 · Anandavardhana (आनन्दवर्धन)

`năm: hoạt động k. 855–890 CN | nơi: Kashmir | vùng: Nam Á | lĩnh vực: Văn học, Triết học | độ tin cậy niên đại: Thấp | wikidata: Q2551244 | câu hỏi lớn: Con người`

**Luận đề cho "Tư tưởng / đóng góp chính":** *Dhvanyāloka* đặt một câu hỏi mà thi học Sanskrit trước đó không hỏi — **cái gì làm một bài thơ thành thơ?** — và trả lời bằng *dhvani*: không phải nghĩa đen, không phải phép tu từ, mà **cái được gợi** (*vyañjanā*) mới là **linh hồn** (*ātman*) của thơ; từ đó ông xếp thơ thành ba hạng theo mức độ gợi, và biến phê bình văn học từ một bảng liệt kê thủ pháp thành **một lý thuyết về nghĩa**.

**Luận đề cho "Vì sao chọn":** Tiêu chí (d) ở dạng kiểm chứng được: **Abhinavagupta (k. 950–1016) viết nguyên một bộ bình chú — *Locana* — lên chính tác phẩm này**, và sau đó dhvani thành khung thẩm mỹ chủ đạo của toàn bộ thi học Sanskrit, tức một tác phẩm thế kỷ 9 đã **định nghĩa lại bộ môn** cho nghìn năm sau.

**Kế thừa từ:** `Bharata, Nāṭyaśāstra và lý thuyết rasa · kế thừa · qua trường phái`; `Bhāmaha và Daṇḍin, truyền thống alaṃkāra · phản bác · trực tiếp` (ông hạ phép tu từ xuống hàng phụ thuộc); `CH02-BCE05-08 · kế thừa · suy đoán học giả` (đường nối tới lý thuyết nghĩa của truyền thống ngữ pháp là **tái dựng của học giả**, không phải lời tự khai).
**Ảnh hưởng tới:** `Abhinavagupta và bình chú Locana · kế thừa · trực tiếp`; `Toàn bộ thi học Sanskrit sau thế kỷ 10 · kế thừa · qua trường phái`.

**Nguồn (đã tự mở kiểm):**
1. Ānandavardhana & Abhinavagupta, *The Dhvanyāloka of Ānandavardhana with the Locana of Abhinavagupta*, D. H. H. Ingalls, J. M. Masson, M. V. Patwardhan dịch, Harvard Oriental Series — `https://archive.org/details/dhvanyalokaofana0000anan` (**HTTP 200**). Bản dịch Anh ngữ đầy đủ kèm bình chú.
2. Bản HOS tập 49 trên Internet Archive — `https://archive.org/details/in.ernet.dli.2015.502083` (**HTTP 200**).

> **Niên đại `Thấp`, lý do:** Wikidata ghi 820–890 nhưng chỉ dựa vào **một nguồn cấp ba duy nhất** (`Q6023365`), và `P569` còn mang `imported-from-wikimedia`. Mỏ neo chắc duy nhất là ông soạn sách dưới triều **Avantivarman xứ Kashmir (trị vì 855–883)** và được phong tước *Rājānaka*; Kalhaṇa nhắc tên ông trong *Rājataraṅgiṇī* — **nhưng *Rājataraṅgiṇī* là thế kỷ 12**. Viết `hoạt động k. 855–890 CN`.

---

## CH05-CE09-12 · Kʼakʼupakal (Kʼakʼ-u-pakal Kʼawiil)

`năm: hoạt động k. 869–890 CN | nơi: Chichén Itzá, bán đảo Yucatán | vùng: Châu Mỹ | lĩnh vực: Chính trị/Nhà nước, Nghệ thuật/Kiến trúc | độ tin cậy niên đại: Thấp | wikidata: Q26904572 | câu hỏi lớn: Không áp dụng`

**Luận đề cho "Tư tưởng / đóng góp chính":** Ở Chichén Itzá thế kỷ 9, cái thay đổi không chỉ là ai cầm quyền mà là **hình thức của quyền lực được ghi lại**: thay vì một vua duy nhất độc chiếm bi ký như ở Palenque hay Tikal, các văn bản ở đây nêu tên Kʼakʼupakal **cùng với anh em và đồng liêu**, gắn vào các lễ hiến cúng kiến trúc — và tên ông là **tên người riêng được nhắc nhiều nhất** trong toàn bộ bi ký còn lại của thành phố, còn vọng tới tận Uxmal.

**Luận đề cho "Vì sao chọn":** Ông là **người Châu Mỹ duy nhất của thế kỷ 9 mà ta có tên, có niên đại bi ký, và có phạm vi ảnh hưởng liên thành phố**; và mục này buộc atlas phải khai ra một giới hạn thật — Wari và Tiwanaku đang ở đỉnh cùng thế kỷ nhưng **không để lại chữ viết ghi tên người**.

**Kế thừa từ:** `CH05-CE07-12 · kế thừa · suy đoán học giả` (truyền thống bi ký vương quyền Maya vùng đất thấp cổ điển); `CH05-CE08-12 · tương đồng độc lập · suy đoán học giả` (hai mô hình vương quyền song song, không có tiếp xúc chứng minh được).
**Ảnh hưởng tới:** `Trật tự chính trị Chichén Itzá cho tới k. 1000 · kế thừa · suy đoán học giả`; `Truyền thống Chilam Balam đời sau về Chichén · kế thừa · suy đoán học giả`.

**Nguồn (đã tự mở kiểm):**
1. Alexander W. Voss & H. Juergen Kremer, "Kʼakʼ-u-pakal, Hun-pik-tokʼ and the Kokom: The Political Organisation of Chichén Itzá" — `http://ecoyuc.com.mx/articles.php?task=detail&aid=1` (**HTTP 200**). Dùng cho: tên ông là tên người riêng được nhắc nhiều nhất trong bi ký còn lại của Chichén Itzá, và cho mô hình tổ chức chính trị **nhiều người cùng tên trong văn bản** thay vì một vua duy nhất.
2. Bài `Chichen Itza` và bài `Kʼakʼupakal` trên Wikipedia tiếng Anh, **tôi tự tải wikitext bằng `curl` (HTTP 200)** — dùng **chỉ** cho ba dữ kiện kiểm được chéo: bi ký **Casa Colorada** quy ra **869 CN**; niên đại chữ viết sớm nhất ở Chichén là **832**, muộn nhất **998**; tên ông xuất hiện ở **Uxmal**. *Đây là nguồn cấp ba — người viết mục nên thay bằng một ấn phẩm bi ký học nếu mở được.*
3. `www.mesoweb.com/pari/publications/journal/504/Kakupakal.pdf` — **[KHÔNG KIỂM ĐƯỢC — HTTP 404]**.

> **Niên đại `Thấp`, và lý do **không** phải là nguồn kém:** bi ký Maya là nguồn **đương thời**, chính xác hơn nhiều sử ký đời sau. `Thấp` vì (i) Wikidata **không có `P569`/`P570` nào** để đối chiếu, và (ii) khung năm phụ thuộc hoàn toàn vào phép quy đổi Lịch Đếm Dài, vốn có **hai hệ số tương quan GMT cạnh tranh**. Mục phải nói rõ điều này, nếu không `Thấp` sẽ bị đọc nhầm thành "bằng chứng yếu".
> **Lĩnh vực:** `Nghệ thuật/Kiến trúc` là đề xuất **có thể bị bác** — cơ sở là các văn bản nêu tên ông đều là **lễ hiến cúng công trình** (Casa Colorada, Las Monjas). Lựa chọn thay thế: `Quân sự` (truyền thống đời sau gắn ông với chiến tranh, nhưng đó là **truyền thống đời sau**, nên tôi không chọn).

---

## §4.13 · Phân bố vùng — CE09, ch05 sau CE09, và atlas sau CE09

**(a) Trong nội bộ CE09 (12 người):**

| Vùng | Số | Ai |
|---|---|---|
| Trung Đông/Bắc Phi | 3 | al-Khwarizmi, Hunayn, Ahmad ibn Hanbal |
| Đông Á | 3 | Hàn Dũ, Kūkai, Trương Bảo Cao |
| Nam Á | 1 | Ānandavardhana |
| Châu Âu | 1 | Eriugena |
| Trung Á | 1 | al-Bukhari |
| Đông Nam Á | 1 | Jayavarman II |
| Châu Phi hạ Sahara | 1 | Georgios I |
| Châu Mỹ | 1 | Kʼakʼupakal |
| **Châu Đại Dương** | **0** | — (§3.2: không có hệ chữ viết ghi tên người; gia phả truyền miệng chỉ được ghi lại từ TK 19) |

**Điểm cần vòng duyệt nhìn thẳng:** Châu Âu **1/12** và Trung Đông **3/12** là **cắt có chủ ý**, không phải khan ứng viên. Thế kỷ 9 ở châu Âu có ít nhất tám ứng viên qua cổng (§3.8) và ở Trung Đông cũng có tám (§3.9). Tôi giữ ít để **năm vùng mỏng mỗi vùng có một người thật**, chứ không phải để làm đẹp bảng. Nếu vòng duyệt muốn đảo, hãy đảo trong **ba người Đông Á** hoặc **ba người Trung Đông**; đảo với năm người ở vùng mỏng là **xoá một vùng khỏi bản đồ thế kỷ 9**.

**(b) ch05 sau khi thêm CE09 (36 → 48 mục):**

| Vùng | Trước | +CE09 | Sau | % ch05 |
|---|---|---|---|---|
| Đông Á | 12 | +3 | 15 | 31,3% |
| Trung Đông/Bắc Phi | 8 | +3 | 11 | 22,9% |
| Châu Âu | 6 | +1 | 7 | 14,6% |
| Nam Á | 5 | +1 | 6 | 12,5% |
| Châu Mỹ | 2 | +1 | 3 | 6,3% |
| Châu Phi hạ Sahara | 1 | +1 | 2 | 4,2% |
| Đông Nam Á | 1 | +1 | 2 | 4,2% |
| Trung Á | 1 | +1 | 2 | 4,2% |
| Châu Đại Dương | 0 | 0 | 0 | 0,0% |

**(c) Atlas chính sau CE09 (221 → 233 người) — so với `reports/stats.txt` hiện tại:**

| Vùng | Hiện tại | % | Sau CE09 | % | Đổi |
|---|---|---|---|---|---|
| Trung Đông/Bắc Phi | 73 | 33,0% | 76 | 32,6% | −0,4 đ% |
| Châu Âu | 59 | 26,7% | 60 | 25,8% | −0,9 đ% |
| Đông Á | 54 | 24,4% | 57 | 24,5% | +0,1 đ% |
| Nam Á | 26 | 11,8% | 27 | 11,6% | −0,2 đ% |
| Châu Phi hạ Sahara | 4 | 1,8% | 5 | 2,1% | +0,3 đ% |
| Trung Á | 2 | 0,9% | 3 | 1,3% | +0,4 đ% |
| Châu Mỹ | 2 | 0,9% | 3 | 1,3% | +0,4 đ% |
| Đông Nam Á | 1 | 0,5% | 2 | 0,9% | +0,4 đ% |
| Châu Đại Dương | 0 | 0,0% | 0 | 0,0% | 0 |

**Phải nói thật về quy mô của hiệu ứng:** 12 người không sửa được một bảng 221 người. Ba vùng mỏng nhất mỗi vùng nhích **0,4 điểm phần trăm**. Đó là **mức tối đa** mà một vòng trung thực có thể làm — vì cách duy nhất để nhích nhanh hơn là hạ chuẩn hoặc đổi nhãn `vùng:`, và cả hai đều bị `CONTRIBUTING.md` cấm. **Kết luận đáng ghi vào `## Ghi chú biên tập`: độ nghiêng vùng của atlas không sửa được ở tầng chọn người của một thế kỷ; nó chỉ sửa được bằng nhiều thế kỷ liên tiếp đều tìm kỹ ở vùng mỏng.**

---

## §4.14 · Phân bố lĩnh vực — và ô nào lấp được, ô nào không

**(a) 24 ô lĩnh vực của CE09 (12 người × tối đa 2):**

| Lĩnh vực | Số | Ai |
|---|---|---|
| Tôn giáo/Tâm linh | 5 | Jayavarman II, Kūkai, Ibn Hanbal, al-Bukhari, Eriugena |
| Triết học | 4 | Kūkai, Hàn Dũ, Eriugena, Ānandavardhana |
| Chính trị/Nhà nước | 3 | Jayavarman II, Georgios I, Kʼakʼupakal |
| Văn học | 2 | Hàn Dũ, Ānandavardhana |
| **Kinh tế** | **2** | Trương Bảo Cao, Georgios I |
| Toán học | 1 | al-Khwarizmi |
| **Khám phá/Địa lý** | **1** | al-Khwarizmi (*Kitāb Ṣūrat al-Arḍ*, 833) |
| **Y học** | **1** | Hunayn |
| Ngôn ngữ học | 1 | Hunayn |
| Luật | 1 | Ibn Hanbal |
| Sử học | 1 | al-Bukhari (đề xuất có thể bị bác — xem mục 09) |
| Quân sự | 1 | Trương Bảo Cao |
| Nghệ thuật/Kiến trúc | 1 | Kʼakʼupakal (đề xuất có thể bị bác — xem mục 12) |
| **Kỹ thuật/Công nghệ** | **0** | **không lấp được — xem (c)** |
| Khoa học tự nhiên | 0 | — |
| Giáo dục | 0 | — |

**(b) Bốn ô mỏng mà đề bài yêu cầu cố lấp — kết quả thật:**

| Ô | Atlas hiện tại | CE09 thêm | Atlas sau CE09 | Đánh giá |
|---|---|---|---|---|
| Y học | 4 (1,1%) | +1 | 5 (1,3%) | **Lấp được**, bằng một người mà đóng góp thật sự là y học |
| Kinh tế | 6 (1,7%) | +2 | 8 (2,1%) | **Lấp được**, nhưng một trong hai (Georgios I) là đề xuất có thể bị bác |
| Khám phá/Địa lý | 7 (1,9%) | +1 | 8 (2,1%) | **Lấp được mỏng** — chỉ qua *Ṣūrat al-Arḍ*, không có nhà thám hiểm nào |
| Kỹ thuật/Công nghệ | 7 (1,9%) | **+0** | 7 (**1,8%**) | **KHÔNG lấp được — tỉ lệ còn tụt xuống** |

**Chú ý số liệu:** `Kỹ thuật/Công nghệ` **giảm tỉ lệ** (1,9% → 1,8%) dù số tuyệt đối không đổi, vì mẫu số ô lĩnh vực tăng từ 361 lên 385. Đây là một thất bại có thật, và tôi không che nó bằng cách gán nhãn `Kỹ thuật/Công nghệ` cho ai đó không xứng.

**(c) Vì sao `Kỹ thuật/Công nghệ` không lấp được, nói thẳng:** hai ứng viên đúng ô đều **bị trần 12 cắt**, không phải không tồn tại —
- **Anh em Banū Mūsā**: *Kitāb al-Ḥiyal* (Sách về các thiết bị tinh xảo, k. 850) mô tả khoảng một trăm cơ cấu tự động. **Nhưng** `Q423210` **không phải `P31 = Q5`** — nó là một **thực thể tập thể** (`Q109288756`/`Q16017119`), nên muốn đưa vào phải tách ra một trong ba anh em, và việc tách ấy không có cơ sở văn bản (§1.1).
- **Ibn Khordādbeh**: *Kitāb al-Masālik wa-l-Mamālik* (k. 870), sách địa lý hành chính kiêm cẩm nang tuyến đường — đúng ô `Khám phá/Địa lý`, bị cắt vì trần (§5).

**(d) Một hệ quả đáng chú ý về `Chính trị/Nhà nước`:** ô này chiếm **24,1%** toàn atlas nhưng chỉ **3/24 = 12,5%** trong CE09. Đó là **cố ý**: nguyên tắc tôi áp ở §3.9 — "ưu tiên người làm ra tri thức, loại người chi tiền cho tri thức" — và nó đã loại Harun al-Rashid, al-Maʾmūn, Amoghavarsha I, Balaputradeva, Rakai Pikatan, Devapala. Nếu vòng duyệt thấy thế kỷ 9 **đáng lẽ** phải nhiều nhà cai trị hơn, thì đó là một bất đồng về **tiêu chí**, không phải về dữ kiện — và nên tranh luận ở tầng `CONTRIBUTING.md`, không phải ở tầng từng mục.

---

# §5 · Danh sách bị loại — mỗi người một câu, chấm theo bốn tiêu chí

**Kiểm quy tắc 6 trước khi viết mục này.** Tôi `grep` toàn bộ `content/*.md` (261 dòng tiêu đề mục) với từng tên dưới đây. **Kết quả: không ai trong danh sách này có mục riêng ở bất kỳ chapter nào, kể cả `ch90.md`.** Một va chạm duy nhất xuất hiện và nó là **va chạm tên, không phải va chạm người**: `CH02-BCE06-04 · Mahāvīra (महावीर, Vardhamāna)` là **tổ Jain thế kỷ 6 TCN**, không phải nhà toán học thế kỷ 9 — xem bẫy nhãn ở §1.2, và đây chính là lý do phải viết **Mahāvīrācārya**. Riêng Harun al-Rashid và Alcuin: cả hai chỉ xuất hiện trong `content/ch05.md` dưới dạng **văn bản tự do** (đích quan hệ, hoặc ghi chú biên tập), **không có mục riêng** — nên nêu tên họ ở đây là **hợp quy tắc 6** (đã kiểm từng dòng).

Ký hiệu tiêu chí: **(a)** phạm vi · **(b)** độ bền · **(c)** tính nguyên bản · **(d)** counterfactual.

## §5.1 · Hai người dự bị — bị **trần 12** cắt, không phải bị chuẩn cắt

Đây là mục quan trọng nhất của §5, vì nó là chỗ duy nhất tôi loại người **không** vì họ yếu.

1. **Mahāvīrācārya (महावीराचार्य), `Q2269861`, Nam Á** — *Gaṇitasārasaṅgraha* (850) là **văn bản Ấn Độ sớm nhất dành riêng hoàn toàn cho toán học**, tách toán khỏi thiên văn–chiêm tinh, và được dịch sang tiếng Telugu; ông qua cả bốn tiêu chí, và tôi loại ông **chỉ vì ông là người thứ 13** — nếu vòng duyệt muốn 12 người khác, hãy đổi ông vào chỗ một trong ba người Đông Á hoặc ba người Trung Đông. *(Ghi cả chỗ ông sai, để không ai phải phát hiện lại: ông khẳng định một số chia cho **không** thì không đổi — một bước lùi so với `CH05-CE07-08`.)*
2. **Alfred Đại đế, Châu Âu** — ông **đủ chuẩn** và niên đại của ông là **tốt nhất cả nhóm** (848/9 – 26-10-899, có *Asser* và *Anglo-Saxon Chronicle*, `độ tin cậy niên đại: Cao`); ông bị cắt vì **trần 12 cộng với việc Châu Âu đang ở 26,7%**, và tôi ghi rõ điều đó thay vì bịa ra một lý do chất lượng.

> **Quy tắc đảo người, viết ra để vòng duyệt khỏi phải đoán:** nếu đảo, **đảo trong Đông Á hoặc Trung Đông**. Không đảo với Jayavarman II, Georgios I, al-Bukhari, Ānandavardhana, Kʼakʼupakal — vì mỗi người trong số đó là **người duy nhất của vùng mình**, và bỏ họ là xoá một vùng khỏi bản đồ thế kỷ 9.

## §5.2 · Trung Đông/Bắc Phi — loại sáu, giữ ba

3. **Harun al-Rashid `Q131002`** — hai thứ làm ông nổi tiếng đều không phải của ông (*Nghìn lẻ một đêm* dùng ông làm **nhân vật**; Bayt al-Ḥikma có lẽ **chưa bao giờ là một thiết chế** — İhsanoğlu 2023), nên ông rỗng ở **(c)**, và di sản chính trị trực tiếp nhất của ông ở **(d)** là **cuộc nội chiến 811–813** do chính sắp xếp kế vị của ông gây ra. **Lập luận đầy đủ ở §2.1.**
4. **al-Maʾmūn `Q61056`** — ông mạnh hơn cha ở (c), nhưng công trạng chính được gán cho ông là **sáng lập/bảo trợ Bayt al-Ḥikma**, tức đúng mệnh đề đang bị học thuật tháo dỡ (§2.1); và mặt (d) rõ ràng nhất của ông — **áp *Miḥna*** — là phía **thua**, nên atlas ghi phía thắng (`CH05-CE09-07`).
5. **al-Kindī `Q9203`** — "nhà triết học của người Ả Rập", ứng viên **mạnh nhất** trong số bị loại ở vùng này và là mất mát thật sự: ông rơi vì trần 12 và vì Trung Đông đã có ba người, chứ không vì tiêu chí; *(niên đại `Trung bình`: sinh 796/800/801, mất 870/873, mọi con số đều mang tiền tố "k." trong chính học thuật.)*
6. **al-Ṭabarī** — *Taʾrīkh al-rusul wa-l-mulūk* là nguồn nền của toàn bộ sử học Hồi giáo sơ kỳ nên ông rất mạnh ở **(b)**, nhưng **thời kỳ ảnh hưởng chính của ông là 900–923** (ông mất 923), tức **thuộc CE10, không thuộc CE09** — đây là loại vì **quy tắc xếp nhóm theo thời kỳ ảnh hưởng chính**, không phải vì chất lượng.
7. **Ibn Khordādbeh** — *Kitāb al-Masālik wa-l-Mamālik* (k. 870) đúng ô `Khám phá/Địa lý` đang mỏng, nhưng nó là **cẩm nang hành chính về tuyến đường và thuế**, mạnh ở (a) và yếu ở **(c)**; và trần 12 không còn chỗ.
8. **Anh em Banū Mūsā `Q423210`** — *Kitāb al-Ḥiyal* (k. 850) là ứng viên tự nhiên cho ô `Kỹ thuật/Công nghệ` **đang trống**, nhưng Q-ID **không phải `P31 = Q5`** mà là một **thực thể tập thể** (§1.1), và việc tách ra một trong ba anh em **không có cơ sở văn bản** — đây là ca mà quy tắc "một người, một thân thế" của atlas **không đỡ nổi**, và phải ghi vào ghi chú biên tập.
9. **Jābir ibn Ḥayyān `Q167852`** — không vào CE09 **cũng không vào CE10**, vì đây không phải một người có niên đại khó mà là **một sai đơn vị phân tích**: con người mất k. 806–816 **không có tác phẩm nào quy được cho ông**, còn khối ~215 chuyên luận mang tên ông là của **nhiều tác giả ẩn danh k. 850–950**; nhãn `[Tranh cãi lịch sử]` sẽ **khẳng định điều mà học thuật phủ định**. **Lập luận đầy đủ ở §2.2.**

## §5.3 · Châu Âu — loại tám, giữ một

10. **Photios I `Q243187`** — Thượng phụ Constantinopolis, *Bibliotheca* bảo tồn tóm lược hàng trăm tác phẩm cổ nay đã mất nên ông mạnh ở **(b)**; loại vì Châu Âu đang ở 26,7%, và vì niên đại ông là ca xấu nhất vùng — **năm giá trị cạnh tranh cho năm mất** (891/893/895/896/900), biên độ **9 năm** (§1.3).
11. **Constantinus–Cyrillus và Methodius** — bảng chữ Glagolitic và việc dịch phụng vụ sang tiếng Slav là một đóng góp **(c)** thật và **(b)** rất dài (toàn bộ văn tự Kirin về sau), và đây là chỗ tôi **gần đổi ý nhất**; tôi vẫn loại vì hai lý do **không** liên quan tới chất lượng: họ là **hai người cho một đóng góp** (vấn đề đơn vị, giống ca Banū Mūsā), và Châu Âu đã có Eriugena. **Khuyến nghị thật lòng: nếu CE10 không nhận họ, vòng duyệt nên cân nhắc đảo họ vào chỗ một người Đông Á của CE09.**
12. **Rabanus Maurus** — *De rerum naturis* là một bộ bách khoa lớn và ông là "praeceptor Germaniae", nhưng công việc của ông là **biên tập và truyền đạt** di sản Carolingian, tức yếu ở **(c)** so với Eriugena.
13. **Hincmar xứ Reims** — quyền lực giáo hội–chính trị rất lớn ở Tây Frank, nhưng đóng góp của ông là **vận dụng** giáo luật trong các vụ tranh chấp cụ thể, không phải một hệ thống mới: yếu ở **(c)**.
14. **Gottschalk xứ Orbais** — luận đề **tiền định kép** của ông thật sự là một mệnh đề nguyên bản và gây ra cuộc tranh luận thần học lớn nhất thời Carolingian, nhưng ông bị kết án và bị giam tới chết, nên **(d)** của ông là một **phản chứng**: tư tưởng ấy phải đợi tới Cải cách mới có hậu duệ.
15. **ʿAbd al-Raḥmān II của Córdoba** — người bảo trợ, cùng dạng đã bị loại suốt từ CE08 trở đi.
16. **Ziryāb** — nhân vật hấp dẫn nhất bị loại ở đây (âm nhạc, ẩm thực, thời trang ở Córdoba), nhưng gần như **toàn bộ** những gì ta "biết" về ông đến từ **al-Maqqarī, thế kỷ 17**, tức muộn **tám thế kỷ**: hồ sơ không đỡ nổi một mục.
17. **Alcuin xứ York** — **không tái đề xuất**, và tôi **không** bác lập luận của CE08: ông bị loại vì **trùng vai với `CH05-CE08-06 · Charlemagne`** (cải cách giáo dục Carolingian đã vào atlas qua Charlemagne), và **không** phải vì niên đại — ông mất **804**, tức thời kỳ ảnh hưởng chính của ông nằm ở **CE08**, nên dù có nhận ông thì cũng **không phải nhóm này nhận**. **Chi tiết ở §2.3.**

## §5.4 · Đông Á — loại nhiều nhất, vì đây là vùng chật nhất

18. **Bạch Cư Dị** — thi nhân lớn, ảnh hưởng sang Nhật Bản rất mạnh, niên đại `Cao`; loại vì **trùng vai với `CH05-CE08-09 · Đỗ Phủ`** (thơ Đường đã có mặt) và vì Đông Á đang ở 24,4%.
19. **Sugawara no Michizane `Q382005`** — học giả–quan lại, người **chấm dứt các sứ bộ sang nhà Đường năm 894**, một mốc **(d)** thật; loại vì Đông Á đã có ba người và vì mốc 894 là một **quyết định hành chính**, không phải một ý tưởng. *(Niên đại Wikidata 01-08-845 → 26-03-903 ở `p11` nhưng tham chiếu là `P143` imported from jawiki — §1.3.)*
20. **Đường Vũ Tông `Q9801`** — cuộc **phế Phật năm 845** là một sự kiện có hệ quả khổng lồ, nhưng nó là một **chính sách đàn áp của nhà nước**, không phải một đóng góp tri thức; và ý tưởng chống Phật giáo của thời ấy đã vào atlas qua **`CH05-CE09-02 · Hàn Dũ`**, người **nghĩ ra lập luận**, không phải người thi hành nó.
21. **Ennin (円仁)** — nhật ký *Nittō Guhō Junrei Kōki* của ông là **một trong những nguồn tường thuật quý nhất về Trung Hoa thế kỷ 9** và tôi đã dùng chính nó để chấm niên đại của mục 05; nhưng giá trị của ông chủ yếu là **giá trị tư liệu cho ta**, không phải ảnh hưởng tư tưởng đương thời ở mức (c) ngang nhóm — loại **sát nút**.
22. **Saichō (最澄)** — sáng lập Thiên Thai tông Nhật Bản, đối trọng đương thời của Kūkai; loại vì **trùng vai hai lớp**: với `CH05-CE06-07 · Trí Di` (nguồn giáo lý Thiên Thai đã có mặt) và với `CH05-CE09-03 · Kūkai` (cùng vai người đưa tông phái Trung Hoa vào Nhật Bản), và Kūkai mạnh hơn ở **(c)**.

## §5.5 · Nam Á, Đông Nam Á, Trung Á — loại vì Q-ID hỏng, vì niên đại, hoặc vì là người bảo trợ

23. **Balaputradeva `Q4199265`** — ông là **người bảo trợ** (ra lệnh xây tu viện ở Nālandā), và phần "quan trọng" của ông — thua trận 856 rồi chạy sang Srivijaya — là **giả thuyết de Casparis (1956)**, không phải nội dung bi ký, và đã bị học thuật xét lại (§3.3).
24. **Rakai Pikatan `Q7286535`** — lại là người bảo trợ công trình (Prambanan), và chính bài khảo cứu thừa nhận triều đại ông "**highly conjectural**" do thiếu tư liệu gốc.
25. **Devapala nhà Pāla** — `Q27793406` là **trang định hướng Wikimedia** (`P31 = Q4167410`), không phải người (§1.1); và dù giải đúng Q-ID thì ông vẫn là một vị vua bảo trợ.
26. **Vācaspati Miśra** — niên đại dao động giữa **841 và 976**, biên độ **135 năm**: **không thể xếp vào một nhóm thế kỷ**, phải để CE10 quyết.
27. **Śaṅkaranārāyaṇa `Q7488718`** — `P31 = Q56436498`, **không phải `Q5`** (§1.1): không có đường vào atlas ở dạng hiện tại.
28. **Sureśvara** — **không giải được Q-ID ổn định**, và trùng vai với `CH05-CE08-11 · Ādi Shankara`.
29. **Amoghavarsha I** — người bảo trợ (chính là người mà niên đại của Mahāvīrācārya phải neo vào), cùng dạng đã loại ở CE08.
30. **al-Tirmidhī `Q293578`** (824–892, Termez) — hồ sơ mạnh và cũng là Trung Á, nhưng ông là **học trò của `CH05-CE09-09`** và đóng góp **cùng loại**: trùng vai.
31. **Yaʿqūb ibn al-Layth al-Ṣaffār `Q45261`** (mất 879, Sistan) — chấm dứt độc quyền chính trị của người Ả Rập ở Iran, một mốc **(d)** thật, nhưng ông là **một lãnh chúa quân sự**, yếu ở **(c)**.
32. **Ismāʿīl Samānī `Q862648`** — mất **907**: **thời kỳ ảnh hưởng chính rơi sang thế kỷ 10**, phải để **CE10**. *(Khuyến nghị cho CE10: đây là ứng viên Trung Á mạnh nhất còn lại.)*
33. **al-Farghānī và Abū Maʿshar al-Balkhī** — cả hai qua cổng về chất lượng, nhưng cả hai **hoạt động ở Baghdad**, nên theo quy ước §5.3 họ là `Trung Đông/Bắc Phi`, **không** phải Trung Á — tức họ **không** giải được bài toán vùng mỏng, và ở vùng của mình thì họ đứng sau al-Khwārizmī và Ḥunayn. **Không được dùng nisba để kéo thống kê.**

## §5.6 · Châu Phi hạ Sahara, Châu Mỹ, Châu Đại Dương — loại vì **không có tên người**, không vì không có lịch sử

34. **Kanem** — ghi chép viết sớm nhất về vương quốc này là của **al-Yaʿqūbī năm 872**, nhưng nó **không nêu tên một cá nhân nào**.
35. **Ghana (Wagadu)** — tương tự: có vương quốc trong nguồn Ả Rập, **không có tên người**.
36. **Igbo-Ukwu** — đồ đồng được định niên phóng xạ quanh thế kỷ 9 và kỹ thuật đúc sáp mất rất cao, nhưng **thợ đúc vô danh**: đúng ô `Kỹ thuật/Công nghệ` đang trống, và **vẫn không vào được**, vì atlas lập chỉ mục **con người**, không lập chỉ mục hiện vật.
37. **Bờ Swahili** — bi ký Kufic ở **Kizimkazi** niên đại **1107**: quá muộn.
38. **Aksum** — đã ngừng đúc tiền từ đầu thế kỷ 8; không còn tên vua nào chắc chắn cho thế kỷ 9.
39. **Wari và Tiwanaku** — đang ở **đỉnh** trong thế kỷ 9, và **không để lại hệ chữ viết ghi tên người**; đây là lý do "Châu Mỹ" trong atlas hiện nghĩa là **"Maya vùng đất thấp"**, và phải khai ra chứ không được che (§3.1).
40. **ʻAhoʻeitu và triều Tuʻi Tonga** — ứng viên gần nhất có thể phá thế trống của Châu Đại Dương, và **thất bại hai lần độc lập**: niên đại truyền thống là **k. 950** (tức **CE10**), và trong chính truyền thống ấy ông là **con của thần bầu trời Tangaloa**, bị giết rồi hồi sinh — một nhân vật **thần thoại** (§3.2).

---

# §6 · Ứng viên Việt Nam thế kỷ 9 (yêu cầu D5)

**Kiểm quy tắc 6 trước.** `grep -rn` toàn bộ `content/`: **Dương Thanh** và **Khúc Thừa Dụ** chỉ xuất hiện **bên trong phần "Vì sao chọn" của các mục khác ở `ch90.md`**, đúng ở vai **ứng viên bị loại** (`ch90.md:142` nêu Dương Thanh trong mục Phùng Hưng; `ch90.md:176` và `ch90.md:687` nêu Khúc Thừa Dụ trong mục Ngô Quyền). **Cao Biền không xuất hiện ở bất kỳ dòng nào trong `content/`.** Cả ba **không có mục riêng** → nêu tên họ ở đây là hợp quy tắc 6.

**Bối cảnh:** `ch90.md` nhảy từ `CH90-CE01_09-08 · Khương Công Phụ` (731–805) thẳng tới `CH90-CE10_14-01 · Ngô Quyền` (938). **Thế kỷ 9 là một khoảng trống trong chính phụ lục Việt Nam** — không phải vì ai đó bỏ sót, mà vì nhóm `CE01_09` kết thúc đúng ở đầu thế kỷ 9. Ba cái tên dưới đây là những gì lấp được khoảng ấy nếu `ch90` muốn lấp.

## §6.1 · Dương Thanh (771 – 820/828?) — **không vào CE09, và vướng một lỗi Wikidata phải ghi lại**

Năm **819**, đang là nha tướng bị điều về phủ thành Tống Bình để kiềm chế, ông được giao 3.000 quân đi đánh Hoàng Động; ông quay quân, đánh chiếm Tống Bình, **giết đô hộ sứ Lý Tượng Cổ** (tông thất nhà Đường) và chiếm Giao Châu trong khoảng **gần một năm**.

**Lỗi Wikidata, đây là phần đáng ghi nhất:** **không có thực thể nào là *con người* Dương Thanh.** Thực thể duy nhất là **`Q6771941`**, nhãn tiếng Việt **"Khởi nghĩa Dương Thanh"** — tức tên một **sự kiện** — nhưng `P31` của nó lại là **`Q5` (con người)**. Đây là một ca **nhãn và `P31` mâu thuẫn nhau**, khác cả ba ca ở §1.1 (ở đó nhãn là người mà `P31` không phải `Q5`; ở đây ngược lại). Bài viwiki tương ứng cũng mang tiêu đề sự kiện nhưng câu mở đầu lại viết về con người, và bài mang bản mẫu bảo trì **`{{chú thích trong bài}}`** — thiếu chú thích nội văn.

**Lý do không đề xuất:** niên đại mất ghi **"820/828?"** — biên độ 8 năm **kèm dấu hỏi** ngay trong nguồn; cuộc khởi nghĩa **bị dập trong vòng một năm** và không đổi cấu trúc An Nam đô hộ phủ, nên yếu ở **(b)** và **(d)**; và ở thang toàn nhân loại ông đứng sau chính `CH90-CE01_09-07 · Phùng Hưng`, người mà mục đã nêu ông làm ứng viên bị loại. **Đề xuất: nếu `ch90` mở một nhóm thế kỷ 9, ông là ứng viên số một; atlas chính thì không.**

## §6.2 · Cao Biền (高駢, 821 – 24-09-887) `Q5521624` — **không vào CE09**, và lý do thì không đơn giản

`P31 = Q5`. Ông là **Tiết độ sứ đầu tiên của Tĩnh Hải quân**, đánh lui **Nam Chiếu** khỏi An Nam (chiến dịch kết thúc 866), và năm **866** cho đắp lại **thành Đại La** ở khu vực Long Biên — tiền thân trực tiếp của Thăng Long, tức một quyết định quy hoạch có hệ quả **nghìn năm** ở **(b)**.

**Ba lý do loại, xếp theo độ mạnh:**
1. **Ông là quan đô hộ, không phải nhân vật Việt Nam** — ông sinh ở U Châu (Bắc Kinh), mất ở Dương Châu, và sự nghiệp của ông là sự nghiệp của một tướng nhà Đường; đưa ông vào `ch90` sẽ làm hỏng định nghĩa của chính phụ lục ấy.
2. **Ở atlas chính, ông đứng ở ô `Quân sự`/`Chính trị/Nhà nước` vốn đã dày**, và yếu ở **(c)**: đắp thành là thi công, không phải phát kiến.
3. **Hồ sơ nguồn có vấn đề đã bị chính Wikipedia đánh dấu:** mục "Đắp Đại La thành (năm 866)" mang bản mẫu **`{{thiếu nguồn gốc}}`**, và phần được nhớ nhất về ông trong văn hoá Việt — chuyện **trấn yểm sông Tô Lịch** — là **truyền thuyết**, không phải sử liệu.

**Bẫy niên đại, ghi cho vòng sau:** Wikidata `P570` ghi **24-09-887** ở `precision` **tới từng ngày** và **không có tham chiếu nào**; bài viwiki thì gắn ngày ấy với **công cụ chuyển hoán lịch Trung–Tây của Viện Nghiên cứu Trung ương (Đài Loan)** — đó là một **máy quy đổi lịch**, không phải một nguồn sử. Một ngày chính xác tới thế mà chỗ dựa chỉ là phép quy đổi thì phải ghi là `Trung bình`, không phải `Cao`.

## §6.3 · Khúc Thừa Dụ `Q1001807` — **thuộc CE10, không thuộc CE09**

`P31 = Q5`. Ông giành quyền tự chủ trên thực tế từ **905** — tức **ngoài khung 801–900**, nên theo `group_range('CE09')` ông **không thể** vào nhóm này dù có đủ chuẩn hay không.

**Hai chi tiết Wikidata phải sửa tay nếu CE10 dùng ông:** `P569` ghi **+0801 ở `precision` 7 = thế kỷ** — tức đây là **giá trị độn "thế kỷ 9"**, không phải năm sinh 801; và `P570` ghi **907** (không phải 905) với **0 tham chiếu**. Người viết CE10 phải viết `hoạt động 905–907 CN`, không được chép 801.

## §6.4 · Kết luận D5

**Thế kỷ 9 Việt Nam không có ứng viên nào vào được atlas chính**, và lý do phải nói cho đúng: không phải "Việt Nam thế kỷ 9 không có ai", mà là **thế kỷ 9 ở Giao Châu là thế kỷ của chính quyền đô hộ**, nên những cái tên để lại dấu vết trong văn khố hoặc là **quan nhà Đường** (Cao Biền), hoặc là **người nổi dậy bị dập nhanh** (Dương Thanh), còn người thật sự mở ra nền tự chủ thì **rơi sang thế kỷ 10** (Khúc Thừa Dụ). Đây là **cùng một hiện tượng văn khố** đã làm Châu Đại Dương trống và làm Châu Phi hạ Sahara chỉ còn Nubia: **atlas đang đo phạm vi của việc ghi chép, không đo phạm vi của lịch sử.**

**Khuyến nghị cụ thể cho P4 (không phải cho vòng này):** nếu muốn `ch90` hết trống thế kỷ 9, hãy mở nhóm `CH90-CE09_09` với **Dương Thanh** — nhưng phải sửa trước lỗi `Q6771941` (nhãn sự kiện, `P31` con người) hoặc chấp nhận để trường `wikidata:` trống kèm chú.

---

# §7 · Đề xuất nội dung cho `## Ghi chú biên tập`

Dưới đây là **mười khối** tôi đề nghị người viết mục đưa vào `## Ghi chú biên tập` của `content/ch05.md`. Mỗi khối có tiêu đề in đậm theo đúng kiểu các khối đã có.

**1. Tiền đề bị bác bỏ: Harun al-Rashid và cái gọi là "Nhà Trí tuệ"**
Ghi chú CE08 dặn vòng CE09 "nhặt lại Harun al-Rashid". Vòng này đã đánh giá lại độc lập và **từ chối**. Lý do không phải trần 12 mà là một mệnh đề học thuật: İhsanoğlu, *The Abbasid House of Wisdom: Between Myth and Reality* (Routledge, 2023) lập luận rằng Bayt al-Ḥikma **như một học viện có khoa, có ban** là sản phẩm được dựng lên trong **thế kỷ 19 – đầu 20** bởi học giả Đông phương học; Gutas (1998) từ lâu đã mô tả phong trào dịch thuật như một **hiện tượng xã hội rộng**, không phải sản phẩm của một toà nhà. Hệ quả: mệnh đề ấy **không cứu được Harun mà cũng không cứu được al-Maʾmūn**, và cách đúng để đưa phong trào dịch thuật vào atlas là **qua người dịch** — vì vậy chapter có Ḥunayn ibn Isḥāq chứ không có người chi tiền. **Cảnh báo kèm:** MacTutor vẫn viết Ḥunayn là dịch giả hàng đầu "in the House of Wisdom"; dùng MacTutor cho niên đại, **đừng** dùng cho mệnh đề thiết chế.

**2. Sai đơn vị phân tích: khối văn bản Jābirian**
CE08 để ngỏ khả năng nhận Jābir ibn Ḥayyān ở CE09 hoặc CE10 kèm nhãn `[Tranh cãi lịch sử]`. Vòng này **đóng khả năng đó**. Đây không phải một người có niên đại khó mà là **hai vật thể tách rời**: con người mất **k. 806–816** và **không có tác phẩm nào quy được cho ông**; khối ~**215 chuyên luận** mang tên ông được định niên **k. 850–950** (Kraus 1942–43, I, tr. lxv) và là của **nhiều tác giả ẩn danh**. Nhãn `[Tranh cãi lịch sử]` đánh dấu **một con người có tồn tại gây tranh cãi** — dùng nó ở đây sẽ **khẳng định điều học thuật phủ định**, tức vi phạm quy tắc 7.

**3. Đính chính một trích dẫn của ghi chú CE08 (PNAS)**
Bài Wilmshurst–Hunt–Lipo–Anderson về định cư Đông Polynesia là **PNAS 108(5): 1815–1820, bản in tháng 2 năm 2011**; **27-12-2010** chỉ là ngày đăng trực tuyến trước. Ghi chú CE08 ghi "(2010)". **Nên sửa thành 2011** (hoặc "2011, trực tuyến 27-12-2010"). Kiểm qua Crossref API, DOI `10.1073/pnas.1015876108`.

**4. Đính chính lập luận về Châu Đại Dương — vùng này trống, nhưng không vì lý do CE08 nêu**
Nói "Châu Đại Dương chưa có người ở" là **sai**: thế kỷ 9 Úc đã có người hàng chục nghìn năm, Melanesia và Micronesia đã có người, và **Tây Polynesia (Tonga, Samoa, Fiji) đã được định cư từ thời Lapita**, khoảng 2.800 năm trước đó. Bài *PNAS* chỉ chứng minh **Đông** Polynesia được định cư muộn. **Lý do thật** khiến vùng này trống là: toàn Châu Đại Dương tiền tiếp xúc **không có hệ chữ viết ghi được tên người**, và **gia phả truyền miệng chỉ được ghi lại từ thế kỷ 19**. Ca phản bác gần nhất — **ʻAhoʻeitu** của triều Tuʻi Tonga — **thất bại hai lần độc lập**: niên đại truyền thống **k. 950** (thuộc CE10) và ông là **con của thần bầu trời Tangaloa**, một nhân vật thần thoại.

**5. Wikidata khai cả thứ hạng, và thứ hạng ấy có thể sai — ca Trương Bảo Cao**
Ghi chú CE08 viết "Wikidata khai độ chính xác, nó không khai độ tin cậy". Nhóm này tìm được ví dụ đi xa hơn: với **`Q493856`**, Wikidata để năm mất **841 ở hạng `deprecated`** và **846 ở hạng `preferred`** — tức nó đã **chọn phe**, và chọn **phe yếu hơn**. Phía 841 có ba chỗ dựa gần đương thời (*Shoku Nihon Kōki* 869; nhật ký Ennin về tháng 7 năm 845; *Tân Đường thư* về việc sứ bộ chấm dứt) và là lập trường của **Uỷ ban Biên soạn Quốc sử Hàn Quốc**; phía 846 chỉ có *Tam quốc sử ký* (TK 12). Và chính **한국 고대 사료 DB** của Uỷ ban ấy chú rằng 張保皐列傳 **"không tham khảo một ghi chép trong nước nào"**, mà chủ yếu chép lại 張保皐鄭年傳 trong 樊川文集 của **Đỗ Mục** — nên con số 846 **không phải chứng cứ độc lập**. **Phải ghi 841.**

**6. "Châu Mỹ" trong atlas này hiện nghĩa là "Maya vùng đất thấp"**
Với `CH05-CE09-12`, cả **ba** mục Châu Mỹ của atlas đều là Maya: Palenque (`CH05-CE07-12`), Tikal (`CH05-CE08-12`), Chichén Itzá. **Wari và Tiwanaku đang ở đỉnh trong chính thế kỷ 9** và không vào được vì **không để lại chữ viết ghi tên người**. Đây là giới hạn của tư liệu và phải khai ra, không được để bảng thống kê ngụ ý rằng atlas đã rà hết châu Mỹ.

**7. Ô `Kỹ thuật/Công nghệ` không lấp được, và tỉ lệ còn tụt**
CE09 thêm **0** mục cho ô này; vì mẫu số ô lĩnh vực tăng từ 361 lên 385, tỉ lệ **giảm 1,9% → 1,8%**. Hai ứng viên đúng ô đều **mất vì trần hoặc vì Q-ID**: **Ibn Khordādbeh** (*Kitāb al-Masālik wa-l-Mamālik*, k. 870) bị trần 12 cắt; **anh em Banū Mūsā** (*Kitāb al-Ḥiyal*, k. 850) vướng `Q423210` **không phải `P31 = Q5`** mà là **thực thể tập thể** (`Q109288756`/`Q16017119`). Ca Banū Mūsā nối thẳng vào ngõ cụt "Lý Xuân" mà vòng CE06 đã ghi: **atlas lập chỉ mục con người, nên các thành tựu kỹ thuật do tập thể hoặc do thợ vô danh làm ra sẽ luôn rơi ra ngoài.** Đó là một **giới hạn thiết kế**, không phải một lỗ hổng khảo sát, và nên được thừa nhận ở tầng `CONTRIBUTING.md`.

**8. Bốn bẫy nhãn Wikidata của thế kỷ 9, kèm dạng viết tên bắt buộc**
- `Q2269861` nhãn `en` là **"Mahāvīra"**, **va chạm** với `CH02-BCE06-04 · Mahāvīra` (tổ Jain, TK 6 TCN) — hai người cách nhau **mười bốn thế kỷ**. Phải viết **Mahāvīrācārya**.
- `Q194442` nhãn `vi` là **"Hanbal"** trần, mà Ḥanbal là tên **ông cố**. Phải viết **Ahmad ibn Hanbal**.
- `Q61056` có cả "Al-Mamun" và "Al-Ma'mun" song song; chapter phải giữ **đúng một** dạng (CE08 đã dùng **al-Maʾmun**).
- `Q6771941` nhãn là **"Khởi nghĩa Dương Thanh"** (một **sự kiện**) nhưng `P31` lại là **`Q5` (con người)** — ca ngược với ba ca ở §1.1.

**9. Một mâu thuẫn nội bộ trong chính `## Ghi chú biên tập` hiện tại — cần sửa**
Khối của vòng CE07 (`content/ch05.md`, **dòng 695**) viết: *"sau Chapter 5, **Đông Nam Á vẫn đứng ở 0,0%** trong atlas chính"*. Mệnh đề này **mâu thuẫn với ba chỗ khác trong cùng file**: dòng **648** gọi `CH05-CE06-11 · Bhavavarman I` là "**mục Đông Nam Á đầu tiên của atlas chính**"; dòng **678** ghi rằng vòng bình duyệt đã bắt được đúng tiền đề lạc hậu này ("Đông Nam Á **không còn ở 0,0%**"); và dòng **742** ghi "**Đông Nam Á ở lại 0,5%**". `reports/stats.txt` xác nhận **1 người / 0,5%**. **Đề nghị: sửa dòng 695 thành "Đông Nam Á vẫn ở mức một người (0,5%)".** Tôi **không** sửa, vì phạm vi của vòng này chỉ gồm `reports/ch05-ce09-gate.md`.

**10. Độ nghiêng lĩnh vực của CE09: hình dạng của thế kỷ hay thiên kiến của người chọn?**
Câu trả lời trung thực là **cả hai, và tách được**.
*Phần thuộc về thế kỷ:* `Tôn giáo/Tâm linh` chiếm **5/24** ô của CE09 — và thế kỷ 9 **đúng là** thế kỷ mà bốn truyền thống lớn cùng lúc đóng khung chính điển của mình: ḥadīth Sunni (al-Bukhārī), luật Sunni qua *Miḥna* (Ibn Ḥanbal), Mật giáo Nhật Bản (Kūkai), và siêu hình Latin–Hy Lạp (Eriugena). Đó là hình dạng của thế kỷ, không phải lựa chọn của tôi.
*Phần thuộc về người chọn, và tôi khai ra:* (i) `Chính trị/Nhà nước` chỉ **3/24 = 12,5%** trong khi atlas ở **24,1%** — vì tôi áp nguyên tắc "**loại người bảo trợ, giữ người làm ra tri thức**", và nguyên tắc ấy một mình đã loại Harun, al-Maʾmūn, Amoghavarsha I, Balaputradeva, Rakai Pikatan, Devapala, ʿAbd al-Raḥmān II. (ii) `Khoa học tự nhiên` và `Giáo dục` **bằng 0** — và ở đây tôi **không** biện hộ: thế kỷ 9 có al-Kindī và al-Farghānī, tôi loại họ vì trần 12 và vì cân vùng, nên **hai ô trống này là lựa chọn của tôi, không phải hình dạng của thế kỷ**. (iii) Hai đề xuất lĩnh vực của tôi **tự nhận là có thể bị bác**: `Sử học` cho al-Bukhārī và `Nghệ thuật/Kiến trúc` cho Kʼakʼupakal.
*Phần không ai chọn được:* `Kỹ thuật/Công nghệ` = 0 vì **đơn vị phân tích của atlas là con người** (khối 7).
