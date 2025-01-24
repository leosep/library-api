import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from presentation.controllers.book_controller import BookController
from infrastructure.repositories.book_repo_impl import BookRepoImpl
from config import DATABASE_PATH

db_connection = sqlite3.connect(DATABASE_PATH, check_same_thread=False)  # Or your actual database path
repo = BookRepoImpl(db_connection)  
controller = BookController(repo)

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        if self.path == '/books':
            books = controller.get_books()
            self._set_response()
            self.wfile.write(json.dumps(books).encode())
        elif self.path.startswith('/books/'):
            parts = self.path.split('/')
            if len(parts) == 3:
                book_id = int(parts[2])
                try:
                    book = controller.get_book_detail(book_id)
                    self._set_response()
                    self.wfile.write(json.dumps(book).encode())
                except ValueError:
                    self.send_error(404, "Book not found")
            elif len(parts) == 6 and parts[3] == 'pages':
                book_id = int(parts[2])
                page_number = int(parts[4])
                content_type = str(parts[5])
                try:
                    page = controller.get_book_page(book_id, page_number, content_type)
                    self._set_response()
                    self.wfile.write(json.dumps(page).encode())
                except ValueError:
                    self.send_error(404, "Page not found")
            else:
                self.send_error(404, "Invalid path")
        else:
            self.send_error(404, "Invalid path")

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), RequestHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()
