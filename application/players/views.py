from application import app, db
from flask import render_template, request, redirect, url_for
from application.players.models import Player
from application.players.forms import PlayerForm

@app.route("/players/new/")
def players_form():
    return render_template("players/new.html", form = PlayerForm())

@app.route("/players/", methods=["POST"])
def players_create():
    form = PlayerForm(request.form)

    if not form.validate():
        return render_template("players/new.html", form = form)

    pl = Player(form.player_tag.data)
    pl.top = form.top.data
    pl.jgl = form.jgl.data
    pl.mid = form.mid.data
    pl.adc = form.adc.data
    pl.sup = form.sup.data

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
