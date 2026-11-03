# Rà soát liêm chính học thuật & bản quyền — history-atlas

Phạm vi: toàn bộ file trên đĩa tại gốc repo (bản dựng P1: `content/ch02.md`, `content/ch90.md`, 56 ảnh đã nhúng).
Ngày rà: 2026-10-30. Người rà: không phải luật sư — tài liệu này chỉ đọc đúng những gì **văn bản giấy phép nói thẳng ra**, không suy diễn pháp lý.

---

## 0. Quy ước mức độ & tóm tắt

| Mức | Nghĩa |
|---|---|
| **bắt buộc** | Điều kiện của một giấy phép đang dùng, hoặc một tuyên bố mà nếu thiếu thì người đọc có thể hiểu sai bản chất tác phẩm. |
| **nên làm** | Thông lệ tốt, giảm rủi ro và tăng độ tin cậy. Không làm cũng không vi phạm gì. |
| **tuỳ chọn** | Cải thiện chất lượng, làm khi rảnh. |

### Danh sách "bắt buộc"

| # | Mục | Gap một dòng |
|---|---|---|
| B1 | §1.3 | Chưa có tuyên bố giấy phép cho chính dự án → không rõ điều khoản nào đang áp lên ảnh CC BY-SA đã nhúng. |
| B2 | §1.4 | `fetch_images.py`: nhánh dự phòng (khi Commons API 429) **vẫn nhúng ảnh** dù không kiểm tra được trường `Restrictions`. Dữ liệu hiện tại an toàn, nhưng sẽ vỡ khi sản xuất Ch1, Ch3–Ch11. |
| B3 | §2.2 | `assets/LICENSE-mermaid.txt` chỉ có thông báo MIT của Knut Sveidqvist; bundle 2,5 MB còn gói DOMPurify, Cytoscape, dagre, lodash, marked, Langium, uuid… mà thông báo bản quyền của chúng không được kèm theo. |
| B4 | §3 | **Trang web không nói ở đâu rằng phần văn xuôi do model viết.** Chỉ `README.md` có một mệnh đề, mà README không được xuất bản. |
| B5 | §4 | Chưa có tuyên bố giới hạn học thuật ở cấp trang (tiêu chí lựa chọn là phán đoán biên tập, không phải xếp hạng khách quan). |

Điểm tốt đã có sẵn, không cần sửa: ghi công ảnh trên trang chapter **đã đủ 5 yếu tố** của CC BY-SA; Wikidata CC0 đã được ghi ở footer mọi trang; `assets/LICENSE-d3.txt` đã đúng và đủ; `## Ghi chú biên tập` ở cả `ch02.md` và `ch90.md` đã tự bạch rất thẳng thắn về lựa chọn, niên đại và tranh luận sử học.

> ### ⚠ Lưu ý kỹ thuật quan trọng trước khi dán bất kỳ khối text nào
> `index.html`, `overview.html`, `credits.html`, `chapters/*.html` **đều do `build.py` sinh ra và sẽ bị ghi đè**. Không sửa tay. Mọi text hiển thị trên web phải dán vào `atlaslib/render.py` (hàm `footer()`, `render_overview()`, `render_credits()`) rồi chạy lại `python build.py`. Chỉ `README.md`, `LICENSE`, `CONTRIBUTING.md`, `content/*.md`, `assets/*.txt` là file viết tay.

---

## 1. Ghi công & tuân thủ giấy phép ảnh

### 1.1 Hiện trạng đo được

56 ảnh nhúng, tất cả lấy qua đường API (`via: api` — nghĩa là trường `Restrictions` **đã** được kiểm tra cho toàn bộ dữ liệu hiện có):

| Giấy phép | Số ảnh |
|---|---|
| Public domain | 31 |
| CC BY-SA 3.0 | 12 |
| CC BY-SA 4.0 | 6 |
| CC BY-SA 2.0 | 3 |
| CC BY 3.0 | 2 |
| CC0 | 2 |

23 ảnh thuộc nhóm CC BY / CC BY-SA. Kiểm tra `data/images.json`: **23/23 có `author` và 23/23 có `license_url`**. 3 ảnh bị giữ lại ở trạng thái `review` (`ita-mibac`; `personality|communist`; `communist`), 1 ảnh bị loại vì GFDL-only. Chính sách trong `fetch_images.py` chạy đúng như mô tả.

### 1.2 CC BY-SA đòi gì, và dự án có làm đủ không — **Kết luận: ĐỦ**

CC BY-SA 4.0 §3(a)(1) và CC BY-SA 3.0 §4(c) yêu cầu, khi phân phối tác phẩm:

| Yêu cầu của giấy phép | Trang chapter có? | Bằng chứng |
|---|---|---|
| Tên tác giả / bên được ghi công | ✔ | `figure_html()` in `im["author"]` |
| Tên giấy phép | ✔ | `im["license"]` |
| Liên kết tới văn bản giấy phép | ✔ | `<a href="{license_url}">` |
| Liên kết tới tệp gốc | ✔ | `<a href="{source_url}">Wikimedia Commons</a>` → trang `File:` |
| Nêu rõ đã sửa đổi | ✔ | `", đã thu nhỏ"` khi `attribution_required` |
| Giữ thông báo bản quyền / miễn trừ bảo hành gốc | ✔ (gián tiếp) | CC 4.0 §3(a)(2) cho phép thoả mãn bằng **một liên kết tới nguồn chứa các thông tin đó** — chính là link trang `File:` |

Ví dụ thật đang hiển thị trên `chapters/ch02.html`:

> Ảnh: *Wikimedia Commons*, எஸ். பி. கிருஷ்ணமூர்த்தி, *CC BY-SA 3.0*, đã thu nhỏ.

→ Đây là ghi công hợp lệ. Không có gap bắt buộc nào ở phần hiển thị.

### 1.3 ShareAlike — nói chính xác điều khoản copyleft có và KHÔNG có nghĩa gì

**Không có nghĩa gì.** ShareAlike chỉ kích hoạt với *Adapted Material* (CC 4.0 §3(b)) / *Derivative Works* (CC 3.0 §4(b)). Hai điểm văn bản giấy phép nói thẳng:

1. **Thu nhỏ ảnh không tạo ra tác phẩm phái sinh.** CC BY-SA 4.0 §2(a)(4) ("Media and formats; technical modifications allowed") nói rõ các sửa đổi kỹ thuật *không bao giờ* tạo ra Adapted Material. Thumbnail 500px trong `assets/img/` vẫn là bản sao của tác phẩm gốc, vẫn mang đúng giấy phép gốc. (Việc ghi "đã thu nhỏ" vẫn nên giữ — vô hại và minh bạch.)
2. **Đặt ảnh CC BY-SA cạnh văn xuôi tự viết không làm văn xuôi đó thành CC BY-SA.** Đó là một *Collection* theo định nghĩa của giấy phép, không phải tác phẩm phái sinh. → **Văn xuôi `content/*.md` của dự án KHÔNG bị ràng buộc phải mang CC BY-SA.** Nếu có ai nói ngược lại, đó là hiểu sai.

**Có nghĩa gì — và đây là lý do bắt buộc phải có file LICENSE (B1).** CC BY-SA 4.0 §2(a)(5)(B) và §3(a)(4) cấm áp thêm điều khoản hạn chế lên tác phẩm được cấp phép ("no downstream restrictions"). Hệ quả thực tế:

- Một dòng `© 2026 … All rights reserved` phủ toàn site, **hoặc** một giấy phép site-wide kiểu CC BY-NC, sẽ mâu thuẫn với 23 ảnh CC BY/CC BY-SA đang nhúng.
- Hiện tại site **không có tuyên bố giấy phép nào cả**. Không có tuyên bố thì mặc định pháp luật là "bảo lưu mọi quyền" — tức là tình trạng mơ hồ đúng kiểu điều khoản trên muốn tránh.
- Cách sửa: tuyên bố giấy phép **theo từng thành phần** (code / văn xuôi / dữ liệu / ảnh), và nói rõ ảnh giữ nguyên giấy phép riêng của chúng, liệt kê ở `credits.html`. Xem §6.

**Quy tắc hướng tới tương lai** (đưa vào CONTRIBUTING): nếu ai đó **cắt cúp, ghép, tô màu, lồng chữ** lên một ảnh CC BY-SA — lúc đó mới là Adapted Material, và **ảnh kết quả bắt buộc phải phát hành dưới đúng giấy phép đó (hoặc tương thích)**. Áp dụng cho cả ảnh ghép/montage có thể sinh ra ở P5 (graph D3, bản đồ).

