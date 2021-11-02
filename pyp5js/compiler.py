import shutil
import subprocess
from cprint import cprint

from pyp5js.config.fs import PYP5JS_FILES
from pyp5js.templates_renderers import get_target_sketch_content


class BasePyp5jsCompiler:

    def __init__(self, sketch, force_local=False):
        self.sketch = sketch
        self.force_local = force_local

    @property
    def target_dir(self):
        """
        Path to directory with the js and assets files
        """
        return self.sketch.sketch_dir.joinpath('__target__')

    def compile_sketch_js(self):
        self.prepare()
        self.run_compiler()
        self.clean_up()

    def run_compiler(self):
        pass

    def clean_up(self):
        pass

    def prepare(self):
        """
        Creates target_sketch.py to import the sketch's functions
        """
        content = get_target_sketch_content(self.sketch)

        with self.sketch.target_sketch.open('w', encoding="utf-8") as fd:
            fd.write(content)

        cprint.info(f"{self.sketch.target_sketch.resolve()} updated with sketch code")


class TranscryptCompiler(BasePyp5jsCompiler):

    @property
    def command_line(self):
        """
        Builds transcrypt command line with the required parameters and flags
        """
        pyp5_dir = PYP5JS_FILES.transcrypt_conf_dir
        target = self.sketch.target_sketch
        return ' '.join([str(c) for c in [
            'transcrypt', '-xp', f'"{pyp5_dir}"', '-k', '-ks', '-b', '-m', '-n', f'"{target}"'
        ]])

    def run_compiler(self):
        """
        Execute transcrypt command to generate the JS files
        """
        command = self.command_line
        cprint.info(
            f"Converting Python to P5.js...\nRunning command:\n\t {command}")

        subprocess.call(command, shell=True)

    def clean_up(self):
        """
        Rename the assets dir from __target__ to target and delete target_sketch.py

        This is required because github pages can't deal with assets under a __target__ directory
        """
        if self.sketch.target_dir.exists():
            shutil.rmtree(self.sketch.target_dir)
        # mv __target__ target
        shutil.move(self.target_dir, self.sketch.target_dir)

        if self.sketch.target_sketch.exists():

            self.sketch.target_sketch.unlink()


class PyodideCompiler(BasePyp5jsCompiler):

    def prepare(self):
        # this is a hack for web editor to always run using local JS files
        if self.force_local:
            self.sketch.config.pyodide_js_url = "/static/js/pyodide/pyodide_v0.18.1.js"
        return super().prepare()


def compile_sketch_js(sketch, force_local=False):
    if sketch.config.is_transcrypt:
        compiler = TranscryptCompiler(sketch, force_local=force_local)
    else:
        compiler = PyodideCompiler(sketch, force_local=force_local)
    compiler.compile_sketch_js()
