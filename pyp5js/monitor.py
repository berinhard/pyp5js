import time
from cprint import cprint
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from pyp5js.compiler import compile_sketch_js



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
        cprint.info(f"New change in {event.src_path}")

        compile_sketch_js(self.sketch_files)

        index_file = self.sketch_files.index_html
        cprint.ok(f"Your sketch is ready and available at {index_file}")
