# Mục mới đề xuất · CH02-BCE08-07 · Hezekiah xứ Judah

Soạn theo `prompts/atlas-prompt.md`, trả lời phát hiện **N12** của `reports/review-ch02.md` (Hezekiah "được chứng thực tốt hơn Josiah — người chapter có nêu là đã loại — và tốt hơn phần lớn các ngôn sứ được chọn").
**Không chỉnh sửa `content/ch02.md`.** Tài liệu này chỉ đề xuất.

> TRẠNG THÁI: HOÀN TẤT — đã lint thử trên bản sao (§6): 0 lỗi, 2 cảnh báo đều đã lường trước. Phiên trước bị ngắt vì rate limit sau khi đối chiếu Wikidata (và đã ghi nhầm Q179745 — đó là "axial tilt"); phiên này làm lại toàn bộ, không dùng sub-agent. Những gì chưa kiểm được ghi thẳng ở §5.

---

## 0 · Các điểm đã chốt

- Wikidata đúng: **Q244912** — nhãn "Hezekiah", mô tả "King of Judah". `P569 = -0741` (độ chính xác năm, qualifier "circa"), `P570 = -0686` (năm, "circa"). `P39` King of Judah với `P580 = -0716`, `P582 = -0687`. `P22` (cha) = Q30914 Ahaz. `P31 = Q20643955` (nhân vật Kinh Thánh, **không phải Q5**) → lint sẽ cảnh báo "không phải người", đúng như đã xảy ra với Isaiah và Jeremiah; cần thêm ông vào câu ghi chú sẵn có (xem §4.5).
- Trường `năm:` ghi **`k. 741–687 TCN`**, không ghi "trị vì 715–687": `parse_years()` đọc số đầu làm năm sinh, nên "trị vì 715" sẽ lệch 26 năm so với P569 và vướng lint ở mọi mức tin cậy trừ Thấp. Năm sinh 741 suy từ 2 Các Vua 18:2 (lên ngôi lúc 25 tuổi) và trùng P569; năm mất 687 = P582, lệch 1 năm so với P570 (686). Đã chạy thử: `parse_years('k. 741–687 TCN') → born -741, died -687`.
- `độ tin cậy niên đại: Trung bình`, không phải Cao: 2 Các Vua cho hai mốc đồng bộ không khớp nhau (Samaria thất thủ năm thứ 6 → lên ngôi k. 727; Sennacherib đến năm thứ 14 → lên ngôi k. 715), nên giới nghiên cứu chia thành 715–686 (Thiele), 715–687 (Albright) và 727–698; chênh lệch ~12 năm vượt dung sai ±5 của mức Cao, nằm trong ±25 của Trung bình.
- Nhóm **BCE08** đúng: bốn sự kiện mang hồ sơ của ông — dẹp nơi cao, hệ bình lmlk, đường hầm Siloam, chiến dịch 701 — đều trước 700 TCN.
- Lĩnh vực: **Chính trị/Nhà nước, Tôn giáo/Tâm linh**. Vùng: Trung Đông/Bắc Phi. Nhóm BCE08 sau khi thêm có 8 người, 6 lĩnh vực, 4 vùng.
- **Liên kết tới Sennacherib (CH02-BCE07-08):** mục đó đang được soạn song song. Nếu nó KHÔNG được chấp nhận, dòng `- CH02-BCE07-08 · phản bác · trực tiếp` trong "Ảnh hưởng tới" phải đổi thành `- Sennacherib (vua Assyria) · phản bác · trực tiếp`, nếu không lint sẽ báo "liên kết tới ID chưa tồn tại".

---

## 1 · Mục hoàn chỉnh, sẵn sàng dán vào `content/ch02.md` (nhóm BCE08, chèn giữa CH02-BCE08-06 và CH02-BCE08-08)

