/* index.html — sidebar, hash routing (#ch02/BCE05, #ch02/CH02-BCE06-01, #overview, #credits), tìm kiếm, prev/next.
   Không fetch(): nội dung hiển thị qua <iframe> để mở được bằng file://. Dữ liệu tìm kiếm từ data/persons.js. */
(function () {
  "use strict";
  var frame = document.getElementById("frame");
  var items = Array.prototype.slice.call(document.querySelectorAll("a.item"));
  var openNew = document.getElementById("open-new");
  var crumb = document.getElementById("crumb");
  var btnPrev = document.getElementById("prev"), btnNext = document.getElementById("next");
  var body = document.body;
  var PERSONS = window.ATLAS_PERSONS || [];
  var CHAPTERS = (window.ATLAS_CHAPTERS || []).filter(function (c) { return c.has; }); // chỉ chapter có dữ liệu
  var TRACK = {}; (window.ATLAS_CHAPTERS || []).forEach(function (c) { TRACK[c.no] = c.track || "main"; });
  var chapterNos = CHAPTERS.map(function (c) { return c.no; });

  // ---- hash <-> trang
  function hashToPage(h) {
    // "ch02/BCE05" -> chapters/ch02.html#BCE05 ; "overview" -> overview.html ; "ch02" -> chapters/ch02.html
    if (!h) return null;
    var m = /^(ch\d{2})(?:\/([A-Za-z0-9_-]+))?$/.exec(h);
    if (m) return "chapters/" + m[1] + ".html" + (m[2] ? "#" + m[2] : "");
    if (/^(overview|credits)$/.test(h)) return h + ".html";
    if (/^chapters\/ch\d{2}\.html(#[\w-]+)?$/.test(h) || /^(overview|credits)\.html$/.test(h)) return h; // dạng cũ
    return null;
  }
  function pageToHash(page) {
    var m = /^chapters\/(ch\d{2})\.html(?:#([\w-]+))?$/.exec(page);
    if (m) return m[1] + (m[2] ? "/" + m[2] : "");
    return page.replace(/\.html$/, "");
  }
  function currentChapterNo(page) {
    var m = /^chapters\/ch(\d{2})\.html/.exec(page || "");
    return m ? parseInt(m[1], 10) : null;
  }

  function setActive(page) {
    var base = page.split("#")[0];
    var best = null;
    items.forEach(function (a) {
      var p = a.dataset.page;
      var hit = p === page || p === base;
      a.classList.toggle("active", hit);
      if (hit) best = a;
    });
    if (best) {
      var det = best.closest("details"); if (det) det.open = true;
    }
    openNew.href = page;
    var no = currentChapterNo(page);
    var lbl = best ? best.querySelector(".lbl") : null;
    var lblText = lbl ? (lbl.childNodes[0] ? lbl.childNodes[0].textContent : lbl.textContent).trim() : "";
    var head = no !== null ? (TRACK[no] === "main" ? "Chapter " + no : "Phụ lục") : null;
    var title = head !== null ? (head + (lblText ? " · " + lblText : "")) : (base.replace(".html", "") === "overview" ? "Overview" : "Credits");
    crumb.textContent = title;
    var idx = no !== null ? chapterNos.indexOf(no) : -1;
    btnPrev.disabled = idx <= 0; btnNext.disabled = idx < 0 || idx >= chapterNos.length - 1;
  }

  function go(page, push) {
    if (!page) return;
    frame.src = page;
    if (push !== false) { var h = pageToHash(page); if (location.hash.slice(1) !== h) location.hash = h; }
    setActive(page);
    body.classList.remove("menu-open");
  }

  items.forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); go(a.dataset.page); }); });
  btnPrev.addEventListener("click", function () { var no = currentChapterNo(frame.getAttribute("src")); var i = chapterNos.indexOf(no); if (i > 0) go("chapters/ch" + pad(chapterNos[i - 1]) + ".html"); });
  btnNext.addEventListener("click", function () { var no = currentChapterNo(frame.getAttribute("src")); var i = chapterNos.indexOf(no); if (i >= 0 && i < chapterNos.length - 1) go("chapters/ch" + pad(chapterNos[i + 1]) + ".html"); });
  function pad(n) { return (n < 10 ? "0" : "") + n; }

  // khi người đọc bấm link bên trong iframe (prev/next, link nhân vật) → đồng bộ hash + menu
  frame.addEventListener("load", function () {
    try {
      var loc = frame.contentWindow.location;
      var here = location.href.replace(/index\.html.*$/, "").replace(/#.*$/, "");
      var full = loc.href;
      if (full.indexOf(here) === 0) {
        var rel = full.slice(here.length);
        if (rel) { setActive(rel); var h = pageToHash(rel); if (location.hash.slice(1) !== h) history.replaceState(null, "", "#" + h); }
      }
      // link trong iframe có target=_top đã xử lý; các link khác giữ trong iframe
    } catch (e) { /* khác origin — bỏ qua */ }
  });

  window.addEventListener("hashchange", function () {
    var page = hashToPage(location.hash.slice(1));
    if (page && frame.getAttribute("src") !== page) go(page, false);
  });

  // ---- menu mobile
  var mb = document.getElementById("menu-btn");
  if (mb) mb.addEventListener("click", function () { body.classList.toggle("menu-open"); });
  document.getElementById("brand-link").addEventListener("click", function (e) { e.preventDefault(); go("overview.html"); });

  // ---- tìm kiếm: tên, tên gốc, lĩnh vực, vùng, ID
  var q = document.getElementById("q"), hits = document.getElementById("hits");
  function norm(s) { return (s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d").replace(/Đ/g, "D").toLowerCase(); }
  q.addEventListener("input", function () {
    var v = norm(q.value.trim());
    hits.innerHTML = "";
    if (v.length < 2) return;
    var res = PERSONS.filter(function (p) {
      return norm(p.n).indexOf(v) >= 0 || norm(p.o).indexOf(v) >= 0 || norm(p.id).indexOf(v) >= 0 ||
        (p.f || []).some(function (f) { return norm(f).indexOf(v) >= 0; }) || norm(p.r).indexOf(v) >= 0;
    }).slice(0, 15);
    res.forEach(function (p) {
      var a = document.createElement("a"); a.className = "item"; a.href = p.u; a.dataset.page = p.u;
      a.innerHTML = '<span class="num">→</span><span class="lbl">' + esc(p.n) + '<span class="range">' + esc(p.g + " · " + (p.f || []).join(", ") + (p.r ? " · " + p.r : "")) + "</span></span>";
      a.addEventListener("click", function (e) { e.preventDefault(); go(p.u); });
      hits.appendChild(a);
    });
    if (!res.length) hits.innerHTML = '<div class="small muted" style="padding:4px 8px">không có kết quả</div>';
  });
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  // ---- khởi động
  var start = hashToPage(location.hash.slice(1)) || "overview.html";
  go(start, false);
})();
