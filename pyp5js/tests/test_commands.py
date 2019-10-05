import pytest
import shutil
from unittest import TestCase
from unittest.mock import Mock, patch

from pyp5js import commands
from pyp5js.fs import SketchFiles


@patch('pyp5js.commands.SketchFiles')
def test_transcrypt_sketch(MockedFiles):
    files = Mock(spec=SketchFiles)
    files.check_sketch_exists.return_value = True
    MockedFiles.return_value = files

    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        output = commands.transcrypt_sketch(sketch_name='foo', sketch_dir='bar')

        assert output == files.index_html
        MockedFiles.assert_called_once_with('bar', 'foo')
        compiler.assert_called_once_with(files)


@patch('pyp5js.commands.SketchFiles')
def test_transcrypt_sketch_error_if_sketch_does_not_exist(MockedFiles):
    files = Mock(spec=SketchFiles)
    files.check_sketch_exists.return_value = False
    MockedFiles.return_value = files

    with patch('pyp5js.commands.compile_sketch_js') as compiler:
        with pytest.raises(SystemExit):
            commands.transcrypt_sketch(sketch_name='foo', sketch_dir='bar')


@patch('pyp5js.commands.SketchFiles')
def test_monitor_sketch(MockedFiles):
    files = Mock(spec=SketchFiles)
    files.check_sketch_exists.return_value = True
    MockedFiles.return_value = files

    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        commands.monitor_sketch(sketch_name='foo', sketch_dir='bar')

        MockedFiles.assert_called_once_with('bar', 'foo')
        monitor.assert_called_once_with(files)


@patch('pyp5js.commands.SketchFiles')
def test_monitor_sketch_error_if_sketch_does_not_exist(MockedFiles):
    files = Mock(spec=SketchFiles)
    files.check_sketch_exists.return_value = False
    MockedFiles.return_value = files

    with patch('pyp5js.commands.monitor_sketch_service') as monitor:
        with pytest.raises(SystemExit):
            commands.monitor_sketch(sketch_name='foo', sketch_dir='bar')


class TestNewSketchCommand(TestCase):

    def setUp(self):
        self.dirname = 'test_dir'
        self.sketch_name = 'foo'
        self.sketch_files = SketchFiles(self.dirname, self.sketch_name, check_sketch_dir=False)

    def tearDown(self):
        try:
            if self.sketch_files.sketch_dir.exists():
                shutil.rmtree(self.sketch_files.sketch_dir)
        except SystemExit:
            pass

    def test_create_new_sketch_with_all_required_files(self):
        commands.new_sketch(self.sketch_name, self.dirname)

        assert self.sketch_files.index_html.exists()
        assert self.sketch_files.sketch_py.exists()
        assert self.sketch_files.p5js.exists()
        assert self.sketch_files.p5_dom_js.exists()

    def test_raise_exception_if_dir_already_exist(self):
        self.sketch_files.sketch_dir.mkdir()

        with pytest.raises(SystemExit):
            commands.new_sketch(self.sketch_name, self.dirname)
