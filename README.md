## Python to P5.js Transcriptor

> Processing ideas and Python 3 together with P5.js in the browser, using Transcrypt.

Here's an example of a valid Python code using P5.js API:

```python
from pytop5js import *

def setup():
    createCanvas(200, 200)
    background(160)


def draw():
    fill('blue')
    background(200)
    r = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, r, r)


start_p5(setup, draw)
```

### Installation

This project requires Python 3 and is now on PyPI, so you can install it with `pip` or `pip3`, depending on your environment:

```
$ pip install pyp5js
```

### Usage and more: hit the [docs](/docs/index.md)!


```
