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
