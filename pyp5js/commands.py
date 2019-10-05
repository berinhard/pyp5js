import os
import shutil

from cprint import cprint
from jinja2 import Environment, FileSystemLoader

from pyp5js.compiler import compile_sketch_js
from pyp5js.fs import SketchFiles
from pyp5js.monitor import monitor_sketch as monitor_sketch_service
from pyp5js.templates_renderer import get_index_content
from pyp5js.http import SketchesWebApplication


def new_sketch(sketch_name, sketch_dir):
    """
    Creates a new sketch, on a folder/directory
    with the required assets and a index.html file,
    all based on a template

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :param sketch_dir: directory name
    :type sketch_dir: string
    :return: file names
    :rtype: list of strings
    """

    sketch_files = SketchFiles(sketch_dir, sketch_name, check_sketch_dir=False)
    if not sketch_files.can_create_sketch():
        cprint.warn(f"Cannot configure a new sketch.")
        cprint.err(f"The directory {sketch_files.sketch_dir} already exists.", interrupt=True)

    templates_files = [
        (sketch_files.from_lib.base_sketch, sketch_files.sketch_py),
        (sketch_files.from_lib.p5js, sketch_files.p5js),
        (sketch_files.from_lib.p5_dom_js, sketch_files.p5_dom_js),
    ]

    os.makedirs(sketch_files.sketch_dir)
    sketch_files.static_dir.mkdir()
    for src, dest in templates_files:
        shutil.copyfile(src, dest)

    index_contet = get_index_content(sketch_name)
    with open(sketch_files.index_html, "w") as fd:
        fd.write(index_contet)

    return sketch_files.sketch_py, sketch_files.index_html


def transcrypt_sketch(sketch_name, sketch_dir):
    """
    Transcrypt the sketch python code to javascript.

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :param sketch_dir: directory name
    :type sketch_dir: string
    :return: file names
    :rtype: list of strings
    """

    sketch_files = SketchFiles(sketch_dir, sketch_name)
    if not sketch_files.check_sketch_exists():
        cprint.err(f"Couldn't find {sketch_name}", interrupt=True)

    compile_sketch_js(sketch_files)
    return sketch_files.index_html


def monitor_sketch(sketch_name, sketch_dir):
    """
    Monitor for any change in any .py code under
    the sketch dir and, for every new change,
    runs the transcrypt to update the js files.

    :param sketch_name: name for new sketch
    :type sketch_name: string
    :param sketch_dir: directory name
    :type sketch_dir: string
    :return: file names
    :rtype: list of strings
    """

    sketch_files = SketchFiles(sketch_dir, sketch_name)
    if not sketch_files.check_sketch_exists():
        cprint.err(f"Couldn't find {sketch_name}", interrupt=True)

    cprint(f"Monitoring for changes in {sketch_files.sketch_dir.absolute()}...")

    try:
        monitor_sketch_service(sketch_files)
    except KeyboardInterrupt:
        cprint.info("Exiting monitor...")


def serve_http(sketches_path, host, port, workers):
    """
    Run a HTTP server which compiles sketches on the fly and serves static files

    :param sketches_path: directory to search for sketches
    :type sketches_path: pathlib.Path
    :param host: server's hostname
    :type host: string
    :param port: server's port
    :type port: int
    :param workers: number of workers
    :type workers: int
    """
    options = {"bind": f"{host}:{port}", "workers": workers}
    SketchesWebApplication(sketches_path, options).run()
