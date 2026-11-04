# Đánh giá độc lập — Chapter 9 · Cách mạng công nghiệp (nhóm CE19)

- **Phạm vi:** `content/ch09.md` — Giới thiệu chapter, Bối cảnh CE19, 12 mục `CH09-CE19-01..12`, toàn bộ `## Ghi chú biên tập`.
- **Ngày:** 2026-11-04
- **Người đánh giá:** agent độc lập (không viết chapter này), theo CONTRIBUTING "Quy trình một chapter" bước 8 và "Chín điều bắt buộc".
- **Phương pháp:**
  1. Q-ID / niên đại: đối chiếu `wikidata-cache.json` (nhãn, P31, P569/P570 + precision) và kiến thức lịch sử chuẩn (quy tắc 4).
  2. Quy tắc 6: script dò mọi tên ứng viên bị loại trong "Vì sao chọn" + Ghi chú biên tập (Maxwell, Henry, Ørsted, Wallace, Lamarck, Mendel, Engels, Proudhon, Bakunin, Koch, Semmelweis, Lister, Mahmud II, Tahtawi, Ibrahim, Nakamura, Mori, Nishi, Vidyasagar, Debendranath, Derozio, Taytu, Samori, Yohannes, San Martín, Toussaint, Sucre, Bonifacio, del Pilar, Mabini, Tohu, Tāwhiao, Te Kooti, Altynsarin, Walikhanov, Donish, Bessemer, Edison, Watt, Stephenson, Bell) với `persons.json` (417 mục) → **không ai có mục riêng**; quy tắc 6 sạch.
  3. Đích liên kết có ID: mở `persons.json` đọc tên (quy tắc 8): CH08-CE17-03 = Newton, CH08-CE18-01 = Voltaire, -02 = Rousseau, -04 = Adam Smith, -05 = Lavoisier, -07 = Sugita Genpaku; CH90-CE19_20-01..04 = Nguyễn Du, Gia Long, Hồ Xuân Hương, Trương Vĩnh Ký → **tất cả trỏ đúng người**.
  4. Mức bằng chứng `trực tiếp`: cộng trừ năm sinh–mất hai bên + có tiếp xúc chứng minh được (quy tắc 9 / "Quy ước mức bằng chứng").
  5. Nguồn: kiểm tồn tại, nhà xuất bản, năm, thể loại, luận điểm (quy tắc 2, 3, 7) bằng hiểu biết thư mục + WebSearch/WebFetch ở chỗ cần.
- **Giới hạn:** Wikidata API **không truy cập được** từ phiên này (WebFetch trả `url_not_found` cho cả `Special:EntityData` lẫn `w/api.php`) → chỉ dùng cache, mà cache chỉ giữ alias vi/en. Không mở được bản in của các sách chuyên khảo; nhận định về luận điểm sách dựa trên hiểu biết thư mục chuẩn, chỗ nào không chắc đều ghi `[KHÔNG KIỂM ĐƯỢC]`. Chương không có URL nào để kiểm (mọi nguồn là sách / văn bản gốc).

**Kết luận nhanh về Q-ID:** cả 12 Q-ID đúng người (P31 = Q5, nhãn khớp tên, P569/P570 khớp trường `năm:`); niên đại cũng khớp thực tế. Lỗi của chapter nằm ở **mức bằng chứng `trực tiếp`**, vài **mệnh đề sự kiện**, và **lập luận "Vì sao chọn" gán sai tiêu chí**.

---

## Phát hiện theo mục

### CH09-CE19-01 · Michael Faraday
Q8750 đúng; 1791–1867 đúng. Nguồn: *Experimental Researches in Electricity* (3 tập, London 1839, 1844, 1855) và F. A. J. L. James, *Michael Faraday: A Very Short Introduction* (OUP 2010) — đều có thật, đúng thể loại.

1. **BẮT BUỘC** — Tư tưởng: *"Maxwell về sau viết hình dung ấy thành bốn phương trình."* Sai sự kiện. Maxwell (1861–1865, *A Dynamical Theory of the Electromagnetic Field*) viết **hai mươi** phương trình thành phần; dạng **bốn** phương trình vectơ là do Oliver Heaviside (và Hertz) rút gọn khoảng 1884–1885. Đây là lỗi phổ biến đúng loại "tự tin mà sai".
   → Sửa: *"Maxwell về sau toán học hoá hình dung ấy (1861–1865); dạng bốn phương trình quen thuộc ngày nay là do Heaviside rút gọn lại."*
2. **NÊN** — Kế thừa: *"Hans Christian Ørsted · kế thừa · trực tiếp"*. Đường truyền thực tế là **văn bản**: Faraday đọc báo cáo 1820 của Ørsted và viết "Historical Sketch of Electro-magnetism" (1821) rồi thí nghiệm quay điện từ (1821). Theo định nghĩa, truyền qua văn bản = `qua trường phái`. Có tiếp xúc người–người (Ørsted thăm London 1823) hay không: `[KHÔNG KIỂM ĐƯỢC]` — và kể cả có thì ảnh hưởng đã truyền trước đó qua văn bản.
   → Sửa: *"- Hans Christian Ørsted · kế thừa · qua trường phái"*. (Davy · trực tiếp và Maxwell · trực tiếp thì **đúng**: Faraday là trợ lý của Davy; Faraday–Maxwell có thư từ từ 1857 và gặp nhau ở London.)
3. **NÊN** — Vì sao chọn: *"Henry bị loại theo phạm vi (a): ông công bố sau."* Công bố sau là chuyện **ưu tiên/nguyên bản (c)**, không phải phạm vi. Và *"Maxwell bị loại theo tính nguyên bản (c) …: ông toán học hoá một hình dung đã có"* đánh giá thấp Maxwell (dòng dịch chuyển, tiên đoán sóng điện từ, ánh sáng là sóng điện từ — đều nguyên bản). Lập luận không đứng.
   → Sửa: *"Henry bị loại theo (c): ông tìm ra cảm ứng gần như cùng lúc nhưng công bố sau (1832). Maxwell là ca sát nhất; ông được xét như người kế tục, vì tầm quan trọng của ông nằm chủ yếu ở nửa sau thế kỷ và chapter giữ một suất điện từ học. Đây là phán đoán, không phải vì Maxwell kém nguyên bản."*
4. **CÂN NHẮC** — Kế thừa: *"CH08-CE17-03 · phản bác · qua trường phái"* (Newton). Chính Newton (thư gửi Bentley, 1692/3) coi tác động từ xa không qua môi trường là vô lý; thứ Faraday bác là lối đọc tác-động-từ-xa của trường phái Laplace/Ampère. Giữ được, nhưng nên nói rõ ở thân mục hoặc Ghi chú.
5. **[KHÔNG KIỂM ĐƯỢC]** — Ghi chú biên tập: *"Wikidata có 34 alias, toàn bộ là phiên âm sang tiếng Ả Rập, Nga, Trung, Ukraina…"*. Cache chỉ giữ alias vi/en (cả hai rỗng), API không truy cập được. Kết luận "không có dạng tên dùng được" khớp với phần cache thấy được.

