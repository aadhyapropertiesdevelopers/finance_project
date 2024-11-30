import jwt
import datetime
import os
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_unsafe_secret")  # Replace fallback in production!


def encode_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
        "iat": datetime.datetime.utcnow(),
        "iss": "your-app"
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def decode_jwt(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], issuer="your-app")
        return {"status": "success", "data": decoded}
    except ExpiredSignatureError:
        return {"status": "error", "message": "Token has expired"}
    except InvalidTokenError:
        return {"status": "error", "message": "Invalid token"}
