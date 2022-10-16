document.getElementById("returnBtn").addEventListener("click", () => {
  const currentSketchParam = new URLSearchParams(window.location.search);
  const baseUrl = new URL(window.location.origin);
  window.location = `${baseUrl}?${currentSketchParam}`;
});
