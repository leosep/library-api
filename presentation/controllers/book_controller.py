from application.interfaces.renderer_interface import PageRenderer
from application.use_cases.book_list import GetBookList
from application.use_cases.book_detail import GetBookDetail
from application.use_cases.book_page import GetBookPage
from application.renderers.plain_text_renderer import PlainTextRenderer
from application.renderers.html_renderer import HTMLRenderer
from application.renderers.json_renderer import JsonRenderer

class BookController:
    def __init__(self, book_repository):
        self.book_repository = book_repository
        self.get_books_use_case = GetBookList(book_repository)
        self.get_book_detail_use_case = GetBookDetail(book_repository)

    def _get_renderer(self, format: str) -> PageRenderer:
        renderer_map = {
            "html": HTMLRenderer,
            "json": JsonRenderer
        }
        return renderer_map.get(format, PlainTextRenderer)()

    def get_books(self):
        """Returns the list of books."""
        return [book.__dict__ for book in self.get_books_use_case.execute()]

    def get_book_detail(self, book_id):
        """Returns the details of a single book by its ID."""
        book = self.get_book_detail_use_case.execute(book_id)
        if not book:
            raise ValueError("Book not found")
        return book.__dict__

    def get_book_page(self, book_id, page_number, content_type='json'):
        """Returns the requested page of the book in the specified format."""
        renderer = self._get_renderer(content_type)
        get_book_page_use_case = GetBookPage(self.book_repository, renderer)
        
        page_content = get_book_page_use_case.execute(book_id, page_number)
        if not page_content:
            raise ValueError("Page not found")
        
        return page_content
