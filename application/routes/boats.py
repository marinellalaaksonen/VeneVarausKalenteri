from application import app, db
from flask import redirect, render_template, request, url_for
from application.models.boats import Boat

@app.route("/boats/", methods=["GET"])
def boats_index():
    return render_template("boats/list_boats.html", boats = Boat.query.all())

@app.route("/boats/add/", methods=["GET"])
def add_boat():
    return render_template("boats/add_boat.html")

@app.route("/boats/<boat_id>/", methods=["GET"])
def show_boat(boat_id):
    return render_template("boats/modify_boat.html", boat = Boat.query.get(boat_id))

@app.route("/boats/<boat_id>/delete/", methods=["POST"])
def delete_boat(boat_id):
    print("pöö")
    boat = Boat.query.get(boat_id)
    db.session().delete(boat)
    db.session().commit()
  
    return redirect(url_for("boats_index"))

@app.route("/boats/<boat_id>/", methods=["POST"])
def modify_boat(boat_id):
    boat = Boat.query.get(boat_id)
    boat.name = request.form.get("name")
    db.session().commit()
  
    return redirect(url_for("boats_index"))

@app.route("/boats/", methods=["POST"])
def create_boat():
    boat = Boat(request.form.get("name"), "purjevene", "J/80")

    db.session().add(boat)
    db.session().commit()

    return redirect(url_for("boats_index"))

#@app.route("/boats/modify/")