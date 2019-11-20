from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.models.user import User
from application.forms.loginform import LoginForm

@app.route("/login/", methods = ["GET"])
def show_login():
    return render_template("login.html", form = LoginForm())

@app.route("/login/", methods = ["POST"])
def auth_login():
    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("login.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))  

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 