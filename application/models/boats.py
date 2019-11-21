from application import db
from application.models.reservation import boat_reservation
from sqlalchemy.sql import text

class Boat(db.Model):
    __tablename__ = "boats"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    boat_type = db.Column(db.String(144), nullable=False)
    boat_class = db.Column(db.String(144), nullable=False)

    reservations_for_boat = db.relationship("Reservation", secondary = boat_reservation, back_populates = "boats_reserved")

    def __init__(self, name, boat_type, boat_class):
        self.name = name
        self.boat_type = boat_type
        self.boat_class = boat_class

    @staticmethod
    def count_boats(boat_class = "J/80"):
        stmt = text("SELECT COUNT(*) FROM boats"
                    " WHERE boats.boat_class = :boat_class"
                    ).params(boat_class = boat_class)

        result = db.engine.execute(stmt).fetchone()

        return result[0]