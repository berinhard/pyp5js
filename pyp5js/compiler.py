import shlex
import shutil
import subprocess
import time
from cprint import cprint
from unipath import Path
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

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


def monitor_sketch(sketch_files):
    event_handler = TranscryptSketchEventHandler(sketch_files=sketch_files)
    observer = Observer()

    observer.schedule(event_handler, sketch_files.sketch_dir)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt as e:
        observer.stop()
        raise e
    observer.join()


class TranscryptSketchEventHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def __init__(self, *args, **kwargs):
        self.sketch_files = kwargs.pop('sketch_files')
        self._last_event = None
        super().__init__(*args, **kwargs)

    def on_modified(self, event):
        event_id = id(event)
        if event_id == self._last_event:
            return

        cprint.info(f"New change in {event.src_path}")

        compile_sketch_js(self.sketch_files)
        self._last_event = event_id

        index_file = self.sketch_files.index_html
        cprint.ok(f"Your sketch is ready and available at {index_file}")
