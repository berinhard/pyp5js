from pyp5js import *

def preload():
    pass

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
keyIsDown = None


from random import choice


images = []

def setup():
    global images

    createP("Click to add a new image")
    createCanvas(600, 600)
    background(200)
    images = [
        loadImage('smile.png'),
        loadImage('alien.png'),
        loadImage('rainbow.png'),
    ]


def mousePressed():
    x, y = mouseX, mouseY
    img = choice(images)
    image(img, x, y)


def draw():
    pass



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
    "keyIsDown": keyIsDown,
}

start_p5(preload, setup, draw, event_functions)