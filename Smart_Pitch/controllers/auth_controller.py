from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    return render_template("index.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.login(email, password)
        if user:
            session["email"] = user["email"]
            session["role"] = user["role"]

            if user["role"] == "user":
                return redirect(url_for("user.dashboard"))
            elif user["role"] == "owner":
                return redirect(url_for("owner.dashboard"))
            elif user["role"] == "admin":
                return redirect(url_for("admin.dashboard"))

        return render_template("auth/login.html", error="Invalid credentials")

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
