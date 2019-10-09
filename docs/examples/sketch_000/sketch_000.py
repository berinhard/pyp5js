from pyp5js import *

def setup():
    createCanvas(200, 200)
    background(160)

def draw():
    fill('blue')
    background(200)
    r = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, r, r)
