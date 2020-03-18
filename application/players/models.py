from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    player_tag = db.Column(db.String(144), nullable=False)
   
    top = db.Column(db.Boolean, nullable=False)
    jgl = db.Column(db.Boolean, nullable=False)
    mid = db.Column(db.Boolean, nullable=False)
    adc = db.Column(db.Boolean, nullable=False)
    sup = db.Column(db.Boolean, nullable=False)

    def __init__(self, player_tag):
        self.player_tag = player_tag
        self.role_top = False
        self.role_jgl = False
        self.role_mid = False
        self.role_adc = False
        self.role_sup = False
