import math
from pyp5js import P5, start_p5


def setup():
    P5.createCanvas(200, 200)
    P5.background(160)


def draw():
    P5.fill('blue')
    fc = P5.frameCount
    P5.background(200)
    r = math.sin(fc/60) * 50 + 50
    P5.ellipse(100, 100, r, r)


my_p5 = start_p5(setup, draw)
