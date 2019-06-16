from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.fs import Pyp5jsLibFiles, Pyp5jsSketchFiles

pyp5js_files = Pyp5jsLibFiles()

def get_pytop5js_content(variables_names, methods_names, event_function_names):
    templates = Environment(loader=FileSystemLoader(pyp5js_files.templates_dir))
    pyp5_template = templates.get_template(
        str(pyp5js_files.pytop5js_template.name)
    )
    context = {
        'function_names': methods_names,
        'variables_names': variables_names,
        'event_function_names': event_function_names,
    }
    return pyp5_template.render(context)


def get_index_content(sketch_name, p5_js_url=None, sketch_js_url=None):
    context = {
        "sketch_name": sketch_name,
        "p5_js_url": p5_js_url or f"{Pyp5jsSketchFiles.STATIC_NAME}/p5.js",
        "sketch_js_url": sketch_js_url or f"{Pyp5jsSketchFiles.TARGET_NAME}/target_sketch.js",
    }
    templates = Environment(loader=FileSystemLoader(pyp5js_files.templates_dir))
    index_template = templates.get_template(
        str(pyp5js_files.index_html.name)
    )
    return index_template.render(context)



def get_target_sketch_template_content(event_function_names):
    content = "import {{ sketch_name }} as source_sketch\nfrom pyp5js import *\n\n"
    content += "event_functions = {\n"

    for event in event_function_names:
        content += f'    "{event}": source_sketch.{event},\n'

    content += '}\n\nstart_p5(source_sketch.setup, source_sketch.draw, event_functions)'

    return content


def get_target_sketch_content(sketch_name):
    context = {"sketch_name": sketch_name}
    templates = Environment(loader=FileSystemLoader(pyp5js_files.templates_dir))
    index_template = templates.get_template(
        str(pyp5js_files.target_sketch_template.name)
    )
    return index_template.render(context)
