from flask import Blueprint, request, jsonify, abort
from . import db
from models import InStoreCustomer

in_store_customer_routes = Blueprint('in_store_customer_routes', __name__)

@in_store_customer_routes.route('/in_store_customers', methods=['GET'])
def get_in_store_customers():
    customers = InStoreCustomer.query.all()
    return jsonify([customer.to_dict() for customer in customers])

@in_store_customer_routes.route('/in_store_customers/<int:customer_id>', methods=['GET'])
def get_in_store_customer(customer_id):
    customer = InStoreCustomer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict())

@in_store_customer_routes.route('/in_store_customers', methods=['POST'])
def create_in_store_customer():
    data = request.json
    try:
        customer = InStoreCustomer(name=data['name'], contact_info=data['contact_info'], address=data['address'])
        db.session.add(customer)
        db.session.commit()
        return jsonify(customer.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@in_store_customer_routes.route('/in_store_customers/<int:customer_id>/made_reservation', methods=['GET'])
def made_reservation(customer_id):
    customer = InStoreCustomer.query.get_or_404(customer_id)
    return jsonify({"made_reservation": customer.made_reservation()})

@in_store_customer_routes.route('/in_store_customers/<int:customer_id>/has_made_reservation', methods=['GET'])
def has_made_reservation(customer_id):
    customer = InStoreCustomer.query.get_or_404(customer_id)
    return jsonify({"has_made_reservation": customer.has_made_reservation()})
