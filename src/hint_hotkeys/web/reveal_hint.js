/**
 *
 * @param {boolean} incremental
 */
function hintHotkeysRevealHints(incremental) {
  // Cloze Overlapper support
  if (typeof olToggle === "function") {
    olToggle();
  }

  // Image Occlusion Enhanced support
  const ioBtn = document.getElementById("io-revl-btn");
  if (!(typeof ioBtn === "undefined" || !ioBtn)) {
    ioBtn.click();
  }

  let clickEvent = new MouseEvent("click", {
    view: window,
    bubbles: true,
    cancelable: true,
  });

  const arr = document.getElementsByClassName("hint");
  for (var i = 0; i < arr.length; i++) {
    let l = arr[i];
    if (l.style.display === "none") {
      continue;
    }
    if (l.href.charAt(l.href.length - 1) === "#") {
      l.dispatchEvent(clickEvent);
      if (incremental) {
        break;
      }
    }
  }
}
