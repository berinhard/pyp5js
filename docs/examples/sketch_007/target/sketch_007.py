from pytop5js import *


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


# ==== This is required by pyp5js to work

# Register your events functions here
event_functions = {
    # "keyPressed": keyPressed,    as an example
}
start_p5(setup, draw, event_functions)
