"""__init__.py
This module initializes the src package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import Blueprints
from .auth import auth
from .views import views

# Initialize the database (without binding it yet)
db = SQLAlchemy()


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Load configuration
    app.config["SECRET_KEY"] = "your_secret_key_here"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev-testing.db"

    # Initialize and create the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
