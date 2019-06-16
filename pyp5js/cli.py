#!/usr/bin/env python3
from cprint import cprint
import click

from pyp5js import commands

@click.group()
def command_line_entrypoint():
    """
    Function to define the entry point for the command line
    """
    pass


@command_line_entrypoint.command('new')
@click.argument('sketch_name')
@click.option('--sketch-dir', '-d', default=None)
@click.option('--monitor', '-m', is_flag=True)
def configure_new_sketch(sketch_name, sketch_dir, monitor):
    """
    Create dir and configure boilerplate

    Params:
    - sketch_name: name of the sketch (will create a {sketch_name}.py)

    Opitionals:
    - sketch_dir: directory to save the sketch (defaults to {sketch_name})

    Example:
    $ pyp5js new my_sketch
    """
    sketch_py, index_html = commands.new_sketch(sketch_name, sketch_dir)

    cprint.ok(f"Your sketch was created!")

    if not monitor:
        cprint.ok(f"Please, open and edit the file {sketch_py} to draw. When you're ready to see your results, just run:")
        cmd = f"\t pyp5js transcrypt {sketch_name}"
        if sketch_dir:
            cmd += f" --sketch-dir {sketch_dir}"
        cprint.ok(cmd)
        cprint.ok(f"And open file://{index_html.absolute()} on your browser to see yor results!")
    else:
        cprint.ok(f"Please, open and edit the file {sketch_py} to draw.")
        cprint.ok(f"And open file://{index_html.absolute()} on your browser to see yor results!")
        commands.monitor_sketch(sketch_name, sketch_dir)



@command_line_entrypoint.command("transcrypt")
@click.argument("sketch_name")
@click.option('--sketch-dir', '-d', default=None)
def transcrypt_sketch(sketch_name, sketch_dir):
    """
    Command to generate the P5.js code for a python sketch

    Params:
    - sketch_name: name of the sketch

    Opitionals
    - sketch_dir: sketch's directory (defaults to {sketch_name})

    Example:
    $ pyp5js transcrypt my_sketch
    """
    index_file = commands.transcrypt_sketch(sketch_name, sketch_dir)
    cprint.ok(f"Your sketch is ready and available at file://{index_file.absolute()}")


@command_line_entrypoint.command("monitor")
@click.argument("sketch_name")
@click.option('--sketch-dir', '-d', default=None)
def monitor_sketch(sketch_name, sketch_dir):
    """
    Command to generate keep watching a sketch's dir and, after any change,
    it'll automatically generate the JS files as in pyp5js transcrypt command

    Params:
    - sketch_name: name of the sketch

    Opitionals
    - sketch_dir: sketch's directory (defaults to ./{sketch_name})

    Example:
    $ pyp5js monitor my_sketch
    """
    commands.monitor_sketch(sketch_name, sketch_dir)

if __name__ == "__main__":
    command_line_entrypoint()
