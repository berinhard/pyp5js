"""
pyp5js
Copyright (C) 2019-2021 Bernardo Fontes

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import time
from cprint import cprint
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from pyp5js.compiler import compile_sketch_js


def monitor_sketch(sketch):
    observer = Observer()

    event_handler = TranscryptSketchEventHandler(sketch=sketch, observer=observer)

    observer.schedule(event_handler, str(sketch.sketch_dir.resolve()))
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
        self.sketch = kwargs.pop('sketch')
        self.observer = kwargs.pop('observer')
        self._last_event = None
        super().__init__(*args, **kwargs)

    def on_modified(self, event):
        cprint.info(f"New change in {event.src_path}")

        # monkey patch on the observer handlers to avoid recursion
        handlers_config = self.observer._handlers.copy()
        handlers_copy = {}

        compile_sketch_js(self.sketch)

        queue = self.observer.event_queue
        while queue.qsize():
            queue.get()

        index_file = self.sketch.index_html
        cprint.ok(f"Your sketch is ready and available at file://{index_file.absolute()}")
