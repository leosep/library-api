import unittest
from http.server import HTTPServer
from threading import Thread
import requests
from presentation.routes.routes import RequestHandler

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('localhost', 8081), RequestHandler)
        cls.thread = Thread(target=cls.server.serve_forever)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join()

    def test_get_books_route(self):
        response = requests.get("http://localhost:8081/books")
        self.assertEqual(response.status_code, 200)

    def test_get_book_detail_route(self):
        response = requests.get("http://localhost:8081/books/1")
        self.assertIn(response.status_code, [200, 404])

    def test_get_book_page_route(self):
        response = requests.get("http://localhost:8081/books/1/pages/1/json")
        self.assertIn(response.status_code, [200, 404])