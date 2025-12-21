from flask import Blueprint, render_template, request, redirect, url_for, session
from Smart_Pitch.models.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/")
def index():
    return render_template("index.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip()
        password = request.form.get("password") or ""

        user = User.login(email, password)

        if user:
            session["user_id"] = user["id"]
            session["email"] = user["email"]
            session["role"] = user["role"]

            if user["role"] == "user":
                return redirect(url_for("user.dashboard"))
            elif user["role"] == "owner":
                return redirect(url_for("owner.dashboard"))
            elif user["role"] == "admin":
                return redirect(url_for("admin.dashboard"))

            return redirect(url_for("auth.index"))

        return render_template("auth/login.html", error="Invalid credentials")

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """
    Simple in-memory register (for prototype).
    Creates a normal 'user' role account.
    """
    if request.method == "POST":
        email = (request.form.get("email") or "").strip()
        password = request.form.get("password") or ""


        if not email or not password:
            return render_template("auth/register.html", error="Email and password are required")

        exists = any(u["email"].lower() == email.lower() for u in User.users)
        if exists:
            return render_template("auth/register.html", error="Email already exists")

        new_id = max((u["id"] for u in User.users), default=0) + 1
        User.users.append({"id": new_id, "email": email, "password": password, "role": "user"})

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
