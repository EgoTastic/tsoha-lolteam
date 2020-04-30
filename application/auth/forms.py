from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

#Login formin koostumus  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

#Rekisteröinti formin koostumus
class RegisterForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=12)])
    name = StringField("Name", [validators.Length(min=3, max=12)])
    password = PasswordField("Password", [validators.Length(min=3, max=12)])

    #Validaattorit inputille
    def validate_username(form, field):
        if " " in field.data:
            raise validators.ValidationError("Username can not contain empty spaces")

    def validate_name(form, field):
        if " " in field.data:
            raise validators.ValidationError("Name can not contain empty spaces")

    def validate_password(form, field):
        if " " in field.data:
            raise validators.ValidationError("Password can not contain empty spaces")


    class Meta:
        csrf = False
