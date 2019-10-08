from decouple import config
from pathlib import Path

SKETCHBOOK_DIR = config("SKETCHBOOK_DIR", cast=Path, default=Path.home().joinpath('sketchbook-pyp5js'))

if not SKETCHBOOK_DIR.exists():
    SKETCHBOOK_DIR.mkdir()
