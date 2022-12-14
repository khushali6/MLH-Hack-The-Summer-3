const root = document.querySelector("body, html");
const container = document.querySelector(".gg-container");
const images = document.querySelectorAll(".gg-box > img");
const l = images.length;
for (var i = 0; i < l; i++) {
  images[i].addEventListener("click", function (h) {
    var f = this;
    const c = f.parentElement,
      a = document.createElement("div");
    a.id = "gg-screen";
    container.prepend(a);
    if (c.hasAttribute("data-theme")) {
      a.setAttribute("data-theme", "dark");
    }
    var p = f.src;
    root.style.overflow = "hidden";
    a.innerHTML =
      '<div class="gg-image"></div><div class="gg-close gg-btn">&times</div><div class="gg-next gg-btn">&rarr;</div><div class="gg-prev gg-btn">&larr;</div>';
    const k = images[0].src,
      q = images[l - 1].src;
    const o = document.querySelector(".gg-image"),
      e = document.querySelector(".gg-prev"),
      b = document.querySelector(".gg-next"),
      r = document.querySelector(".gg-close");
    o.innerHTML = '<img src="' + p + '">';
    if (l > 1) {
      if (p == k) {
        e.hidden = true;
        var n = false;
        var g = f.nextElementSibling;
      } else {
        if (p == q) {
          b.hidden = true;
          var g = false;
          var n = f.previousElementSibling;
        } else {
          var n = f.previousElementSibling;
          var g = f.nextElementSibling;
        }
      }
    } else {
      e.hidden = true;
      b.hidden = true;
    }
    a.addEventListener("click", function (s) {
      if (s.target == this || s.target == r) {
        m();
      }
    });
    root.addEventListener("keydown", function (s) {
      if (s.keyCode == 37 || s.keyCode == 38) {
        d();
      }
      if (s.keyCode == 39 || s.keyCode == 40) {
        j();
      }
      if (s.keyCode == 27) {
        m();
      }
    });
    e.addEventListener("click", d);
    b.addEventListener("click", j);
    function d() {
      n = f.previousElementSibling;
      o.innerHTML = '<img src="' + n.src + '">';
      f = f.previousElementSibling;
      var s = document.querySelector(".gg-image > img").src;
      b.hidden = false;
      e.hidden = s === k;
    }
    function j() {
      g = f.nextElementSibling;
      o.innerHTML = '<img src="' + g.src + '">';
      f = f.nextElementSibling;
      var s = document.querySelector(".gg-image > img").src;
      e.hidden = false;
      b.hidden = s === q;
    }
    function m() {
      root.style.overflow = "auto";
      a.remove();
    }
  });
}
function gridGallery(a) {
  if (a.selector) {
    selector = document.querySelector(a.selector);
  }
  if (a.darkMode) {
    selector.setAttribute("data-theme", "dark");
  }
  if (a.layout == "horizontal" || a.layout == "square") {
    selector.setAttribute("data-layout", a.layout);
  }
  if (a.gaplength) {
    selector.style.setProperty("--gap-length", a.gaplength + "px");
  }
  if (a.rowHeight) {
    selector.style.setProperty("--row-height", a.rowHeight + "px");
  }
  if (a.columnWidth) {
    selector.style.setProperty("--column-width", a.columnWidth + "px");
  }
}
