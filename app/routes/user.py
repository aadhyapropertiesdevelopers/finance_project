# # /app/routes.py
# from sqlite3 import IntegrityError
# from flask import Blueprint, request, jsonify
# from ..models.user import User
# from .. import db
# from ..services.user_service import user_post_method

# bp = Blueprint('main', __name__)

# # POST method to create a user
# @bp.route('/users', methods=['POST'])
# def create_user():
#     try:
#         # Get data from request
#         data = request.get_json()
#         name = data['name']
#         email = data['email']
#         response = user_post_method(name,email)
#         return response
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({"error": "Email already exists in the database. "}), 400
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # GET method to fetch all users
# @bp.route('/', methods=['GET'])
# def get_users():
#     try:
#         # Query all users from the database
#         users = User.query.all()

#         # Convert the result to a list of dictionaries
#         users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]

#         return jsonify(users_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500






from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db
from werkzeug.security import generate_password_hash
from app.utils.auth_decorators import token_required
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

bp = Blueprint('user', __name__)

# POST method to create a user
# POST method to create a user
@bp.route('/users', methods=['POST'])
def create_user():
    try:
        # Get data from request
        data = request.get_json()
        print(f"Data received: {data}")
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        print(f"parsed data -Username: {username},Email:{email}")

        # Validate passwords match
        if password != confirm_password:
            return jsonify({"error": "Passwords do not match."}), 400

        # Hash the password before saving it
        hashed_password = generate_password_hash(password)

        # Create a new User instance
        new_user = User(username=username, email=email, password=hashed_password)  # No confirm_password here

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully."}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username or email already exists in the database."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# # GET method to fetch all users
# @bp.route('/user', methods=['GET'])
# # @token_required
# def get_users():
#     try:
#         # Query all users from the database
#         users = User.query.all()

#         # Convert the result to a list of dictionaries
#         users_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]

#         return jsonify(users_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    

#     # Login method
# @bp.route('/login', methods=['POST'])
# def login_user():
#     try:
#         # Get data from request
#         data = request.get_json()
#         email = data['email']
#         password = data['password']

#         # Query the database for the user
#         user = User.query.filter_by(email=email).first()

#         # If user does not exist or password does not match
#         if not user or not check_password_hash(user.password, password):
#             return jsonify({"error": "Invalid email or password."}), 401

#         # If authentication is successful
#         return jsonify({"message": "Login successful.", "user": {"id": user.id, "username": user.username, "email": user.email}}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400


# # GET method to fetch all users
# @bp.route('/users', methods=['GET'])
# def get_users():
#     try:
#         # Query all users from the database
#         users = User.query.all()

#         # Convert the result to a list of dictionaries
#         users_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]

#         return jsonify(users_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

