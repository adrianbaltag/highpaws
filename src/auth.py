"""_summary_: This module contains the views for the Flask application.
It defines the routes and their corresponding view functions.
Using Blueprints to organize the application structure.
This module is part of the src package.
"""

# Create a Blueprint for the views
from flask import Blueprint

auth = Blueprint(
    "auth", __name__
)  # Create a Blueprint instance named 'auth' with the current module's name


@auth.route("/login")
def login():
    """Render the login page."""
    return "Login Page"


@auth.route("/logout")
def logout():
    """Render the logout page."""
    return "Logout Page"


@auth.route("/register")
def register():
    """Render the registration page."""
    return "Register Page"
