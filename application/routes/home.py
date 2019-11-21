from flask import render_template
from application import app
from application.models.reservation import Reservation

@app.route("/")
def index():
    return render_template("index.html", boats_reserved_2019 = Reservation.count_reserved_boats("2019-01-01 00:00:00", "2020-01-01 00:00:00"))