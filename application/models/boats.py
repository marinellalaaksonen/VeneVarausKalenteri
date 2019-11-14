from application import db

class Boat(db.Model):
    __tablename__ = "boats"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    boat_type = db.Column(db.String(144), nullable=False)
    boat_class = db.Column(db.String(144), nullable=False)

    def __init__(self, name, boat_type, boat_class):
        self.name = name
        self.boat_type = boat_type
        self.boat_class = boat_class