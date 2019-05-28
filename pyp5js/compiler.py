import shlex
import shutil
import subprocess
import time
from cprint import cprint
from unipath import Path
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


PYP5_DIR = Path(__file__).parent


def compile_sketch_js(sketch_files):
    command = ' '.join([str(c) for c in [
        'transcrypt', '-xp', PYP5_DIR, '-b', '-m', '-n', sketch_files.sketch_py
    ]])

    cprint.info(f"Converting Python to P5.js...\nRunning command:\n\t {command}")

    proc = subprocess.Popen(shlex.split(command))
    proc.wait()

    __target = sketch_files.sketch_dir.child('__target__')
    if not __target.exists():
        cprint.err(f"Error with transcrypt: the {__target} directory wasn't created.", interrupt=True)

    if sketch_files.target_dir.exists():
        shutil.rmtree(sketch_files.target_dir)
    shutil.move(__target, sketch_files.target_dir)


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
