# League of Legends TeamBuilder
  
  [Linkki herokuun jossa appi on deployattu](https://tsohateambuilder.herokuapp.com)  
  
  Testitunnukset: 
  
  Normaali käyttäjä
  ```
  username = username, password = password
  ```
  Admin käyttäjä
  ```
  username = adminstrator, password = password
  ```
  [Linkki nykyiseen tietokantakaavioon](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/Tietokantakaavio%20v4.png)
  
  [Linkki user storyyn](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/User%20Storyt.md)
  
  [Linkki asennusohjeisiin](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/Asennusohjeet.md)
  
  [Linkki käyttöohjeisiin](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/Kayttoohjeet.md)
  
## Applikaatio lyhyesti
  
Sovellus mahdollistaa pelikavereiden ja tiimien etisimisen sekä koostamisen. 
Sovelluksessa voi luoda oman tunnuksen, jonka avulla voi määritellä itselleen omat tilit mitä käyttää League of Legendsissä, sen lisäksi voi määrittää mitä eri pelin rooleja pelaa. 
Voit luoda tiimejä ja täyttää tiimin 5 eri roolia pelaajilla ja tiimin puuttuvia rooleja voi etsiä pelaajien joukosta, etsimällä kyseistä roolia pelaavia pelaajia. 
  
## Tietokantarakenne

- Account taulussa on id, luonti ja muokkaus pvm, nimi, käyttäjätunnus, salasana, rooli ja relaatio playeriin. 
- Tauluja on neljä Player, jossa on player_id, login_name, player_tag (eli LoL käyttäjänimi), salasana, roolipreferenssit ja hakeeko tiimiä, sekä minkä tilin luoma player on. 
- Team taulussa on tiimin id sekä nimi. 
- Viimeisenä liitostaulu pelaajien ja tiimien välillä mikä kertoo myös roolin tiimissä.
[Linkki nykyiseen tietokantakaavioon](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/Tietokantakaavio%20v4.png)
[Tietokannan CREATE TABLE komennot](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/taulujenluonti.md)

## Projektin edistyminen

### 7 viikon aikana toteutetut asiat V0.00.07
- Listitty kaikki löydetyt ongelmat sekä lokaalista että herokusta
- Lisätty kaksi yhteenvetokyselyä, toinen pelaajista joilla ei tiimiä ja toinen tiimeistä ja niiden omistajista
- Tileillä nyt kahta eri tasoa, admin ja user. Erona se että vain admin näkee tiimien omistajatilit
- Dokumentaatiota edistetty loppuun

### 5 ja 6 viikon aikana ei edistymistä

### 4 viikon aikana toteutetut asiat V0.00.04

- liitostaulu teammates lisätty, yhdistää pelaajan tiimiin ja ilmaisee roolin
- abstrakti luokka toteutettu
- pelaajalistausta muutettu niin, että käyttäjä näkee myös erillisen listauksen omista pelaajista, joita voi muokata (roolin vaihto sekä pelaajan poisto)
- tiimilistausta muutettu samalla tavalla, muokkausmahdollisuuksissa on pelaajan lisäys rooliin, poistaminen sekä tiimin poistaminen kokonaan
- yhteenvetokyseyä käytetty laajemmin tiimien pelaajien listaukseen
- raa'at sql kyselyt toteutettu parametreilla
- bootsrapilla muokattu ulkoasua (alkeellisesti)

### 3 viikon aikana toteutetut asiat V0.00.03

- Muutettu käyttämään wtformia
- herokussa siirrytty postresql käyttöön
- uusi taulu tilejä varten
- kirjautuminen lisätty ja sivulta piilotettu osia jos ei ole kirjautunut
- rekisteröinti lisätty
- uutta pelaajaa luodessa voi etukäteen määritellä roolit, ilman että ne joutuu muuttaa jälkikäteen
- player taulukolle täysi CRUD, tässä lisättiin playerin poisto
- päätä taottu seinään


### 2 viikon aikana toteutetut asiat V0.00.02

- perustoiminnallisuus, sisältäen pelaajan lisäämisen, listaamisen, muokkaamisen sekä valikon
- Tarvittava taulu, joka nykyisessä muodossa sisältää vain pelaajan id, muokkaustiedot, player tägin, sekä tiedot pelaako mitä rooleja
- Roolien true/false arvoja voi vaihtaa napista listauksessa
- Tietokanta tauluja mietitty hieman uudestaan vastaamaan kurssin tarkoitusta (suurimpana lisäys many-to-many taulu)

  
