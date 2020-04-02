from application import db
from application.models import Base

class Team(Base):
    
    #Tietokannan sisältö
    name = db.Column(db.String(144), nullable = False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)
        
    #Uuden tiimin luominen
    def __init__(self, name):
        self.name = name
