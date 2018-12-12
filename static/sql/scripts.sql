CREATE TABLE IF NOT EXISTS comic(
comic_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
comic_number VARCHAR(25) NOT NULL UNIQUE,
comic_name VARCHAR(25) NOT NULL UNIQUE,
issue_number VARCHAR(5) NULL,
description TEXT NULL,
PRIMARY KEY (comic_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'comics1.csv'
INTO TABLE comic
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(comic_number,comic_name,issue_number,description);

CREATE TABLE IF NOT EXISTS power(
power_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
power_name VARCHAR(25) NOT NULL UNIQUE,
PRIMARY KEY (power_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'power1.csv'
INTO TABLE power
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(power_name);


CREATE TABLE IF NOT EXISTS alignment
  (
    alignment_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    alignment_name VARCHAR(8) NOT NULL UNIQUE,
    PRIMARY KEY (alignment_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO alignment (alignment_name) VALUES
  ('good'), ('bad'),('neutral');

CREATE TABLE IF NOT EXISTS gender
  (
    gender_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    gender_name VARCHAR(8) NOT NULL UNIQUE,
    PRIMARY KEY (gender_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO gender (gender_name) VALUES
  ('Male'), ('Female');

CREATE TABLE IF NOT EXISTS eye_color
  (
    eye_color_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    eye_color_name VARCHAR(25) NOT NULL UNIQUE,
    PRIMARY KEY (eye_color_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO eye_color (eye_color_name) VALUES
  ('yellow'),('blue'),('green'),('brown'),('red'),('violet'),('white'),('purple'),('black'),('grey'),('silver'),('yellow / red'),('yellow (without irises)'),('gold'),('blue / white'),('hazel'),('green / blue'),('white / red'),('indigo'),('amber'),('yellow / blue');

CREATE TABLE IF NOT EXISTS race
  (
    race_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    race_name VARCHAR(25) NOT NULL UNIQUE,
    PRIMARY KEY (race_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'race.csv'
INTO TABLE race
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(race_name);

CREATE TABLE IF NOT EXISTS hair_color
  (
    hair_color_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    hair_color_name VARCHAR(25) NOT NULL UNIQUE,
    PRIMARY KEY (hair_color_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'hair_color.csv'
INTO TABLE hair_color
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(hair_color_name);


CREATE TABLE IF NOT EXISTS publisher
  (
    publisher_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    publisher_name VARCHAR(25) NOT NULL UNIQUE,
    PRIMARY KEY (publisher_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'publisher.csv'
INTO TABLE publisher
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(publisher_name);

CREATE TABLE IF NOT EXISTS skin_color
  (
    skin_color_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    skin_color_name VARCHAR(25) NOT NULL UNIQUE,
    PRIMARY KEY (skin_color_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'skincolor.csv'
INTO TABLE skin_color
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(skin_color_name);


CREATE TEMPORARY TABLE temp_character
  (
    character_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    character_name VARCHAR(20) NOT NULL,
    alignment_name VARCHAR(8) NULL,
    gender_name VARCHAR(8) NULL,
    eye_color_name VARCHAR(25) NULL,
    race_name VARCHAR(25) NULL,
    hair_color_name VARCHAR(25) NULL,
    publisher_name VARCHAR(25) NULL,
    skin_color_name VARCHAR(25) NULL,
    height INT(4) NOT NULL,
    weight INT(4) NOT NULL,
    character_number VARCHAR(8) NOT NULL,
    intelligence INT(4) NULL,
    strength INT(4) NULL,
    speed INT(4) NULL,
    durability INT(4) NULL,
    power INT(4) NULL,
    combat INT(4) NULL,
    total INT(4) NULL,
    PRIMARY KEY (character_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'character_total3.csv'
INTO TABLE temp_character
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(character_name,alignment_name,gender_name,eye_color_name,race_name,hair_color_name,publisher_name,
skin_color_name,height,weight,character_number,intelligence,strength,speed,durability,power,combat,total);



UPDATE temp_character
SET alignment_name = IF(alignment_name = '', NULL, alignment_name),
gender_name = IF(gender_name = '', NULL, gender_name),
eye_color_name = IF(eye_color_name = '', NULL, eye_color_name),
race_name = IF(race_name = '', NULL, race_name),
hair_color_name = IF(hair_color_name = '', NULL, hair_color_name),
publisher_name = IF(publisher_name = '', NULL, publisher_name),
skin_color_name = IF(skin_color_name = '', NULL, skin_color_name),
intelligence = IF(intelligence = '', NULL, intelligence),
strength = IF(strength = '', NULL, strength),
speed = IF(speed = '', NULL, speed),
durability = IF(durability= '', NULL, durability),
power = IF(power = '', NULL, power),
combat = IF(combat = '', NULL, combat),
total = IF(total = '', NULL, total);

CREATE TABLE IF NOT EXISTS character_info
  (
    character_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    character_name VARCHAR(20) NOT NULL UNIQUE,
    alignment_id INTEGER NULL,
    gender_id INTEGER NULL,
    eye_color_id INTEGER NULL,
    race_id INTEGER NULL,
    hair_color_id INTEGER NULL,
    publisher_id INTEGER NULL,
    skin_color_id INTEGER NULL,
    height INT(4) NOT NULL,
    weight INT(4) NOT NULL,
    character_number VARCHAR(8) NOT NULL,
    intelligence INT(4) NULL,
    strength INT(4) NULL,
    speed INT(4) NULL,
    durability INT(4) NULL,
    power INT(4) NULL,
    combat INT(4) NULL,
    total INT(4) NULL,
    PRIMARY KEY (character_id),
    FOREIGN KEY (alignment_id) REFERENCES alignment(alignment_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (gender_id) REFERENCES gender(gender_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (eye_color_id) REFERENCES eye_color(eye_color_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (race_id) REFERENCES race(race_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (hair_color_id) REFERENCES hair_color(hair_color_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (skin_color_id) REFERENCES skin_color(skin_color_id)
    ON DELETE RESTRICT ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;


INSERT IGNORE INTO character_info
  (
    character_name,
    alignment_id,
    gender_id,
    eye_color_id,
    race_id,
    hair_color_id,
    publisher_id,
    skin_color_id,
    height,
    weight,
    character_number,
    intelligence,
    strength,
    speed,
    durability,
    power,
    combat,
    total
  )
SELECT tc.character_name, a.alignment_id, g.gender_id, e.eye_color_id,r.race_id,h.hair_color_id,p.publisher_id,s.skin_color_id,tc.height, tc.weight, tc.character_number,tc.intelligence,tc.strength,tc.speed,tc.durability,tc.power,tc.combat,tc.total
  FROM temp_character tc
       LEFT JOIN alignment a
              ON tc.alignment_name = a.alignment_name
       LEFT JOIN gender g
              ON tc.gender_name = g.gender_name
       LEFT JOIN eye_color e
              ON tc.eye_color_name = e.eye_color_name
       LEFT JOIN race r
              ON tc.race_name = r.race_name
       LEFT JOIN hair_color h
              ON tc.hair_color_name = h.hair_color_name
       LEFT JOIN publisher p
              ON tc.publisher_name = p.publisher_name
       LEFT JOIN skin_color s
              ON tc.skin_color_name = s.skin_color_name
 WHERE IFNULL(tc.alignment_name, 0) = IFNULL(a.alignment_name, 0)
   AND IFNULL(tc.gender_name, 0) = IFNULL(g.gender_name, 0)
   AND IFNULL(tc.eye_color_name, 0) = IFNULL(e.eye_color_name, 0)
   AND IFNULL(tc.race_name, 0) = IFNULL(r.race_name, 0)
   AND IFNULL(tc.hair_color_name, 0) = IFNULL(h.hair_color_name, 0)
   AND IFNULL(tc.publisher_name , 0) = IFNULL(p.publisher_name, 0)
   AND IFNULL(tc.skin_color_name, 0) = IFNULL(s.skin_color_name, 0)
 ORDER BY tc.character_name;


CREATE TABLE IF NOT EXISTS character_power
  (
    character_power_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    character_id INTEGER NOT NULL,
    power_id INTEGER NOT NULL,
    PRIMARY KEY (character_power_id),
    FOREIGN KEY (character_id) REFERENCES character_info(character_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (power_id) REFERENCES power(power_id)
    ON DELETE CASCADE ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;


CREATE TEMPORARY TABLE temp_character_power
  (
    character_power_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    character_name VARCHAR(20) NOT NULL,
    power_name VARCHAR(25) NOT NULL,
    PRIMARY KEY (character_power_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;


LOAD DATA LOCAL INFILE 'character_power.csv'
INTO TABLE temp_character_power
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(character_name,power_name);

INSERT IGNORE INTO character_power
(character_id,
 power_id
)
SELECT c.character_id,p.power_id
FROM temp_character_power tcp
LEFT JOIN character_info c
     ON c.character_name=tcp.character_name
LEFT JOIN power p
     ON p.power_name=tcp.power_name
ORDER BY c.character_id,p.power_id;

CREATE TEMPORARY TABLE temp_character_comic
  (
    character_comic_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    comic_number VARCHAR(8) NOT NULL,
    character_number VARCHAR(25) NOT NULL,
    PRIMARY KEY (character_comic_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;


LOAD DATA LOCAL INFILE 'character_comic.csv'
INTO TABLE temp_character_comic
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
(comic_number,character_number);

CREATE TABLE IF NOT EXISTS character_comic
  (
    character_comic_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    character_id INTEGER NOT NULL,
    comic_id INTEGER NOT NULL,
    PRIMARY KEY (character_comic_id),
    FOREIGN KEY (character_id) REFERENCES character_info(character_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (comic_id) REFERENCES comic(comic_id)
    ON DELETE CASCADE ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO character_comic
(character_id,
 comic_id
)
SELECT c.character_id,cm.comic_id
FROM temp_character_comic tcc
LEFT JOIN character_info c
     ON c.character_number=tcc.character_number
LEFT JOIN comic cm
     ON cm.comic_number=tcc.comic_number
ORDER BY c.character_id,cm.comic_id;
DROP TABLE temp_character;
DROP TABLE  temp_character_comic;
DROP TABLE  temp_character_power;
