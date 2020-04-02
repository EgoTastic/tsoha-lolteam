from flask_wtf import FlaskForm
from wtforms import SelectField, validators
from application import app, db
from sqlalchemy.sql import text
from application.players.models import Player
from wtforms.ext.sqlalchemy.fields import QuerySelectField

#Formi jolla lisätään teammate
class TeammateForm(FlaskForm):


    player = QuerySelectField(u'Player', query_factory=Player.get_player_list, get_label='player_tag')
    role = SelectField(u'Role', choices=[('1','Top'), ('2','Jungle'), ('3','Middle'),('4','ADC'),('5','Support')])

    class Meta:
        csrf = False
