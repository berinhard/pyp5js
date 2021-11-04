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
from pyp5js import templates_renderers as renderers

from .fixtures import sketch, sketch_pyodide
from ..config.sketch import P5_JS_CDN, PYODIDE_JS_CDN


def test_get_transcrypt_index_content(sketch):
    expected_template = renderers.templates.get_template('transcrypt/index.html')
    url = sketch.TARGET_NAME + "/target_sketch.js"
    expected_content = expected_template.render({
        "sketch_name": sketch.sketch_name,
        "p5_js_url": P5_JS_CDN,
        "sketch_js_url": url,
    })

    content = renderers.get_sketch_index_content(sketch)
    assert expected_content == content
    assert sketch.sketch_name in content
    assert P5_JS_CDN in content
    assert url in content


def test_get_pyodide_index_content(sketch_pyodide):
    expected_template = renderers.templates.get_template('pyodide/index.html')
    url = sketch_pyodide.TARGET_NAME + "/target_sketch.js"
    expected_content = expected_template.render({
        "sketch_name": sketch_pyodide.sketch_name,
        "p5_js_url": P5_JS_CDN,
        "sketch_js_url": url,
        "pyodide_js_url": PYODIDE_JS_CDN,
    })

    content = renderers.get_sketch_index_content(sketch_pyodide)
    assert sketch_pyodide.sketch_name in content
    assert P5_JS_CDN in content
    assert PYODIDE_JS_CDN in content
    assert url in content
    assert expected_content == content


def test_get_transcrypt_target_sketch_content(sketch):
    with open(sketch.sketch_py, 'w') as fd:
        fd.write('content')

    expected_template = renderers.templates.get_template('transcrypt/target_sketch.py.template')
    expected_content = expected_template.render({
        'sketch_name': sketch.sketch_name,
        'sketch_content': 'content'
    })
    content = renderers.get_target_sketch_content(sketch)

    assert expected_content == content


def test_get_pyodide_target_sketch_content(sketch_pyodide):
    with open(sketch_pyodide.sketch_py, 'w') as fd:
        fd.write('content')

    expected_template = renderers.templates.get_template('pyodide/target_sketch.js.template')
    expected_content = expected_template.render({
        'sketch_name': sketch_pyodide.sketch_name,
        'sketch_content': 'content',
        'pyodide_index_url': 'https://cdn.jsdelivr.net/pyodide/v0.18.1/full/',
    })
    content = renderers.get_target_sketch_content(sketch_pyodide)

    assert expected_content == content
