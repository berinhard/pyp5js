from pyp5js import *


MY_POINTS = [
    (100, 50),
    (300, 100),
    (200, 300),
    (100, 300),
]
FRAME_IDX = 0
POINT_SIZE = 10
CNV = None

def setup():
    global CNV
    CNV = createCanvas(400, 400)

    BUTTON_PREV = createButton('Previous frame')
    BUTTON_PREV.position(CNV.position().x,
                         CNV.height + CNV.position().y)
    BUTTON_PREV.mousePressed(prev_frame)

    BUTTON_NEXT = createButton('Next frame')
    BUTTON_NEXT.position(CNV.position().x + BUTTON_PREV.size().width,
                         BUTTON_PREV.position().y)
    BUTTON_NEXT.mousePressed(next_frame)

    background(190)
    draw_labels(MY_POINTS)

def draw():
    background(190)
    draw_closed_curve_vertex(MY_POINTS, FRAME_IDX)
    draw_labels(MY_POINTS)

def mouseClicked():
    global FRAME_IDX
    global MY_POINTS
    if is_point_in_canvas(mouseX, mouseY):
        i = get_point_index(mouseX, mouseY)
        if i != None:
            MY_POINTS.pop(i)
            if FRAME_IDX >= len(MY_POINTS):
                # cap i if it exceeds maximum length now.
                FRAME_IDX = len(MY_POINTS) - 1
        else:
            MY_POINTS.append((mouseX, mouseY))

def get_point_index(x, y):
    for idx, (p_x,p_y) in enumerate(MY_POINTS):
        if (p_x - POINT_SIZE < x and x < p_x + POINT_SIZE) and \
           (p_y - POINT_SIZE < y and y < p_y + POINT_SIZE):
            return idx

def is_point_in_canvas(x, y):
    if (x < 0 or x > CNV.width) or \
       (y < 0 or y > CNV.height):
        return False
    return True

def next_frame():
    global FRAME_IDX
    if FRAME_IDX < len(MY_POINTS) - 1:
        FRAME_IDX += 1

def prev_frame():
    global FRAME_IDX
    if FRAME_IDX > 0:
        FRAME_IDX -= 1

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
    text('Points used to draw this curve (first and last are control points only)', 5, CNV.height - 30)

    textSize(20)
    text(', '.join(used_points), 10, CNV.height - 10)
    stroke(0)

    for i in range(len(used_points) - 1):
        draw_dotted_line(points[used_points[i]],
                         points[used_points[i + 1]])

def draw_labels(points):
    strokeWeight(POINT_SIZE)
    for idx, p in enumerate(points):
        ts = 32
        textSize(ts)
        textY = p[1] - ts / 2

        if p[1] > CNV.height / 2:
            textY = p[1] + ts

        noStroke()
        text(idx, p[0], textY)
        stroke(0)
        point(*p)

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
