from application import db
from application.models.reservation import boat_reservation
from sqlalchemy.sql import text

class Boat(db.Model):
    __tablename__ = "boat"
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
        stmt = text("SELECT COUNT(*) FROM boat"
                    " WHERE boat.boat_class = :boat_class"
                    ).params(boat_class = boat_class)

        result = db.engine.execute(stmt).fetchone()

        return result[0]

    @staticmethod
    def available_boats(starting_time, ending_time):
        stmt = text("""SELECT bo.id FROM boat bo WHERE bo.id NOT IN (
                        SELECT b.id FROM boat b
                        LEFT JOIN boat_reservation br ON b.id = br.boat_id
                        LEFT JOIN reservation r ON br.reservation_id = r.id
                        WHERE (r.starting_time < :ending_time AND r.ending_time > :starting_time))"""
                    ).params(starting_time = starting_time, ending_time = ending_time)
        boats = db.engine.execute(stmt)

        response = []
        for boat in boats:
            response.append(boat[0])

        return response

    @staticmethod
    def available_boats_for_changing_reservation(starting_time, ending_time, reservation_id):
        stmt = text("""SELECT bo.id FROM boat bo WHERE bo.id NOT IN (
                        SELECT b.id FROM boat b
                        LEFT JOIN boat_reservation br ON b.id = br.boat_id
                        LEFT JOIN reservation r ON br.reservation_id = r.id
                        WHERE ((r.starting_time < :ending_time AND r.ending_time > :starting_time)
                         AND r.id <> :reservation_id))"""
                    ).params(
                        starting_time = starting_time, ending_time = ending_time, reservation_id  = reservation_id
                    )
        boats = db.engine.execute(stmt)

        response = []
        for boat in boats:
            response.append(boat[0])

        return response