## pyp5js: drawing with Python 3

[![PyPI version](https://badge.fury.io/py/pyp5js.svg)](https://badge.fury.io/py/pyp5js)
![Continuous Integration](https://github.com/berinhard/pyp5js/workflows/Continuous%20Integration/badge.svg?branch=develop&event=push)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berinhard/pyp5js/tree/main)

> [Processing](https://processing.org) ideas and Python 3 together with [P5.js](https://p5js.org) in the browser.

Python 3 drawing in the web! Try it [here](https://berinhard.github.io/pyp5js/pyodide/)!

Here's an example of a valid Python code using P5.js API:

```python
def setup():
    createCanvas(200, 200)

def draw():
    background(200)
    diameter = sin(frameCount / 60) * 50 + 50
    fill('blue')
    ellipse(100, 100, diameter, diameter)
```

## Project setup

```
$ git clone git@github.com:YOUR_GITHUB_PROFILE/pyp5js.git
$ cd pyp5js
$ pip install -r dev-requirements.txt
$ python setup.py develop
$ make test
```

## More references

### [Documentation](https://berinhard.github.io/pyp5js)

### [Examples](https://berinhard.github.io/pyp5js/examples/)

### [Installation](https://berinhard.github.io/pyp5js#installation)

### [Quickstart](https://berinhard.github.io/pyp5js#quickstart)

### [Internals details](https://berinhard.github.io/pyp5js#internals-details)

### [Known issues and differences to the Processing.Py and P5.js ways of doing things](https://berinhard.github.io/pyp5js#known-issues-and-differences-to-the-processingpy-and-p5js-ways-of-doing-things)

### [How can I contribute?](https://berinhard.github.io/pyp5js#how-can-i-contribute)
