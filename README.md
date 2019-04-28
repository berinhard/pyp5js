## Python to P5.js Transcriptor

This project started from a proof of concept based in [Axel Tanner's "Transcrypt & p5js" blogpost](https://4nomore.net/2018/transcrypt_p5js/). The project's main goal was to use Tanner's approach combined with decorator and global variables control to enable P5.js API from being called "directly" from the Python code as clean as possible.

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


start_p5(setup, draw)
```

### Installation

The project is not under Pypi yet, so you'll have to install it from the git repo. To do so, just run:

```
$ pip install git+https://github.com/berinhard/pyp5js.git@master  # python 3 only
```

### Usage

Since you'll be writting Python code and then generating the correspondent P5.js code from it, pyp5js provides a simple command line API to help you to generate the files.

So, to start a new sketch, you'll have to run:

```
$ pytop5js new my_sketch
```

This command will create a directory with the following code structure:

```
~ my_sketch/
  ~ static /
    - p5.js
  - index.html
  - my_sketch.py
```

The `index.html` is prepared to display your sketch, so you'll have to keep on opening it to refresh see results from the code you'll add to `my_sketch.py`.

After updating your code, you'll have to run the `transcrypt` command to update the files. Run it as:

```
$ pytop5js transcrypt my_sketch
```

The way the code is now, you'll have execute from the same directory-level as the `my_sketch` one. You can't run it from inside the directory.

Both methods has a few optional arguments and you can check them by running:

```
$ pytop5js --help
```
