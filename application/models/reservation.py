from application import db

from sqlalchemy.sql import text

boat_reservation = db.Table('boat_reservation',
    db.Column("reservation_id", db.Integer, db.ForeignKey("reservations.id")), 
    db.Column("boats_id", db.Integer, db.ForeignKey("boats.id"))    
)

class Reservation(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key = True)
    starting_time = db.Column(db.DateTime, nullable = False)
    ending_time = db.Column(db.DateTime, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    boats_reserved = db.relationship("Boat", secondary = boat_reservation, backref = "reservations")

    def __init__(self, starting_time, ending_time, user_id):
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.user_id = user_id

    @staticmethod
    def count_reserved_boats(starting_time, ending_time):
        stmt = text("SELECT COUNT(*) FROM boat_reservation"
                    " JOIN reservations ON reservations.id = boat_reservation.reservation_id"
                    " WHERE (reservations.starting_time < :ending_time AND reservations.ending_time > :starting_time)"
                    ).params(starting_time = starting_time, ending_time = ending_time)

        result = db.engine.execute(stmt).fetchone()

        return result[0]