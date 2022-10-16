document.getElementById("returnBtn").addEventListener("click", () => {
  const currentSketchParam = new URLSearchParams(window.location.search);
  const pathname = window.location.pathname.replace(/fullscreen.html/g, "");
  const baseUrl = new URL(window.location.origin + pathname);
  window.location = `${baseUrl}?sketch=${currentSketchParam.get("sketch")}`;
});
