from application import db
from application.models import Base
from flask_login import login_required, current_user

class Team(Base):
    
    #Tietokannan sisältö
    name = db.Column(db.String(144), nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
        
    #Uuden tiimin luominen
    def __init__(self, name):
        self.name = name


    @staticmethod
    def get_own_teams():
        if current_user == None:
            id = 0
        else:
            id = current_user.id
        return Team.query.filter(Team.account_id == id)