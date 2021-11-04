"""
pyp5js
Copyright (C) 2019-2021 The pyp5js Contributors

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
from queue import Queue
from unittest import TestCase
from unittest.mock import Mock, patch

from pyp5js.monitor import TranscryptSketchEventHandler
from pyp5js.sketch import Sketch


class TranscryptSketchEventHandlerTests(TestCase):

    def setUp(self):
        self.files = Mock(spec=Sketch)
        self.queue = Mock(spec=Queue)
        self.observer = Mock(event_queue=self.queue)
        self.handler = TranscryptSketchEventHandler(sketch=self.files, observer=self.observer)

    def test_handler_config(self):
        assert self.files == self.handler.sketch
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
