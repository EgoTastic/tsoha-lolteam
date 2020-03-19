<h1> LoL-tiimien koostaminen ja haasteiden heittäminen kaveriporukassa  </h1>
  
  [Linkki herokuun jossa appi on deployattu](https://tsohateambuilder.herokuapp.com)
  
  <h2>Applikaation tavoite</h2>
  
<p> Tarkoitus luoda sovellus, jolla käyttäjä voi luoda itselleen profiilin ja määritellä preferoimansa rooli tiimissä (top/jungle/mid/adc/support)  
Sovelluksessa voi lisätä itsensä tiimiin, etsien esim tiimejä joista puuttuu pelaaja itse preferoimasta roolista, samalla taas tiimille voi etsiä pelaajia, jotka preferoivat juuri kyseistä roolia
Haasteita voi heittää tiimiltä tiimille, kunhan ne ovat täynnä, haasteelle määritellään pvm ja samalla myäs tulokselle oma kohta, jonka admin voi päivittää todisteiden valossa.  
Tauluja on kolme, yksi pelaajalle jossa on pelaajan tagi, id sekä preferoitu rooli. Joukkue taulussa on taas joukkueen id, nimi ja 5 kohtaa eri rooleille jotka ovat tyhjänä null tai sitten pelaajan_id. Haaste taulussa taas on oma id, joukkueiden id (eli kaksi joukkuetta), peli pvm ja tulos. </p>

<h2>2 viikon aikana toteutetut asiat V0.00.02</h2>
<ul>
<li>perustoiminnallisuus, sisältäen pelaajan lisäämisen, listaamisen, muokkaamisen sekä valikon</li>
<li>Tarvittava taulu, joka nykyisessä muodossa sisältää vain pelaajan id, muokkaustiedot, player tägin, sekä tiedot pelaako mitä rooleja</li>
<li>Roolien true/false arvoja voi vaihtaa napista listauksessa</li>
<li>Tietokanta tauluja mietitty hieman uudestaan vastaamaan kurssin tarkoitusta (suurimpana lisäys many-to-many taulu)</li>
</ul>

<h2>User Story</h2>
<p>Käyttäjänä voin lisätä pelaajatägin, jonka jälkeen voin valita itselleni sopivat roolit joita voin pelata LoLissa</p>
