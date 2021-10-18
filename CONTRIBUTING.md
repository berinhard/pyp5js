## Contributing to pyp5js

Here you'll find all possible ways to contribute to the project.

### Testing, testing and testing

Since pyp5js have a lot of moving parts, it would be great to have the p5.js API fully covered and tested. So, use your imagination, code your sketches and, if pyp5js breaks or starts to annoy you with something, you're very welcome to [open an issue](https://github.com/berinhard/pyp5js/issues/new) documenting your thoughts. Test it and let me know how can I improve it.

### What about these shinning examples?

If you fell confortable with that, I'd be happy to add some of your pyp5js sketches to our [examples list](https://berinhard.github.io/pyp5js/examples/)! To do so, you'll have [to fork this repository](https://help.github.com/en/articles/fork-a-repo) and add your new sketch example in the `docs/examples` directory. Once you've your sketch ready, you can [open a pull request](https://help.github.com/en/articles/about-pull-requests) and I'll take a look at it.

### I want to hack!

Okay, if you want to contribute with pyp5js's code, let's go! I really advise you to use [virtualenv with virtualenvwrapper](http://www.indjango.com/python-install-virtualenv-and-virtualenvwrapper/) or [pyenv](https://amaral.northwestern.edu/resources/guides/pyenv-tutorial) to isolate your pyp5js fork from the rest of your system. Once you have everything ready, you can run:

```
$ git clone git@github.com:YOUR_GITHUB_PROFILE/pyp5js.git
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
- `sketch.py`: class to abstract Sketches' files, directories and configuration
- `template_renderers.py`: simple module with the renderization logic for the code templates like `target_sketch.py`
- `http/web_app.py`: Flask application for the web interface.

Now go [fetch yourself an issue](https://github.com/berinhard/pyp5js/issues) and happy hacking!