```markdown
### CH02-BCE08-07 · Hezekiah (חִזְקִיָּהוּ Ḥizqiyyāhū, Ê-xê-chia)
`năm: k. 741–687 TCN | nơi: Jerusalem, vương quốc Judah | vùng: Trung Đông/Bắc Phi | lĩnh vực: Chính trị/Nhà nước, Tôn giáo/Tâm linh | độ tin cậy niên đại: Trung bình | wikidata: Q244912 | câu hỏi lớn: Không áp dụng`

**Tư tưởng / đóng góp chính (~100 chữ):** Theo 2 Các Vua 18:4, ông dẹp các nơi cao (bāmôt) và rắn đồng Nehushtan, dồn phụng tự về Jerusalem. Khảo cổ chia rẽ: điện thờ Arad và bàn thờ Beersheba bị dỡ trước 701 TCN (Herzog), song Na'aman và Edelman quy cho chiến tranh. Hơn 2.000 quai bình dấu lmlk ("của nhà vua"), đường hầm Siloam 533 m (2 Các Vua 20:20) và bulla tên ông khai quật ở Ophel cho thấy quyền lực Isaiah không có: đóng điện thờ, thu thuế, quyết định chiến tranh. Năm 701 TCN, lăng trụ Sennacherib kể 46 thành bị chiếm, 2 Các Vua kể quân Assyria bị diệt; cả hai thừa nhận Jerusalem không thất thủ. Đệ Nhị Luật và Josiah sẽ hệ thống hoá mô hình một đền thờ này.

**Vì sao chọn (~80 chữ):** Cùng thời có Ahaz, cha ông, vua Judah k. 732–716 TCN, và Marduk-apla-iddina II (Merodach-baladan), vua Babylon 722–710 và 703 TCN chống Assyria. Ahaz bị loại theo counterfactual (d): ông thần phục Tiglath-Pileser III, không để lại thiết chế nào. Marduk-apla-iddina bị loại theo độ bền (b): bị Sennacherib đánh bật năm 702 TCN, Babylon chỉ độc lập lại từ 626 TCN. Hezekiah thắng ở tính nguyên bản (c) — bước tập trung phụng tự đầu tiên có dấu vết khảo cổ — và ở chất lượng chứng thực: bulla, bi ký Siloam, lăng trụ Assyria. Isaiah bổ sung, không cạnh tranh.

**Kế thừa từ:**
- Ahaz (vua Judah, cha ông) · phản bác · trực tiếp
- CH02-BCE08-04 · kế thừa · qua trường phái
- CH02-BCE08-05 · phản bác · suy đoán học giả

**Ảnh hưởng tới:**
- CH02-BCE07-08 · phản bác · trực tiếp
- Josiah (vua Judah) · kế thừa · qua trường phái
- CH02-BCE07-06 · phản bác · qua trường phái

**Nguồn:** Lester L. Grabbe (chủ biên), *'Like a Bird in a Cage': The Invasion of Sennacherib in 701 BCE* (JSOT Supplement Series 363, Sheffield Academic Press, 2003); Israel Finkelstein và Neil Asher Silberman, "Temple and Dynasty: Hezekiah, the Remaking of Judah and the Rise of the Pan-Israelite Ideology", *Journal for the Study of the Old Testament* 30/3 (2006), 259–285.
```

### Giải thích các lựa chọn trong mục

