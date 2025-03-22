# make sure to install flask in terminal below with command: pip install Flask
# command to run website: flask --app hello run

# Import the Flask class
from flask import Flask

# Create a new Flask web app
# __name__ is a special Python variable that tells Flask which file is being run
app = Flask(__name__)

# Tell Flask that when someone visits the homepage ("/"), run the following function
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"