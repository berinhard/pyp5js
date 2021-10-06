r = None

def setup():
    global r

    createCanvas(900, 900)
    r = random(100, 700)
    noFill()

def draw():
    x, y = 100, 100
    rect(x, y, r, r)

def keyPressed():
    console.log("Key pressed event")

    if key == "n":
        global r
        r = random(100, 700)
        redraw()

def mouseDragged():
    global r
    r = random(100, 700)
    redraw()
