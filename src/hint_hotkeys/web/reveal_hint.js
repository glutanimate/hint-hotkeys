/**
 *
 * @param {boolean} revealAll
 */
function hintHotkeysRevealHints(revealAll) {
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

  const hintElements = document.getElementsByClassName("hint");
  for (var i = 0; i < hintElements.length; i++) {
    let hint = hintElements[i];
    if (hint.style.display === "none" || hint.href === undefined) {
      continue;
    }
    if (hint.href.charAt(hint.href.length - 1) === "#") {
      hint.dispatchEvent(clickEvent);
      if (!revealAll) {
        break;
      }
    }
  }
}
