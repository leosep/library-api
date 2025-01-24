from application.interfaces.repository_interface import BookRepository

class GetBookDetail:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: int):
        return self.book_repository.get_book_by_id(book_id)