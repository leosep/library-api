from infrastructure.database.sql_queries import INSERT_BOOK, INSERT_PAGE

def seed_data(db_connection):
    cursor = db_connection.cursor()
    
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

    # Book 1
    cursor.execute(INSERT_BOOK, ("Book 1",))
    book_id = cursor.lastrowid
    cursor.execute(INSERT_PAGE, (book_id, 1, f"Book 1 - Page 1: {lorem_ipsum}"))
    cursor.execute(INSERT_PAGE, (book_id, 2, f"Book 1 - Page 2: {lorem_ipsum}"))

    # Book 2
    cursor.execute(INSERT_BOOK, ("Book 2",))
    book_id = cursor.lastrowid
    cursor.execute(INSERT_PAGE, (book_id, 1, f"Book 2 - Page A: {lorem_ipsum}"))
    cursor.execute(INSERT_PAGE, (book_id, 2, f"Book 2 - Page B: {lorem_ipsum}"))

    db_connection.commit()
