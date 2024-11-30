from sqlalchemy.exc import IntegrityError
from flask import Blueprint, request, jsonify,render_template,redirect
from ..models.user import User
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash  # Import check_password_hash
from app.services.jwt_utils import encode_jwt


bp = Blueprint('dashboard', __name__)
# Route for the Dashboard page
@bp.route('/')
def dashboard():
    return render_template('dashboard.html')  # Serve the main dashboard page
#Route for submitting the payment form
@bp.route('/submit_payment', methods=['POST'])
def submit_payment():
    # Process the form data here (e.g., save to database)
    print("Form Submitted")
    return redirect(url_for('dashboard'))  # Redirect to dashboard after submission

