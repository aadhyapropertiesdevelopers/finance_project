
from sqlite3 import IntegrityError
from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db
from ..services.user_service import user_post_method

bp = Blueprint('payment_types', __name__)

@bp.route('/payments_type', methods=['POST'])
def create_payment_type():
    try:
        # Get data from request
        data = request.get_json()
        payment_type_name = data['payment_type_name']
        status = data['status']
        response = user_post_method(payment_type_name,status)
        return response
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists in the database."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

