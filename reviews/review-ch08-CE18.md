# Đánh giá độc lập — Chapter 8 · Cách mạng khoa học, Khai sáng (nhóm CE18)

- **Phạm vi:** `content/ch08.md` — Bối cảnh CE18, 12 mục `CH08-CE18-01..12`, và các khối `## Ghi chú biên tập` liên quan CE18 (khối Equiano, khối Ô Châu Âu 10/24, phần CE18 của khối Ứng viên Việt Nam; khối "Mức `trực tiếp`…" chỉ xét ở chỗ nó chi phối cạnh của CE18). Giới thiệu chapter và CE17 do reviewer khác làm.
- **Ngày:** 2026-11-04
- **Người đánh giá:** agent độc lập (không viết chapter này), theo CONTRIBUTING "Quy trình một chapter" bước 8, "Chín điều bắt buộc", "Quy ước mức bằng chứng", "Quy ước trường `vùng`".
- **Phương pháp:**
  1. Q-ID / niên đại: `wikidata-cache.json` (nhãn, P31, P569/P570 + precision) + đối chiếu thực tế (quy tắc 4).
  2. Quy tắc 6: script dò mọi tên trong "Vì sao chọn" (Montesquieu, Diderot, Bayle, Mably, Helvétius, Hume, Wolff, Mendelssohn, Quesnay, Turgot, Hutcheson, Priestley, Scheele, Cavendish, Huệ Đống, Chương Học Thành, Cố Viêm Vũ, Maeno, Yamawaki, Ōtsuki, Mirza Mazhar, Mir Dard, Ibn Taymiyya, Sirhindi, Ibn Saud, al-Sanani, Bastidas, Túpac Katari, Cugoano, Sancho, Jefferson, Paine, Rittenhouse) với `persons.json` (417 mục) theo tên và theo Q-ID → **không ai có mục riêng**; quy tắc 6 sạch. Ba câu "X có mục riêng…" (Voltaire, Chu Hy, Shah Waliullah/Ibn Abd al-Wahhab) đều đúng ID.
  3. Đích liên kết có ID: mở `persons.json` đọc tên — CH08-CE17-03 Newton, CH08-CE17-05 Locke, CH06-CE12-04 Chu Hy, CH07-CE16-12 Inca Garcilaso de la Vega → đều trỏ đúng người được nói tới.
  4. Mức `trực tiếp`: script tính chồng đời cho mọi cạnh ID chạm CE18 (kể cả cạnh vào từ ch07/ch09/ch10); cạnh văn bản tự do kiểm bằng hiểu biết tiểu sử.
  5. Nguồn: kiểm tồn tại / nhà xuất bản / năm / thể loại bằng WebSearch/WebFetch (danh mục thư viện, SEP, Wikipedia) và hiểu biết thư mục.
- **Giới hạn:** Wikidata live không gọi (dùng cache; cache chỉ giữ nhãn/alias vi-en). Không mở được bản in các chuyên khảo; nhận định về luận điểm sách dựa trên hiểu biết thư mục chuẩn. Đếm chữ bằng `wc -w` (có thể khác cách lint đếm).

**Kết luận nhanh về Q-ID:** 12/12 Q-ID đúng người (P31 = Q5, P569/P570 khớp trường `năm:`, niên đại khớp thực tế). Lỗi tập trung ở **mức `trực tiếp`** (5 cạnh), vài **mệnh đề sự kiện** (Equiano, Voltaire, Cugoano), và **gán sai tiêu chí** trong "Vì sao chọn".

---

## Bối cảnh CE18

B1. **NÊN** — *"Chiến tranh Bảy Năm đẩy xung đột châu Âu ra bốn lục địa."* Chiến trường gồm châu Âu, Bắc Mỹ, Nam Á, Tây Phi (Senegal/Gorée), Nam Mỹ (Río de la Plata) và Philippines → ít nhất năm lục địa nếu tính Nam Mỹ riêng. Con số "bốn" là thừa và dễ bị bắt.
   → Sửa: *"Chiến tranh Bảy Năm đánh ở cả châu Âu, châu Mỹ, Ấn Độ và Tây Phi."*
B2. **NÊN** — Thiếu Cách mạng Haiti (1791–1804), cuộc cách mạng nô lệ thành công duy nhất, trong khi Bối cảnh kể cả Mỹ và Pháp. Với một nhóm có Equiano, Túpac Amaru II (sắc lệnh bãi nô) và Franklin (chủ nô → hội bãi nô), bỏ Haiti là thiên lệch khung "cách mạng Đại Tây Dương = Mỹ + Pháp". Đếm `wc -w` cho Bối cảnh hiện tại = **61 chữ** (trần ≤ 60) → phải cắt trước khi cộng.
   → Sửa đề xuất (≈55 chữ): *"Chiến tranh Bảy Năm đánh ở châu Âu, châu Mỹ, Ấn Độ và Tây Phi. Mười ba thuộc địa Bắc Mỹ độc lập, Pháp lật quân chủ, nô lệ Saint-Domingue nổi dậy năm 1791. Công ty Đông Ấn Anh thắng Plassey (1757) và nắm Bengal. Watt được cấp bằng sáng chế máy hơi nước năm 1769."*
B3. **CÂN NHẮC** — *"Nhà Thanh và Mughal đi hai hướng ngược nhau"*: câu không nói được gì kiểm được (hướng nào?). Nếu giữ, nói rõ: Thanh đạt cực thịnh thời Càn Long, Mughal tan rã sau 1707.

---

## Phát hiện theo mục

### CH08-CE18-01 · Voltaire
Q9068 đúng; 1694–1778 đúng. *Lettres philosophiques* 1734 bị Parlement Paris ra lệnh đốt — đúng. Calas bị xử 1762, án huỷ 1765 — đúng. *Candide* 1759 — đúng. Pearson, *Voltaire Almighty* (Bloomsbury 2005) — có thật.

1. **BẮT BUỘC** — Kế thừa: *"CH08-CE17-05 · kế thừa · trực tiếp"* (Locke 1632–1704). Chồng đời 10 năm (Voltaire 0–10 tuổi), không có tiếp xúc nào; Voltaire đọc Locke ở Anh 1726–28, tức qua văn bản. Vi phạm quy tắc 9 / định nghĩa `trực tiếp` (cạnh ngược `CH08-CE17-05 → CH08-CE18-01 · trực tiếp` ở CE17 cũng phải sửa theo, thuộc reviewer CE17).
   → Sửa: *"- CH08-CE17-05 · kế thừa · qua trường phái"*.
