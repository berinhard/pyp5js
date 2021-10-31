def setup():
    createCanvas(900, 900)
    stroke(27, 27, 27, 10)
    strokeWeight(2)


def draw():
    push()

    translate(width / 2, height / 2)
    v = p5.Vector.random2D()
    v.normalize()
    v.mult(random(100, 400))
    line(0, 0, v.x, v.y)

    pop()
