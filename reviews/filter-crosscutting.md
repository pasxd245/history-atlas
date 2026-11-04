# Lọc lỗi dữ kiện: báo cáo xuyên chapter (ro1, tructiep-freetext A/B/C, compliance, design)

- **Phạm vi:** `rv/old/ro1-nguon-ngoai-review.md` (44 ca, thực tế toàn bộ thuộc `ch05`), `tructiep-freetext-A.md` (ch01–ch02), `-B.md` (ch03–ch04), `-C.md` (ch05), `compliance-review.md`, `design-review.md`. Không chạm ch06–ch11.
- **Ngày:** 2026-11-04.
- **Phương pháp:** đọc hết sáu báo cáo, rút mọi mục NÊN/CÂN NHẮC/không gắn mức có nội dung là khẳng định dữ kiện sai hoặc câu tự mâu thuẫn, cộng các mục BẮT BUỘC. Đối chiếu từng mục với `W/content/chXX.md` hiện tại bằng grep chuỗi. Nếu bản sửa đã áp ở thân mục, tìm tiếp xem còn câu nào nói ngược lại ở Ghi chú biên tập không. Phần lớn lỗi còn sót nằm ở dạng này. Mục còn mở được xác minh lại bằng web.
- **Chế độ:** chỉ lọc và xác minh, **không sửa file content nào** (các agent khác đang sửa ch01–ch05, ch90 song song). Mọi `old_str` dưới đây đã được kiểm là xuất hiện đúng 1 lần trong `content/ch05.md` *tại thời điểm lọc*. Người áp phải kiểm lại, vì agent ch05 có thể đã đổi đoạn ấy.
- **Giới hạn:** các mục tructiep-freetext loại "hạ mức vì hình thức đích" là quy ước, không phải dữ kiện, nên chỉ kiểm đã áp hay chưa. Với ro1 Ca 6, tôi không mở lại được PDF Barney (chú thích 56 "fifteen books"), nên bản sửa E1 chỉ **bỏ con số**, không thêm khẳng định mới. Mục compliance B3 (thông báo bản quyền bundle mermaid) không kiểm được trong W: `W/assets/` chỉ có `app.js` và `style.css`, không có `mermaid.min.js`, `d3.min.js` hay `LICENSE-*.txt`, dù `render.py:139` và `:537` (trang credits) trỏ tới chúng. Nhiều khả năng bản sao làm việc đã bỏ file vendored. Cần kiểm trên repo thật trước khi phát hành.

## 1. Ứng viên lọc được

