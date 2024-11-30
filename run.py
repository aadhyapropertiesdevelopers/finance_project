# from flask import Flask
# from routes.employee_routes import employee_bp
# from routes.payment_routes import payment_bp
# from routes.payment_type_routes import payment_type_bp

# app = Flask(__name__)

# # PostgreSQL database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/pranith'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize the database
# db.init_app(app)
# # Register blueprints
# app.register_blueprint(employee_bp)
# app.register_blueprint(payment_bp)
# app.register_blueprint(payment_type_bp)


# if __name__ == '__main__':
#     app.run(debug=True)
from app import create_app, db
from app.models.payment_type import PaymentType

app = create_app()

# Create tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
