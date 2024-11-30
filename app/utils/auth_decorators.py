from functools import wraps
from flask import request, jsonify
from app.services.jwt_utils import decode_jwt

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Token is missing!"}), 403
        token = token.split(" ")[1]  # Expecting "Bearer <token>"

        result = decode_jwt(token)
        if result["status"] == "error":
            return jsonify({"error": result["message"]}), 401

        request.user = result["data"]
        return f(*args, **kwargs)

    return decorated_function
