# make sure to install flask in terminal below with command: pip install Flask
# command to run website: flask --app starterCode run

# Import the Flask class
from flask import Flask, render_template

# Create a new Flask web app
# __name__ is a special Python variable that tells Flask which file is being run
app = Flask(__name__)

# Tell Flask that when someone visits the homepage ("/"), run the following function
@app.route("/")
def home():
    my_message = "Welcome to Flask Basics!"  # Define a Python variable
    return render_template("index.html", message=my_message)  # Pass to HTML