### CH09-CE19-02 · Charles Darwin
Q1035 đúng; 1809–1882 đúng. Nguồn: *Origin* (London 1859), *Descent of Man* (London 1871), Janet Browne, *Charles Darwin: Voyaging* (1995) + *The Power of Place* (2002), Jonathan Cape — đúng.

1. **BẮT BUỘC** — Kế thừa: *"Thomas Robert Malthus · kế thừa · trực tiếp"*. Darwin đọc *Essay on the Principle of Population* tháng 9/1838, **bốn năm sau khi Malthus mất (1834)**; hai người không có tiếp xúc nào được ghi nhận. Truyền qua văn bản → quy tắc 9.
   → Sửa: *"- Thomas Robert Malthus · kế thừa · qua trường phái"*.
2. **NÊN** — Vì sao chọn: *"Wallace … bị loại theo phạm vi (a) …: ông có cơ chế mà không có khối bằng chứng"* — "thiếu khối bằng chứng" không phải là phạm vi; và *"Lamarck bị loại theo tính nguyên bản (c): cơ chế của ông sai"* — sai không phải là thiếu nguyên bản (Lamarck rất nguyên bản; *Philosophie zoologique* 1809 là thuyết biến đổi loài có hệ thống đầu tiên). Gán sai tiêu chí làm lập luận không đứng.
   → Sửa: *"Wallace là ca sát nhất; ông bị loại theo phạm vi (a): chính *Nguồn gốc các loài* — không phải bài 1858 của Wallace — là văn bản thuyết phục giới khoa học và công chúng. Lamarck bị loại theo độ bền (b): cơ chế di truyền tính thu được của ông không đứng được. Mendel bị loại theo (a): công trình 1866 nằm im tới 1900."*
3. **CÂN NHẮC** — Ảnh hưởng: *"Các thuyết Darwin xã hội … · kế thừa · suy đoán học giả"*. Quy ước nói `suy đoán học giả` "nên nói rõ giả thuyết của ai"; và giới sử học (Bannister 1979; Hodgson 2004) cho rằng "Social Darwinism" phần lớn là nhãn đặt sau, gốc ở Spencer hơn Darwin — tức có tranh luận về chính loại quan hệ `kế thừa`. Đề xuất thêm một câu vào Ghi chú biên tập nêu tranh luận này.
4. **CÂN NHẮC** — *"Alfred Russel Wallace · tương đồng độc lập · trực tiếp"*: chấp nhận được (thư từ 1856–1858, bài Ternate gửi thẳng cho Darwin), nhưng ghép "độc lập" với "trực tiếp" dễ đọc thành mâu thuẫn; có thể thêm "(thư từ 1857–1858)" ở thân mục.

### CH09-CE19-03 · Karl Marx
Q9061 đúng; 1818–1883 đúng; "Các Mác" là alias vi có thật trong cache. Nguồn: *Das Kapital* I (Hamburg: Meissner, 1867), *Manifest* (London, 1848), G. Stedman Jones (Allen Lane, 2016) — đúng.

1. **BẮT BUỘC** — Kế thừa: *"CH08-CE18-04 · phản bác · trực tiếp"* (Adam Smith, 1723–1790). **Không chồng đời** (Smith mất 28 năm trước khi Marx sinh) → vi phạm thẳng điều kiện cần của `trực tiếp`.
   → Sửa: *"- CH08-CE18-04 · phản bác · qua trường phái"* (cân nhắc thêm loại quan hệ: Marx vừa dùng vừa phê phán kinh tế chính trị cổ điển — `tổng hợp` có thể đúng hơn `phản bác`).
2. **BẮT BUỘC** — Kế thừa: *"David Ricardo · kế thừa · trực tiếp"*. Ricardo mất 1823 khi Marx 5 tuổi; quan hệ hoàn toàn qua văn bản.
   → Sửa: *"- David Ricardo · kế thừa · qua trường phái"*.
3. **BẮT BUỘC** — Kế thừa: *"Georg Wilhelm Friedrich Hegel · phản bác · trực tiếp"*. Hegel mất 1831 khi Marx 13 tuổi; Marx tiếp nhận Hegel qua giảng đường Berlin và nhóm Hegel trẻ (1836–1841) — `qua trường phái`. Thêm nữa, `phản bác` đơn thuần là thiếu: Marx giữ phép biện chứng và "dựng ngược" nó (Lời bạt *Tư bản*, 1873).
   → Sửa: *"- Georg Wilhelm Friedrich Hegel · tổng hợp · qua trường phái"*.
4. **NÊN** — Vì sao chọn: *"phần lý thuyết giá trị là của Marx"*. Thuyết giá trị–lao động là của Smith và Ricardo; phần riêng của Marx là **giá trị thặng dư** và phân biệt lao động / sức lao động.
   → Sửa: *"…nhưng lý thuyết giá trị thặng dư là của Marx."*
5. **CÂN NHẮC** — Nguồn / quy tắc 7: Stedman Jones lập luận rằng "Marx thế kỷ 20" phần lớn là sản phẩm hậu kỳ (Engels, Kautsky, đảng Đức) và rằng dự án *Tư bản* của Marx dang dở/thất bại — tức đi ngược mệnh đề *"không có khung của ông thì … chính trị thế kỷ 20 đều khác hẳn"*. Dùng làm tiểu sử thì được, nhưng đừng để nó đỡ câu "Vì sao chọn"; có thể thêm một nguồn trung tính hơn (vd. David McLellan, *Karl Marx: His Life and Thought*, 1973) hoặc ghi một câu ở Ghi chú biên tập.
6. **CÂN NHẮC** — Tư tưởng: *"chênh lệch giữa giá trị công nhân tạo ra và tiền công họ nhận"* — giản lược chấp nhận được ở trần ~100 chữ.

