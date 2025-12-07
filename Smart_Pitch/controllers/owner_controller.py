from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.pitch import Pitch
from . import db

owner_bp = Blueprint('owner', _name_)

@owner_bp.route('/owner/dashboard')
def owner_dashboard():
    owner_id = 1
    pitches = Pitch.query.filter_by(owner_id=owner_id).all()
    return render_template('owner_dashboard.html', pitches=pitches)

@owner_bp.route('/owner/add', methods=['GET', 'POST'])
def add_pitch():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        type_ = request.form['type']
        price = request.form['price']
        owner_id = 1
        new_pitch = Pitch(name=name, location=location, type=type_, price=price, owner_id=owner_id)
        db.session.add(new_pitch)
        db.session.commit()
        flash('Pitch added successfully!')
        return redirect(url_for('owner.owner_dashboard'))
    return render_template('owner_add_pitch.html')

@owner_bp.route('/owner/edit/<int:pitch_id>', methods=['GET', 'POST'])
def edit_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if request.method == 'POST':
        pitch.name = request.form['name']
        pitch.location = request.form['location']
        pitch.type = request.form['type']
        pitch.price = request.form['price']
        db.session.commit()
        flash('Pitch updated successfully!')
        return redirect(url_for('owner.owner_dashboard'))
    return render_template('owner_edit_pitch.html', pitch=pitch)

@owner_bp.route('/owner/delete/<int:pitch_id>', methods=['POST'])
def delete_pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    db.session.delete(pitch)
    db.session.commit()
    flash('Pitch deleted successfully!')
    return redirect(url_for('owner.owner_dashboard'))