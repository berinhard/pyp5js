from unittest.mock import Mock, patch

from pyp5js.compiler import Pyp5jsCompiler, compile_sketch_js
from pyp5js.fs import Pyp5jsSketchFiles


@patch('pyp5js.compiler.Pyp5jsCompiler')
def test_compile_sketch_js_service(MockedCompiler):
    files = Mock(Pyp5jsSketchFiles)
    compiler = Mock(spec=Pyp5jsCompiler)
    MockedCompiler.return_value = compiler

    compile_sketch_js(files)

    MockedCompiler.assert_called_once_with(files)
    compiler.compile_sketch_js.assert_called_once_with()
