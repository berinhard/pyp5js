import os
import shutil

from cprint import cprint
from jinja2 import Environment, FileSystemLoader

from pyp5js.compiler import compile_sketch_js
from pyp5js.exceptions import PythonSketchDoesNotExist
from pyp5js.fs import SketchFiles
from pyp5js.http import pyp5js_web_app
from pyp5js.monitor import monitor_sketch as monitor_sketch_service
from pyp5js.templates_renderers import get_sketch_index_content


def new_sketch(sketch_name):
    """
    Creates a new sketch with the required assets and a index.html file, based on pyp5js's templates

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """
    sketch_files = SketchFiles(sketch_name)
    sketch_files.create_sketch_dir()

    templates_files = [
        (sketch_files.from_lib.base_sketch, sketch_files.sketch_py),
        (sketch_files.from_lib.p5js, sketch_files.p5js),
        (sketch_files.from_lib.p5_dom_js, sketch_files.p5_dom_js),
    ]
    for src, dest in templates_files:
        shutil.copyfile(src, dest)

    index_contet = get_sketch_index_content(sketch_files)
    with open(sketch_files.index_html, "w") as fd:
        fd.write(index_contet)

    return sketch_files


def transcrypt_sketch(sketch_name):
    """
    Transcrypt the sketch python code to javascript.

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """

    sketch_files = SketchFiles(sketch_name)
    sketch_files.validate_name()

    if not sketch_files.sketch_exists:
        raise PythonSketchDoesNotExist(sketch_files.sketch_py.resolve())

    compile_sketch_js(sketch_files)
    return sketch_files


def monitor_sketch(sketch_name):
    """
    Monitor for any change in any .py inside the sketch dir.
    For every new change, runs the transcrypt to update the js files.

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :return: file names
    :rtype: list of strings
    """

    sketch_files = SketchFiles(sketch_name)
    sketch_files.validate_name()

    if not sketch_files.sketch_exists:
        raise PythonSketchDoesNotExist(sketch_files.sketch_py.resolve())

    cprint(f"Monitoring for changes in {sketch_files.sketch_dir.resolve()}...")

    try:
        monitor_sketch_service(sketch_files)
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
