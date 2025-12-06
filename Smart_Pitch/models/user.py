from database.db import get_db

class User:

    @staticmethod
    def create(name, email, password):
        db = get_db()
        db.execute(
            "INSERT INTO users (full_name, email, password, role) VALUES (?, ?, ?, ?)",
            (name, email, password, "user")
        )
        db.commit()

    @staticmethod
    def get_by_login(email, password):
        db = get_db()
        return db.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        ).fetchone()