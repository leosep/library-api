from application.interfaces.repository_interface import BookRepository

class GetBookPage:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: int, page_number: int, content_type: str):
        page_content = self.book_repository.get_page_content_by_book_id(book_id, page_number)
        if not page_content:
            raise ValueError("Page not found.")

        if content_type == 'json':
            return {"content": page_content}
        elif content_type == 'html':
            return f"<html><body><h1>Page {page_number} of Book {book_id}</h1><p>{page_content}</p></body></html>"
        elif content_type == 'text':
            return f"Page {page_number} of Book {book_id}: {page_content}"
        else:
            return {"content": page_content}