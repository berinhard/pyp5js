import os
import shutil
from pathlib import Path

from pyp5js import commands
from pyp5js.sketch import Sketch
from pyp5js.config import SKETCHBOOK_DIR, PYODIDE_INTERPRETER, TRANSCRYPT_INTERPRETER
from pyp5js.http.web_app import app as web_app
from flask_testing import TestCase


class Pyp5jsWebTestCase(TestCase):
    render_templates = False

    def create_app(self):
        app = web_app
        app.config['TESTING'] = True
        return app

    def setUp(self):
        if not SKETCHBOOK_DIR.exists():
            SKETCHBOOK_DIR.mkdir()

    def tearDown(self):
        if SKETCHBOOK_DIR.exists():
            shutil.rmtree(SKETCHBOOK_DIR)

    def create_sketch(self, name, interpreter=PYODIDE_INTERPRETER):
        return commands.new_sketch(name, interpreter=interpreter)

    def create_sketch_with_static_files(self, name, use_cdn=True):
        sketch = commands.new_sketch(name, use_cdn=use_cdn)
        commands.compile_sketch(name)
        return sketch.sketch_dir

    def create_file(self, file_name, content=''):
        mode = 'w'
        if isinstance(content, bytes):
            mode += 'b'
        with (SKETCHBOOK_DIR.joinpath(file_name).resolve()).open(mode) as fd:
            fd.write(content)


class IndexViewTests(Pyp5jsWebTestCase):
    route = '/'

    def test_get_home_renders_index_template_and_context_with_empty(self):
        self.client.get(self.route)
        self.assert_template_used('index.html')
        self.assert_context('sketches', [])

    def test_get_home_renders_index_template_and_context_all_files(self):
        self.create_sketch('first_sketch')
        self.create_sketch('second_sketch')
        self.client.get(self.route)
        self.assert_template_used('index.html')
        assert len(self.get_context_variable('sketches')) == 2
        assert dict(name='first_sketch', url='/sketch/first_sketch/') in self.get_context_variable('sketches')
        assert dict(name='second_sketch', url='/sketch/second_sketch/') in self.get_context_variable('sketches')


class NewSketchViewTests(Pyp5jsWebTestCase):
    route = '/new-sketch/'

    def test_get_new_sketch_renders_new_sketch_form_template(self):
        self.client.get(self.route)
        self.assert_template_used('new_sketch_form.html')
        self.assert_context('sketches_dir', SKETCHBOOK_DIR.resolve())
        self.assert_context('pyodide_interpreter', PYODIDE_INTERPRETER)
        self.assert_context('transcrypt_interpreter', TRANSCRYPT_INTERPRETER)

    def test_post_without_sketch_name_should_render_form_with_error(self):
        self.client.post(self.route, data={'sketch_name': ''})
        self.assert_template_used('new_sketch_form.html')
        self.assert_context('error', 'You have to input a sketch name to proceed.')

    def test_post_with_existing_sketch_name_should_render_form_with_error(self):
        self.create_sketch('my_existing_sketch')
        self.client.post(self.route, data={'sketch_name': 'my_existing_sketch'})
        self.assert_template_used('new_sketch_form.html')
        sketch_name = os.path.join('tests-sketchbook', 'my_existing_sketch')
        self.assert_context('error', f'The sketch {sketch_name} already exists.')

    def test_post_with_sketch_name_should_render_success_form(self):
        self.client.post(self.route, data={'sketch_name': 'a_name'})
        self.assert_template_used('new_sketch_success.html')
        assert Sketch('a_name').config.is_pyodide

    def test_can_specify_the_compiler_for_sketch(self):
        data = {'sketch_name': 'a_name', 'interpreter': 'transcrypt'}
        self.client.post(self.route, data=data)
        self.assert_template_used('new_sketch_success.html')
        assert Sketch('a_name').config.is_transcrypt

    def test_error_if_invalid_p5js_interpreter(self):
        data = {'sketch_name': 'a_name', 'interpreter': 'foo'}
        self.client.post(self.route, data=data)
        self.assert_template_used('new_sketch_form.html')
        self.assert_context('error', f'The interpreter foo is not valid. Please, select a valid one.')