- **Vua và ngôn sứ.** Mục Isaiah (CH02-BCE08-04) đã kể Jerusalem dưới áp lực Assyria từ phía ngôn sứ. Mục này không kể lại câu chuyện đó mà chỉ ra khác biệt về *phương tiện*: ngôn sứ chỉ có lời; vua có quyền đóng điện thờ ngoài Jerusalem, vận hành hệ bình lmlk (thuế/tiếp tế), tổ chức công trình nước, và quyết định nổi dậy. Đó là lý do "tập trung phụng tự" là một bước *thiết chế* chứ không phải một ý tưởng — và tại sao nó cần một vua.
- **Không khẳng định cải cách là sự thật đã xác lập.** Câu "Khảo cổ chia rẽ" nêu đích danh hai phía (Herzog / Na'aman–Edelman). Chi tiết tranh luận ở §2 dòng 5–7.
- **701 TCN:** hai nguồn được đặt cạnh nhau, không phân xử. Điểm chung duy nhất được nêu là điều cả hai nguồn cùng hàm ý: Jerusalem không bị chiếm, Hezekiah vẫn tại vị.
- **Đường hầm Siloam** được gán cho ông *theo 2 Các Vua 20:20* — ghi rõ trong ngoặc, vì bi ký Siloam không nêu tên vua nào và niên đại đang bị tranh luận theo cả hai chiều (§2 dòng 9).
- **"Đệ Nhị Luật và Josiah sẽ hệ thống hoá"**: chỉ nói mô hình này được hệ thống hoá *về sau*; không nói Hezekiah "sáng lập độc thần giáo". Quan điểm ngược (cải cách Hezekiah là hình chiếu ngược từ Josiah — Na'aman, Edelman, Kleiman) được trình bày ở §2.
- **câu hỏi lớn: Không áp dụng** — theo tiền lệ các vua Tiglath-Pileser III và Piye; nội dung thần học của tập trung phụng tự thuộc truyền thống Đệ Nhị Luật, không phải tư tưởng cá nhân ông.
- **Loại quan hệ:**
  - *Ahaz · phản bác · trực tiếp* — cha–con, chính bulla ghi "Hezekiah [con] Ahaz"; 2 Các Vua 16 kể Ahaz thần phục Assyria và dựng bàn thờ kiểu Damascus, 2 Các Vua 18 kể con làm ngược lại.
  - *CH02-BCE08-04 (Isaiah) · kế thừa · qua trường phái* — Isaiah 36–39 ∥ 2 Các Vua 18–20: ngôn sứ cố vấn vua giữ thành năm 701. Bằng chứng là văn bản cùng một truyền thống biên tập, nên không ghi "trực tiếp".
  - *CH02-BCE08-05 (Tiglath-Pileser III) · phản bác · suy đoán học giả* — Judah thành chư hầu Assyria dưới Ahaz (bi ký Tiglath-Pileser ghi cống nạp của "Ia-ú-ḫa-zi xứ Judah"); cuộc nổi dậy của Hezekiah là phản ứng với trật tự tỉnh–chư hầu đó. Quan hệ bối cảnh, nên mức "suy đoán học giả".
  - *CH02-BCE07-08 (Sennacherib) · phản bác · trực tiếp* — cuộc nổi dậy của Hezekiah là nguyên nhân chiến dịch thứ ba của Sennacherib; được chính bi ký Sennacherib nêu tên ông.
  - *Josiah · kế thừa · qua trường phái* — 2 Các Vua 22–23 mô tả cải cách Josiah như bước tiếp của 18:4; cả hai vua đều được Sử Đệ Nhị Luật khen "không vua nào như ông" (18:5; 23:25).
  - *CH02-BCE07-06 (Jeremiah) · phản bác · qua trường phái* — Jeremiah 7:4 bác bỏ niềm tin đền thờ bất khả xâm phạm mà kết cục 701 nuôi dưỡng; Jeremiah 26:18–19 nêu đích danh Hezekiah làm tiền lệ. "Phản bác" ở đây là với *hệ quả thần học* của 701, không phải với cá nhân ông.

---

## 2 · Bảng kiểm chứng

| # | Khẳng định trong mục | Nguồn | Đã làm gì để xác nhận |
|---|---|---|---|
| 1 | Q244912 là Hezekiah vua Judah; P569 k. 741 TCN; P570 k. 686 TCN; trị vì 716–687; cha = Ahaz (Q30914); P31 ≠ Q5 | Wikidata API `wbgetentities` | Fetch trực tiếp; đọc raw time string và precision (9 = năm). Q179745 của phiên trước là "axial tilt" — sai. |
| 2 | `năm: k. 741–687 TCN` | 2 Các Vua 18:2 (25 tuổi lên ngôi, trị vì 29 năm) + P582 | Fetch BibleGateway NRSVue; chạy `common.parse_years` xác nhận born −741 / died −687; lệch so với Wikidata 0 và 1 năm. |
| 3 | Độ tin cậy Trung bình: hai mốc đồng bộ mâu thuẫn (18:9–10 vs 18:13); Thiele 715–686, Albright 715–687, phương án 727–698 | 2 Các Vua 18:9–10, 18:13 (fetch); Wikipedia "Hezekiah" mục Chronology (fetch) | Thông cáo của chính Mazar 2015 dùng 727–698, cho thấy phương án dài vẫn được dùng. |
| 4 | 18:4: dẹp nơi cao, phá trụ đá, chặt cột thờ, đập rắn đồng Nehushtan | 2 Các Vua 18:4 NRSVue | Fetch, đọc từng câu. Mục chỉ nêu nơi cao và Nehushtan vì giới hạn số chữ. |
| 5 | Arad: điện thờ bị dỡ và chôn **trước** 701 (Herzog: cuối Stratum IX; Stratum VIII bị Sennacherib đánh không còn điện thờ). Aharoni: hai giai đoạn (bàn thờ dưới Hezekiah, điện thờ dưới Josiah). Ussishkin 1988: điện thờ xây sau Stratum VIII, mất cuối Stratum VI, không liên quan cải cách nào. Na'aman 1995/1999/2002: điện thờ sống tới 701. Edelman 2008: bị chính quyền mới của Stratum VII đóng | Finkelstein & Silberman, *JSOT* 30/3 (2006) 270–271 (PDF tải về, trích text); Moulis, "Hezekiah's Cultic Reforms according to the Archaeological Evidence" (2019) §7.3 (PDF tải về) | Đọc trực tiếp hai bản PDF. Lưu ý Herzog thừa nhận "methodological problems" của khai quật Arad; F&S gọi phục dựng của Herzog là "most convincing" chứ không phải chắc chắn. |
| 6 | Beersheba: đá bàn thờ có sừng được tái dùng trong tường nhà kho và glacis Stratum II; Aharoni/Herzog: dỡ dưới Hezekiah; Na'aman 1995: 185–87 đề nghị "để bàn thờ Beersheba ngoài cuộc thảo luận"; niên đại kết thúc Stratum II (701) cũng bị nghi | F&S 2006, 271–272; Moulis 2019 §7.4 | Đọc trực tiếp. |
| 7 | Lachish: điện thờ ở cổng Level III, hai bàn thờ bốn sừng bị cắt sừng, "bệ xí" đá không có dấu phân; người khai quật gắn với 18:4; Kleiman và Moulis nghi ngờ (đồ thờ còn trong phòng chưa niêm cùng mũi tên; biến cố ở Lachish sớm hơn cuối TK 8) | Ganor & Kreimerman, *BASOR* 381 (2019) 211–236 (xác nhận tồn tại qua tìm kiếm); Archaeology Magazine 29/9/2016 (fetch); Kleiman, TheTorah.com (fetch); Moulis 2019 §7.5 | **Không đưa vào văn bản mục** vì hết chỗ và vì đây là điểm yếu nhất trong ba di chỉ. |
| 8 | > 2.000 quai bình lmlk, ~75 di chỉ; bốn địa danh Hebron, Ziph, Socoh, mmšt; biểu tượng hai hoặc bốn cánh; không dấu nào nêu tên Hezekiah; Ussishkin: toàn bộ trước 701 (Lachish III); Lipschits–Sergi–Koch 2010/2011: bắt đầu trước 701, một số loại tiếp tục sang TK 7 | Wikipedia "LMLK seal" (fetch); tóm tắt tranh luận Ussishkin–Lipschits từ kết quả tìm kiếm (rejoinder của Ussishkin, Antiguo Oriente); Lipschits, *Age of Empires* (2021) mô tả của NXB (fetch) | Con số "693 ở Khirbet Qeiyafa" trong Wikipedia **không đáng tin** (Qeiyafa là di chỉ TK 10) — không dùng. Mục chỉ dùng "hơn 2.000". |
| 9 | Đường hầm Siloam 533 m; gán cho Hezekiah theo 2 Các Vua 20:20 (và 2 Sử ký 32:30); bi ký tìm 1880, nay ở Istanbul, **không nêu tên vua**; Frumkin, Shimron & Rosenbaum, *Nature* 425 (2003) 169–171: ¹⁴C vật liệu hữu cơ trong vữa + U–Th thạch nhũ → Iron Age II, bác giả thuyết TK 2 TCN; Sneh, Weinberger & Shalev, *BASOR* 359 (2010) 57–65: hầm men theo khe karst tự nhiên, gán cho Manasseh đầu TK 7; Shimron & Frumkin phản hồi; Reich & Shukron: gốm trong lớp lấp chặn Tunnel IV → cuối TK 9/đầu TK 8, có thể thời Jehoash; Maeir & Chadwick phản bác; Regev et al., *PNAS* 122 (2025): đập Siloam k. 800 TCN | PubMed 12968177 (abstract nguyên văn); Wikipedia "Siloam tunnel" (fetch); BAS "Regarding Recent Suggestions Redating the Siloam Tunnel" và "Hezekiah's Tunnel Reexamined" (fetch); PubMed 40854121 (abstract) | **Trạng thái bằng chứng:** niên đại Iron II vững (radiometric); quy công *cho đúng Hezekiah* dựa vào 2 Các Vua 20:20 + cổ tự học bi ký, và đang bị đẩy theo cả hai chiều (sớm hơn: Reich–Shukron; muộn hơn: Sneh et al.). Kết quả 2025 về đập cho thấy hệ thống nước Gihon là công trình nhiều thế hệ. Mục ghi "(2 Các Vua 20:20)" để người đọc thấy cơ sở quy công. |
| 10 | Lăng trụ Sennacherib (Taylor, BM, 691 TCN; Chicago/ISAC 689; Jerusalem 691): 46 thành kiên cố, 200.150 người, "như chim trong lồng", trả Padi về Ekron, cống 30 talent vàng + 800 talent bạc gửi về Nineveh; không nói chiếm Jerusalem | Wikipedia "Sennacherib's Annals" và "Taylor Prism" (fetch) | Livius (bản dịch ANET) 404/timeout — con số 800 talent bạc dựa vào Wikipedia, khớp với bản dịch Luckenbill/ANET theo hiểu biết của tôi. |
| 11 | 2 Các Vua 18:14–16: 300 talent bạc + 30 vàng, lột vàng cửa đền; 19:35–36: 185.000 quân Assyria chết, Sennacherib về Nineveh | NRSVue (fetch) | Hai nguồn khớp về vàng (30), lệch về bạc (300/800), và kết cục trái ngược. Mục không phân xử. Giả thuyết "hai chiến dịch" bị đa số Assyriologist bác (Wikipedia "Assyrian siege of Jerusalem"). |
| 12 | Bulla: khai quật 2009–2010 (Ophel, Eilat Mazar), công bố 2015; tìm khi sàng ướt đất từ bãi rác cạnh toà nhà hoàng gia, cùng 33 bulla khác; 13 × 12 mm, dày 3 mm; *lḥzqyhw ʾḥz mlk yhdh*; đĩa mặt trời hai cánh rủ, hai ankh; bulla hoàng gia Judah đầu tiên từ khai quật có kiểm soát; các bulla "Hezekiah" trên thị trường cổ vật từ giữa 1990s không có xuất xứ | Wikipedia "King Hezekiah bulla" (fetch); phys.org 2/12/2015; Mazar, "A Seal Impression of King Hezekiah from the Ophel Excavations", trong *The Ophel Excavations to the South of the Temple Mount 2009–2013: Final Reports* I (Shoham, Jerusalem 2015) — xác nhận tồn tại qua ResearchGate/Academia | **Bulla xác lập:** sự tồn tại, tên, phụ danh (khớp 2 Các Vua), tước hiệu "vua Judah", và biểu tượng vương quyền kiểu Ai Cập. **Bulla không xác lập:** bất kỳ hành động nào (cải cách, hầm, nổi dậy), niên đại trị vì, hay cách sử dụng — ngữ cảnh là lớp rác (thứ cấp), nên chỉ cho terminus, không cho tầng niêm phong. |
| 13 | Finkelstein & Silberman: dân Judah ít nhất tăng gấp đôi sau 722; Jerusalem từ k. 6 lên k. 60 ha, k. 1.000 lên > 10.000 dân (200/ha, giả định Tường Rộng trước 701); tập trung phụng tự để chặn hành hương về Bethel | F&S 2006, abstract + tr. 266 (PDF) | **Không đưa con số vào mục** vì: Na'aman, *BASOR* 347 (2007) 21–56 cho tăng trưởng là tiệm tiến từ TK 9 và người tị nạn phần lớn từ chính Judah; Regev et al., *PNAS* 121 (2024) định niên đại ¹⁴C một đoạn tường thành sang thời Uzziah. Tường Rộng vì thế **không** được gán cho Hezekiah trong mục. |
| 14 | Ahaz cùng thời: trị vì k. 732–716; thần phục Tiglath-Pileser III (2 Các Vua 16); cống nạp ghi trong bi ký Tiglath-Pileser ("Ia-ú-ḫa-zi"); bàn thờ kiểu Damascus | Wikidata Q30914 P39 (fetch); Wikipedia "Ahaz" (fetch) | Đúng là cùng thời — cha và tiền nhiệm trực tiếp. |
| 15 | Marduk-apla-iddina II cùng thời: vua Babylon 722–710 và 703; bị Sennacherib đánh bại gần Kish 702, chạy sang Elam, chết lưu vong; gửi sứ tới Hezekiah (2 Các Vua 20:12) | Wikidata Q356505 P39 (fetch); Wikipedia (fetch); 2 Các Vua 20:12 NRSVue | Cùng thời, cùng chống Assyria, cùng lĩnh vực Chính trị/Nhà nước. "Babylon chỉ độc lập lại từ 626 TCN" = Nabopolassar; không viết "một thế kỷ" vì chỉ 77 năm. |
| 16 | Nguồn 1: Grabbe (chủ biên), *'Like a Bird in a Cage'*, JSOTSup 363, Sheffield 2003, 370 tr. | Amazon/epdf listing; được Wikipedia "Sennacherib's Annals" trích dẫn | Tồn tại; toàn tập về chiến dịch 701 và Hezekiah. **Chưa xem mục lục** (xem §5). |
| 17 | Nguồn 2: Finkelstein & Silberman, *JSOT* 30/3 (2006) 259–285, DOI 10.1177/0309089206063428 | PDF toàn văn + trang CRIS Haifa (abstract nguyên văn) | Đã đọc toàn văn; bài lấy Hezekiah làm trung tâm. |
| 18 | Josiah kế thừa (2 Các Vua 22–23; 18:5 ∥ 23:25); Jeremiah 7:4 và 26:18–19 | Văn bản Kinh Thánh, kiến thức chuẩn | Không fetch riêng; đây là các quy chiếu văn bản chuẩn, không có con số. |

---

## 3 · Số chữ (đếm bằng `len(s.split())`, đúng cách `atlaslib/lint.py: words()` đếm)

- **Tư tưởng / đóng góp chính:** **129** (yêu cầu 70–130).
- **Vì sao chọn:** **102** (yêu cầu 56–104).

Đếm bằng script trên chính khối fenced ở §1 (trích đoạn giữa nhãn in đậm và dòng trống kế tiếp), nên là con số lint sẽ thấy. Biên độ còn lại rất hẹp (1 chữ ở đoạn "Tư tưởng"): nếu người biên tập cần sửa câu chữ, bỏ "Hơn" ở "Hơn 2.000" hoặc "(bāmôt)" để lấy chỗ.

---

## 4 · Đề xuất sửa liên kết đối ứng và Ghi chú biên tập

Giữ tối thiểu. Hai mục hiện có cần thêm một dòng; một mục đang soạn cần đổi tên thường thành ID; Ghi chú biên tập cần ba sửa đổi nhỏ.

### 4.1 · CH02-BCE08-04 (Isaiah) — thêm một dòng vào "Ảnh hưởng tới"

Dòng hiện tại:
```
- CH02-BCE07-06 · kế thừa · qua trường phái
- Kitô giáo sơ khai · kế thừa · qua trường phái
```
Đổi thành:
```
- CH02-BCE07-06 · kế thừa · qua trường phái
- Kitô giáo sơ khai · kế thừa · qua trường phái
- CH02-BCE08-07 · kế thừa · qua trường phái
```
Lý do: đối ứng với "Kế thừa từ" của mục mới; Isaiah 36–39 ∥ 2 Các Vua 18–20. Thành 3 mục, đúng trần.

### 4.2 · CH02-BCE07-06 (Jeremiah) — thêm một dòng vào "Kế thừa từ"

Dòng hiện tại:
```
- CH02-BCE08-03 · kế thừa · qua trường phái
- CH02-BCE08-04 · kế thừa · qua trường phái
```
Đổi thành:
```
- CH02-BCE08-03 · kế thừa · qua trường phái
- CH02-BCE08-04 · kế thừa · qua trường phái
- CH02-BCE08-07 · phản bác · qua trường phái
```
Lý do: Jeremiah 7:4 bác bỏ thần học đền thờ bất khả xâm phạm hình thành sau 701; Jeremiah 26:18–19 nêu đích danh Hezekiah. Phần văn xuôi của Jeremiah ("đền thờ không bảo đảm an toàn nếu dân bất công") đã có sẵn câu đỡ, không cần sửa.

### 4.3 · CH02-BCE08-05 (Tiglath-Pileser III) — **không** sửa

"Ảnh hưởng tới" của mục này đã có 3 dòng (Ashurbanipal, Cyrus, Darius) — đủ trần. Quan hệ chỉ ghi một chiều ở mục Hezekiah.

### 4.4 · CH02-BCE07-08 (Sennacherib, đang soạn song song)

Bản nháp đó dự định ghi "Hezekiah xứ Judah" bằng tên thường. Nếu cả hai mục cùng được chấp nhận, đổi thành `- CH02-BCE08-07 · phản bác · trực tiếp`. Nếu chỉ mục Hezekiah được nhận, giữ nguyên tên thường bên phía họ và đổi dòng Sennacherib bên mục này thành tên thường (xem §0).

### 4.5 · Ghi chú biên tập — ba sửa đổi

**(a) Dòng Josiah trong "Ứng viên mạnh đã bị loại và lý do".** Dòng hiện tại:
```
- Hosea, Micah, Ezekiel, Josiah, Ezra: lớp ngôn sứ và cải cách Israel–Judah đã được Amos, Isaiah và Jeremiah đại diện. Ezra (TK 5 TCN) đáng xem lại ở P4 vì vai trò định hình kinh điển Torah.
```
Đổi thành hai dòng:
```
- Hosea, Micah, Ezekiel, Ezra: lớp ngôn sứ Israel–Judah đã được Amos, Isaiah và Jeremiah đại diện. Ezra (TK 5 TCN) đáng xem lại ở P4 vì vai trò định hình kinh điển Torah.
- Josiah (trị vì k. 640–609 TCN): mạch tập trung phụng tự đã được Hezekiah (CH02-BCE08-07) đại diện. Josiah bị loại theo tính nguyên bản (c) — bước đầu thuộc về Hezekiah theo cả 2 Các Vua 18:4 lẫn tầng khảo cổ Arad và Beersheba (Herzog) — và theo chất lượng chứng thực: không có bi ký hay ấn tín đương thời nào nêu tên Josiah, trong khi Hezekiah có bulla khai quật tại chỗ, bi ký Siloam cùng thời và lăng trụ Sennacherib. Nếu quan điểm "cải cách Hezekiah là hình chiếu ngược từ Josiah" (Na'aman, Edelman) được chấp nhận, thứ tự ưu tiên này phải xem lại.
```

**(b) Câu về Wikidata trong "Điểm cần kiểm chứng thêm".** Dòng hiện tại:
```
- Wikidata xếp Isaiah (Q188794), Jeremiah (Q158825) là nhân vật Kinh Thánh chứ không phải người (thiếu P31 = Q5), và Mahāvīra (Q9422) cũng không gắn Q5. Lint sẽ cảnh báo; đây là đặc điểm phân loại của Wikidata, không phải phán quyết về tính lịch sử của nhân vật.
```
Đổi thành:
```
- Wikidata xếp Isaiah (Q188794), Jeremiah (Q158825) và Hezekiah (Q244912) là nhân vật Kinh Thánh chứ không phải người (thiếu P31 = Q5), và Mahāvīra (Q9422) cũng không gắn Q5. Lint sẽ cảnh báo; đây là đặc điểm phân loại của Wikidata, không phải phán quyết về tính lịch sử của nhân vật — riêng Hezekiah còn được chứng thực bằng bi ký đương thời.
```

**(c) Hai ghi sổ:** "Giới thiệu chapter" hiện ghi "Bốn nhóm thế kỷ gồm 36 nhân vật" và `build.py --list-ids` hiện đếm đúng 36; thêm Hezekiah thì thành **37** (và 38 nếu Sennacherib cũng được nhận). Sửa một lần sau khi chốt mọi mục bổ sung từ review. Dòng "Tiglath-Pileser III và Piye: không có năm sinh… ghi theo thời gian trị vì" nên thêm: "Hezekiah ghi sinh–mất vì 2 Các Vua 18:2 cho tuổi lên ngôi; niên đại trị vì (715 hay 727 – 687 hay 698) vẫn bị tranh luận."

### 4.6 · Liên kết đã cân nhắc và **không** đề xuất

- **Hezekiah → CH02-BCE08-03 (Amos).** Amos giảng ở Bethel trước ông một thế hệ; không có quan hệ nội dung kiểm chứng được. Bỏ.
- **Hezekiah → Micah.** Jeremiah 26:18–19 nói Hezekiah nghe Micah — nhưng Micah không có trong chapter và mức bằng chứng chỉ là "qua trường phái". Bỏ để giữ trần 3.
- **Hezekiah ← Shabaka / Vương triều 25.** Liên minh với Ai Cập–Kush năm 701 (Isaiah 30–31; lăng trụ nhắc quân Ai Cập ở Eltekeh) là có thật, nhưng không có mục Shabaka/Taharqa trong chapter, và mục Piye không thích hợp. Bỏ.

---

## 5 · Những điều **không** kiểm chứng được, nói thẳng

1. **Sneh, Weinberger & Shalev 2010** — JSTOR và Semantic Scholar đều chặn; tôi dựa vào tóm tắt của Maeir & Chadwick trên BAS và trích dẫn thứ cấp (BASOR 359, tr. 57–65). Luận điểm "Manasseh, karst" được nhiều nguồn độc lập nhắc giống nhau nên tôi tin, nhưng chưa đọc bản gốc.
2. **Reich & Shukron 2011** — trích dẫn *Tel Aviv* 38 (2011) 147–157 là theo trí nhớ; nội dung (gốm cuối TK 9/đầu TK 8 trong lớp lấp Tunnel IV, gợi ý Jehoash) lấy từ hai bài BAS đã fetch.
3. **Mazar 2015** — chưa đọc chính chương; chi tiết bulla từ Wikipedia và phys.org (bản tin của Đại học Hebrew). Bài "The New Hezekiah Seal: Outstanding Questions" trên Academia chưa đọc; có thể chứa phản biện về ngữ cảnh.
4. **Herzog 2010** (trong *One God – One Cult – One Nation*) bị 403; lập luận của ông được đọc qua F&S 2006 và Moulis 2019, cả hai đều trích ông dài và nhất quán.
5. **Edelman 2008** — chỉ biết qua Moulis 2019 (JSOT 32/4, 395–434); không đọc được abstract (403).
6. **Lipschits 2021** — trang NXB không nêu tên Hezekiah; vì thế **không** dùng làm Nguồn dù chắc chắn sách bàn về lmlk thời ông.
7. **Grabbe 2003** — xác nhận tồn tại (NXB, năm, số trang, series) nhưng chưa xem mục lục. Chủ đề sách là chính xác chiến dịch 701 nên khả năng "không nhắc Hezekiah" bằng không.
8. **800 talent bạc** trên lăng trụ: từ Wikipedia (Livius không truy cập được). Khớp với bản dịch ANET theo hiểu biết của tôi.
9. **Josiah không có chứng thực ngoài Kinh Thánh** — đã kiểm bằng tìm kiếm: phát hiện gần nhất được viện dẫn cho Josiah là bulla "(thuộc về) Nathan-Melech, tôi tớ của vua" (bãi đỗ xe Givati, 2019, niên đại giữa TK 7–đầu TK 6), tức tên một quan chức trong 2 Các Vua 23:11, **không phải tên vua**; không nguồn nào đưa ra bi ký đương thời nêu tên Josiah. Khẳng định ở §4.5(a) đứng được.
10. **Hình minh hoạ**: chưa xét `content/images.yaml`; nếu muốn ảnh, bulla Ophel (ảnh của Ouria Tadmor/Eilat Mazar) có bản quyền hạn chế; Lăng trụ Taylor (BM) và bi ký Siloam (Istanbul) có ảnh Wikimedia Commons.

---

## 6 · Kết quả lint thử (không đụng `content/ch02.md`)

Chèn khối §1 vào một bản sao tạm của `content/ch02.md` (trước `### CH02-BCE08-08`) rồi chạy `python build.py --lint-only <bản sao>` — chế độ này ghi báo cáo vào `reports/tests/`, không ghi đè `reports/lint-ch02.txt`.

- Offline: `Parse: 1 chapter, 37 nhân vật · 0 lỗi · 1 cảnh báo` — cảnh báo duy nhất là `liên kết tới ID chưa tồn tại: CH02-BCE07-08` (đã lường trước ở §0).
- Online (đối chiếu Wikidata): `0 lỗi`; mục mới nhận thêm đúng một cảnh báo `Wikidata Q244912 không phải người (P31=['Q20643955'])` (đã lường trước, xử lý ở §4.5(b)). **Không** có cảnh báo lệch niên đại — `k. 741–687 TCN` khớp P569/P570 trong dung sai — và **không** có cảnh báo số chữ.
- Nhóm BCE08 sau khi chèn: 8 người, không cảnh báo về số lĩnh vực hay số vùng.
