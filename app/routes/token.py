from flask import Blueprint, request, jsonify
from app.services.jwt_utils import decode_jwt  # Import decode_jwt function

bp = Blueprint('token', __name__)  # Unique name 'token'

@bp.route('/validate', methods=['POST'])
def validate_token():
    try:
        # Get the token from the request
        data = request.get_json()
        token = data.get('token')

        # Validate the token
        result = decode_jwt(token)

        if result["status"] == "success":
            return jsonify({
                "message": "Token is valid",
                "data": result["data"]
            }), 200
        else:
            return jsonify({
                "error": result["message"]
            }), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 400
