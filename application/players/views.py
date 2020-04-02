from application import app, db

from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for

from application.players.models import Player
from application.players.forms import PlayerForm

#Uuden pelaajan luomiseen render käsky, ei voi käyttää ilman kirjautumista
@app.route("/players/new/")
@login_required
def players_form():
    return render_template("players/new.html", form = PlayerForm())

#Pelaajan luominen
@app.route("/players/", methods=["POST"])
def players_create():
    form = PlayerForm(request.form)

    if not form.validate():
        return render_template("players/new.html", form = form)

    pl = Player(form.player_tag.data)
    pl.account_id = current_user.id
    pl.top = form.top.data
    pl.jgl = form.jgl.data
    pl.mid = form.mid.data
    pl.adc = form.adc.data
    pl.sup = form.sup.data

    db.session().add(pl)
    db.session().commit()

    return redirect(url_for("players_index"))

#Pelaajalistan tulostus redirect
@app.route("/players/", methods=["GET"])
@login_required
def players_index():
    return render_template("players/list.html", players = Player.query.all(), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/top", methods=["GET"])
@login_required
def players_index_top():
    return render_template("players/list.html", players = Player.query.filter(Player.top == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/jgl", methods=["GET"])
@login_required
def players_index_jgl():
    return render_template("players/list.html", players = Player.query.filter(Player.jgl == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/mid", methods=["GET"])
@login_required
def players_index_mid():
    return render_template("players/list.html", players = Player.query.filter(Player.mid == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/adc", methods=["GET"])
@login_required
def players_index_adc():
    return render_template("players/list.html", players = Player.query.filter(Player.adc == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/sup", methods=["GET"])
@login_required
def players_index_sup():
    return render_template("players/list.html", players = Player.query.filter(Player.sup == True), own_players = Player.query.filter(Player.account_id == current_user.id))


#Statuksen vaihto tai pelaajan poisto napin painolla


@app.route("/players/<player_id>/", methods=["POST"])
@login_required
def players_set(player_id):
    pl = Player.query.get(player_id)
    print(player_id)
    if request.form["btn"] == "Remove player":
        db.session().delete(pl)
        db.session().commit()
        return redirect(url_for("players_index"))
        
    if request.form["btn"] == "Change top!":
        if pl.top == True:
            pl.top = False
            db.session().commit()
            return redirect(url_for("players_index"))

        if pl.top == False:
            pl.top = True
            db.session().commit()
            return redirect(url_for("players_index"))
    print(player_id)
    if request.form["btn"] == "Change jgl!":
        if pl.jgl == True:
            pl.jgl = False
            db.session().commit()
            return redirect(url_for("players_index"))

        if pl.jgl == False:
            pl.jgl = True
            db.session().commit()
            return redirect(url_for("players_index"))

    print(player_id)
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
