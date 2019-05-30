from unittest import TestCase
from unittest.mock import Mock, patch

from pyp5js.compiler import TranscryptSketchEventHandler
from pyp5js.fs import Pyp5jsSketchFiles


class TranscryptSketchEventHandlerTests(TestCase):

    def setUp(self):
        self.files = Mock(spec=Pyp5jsSketchFiles)
        self.handler = TranscryptSketchEventHandler(sketch_files=self.files)

    def test_handler_config(self):
        assert self.files == self.handler.sketch_files
        assert ['*.py'] == self.handler.patterns
        assert self.handler._last_event is None

    @patch('pyp5js.compiler.compile_sketch_js')
    def test_on_modified(self, mocked_compiler):
        event = Mock()

        self.handler.on_modified(event)

        mocked_compiler.assert_called_once_with(self.files)
