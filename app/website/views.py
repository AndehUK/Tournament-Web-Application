from flask import (Blueprint, #Import the Blueprint class from the flask package
                  render_template) #Import the render_template function that will display the HTML file
from .models import *
from random import randint

views = Blueprint("views", __name__) #Initialise our blueprint and name it "views"

def fetch_db() -> tuple:
    individuals = Individuals.query.all()
    teams = Teams.query.all()
    events = Events.query.all()
    return (individuals, teams, events)

@views.route("/") #Nothing is specified after the url prefix, meaning only the main url needs to be entered to view this page
def home():
    data = fetch_db()
    individuals, teams, events = data
    individuals = sorted(individuals, key=lambda x: x.name) #Organises the individuals alphabetically
    teams = sorted(teams, key=lambda x: x.name) #Organises the teams alphabetically
    le_individuals = sorted(individuals, key=lambda x: x.points, reverse=True) #Organises the individuals in point order
    le_teams = sorted(teams, key=lambda x: x.points, reverse=True) #Organises the teams in point order
    return render_template("home.html", individuals=individuals, teams=teams, li=le_individuals, lt=le_teams) #Will render the "home.html" file in the templates directory
    
