import pytest
from unittest.mock import Mock, patch

from pyp5js import commands
from pyp5js.fs import Pyp5jsSketchFiles, Pyp5jsLibFiles


@patch('pyp5js.commands.Pyp5jsSketchFiles')
def test_transcrypt_sketch(MockedFiles):
    files = Mock(spec=Pyp5jsSketchFiles)
    files.check_sketch_exists.return_value = True
    MockedFiles.return_value = files

    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        output = commands.transcrypt_sketch(sketch_name='foo', sketch_dir='bar')

        assert output == files.index_html
        MockedFiles.assert_called_once_with('bar', 'foo')
        compiler.assert_called_once_with(files)


@patch('pyp5js.commands.Pyp5jsSketchFiles')
def test_transcrypt_sketch_error_if_sketch_does_not_exist(MockedFiles):
    files = Mock(spec=Pyp5jsSketchFiles)
    files.check_sketch_exists.return_value = False
    MockedFiles.return_value = files

    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        with pytest.raises(SystemExit):
            commands.transcrypt_sketch(sketch_name='foo', sketch_dir='bar')


@patch('pyp5js.commands.Pyp5jsSketchFiles')
def test_monitor_sketch(MockedFiles):
    files = Mock(spec=Pyp5jsSketchFiles)
    files.check_sketch_exists.return_value = True
    MockedFiles.return_value = files

    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        commands.monitor_sketch(sketch_name='foo', sketch_dir='bar')

        MockedFiles.assert_called_once_with('bar', 'foo')
        monitor.assert_called_once_with(files)


@patch('pyp5js.commands.Pyp5jsSketchFiles')
def test_monitor_sketch_error_if_sketch_does_not_exist(MockedFiles):
    files = Mock(spec=Pyp5jsSketchFiles)
    files.check_sketch_exists.return_value = False
    MockedFiles.return_value = files

    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        with pytest.raises(SystemExit):
            commands.monitor_sketch(sketch_name='foo', sketch_dir='bar')
