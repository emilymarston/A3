from flask import Blueprint, request, jsonify, abort
from . import db
from models import CustomerDataRecord, Feedback, Customer

customer_record_routes = Blueprint('customer_record_routes', __name__)

# Create an instance of CustomerRecordData
customer_record_data = CustomerDataRecord()

@customer_record_routes.route('/customer/feedback', methods=['POST'])
def add_feedback():
    data = request.json
    try:
        feedback = Feedback(**data)
        customer_record_data.addFeedback(feedback)
        return jsonify(feedback.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@customer_record_routes.route('/customer/membership', methods=['POST'])
def add_membership():
    data = request.json
    try:
        membership = Membership(**data)
        customer_record_data.addMembership(membership)
        return jsonify(membership.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@customer_record_routes.route('/customer', methods=['POST'])
def add_customer():
    data = request.json
    try:
        customer = Customer(**data)
        customer_record_data.addCustomer(customer)
        return jsonify(customer.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))
