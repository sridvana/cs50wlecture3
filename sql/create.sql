CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights
    (origin, destnation, duration)
    VALUES ('New York', 'London', 415);