import pytest
from unipath import Path

from pyp5js.fs import Pyp5jsLibFiles

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

    assert lib_files.index_html == pyp5_dir.child('templates', 'index.html')
    assert lib_files.index_html.exists()

    assert lib_files.p5js == pyp5_dir.child('static', 'p5.js')
    assert lib_files.p5js.exists()

    assert lib_files.p5_yml == pyp5_dir.child('assets', 'p5_reference.yml')
    assert lib_files.p5_yml.exists()
