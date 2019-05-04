import os
import shutil
import time
from cprint import cprint
from datetime import date
from jinja2 import Environment, FileSystemLoader
from unipath import Path
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
from watchdog.observers import Observer

from pyp5js.compiler import compile_sketch_js

PYP5_DIR = Path(__file__).parent
TEMPLATES_DIR = PYP5_DIR.child('templates')
TARGET_DIRNAME = "target"
templates = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


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
    
    SKETCH_DIR = Path(sketch_dir or f'{sketch_name}')

    if SKETCH_DIR.exists():
        cprint.warn(f"Cannot configure a new sketch.")
        cprint.err(f"The directory {SKETCH_DIR} already exists.", interrupt=True)

    static_dir = SKETCH_DIR.child('static')
    templates_files = [
        (TEMPLATES_DIR.child('base_sketch.py'), SKETCH_DIR.child(f'{sketch_name}.py')),
        (PYP5_DIR.child('static', 'p5.js'), static_dir.child('p5.js'))
    ]

    index_template = templates.get_template('index.html')
    context = {
        "p5_js_url": "static/p5.js",
        "sketch_js_url": f"{TARGET_DIRNAME}/{sketch_name}.js",
        "sketch_name": sketch_name,
    }
    index_contet = index_template.render(context)

    os.mkdir(SKETCH_DIR)
    os.mkdir(static_dir)
    for src, dest in templates_files:
        shutil.copyfile(src, dest)

    with open(SKETCH_DIR.child("index.html"), "w") as fd:
        fd.write(index_contet)

    return templates_files[0][1]


def _validate_sketch_path(sketch_name=None, sketch_dir=None):
    """
    Searches for the sketch .py file
    """
    sketch_dir = Path(sketch_dir or f'{sketch_name}')

    sketch = sketch_dir.child(f"{sketch_name}.py")
    if not sketch.exists():
        sketch_file = Path(os.getcwd()).child(f"{sketch_name}.py")
        if not sketch_file.exists():
            cprint.warn(f"Couldn't find the sketch.")
            cprint.err(f"Neither the file {sketch} or {sketch_file} exist.", interrupt=True)

        sketch = sketch_file
        sketch_dir = sketch.parent

    return sketch


def transcrypt_sketch(sketch_name, sketch_dir):
    sketch = _validate_sketch_path(sketch_name, sketch_dir)
    compile_sketch_js(sketch, TARGET_DIRNAME)
    return sketch.parent.child("index.html")


class TranscryptSketchEvent(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def __init__(self, *args, **kwargs):
        self.sketch = kwargs.pop('sketch')
        self._last_event = None
        super().__init__(*args, **kwargs)

    def on_modified(self, event):
        event_id = id(event)
        if event_id == self._last_event:
            return

        cprint.info(f"New change in {event.src_path}")
        compile_sketch_js(self.sketch, TARGET_DIRNAME)


def monitor_sketch(sketch_name, sketch_dir):
    sketch = _validate_sketch_path(sketch_name, sketch_dir)
    cprint(f"Monitoring for changes in {sketch.parent.absolute()}...")

    event_handler = TranscryptSketchEvent(sketch=sketch)
    observer = Observer()

    observer.schedule(event_handler, sketch.parent)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cprint.info("Exiting monitor...")
        observer.stop()
    observer.join()
