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
(You might have to install `setuptools` first, if it's not already installed)

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

The `index.html` is prepared to display your sketch, so you'll have to keep it open in your browser (I really advise you to use [Firefox](https://www.mozilla.org/en-US/firefox/new/)) to see results from the code you'll add to `my_sketch.py`.

After updating your code, you'll have to run the `transcrypt` command to update the files. Run it as:

```
$ pyp5js transcrypt my_sketch
```

If you're lazy as me, you can use the `monitor` command instead of the previous one. The command will monitor your sketch directory and keep track of any changes on any `.py` files. When it notices a new change, it automatically runs the transcrypt process for you. So, now you'll just have to refresh your `index.html` file in your browser to see the results.

```
$ pyp5js monitor my_sketch
```

All of the command-line interface methods have a few optional arguments, such as specifying the sketch directory. You can check them by running:

```
$ pyp5js --help
```

### Known [issues](https://github.com/berinhard/pyp5js/issues) and differences to the Processing.Py and P5.js ways of doing things

- Remember to use **P5.js** method names & conventions for most things.

- To use event functions such as `keyPressed`, `mouseDragged`, `deviceMoved`, `touchMoved`, `windowResized` and others listed in [P5.js reference manual](https://p5js.org/reference/), you have to pass more values to `start_p5` like the following snippet of code. You can check this [live demo](https://berinhard.github.io/pyp5js/examples/sketch_006/index.html) here and also the [Python code](https://github.com/berinhard/pyp5js/blob/master/docs/examples/sketch_006/index.html) for a more expressive example.

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
```

- The `p5.dom.js` library can be used, but you'll have to acess it's methods and objects with `_P5_INSTANCE_.` prefix.

- There are no Py.Processing `with` context facilities for `push/pop` or `beginShape/endShape` ... yet.

- There are no `PVector` objects, with their nice syntatic operator overloaded sugar - use `P5.Vector` with `createVector()` and P5.js conventions ... for now...

- At this point, it is a known limitation that you have to "declare" global variables before `setup()` and `draw()`, maybe using `name = None`, as they can't be created inside methods.

### How can I contribute?

#### Testing, testing and testing

Since pyp5js have a lot of moving parts, it would be great to have the p5.js API fully covered and tested. So, use your imagination, code your sketches and, if pyp5js breaks or starts to annoy you with something, you're very welcome to [open an issue](https://github.com/berinhard/pyp5js/issues/new) documenting your thoughts. Test it and let me know how can I improve it.

#### What about these shinning examples?

If you fell confortable with that, I'd be happy to add some of your pyp5js sketches to our [examples list](https://berinhard.github.io/pyp5js/examples/)! To do so, you'll have [to fork this repository](https://help.github.com/en/articles/fork-a-repo) and add your new sketch example in the `docs/examples` directory. Once you've your sketch ready, you can [open a pull request](https://help.github.com/en/articles/about-pull-requests) and I'll take a look at it.

#### I want to hack!

Okay, if you want to contribute with pyp5js's code, let's go! I really advise you to use [virtualenv with virtualenvwrapper](http://www.indjango.com/python-install-virtualenv-and-virtualenvwrapper/) or [pyenv](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial) to isolate your pyp5js fork from your the rest of your system. Once you have everything ready, you can run:

```
$ git clone git@github.com:YOUR_GITHUB_PROFILE/pyp5js.git
$ mkvirtualenv pyp5js -p /usr/bin/python3  # python3 path can change depending on your system
$ cd pyp5js
$ pip install -r dev-requirements.txt
$ python setup.py develop
$ pytest
```

After that, you should have the `pyp5js` command enabled and it will respect all the changes you introduce to the code. Now, a brief explanation about the code under `pyp5js` directory:

- `cli.py`: the entrypoint for `pyp5js` commands such as `new` or `transcrypt`
- `commands.py`: just functions responsible for the real implementations for `pyp5js` commands
- `fs.py`: classes to abstract the files and directories manipulations from the commands
- `pytop5js.py`: module which is imported by the sketches and integrates with P5.js API
- `update_pytop5js`: this script is responsible for generating the `pytop5js.py` file

I still have to add some tests to pyp5js, so I'd love help on that as well.

Now go [fetch yourself an issue](https://github.com/berinhard/pyp5js/issues) and happy hacking!
