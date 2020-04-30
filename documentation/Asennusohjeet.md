# LoL TeamBuilder asentaminen lokaalisti ja herokuun

## Lokaali asennus

Sovelluksen ajamiseen tarvitset koneellesi asennetun Python3 ohjelmointikielitulkin sekä pip -pakettiasentajan.

### Ohjelman lataaminen

Voit ladata ohjelman githubista joko suoralla latauksella tai vaihtoehtoisesti konsolista git clone -komennolla

### Riippuvuuksien asentaminen 

Voit asentaa sovelluksen vaatimat riippuvuudet seuraavalla komennolla: 

'''
pip install -r requirements.txt
'''

Aja komento kansion juuressa.

### Sovelluksen käynnistäminen

Käynnistä virtuaaliympäristö juuressa ajettavalla komennolla:

'''
source venv/bin/activate
'''

Tämän jälkeen voit käynnistää sovelluksen komennolla:

'''
python3 run.py
'''

Voit sammuttaa sovelluksen näppäimillä CTRL+C ja sammuttaa virtuaalympäristön "deactivate" -komennolla

### Admin-tilin lisääminen lokaalissa sovelluksessa

Admin tilien lisäämistä varten joudut luomaan suoraan tietokantaan tunnuksen. Tähän sopii esimerkiksi DB Browser for SQLite, tia jokin muu tietokannan muokkaamiseen sopiva ohjelma.
Voit luoda uuden tunnuksen SQL-käskyllä:

'''
INSERT INTO account (name, username, password, role) VALUES ("haluttu_nimi", "haluttu_käyttäjänimi", "haluttu_salasana", "ADMIN")
'''

## Asennus Herokuun

- Lataa tiedostot
- Luo itsellesi tunnus Heroku-palveluun.
- Luo heroku paikka herokuun komennolla:

'''
heroku create haluttu_sovellusnimi
'''

- Onnistuneesta luomisesta saat linkin sovellukselle luotuun git ympäristöön
- Tämän jälkeen voit lisätä versionhallintaan tiedon herokusta

'''
git remote add heroku linkki_herokugit_ympäristöön
'''

- Tämän jälkeen voit lähettää sovelluksen herokuun tavalliseen git -commit tapaan

### PostgreSQL käyttöönotto

Kun olet saanut lähetettyä sovelluksen herokuun, sinun tarvitsee suorittaa seuraavat komennot:

'''
heroku config:set HEROKU=1 -a ohjelmasi_nimi_herokussa
'''

Tällä sovellus tietää, että se ajetaan Herokun ympäristössä. Tämän jälkeen seuraavalla komennolla saat luotua tietokannan:

'''
heroku addons:add heroku-postgresql:hobby-dev -a ohjelmasi_nimi_herokussa
'''

### Admin-tilin lisääminen Herokuun

Jotta voit lisätä admin tilin Herokuun, tarvitset yhteyden herokun postgresql omninaisuuteen seuraavilla komennoilla:

'''
heroku pg:psql -a ohjelmasi_nimi_herokussa
'''

Tämän jälkeen voit lisätä admin tilin itsellesi aiempaan tapaan:

'''
INSERT INTO account (name, username, password, role) VALUES ("haluttu_nimi", "haluttu_käyttäjänimi", "haluttu_salasana", "ADMIN")
'''