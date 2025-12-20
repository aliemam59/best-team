class User:
    users = [
        {"id": 1, "email": "user@demo.com", "password": "123", "role": "user"},
        {"id": 2, "email": "owner@demo.com", "password": "123", "role": "owner"},
        {"id": 3, "email": "admin@demo.com", "password": "123", "role": "admin"},
    ]

    @staticmethod
    def login(email, password):
        for user in User.users:
            if user["email"] == email and user["password"] == password:
                return user
        return None

    @staticmethod
    def get_all():
        return User.users

    @staticmethod
    def delete(user_id):
        User.users = [u for u in User.users if u["id"] != user_id]
