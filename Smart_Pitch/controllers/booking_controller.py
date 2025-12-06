from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.booking import Booking
from models.pitch import Pitch
from app import db

booking_bp = Blueprint('booking', __name__, template_folder='templates/booking')

# Search pitches
@booking_bp.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        location = request.form.get('location')
        date = request.form.get('date')
        # مثال على فلترة حسب location فقط
        pitches = Pitch.query.filter(Pitch.location.contains(location)).all()
        return render_template('search.html', pitches=pitches)
    return render_template('search.html', pitches=[])

# View pitch details
@booking_bp.route('/pitch/<int:pitch_id>')
def pitch_details(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    return render_template('pitch_details.html', pitch=pitch)

# Book a pitch
@booking_bp.route('/book/<int:pitch_id>', methods=['GET', 'POST'])
def book_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if request.method == 'POST':
        user_id = session.get('user_id')  # assuming user is logged in
        booking = Booking(user_id=user_id, pitch_id=pitch.id)
        db.session.add(booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('booking.list_bookings'))
    return render_template('booking_page.html', pitch=pitch)

# Cancel booking
@booking_bp.route('/cancel/<int:booking_id>')
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    booking.status = 'canceled'
    db.session.commit()
    flash('Booking canceled.', 'info')
    return redirect(url_for('booking.list_bookings'))

# List user bookings
@booking_bp.route('/my_bookings')
def list_bookings():
    user_id = session.get('user_id')
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return render_template('my_bookings.html', bookings=bookings)

