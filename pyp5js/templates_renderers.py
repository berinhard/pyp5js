from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.fs import SketchFiles

templates = Environment(loader=FileSystemLoader(str(PYP5JS_FILES.templates_dir)))


def get_sketch_index_content(sketch_files):
    """
    Renders SKETCH_NAME/index.html to display the sketch visualization
    """
    context = {
        "sketch_name": sketch_files.sketch_name,
        "p5_js_url": sketch_files.urls.p5_js_url,
        "sketch_js_url":  sketch_files.urls.sketch_js_url,
    }
    template_file = sketch_files.config.get_index_template()
    index_template = templates.get_template(template_file.name)
    return index_template.render(context)


def get_target_sketch_content(sketch_files):
    """
    Renders the content to be written in the temporary SKETCH_NAME/target_sketch.py file
    """
    context = {"sketch_name": sketch_files.sketch_name}
    index_template = templates.get_template(PYP5JS_FILES.target_sketch_template.name)
    return index_template.render(context)