### 1.4 Gap thật trong pipeline ảnh

#### B2 — **bắt buộc** · Nhánh dự phòng nhúng ảnh mà không kiểm tra được `Restrictions`

`fetch_images.py` khi `api.php` trả 429 sẽ chuyển sang `meta_from_html()`. Ở nhánh đó:

- `RESTRICT_HTML_RE` chỉ bắt `Personality rights|Quyền nhân thân|Trademarked|insignia|Freedom of panorama`. **Không bắt `ita-mibac`**, không bắt `communist`, không bắt các template hạn chế khác — đúng hai loại đã khiến 3 ảnh hiện tại bị giữ lại.
- `meta` trả về cờ `restrictions_unverified: True`, nhưng ở `main()` cờ này **chỉ sinh một dòng `[info]` trong `reports/images-review.txt` rồi vẫn tải và nhúng ảnh**.

Dữ liệu hiện tại không bị ảnh hưởng (56/56 đều `via: api`). Nhưng Ch1 và Ch3–Ch11 sẽ fetch hàng trăm ảnh; chỉ cần một đợt 429 là ảnh có `Restrictions` sẽ được nhúng âm thầm — đúng loại ảnh mà chính sách của dự án đã cố ý loại ra.

**Sửa:** trong `main()`, ngay sau khi tính `kind`, nếu `meta.get("restrictions_unverified")` thì chuyển `status` thành `"review"` thay vì nhúng:

```python
if meta.get("restrictions_unverified"):
    rec.update(status="review", license=lic_label,
               note=f"đọc qua fallback (trang File) — KHÔNG kiểm tra được Restrictions; giấy phép: {lic_label}")
    images[pid] = rec
    review.append(f"[review] {pid} {p['name_vi']}: {title} — {rec['note']} → chạy lại khi API Commons trả lời, hoặc quyết định tay")
    stats["review"] += 1
    continue
```

Kèm theo (rẻ, nên làm cùng lúc): bổ sung `ita-mibac|mibac|communist|Nazi symbol|currency|Costume` vào `RESTRICT_HTML_RE`.

#### N1 — **nên làm** · Ảnh CC thiếu tác giả vẫn được nhúng

`figure_html()` có fallback `"không rõ tác giả"`. Với ảnh PD thì vô hại. Với ảnh CC BY/CC BY-SA thì đó là ghi công thiếu yếu tố mà giấy phép đòi. Hiện chỉ 1 ảnh thiếu `author` và nó là Public domain, nên chưa có vấn đề thật. Chặn trước:

```python
if kind == "ccby" and not (meta.get("author") or "").strip():
    rec.update(status="review", license=lic_label,
               note=f"{lic_label} nhưng Commons không có trường Artist → không đủ dữ liệu ghi công")
    ...
    continue
```

#### N2 — **nên làm** · Trường `Attribution` của Commons bị lấy rồi vứt đi

`meta_from_api()` có lấy `Attribution` (chuỗi ghi công mà người tải lên *yêu cầu* dùng) và `AttributionRequired`, nhưng `rec.update(...)` chỉ lưu `author`. CC BY-SA 4.0 §3(a)(1)(A)(i) nói ghi công "in any reasonable manner requested by the Licensor". Khi người cấp phép đã nêu rõ chuỗi mong muốn thì dùng chuỗi đó là cách chắc chắn nhất.

**Sửa:** lưu `attribution=meta.get("attribution", "")` vào `rec`, và trong `figure_html()` / `render_credits()` ưu tiên `im.get("attribution") or im.get("author")`.

#### N3 — **nên làm** · Chuỗi tác giả bị cắt và bị lược thẻ, có bản ghi hỏng

`author=(meta.get("author") or "").strip()[:200]` + `strip_tags()`. Kết quả thực tế trong `data/images.json`:

```
CH90-CE15_18-08  CC BY-SA 3.0  author='Statue_of_Le_Quy_Don.JPG : Amore Mio derivative work: Amore Mio ( talk'
CH02-BCE05-05    CC BY-SA 3.0  author='Original uploader was Odysses'
```

Bản ghi đầu bị cắt giữa chừng và lẫn tên file. Không phải vi phạm (tên tác giả vẫn đọc ra được, và có link về trang `File:`), nhưng là ghi công cẩu thả trên một trang tự nhận là nghiêm túc. Nên: nâng giới hạn lên ~300 ký tự, bỏ tiền tố `"Original uploader was "`, và **giữ lại URL trang người dùng** của tác giả (hiện `strip_tags()` xoá mất) để ghi công có link — CC coi đây là nên, không bắt buộc.

#### N4 — **nên làm** · `credits.html` không nêu "đã thu nhỏ"

Ghi chú chính sách ở đầu `credits.html` hứa *"CC BY / CC BY-SA: nhúng kèm tác giả, tên giấy phép có link, link tệp gốc và ghi chú 'đã thu nhỏ'"*, nhưng bảng bên dưới không có cột/chú thích nào nói ảnh đã bị thu nhỏ (chỉ `figcaption` ở trang chapter có). Ghi công ở trang chapter đã đủ, nên đây là chuyện nhất quán chứ không phải tuân thủ — nhưng `credits.html` là trang ghi công "chính thức", nên sửa.

**Sửa trong `atlaslib/render.py`, hàm `render_credits()`**, cột giấy phép:

```python
{lic}{" <span class=badge>ghi công bắt buộc</span>" if im.get("attribution_required") else ""}{" <span class='small muted'>· đã thu nhỏ</span>" if im.get("attribution_required") else ""}
```

#### T1 — **tuỳ chọn** · `classify_license()` cắt nhãn giấy phép theo `[;/]|\bor\b|\band\b`

Với `"GFDL or CC BY-SA 3.0"` thì cắt đúng (chọn nhánh CC — hợp lệ). Nhưng nhãn có dấu `/` hoặc chữ "and" trong tên bản địa hoá (ví dụ `CC BY-SA 3.0 DE`, hoặc nhãn ghép) có thể bị cắt cụt, làm `license` hiển thị thiếu phiên bản port. Hiện chưa xảy ra. Nếu muốn chắc: so khớp regex phiên bản đầy đủ trước khi cắt.

---

## 2. Mã nguồn bên thứ ba

### 2.1 d3.min.js — **đủ, không cần làm gì**

`assets/d3.min.js` v7.9.0 có đúng một dòng bản quyền (`Copyright 2010-2023 Mike Bostock`), và `assets/LICENSE-d3.txt` chính là văn bản ISC với đúng dòng đó. Đã khớp. ✔

### 2.2 B3 — **bắt buộc** · mermaid.min.js thiếu thông báo của các thư viện được đóng gói kèm

`assets/mermaid.min.js` nặng 2,5 MB và là bundle esbuild. Quét trong file tìm được tên của các thư viện được gói vào: **DOMPurify, Cytoscape, dagre, lodash, marked, Langium, uuid**, cùng ít nhất một thông báo bản quyền còn sót của bên thứ ba (`Copyright (c) 2013-2014 Ralf S. Engelschall`). `assets/LICENSE-mermaid.txt` chỉ chứa thông báo MIT của Knut Sveidqvist (mermaid).

Giấy phép MIT nói thẳng: *"The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."* Mỗi thư viện MIT được gói kèm có thông báo riêng, và thông báo đó phải đi cùng bản phân phối. DOMPurify còn cấp phép theo **Apache-2.0 HOẶC MPL-2.0** — Apache-2.0 §4 có yêu cầu riêng về việc kèm bản giấy phép và file NOTICE.

Repo này commit và phục vụ `mermaid.min.js` → đây là phân phối lại. Rủi ro thực tế rất thấp (không ai kiện vì chuyện này, và bản npm của mermaid cũng không kèm NOTICE tổng hợp), nhưng điều kiện giấy phép thì vẫn là điều kiện, và sửa mất ~15 phút.

**Sửa:** tạo `assets/LICENSE-mermaid-thirdparty.txt` liệt kê các thư viện được đóng gói, giấy phép và link repo của từng cái, kèm **nguyên văn** giấy phép của những cái không phải MIT (DOMPurify Apache-2.0). Rồi nhắc file đó ở `render_credits()`.

