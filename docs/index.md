## pyp5js: Python to P5.js Transcriptor

> [Processing](https://processing.org) ideas and Python 3 together with [P5.js](https://p5js.org) in the browser, using [Transcrypt](https://transcrypt.org/).

This project started from a proof of concept based in [Axel Tanner's "Transcrypt & p5js" blogpost](https://4nomore.net/2018/transcrypt_p5js/).

The project's main goal was to use Tanner's approach combined with decorator and global variables control to enable P5.js API from being called "directly" from the Python code as clean as possible.

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


start_p5(setup, draw, {})
```
### More Examples
[Click here](https://berinhard.github.io/pyp5js/examples/) to see a list of examples generated with `pyp5js`.


### Installation

This project requires Python 3 and is now on PyPI, so you can install it with `pip` or `pip3`, depending on your environment:

```
$ pip install pyp5js
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

If you're lazy as me, you can use the `monitor` command instead of the previous one. The command will monitor your sketch directory and keep track of any changes on any `.py` files. When it notices a new change, it automatically runs the transcrypt process for you. So, now you'll just have to refresh your `index.html` file to see the results.

```
$ pyp5js monitor my_sketch
```

All of the command-line interface methods have a few optional arguments and you can check them by running:

```
$ pyp5js --help
```

### Known [issues](https://github.com/berinhard/pyp5js/issues) and differences to the Processing.Py and P5.js ways of doing things

- Remember to use **P5.js** method names & conventions for most things.

- To use event functions such as `keyPressed`, 'mouseDragged`, `deviceMoved`, `touchMoved`, `windowResized` and others listed in [P5.js reference manual](https://p5js.org/reference/), you have to pass more values to `start_p5` like the following snippet of code. You can check this [live demo](https://berinhard.github.io/pyp5js/examples/sketch_006/index.html) here and also the [Python code](https://github.com/berinhard/pyp5js/blob/master/docs/examples/sketch_003/index.html) for a more expressive example.

```
def keyPressed():
    ### your keyPressed implementation


def mouseDragged():
    ### your mouseDragged implementation

event_functions = {
    'keyPressed': keyPressed,
    'mouseDragged': mouseDragged,
}
start_p5(setup, draw, event_functions)
``

- The `p5.dom.js` library can be used, but you'll have to acess it's methods and objects with `_P5_INSTANCE_.` prefix.

- There are no Py.Processing `with` context facilities for `push/pop` or `beginShape/endShape` ... yet.

- There are no `PVector` objects, with their nice syntatic operator overloaded sugar - use `P5.Vector` with `createVector()` and P5.js conventions ... for now...

- At this point, it is a known limitation that you have to "declare" global variables before `setup()` and `draw()`, maybe using `name = None`, as they can't be created inside methods.

### How can I contribute?

Test it! Have a look at the issues... open a new one if needed.

More instructions, like how to submit a Pull Request, will be available soon.
