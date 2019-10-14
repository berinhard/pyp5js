import os
import shutil
from pyp5js.config import SKETCHBOOK_DIR
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

    def create_sketch(self, name):
        sketch_dir = SKETCHBOOK_DIR.joinpath(name)
        os.makedirs(sketch_dir)
        target_file = sketch_dir.joinpath(f'{name}.py')
        index_file = sketch_dir.joinpath('index.html')
        self.create_file(target_file)
        self.create_file(index_file, 'index file content')
        return sketch_dir

    def create_sketch_with_static_files(self, name, static_path):
        sketch_dir = SKETCHBOOK_DIR.joinpath(name)
        static_dir = sketch_dir.joinpath(static_path.split('/')[0])
        os.makedirs(static_dir)
        target_file = sketch_dir.joinpath(f'{name}.py')
        index_file = sketch_dir.joinpath('index.html')
        static_file = static_dir.joinpath(static_path.split('/')[1])
        self.create_file(target_file)
        self.create_file(index_file)
        self.create_file(static_file, 'static file content')
        return sketch_dir

    def create_file(self, file_name, content=''):
        with file_name.open('w') as fd:
            fd.write(content)


class IndexViewTests(Pyp5jsWebTestCase):
    route = '/'

    def test_get_home_renders_index_template(self):
        self.client.get(self.route)
        self.assert_template_used('index.html')


class NewSketchViewTests(Pyp5jsWebTestCase):
    route = '/new-sketch/'

    def test_get_new_sketch_renders_new_sketch_form_template(self):
        self.client.get(self.route)
        self.assert_template_used('new_sketch_form.html')

    def test_post_without_sketch_name_should_render_form_with_error(self):
        self.client.post(self.route, data=dict(sketch_name=''))
        self.assert_template_used('new_sketch_form.html')
        self.assert_context('error', 'You have to input a sketch name to proceed.')

    def test_post_with_existing_sketch_name_should_render_form_with_error(self):
        self.create_sketch('my_existing_sketch')
        self.client.post(self.route, data=dict(sketch_name='my_existing_sketch'))
        self.assert_template_used('new_sketch_form.html')
        self.assert_context('error', 'The sketch tests-sketchbook/my_existing_sketch already exists.')

    def test_post_with_sketch_name_should_render_success_form(self):
        self.client.post(self.route, data=dict(sketch_name='a_name'))
        self.assert_template_used('new_sketch_success.html')


class SketchViewTests(Pyp5jsWebTestCase):
    route = '/sketch/'

    def test_get_sketch_does_not_exist(self):
        response = self.client.get(self.route + 'sketch_does_not_exist/')
        self.assert_404(response)

    def test_get_sketch_exists(self):
        self.create_sketch('sketch_exists')
        response = self.client.get(self.route + 'sketch_exists/')
        self.assert_200(response)
        self.assertEqual(response.data, b"index file content")

    def test_get_static_file_does_not_exist(self):
        response = self.client.get(self.route + 'foo/static/file.js')
        self.assert_404(response)

    def test_get_static_javascript_file(self):
        self.create_sketch_with_static_files('foo', 'static/file.js')
        response = self.client.get(self.route + 'foo/static/file.js')
        self.assert_200(response)
        self.assertEqual(response.headers['Content-Type'], 'application/javascript')
        self.assertEqual(response.data, b"static file content")

    def test_get_static_file(self):
        self.create_sketch_with_static_files('foo', 'static/style.css')
        response = self.client.get(self.route + 'foo/static/style.css')
        self.assert_200(response)
        self.assertEqual(response.data, b"static file content")
