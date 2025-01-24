def run_migrations(db_connection, sql_file="infrastructure/database/migrations.sql"):
    cursor = db_connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books';")
    table_exists = cursor.fetchone()

    if not table_exists:
        print("Running migrations...")

        with open(sql_file, "r") as file:
            sql_script = file.read()
            cursor.executescript(sql_script)
        print("Migrations completed successfully.")
    else:
        print("Tables already exist. Skipping migrations.")
