class Booking:
    bookings = [
        {
            "id": 1,
            "user": "Ahmed Ali",
            "pitch": "Riverside Sports Complex",
            "date": "2025-12-20",
            "time": "18:00 - 20:00",
            "price": 100,
            "status": "Confirmed"
        }
    ]

    @staticmethod
    def get_all():
        return Booking.bookings

    @staticmethod
    def add(user, pitch, date, time, price):
        new_id = len(Booking.bookings) + 1
        Booking.bookings.append({
            "id": new_id,
            "user": user,
            "pitch": pitch,
            "date": date,
            "time": time,
            "price": price,
            "status": "Pending"
        })

    @staticmethod
    def delete(booking_id):
        Booking.bookings = [b for b in Booking.bookings if b["id"] != booking_id]
