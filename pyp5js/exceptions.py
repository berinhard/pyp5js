class PythonSketchDoesNotExist(Exception):

    def __init__(self, sketch_py):
        message = f"Sketch file {sketch_py} does not exist"
        super().__init__(message)


class SketchDirAlreadyExistException(Exception):

    def __init__(self, sketch_dir):
        message = f'The directory {sketch_dir} already exists.'
        super().__init__(message)
