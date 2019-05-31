from jinja2 import Environment, FileSystemLoader, select_autoescape

from pyp5js.fs import Pyp5jsLibFiles

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


def get_target_sketch_template_content(event_function_names):
    content = "import {{ sketch_name }} as source_sketch\nfrom pytop5js import *\n\n"
    content += "event_functions = {\n"

    for event in event_function_names:
        content += f'    "{event}": source_sketch.{event},\n'

    content += '}\n\nstart_p5(sketch_source.setup, sketch_source.draw, event_functions)'

    return content
