from pyp5js import *

def setup():
    pass

def draw():
    pass

deviceMoved = None
deviceTurned = None
deviceShaken = None
keyPressed = None
keyReleased = None
keyTyped = None
mouseMoved = None
mouseDragged = None
mousePressed = None
mouseReleased = None
mouseClicked = None
doubleClicked = None
mouseWheel = None
touchStarted = None
touchMoved = None
touchEnded = None
windowResized = None


rect_base_size = 30
positions = []
rect_size = None

def setup():
    global rect_size

    createP("Hi! This is an example of how to use p5.dom.js with pyp5js")

    # creates a container div
    slider_div = createDiv()
    slider_div.style("display", "block")

    # creates the slider
    rect_size = createSlider(0, 600, 100)
    rect_size.style('width', '50%')

    # adds the slider to the container div
    slider_div.child(rect_size)

    createCanvas(600, 600)

    for x in range(-rect_base_size, width + rect_base_size, rect_base_size):
        for y in range(-rect_base_size, height + rect_base_size, rect_base_size):
            positions.append((x, y))

    noFill()
    strokeWeight(2)
    rectMode(CENTER)


def draw():
    background(255)
    size = rect_size.value()
    for x, y in positions:
        rect(x, y, size, size)



event_functions = {
    "deviceMoved": deviceMoved,
    "deviceTurned": deviceTurned,
    "deviceShaken": deviceShaken,
    "keyPressed": keyPressed,
    "keyReleased": keyReleased,
    "keyTyped": keyTyped,
    "mouseMoved": mouseMoved,
    "mouseDragged": mouseDragged,
    "mousePressed": mousePressed,
    "mouseReleased": mouseReleased,
    "mouseClicked": mouseClicked,
    "doubleClicked": doubleClicked,
    "mouseWheel": mouseWheel,
    "touchStarted": touchStarted,
    "touchMoved": touchMoved,
    "touchEnded": touchEnded,
    "windowResized": windowResized,
}

start_p5(setup, draw, event_functions)