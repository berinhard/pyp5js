import pytest
import shutil
from unittest import TestCase

from pyp5js.config import SKETCHBOOK_DIR, PYODIDE_INTERPRETER
from pyp5js.config.sketch import P5_JS_CDN
from pyp5js.exceptions import SketchDirAlreadyExistException
from pyp5js.sketch import Sketch
from pyp5js.exceptions import InvalidName


class SketchTests(TestCase):

    def setUp(self):
        self.base_dir = SKETCHBOOK_DIR
        self.sketch_name = 'foo'
        self.files = Sketch(self.sketch_name)

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

    def test_sketch(self):
        self.files.check_sketch_dir = False
        assert self.get_expected_path('index.html') == self.files.index_html
        assert self.get_expected_path('static', 'p5.js') == self.files.p5js
        assert self.get_expected_path('foo.py') == self.files.sketch_py
        assert self.get_expected_path('.properties.json') == self.files.config_file

    def test_target_sketch_variations(self):
        assert self.get_expected_path('target_sketch.py') == self.files.target_sketch
        self.files.config.interpreter = PYODIDE_INTERPRETER
        assert self.get_expected_path('target', 'target_sketch.js') == self.files.target_sketch

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
        files = Sketch('123name')
        with pytest.raises(InvalidName):
            files.validate_name()

    def test_raise_exception_when_name_contains_non_alphanumeric_chars(self):
        files = Sketch('name&')
        with pytest.raises(InvalidName):
            files.validate_name()

    def test_raise_exception_when_name_creating_dir_with_invalid_name(self):
        files = Sketch('name&')
        with pytest.raises(InvalidName):
            files.create_sketch_dir()

    def test_name_should_accept_underscore_in_the_beginning(self):
        file = Sketch('__name__')
        assert file.sketch_name == '__name__'

    def test_name_should_accept_underscore_in_the_middle(self):
        file = Sketch('na_me')
        assert file.sketch_name == 'na_me'

    def test_loads_config_from_config_file(self):
        files = Sketch('bar', interpreter=PYODIDE_INTERPRETER)
        files.create_sketch_dir()  # writes config file json

        same_files = Sketch('bar')

        assert same_files.config_file == files.config_file
        assert same_files.config.interpreter == PYODIDE_INTERPRETER

    def test_sketch_custom_urls(self):
        files = Sketch(self.files.sketch_name, p5_js_url="static/p5.js", pyodide_js_url="static/pyodide/pyodide.js")
        urls = files.urls
        assert "static/p5.js" == urls.p5_js_url
        assert "static/pyodide/pyodide.js" == urls.pyodide_js_url
        assert "target/target_sketch.js" == urls.sketch_js_url

    def test_sketch_urls(self):
        urls = self.files.urls
        assert P5_JS_CDN == urls.p5_js_url
        assert PYODIDE_JS_CDN == urls.pyodide_js_url
        assert "target/target_sketch.js" == urls.sketch_js_url