| # | Báo cáo · mục gốc | ID / chỗ | Trường | Trích ngắn | Loại | Trạng thái content |
|---|---|---|---|---|---|---|
| 1 | ro1 Ca 2 | `CH05-CE06-11` Bhavavarman | Tư tưởng | "giới nghiên cứu thấy" / "vị vua đầu tiên" | dữ kiện (nguồn dùng ngược) | đã sửa trước |
| 2 | ro1 Ca 4 | `CH05-CE07-03` Ali | Vì sao chọn | Madelung "rõ nhất trong giới hiện đại" | dữ kiện (cấp nhất không nguồn) | thân mục đã sửa; **Ghi chú biên tập (khối bốn nguồn) còn câu cũ** → E2 |
| 3 | ro1 Ca 5 | `CH05-CE07-04` Thái Tông | Vì sao chọn | "sử do chính triều ông soạn" | dữ kiện | đã sửa trước |
| 4 | ro1 Ca 6b (BẮT BUỘC) | `CH05-CE07-09` Isiđôrô | Tư tưởng | Braulio chia "hai mươi quyển" | dữ kiện | thân mục đã sửa; **Ghi chú biên tập còn "chia hai mươi quyển là do Braulio"** → E1 |
| 5 | ro1 Ca 8 (phát hiện mới, KKĐ) | `CH05-CE07-11` Tùng Tán Cán Bố | Nguồn | Annals "bắt đầu ở năm 650, tức năm ông mất" | dữ kiện (nguồn vênh) | còn → E4 |
| 6 | ro1 Ca 9 | `CH05-CE07-12` Pakal | Vì sao chọn | "cá nhân châu Mỹ… biết rõ nhất" | dữ kiện (cấp nhất) | đã sửa trước |
| 7 | ro1 Ca 11 (BẮT BUỘC) | `CH05-CE08-01` Abu Muslim | Tư tưởng | "cuối năm ấy chiếm Merv" | dữ kiện | đã sửa trước ("đầu năm 748") |
| 8 | ro1 Ca 12 | `CH05-CE08-02` Al-Mansur | Tư tưởng | "suốt năm thế kỷ" | dữ kiện | đã sửa trước |
| 9 | ro1 Ca 13 | `CH05-CE08-05` Sibawayh | Tư tưởng | "khác các sách ngữ pháp Hy Lạp và Latin" | dữ kiện | đã sửa trước |
| 10 | ro1 Ca 15 | `CH05-CE08-07` Bêđa | Tư tưởng | "bắt đầu ở một tu viện Northumbria" | dữ kiện | đã sửa trước ("lan ra từ") |
| 11 | ro1 Ca 16 | `CH05-CE08-07` Bêđa | Ảnh hưởng tới | Alcuin · `trực tiếp` | dữ kiện (không chồng đời) | đã sửa trước |
| 12 | ro1 Ca 17/33 | `CH05-CE08-09` Đỗ Phủ | Tư tưởng | "biến cố lớn nhất thế kỷ 8" không rào | mâu thuẫn nội bộ | đã sửa trước |
| 13 | ro1 Ca 19 | ch05 Ghi chú, khối Kaleb | Ghi chú | Robin "tự đặt tên chuyên khảo" | dữ kiện | đã sửa trước |
| 14 | ro1 Ca 20 | ch05 Ghi chú, khối Kaleb | Ghi chú | "khoảng ba mươi lăm năm" | mâu thuẫn nội bộ | đã sửa trước |
| 15 | ro1 Ca 21 | ch05 Ghi chú, khối Chân Lạp | Ghi chú | quy mệnh đề cho Vickery thay vì Jacques | dữ kiện (quy kết) | đã sửa trước |
| 16 | ro1 Ca 24 | ch05 Ghi chú, Boethius ý (4) | Ghi chú | "làm nó nổi tiếng" | dữ kiện (nói quá nguồn) | đã sửa trước |
| 17 | ro1 Ca 25 | ch05 Ghi chú, khối Đông Nam Á | Ghi chú | "dòng đầu của ch90.md nói rõ" | mâu thuẫn nội bộ | đã sửa trước |
| 18 | ro1 Ca 26 | ch05 Ghi chú, Võ Tắc Thiên ý (2) | Ghi chú | "k. 424–430" | dữ kiện (số chặt hơn nguồn) | đã sửa trước |
| 19 | ro1 Ca 27 | ch05 Ghi chú, khối bốn nguồn | Ghi chú | "Plofker là người phản đối" + mốc Bodleian 10/2024 (KKĐ) | dữ kiện | đã sửa trước; mốc 10/2024 nay xác minh được → giữ |
| 20 | ro1 Ca 28 | ch05 Ghi chú, Charlemagne/CE08 | Ghi chú | sứ bộ Harun "đều thuộc thế kỷ 8" | dữ kiện | đã sửa trước |
| 21 | ro1 Ca 30 | ch05 Ghi chú, khối Shankara | Ghi chú | bỏ mất cách đọc Chandragupta II | dữ kiện (thiếu vế làm câu sai trọng số) | đã sửa trước |
| 22 | ro1 Ca 35/36 | ch05 Ghi chú, người bị cắt CE09 | Ghi chú | "(850)" trần; "bước lùi" bỏ sót lỗi 0÷0 của Brahmagupta; "sớm nhất" (KKĐ) | dữ kiện | đã sửa trước; "sớm nhất" nay xác minh → giữ |
| 23 | ro1 Ca 43b | ch05 Ghi chú, al-Ashʿarī | Ghi chú | lời chẩn "quy đổi AH→CE bằng công thức" | dữ kiện | khối al-Ashʿarī đã sửa; **Nguồn của `CH05-CE10-01` al-Ṭabarī còn viện lời chẩn ấy như đúng** → E3 |
| 24 | ro1 Ca 37 | ba mục CE09 | Ghi chú | chỉ một mục tự khai "có thể bị bác" | mâu thuẫn nội bộ (mức tự tin) | đã sửa trước |
| 25 | freetext-A Ca 10 | `CH02-BCE07-08` Sennacherib | Ảnh hưởng tới | Esarhaddon (tái thiết Babylon) · `trực tiếp`, sự kiện sau khi ông chết | dữ kiện (tiếp xúc với sự kiện sau khi chết) | đã sửa trước (`qua trường phái`) |
| 26 | freetext-A Ca 11 | `CH02-BCE07-09` Taharqa | Ảnh hưởng tới | Tanwetamani (… năm 663) · `trực tiếp` | dữ kiện (như trên) | đã sửa trước |
| 27 | freetext-C Ca 37 | `CH05-CE09-08` Georgios I | Kế thừa từ | Zacharias III "phong ông làm đồng trị năm 835" | dữ kiện? | còn, xác minh → **giữ nguyên** |
| 28 | freetext-C Ca 34 (quan sát, không phán) | `CH05-CE08-12` Yikʼin | `năm:` | "trị vì 734 – k. 766" và en.wiki "c. 755" | dữ kiện? | còn, xác minh → **giữ nguyên** + KNOWN-ISSUES |
| 29 | compliance B1 | `LICENSE` | — | thiếu giấy phép dự án | BẮT BUỘC | đã áp (LICENSE tách code/văn xuôi/ảnh) |
| 30 | compliance B2 | `fetch_images.py` | — | nhánh fallback nhúng ảnh không kiểm `Restrictions` | BẮT BUỘC | đã áp (`fetch_images.py:437–441` chuyển sang chờ xem xét) |
| 31 | compliance B3 | `assets/LICENSE-mermaid.txt` | — | thiếu thông báo thư viện đóng gói kèm | BẮT BUỘC | **không kiểm được trong W** (thiếu cả thư mục vendored) |
| 32 | compliance B4 | `render.py` footer/overview | — | không nói văn xuôi do AI viết | BẮT BUỘC | đã áp (`render.py:170`, `:460`) |
| 33 | compliance B5 | `render.py` overview | — | thiếu tuyên bố giới hạn | BẮT BUỘC | đã áp (`render.py:468`, khối `#trung-lap`) |
| 34 | design #11 | `render.py` `mermaid_timeline` | — | trục thời gian không theo thời gian (Piye sau Hesiod) | dữ kiện (lỗi nội dung hiển thị) | đã sửa trước (`render.py:69–90`) |

