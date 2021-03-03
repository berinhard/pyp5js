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
