from abc import ABC, abstractmethod
from typing import List
from domain.entities.book import Book

class BookRepository(ABC):
    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def get_book_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def get_page_content_by_book_id(self, book_id: int, page_id: int) -> str:
        pass

    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def delete_book(self, book_id: int):
        pass
    
    @abstractmethod
    def get_total_pages_by_book_id(self, book_id: int) -> int:
        pass
