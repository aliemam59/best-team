from flask import Blueprint, render_template, session, redirect, url_for, request
from Smart_Pitch.models.booking import Booking
from Smart_Pitch.models.pitch import Pitch


def _require_user():
    """Redirect to login if not logged in as a normal user."""
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))
    return None

booking_bp = Blueprint(
    "booking",
    __name__,
    url_prefix="/booking"
)


def _require_user():
    """Redirect to login if not logged in as a normal user."""
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))
    return None


@booking_bp.route("/search")
def search():
    guard = _require_user()
    if guard:
        return guard

    return render_template("booking/search.html")


@booking_bp.route("/pitch-details")
def pitch_details():
    guard = _require_user()
    if guard:
        return guard

    pitch_id = request.args.get("id")
    pitch = None
    if pitch_id:
        pitch = Pitch.get_by_id(int(pitch_id))
    return render_template("booking/pitch_details.html", pitch=pitch)


@booking_bp.route("/confirm")
def confirm_booking():
    guard = _require_user()
    if guard:
        return guard

    pitch_id = request.args.get("id")
    pitch = None
    if pitch_id:
        pitch = Pitch.get_by_id(int(pitch_id))
    return render_template("booking/booking_page.html", pitch=pitch)


@booking_bp.route("/success", methods=["GET","POST"])
def success():
    guard = _require_user()
    if guard:
        return guard

    if request.method == "POST":
        user_id = session.get("user_id")
        user_email = session.get("email")
        pitch_id = int(request.form.get("pitch_id"))
        pitch_name = request.form.get("pitch_name")
        date = request.form.get("date")
        time = request.form.get("time_slot")
        price = float(request.form.get("price") or 0)

        Booking.add(user_id, user_email, pitch_id, pitch_name, date, time, price, status="Confirmed")
        return render_template("booking/booking_success.html")

    # GET fallback
    return render_template("booking/booking_success.html")





@booking_bp.route("/my-bookings")
def my_bookings():
    guard = _require_user()
    if guard:
        return guard

    user_id = session.get("user_id")
    bookings = Booking.get_by_user(user_id)
    return render_template("booking/my_bookings.html", bookings=bookings)


@booking_bp.route("/cancel/<int:booking_id>", methods=["POST"])
def cancel_booking(booking_id):
    guard = _require_user()
    if guard:
        return guard

    user_id = session.get("user_id")
    # ensure booking belongs to current user before deleting
    b = next((b for b in Booking.get_all() if b["id"] == booking_id), None)
    if b and b.get("user_id") == user_id:
        Booking.delete(booking_id)
    return redirect(url_for("booking.my_bookings"))
