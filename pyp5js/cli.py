#!/usr/bin/env python3
import click
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

@click.group()
def command_line_entrypoint():
    """
    Function to define the entry point for the command line
    """
    pass


@command_line_entrypoint.command('new')
@click.argument('sketch_name')
@click.option('--sketch_dir', '-d', default=None)
def configure_new_sketch(sketch_name, sketch_dir):
    """
    Create dir and configure boilerplate

    Params:
    - sketch_name: name of the sketch (will create a {sketch_name}.py)

    Opitionals
    - sketch_dir: directory to save the sketch (defaults to {sketch_name})
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


@command_line_entrypoint.command("transcrypt")
@click.argument("sketch_name")
@click.option('--sketch_dir', '-d', default=None)
def transcrypt_sketch(sketch_name, sketch_dir):
    """
    Command to generate the P5.js code for a python sketch

    Params:
    - sketch_name: name of the sketch

    Opitionals
    - sketch_dir: sketch's directory (defaults to {sketch_name})
    """
    sketch_dir, sketch = _validate_sketch_paths(sketch_name, sketch_dir)

    command = ' '.join([str(c) for c in [
        'transcrypt', '-xp', PYP5_DIR, '-b', '-m', '-n', sketch
    ]])
    cprint.info(f"Command:\n\t {command}")

    subprocess.check_output(shlex.split(command))

    __target = sketch_dir.child('__target__')
    if not __target.exists():
        cprint.err(f"Error with transcrypt: the {__target} directory wasn't created.", interrupt=True)

    target_dir = sketch_dir.child(TARGET_DIRNAME)
    shutil.move(__target, target_dir)


if __name__ == "__main__":
    command_line_entrypoint()
