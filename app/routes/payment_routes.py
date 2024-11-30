from flask import Blueprint, request, jsonify
from services.payment_service import (
    add_payment_voucher, 
    get_all_payment_vouchers, 
    get_payment_voucher_by_id, 
    update_payment_voucher, 
    delete_payment_voucher
)

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payments', methods=['GET'])
def list_payment_vouchers():
    return jsonify(get_all_payment_vouchers())

@payment_bp.route('/payments', methods=['POST'])
def create_payment_voucher():
    data = request.json
    voucher = add_payment_voucher(data)
    return jsonify(voucher.to_dict()), 201

@payment_bp.route('/payments/<int:voucher_id>', methods=['GET'])
def get_payment_voucher(voucher_id):
    voucher = get_payment_voucher_by_id(voucher_id)
    if voucher:
        return jsonify(voucher)
    return jsonify({"error": "Payment voucher not found"}), 404

@payment_bp.route('/payments/<int:voucher_id>', methods=['PUT'])
def update_payment_voucher_route(voucher_id):
    data = request.json
    updated_voucher = update_payment_voucher(voucher_id, data)
    if updated_voucher:
        return jsonify(updated_voucher)
    return jsonify({"error": "Payment voucher not found"}), 404

@payment_bp.route('/payments/<int:voucher_id>', methods=['DELETE'])
def delete_payment_voucher_route(voucher_id):
    if delete_payment_voucher(voucher_id):
        return jsonify({"message": "Payment voucher deleted successfully"})
    return jsonify({"error": "Payment voucher not found"}), 404
