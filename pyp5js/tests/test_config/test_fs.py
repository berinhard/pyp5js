import pytest
from pathlib import Path

from pyp5js.config.fs import PYP5JS_FILES

pyp5_dir = Path(__file__).parents[3].joinpath('pyp5js')

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

    assert lib_files.transcrypt_target_sketch_template == pyp5_dir.joinpath('templates', 'target_sketch.py.template')
    assert lib_files.transcrypt_target_sketch_template.exists()

    assert lib_files.transcrypt_index_html == pyp5_dir.joinpath('templates', 'transcrypt', 'index.html')
    assert lib_files.transcrypt_index_html.exists()

    assert lib_files.pyodide_index_html == pyp5_dir.joinpath('templates', 'pyodide', 'index.html')
    assert lib_files.pyodide_index_html.exists()

    assert lib_files.p5js == pyp5_dir.joinpath('assets', 'static', 'p5', 'p5.min.js')
    assert lib_files.p5js.exists()

    assert lib_files.p5_yml == pyp5_dir.joinpath('assets', 'p5_reference.yml')
    assert lib_files.p5_yml.exists()
