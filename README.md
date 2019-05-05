## Python to P5.js Transcriptor

This project started from a proof of concept based in [Axel Tanner's "Transcrypt & p5js" blogpost](https://4nomore.net/2018/transcrypt_p5js/). The project's main goal was to use Tanner's approach combined with decorator and global variables control to enable P5.js API from being called "directly" from the Python code as clean as possible.

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

Otherwise, you can install it from the project repo:

```
$ pip install git+https://github.com/berinhard/pyp5js.git@master
```

### Usage

Since you'll be writting Python code and then generating the correspondent P5.js code from it, pyp5js provides a simple command line API to help you to generate the files.

So, to start a new sketch, you'll have to run:

```
$ pyp5js new my_sketch
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
$ pyp5js transcrypt my_sketch
```

The way the code is implemented, for now, you'll have to execute it from the same directory-level where `my_sketch` is - you can't run it from inside the `my_sketch` directory.

If you're lazy as me, you can use the `monitor` command instead of the previous one. The command will monitor your sketch directory and keep track of any changes on any `.py` files. When it notices a new change, it automatically runs the transcrypt process for you. So, now you'll just have to refresh your `index.html` file to see the results.

```
$ pyp5js monitor my_sketch
```

All of the command-line interface methods have a few optional arguments and you can check them by running:

```
$ pyp5js --help
```