> **DÁN VÀO: `assets/LICENSE-mermaid-thirdparty.txt` (file mới)**
>
> ```
> assets/mermaid.min.js là bản dựng gộp (bundle) của Mermaid 11.4.1.
> Giấy phép của chính Mermaid: xem assets/LICENSE-mermaid.txt (MIT, Knut Sveidqvist).
>
> Bản dựng này có gộp kèm mã của các thư viện bên thứ ba dưới đây. Thông báo bản quyền và
> giấy phép của từng thư viện được giữ lại theo yêu cầu của chính giấy phép đó.
>
>   DOMPurify   — Apache-2.0 HOẶC MPL-2.0 — https://github.com/cure53/DOMPurify
>                 (nguyên văn Apache-2.0 kèm bên dưới)
>   Cytoscape.js— MIT  — https://github.com/cytoscape/cytoscape.js
>   dagre / dagre-d3 — MIT — https://github.com/dagrejs/dagre
>   d3          — ISC  — https://github.com/d3/d3   (xem thêm assets/LICENSE-d3.txt)
>   lodash      — MIT  — https://github.com/lodash/lodash
>   marked      — MIT  — https://github.com/markedjs/marked
>   Langium     — MIT  — https://github.com/eclipse-langium/langium
>   uuid        — MIT  — https://github.com/uuidjs/uuid
>
> Danh sách trên lập bằng cách quét chuỗi trong bundle; nếu nâng cấp Mermaid, hãy lập lại danh sách
> từ node_modules của đúng phiên bản (ví dụ bằng `license-checker`) rồi cập nhật file này.
>
> ---------- Apache License 2.0 (áp dụng cho DOMPurify) ----------
> [dán nguyên văn https://www.apache.org/licenses/LICENSE-2.0.txt vào đây]
>
> ---------- MIT License (áp dụng cho các thư viện ghi MIT ở trên) ----------
> [dán nguyên văn giấy phép MIT của từng thư viện, hoặc tối thiểu một bản MIT chung kèm
>  dòng bản quyền của từng tác giả, lấy từ repo tương ứng]
> ```

**Và sửa `atlaslib/render.py`, hàm `render_credits()`**, mục "Thư viện":

> **DÁN VÀO: `atlaslib/render.py` → `render_credits()`, thay dòng `<h2>Thư viện</h2>` hiện có**
>
> ```python
> <h2>Thư viện &amp; dữ liệu bên thứ ba</h2>
> <p class="small">Mermaid 11.4.1 — MIT (<code>assets/LICENSE-mermaid.txt</code>); bản dựng gộp có kèm mã của DOMPurify, Cytoscape, dagre, d3, lodash, marked, Langium, uuid — thông báo giấy phép của các thư viện này ở <code>assets/LICENSE-mermaid-thirdparty.txt</code>.<br>
> D3 7.9.0 — ISC (<code>assets/LICENSE-d3.txt</code>). Python-Markdown — BSD-3-Clause, chỉ dùng lúc build, không phát hành kèm site.<br>
> Dữ liệu danh tính, niên đại và liên kết ảnh (P18/P569/P570) lấy từ <a href="https://www.wikidata.org" rel="noopener">Wikidata</a>, phát hành theo <a href="https://creativecommons.org/publicdomain/zero/1.0/" rel="noopener">CC0 1.0</a> — không bắt buộc ghi công, dự án ghi vì lịch sự.<br>
> Ảnh lấy từ <a href="https://commons.wikimedia.org" rel="noopener">Wikimedia Commons</a>, mỗi ảnh giữ nguyên giấy phép riêng, liệt kê đầy đủ ở bảng trên. Ảnh được tải về <code>assets/img/</code>, không hotlink; mọi truy vấn API đều khai báo User-Agent và giãn cách ≥ 1 giây theo quy tắc sử dụng của Wikimedia.<br>
> Không dùng CDN.</p>
> ```

### 2.3 Wikidata CC0 và Wikimedia — **đã đúng**

- CC0 **không đòi hỏi ghi công gì cả**. Dự án vẫn ghi ở `footer()` trên mọi trang và trong ghi chú của `credits.html`. Đó là lịch sự, và đã đủ. ✔
- Văn bản mô tả trên Commons (bản thân nó là CC BY-SA) **không bị copy vào site**: `meta["description"]` có được lấy nhưng không được lưu vào `rec` và không hiển thị ở đâu. Không phát sinh nghĩa vụ. ✔
- Quy tắc truy cập API của Wikimedia (User-Agent mô tả rõ, giãn cách, tôn trọng `Retry-After`) đã được `atlaslib/common.py: Http` và `PROJECT["user_agent"]` tuân thủ. ✔ Mục §2.2 ở trên đã gộp câu mô tả việc này vào credits.

---

## 3. B4 — **bắt buộc** · Công bố tác giả là model AI

### Hiện trạng

Grep toàn bộ `index.html`, `overview.html`, `credits.html`, `chapters/*.html`: **không có một chữ nào** về việc văn xuôi do model sinh ra. `README.md` có câu *"Nội dung do model viết dưới dạng Markdown theo template cố định"* — nhưng README không nằm trong site, và một người đọc mở `index.html` sẽ không bao giờ thấy nó. Footer chỉ nói *"HTML sinh bởi build.py từ content/*.md"* — câu này mô tả công cụ dựng trang, không mô tả tác giả.

### Mức tối thiểu trung thực

Một tác phẩm tham khảo có dáng vẻ học thuật — có mục nguồn, có ghi chú biên tập, có đối chiếu Wikidata, có mức độ tin cậy niên đại — sẽ được mặc định đọc như công trình của người có chuyên môn. Nó không phải vậy. Mức tối thiểu gồm ba lớp:

1. **Một dòng trên footer của *mọi* trang** — để không trang nào bị chia sẻ lẻ mà mất ngữ cảnh.
2. **Một khối "Về dự án" đầy đủ ở `overview.html`** — đây là trang mặc định mà `index.html` nạp vào iframe, tức là trang đầu tiên người đọc thấy.
3. **Một đoạn chuẩn ở đầu `## Ghi chú biên tập` của mỗi chapter** — để ai mở thẳng một chapter vẫn thấy.

Về mục **Nguồn**: mỗi mục có 1–2 nguồn, nhưng nguồn đó cũng do model liệt kê. Nếu Owner **chưa** tự mở từng nguồn để đối chiếu thì phải nói thẳng — vì trích dẫn sai/ảo là lỗi đã biết của model, và nói "có nguồn" mà không nói "chưa kiểm" là phần dễ gây hiểu lầm nhất của cả dự án. Hai biến thể dưới đây, Owner chọn đúng một.

### Khối dán

> **DÁN VÀO: `atlaslib/render.py` → hàm `footer()`, thêm vào trước `· Ảnh:`** (xuất hiện trên mọi trang)
>
> ```python
> f'Văn bản do mô hình AI (Claude) soạn theo prompt cố định, <a href="{rel}overview.html#ve-du-an">chưa qua bình duyệt chuyên môn</a> · '
> ```

