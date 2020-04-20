CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights
    (origin, destnation, duration)
    VALUES ('New York', 'London', 415);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER NOT NULL
);

INSERT INTO passengers
    (name, flight_id)
    VALUES ('Passenger-1', 10);