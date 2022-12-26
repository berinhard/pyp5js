"""
pyp5js
Copyright (C) 2019-2021 Bernardo Fontes

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import ast
import os

from flask import Flask, render_template, request, send_from_directory
from pyp5js import commands
from pyp5js.config import (AVAILABLE_INTERPRETERS, PYODIDE_INTERPRETER,
                           SKETCHBOOK_DIR, TRANSCRYPT_INTERPRETER)
from pyp5js.exceptions import (PythonSketchDoesNotExist,
                               SketchDirAlreadyExistException)
from pyp5js.sketch import Sketch
from slugify import slugify

app = Flask(__name__)
SUPPORTED_IMAGE_FILE_SUFFIXES = (".gif", ".jpg", ".png")


@app.route("/")
def sketches_list_view():
    sketches = []
    for sketch_dir in (p for p in SKETCHBOOK_DIR.iterdir() if p.is_dir()):
        name = sketch_dir.name
        sketch = Sketch(name)
        if sketch.has_all_files:
            sketches.append({
                'name': name,
                'url': f'/sketch/{name}/'
            })

    sketches = sorted(sketches, key=lambda s: s['name'])
    return render_template('index.html', sketches=sketches, sketches_dir=SKETCHBOOK_DIR.resolve())


@app.route("/new-sketch/", methods=['GET', 'POST'])
def add_new_sketch_view():
    template = 'new_sketch_form.html'
    context = {
        'sketches_dir': SKETCHBOOK_DIR.resolve(),
        'pyodide_interpreter': PYODIDE_INTERPRETER,
        'transcrypt_interpreter': TRANSCRYPT_INTERPRETER,
    }

    if request.method == 'POST':
        sketch_name = slugify(request.form.get(
            'sketch_name', '').strip(), separator='_')
        interpreter = request.form.get('interpreter', PYODIDE_INTERPRETER)
        if not sketch_name:
            context['error'] = "You have to input a sketch name to proceed."
        elif interpreter not in AVAILABLE_INTERPRETERS:
            context['error'] = f"The interpreter {interpreter} is not valid. Please, select a valid one."
        else:
            try:
                files = commands.new_sketch(sketch_name, interpreter=interpreter)
                template = 'new_sketch_success.html'
                context.update({
                    'files': files,
                    'sketch_url': f'/sketch/{sketch_name}/',
                })
            except SketchDirAlreadyExistException:
                path = SKETCHBOOK_DIR.joinpath(sketch_name)
                context['error'] = f"The sketch {path} already exists."

    return render_template(template, **context)


@app.route('/sketch/<string:sketch_name>/', defaults={'static_path': ''}, methods=['GET', 'POST'])
@app.route('/sketch/<string:sketch_name>/<path:static_path>')
def render_sketch_view(sketch_name, static_path):
    sketch = Sketch(sketch_name)

    error = ''
    if static_path:
        return _serve_static(sketch.sketch_dir, static_path)

    elif request.method == 'POST':
        py_code = request.form.get('py_code', '')
        if not py_code.strip():
            error = 'You have to input the Python code.'
        elif 'def setup():' not in py_code:
            error = 'You have to define a setup function.'
        elif 'def draw():' not in py_code:
            error = 'You have to define a draw function.'
        else:
            try:
                ast.parse(py_code, sketch.sketch_py.name)
                sketch.sketch_py.write_bytes(bytes(py_code, encoding="utf-8"))
            except SyntaxError as exc:
                error = f'SyntaxError: {exc}'

    if not error:
        try:
            # web editor must always use local install of JS dependencies
            commands.compile_sketch(sketch_name, force_local=True)
        except PythonSketchDoesNotExist:
            return f"There's no sketch in {sketch.sketch_dir.resolve()}", 404

    context = {
        'p5_js_url': sketch.urls.p5_js_url,
        'sketch_js_url': sketch.urls.sketch_js_url,
        'sketch_name': sketch.sketch_name,
        'py_code': sketch.sketch_py.read_text(),
        'error': error,
        'js_as_module': sketch.config.is_transcrypt,
        'live_run': sketch.config.is_pyodide,
    }
    return render_template('view_sketch.html', **context)


def _serve_static(static_dir, static_path):
    content_file = static_dir.joinpath(static_path).resolve()
    if not str(content_file).startswith(str(static_dir.resolve())):
        # User tried something not allowed (as "/root/something" or "../xxx")
        return '', 403

    resp = send_from_directory(static_dir.absolute(), static_path, etag=False, max_age=0)

    if os.name == 'nt' and static_path.lower().endswith('.js'):
        js_content = resp.headers['Content-Type'].replace('text/plain', 'application/javascript')
        resp.headers['Content-Type'] = js_content

    return resp
