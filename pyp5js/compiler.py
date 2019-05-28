import shlex
import shutil
import subprocess
from cprint import cprint
from unipath import Path

from pyp5js.fs import Pyp5jsLibFiles



class Pyp5jsCompiler:

    def __init__(self, sketch_files):
        self.pyp5js_files = Pyp5jsLibFiles()
        self.sketch_files = sketch_files

    def compile_sketch_js(self):
        self.run_compiler()
        self.clean_up()

    @property
    def target_dir(self):
        """
        Path to directory with the js and assets files
        """
        return self.sketch_files.sketch_dir.child('__target__')

    @property
    def command_line(self):
        """
        Builds transcrypt command line with the required parameters and flags
        """
        pyp5_dir = self.pyp5js_files.install
        return ' '.join([str(c) for c in [
            'transcrypt', '-xp', pyp5_dir, '-b', '-m', '-n', self.sketch_files.sketch_py
        ]])

    def run_compiler(self):
        """
        Execute transcrypt command to generate the JS files
        """
        command = self.command_line
        cprint.info(f"Converting Python to P5.js...\nRunning command:\n\t {command}")

        proc = subprocess.Popen(shlex.split(command))
        proc.wait()

    def clean_up(self):
        """
        Rename the assets dir from __target__ to target

        This is required because github pages can't deal with assets under a __target__ directory
        """
        if self.sketch_files.target_dir.exists():
            shutil.rmtree(self.sketch_files.target_dir)
        shutil.move(self.target_dir, self.sketch_files.target_dir)


def compile_sketch_js(sketch_files):
    compiler = Pyp5jsCompiler(sketch_files)
    compiler.compile_sketch_js()
