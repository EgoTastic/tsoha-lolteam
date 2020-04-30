# User Story

## tiliaiheiset

Tavallisena käyttäjänä voin:
- luoda itselleni tunnuksen (määritellen usernamen, namen ja salasanan)
```
INSERT INTO account (name, username, password) VALUES (?,?,?)
```
- kirjautua tiedoillani sisään, jolloin pääsen käsiksi sovellukseen sisään

## pelaajaaiheiset
Tavallisena käyttäjänä voin:
- luoda uuden pelaajan kertoen nimen ja luodessa valita etukäteen roolit joita pelaa
```
INSERT INTO player (player_tag, top, jgl, mid, adc, sup, account_id) VALUES (?,?,?,?,?,?,?)
```
- nähdä pelaajalistauksen ja pelaajien roolipreferensseistä
```
SELECT player_tag, top, jgl, mid, adc, sup FROM player
```
- nähdä listauksen omista pelaajistaan ja niille asetetut roolipreferenssit
```
SELECT player_tag, top, jgl, mid, adc, sup FROM player where account_id = ?
```
- poistaa oman pelaajani
```
DELETE player WHERE id = ?
```
- muokata omien pelaajieni roolipreferenssejä
```
UPDATE player SET ? = ?
```
- listata ne pelaajat, jotka eivät ole mukana missään tiimissä
```
SELECT player.player_tag, player.top, player.jgl, player.mid, player.adc, player.sup FROM Player LEFT JOIN teammate ON teammate.player = player.id WHERE player.id NOT IN (SELECT player FROM teammate WHERE player NOTNULL)
```

## tiimiaiheiset
Tavallisena käyttäjänä voin:

- luoda uuden tiimin kertoen nimen
```
INSERT INTO team (name, account_id) VALUES (?,?)
```
- nähdä tiimilistauksen ja niihin asetetuista rooleista
```
SELECT team.name, player.player_tag, player.player_tag, player.player_tag, player.player_tag, player.player_tag FROM teammates LEFT JOIN teammates.player = player.id LEFT JOIN teammates.team = team.id
```
- nähdä listauksen omista tiimeistäni ja sen rooleihin liitetyistä pelaajista
```
SELECT team.name, player.tag, player.tag AS p1, player.tag AS p2, player.tag AS p3, player.tag AS p4, player.tag AS p5 FROM teammates LEFT JOIN teammates.player = player.id LEFT JOIN teammates.team = team.id WHERE team.account_id = ?
```
- poistaa oman tiimini
```
DELETE team WHERE id = ?
```
- lisätä tiimiini valitsemaani rooliin pelaajan
```
UPDATE team SET ? = ?
```
- poistaa tiimistäni pelaajan
```
UPDATE team SET ? = NULL
```

## adminille rajoitettu
Admin-käyttäjänä voin nähdä listauksen tiimeistä ja niiden omistajista (username)
```
SELECT team.name, account.username FROM team LEFT JOIN account ON team.account_id = account.id ORDER BY team.name
```