from application import app, db
from flask import render_template, request, redirect, url_for
from application.players.models import Player

@app.route("/players/new/")
def players_form():
    return render_template("players/new.html")

@app.route("/players/", methods=["POST"])
def players_create():
    pl = Player(request.form.get("player_tag"))
    db.session().add(pl)
    db.session().commit()
    return redirect(url_for("players_index"))

@app.route("/players/", methods=["GET"])
def players_index():
    return render_template("players/list.html", players = Player.query.all())

@app.route("/players/<player_id>/", methods=["POST"])
def players_set(player_id):
    pl = Player.query.get(player_id)
    if request.form["btn"] == "Change top!":
        if pl.top == True:
            pl.top = False
            db.session().commit()
            return redirect(url_for("players_index"))
        if pl.top == False:
            pl.top = True
            db.session().commit()
            return redirect(url_for("players_index"))

    if request.form["btn"] == "Change jgl!":
        if pl.jgl == True:
            pl.jgl = False
            db.session().commit()
            return redirect(url_for("players_index"))
        if pl.jgl == False:
            pl.jgl = True
            db.session().commit()
            return redirect(url_for("players_index"))

    if request.form["btn"] == "Change mid!":
        if pl.mid == True:
            pl.mid = False
            db.session().commit()
            return redirect(url_for("players_index"))
        if pl.mid == False:
            pl.mid = True
            db.session().commit()
            return redirect(url_for("players_index"))

    if request.form["btn"] == "Change adc!":
        if pl.adc == True:
            pl.adc = False
            db.session().commit()
            return redirect(url_for("players_index"))
        if pl.adc == False:
            pl.adc = True
            db.session().commit()
            return redirect(url_for("players_index"))

    if request.form["btn"] == "Change sup!":
        if pl.sup == True:
            pl.sup = False
            db.session().commit()
            return redirect(url_for("players_index"))
        if pl.sup == False:
            pl.sup = True
            db.session().commit()
            return redirect(url_for("players_index"))
