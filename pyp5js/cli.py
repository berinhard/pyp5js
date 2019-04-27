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
from jinja2 import Environment, FileSystemLoader, select_autoescape


PYP5_DIR = Path(__file__).parent
TEMPLATES_DIR = PYP5_DIR.child('templates')

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
    """
    SKETCH_DIR = Path(sketch_dir or f'./{sketch_name}')
    if SKETCH_DIR.exists():
        cprint.warn(f"Cannot configure a new sketch.")
        cprint.err(f"The directory {SKETCH_DIR} already exists.", interrupt=True)

    static_dir = SKETCH_DIR.child('static')
    templates_files = [
        (TEMPLATES_DIR.child('base_sketch.py'), SKETCH_DIR.child(f'{sketch_name}.py')),
        (TEMPLATES_DIR.child('index.html'), SKETCH_DIR.child(f'index.html')),
        (PYP5_DIR.child('static', 'p5.js'), static_dir.child('p5.js'))
    ]

    os.mkdir(SKETCH_DIR)
    os.mkdir(static_dir)
    for src, dest in templates_files:
        copyfile(src, dest)


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

#    command = ' '.join([str(c) for c in [
#        'ffmpeg', '-framerate', frame_rate, '-pattern_type', 'glob', '-i', query, '-c:v', 'libx264', '-r', frame_rate, '-pix_fmt', 'yuv420p', output
#    ]])
#
#    cprint.info(f"Command:\n\t$ {command}")
#
#    convert = subprocess.Popen(
#        shlex.split(command),
#    )
#    convert.wait()




#@cli.command('export')
#@click.argument('sketch_name')
#@click.option('--frame-rate', '-r', default=24)
#@click.option('--output', '-o', default=None)
#@click.option('--clean-after', '-c', is_flag=True, default=False)
#def export_to_video(sketch_name, frame_rate, output, clean_after):
#    """
#    Export frames from sketch to a MP4 video
#    """
#    sketch_dir = SKETCH_DIR.child(sketch_name)
#
#    if not sketch_dir.exists():
#        cprint.err(f"There's no directory for the sketch {sketch_name}", interrupt=True)
#
#    output = output or sketch_dir.child('output.mp4')
#    cprint.info(f"Generating {output} from sketch sketch_name")
#    query = sketch_dir + "/*.png"
#    command = ' '.join([str(c) for c in [
#        'ffmpeg', '-framerate', frame_rate, '-pattern_type', 'glob', '-i', query, '-c:v', 'libx264', '-r', frame_rate, '-pix_fmt', 'yuv420p', output
#    ]])
#
#    cprint.info(f"Command:\n\t$ {command}")
#
#    convert = subprocess.Popen(
#        shlex.split(command),
#    )
#    convert.wait()
#
#    if clean_after:
#        pngs = sketch_dir.listdir("*.png")
#        cover = random.choice(pngs)
#        cover.rename("cover.png")
#        for png in pngs:
#            png.remove()
#
#@cli.command('update_index')
#@click.argument('sketch_name')
#@click.option('--title', '-t', default='')
#@click.option('--cover', '-c', default='cover.png')
#def update_index_with_sketch(sketch_name, title, cover):
#    """
#    Updates index.html with new the new sketch
#    """
#    sketch_dir = SKETCH_DIR.child(sketch_name)
#
#    if not sketch_dir.exists():
#        cprint.err(f"There's no directory for the sketch {sketch_name}", interrupt=True)
#
#    desc, desc_ptbr = '', ''
#    while not desc:
#        desc = input("Enter with sketch's description: ").strip()
#    while not desc_ptbr:
#        desc_ptbr = input("Entre com a descrição do sketch (PT-BR): ").strip()
#
#    title = title or f'#{sketch_name}'
#    template = templates.get_template('new_entry_snippet.html')
#    today = date.today()
#    ctx = {
#        'sketch_id': sketch_name,
#        'title': title,
#        'cover': cover,
#        'sketch_date': f'{today:%m/%d/%Y}',
#        'description': desc,
#    }
#
#    content = template.render(ctx)
#    index_template = templates.get_template('index_base.html')
#    new_index_content = index_template.render(new_sketch_content=content)
#
#    with open(SKETCH_DIR.child('index.html'), 'w') as fd:
#        fd.write(new_index_content)
#
#    content = template.render(ctx)
#    index_template = templates.get_template('index_base.html')
#    base_index_content = index_template.render(new_sketch_content='{{ new_sketch_content }}\n\n' + content)
#
#    with open(TEMPLATES_DIR.child('index_base.html'), 'w') as fd:
#        fd.write(base_index_content)
#
#    cprint.ok("\nTweet content:")
#    tweet_template = templates.get_template('tweet_template.txt')
#    ctx = {'eng_desc': desc, 'pt_desc': desc_ptbr, 'name': sketch_name}
#    content = tweet_template.render(**ctx)
#    cprint.ok(content)
#
#
#
if __name__ == '__main__':
    cli()
