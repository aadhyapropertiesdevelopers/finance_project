from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('Config,config')

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from app.routes.payment_type_routes import payment_type_bp
    app.register_blueprint(payment_type_bp)
    

    return app
