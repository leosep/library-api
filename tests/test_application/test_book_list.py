import unittest
from unittest.mock import MagicMock
from application.use_cases.book_list import GetBookList

class TestGetBookList(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.use_case = GetBookList(self.mock_repo)

    def test_execute_returns_all_books(self):
        self.mock_repo.get_all_books.return_value = [
            {"book_id": 1, "title": "Book 1", "pages": []},
            {"book_id": 2, "title": "Book 2", "pages": []}
        ]
        result = self.use_case.execute()
        self.assertEqual(len(result), 2)
        self.mock_repo.get_all_books.assert_called_once()