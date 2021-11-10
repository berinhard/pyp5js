function createSketchUrl() {
  const baseUrl = window.location.origin;
  const userCode = editor.getSession().getValue();

  const encodedUserCode = btoa(encodeURIComponent(userCode));

  const sketchUrl = new URL(baseUrl);
  sketchUrl.searchParams.append("sketch", encodedUserCode);

  return sketchUrl;
}

function decodeSketchUrl(encodedSketch) {
  const decodedSketch = decodeURIComponent(atob(encodedSketch));

  return decodedSketch;
}

function checkForSketch() {
  let initialSketch = `def setup():
    createCanvas(200, 200)

def draw():
    background(200)
    diameter = sin(frameCount / 60) * 50 + 50
    fill("blue")
    ellipse(100, 100, diameter, diameter)
    `;

  const currentUrl = new URLSearchParams(window.location.search);

  if (currentUrl.has("sketch")) {
    initialSketch = decodeSketchUrl(currentUrl.get("sketch"));
  }

  return initialSketch;
}
