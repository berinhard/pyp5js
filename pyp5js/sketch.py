import os
import re
import shutil
from collections import namedtuple

from pyp5js import config
from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.config.sketch import SketchConfig
from pyp5js.exceptions import SketchDirAlreadyExistException, InvalidName

SketchUrls = namedtuple('SketchUrls', ['p5_js_url', 'pyodide_js_url', 'sketch_js_url'])


class Sketch:
    """
    This class abstracts the sketch filesystem and configuration.
    Every path propery return pathlib.Path objects.
    """
    TARGET_NAME = 'target'
    STATIC_NAME = 'static'

    def __init__(self, sketch_name, interpreter=config.TRANSCRYPT_INTERPRETER, **cfg):
        self.sketch_name = sketch_name
        if self.config_file.exists():
            self.config = SketchConfig.from_json(self.config_file)
        else:
            self.config = SketchConfig(interpreter=interpreter, **cfg)

    def validate_name(self):
        does_not_start_with_letter_or_underscore = r'^[^a-zA-Z_]'
        contains_non_alphanumerics_except_underscore = r'[^a-zA-Z0-9_]'
        if re.match(does_not_start_with_letter_or_underscore, self.sketch_name) or \
                re.search(contains_non_alphanumerics_except_underscore, self.sketch_name):
            raise InvalidName(self)

    def create_sketch_dir(self):
        """
        Create sketch required directories
        """
        self.validate_name()

        if self.sketch_dir.exists():
            raise SketchDirAlreadyExistException(self)

        os.makedirs(self.sketch_dir)
        self.static_dir.mkdir()
        self.target_dir.mkdir()
        self.config.write(self.config_file)

    def copy_initial_files(self, use_cdn=True):
        """
        Copy requlred template files to the sketch directory
        """
        if not use_cdn:
            self.config.p5_js_url = "/static/p5.js"
            if self.config.is_pyodide:
                self.config.pyodide_js_url = "/static/pyodide/pyodide_v0.18.1.js"

        templates_files = [
            (self.config.get_base_sketch_template(), self.sketch_py),
        ]
        if not use_cdn:
            templates_files.append((PYP5JS_FILES.p5js, self.p5js))
            if self.config.is_pyodide:
                shutil.copytree(PYP5JS_FILES.pyodide_js_dir, self.static_dir / "pyodide")
                # delete packages.json that's not necessary
                (self.static_dir / "pyodide" / "packages.json").unlink()

        for src, dest in templates_files:
            shutil.copyfile(src, dest)

    @property
    def sketch_exists(self):
        return self.sketch_py.exists()

    @property
    def sketch_content(self):
        if not self.sketch_py.exists():
            return ""
        with self.sketch_py.open(encoding="utf-8") as fd:
            return fd.read()

    @property
    def has_all_files(self):
        return all([
            self.sketch_exists,
            self.index_html.exists()
        ])

    @property
    def sketch_dir(self):
        return config.SKETCHBOOK_DIR.joinpath(f'{self.sketch_name}')

    @property
    def static_dir(self):
        return self.sketch_dir.joinpath(self.STATIC_NAME)

    @property
    def index_html(self):
        return self.sketch_dir.joinpath('index.html')

    @property
    def p5js(self):
        return self.static_dir.joinpath('p5.js')

    @property
    def target_sketch(self):
        # TODO: There is a potential major refactoring here that's to create
        # base sketch classes and specific implementations. One for a TranscryptSketch
        # and another one for a PyodideSketch. I think the config
        # attribute strategy can escalate complexity quickly and it
        # was a bad idea, but have been working so far...
        # bonus: opens path to a BrythonSketch ;]
        if self.config.is_transcrypt:
            return self.sketch_dir.joinpath("target_sketch.py")
        else:
            return self.target_dir.joinpath("target_sketch.js")

    @property
    def sketch_py(self):
        return self.sketch_dir.joinpath(f'{self.sketch_name}.py')

    @property
    def config_file(self):
        return self.sketch_dir.joinpath('.properties.json')

    @property
    def target_dir(self):
        return self.sketch_dir.joinpath(self.TARGET_NAME)

    def __eq__(self, other):
        return self.sketch_name == other.sketch_name

    @property
    def urls(self):
        return SketchUrls(
            p5_js_url=self.config.p5_js_url,
            pyodide_js_url=self.config.pyodide_js_url,
            sketch_js_url=f"{self.TARGET_NAME}/target_sketch.js",
        )

    def get_target_sketch_context(self):
        """
        This method is used by the template renderers to get the context to be used
        to render final target/target_sketch.js file.
        """
        context = {
            "sketch_name": self.sketch_name,
            "sketch_content": self.sketch_content,
        }
        if self.config.is_pyodide:
            index = "/".join(self.config.pyodide_js_url.split("/")[:-1]) + "/"
            context.update({'pyodide_index_url': index})
        return context

