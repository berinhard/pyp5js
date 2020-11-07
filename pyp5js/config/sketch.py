import json


class SketchConfig:

    @classmethod
    def from_json(cls, json_file_path):
        with open(json_file_path) as fd:
            config_data = json.load(fd)
            return cls(**config_data)

    def __init__(self, interpreter):
        self.interpreter = interpreter

    def get_index_template(self):
        from pyp5js.fs import LibFiles
        pyp5js_files = LibFiles()
        return pyp5js_files.index_html

    def write(self, fname):
        with open(fname, "w") as fd:
            data = {"interpreter": self.interpreter}
            json.dump(data, fd)
