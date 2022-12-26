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
from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.sketch import Sketch

templates = Environment(loader=FileSystemLoader(str(PYP5JS_FILES.templates_dir)))


def _template_from_file(filename, context):
    templates = Environment(loader=FileSystemLoader(str(filename.parent.resolve())))
    template = templates.get_template(filename.name)
    return template.render(context)


def get_sketch_index_content(sketch):
    """
    Renders SKETCH_NAME/index.html to display the sketch visualization.
    template can be a pathlib.Path object with a specified custom template path
    """
    context = {
        "sketch_name": sketch.sketch_name,
        "p5_js_url": sketch.urls.p5_js_url,
        "pyodide_js_url": sketch.urls.pyodide_js_url,
        "sketch_js_url":  sketch.urls.sketch_js_url,
        "sketch_content": sketch.sketch_content,
    }
    template_file = sketch.config.get_index_template()
    return _template_from_file(template_file, context)


def get_target_sketch_content(sketch):
    """
    Renders the content to be written in the temporary SKETCH_NAME/target_sketch.py file
    """
    context = sketch.get_target_sketch_context()
    target_js_file = sketch.config.get_target_js_template()
    return _template_from_file(target_js_file, context)
