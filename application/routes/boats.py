from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.models.boats import Boat
from application.forms.boatform import BoatForm

@app.route("/boats/", methods=["GET"])
def boats_index():
    return render_template("boats/list_boats.html", boats = Boat.query.all())

@app.route("/boats/add/", methods=["GET"])
@login_required
def add_boat():
    return render_template("boats/add_boat.html", form = BoatForm())

@app.route("/boats/<boat_id>/", methods=["GET"])
@login_required
def show_boat(boat_id):
    boat = Boat.query.get(boat_id)
    return render_template("boats/modify_boat.html", boat = boat,  form = BoatForm(obj=boat))

@app.route("/boats/<boat_id>/delete/", methods=["POST"])
@login_required
def delete_boat(boat_id):
    boat = Boat.query.get(boat_id)
    db.session().delete(boat)
    db.session().commit()
  
    return redirect(url_for("boats_index"))

@app.route("/boats/<boat_id>/", methods=["POST"])
@login_required
def modify_boat(boat_id):
    form = BoatForm(request.form)
    boat = Boat.query.get(boat_id)

    if not form.validate():
        return render_template("boats/modify_boat.html", boat = boat, form = form)

    boat.name = form.name.data
    db.session().commit()
  
    return redirect(url_for("boats_index"))

@app.route("/boats/", methods=["POST"])
@login_required
def create_boat():
    form = BoatForm(request.form)

    if not form.validate():
        return render_template("boats/add_boat.html", form = form)

    boat = Boat(form.name.data, "purjevene", "J/80")

    db.session().add(boat)
    db.session().commit()

    return redirect(url_for("boats_index"))