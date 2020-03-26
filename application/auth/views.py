from application import app, db

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

#Kirjautuminen
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))   

#Uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

#Rekisteröinti render käsky
@app.route("/auth/register")
def register_form():
    return render_template("/auth/register.html", form = RegisterForm())

#Uuden käyttäjän luonti
@app.route("/auth/", methods=["POST"])
def account_create():
    form = RegisterForm(request.form)
    
    if not form.validate():
        return render_template("auth/register.html", form = form)

    acc = User(form.name.data, form.username.data, form.password.data)
    acc.name = form.name.data
    acc.password = form.password.data

    db.session().add(acc)
    db.session().commit()

    return redirect(url_for("players_index"))
