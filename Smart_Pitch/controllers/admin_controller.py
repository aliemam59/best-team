from flask import Blueprint, render_template, session, redirect, url_for
from models.admin import (
    get_all_users,
    get_all_pitches,
    get_all_bookings
)

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

@admin_bp.route("/dashboard")
def dashboard():
    if session.get("role") != "admin":
        return redirect(url_for("auth.login"))

    users = get_all_users()
    pitches = get_all_pitches()
    bookings = get_all_bookings()

    return render_template(
        "admin/admin_dashboard.html",
        users=users,
        pitches=pitches,
        bookings=bookings
    )

@admin_bp.route("/users")
def users():
    if session.get("role") != "admin":
        return redirect(url_for("auth.login"))

    return render_template("admin/admin_users.html")

@admin_bp.route("/pitches")
def pitches():
    if session.get("role") != "admin":
        return redirect(url_for("auth.login"))

    return render_template("admin/admin_pitches.html")

@admin_bp.route("/bookings")
def bookings():
    if session.get("role") != "admin":
        return redirect(url_for("auth.login"))

    return render_template("admin/admin_bookings.html")
