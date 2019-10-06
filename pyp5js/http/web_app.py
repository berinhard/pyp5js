from flask import Flask, render_template, Response
from textwrap import dedent

from pyp5js.compiler import compile_sketch_js
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

    return render_template('index.html', sketches=sketches, sketches_dir=SKETCHBOOK_DIR.resolve())


@app.route('/sketch/<string:sketch_name>/', defaults={'static_path': ''})
@app.route('/sketch/<string:sketch_name>/<path:static_path>')
def render_sketch(sketch_name, static_path):
    sketch_files = SketchFiles(sketch_name)

    msg_404 = ''
    if not sketch_files.sketch_dir.exists():
        msg_404 = f"There's no sketch in {sketch_files.sketch_dir.resolve()}"
    elif not sketch_files.has_all_files:
        msg_404 = f"The sketch {sketch_name} has missing files."

    if msg_404:
        return msg_404, 404

    content_file = sketch_files.index_html
    if static_path:
        content_file = sketch_files.sketch_dir.joinpath(static_path)
        if not content_file.exists():
            return '', 404
    else:
        compile_sketch_js(sketch_files)

    with content_file.open() as fd:
        response = Response(fd.read())

    if static_path.endswith('js'):
        # To avoid MIME type errors
        # More can be found here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options
        response.headers['Content-Type'] = 'application/javascript'

    return response
