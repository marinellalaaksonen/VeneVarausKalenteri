from flask import redirect, render_template, request, url_for
from flask_login import current_user
from datetime import datetime, timedelta

from application import app, db, login_required
from application.models.boats import Boat
from application.models.reservation import Reservation
from application.forms.reservationform import ReservationForm

@app.route("/reservation/", methods = ["GET"])
@login_required()
def reserve_boat():
    form = ReservationForm()
    if not ("admin" in current_user.roles() or "club" in current_user.roles()):
        del form.boats
    return render_template("reservations/show_reservationform.html", 
                            form = form, 
                            form_action = url_for("make_reservation"), 
                            button_text = "Reserve boat")

@app.route("/reservation/", methods = ["POST"])
@login_required()
def make_reservation():
    form = ReservationForm(request.form)

    validate_form(form, 
                    form_action = url_for("make_reservation"), 
                    button_text = "Reserve boat")

    if "admin" in current_user.roles() or "club" in current_user.roles():
        number_of_boats = form.boats.data
    else:
        count_users_reservations = Reservation.count_reserved_boats_for_user(datetime.now(), 
                                        datetime.now() + timedelta(days = 365),
                                        user_id = current_user.id)
        if count_users_reservations >= 4:
            return render_template("reservations/show_reservationform.html", 
                                    form = form, 
                                    form_action = url_for("make_reservation"), 
                                    button_text = "Reserve boat",  
                                    error = "You can only have 4 reservations")
        number_of_boats = 1

    starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    ending = datetime.combine(form.ending_date.data, form.ending_time.data)
    available_boats = Boat.available_boats(starting, ending)
    if len(available_boats) < number_of_boats:
        return render_template("reservations/show_reservationform.html", 
                                form = form, 
                                form_action = url_for("make_reservation"), 
                                button_text = "Reserve boat",  
                                error = "Not enough boats available for this time, only " +
                                    len(available_boats) + "boats available")
    
    reservation = Reservation(starting, ending, current_user.id)

    for i in range(number_of_boats):
        reservation.boats_reserved.append(Boat.query.get(available_boats[i]))
    
    db.session().add(reservation)
    db.session().commit()

    return redirect(url_for("calendar_index"))

@app.route("/reservation/<reservation_id>/", methods = ["GET"])
@login_required()
def show_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)

    if reservation.user_id != current_user.id or reservation.ending_time < datetime.now():
        return redirect(url_for("calendar_index"))

    form = ReservationForm(obj=reservation, boats = reservation.number_of_boats())
    if not "admin" in current_user.roles() or "club" in current_user.roles():
        del form.boats
        
    return render_template("reservations/show_reservationform.html",  
                            form = form,
                            form_action = url_for("modify_reservation", reservation_id=reservation_id),
                            button_text = "Save changes")

@app.route("/reservation/<reservation_id>/", methods = ["POST"])
@login_required()
def modify_reservation(reservation_id):
    form = ReservationForm(request.form)
    reservation = Reservation.query.get(reservation_id)

    if reservation.user_id != current_user.id or reservation.ending_time < datetime.now():
        return redirect(url_for("calendar_index"))

    validate_form(form, 
                    form_action = url_for("modify_reservation", reservation_id=reservation_id), 
                    button_text = "Save changes")

    if "admin" in current_user.roles() or "club" in current_user.roles():
        number_of_boats = form.boats.data
    else:
        number_of_boats = 1

    starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    ending = datetime.combine(form.ending_date.data, form.ending_time.data)
    available_boats = Boat.available_boats_for_changing_reservation(starting, ending, reservation.id)
    if len(available_boats) < number_of_boats:
        return render_template("reservations/show_reservationform.html", 
                                reservation = reservation, 
                                form = form,
                                form_action = url_for("modify_reservation", reservation_id=reservation_id),
                                button_text = "Save changes", 
                                error = "Not enough boats available for this time, only " +
                                    len(available_boats) + "boats available")
    
    reservation.update(starting, ending)
    reservation.boats_reserved = []

    for i in range(number_of_boats):
        reservation.boats_reserved.append(Boat.query.get(available_boats[i]))
    
    db.session().add(reservation)
    db.session().commit()

    return redirect(url_for("calendar_index"))

@app.route("/reservation/<reservation_id>/delete/", methods = ["POST"])
@login_required()
def delete_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)

    if reservation.user_id != current_user.id or reservation.ending_time < datetime.now():
        return redirect(url_for("calendar_index"))

    db.session().delete(reservation)
    db.session.commit()

    return redirect(url_for("calendar_index"))

def validate_form(form, form_action, button_text):
    if not ("admin" in current_user.roles() or "club" in current_user.roles()):
        del form.boats

    if not form.validate():
        return render_template("reservations/show_reservationform.html", 
                                form = form, 
                                form_action = form_action, 
                                button_text = button_text)

    starting = datetime.combine(form.starting_date.data, form.starting_time.data)
    ending = datetime.combine(form.ending_date.data, form.ending_time.data)
    message = validate_reservation_times(starting, ending)

    if not message == "Clear":
        return render_template("reservations/show_reservationform.html",
                                form = form, 
                                form_action = form_action, 
                                button_text = button_text,
                                error = message)

def validate_reservation_times(starting, ending):
    if starting < datetime.now():
        return "Starting time should be in the future"
    elif starting >= ending:
        return "Ending date or time should be after starting time"
    elif ending >= datetime.now() + timedelta(days = 365):
        return "Ending time should be within one year from now"
    else:
        return "Clear"