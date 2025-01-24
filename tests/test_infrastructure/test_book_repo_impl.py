import unittest
from unittest.mock import MagicMock
from infrastructure.repositories.book_repo_impl import BookRepoImpl
from domain.entities.book import Book

class TestBookRepoImpl(unittest.TestCase):
    def setUp(self):
        # Mock the database connection and the repo
        self.db_connection_mock = MagicMock()
        self.repo = BookRepoImpl(self.db_connection_mock)
        
        # Create a book mock
        self.book = Book(1, "Test Book", ["Page 1", "Page 2"])
        
        # Mock the method add_book to simulate adding a book
        self.repo.add_book = MagicMock()

        # Mock repository methods for testing
        self.repo.get_all_books = MagicMock(return_value=[self.book])
        self.repo.get_book_by_id = MagicMock(return_value=self.book)
        self.repo.delete_book = MagicMock()

    def test_get_all_books(self):
        books = self.repo.get_all_books()
        self.assertGreater(len(books), 0)

    def test_get_book_by_id(self):
        book = self.repo.get_book_by_id(2)
        print(book)
        self.assertEqual(book.title, "Test Book")

    def test_add_book(self):
        new_book = Book(2, "New Book", ["Page A"])
        self.repo.add_book(new_book)
        self.repo.add_book.assert_called_once_with(new_book)

    def test_delete_book(self):
        self.repo.delete_book(1)
        self.repo.delete_book.assert_called_once_with(1)

