from flask import Flask, render_template

from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from controllers.owner_controller import owner_bp
from controllers.booking_controller import booking_bp
from controllers.admin_controller import admin_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "smartpitch-secret"

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
