from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ID acting as a primary key
    name = db.Column(db.String(50), unique=True) # Unique kwarg to make sure there can't be 2 teams of the same name
    members = db.Column(db.String(500), unique=True) # This will be a string representation of a list, containing the team members
    events_played = db.Column(db.String(500)) # This will also be a string representation of a list, containing the events the team has played
    points = db.Column(db.Integer) # Integer which represents the team's total points
    
class Individuals(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ID acting as a primary key
    name = db.Column(db.String(50), unique=True) # Unique kwarg to make sure there can't be 2 individuals of the same name
    events_played = db.Column(db.String(500)) # This will be a string representation of a list, containing the events the team has played
    points = db.Column(db.Integer) # Integer which represents the individual's total points

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True) # ID acting as a primary key
    name = db.Column(db.String(100), unique=True) # Unique kwarg to make sure there can't be 2 teams of the same name
    date = db.Column(db.String(10)) # String representation of a date that the event is being held on
    time = db.Column(db.String(13)) # String representation of a time that the event is being held on
    place = db.Column(db.String(50)) #The location of the event
    type = db.Column(db.String(30)) # The type of event (Academic/Sports)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # ID acting as a primary key
    email = db.Column(db.String(150), unique=True) # Unique so 1 email cant be used for multiple logins
    password = db.Column(db.String(150)) # Password for the user, no requirements set other than character limit.
    
    