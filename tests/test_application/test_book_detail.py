import unittest
from unittest.mock import MagicMock
from application.use_cases.book_detail import GetBookDetail

class TestGetBookDetail(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.use_case = GetBookDetail(self.mock_repo)

    def test_execute_returns_correct_book(self):
        self.mock_repo.get_book_by_id.return_value = {"book_id": 1, "title": "Book 1", "pages": []}
        result = self.use_case.execute(2)
        self.assertEqual(result["title"], "Book 1")
        self.mock_repo.get_book_by_id.assert_called_once_with(2)