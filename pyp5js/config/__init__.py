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
from . import sketch
from .sketch import TRANSCRYPT_INTERPRETER, PYODIDE_INTERPRETER
from decouple import config
from pathlib import Path

SKETCHBOOK_DIR = config("SKETCHBOOK_DIR", cast=Path, default=Path.home().joinpath('sketchbook-pyp5js'))

if not SKETCHBOOK_DIR.exists():
    SKETCHBOOK_DIR.mkdir()

AVAILABLE_INTERPRETERS = [TRANSCRYPT_INTERPRETER, PYODIDE_INTERPRETER]
