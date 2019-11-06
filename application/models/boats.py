from application import db

class Boat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    boat_type = db.Column(db.String(), nullable=False)
    boat_class = db.Column(db.String(), nullable=False)

    def __init__(self, name, boatType, boatClass):
        self.name = name
        self.boatType = boatType
        self.boatClass = boatClass
