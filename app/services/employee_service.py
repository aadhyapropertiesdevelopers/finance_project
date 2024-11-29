# /app/services/employee_service.py

from flask import jsonify  # Import jsonify
from ..models.employee import Employee
from .. import db

def employee_post_method(name, email, phone_number, address, branch_name, role):
    try:
        # Create a new employee object
        new_employee = Employee(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            branch_name=branch_name,
            role=role
        )
        
        # Add to the session and commit
        db.session.add(new_employee)
        db.session.commit()

        return jsonify({"message": "Employee created successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
