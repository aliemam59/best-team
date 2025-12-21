
from Smart_Pitch.data.db import get_connection


class Pitch:
    @staticmethod
    def _row_to_dict(row):
        return {k: row[k] for k in row.keys()}

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, location, price, owner, status FROM pitches ORDER BY id")
        rows = cur.fetchall()
        conn.close()
        return [Pitch._row_to_dict(r) for r in rows]

    @staticmethod
    def get_by_id(pitch_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, location, price, owner, status FROM pitches WHERE id = ?", (pitch_id,))
        row = cur.fetchone()
        conn.close()
        return Pitch._row_to_dict(row) if row else None

    @staticmethod
    def add(name, location, price, owner):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO pitches (name, location, price, owner, status) VALUES (?, ?, ?, ?, ?)",
            (name, location, price, owner, "Pending"),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update(pitch_id, name, location, price, owner, status=None):
        conn = get_connection()
        cur = conn.cursor()
        if status is None:
            cur.execute(
                "UPDATE pitches SET name = ?, location = ?, price = ?, owner = ? WHERE id = ?",
                (name, location, price, owner, pitch_id),
            )
        else:
            cur.execute(
                "UPDATE pitches SET name = ?, location = ?, price = ?, owner = ?, status = ? WHERE id = ?",
                (name, location, price, owner, status, pitch_id),
            )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(pitch_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM pitches WHERE id = ?", (pitch_id,))
        conn.commit()
        conn.close()
