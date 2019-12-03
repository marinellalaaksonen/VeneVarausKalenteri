from flask import redirect, render_template, request, url_for
from flask_login import current_user
from datetime import datetime

from application import app, db, login_required
from application.models.boats import Boat
from application.models.reservation import Reservation
from application.forms.reservationform import ReservationForm

@app.route("/reservation/", methods = ["GET"])
@login_required()
def reserve_boat():
    return render_template("reservations/reserve_boat.html", form = ReservationForm())

@app.route("/reservation/", methods = ["POST"])
@login_required()
def make_reservation():
    form = ReservationForm(request.form)

    if not form.validate():
        return render_template("reservations/reserve_boat.html", form = form)

    starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    ending = datetime.combine(form.ending_date.data, form.ending_time.data)

    if starting > ending:
        return render_template("reservations/reserve_boat.html", form = form, 
                                error = "Ending time should be after starting time")

    available_boats = Boat.available_boats(starting, ending)
    if len(available_boats) < form.boats.data:
        return render_template("reservations/reserve_boat.html", form = form, 
                                error = "Not enough boats available for this time")
    
    reservation = Reservation(starting, ending, current_user.id)

    for i in range(form.boats.data):
        reservation.boats_reserved.append(Boat.query.get(available_boats[i]))
    
    db.session().add(reservation)
    db.session().commit()

    return redirect(url_for("calendar_index"))