from sqlite3 import IntegrityError
from flask import Blueprint, request, jsonify
from ..models.employee import Employee  # Assuming Employee model exists
from .. import db
from ..services.employee_service import employee_post_method  # Assuming employee_post_method exists

bp = Blueprint('emp_table', __name__)


# POST method to create an employee
@bp.route('/employees', methods=['POST'])
def create_employee():
    try:
        # Get data from request
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        address = data['address']
        branch_name = data['branch_name']
        role = data['role']
        
        # Assuming you have a function to handle the POST logic
        response = employee_post_method(name, email, phone_number, address, branch_name, role)
        return response
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists in the database."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# GET method to fetch all employees
@bp.route('/employees', methods=['GET'])
def get_employees():
    try:
        # Query all employees from the database
        employees = Employee.query.all()

        # Convert the result to a list of dictionaries
        employees_list = [{
            "id": emp.id,
            "name": emp.name,
            "email": emp.email,
            "phone_number": emp.phone_number,
            "address": emp.address,
            "branch_name": emp.branch_name,
            "role": emp.role
        } for emp in employees]

        return jsonify(employees_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
