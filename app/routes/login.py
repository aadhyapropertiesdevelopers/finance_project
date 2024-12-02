from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash  # Import check_password_hash
from app.services.jwt_utils import encode_jwt


bp = Blueprint('login', __name__)

    # Login method
@bp.route('/login', methods=['POST'])
def login_user():
    try:
        # Get data from request
        data = request.get_json()
        email = data['email']
        password = data['password']
        print(f"Login Attempt: Email - {email}, Password - {password}")  # Debugging log

        # Query the database for the user
        user = User.query.filter_by(email=email).first()

        # If user does not exist or password does not match
        if not user or not check_password_hash(user.password, password):
            print("User not found")
            return jsonify({"error": "Invalid email or password."}), 401
        token = encode_jwt(user.id)

        # If authentication is successful
        return jsonify({"message": "Login successful.", "token":token,"user": {"id": user.id, "username": user.username, "email": user.email}}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# GET method to fetch all users
# @bp.route('/login', methods=['GET'])
# def get_users():
#     try:
#         # Query all users from the database
#         users = User.query.all()

#         # Convert the result to a list of dictionaries
#         users_list = [{"id": user.id, "username": user.username, "email": user.email} for user in users]

#         return jsonify(users_list), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500