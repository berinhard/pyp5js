from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.fs import LibFiles, SketchFiles

pyp5js_files = LibFiles()
templates = Environment(loader=FileSystemLoader(str(pyp5js_files.templates_dir)))


def get_sketch_index_content(sketch_files):
    """
    Renders SKETCH_NAME/index.html to display the sketch visualization
    """
    context = {
        "sketch_name": sketch_files.sketch_name,
        "p5_js_url": f"{sketch_files.STATIC_NAME}/p5.js",
        "sketch_js_url": f"{sketch_files.TARGET_NAME}/target_sketch.js",
    }
    index_template = templates.get_template(pyp5js_files.index_html.name)
    return index_template.render(context)


def get_target_sketch_content(sketch_files):
    """
    Renders the content to be written in the temporary SKETCH_NAME/target_sketch.py file
    """
    context = {"sketch_name": sketch_files.sketch_name}
    index_template = templates.get_template(pyp5js_files.target_sketch_template.name)
    return index_template.render(context)
