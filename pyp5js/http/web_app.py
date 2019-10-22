from flask import Flask, render_template, Response, request
from slugify import slugify
from textwrap import dedent

from pyp5js import commands
from pyp5js.config import SKETCHBOOK_DIR
from pyp5js.exceptions import PythonSketchDoesNotExist, SketchDirAlreadyExistException
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


@app.route("/new-sketch/", methods=['GET', 'POST'])
def add_new_sketch_view():
    template = 'new_sketch_form.html'
    context = {'sketches_dir': SKETCHBOOK_DIR.resolve()}

    if request.method == 'POST':
        sketch_name = slugify(request.form.get('sketch_name', '').strip(), separator='_')
        if not sketch_name:
            context['error'] = "You have to input a sketch name to proceed."
        else:
            try:
                files = commands.new_sketch(sketch_name)
                template = 'new_sketch_success.html'
                context.update({
                    'files': files,
                    'sketch_url': f'/sketch/{sketch_name}/',
                })
            except SketchDirAlreadyExistException:
                path = SKETCHBOOK_DIR.joinpath(sketch_name)
                context['error'] = f"The sketch {path} already exists."

    return render_template(template, **context)


@app.route('/sketch/<string:sketch_name>/', defaults={'static_path': ''})
@app.route('/sketch/<string:sketch_name>/<path:static_path>')
def render_sketch_view(sketch_name, static_path):
    sketch_files = SketchFiles(sketch_name)

    content_file = sketch_files.index_html
    if static_path:
        content_file = sketch_files.sketch_dir.joinpath(static_path).resolve()
        if not str(content_file).startswith(str(sketch_files.sketch_dir.resolve())):
            # User tried something not allowed (as "/root/something" or "../xxx")
            return '', 403
        elif not content_file.exists():
            return '', 404
    else:
        try:
            commands.transcrypt_sketch(sketch_name)
        except PythonSketchDoesNotExist:
            return f"There's no sketch in {sketch_files.sketch_dir.resolve()}", 404

    with content_file.open() as fd:
        response = Response(fd.read())

    if static_path.endswith('js'):
        # To avoid MIME type errors
        # More can be found here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options
        response.headers['Content-Type'] = 'application/javascript'

    return response
