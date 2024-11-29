# /app/routes.py
from sqlite3 import IntegrityError
from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db
from ..services.user_service import user_post_method

bp = Blueprint('main', __name__)

# POST method to create a user
@bp.route('/users', methods=['POST'])
def create_user():
    try:
        # Get data from request
        data = request.get_json()
        name = data['name']
        email = data['email']
        response = user_post_method(name,email)
        return response
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists in the database."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET method to fetch all users
@bp.route('/', methods=['GET'])
def get_users():
    try:
        # Query all users from the database
        users = User.query.all()

        # Convert the result to a list of dictionaries
        users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]

        return jsonify(users_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
