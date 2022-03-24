from flask import (Blueprint, #Import the Blueprint class from the flask package
                  render_template) #Import the render_template function that will display the HTML file

views = Blueprint("views", __name__) #Initialise our blueprint and name it "views"

@views.route("/") #Nothing is specified after the url prefix, meaning only the main url needs to be entered to view this page
def home():
    return render_template("home.html") #Will render the "home.html" file in the templates directory
    
    