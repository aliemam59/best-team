from . import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # يمكن تخزين hash
    email = db.Column(db.String(100), unique=True, nullable=False)

    def _repr_(self):
        return f"<Admin {self.username}>"