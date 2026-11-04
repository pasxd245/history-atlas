# Lọc lỗi dữ kiện trong báo cáo cũ — Chapter 5, nhóm CE08 · CE09 · CE10 (kèm Ghi chú biên tập ch05)

- **Ngày:** 2026-11-04 · **Phạm vi:** `content/ch05.md` dòng 421–1070 (ba nhóm) và các khối Ghi chú biên tập từ "Charlemagne ở nhóm thế kỷ 8" (dòng 1160) tới hết (dòng 1301).
- **Báo cáo đã đọc** (`rv/old/`): ch05-ce08-gate, ch05-ce08-review, ch05-ce08-review-2, ch05-ce08-notes-review-1, ch05-ce08-notes-review-2, ch05-ce09-gate, ch05-ce09-review-a/-b/-c/-d, ch05-ce10-review, ch05-ce10-notes-review, ch05-ce10-wikidata, và phần CE08–CE10 (Ca 9–38) của tructiep-ch04-05-review.
- **Phương pháp:** (1) rút mọi mục NÊN / CÂN NHẮC / [KHÔNG KIỂM ĐƯỢC] có nội dung là khẳng định dữ kiện hoặc mâu thuẫn nội bộ; kiểm nhanh mọi mục BẮT BUỘC xem đã áp chưa; (2) đối chiếu từng mục với `wk/content/ch05.md` hiện tại; (3) mục còn nguyên thì tự kiểm bằng nguồn ngoài (Britannica, MacTutor, INAH, World History Encyclopedia, Wikipedia làm điểm khởi đầu) hoặc bằng chính repo (`data/wikidata-cache.json`, `atlaslib/lint.py`); (4) quyết định `sửa` / `làm mềm` / `giữ nguyên`.
- **Chế độ:** chỉ lọc + xác minh, **không sửa file content nào**. Mỗi mục sửa có `old_str` (chuỗi con duy nhất, đã kiểm `count == 1` trên `wk/content/ch05.md` lúc 2026-11-04) và `new_str` để áp máy. Bản máy đọc được: `scratchpad/rvtools/edits.json` (18 cặp, E1–E18).
- **Giới hạn:** hai hồ sơ cổng (ce08-gate, ce09-gate) và ce10-wikidata là hồ sơ chọn người trước khi viết, không gắn mức; đã đọc lướt để đối chiếu, không rút ra mục nào ngoài những gì các vòng bình duyệt đã nêu. Không mở được Richardson *Corpus of Early Tibetan Inscriptions*, bài Voss & Kremer, hay danh mục UNESCO bản gốc; các kết luận dựa vào nguồn cấp hai được ghi rõ. Một agent khác đang sửa cùng `ch05.md`: nếu file đổi trước khi áp, phải kiểm lại `count(old_str) == 1`.

## 1. Ứng viên lọc được

Chỉ liệt kê mục có nội dung dữ kiện / mâu thuẫn nội bộ. Các mục thuần từ vựng (`trực tiếp`, `tương đồng độc lập`, `phản bác` cho sự kiện), thể thức (§5 nêu ứng viên bị loại), nhãn `độ tin cậy` hay `lĩnh vực`, và đề xuất thêm góc nhìn **không** vào bảng này.

