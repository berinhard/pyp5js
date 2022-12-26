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
from pathlib import Path
from unittest import TestCase
from unittest.mock import Mock, patch

from pyp5js.compiler import TranscryptCompiler, compile_sketch_js
from pyp5js import config
from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.sketch import Sketch
from pyp5js.templates_renderers import get_target_sketch_content

from .fixtures import sketch


@patch('pyp5js.compiler.TranscryptCompiler')
def test_compile_sketch_js_service(MockedCompiler, sketch):
    compiler = Mock(spec=TranscryptCompiler)
    MockedCompiler.return_value = compiler

    compile_sketch_js(sketch)

    MockedCompiler.assert_called_once_with(sketch, force_local=False)
    compiler.compile_sketch_js.assert_called_once_with()


class TranscryptCompilerTests(TestCase):

    def setUp(self):
        self.sketch = Sketch('foo')
        self.compiler = TranscryptCompiler(self.sketch)

        self.sketch.create_sketch_dir()
        self.sketch.sketch_py.touch()

    def tearDown(self):
        if config.SKETCHBOOK_DIR.exists():
            shutil.rmtree(config.SKETCHBOOK_DIR)

    def test_transcrypt_target_dir_path(self):
        assert self.sketch.sketch_dir.joinpath(
            '__target__') == self.compiler.target_dir

    def test_command_line_string(self):
        pyp5_dir = PYP5JS_FILES.transcrypt_conf_dir
        target = self.sketch.target_sketch

        expected = ' '.join([str(c) for c in [
            'transcrypt', '-xp', f'"{pyp5_dir}"', '-k', '-ks', '-b', '-m', '-n', f'"{target}"'
        ]])

        assert expected == self.compiler.command_line

    def test_run_compiler_as_expected(self):
        self.compiler.prepare()
        self.compiler.run_compiler()

        assert self.compiler.target_dir.exists()
        assert self.sketch.target_sketch.exists()

    def test_run_compiler_as_expected_if_dir_name_with_space(self):
        previous_dir = config.SKETCHBOOK_DIR
        dir_with_space = Path.home().joinpath("pyp5js space dir")
        if not dir_with_space.exists():
            dir_with_space.mkdir()
        config.__dict__["SKETCHBOOK_DIR"] = dir_with_space

        self.sketch = Sketch('foo')
        self.compiler = TranscryptCompiler(self.sketch)
        self.sketch.create_sketch_dir()
        self.sketch.sketch_py.touch()

        try:
            self.compiler.prepare()
            self.compiler.run_compiler()

            assert self.compiler.target_dir.exists()
            assert self.sketch.target_sketch.exists()
        finally:
            if dir_with_space.exists():
                shutil.rmtree(dir_with_space)
            config.__dict__["SKETCHBOOK_DIR"] = previous_dir

    def test_clean_up(self):
        self.compiler.target_dir.mkdir()
        self.sketch.target_sketch.touch()

        self.compiler.clean_up()

        assert not self.compiler.target_dir.exists()
        assert self.sketch.target_dir.exists()
        assert not self.sketch.target_sketch.exists()

    def test_prepare_sketch(self):
        expected_content = get_target_sketch_content(self.sketch)
        assert not self.sketch.target_sketch.exists()

        self.compiler.prepare()

        assert self.sketch.target_sketch.exists()
        with self.sketch.target_sketch.open('r') as fd:
            content = fd.read()
        assert expected_content == content
