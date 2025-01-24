from application.use_cases.book_list import GetBookList
from application.use_cases.book_detail import GetBookDetail
from application.use_cases.book_page import GetBookPage

class BookController:
    def __init__(self, book_repository):
        self.get_books_use_case = GetBookList(book_repository)
        self.get_book_detail_use_case = GetBookDetail(book_repository)
        self.get_book_page_use_case = GetBookPage(book_repository)

    def get_books(self):
        return [book.__dict__ for book in self.get_books_use_case.execute()]

    def get_book_detail(self, book_id):
        book = self.get_book_detail_use_case.execute(book_id)
        if not book:
            raise ValueError("Book not found")
        return book.__dict__

    def get_book_page(self, book_id, page_number, content_type='json'):
        page_content = self.get_book_page_use_case.execute(book_id, page_number, content_type)
        if not page_content:
            raise ValueError("Page not found")
        return page_content