| # | Báo cáo · mục gốc | ID | Trường | Trích ngắn | Loại | Trạng thái content |
|---|---|---|---|---|---|---|
| 1 | ce08-review F-1 (9 mục BB) | nhiều | — | Sibawayh "cổ nhất ngoài Pāṇini", Lịch Đại Diễn, Đền IV, Shankara ×2, Charles Martel, Abu Muslim/Abu Hanifa, Aksum, Society | BẮT BUỘC | đã áp cả 9 |
| 2 | ce08-review F-2 #10 | CE08-01 | Tư tưởng | "Trong ba năm" mốc mơ hồ | dữ kiện | còn nguyên, không sai (câu trước nêu 747; 747→750) |
| 3 | ce08-review F-2 #11, review-2 BB3 | CE08-02 | Vì sao chọn | lý do Trung bình / năm sinh 709 | dữ kiện | đã sửa trước (713/714) |
| 4 | ce08-review F-2 #12–13, review-2 BB2 + 2 NÊN | CE08-02/-04 | Tư tưởng, Vì sao chọn | Abu Hanifa chết trong ngục; Melchert; "vì thế" Hanafī | dữ kiện / mâu thuẫn | đã sửa trước |
| 5 | ce08-review F-2 #14 | CE08-12 | Vì sao chọn | "bốn phương án" năm sinh Charlemagne | dữ kiện | đã sửa trước (ba: 742/747/748) |
| 6 | ce08-review F-2 #15 | CE08-06 | Vì sao chọn | Charles Martel "không để lại thiết chế nào" | dữ kiện | đã sửa trước |
| 7 | ce08-review F-2 #16–17 | CE08-08 | năm / Tư tưởng | thiếu "k."; "tổ tiên mọi đồng hồ cơ" | dữ kiện | đã sửa trước |
| 8 | ce08-review F-2 #18–19 | CE08-10 | Tư tưởng, Vì sao chọn | sắc chỉ 791; "Phía Ấn Độ thắng" | dữ kiện | đã sửa trước |
| 9 | ce08-review F-2 #20; review-2 NÊN -11 | CE08-11 | Vì sao chọn | Vācaspati "nửa đầu TK 9" | mâu thuẫn nội bộ | đã sửa trước |
| 10 | ce08-review F-2 #21 | CE08-12 | năm | `trị vì 734–766` thiếu "k." | dữ kiện | đã sửa trước |
| 11 | ce08-review F-2 #22–28 | Ghi chú | Ghi chú | K.P. Tiele; Jabir sau 2010; Ibn Ishaq "đầu tiên"; *Patriarchs* "soạn muộn"; Wilmshurst 2010; 33,2%; Mugh của Abu Muslim | dữ kiện | đã sửa trước (cả 7) |
| 12 | ce08-review F-3 #31, #35, #38, #40 | CE08-02/-06/-10, Ghi chú | nhiều | "năm thế kỷ"; "bản chép thời ông"; "người kế vị"; "tháp im lặng" | dữ kiện | đã sửa trước (cả 4) |
| 13 | ce08-review-2 F-2 (5 BB) | Bối cảnh, -02, -11, -12 | — | trường phái Sunni "thành hình"; Abu Hanifa bị giam; 709; "đề xuất"; Toniná | BẮT BUỘC | đã áp cả 5 |
| 14 | ce08-review-2 §A-01 CN(1) | CE08-01 | Tư tưởng | "cuối năm ấy chiếm Merv" | dữ kiện | đã sửa trước ("đầu năm 748") |
| 15 | ce08-review-2 §A-02 NÊN | CE08-02 | Nguồn | El-Hibri không nói về al-Mansur | quy tắc 7 | đã sửa trước (bỏ El-Hibri) |
| 16 | ce08-review-2 §A-05 CN | CE08-05 | Tư tưởng | so sánh với ngữ pháp Hy–Latin | dữ kiện | đã sửa trước |
| 17 | ce08-review-2 §A-06 NÊN ×2 | CE08-06 | Tư tưởng, Vì sao chọn | 33/46; "bản chép thời ông" | mâu thuẫn nội bộ | đã sửa trước |
| 18 | ce08-review-2 §A-07 CN | CE08-07 | Tư tưởng | AD "bắt đầu" ở Northumbria | dữ kiện | đã sửa trước ("lan ra") |
| 19 | ce08-review-2 §A-10 [KKĐ] | CE08-10 | Vì sao chọn | trụ Kar-cun "xác nhận việc lập chùa Samye" | dữ kiện chưa kiểm | **còn nguyên** → xác minh ở §2 |
| 20 | ce08-notes-review-1 (6 BB) | Ghi chú | — | Vācaspati; Harun nhặt lại; 15 ứng viên; precision; "bốn người vì trần"; al-Najāshī "sớm" | BẮT BUỘC | đã áp cả 6 |
| 21 | ce08-notes-review-1 Khối 1 NÊN + CN | CE08-11 / Ghi chú | — | "đề xuất" ≠ "chọn và phổ biến"; thiếu Chandragupta II | mâu thuẫn nội bộ | đã sửa trước |
| 22 | ce08-notes-review-1 Khối 3, 4, 5 NÊN | Ghi chú | — | P569 Charles Martel; con trỏ Jabir; Padmasambhava §3; *Testament of Ba* | dữ kiện | đã sửa trước |
| 23 | ce08-notes-review-1 Khối 7 NÊN | CE08-10 | Tư tưởng | góc An Lộc Sơn trong mục Trisong Detsen | dữ kiện | đã thêm, **nhưng câu thêm vào sai mốc** ("loạn chưa dứt" năm 763) → §2 |
| 24 | ce08-notes-review-1 Khối 8 NÊN ×2 | CE08-01, Ghi chú | — | "trong chính Sogdiana"; 80 văn kiện "Sogdian" | dữ kiện | đã sửa trước |
| 25 | ce08-notes-review-1 Khối 8 CN [KKĐ] | Ghi chú Divashtich | Ghi chú | UNESCO *Memory of the World* 2025 | dữ kiện chưa kiểm | **còn nguyên** → §2 |
| 26 | ce08-notes-review-2 (12 BB) | Ghi chú | — | tỉ lệ vùng rữa; "bốn trường phái"; Harun/trần 16; Merkurios; "đỗ đầu kỳ thi 780"; "hai chapter"; phản biện PNAS; İhsanoğlu 2023 | BẮT BUỘC | đã áp cả 12 |
| 27 | ce08-notes-review-2 NÊN (Khối 2, 4, 5, 6) | Ghi chú | — | ch90 là phụ lục VN; "quy tắc 7"; "các bộ sử Đường"; mức nền; Sogdian–Khurasan | dữ kiện | đã sửa trước |
| 28 | ce08-notes-review-2 Khối 7 NÊN | Ghi chú Alcuin | Ghi chú | Alcuin `Thấp` → `Trung bình` "cùng cách -02 xử **ba** năm sinh của al-Mansur" | mâu thuẫn nội bộ | đã sửa nhấn, **nhưng câu so sánh nay trái với mục -02** (hai giá trị 713/714) → §2 |
| 29 | ce08-notes-review-2 Khối 7 CN | Ghi chú Alcuin | Ghi chú | "triều Aachen 782–796" đặt tên nơi quá sớm | dữ kiện | **còn nguyên** → §2 |
| 30 | ce08-notes-review-2 Khối 8 NÊN ×2 | Ghi chú Harun | Ghi chú | Gutas không tên sách; hai điểm ce09-review-c §1 | dữ kiện | đã sửa trước |
| 31 | ce09-review-a (7 BB) | CE09-01/-02/-03/-05 | — | kamrateṅ; devarāja không nguồn; đạo thống; Kūkai←Huyền Trang; URL sai người; k. 787 | BẮT BUỘC | đã áp cả 7 |
| 32 | ce09-review-a NÊN | CE09-01 | Tư tưởng | "không … công trình nào còn đứng" | dữ kiện | đã sửa trước |
| 33 | ce09-review-a CN | CE09-01 | Vì sao chọn | Sdok Kak Thom 1052 hay 1053 | dữ kiện | còn nguyên; reviewer tự kết luận "không cần sửa" → giữ |
| 34 | ce09-review-a NÊN | CE09-02 | Vì sao chọn | "Toàn bộ Tân Nho học" | dữ kiện | đã sửa trước ("Dòng Lý học") |
| 35 | ce09-review-a NÊN | CE09-02 | Tư tưởng | "khác các đợt bài Phật trước, vốn là chính sách nhà nước" (Phó Dịch dâng sớ trước Hàn Dũ) | dữ kiện | **còn nguyên** → §2 |
| 36 | ce09-review-a NÊN | CE09-04 | Tư tưởng | "phân loại mọi phương trình **bậc hai** thành sáu dạng" | dữ kiện | **còn nguyên** → §2 |
| 37 | ce09-review-a NÊN | CE09-04 | Vì sao chọn | "al-Ṭabarī còn gọi ông là al-Qutrubbulli" — Rashed đọc là hai người | quy tắc 7 / dữ kiện | **còn nguyên** → §2 |
| 38 | ce09-review-a CN | CE09-05 | Tư tưởng | "vừa là nơi thu xếp vốn" không nguồn nào đỡ | dữ kiện chưa kiểm | **còn nguyên** → §2 |
| 39 | ce09-review-a NÊN | CE09-05 | Vì sao chọn | lý do Trung bình chỉ nói năm mất | dữ kiện | đã sửa trước |
| 40 | ce09-review-b (11 BB) | CE09-08/-09/-10/-11/-12 | — | Kanem; DBMNT 33; Q76499581; Eriugena 845; Anandavardhana 890 + URL; Uxmal; V&K tần suất; 869–890; Quân sự | BẮT BUỘC | đã áp cả 11 |
| 41 | ce09-review-b NÊN | CE09-08 | Vì sao chọn | "neo được năm mất vào bi ký" | dữ kiện | đã sửa trước ("neo được niên đại") |
| 42 | ce09-review-b NÊN | CE09-08 | Tư tưởng | "được cha cử tới Baghdad" — không chắc ông tới Baghdad hay chỉ Cairo | dữ kiện | **còn nguyên** → §2 |
| 43 | ce09-review-b NÊN | CE09-08 | Tư tưởng | "mang về một hiệp ước" nâng thể loại | dữ kiện | **còn nguyên** → §2 |
| 44 | ce09-review-b NÊN | CE09-11 | Tư tưởng | "đặt một câu hỏi mà thi học Sanskrit trước đó không đặt" | dữ kiện ("đầu tiên") | **còn nguyên** → §2 |
| 45 | ce09-review-b NÊN | CE09-12 | Nguồn | lý do `Thấp` = "hai hệ số tương quan GMT cạnh tranh" (lệch 2 ngày, không lệch năm) | dữ kiện | **còn nguyên** → §2 |
| 46 | ce09-review-c (BB) | Ghi chú | — | Hanbal "ông cố"; Igbo-Ukwu niên đại | BẮT BUỘC | đã áp |
| 47 | ce09-review-c NÊN (§1, §2, §3) | Ghi chú | — | İhsanoğlu "TK 19 – đầu 20"; Harun "hai thứ"; Kraus lxv; quy tắc 7 / [Tranh cãi lịch sử]; *Tân Đường thư* | dữ kiện | đã sửa trước |
| 48 | ce09-review-c §4 NÊN | Ghi chú "Bốn bẫy nhãn" | Ghi chú | "lint chỉ kiểm `wikidata:` có tồn tại và có `P31 = Q5`" | mâu thuẫn với repo | **còn nguyên** → §2 |
| 49 | ce09-review-c §5 NÊN | CE09-12 + Ghi chú "Châu Mỹ" | Vì sao chọn, Ghi chú | "Wari và Tiwanaku đang ở đỉnh trong chính thế kỷ 9" | dữ kiện | **còn nguyên (2 chỗ)** → §2 |
| 50 | ce09-review-c §5 NÊN | như trên | — | "không để lại hệ chữ viết ghi tên người" (khipu) | dữ kiện | còn nguyên → §2 |
| 51 | ce09-review-c §6 NÊN | Ghi chú `Kỹ thuật/Công nghệ` | Ghi chú | Banū Mūsā "khoảng một trăm **cơ cấu tự động**" | dữ kiện | **còn nguyên** → §2 |
| 52 | ce09-review-c §6 NÊN | như trên | Ghi chú | Ibn Khordādbeh "k. 870" (hai bản 846/885) | dữ kiện | còn nguyên → §2 |
| 53 | ce09-review-c §6 NÊN | như trên | Ghi chú | gộp ba ca vào một kết luận | lập luận | đã sửa trước |
| 54 | ce09-review-d (10 BB) | Ghi chú | — | al-Tirmidhī; Cyrillus–Methodius ×2; ô thứ năm; madhhab; [Truyền thuyết]; phụ lục ×2; CE01_09; stats | BẮT BUỘC | đã áp cả 10 |
| 55 | ce09-review-d NÊN (Khối 7–13, 17 mục) | Ghi chú | — | 221; "ba vùng mỏng nhất"; 13 người; Alfred; 8→7; (850); "bốn truyền thống"; ô thứ ba; Giáo dục; "đều"; "hợp lý"; tầng (3); 950; "không đổi cấu trúc"; nguồn 820/828; "đô hộ sứ"; Cao Biền (c) | dữ kiện / mâu thuẫn | đã sửa trước (cả 17) |
| 56 | ce09-review-d Khối 9 CN | Ghi chú "Độ nghiêng lĩnh vực CE09" | Ghi chú | 3/24 so với 23,4% | dữ kiện | đã sửa, **nhưng để lại câu cụt ". vì vòng này…"** và khối "Ba việc…" dòng 1301 tả sai cách đã sửa → §2 |
| 57 | ce10-review (12 BB) | CE10-02…-12 | — | "sổ ghi ca bệnh"; Y học 1,3%; "thầy thứ hai" Latin; Ṭāhir/Baghdad; Noonan; "bốn nguồn"; CE09 bị dập; de Casparis; "chứ bằng quân"; Khiết Đan "lần đầu"; Córdoba; Gerbert "sớm nhất" | BẮT BUỘC | đã áp cả 12 |
| 58 | ce10-review NÊN/CN Bối cảnh | Bối cảnh CE10 | Bối cảnh | 905 trước 907; "nhà Liêu" | dữ kiện | đã sửa trước |
| 59 | ce10-review NÊN | CE10-02 | Vì sao chọn | chọn 854 ngược SEP | dữ kiện | đã sửa sang 865, **nhưng câu sửa ghi 865 "khớp giá trị `preferred` của Wikidata"** (thật ra 866) → §2 |
| 60 | ce10-review NÊN ×2 | CE10-03 | Tư tưởng, Vì sao chọn | "nhận chân lý qua tưởng tượng"; giai thoại Ibn Sīnā không nguồn | quy tắc 7 | đã sửa trước |
| 61 | ce10-review NÊN ×2 | CE10-04 | Kế thừa, Vì sao chọn | Yaʿqūb thay ʿAmr; al-Tirmidhī ngoài khung | dữ kiện | đã sửa trước |
| 62 | ce10-review NÊN | CE10-06 | Tư tưởng | Prambanan không ở Kedu | dữ kiện | đã sửa trước |
| 63 | ce10-review NÊN ×2 | CE10-07 | Nguồn, năm | Potter tập II; 950–1000 là suy ra | dữ kiện | đã sửa trước |
| 64 | ce10-review NÊN | CE10-08 | Vì sao chọn | Tống Thái Tổ "đã có người giữ" | dữ kiện | đã sửa trước |
| 65 | ce10-review NÊN [KKĐ] | CE10-09 | Tư tưởng | `Tôn giáo/Tâm linh` đứng trần | dữ kiện | đã "sửa" bằng câu **"Ông đặt Phật giáo làm quốc giáo"** — chưa kiểm → §2 |
| 66 | ce10-review NÊN | CE10-10 | Ảnh hưởng tới | "hai mươi mốt" tuyển tập | dữ kiện | đã sửa trước (hai mươi) |
| 67 | ce10-review NÊN | CE10-11 | Tư tưởng | "độc quyền danh hiệu từ năm 632" | dữ kiện | đã sửa trước |
| 68 | ce10-review NÊN | CE10-12 | Nguồn | bỏ sót thư từ Gerbert | nguồn | đã sửa trước |
| 69 | ce10-notes-review (20 BB) | Ghi chú CE10 | — | (các khối 1–13) | BẮT BUỘC | đã áp |
| 70 | ce10-notes-review Khối 3 NÊN | CE10-02 (thân mục) | Vì sao chọn | "khai **năm** năm sinh **khác nhau** — 854 hai lần…" (thực ra bốn giá trị khác nhau) | mâu thuẫn nội bộ | khối ghi chú đã sửa, **thân mục còn nguyên** → §2 (gộp với #59) |
| 71 | ce10-notes-review NÊN (Khối 1, 2, 3, 4, 7, 9, 10, 12, 13) | Ghi chú CE10 | — | 5/6; dirham; "không mục nào"; "lần đầu atlas gặp"; tầng Śaka; người mở chuỗi; Gudit `somevalue`; Châu Mỹ chưa rà; Hrotsvitha 1501; 4 tên [CHƯA KẾT LUẬN]; "hơn 420 năm" | dữ kiện | đã sửa trước |
| 72 | ce10-notes-review Khối 11 NÊN | Ghi chú "`Khoa học tự nhiên` bằng 0" | Ghi chú | al-Masʿūdī "bị cắt hai lần" | dữ kiện | đã sửa, **nhưng bản áp bị chép chồng thành một câu lặp vô nghĩa** → §2 |
| 73 | ce10-notes-review Khối 7 CN [KKĐ] | Ghi chú Vācaspati | Ghi chú | trích "sớ cho ông ở nửa đầu thế kỷ 9" không còn chứng cứ | dữ kiện | còn nguyên → §2 |
| 74 | tructiep-ch04-05 Ca 9–38 | CE08–CE10 | Kế thừa / Ảnh hưởng | các cạnh `trực tiếp` không chồng đời (al-Fārābī→Ibn Sīnā, Sibawayh→al-Mubarrad, …) | từ vựng + dữ kiện | đã áp (ghi chú dòng 1300: CE10 còn 1 dòng `trực tiếp`); lint hiện không cảnh báo |

## 2. Quyết định cho các mục còn nguyên

Cột "old_str / new_str" chỉ tóm; chuỗi chính xác để áp máy ở **Phụ lục A** (và `scratchpad/rvtools/edits.json`).

| # | Ứng viên | ID | Trường | Trước | Sau | Quyết định | Bằng chứng |
|---|---|---|---|---|---|---|---|
| D1 | #23 | `CH05-CE08-10` Trisong Detsen | Tư tưởng | "loạn An Lộc Sơn chưa dứt, năm 763 quân Tây Tạng vào Trường An" | "loạn An Lộc Sơn vừa dứt, cuối năm 763 quân Tây Tạng vào Trường An" (E1) | **sửa.** Loạn kết thúc năm 763 khi Sử Triều Nghĩa chết (đầu năm, tháng 2); quân Tây Tạng vào Trường An cuối năm. Câu cũ là sản phẩm áp sai đề xuất (a) của ce08-notes-review-1 Khối 7 ("khi nhà Đường còn chưa gượng lại sau loạn"). Khối ghi chú "An Lộc Sơn: bốn tiêu chí…" vẫn khớp. | https://www.britannica.com/biography/An-Lushan · https://www.ebsco.com/research-starters/history/tibetans-capture-changan · https://en.wikipedia.org/wiki/Shi_Chaoyi (điểm khởi đầu) |
| D2 | #35 | `CH05-CE09-02` Hàn Dũ | Tư tưởng | "khác các đợt bài Phật trước, vốn là chính sách nhà nước" | "khác các đợt pháp nạn trước, vốn là chính sách nhà nước" (E2) | **làm mềm.** Phó Dịch đã dâng sớ xin bỏ hẳn Phật giáo dưới Đường Cao Tổ (Vũ Đức 7), cùng dạng hành vi quan dâng sớ như Hàn Dũ, nên "các đợt bài Phật trước" không chỉ là chính sách nhà nước. Thu hẹp về "pháp nạn" (446, 574) là phần đúng; không thêm tên/năm mới vào mục. | https://pages.ucsd.edu/~dkjordan/chin/faanfor/FuhYihMemorial.html · https://en.wikipedia.org/wiki/Fu_Yi |
| D3 | #36 | `CH05-CE09-04` Al-Khwarizmi | Tư tưởng | "phân loại mọi phương trình bậc hai thành sáu dạng chuẩn" | "quy mọi phương trình bậc nhất hoặc bậc hai về sáu dạng chuẩn" (E3) | **sửa.** MacTutor: "He first reduces an equation (linear or quadratic) to one of six standard forms"; dạng 3 "roots equal to numbers" là bậc nhất. | https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/ |
| D4 | #37 | `CH05-CE09-04` | Vì sao chọn | "…nơi hoạt động chính; al-Ṭabarī còn gọi ông là al-Qutrubbulli, theo một quận gần Baghdad." | "…nơi hoạt động chính, ở đây là Baghdad." (E4) | **làm mềm.** Chính MacTutor (nguồn 1 của mục) nêu cách đọc của Rashed: chữ "wa" bị rơi, al-Ṭabarī nói về hai người (al-Khwarizmi **và** al-Majusi al-Qutrubbulli). Bỏ epithet đang tranh chấp; kết luận `vùng:` không đổi. | https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/ |
| D5 | #38 | `CH05-CE09-05` Trương Bảo Cao | Tư tưởng | "vừa là hải quân vừa là bến trung chuyển vừa là nơi thu xếp vốn, dựa trên" | "vừa là hải quân vừa là bến trung chuyển, dựa trên" (E5) | **làm mềm.** Hai nguồn của mục (신편 한국사, 三國史記 DB) nói điều phối thương nhân, không nói chức năng tài chính (reviewer ce09-review-a). Không tìm được nguồn đỡ; bỏ vế, không thay bằng mệnh đề mới. | không xác minh được; lý do theo `rv/old/ch05-ce09-review-a.md` CE09-05 CN |
| D6 | #42 | `CH05-CE09-08` Georgios I | Tư tưởng | "ông được cha cử tới Baghdad để gỡ món nợ ấy, và mang về" | "ông được cha cử đi gỡ món nợ ấy với triều Abbasid — nguồn muộn chép là tới tận Baghdad, dù có thể ông chỉ tới Cairo — và mang về" (E6) | **làm mềm.** "It is not certain if he traveled all the way to Baghdad or whether he simply went to Cairo." Dòng Nguồn của mục đã tự khai nguồn muộn và mâu thuẫn. `ideas` 107 → 124 (trần lint 130). | https://en.wikipedia.org/wiki/Georgios_I_of_Makuria (điểm khởi đầu; dẫn Vantini/Werner) |
| D7 | #44 | `CH05-CE09-11` Anandavardhana | Tư tưởng | "Dhvanyāloka đặt một câu hỏi mà thi học Sanskrit trước đó không đặt: cái gì làm một bài thơ thành thơ? Và trả lời bằng dhvani." | "Dhvanyāloka trả lời lại một câu hỏi thi học Sanskrit đã đặt — Vāmana, khoảng năm 800, gọi rīti là linh hồn của thơ: cái gì làm một bài thơ thành thơ? Câu trả lời mới là dhvani." (E7) | **sửa** (mệnh đề "đầu tiên" sai). Vāmana (*Kāvyālaṅkārasūtravṛtti*, k. 800) đã nêu "rītir ātmā kāvyasya"; Bhāmaha trước đó nữa đã định nghĩa thơ qua alaṅkāra. Câu sau của mục ("vyañjanā … mới là linh hồn, ātman") nay ăn khớp. `ideas` 106 → 118. | https://ebooks.inflibnet.ac.in/icp04/chapter/schools-of-poetry/ |
| D8 | #45 | `CH05-CE09-12` Kʼakʼupakal | Nguồn | "…và vì khung năm phụ thuộc hoàn toàn vào phép quy đổi Lịch Đếm Dài, vốn có hai hệ số tương quan GMT cạnh tranh." | "…và vì phần lớn niên đại ở Chichén Itzá không ghi bằng Lịch Đếm Dài đầy đủ mà bằng lối rút gọn, chỉ neo được vào thế kỷ bằng suy luận; hai hệ số tương quan GMT thông dụng chỉ lệch nhau hai ngày, nên chúng không phải nguồn bất định ở cấp năm." (E9) | **sửa.** GMT 584283 và 584285 lệch đúng 2 ngày. Bi ký Chichén chủ yếu dùng lối ghi rút gọn phải diễn giải (Tun-Ahau / Katun-Ahau); mốc Chuỗi Khởi đầu là rầm Đền Serie Inicial, 30-7-878. Không ghi "duy nhất" vì chưa mở được bài Voss & Kremer để kiểm chữ ấy. | https://en.wikipedia.org/wiki/Mesoamerican_Long_Count_calendar · https://www.cambridge.org/core/journals/american-antiquity/article/abs/chichen-itza-inscriptions-and-the-maya-correlation-problem/878A603880F4F06348D2A6C3FA2A3C7D · https://lugares.inah.gob.mx/en/pagina-de-elemento/2023 |
| D9 | #49 | `CH05-CE09-12` + Ghi chú "Châu Mỹ…" | Vì sao chọn; Ghi chú | "Wari và Tiwanaku đang ở đỉnh trong chính thế kỷ này…" · "**Wari và Tiwanaku đang ở đỉnh trong chính thế kỷ 9**" | "Wari và Tiwanaku vẫn là hai nhà nước lớn ở Andes trong chính thế kỷ này…" (E8) · "**Wari và Tiwanaku vẫn còn đứng trong chính thế kỷ 9**" (E17) | **làm mềm.** Britannica đặt đế quốc Wari ở "the earlier part of the Middle Horizon" (Middle Horizon c. 600–1000), tức thế kỷ 9 không phải đỉnh của Wari; cả hai còn tồn tại tới k. 1000. Bỏ mệnh đề "đỉnh", không thêm mốc suy tàn chưa kiểm. | https://www.britannica.com/place/Huari |
| D10 | #51 | Ghi chú "Ô `Kỹ thuật/Công nghệ`…" | Ghi chú | "mô tả khoảng một trăm cơ cấu tự động" | "mô tả khoảng một trăm thiết bị cơ khí, trong đó có các cơ cấu tự động" (E16) | **làm mềm.** "The book described about one hundred devices"; trong đó có automata, bình mẹo và các cơ cấu điều khiển tự động, không phải cả trăm đều là automata. | https://en.wikipedia.org/wiki/Book_of_Ingenious_Devices |
| D11 | #48 | Ghi chú "Bốn bẫy nhãn Wikidata…" | Ghi chú | "Không ca nào bị lint bắt được, vì lint chỉ kiểm `wikidata:` có tồn tại và có `P31 = Q5`." | "Không ca nào bị lint bắt được: lint chỉ đối chiếu nhãn, `P31` và niên đại của những Q-ID mà một mục đang dùng — ca (1), (3), (4) không phải Q-ID của mục nào, còn ở ca (2) phép so nhãn vẫn qua vì "Hanbal" nằm trong tên mục." (E12) | **sửa** (mô tả sai chính repo). `lint_wikidata` duyệt `all_persons` và kiểm nhãn (so chuỗi con, độ dài > 3), `P31`, rồi `P569/P570`; Q2269861, Q61056, Q6771941 không là `wikidata:` của mục nào. | kiểm trong atlas: `atlaslib/lint.py:315–390` |
| D12 | #56 | Ghi chú "Độ nghiêng lĩnh vực của CE09…" + "Ba việc ở tầng chapter" | Ghi chú | "…nên nó thu hẹp khoảng cách thật. vì vòng này áp nguyên tắc" · "và `23,4%` của khối lĩnh vực CE09 được ghi thành "toàn atlas **khi ấy**"." | "…nên nó thu hẹp khoảng cách thật. Khoảng cách ấy có là vì vòng này áp nguyên tắc" (E13) · "và `23,4%` của khối lĩnh vực CE09 được ghi kèm mẫu số (90/385) cạnh con số của phần atlas trước vòng ấy (87/361)." (E14) | **sửa** (nhất quán nội bộ). Bản áp CÂN NHẮC của ce09-review-d để lại câu cụt bắt đầu bằng chữ thường; còn khối "Ba việc" nói con số đã được ghi thành "toàn atlas khi ấy", trong khi khối kia nay ghi theo mẫu số. | kiểm trong atlas: `content/ch05.md` dòng 1233 và 1301 |
| D13 | #59 + #70 | `CH05-CE10-02` al-Rāzī | Vì sao chọn | "`Q169234` khai năm năm sinh khác nhau — 854 hai lần, … mục chọn **865** cho khớp nguồn SEP mà chính nó dẫn và khớp giá trị `preferred` của Wikidata." | "`Q169234` khai năm giá trị năm sinh — 854 hai lần, … mục chọn **865** cho khớp nguồn SEP mà chính nó dẫn; giá trị `preferred` của Wikidata là 866." (E10) | **sửa.** Cache: `P569` = 866 (`preferred`), 854, 854, 864, 865 (`normal`), tức năm phát biểu, bốn giá trị khác nhau; 865 **không** phải giá trị `preferred`. Lệch 1 năm nằm trong dung sai `Trung bình`, nên trường `năm:` không đổi và không cần dòng Ghi chú về độ vênh mới. `why` giữ 102/104. | `data/wikidata-cache.json` (`wd:Q169234`) · https://www.wikidata.org/wiki/Q169234 |
| D14 | #28 | Ghi chú "Alcuin: người lẽ ra phải ở nhóm này" | Ghi chú | "cùng cách `CH05-CE08-02` xử ba năm sinh của al-Mansur" | "cùng nấc mà `CH05-CE08-02` dùng cho hai cách quy đổi năm sinh 713/714 của al-Mansur" (E11) | **sửa** (nhất quán nội bộ). Sau khi bỏ năm 709 không nguồn (ce08-review-2 BB3), mục -02 chỉ còn 713/714, khớp `Q31066` (`P569` 713 preferred, 714). | `data/wikidata-cache.json` (`wd:Q31066`); `content/ch05.md` dòng 446 |
| D15 | #72 | Ghi chú "`Khoa học tự nhiên` bằng 0…" | Ghi chú | "Mục `CH05-CE10-01` nêu al-Masʿūdī làm ứng viên cùng ô bị cắt, nhưng nói cho đủ thì mục `CH05-CE10-01` nêu ông làm ứng viên bị cắt ở ô `Sử học`, nhưng nói cho đủ thì ông còn là" | "Mục `CH05-CE10-01` nêu ông làm ứng viên bị cắt ở ô `Sử học`, nhưng nói cho đủ thì ông còn là" (E15) | **sửa** (câu hỏng do áp chồng câu thay thế của ce10-notes-review Khối 11 lên câu cũ). | kiểm trong atlas: `content/ch05.md` dòng 1283 |
| D16 | #65 | `CH05-CE10-09` Cao Ly Thái Tổ | Tư tưởng | "Ông đặt Phật giáo làm quốc giáo, và dựng bộ máy" | "Ông bảo trợ Phật giáo, và dựng bộ máy" (E18) | **làm mềm.** Câu được thêm để đỡ nhãn `Tôn giáo/Tâm linh` sau ce10-review (reviewer tự ghi [KHÔNG KIỂM ĐƯỢC]). Britannica không nói ông lập quốc giáo; World History Encyclopedia nói ông "endorse Confucianism, Buddhism, and Shamanism as the state's main three religions" và tài trợ nhiều chùa ở kinh đô. "Bảo trợ" là phần cả hai đỡ. | https://www.britannica.com/biography/Wang-Kon · https://www.worldhistory.org/Taejo_of_Goryeo/ |
| G1 | #2 | `CH05-CE08-01` | Tư tưởng | "Trong ba năm, một cuộc nổi dậy…" | — | **giữ nguyên.** Câu đứng sau mốc 747; 747 → 750 là ba năm. Mốc chưa nêu rõ là chuyện văn, không phải sai. | `content/ch05.md` dòng 427 |
| G2 | #19 | `CH05-CE08-10` | Vì sao chọn | "trụ đá Kar-cun do con ông dựng xác nhận việc lập chùa Samye" | — | **giữ nguyên.** Trụ Kar-cun (Tride Songtsen dựng) ghi rằng thời Trisong Detsen đã lập các chùa Tam Bảo, nêu tên Samye ở Brag-mar. Hết [KHÔNG KIỂM ĐƯỢC] ở mức nguồn cấp hai; bản gốc là Richardson 1985, tr. 72–81 (chưa mở). | https://en.wikipedia.org/wiki/Trisong_Detsen · https://tibet.prm.ox.ac.uk/photo_2001.59.2.6.1.html |
| G3 | #25 | Ghi chú Divashtich | Ghi chú | "UNESCO ghi danh *Memory of the World* năm 2025" | — | **giữ nguyên.** Bảng sổ đăng ký MoW châu Á–TBD ghi "Collection of documents from Mount Mugh", năm 2025; báo UzA xác nhận văn kiện Sogdian núi Mugh có trong sổ. Chưa mở được trang UNESCO gốc (dựng động); quốc gia đề cử trong bảng cấp hai có vẻ lệch dòng. | https://www.doc.surf/wiki/memory-of-the-world-register-asia-and-the-pacific · https://uza.uz/ar/posts/unesco-unanimously-approves-uzbekistans-initiative-to-preserve-documentary-heritage_863475 |
| G4 | #29 | Ghi chú Alcuin | Ghi chú | "hoạt động ở triều Aachen 782–796" | — | **giữ nguyên.** Britannica: năm 781 Alcuin gặp Charlemagne ở Ý và "accepted his invitation to Aachen"; năm 796 về Tours. Reviewer nói đúng rằng cung Aachen chủ yếu dựng vào thập niên 790, nhưng cách gọi này có trong nguồn tham khảo chuẩn. | https://www.britannica.com/biography/Alcuin |
| G5 | #33 | `CH05-CE09-01` | Vì sao chọn | "bia Sdok Kak Thom khắc năm 1052, tức 250 năm sau" | — | **giữ nguyên.** Śaka 974 → 1052 là cách quy đổi phổ biến; reviewer tự kết luận không cần sửa. | `rv/old/ch05-ce09-review-a.md` CE09-01 CN |
| G6 | #43 | `CH05-CE09-08` | Tư tưởng | "mang về một hiệp ước viết lại điều khoản" | — | **giữ nguyên.** Nguồn tham khảo ghi "a new treaty was signed", xoá nợ và đổi sang ba năm một lần. Chữ "hiệp ước" có nguồn đỡ. | https://en.wikipedia.org/wiki/Georgios_I_of_Makuria |
| G7 | #50 | `CH05-CE09-12` + Ghi chú Châu Mỹ | — | "không để lại hệ chữ viết ghi tên người" | — | **giữ nguyên.** Khipu không phải chữ viết theo nghĩa hẹp, và reviewer thừa nhận câu "về mặt chữ nghĩa vẫn chống đỡ được". Đề xuất nói rõ khipu là thêm góc nhìn → KNOWN-ISSUES. | `rv/old/ch05-ce09-review-c.md` §5 |
| G8 | #52 | Ghi chú `Kỹ thuật/Công nghệ` | Ghi chú | "Ibn Khordādbeh (*Kitāb al-Masālik wa-l-Mamālik*, k. 870)" | — | **giữ nguyên.** "k. 870" nằm giữa hai bản 846 và 885 và có "k."; không sai. | `rv/old/ch05-ce09-review-c.md` §6 |
| G9 | #73 | Ghi chú Vācaspati | Ghi chú | "ghi ông "sớ cho ông ở nửa đầu thế kỷ 9"" | — | **giữ nguyên.** Nguyên văn cũ được ghi lại trong `ch05-ce08-review.md` F-2 #20 ("Vācaspati Miśra sớ cho ông ở nửa đầu thế kỷ 9"), nên trích dẫn có chứng cứ trong `reviews/`. | `rv/old/ch05-ce08-review.md` §F-2 #20 |

## Phụ lục A · Cặp `old_str` / `new_str` để áp máy

Mỗi `old_str` đã kiểm xuất hiện đúng **một** lần trong `wk/content/ch05.md` (2026-11-04). Áp theo thứ tự nào cũng được, vì không cặp nào chồng lên cặp khác. Thử áp cả 18 cặp trên một bản sao (`scratchpad/rvtools/wkcopy`) rồi chạy lint thì kết quả không đổi (xem §4).

### E1 → D1 (dòng 589)

old_str (verbatim):
```text
loạn An Lộc Sơn chưa dứt, năm 763 quân Tây Tạng vào Trường An
```
new_str:
```text
loạn An Lộc Sơn vừa dứt, cuối năm 763 quân Tây Tạng vào Trường An
```

### E2 → D2 (dòng 664)

old_str (verbatim):
```text
khác các đợt bài Phật trước, vốn là chính sách nhà nước
```
new_str:
```text
khác các đợt pháp nạn trước, vốn là chính sách nhà nước
```

### E3 → D3 (dòng 701)

old_str (verbatim):
```text
Nó phân loại mọi phương trình bậc hai thành sáu dạng chuẩn
```
new_str:
```text
Nó quy mọi phương trình bậc nhất hoặc bậc hai về sáu dạng chuẩn
```

### E4 → D4 (dòng 703)

old_str (verbatim):
```text
theo quy ước lấy nơi hoạt động chính; al-Ṭabarī còn gọi ông là al-Qutrubbulli, theo một quận gần Baghdad.
```
new_str:
```text
theo quy ước lấy nơi hoạt động chính, ở đây là Baghdad.
```

### E5 → D5 (dòng 719)

old_str (verbatim):
```text
vừa là hải quân vừa là bến trung chuyển vừa là nơi thu xếp vốn, dựa trên
```
new_str:
```text
vừa là hải quân vừa là bến trung chuyển, dựa trên
```

### E6 → D6 (dòng 774)

old_str (verbatim):
```text
Năm 835, ở tuổi hai mươi, ông được cha cử tới Baghdad để gỡ món nợ ấy, và mang về
```
new_str:
```text
Năm 835, ở tuổi hai mươi, ông được cha cử đi gỡ món nợ ấy với triều Abbasid — nguồn muộn chép là tới tận Baghdad, dù có thể ông chỉ tới Cairo — và mang về
```

### E7 → D7 (dòng 828)

old_str (verbatim):
```text
Dhvanyāloka đặt một câu hỏi mà thi học Sanskrit trước đó không đặt: cái gì làm một bài thơ thành thơ? Và trả lời bằng dhvani.
```
new_str:
```text
Dhvanyāloka trả lời lại một câu hỏi thi học Sanskrit đã đặt — Vāmana, khoảng năm 800, gọi rīti là linh hồn của thơ: cái gì làm một bài thơ thành thơ? Câu trả lời mới là dhvani.
```

### E8 → D9 (dòng 848)

old_str (verbatim):
```text
Wari và Tiwanaku đang ở đỉnh trong chính thế kỷ này nhưng không để lại chữ viết ghi tên người.
```
new_str:
```text
Wari và Tiwanaku vẫn là hai nhà nước lớn ở Andes trong chính thế kỷ này nhưng không để lại chữ viết ghi tên người.
```

### E9 → D8 (dòng 858)

old_str (verbatim):
```text
và vì khung năm phụ thuộc hoàn toàn vào phép quy đổi Lịch Đếm Dài, vốn có hai hệ số tương quan GMT cạnh tranh.
```
new_str:
```text
và vì phần lớn niên đại ở Chichén Itzá không ghi bằng Lịch Đếm Dài đầy đủ mà bằng lối rút gọn, chỉ neo được vào thế kỷ bằng suy luận; hai hệ số tương quan GMT thông dụng chỉ lệch nhau hai ngày, nên chúng không phải nguồn bất định ở cấp năm.
```

### E10 → D13 (dòng 885)

old_str (verbatim):
```text
`Q169234` khai năm năm sinh khác nhau — 854 hai lần, 864, 865, 866 — biên độ mười hai năm. Hồ sơ cổng đề xuất lấy đầu thấp, 854; mục chọn **865** cho khớp nguồn SEP mà chính nó dẫn và khớp giá trị `preferred` của Wikidata.
```
new_str:
```text
`Q169234` khai năm giá trị năm sinh — 854 hai lần, 864, 865, 866 — biên độ mười hai năm. Hồ sơ cổng đề xuất lấy đầu thấp, 854; mục chọn **865** cho khớp nguồn SEP mà chính nó dẫn; giá trị `preferred` của Wikidata là 866.
```

### E11 → D14 (dòng 1206)

old_str (verbatim):
```text
cùng cách `CH05-CE08-02` xử ba năm sinh của al-Mansur
```
new_str:
```text
cùng nấc mà `CH05-CE08-02` dùng cho hai cách quy đổi năm sinh 713/714 của al-Mansur
```

### E12 → D11 (dòng 1218)

old_str (verbatim):
```text
Không ca nào bị lint bắt được, vì lint chỉ kiểm `wikidata:` có tồn tại và có `P31 = Q5`.
```
new_str:
```text
Không ca nào bị lint bắt được: lint chỉ đối chiếu nhãn, `P31` và niên đại của những Q-ID mà một mục đang dùng — ca (1), (3), (4) không phải Q-ID của mục nào, còn ở ca (2) phép so nhãn vẫn qua vì "Hanbal" nằm trong tên mục.
```

### E13 → D12 (dòng 1233)

old_str (verbatim):
```text
nên nó thu hẹp khoảng cách thật. vì vòng này áp nguyên tắc
```
new_str:
```text
nên nó thu hẹp khoảng cách thật. Khoảng cách ấy có là vì vòng này áp nguyên tắc
```

### E14 → D12 (dòng 1301)

old_str (verbatim):
```text
và `23,4%` của khối lĩnh vực CE09 được ghi thành "toàn atlas **khi ấy**".
```
new_str:
```text
và `23,4%` của khối lĩnh vực CE09 được ghi kèm mẫu số (90/385) cạnh con số của phần atlas trước vòng ấy (87/361).
```

### E15 → D15 (dòng 1283)

old_str (verbatim):
```text
Mục `CH05-CE10-01` nêu al-Masʿūdī làm ứng viên cùng ô bị cắt, nhưng nói cho đủ thì mục `CH05-CE10-01` nêu ông làm ứng viên bị cắt ở ô `Sử học`, nhưng nói cho đủ thì ông còn là
```
new_str:
```text
Mục `CH05-CE10-01` nêu ông làm ứng viên bị cắt ở ô `Sử học`, nhưng nói cho đủ thì ông còn là
```

### E16 → D10 (dòng 1224)

old_str (verbatim):
```text
mô tả khoảng một trăm cơ cấu tự động
```
new_str:
```text
mô tả khoảng một trăm thiết bị cơ khí, trong đó có các cơ cấu tự động
```

### E17 → D9 (dòng 1221)

old_str (verbatim):
```text
Điều phải khai ra là **Wari và Tiwanaku đang ở đỉnh trong chính thế kỷ 9** — hai nhà nước lớn ở Andes
```
new_str:
```text
Điều phải khai ra là **Wari và Tiwanaku vẫn còn đứng trong chính thế kỷ 9** — hai nhà nước lớn ở Andes
```

### E18 → D16 (dòng 1005)

old_str (verbatim):
```text
Ông đặt Phật giáo làm quốc giáo, và dựng bộ máy
```
new_str:
```text
Ông bảo trợ Phật giáo, và dựng bộ máy
```

## 3. Cho KNOWN-ISSUES (mỏng / yếu / thiếu góc nhìn, còn mở, không sửa ở lượt này)

- `CH05-CE09-04` Al-Khwarizmi: câu mở "không hơn người đi trước ở độ khó của bài toán" là mệnh đề so sánh (với Diophantus / Babylon) mà hai nguồn của mục không đỡ. Nên dẫn Rashed hoặc hạ xuống. → `reviews/ch05-ce09-review-a.md` #CE09-04 NÊN 3
- `CH05-CE09-04`: `lĩnh vực: Khám phá/Địa lý` chỉ đỡ bằng một câu; *Zīj al-Sindhind* (cầu nối tới Brahmagupta) vắng mặt. → `reviews/ch05-ce09-review-a.md` #CE09-04 CN
- `CH05-CE09-06` Hunayn: mệnh đề "Bayt al-Ḥikma đang bị tháo dỡ" không có nguồn trong dòng Nguồn của mục (Gutas / İhsanoğlu chỉ có ở Ghi chú). → `reviews/ch05-ce09-review-a.md` #CE09-06 NÊN 2
- `CH05-CE09-07` Ibn Hanbal: "Miḥna là lần quyền lực chính trị Hồi giáo thử nắm quyền định tín điều" dễ đọc thành "duy nhất" (còn Fatimid, Almohad về sau). Musnad xếp theo Ṣaḥāba chứ không theo người truyền nói chung. → `reviews/ch05-ce09-review-b.md` #CE09-07
- `CH05-CE09-09` al-Bukhari: chưa nêu việc Muslim ibn al-Hajjaj bác điều kiện *liqāʾ*, vốn là tranh luận phương pháp lớn nhất của đúng đóng góp mà mục nêu. → `reviews/ch05-ce09-review-b.md` #CE09-09 NÊN
- `CH05-CE09-11` Anandavardhana: "hạ toàn bộ truyền thống alaṃkāra, tức bảng liệt kê thủ pháp" làm hẹp Bhāmaha / Daṇḍin (đã có guṇa, doṣa); "khung thẩm mỹ chủ đạo" chưa nhắc phe phản đối (Mahimabhaṭṭa, Kuntaka); đích Pāṇini nên là Bhartṛhari. → `reviews/ch05-ce09-review-b.md` #CE09-11 NÊN 2–4
- `CH05-CE09-12` Kʼakʼupakal: "người Châu Mỹ thế kỷ 9 duy nhất mà vòng chọn này tìm được" trong khi chính bài Voss & Kremer có Hun-pik-tokʼ (Ek Balam). → `reviews/ch05-ce09-review-b.md` #CE09-12 NÊN cuối
- Ghi chú "Châu Mỹ…": "không để lại hệ chữ viết" nên nói rõ Wari có khipu (780–1024) chưa giải mã phần phi số, và có bi ký Trung Mỹ ngoài Maya (Xochicalco, Cacaxtla). → `reviews/ch05-ce09-review-c.md` §5
- Ghi chú Harun al-Rashid: "hệ quả chính trị trực tiếp nhất" là xếp hạng không kiểm được. → `reviews/ch05-ce08-notes-review-2.md` #Khối 8 CN
- `CH05-CE10-10` Ki no Tsurayuki: ba mệnh đề đánh giá ("phê bình văn học đầu tiên bằng tiếng Nhật", nhật ký kana là việc của đàn bà, mạch tới *Chẩm thảo tử*) nay dựa vào McCullough 1985 nhưng chưa ai mở sách để đối chiếu. → `reviews/ch05-ce10-review.md` #CE10-10 NÊN 2
- `CH05-CE10-11` ʿAbd al-Raḥmān III: "tiền lệ ấy còn được dùng tới tận thời Ottoman" là chuỗi nhân quả chín thế kỷ không nguồn. → `reviews/ch05-ce10-review.md` #CE10-11 CN
- `CH05-CE10-08` Liêu Thái Tổ: hệ quan chế bắc–nam thành hình dưới A Bảo Cơ hay đời sau là `[KHÔNG KIỂM ĐƯỢC]`; câu "Vì sao chọn" dựa hẳn vào nó. → `reviews/ch05-ce10-review.md` #CE10-08 [KKĐ]
- `CH05-CE10-09` Cao Ly Thái Tổ: sau D16, nhãn `Tôn giáo/Tâm linh` chỉ còn đỡ bằng hai chữ "bảo trợ"; nguồn kiểm được thực chất chỉ có Breuker. → `reviews/ch05-ce10-review.md` #CE10-09 NÊN 1, CN
- Thể thức nêu ứng viên bị loại: CE08 6/12, CE09 4/12, CE10 5/12 (đã ghi ở Ghi chú "Ba việc ở tầng chapter"). → `reviews/ch05-ce10-review.md` #Phát hiện ở tầng nhóm 1
- **Ngoài báo cáo cũ, bắt gặp khi đọc (chưa xác minh, chỉ ghi để vòng sau kiểm):** (a) `CH05-CE10-05` "Từ ông tới 938 là một chuỗi liên tục" trong khi Nam Hán chiếm Giao Châu khoảng 930–931 rồi Dương Đình Nghệ mới khôi phục (chính mục ghi "khôi phục quyền tự chủ năm 931"); (b) `CH05-CE10-08` "*Liêu sử* … soạn đời Nguyên, tức sau ba trăm năm": 1344 cách 920 hơn bốn trăm năm (ce10-review đã ghi "sau hơn ba trăm năm"); (c) `CH05-CE08-12` "Đền IV, cao 70 mét": nguồn phổ thông cho 64,6–70 m tuỳ cách đo.

## 4. Lint

Không sửa file content nào trong `wk/`, nên `wk` không đổi. Để kiểm rằng các cặp ở Phụ lục A không gây cảnh báo mới, đã áp cả 18 cặp lên một bản sao `scratchpad/rvtools/wkcopy` rồi chạy `python3 build.py --offline --lint-only`:

- Trước khi áp (bản sao nguyên trạng): `Lint: 0 lỗi · 6 cảnh báo · 284 ghi chú`
- Sau khi áp 18 cặp: `Lint: 0 lỗi · 6 cảnh báo · 284 ghi chú` (cùng 6 WARN cũ, không WARN mới ở ch05)

Trần chữ sau khi áp (đếm `len(split())`): CE08-10 ý chính 128/130 · CE09-08 ý chính 124 · CE09-11 ý chính 118 · CE10-09 ý chính 121 · CE10-02 vì sao chọn 102/104 · CE09-12 vì sao chọn 99. Không mục nào vượt ngưỡng cảnh báo. Không cặp nào chạm dòng `năm:`, nên không có độ vênh Wikidata mới phải ghi vào Ghi chú biên tập.
