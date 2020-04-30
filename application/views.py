from flask import render_template
from application import app

#Etusivun rendausohje
@app.route("/")
def index():
    return render_template("index.html")
