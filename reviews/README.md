# reviews/ — hồ sơ cổng và báo cáo bình duyệt

Thư mục này **có version-control**. Nó chứa thứ không máy nào sinh lại được:
hồ sơ cổng tuyển chọn, báo cáo của các vòng bình duyệt độc lập, dossier ứng
viên, và các patch viết tay.

Phân biệt với `reports/`, vốn nằm trong `.gitignore`:

| | `reports/` | `reviews/` |
|---|---|---|
| Ai sinh ra | `build.py`, `fetch_images.py` | người và agent bình duyệt |
| Chạy lại có ra y hệt không | có | không |
| Trong git | không | có |

Lý do tách: `.gitignore` trước đây bọc cả `reports/` với chú thích "báo cáo
sinh ra mỗi lần build". Chú thích ấy mô tả đúng mười file `.txt` nhưng bọc
nhầm 57 file `.md` viết tay. Hệ quả cụ thể: `ch05-ce08-review-2.md` là bằng
chứng duy nhất cho việc vòng bình duyệt thứ nhất đã ký ✓ cho ba mệnh đề sai,
và nó chỉ tồn tại trên một ổ đĩa.

## Đọc hồ sơ cũ

Báo cáo viết trước lần tách này trỏ tới nhau bằng đường dẫn `reports/...`.
Những dòng đó **cố ý không sửa**: báo cáo bình duyệt là bản ghi có thời điểm,
sửa đường dẫn bên trong là sửa bản ghi. Khi đọc, cứ đổi `reports/` thành
`reviews/` cho mọi file `.md` và `.json`.

## Quy ước

- Một vòng bình duyệt một file. Không ghi đè file cũ; vòng hai đặt tên
  `-review-2.md` để còn đối chiếu được vòng một đã bỏ sót gì.
- Ba ràng buộc cho agent bình duyệt: không spawn sub-agent, ghi tăng dần bằng
  `cat >>`, và nói thẳng `[KHÔNG KIỂM ĐƯỢC]` khi không xác minh được.
- Bốn mức kết luận: **BẮT BUỘC** · **NÊN** · **CÂN NHẮC** · **[KHÔNG KIỂM ĐƯỢC]**.
- UA trung lập `history-atlas/0.1 (research)`. Không để thông tin cá nhân vào
  header, URL, payload hay báo cáo.

## Lịch sử git đã được viết lại một lần (2026-11-03)

`atlaslib/common.py` từng đặt User-Agent mặc định kèm địa chỉ email và tên
miền nơi làm việc của Chủ dự án, nên mọi lần `build.py` chạy online đều gửi
chuỗi ấy tới Wikidata. Hồ sơ cổng CE08 (`ch05-ce08-gate.md`) đã nêu từ vòng
CE08; chuỗi được sửa ở HEAD trước, rồi gỡ khỏi toàn bộ lịch sử sau.

Thao tác: `git filter-branch --index-filter` trên cả hai nhánh, thay
`(personal research project; <email>)` thành `(personal research project)`
trong 8 phiên bản của đúng một file. Không file nào khác chứa chuỗi ấy, và
nó không có trong bất kỳ commit message nào. Author/committer của mọi commit
là một địa chỉ khác, không bị đụng tới.

Kết quả kiểm: cây HEAD **không đổi** (`7028460`), 83 commit giữ nguyên, quét
mọi blob còn sống và mọi object mồ côi đều không còn chuỗi ấy.

Hệ quả phải biết:

- **Mọi hash commit đã đổi.** Bất kỳ ghi chú nào trỏ tới hash trước
  2026-11-03 đều không còn giải ra được. Các báo cáo trong thư mục này trỏ
  tới nhau bằng tên file và số dòng, không bằng hash, nên không bị ảnh hưởng.
- **Bản bundle sao lưu và mọi clone cũ VẪN CÒN email.** Bundle nằm ở
  `../history-atlas-backup-20261103-*.bundle`, cố ý giữ lại làm đường lùi.
  Khi đã chắc không cần lùi nữa thì xoá nó, nếu không thì việc gỡ coi như
  chưa trọn.
