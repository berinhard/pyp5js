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
import pytest
import shutil
from unittest import TestCase
from unittest.mock import Mock, patch

from pyp5js import commands
from pyp5js.config import SKETCHBOOK_DIR, TRANSCRYPT_INTERPRETER, PYODIDE_INTERPRETER
from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.exceptions import PythonSketchDoesNotExist, SketchDirAlreadyExistException, InvalidName
from pyp5js.sketch import Sketch

from .fixtures import sketch


def test_compile_sketch(sketch):
    sketch.sketch_py.touch()
    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        output = commands.compile_sketch('foo')

        assert output == sketch
        compiler.assert_called_once_with(sketch, force_local=False)


def test_compile_sketch_error_if_sketch_does_not_exist(sketch):
    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        with pytest.raises(PythonSketchDoesNotExist):
            commands.compile_sketch('foo')
        assert not compiler.called


def test_compile_sketch_error_if_invalid_sketch(sketch):
    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        with pytest.raises(InvalidName):
            commands.compile_sketch('123foo')
        assert not compiler.called


def test_monitor_sketch(sketch):
    sketch.sketch_py.touch()
    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        commands.monitor_sketch('foo')

        monitor.assert_called_once_with(sketch)


def test_monitor_sketch_error_if_sketch_does_not_exist(sketch):
    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        with pytest.raises(PythonSketchDoesNotExist):
            commands.monitor_sketch('foo')
        assert not monitor.called


def test_monitor_sketch_error_if_invalid_name(sketch):
    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        with pytest.raises(InvalidName):
            commands.monitor_sketch('1234foo')
        assert not monitor.called


class TestNewSketchCommand(TestCase):

    def setUp(self):
        self.sketch_name = 'foo'
        self.sketch = Sketch(self.sketch_name)

    def tearDown(self):
        if SKETCHBOOK_DIR.exists():
            shutil.rmtree(SKETCHBOOK_DIR)

    def test_create_new_sketch_with_all_required_files(self):
        commands.new_sketch(self.sketch_name)

        assert self.sketch.index_html.exists()
        assert self.sketch.sketch_py.exists()
        assert not self.sketch.p5js.exists()
        assert self.sketch.config_file.exists()
        assert self.sketch.config.interpreter == TRANSCRYPT_INTERPRETER
        assert self.sketch.config.index_template == ""

    def test_create_pyodide_sketch(self):
        commands.new_sketch(self.sketch_name, interpreter=PYODIDE_INTERPRETER)
        self.sketch = Sketch(self.sketch_name)  # read config after init

        assert self.sketch.index_html.exists()
        assert self.sketch.sketch_py.exists()
        assert not self.sketch.p5js.exists()
        assert self.sketch.config_file.exists()
        assert self.sketch.config.interpreter == PYODIDE_INTERPRETER

    def test_raise_exception_if_dir_already_exist(self):
        self.sketch.create_sketch_dir()

        with pytest.raises(SketchDirAlreadyExistException):
            commands.new_sketch(self.sketch_name)

    def test_create_sketch_with_custom_index(self):
        template = PYP5JS_FILES.install.parent / "docs" / "examples" / "transcrypt" / "index.html.template"
        commands.new_sketch(self.sketch_name, template_file=template)

        assert self.sketch.index_html.exists()
        with open(self.sketch.index_html) as fd:
            content = fd.read()
        assert "demoContainer" in content

    def test_create_sketch_using_local_installed_assets(self):
        commands.new_sketch(self.sketch_name, use_cdn=False)

        assert self.sketch.p5js.exists()
