from flask import Flask #Imports the flask class from the flask package
from .views import views #Imports the "views" blueprint class we initialised in "views.py"

class App:
    def __init__(self):
        self.app = Flask(__name__) #Creates a Flask application with the name being the value of __name__
        self.app.config["SECRET_KEY"] = "youshallnotpass" # Temporary password, this will be changed when the app is ready for production
        
        self.app.register_blueprint(views, url_prefix="/") #Registers the "views" blueprint to the application
        
    def run(self, debug: bool=False):
        self.app.run(debug=debug)
        
