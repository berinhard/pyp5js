import os
import shutil
from pathlib import Path
from cprint import cprint

from pyp5js.config import SKETCHBOOK_DIR


class SketchFiles():
    TARGET_NAME = 'target'
    STATIC_NAME = 'static'

    def __init__(self, sketch_name):
        self.sketch_name = sketch_name
        self.from_lib = LibFiles()

    def create_sketch_dir(self):
        if self.sketch_dir.exists():
            cprint.err(f'Cannot create the directory {self.sketch_dir} because it already exists.', interrupt=True)
        os.makedirs(self.sketch_dir)
        self.static_dir.mkdir()
        self.target_dir.mkdir()

    @property
    def sketch_exists(self):
        return self.sketch_py.exists()

    @property
    def sketch_dir(self):
        return SKETCHBOOK_DIR.joinpath(f'{self.sketch_name}')

    @property
    def static_dir(self):
        return self.sketch_dir.joinpath(self.STATIC_NAME)

    @property
    def index_html(self):
        return self.sketch_dir.joinpath('index.html')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5.js')

    @property
    def p5_dom_js(self):
        return self.static_dir.joinpath('p5.dom.js')

    @property
    def target_sketch(self):
        return self.sketch_dir.joinpath("target_sketch.py")

    @property
    def sketch_py(self):
        return self.sketch_dir.joinpath(f'{self.sketch_name}.py')

    @property
    def target_dir(self):
        return self.sketch_dir.joinpath(self.TARGET_NAME)

    def __eq__(self, other):
        return self.sketch_name == other.sketch_name


class LibFiles():

    def __init__(self):
        self.install = Path(__file__).parent

    @property
    def templates_dir(self):
        return self.install.joinpath('templates')

    @property
    def assets_dir(self):
        return self.install.joinpath('assets')

    @property
    def static_dir(self):
        return self.install.joinpath('static')

    @property
    def pytop5js(self):
        return self.install.joinpath('pyp5js.py')

    @property
    def base_sketch(self):
        return self.templates_dir.joinpath('base_sketch.py.template')

    @property
    def pytop5js_template(self):
        return self.templates_dir.joinpath('pyp5js.py.template')

    @property
    def target_sketch_template(self):
        return self.templates_dir.joinpath('target_sketch.py.template')

    @property
    def index_html(self):
        return self.templates_dir.joinpath('index.html')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5', 'p5.min.js')

    @property
    def p5_dom_js(self):
        return self.static_dir.joinpath('p5', 'addons', 'p5.dom.min.js')

    @property
    def p5_yml(self):
        return self.assets_dir.joinpath('p5_reference.yml')
