import os
from flask import Flask

from Smart_Pitch.controllers.auth_controller import auth_bp
from Smart_Pitch.controllers.user_controller import user_bp
from Smart_Pitch.controllers.owner_controller import owner_bp
from Smart_Pitch.controllers.booking_controller import booking_bp
from Smart_Pitch.controllers.admin_controller import admin_bp
from Smart_Pitch.data.db import init_db


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.secret_key = os.environ.get("SECRET_KEY", "smartpitch-secret")

    # ensure DB/schema/seed exists on startup
    init_db()

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(admin_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
