from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.players.models import Player

#Formi jolla luodaan uusi pelaaja, validointi sääntöinä tyhjät välit ja pituus
class PlayerForm(FlaskForm):

    def validate_player_tag(form, field):
        if " " in field.data:
            raise validators.ValidationError("Name can not contain empty spaces")

    player_tag = StringField("Player name", [validators.Length(min=3, max=20)])
    
    top = BooleanField("Top Lane")
    jgl = BooleanField("Jungle")
    mid = BooleanField("Mid Lane")
    adc = BooleanField("ADC")
    sup = BooleanField("Support")

    class Meta:
        csrf = False

class PlayerEditForm(FlaskForm):

    player = QuerySelectField(u'Player', query_factory=Player.get_own_players, get_label='player_tag')
    role = SelectField(u'Role', choices=[('1','Top'), ('2','Jungle'), ('3','Middle'),('4','ADC'),('5','Support')])
    play = BooleanField("Plays role")

    class Meta:
        csrf = False