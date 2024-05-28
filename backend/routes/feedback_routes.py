from flask import Blueprint, request, jsonify
from . import db
from models import Feedback

feedback_routes = Blueprint('feedback_routes', __name__)

@feedback_routes.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    customer_id = data.get('customer_id')
    content = data.get('content')
    rating = data.get('rating')

    if not all([customer_id, content, rating]):
        return jsonify({"error": "Missing required data"}), 400

    try:
        Feedback.submit_feedback(customer_id, content, rating)
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
