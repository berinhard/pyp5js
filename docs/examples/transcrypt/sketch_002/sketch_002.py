"""
 * Move Eye.
 * by Simon Greenwold.
 *
 * The camera lifts up (controlled by mouseY) while looking at the same point.
 """

def setup():
    createCanvas(640, 360, _P5_INSTANCE.WEBGL)
    fill(204)


def draw():
    ambientLight(50)
    directionalLight(255, 0, 0, 0.25, 0.25, 0);
    background(0)

    # Change height of the camera with mouseY
    camera(30.0, mouseY, 220.0,  # eyeX, eyeY, eyeZ
           0.0, 0.0, 0.0,        # centerX, centerY, centerZ
           0.0, 1.0, 0.0)        # upX, upY, upZ

    noStroke()
    box(90)
    stroke(255)
    line(-100, 0, 0, 100, 0, 0)
    line(0, -100, 0, 0, 100, 0)
    line(0, 0, -100, 0, 0, 100)
