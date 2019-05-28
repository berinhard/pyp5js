import os
import shutil
from cprint import cprint
from jinja2 import Environment, FileSystemLoader

from pyp5js import compiler
from pyp5js.fs import Pyp5jsSketchFiles, Pyp5jsLibFiles


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

    sketch_files = Pyp5jsSketchFiles(sketch_dir, sketch_name, check_sketch_dir=False)
    if not sketch_files.can_create_sketch():
        cprint.warn(f"Cannot configure a new sketch.")
        cprint.err(f"The directory {sketch_files.sketch_dir} already exists.", interrupt=True)

    pyp5js_files = Pyp5jsLibFiles()
    templates_files = [
        (pyp5js_files.base_sketch, sketch_files.sketch_py),
        (pyp5js_files.p5js, sketch_files.p5js)
    ]

    context = {
        "p5_js_url": f"{Pyp5jsSketchFiles.STATIC_NAME}/p5.js",
        "sketch_js_url": f"{Pyp5jsSketchFiles.TARGET_NAME}/{sketch_name}.js",
        "sketch_name": sketch_name,
    }

    templates = Environment(loader=FileSystemLoader(pyp5js_files.templates_dir))
    index_template = templates.get_template(
        str(pyp5js_files.index_html.name)
    )
    index_contet = index_template.render(context)

    os.makedirs(sketch_files.sketch_dir)
    os.mkdir(sketch_files.static_dir)
    for src, dest in templates_files:
        shutil.copyfile(src, dest)

    with open(sketch_files.index_html, "w") as fd:
        fd.write(index_contet)

    return sketch_files.sketch_py


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

    sketch_files = Pyp5jsSketchFiles(sketch_dir, sketch_name)
    if not sketch_files.check_sketch_exists():
        cprint.err(f"Couldn't find {sketch_name}", interrupt=True)

    compiler.compile_sketch_js(sketch_files)
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

    sketch_files = Pyp5jsSketchFiles(sketch_dir, sketch_name)
    if not sketch_files.check_sketch_exists():
        cprint.err(f"Couldn't find {sketch_name}", interrupt=True)

    cprint(f"Monitoring for changes in {sketch_files.sketch_dir.absolute()}...")

    try:
        compiler.monitor_sketch(sketch_files)
    except KeyboardInterrupt:
        cprint.info("Exiting monitor...")
