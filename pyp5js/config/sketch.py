"""
pyp5js
Copyright (C) 2019-2021 The pyp5js Contributors

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import json
from pathlib import Path

from pyp5js.config.fs import PYP5JS_FILES

TRANSCRYPT_INTERPRETER = 'transcrypt'
PYODIDE_INTERPRETER = 'pyodide'
P5_JS_CDN = 'https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.min.js'
PYODIDE_JS_CDN = 'https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js'


class SketchConfig:

    @classmethod
    def from_json(cls, json_file_path):
        with open(json_file_path) as fd:
            config_data = json.load(fd)
            return cls(**config_data)

    def __init__(self, interpreter, **kwargs):
        self.interpreter = interpreter
        self.index_template = kwargs.get("index_template", "")
        self.p5_js_url = kwargs.get("p5_js_url", P5_JS_CDN)
        self.pyodide_js_url = kwargs.get("pyodide_js_url", PYODIDE_JS_CDN)

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
                "p5_js_url": self.p5_js_url,
            }
            if self.index_template:
                data.update({"index_template": index_template})
            if self.is_pyodide:
                data.update({"pyodide_js_url": self.pyodide_js_url})
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
