from flask import Blueprint, render_template, session, redirect, url_for
from Smart_Pitch.models.admin import get_all_users, get_all_pitches, get_all_bookings

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)


def _require_admin():
    """Redirect to login if not logged in as admin."""
    if session.get("role") != "admin":
        return redirect(url_for("auth.login"))
    return None


@admin_bp.route("/dashboard")
def dashboard():
    guard = _require_admin()
    if guard:
        return guard

    users = get_all_users()
    pitches = get_all_pitches()
    bookings = get_all_bookings()

    return render_template(
        "admin/admin_dashboard.html",
        users=users,
        pitches=pitches,
        bookings=bookings,
        users_count=len(users),
        pitches_count=len(pitches),
        bookings_count=len(bookings),
    )


@admin_bp.route("/users")
def users():
    guard = _require_admin()
    if guard:
        return guard

    users_list = get_all_users()
    return render_template("admin/admin_users.html", users=users_list)


@admin_bp.route("/pitches")
def pitches():
    guard = _require_admin()
    if guard:
        return guard

    pitches_list = get_all_pitches()
    return render_template("admin/admin_pitches.html", pitches=pitches_list)


@admin_bp.route("/bookings")
def bookings():
    guard = _require_admin()
    if guard:
        return guard

    bookings_list = get_all_bookings()
    return render_template("admin/admin_bookings.html", bookings=bookings_list)
