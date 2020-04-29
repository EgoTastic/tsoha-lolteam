from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

#Jos herokussa, käytä niiden paikallista db, muuten käytä omaa polkua, modifications false asetuksen puute kaataa kaiken
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///players.db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Login tarpeet
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


from functools import wraps

def login_required(_func=None, *, role="ANY"):
    print("loggari000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            
            if not (current_user and current_user.is_authenticated):
                
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))
            print(acceptable_roles)
            if role not in acceptable_roles:
                print("00000000000000000000000000000000000000000000000000000000000000000")
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)



from application import views

from application.players import models
from application.players import views

from application.auth import models
from application.auth import views

from application.teams import models
from application.teams import views

from application.teammates import models

from application.auth.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Luo tietokanta jos sitä ei ole
try:
    db.create_all()
except:
    pass
