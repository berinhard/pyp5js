import pytest
import shutil
from pathlib import Path
from unittest import TestCase

from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.config import SKETCHBOOK_DIR, PYODIDE_INTERPRETER
from pyp5js.exceptions import SketchDirAlreadyExistException
from pyp5js.fs import SketchFiles
from pyp5js.exceptions import InvalidName

pyp5_dir = Path(__file__).parents[2].joinpath('pyp5js')

@pytest.fixture
def lib_files():
    return PYP5JS_FILES

def test_dir_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.templates_dir == pyp5_dir.joinpath('templates')
    assert lib_files.templates_dir.exists()
    assert lib_files.assets_dir == pyp5_dir.joinpath('assets')
    assert lib_files.assets_dir.exists()
    assert lib_files.static_dir == pyp5_dir.joinpath('assets', 'static')
    assert lib_files.static_dir.exists()


def test_files_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.pytop5js == pyp5_dir.joinpath('pyp5js.py')
    assert lib_files.pytop5js.exists()

    assert lib_files.base_sketch == pyp5_dir.joinpath('templates', 'base_sketch.py.template')
    assert lib_files.base_sketch.exists()

    assert lib_files.target_sketch_template == pyp5_dir.joinpath('templates', 'target_sketch.py.template')
    assert lib_files.target_sketch_template.exists()

    assert lib_files.transcrypt_index_html == pyp5_dir.joinpath('templates', 'transcrypt_index.html')
    assert lib_files.transcrypt_index_html.exists()

    assert lib_files.pyodide_index_html == pyp5_dir.joinpath('templates', 'pyodide_index.html')
    assert lib_files.pyodide_index_html.exists()

    assert lib_files.p5js == pyp5_dir.joinpath('assets', 'static', 'p5', 'p5.min.js')
    assert lib_files.p5js.exists()

    assert lib_files.p5_yml == pyp5_dir.joinpath('assets', 'p5_reference.yml')
    assert lib_files.p5_yml.exists()


class SketchFilesTests(TestCase):

    def setUp(self):
        self.base_dir = SKETCHBOOK_DIR
        self.sketch_name = 'foo'
        self.files = SketchFiles(self.sketch_name)

    def tearDown(self):
        if self.base_dir.exists():
            shutil.rmtree(self.base_dir)

    def get_expected_path(self, *args):
        return self.base_dir.joinpath(self.sketch_name, *args)

    def test_sketch_dirs(self):
        assert self.get_expected_path() == self.files.sketch_dir
        assert self.get_expected_path('static') == self.files.static_dir
        assert self.get_expected_path('target') == self.files.target_dir
        assert self.files.TARGET_NAME == 'target'

    def test_sketch_files(self):
        self.files.check_sketch_dir = False
        assert self.get_expected_path('index.html') == self.files.index_html
        assert self.get_expected_path('static', 'p5.js') == self.files.p5js
        assert self.get_expected_path('foo.py') == self.files.sketch_py
        assert self.get_expected_path('target_sketch.py') == self.files.target_sketch
        assert self.get_expected_path('properties.json') == self.files.config_file

    def test_create_dirs(self):
        assert self.files.sketch_dir.exists() is False
        assert self.files.static_dir.exists() is False
        assert self.files.target_dir.exists() is False
        assert self.files.config_file.exists() is False

        self.files.create_sketch_dir()

        assert self.files.sketch_dir.exists() is True
        assert self.files.static_dir.exists() is True
        assert self.files.target_dir.exists() is True
        assert self.files.config_file.exists() is True

        with pytest.raises(SketchDirAlreadyExistException):
            self.files.create_sketch_dir()

    def test_raise_exception_when_name_starts_with_numbers(self):
        files = SketchFiles('123name')
        with pytest.raises(InvalidName):
            files.validate_name()

    def test_raise_exception_when_name_contains_non_alphanumeric_chars(self):
        files = SketchFiles('name&')
        with pytest.raises(InvalidName):
            files.validate_name()

    def test_raise_exception_when_name_creating_dir_with_invalid_name(self):
        files = SketchFiles('name&')
        with pytest.raises(InvalidName):
            files.create_sketch_dir()

    def test_name_should_accept_underscore_in_the_beginning(self):
        file = SketchFiles('__name__')
        assert file.sketch_name == '__name__'

    def test_name_should_accept_underscore_in_the_middle(self):
        file = SketchFiles('na_me')
        assert file.sketch_name == 'na_me'

    def test_loads_config_from_config_file(self):
        files = SketchFiles('bar', interpreter=PYODIDE_INTERPRETER)
        files.create_sketch_dir()  # writes config file json

        same_files = SketchFiles('bar')

        assert same_files.config_file == files.config_file
        assert same_files.config.interpreter == PYODIDE_INTERPRETER
