from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import login_required, current_user

class Player(Base):
    #Tietokannan sisällön määrittely, arvotyypit, voiko olla tyhjä

    __tablename__ = "player"

    player_tag = db.Column(db.String(144), nullable=False)
   
    top = db.Column(db.Boolean, nullable=False)
    jgl = db.Column(db.Boolean, nullable=False)
    mid = db.Column(db.Boolean, nullable=False)
    adc = db.Column(db.Boolean, nullable=False)
    sup = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)


    #Uuden playerin luominen
    def __init__(self, player_tag):
        self.player_tag = player_tag
        self.top = False
        self.jgl = False
        self.mid = False
        self.adc = False
        self.sup = False


    @staticmethod
    def get_player_list():
        return Player.query

    @staticmethod
    def get_own_players():
        if current_user == None:
            id = 0
        else:
            id = current_user.id
        return Player.query.filter(Player.account_id == id)

    @staticmethod
    def get_players_noteam():
        stmt = text("SELECT player.player_tag, player.top, player.jgl, player.mid, player.adc, player.sup FROM Player LEFT JOIN teammate ON teammate.player = player.id WHERE player.id NOT IN (SELECT player FROM teammate WHERE player NOTNULL)")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            top = row[1] == 1
            jgl = row[2] == 1
            mid = row[3] == 1
            adc = row[4] == 1
            sup = row[5] == 1
            response.append({"tag":row[0], "top":top, "jgl":jgl, "mid":mid, "adc":adc, "sup":sup})
        return response