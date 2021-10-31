x = 50
y = 100
diam = 10

vx = 2
vy = 2
framecount = 0

WIDTH = 640
HEIGHT = 400
FPS = 60
afps = FPS

def setup():
    createCanvas(WIDTH, HEIGHT)
    frameRate(FPS)
    
def draw():
    global x, y, vx, vy, framecount, afps
    
    background(220)
    fill(255, 0, 0)
    ellipse(x, y, diam)
    framecount += 1
    if not framecount % FPS:
        afps = frameRate() 
    fill(10)
    textSize(20)
    text("FPS: %.1f" %afps, 30, HEIGHT - 24)
    x += vx
    y += vy
  
    if (x + diam // 2 >= width or x - diam // 2 <= 0):
        vx = -vx
    
    if (y + diam // 2 >= height or y - diam // 2 <= 0):
        vy = -vy
      
