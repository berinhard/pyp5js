"""
This script is an auxiliar one to update the final version of pyp5js/pyp5js.py file.

Every time p5.JS add a new method, variable, constant or event function, pyp5js will have to:

    1 - update pyp5js/assets/p5_reference.yml with the new values;
    2 - run $ python pyp5js/pre_compile/update_pytop5js.py;
    3 - release a new version of pyp5js supporting the new features;
"""
import yaml
from cprint import cprint

from pyp5js.fs import LibFiles
from pyp5js.templates_renderers import templates


pyp5js_files = LibFiles()


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


if __name__ == '__main__':
    with open(pyp5js_files.p5_yml) as fd:
        data = yaml.load(fd.read())
        p5_data, dom_data = data['p5'], data['dom']
        methods_names = p5_data['methods'] + dom_data['methods']
        event_function_names = p5_data['events']
        variables_names = p5_data['variables'] + dom_data['variables']

    pyp5_content = get_pytop5js_content(variables_names, methods_names, event_function_names)
    with open(pyp5js_files.pytop5js, 'w') as fd:
        fd.write(pyp5_content)

    cprint.ok(f"File {pyp5js_files.pytop5js} was updated with success.")

    target_content = get_target_sketch_template_content(event_function_names)
    with open(pyp5js_files.target_sketch_template, 'w') as fd:
        fd.write(target_content)

    cprint.ok(f"File {pyp5js_files.target_sketch_template} was updated with success.")
