from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.get_by_login(email, password)
        if user:
            session["user_id"] = user["user_id"]
            session["role"] = user["role"]
            session["name"] = user["full_name"]
            return redirect(url_for("auth.dashboard"))

        return "Invalid email or password."

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        User.create(name, email, password)
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("user/dashboard.html", name=session["name"])


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))