Không lấy, vì không phải lỗi dữ kiện: ro1 Ca 3, 7 (URL/tác giả SEP ở dòng Nguồn đều đã áp), 14 (thể loại nguồn, đã áp), 22, 32 (phân loại URL, đã áp), 39, 40, 42, 44 (ghi chú quy trình/lint), và các ca KHÔNG CẦN SỬA (1, 6a, 10, 18, 23, 29, 31, 34, 38, 41, 43a). Cũng không lấy các ca "HẠ vì đích hai người/hỗn hợp" ở freetext A1, A2, A9, A12, B22, B25, C38, C39 (đều đã áp; xem `ch01.md:145–146`, `ch02.md:271/277/295/346`, `ch03.md:620/747`, `ch05.md:798/802`), và B20 Scipio, nay đã là "Scipio Africanus Lớn" (`ch03.md:416`).

## 2. Quyết định cho mục còn sai

| # | ID | File · trường | Trước (`old_str`, nguyên văn) | Sau (`new_str`) | Quyết định | Bằng chứng |
|---|---|---|---|---|---|---|
| E1 | ro1 Ca 6b, phần còn sót · `CH05-CE07-09` Isiđôrô | `content/ch05.md` · Ghi chú biên tập (khối "Hai chi tiết **không kiểm được tới nguồn gốc**…") | `và việc chia hai mươi quyển là do Braulio làm sau chứ không phải Isiđôrô` | `và việc chia thành quyển là do Braulio làm sau chứ không phải Isiđôrô, còn con số hai mươi có lẽ của khâu sao chép` | **sửa** (nhất quán nội bộ). Thân mục (đã sửa theo BẮT BUỘC của ro1) nay viết "việc chia thành quyển là do Braulio… còn con số hai mươi có lẽ của khâu sao chép"; Ghi chú vẫn khẳng định trần "chia hai mươi quyển". Bản mới chép đúng mức rào của thân mục, không thêm mệnh đề nào. Lưu ý: Brehaut 1912 và en.wiki vẫn ghi "twenty"; con số mười lăm chỉ có ở Barney 2006 (ro1 Ca 6, chú thích 56 dẫn Reydellet 1966) mà vòng này không mở lại được, nên giữ chữ "có lẽ". | Barney et al. 2006 qua ro1 Ca 6 · https://www.wordtrade.com/philosophy/medieval/isidoreseville.htm (Barney: Braulio "who divided the text into books") · https://gutenberg.org/ebooks/51511 (Brehaut: "twenty") |
| E2 | ro1 Ca 4, phần còn sót · `CH05-CE07-03` | `content/ch05.md` · Ghi chú biên tập (khối bốn nguồn) | `Madelung 1997 là chuyên khảo nghiêng về phía Alid rõ nhất trong giới hiện đại, nên` | `Madelung 1997 là chuyên khảo đọc thiên Alid, ngược chiều phần lớn học thuật phương Tây, nên` | **sửa** (bỏ cấp nhất không nguồn; khớp câu đã sửa ở `Vì sao chọn` của mục). Các bài điểm sách (Kennedy, Crone, Daniel…) đều gọi sách "partisan" và "pro-Alid reading", ngược với học thuật hiện đại vốn "pro-Sunnite", nhưng không ai xếp hạng nó là "rõ nhất". | https://en.wikipedia.org/wiki/The_Succession_to_Muhammad (mục Reception: Kennedy "pro-Alid reading… most modern scholarship has been pro-Sunnite") |
| E3 | ro1 Ca 43b, phần còn sót · `CH05-CE10-01` al-Ṭabarī | `content/ch05.md` · Nguồn | `lệch một năm theo đúng dạng sai quy đổi AH→CE mà hồ sơ cổng CE10 đã cảnh báo.` | `lệch một năm vì 922 là năm CE mà năm 310 AH bắt đầu (310 AH chạy từ giữa 922 sang đầu 923), còn ngày mất rơi vào tháng 2/923 — cùng cơ chế lịch mà khối al-Ashʿarī ở Ghi chú biên tập giải thích, không phải vết của quy đổi bằng công thức.` | **sửa** (mâu thuẫn nội bộ). Khối al-Ashʿarī (`ch05.md`, "**lời chẩn ấy sai, sửa ở đây**") bác lời chẩn "quy đổi AH→CE bằng công thức" của hồ sơ cổng, trong khi dòng Nguồn này lại viện chính lời chẩn ấy như đúng. Dữ kiện đã kiểm: al-Ṭabarī mất 17/2/923; cache `wd:Q192124` `P570` = 922 (precision 9); 1 Muharram 310 AH ≈ tháng 5/922 (tính từ 16/7/622 cộng 309 × 354,367 ngày). | https://en.wikipedia.org/wiki/Al-Tabari ("Tabari died on 17 February 923") · `data/wikidata-cache.json` (`wd:Q192124`) |
| E4 | ro1 Ca 8 (phát hiện mới, KKĐ) · `CH05-CE07-11` Tùng Tán Cán Bố | `content/ch05.md` · Nguồn | `lưu ý bản chép này bắt đầu ở năm 650, tức năm ông mất, nên` | `lưu ý bản chép này bắt đầu ở năm 650, sát năm ông mất (nguồn ghi 649 hoặc 650), nên` | **làm mềm.** Nguồn vênh: chính Dotson (tác giả bản dịch mà dòng Nguồn này dẫn) ghi "Tri Songtsen (alias Songtsen Gampo) c.605–649" và "entries from 650 to 764"; en.wiki "Tibetan Annals" ghi ông mất năm 650; en.wiki "Songtsen Gampo" suy từ Annals ra 649. Câu "tức năm ông mất" chốt một phe mà nguồn của chính mục không đỡ. Ý chính của câu (Annals không đỡ các mệnh đề về chính thời ông) giữ nguyên. **Không** đổi dòng `năm: k. 617–650` (khớp Wikidata, đã rào "k."), nên không cần thêm ghi chú lệch Wikidata. | https://www.societyforasianart.org/sites/default/files/2022-11-11%20Dotson%20Study%20Guide.pdf · https://en.wikipedia.org/wiki/Tibetan_Annals |
| G1 | freetext-C Ca 37 · `CH05-CE09-08` Georgios I | `ch05.md` · Kế thừa từ ("Zacharias III, cha ông, người phong ông làm đồng trị năm 835") | — | — | **giữ nguyên.** Reviewer dựa vào en.wiki "Zacharias III" ("named him heir and may have given him the title of caesar"; cùng trị từ 837). Nhưng en.wiki "Georgios I of Makuria" dẫn Welsby tr. 74: năm 835 ông được "appointed co-regent, possibly with the title of caesar". Hai nguồn vênh, và câu hiện tại có Welsby đỡ, nên không phải lỗi đã biết. | https://en.wikipedia.org/wiki/Georgios_I_of_Makuria · https://en.wikipedia.org/wiki/Zacharias_III_of_Makuria |
| G2 | freetext-C Ca 34 · `CH05-CE08-12` Yikʼin | `ch05.md` · `năm: trị vì 734 – k. 766` | — | — | **giữ nguyên.** Ngay trong en.wiki số liệu đã vênh: hộp thông tin ghi trị vì tới c. 755, bảng tước hiệu ghi c. 746, phần mở đầu ghi "746/766?". Mục đã ghi "k.", để `Trung bình` và tự khai "năm mất còn để ngỏ". Chuyển sang KNOWN-ISSUES. | https://en.wikipedia.org/wiki/Yikʼin_Chan_Kʼawiil |
| G3 | ro1 Ca 27 (phần KKĐ) | `ch05.md` · Ghi chú, khối bốn nguồn ("tháng 10/2024 Bodleian đã lùi niên đại… về 799–1102") | — | — | **giữ nguyên**, nay đã xác minh: Oxford công bố ngày 14/10/2024 niên đại mới 799–1102 CN. | https://en.wikipedia.org/wiki/Bakhshali_manuscript |
| G4 | ro1 Ca 36 (phần KKĐ) | `ch05.md` · Ghi chú, người bị cắt CE09 ("văn bản Ấn Độ sớm nhất dành riêng hoàn toàn cho toán học") | — | — | **giữ nguyên.** Có nguồn đỡ ("It is the earliest Indian text entirely devoted to mathematics"). Việc so với *Pāṭīgaṇita* và Bakhshālī (nay 799–1102) vẫn còn bàn được, chuyển sang KNOWN-ISSUES. | https://en.wikipedia.org/wiki/Mahāvīra_(mathematician) |

