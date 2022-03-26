from flask import Flask #Imports the flask class from the flask package
from .views import views #Imports the "views" blueprint class we initialised in "views.py"
from flask_sqlalchemy import SQLAlchemy #Imports the SQLAlchemy class from the flask_sqlalchemy package
from os import path #Allows me to conduct checks on a local file path from the core python package "os"
from .models import db

class App:
    def __init__(self):
        self.app = Flask(__name__) #Creates a Flask application with the name being the value of __name__
        self.app.config["SECRET_KEY"] = "youshallnotpass" # Temporary password, this will be changed when the app is ready for production
        self.app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
        self.app.register_blueprint(views, url_prefix="/") #Registers the "views" blueprint to the application
        
    def run(self, debug: bool=False):
        db.init_app(self.app) #Creates a database connection to allow us to interact with the database
        self.create_database() #Create the database.db file if it does not exist
        self.app.run(debug=debug, port=3000)
        
    def create_database(self):
        if not path.exists("website/database.db"):
            db.create_all(app=self.app)
            print("Created Database.")

