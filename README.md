<h1> LoL-tiimien koostaminen ja tiimikavereiden etsiminen </h1>
  
  [Linkki herokuun jossa appi on deployattu](https://tsohateambuilder.herokuapp.com)  
  
  Testitunnukset: username = username, password = password
    
  [Linkki nykyiseen tietokaaviopohjaan](https://github.com/EgoTastic/tsoha-lolteam/blob/master/documentation/Tietokantakaavio%20v2.pdf)
  
  <h2>Applikaation tavoite</h2>
  
<p> Tarkoitus luoda sovellus, jolla käyttäjä voi luoda itselleen profiilin ja määritellä preferoimansa rooli tiimissä (top/jungle/mid/adc/support)  
Sovelluksessa voi luoda oman tunnuksen, jonka avulla voi määritellä itselleen oman pelaajatägin mitä käyttää League of Legendsissä, sen lisäksi voi määrittää mitä eri pelin rooleja pelaa. Sovelluksessa voi luoda tiimejä ja täyttää tiimin 5 eri roolia pelaajilla. Tiimin puuttuvia rooleja voi etsiä pelaajien joukosta, etsimällä kyseistä roolia pelaavia pelaajia. Toiminnallisuuteen voi mahdollisesti lisätä myös filtteröintiä pelaajan ränkin perusteella tai vastaavaa.  
  
  
  Tauluja on neljä Player, jossa on player_id, login_name, player_tag (eli LoL käyttäjänimi), salasana, roolipreferenssit ja hakeeko tiimiä, sekä minkä tilin luoma player on. Account taulussa on id, luonti ja muokkaus pvm, nimi, käyttäjätunnus, salasana ja relaatio playeriin. Team taulussa on tiimin id sekä nimi. Viimeisenä liitostaulu pelaajien ja tiimien välillä mikä kertoo myös roolin tiimissä. Mahdollistaa useamman samaa roolia pelaavan samassa tiimissä</p>

<h2>2 viikon aikana toteutetut asiat V0.00.02</h2>
<ul>
<li>perustoiminnallisuus, sisältäen pelaajan lisäämisen, listaamisen, muokkaamisen sekä valikon</li>
<li>Tarvittava taulu, joka nykyisessä muodossa sisältää vain pelaajan id, muokkaustiedot, player tägin, sekä tiedot pelaako mitä rooleja</li>
<li>Roolien true/false arvoja voi vaihtaa napista listauksessa</li>
<li>Tietokanta tauluja mietitty hieman uudestaan vastaamaan kurssin tarkoitusta (suurimpana lisäys many-to-many taulu)</li>
</ul>

<h2>User Story</h2>
<ul>
<li>Käyttäjänä voin lisätä pelaajatägin ja luodessa valita mitä rooleja pelaa</li>
<li>Käyttäjä voi rekisteröidä itselleen tunnuksen</li>
<li>Käyttäjä ei pääse muuhun kuin kirjautumiseen sekä rekisteröintiin käsiksi jos ei ole kirjautunut sisään</li>
<li>Käyttäjä voi muuttaa playerin rooleja</li>
<li>Käyttäjä voi listata nykyiset playerit</li>
<li>Käyttäjä voi poistaa playerin</li>
<li>Käyttäjä voi kirjautua ulos</li>
<ul>
