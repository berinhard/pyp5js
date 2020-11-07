import json
import os
from pytest import fixture
from pathlib import Path
from tempfile import NamedTemporaryFile

from pyp5js.config import TRANSCRYPT_INTERPRETER, PYODIDE_INTERPRETER
from pyp5js.config.sketch import SketchConfig


@fixture
def transcrypt_json_file():
    with NamedTemporaryFile(mode='w') as fd:
        data = {"interpreter": "transcrypt"}
        json.dump(data, fd)
        fd.seek(0)
        yield fd


@fixture
def pyodide_json_file():
    with NamedTemporaryFile(mode='w') as fd:
        data = {"interpreter": "pyodide"}
        json.dump(data, fd)
        fd.seek(0)
        yield fd


def test_init_transcrypt_sketch_config_from_json(transcrypt_json_file):
    config = SketchConfig.from_json(transcrypt_json_file.name)
    assert config.interpreter == TRANSCRYPT_INTERPRETER


def test_init_pyodide_sketch_config_from_json(pyodide_json_file):
    config = SketchConfig.from_json(pyodide_json_file.name)
    assert config.interpreter == PYODIDE_INTERPRETER


def test_write_sketch_interpreter_config():
    config = SketchConfig(interpreter=TRANSCRYPT_INTERPRETER)
    fd = NamedTemporaryFile(mode="w", delete=False)
    config.write(fd.name)
    fd.close()
    with open(fd.name) as fd:
        data = json.load(fd)

    assert data["interpreter"] == TRANSCRYPT_INTERPRETER
    os.remove(fd.name)
