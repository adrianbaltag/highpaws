"""__init__.py
This module initializes the src package.
"""

from flask import Flask

# Import the Blueprints for the application
from .auth import auth
from .views import views


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # ! Load configuration from a config file or object
    app.config["SECRET_KEY"] = "your_secret_key_here"

    # !  Register the Blueprints
    app.register_blueprint(
        views, url_prefix="/"
    )  # Register views blueprint at the root URL
    app.register_blueprint(
        auth, url_prefix="/"
    )  # Register auth blueprint at the root URL

    return app
