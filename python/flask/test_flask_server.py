import codecs
import pathlib
import unittest

import xmlrunner

from flask_server import app

path = str(pathlib.Path(__file__).parent.absolute())


class ServerTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_index_html(self):
        content = b'<p>Hello ! ...</p>'
        self.assertEqual(self.app.get('/').data, content)

    def test_get_blog_html(self):
        content = b'<p>Hier ist der Blog</p>'
        self.assertEqual(self.app.get('/blog').data, content)

    def test_get_about_html(self):
        html_input = codecs.open(path + '/templates/about.html')
        text = html_input.read()
        html_input.close()
        self.assertEqual(text.encode('UTF-8'), self.app.get('/about').data)


if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output=path + 'test-reports/')
    unittest.main(testRunner=runner)
