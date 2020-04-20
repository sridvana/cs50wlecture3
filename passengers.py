import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))

db = scoped_session(sessionmaker(bind=engine))

def main():

    #list all the flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination} in {flight.duration} minutes")

    #prompt the user to choose a flight.
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id": flight_id}).fetchone()

    #make sure flight is valid.
    if flight is None:
        print("Error: No such flight")
        return

    #List passengers.
    passengers=db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()

    print("\nPassngers:")
    for passenger in passengers:
        print(f"{passenger.name} who is traveling from {flight.origin} to {flight.destination}")
    if len(passengers) == 0:
        print(f"No passengers for the flight id {flight_id} from {flight.origin} to {flight.destination}")

if __name__ == "__main__":
    main()