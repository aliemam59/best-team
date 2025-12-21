from flask import Blueprint, render_template, session, redirect, url_for, request

owner_bp = Blueprint(
    "owner",
    __name__,
    url_prefix="/owner"
)

@owner_bp.route("/dashboard")
def dashboard():
    if session.get("role") != "owner":
        return redirect(url_for("auth.login"))

    from Smart_Pitch.models.pitch import Pitch
    owner_email = session.get("email")
    pitches = [p for p in Pitch.get_all() if p.get("owner") == owner_email]

    return render_template("owner/owner_dashboard.html", pitches=pitches)

@owner_bp.route("/add-pitch", methods=["GET","POST"])
def add_pitch():
    if session.get("role") != "owner":
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        location = (request.form.get("location") or "").strip()
        price = float(request.form.get("price") or 0)
        owner = session.get("email") or "Unknown"

        from Smart_Pitch.models.pitch import Pitch
        Pitch.add(name, location, price, owner)

        return redirect(url_for("owner.dashboard"))

    return render_template("owner/owner_add_pitch.html")

@owner_bp.route("/edit-pitch", methods=["GET","POST"])
def edit_pitch():
    if session.get("role") != "owner":
        return redirect(url_for("auth.login"))

    pitch_id = request.args.get("id")
    if not pitch_id:
        return redirect(url_for("owner.dashboard"))

    from Smart_Pitch.models.pitch import Pitch
    p = Pitch.get_by_id(int(pitch_id))
    if not p or p.get("owner") != session.get("email"):
        return redirect(url_for("owner.dashboard"))

    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        location = (request.form.get("location") or "").strip()
        price = float(request.form.get("price") or 0)
        status = (request.form.get("status") or p.get("status"))

        Pitch.update(int(pitch_id), name, location, price, p.get("owner"), status=status)
        return redirect(url_for("owner.dashboard"))

    return render_template("owner/owner_edit_pitch.html", pitch=p)
