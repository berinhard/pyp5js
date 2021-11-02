import os
import shutil

from cprint import cprint
from jinja2 import Environment, FileSystemLoader

from pyp5js.compiler import compile_sketch_js
from pyp5js.exceptions import PythonSketchDoesNotExist
from pyp5js.sketch import Sketch
from pyp5js.http import pyp5js_web_app
from pyp5js.monitor import monitor_sketch as monitor_sketch_service
from pyp5js.templates_renderers import get_sketch_index_content
from pyp5js.config import PYODIDE_INTERPRETER


def new_sketch(sketch_name, interpreter=PYODIDE_INTERPRETER, template_file="", use_cdn=True):
    """
    Creates a new sketch with the required assets and a index.html file, based on pyp5js's templates

    :param sketch_name: name for new sketch
    :param interpreter: interpreter to use (transcrypt or pyodide)
    :param template_file: use a custom template for index.html instead of default one
    :param use_cdn: if false, the sketch will have copies of required static assets (p5.js and pyodide)
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """
    cfg = {
        "interpreter": interpreter,
        "index_template": template_file,
    }

    sketch = Sketch(sketch_name, **cfg)
    sketch.create_sketch_dir()
    sketch.copy_initial_files(use_cdn=use_cdn)

    index_contet = get_sketch_index_content(sketch)
    with open(sketch.index_html, "w", encoding="utf-8") as fd:
        fd.write(index_contet)

    return sketch


def compile_sketch(sketch_name, generate_index=False, index_template=None, force_local=False):
    """
    Transcrypt the sketch python code to javascript.

    :param sketch_name: name for new sketch
    :param generate_index: boolean to flag if the index.html file should be updated
    :param force_local: boolean to flag to force local run (used by web editor only)
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """

    sketch = Sketch(sketch_name)
    sketch.validate_name()

    if not sketch.sketch_exists:
        raise PythonSketchDoesNotExist(sketch)

    compile_sketch_js(sketch, force_local=force_local)
    if generate_index:
        # to be able to overwrite default index template file
        # useful for generating the docs or debugging
        sketch.config.index_template = index_template
        index_contet = get_sketch_index_content(sketch)
        with open(sketch.index_html, "w", encoding="utf-8") as fd:
            fd.write(index_contet)
        cprint.info(f"{sketch.index_html.resolve()} updated")

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
