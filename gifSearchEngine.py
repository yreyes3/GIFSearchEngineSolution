# make sure to install flask in terminal below with command: pip install Flask
# command to run website: flask --app gifSearchEngine run

# Import the Flask class
from flask import Flask, render_template, request
# To parse API responses
import json
# For making requests to Giphy API
from urllib import parse, request as url_request

# Create a new Flask web app
# __name__ is a special Python variable that tells Flask which file is being run
app = Flask(__name__)

# Replace this with your actual Giphy API key
API_KEY = "i5yl6nbONe67xGS0cupRca0mwNO0UiJ4"  

# Tell Flask that when someone visits the homepage ("/"), run the following function
@app.route("/", methods=["GET", "POST"])
def home():
    gif_urls = []  # Empty list to store retrieved GIFs

    if request.method == "POST":  # Check if the user submitted the form
        search_term = request.form["search"]  # Get the user's search input

        url = "http://api.giphy.com/v1/gifs/search"  # Base URL for Giphy API

        # Prepare the search parameters (query, API key, and limit of results)
        params = parse.urlencode({
            "q": search_term,  # User's search term
            "api_key": API_KEY,  # API key to authenticate request
            "limit": "5"  # Number of GIFs to retrieve
        })

        # Make the API request to Giphy
        with url_request.urlopen("".join((url, "?", params))) as response:
            data = json.loads(response.read())  # Convert JSON response to Python dictionary

        # Extract GIF URLs from the API response
        for gif in data.get("data", []):
            gif_urls.append(gif["images"]["original"]["url"])

    # Render the HTML template and pass the list of GIF URLs to display
    return render_template("index.html", gif_urls=gif_urls)