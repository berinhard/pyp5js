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


@pytest.fixture()
def files():
    files = Sketch('foo')
    files.create_sketch_dir()
    yield files
    shutil.rmtree(config.SKETCHBOOK_DIR)


@patch('pyp5js.compiler.TranscryptCompiler')
def test_compile_sketch_js_service(MockedCompiler, files):
    compiler = Mock(spec=TranscryptCompiler)
    MockedCompiler.return_value = compiler

    compile_sketch_js(files)

    MockedCompiler.assert_called_once_with(files)
    compiler.compile_sketch_js.assert_called_once_with()


class TranscryptCompilerTests(TestCase):

    def setUp(self):
        self.files = Sketch('foo')
        self.compiler = TranscryptCompiler(self.files)

        self.files.create_sketch_dir()
        self.files.sketch_py.touch()

    def tearDown(self):
        if config.SKETCHBOOK_DIR.exists():
            shutil.rmtree(config.SKETCHBOOK_DIR)

    def test_transcrypt_target_dir_path(self):
        assert self.files.sketch_dir.joinpath(
            '__target__') == self.compiler.target_dir

    def test_command_line_string(self):
        pyp5_dir = PYP5JS_FILES.install
        target = self.files.target_sketch

        expected = ' '.join([str(c) for c in [
            'transcrypt', '-xp', f'"{pyp5_dir}"', '-k', '-ks', '-b', '-m', '-n', f'"{target}"'
        ]])

        assert expected == self.compiler.command_line

    def test_run_compiler_as_expected(self):
        self.compiler.prepare()
        self.compiler.run_compiler()

        assert self.compiler.target_dir.exists()
        assert self.files.target_sketch.exists()

    def test_run_compiler_as_expected_if_dir_name_with_space(self):
        previous_dir = config.SKETCHBOOK_DIR
        dir_with_space = Path.home().joinpath("pyp5js space dir")
        if not dir_with_space.exists():
            dir_with_space.mkdir()
        config.__dict__["SKETCHBOOK_DIR"] = dir_with_space

        self.files = Sketch('foo')
        self.compiler = TranscryptCompiler(self.files)
        self.files.create_sketch_dir()
        self.files.sketch_py.touch()

        try:
            self.compiler.prepare()
            self.compiler.run_compiler()

            assert self.compiler.target_dir.exists()
            assert self.files.target_sketch.exists()
        finally:
            if dir_with_space.exists():
                shutil.rmtree(dir_with_space)
            config.__dict__["SKETCHBOOK_DIR"] = previous_dir

    def test_clean_up(self):
        self.compiler.target_dir.mkdir()
        self.files.target_sketch.touch()

        self.compiler.clean_up()

        assert not self.compiler.target_dir.exists()
        assert self.files.target_dir.exists()
        assert not self.files.target_sketch.exists()

    def test_prepare_sketch(self):
        expected_content = get_target_sketch_content(self.files)
        assert not self.files.target_sketch.exists()

        self.compiler.prepare()

        assert self.files.target_sketch.exists()
        with self.files.target_sketch.open('r') as fd:
            content = fd.read()
        assert expected_content == content
