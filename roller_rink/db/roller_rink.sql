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
    skater_id INT NOT NULL REFERENCES skaters(id) ON DELETE CASCADE,
    lesson_id INT NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
    level_reached VARCHAR(255)
);


INSERT INTO skaters (full_name, premium_member) VALUES ('Wheels Smith', true);
INSERT INTO skaters (full_name, premium_member) VALUES ('Skate Beckinsale', false);
INSERT INTO lessons (name, day, capacity, premium) VALUES ('Speed Skating', 'Monday', 10, false);
INSERT INTO lessons (name, day, capacity, premium) VALUES ('Artistic Skating', 'Wednesday', 10, false);

-- SELECT skaters.* FROM skaters INNER JOIN levels ON levels.skater_id = skaters.id;
-- SELECT lessons.* FROM lessons INNER JOIN levels ON levels.lesson_id = lessons.id;

-- INSERT INTO levels (skater_id, lesson_id, level_reached) VALUES (1, 1, 'Beginner');