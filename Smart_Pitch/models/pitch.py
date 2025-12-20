class Pitch:
    pitches = [
        {
            "id": 1,
            "name": "Riverside Sports Complex",
            "location": "Manchester",
            "price": 50,
            "owner": "Ahmed Ali",
            "status": "Pending"
        },
        {
            "id": 2,
            "name": "City Center Arena",
            "location": "London",
            "price": 80,
            "owner": "Mohamed Samy",
            "status": "Approved"
        }
    ]

    @staticmethod
    def get_all():
        return Pitch.pitches

    @staticmethod
    def add(name, location, price, owner):
        new_id = len(Pitch.pitches) + 1
        Pitch.pitches.append({
            "id": new_id,
            "name": name,
            "location": location,
            "price": price,
            "owner": owner,
            "status": "Pending"
        })

    @staticmethod
    def delete(pitch_id):
        Pitch.pitches = [p for p in Pitch.pitches if p["id"] != pitch_id]
