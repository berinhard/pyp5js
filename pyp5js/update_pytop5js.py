import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from unipath import Path
from cprint import cprint

from pyp5js.fs import Pyp5jsLibFiles, Pyp5jsSketchFiles

PYP5_DIR = Path(__file__).parent
TEMPLATES_DIR = PYP5_DIR.child('templates')
ASSETS_DIR = PYP5_DIR.child('assets')

if __name__ == '__main__':
    pyp5js_files = Pyp5jsLibFiles()

    with open(pyp5js_files.p5_yml) as fd:
        data = yaml.load(fd.read())
        methods_names = data['methods']
        event_function_names = data['events']
        variables_names = data['variables']


    templates = Environment(loader=FileSystemLoader(pyp5js_files.templates_dir))
    pyp5_template = templates.get_template(
        str(pyp5js_files.pytop5js_template.name)
    )
    context = {
        'function_names': methods_names,
        'variables_names': variables_names,
        'event_function_names': event_function_names,
    }
    pyp5_content = pyp5_template.render(context)

    with open(pyp5js_files.pytop5js, 'w') as fd:
        fd.write(pyp5_content)

    cprint.ok(f"File {pyp5js_files.pytop5js} was updated with success.")
