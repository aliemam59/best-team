from Smart_Pitch.data.db import get_connection


class Booking:
    @staticmethod
    def _row_to_dict(row):
        return {k: row[k] for k in row.keys()}

    @staticmethod
    def get_all():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookings ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()
        return [Booking._row_to_dict(r) for r in rows]

    @staticmethod
    def get_by_user(user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bookings WHERE user_id = ? ORDER BY id DESC", (user_id,))
        rows = cur.fetchall()
        conn.close()
        return [Booking._row_to_dict(r) for r in rows]

    @staticmethod
    def add(user_id, user_email, pitch_id, pitch_name, date, time, price, status="Pending"):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO bookings (user_id, user_email, pitch_id, pitch_name, date, time, price, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, user_email, pitch_id, pitch_name, date, time, price, status),
        )
        conn.commit()
        new_id = cur.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def delete(booking_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
        conn.commit()
        conn.close()
