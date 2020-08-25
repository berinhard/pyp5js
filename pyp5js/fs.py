import os
import re
import shutil
from pathlib import Path
from cprint import cprint
from collections import namedtuple

from pyp5js import config
from pyp5js.exceptions import SketchDirAlreadyExistException, InvalidName


SketchUrls = namedtuple('SketchUrls', ['p5_js_url', 'sketch_js_url'])


class SketchFiles():
    TARGET_NAME = 'target'
    STATIC_NAME = 'static'

    def __init__(self, sketch_name):
        self.sketch_name = sketch_name
        self.from_lib = LibFiles()

    def validate_name(self):
        does_not_start_with_letter_or_underscore = r'^[^a-zA-Z_]'
        contains_non_alphanumerics_except_underscore = r'[^a-zA-Z0-9_]'
        if re.match(does_not_start_with_letter_or_underscore, self.sketch_name) or \
           re.search(contains_non_alphanumerics_except_underscore, self.sketch_name):
            raise InvalidName(self.sketch_name)

    def create_sketch_dir(self):
        self.validate_name()

        if self.sketch_dir.exists():
            raise SketchDirAlreadyExistException(self.sketch_dir.resolve())

        os.makedirs(self.sketch_dir)
        self.static_dir.mkdir()
        self.target_dir.mkdir()

    @property
    def sketch_exists(self):
        return self.sketch_py.exists()

    @property
    def has_all_files(self):
        return all([
            self.sketch_exists,
            self.index_html.exists()
        ])

    @property
    def sketch_dir(self):
        return config.SKETCHBOOK_DIR.joinpath(f'{self.sketch_name}')

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

    @property
    def urls(self):
        return SketchUrls(
            p5_js_url=f"{self.STATIC_NAME}/p5.js",
            sketch_js_url=f"{self.TARGET_NAME}/target_sketch.js",
        )


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
    def target_sketch_template(self):
        return self.templates_dir.joinpath('target_sketch.py.template')

    @property
    def index_html(self):
        return self.templates_dir.joinpath('index.html')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5', 'p5.min.js')

    @property
    def p5_yml(self):
        return self.assets_dir.joinpath('p5_reference.yml')
