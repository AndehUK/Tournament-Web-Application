from asyncio import events
from discord import Team
from flask import (Blueprint, #Import the Blueprint class from the flask package
                   redirect, 
                  render_template, #Import the render_template function that will display the HTML file
                  request, 
                  url_for) 
from flask_login import login_user, logout_user, login_required
from .models import *
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.security import check_password_hash
from ast import literal_eval

views = Blueprint("views", __name__) #Initialise our blueprint and name it "views"

def fetch_db() -> tuple:
    individuals = Individuals.query.all()
    teams = Teams.query.all()
    events = Events.query.all()
    return (individuals, teams, events)

def add_new_participant(data):
    try:
        if data["new_individual"]:
            new_participant = Individuals(name=data["new_individual"], events_played="[]", points=0)
    except BadRequestKeyError:
        pass
    try:
        if data["new_team_name"]:
            new_participant = Teams(name=data["new_team_name"], 
                             members=f'[{data["new_team_1"]}, {data["new_team_2"]}, {data["new_team_3"]}, {data["new_team_4"]}, {data["new_team_5"]}]',
                             events_played="[]",
                             points=0)
    except BadRequestKeyError:
        pass
    try:
        db.session.add(new_participant)
        db.session.commit()
    except UnboundLocalError:
        pass
    
def delete_participant(data):
    participants = fetch_db()[-1] #Gets all participants from the database
    for x in participants:
        try:
            if data["username"] == x.name:
                y = Individuals.query.filter_by(name=x.name).first() #Fetches the first instance that matches the username provided
                if not y: #if an individual with this name doesnt exist:
                    y = Teams.query.filter_by(name=x.name).first() #Fetch from teams instead
                try:
                    db.session.delete(y)
                    db.session.commit()
                except UnboundLocalError:
                    pass
        except BadRequestKeyError:
            pass
        
def add_event_score(data):
    try:
        if data["event"] and data["points"] and data["name"]:
            user = Individuals.query.filter_by(name=data["name"]).first()
            if not user:
                user = Teams.query.filter_by(name=data["name"]).first()
            events_played = literal_eval(user.events_played) #Will turn string representation of a list, into an actual list object
            events_played.append(data["event"]) #Add the new event to the list of the events they've played
            user.events_played = str(events_played) #Replace their old events_played, with the new one we just appended to
            user.points += int(request["points"]) #Add the points they earned to their current total.
            db.session.commit()
    except BadRequestKeyError:
        pass
    
def add_new_event(data):
    new_event = Events(name=data["new_event_name"],
                       date=data["new_event_date"],
                       time=data["new_event_time"],
                       place=data["new_event_place"],
                       type=data["new_event_type"])
    db.session.add(new_event)
    db.session.commit()
    
def edit_event(data):
    event = Events.query.filter_by(name=data["edit_event"]).first()
    db.session.delete(event)
    db.session.commit()
    event = Events(name=data["edit_event_name"],
                   date=data["edit_event_date"],
                   time=data["edit_event_time"],
                   place=data["edit_event_place"],
                   type=data["edit_event_type"])
    db.session.add(event)
    db.session.commit()
    
def delete_event(data):
    try:
        if request.form["delete_event"]:
            event = Events.query.filter_by(name=data["edit_event"]).first()
            db.session.delete(event)
            db.session.commit()
    except BadRequestKeyError:
        pass

@views.route("/", methods=["POST", "GET"]) #Nothing is specified after the url prefix, meaning only the main url needs to be entered to view this page
@login_required()
def home():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        try: #Adding a new individual
            if data["new_individual"]:
                add_new_participant(data)
                return redirect(url_for("views.home"))
        except BadRequestKeyError:
            pass
        try: #Adding a new team
            if data["new_team_name"]:
                add_new_participant(data)
                return redirect(url_for("views.home"))
        except BadRequestKeyError:
            pass
        try: #Deleting a Individual/Team
            if data["username"]:
                delete_participant(data)
                return redirect(url_for("views.home"))
        except BadRequestKeyError:
            pass
        try:
            if data["event"]:
                add_event_score(data)
                return redirect(url_for("views.home"))
        except BadRequestKeyError:
            pass
        try:
            if request.form["new_event_name"]:
                add_new_event(data)
                return redirect(url_for("views.home"))
        except BadRequestKeyError:
            pass
        try:
            if request.form["edit_event_name"]:
                try:
                    print(request.form["delete_event"])
                    if request.form["delete_event"]:
                        events = fetch_db()[2]
                        delete_event(events, request)
                        return redirect(url_for("views.home"))
                except BadRequestKeyError:
                    pass
                try:
                    if request.form["edit_event_name"]:
                        edit_event(request.form.to_dict())
                        return redirect(url_for("views.home"))
                except BadRequestKeyError:
                    pass
        except BadRequestKeyError:
            pass
    data = fetch_db()
    individuals, teams, events = data
    individuals = sorted(individuals, key=lambda x: x.name) #Organises the individuals alphabetically
    teams = sorted(teams, key=lambda x: x.name) #Organises the teams alphabetically
    le_individuals = sorted(individuals, key=lambda x: x.points, reverse=True) #Organises the individuals in point order
    le_teams = sorted(teams, key=lambda x: x.points, reverse=True) #Organises the teams in point order
    return render_template("home.html", individuals=individuals, teams=teams, li=le_individuals, lt=le_teams, events=events) #Will render the "home.html" file in the templates directory

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form.to_dict()
        email = data["email"]
        password = data["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
    return render_template("login.html")
    
@views.route("/logout")
@login_required()
def logout():
    logout_user()
    return redirect(url_for("views.login"))

