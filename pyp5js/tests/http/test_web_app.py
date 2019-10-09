from pyp5js.http.web_app import app as web_app
from flask_testing import TestCase

class WebAppTests(TestCase):

    render_templates = False

    def create_app(self):
        app = web_app
        app.config['TESTING'] = True
        return app

    def test_get_home_renders_index_template(self):
        self.client.get('/')
        self.assert_template_used('index.html')

    def test_get_new_sketch_renders_new_sketch_form_template(self):
        self.client.get('/new-sketch/')
        self.assert_template_used('new_sketch_form.html')
