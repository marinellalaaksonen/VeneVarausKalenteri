from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.models.user import User
from application.models.role import Role
from application.forms.loginform import LoginForm
from application.forms.registerform import RegisterForm

@app.route("/login/", methods = ["GET"])
def show_login():
    return render_template("auth/login.html", form = LoginForm())

@app.route("/login/", methods = ["POST"])
def auth_login():
    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/login.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))  

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/register/", methods = ["GET"])
def register_user():
    return render_template("auth/register.html", form = RegisterForm())

@app.route("/auth/register/", methods = ["POST"])
def create_user():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form)

    user = User(form.name.data, form.username.data, form.password.data, "test")

    user.users_roles.append(Role.query.filter_by(name = "skipper").first())

    db.session.add(user)
    db.session.commit()

    login_user(user)
    return redirect(url_for("index"))