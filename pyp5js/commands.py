import os
import subprocess
import shlex
import random
from datetime import date
from cprint import cprint
import shutil
from unipath import Path
from jinja2 import Environment, FileSystemLoader

PYP5_DIR = Path(__file__).parent
TEMPLATES_DIR = PYP5_DIR.child('templates')
TARGET_DIRNAME = "target"
templates = Environment(loader=FileSystemLoader(TEMPLATES_DIR))



def new_sketch(sketch_name, sketch_dir):
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


def _validate_sketch_paths(sketch_name=None, sketch_dir=None):
    sketch_dir = Path(sketch_dir or f'{sketch_name}')

    sketch = sketch_dir.child(f"{sketch_name}.py")
    if not sketch.exists():
        sketch_file = Path(os.getcwd()).child(f"{sketch_name}.py")
        if not sketch_file.exists():
            cprint.warn(f"Couldn't find the sketch.")
            cprint.err(f"Neither the file {sketch} or {sketch_file} exist.", interrupt=True)

        sketch = sketch_file
        sketch_dir = sketch.parent

    return sketch_dir, sketch


def transcrypt_sketch(sketch_name, sketch_dir):
    sketch_dir, sketch = _validate_sketch_paths(sketch_name, sketch_dir)

    command = ' '.join([str(c) for c in [
        'transcrypt', '-xp', PYP5_DIR, '-b', '-m', '-n', sketch
    ]])
    cprint.info(f"Converting Python to P5.js...\nRunning command:\n\t {command}")

    proc = subprocess.Popen(shlex.split(command))
    proc.wait()

    __target = sketch_dir.child('__target__')
    if not __target.exists():
        cprint.err(f"Error with transcrypt: the {__target} directory wasn't created.", interrupt=True)

    target_dir = sketch_dir.child(TARGET_DIRNAME)
    if target_dir.exists():
        shutil.rmtree(target_dir)
    shutil.move(__target, target_dir)

    return sketch_dir.child("index.html")
