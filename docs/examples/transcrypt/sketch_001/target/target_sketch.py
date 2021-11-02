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


# https://p5js.org/examples/interaction-wavemaker.html

t = 0

def setup():
    createCanvas(600, 600)
    stroke(250)
    strokeWeight(3)
    fill(40, 200, 40)


def draw():
    global t
    background(10, 10)

    xAngle = map(mouseX, 0, width, -4 * PI, 4 * PI, True)
    yAngle = map(mouseY, 0, height, -4 * PI, 4 * PI, True)
    for x in range(0, width, 30):
        for y in range(0, height, 30):

            angle = xAngle * (x / width) + yAngle * (y / height)

            myX = x + 20 * cos(2 * PI * t + angle)
            myY = y + 20 * sin(2 * TWO_PI * t + angle)

            ellipse(myX, myY, 10)

    t = t + 0.01



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