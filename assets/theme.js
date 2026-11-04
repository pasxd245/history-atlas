/* history-atlas — nút theme, reading mode, phím ←/→.
   Phần đặt thuộc tính trước khi vẽ nằm inline trong <head> (xem render.page);
   file này chỉ lo nút bấm, đồng bộ giữa index.html với trang trong iframe, và bàn phím. */
(function () {
  "use strict";
  var root = document.documentElement;
  var THEME = "ha-theme", READ = "ha-reading";
  var CYCLE = ["auto", "light", "dark"];
  var NHAN = { auto: "◐ Theo hệ thống", light: "☀ Sáng", dark: "☾ Tối" };

  function doc(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function ghi(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  function theme() { var v = doc(THEME); return CYCLE.indexOf(v) >= 0 ? v : "auto"; }
  function reading() { return doc(READ) === "on"; }

  function apDung() {
    var t = theme();
    if (t === "auto") root.removeAttribute("data-theme"); else root.setAttribute("data-theme", t);
    if (reading()) root.setAttribute("data-reading", "on"); else root.removeAttribute("data-reading");
    veNut();
  }

  function veNut() {
    var bt = document.querySelector('[data-toggle="theme"]');
    // aria-pressed là nhị phân, không mô tả được ba trạng thái — trạng thái nằm ở nhãn chữ.
    if (bt) bt.textContent = NHAN[theme()];
    var br = document.querySelector('[data-toggle="reading"]');
    if (br) { br.setAttribute("aria-pressed", reading() ? "true" : "false"); }
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-toggle]");
    if (!b) return;
    if (b.dataset.toggle === "theme") ghi(THEME, CYCLE[(CYCLE.indexOf(theme()) + 1) % CYCLE.length]);
    else if (b.dataset.toggle === "reading") ghi(READ, reading() ? "off" : "on");
    apDung();
  });

  // index.html và trang trong iframe là hai document cùng origin: `storage` bắn sang
  // document KIA mỗi lần ghi, nên bấm ở bên nào thì bên kia cũng đổi theo.
  window.addEventListener("storage", function (e) {
    if (e.key === THEME || e.key === READ) apDung();
  });

  // ---- phím ←/→ lật chapter, chỉ trên trang chapter (index.html tự lo trong app.js).
  // Bỏ qua khi đang gõ trong ô nhập hoặc khi giữ phím bổ trợ, để không cướp thao tác.
  document.addEventListener("keydown", function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    var el = document.activeElement;
    if (el && (el.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(el.tagName))) return;
    var nav = document.querySelector(".topnav");
    if (!nav) return;
    var dau = e.key === "ArrowLeft" ? "←" : "→";
    var links = Array.prototype.filter.call(nav.querySelectorAll("a"), function (a) {
      return a.textContent.indexOf(dau) >= 0;
    });
    if (links.length) { e.preventDefault(); links[0].click(); }
  });

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", veNut);
  else veNut();
})();
