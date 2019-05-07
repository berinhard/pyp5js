# 3d example
from pytop5js import *


def setup():
    createCanvas(600, 600, WEBGL)

def draw():
  background(200)
  translate(-100, -100, 0)
  normalMaterial()
  rotateZ(frameCount * 0.01)
  rotateX(frameCount * 0.01)
  rotateY(frameCount * 0.01)
  box(50, 70, 100)


start_p5(setup, draw)
