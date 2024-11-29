# /app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from the config.py file
    app.config.from_object('config.Config')

    # Initialize the app with SQLAlchemy
    db.init_app(app)

    # Create all tables (only for development)
    with app.app_context():
        db.create_all()

    # Import routes after initializing the app
    from .routes import user

    # Register the routes with the app
    app.register_blueprint(user.bp)

    return app
