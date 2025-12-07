from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.admin import Admin
from models.pitch import Pitch
from models.booking import Booking
from models.user import User
from . import db

admin_bp = Blueprint('admin', _name_)

@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    users = User.query.all()
    pitches = Pitch.query.all()
    bookings = Booking.query.all()
    return render_template('admin_dashboard.html', users=users, pitches=pitches, bookings=bookings)

@admin_bp.route('/admin/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/admin/delete_pitch/<int:pitch_id>', methods=['POST'])
def delete_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    db.session.delete(pitch)
    db.session.commit()
    flash('Pitch deleted successfully!')
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/admin/delete_booking/<int:booking_id>', methods=['POST'])
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash('Booking deleted successfully!')
    return redirect(url_for('admin.admin_dashboard'))

@admin_bp.route('/admin/remove_spam/<int:user_id>', methods=['POST'])
def remove_spam(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Spam account removed successfully!')
    return redirect(url_for('admin.admin_dashboard'))