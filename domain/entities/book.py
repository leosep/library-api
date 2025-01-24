from typing import List

class Book:
    def __init__(self, book_id: int, title: str, pages: List[str]):
        self.book_id = book_id
        self.title = title
        self.pages = pages

    def get_page(self, page_number: int) -> str:
        if 0 < page_number <= len(self.pages):
            return self.pages[page_number - 1]
        raise ValueError("Page number out of range")