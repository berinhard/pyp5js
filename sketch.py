# https://p5js.org/examples/interaction-wavemaker.html


from pyp5js import P5, start_p5

t = 0

def setup():
    P5.createCanvas(600, 600)
    P5.noStroke()
    P5.fill(40, 200, 40)


def draw():
    global t
    width = P5.width
    height = P5.height

    P5.background(10, 10)

    xAngle = P5.map(P5.mouseX, 0, P5.width, -4 * P5.PI, 4 * P5.PI, True)
    yAngle = P5.map(P5.mouseY, 0, P5.height, -4 * P5.PI, 4 * P5.PI, True)
    for x in range(0, width, 30):
        for y in range(0, height, 30):

            angle = xAngle * (x / width) + yAngle * (y / height)

            myX = x + 20 * P5.cos(2 * P5.PI * t + angle)
            myY = y + 20 * P5.sin(2 * P5.PI * t + angle)

            P5.ellipse(myX, myY, 10)

    t = t + 0.01

    console.log(P5.frameRate())


my_p5 = start_p5(setup, draw)