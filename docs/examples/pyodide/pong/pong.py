RAD =    10
P_RAD =  30
WIDTH =  600
HEIGHT = 300

class Ball:
    def __init__self(x, y, sx, sy): 
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        
    def draw(self):
        circle(self.x, self.y, 2 * RAD)
        
    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.sx = 4
        self.sy = 0
        self.play = True

ball = Ball()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def reset(self):
        self.y = HEIGHT // 2

    def set_pos(self,y):
        self.y = min(HEIGHT, max(y, 0))

    def draw(self):
        strokeWeight(2)
        line(self.x, self.y - P_RAD, self.x, self.y + P_RAD)


player1 = Player(10, HEIGHT // 2)
player2 = Player(WIDTH - 10, HEIGHT // 2)

game = None

def setup():
    global game
    createCanvas(WIDTH, HEIGHT)
    stroke(255)
    fill(255)
    game = Game()
    game.reset()
    
class Game:
    def __init__(self):
        self.over = False
  
    def reset(self):
        self.over = False
        ball.reset()
        player1.reset()
        player2.reset()

    def tick(self):
        if not self.over:
        #  y: keep ball inside of vertical bounds
            if (ball.y < 10) or (ball.y > height - 10): 
                ball.sy *= -1

            ball.y += ball.sy

            # x: player 2
            if (ball.x + RAD >= player2.x):
                ball.sx *= -1

            # x: player 1
            if (ball.x - RAD <= player1.x):
                if ((ball.y > player1.y - P_RAD) and
                    (ball.y < player1.y + P_RAD)):
                    # player 1 hits the ball

                    # bounce back
                    ball.sx *= -1
                    # get ball-paddle angle
                    angle = ball.y - player1.y
                    ball.sy = angle / 9
                    ball.sx = map(abs(angle), 0, P_RAD, 3, 9)

                else:
                    # player misses the ball
                    self.over = True
              
        if (ball.x < -100):
                game.reset()    
        ball.x += ball.sx
        ball.draw()


def draw(): 
    if not game.over:
        background(0)
    else:
        background(255,0,0)

    player1.set_pos(mouseY)
    player1.draw()

    player2.set_pos(ball.y)
    player2.draw()

    game.tick()
