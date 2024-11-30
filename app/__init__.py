# # /app/__init__.py
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
    
#     # Load configuration from the config.py file
#     app.config.from_object('config.Config')

#     # Initialize the app with SQLAlchemy
#     db.init_app(app)

#     # Create all tables (only for development)
#     with app.app_context():
#         db.create_all()

#     # Import routes after initializing the app
#     from .routes import user

#     # Register the routes with the app
#     app.register_blueprint(user.bp)

#     return app

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here to avoid circular import
    with app.app_context():
        from .models.user import User  # Delayed import
        db.create_all()

    # Register blueprints
    from .routes import user,login,token,dashboard
    app.register_blueprint(user.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(token.bp)
    app.register_blueprint(dashboard.bp)
    
    
    

    # from app.routes.user import bp as user_bp
    # from app.routes.login import bp as login_bp

    # app.register_blueprint(user_bp, url_prefix='/user')
    # app.register_blueprint(login_bp, url_prefix='/auth')

    return app



