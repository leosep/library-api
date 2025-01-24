# Book SQL queries
SELECT_ALL_BOOKS = "SELECT * FROM books;"
SELECT_BOOK_BY_ID = "SELECT * FROM books WHERE id = ?;"
INSERT_BOOK = "INSERT OR IGNORE INTO books (title) VALUES (?);"
DELETE_BOOK = "DELETE FROM books WHERE id = ?;"

COUNT_PAGES_BY_BOOK_ID = "SELECT COUNT(id) FROM pages WHERE book_id = ?;"
SELECT_PAGE_BY_BOOK_ID = "SELECT content FROM pages WHERE book_id = ? AND page_number = ?;"
INSERT_PAGE = "INSERT OR IGNORE INTO pages (book_id, page_number, content) VALUES (?, ?, ?);"
