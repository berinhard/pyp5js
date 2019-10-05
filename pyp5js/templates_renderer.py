from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.fs import LibFiles, SketchFiles

pyp5js_files = LibFiles()
templates = Environment(loader=FileSystemLoader(str(pyp5js_files.templates_dir)))

def get_pytop5js_content(variables_names, methods_names, event_function_names):
    """
    Renders content for the final pyp5js/pyp5js.py file
    """
    pyp5_template = templates.get_template(
        str(pyp5js_files.pytop5js_template.name)
    )
    context = {
        'function_names': methods_names,
        'variables_names': variables_names,
        'event_function_names': event_function_names,
    }
    return pyp5_template.render(context)


def get_target_sketch_template_content(event_function_names):
    """
    Renders the content for pyp5js/templates/target_sketch.py.template file
    """
    content = "import {{ sketch_name }} as source_sketch\nfrom pyp5js import *\n\n"
    content += "event_functions = {\n"

    for event in event_function_names:
        content += f'    "{event}": source_sketch.{event},\n'

    content += '}\n\nstart_p5(source_sketch.setup, source_sketch.draw, event_functions)'

    return content


def get_sketch_index_content(sketch_files):
    """
    Renders SKETCH_NAME/index.html to display the sketch visualization
    """
    context = {
        "sketch_name": sketch_files.sketch_name,
        "p5_js_url": f"{sketch_files.STATIC_NAME}/p5.js",
        "sketch_js_url": f"{sketch_files.TARGET_NAME}/target_sketch.js",
    }
    index_template = templates.get_template(
        str(pyp5js_files.index_html.name)
    )
    return index_template.render(context)


def get_target_sketch_content(sketch_files):
    """
    Renders the content to be written in the temporary SKETCH_NAME/target_sketch.py file
    """
    context = {"sketch_name": sketch_files.sketch_name}
    index_template = templates.get_template(
        str(pyp5js_files.target_sketch_template.name)
    )
    return index_template.render(context)
