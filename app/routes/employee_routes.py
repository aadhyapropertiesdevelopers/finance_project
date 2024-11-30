from flask import Blueprint, request, jsonify
from services.employee_service import add_employee, get_all_employees, get_employee_by_id, update_employee, delete_employee

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['GET'])
def list_employees():
    return jsonify(get_all_employees())

@employee_bp.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee = add_employee(data)
    return jsonify(employee.to_dict()), 201

@employee_bp.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = get_employee_by_id(emp_id)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404

@employee_bp.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee_route(emp_id):
    data = request.json
    updated_employee = update_employee(emp_id, data)
    if updated_employee:
        return jsonify(updated_employee)
    return jsonify({"error": "Employee not found"}), 404

@employee_bp.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee_route(emp_id):
    if delete_employee(emp_id):
        return jsonify({"message": "Employee deleted successfully"})
    return jsonify({"error": "Employee not found"}), 404
