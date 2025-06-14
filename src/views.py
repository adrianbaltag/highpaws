"""_summary_: This module contains the views for the Flask application.
It defines the routes and their corresponding view functions.
Using Blueprints to organize the application structure.
This module is part of the src package.
"""

# Create a Blueprint for the views
from flask import Blueprint, render_template

views = Blueprint(
    "views", __name__
)  # Create a Blueprint instance named 'views' with the current module's name


@views.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")
