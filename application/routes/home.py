from flask import render_template
from datetime import date
from application import app
from application.models.reservation import Reservation

@app.route("/")
def index():
    current_year = date.today().year 
    start_year = str(current_year) + "-01-01 00:00:00"
    end_year = str(current_year + 1) + "-01-01 00:00:00"
    return render_template("index.html", 
                            current_year = current_year,
                            boats_reserved = 
                                Reservation.count_reserved_boats(start_year, end_year),
                            avg_reserved_boats_per_skipper = 
                                Reservation.avg_reserved_boats_per_skipper(start_year, end_year))