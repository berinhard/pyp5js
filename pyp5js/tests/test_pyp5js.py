"""
Test file to guarantee the Python code that'll be translated to JS
"""
from pyaml import yaml
import pytest

from pyp5js.fs import LibFiles

LIB_FILES = LibFiles()


@pytest.fixture
def pyp5js():
    with LIB_FILES.pytop5js.open('r') as fd:
        return fd.read()


@pytest.fixture
def p5_reference():
    with LIB_FILES.p5_yml.open('r') as fd:
        return yaml.load(fd)


special_methods = ['pop']


def test_all_regular_p5_methods_are_defined(pyp5js, p5_reference):
    for method in [m for m in p5_reference['p5']['methods'] if m not in special_methods]:
        assert f"def {method}(*args):" in pyp5js
        assert f"    return _P5_INSTANCE.{method}(*args)" in pyp5js

    for method in [m for m in p5_reference['dom']['methods'] if m not in special_methods]:
        assert f"def {method}(*args):" in pyp5js
        assert f"    return _P5_INSTANCE.{method}(*args)" in pyp5js


def test_all_special_methods(pyp5js, p5_reference):
    for method in special_methods:
        assert f"def {method}(*args):" in pyp5js
        assert f"    __pragma__('noalias', '{method}')" in pyp5js
        assert f"    p5_{method} = _P5_INSTANCE.{method}(*args)" in pyp5js
        assert f"    __pragma__('alias', '{method}', 'py_{method}')" in pyp5js
        assert f"    return p5_{method}" in pyp5js
