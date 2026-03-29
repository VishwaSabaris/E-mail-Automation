import sqlite3

DB_NAME = "events.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event TEXT,
        repo TEXT,
        user TEXT,
        time TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_event(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events (event, repo, user, time, status)
    VALUES (?, ?, ?, ?, ?)
    """, (
        data.get("event"),
        data.get("repo"),
        data.get("user"),
        data.get("time"),
        data.get("status")
    ))

    conn.commit()
    conn.close()
