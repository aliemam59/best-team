import sqlite3
from flask import g

DB_NAME = "smartpitch.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_NAME)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        with open("database/schema.sql", "r") as f:
            db.executescript(f.read())
        db.commit()
    app.teardown_appcontext(close_db)