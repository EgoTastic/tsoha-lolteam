from application import db
from application.models import Base
from sqlalchemy.sql import text
from application.teams.models import Team

class Teammate(Base):
    #Tietokannan sisällön määrittely, arvotyypit ja voiko olla tyhjä

    __tablename__ = "teammate"
    
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable = False)
    role = db.Column(db.Integer)
    player = db.Column(db.Integer, db.ForeignKey('player.id'), nullable = True)

    #Uusi tiimikaveri
    def __init__(self, id):
        self.team_id = id
