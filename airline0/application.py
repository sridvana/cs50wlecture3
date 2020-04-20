import os

from flask import Flask, render_template, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#from flask_session import Session

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET", "POST"])
def index():
    headline = "This is a flight booking app"
    flights = db.execute("SELECT * FROM flights").fetchall()   
    return render_template("index.html", headline=headline, flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    # Get form information
    name = request.form.get("name")
    if name == "":
           return render_template("error.html", message="Pl. enter a valid name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid Flight Number")
    
    #Make sure the flight exists.
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that flight number")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    {"name": name, "flight_id": flight_id})
    db.commit()

    return render_template("success.html", name=name, flight_id=flight_id)