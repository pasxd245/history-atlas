# Patch ch09 theo review — ghi chú

Nguồn review: `rv/review-ch09.md`, "Danh sách BẮT BUỘC" (11 mục). Chỉ sửa `content/ch09.md`. Bỏ qua mọi mục NÊN / CÂN NHẮC / [KHÔNG KIỂM ĐƯỢC] (quyết định của owner). Bản trước khi sửa lưu ở `rv/ch09.before.md`.

## Các mục BẮT BUỘC

| # | Review | Mục | Trường | Trước | Sau | Kết quả |
|---|---|---|---|---|---|---|
| 1 | 01-1 | CH09-CE19-01 Faraday | Tư tưởng | "Maxwell về sau viết hình dung ấy thành bốn phương trình." | "Maxwell về sau toán học hoá hình dung ấy (1861–1865); dạng bốn phương trình quen thuộc ngày nay là do Heaviside rút gọn lại." | Đã áp dụng (đúng chữ reviewer). 100 → 113 chữ, trong ngưỡng lint. |
| 2 | 02-1 | CH09-CE19-02 Darwin | Kế thừa | `Thomas Robert Malthus · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` | Đã áp dụng. |
| 3 | 03-1 | CH09-CE19-03 Marx | Kế thừa | `CH08-CE18-04 · phản bác · trực tiếp` | `CH08-CE18-04 · phản bác · qua trường phái` | Đã áp dụng. Giữ `phản bác`; gợi ý đổi sang `tổng hợp` chỉ là "cân nhắc" nên để owner quyết. |
| 4 | 03-2 | CH09-CE19-03 Marx | Kế thừa | `David Ricardo · kế thừa · trực tiếp` | `… · kế thừa · qua trường phái` | Đã áp dụng. |
| 5 | 03-3 | CH09-CE19-03 Marx | Kế thừa | `Georg Wilhelm Friedrich Hegel · phản bác · trực tiếp` | `… · tổng hợp · qua trường phái` | Đã áp dụng (đúng đề xuất trong danh sách BẮT BUỘC; `tổng hợp` có trong RELATION_TYPES). |
| 6 | 04-1 | CH09-CE19-04 Pasteur | Tư tưởng | "Bình cổ ngỗng của ông (1859–1864) kết thúc… Từ đó ra chuỗi hệ quả: lên men là việc của vi sinh vật, bệnh truyền nhiễm cũng vậy…" | "Sau khi các nghiên cứu lên men (từ 1857) cho thấy lên men là việc của vi sinh vật, bình cổ ngỗng của ông (1859–1864) kết thúc… Từ đó ra chuỗi hệ quả: bệnh truyền nhiễm cũng do vi sinh vật…" | Điều chỉnh. Đề xuất của reviewer viết lại cả hai câu đầu: bỏ phần giải thích cơ chế bình cổ ngỗng và đổi niên đại 1859–1864 thành 1859–1862 — niên đại không bị gắn BẮT BUỘC. Bản sửa chỉ đảo trình tự (lên men trước, bình cổ ngỗng sau), giữ nguyên phần còn lại. "kết thúc tranh cãi" là mục NÊN 04-2, không đụng. 107 → 121 chữ. |
| 7 | 05-1 | CH09-CE19-05 Muhammad Ali | Tư tưởng + Nguồn | "Rồi công ước Luân Đôn năm 1840, do các cường quốc châu Âu áp đặt, buộc ông bỏ độc quyền và cắt quân số"; Nguồn "Công ước Luân Đôn (1840)." | "Rồi châu Âu can thiệp: Công ước Luân Đôn (1840) buộc ông rút khỏi Syria; firman năm 1841 giới hạn quân ông ở mười tám nghìn, và hiệp ước Balta Liman (1838) áp cho Ai Cập xoá độc quyền"; Nguồn "Công ước Luân Đôn (1840) và firman 1841." | Điều chỉnh. Giữ đủ ba ý của reviewer nhưng rút gọn câu chữ: bản đề xuất nguyên văn đưa mục lên 131 chữ và sinh WARN mới (lệch > 30% so với ~100). Bản rút gọn: 104 → 119 chữ, không còn WARN. "phần lớn cơ sở công nghiệp sụp theo" giữ nguyên (mục NÊN 05-3). Nguồn đổi đúng đề xuất. |
| 8 | 07-1 | CH09-CE19-07 Ram Mohan Roy | Tư tưởng | "nhất thần không tượng, không đẳng cấp." | "nhất thần, không tượng, dựa trên Upanishad." | Đã áp dụng (khớp cạnh Kế thừa "các Upanishad ông tự dịch" có sẵn). |
| 9 | 09-1 | CH09-CE19-09 Bolívar | Kế thừa | `CH08-CE18-02 · kế thừa · trực tiếp` | `CH08-CE18-02 · kế thừa · qua trường phái` | Đã áp dụng. |
| 10 | 10-1 | CH09-CE19-10 Rizal | Tư tưởng | "bản án tử hình năm 1896 châm ngòi cho cách mạng." | "bản án tử hình cuối năm 1896, khi khởi nghĩa đã nổ ra bốn tháng, biến ông thành biểu tượng của nó." | Đã áp dụng (đúng chữ reviewer). 106 → 117 chữ. |
| 11 | 10-2 | CH09-CE19-10 Rizal | Kế thừa | `Antonio de Morga · phản bác · trực tiếp` | `… · phản bác · qua trường phái` | Đã áp dụng. |

Tổng: **9 áp dụng nguyên văn · 2 điều chỉnh (#6, #7) · 0 không áp dụng.**

## Cạnh đối xứng ở chapter khác

Không có. Đã grep `content/*.md`: `ch08.md` (CH08-CE18-02 Rousseau, CH08-CE18-04 Smith) không có dòng "Ảnh hưởng tới" nào trỏ `CH09-CE19-03` hay `CH09-CE19-09`, cũng không nhắc Marx/Bolívar bằng tên. Malthus, Ricardo, Hegel, Morga không có mục riêng (đích văn bản tự do). Các dòng ở `ch10.md`/`ch11.md` trỏ vào CH09 đều là `qua trường phái` và không phải cạnh đối xứng của các cạnh đã sửa. Trong ch09 cũng không có cạnh đối xứng nào phải sửa theo.

## Lint (`python3 build.py --offline --lint-only`)

- Trước: `Lint: 0 lỗi · 6 cảnh báo · 287 ghi chú` — WARN của ch09: chỉ `CH09-CE19-01: thiếu tên gốc trong ngoặc` (đã biết, có giải thích trong Ghi chú biên tập).
- Sau: `Lint: 0 lỗi · 8 cảnh báo · 287 ghi chú` — WARN của ch09: vẫn chỉ `CH09-CE19-01`. Hai WARN mới là `ch10/CH10-CE20-02` và `ch10/CH10-CE20-09` ('why' quá dài): chúng đến từ ch10.md, file này không đụng tới, và xuất hiện trong lúc chạy (có thể do một lượt sửa ch10 chạy song song).
