from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class PlayerForm(FlaskForm):

    def validate_player_tag(form, field):
        if " " in field.data:
            raise validators.ValidationError("Name can not contain empty spaces")

    player_tag = StringField("Player name", [validators.Length(min=3)])
    
    top = BooleanField("Top Lane")
    jgl = BooleanField("Jungle")
    mid = BooleanField("Mid Lane")
    adc = BooleanField("ADC")
    sup = BooleanField("Support")

    class Meta:
        csrf = False
