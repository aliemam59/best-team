from database.db import get_db

class Booking:

    @staticmethod
    def create(user_id, pitch_id, date, time_slot, status="confirmed"):
        db = get_db()
        db.execute(
            """
            INSERT INTO bookings (user_id, pitch_id, date, time_slot, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, pitch_id, date, time_slot, status)
        )
        db.commit()

    @staticmethod
    def get_by_id(booking_id):
        db = get_db()
        return db.execute(
            "SELECT * FROM bookings WHERE booking_id = ?",
            (booking_id,)
        ).fetchone()

    @staticmethod
    def get_user_bookings(user_id):
        db = get_db()
        return db.execute(
            "SELECT * FROM bookings WHERE user_id = ?",
            (user_id,)
        ).fetchall()

    @staticmethod
    def cancel(booking_id):
        db = get_db()
        db.execute(
            "UPDATE bookings SET status = 'cancelled' WHERE booking_id = ?",
            (booking_id,)
        )
        db.commit()