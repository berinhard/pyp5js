import yaml
from cprint import cprint

from pyp5js.fs import Pyp5jsLibFiles, Pyp5jsSketchFiles
from pyp5js.templates_renderer import get_pytop5js_content

if __name__ == '__main__':
    pyp5js_files = Pyp5jsLibFiles()

    with open(pyp5js_files.p5_yml) as fd:
        data = yaml.load(fd.read())
        methods_names = data['methods']
        event_function_names = data['events']
        variables_names = data['variables']

    pyp5_content = get_pytop5js_content(variables_names, methods_names, event_function_names)
    with open(pyp5js_files.pytop5js, 'w') as fd:
        fd.write(pyp5_content)

    cprint.ok(f"File {pyp5js_files.pytop5js} was updated with success.")
