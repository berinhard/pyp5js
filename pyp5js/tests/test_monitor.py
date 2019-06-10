from queue import Queue
from unittest import TestCase
from unittest.mock import Mock, patch

from pyp5js.monitor import TranscryptSketchEventHandler
from pyp5js.fs import Pyp5jsSketchFiles


class TranscryptSketchEventHandlerTests(TestCase):

    def setUp(self):
        self.files = Mock(spec=Pyp5jsSketchFiles)
        self.queue = Mock(spec=Queue)
        self.observer = Mock(event_queue=self.queue)
        self.handler = TranscryptSketchEventHandler(sketch_files=self.files, observer=self.observer)

    def test_handler_config(self):
        assert self.files == self.handler.sketch_files
        assert ['*.py'] == self.handler.patterns
        assert self.observer == self.handler.observer

    @patch('pyp5js.monitor.compile_sketch_js')
    def test_on_modified(self, mocked_compiler):
        self.queue.qsize.return_value = 0
        event = Mock()

        self.handler.on_modified(event)

        mocked_compiler.assert_called_once_with(self.files)
        self.queue.qsize.assert_called_once_with()

    @patch('pyp5js.monitor.compile_sketch_js')
    def test_on_modified_cleans_event_queue_from_changes_introduced_by_pyp5(self, mocked_compiler):
        self.queue.qsize.side_effect = sorted(range(11), reverse=True)
        event = Mock()

        self.handler.on_modified(event)

        mocked_compiler.assert_called_once_with(self.files)
        assert self.queue.qsize.call_count == 11
        assert 10 == self.queue.get.call_count
