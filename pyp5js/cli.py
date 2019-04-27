#!/usr/bin/env python3
import click
import os
import subprocess
import shlex
import random
from datetime import date
from cprint import cprint
from shutil import copyfile
from unipath import Path
from jinja2 import Environment, FileSystemLoader


PYP5_DIR = Path(__file__).parent
TEMPLATES_DIR = PYP5_DIR.child('templates')
templates = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

@click.group()
def cli():
    """
    Function to define the entry point for the command line
    """
    pass


@cli.command('new')
@click.argument('sketch_name')
@click.option('--sketch_dir', '-d', default=None)
def configure_new_sketch(sketch_name, sketch_dir):
    """
    Create dir and configure boilerplate

    Params:
    - sketch_name: name of the sketch (will create a {sketch_name}.py)

    Opitionals
    - sketch_dir: directory to save the sketch (defaults to ./{sketch_name})
    """
    SKETCH_DIR = Path(sketch_dir or f'./{sketch_name}')
    if SKETCH_DIR.exists():
        cprint.warn(f"Cannot configure a new sketch.")
        cprint.err(f"The directory {SKETCH_DIR} already exists.", interrupt=True)

    static_dir = SKETCH_DIR.child('static')
    templates_files = [
        (TEMPLATES_DIR.child('base_sketch.py'), SKETCH_DIR.child(f'{sketch_name}.py')),
        (PYP5_DIR.child('static', 'p5.js'), static_dir.child('p5.js'))
    ]

    os.mkdir(SKETCH_DIR)
    os.mkdir(static_dir)
    for src, dest in templates_files:
        copyfile(src, dest)

    index_template = templates.get_template('index.html')
    context = {
        "p5_js_url": "static/p5.js",
        "sketch_js_url": f"__target__/{sketch_name}.js",
    }
    index_contet = index_template.render(context)

    with open(SKETCH_DIR.child("index.html"), "w") as fd:
        fd.write(index_contet)


@cli.command("transcrypt")
@click.argument("sketch_name")
@click.option('--sketch_dir', '-d', default=None)
@click.option('--pyp5js', '-p', default=None)
def transcrypt_sketch(sketch_name, sketch_dir, pyp5js):
    """
    Command to generate the P5.js code for a python sketch

    Params:
    - sketch_name: name of the sketch (will create a {sketch_name}.py)

    Opitionals
    - sketch_dir: sketch's directory (defaults to ./{sketch_name})
    - pyp5hs: path to the pyp5js main file (defaults to local install)
    """
    SKETCH_DIR = Path(sketch_dir or f'./{sketch_name}')
    if not SKETCH_DIR.exists():
        cprint.warn(f"Couldn't find the sketch.")
        cprint.err(f"The directory {SKETCH_DIR} doesn't exist.", interrupt=True)

    sketch = SKETCH_DIR.child(f"{sketch_name}.py")
    pyp5js = Path(pyp5js or PYP5_DIR)


    command = ' '.join([str(c) for c in [
        'transcrypt', '-xp', pyp5js, '-b', '-m', '-n', sketch
    ]])
    cprint.info(f"Command:\n\t {command}")

    transcrypt = subprocess.Popen(shlex.split(command))
    transcrypt.wait()


if __name__ == "__main__":
    cli()
