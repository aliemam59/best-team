from flask import Blueprint, render_template, request, redirect, session, url_for
from models.booking import Booking
from models.pitch import Pitch

booking_bp = Blueprint("booking", __name__, url_prefix="/booking")


@booking_bp.route("/create/<int:pitch_id>", methods=["GET", "POST"])
def create_booking(pitch_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    pitch = Pitch.get_by_id(pitch_id)

    if not pitch:
        return "Pitch not found."

    if request.method == "POST":
        date = request.form["date"]
        time_slot = request.form["time_slot"]

        Booking.create(
            user_id=session["user_id"],
            pitch_id=pitch_id,
            date=date,
            time_slot=time_slot
        )

        return redirect(url_for("booking.my_bookings"))

    return render_template("booking/create_booking.html", pitch=pitch)


@booking_bp.route("/my")
def my_bookings():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    bookings = Booking.get_user_bookings(session["user_id"])

    return render_template("booking/my_bookings.html", bookings=bookings)


@booking_bp.route("/cancel/<int:booking_id>")
def cancel_booking(booking_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    Booking.cancel(booking_id)

    return redirect(url_for("booking.my_bookings"))