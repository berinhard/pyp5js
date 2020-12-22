from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.sketch import Sketch

templates = Environment(loader=FileSystemLoader(str(PYP5JS_FILES.templates_dir)))


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
    index_template = templates.get_template(template_file.name)
    return index_template.render(context)


def get_target_sketch_content(sketch):
    """
    Renders the content to be written in the temporary SKETCH_NAME/target_sketch.py file
    """
    context = {"sketch_name": sketch.sketch_name}
    target_js_file = sketch.config.get_target_js_template()
    index_template = templates.get_template(target_js_file)
    return index_template.render(context)
