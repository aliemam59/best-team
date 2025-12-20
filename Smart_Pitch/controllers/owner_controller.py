from flask import Blueprint, render_template, session, redirect, url_for

owner_bp = Blueprint(
    "owner",
    __name__,
    url_prefix="/owner"
)

@owner_bp.route("/dashboard")
def dashboard():
    if session.get("role") != "owner":
        return redirect(url_for("auth.login"))

    return render_template("owner/owner_dashboard.html")

@owner_bp.route("/add-pitch")
def add_pitch():
    if session.get("role") != "owner":
        return redirect(url_for("auth.login"))

    return render_template("owner/owner_add_pitch.html")

@owner_bp.route("/edit-pitch")
def edit_pitch():
    if session.get("role") != "owner":
        return redirect(url_for("auth.login"))

    return render_template("owner/owner_edit_pitch.html")
