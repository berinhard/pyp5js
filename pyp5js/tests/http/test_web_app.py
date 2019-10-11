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
        return os.makedirs(SKETCHBOOK_DIR.joinpath(name))


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

