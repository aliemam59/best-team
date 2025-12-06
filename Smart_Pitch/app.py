from flask import Flask
from controllers.auth_controller import auth_bp
from database.db import init_db

def create_app():
    app = Flask(__name__)
    app.secret_key = "smartpitch-secret-key"

    init_db(app)

    app.register_blueprint(auth_bp)

    @app.route("/")
    def home():
        return "Welcome to Smart Pitch!"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

