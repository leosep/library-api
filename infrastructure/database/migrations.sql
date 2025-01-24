CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS pages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    page_number INTEGER,
    content TEXT,
    UNIQUE (book_id, page_number),
    FOREIGN KEY (book_id) REFERENCES books (id)
);