> **DÁN VÀO: `atlaslib/render.py` → hàm `render_overview()`, ngay sau `<header class="chapter-head">…</header>`, trước khối `<div class="note"><p><b>Trạng thái.</b>`**
>
> ```html
> <section class="note" id="ve-du-an">
> <h2>Về dự án — đọc trước khi dùng</h2>
>
> <p><b>Đây là dự án nghiên cứu cá nhân, không phải bách khoa thư.</b> Mục đích là dựng một bản đồ có cấu trúc về dòng chảy tư tưởng để tự học và để thảo luận, không phải để trích dẫn như tài liệu tham khảo học thuật.</p>
>
> <p><b>Phần văn xuôi do mô hình AI viết.</b> Toàn bộ phần "Tư tưởng / đóng góp chính", "Vì sao chọn", phần bối cảnh nhóm, giới thiệu chapter và ghi chú biên tập đều do mô hình ngôn ngữ (Claude của Anthropic) soạn theo một prompt cố định lưu tại <code>prompts/atlas-prompt.md</code>. Không có nhà sử học hay chuyên gia nào viết hoặc bình duyệt những đoạn này. Văn bản là <i>tổng hợp</i> do model thực hiện, không phải nghiên cứu sơ cấp.</p>
>
> <p><b>Phần nào KHÔNG do model quyết định.</b> Tên, năm sinh, năm mất, định danh nhân vật và liên kết ảnh được đối chiếu tự động với <a href="https://www.wikidata.org" rel="noopener">Wikidata</a> (CC0) bằng <code>build.py</code>; chênh lệch niên đại vượt ngưỡng sẽ bị báo lỗi và phải xử lý tay. Ảnh lấy từ Wikimedia Commons theo chính sách giấy phép cứng trong <code>fetch_images.py</code>. Cấu trúc chapter, từ vựng lĩnh vực/vùng/quan hệ, và mọi ngưỡng kiểm tra là do người đặt ra.</p>
>
> <p><b>Về mục "Nguồn".</b> Mỗi nhân vật có 1–2 nguồn tham khảo do model liệt kê. <!-- CHỌN MỘT TRONG HAI CÂU DƯỚI, XOÁ CÂU CÒN LẠI -->
> Các nguồn này <b>chưa được đối chiếu từng mục</b> với bản gốc; hãy coi chúng là điểm khởi đầu để tự kiểm tra, không phải là bằng chứng đã được xác minh.
> <!-- hoặc --> Các nguồn này đã được Owner mở và đối chiếu ở mức tên tài liệu và sự tồn tại; nội dung chi tiết bên trong nguồn chưa được kiểm từng câu.</p>
>
> <p class="small muted">Nếu bạn phát hiện một chi tiết sai, một nguồn không tồn tại, hoặc một quy kết không có cơ sở — xin báo lại. Đó là cách dự án này khá lên.</p>
> </section>
> ```

> **DÁN VÀO: đầu mục `## Ghi chú biên tập` của `content/ch02.md` và `content/ch90.md`** (và mọi chapter sau này — nên đưa luôn vào `prompts/atlas-prompt.md` làm đoạn bắt buộc)
>
> ```markdown
> **Cách chapter này được soạn**
> Phần văn xuôi của chapter do mô hình AI viết theo prompt cố định tại `prompts/atlas-prompt.md`, không qua bình duyệt chuyên môn. Tên, niên đại và định danh được đối chiếu tự động với Wikidata; phần diễn giải, đánh giá ảnh hưởng và lựa chọn nhân vật là tổng hợp của model theo bốn tiêu chí (a)–(d), không phải kết luận của giới nghiên cứu. Xem mục "Về dự án" ở trang Overview để biết giới hạn đầy đủ.
> ```

---

## 4. B5 — **bắt buộc** · Tuyên bố giới hạn học thuật

### Những gì cần nói, và vì sao

| Giới hạn | Vì sao bắt buộc nói | Dự án đã nói ở đâu chưa |
|---|---|---|
| **Lựa chọn là phán đoán biên tập, không phải xếp hạng khách quan** | Tiêu đề *"Những người định hình tư tưởng nhân loại"* + bảng đếm + lưới độ phủ tạo ấn tượng về một bảng xếp hạng có thẩm quyền. Tiêu chí (a)–(d) là một khung do người đặt ra, không phải phép đo. | Chỉ ở `prompts/atlas-prompt.md` (không xuất bản) và rải rác trong "Vì sao chọn". |
| **Trần 10 người/nhóm ép phải loại người xứng đáng** | Đây là ràng buộc kỹ thuật, không phải phán quyết lịch sử. `ch90.md` ghi rõ nhóm CE19_20 "đã chạm trần 10 người" nên loại Huỳnh Thúc Kháng, Phạm Quỳnh, Nguyễn Thái Học… | Có, trong Ghi chú biên tập — nhưng ở cuối trang chapter, không ở cấp site. |
| **Độ sâu nguồn: 1–2 nguồn/mục** | Một mục bách khoa thật có hàng chục. | Chưa nói ở đâu. |
| **Niên đại nhiều mục không chắc** | Đã có cơ chế tốt (`độ tin cậy: Cao/Trung bình/Thấp`, dung sai 5/25 năm, Zarathustra lệch 400+ năm, Đức Phật lệch 80 năm, Tôn Tử niên đại văn bản vs. nhân vật). Cần giải thích huy hiệu "niên đại: Thấp" nghĩa là gì cho người đọc. | Có trong Ghi chú biên tập; không giải thích ở nơi hiển thị huy hiệu. |
| **Rủi ro thiên lệch châu Âu — và cả thiên lệch tư liệu** | Prompt có chỉ thị chống thiên lệch, và `overview.html` đã công bố phân bố theo vùng. Điểm trung thực hơn: nguồn tư liệu *bản thân nó* thiên lệch. Ví dụ hay nhất của chính dự án: văn hoá Đông Sơn có trống đồng Ngọc Lũ nhưng "không để lại tên người nào" → vắng mặt trong atlas không có nghĩa là không có đóng góp. | Có ví dụ cụ thể trong `ch02.md`/`ch90.md`; chưa nêu thành nguyên tắc. |
| **Phụ lục dùng hệ quy chiếu khác** | `ch90.md` đã nói rất rõ và `build.py` đã tách khỏi thống kê. Nhưng người đọc click thẳng vào "VN" ở sidebar sẽ thấy một danh sách trông giống hệt chapter chính. | Có ở intro và Ghi chú biên tập của ch90; **chưa** ở `overview.html` nơi có bảng thống kê. |
| **"Ảnh hưởng" ≠ "công trạng"** | Danh sách có vua chinh phạt, có nhân vật chính trị thế kỷ 20. Không nói rõ thì bị đọc thành bảng vinh danh. | Chưa nói ở đâu. |

### Khối dán

> **DÁN VÀO: `atlaslib/render.py` → `render_overview()`, ngay sau khối "Về dự án" ở §3**
>
> ```html
> <section class="note" id="gioi-han">
> <h2>Giới hạn của atlas này</h2>
>
> <p><b>Đây không phải bảng xếp hạng.</b> Mỗi mục được chọn theo bốn tiêu chí, xếp theo thứ tự ưu tiên: (a) phạm vi ảnh hưởng, (b) độ bền theo thời gian, (c) tính nguyên bản, (d) counterfactual — nếu không có người này thì thay đổi có đến muộn hơn đáng kể không. Bốn tiêu chí đó là một khung do người đặt ra, không phải một phép đo. Đổi khung thì đổi danh sách. Mục "Vì sao chọn" của mỗi nhân vật nêu đích danh 1–2 người cùng thời đã bị loại và lý do, để bạn tự đánh giá được phán đoán đó thay vì phải tin.</p>
>
> <p><b>Mỗi nhóm tối đa 10 người.</b> Đó là ràng buộc của định dạng, không phải kết luận lịch sử. Nhiều nhân vật xứng đáng bị loại chỉ vì nhóm đã đầy; danh sách những người bị loại và lý do nằm ở mục "Ghi chú biên tập" cuối mỗi chapter — nên đọc phần đó cùng với danh sách chính.</p>
>
> <p><b>Độ sâu nguồn rất mỏng.</b> Mỗi mục dẫn 1–2 nguồn. Đủ để lần ra đầu mối, không đủ để dùng làm căn cứ. Đừng trích atlas này trong bài viết học thuật — hãy đi tới nguồn, rồi trích nguồn.</p>
>
> <p><b>Niên đại nhiều mục không chắc chắn.</b> Huy hiệu "niên đại: Cao / Trung bình / Thấp" trên mỗi thẻ là mức tin cậy của chính niên đại đó. Năm sinh–mất được đối chiếu tự động với Wikidata; lệch quá ngưỡng sẽ bị báo và xử lý tay. Với nhân vật cổ đại, "năm" đôi khi là khoảng hoạt động hoặc thời gian trị vì chứ không phải năm sinh–mất, và điều này được ghi rõ trong Ghi chú biên tập. Có những trường hợp giới nghiên cứu lệch nhau hàng trăm năm — atlas ghi nhận sự bất định đó thay vì giấu đi.</p>
>
> <p><b>Thiên lệch tư liệu, không chỉ thiên lệch châu Âu.</b> Prompt research có chỉ thị chủ động xét Trung Hoa, Ấn Độ, Ba Tư, thế giới Hồi giáo, châu Phi, châu Mỹ và Đông Nam Á; phân bố theo vùng được công bố ngay trên trang này để bạn tự kiểm tra thay vì phải tin lời hứa. Nhưng còn một thiên lệch sâu hơn không sửa được bằng ý chí: <b>bản thân tư liệu đã thiên lệch</b>. Nền văn minh nào có chữ viết sớm, có truyền thống chép sử, có văn bản sống sót thì có tên người; nền văn minh nào không, thì không. Văn hoá Đông Sơn để lại trống đồng Ngọc Lũ và kỹ thuật đúc đồng ở trình độ cao mà không để lại một cái tên nào — nên nó vắng mặt trong atlas. Vắng mặt ở đây nghĩa là <i>không có tên được ghi lại</i>, không phải <i>không có đóng góp</i>.</p>
>
> <p><b>Phụ lục Việt Nam dùng thước đo khác.</b> Phụ lục giữ nguyên bốn tiêu chí nhưng đổi hệ quy chiếu: ảnh hưởng được đo trong phạm vi Việt Nam và Đông Nam Á, không phải toàn nhân loại. Vì là hai thước đo khác nhau nên phụ lục <b>không</b> được tính vào thống kê và lưới độ phủ trên trang này. Đừng so sánh trực tiếp một mục ở phụ lục với một mục ở chapter chính — chúng không đo cùng một thứ.</p>
>
> <p><b>"Ảnh hưởng" không có nghĩa là "đáng ngưỡng mộ".</b> Atlas ghi nhận mức độ một người định hình đường đi của tư tưởng hay thiết chế về sau. Nhiều người trong danh sách đạt được điều đó bằng chinh phạt, cưỡng ép hoặc những cách mà hôm nay ta lên án. Có mặt trong atlas là một nhận định về hệ quả, không phải một lời tán thành.</p>
> </section>
> ```

