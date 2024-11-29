
# from ..models.user import User
# from flask import jsonify
# from .. import db
# def user_post_method(name,email):
#            # Check if the email already exists
#         existing_user = User.query.filter_by(email=email).first()
#         if existing_user:
#             return jsonify({"error": "Email already exists."}), 400

#         # Create a new User instance
#         new_user = User(name=name, email=email)

#         # Add the new user to the session and commit it to the database
#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({"message": "User created successfully!"}), 201




from ..models.user import User
from flask import jsonify
from .. import db
from werkzeug.security import generate_password_hash

def user_post_method(username, email, password, confirm_password):
    # Check if the username or email already exists
    existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
    if existing_user:
        return jsonify({"error": "Username or email already exists."}), 400

    # Validate that passwords match
    if password != confirm_password:
        return jsonify({"error": "Passwords do not match."}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new User instance
    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        confirm_password=hashed_password  # Storing hashed password for confirm_password too
    )

    # Add the new user to the session and commit it to the database
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
