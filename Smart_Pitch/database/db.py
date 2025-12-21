import os
import sqlite3

BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "app.db")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

 
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript(
        """
        -- Users table (kept for potential future use)
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        -- Pitches table: store available pitches for the app
        CREATE TABLE IF NOT EXISTS pitches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT,
            price REAL DEFAULT 0,
            owner TEXT,
            status TEXT DEFAULT 'Pending'
        );

        -- Bookings table: simple storage for confirmed bookings (kept minimal)
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            user_email TEXT,
            pitch_id INTEGER NOT NULL,
            pitch_name TEXT,
            date TEXT,
            time TEXT,
            price REAL,
            status TEXT DEFAULT 'Pending'
        );

        -- Older movie watchlist/rating tables removed from this app context
        """
    )

    conn.commit()

    # Seed default pitches if table is empty
    cur.execute("SELECT COUNT(*) as cnt FROM pitches")
    row = cur.fetchone()
    if row["cnt"] == 0:
        seed = [
            ("Riverside Sports Complex", "Manchester", 50, "Ahmed Ali", "Pending"),
            ("City Center Arena", "London", 80, "Mohamed Samy", "Approved"),
            ("Green Park Pitch", "Birmingham", 40, "Laila Karim", "Approved"),
            ("Elite Indoor Sports", "Manchester", 65, "Zain Saleh", "Approved")
        ]
        cur.executemany(
            "INSERT INTO pitches (name, location, price, owner, status) VALUES (?, ?, ?, ?, ?)",
            seed,
        )
        conn.commit()

    conn.close()