## 3. Cho KNOWN-ISSUES (mỏng / tranh luận / quy ước còn mở, không sửa)

- `CH05-CE07-11` Tùng Tán Cán Bố: năm mất 649 (Dotson) hay 650 (Wikidata, en.wiki Tibetan Annals). Dòng `năm:` giữ 650. Mở Dotson 2009 ra đọc rồi mới quyết. — `reviews/ro1-nguon-ngoai-review.md` #Ca 8
- `CH05-CE08-12` Yikʼin Chan Kʼawiil: mốc cuối triều 746, 755 hay 766 còn vênh, mục đang ghi `k. 766`. — `reviews/tructiep-freetext-C.md` #Ca 34
- `CH05-CE09-08` Georgios I: năm 835 là năm "lập làm người kế vị" (en.wiki Zacharias III) hay "đồng trị/co-regent" (Welsby qua en.wiki Georgios I). — `reviews/tructiep-freetext-C.md` #Ca 37
- ch05 Ghi chú, người bị cắt CE09: "*Gaṇitasārasaṅgraha* sớm nhất dành riêng cho toán học" chưa đối chiếu với *Pāṭīgaṇita* của Śrīdhara và Bakhshālī sau đợt định niên đại lại năm 2024. — `reviews/ro1-nguon-ngoai-review.md` #Ca 36
- Quy ước mức bằng chứng: (a) đích gồm nhiều người mà ai cũng có tiếp xúc trực tiếp (Hillel ← Shemaiah và Avtalyon; al-Bukhari ×2) bị hạ thành `qua trường phái`, làm mất thông tin. Đề xuất cho tách dòng khi còn chỗ. (b) Leucippus → Democritus: bằng chứng chồng đời vòng lại chính mệnh đề quan hệ. Nên quyết một lần cho cả atlas. — `reviews/tructiep-freetext-B.md` #Ca 25, `reviews/tructiep-freetext-A.md` #Ca 16, `reviews/tructiep-freetext-C.md` #Ca 38–39
- Mục vua dạng `trị vì X–Y` không được lint đối chiếu Wikidata, kể cả khi Wikidata có năm sinh (Trisong Detsen `Q366661`). Hai mục Tây Tạng đang chịu hai chế độ kiểm khác nhau. — `reviews/ro1-nguon-ngoai-review.md` #Ca 18
- ch05 Ghi chú: *Trinh Quán chính yếu* soạn 707–709 hay đời Huyền Tông; niên đại *Martyrium Arethae* "k. 560"; trạng thái `bitig.kz` chưa kiểm lại. — `reviews/ro1-nguon-ngoai-review.md` #Ca 5, #Ca 20, #Ca 22
- (Ngoài content) `credits.html`/`render.py:537` khai Mermaid 11.4.1 và D3 7.9.0 vendored kèm `assets/LICENSE-*.txt`; overview (`render.py:488`) khai `assets/d3.min.js`. Không có file nào trong `W/assets/`. Kiểm trên repo thật, kèm compliance B3. — `reviews/compliance-review.md` #2.2

## 4. Lint

Không chạy `build.py --offline --lint-only`: lượt này không sửa file content nào. Sau khi agent ch05 áp E1–E4: cả bốn chỗ đều nằm ở Ghi chú biên tập hoặc dòng `Nguồn`, không thuộc `WORD_TARGET`, nên không thể sinh WARN đếm chữ mới.
