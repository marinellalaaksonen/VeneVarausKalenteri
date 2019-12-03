from flask import redirect, render_template, request, url_for

from application import app, db
from application.models.reservation import Reservation

@app.route("/calendar/", methods = ["GET"])
def calendar_index():
    return render_template("calendar.html", reservations = Reservation.query.all())