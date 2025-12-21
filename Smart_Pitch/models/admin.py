from Smart_Pitch.models.user import User
from Smart_Pitch.models.booking import Booking
from Smart_Pitch.models.pitch import Pitch


def get_all_users():
    return User.get_all()


def get_all_pitches():
    return Pitch.get_all()


def get_all_bookings():
    return Booking.get_all()


def delete_user(user_id):
    User.delete(user_id)


def delete_pitch(pitch_id):
    Pitch.delete(pitch_id)


def delete_booking(booking_id):
    Booking.delete(booking_id)
