"""_summary_: Entry point for the application."""

from src import create_app  # Import the create_app function from the src package

app = create_app()  # Create the Flask application instance


if __name__ == "__main__":
    app.run(debug=True)  # Run the application in debug mode
# Note: In a production environment, you would typically not run the app with debug=True.
# Instead, you would use a production-ready server like Gunicorn or uWSGI.
