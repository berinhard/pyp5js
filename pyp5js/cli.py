#!/usr/bin/env python3
import warnings
from pathlib import Path

from cprint import cprint
import click

from pyp5js import commands
from pyp5js.config import SKETCHBOOK_DIR, AVAILABLE_INTERPRETERS, PYODIDE_INTERPRETER


@click.group()
def command_line_entrypoint():
    """
    pyp5js is a command line tool to conver Python 3 code to p5.js.
    """
    pass


@command_line_entrypoint.command('new')
@click.argument('sketch_name')
@click.option('--monitor', '-m', is_flag=True, help='Starts the monitor command too')
@click.option('--interpreter', '-i', type=click.Choice(AVAILABLE_INTERPRETERS), default=PYODIDE_INTERPRETER, help='Which python tool to use to run the sketch. (defaults to pyodide)')
def configure_new_sketch(sketch_name, monitor, interpreter):
    """
    Create dir and configure boilerplate - Example:\n
    $ pyp5js new my_sketch -i pyodide
    """
    files = commands.new_sketch(sketch_name, interpreter)

    cprint.ok(f"Your sketch was created!")

    if not monitor:
        cprint.ok(f"Please, open and edit the file {files.sketch_py} to draw. When you're ready to see your results, just run:")
        cmd = f"\t pyp5js compile {sketch_name}"
        cprint.ok(cmd)
        cprint.ok(f"And open file://{files.index_html.absolute()} on your browser to see yor results!")
    else:
        cprint.ok(f"Please, open and edit the file {files.sketch_py} to draw.")
        cprint.ok(f"And open file://{files.index_html.absolute()} on your browser to see yor results!")
        commands.monitor_sketch(sketch_name)


@command_line_entrypoint.command("transcrypt")
@click.argument("sketch_name")
def transcrypt_sketch(sketch_name):
    """
    Command to generate the P5.js code for a python sketch

    Params:

    - sketch_name: name of the sketch

    Example:
    $ pyp5js transcrypt my_sketch
    """
    msg = f"transcript command is deprecated. Instead, please run: \n\n\tpyp5js compile {sketch_name}\n"
    warnings.warn(msg, UserWarning)


@command_line_entrypoint.command("compile")
@click.argument("sketch_name")
def compile_sketch(sketch_name):
    files = commands.compile_sketch(sketch_name)
    cprint.ok(f"Your sketch is ready and available at file://{files.index_html.absolute()}")


@command_line_entrypoint.command("monitor")
@click.argument("sketch_name")
def monitor_sketch(sketch_name):
    """
    Command to generate keep watching a sketch's dir and, after any change,
    it'll automatically generate the JS files as in pyp5js transcrypt command

    Params:

    - sketch_name: name of the sketch

    Example:

    $ pyp5js monitor my_sketch
    """
    commands.monitor_sketch(sketch_name)


@command_line_entrypoint.command("serve")
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=5000)
@click.option('--debug', is_flag=True)
def serve_sketches(host, port, debug):
    """
    Run HTTP server to compile and serve sketches

    Opitionals:
    - host: http server host (defaults to 127.0.0.1)
    - port: listened by the server (defaults to 5000)

    Example:
    $ pyp5js serve
    """

    if not SKETCHBOOK_DIR.exists():
        SKETCHBOOK_DIR.mkdir()

    commands.serve_http(host, port, debug)


if __name__ == "__main__":
    command_line_entrypoint()
