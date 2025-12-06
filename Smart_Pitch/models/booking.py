from datetime import datetime
from app import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'), nullable=False)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')  # active / canceled

    user = db.relationship('User', backref='bookings')
    pitch = db.relationship('Pitch', backref='bookings')
