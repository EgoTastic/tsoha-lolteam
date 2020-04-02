from flask_wtf import FlaskForm
from wtforms import StringField, validators

#Formi jolla voi luoda uuden tiimin
class TeamForm(FlaskForm):
    
    name = StringField("Team name", [validators.Length(min=3, max=12)])
    
    class Meta:
        csrf = False
