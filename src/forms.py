"""_summary_: This module contains the forms used in the Flask application.
It defines the form classes using Flask-WTF for handling user input.

"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    """Form for user registration."""

    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(min=6), EqualTo("password")],
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    """Form for user login."""

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6)],
    )
    remember = BooleanField(
        "Remember Me"
    )  # Optional field for remember me functionality
    submit = SubmitField("Login")
