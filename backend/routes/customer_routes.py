from flask import Blueprint, request, jsonify, abort
from . import db
from models import Customer, InStoreCustomer, OnlineCustomer

customer_routes = Blueprint('customer_routes', __name__)

@customer_routes.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customer_type = data.pop('type', None)

    if customer_type == 'instore':
        customer = InStoreCustomer(**data)
    elif customer_type == 'online':
        customer = OnlineCustomer(**data)
    else:
        customer = Customer(**data)

    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@customer_routes.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict())

@customer_routes.route('/customers/<int:customer_id>/place_order', methods=['POST'])
def place_order(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    data = request.json
    order_items = data.get('order_items')
    order_type = data.get('order_type')
    order = customer.place_order(order_items, order_type)
    return jsonify(order.to_dict()), 201

@customer_routes.route('/customers/<int:customer_id>/has_membership', methods=['GET'])
def has_membership(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({'has_membership': customer.has_membership()})

@customer_routes.route('/customers/instore/<int:customer_id>/made_reservation', methods=['POST'])
def made_reservation(customer_id):
    customer = InStoreCustomer.query.get_or_404(customer_id)
    customer.made_reservation()
    return '', 204

@customer_routes.route('/customers/instore/<int:customer_id>/has_made_reservation', methods=['GET'])
def has_made_reservation(customer_id):
    customer = InStoreCustomer.query.get_or_404(customer_id)
    return jsonify({'has_made_reservation': customer.has_made_reservation()})

@customer_routes.route('/customers/online/<int:customer_id>/is_delivery', methods=['GET'])
def is_delivery(customer_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    return jsonify({'is_delivery': customer.is_delivery()})

@customer_routes.route('/customers/online/<int:customer_id>/is_takeaway', methods=['GET'])
def is_takeaway(customer_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    return jsonify({'is_takeaway': customer.is_takeaway()})

@customer_routes.route('/customers/online/<int:customer_id>/view_order/<int:order_id>', methods=['GET'])
def view_order(customer_id, order_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    order = customer.view_order(order_id)
    if order:
        return jsonify(order)
    else:
        abort(404, description="Order not found")
