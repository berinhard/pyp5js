from pathlib import Path


class LibFiles():
    """
    This class abstracts pyp5js lib files path from the filesystem.
    It expose properties for the directories and files.
    Every property returns a pathlib.Path object
    """

    def __init__(self):
        self.install = Path(__file__).parents[1]

    ##### GENERAL PURPOSE

    @property
    def templates_dir(self):
        return self.install.joinpath('templates')

    @property
    def assets_dir(self):
        return self.install.joinpath('assets')

    @property
    def static_dir(self):
        return self.assets_dir.joinpath('static')

    @property
    def pytop5js(self):
        return self.install.joinpath('pyp5js.py')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5', 'p5.min.js')

    @property
    def p5_yml(self):
        return self.assets_dir.joinpath('p5_reference.yml')

    ##### TRANSCRYPT SPECIFICS

    @property
    def transcrypt_index_html(self):
        return self.templates_dir.joinpath('transcrypt', 'index.html')

    @property
    def transcrypt_target_sketch_template(self):
        return self.templates_dir.joinpath('transcrypt', 'target_sketch.py.template')

    @property
    def transcrypt_base_sketch_template(self):
        return self.templates_dir.joinpath('transcrypt', 'base_sketch.py.template')

    ##### PYODIDE SPECIFICS

    @property
    def pyodide_target_sketch_template(self):
        return self.templates_dir.joinpath('pyodide', 'target_sketch.js.template')

    @property
    def pyodide_index_html(self):
        return self.templates_dir.joinpath('pyodide', 'index.html')

    @property
    def pyodide_base_sketch_template(self):
        return self.templates_dir.joinpath('pyodide', 'base_sketch.py.template')


PYP5JS_FILES = LibFiles()
