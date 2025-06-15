"""_summary_: This module contains the views for the Flask application.
It defines the routes and their corresponding view functions.
Using Blueprints to organize the application structure.
This module is part of the src package.
"""

# Create a Blueprint for the views
from flask import Blueprint, flash, redirect, render_template, url_for

from src.forms import (  # Import the RegistrationForm class from forms.py
    LoginForm,
    RegistrationForm,
)

auth = Blueprint(
    "auth", __name__
)  # Create a Blueprint instance named 'auth' with the current module's name


@auth.route("/login", methods=["GET", "POST"])
def login():
    """Render the login page."""
    form = LoginForm()
    if form.validate_on_submit():
        # flash
        flash(f"Login successful for {form.email.data}!", "success")
        # redirect to home page
        return redirect(url_for("views.home"))
    return render_template(
        "login.html", title="Login", form=form
    )  # Pass the form to the template for rendering, displaying the login form


@auth.route("/logout")
def logout():
    """Render the logout page."""
    return "Logout Page"


@auth.route("/register", methods=["GET", "POST"])
def register():
    """Render the registration page."""
    form = RegistrationForm()  # Create an instance of the RegistrationForm
    if form.validate_on_submit():  # Check if the form is submitted and valid
        # flash
        flash(f"Account created for {form.username.data}!", "success")
        # redirect to home page
        return redirect(url_for("views.home"))

    return render_template(
        "register.html", form=form, title="Register"
    )  # Pass the form to the template for rendering, displaying the registration form
