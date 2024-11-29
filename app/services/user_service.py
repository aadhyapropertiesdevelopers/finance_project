
from ..models.user import User
from flask import jsonify
from .. import db
def user_post_method(name,email):
           # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already exists."}), 400

        # Create a new User instance
        new_user = User(name=name, email=email)

        # Add the new user to the session and commit it to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "payment added sucessfully!"}), 201