x = 50
y = 100
rad = 6

vx = 5
vy = 5

WIDTH = 640
HEIGHT = 400
FPS = 60

def setup():
    createCanvas(WIDTH, HEIGHT)
    frameRate(FPS)

def draw():
    global x, y, vx, vy
    
    background(220)
    fill(0, 255, 0)
    ellipse(x, y, 2 * rad)

    x += vx
    y += vy
  
    if (x + rad >= width or x - rad <= 0):
        vx = -vx
    
    if (y + rad >= height or y - rad <= 0):
        vy = -vy
