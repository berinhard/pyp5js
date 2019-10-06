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
            sketches.append(name)

    return render_template('index.html', sketches=sketches)
