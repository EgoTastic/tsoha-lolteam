from application import db
from application.models import Base
from sqlalchemy.sql import text
from flask_login import current_user

class Team(Base):
    
    #Tietokannan sisältö
    name = db.Column(db.String(144), nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
        
    #Uuden tiimin luominen
    def __init__(self, name):
        self.name = name

    #Nykyisen käyttäjän id-palautus
    @staticmethod
    def get_own_teams():
        if current_user == None:
            id = 0
        else:
            id = current_user.id
        return Team.query.filter(Team.account_id == id)

    #Tiimien ja niiden omistajien listaus
    @staticmethod
    def team_owners():
        stmt = text("SELECT team.name, account.username FROM team LEFT JOIN account ON team.account_id = account.id ORDER BY team.name")

        res = db.engine.execute(stmt)
        result = []
        for row in res:
            result.append({"name":row[0], "owner":row[1]})
        return result