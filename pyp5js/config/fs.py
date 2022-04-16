"""
pyp5js
Copyright (C) 2019-2021 Bernardo Fontes

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
    def static_dir(self):
        return self.install.joinpath('http', 'static')

    @property
    def pytop5js(self):
        return self.transcrypt_conf_dir.joinpath('pyp5js.py')

    @property
    def p5js(self):
        return self.static_dir.joinpath('js', 'p5', 'p5.min.js')

    @property
    def p5_yml(self):
        return self.static_dir.joinpath('p5_reference.yml')

    ##### TRANSCRYPT SPECIFICS

    @property
    def transcrypt_conf_dir(self):
        return self.templates_dir.joinpath('transcrypt')

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

    @property
    def pyodide_js_dir(self):
        return self.static_dir / "js" / "pyodide"


PYP5JS_FILES = LibFiles()
