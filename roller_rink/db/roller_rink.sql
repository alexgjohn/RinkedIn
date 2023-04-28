DROP TABLE IF EXISTS levels;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS skaters;

CREATE TABLE skaters(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    premium_member BOOLEAN
);




CREATE TABLE lessons(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    day VARCHAR(255),
    capacity INT,
    premium BOOLEAN
);



CREATE TABLE levels(
    id SERIAL PRIMARY KEY,
    skater_id INT NOT NULL REFERENCES skaters(id),
    lesson_id INT NOT NULL REFERENCES lessons(id),
    level_reached VARCHAR(255)
);