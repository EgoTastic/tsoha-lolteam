from application import app

#Jos heroku menee rikki niin alla olevat korjaa, ehkä...
#app.logger.addHandler(logging.StreamHandler(sys.stdout))
#app.logger.setLevel(logging.ERROR)



if __name__ == '__main__':
    #Ajettu debug tilassa
    app.run(debug=True)
