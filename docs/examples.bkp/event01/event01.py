def setup():
    createCanvas(200, 200)
    background(160)
    fill("blue")


def draw():
    background(200)
    radius = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, radius, radius)
    
    
def mouseClicked():
    print('mouse clicked')


def keyPressed(e):
    print(keyPressed)
    fill('red')
    print(e)        
    print(key)