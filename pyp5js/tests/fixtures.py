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
import json
import os
import shutil
from pytest import fixture
from tempfile import NamedTemporaryFile

from pyp5js.config import TRANSCRYPT_INTERPRETER, PYODIDE_INTERPRETER
from pyp5js.config.sketch import SketchConfig
from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.config import SKETCHBOOK_DIR
from pyp5js.sketch import Sketch


@fixture
def lib_files():
    return PYP5JS_FILES


@fixture()
def sketch():
    files = Sketch('foo')
    files.create_sketch_dir()
    yield files
    shutil.rmtree(SKETCHBOOK_DIR)


@fixture()
def sketch_pyodide():
    files = Sketch('foo', interpreter=PYODIDE_INTERPRETER)
    files.create_sketch_dir()
    yield files
    shutil.rmtree(SKETCHBOOK_DIR)

@fixture
def transcrypt_json_file():
    try:
        fd = NamedTemporaryFile(mode='w', delete=False)
        data = {"interpreter": "transcrypt"}
        json.dump(data, fd)
        filename = fd.name
        fd.seek(0)
        fd.close()
        yield filename
    finally:
        os.remove(filename)

@fixture
def pyodide_json_file():
    try:
        fd = NamedTemporaryFile(mode='w', delete=False)
        data = {"interpreter": "pyodide"}
        json.dump(data, fd)
        filename = fd.name
        fd.seek(0)
        fd.close()
        yield filename
    finally:
        os.remove(filename)

@fixture
def custom_index_json_file():
    try:
        fd = NamedTemporaryFile(mode='w', delete=False)
        data = {"interpreter": "transcrypt", "index_template": "docs/examples/transcrypt/index.html.template"}
        json.dump(data, fd)
        filename = fd.name
        fd.seek(0)
        fd.close()
        yield filename
    finally:
        os.remove(filename)

@fixture
def transcrypt_config():
    return SketchConfig(interpreter=TRANSCRYPT_INTERPRETER)

@fixture
def pyodide_config():
    return SketchConfig(interpreter=PYODIDE_INTERPRETER)
