"""
pyp5js
Copyright (C) 2019-2021 Bernardo Fontes

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
import pytest
from pathlib import Path

from pyp5js.config.fs import PYP5JS_FILES

pyp5_dir = Path(__file__).parents[3].joinpath('pyp5js')

from ..fixtures import lib_files

def test_dir_properties(lib_files):
    assert pyp5_dir.exists()

    assert lib_files.templates_dir == pyp5_dir.joinpath('templates')
    assert lib_files.templates_dir.exists()
    assert lib_files.static_dir == pyp5_dir.joinpath('http', 'static')
    assert lib_files.static_dir.exists()


def test_files_properties(lib_files):
    assert pyp5_dir.exists()

    ##### GENERAL PURPOSE
    assert lib_files.pytop5js == pyp5_dir.joinpath('templates', 'transcrypt', 'pyp5js.py')
    assert lib_files.pytop5js.exists()

    assert lib_files.p5js == pyp5_dir.joinpath('http', 'static', 'js', 'p5', 'p5.min.js')
    assert lib_files.p5js.exists()

    assert lib_files.p5_yml == pyp5_dir.joinpath('http', 'static', 'p5_reference.yml')
    assert lib_files.p5_yml.exists()


def test_transcrypt_specifict_properties(lib_files):
    assert lib_files.transcrypt_target_sketch_template == pyp5_dir.joinpath('templates', 'transcrypt', 'target_sketch.py.template')
    assert lib_files.transcrypt_target_sketch_template.exists()

    assert lib_files.transcrypt_index_html == pyp5_dir.joinpath('templates', 'transcrypt', 'index.html')
    assert lib_files.transcrypt_index_html.exists()

    assert lib_files.transcrypt_base_sketch_template == pyp5_dir.joinpath('templates', 'transcrypt', 'base_sketch.py.template')
    assert lib_files.transcrypt_base_sketch_template.exists()


def test_pyodide_specifict_properties(lib_files):
    assert lib_files.pyodide_target_sketch_template == pyp5_dir.joinpath('templates', 'pyodide', 'target_sketch.js.template')
    assert lib_files.pyodide_target_sketch_template.exists()

    assert lib_files.pyodide_index_html == pyp5_dir.joinpath('templates', 'pyodide', 'index.html')
    assert lib_files.pyodide_index_html.exists()

    assert lib_files.pyodide_base_sketch_template == pyp5_dir.joinpath('templates', 'pyodide', 'base_sketch.py.template')
    assert lib_files.pyodide_base_sketch_template.exists()
