import json
import os
from tempfile import NamedTemporaryFile

from pyp5js.config import TRANSCRYPT_INTERPRETER, PYODIDE_INTERPRETER
from pyp5js.config.sketch import SketchConfig
from pyp5js.config.fs import PYP5JS_FILES

from ..fixtures import transcrypt_json_file, pyodide_json_file, transcrypt_config, pyodide_config


def test_init_transcrypt_sketch_config_from_json(transcrypt_json_file):
    config = SketchConfig.from_json(transcrypt_json_file)
    assert config.interpreter == TRANSCRYPT_INTERPRETER


def test_init_pyodide_sketch_config_from_json(pyodide_json_file):
    config = SketchConfig.from_json(pyodide_json_file)
    assert config.interpreter == PYODIDE_INTERPRETER


def test_write_sketch_interpreter_config(transcrypt_config):
    config = transcrypt_config
    fd = NamedTemporaryFile(mode="w", delete=False)
    config.write(fd.name)
    fd.close()
    with open(fd.name) as fd:
        data = json.load(fd)

    assert data["interpreter"] == TRANSCRYPT_INTERPRETER
    os.remove(fd.name)

def test_get_transcrypt_index_template(transcrypt_config):
    template = transcrypt_config.get_index_template()
    assert PYP5JS_FILES.transcrypt_index_html == template
    assert template.exists()

def test_get_pyodide_index_template(pyodide_config):
    template = pyodide_config.get_index_template()
    assert PYP5JS_FILES.pyodide_index_html == template
    assert template.exists()

def test_get_transcrypt_target_js_template(transcrypt_config):
    template = transcrypt_config.get_target_js_template()
    assert PYP5JS_FILES.transcrypt_target_sketch_template == template
    assert template.exists()

def test_get_pyodide_target_js_template(pyodide_config):
    template = pyodide_config.get_target_js_template()
    assert PYP5JS_FILES.pyodide_target_sketch_template == template
    assert template.exists()
