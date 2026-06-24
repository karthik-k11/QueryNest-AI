import sqlite3
from pathlib import Path

DATABASE_FOLDER = Path("database")
DATABASE_FOLDER.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_FOLDER / "sql_history.db"


def get_connection():

    return sqlite3.connect(DATABASE_PATH)


def create_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS query_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_question TEXT NOT NULL,

            generated_sql TEXT NOT NULL,

            query_type TEXT NOT NULL,

            difficulty TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()


def save_query(user_question, generated_sql, query_type, difficulty):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO query_history
        (
            user_question,
            generated_sql,
            query_type,
            difficulty
        )

        VALUES (?, ?, ?, ?)
    """, (
        user_question,
        generated_sql,
        query_type,
        difficulty
    ))

    connection.commit()

    connection.close()


def get_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            user_question,
            generated_sql,
            query_type,
            difficulty,
            created_at

        FROM query_history

        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    connection.close()

    return history