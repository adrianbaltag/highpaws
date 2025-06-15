"""_summary_: This module contains the database models for the Flask application.
It defines the User and Post models using SQLAlchemy ORM.
"""

from datetime import datetime

from . import db

# db = SQLAlchemy()


class User(db.Model):
    """User model for the application."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(
        db.String(20), nullable=False, default="default.jpg"
    )  # Default profile image
    posts = db.relationship(
        "Post", backref="author", lazy=True
    )  # Relationship with Post model

    # How object is represented as a string
    def __repr__(self):
        return f"<User {self.username}, {self.email},   {self.image_file}>"


class Post(db.Model):
    """Post model for the application."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
    )  # Foreign key to User model 1to many relationship

    def __repr__(self):
        return f"<Post {self.title}, {self.date_posted}>"
