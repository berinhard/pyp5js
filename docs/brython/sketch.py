def setup():
  createCanvas(400, 400)
  rectMode(CENTER)


def draw():
  background('dodgerblue')
  fill('#ff1e8e')
  stroke('#8eff1e')
  strokeWeight(2)
  pattern(width * 0.5, height * 0.5, width * 2 / (1 + sqrt(5)))


def pattern(x, y, d):
  square(x, y, d)
  if d < 10:
    return

  smaller = d * 2 / (1 + sqrt(5))
  pattern(x, y, smaller)
