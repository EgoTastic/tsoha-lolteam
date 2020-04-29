from application import app, db, login_required

from flask_login import current_user
from flask import render_template, request, redirect, url_for

from application.players.models import Player
from application.players.forms import PlayerForm, PlayerEditForm

#Uuden pelaajan luomiseen render käsky, ei voi käyttää ilman kirjautumista
@app.route("/players/new/")
@login_required
def players_form():
    return render_template("players/new.html", form = PlayerForm())

@app.route("/players/teamless/")
@login_required
def teamless_players():
    return render_template("players/teamless.html", noteamplayers = Player.get_players_noteam())

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
    return render_template("players/list.html", form = PlayerEditForm() , players = Player.query.order_by(Player.id).all(), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/top", methods=["GET"])
@login_required
def players_index_top():
    return render_template("players/list.html", form = PlayerEditForm(), players = Player.query.filter(Player.top == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/jgl", methods=["GET"])
@login_required
def players_index_jgl():
    return render_template("players/list.html", form = PlayerEditForm(), players = Player.query.filter(Player.jgl == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/mid", methods=["GET"])
@login_required
def players_index_mid():
    return render_template("players/list.html", form = PlayerEditForm(), players = Player.query.filter(Player.mid == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/adc", methods=["GET"])
@login_required
def players_index_adc():
    return render_template("players/list.html", form = PlayerEditForm(), players = Player.query.filter(Player.adc == True), own_players = Player.query.filter(Player.account_id == current_user.id))

@app.route("/players/sup", methods=["GET"])
@login_required
def players_index_sup():
    return render_template("players/list.html", form = PlayerEditForm(), players = Player.query.filter(Player.sup == True), own_players = Player.query.filter(Player.account_id == current_user.id))


#Statuksen vaihto tai pelaajan poisto napin painolla


@app.route("/players/edit", methods=["POST"])
@login_required
def player_edit():
    form = PlayerEditForm(request.form)
    if form.player.data == None:
        return redirect(url_for("players_index"))
    player = form.player.data.id
    role = form.role.data
    status = form.play.data
    if request.form["btn"] == "Change":
        if role == "1":
            db.session().query(Player).filter(Player.id == player).update({"top": status})
        if role == "2":
            db.session().query(Player).filter(Player.id == player).update({"jgl": status})
        if role == "3":
            db.session().query(Player).filter(Player.id == player).update({"mid": status})
        if role == "4":
            db.session().query(Player).filter(Player.id == player).update({"adc": status})
        if role == "5":
            db.session().query(Player).filter(Player.id == player).update({"sup": status})
    if request.form["btn"] == "Remove player":
        db.session().query(Player).filter(Player.id == player).delete()

    db.session().commit()
    return redirect(url_for("players_index"))