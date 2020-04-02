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