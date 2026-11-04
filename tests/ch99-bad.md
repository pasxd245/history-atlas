# Chapter 2 · Test case lint — file này CỐ TÌNH SAI (không nằm trong content/)
**Giới thiệu chapter (≤ 100 chữ):** File kiểm thử: mỗi nhân vật cài một hoặc nhiều lỗi để chắc rằng lint bắt được. Chạy `python build.py --lint-only tests/ch99-bad.md` — kỳ vọng mã thoát 1 và danh sách lỗi dưới đây.

## Nhóm BCE06 · TK 6 TCN (600 – 501 TCN)
**Bối cảnh (≤ 60 chữ):** Nhóm hợp lệ nhưng chứa 14 mục (13 ID + 1 ID trùng), vượt trần 12 và nhiều lỗi metadata.

### CH02-BCE06-01 · Người A (A)
`năm: 551–479 TCN | nơi: X | vùng: Đông Á | lĩnh vực: Triết học | độ tin cậy niên đại: Cao | wikidata: Q4604 | câu hỏi lớn: Con người`

**Tư tưởng / đóng góp chính (~100 chữ):** Hợp lệ. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum sed ut perspiciatis.

**Vì sao chọn (~80 chữ):** Hợp lệ. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa.

**Kế thừa từ:**
- Không xác định

**Ảnh hưởng tới:**
- CH02-BCE06-01 · kế thừa · trực tiếp

**Nguồn:** test.

### CH02-BCE06-02 · Người B (B)
`năm: 600–550 TCN | nơi: X | vùng: Châu Á | lĩnh vực: Thiên văn, Triết học, Toán học | độ tin cậy niên đại: Khá | wikidata: 4604 | câu hỏi lớn: Vũ trụ, Con người, Thực tại`

**Tư tưởng / đóng góp chính (~100 chữ):** Quá ngắn.

**Vì sao chọn (~80 chữ):** Quá ngắn.

**Kế thừa từ:**
- Người A · bắt chước · nghe nói

**Ảnh hưởng tới:**
- CH02-BCE06-01 · kế thừa · trực tiếp

**Nguồn:** test.

### CH03-BCE05-03 · Người C (C)
`năm: 500–520 TCN | nơi: X | vùng: Châu Âu | lĩnh vực: Triết học | wikidata: ? | câu hỏi lớn: Con người`

**Tư tưởng / đóng góp chính (~100 chữ):** Thiếu độ tin cậy; ID mang sai chapter và sai nhóm; năm mất 520 TCN sớm hơn năm sinh 500 TCN → lỗi; thiếu Ảnh hưởng tới. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat.

**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.

**Kế thừa từ:**
- Không xác định

**Nguồn:** test.

### CH02-BCE06-04 · Người D
**Tư tưởng / đóng góp chính (~100 chữ):** Thiếu dòng metadata, thiếu tên gốc, thiếu Vì sao chọn, thiếu Ảnh hưởng tới và Nguồn.

### CH02-BCE06-05 · E (E)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Tôn giáo/Tâm linh | độ tin cậy niên đại: Cao | wikidata: Q9441 | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Trùng ID với nhân vật bên dưới. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-05 · E bis (E)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Tôn giáo/Tâm linh | độ tin cậy niên đại: Cao | wikidata: Q9441 | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Trùng ID. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-06 · F (F)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Y học | độ tin cậy niên đại: Cao | wikidata: Q868 | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Wikidata Q868 là Aristotle (384–322 TCN) — lint online phải cảnh báo lệch niên đại và nhãn không khớp. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-07 · G (G)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Đệm cho đủ 13 người. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-08 · H (H)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Đệm. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-09 · I (I)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Đệm. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-10 · J (J)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Đệm. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-11 · K (K)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Đệm. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-12 · L (L)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Đệm. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

### CH02-BCE06-13 · M (M)
`năm: 560–480 TCN | nơi: X | vùng: Nam Á | lĩnh vực: Luật | độ tin cậy niên đại: Cao | wikidata: ? | câu hỏi lớn: Con người`
**Tư tưởng / đóng góp chính (~100 chữ):** Người thứ 13 → nhóm vượt trần 12 (PROJECT max_per_group). Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat.
**Vì sao chọn (~80 chữ):** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur sunt in culpa qui.
**Kế thừa từ:**
- Không xác định
**Ảnh hưởng tới:**
- Không xác định
**Nguồn:** test.

## Nhóm CE05 · TK 5 (401 – 500)
**Bối cảnh (≤ 60 chữ):** Nhóm này không thuộc chapter 2 → lỗi.
