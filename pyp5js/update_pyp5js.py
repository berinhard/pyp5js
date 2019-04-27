import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from unipath import Path
from cprint import cprint

PYP5_DIR = Path(__file__).parent
TEMPLATES_DIR = PYP5_DIR.child('templates')
ASSETS_DIR = PYP5_DIR.child('assets')

if __name__ == '__main__':
    with open(ASSETS_DIR.child('p5_methods.yml')) as fd:
        methods_names = yaml.load(fd.read())['methods']
    with open(ASSETS_DIR.child('p5_variables.yml')) as fd:
        variables_names = yaml.load(fd.read())['variables']

    templates = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    pyp5_template = templates.get_template('pyp5js.py.template')
    context = {'function_names': methods_names, 'variables_names': variables_names}
    pyp5_content = pyp5_template.render(context)

    pyp5_path = PYP5_DIR.child('pyp5js.py')
    with open(pyp5_path, 'w') as fd:
        fd.write(pyp5_content)

    cprint.ok(f"File {pyp5_path} was updated with success.")
