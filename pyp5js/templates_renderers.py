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
    Renders SKETCH_NAME/index.html to display the sketch visualization
    """
    context = {
        "sketch_name": sketch.sketch_name,
        "p5_js_url": sketch.urls.p5_js_url,
        "sketch_js_url":  sketch.urls.sketch_js_url,
    }
    template_file = sketch.config.get_index_template()
    return _template_from_file(template_file, context)


def get_target_sketch_content(sketch):
    """
    Renders the content to be written in the temporary SKETCH_NAME/target_sketch.py file
    """
    with sketch.sketch_py.open() as fd:
        content = fd.read()

    context = {
        "sketch_name": sketch.sketch_name,
        "sketch_content": content,
    }
    target_js_file = sketch.config.get_target_js_template()
    return _template_from_file(target_js_file, context)
