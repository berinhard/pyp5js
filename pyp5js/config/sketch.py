import json
from pathlib import Path

from pyp5js.config.fs import PYP5JS_FILES

TRANSCRYPT_INTERPRETER = 'transcrypt'
PYODIDE_INTERPRETER = 'pyodide'

class SketchConfig:

    @classmethod
    def from_json(cls, json_file_path):
        with open(json_file_path) as fd:
            config_data = json.load(fd)
            return cls(**config_data)

    def __init__(self, interpreter, index_template=""):
        self.interpreter = interpreter
        self.index_template = index_template # must be a string

    @property
    def index_template_path(self):
        return Path(self.index_template).absolute()

    def write(self, fname):
        index_template = ""
        if self.index_template and self.index_template_path.exists():
            index_template = str(self.index_template_path.resolve())
        with open(fname, "w") as fd:
            data = {
                "interpreter": self.interpreter,
                "index_template": index_template
            }
            json.dump(data, fd)

    @property
    def is_transcrypt(self):
        return self.interpreter == TRANSCRYPT_INTERPRETER

    @property
    def is_pyodide(self):
        return self.interpreter == PYODIDE_INTERPRETER

    def get_index_template(self):
        if self.index_template and self.index_template_path.exists():
            return self.index_template_path
        index_map = {
            TRANSCRYPT_INTERPRETER: PYP5JS_FILES.transcrypt_index_html,
            PYODIDE_INTERPRETER: PYP5JS_FILES.pyodide_index_html,
        }
        return index_map[self.interpreter]

    def get_target_js_template(self):
        target_map = {
            TRANSCRYPT_INTERPRETER: PYP5JS_FILES.transcrypt_target_sketch_template,
            PYODIDE_INTERPRETER: PYP5JS_FILES.pyodide_target_sketch_template,
        }
        return target_map[self.interpreter]

    def get_base_sketch_template(self):
        base_map = {
            TRANSCRYPT_INTERPRETER: PYP5JS_FILES.transcrypt_base_sketch_template,
            PYODIDE_INTERPRETER: PYP5JS_FILES.pyodide_base_sketch_template,
        }
        return base_map[self.interpreter]
