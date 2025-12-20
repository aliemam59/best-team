from flask import Blueprint, render_template, session, redirect, url_for

booking_bp = Blueprint(
    "booking",
    __name__,
    url_prefix="/booking"
)

@booking_bp.route("/search")
def search():
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))

    return render_template("booking/search.html")

@booking_bp.route("/pitch-details")
def pitch_details():
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))

    return render_template("booking/pitch_details.html")

@booking_bp.route("/confirm")
def confirm_booking():
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))

    return render_template("booking/booking_page.html")

@booking_bp.route("/success")
def success():
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))

    return render_template("booking/booking_success.html")
