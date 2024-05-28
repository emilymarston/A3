from flask import Blueprint, jsonify, request, abort
from models import Membership

membership_routes = Blueprint('membership_routes', __name__)

@membership_routes.route('/memberships', methods=['GET'])
def get_memberships():
    memberships = Membership.query.all()
    return jsonify([membership.get_membership_details() for membership in memberships])

@membership_routes.route('/memberships/<int:membership_id>', methods=['GET'])
def get_membership_details(membership_id):
    membership = Membership.query.get_or_404(membership_id)
    return jsonify(membership.get_membership_details())

@membership_routes.route('/memberships', methods=['POST'])
def sign_up_membership():
    data = request.json
    customer_id = data.get('customer_id')
    membership_type = data.get('membership_type')
    if not customer_id or not membership_type:
        abort(400, description="Customer ID and membership type are required")
    Membership.sign_up_membership(customer_id, membership_type)
    return jsonify(message="Membership signed up successfully"), 201

@membership_routes.route('/memberships/<int:customer_id>/status', methods=['GET'])
def check_membership_status(customer_id):
    has_membership = Membership.has_membership(customer_id)
    if has_membership:
        return jsonify(status="Active")
    else:
        return jsonify(status="Inactive")
