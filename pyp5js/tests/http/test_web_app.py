from pyp5js.http.web_app import app
from unittest import TestCase

class WebAppTests(TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/') 
        assert result.status_code == 200
