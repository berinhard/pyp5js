from pyp5js import *


def setup():
    createCanvas(200, 200)
    background(160)


def draw():
    fill("blue")
    background(200)
    radius = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, radius, radius)
