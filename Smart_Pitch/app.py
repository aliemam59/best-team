from flask import Flask
from controllers.auth import auth_bp
from controllers.owner import owner_bp
from controllers.booking import booking_bp
from controllers.admin import admin_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret-key"

    app.register_blueprint(auth_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def home():
        return "Pitch Booking System Running"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
