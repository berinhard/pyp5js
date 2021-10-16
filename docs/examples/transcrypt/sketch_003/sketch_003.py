# 3d example


def setup():
    createCanvas(600, 600, WEBGL)

def draw():
    background(200)
    translate(-100, -100, 0)
    push()
    normalMaterial()
    rotateZ(frameCount * 0.01)
    rotateX(frameCount * 0.01)
    rotateY(frameCount * 0.01)
    box(50, 70, 100)
    pop()
