from flask import Blueprint, render_template, session, redirect, url_for

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/user"
)

@user_bp.route("/dashboard")
def dashboard():
    if session.get("role") != "user":
        return redirect(url_for("auth.login"))

    return render_template("user/dashboard.html")
