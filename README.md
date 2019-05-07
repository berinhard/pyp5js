## pyp5js: Python to P5.js Transcriptor

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
### [Documentation](https://github.com/berinhard/pyp5js/blob/master/docs/index.md)

- [Examples](https://berinhard.github.io/pyp5js/examples/)

#### [Installation](https://github.com/berinhard/pyp5js/blob/master/docs/index.md#installation)

#### [Usage](https://github.com/berinhard/pyp5js/blob/master/docs/index.md#usage)

#### [Known issues and differences to the Processing.Py and P5.js ways of doing things](known-issues-and-differences-to-the-processingpy-and-p5js-ways-of-doing-things)
