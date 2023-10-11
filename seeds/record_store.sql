-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
    );

-- Finally, we add any records that are needed for the tests to run
-- INSERT INTO albums (title, release_year, artist_id) VALUES ('Rock Album 2020', 2020, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Pop Album 2019', 2019, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Hip-Hop Album 2021', 2021, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Jazz Album 2018', 2018, 4);
-- INSERT INTO albums (title, release_year, artist_id) VALUES ('Classical Album 2017', 2017, 5);


