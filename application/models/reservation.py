from application import db

from sqlalchemy.sql import text

boat_reservation = db.Table('boat_reservation',
    db.Column("reservation_id", db.Integer, db.ForeignKey("reservation.id")), 
    db.Column("boat_id", db.Integer, db.ForeignKey("boat.id"))    
)

class Reservation(db.Model):
    __tablename__ = "reservation"
    id = db.Column(db.Integer, primary_key = True)
    starting_time = db.Column(db.DateTime, nullable = False)
    ending_time = db.Column(db.DateTime, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
    boats_reserved = db.relationship("Boat", secondary = boat_reservation, back_populates = "reservations_for_boat")

    def __init__(self, starting_time, ending_time, user_id):
        self.starting_time = starting_time
        self.ending_time = ending_time
        self.user_id = user_id

    @staticmethod
    def count_reserved_boats(starting_time, ending_time):
        stmt = text("SELECT COUNT(*) FROM boat_reservation br"
                    " JOIN reservation r ON r.id = br.reservation_id"
                    " WHERE (r.starting_time < :ending_time AND r.ending_time > :starting_time)"
                    ).params(starting_time = starting_time, ending_time = ending_time)

        result = db.engine.execute(stmt).fetchone()

        return result[0]