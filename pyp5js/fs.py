import os
from unipath import Path
from cprint import cprint
from jinja2 import Environment, FileSystemLoader


class Pyp5jsSketchFiles():

    def __init__(self, sketch_dir, sketch_name, check_sketch_dir=True):
        self._sketch_dir = sketch_dir or ''
        self.sketch_name = sketch_name
        self.check_sketch_dir = check_sketch_dir

    def can_create_sketch(self):
        if self.sketch_dir.exists():
            cprint.warn(f"Cannot configure a new sketch.")
            cprint.err(f"The directory {self.sketch_dir} already exists.", interrupt=True)

    def check_sketch_exists(self):
        return bool(self.sketch_dir and self.sketch_py)

    @property
    def sketch_dir(self):
        sketch_dir = Path(self._sketch_dir)

        if not sketch_dir:
            return sketch_dir.child(f'{self.sketch_name}')

        if self.check_sketch_dir and not sketch_dir.exists():
            cprint.err(f"The directory {sketch_dir} does not exists.", interrupt=True)

        return sketch_dir

    @property
    def static_dir(self):
        return self.sketch_dir.child('static')

    @property
    def index_html(self):
        return self.sketch_dir.child('index.html')

    @property
    def p5js(self):
        return self.static_dir.child('p5.js')

    @property
    def sketch_py(self):
        py_file = self.sketch_dir.child(f'{self.sketch_name}.py')

        if self.check_sketch_dir and not py_file.exists():
            cwd_py_file = Path(os.getcwd()).child(f"{sketch_name}.py")
            if not cwd_py_file.exists():
                cprint.warn(f"Couldn't find the sketch.")
                cprint.err(f"Neither the file {py_file} or {cwd_py_file} exist.", interrupt=True)

            py_file = cwd_py_file
            self._sketch_dir = py_file.parent

        return py_file

    @property
    def target_dir(self):
        return self.sketch_dir.child("target")


class Pyp5jsLibFiles():

    def __init__(self):
        self.install = Path(__file__).parent

    @property
    def templates_dir(self):
        return self.install.child('templates')

    @property
    def base_sketch(self):
        return self.templates_dir.child('base_sketch.py')

    @property
    def p5js(self):
        return self.install.child('static', 'p5.js')

    def render_new_index(self, context):
        templates = Environment(loader=FileSystemLoader(self.templates_dir))
        index_template = templates.get_template('index.html')
        return index_template.render(context)
