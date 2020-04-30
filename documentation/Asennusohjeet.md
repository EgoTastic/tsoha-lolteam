# LoL TeamBuilder asentaminen lokaalisti ja herokuun

## Lokaali asennus

Sovelluksen ajamiseen tarvitset koneellesi asennetuna valmiiksi
- [Python3 ohjelmointikielitulkin](https://www.python.org/downloads/)
- [pip -pakettiasentajan](https://pip.pypa.io/en/stable/)

### Ohjelman lataaminen

Voit ladata ohjelman githubista joko [suoralla latauksella githubista](https://github.com/EgoTastic/tsoha-lolteam) tai vaihtoehtoisesti konsolista git clone -komennolla.

### Riippuvuuksien asentaminen 

Sovelluksen vaatimien riippuvuuksien asennus suoriutuu komennolla: 

```
pip install -r requirements.txt
```

Aja komento kansion juuressa.

### Sovelluksen käynnistäminen

Käynnistä virtuaaliympäristö juuressa ajettavalla komennolla:

```
source venv/bin/activate
```

Tämän jälkeen voit käynnistää sovelluksen komennolla:

```
python3 run.py
```
Käskyn jälkeen sovellus käynnistyy lokaalisti ja pääset siihin käsiksi selaimestasi osoitteella http://127.0.0.1:5000/

Voit sammuttaa sovelluksen näppäimillä CTRL+C ja sammuttaa virtuaalympäristön deactivate -komennolla

### Admin-tilin lisääminen lokaalissa sovelluksessa

Admin tilien lisäämistä varten joudut luomaan suoraan tietokantaan tunnuksen. Tähän sopii esimerkiksi DB Browser for SQLite, tai jokin muu tietokannan muokkaamiseen sopiva ohjelma.
Voit luoda uuden tunnuksen SQL-käskyllä:

```
INSERT INTO account (name, username, password, role) VALUES ("haluttu_nimi", "haluttu_käyttäjänimi", "haluttu_salasana", "ADMIN")
```
Korvaa esimerkkikäskyyn haluamasi arvot joilla haluat luoda admin tunnuksen.

## Asennus Herokuun

- Lataa tiedostot kuten lokaalissa asennuksessa ohjeistettu
- [Luo itsellesi tunnus Heroku-palveluun](https://www.heroku.com/)
- [Lataa heroku koneellesi ja kirjaudu](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
- Luo itsellesi uusi applikaatio herokuun komennolla:

```
heroku create haluttu_sovellusnimi
```

- Onnistuneesta luomisesta saat linkin sovellukselle luotuun git ympäristöön
- Tämän jälkeen voit lisätä versionhallintaan tiedon herokusta

```
git remote add heroku linkki_herokugit_ympäristöön
```

- [Tämän jälkeen voit lähettää sovelluksen herokuun tavalliseen git -commit tapaan](https://help.github.com/en/github/managing-files-in-a-repository/adding-a-file-to-a-repository-using-the-command-line)

### PostgreSQL käyttöönotto

Kun olet saanut lähetettyä sovelluksen herokuun, sinun tarvitsee suorittaa seuraavat komennot:

```
heroku config:set HEROKU=1 -a ohjelmasi_nimi_herokussa
```

Tällä sovellus tietää, että se ajetaan Herokun ympäristössä. Tämän jälkeen seuraavalla komennolla saat luotua tietokannan:

```
heroku addons:add heroku-postgresql:hobby-dev -a ohjelmasi_nimi_herokussa
```
Nyt sovellus on käytettävissä herokussa normaaliin tapaan.

### Admin-tilin lisääminen Herokuun

Jotta voit lisätä admin tilin Herokuun, tarvitset yhteyden herokun postgresql omninaisuuteen seuraavilla komennoilla:

```
heroku pg:psql -a ohjelmasi_nimi_herokussa
```

Tämän jälkeen voit lisätä admin tilin itsellesi aiempaan tapaan:

```
INSERT INTO account (name, username, password, role) VALUES ("haluttu_nimi", "haluttu_käyttäjänimi", "haluttu_salasana", "ADMIN");
```

Saat katkaistua yhteyden herokuun postgresql -ominaisuuteen komennolla:
```
\q
```
Nyt pystyt kirjautumaan sisään Herokuun admin-tunnuksella.