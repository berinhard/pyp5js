from flask import Flask, render_template
from textwrap import dedent

from pyp5js.config import SKETCHBOOK_DIR
from pyp5js.fs import SketchFiles


app = Flask(__name__)


@app.route("/")
def sketches_list_view():
    sketches = []
    for sketch_dir in (p for p in SKETCHBOOK_DIR.iterdir() if p.is_dir()):
        name = sketch_dir.name
        sketch_files = SketchFiles(name)
        if sketch_files.has_all_files:
            sketches.append({
                'name': name,
                'url': f'/sketch/{name}'
            })

    return render_template('index.html', sketches=sketches)


@app.route('/sketch/<string:sketch_name>/')
def render_sketch(sketch_name):
    sketch_files = SketchFiles(sketch_name)

    msg_404 = ''
    if not sketch_files.sketch_dir.exists():
        msg_404 = f"There's no sketch in {sketch_files.sketch_dir.resolve()}"
    elif not sketch_files.has_all_files:
        msg_404 = f"The sketch {sketch_name} has missing files."

    if msg_404:
        return msg_404, 404

    with sketch_files.index_html.open() as fd:
        return fd.read()
