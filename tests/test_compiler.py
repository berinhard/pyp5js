import shlex
import shutil
import os
from unittest import TestCase
from unittest.mock import Mock, patch
from subprocess import Popen

from pyp5js.compiler import Pyp5jsCompiler, compile_sketch_js
from pyp5js.fs import Pyp5jsSketchFiles, Pyp5jsLibFiles
from pyp5js.templates_renderer import get_target_sketch_content


@patch('pyp5js.compiler.Pyp5jsCompiler')
def test_compile_sketch_js_service(MockedCompiler):
    files = Mock(spec=Pyp5jsSketchFiles)
    compiler = Mock(spec=Pyp5jsCompiler)
    MockedCompiler.return_value = compiler

    compile_sketch_js(files)

    MockedCompiler.assert_called_once_with(files)
    compiler.compile_sketch_js.assert_called_once_with()


class Pyp5jsCompilerTests(TestCase):

    def setUp(self):
        self.pyp5js_files = Pyp5jsLibFiles()
        self.files = Pyp5jsSketchFiles('dir', 'foo', check_sketch_dir=False)
        self.compiler = Pyp5jsCompiler(self.files)

        os.mkdir(self.files.sketch_dir)
        with open(self.files.sketch_py, 'w') as fd:
            fd.write('hi')

    def tearDown(self):
        try:
            if self.files.sketch_dir.exists():
                shutil.rmtree(self.files.sketch_dir)
        except SystemExit:
            pass

    def test_transcrypt_target_dir_path(self):
        assert self.files.sketch_dir.child('__target__') == self.compiler.target_dir

    def test_command_line_string(self):
        pyp5_dir = self.pyp5js_files.install

        expected = ' '.join([str(c) for c in [
            'transcrypt', '-xp', pyp5_dir, '-b', '-m', '-n', self.files.target_sketch
        ]])

        assert expected == self.compiler.command_line

    @patch('pyp5js.compiler.subprocess.Popen')
    def test_run_compiler_as_expected(self, MockedPopen):
        proc = Mock(spec=Popen)
        MockedPopen.return_value = proc

        self.compiler.run_compiler()
        expected_command_line = shlex.split(self.compiler.command_line)

        MockedPopen.assert_called_once_with(expected_command_line)
        proc.wait.assert_called_once_with()

    def test_clean_up(self):
        os.mkdir(self.compiler.target_dir)
        with open(self.files.target_sketch, 'w') as fd:
            fd.write('some content')

        self.compiler.clean_up()

        assert not self.compiler.target_dir.exists()
        assert self.files.target_dir.exists()
        assert not self.files.target_sketch.exists()

    def test_prepare_sketch(self):
        expected_content = get_target_sketch_content(self.files.sketch_name)
        assert not self.files.target_sketch.exists()

        self.compiler.prepare()

        assert self.files.target_sketch.exists()
        with open(self.files.target_sketch, 'r') as fd:
            content = fd.read()
        assert expected_content == content
