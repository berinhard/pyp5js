## pyp5js: drawing with Python 3

[![PyPI version](https://badge.fury.io/py/pyp5js.svg)](https://badge.fury.io/py/pyp5js)
![Continuous Integration](https://github.com/berinhard/pyp5js/workflows/Continuous%20Integration/badge.svg?branch=develop&event=push)
[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/berinhard/pyp5js/tree/main)


> [Processing](https://processing.org) ideas and Python 3 together with [P5.js](https://p5js.org) in the browser, using [Transcrypt](https://transcrypt.org/).

Python 3 drawing in the web 🐍 🐍 🐍  Try it [here](https://berinhard.github.io/pyp5js/pyodide/)!

`pyp5js` covers **all** the methods, variables and event handlers listed in [the p5.js API documentation](https://p5js.org/reference/). Here's an example of a valid Python code using p5.js API:

```python
def setup():
    createCanvas(200, 200)
    background(160)


def draw():
    fill("blue")
    background(200)
    radius = sin(frameCount / 60) * 50 + 50
    ellipse(100, 100, radius, radius)
```
<iframe src="/pyp5js/examples/sketch_000/" style="width: 200px; height: 200px; border: 0px"></iframe>

## Examples

[Click here](https://berinhard.github.io/pyp5js/examples/) to see a list of
examples generated with `pyp5js`.


## Installation

This project requires Python 3 and is now on PyPI, so you can install it with
`pip` or `pip3`, depending on your environment:

```
$ pip install pyp5js
```
(You might have to install `setuptools` first, if it's not already installed)

## Quickstart

Since you'll be writting Python code and then generating the correspondent
P5.js code from it, pyp5js provides a web application interface to help you
to generate the files.

So, to start a the application, you'll have to run:

```bash
$ pyp5js serve
```

Then point your browser to [http://localhost:5000/](http://localhost:5000/) and
create a new sketch via the browser by filling the form with the name of your
sketch. This command will compile the sketches on the
fly, so after changing/saving the sketch file you just need to reload the page
on your browser. It'll also guide you on which file you have to edit the Python code
and how to see it running after you save it.

`pyp5js` will create a new directory in your home called `sketchbook-pyp5js`.
If you don't want to save your sketch in this default directory, you can set
the environment variable `SKETCHBOOK_DIR` to point to the directory you want
to use. Or you can also run the `serve` command as:

```bash
$ SKETCHBOOK_DIR='~/my-custom-sketchbook' pyp5js serve
```

Now, have fun =]

## Internals details

The web application is an interface to reduce barriers on playing around with
`pyp5js` to newcomers and people who don't feel confortable with the terminal
interface. But if you want to use the terminal, `pyp5js` also exposes a CLI.

So, to start a new sketch, you'll have to run:

```bash
$ pyp5js new my_sketch
```

This command will create a directory with the following code structure using **p5.js 1.0.0**:

```
~ my_sketch/
  ~ static /
    - p5.js
  - index.html
  - my_sketch.py
```

The `index.html` is prepared to display your sketch, so you'll have to keep it
open in your browser (I really advise you to use
[Firefox](https://www.mozilla.org/en-US/firefox/new/)) to see results from the
code you'll add to `my_sketch.py`.

To see your app on your browser you'll need to run a Web server (opening the
"index.html" file directly won't work since [it is disabled by
default](https://github.com/berinhard/pyp5js/issues/72)) - we packaged it
already for you, just run:

```bash
$ pyp5js serve
```

If you just want to compile your code (without running the Web server) there's
the `compile` command:

```
$ pyp5js compile my_sketch
```

If you're lazy as me, you can use the `monitor` command instead of the previous
one. The command will monitor your sketch directory and keep track of any
changes on any `.py` files. When it notices a new change, it automatically runs
the compile process for you:

```
$ pyp5js monitor my_sketch
```

You can also use the `monitor` command within the `new` by running:

```
$ pyp5js new my_sketch --monitor
```

All of the command-line interface methods have a few optional arguments, such
as specifying the sketch directory. You can check them by running:

```
$ pyp5js --help
```


### Known [issues](https://github.com/berinhard/pyp5js/issues), differences to the Processing.Py and P5.js ways of doing things and limitations

- Remember to use **P5.js** method names & conventions for most things.

- There are no Py.Processing `with` context facilities for `push/pop` or `beginShape/endShape`.

- There are no `PVector` objects, with their nice syntatic operator overloaded sugar - use `p5.Vector` with `createVector()` and P5.js conventions ... for now...

- For the `mouseWheel()` event funtion, use `def mouseWheel()` with NO parameters, then, inside the function, the magic `event.delta` will have a value equivalent to the one returned by Java&Python Mode's `event.getCount()`.

- At this point, it is a known limitation that you have to "declare" global variables before `setup()` and `draw()`, maybe using `name = None`, as they can't be created inside methods.

- Not all Python libs are available when using Transcrypt because they required a JS-version to be enabled. In [this link](https://github.com/QQuick/Transcrypt/tree/master/transcrypt/modules) you can take a look in all modules Transcrypt enables.

## How can I contribute?

### Testing, testing and testing

Since pyp5js have a lot of moving parts, it would be great to have the p5.js API fully covered and tested. So, use your imagination, code your sketches and, if pyp5js breaks or starts to annoy you with something, you're very welcome to [open an issue](https://github.com/berinhard/pyp5js/issues/new) documenting your thoughts. Test it and let me know how can I improve it.

### What about these shinning examples?

If you fell confortable with that, I'd be happy to add some of your pyp5js sketches to our [examples list](https://berinhard.github.io/pyp5js/examples/)! To do so, you'll have [to fork this repository](https://help.github.com/en/articles/fork-a-repo) and add your new sketch example in the `docs/examples` directory. Once you've your sketch ready, you can [open a pull request](https://help.github.com/en/articles/about-pull-requests) and I'll take a look at it.

### I want to hack!

Okay, if you want to contribute with pyp5js's code, let's go! I really advise you to use [virtualenv with virtualenvwrapper](http://www.indjango.com/python-install-virtualenv-and-virtualenvwrapper/) or [pyenv](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial) to isolate your pyp5js fork from the rest of your system. Once you have everything ready, you can run:

```
$ git clone git@github.com:YOUR_GITHUB_PROFILE/pyp5js.git
$ mkvirtualenv pyp5js -p /usr/bin/python3  # python3 path can change depending on your system
$ cd pyp5js
$ pip install -r dev-requirements.txt
$ python setup.py develop
$ make test
```

After that, you should have the `pyp5js` command enabled and it will respect all the changes you introduce to the code. Now, a brief explanation about the code under `pyp5js` directory:

- `config` module: centralize pieces of code used to configure how `pyp5js` runs
- `cli.py`: the entrypoint for `pyp5js` commands such as `new` or `compile`
- `commands.py`: just functions responsible for the real implementations for `pyp5js` commands
- `compiler.py`: where all the magic happens!
- `exception.py`: custom exceptions used by `pyp5js`
- `monitor.py`: module with the objects used by the `monitor` command
- `pyp5js.py`: module which is imported by the sketches and integrates with P5.js API
- `sketch.py`: class to abstract Sketches' files, directories and configuration
- `template_renderers.py`: simple module with the renderization logic for the code templates like `target_sketch.py`
- `http/web_app.py`: Flask application for the web interface.

Now go [fetch yourself an issue](https://github.com/berinhard/pyp5js/issues) and happy hacking!

### References

This project started from a proof of concept based in [Axel Tanner's "Transcrypt & p5js" blogpost](https://4nomore.net/2018/transcrypt_p5js/). The source code in [this Github repo](https://github.com/berinhard/pyp5js).

The [Pyodide](https://github.com/iodide-project/pyodide) interpreter was implemented based on [Luca Damasco's experiment](https://github.com/Luxapodular/Py5.js) supported by [COSA (The Clinic for Open Source Arts)](https://www.du.edu/ahss/opensourcearts/) at the University of Denver College of Arts and Sciences.
