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
def players_set_top(player_id):
    pl = Player.query.get(player_id)
    pl.top = True
    db.session().commit()
    return redirect(url_for("players_index"))

@app.route("/players/<player_id>/", methods=["POST"])
def players_set_jgl(player_id):
    pl = Player.query.get(player_id)
    pl.jgl = True
    db.session().commit()
    return redirect(url_for("players_index"))

@app.route("/players/<player_id>/", methods=["POST"])
def players_set_mid(player_id):
    pl = Player.query.get(player_id)
    pl.mid = True
    db.session().commit()
    return redirect(url_for("players_index"))

@app.route("/players/<player_id>/", methods=["POST"])
def players_set_adc(player_id):
    pl = Player.query.get(player_id)
    pl.adc = True
    db.session().commit()
    return redirect(url_for("players_index"))

@app.route("/players/<player_id>/", methods=["POST"])
def players_set_sup(player_id):
    pl = Player.query.get(player_id)
    pl.sup = True
    db.session().commit()
    return redirect(url_for("players_index"))
