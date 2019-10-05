import pytest
import shutil
from pathlib import Path
from unittest import TestCase

from pyp5js.fs import LibFiles, SketchFiles

pyp5_dir = Path(__file__).parents[2].joinpath('pyp5js')

@pytest.fixture
def lib_files():
    return LibFiles()

def test_dir_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.templates_dir == pyp5_dir.joinpath('templates')
    assert lib_files.templates_dir.exists()
    assert lib_files.assets_dir == pyp5_dir.joinpath('assets')
    assert lib_files.assets_dir.exists()
    assert lib_files.static_dir == pyp5_dir.joinpath('static')
    assert lib_files.static_dir.exists()


def test_files_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.pytop5js == pyp5_dir.joinpath('pyp5js.py')
    assert lib_files.pytop5js.exists()

    assert lib_files.base_sketch == pyp5_dir.joinpath('templates', 'base_sketch.py.template')
    assert lib_files.base_sketch.exists()

    assert lib_files.pytop5js_template == pyp5_dir.joinpath('templates', 'pyp5js.py.template')
    assert lib_files.pytop5js_template.exists()

    assert lib_files.target_sketch_template == pyp5_dir.joinpath('templates', 'target_sketch.py.template')
    assert lib_files.target_sketch_template.exists()

    assert lib_files.index_html == pyp5_dir.joinpath('templates', 'index.html')
    assert lib_files.index_html.exists()

    assert lib_files.p5js == pyp5_dir.joinpath('static', 'p5', 'p5.min.js')
    assert lib_files.p5js.exists()

    assert lib_files.p5_dom_js == pyp5_dir.joinpath('static', 'p5', 'addons', 'p5.dom.min.js')
    assert lib_files.p5_dom_js.exists()

    assert lib_files.p5_yml == pyp5_dir.joinpath('assets', 'p5_reference.yml')
    assert lib_files.p5_yml.exists()


class SketchFilesTests(TestCase):

    def setUp(self):
        self.sketch_name = 'foo'
        self.files = SketchFiles('', self.sketch_name)

    def tearDown(self):
        try:
            if self.files.sketch_dir.exists():
                shutil.rmtree(self.files.sketch_dir)
        except SystemExit:
            pass

    def test_sketch_dir_argument(self):
        assert Path('').joinpath(self.sketch_name) == self.files.sketch_dir  # default value

        self.files = SketchFiles('foo', self.sketch_name, check_sketch_dir=False)
        assert Path('foo') == self.files.sketch_dir

        # shold stop execution if custom directory does not exist
        self.files = SketchFiles('foo', self.sketch_name)
        with pytest.raises(SystemExit):
            self.files.sketch_dir

    def test_can_create_sketch(self):
        assert self.files.can_create_sketch() is True
        self.files.sketch_dir.mkdir()
        assert self.files.can_create_sketch() is False

    def test_sketch_dirs(self):
        assert Path(self.sketch_name).joinpath('static') == self.files.static_dir
        assert Path(self.sketch_name).joinpath('target') == self.files.target_dir
        assert self.files.TARGET_NAME == 'target'

    def test_sketch_files(self):
        self.files.check_sketch_dir = False
        assert Path(self.sketch_name).joinpath('index.html') == self.files.index_html
        assert Path(self.sketch_name).joinpath('static', 'p5.js') == self.files.p5js
        assert Path(self.sketch_name).joinpath('static', 'p5.dom.js') == self.files.p5_dom_js
        assert Path(self.sketch_name).joinpath('foo.py') == self.files.sketch_py
        assert Path(self.sketch_name).joinpath('target_sketch.py') == self.files.target_sketch

    def test_sketch_exists(self):
        self.files.check_sketch_dir = False
        assert self.files.check_sketch_exists() is False
        self.files.sketch_dir.mkdir()
        assert self.files.check_sketch_exists() is False
        with self.files.sketch_py.open('w') as fd:
            fd.write("import this")
        assert self.files.check_sketch_exists() is True

    def test_sketch_files_holds_reference_to_lib_files(self):
        lib_files = LibFiles()
        assert isinstance(self.files.from_lib, LibFiles)
        assert self.files.from_lib.install == lib_files.install