> **DÁN VÀO: `README.md`, thêm một mục mới ngay sau đoạn mở đầu** (bản rút gọn cho người đọc repo)
>
> ```markdown
> ## Bản chất và giới hạn của nội dung
>
> Đây là **dự án nghiên cứu cá nhân**, không phải bách khoa thư và không phải sản phẩm thương mại.
>
> - **Văn xuôi do mô hình AI (Claude) viết** theo prompt cố định ở `prompts/atlas-prompt.md`. Không có nhà sử học nào viết hay bình duyệt. Đây là tổng hợp do model thực hiện, không phải nghiên cứu sơ cấp.
> - **Tên, niên đại, định danh** được đối chiếu tự động với Wikidata (CC0) bởi `build.py`; lệch quá ngưỡng thì lint chặn build.
> - **Lựa chọn nhân vật là phán đoán biên tập** theo bốn tiêu chí (a) phạm vi, (b) độ bền, (c) tính nguyên bản, (d) counterfactual — không phải xếp hạng khách quan. Trần 10 người/nhóm buộc phải loại nhiều người xứng đáng; danh sách bị loại và lý do nằm ở `## Ghi chú biên tập` cuối mỗi chapter.
> - **Mỗi mục chỉ có 1–2 nguồn.** Đủ để lần đầu mối, không đủ để trích dẫn. Hãy đi tới nguồn.
> - **Phụ lục Việt Nam dùng hệ quy chiếu Việt Nam / Đông Nam Á**, không phải nhân loại, và vì vậy bị loại khỏi mọi thống kê toàn cục.
> - **"Ảnh hưởng" không đồng nghĩa với "đáng ngưỡng mộ".**
> ```

---

## 5. Nội dung lịch sử – chính trị nhạy cảm

### Nhận định

Phần này của dự án **đang được xử lý tốt hơn mức trung bình rất nhiều**, và điều đó đáng ghi nhận trước khi nói đến gap. Những gì đã có trong `content/ch90.md`:

- Mục Triệu Đà nêu thẳng tranh luận "chính thống hay ngoại xâm", dẫn cả *Đại Việt sử ký toàn thư* (xếp nhà Triệu vào quốc thống) lẫn Ngô Thì Sĩ phản bác, rồi kết: *"Phụ lục ghi nhận ông mà không kết luận thay người đọc."* Đó đúng là tư thế cần có.
- Giai đoạn 1954–1975: không lập nhóm TK 21, và với 1954–1975 thì ghi rõ *"các nhân vật chính trị và quân sự của cả hai miền đều đã được xem xét"*, lý do không mở rộng là tiêu chí (b) độ bền chưa đủ thời gian — một lý do **có nguyên tắc**, không phải né tránh. Đây là cách duy nhất xử lý được chuyện này mà không thành tuyên truyền theo hướng nào.
- Nhãn `[Tranh cãi lịch sử]` và `[Truyền thuyết]` là một cơ chế đánh dấu sẵn có, đã dùng đúng (An Dương Vương).
- Alexandre de Rhodes: ghi rõ công chữ Quốc ngữ là của một tập thể gồm Francisco de Pina, Gaspar do Amaral, António Barbosa và các thầy giảng người Việt — tránh đúng cái bẫy quy công cá nhân đang gây tranh cãi.
- `images.yaml` có danh sách `sensitive` cho vấn đề hình tượng (Q9458 — Muhammad), và ảnh có `Restrictions: personality` đã bị giữ lại chờ duyệt thay vì nhúng.

**Gap:** tất cả những tư thế biên tập trên nằm ở cuối trang chapter, trong một mục mà nhiều người đọc sẽ không cuộn tới. Chưa có tuyên bố ở cấp site. Và chưa có quy tắc thành văn cho người đóng góp — mà đây chính là chỗ một dự án mở dễ trượt nhất.

### Khối dán — **nên làm** (thực dụng, không lên lớp)

> **DÁN VÀO: `atlaslib/render.py` → `render_overview()`, sau khối "Giới hạn" ở §4**
>
> ```html
> <section class="note" id="trung-lap">
> <h2>Về những giai đoạn còn tranh luận</h2>
>
> <p>Atlas đi qua nhiều giai đoạn mà giới sử học chưa thống nhất, và nhiều nhân vật còn trong ký ức sống của người đang đọc. Nguyên tắc làm việc ở đây gồm bốn điều:</p>
>
> <p><b>1. Ghi nhận tranh luận, không phân xử.</b> Khi một vấn đề còn chưa khép lại trong giới nghiên cứu — nhà Triệu có thuộc quốc thống Việt Nam hay không là ví dụ rõ nhất — atlas trình bày các lập trường và nguồn của chúng, rồi dừng ở đó. Mục đích là để bạn thấy được cuộc tranh luận, không phải để nhận một kết luận có sẵn.</p>
>
> <p><b>2. Nhân vật được chọn vì hệ quả, không vì lập trường.</b> Có mặt trong atlas nghĩa là người đó đã định hình đáng kể đường đi về sau — không phải là một đánh giá đạo đức, không phải một lời tán thành, và cũng không phải một lời lên án.</p>
>
> <p><b>3. Giai đoạn càng gần, kết luận càng tạm.</b> Tiêu chí (b) độ bền cần thời gian mới đo được. Vì vậy phụ lục Việt Nam dừng ở thế kỷ 20 và không lập nhóm thế kỷ 21; với giai đoạn 1954–1975, các nhân vật của cả hai phía đều đã được xem xét theo cùng một bộ tiêu chí, và việc không mở rộng là vì chưa đủ độ lùi thời gian chứ không phải vì né tránh.</p>
>
> <p><b>4. Phân biệt sự kiện với quy kết.</b> Atlas nêu những gì có nguồn và tránh gán động cơ cho người đã khuất hay người còn sống. Với nhân vật đương đại hoặc mới qua đời, phạm vi chỉ gồm những gì đã được ghi chép công khai và liên quan trực tiếp tới ảnh hưởng của họ.</p>
>
> <p class="small muted">Nếu bạn thấy một mục nghiêng lệch, thiếu một lập trường có cơ sở, hoặc nêu sai một sự kiện — xin báo kèm nguồn. Phản hồi có nguồn sẽ được sửa; phản hồi chỉ là quan điểm sẽ được ghi nhận nhưng không làm đổi nội dung.</p>
> </section>
> ```

### Điểm cần luật sư, không cần tài liệu này

Ba tình huống dưới đây nằm ngoài phạm vi rà soát kỹ thuật và **nếu xảy ra thật thì phải hỏi luật sư Việt Nam**, không tự xử theo checklist:

1. Khiếu nại từ cá nhân còn sống hoặc thân nhân người đã mất về nội dung một mục (danh dự, nhân phẩm, quyền nhân thân về hình ảnh).
2. Yêu cầu gỡ bỏ từ cơ quan quản lý, hoặc câu hỏi về nghĩa vụ khi đặt máy chủ / tên miền tại Việt Nam cho một trang có nội dung lịch sử – chính trị.
3. Tranh chấp bản quyền thực tế về một ảnh cụ thể (ví dụ bảo tàng khẳng định quyền với ảnh chụp tác phẩm 2D đã hết hạn bản quyền — `ita-mibac` là đúng loại này, và dự án đã làm đúng khi **không** nhúng).

Tài liệu này không đưa ý kiến pháp lý về ba việc đó.

---

## 6. Giấy phép cho chính dự án — **bắt buộc (B1)**, một khuyến nghị duy nhất

### Khuyến nghị

| Thành phần | Giấy phép | Lý do một dòng |
|---|---|---|
| **Code** — `build.py`, `fetch_images.py`, `atlaslib/`, `assets/style.css`, `assets/app.js`, `tests/` | **MIT** | Khớp với MIT/ISC của hai thư viện đã vendored, và để công cụ tái dùng được ở mức tối đa. |
| **Văn xuôi** — `content/*.md`, `prompts/atlas-prompt.md`, và HTML sinh ra từ chúng | **CC BY-SA 4.0** | Chọn đúng giấy phép chặt nhất đã có mặt trên trang (ảnh CC BY-SA) nên không bao giờ phát sinh mâu thuẫn giữa chữ và ảnh trên cùng một trang, đồng thời buộc đóng góp quay về cùng điều khoản. |
| **Dữ liệu** — `data/persons.json`, `data/persons.js`, `data/images.json`, `data/wikidata-cache.json` | **CC0 1.0** | Phần lớn là sự kiện lấy từ Wikidata vốn đã CC0; đặt điều khoản chặt hơn lên trên là tự tạo mâu thuẫn. |
| **Ảnh** trong `assets/img/` | Giữ nguyên giấy phép riêng từng ảnh | Dự án không sở hữu chúng; `credits.html` là danh mục chính thức. |
| **Thư viện vendored** | Giữ nguyên MIT / ISC của tác giả | `assets/LICENSE-*.txt` + file third-party ở §2.2. |

**Nói cho rõ để Owner không hiểu nhầm:** CC BY-SA 4.0 cho văn xuôi là một **lựa chọn**, không phải nghĩa vụ do ảnh CC BY-SA áp xuống (xem §1.3 — đặt ảnh cạnh chữ không kích hoạt ShareAlike). Lý do chọn nó là thực dụng: nó dọn sạch mọi khả năng tranh cãi về việc "điều khoản của trang có đang hạn chế ảnh hơn mức giấy phép cho phép không", và nó phù hợp với ý định *"welcome contribution"* — người đóng góp biết công sức của mình không bị đóng lại sau này. Nếu Owner muốn tái sử dụng tự do hơn thì CC BY 4.0 cũng hợp lệ và cũng không mâu thuẫn với ảnh; chỉ là mất phần "đóng góp phải quay về cùng điều khoản".

### Khối dán

> **DÁN VÀO: `LICENSE` (file mới ở gốc repo)**
> Dán **nguyên văn** giấy phép MIT từ https://opensource.org/license/mit, với dòng bản quyền:
> `Copyright (c) 2026 <tên hoặc handle của Owner>`
> (File `LICENSE` ở gốc chỉ nên chứa giấy phép của code — GitHub đọc file này để gắn nhãn repo.)

> **DÁN VÀO: `LICENSES.md` (file mới ở gốc repo)**
>
> ```markdown
> # Giấy phép
>
> Kho này gồm nhiều thành phần với giấy phép khác nhau. Đây là bản tóm tắt; văn bản giấy phép đầy đủ nằm ở các file được dẫn.
>
> ## Mã nguồn — MIT
> `build.py`, `fetch_images.py`, `atlaslib/`, `assets/style.css`, `assets/app.js`, `tests/`.
> Văn bản: [`LICENSE`](LICENSE).
>
> ## Nội dung văn bản — CC BY-SA 4.0
> `content/*.md`, `prompts/atlas-prompt.md`, và phần văn bản của HTML sinh ra từ chúng
> (`chapters/*.html`, `overview.html`, `index.html`, `credits.html`).
> Giấy phép: [Creative Commons Ghi công – Chia sẻ tương tự 4.0 Quốc tế](https://creativecommons.org/licenses/by-sa/4.0/deed.vi).
> Ghi công đề nghị: *"Atlas nhân vật ảnh hưởng — history-atlas, CC BY-SA 4.0"* kèm link tới kho này.
> Lưu ý: phần văn xuôi do mô hình AI soạn (xem README). Giấy phép này áp lên bản biên tập, không phải là một tuyên bố về quyền tác giả của model.
>
> ## Dữ liệu — CC0 1.0
> `data/persons.json`, `data/persons.js`, `data/images.json`, `data/wikidata-cache.json`.
> Phần lớn là sự kiện bắt nguồn từ [Wikidata](https://www.wikidata.org) (CC0 1.0); dự án từ bỏ mọi quyền còn lại đối với phần dữ liệu này theo [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.vi).
>
> ## Ảnh — mỗi ảnh một giấy phép riêng
> Ảnh trong `assets/img/` **không** thuộc giấy phép của dự án. Mỗi ảnh giữ nguyên giấy phép của nó
> (Public domain, CC0, CC BY, hoặc CC BY-SA 2.0/3.0/4.0) cùng với tác giả và link tệp gốc trên Wikimedia Commons.
> Danh mục đầy đủ: [`credits.html`](credits.html) và `data/images.json`.
> Không điều khoản nào của dự án này được hiểu là áp thêm hạn chế lên các ảnh đó ngoài giấy phép của chính chúng.
>
> ## Thư viện bên thứ ba
> - Mermaid 11.4.1 — MIT — [`assets/LICENSE-mermaid.txt`](assets/LICENSE-mermaid.txt), và thông báo của các thư viện được đóng gói kèm ở [`assets/LICENSE-mermaid-thirdparty.txt`](assets/LICENSE-mermaid-thirdparty.txt).
> - D3 7.9.0 — ISC — [`assets/LICENSE-d3.txt`](assets/LICENSE-d3.txt).
> - Python-Markdown — BSD-3-Clause — chỉ dùng lúc build, không phát hành kèm site.
> ```

> **DÁN VÀO: `atlaslib/render.py` → `footer()`, thêm vào cuối chuỗi**
>
> ```python
> f' · Văn bản: <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.vi" rel="noopener">CC BY-SA 4.0</a> · Mã nguồn: MIT · Ảnh giữ giấy phép riêng, xem <a href="{rel}credits.html">Credits</a>'
> ```

---

## 7. CONTRIBUTING — mức tối thiểu cho *dự án này*

Chưa có file nào. Dưới đây là bản đầy đủ, viết riêng theo cấu trúc thật của repo (file sinh tự động, cổng lint, từ vựng cố định, chính sách ảnh).

> **DÁN VÀO: `CONTRIBUTING.md` (file mới ở gốc repo)**
>
> ````markdown
> # Đóng góp cho history-atlas
>
> Cảm ơn bạn quan tâm. Đây là dự án nghiên cứu cá nhân, không phải bách khoa thư — xin đọc mục "Bản chất và giới hạn của nội dung" trong `README.md` trước.
>
> Ngôn ngữ hiện tại: **tiếng Việt**. Bản tiếng Anh có thể có sau; chưa nhận bản dịch lúc này.
>
> ## 0. Quy tắc quan trọng nhất: đừng sửa file được sinh ra
>
> | Sửa được | **KHÔNG BAO GIỜ sửa tay** (bị `build.py` ghi đè) |
> |---|---|
> | `content/*.md` · `content/images.yaml` · `atlaslib/*.py` · `build.py` · `fetch_images.py` · `assets/style.css` · `assets/app.js` · `prompts/atlas-prompt.md` · `tests/*.md` · `README.md` | `index.html` · `overview.html` · `credits.html` · `chapters/*.html` · `data/persons.json` · `data/persons.js` · `data/images.json` · `reports/` |
>
> Muốn đổi chữ hiển thị trên web? Sửa trong `atlaslib/render.py` rồi chạy lại `python build.py`.
>
> ## 1. Chuẩn nội dung
>
> Mỗi mục nhân vật phải theo đúng template trong `prompts/atlas-prompt.md`. Không được tự chế biến thể.
>
> - **ID**: `CHxx-NHÓM-nn`, nhóm phải thuộc đúng chapter (bảng `CHAPTERS` / `APPENDICES` trong `atlaslib/common.py`).
> - **Dòng metadata**: `năm: | nơi: | vùng: | lĩnh vực: | độ tin cậy niên đại: | wikidata: | câu hỏi lớn:` — đúng thứ tự, đúng dấu phân cách.
> - **Số chữ**: "Tư tưởng / đóng góp chính" ~100 chữ · "Vì sao chọn" ~80 chữ · giới thiệu chapter ≤100 · bối cảnh nhóm ≤60. Lệch quá 30% sẽ bị cảnh báo.
> - **"Vì sao chọn" phải nêu ĐÍCH DANH 1–2 người cùng thời, cùng lĩnh vực đã bị loại** và lý do theo tiêu chí (a)–(d). Viết chung chung là lý do từ chối PR.
> - **Tối đa 2 lĩnh vực, tối đa 2 câu hỏi lớn, tối đa 10 người/nhóm.**
> - **Nguồn**: 1–2 nguồn thật, ưu tiên nguồn học thuật, kèm link nếu có. **Nguồn phải tồn tại và phải nói đúng điều được dẫn** — xem mục 5.
> - **Nhãn**: dùng `[Truyền thuyết]` hoặc `[Tranh cãi lịch sử]` khi nhân vật chỉ có trong thư tịch soạn muộn, hoặc khi tính lịch sử còn tranh luận.
> - **Mỗi chapter phải có `## Ghi chú biên tập`**, gồm: ứng viên mạnh đã loại và lý do, điểm cần kiểm chứng thêm, và một dòng về ứng viên Việt Nam (có hoặc không, nhưng phải nói).
>
> ## 2. Từ vựng cố định — không tự thêm từ trong nội dung
>
> Các trường sau chỉ nhận **đúng** những giá trị liệt kê trong `atlaslib/common.py`. Viết sai một chữ là lint báo ERROR và build dừng:
>
> | Hằng số | Số giá trị | Trường trong `.md` |
> |---|---|---|
> | `FIELDS` | 16 | `lĩnh vực:` |
> | `REGIONS` | 9 | `vùng:` |
> | `BIG_QUESTIONS` | 4 | `câu hỏi lớn:` |
> | `CONFIDENCE` | 3 | `độ tin cậy niên đại:` |
> | `RELATION_TYPES` | 4 | loại quan hệ ở "Kế thừa từ" / "Ảnh hưởng tới" |
> | `EVIDENCE_LEVELS` | 3 | mức bằng chứng ở cùng hai mục trên |
> | `LABELS` | 2 | nhãn `[…]` sau tên |
>
> **Thiếu một mục từ vựng thì sửa từ vựng, đừng ép nội dung vào ô sai.** Quy trình đúng — có tiền lệ: khi Pāṇini không có chỗ, Owner đã thêm **Giáo dục** và **Ngôn ngữ học** vào `FIELDS`. Một PR thêm từ vựng phải sửa **cả ba** nơi trong cùng một PR:
> 1. hằng số trong `atlaslib/common.py`,
> 2. danh sách tương ứng trong `prompts/atlas-prompt.md`,
> 3. nếu là `RELATION_TYPES` / `EVIDENCE_LEVELS` / `CONFIDENCE`: thêm biến màu và selector CSS tương ứng trong `assets/style.css` — tên class được sinh từ nhãn đã bỏ dấu (ví dụ `kế thừa` → `.badge.rel-ke-thua`), thiếu là huy hiệu mất màu.
>
> ## 3. Cổng lint — PR phải sạch mới được xét
>
> ```bash
> pip install -r requirements.txt
> python build.py                 # lint + đối chiếu Wikidata + sinh HTML
> python build.py --offline       # nếu không muốn gọi Wikidata
> python build.py --lint-only content/ch02.md   # chỉ lint một file
> ```
>
> - **ERROR chặn build.** Gồm: thiếu trường / sai format metadata; ID trùng hoặc sai quy ước; nhóm không thuộc chapter; giá trị ngoài từ vựng; quá 2 lĩnh vực / 2 câu hỏi lớn; nhóm quá 10 người; năm mất trước năm sinh; liên kết tới chính mình; thiếu `## Ghi chú biên tập`; ảnh nhúng không có giấy phép.
> - **WARNING không chặn build, nhưng PR phải xử lý.** Hoặc sửa nội dung, hoặc **thêm một dòng giải thích vào `## Ghi chú biên tập`**. Cảnh báo niên đại lệch Wikidata, cảnh báo đa dạng lĩnh vực/vùng, cảnh báo nhãn không khớp — đều phải có câu trả lời ở đó. Tiền lệ: nhóm `BCE03_01` chỉ có 2 lĩnh vực và điều đó được giải thích là giới hạn tư liệu Đông Sơn, không phải thiếu sót.
> - **`--force` chỉ để xem giao diện.** Không bao giờ dùng để merge một PR còn ERROR.
> - **Kiểm thử hồi quy** — chạy trước khi gửi PR, nhất là khi bạn sửa `atlaslib/lint.py`:
>   ```bash
>   python build.py --lint-only tests/ch99-bad.md      # phải ra 23 ERROR, exit 1
>   python build.py --lint-only tests/ch98-wikidata.md # phải cảnh báo nhãn không khớp + lệch niên đại
>   ```
>   Nếu con số 23 thay đổi vì bạn thêm luật lint mới, hãy nói rõ trong PR và cập nhật `README.md`.
>
> ## 4. Ảnh — quy tắc cứng
>
> - **Không bao giờ commit tay một file vào `assets/img/`.** Mọi ảnh phải đi qua `python fetch_images.py`, để metadata giấy phép được ghi vào `data/images.json` và hiện lên `credits.html`.
> - **Chỉ được nhúng**: Public domain / PD-* / PDM / CC0 / CC BY / CC BY-SA (mọi phiên bản).
> - **Không bao giờ nhúng**: NC · ND · fair use · non-free · GFDL-only · không rõ giấy phép · bất kỳ ảnh nào có trường `Restrictions` trên Commons (quyền nhân thân, `ita-mibac`, nhãn hiệu…). Những ảnh này chỉ được đặt link "Xem ảnh tại Wikimedia Commons".
> - Muốn đổi ảnh hoặc viết lại chú thích thì sửa `content/images.yaml`, không sửa `data/images.json`.
> - Nhân vật nhạy cảm về hình tượng (ví dụ aniconism trong Hồi giáo) đưa Q-ID vào mục `sensitive:` của `content/images.yaml`.
> - **Nếu bạn cắt cúp, ghép, tô màu hoặc lồng chữ lên một ảnh CC BY-SA**, ảnh kết quả là tác phẩm phái sinh và **bắt buộc phải phát hành dưới đúng giấy phép CC BY-SA đó**. Ghi rõ việc này trong PR. Thu nhỏ đơn thuần (việc mà `fetch_images.py` đang làm) không tạo ra tác phẩm phái sinh.
>
> ## 5. Nội dung do AI sinh ra
>
> Phần văn xuôi hiện có của dự án do mô hình AI viết, và đó là điều được công bố công khai. Bạn **được phép** dùng AI để soạn đóng góp, với hai điều kiện không thương lượng:
>
> 1. **Nói rõ trong PR** là phần nào do AI soạn và bằng prompt nào.
> 2. **Tự mở và đối chiếu từng nguồn trước khi gửi.** Trích dẫn bịa — sách không tồn tại, số trang sai, nguồn không nói điều được dẫn — là lý do đóng PR ngay, không sửa lại.
>
> ## 6. Nội dung lịch sử – chính trị nhạy cảm
>
> - **Ghi nhận tranh luận, không phân xử.** Khi giới nghiên cứu chưa thống nhất, trình bày các lập trường kèm nguồn rồi dừng.
> - **Nêu sự kiện có nguồn, không quy kết động cơ** — với cả người đã khuất lẫn người còn sống.
> - PR biến một mục thành bài ca ngợi hoặc bài kết tội sẽ bị từ chối, dù nguồn có đúng.
> - Góp ý về một mục xin kèm nguồn. Góp ý có nguồn sẽ được xử lý; góp ý thuần quan điểm được ghi nhận nhưng không làm đổi nội dung.
>
> ## 7. Giấy phép cho đóng góp của bạn
>
> Khi gửi PR, bạn đồng ý rằng đóng góp của mình được phát hành theo:
> - **MIT** nếu là mã nguồn,
> - **CC BY-SA 4.0** nếu là nội dung văn bản,
> - **CC0 1.0** nếu là dữ liệu.
>
> Xem [`LICENSES.md`](LICENSES.md). Nếu bạn không có quyền cấp phép phần mình gửi (ví dụ copy từ nguồn có bản quyền), đừng gửi.
>
> ## 8. Checklist trước khi gửi PR
>
> - [ ] `python build.py` chạy sạch, 0 ERROR
> - [ ] Mọi WARNING hoặc đã sửa, hoặc đã có dòng giải thích trong `## Ghi chú biên tập`
> - [ ] `tests/ch99-bad.md` vẫn ra 23 ERROR
> - [ ] Không sửa tay file nào trong cột "KHÔNG BAO GIỜ sửa tay" ở mục 0
> - [ ] Ảnh (nếu có) đi qua `fetch_images.py`, giấy phép hợp lệ, `credits.html` đã dựng lại
> - [ ] Nguồn đã được tự mở và đối chiếu
> - [ ] Đã nói rõ phần nào do AI soạn
> ````

---

## 8. Chuẩn bị cho bản tiếng Anh — **có vấn đề thật, và nên xử lý sớm**

Không phải "không thấy gì". Cấu trúc hiện tại có bốn chỗ sẽ rất đau khi thêm EN, xếp theo mức độ:

### I1 — nặng nhất · Từ vựng cố định vừa là **dữ liệu** vừa là **nhãn hiển thị**

`FIELDS`, `REGIONS`, `BIG_QUESTIONS`, `CONFIDENCE`, `RELATION_TYPES`, `EVIDENCE_LEVELS`, `LABELS` là các chuỗi tiếng Việt được viết **nguyên văn vào `content/*.md`**, được `atlaslib/lint.py` kiểm tra bằng so khớp chuỗi, rồi được `render.py` in thẳng ra HTML. Không có khoá ổn định nào ở giữa.

Hệ quả: thêm EN nghĩa là hoặc (a) duy trì hai bộ nội dung với hai bộ từ vựng song song, hoặc (b) migrate toàn bộ `.md` sang khoá trung tính.

### I2 — âm thầm và dễ bỏ sót · Tên class CSS được sinh từ nhãn tiếng Việt

`C.slug()` bỏ dấu rồi tạo class. HTML đang sinh ra: `conf-cao`, `conf-trung-binh`, `conf-thap`, `rel-ke-thua`, `rel-tong-hop`, `rel-phan-bac`, `rel-tuong-dong-doc-lap`, `ev-truc-tiep`, `ev-qua-truong-phai`, `ev-suy-doan-hoc-gia`. Và `assets/style.css` khớp cứng với chúng, kể cả biến màu (`--rel-ke-thua`, `--ev-truc-tiep`…).

→ **Đổi nhãn sang tiếng Anh là toàn bộ huy hiệu mất màu**, không có lỗi nào báo ra. Đây là loại hỏng tệ nhất: im lặng.

### I3 — nhiều nhưng dễ · Chuỗi giao diện nằm rải rác trong code

`page()` hard-code `<html lang="vi">`. Chuỗi UI nằm inline trong `render.py` và `app.js`: "Mục lục", "Overview", "Credits", "Chapter", "Phụ lục", "Tư tưởng / đóng góp chính", "Vì sao chọn", "Kế thừa từ", "Ảnh hưởng tới", "Được ghi là nguồn kế thừa bởi", "Nguồn", "còn sống", "Chưa có dữ liệu cho nhóm này", "Bối cảnh", "Ghi chú biên tập", "Xem ảnh tại Wikimedia Commons", "không rõ tác giả", "đã thu nhỏ", "Thư viện"… Cộng thêm `group_label()` sinh `"TK 8–5 TCN"`, `year_label()` sinh `"TCN"`, và `build_caption()` trong `fetch_images.py` ráp cả một câu tiếng Việt: *"Chân dung X, …, (tưởng tượng). Ảnh: Wikimedia Commons, …"*. Và tiêu đề/nhãn chapter trong `CHAPTERS` / `APPENDICES`.

### I4 — nhỏ · Mô hình dữ liệu chỉ có một tên

`name_vi` + `name_orig`, không có chỗ cho `name_en`. `data/persons.js` (chỉ mục tìm kiếm) cũng chỉ một ngôn ngữ.

### Điểm đã làm đúng, không cần sửa

- **ID nhân vật và ID nhóm đều là ASCII** (`CH02-BCE05-01`, `BCE20_18`, `CE19_20`) → anchor và URL dùng chung được cho mọi ngôn ngữ.
- **Hash routing trung tính ngôn ngữ** (`#ch02/BCE05`) → link sâu không vỡ khi thêm EN.
- Cache Wikidata đã lưu theo Q-ID chứ không theo nhãn.

### Khuyến nghị — làm **trước** khi viết Ch1 và Ch3–Ch11

Hiện mới có 2 chapter / ~73 nhân vật. Sau khi có 11 chapter với 400+ mục, việc này thành một cuộc migrate thật sự. Ba bước, rẻ nếu làm bây giờ:

1. **Tách khoá khỏi nhãn.** Đổi các hằng số thành `{"key": "philosophy", "vi": "Triết học", "en": "Philosophy"}`. Lint chấp nhận **cả** nhãn VI (để `.md` hiện tại không phải sửa) lẫn khoá; `render.py` tra nhãn theo ngôn ngữ đang dựng.
2. **Khoá chết tên class CSS theo `key`, không theo `slug(nhãn)`.** Sửa trong `person_card()`: `rel-{l["key"]}` thay vì `rel-{C.slug(l["relation"])}`. Đổi tên selector trong `style.css` một lần cho xong.
3. **Gom chuỗi UI vào một `STRINGS = {"vi": {...}, "en": {...}}` trong `common.py`**, thêm `PROJECT["lang"]`, và dựng ra `vi/` + `en/`. `build_caption()` cũng lấy mẫu câu từ đó.

Bước 2 là bước đáng làm nhất ngay cả khi **không bao giờ** có bản tiếng Anh — vì hiện tại chỉ cần đổi cách viết một nhãn trong `common.py` (ví dụ `"kế thừa"` → `"Kế thừa"`) là CSS đứt im lặng.

---

## 9. Bảng tra nhanh: dán cái gì vào đâu

| Khối text | File đích | Loại file | Sau đó |
|---|---|---|---|
| Công bố AI — một dòng | `atlaslib/render.py` → `footer()` | code sinh HTML | `python build.py` |
| Công bố AI — khối "Về dự án" | `atlaslib/render.py` → `render_overview()` | code sinh HTML | `python build.py` |
| Công bố AI — đoạn chuẩn mỗi chapter | `content/ch02.md`, `content/ch90.md`, `prompts/atlas-prompt.md` | viết tay | `python build.py` |
| Giới hạn học thuật — khối đầy đủ | `atlaslib/render.py` → `render_overview()` | code sinh HTML | `python build.py` |
| Giới hạn học thuật — bản rút gọn | `README.md` | viết tay | — |
| Trung lập về giai đoạn tranh luận | `atlaslib/render.py` → `render_overview()` | code sinh HTML | `python build.py` |
| Dòng giấy phép ở footer | `atlaslib/render.py` → `footer()` | code sinh HTML | `python build.py` |
| Mục "Thư viện & dữ liệu bên thứ ba" | `atlaslib/render.py` → `render_credits()` | code sinh HTML | `python build.py` |
| Giấy phép MIT | `LICENSE` | file mới | — |
| Bảng giấy phép theo thành phần | `LICENSES.md` | file mới | — |
| Hướng dẫn đóng góp | `CONTRIBUTING.md` | file mới | — |
| Thông báo bên thứ ba của Mermaid | `assets/LICENSE-mermaid-thirdparty.txt` | file mới | — |
| Chặn nhúng khi không kiểm được `Restrictions` (B2) | `fetch_images.py` → `main()` | code | chạy lại fetch |

---

*Hết. Mọi nhận định về giấy phép ở trên chỉ đọc đúng những gì văn bản CC BY-SA 2.0/3.0/4.0, CC0 1.0, MIT, ISC và Apache-2.0 nói thẳng ra. Không có nội dung nào ở đây là tư vấn pháp lý.*