class SketchViewTests(Pyp5jsWebTestCase):
    route = '/sketch/'

    def test_get_sketch_does_not_exist(self):
        response = self.client.get(self.route + 'sketch_does_not_exist/')
        self.assert_404(response)

    def test_get_sketch_exists(self):
        sketch = self.create_sketch('sketch_exists')
        py_code = sketch.sketch_py.read_text()

        response = self.client.get(self.route + 'sketch_exists/')
        self.assert_200(response)
        self.assert_template_used('view_sketch.html')
        self.assert_context('p5_js_url', sketch.urls.p5_js_url)
        self.assert_context('sketch_js_url', sketch.urls.sketch_js_url)
        self.assert_context('sketch_name', sketch.sketch_name)
        self.assert_context('py_code', py_code)
        self.assert_context('js_as_module', False)
        self.assert_context('live_run', True)

    def test_get_transcrypt_sketch(self):
        sketch = self.create_sketch('sketch_exists', interpreter=TRANSCRYPT_INTERPRETER)
        response = self.client.get(self.route + 'sketch_exists/')
        self.assert_200(response)
        self.assert_context('js_as_module', True)
        self.assert_context('live_run', False)


    def test_get_static_file_does_not_exist(self):
        response = self.client.get(self.route + 'foo/static/file.js')
        self.assert_404(response)

    def test_get_static_javascript_file(self):
        self.create_sketch_with_static_files('sketch_with_static_js', use_cdn=False)
        response = self.client.get(self.route + 'sketch_with_static_js/static/p5.js')
        self.assert_200(response)
        self.assertEqual(response.headers['Content-Type'], 'application/javascript; charset=utf-8')

    def test_get_static_javascript_file_upper_case(self):
        js_code = 'alert("hi!");'
        self.create_sketch_with_static_files('sketch_with_static_js')
        self.create_file(f'sketch_with_static_js/static/custom.JS', js_code)

        response = self.client.get(self.route + 'sketch_with_static_js/static/custom.JS')

        self.assert_200(response)
        self.assertEqual(response.headers['Content-Type'], 'application/javascript; charset=utf-8')
        self.assertEqual(js_code.encode(), response.get_data())

    def test_get_static_file(self):
        self.create_sketch('my_sketch_file')
        self.create_file('my_sketch_file/static/style.css', 'css file content')
        response = self.client.get(self.route + 'my_sketch_file/static/style.css')
        self.assert_200(response)
        self.assertEqual(response.data, b"css file content")

    def test_get_image_files(self):
        img_content = b'image content'
        self.create_sketch('my_sketch_file')
        supported_extensions = ['.gif', '.jpeg', '.png', '.PNG', '.JPEG', '.GIF']

        for suffix in supported_extensions:
            img_name = f"image{suffix}"
            self.create_file(f'my_sketch_file/{img_name}', img_content)

            response = self.client.get(self.route + f'my_sketch_file/{img_name}')

            self.assert_200(response)
            self.assertEqual(f'image/{suffix[1:].lower()}', response.headers['Content-Type'])
            self.assertEqual(response.get_data(), img_content)

    def test_regression_test_with_real_png_image(self):
        img_name = 'alien.png'
        alien_img = Path(__file__).resolve().parent / 'assets' / img_name
        assert alien_img.exists()

        sketch = self.create_sketch('my_sketch_file')
        shutil.copyfile(alien_img, sketch.sketch_dir / img_name)

        response = self.client.get(self.route + f'my_sketch_file/{img_name}')

        self.assert_200(response)
        self.assertEqual(f'image/png', response.headers['Content-Type'])
        with alien_img.open(mode='rb') as fd:
            self.assertEqual(response.get_data(), fd.read())

    def test_403_if_invalid_path(self):
        self.create_sketch('my_sketch_file')
        self.create_file('my_sketch_file/static/style.css', 'css file content')
        response = self.client.get(self.route + 'my_sketch_file/../static/style.css')
        self.assert_403(response)


class UpdateSketchViewTests(Pyp5jsWebTestCase):
    route = '/sketch/'
    test_code = """
from pyp5js import *

def setup():
    createCanvas(300, 300)

def draw():
    rect(10, 10, 200, 100)
    """.strip()

    def test_update_sketch_on_post(self):
        sketch = self.create_sketch('sketch_exists')

        url = self.route + 'sketch_exists/'
        response = self.client.post(url, data={'py_code': self.test_code})

        assert self.test_code == sketch.sketch_py.read_text()

    def test_python_code_is_required(self):
        sketch = self.create_sketch('sketch_exists')
        old_content = sketch.sketch_py.read_text()

        url = self.route + 'sketch_exists/'
        response = self.client.post(url, data={'py_code': ''})

        self.assert_template_used('view_sketch.html')
        self.assert_context('error', 'You have to input the Python code.')
        assert old_content == sketch.sketch_py.read_text()

    def test_check_python_syntax_before_updating(self):
        test_code = self.test_code.replace('300)', '300')
        sketch = self.create_sketch('sketch_exists')
        old_content = sketch.sketch_py.read_text()

        url = self.route + 'sketch_exists/'
        response = self.client.post(url, data={'py_code': test_code})

        self.assert_template_used('view_sketch.html')
        self.assert_context('error', 'SyntaxError: invalid syntax (sketch_exists.py, line 6)')
        assert old_content == sketch.sketch_py.read_text()

    def test_check_for_setup_function_before_updating(self):
        test_code = """
from pyp5js import *

def draw():
    rect(10, 10, 200, 100)
    """.strip()
        sketch = self.create_sketch('sketch_exists')
        old_content = sketch.sketch_py.read_text()

        url = self.route + 'sketch_exists/'
        response = self.client.post(url, data={'py_code': test_code})

        self.assert_template_used('view_sketch.html')
        self.assert_context('error', 'You have to define a setup function.')
        assert old_content == sketch.sketch_py.read_text()

    def test_check_for_draw_function_before_updating(self):
        test_code = """
from pyp5js import *

def setup():
    createCanvas(300, 300)
    """.strip()
        sketch = self.create_sketch('sketch_exists')
        old_content = sketch.sketch_py.read_text()

        url = self.route + 'sketch_exists/'
        response = self.client.post(url, data={'py_code': test_code})

        self.assert_template_used('view_sketch.html')
        self.assert_context('error', 'You have to define a draw function.')
        assert old_content == sketch.sketch_py.read_text()
