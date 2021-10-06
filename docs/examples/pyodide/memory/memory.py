import random

def load_image(img_file, im_dir="images",ext="png"):
    img = loadImage("%s/%s.%s" %(im_dir,img_file,ext))    
    return img
     
class Actor:
    def __init__(self,img,x=0,y=0):
        self.img = load_image(img)
        self.x = x
        self.y = y

    def draw(self):
        image(self.img,self.x,self.y)

COLS = 4
ROWS= 3
IMSIZE = 200

STATUS = []        # cells that have been clicked on
ignore = []        # cells that have been matches and are no longer in play

# Create two of each card image, then randomize before creating the board
START_IMAGES= [ "im"+str(i+1) for i in range(COLS*ROWS//2)]*2
random.shuffle(START_IMAGES)


board = []                    # initialize the board

steve = None
checkmark = None

def setup():
    global steve, checkmark
    checkmark = Actor('checkmark')
    steve = Actor('card_back')
    steve.x, steve.y = 0, 0

    for row in range(ROWS):
        new_row=[]
        for col in range(COLS):
            image_name = START_IMAGES.pop()
            temp=Actor(image_name, col*IMSIZE, row*IMSIZE)
            temp.image_name = image_name # used to verify matches
            new_row.append(temp)
        board.append(new_row)
        createCanvas(COLS * IMSIZE, ROWS * IMSIZE)
        
def draw():
    background(200)
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) in ignore:    # already matched
                checkmark.x, checkmark.y = IMSIZE * col, IMSIZE * row
                checkmark.draw()
            elif (row, col) in STATUS:    # clicked this move: show face
                board[row][col].draw()
            else:                        # regular clickable card
                steve.x, steve.y = IMSIZE * col, IMSIZE * row
                steve.draw()

def findTile(pos):
    y, x = pos
    result = x // IMSIZE , y // IMSIZE
    return result


def mousePressed():
    global STATUS, ignore
    if len(STATUS) == 2:
        STATUS = []
    pos = (mouseX, mouseY)    
    if pos in ignore: # has already been matched
        return
    if mouseButton == LEFT:
        coords = findTile(pos)
        xc, yc = coords
        if not ((0 <= xc < ROWS) and (0 <= yc < COLS)):
            return
        if coords not in STATUS:
            STATUS.append(coords) # now they are
            if len(STATUS) == 1:  # 1st click - turn not yet over
                pass
            elif len(STATUS) == 2: # 2nd click - check for match
                (x1, y1), (x2, y2) = STATUS
                if board[x1][y1].image_name == board[x2][y2].image_name:
                    for pos in STATUS:
                        ignore.append(pos)

