import sqlite3
from infrastructure.repositories.book_repo_impl import BookRepoImpl
from infrastructure.database.migrations import run_migrations
from infrastructure.database.seeder import seed_data
from presentation.routes.routes import RequestHandler
from http.server import HTTPServer
from config import DATABASE_PATH

def create_db_connection():
    return sqlite3.connect(DATABASE_PATH, check_same_thread=False)

if __name__ == "__main__":
    db_connection = create_db_connection()

    # Run migrations to ensure tables exist
    run_migrations(db_connection)

    # Seed initial data if necessary
    seed_data(db_connection)

    repo = BookRepoImpl(db_connection)
    server = HTTPServer(("0.0.0.0", 8080), RequestHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()
