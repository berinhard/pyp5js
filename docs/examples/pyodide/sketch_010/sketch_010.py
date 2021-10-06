MY_POINTS = [(100, 50), (300, 100), (200, 300), (100, 300)]

WIDTH =  400
HEIGHT = 400
FRAME_IDX = 0
POINT_SIZE = 10
BUTT_Y = HEIGHT
BUTT_PREV_X = 0
BUTT_NEXT_X = WIDTH // 2
BUTT_WIDTH  = WIDTH // 2 - 1
BUTT_HEIGHT = 30

buttons = {"prev": (BUTT_PREV_X, BUTT_Y, BUTT_WIDTH, BUTT_HEIGHT),
           "next": (BUTT_NEXT_X, BUTT_Y, BUTT_WIDTH, BUTT_HEIGHT)} # x, y, w, h
cnv = None

def setup():

    global cnv
    cnv = createCanvas(400, 400)

    button_prev = createButton('Previous frame')
    button_prev.position(BUTT_PREV_X, BUTT_Y)
    button_prev.size(BUTT_WIDTH,BUTT_HEIGHT)
    
    button_next = createButton('Next frame')
    button_next.position(BUTT_NEXT_X, BUTT_Y)
    button_next.size(BUTT_WIDTH,BUTT_HEIGHT)
    
    background(190)
    draw_labels(MY_POINTS)

def inButton(butt_kind, x, y):
    try:
        bx, by, bw, bh = buttons[butt_kind]
    except:
        return False
    return (bx < x < bx + bw ) and (by < y < by + bh)
     
def draw():
    background(190)
    draw_closed_curve_vertex(MY_POINTS, FRAME_IDX)
    draw_labels(MY_POINTS)

def mouseClicked():
    global FRAME_IDX
    global MY_POINTS
    x, y = mouseX, mouseY
    if inCanvas(x, y):
        i = get_point_index(y, y)
        if i != None:
            MY_POINTS.pop(i)
            if FRAME_IDX >= len(MY_POINTS):
                # cap i if it exceeds maximum length now.
                FRAME_IDX = len(MY_POINTS) - 1
        else:
            MY_POINTS.append((x, y))
    elif inButton("prev", x, y):
        FRAME_IDX = max(0, FRAME_IDX - 1)
    elif inButton("next", x, y):
        FRAME_IDX = min(len(MY_POINTS) -1, FRAME_IDX + 1) 
    
def get_point_index(x, y):
    for idx, (p_x, p_y) in enumerate(MY_POINTS):
        if ((p_x - POINT_SIZE < x < p_x + POINT_SIZE) and 
            (p_y - POINT_SIZE < y < p_y + POINT_SIZE)):
            return idx

def inCanvas(x, y):
    return  (0 <=  x <= WIDTH) and (0 <= y <= HEIGHT)


def draw_closed_curve_vertex(points, max_idx):
    if len(points) < 2:
        return
    used_points = []
    beginShape()

    # start by using the last point as the initial control point
    idx = len(points) - 1
    curveVertex(*points[idx])
    used_points.append(idx)

    # add each point to the curve
    for idx,p in enumerate(points):
        if idx > max_idx:
            break
        curveVertex(*p)
        used_points.append(idx)

    # to close the curve, we need to create the last curve.
    # for that, we must go to the first point
    idx = 0
    curveVertex(*points[idx])
    used_points.append(idx)

    # and use the next point as a control point.
    idx = 1
    curveVertex(*points[idx])
    used_points.append(idx)
    endShape()

    textSize(10)
    noStroke()
    text('Points used to draw this curve (first and last are control points only)', 5, cnv.height - 30)

    textSize(20)
    text(', '.join([str(p) for p in used_points]), 10, cnv.height - 10)
    stroke(0)

    for i in range(len(used_points) - 1):
        draw_dotted_line(points[used_points[i]],
                         points[used_points[i + 1]])

def draw_labels(points):
    strokeWeight(POINT_SIZE)
    for idx, (px, py) in enumerate(points):
        ts = 32
        textSize(ts)
        textY = py - ts / 2

        if py > cnv.height / 2:
            textY = py + ts

        noStroke()
        text(idx, px, textY)
        stroke(0)
        point(px, py)

    strokeWeight(1)

def draw_dotted_line(p1, p2):
    stroke(100)
    strokeWeight(3)
    for i in range(11):
        x = lerp(p1[0], p2[0], i/10)
        y = lerp(p1[1], p2[1], i/10)
        point(x, y)

    stroke(0)
    strokeWeight(1)
