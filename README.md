## pyp5js: Python to P5.js Transcriptor

[![PyPI version](https://badge.fury.io/py/pyp5js.svg)](https://badge.fury.io/py/pyp5js) [![CircleCI](https://circleci.com/gh/berinhard/pyp5js.svg?style=svg)](https://circleci.com/gh/berinhard/pyp5js)

> [Processing](https://processing.org) ideas and Python 3 together with [P5.js](https://p5js.org) in the browser, using [Transcrypt](https://transcrypt.org/).

Here's an example of a valid Python code using P5.js API:

```python
from pyp5js import *

def setup():
    createCanvas(200, 200)
    background(160)

def draw():
    fill('blue')
    background(200)
    r = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, r, r)
```

### [Documentation](https://berinhard.github.io/pyp5js)

### [Examples](https://berinhard.github.io/pyp5js/examples/)

### [Installation](https://berinhard.github.io/pyp5js#installation)

### [Quickstart](https://berinhard.github.io/pyp5js#quickstart)

### [Internals details](https://berinhard.github.io/pyp5js#internals-details)

### [Known issues and differences to the Processing.Py and P5.js ways of doing things](https://berinhard.github.io/pyp5js#known-issues-and-differences-to-the-processingpy-and-p5js-ways-of-doing-things)

### [How can I contribute?](https://berinhard.github.io/pyp5js#how-can-i-contribute)
