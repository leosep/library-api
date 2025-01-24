from application.interfaces.repository_interface import BookRepository
from domain.entities.book import Book
from infrastructure.database.sql_queries import (
    SELECT_ALL_BOOKS,
    SELECT_BOOK_BY_ID,
    INSERT_BOOK,
    DELETE_BOOK,
    SELECT_PAGE_BY_BOOK_ID,
    COUNT_PAGES_BY_BOOK_ID,
    INSERT_PAGE
)

class BookRepoImpl(BookRepository):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_books(self):
        cursor = self.db_connection.cursor()
        cursor.execute(SELECT_ALL_BOOKS)
        rows = cursor.fetchall()
        return [Book(book_id=row[0], title=row[1], pages=self.get_total_pages_by_book_id(row[0])) for row in rows]

    def get_book_by_id(self, book_id):
        cursor = self.db_connection.cursor()
        cursor.execute(SELECT_BOOK_BY_ID, (book_id,))
        row = cursor.fetchone()
        if row:
            return Book(book_id=row[0], title=row[1], pages=self.get_total_pages_by_book_id(row[0]))
        return None

    def add_book(self, book: Book):
        cursor = self.db_connection.cursor()
        cursor.execute(INSERT_BOOK, (book.title,))
        book_id = cursor.lastrowid
        for page_number, content in enumerate(book.pages, 1):
            cursor.execute(INSERT_PAGE, (book_id, page_number, content))  # Ensure this query is correct
        self.db_connection.commit()

    def delete_book(self, book_id: int):
        cursor = self.db_connection.cursor()
        cursor.execute(DELETE_BOOK, (book_id,))
        self.db_connection.commit()

    def get_page_content_by_book_id(self, book_id, page_number):
        cursor = self.db_connection.cursor()
        cursor.execute(SELECT_PAGE_BY_BOOK_ID, (book_id, page_number))
        
        row = cursor.fetchone()  
        
        if row:
            return str(row[0]) 
        else:
            print("No content found for book_id: {} and page_number: {}".format(book_id, page_number))
            return None  # Return None if no content is found

    def get_total_pages_by_book_id(self, book_id):
        cursor = self.db_connection.cursor()
        cursor.execute(COUNT_PAGES_BY_BOOK_ID, (book_id,))
        row = cursor.fetchone()  
        if row: 
            return int(row[0]) 