2. **BẮT BUỘC** — Tư tưởng: *"ông viết liên tục ba năm cho tới khi bản án bị huỷ, rồi rút kinh nghiệm ấy thành *Traité sur la tolérance*."* Sai trình tự: *Traité* in năm **1763** (chính dòng Nguồn ghi vậy), còn án Calas bị huỷ tháng 3/**1765**. Cuốn sách là công cụ **trong** chiến dịch, không phải tổng kết sau.
   → Sửa: *"…ông viết liên tục ba năm cho tới khi bản án bị huỷ (1765), và giữa chiến dịch ấy in *Traité sur la tolérance* (1763)."*
3. **CÂN NHẮC** — Vì sao chọn: *"Montesquieu … bị loại theo phạm vi (a) rất sát: ảnh hưởng hiến chế của ông lớn nhưng tập trung vào thiết kế nhà nước."* Thuyết phân quyền đi vào hiến pháp Mỹ 1787 và nhiều hiến pháp sau — tức (a) là điểm **mạnh** của Montesquieu; "tập trung vào một lĩnh vực" không phải thước đo phạm vi. Tương tự *"Diderot bị loại theo (c): công lao lớn của ông là tổ chức"* bỏ qua phần nguyên bản (duy vật luận trong *Le Rêve de d'Alembert*, *Le Neveu de Rameau*). Lập luận nên đặt ở (d): vai trò trí thức công can thiệp vào án là cái chỉ Voltaire tạo ra.
   → Sửa: *"Montesquieu là ca sát nhất; ông không thua về phạm vi — thuyết phân quyền đi vào hiến pháp Mỹ — mà thua ở (d): ý tưởng phân quyền đã có từ Locke và truyền thống Anh, còn vai trò trí thức công can thiệp vào án thì trước Voltaire chưa ai làm."*

### CH08-CE18-02 · Jean-Jacques Rousseau
Q6527 đúng; 1712–1778 đúng. *Discours* (Amsterdam, Rey, 1755), *Du contrat social* (Amsterdam, Rey, 1762), *Émile* 1762, năm con vào Enfants-Trouvés (theo lời chính ông trong *Confessions*) — đúng. Damrosch (Houghton Mifflin 2005) — có thật. Mably (1709–1785), Helvétius (1715–1771) cùng thời — đúng.

4. **BẮT BUỘC** — Ảnh hưởng tới: *"CH08-CE18-03 · kế thừa · trực tiếp"* (và cạnh ngược ở mục Kant). Đời chồng lấn 54 năm nhưng Kant và Rousseau **không bao giờ gặp, không thư từ**; Kant đọc *Émile* và *Contrat social* (giai thoại bức chân dung Rousseau trong phòng làm việc, ghi chú *Bemerkungen* 1764–65) — tức đường truyền văn bản. Theo định nghĩa: chồng đời là điều kiện cần, chưa đủ.
   → Sửa cả hai phía: *"- CH08-CE18-03 · kế thừa · qua trường phái"* và *"- CH08-CE18-02 · kế thừa · qua trường phái"*.
5. **CÂN NHẮC** — Vì sao chọn: câu *"Voltaire có mục riêng ở nhóm CE18 nên không phải ứng viên bị loại"* không trả lời cho ai cả (Voltaire không được nêu làm ứng viên) và tốn ~12 chữ của trần. Bỏ, hoặc dùng chỗ đó để thêm một lý do vì sao Mably "mất hút" (vd. được phái Babeuf đọc rồi bị bỏ).
6. **CÂN NHẮC** — Tư tưởng: *"mở câu 'con người sinh ra tự do…'"* — câu ấy mở **Quyển I, chương 1**, không mở cuốn sách (trước đó có lời dẫn). Sửa: *"…và Quyển I mở bằng câu…"*.
   Cạnh *Voltaire ↔ Rousseau · phản bác · trực tiếp*: **đúng** (thư Voltaire 30/8/1755 về *Discours*, *Lettre sur la Providence* của Rousseau gửi Voltaire 1756, thư "je vous hais" 1760).

### CH08-CE18-03 · Immanuel Kant
Q9312 đúng; 1724–1804 đúng. KrV Riga (Hartknoch) 1781 / B 1787, *Was ist Aufklärung?* 1784, "giấc ngủ giáo điều" (Prolegomena 1783), các bài về chủng tộc (1775, 1785, 1788) — đúng. SEP có mục `kant` (plato.stanford.edu/entries/kant/) — có thật. Hume (1711–1776), Wolff (1679–1754), Mendelssohn (1729–1786) cùng thời — đúng.

7. **BẮT BUỘC** — Kế thừa: *"CH08-CE17-03 · kế thừa · trực tiếp"* (Newton 1642–1727). Chồng đời **3 năm** (Kant 0–3 tuổi). Không có tiếp xúc nào khả dĩ. Cạnh ngược ở mục Newton (CE17) cũng ghi `trực tiếp`.
   → Sửa: *"- CH08-CE17-03 · kế thừa · qua trường phái"*.
8. **BẮT BUỘC** — Kế thừa: *"David Hume · phản bác · trực tiếp"*. Kant và Hume không gặp, không thư từ; Kant đọc Hume qua bản dịch Đức (*Enquiry* dịch 1755) và trích dẫn của Beattie. Đường văn bản → `qua trường phái`. Kèm: ngay câu "Hume đánh thức Kant" cho thấy quan hệ có phần **kế thừa** (nhận bài toán nhân quả) chứ không thuần bác.
   → Sửa: *"- David Hume · phản bác · qua trường phái"* (hoặc `kế thừa`, tuỳ ý định — nhưng mức phải là `qua trường phái`).
9. **BẮT BUỘC** — Ảnh hưởng tới: *"Ý tưởng liên bang hoà bình trong *Zum ewigen Frieden* (1795) · kế thừa · suy đoán học giả"*. Đích là **chính tác phẩm của Kant** — một mục không thể "ảnh hưởng tới" công trình của mình; dòng quan hệ sai loại. Ngoài ra `suy đoán học giả` phải nói giả thuyết của ai (định nghĩa mức 3).
   → Sửa: *"- Thuyết hoà bình dân chủ (Michael Doyle, 1983) và ý tưởng Hội Quốc Liên · kế thừa · suy đoán học giả"*, hoặc đơn giản hơn: *"- Lý thuyết hoà bình dân chủ trong quan hệ quốc tế · kế thừa · qua trường phái"* (Doyle dẫn đích danh *Zum ewigen Frieden*, nên đường văn bản là chứng minh được).
10. **CÂN NHẮC** — Thuật ngữ: *"mệnh lệnh nhất quyết"* — tài liệu tiếng Việt quen dùng *"mệnh lệnh tuyệt đối"* (kategorischer Imperativ). Đề nghị: *"**mệnh lệnh tuyệt đối** (mệnh lệnh nhất quyết)"* nếu còn chỗ.

### CH08-CE18-04 · Adam Smith
Q9381 đúng; 1723–1790 đúng (rửa tội 5/6/1723, ngày sinh không rõ — precision 10 trong cache là hợp lý). Xưởng kim găm "khoảng mười tám thao tác" (WN I.1), "people of the same trade seldom meet together…" (WN I.10), TMS 1759 — đúng. Phillipson, *Adam Smith: An Enlightened Life* (Yale UP 2010; bản Anh Allen Lane 2010) — có thật. Hume · trực tiếp (bạn thân, thư từ), Hutcheson · trực tiếp (thầy ở Glasgow 1737–40), Quesnay · trực tiếp (gặp ở Paris 1766) — **đúng mức**. Quesnay (1694–1774), Turgot (1727–1781) cùng thời — đúng.

11. **NÊN** — Vì sao chọn: *"Quesnay bị loại theo phạm vi (a): hệ của ông coi chỉ nông nghiệp sinh ra giá trị, nên sai chỗ then chốt."* "Sai" không phải tiêu chí (a) phạm vi. Hơn nữa Smith tự ghi ơn trọng nông và định đề tặng WN cho Quesnay — chính dòng Kế thừa của mục nói vậy.
   → Sửa: *"Quesnay bị loại theo độ bền (b): *Tableau économique* mở đầu phân tích dòng chu chuyển, nhưng hệ trọng nông — chỉ nông nghiệp sinh ra giá trị thặng dư — bị bỏ ngay trong thế hệ sau."*
12. **NÊN** — Ảnh hưởng tới: chỉ 2 dòng văn bản tự do, trong khi `CH09-CE19-03` Marx và `CH10-CE20-04` Keynes đều ghi `Kế thừa từ → CH08-CE18-04`. Theo quy ước "một đích có ID hơn một đích văn bản tự do", nên thêm dòng ID thứ ba. (Ngoài phạm vi nhưng ghi lại: cả hai cạnh ngược đó đang ghi `phản bác · trực tiếp` với chồng đời −28 và −93 năm → sai quy tắc 9 ở ch09/ch10.)
   → Thêm: *"- CH09-CE19-03 · phản bác · qua trường phái"*.
13. **CÂN NHẮC** — *"năng suất tăng gấp hàng trăm lần"*: Smith ước 4.800 kim/người/ngày so với "chắc chắn không tới 20, có lẽ không được một" → từ 240 đến hàng nghìn lần. "Hàng trăm" là cận dưới; giữ được, nhưng "hàng trăm, có thể hàng nghìn lần" sát văn bản hơn.

### CH08-CE18-05 · Antoine Lavoisier
Q39607 đúng; 1743–1794 đúng. Nung thiếc trong bình kín (1774), nhóm danh pháp 1787 (Guyton de Morveau, Berthollet, Fourcroy = "ba đồng nghiệp") — đúng. *Méthode de nomenclature chimique* 1787, *Traité élémentaire* 1789 — đúng. Priestley · kế thừa · trực tiếp: **đúng mức** (Priestley kể thí nghiệm với Lavoisier ở Paris tháng 10/1774). Priestley (1733–1804), Scheele (1742–1786), Cavendish (1731–1810) cùng thời — đúng.

14. **NÊN** — Vì sao chọn: *"Scheele bị loại theo phạm vi (a): ông công bố muộn. Cavendish cũng vậy."* Công bố muộn là chuyện **ưu tiên/nguyên bản (c)**, không phải phạm vi. "Cavendish cũng vậy" không đúng cho phần liên quan: hydro 1766 và thành phần nước 1784 đều được công bố đúng lúc; cái ông giấu là điện học. Và Priestley bị loại theo (c) nhưng lý do nêu ("giữ khung nhiên tố") là (d)/(b), không phải tính nguyên bản — Priestley là người tìm ra chất trước.
   → Sửa: *"Priestley bị loại theo (d): ông tìm ra chất nhưng giữ khung nhiên tố đến cuối đời. Scheele bị loại theo (c) về mặt ghi nhận: tìm ra dưỡng khí sớm nhất (k. 1771–72) nhưng sách in năm 1777. Cavendish bị loại theo (d): ông đọc thành phần nước trong khung nhiên tố."*
15. **CÂN NHẮC** — Tư tưởng: *"Marie-Anne Paulze Lavoisier dịch, vẽ hình và ghi chép cho phần lớn công trình ấy."* Bà dịch Kirwan (*Essay on Phlogiston*), vẽ 13 bản khắc của *Traité* và ghi sổ thí nghiệm — "phần lớn công trình" là phóng đại không có nguồn.
   → Sửa: *"…dịch Kirwan, vẽ các bản khắc của *Traité* và ghi sổ thí nghiệm."*
16. **CÂN NHẮC** — Nguồn: *"Arthur Donovan, … (Cambridge University Press, 1993)"*. Bản 1993 là **Blackwell** (Oxford; ISBN 0631178872); Cambridge UP là bản bìa mềm **1996** (ISBN 9780521566728). Ghép NXB của bản này với năm của bản kia. Nguồn: https://www.abebooks.com/9780631178873/Antoine-Lavoisier-Science-Administration-Revolution-0631178872/plp , https://www.thenile.co.nz/books/arthur-donovan/antoine-lavoisier-science-administration-and-revolution/9780521566728
   → Sửa: *"(Blackwell, 1993; Cambridge University Press, 1996)"*.

### CH08-CE18-06 · Đới Chấn
Q714369 đúng (Dai Zhen, alias Dongyuan); 1724–1777 đúng. *Mạnh Tử tự nghĩa sớ chứng*, câu "以理殺人", tham gia *Tứ khố toàn thư* (từ 1773) — đúng. Huệ Đống (1697–1758, phái Ngô), Chương Học Thành (1738–1801) cùng thời — đúng. Huệ Đống · kế thừa · trực tiếp: **đúng mức** (gặp ở Dương Châu 1757). Chu Hy (CH06-CE12-04) · phản bác · qua trường phái — đúng.

17. **NÊN** — Nguồn: *"Benjamin A. Elman, *From Philosophy to Philology* (Harvard University Asia Center, 1984)"*. Bản 1984 do **Council on East Asian Studies, Harvard University** in (Harvard East Asian Monographs 110); tên "Harvard University Asia Center" là tên đơn vị về sau. Bản sửa 2001 là UCLA Asian Pacific Monograph Series. Nguồn: điểm sách JAS ghi "Cambridge, Mass.: Harvard University Council on East Asian Studies, 1984. Harvard East Asian Monographs 110" — https://www.cambridge.org/core/journals/journal-of-asian-studies/article/from-philosophy-to-philology-intellectual-and-social-aspects-of-change-in-late-imperial-china-by-benjamin-a-elman-cambridge-mass-harvard-university-council-on-east-asian-studies-1984-harvard-east-asian-monographs-110-xxv-368-pp-maps-illustrations-notes-bibliography-glossary-index-2000/46D56492BD5938BDC194A5692B1681E3
   → Sửa: *"(Council on East Asian Studies, Harvard University, 1984)"*.
18. **CÂN NHẮC** — Tư tưởng: *"phải qua âm vận học, huấn hỗ và toán pháp đời Hán, chứ không qua chú giải đời Tống"*. "Toán pháp đời Hán" lạc chỗ: toán–lịch là một bộ công cụ khảo chứng của ông (ông khôi phục *Toán kinh thập thư* cho Tứ khố), nhưng đối lập Hán–Tống trong câu này là về **chú giải**. Đề nghị: *"…phải qua âm vận học, huấn hỗ và chú giải đời Hán — cùng toán học, lịch pháp khi văn bản cần — chứ không qua chú giải đời Tống."*
19. **CÂN NHẮC** — Ảnh hưởng tới: *"Phê phán Tống Nho trong tư tưởng Trung Quốc cuối thế kỷ 19"*. Triết học của Đới Chấn bị lờ đi gần một thế kỷ; sự phục hồi gắn với Chương Bính Lân (đầu TK 20), Lương Khải Siêu và Hồ Thích (*Đới Đông Nguyên đích triết học*, 1925). Đề nghị: *"Phê phán Tống Nho của Chương Bính Lân, Lương Khải Siêu và Hồ Thích đầu thế kỷ 20 · kế thừa · qua trường phái"* (đích văn bản; mức đúng).

### CH08-CE18-07 · Sugita Genpaku
Q1385286 đúng; 1733–1817 đúng. Mổ xác ở Kotsukappara ngày 4/3/1771, cuốn *Ontleedkundige Tafelen* (bản Hà Lan của Kulmus), *Giải thể tân thư* 1774, Maeno không đứng tên — đúng. "Ba năm rưỡi" (3/1771 → 8/1774) — đúng. Yamawaki Tōyō (1705–1762), mổ xác 1754 ở Kyoto — đúng, cùng thời. *Lan học sự thuỷ* viết 1815 (in 1869) — đúng. Maeno · kế thừa · trực tiếp — **đúng mức** (đồng sự).

20. **NÊN** — Vì sao chọn: *"Ōtsuki là học trò."* Không nêu tiêu chí nào → không phải lập luận loại. Ngoài ra *"Maeno … không truyền bá"* quá tay: Maeno để lại hàng chục bản dịch/biên soạn tiếng Hà Lan và là thầy của chính Ōtsuki Gentaku.
   → Sửa: *"Maeno bị loại theo phạm vi (a): ông từ chối đứng tên, nên đường truyền ra giới y học đi qua tên Sugita. … Ōtsuki (1757–1827) bị loại theo (c): ông hệ thống hoá Lan học (*Rangaku kaitei*, trường Shirandō) trên nền thầy mình."*
21. **CÂN NHẮC** — Nguồn: *"Grant K. Goodman, *Japan and the Dutch 1600–1853* (Routledge, 2000)"*. Bản 2000 là **Curzon** (Richmond, Surrey; ISBN 9780700712205); Routledge là nhà in lại sau khi mua Curzon. Nguồn: https://ci.nii.ac.jp/ncid/BA46450789 , điểm sách JAS "Richmond, Surrey: Curzon, 2000" — https://cambridge.org/core/journals/journal-of-asian-studies/article/abs/japan-and-the-dutch-by-grant-k-goodman-richmond-surrey-curzon-2000-304-pp-4000/11F900D872B35F29E1F70964986FA65A
   → Sửa: *"(Curzon, 2000)"*.

### CH08-CE18-08 · Shah Waliullah Dehlawi
Q392835 đúng; 1703–1762 đúng. Bản dịch Qur'an tiếng Ba Tư (*Fatḥ al-Raḥmān*, k. 1737–38), *Ḥujjat Allāh al-bāligha*, hoà giải *waḥdat al-wujūd* / *waḥdat al-shuhūd*, thư mời Ahmad Shah Durrani (dẫn tới Panipat 1761), du học Hijaz 1730–32 — đúng. Hermansen, *The Conclusive Argument from God* (Brill 1996) — có thật, là bản dịch quyển 1 kèm dẫn luận (đúng thể loại). Mirza Mazhar Jan-i-Janan (1699–1781), Khwaja Mir Dard (1721–1785) cùng thời — đúng.

22. **NÊN** — Kế thừa: *"Ibn Taymiyya và truyền thống Hanbali · kế thừa · qua trường phái"* — dòng này gần như chép nguyên dòng của mục Ibn Abd al-Wahhab. Shah Waliullah là người **Hanafi**, Sufi **Naqshbandi**; ông có viết bênh Ibn Taymiyya, nhưng "truyền thống Hanbali" không phải gốc của ông. Gốc được giới nghiên cứu (Hermansen, Baljon) nêu là thầy hadith ở Medina, **Abu Tahir al-Kurani** (dòng Shafi'i), và cha ông Shah Abd al-Rahim. Dòng 3 đã nói Hijaz chung chung; nên thay dòng 1 bằng một đích có người.
   → Sửa: *"- Shah Abd al-Rahim, cha ông và người lập trường Rahimiyya · kế thừa · trực tiếp"* (chồng đời, thầy–trò). Nếu giữ Ibn Taymiyya thì bỏ "và truyền thống Hanbali".
23. **CÂN NHẮC** — Tư tưởng: *"việc mà giới ulama Delhi lúc ấy coi là xúc phạm"* — chuyện ông bị phản đối (có bản kể bị ám sát hụt) là truyền thuyết phổ biến, nguồn đương thời yếu. Đề nghị: *"…việc mà theo truyền thống kể lại đã bị giới ulama Delhi phản đối…"*.
24. **CÂN NHẮC** — Vì sao chọn: *"gần như mọi phong trào Hồi giáo Nam Á sau ông đều nhận ông làm gốc"* — Deoband, Ahl-i Hadith và cả Aligarh thì đúng; Barelvi thì nhận một cách dè dặt. "Phần lớn" an toàn hơn "gần như mọi".

### CH08-CE18-09 · Muhammad ibn Abd al-Wahhab
Q69351 đúng; k. 1703 (cache precision 9 = năm) – 1792 đúng; `Trung bình` hợp lý. *Kitāb al-tawḥīd*, bị đuổi khỏi Basra/al-ʿUyayna, giao ước Dirʿiyya 1744 (vài nguồn ghi 1745) — đúng. Muhammad ibn Saud (mất 1765), al-Ṣanʿānī (1688–1768) cùng thời — đúng. Crawford, *Ibn ʿAbd al-Wahhab* (Oneworld, Makers of the Muslim World, 2014) — có thật.

25. **CÂN NHẮC** — Vì sao chọn: *"học thuyết của ông vẫn là tín điều nhà nước của Saudi Arabia"*. Từ 2017 nhà nước Saudi chủ động hạ vai trò Wahhabi (năm 2022 lập "Ngày Thành lập" mốc 1727 thay cho mốc giao ước 1744). Câu "vẫn là" đã cũ đi so với hiện trạng; độ bền (b) vẫn đứng nhưng cần nói chính xác.
   → Sửa: *"…học thuyết của ông là tín điều chính thức của nhà nước Saudi suốt hai thế kỷ rưỡi, dù từ 2017 vai trò ấy bị hạ xuống."* (Ảnh hưởng tới dòng 1 sửa tương ứng: *"Nhà nước Saudi và tín điều chính thức của nó"*.)
26. **CÂN NHẮC** — Kế thừa: dòng 2 *"Học giới hadith ở Medina và Basra"* có thể đổi thành đích có người: **Muhammad Hayat al-Sindi** (mất 1750), thầy ông ở Medina — `trực tiếp` (chồng đời, thầy–trò). Chi tiết thú vị nối hai mục: al-Sindi và Abu Tahir al-Kurani (thầy Shah Waliullah) cùng một học giới Medina — nên nói ở Ghi chú biên tập nếu muốn khẳng định hai mục "ngược hướng nhưng cùng gốc".

### CH08-CE18-10 · Túpac Amaru II
Q315937 đúng; 1738–1781 đúng (bị hành hình 18/5/1781). Sắc lệnh bãi nô 16/11/1780 ở Tungasuca — đúng. Micaela Bastidas (1744–1781), Túpac Katari (1750–1781, vây La Paz 1781) cùng thời — đúng. Walker (Belknap/Harvard UP 2014), Serulnikov (Duke UP 2013) — có thật, đúng chủ đề.

27. **BẮT BUỘC** — Kế thừa: *"CH07-CE16-12 · kế thừa · trực tiếp"* (Inca Garcilaso de la Vega, 1539–1616). Đích đúng người, nhưng **khoảng cách 122 năm** (Garcilaso mất 1616, Túpac Amaru II sinh 1738). Đường truyền là việc đọc *Comentarios Reales* — chính vì thế cuốn sách bị cấm sau khởi nghĩa. Đây là "known suspect"; cạnh ngược ở `CH07-CE16-12` (Ảnh hưởng tới → CH08-CE18-10 · trực tiếp) cũng sai — cần sửa đồng thời ở ch07.
   → Sửa ở cả hai file: *"- CH07-CE16-12 · kế thừa · qua trường phái"* / *"- CH08-CE18-10 · kế thừa · qua trường phái"*. Nguồn: en.wikipedia "Túpac Amaru II" — "interest in the Native American cause had been spurred by the re-reading of one of the Royal Commentaries of the Incas" (https://en.wikipedia.org/wiki/T%C3%BApac_Amaru_II).
28. **NÊN** — Tư tưởng: *"yêu cầu bãi chế độ *mita* … và thua ở mọi cấp toà"*. Hồ sơ ông nộp ở Tinta, Cusco rồi Lima (1777–1780) đòi **miễn** mita Potosí cho người trong vùng ông (và kiện để được công nhận dòng dõi Inca), không đòi bãi bỏ cả chế độ. "Mọi cấp toà" phóng đại: đơn bị bác/ngâm ở Audiencia Lima.
   → Sửa: *"…ông đi kiện nhiều năm ở Cusco rồi Lima, xin miễn mita mỏ Potosí cho người bản địa vùng ông, và bị bác."*
29. **CÂN NHẮC** — *"một trong những văn bản bãi nô sớm nhất ở Tây bán cầu"*: Vermont (1777) và luật bãi nô từ từ của Pennsylvania (3/1780) có trước. Cụm "một trong những" giữ được, nhưng sắc lệnh có phạm vi hẹp (giải phóng nô lệ, chủ yếu của người Tây Ban Nha, trong vùng khởi nghĩa, như một biện pháp chiến tranh); nên nói rõ để khỏi bị đọc như bãi nô phổ quát. Đề nghị: *"…tuyên bố giải phóng nô lệ trong vùng mình kiểm soát — văn bản bãi nô đầu tiên ở châu Mỹ thuộc Tây Ban Nha."*
30. **CÂN NHẮC** — *"cấm cả trang phục lẫn sách vở Inca"*: lệnh cấm sau 1781 gồm y phục, danh hiệu "Inca", nghi lễ, và đích danh *Comentarios Reales* (lệnh hoàng gia 1782) `[KHÔNG KIỂM ĐƯỢC ngày lệnh cấm chính xác]`. Nêu đích danh cuốn sách làm luôn lập luận cho cạnh Garcilaso: *"…cấm y phục, danh hiệu Inca và cả *Comentarios Reales* của Garcilaso."*
31. **CÂN NHẮC** — Vì sao chọn: *"Túpac Katari bị loại theo phạm vi (a)"* không kèm lý do; lại cùng tiêu chí với Bastidas nhưng tình huống khác (Katari lãnh đạo khởi nghĩa Aymara riêng). Thêm nửa câu: *"…(a): khởi nghĩa của ông giới hạn ở vùng Aymara quanh La Paz."*

### CH08-CE18-11 · Olaudah Equiano
Q379887 đúng (cache không có nhãn vi/en, sitelink enwiki "Olaudah Equiano"; P569 1745 precision 9, P570 1797); k. 1745–1797 đúng; `Trung bình` hợp lý (sổ rửa tội 1759 "12 tuổi" → k. 1747). Mua lại tự do 1766, chín lần in khi còn sống (1789–1794), Sons of Africa, báo Granville Sharp vụ Zong (1783), hồ sơ rửa tội + sổ hải quân ghi Carolina — đúng. Carretta (Univ. of Georgia Press 2005) — có thật, đúng là nguồn nêu bằng chứng Carolina. Cugoano · kế thừa · trực tiếp — **đúng mức** (cùng ký thư của Sons of Africa). Cugoano (k. 1757–sau 1791), Sancho (k. 1729–1780) cùng thời — đúng.

32. **BẮT BUỘC** — Tư tưởng: *"nó đưa một **tiếng nói ngôi thứ nhất** vào cuộc tranh luận mà trước đó chỉ có người da trắng nói."* Sai sự kiện, và mâu thuẫn ngay với "Vì sao chọn" của chính mục (Cugoano 1787). Trước 1789 đã có: Briton Hammon (1760), Ukawsaw Gronniosaw (1772), Phillis Wheatley (1773), *Letters* của Sancho (1782), Cugoano (1787).
   → Sửa: *"Giá trị của nó nằm ở chỗ nó đưa một **tiếng nói ngôi thứ nhất** có độ phủ chưa từng có vào cuộc tranh luận — trước đó tiếng nói người Phi ở Anh chỉ có vài cuốn in ít."*
33. **BẮT BUỘC** — Vì sao chọn: *"sách ông bán ít hơn hẳn và không được tái bản."* Sai: *Thoughts and Sentiments* có bản tiếng Pháp năm **1788** (*Réflexions sur la traite et l'esclavage des nègres*) và bản thứ hai rút gọn năm **1791**. Nguồn: SEP "Ottobah Cugoano" §1.3 — "an abridged re-publication of the first" (https://plato.stanford.edu/entries/cugoano/).
   → Sửa: *"Cugoano là ca sát nhất và bị loại theo phạm vi (a): sách ông chỉ có một bản rút gọn (1791) và một bản dịch Pháp, so với chín lần in của Equiano."*
34. **NÊN** — Vùng / Ghi chú biên tập: xem phát hiện #44 (Ghi chú lập luận theo nơi sinh, trái quy ước `vùng` đã ghi trong CONTRIBUTING ngày 2026-11-03).

### CH08-CE18-12 · Benjamin Franklin
Q34969 đúng; 1706–1790 đúng. Alias "Richard Saunders" là bút danh thật của *Poor Richard's Almanack* (không bịa). Thuyết một chất lỏng, đặt "positive/negative", cột thu lôi, Library Company (1731), Union Fire Company (1736), Pennsylvania Hospital (1751), liên minh Pháp 1778, chủ tịch Pennsylvania Abolition Society (1787) — đúng. *Experiments and Observations on Electricity* (London, E. Cave, 1751), Morgan (Yale UP 2002) — có thật. Jefferson (1743–1826), Paine (1737–1809), Rittenhouse (1732–1796) cùng thời — đúng.

35. **NÊN** — Tư tưởng: *"Thí nghiệm hộp canh và thả diều năm 1752 chứng minh sét là hiện tượng điện"* — gán cả hai cho Franklin. Thí nghiệm **hộp canh** (sentry box) do Franklin **đề xuất** (1750) nhưng **Thomas-François Dalibard** làm ở Marly ngày 10/5/1752; thí nghiệm diều của Franklin (6/1752) chỉ được kể lại muộn (thư 10/1752, Priestley 1767) và có học giả nghi ngờ.
   → Sửa: *"Thí nghiệm hộp canh do ông đề xuất, Dalibard làm ở Pháp năm 1752, chứng minh sét là hiện tượng điện; chuyến thả diều của ông cùng năm thì chỉ được kể lại sau."*
36. **NÊN** — Kế thừa: *"Hội Hoàng gia Luân Đôn, nơi công bố thư từ về điện của ông"*. Thư của Franklin gửi **Peter Collinson**; Collinson đọc một phần ở Royal Society, nhưng tập thư được **Edward Cave** in thành sách năm 1751 (chính nguồn số 1 của mục), không phải Royal Society công bố. Hội chỉ trao Huy chương Copley năm 1753. Đồng thời "kế thừa" một định chế công bố là sai loại quan hệ. Nguồn: https://en.wikipedia.org/wiki/Experiments_and_Observations_on_Electricity (publisher E. Cave; Collinson "communicated Franklin's ideas to the Royal Society").
   → Sửa: *"- Peter Collinson, người gửi ống thuỷ tinh điện và nhận thư của ông · kế thừa · trực tiếp"* (chồng đời 1694–1768, thư từ chứng minh được).
37. **CÂN NHẮC** — Kế thừa: *"Thí nghiệm điện của Stephen Gray và Charles Du Fay · kế thừa"*. Thuyết một chất lỏng của Franklin **thay** thuyết hai chất lỏng (thuỷ tinh/nhựa) của Du Fay — một phần là `phản bác`. Đích hai người lại khác quan hệ; xem lại hoặc tách ý vào thân mục.
38. **CÂN NHẮC** — Vì sao chọn: *"Paine bị loại theo phạm vi (a): tác động của ông nằm trong tuyên truyền chính trị."* *Common Sense* bán hàng chục vạn bản, *Rights of Man* đi khắp Anh–Pháp — phạm vi là điểm **mạnh** của Paine. Lý do thật nằm ở (c)/(b). Đề nghị: *"Paine bị loại theo (c): *Common Sense* phổ biến hoá lập luận cộng hoà có sẵn chứ không khởi xướng nó."*
39. **CÂN NHẮC** — Câu hỏi lớn *"Không áp dụng"* cho một mục mà đóng góp đầu tiên là lý thuyết vật lý về điện — *"Vũ trụ"* hoặc *"Thực tại"* (như Lavoisier) hợp hơn.
40. **CÂN NHẮC** — Ảnh hưởng tới: *"Hiến pháp Hoa Kỳ 1787 · kế thừa · qua trường phái"* — Franklin là đại biểu Hội nghị Lập hiến; quan hệ thật là tham gia trực tiếp, nhưng thân mục không nhắc tới Hiến pháp lần nào nên dòng này không có chỗ dựa trong mục. Hoặc thêm nửa câu vào thân mục, hoặc thay bằng *"Phong trào bãi nô Philadelphia"*, khớp với câu cuối thân mục.

---

## Phát hiện cấp nhóm / chapter (trong phạm vi CE18)

41. **BẮT BUỘC** — Ghi chú biên tập, khối *"Mức `trực tiếp` dùng cho đường truyền qua văn bản có tên người"*: *"Chúng vẫn để `trực tiếp` vì quy tắc 9 đo **đường truyền**, không đo khoảng cách thời gian: mỗi ca đều có văn bản của người sau nêu đích danh người trước…"*. Trái thẳng với CONTRIBUTING "Quy ước mức bằng chứng": `trực tiếp` = tiếp xúc người với người, **điều kiện cần: đời hai người chồng lấn**; truyền qua văn bản = `qua trường phái`. Khối này nằm ở phần CE17 (reviewer khác xử nội dung), nhưng nó chính là lý do bốn cạnh CE18 sai ở trên (Locke→Voltaire #1, Newton→Kant #7, Garcilaso→Túpac Amaru II #27; Hume→Kant #8 cùng kiểu). Mọi tiêu chí "đích có đúng một người" mà khối này nêu chỉ quyết định `trực tiếp` **được phép xét**, không quyết định nó **đúng**.
   → Sửa: thay khối bằng *"**Mức `trực tiếp` đã được rà lại theo định nghĩa trong CONTRIBUTING.** Các cạnh nối hai người không cùng sống hoặc không có tiếp xúc chứng minh được — Kepler–Copernicus, Newton–Descartes, Locke–Hobbes, Voltaire–Locke, Kant–Newton, Kant–Hume, Kant–Rousseau, Túpac Amaru II–Garcilaso — đều hạ xuống `qua trường phái`: người sau đọc người trước, nên đường truyền là văn bản. Các đích không phải một con người (Mercator–Hondius, lịch Java) vốn đã ở mức ấy."*

42. **NÊN** — Bảng cạnh `trực tiếp` chạm CE18 (script trên `persons.json`):

| Cạnh | Đời | Chồng đời | Tiếp xúc có nguồn | Kết luận |
|---|---|---|---|---|
| CH08-CE17-05 Locke ↔ CE18-01 Voltaire | 1632–1704 / 1694–1778 | 10 năm (V. 0–10 tuổi) | không | **hạ** |
| CH08-CE17-03 Newton ↔ CE18-03 Kant | 1642–1727 / 1724–1804 | 3 năm (K. 0–3 tuổi) | không | **hạ** |
| CH07-CE16-12 Garcilaso ↔ CE18-10 Túpac Amaru II | 1539–1616 / 1738–1781 | **−122 năm** | không | **hạ** (cả ch07) |
| CE18-02 Rousseau ↔ CE18-03 Kant | 1712–1778 / 1724–1804 | 54 năm | không (không gặp, không thư) | **hạ** |
| David Hume → CE18-03 Kant | 1711–1776 | 52 năm | không | **hạ** |
| CE18-01 Voltaire ↔ CE18-02 Rousseau | | 66 năm | thư từ 1755–1760 | giữ |
| Hume / Hutcheson / Quesnay → Smith | | | bạn / thầy / gặp ở Paris 1766 | giữ |
| Priestley → Lavoisier | | | gặp ở Paris 10/1774 | giữ |
| Huệ Đống → Đới Chấn | | | gặp ở Dương Châu 1757 | giữ |
| Maeno → Sugita | | | đồng dịch giả | giữ |
| Cugoano → Equiano | | | cùng Sons of Africa | giữ |

   Ngoài phạm vi, phát hiện khi chạy script — cạnh **vào** CE18 cũng sai cùng kiểu: `CH09-CE19-03` Marx ← Smith · `trực tiếp` (−28 năm), `CH09-CE19-09` Bolívar ← Rousseau · `trực tiếp` (−5 năm), `CH10-CE20-04` Keynes ← Smith · `trực tiếp` (−93 năm). Chuyển cho reviewer ch09/ch10.

43. **NÊN** — Thiên lệch "cách mạng Đại Tây Dương": Cách mạng Haiti (1791–1804) **không có mặt ở đâu trong CE18** — không trong Bối cảnh, không trong mục nào, không trong Ghi chú. Toussaint Louverture (1743–1803, hoạt động 1791–1803, tức gần trọn trong CE18) chỉ được nêu làm ứng viên bị loại ở **CH09 (CE19)**, mục Bolívar — tức bị xét ở nhóm mà quy tắc chọn số 3 (xếp theo giai đoạn ảnh hưởng chính) lẽ ra không đặt ông vào. Kết quả: cuộc cách mạng nô lệ thành công duy nhất rơi vào khe giữa hai nhóm. Trong khi đó CE18 có Franklin cho cách mạng Mỹ và ba mục Pháp cho Cách mạng Pháp (qua "Ảnh hưởng tới").
   → Tối thiểu: thêm câu Haiti vào Bối cảnh (B2) và một khối Ghi chú: *"**Toussaint Louverture và Cách mạng Haiti.** Giai đoạn ảnh hưởng chính của ông (1791–1803) thuộc CE18, nên ông phải được xét ở nhóm này, không phải ở CH09. Lần soạn này không xét ông; vòng sau cần cân ông với Franklin (ô Châu Mỹ) hoặc với Túpac Amaru II."*

44. **NÊN** — Ghi chú biên tập, khối Equiano: *"Trường `vùng` của mục này ghi `Châu Phi hạ Sahara` theo lời kể trong chính *The Interesting Narrative*… Hai khả năng dẫn tới hai ô vùng khác nhau… nếu vòng sau muốn chặt hơn thì cách đúng là thêm một trường ghi độ tin cậy của `vùng`."* Khối này **đã lỗi thời và lập luận theo nơi sinh**, trái quy ước `vùng` ghi trong CONTRIBUTING ngày 2026-11-03 ("Nơi sinh một mình không quyết định"; Equiano giữ `Châu Phi hạ Sahara` **theo khoản 2** — chất liệu và thẩm quyền của sách là gốc gác châu Phi và chuyến tàu nô lệ). Theo quy ước ấy, tranh cãi nơi sinh **không** còn đổi ô vùng, nên câu "một dòng thống kê vùng đang phụ thuộc vào một tranh cãi chưa khép" không còn đúng.
   → Sửa: *"**`CH08-CE18-11` Equiano: ô vùng không phụ thuộc vào tranh cãi nơi sinh.** Hồ sơ rửa tội 1759 và sổ hải quân ghi South Carolina (Carretta), sách ghi vùng Igbo. Theo quy ước `vùng` (CONTRIBUTING), ô này đo nơi công trình gắn vào: *The Interesting Narrative* lấy thẩm quyền từ gốc gác châu Phi và chuyến tàu nô lệ, nên giữ `Châu Phi hạ Sahara` theo khoản 2 dù nơi sinh thật là đâu. Tranh cãi nơi sinh được ghi ở thân mục và qua mức `Trung bình` của niên đại."* (CÂN NHẮC kèm theo: phần lớn sách kể Caribe, Bắc Mỹ, hải quân và London; áp khoản 2 là phán đoán có thể cãi — nên nói rõ là phán đoán.)

45. **NÊN** — Ghi chú biên tập, khối "Ô Châu Âu 10/24": con số 10/24 **đúng** (đếm `persons.json`). Nhưng câu *"`CH08-CE18-06` Đới Chấn và `CH08-CE18-07` Sugita Genpaku đều là ca đặt quan sát lên trên thẩm quyền văn bản"* sai với Đới Chấn: khảo chứng đặt **chứng cứ ngữ văn kiểm chứng được** (âm vận, huấn hỗ, văn bản cổ hơn) lên trên **thẩm quyền chú giải**, chứ không đặt quan sát lên trên văn bản — chính thân mục #06 nói "một phương pháp ngữ văn". Gộp hai ca làm một là đúng cái "xếp vào khuôn châu Âu" mà khối này tuyên bố tránh.
   → Sửa: *"…`CH08-CE18-07` Sugita Genpaku đặt quan sát lên trên thẩm quyền văn bản; `CH08-CE18-06` Đới Chấn đặt chứng cứ ngữ văn kiểm chứng được lên trên thẩm quyền chú giải — hai lối phê phán thẩm quyền song song với mạch châu Âu, không phải bản sao của nó."*

46. **NÊN** — Ghi chú biên tập, khối Ứng viên Việt Nam: *"Ca đáng cân nhất vòng này là **Lê Quý Đôn** … nhóm CE17 nhận `CH08-CE17-07` Kâtip Çelebi…"*. Lê Quý Đôn (1726–1784) thuộc CE18, còn Kâtip Çelebi (1609–1657) thuộc CE17 — hai người **không cùng thời** và không thể tranh cùng một suất (tinh thần quy tắc 5). Nếu Lê Quý Đôn được cân cho mạch chính thì đối thủ của ông là các mục CE18, gần nhất là `CH08-CE18-06` Đới Chấn (cùng không khí khảo chứng–bách khoa, và ông đi sứ Thanh 1760–62). Phép so với Kâtip Çelebi chỉ là so khuôn, nên nói rõ như vậy.
   → Sửa: *"…Lê Quý Đôn với *Vân đài loại ngữ* và *Phủ biên tạp lục* hợp khuôn bách khoa thư của Kâtip Çelebi (CE17), nhưng suất ông thật sự tranh là ở CE18, cạnh Đới Chấn. Chỗ tách ra là độ phủ của đường truyền: khảo chứng học của Đới Chấn định hình ngữ văn học Trung Hoa, còn trước tác của Lê Quý Đôn gần như không rời khỏi Việt Nam trước thế kỷ 20."*

47. **CÂN NHẮC** — Độ phủ: CE18 có 6 vùng (Châu Âu 5, Đông Á 2, Châu Mỹ 2, Nam Á 1, Trung Đông/Bắc Phi 1, Châu Phi hạ Sahara 1) và 9 lĩnh vực (Triết học 6, Chính trị/Nhà nước 4, Văn học 2, KHTN 2, Ngôn ngữ học 2, Tôn giáo 2, Kinh tế, Y học, Quân sự) → qua ngưỡng ≥4 lĩnh vực, ≥3 vùng. Khoảng trống không được nói ra:
   - **0/12 nữ**; phụ nữ chỉ hiện ra như trợ lý (Marie-Anne Paulze) hoặc ứng viên bị loại vì "gắn với chồng" (Micaela Bastidas). Mary Wollstonecraft (*A Vindication of the Rights of Woman*, 1792) và Émilie du Châtelet (bản dịch–chú giải *Principia*, 1749/1759) không được xét ở đâu (cả hai không có trong `persons.json`).
   - **Thế giới Ottoman / Iran / Trung Á** trống ở CE18 dù có ứng viên rõ: İbrahim Müteferrika (xưởng in chữ Ả Rập đầu tiên ở Istanbul, 1727) — không có trong atlas.
   - **Đông Nam Á** chỉ có qua phụ lục Việt Nam.
   Không có quy tắc nào bắt phải có, nhưng Ghi chú nên nói ra các khoảng trống này như khối Châu Âu đã làm cho tỉ lệ châu Âu.

48. **CÂN NHẮC** — Tên gốc trong ngoặc: *"Rousseau (Ioannes-Iacobus Rousseau)"*, *"Adam Smith (Adamus Smith)"* trông như dạng Latinh sinh ra chứ không phải dạng tên có thật được dùng trong tư liệu; CONTRIBUTING: *"đừng bịa một dạng Latinh … chỉ để lint im."* Cache Q6527 có alias "Citizen of Geneva", Q9381 không có alias. `[KHÔNG KIỂM ĐƯỢC]` dạng Latinh này có xuất hiện trong bản in thế kỷ 18 hay không. Đề nghị dùng dạng chắc chắn có thật: *"Jean-Jacques Rousseau (Citoyen de Genève)"*, *"Adam Smith"* (bỏ ngoặc nếu lint đã khớp nhãn en). "Emmanuel Kant" là dạng Pháp có thật — giữ.

---

## Bảng tổng hợp theo mức

| Mức | Số | Mục |
|---|---|---|
| **BẮT BUỘC** | 10 | #1, #2 (CE18-01) · #4 (CE18-02/-03) · #7, #8, #9 (CE18-03) · #27 (CE18-10) · #32, #33 (CE18-11) · #41 (Ghi chú) |
| **NÊN** | 17 | B1, B2 (Bối cảnh) · #11, #12 (CE18-04) · #14 (CE18-05) · #17 (CE18-06) · #20 (CE18-07) · #22 (CE18-08) · #28 (CE18-10) · #34 (CE18-11) · #35, #36 (CE18-12) · #42, #43, #44, #45, #46 (chapter) |
| **CÂN NHẮC** | 24 | B3 · #3, #5, #6, #10, #13, #15, #16, #18, #19, #21, #23, #24, #25, #26, #29, #30, #31, #37, #38, #39, #40, #47, #48 |
| **[KHÔNG KIỂM ĐƯỢC]** | 2 | ngày chính xác lệnh cấm *Comentarios Reales* (#30); dạng tên Latinh của Rousseau/Smith (#48) |

## Danh sách BẮT BUỘC

1. **CH08-CE18-01** Kế thừa: `CH08-CE17-05 · kế thừa · trực tiếp` → `qua trường phái` (Locke–Voltaire, không tiếp xúc; Voltaire 10 tuổi khi Locke mất).
2. **CH08-CE18-01** Tư tưởng: *Traité sur la tolérance* (1763) bị kể như viết **sau** khi án Calas huỷ (1765) — sai trình tự.
3. **CH08-CE18-02 / -03** `Rousseau ↔ Kant · trực tiếp` → `qua trường phái` (không gặp, không thư).
4. **CH08-CE18-03** Kế thừa: `CH08-CE17-03 · kế thừa · trực tiếp` → `qua trường phái` (Newton–Kant chồng đời 3 năm).
5. **CH08-CE18-03** Kế thừa: `David Hume · phản bác · trực tiếp` → `qua trường phái`.
6. **CH08-CE18-03** Ảnh hưởng tới: đích là chính tác phẩm của Kant (*Zum ewigen Frieden*) — sai loại; `suy đoán học giả` không nêu của ai.
7. **CH08-CE18-10** Kế thừa: `CH07-CE16-12 · kế thừa · trực tiếp` → `qua trường phái` (khoảng cách −122 năm; sửa cả cạnh ngược ở ch07).
8. **CH08-CE18-11** Tư tưởng: "trước đó chỉ có người da trắng nói" — sai (Hammon 1760, Gronniosaw 1772, Wheatley 1773, Sancho 1782, Cugoano 1787) và tự mâu thuẫn với "Vì sao chọn".
9. **CH08-CE18-11** Vì sao chọn: Cugoano "không được tái bản" — sai (bản Pháp 1788, bản rút gọn 1791; SEP "Ottobah Cugoano").
10. **Ghi chú biên tập** khối "Mức `trực tiếp` dùng cho đường truyền qua văn bản…" trái định nghĩa CONTRIBUTING và là gốc của các lỗi 1, 4, 5, 7.

## Nguồn tra cứu đã dùng
- https://plato.stanford.edu/entries/cugoano/
- https://en.wikipedia.org/wiki/T%C3%BApac_Amaru_II
- https://en.wikipedia.org/wiki/Experiments_and_Observations_on_Electricity
- https://www.abebooks.com/9780631178873/Antoine-Lavoisier-Science-Administration-Revolution-0631178872/plp ; https://www.thenile.co.nz/books/arthur-donovan/antoine-lavoisier-science-administration-and-revolution/9780521566728
- https://www.cambridge.org/core/journals/journal-of-asian-studies/article/from-philosophy-to-philology-intellectual-and-social-aspects-of-change-in-late-imperial-china-by-benjamin-a-elman-cambridge-mass-harvard-university-council-on-east-asian-studies-1984-harvard-east-asian-monographs-110-xxv-368-pp-maps-illustrations-notes-bibliography-glossary-index-2000/46D56492BD5938BDC194A5692B1681E3
- https://ci.nii.ac.jp/ncid/BA46450789 ; https://cambridge.org/core/journals/journal-of-asian-studies/article/abs/japan-and-the-dutch-by-grant-k-goodman-richmond-surrey-curzon-2000-304-pp-4000/11F900D872B35F29E1F70964986FA65A
