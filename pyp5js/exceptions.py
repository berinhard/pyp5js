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
class PythonSketchDoesNotExist(Exception):

    def __init__(self, sketch):
        sketch_py = sketch.sketch_py.resolve()
        message = f"Sketch file {sketch_py} does not exist"
        super().__init__(message)


class SketchDirAlreadyExistException(Exception):

    def __init__(self, sketch):
        sketch_dir = sketch.sketch_dir.resolve()
        message = f'The directory {sketch_dir} already exists.'
        super().__init__(message)

class InvalidName(Exception):

    def __init__(self, sketch):
        sketch_name = sketch.sketch_name
        message = f'The name {sketch_name} must start with a letter or an underscore and ' + \
            'contain alphanumeric and underscore characters only.'
        super().__init__(message)
