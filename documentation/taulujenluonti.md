```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)
CREATE TABLE player (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	player_tag VARCHAR(144) NOT NULL, 
	top BOOLEAN NOT NULL, 
	jgl BOOLEAN NOT NULL, 
	mid BOOLEAN NOT NULL, 
	adc BOOLEAN NOT NULL, 
	sup BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (top IN (0, 1)), 
	CHECK (jgl IN (0, 1)), 
	CHECK (mid IN (0, 1)), 
	CHECK (adc IN (0, 1)), 
	CHECK (sup IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
CREATE TABLE team (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)
CREATE TABLE teammate (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	team_id INTEGER NOT NULL, 
	role INTEGER, 
	player INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(team_id) REFERENCES team (id), 
	FOREIGN KEY(player) REFERENCES player (id)
)
```