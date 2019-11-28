from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from datetime import datetime

from application import app, db
from application.models.boats import Boat
from application.models.reservation import Reservation
from application.forms.reservationform import ReservationForm

@app.route("/reservation/", methods = ["GET"])
@login_required
def reserve_boat():
    return render_template("reservations/reserve_boat.html", form = ReservationForm())

@app.route("/reservation/", methods = ["POST"])
@login_required
def make_reservation():
    form = ReservationForm(request.form)

    if not form.validate():
        return render_template("reservations/reserve_boat.html", form = form)

    starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    ending = datetime.combine(form.ending_date.data, form.ending_time.data)

    if starting > ending:
        return render_template("reservations/reserve_boat.html", form = form, 
                                error = "Ending time should be after starting time")

    # boats_reserved = Reservation.count_reserved_boats(form.starting_time.data, form.ending_time.data)
    # print("Veneitä varattu:", Reservation.count_available_boats(form.starting_time.data, form.ending_time.data))
    reservation = Reservation(starting, ending, current_user.id)
    reservation.boats_reserved.append(Boat.query.get(1))
    
    db.session().add(reservation)
    db.session().commit()

    return redirect(url_for("calendar_index"))