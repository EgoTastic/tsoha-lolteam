from application import app, db

from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text
from application.teams.models import Team
from application.teams.forms import TeamForm
from application.teammates.forms import TeammateForm
from application.teammates.models import Teammate
from application.players.models import Player

@app.route("/teams/new")
@login_required
def teams_form():
    return render_template("teams/new.html", form = TeamForm())

#Tiimin luominen
@app.route("/teams/", methods=["POST"])
@login_required
def teams_create():
    form = TeamForm(request.form)
    if not form.validate():
        return render_template("teams/new.html", form = form)

    tm = Team(form.name.data)
    tm.account_id = current_user.id
    db.session().add(tm)
    db.session().commit()

    
    team_id = tm.id
    mate1 = Teammate(team_id)
    mate1.role = 1
    mate2 = Teammate(team_id)
    mate2.role = 2  
    mate3 = Teammate(team_id)
    mate3.role = 3  
    mate4 = Teammate(team_id)
    mate4.role = 4  
    mate5 = Teammate(team_id)
    mate5.role = 5  
    
    db.session().add(mate1)
    db.session().add(mate2)
    db.session().add(mate3)
    db.session().add(mate4)
    db.session().add(mate5)

    db.session().commit()

    return redirect(url_for("teams_index"))

@app.route("/teams/", methods=["GET"])
@login_required
def teams_index():
    
    teamslist = []
    ownlist = []
    statement = text("SELECT team.name, team.id FROM team WHERE team.account_id = :id").params(id = current_user.id)
    result = db.engine.execute(statement)
    for row in result:
        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 1) AND teammate.team_id = :id2 AND teammate.role = 1").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        top = "Free"
        for row2 in result2:
            top = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 2) AND teammate.team_id = :id2 AND teammate.role = 2").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        jgl = "Free"
        for row2 in result2:
            jgl = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 3) AND teammate.team_id = :id2 AND teammate.role = 3").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        mid = "Free"
        for row2 in result2:
            mid = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 4) AND teammate.team_id = :id2 AND teammate.role = 4").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        adc = "Free"
        for row2 in result2:
            adc = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 5) AND teammate.team_id = :id2 AND teammate.role = 5").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        sup = "Free"
        for row2 in result2:
            sup = row2[0]
     
        ownlist.append({"name":row[0], "top":top, "jgl":jgl, "mid":mid, "adc":adc, "sup":sup, "id":row[1]})

    statement = text("SELECT team.name, team.id FROM team")
    result = db.engine.execute(statement)
    for row in result:
        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 1) AND teammate.team_id = :id2 AND teammate.role = 1").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        top = "Free"
        for row2 in result2:
            top = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 2) AND teammate.team_id = :id2 AND teammate.role = 2").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        jgl = "Free"
        for row2 in result2:
            jgl = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 3) AND teammate.team_id = :id2 AND teammate.role = 3").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        mid = "Free"
        for row2 in result2:
            mid = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 4) AND teammate.team_id = :id2 AND teammate.role = 4").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        adc = "Free"
        for row2 in result2:
            adc = row2[0]

        statement2 = text("SELECT player.player_tag FROM teammate, player WHERE player.id = (SELECT teammate.player FROM teammate WHERE teammate.team_id = :id1 AND teammate.role = 5) AND teammate.team_id = :id2 AND teammate.role = 5").params(id1 = row[1], id2=row[1])
        result2 = db.engine.execute(statement2)
        sup = "Free"
        for row2 in result2:
            sup = row2[0]
     
        teamslist.append({"name":row[0], "top":top, "jgl":jgl, "mid":mid, "adc":adc, "sup":sup})
        

    return render_template("teams/list.html", teams = teamslist, own_teams = ownlist, form = TeammateForm())

@app.route("/teams/edit", methods=["POST"])
@login_required
def team_edit():
    form = TeammateForm(request.form)
    team = form.team.data.id
    role = form.role.data
    player = form.player.data.id

    if request.form["btn"] == "Remove team":
        db.session().query(Teammate).filter(Teammate.team_id == team).delete()
        db.session().query(Team).filter(Team.id == team).delete()
        db.session().commit()

    if request.form["btn"] == "Add player":
        db.session().query(Teammate).filter(Teammate.team_id == team, Teammate.role == role).update({"player": player})
        db.session().commit()

    if request.form["btn"] == "Remove role":
        db.session().query(Teammate).filter(Teammate.team_id == team, Teammate.role == role).update({"player": None})
        db.session().commit()
    return redirect(url_for("teams_index"))
