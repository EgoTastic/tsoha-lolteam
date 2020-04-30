from application import db

#Abstrakti luokka mitä muut luokat noudattavat (Sisältää primääriavaimen ja päivämäärien lisäyksen tietokantaan)
class Base(db.Model):
   
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate = db.func.current_timestamp())
