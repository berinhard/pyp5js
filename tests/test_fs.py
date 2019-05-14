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

