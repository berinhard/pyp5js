from unipath import Path
from cprint import cprint
from jinja2 import Environment, FileSystemLoader


class Pyp5jsSketchFiles():
    BASE_DIR = ''

    def __init__(self, sketch_dir, sketch_name, check_sketch_dir=True):
        self._sketch_dir = sketch_dir or self.BASE_DIR
        self.sketch_name = sketch_name
        self.check_sketch_dir = check_sketch_dir

    def can_create_sketch(self):
        if self.sketch_dir.exists():
            cprint.warn(f"Cannot configure a new sketch.")
            cprint.err(f"The directory {self.sketch_dir} already exists.", interrupt=True)

    @property
    def sketch_dir(self):
        sketch_dir = Path(self._sketch_dir)

        if not sketch_dir.exists() and self.check_sketch_dir:
            cprint.err(f"The directory {sketch_dir} does not exists.", interrupt=True)

        if self._sketch_dir == self.BASE_DIR:
            return sketch_dir.child(f'{self.sketch_name}')

        return sketch_dir

    @property
    def static_dir(self):
        return self.sketch_dir.child('static')

    @property
    def index_html(self):
        return self.sketch_dir.child('index_html')

    @property
    def p5js(self):
        return self.static_dir.child('p5.js')

    @property
    def sketch_py(self):
        return self.sketch_dir.child(f'{self.sketch_name}.py')


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
