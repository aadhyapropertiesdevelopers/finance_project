from ..models.payment_types_model import payment_types_model
from flask import jsonify
from .. import db
def payment_type_post_method(type,status):
    

        # Create a new User instance
        new_payment_type = payment_types_model(payment_type_name=type, status=status)


        # Add the new user to the session and commit it to the database
        db.session.add(new_payment_type)
        db.session.commit()

        return jsonify({"message": "User created successfully!"}), 201