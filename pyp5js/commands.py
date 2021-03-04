import os
import shutil

from cprint import cprint
from jinja2 import Environment, FileSystemLoader

from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.compiler import compile_sketch_js
from pyp5js.exceptions import PythonSketchDoesNotExist
from pyp5js.sketch import Sketch
from pyp5js.http import pyp5js_web_app
from pyp5js.monitor import monitor_sketch as monitor_sketch_service
from pyp5js.templates_renderers import get_sketch_index_content
from pyp5js.config import PYODIDE_INTERPRETER


def new_sketch(sketch_name, interpreter=PYODIDE_INTERPRETER):
    """
    Creates a new sketch with the required assets and a index.html file, based on pyp5js's templates

    :param sketch_name: name for new sketch
    :param interpreter: interpreter to use (transcrypt or pyodide)
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """
    sketch = Sketch(sketch_name, interpreter=interpreter)
    sketch.create_sketch_dir()

    templates_files = [
        (sketch.config.get_base_sketch_template(), sketch.sketch_py),
        (PYP5JS_FILES.p5js, sketch.p5js),
    ]
    for src, dest in templates_files:
        shutil.copyfile(src, dest)

    index_contet = get_sketch_index_content(sketch)
    with open(sketch.index_html, "w") as fd:
        fd.write(index_contet)

    return sketch


def compile_sketch(sketch_name):
    """
    Transcrypt the sketch python code to javascript.

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """

    sketch = Sketch(sketch_name)
    sketch.validate_name()

    if not sketch.sketch_exists:
        raise PythonSketchDoesNotExist(sketch)

    compile_sketch_js(sketch)
    return sketch


def monitor_sketch(sketch_name):
    """
    Monitor for any change in any .py inside the sketch dir.
    For every new change, runs the transcrypt to update the js files.

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """

    sketch = Sketch(sketch_name)
    sketch.validate_name()

    if not sketch.sketch_exists:
        raise PythonSketchDoesNotExist(sketch)

    cprint(f"Monitoring for changes in {sketch.sketch_dir.resolve()}...")

    try:
        monitor_sketch_service(sketch)
    except KeyboardInterrupt:
        cprint.info("Exiting monitor...")


def serve_http(host, port, debug=False):
    """
    Run a HTTP server which compiles sketches on the fly and serves static files

    :param host: server's hostname
    :type host: string
    :param port: server's port
    :type port: int
    :param debug: turn on/off debug mode
    :type debug: bool
    """
    pyp5js_web_app.run(host=host, port=port, debug=debug)
