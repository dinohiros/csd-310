-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'BbbdGTR2022$';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Mavericks', 'Champ');

INSERT INTO team(team_name, mascot)
    VALUES('Nuggets', 'Rocky');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Luka', 'Doncic', (SELECT team_id FROM team WHERE team_name = 'Mavericks'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jalen', 'Brunson', (SELECT team_id FROM team WHERE team_name = 'Mavericks'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Tim', 'Hardaway Jr.', (SELECT team_id FROM team WHERE team_name = 'Mavericks'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Nikola', 'Jokic', (SELECT team_id FROM team WHERE team_name = 'Nuggets'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jamal', 'Murray', (SELECT team_id FROM team WHERE team_name = 'Nuggets'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Michael', 'Porter Jr.', (SELECT team_id FROM team WHERE team_name = 'Nuggets'));