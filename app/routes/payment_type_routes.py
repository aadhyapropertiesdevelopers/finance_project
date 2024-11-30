from flask import Blueprint, request, jsonify

from services.payment_type_service import (
    add_payment_type, 
    get_all_payment_types, 
    get_payment_type_by_id, 
    update_payment_type, 
    delete_payment_type
)

payment_type_bp = Blueprint('payment_type', __name__)

@payment_type_bp.route('/payment-types', methods=['GET'])
def list_payment_types():
    return jsonify(get_all_payment_types())

@payment_type_bp.route('/payment-types', methods=['POST'])
def create_payment_type():
    data = request.json
    payment_type = add_payment_type(data)
    return jsonify(payment_type.to_dict()), 201

@payment_type_bp.route('/payment-types/<int:payment_type_id>', methods=['GET'])
def get_payment_type(payment_type_id):
    payment_type = get_payment_type_by_id(payment_type_id)
    if payment_type:
        return jsonify(payment_type)
    return jsonify({"error": "Payment type not found"}), 404

@payment_type_bp.route('/payment-types/<int:payment_type_id>', methods=['PUT'])
def update_payment_type_route(payment_type_id):
    data = request.json
    updated_payment_type = update_payment_type(payment_type_id, data)
    if updated_payment_type:
        return jsonify(updated_payment_type)
    return jsonify({"error": "Payment type not found"}), 404

@payment_type_bp.route('/payment-types/<int:payment_type_id>', methods=['DELETE'])
def delete_payment_type_route(payment_type_id):
    if delete_payment_type(payment_type_id):
        return jsonify({"message": "Payment type deleted successfully"})
    return jsonify({"error": "Payment type not found"}), 404
