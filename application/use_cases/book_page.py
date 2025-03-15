from application.interfaces.repository_interface import BookRepository
from application.interfaces.renderer_interface import PageRenderer

class GetBookPage:
    def __init__(self, book_repository: BookRepository,  renderer: PageRenderer):
        self.book_repository = book_repository
        self.renderer = renderer

    def execute(self, book_id: int, page_number: int):
        page_content = self.book_repository.get_page_content_by_book_id(book_id, page_number)
        if not page_content:
            raise ValueError("Page not found")
        return self.renderer.render(page_content)