### CH09-CE19-04 · Louis Pasteur
Q529 đúng; 1822–1895 đúng. Nguồn: *Mémoire sur les corpuscules organisés…* (Annales des sciences naturelles, 1861/1862) và Geison, *The Private Science of Louis Pasteur* (Princeton UP, 1995) — đúng, mô tả Geison đúng. Mốc "sổ tay mở năm 1971" **đúng**: cháu nội Pasteur Vallery-Radot hiến 1964, hạn chế tới khi ông mất năm 1971 (en.wikipedia "Louis Pasteur"; LRB review Goldhammer, https://lrb.co.uk/v17/n19/arthur-goldhammer/grumpy).

1. **BẮT BUỘC** — Tư tưởng: *"Bình cổ ngỗng của ông (1859–1864) … Từ đó ra chuỗi hệ quả: lên men là việc của vi sinh vật, bệnh truyền nhiễm cũng vậy…"*. Sai trình tự: công trình lên men của Pasteur **có trước** bình cổ ngỗng — mémoire lên men lactic 30/11/1857, lên men rượu 1858 (en.wikipedia "Louis Pasteur"). Lên men không phải "hệ quả" của thí nghiệm tự sinh.
   → Sửa: *"Từ nghiên cứu lên men (1857) ông đi tới kết luận vi sinh vật gây biến đổi hoá học; bình cổ ngỗng (1859–1862) cho thấy chúng đến từ không khí chứ không tự sinh. Từ đó ra chuỗi hệ quả: bệnh truyền nhiễm cũng do vi sinh vật, và đun nhẹ thì diệt được chúng."*
2. **NÊN** — Tư tưởng: *"kết thúc tranh cãi về tự sinh"*. Quá mạnh: tranh cãi còn kéo dài tới cuối thập niên 1870 (Bastian; Tyndall giải bằng bào tử chịu nhiệt). → *"giáng đòn quyết định vào thuyết tự sinh"*.
3. **NÊN** — Tư tưởng: *"vắc-xin dùng trong cuộc thử công khai năm 1881 pha theo cách của Toussaint"*. Chính xác hơn: vắc-xin Pouilly-le-Fort được Chamberland (và Roux) làm yếu bằng **kali dicromat** — một tác nhân hoá học, cùng nguyên lý với lối làm yếu bằng hoá chất (axit carbolic) của Toussaint mà Pasteur từng chê, chứ không phải bằng oxy như Pasteur ngụ ý công khai (fr.wikipedia "Secret de Pouilly-le-Fort"; LRB). Công thức của Toussaint không được dùng nguyên.
   → *"…cho thấy vắc-xin năm 1881 do trợ lý Chamberland làm yếu bằng hoá chất — gần lối của Toussaint mà Pasteur từng bác — chứ không bằng oxy như ông để công chúng hiểu."*
4. **NÊN** — Kế thừa: *"Jean-Joseph Toussaint · kế thừa · trực tiếp"*. Đời chồng lấn (1847–1890), nhưng nguồn kiểm được chỉ cho thấy hai bên là **đối thủ** trong cuộc đua vắc-xin than, Pasteur biết công trình Toussaint qua thông báo ở Viện Hàn lâm; không thấy thư từ/tiếp xúc trực tiếp (fr.wikipedia "Secret de Pouilly-le-Fort"). Tiếp xúc người–người: `[KHÔNG KIỂM ĐƯỢC]`.
   → Sửa: *"- Jean-Joseph Toussaint · kế thừa · qua trường phái"* (trừ khi tìm được thư từ cụ thể).
5. **CÂN NHẮC** — Ảnh hưởng: *"Robert Koch và ngành vi sinh y học · kế thừa · qua trường phái"* là đích hỗn hợp người + ngành mới viết (CONTRIBUTING: khi viết mới, đừng tạo đích hỗn hợp). Hơn nữa Koch–Pasteur là quan hệ đối địch; Koch kế thừa Henle/Cohn nhiều hơn. Đề xuất: *"- Ngành vi sinh y học · kế thừa · qua trường phái"*.
6. **CÂN NHẮC** — Vì sao chọn: Semmelweis (1818–1865), Lister (1827–1912), Koch (1843–1910) — cùng thời, không có mục riêng. Lập luận đứng được.

### CH09-CE19-05 · Muhammad Ali Pasha
Q182781 đúng (nhãn vi "Muhammad Ali của Ai Cập"); 1769–1849 đúng.

1. **BẮT BUỘC** — Tư tưởng: *"Rồi công ước Luân Đôn năm 1840, do các cường quốc châu Âu áp đặt, buộc ông bỏ độc quyền và cắt quân số"* (và Nguồn ghi *"Công ước Luân Đôn (1840)"*). Gán sai văn kiện. Công ước 15/7/1840 buộc ông **rút khỏi Syria, Arabia, Crete, Adana và trả hạm đội Ottoman**, đổi lấy quyền cha truyền con nối ở Ai Cập (en.wikipedia "Convention of London (1840)"). Việc **bỏ độc quyền** đến từ Hiệp ước Balta Liman Anh–Ottoman (1838) được áp cho Ai Cập sau 1841; **trần quân số 18.000** là firman của sultan năm 1841.
   → Sửa: *"Rồi các cường quốc châu Âu can thiệp: Công ước Luân Đôn (1840) buộc ông rút khỏi Syria, firman năm 1841 giới hạn quân ông ở mười tám nghìn, và hiệp ước thương mại Balta Liman (1838) bị áp cho Ai Cập, xoá độc quyền nhà nước."* Nguồn đổi thành: *"Công ước Luân Đôn (1840) và firman 1841"*.
2. **NÊN** — Tư tưởng: *"quân dịch lấy từ nông dân Ai Cập — điều chưa triều nào ở đó làm"*. Quá tuyệt đối (nhà Ptolemy đã dùng lính bản địa Ai Cập, vd. trận Raphia 217 TCN). Fahmy nói tới **nhiều thế kỷ**, không phải "chưa triều nào". → *"điều chưa triều nào ở đó làm trong nhiều thế kỷ"*.
3. **NÊN** — Tư tưởng: *"phần lớn cơ sở công nghiệp sụp theo"*. Giới nghiên cứu ghi nhận nhiều xưởng đã suy thoái từ cuối thập niên 1830 (thiếu năng lượng, quản lý, tay nghề), trước 1840–1841; quan hệ nhân quả với can thiệp châu Âu là điểm tranh luận. → *"…và các xưởng vốn đã suy yếu từ cuối thập niên 1830 phần lớn đóng cửa."*
4. **NÊN** — Nguồn / quy tắc 7: Fahmy, *All the Pasha's Men* (CUP 1997) có thật, nhưng **luận điểm trung tâm** của ông là bác hình ảnh dân tộc chủ nghĩa "Muhammad Ali người sáng lập Ai Cập hiện đại": dự án của Pasha là dự án **vương triều Ottoman**, quân đội là công cụ cưỡng bức nông dân; sách gần như không bàn công nghiệp hoá. Dùng nó để đỡ khung "công nghiệp hoá ngoài châu Âu" và cạnh *"Nhà nước Ai Cập hiện đại"* là dùng lệch luận điểm. → Thêm Afaf Lutfi al-Sayyid Marsot, *Egypt in the Reign of Muhammad Ali* (CUP, 1984) cho phần kinh tế, và một câu ở Ghi chú biên tập: *"Fahmy (1997) bác cách đọc Muhammad Ali như người dựng nước Ai Cập dân tộc; mục giữ cạnh 'nhà nước Ai Cập hiện đại' ở mức thiết chế, không ở mức ý đồ."*
5. **NÊN** — Vì sao chọn: *"Mahmud II bị loại theo tính nguyên bản (c): cải cách của ông theo sau."* Tranh cãi được: cả hai cùng nối mô hình *Nizam-ı Cedid* của Selim III (1790s) — chính quân đội kiểu mới của Muhammad Ali cũng mang tên ấy. Và *"được chọn theo (d): ca của ông là phép thử đầu tiên — và thất bại đầu tiên"* không phải lập luận counterfactual.
   → *"Mahmud II bị loại theo phạm vi (a): cải cách của ông cùng nguồn Selim III nhưng không đi tới công nghiệp hoá. Muhammad Ali được chọn theo (c): ông là người đầu tiên ngoài châu Âu thử dựng công nghiệp nhà nước."*

### CH09-CE19-06 · Fukuzawa Yukichi
Q355447 đúng; 1835–1901 đúng. Nguồn: *Gakumon no susume* (17 phần, 1872–1876), *Bunmeiron no gairyaku* (1875), Albert M. Craig, *Civilization and Enlightenment* (Harvard UP, 2009) — đúng. Ogata Kōan · trực tiếp đúng (Tekijuku, 1855); ba chuyến đi 1860 (Mỹ), 1862 (châu Âu), 1867 (Mỹ) đúng; Keio, *Jiji Shinpō* (1882) đúng.

1. **NÊN** — Tư tưởng: *"mở bằng câu 'Trời không sinh ra người trên người' và bán được chừng ba triệu bản"*. (i) Câu mở đầu có đuôi *"…to ieri"* ("người ta nói rằng") — Fukuzawa **dẫn** một câu nói, không tự xưng. (ii) Con số ~3,4 triệu là **ước tính của chính Fukuzawa, cộng dồn 17 phần** (mỗi phần ~200.000), không phải ba triệu bản của một cuốn.
   → *"…mở bằng câu 'Người ta nói Trời không sinh ra người trên người' và, theo chính Fukuzawa ước tính, cộng dồn mười bảy phần được hơn ba triệu bản…"*
2. **NÊN** — Vì sao chọn: *"Mori Arinori, bộ trưởng giáo dục đầu tiên"*. Mori là bộ trưởng giáo dục đầu tiên **trong hệ nội các (1885)**; Bộ Văn bộ (Monbushō) lập 1871, người đứng đầu đầu tiên là Ōki Takatō. → *"Mori Arinori, bộ trưởng giáo dục đầu tiên của nội các Minh Trị (1885)"*.
3. **NÊN** — Thiên lệch quan điểm (CONTRIBUTING bước 8): mục chỉ giữ mặt khai sáng. Ngoài *Datsu-A Ron* (đã nêu ở Ghi chú), việc Fukuzawa và *Jiji Shinpō* ủng hộ chiến tranh Thanh–Nhật 1894–1895 và can thiệp vào Triều Tiên là chủ đề tranh luận lớn trong sử học Nhật/Hàn; Ghi chú biên tập lấy lý do "không ký tên" của **một bài** để gác cả mạch ấy. → Thêm vào Ghi chú biên tập: *"Ngoài Datsu-A Ron, lập trường của Fukuzawa và tờ Jiji Shinpō ủng hộ chiến tranh Thanh–Nhật và can thiệp vào Triều Tiên là chủ đề tranh luận; quy thuộc từng xã luận còn bị tranh cãi (Hirayama Yō), nhưng lập trường của tờ báo do ông lập thì không."*
4. **CÂN NHẮC** — Ảnh hưởng: *"Phong trào Duy tân và Đông Du ở Việt Nam đọc ông qua tân thư · kế thừa · suy đoán học giả"*. (i) Mối liên hệ có cụ thể hơn "suy đoán": Đông Kinh Nghĩa Thục (1907) lấy tên và mô hình từ Keio **Gijuku** — điều được giới nghiên cứu nêu (vd. Vĩnh Sính). Nhưng quy ước định nghĩa `suy đoán học giả` = "nên nói rõ giả thuyết của ai" — chưa nói. (ii) Quy ước liên kết mạch chính → phụ lục **dùng ID**: Phan Bội Châu có `CH90-CE19_20-05`. Đề xuất: *"- Đông Kinh Nghĩa Thục (1907), lấy mô hình Keio Gijuku · kế thừa · qua trường phái"*, hoặc trỏ `CH90-CE19_20-05` nếu muốn có cạnh trong đồ thị. Mối liên hệ tên "Nghĩa Thục"–"Gijuku" tôi biết từ thư mục nhưng **`[KHÔNG KIỂM ĐƯỢC]`** trong phiên này.
5. **CÂN NHẮC** — Vì sao chọn: *"Nakamura bị loại theo tính nguyên bản (c): ông dịch chứ không lập luận"* — Nakamura có viết luận (vd. bài trên *Meiroku Zasshi*); "chủ yếu dịch" chính xác hơn.

### CH09-CE19-07 · Ram Mohan Roy
Q335269 đúng; 1772–1833 đúng (một số nguồn ghi sinh 1774 — trong dung sai). Nguồn: *A Conference between an Advocate for and an Opponent…* (Calcutta, 1818) có thật, đúng chủ đề; Bruce Carlisle Robertson, *Raja Rammohan Ray: The Father of Modern India* (OUP Delhi, 1995) có thật. Brahmo Sabha 1828 đúng; Regulation XVII ngày 4/12/1829 đúng; tự do báo chí (1823) đúng.

1. **BẮT BUỘC** — Tư tưởng: *"Năm 1828 ông lập Brahmo Sabha, dựng một lối thờ phụng nhất thần không tượng, không đẳng cấp."* "Không đẳng cấp" sai với Brahmo Sabha của Roy: Roy giữ dây thiêng Bà-la-môn tới khi mất, và việc bác bỏ phân biệt đẳng cấp là chương trình về sau của Keshab Chandra Sen (thập niên 1860), gây ly giáo với Debendranath vốn bảo thủ hơn về đẳng cấp (Banglapedia, "Brahma Sabha": *"Keshab Sen advocated complete abolition of caste distinction"*, https://en.banglapedia.org/index.php/Brahma_Sabha).
   → *"…dựng một lối thờ phụng nhất thần, không tượng, dựa trên Upanishad."*
2. **NÊN** — Tư tưởng: *"rồi đem lập luận ấy ra trước công luận và chính quyền; lệnh cấm năm 1829 ra đời dưới áp lực đó."* Gây hiểu lầm: theo ghi chép của chính Bentinck, Roy khuyên **không** ban lệnh cấm công khai ngay mà muốn dập tập tục "một cách lặng lẽ… qua cảnh sát", sợ gây hoang mang (thenewsminute.com, trích Manoj Mitta, *Caste Pride*). Roy vận động dư luận và bảo vệ lệnh cấm **sau** khi ban (thỉnh nguyện lên Viện Cơ mật 1830–1832).
   → *"…rồi đem lập luận ấy ra trước công luận; khi Bentinck ban lệnh cấm năm 1829, ông là người bảo vệ nó trước phản kháng của phe chính thống, kể cả ở London."*
3. **CÂN NHẮC** — Ảnh hưởng: *"Lệnh cấm sati năm 1829 · kế thừa · qua trường phái"* — cùng vấn đề như trên; giữ được nếu thân mục sửa như đề xuất.
4. **CÂN NHẮC** — Vì sao chọn (quy tắc 5): Vidyasagar (1820–1891) chồng đời với Roy chỉ 13 năm và **thời kỳ hoạt động không chồng** (luật tái hôn 1856, 23 năm sau khi Roy mất). Cùng nhóm thế kỷ nên không phạm quy tắc, nhưng câu "dùng đúng phương pháp Roy đã dựng" là so người kế tục chứ không so ứng viên cùng thời — nên viết rõ. Derozio (1809–1831), Debendranath (1817–1905) ổn.
5. **CÂN NHẮC** — Vì sao chọn: *"người đầu tiên biến phép đọc kinh điển thành công cụ cải cách luật pháp ở Nam Á"* — "đầu tiên" khó chứng minh (chính các pandit của tòa án Công ty đã được hỏi ý kiến kinh điển về sati từ 1805–1813). → *"người đầu tiên đem phép đọc kinh điển ấy ra trước công luận bằng báo in"*.

### CH09-CE19-08 · Menelik II
Q244748 đúng; 1844–1913 đúng. Wuchale 1889 điều 17 (bản Amhara "có thể", bản Ý "phải") đúng; Adwa 1/3/1896 đúng; Samori bị bắt 1898 đúng; "mười sáu năm" (1882–1898) chấp nhận được; Taytu chỉ huy quân riêng ở Adwa đúng. Nguồn: Marcus (Clarendon, 1975), Jonas (Belknap/Harvard UP, 2011) — đúng.

1. **NÊN** — Ảnh hưởng: *"Addis Ababa, tuyến đường sắt và điện tín ông cho xây"*. Đường sắt Djibouti–Addis do công ty Pháp xây theo nhượng quyền 1894, **tới Addis năm 1917** — sau khi Menelik mất (1913) và sau khi ông mất năng lực từ 1909. Đây cũng là đích hỗn hợp (thành phố + đường sắt + điện tín) viết mới.
   → *"- Addis Ababa, kinh đô ông và Taytu lập năm 1886 · kế thừa · qua trường phái"*; đường sắt nếu giữ thì ghi "do ông cấp nhượng quyền 1894, hoàn thành 1917" ở thân mục.
2. **NÊN** — Vì sao chọn: *"Yohannes IV bị loại theo (b)."* Không có lý do nào. Theo template ("Không viết chung chung"), cần một mệnh đề. → *"Yohannes IV bị loại theo (b): ông tử trận ở Metemma năm 1889 trước khi cuộc chia cắt lên đỉnh, và nhà nước ông dựng chuyển sang tay Menelik."*
3. **CÂN NHẮC** — Kế thừa: *"Taytu Betul · kế thừa · trực tiếp"*. Tiếp xúc trực tiếp hiển nhiên (vợ chồng), nhưng `kế thừa` (Menelik kế thừa tư tưởng từ Taytu) là cách đọc mạnh; ảnh hưởng của bà rõ nhất ở việc bác Wuchale. Có thể giữ, nhưng nên có một nửa câu ở thân mục cho thấy cạnh này đến từ đâu. Thiếu Tewodros II (người khởi xướng hiện đại hoá quân sự, 1855–1868) là tiền đề rõ hơn Yohannes.
4. **CÂN NHẮC** — Tư tưởng: *"Mười năm trước Adwa ông làm một việc ít ai làm"* — "ít ai làm" bỏ qua chính Samori Ture, người cũng mua súng hiện đại có hệ thống và tự sửa/chế súng. → *"việc chỉ vài nhà nước châu Phi làm được"*.

### CH09-CE19-09 · Simón Bolívar
Q8605 đúng; 1783–1830 đúng. Nguồn: *Carta de Jamaica* (Kingston, 6/9/1815 — bản gốc tiếng Tây Ban Nha thất lạc, in đầu tiên bằng tiếng Anh 1818), *Discurso de Angostura* (15/2/1819), John Lynch (Yale UP, 2006) — đúng. Sáu nước, vượt Andes 1819, Pétion · trực tiếp (Haiti 1815–1816) — đúng.

1. **BẮT BUỘC** — Kế thừa: *"CH08-CE18-02 · kế thừa · trực tiếp"* (Rousseau, 1712–1778). Rousseau mất **5 năm trước khi Bolívar sinh** → không chồng đời. Bolívar tiếp nhận Rousseau qua thầy Simón Rodríguez và qua sách.
   → *"- CH08-CE18-02 · kế thừa · qua trường phái"*.
2. **NÊN** — Tư tưởng: *"hành pháp mạnh, thượng viện tập quyền"*. Đề xuất cụ thể ở Angostura là **thượng viện cha truyền con nối** (mô phỏng Viện Quý tộc Anh), và sau này (Hiến pháp Bolivia 1826) tổng thống **trọn đời**. "Tập quyền" không phải tính chất của thượng viện.
   → *"— hành pháp mạnh, thượng viện cha truyền con nối, về sau là tổng thống trọn đời —"*.
3. **CÂN NHẮC** — Vì sao chọn (quy tắc 5): Toussaint Louverture (1743–1803) chồng đời với Bolívar, nhưng **toàn bộ** sự nghiệp ông (1791–1802) nằm ở thế kỷ 18 — tức thuộc nhóm CE18 theo quy tắc xếp nhóm của prompt, không phải ứng viên cùng ô CE19. Atlas cũng không có ông ở CE18. → Đổi ứng viên thứ hai thành người thật sự cùng ô (vd. Bernardo O'Higgins hoặc Miguel Hidalgo), và đưa Toussaint vào Ghi chú biên tập như một khuyết của CE18.
4. **CÂN NHẮC** — Vì sao chọn: *"San Martín, người giải phóng Argentina, Chile và Peru rồi lui về ở ẩn"* — Argentina tuyên bố độc lập 1816 không do San Martín lãnh đạo; Peru do Bolívar–Sucre hoàn tất (Ayacucho 1824). → *"người dẫn chiến dịch giải phóng Chile và mở đầu giải phóng Peru rồi sống lưu vong ở Pháp"*.
5. **CÂN NHẮC** — Bolívar (và Roy) khó khớp khung Giới thiệu chapter "người ngoài châu Âu đáp lại trật tự công nghiệp": cuộc chiến của ông là chiến tranh độc lập của tầng lớp creole chống Tây Ban Nha (1810–1825), trước khi châu Mỹ Latinh gặp làn sóng công nghiệp. Xem phát hiện cấp chapter.

### CH09-CE19-10 · José Rizal
Q1500 đúng; 1861–1896 đúng. *Noli Me Tangere* (Berlin, 1887), *El Filibusterismo* (Ghent, 1891), Morga *Sucesos* (Mexico, 1609), bản Rizal chú giải (Paris: Garnier, 1890) — đúng. Bonifacio bị xử tử 10/5/1897 đúng; del Pilar chủ bút *La Solidaridad* từ 1889 đúng.

1. **BẮT BUỘC** — Tư tưởng: *"bản án tử hình năm 1896 châm ngòi cho cách mạng."* Sai trình tự: Cách mạng Philippines bùng nổ **tháng 8/1896** (Tiếng hô Pugad Lawin/Balintawak, Katipunan), Rizal bị xử bắn **30/12/1896** — bốn tháng sau. Cái chết của ông **thổi bùng** chứ không **châm ngòi**. Chính mục còn ghi Bonifacio "phát động khởi nghĩa năm 1896".
   → *"…bản án tử hình cuối năm 1896, khi khởi nghĩa đã nổ ra bốn tháng, biến ông thành biểu tượng của nó."*
2. **BẮT BUỘC** — Kế thừa: *"Antonio de Morga · phản bác · trực tiếp"*. Morga (1559–1636) mất **225 năm** trước khi Rizal sinh → không chồng đời; quan hệ qua văn bản.
   → *"- Antonio de Morga · phản bác · qua trường phái"*.
3. **NÊN** — Vì sao chọn: *"Del Pilar bị loại theo phạm vi (a): báo ông chỉ tới giới du học."* *La Solidaridad* nhắm cả công luận và chính giới Tây Ban Nha (Madrid) và được đưa lậu về Philippines; "chỉ tới giới du học" không đúng hẳn. → *"…báo ông viết cho chính giới Tây Ban Nha và giới ilustrado, không tới số đông người đọc như hai cuốn tiểu thuyết."*
4. **CÂN NHẮC** — Nguồn / quy tắc 7 (thể loại): Ocampo, *Rizal Without the Overcoat* (Anvil, 1990) có thật nhưng là **tập tiểu luận báo chí** phổ thông, không phải chuyên khảo. Đề xuất thêm/thay: John N. Schumacher, *The Propaganda Movement 1880–1895* (1973; Ateneo de Manila UP, bản sửa 1997) hoặc Resil B. Mojares, *Brains of the Nation* (Ateneo de Manila UP, 2006).
5. **CÂN NHẮC** — Tư tưởng: *"Ông chủ trương cải cách chứ không ly khai"* — đúng với tuyên bố công khai (tuyên ngôn 15/12/1896 lên án khởi nghĩa), nhưng tranh luận về lập trường thật của ông (Constantino, *Veneration Without Understanding*, 1969) là điểm tranh luận lớn ở Philippines; nên có nửa câu "theo các tuyên bố công khai của ông".

### CH09-CE19-11 · Te Whiti o Rongomai
Q7691036 đúng; Wikidata P569 = 1830 precision năm, DNZB ghi "có lẽ đầu thập niên 1830" → `k. 1830` + độ tin cậy Trung bình là đúng cách; mất 18/11/1907 đúng. Ngày 5/11/1881, ~1.600 lính (1.589), trẻ con mang bánh, Parihaka ~2.000 người, giam không xét xử (West Coast Peace Preservation Act 1882) — đúng. Lời xin lỗi của Crown với Parihaka (9/6/2017) đúng. Nguồn: Dick Scott, *Ask That Mountain* (Heinemann/Southern Cross, 1975); Hazel Riseborough, *Days of Darkness* (Allen & Unwin NZ, 1989) — đúng, đúng chủ đề.

1. **NÊN** — Vì sao chọn: *"Te Kooti bị loại theo độ bền (b)."* Lập luận không đứng: Te Kooti lập **giáo hội Ringatū**, đến nay vẫn hoạt động — xét độ bền thì ông mạnh hơn. → *"Te Kooti bị loại theo tính nguyên bản (c) trong chủ đề của mục: ông có di sản bền (giáo hội Ringatū còn hoạt động), nhưng kháng chiến vũ trang không phải cái mới mà mục này đo."*
2. **NÊN** — Vì sao chọn: *"Tāwhiao bị loại theo tính nguyên bản (c)."* Không có lý do (template: "Không viết chung chung"). → *"Tāwhiao bị loại theo (c): phong trào Kīngitanga có từ 1858 dưới thời cha ông, Pōtatau."*
3. **CÂN NHẮC** — Ảnh hưởng: *"Điều trần Waitangi về Taranaki và lời xin lỗi của nhà nước New Zealand năm 2017"* — đích hỗn hợp (một báo cáo 1996 + một sự kiện 2017) viết mới; quy ước khuyên tránh. → *"- Báo cáo Taranaki của Tòa Waitangi (1996) và lời xin lỗi với Parihaka (2017) · kế thừa · qua trường phái"* vẫn hỗn hợp; tốt hơn là chỉ giữ một vế và chuyển vế kia vào thân mục.
4. **CÂN NHẮC** — Tư tưởng: *"Đây là bất bạo động có tổ chức trước các chiến dịch của Gandhi vài thập niên."* Đúng về thời gian (1881 vs 1906, ~25 năm); Ghi chú biên tập xử lý trung thực. Giữ.

### CH09-CE19-12 · Abai Qunanbaiuly
Q304890 đúng (nhãn en "Abay Kunanbaiuly"); 1845–1904 đúng. *Qara Sözder* — 45 "lời" (1890–1898) đúng; học madrasa (Ahmed Riza, Semey) và trường Nga đúng (en.wikipedia "Abai Qunanbaiuly"). Altynsarin (1841–1889) soạn chữ Kazakh theo mẫu tự Kirin (chrestomathy 1879) đúng.

1. **NÊN** — Vì sao chọn: *"Walikhanov … ông mất năm ba mươi tuổi."* Walikhanov sinh tháng 11/1835, mất 10/4/1865 → **29 tuổi** (en.wikipedia "Shoqan Walikhanov"). → *"ông mất khi chưa tròn ba mươi tuổi (1865)"*.
2. **NÊN** — Tư tưởng: *"dịch Pushkin, Lermontov, Goethe và Byron sang tiếng Kazakh — những bản dịch này là cửa đầu tiên cho văn học châu Âu vào thảo nguyên."* (i) Goethe và Byron được Abai dịch **qua bản tiếng Nga của Lermontov** ("Горные вершины", "Душа моя мрачна"), không từ nguyên bản. (ii) "Cửa đầu tiên" tranh cãi được: tuyển tập 1879 của Altynsarin đã có truyện ngụ ngôn Krylov và văn Nga dịch sang tiếng Kazakh. Bỏ sót Krylov — tác giả Abai dịch nhiều nhất.
   → *"…dịch Krylov, Pushkin, Lermontov, và qua bản Nga của Lermontov cả Goethe lẫn Byron — cùng với Altynsarin, đây là những lối vào sớm nhất của văn học châu Âu bằng tiếng Kazakh."*
3. **NÊN** — Nguồn (yêu cầu template: "1–2 nguồn tham khảo đáng tin"): chỉ có văn bản gốc và **một tiểu thuyết** (Auezov) — tức không có nguồn học thuật thứ cấp nào. Đề xuất thêm: Naomi Caffee, "How Tatiana's voice rang across the steppe: Russian literature in the life and legend of Abai", *Journal of Eurasian Studies* 9(1), 2018, tr. 12–19, doi:10.1016/j.euras.2017.12.002 — bài này bàn đúng chỗ dễ sai nhất của mục (huyền thoại "Abai là cửa ngõ văn học Nga" được dựng ở thời Xô viết). Lưu ý: tôi chỉ xác nhận được bài tồn tại qua thư mục en.wikipedia, **chưa đọc nội dung** `[KHÔNG KIỂM ĐƯỢC luận điểm]`.
4. **CÂN NHẮC** — Vì sao chọn: *"Abai được chọn theo tính nguyên bản (c): ông dựng một ngôn ngữ văn học"* — tranh luận được (Altynsarin cũng được coi là người đặt nền văn xuôi Kazakh viết). Đứng được nếu sửa câu "cửa đầu tiên".

---

## Phát hiện cấp chapter

**Đã kiểm và sạch:** khối "Cách chapter này được soạn" khớp nguyên văn `atlas-prompt.md`; quy tắc 6 sạch (không ứng viên bị loại nào có mục riêng, kể cả Hegel, Maxwell, Engels, Koch, Toussaint, Bessemer, Edison); mọi đích có ID trỏ đúng người; con số "0,0% trên 341 mục" khớp `persons.json` (341 mục mạch chính CH01–CH08, không mục nào `Châu Đại Dương`); "Máy hơi nước Watt" đúng là có trong Bối cảnh CE18; Marx dùng alias vi có thật ("Các Mác"). Nhóm phủ đủ **9/9 vùng** và **9 lĩnh vực** (Chính trị/Nhà nước 5, KHTN 3, Giáo dục 3, Văn học 3, Kinh tế 2, Tôn giáo 2, Quân sự 2, Triết học 1, Y học 1).

**C1. NÊN** — Giới thiệu: *"tới năm 1900 phần lớn châu Phi, Nam Á và Đông Nam Á nằm dưới quyền châu Âu"*. Philippines năm 1900 nằm dưới quyền **Hoa Kỳ** (sau 1898), Xiêm vẫn độc lập. → *"…nằm dưới quyền các cường quốc phương Tây"*.

**C2. NÊN** — Giới thiệu: *"Tám trong mười hai mục là người ở ngoài châu Âu tìm cách đáp lại"* trật tự công nghiệp. Đếm đúng là 8, nhưng hai trong tám không khớp khung: Bolívar (chiến tranh độc lập 1810–1825 chống Tây Ban Nha, trước khi công nghiệp hoá tới châu Mỹ Latinh) và Roy (mất 1833, đáp lại nhà nước Công ty Đông Ấn, không phải công nghiệp). → *"Tám trong mười hai mục là người ở ngoài châu Âu đối diện với quyền lực châu Âu đang lớn lên — bằng…"*.

**C3. NÊN** — Bối cảnh: *"rút ngắn khoảng cách vận tải xuống một phần mười"* — một con số không nguồn, không rõ đo gì (thời gian? chi phí? tuyến nào?). Quy tắc chất lượng: không bịa số liệu. → *"rút ngắn thời gian và giá vận tải theo bậc độ lớn"* hoặc bỏ con số.

**C4. NÊN** — Bối cảnh: *"Điện tín tách thông tin khỏi vận tải lần đầu trong lịch sử."* Quá tuyệt đối: điện báo quang học Chappe (Pháp, từ 1794), lửa hiệu, cờ hiệu đã truyền tin không cần người chở. Câu này là luận điểm nổi tiếng của James W. Carey (1989) về điện tín *điện*. → *"Điện tín điện lần đầu cho tin tức đi nhanh hơn mọi phương tiện chở người, ở quy mô liên lục địa."*

**C5. NÊN** — Bối cảnh: *"Hội nghị Berlin 1884–1885 chia châu Phi trên bàn giấy."* Đây là một ngộ nhận phổ biến: Hội nghị Berlin **không** chia châu Phi; nó đặt luật chơi (thông báo chiếm hữu bờ biển, "chiếm hữu thực tế"), công nhận Nhà nước Tự do Congo, tự do thương mại trên sông Congo/Niger. Việc chia lãnh thổ diễn ra qua hàng loạt hiệp ước song phương sau đó (1885–1914). → *"Hội nghị Berlin 1884–1885 đặt luật chơi cho cuộc tranh giành châu Phi."*

**C6. NÊN** — Bối cảnh: *"Nhật Bản và Ai Cập cùng thử công nghiệp hoá từ trên xuống."* Mâu thuẫn với chính `CH09-CE19-05` (*"trước Nhật Bản nửa thế kỷ"*): Ai Cập 1816–1840, Nhật sau 1868. → *"Ai Cập rồi Nhật Bản, cách nhau nửa thế kỷ, thử công nghiệp hoá từ trên xuống."*

**C7. CÂN NHẮC** — Bối cảnh: *"Anh bãi nô năm 1833"* — Đạo luật thông qua 1833, có hiệu lực 1/8/1834, chế độ "học nghề" kéo tới 1838. Chấp nhận được như mốc luật; có thể ghi "luật bãi nô 1833".

**C8. NÊN** — Thiên lệch vùng: **không có người Trung Hoa nào** trong CE19, và dò `persons.json` cho thấy cả atlas **không có một người Đông Á nào sinh 1760–1870 ngoài Fukuzawa**. Thế kỷ 19 của Trung Hoa — Chiến tranh Nha phiến, Thái Bình Thiên Quốc (một trong những cuộc chiến đẫm máu nhất thế kỷ), Tự cường — là ca "đáp lại" lớn nhất theo đúng khung chapter, và Ngụy Nguyên (*Hải quốc đồ chí*, 1843) còn được giới Nhật đọc trước Minh Trị. Ghi chú biên tập im lặng hoàn toàn. Đề xuất thêm khối Ghi chú: *"Trung Hoa vắng mặt ở CE19. Ứng viên đã xét: Lâm Tắc Từ, Ngụy Nguyên, Hồng Tú Toàn, Tăng Quốc Phiên, Khang Hữu Vi — bị loại vì [lý do]."* (nêu lý do thật; nếu không có lý do thì đó là khuyết cần sửa ở vòng sau).

**C9. CÂN NHẮC** — Độ phủ quan điểm: 12/12 mục là nam giới (Taytu Betul chỉ xuất hiện như ứng viên bị loại); không có tư tưởng cải cách Hồi giáo (al-Afghani, Muhammad Abduh, Sayyid Ahmad Khan), không có Nga. Không phải lỗi quy tắc, nhưng Ghi chú biên tập nên nói ra như đã nói về ô Kỹ thuật/Công nghệ.

**C10. NÊN** — Ghi chú biên tập thiếu hai mục template yêu cầu (`atlas-prompt.md`, phần "Ghi chú biên tập"): *"Nhân vật nào có thể thuộc thế kỷ khác"* — rõ nhất là Roy (1772–1833; tác phẩm chống sati 1818 ở CE19, nhưng một nửa đời ở CE18), Menelik (sống tới 1913), Bolívar; và *"Các điểm cần kiểm chứng thêm"* (vd. quy thuộc *Datsu-A Ron*, cạnh Ørsted–Faraday).

**C11. NÊN** — Ghi chú biên tập trích sai số quy tắc: khối Fukuzawa viết *"Theo quy tắc 8, `lint` không có cách nào bắt được loại sai này"* — quy tắc 8 nói về liên kết trỏ sai người; ý ở đây là quy tắc 7 (dùng nguồn đúng luận điểm) hoặc quy tắc 4. Khối Te Whiti viết *"Đây là ca áp dụng quy tắc 3"* — quy tắc 3 nói về số chương/quyển; ý ở đây là "Quy ước mức bằng chứng" (định nghĩa `suy đoán học giả`). → sửa thành *"quy tắc 7"* và *"Quy ước mức bằng chứng, mục 3"*.

**C12. NÊN** — Ghi chú biên tập, khối Việt Nam: lập luận tách Trương Vĩnh Ký khỏi Abai không đứng. Ghi chú nói tác động của Trương Vĩnh Ký *"nằm gọn trong phạm vi Việt Nam, còn … Abai vào chuẩn ngôn ngữ của cả một quốc gia sau này"* — nhưng chữ quốc ngữ cũng là chuẩn ngôn ngữ viết của **cả một quốc gia** (đông dân hơn Kazakhstan nhiều lần). Theo quy ước (a) "đo trong mạng lưới tiếp xúc", hai ca có cùng hình dạng. Lý do phân biệt thật (nếu có) phải là (c): chữ quốc ngữ do giáo sĩ thế kỷ 17 dựng, Trương Vĩnh Ký phổ biến chứ không dựng. → *"Chỗ ông tách khỏi Abai là tính nguyên bản (c): hệ chữ quốc ngữ do các giáo sĩ thế kỷ 17 dựng, ông là người đưa nó vào báo chí và sách vở đại chúng (Gia Định báo, từ 1869), chứ không dựng ngôn ngữ văn học như Abai làm với tiếng Kazakh. Phán đoán theo hệ quy chiếu toàn cầu; ở phụ lục ông được chấm theo hệ quy chiếu Việt Nam."*

**C13. CÂN NHẮC** — Ứng viên Việt Nam: Nguyễn Trường Tộ (1830–1871, các điều trần cải cách, đề xuất gửi người đi học kỹ nghệ ở nước ngoài) khớp đúng khung "đáp lại bằng công nghiệp hoá / trường học" của chapter và không có mục ở đâu trong atlas; Ghi chú không nhắc. Nên nêu và nói lý do loại.

**C14. CÂN NHẮC** — Hegel (1770–1831, *Hiện tượng học tinh thần* 1807, floruit trọn trong CE19) **không có mục ở đâu trong atlas**, chỉ xuất hiện như đích văn bản tự do trong mục Marx. Triết học của cả nhóm chỉ có 1 mục (Marx). Ghi chú biên tập nên nêu Hegel (và có thể Mill, Kierkegaard, Nietzsche) như ứng viên bị loại có lý do.

---

## Bảng tổng hợp

| Phạm vi | BẮT BUỘC | NÊN | CÂN NHẮC | [KHÔNG KIỂM ĐƯỢC] |
|---|---|---|---|---|
| 01 Faraday | 1 | 2 | 1 | 1 |
| 02 Darwin | 1 | 1 | 2 | 0 |
| 03 Marx | 3 | 1 | 2 | 0 |
| 04 Pasteur | 1 | 3 | 2 | 0 |
| 05 Muhammad Ali | 1 | 4 | 0 | 0 |
| 06 Fukuzawa | 0 | 3 | 2 | 0 |
| 07 Ram Mohan Roy | 1 | 1 | 3 | 0 |
| 08 Menelik II | 0 | 2 | 2 | 0 |
| 09 Bolívar | 1 | 1 | 3 | 0 |
| 10 Rizal | 2 | 1 | 2 | 0 |
| 11 Te Whiti | 0 | 2 | 2 | 0 |
| 12 Abai | 0 | 3 | 1 | 0 |
| Cấp chapter (C1–C14) | 0 | 10 | 4 | 0 |
| **Tổng** | **11** | **34** | **26** | **1** |

Ghi chú: một số phát hiện có mức chính nhưng chứa một phần chưa kiểm được (04-4 tiếp xúc Pasteur–Toussaint; 06-4 Đông Kinh Nghĩa Thục–Keio; 12-3 luận điểm bài Caffee) — đã ghi `[KHÔNG KIỂM ĐƯỢC]` tại chỗ, không đếm riêng.

## Danh sách BẮT BUỘC

1. **CH09-CE19-01** · Tư tưởng — "Maxwell … thành bốn phương trình": Maxwell viết 20 phương trình; dạng 4 phương trình là của Heaviside.
2. **CH09-CE19-02** · Kế thừa — Malthus · `trực tiếp`: Darwin đọc Malthus năm 1838, sau khi Malthus mất (1834); không tiếp xúc → `qua trường phái`.
3. **CH09-CE19-03** · Kế thừa — Adam Smith (CH08-CE18-04) · `trực tiếp`: không chồng đời → `qua trường phái`.
4. **CH09-CE19-03** · Kế thừa — Ricardo · `trực tiếp`: Ricardo mất khi Marx 5 tuổi → `qua trường phái`.
5. **CH09-CE19-03** · Kế thừa — Hegel · phản bác · `trực tiếp`: không tiếp xúc (Hegel mất khi Marx 13 tuổi) → `tổng hợp · qua trường phái`.
6. **CH09-CE19-04** · Tư tưởng — "Từ đó [bình cổ ngỗng 1859] ra … lên men là việc của vi sinh vật": sai trình tự, công trình lên men có từ 1857.
7. **CH09-CE19-05** · Tư tưởng + Nguồn — "công ước Luân Đôn năm 1840 … buộc ông bỏ độc quyền và cắt quân số": gán sai văn kiện (Công ước 1840 = rút khỏi Syria; trần 18.000 quân = firman 1841; bỏ độc quyền = Balta Liman 1838).
8. **CH09-CE19-07** · Tư tưởng — Brahmo Sabha "không đẳng cấp": sai; bác đẳng cấp là chương trình của Keshab Chandra Sen thập niên 1860.
9. **CH09-CE19-09** · Kế thừa — Rousseau (CH08-CE18-02) · `trực tiếp`: Rousseau mất 5 năm trước khi Bolívar sinh → `qua trường phái`.
10. **CH09-CE19-10** · Tư tưởng — "bản án tử hình năm 1896 châm ngòi cho cách mạng": khởi nghĩa nổ ra tháng 8/1896, Rizal bị xử 30/12/1896.
11. **CH09-CE19-10** · Kế thừa — Antonio de Morga · `trực tiếp`: Morga mất 1636 → `qua trường phái`.
