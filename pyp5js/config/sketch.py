class SketchConfig:

    def __init__(self, interpreter):
        self.interpreter = interpreter

    def get_index_template(self):
        from pyp5js.fs import LibFiles
        pyp5js_files = LibFiles()
        return pyp5js_files.index_html
