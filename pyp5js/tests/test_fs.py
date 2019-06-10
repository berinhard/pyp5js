import os
import pytest
import shutil
from unipath import Path
from unittest import TestCase

from pyp5js.fs import Pyp5jsLibFiles, Pyp5jsSketchFiles

pyp5_dir = Path(__file__).ancestor(2).child('pyp5js')

@pytest.fixture
def lib_files():
    return Pyp5jsLibFiles()

def test_dir_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.templates_dir == pyp5_dir.child('templates')
    assert lib_files.templates_dir.exists()
    assert lib_files.assets_dir == pyp5_dir.child('assets')
    assert lib_files.assets_dir.exists()
    assert lib_files.static_dir == pyp5_dir.child('static')
    assert lib_files.static_dir.exists()


def test_files_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.pytop5js == pyp5_dir.child('pytop5js.py')
    assert lib_files.pytop5js.exists()

    assert lib_files.base_sketch == pyp5_dir.child('templates', 'base_sketch.py')
    assert lib_files.base_sketch.exists()

    assert lib_files.pytop5js_template == pyp5_dir.child('templates', 'pytop5js.py.template')
    assert lib_files.pytop5js_template.exists()

    assert lib_files.target_sketch_template == pyp5_dir.child('templates', 'target_sketch.py.template')
    assert lib_files.target_sketch_template.exists()

    assert lib_files.index_html == pyp5_dir.child('templates', 'index.html')
    assert lib_files.index_html.exists()

    assert lib_files.p5js == pyp5_dir.child('static', 'p5', 'p5.min.js')
    assert lib_files.p5js.exists()

    assert lib_files.p5_dom_js == pyp5_dir.child('static', 'p5', 'addons', 'p5.dom.min.js')
    assert lib_files.p5_dom_js.exists()

    assert lib_files.p5_yml == pyp5_dir.child('assets', 'p5_reference.yml')
    assert lib_files.p5_yml.exists()


class Pyp5jsSketchFilesTests(TestCase):

    def setUp(self):
        self.sketch_name = 'foo'
        self.files = Pyp5jsSketchFiles('', self.sketch_name)

    def tearDown(self):
        try:
            if self.files.sketch_dir.exists():
                shutil.rmtree(self.files.sketch_dir)
        except SystemExit:
            pass

    def test_sketch_dir_argument(self):
        assert Path('').child(self.sketch_name) == self.files.sketch_dir  # default value

        self.files = Pyp5jsSketchFiles('foo', self.sketch_name, check_sketch_dir=False)
        assert Path('foo') == self.files.sketch_dir

        # shold stop execution if custom directory does not exist
        self.files = Pyp5jsSketchFiles('foo', self.sketch_name)
        with pytest.raises(SystemExit):
            self.files.sketch_dir

    def test_can_create_sketch(self):
        assert self.files.can_create_sketch() is True
        os.mkdir(self.files.sketch_dir)
        assert self.files.can_create_sketch() is False

    def test_sketch_dirs(self):
        assert Path(self.sketch_name).child('static') == self.files.static_dir
        assert Path(self.sketch_name).child('target') == self.files.target_dir
        assert self.files.TARGET_NAME == 'target'

    def test_sketch_files(self):
        self.files.check_sketch_dir = False
        assert Path(self.sketch_name).child('index.html') == self.files.index_html
        assert Path(self.sketch_name).child('static', 'p5.js') == self.files.p5js
        assert Path(self.sketch_name).child('static', 'p5.dom.js') == self.files.p5_dom_js
        assert Path(self.sketch_name).child('foo.py') == self.files.sketch_py
        assert Path(self.sketch_name).child('target_sketch.py') == self.files.target_sketch

    def test_sketch_exists(self):
        self.files.check_sketch_dir = False
        assert self.files.check_sketch_exists() is False
        os.mkdir(self.files.sketch_dir)
        assert self.files.check_sketch_exists() is False
        with open(self.files.sketch_py, 'w') as fd:
            fd.write("import this")
        assert self.files.check_sketch_exists() is True
