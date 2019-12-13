from flask import redirect, render_template, request, url_for
from flask_login import current_user
from datetime import datetime
from sqlalchemy import asc, desc

from application import app, db, login_required
from application.models.reservation import Reservation
from application.models.user import User

@app.route("/calendar/", methods = ["GET"])
def calendar_index():
    sort = "asc" if request.args.get("sort") == "asc" else "desc"
    order_by = "ending_time" if request.args.get("order_by") == "ending_time" else "starting_time"
    sort_fn = asc if sort == "asc" else desc
    order_by_time = Reservation.ending_time if order_by == "ending_time" else Reservation.starting_time

    return render_template("calendar.html", 
                            reservations = Reservation.query.order_by(sort_fn(order_by_time)).all(), 
                            current_time = datetime.now(),
                            sort_starting = "desc" if sort == "asc" or order_by != "starting_time" else "asc",
                            sort_ending = "desc" if sort == "asc" or order_by != "ending_time" else "asc", 
                            arrow_starting = "" if order_by != "starting_time" else "↓" if sort == "desc" else "↑",
                            arrow_ending = "" if order_by != "ending_time" else "↓" if sort == "desc" else "↑"
                            )

@app.route("/calendar/my_reservations", methods = ["GET"])
@login_required()
def users_reservations():
    sort = "asc" if request.args.get("sort") == "asc" else "desc"
    order_by = "ending_time" if request.args.get("order_by") == "ending_time" else "starting_time"
    sort_fn = asc if sort == "asc" else desc
    order_by_time = Reservation.ending_time if order_by == "ending_time" else Reservation.starting_time

    return render_template("calendar.html", 
                            reservations = Reservation.query.order_by(sort_fn(order_by_time)).filter_by(user_id = current_user.id), 
                            current_time = datetime.now(),
                            sort_starting = "desc" if sort == "asc" or order_by != "starting_time" else "asc",
                            sort_ending = "desc" if sort == "asc" or order_by != "ending_time" else "asc", 
                            arrow_starting = "" if order_by != "starting_time" else "↓" if sort == "desc" else "↑",
                            arrow_ending = "" if order_by != "ending_time" else "↓" if sort == "desc" else "↑"
                            )