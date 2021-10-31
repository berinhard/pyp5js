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
