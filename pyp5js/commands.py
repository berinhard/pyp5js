import os
import shutil
import time
from cprint import cprint
from datetime import date
from unipath import Path
from watchdog.observers import Observer

from pyp5js.compiler import compile_sketch_js, TranscryptSketchEvent
from pyp5js.fs import Pyp5jsSketchFiles, Pyp5jsLibFiles

TARGET_DIRNAME = "target"


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
    sketch_files.can_create_sketch()

    pyp5js_files = Pyp5jsLibFiles()
    templates_files = [
        (pyp5js_files.base_sketch, sketch_files.sketch_py),
        (pyp5js_files.p5js, sketch_files.p5js)
    ]

    context = {
        "p5_js_url": "static/p5.js",
        "sketch_js_url": f"{TARGET_DIRNAME}/{sketch_name}.js",
        "sketch_name": sketch_name,
    }
    index_contet = pyp5js_files.render_new_index(context)

    os.makedirs(sketch_files.sketch_dir)
    os.mkdir(sketch_files.static_dir)
    for src, dest in templates_files:
        shutil.copyfile(src, dest)

    with open(sketch_files.index_html, "w") as fd:
        fd.write(index_contet)

    return sketch_files.sketch_py


def transcrypt_sketch(sketch_name, sketch_dir):
    sketch_files = Pyp5jsSketchFiles(sketch_dir, sketch_name)
    sketch_files.check_sketch_exists()

    compile_sketch_js(sketch_files)
    return sketch_files.index_html


def monitor_sketch(sketch_name, sketch_dir):
    sketch_files = Pyp5jsSketchFiles(sketch_dir, sketch_name)
    sketch_files.check_sketch_exists()

    cprint(f"Monitoring for changes in {sketch_files.sketch_dir.absolute()}...")

    event_handler = TranscryptSketchEvent(sketch_files=sketch_files)
    observer = Observer()

    observer.schedule(event_handler, sketch_files.sketch_dir)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cprint.info("Exiting monitor...")
        observer.stop()
    observer.join()
