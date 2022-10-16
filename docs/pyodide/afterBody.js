const initialSketch = checkForSketch();

//// Configure ACE editor
const editor = ace.edit("text-editor");
editor.session.setMode("ace/mode/python");
editor.setFontSize(18);
editor.session.setOptions({
  tabSize: 4,
});
editor.setValue(initialSketch);

//// Update div's content with most up to date code
editor.session.on("change", function () {
  document.getElementById("id_py_code").innerHTML = editor
    .getSession()
    .getValue();
});
document.getElementById("id_py_code").innerHTML = initialSketch;

document.addEventListener("DOMContentLoaded", function () {
  //// Buttons
  const shareBtn = document.getElementById("shareBtn");
  const fullScreenBtn = document.getElementById("fullScreenBtn");
  const collapseBtn = document.getElementById("collapseBtn");
  const executeBtn = document.getElementById("executeBtn");
  const clearBtn = document.getElementById("clearBtn");

  //// Event functions
  function runCode() {
    document.getElementById("sketch-holder").innerHTML = "";
    const userCode = editor.getSession().getValue();

    // from pyp5js
    window.runSketchCode(userCode);
  }

  function cleanKeyCode(e) {
    // Shortcuts work for Ctrl or Cmd
    if (e.ctrlKey || e.metaKey) {
      return e.keyCode;
    }
  }

  function keyDown(e) {
    if (cleanKeyCode(e) === 13) {
      // Ctrl + Enter to run
      e.preventDefault();
      executeBtn.click();
    } else if (cleanKeyCode(e) === 190) {
      // Ctrl + . to clear
      e.preventDefault();
      clearBtn.click();
    }
  }

  executeBtn.addEventListener("click", () => {
    if (window.instance) {
      runCode();
    } else {
      window.alert(
        "Pyodide is still loading.\nPlease, wait a few seconds and try to run it again."
      );
    }
  });
  clearBtn.addEventListener("click", () => {
    if (window.instance) {
      document.getElementById("sketch-holder").innerHTML = "";
      window.instance.remove();
    }
  });
  shareBtn.addEventListener("click", () => {
    if (window.instance) {
      const sketchUrl = createSketchUrl();
      copyTextToClipboard(sketchUrl);
      shareBtn.textContent = "Copied URL!";
      setTimeout(() => {
        shareBtn.textContent = "Share";
      }, 3000);
      runCode();
    }
  });
  fullScreenBtn.addEventListener("click", () => {
    const fullScreenSketchUrl = createSketchUrl(true);
    window.location = fullScreenSketchUrl;
  });
  collapseBtn.addEventListener("click", () => {
    const textEditorEl = document.getElementById("text-editor");
    textEditorEl.classList.toggle("hidden-editor");
    collapseBtn.textContent = collapseBtn.textContent.includes("Collapse")
      ? "Expand"
      : "Collapse";
  });
  document.body.addEventListener("keydown", keyDown);
});
