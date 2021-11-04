"""
pyp5js
Copyright (C) 2019-2021 The pyp5js Contributors

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
"""
Test file to guarantee the Python code that'll be translated to JS
"""
from pyaml import yaml
import pytest

from pyp5js.config.fs import PYP5JS_FILES


@pytest.fixture
def pyp5js():
    with PYP5JS_FILES.pytop5js.open('r') as fd:
        return fd.read()


@pytest.fixture
def p5_reference():
    with PYP5JS_FILES.p5_yml.open('r') as fd:
        return yaml.safe_load(fd)


special_methods = ['pop', 'clear', 'get']


def test_all_regular_p5_methods_are_defined(pyp5js, p5_reference):
    for method in [m for m in p5_reference['p5']['methods'] if m not in special_methods]:
        if method == 'loadImage':
            continue
        assert f"def {method}(*args):" in pyp5js
        assert f"    return _P5_INSTANCE.{method}(*args)" in pyp5js

    assert f"def loadImage(*args):" in pyp5js
    assert f"    imageObj = _P5_INSTANCE.loadImage(*args)" in pyp5js
    assert f"    return image_proxy(imageObj)" in pyp5js

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
