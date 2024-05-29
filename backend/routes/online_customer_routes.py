from flask import Blueprint, request, jsonify, abort
from . import db
from models import OnlineCustomer, Order

online_customer_routes = Blueprint('online_customer_routes', __name__)

@online_customer_routes.route('/online_customers', methods=['GET'])
def get_online_customers():
    customers = OnlineCustomer.query.all()
    return jsonify([customer.to_dict() for customer in customers])

@online_customer_routes.route('/online_customers/<int:customer_id>', methods=['GET'])
def get_online_customer(customer_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict())

@online_customer_routes.route('/online_customers', methods=['POST'])
def create_online_customer():
    data = request.json
    try:
        customer = OnlineCustomer(name=data['name'], contact_info=data['contact_info'], address=data['address'], delivery=data['delivery'], takeaway=data['takeaway'])
        db.session.add(customer)
        db.session.commit()
        return jsonify(customer.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@online_customer_routes.route('/online_customers/<int:customer_id>/is_delivery', methods=['GET'])
def is_delivery(customer_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    return jsonify({"is_delivery": customer.is_delivery()})

@online_customer_routes.route('/online_customers/<int:customer_id>/is_takeaway', methods=['GET'])
def is_takeaway(customer_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    return jsonify({"is_takeaway": customer.is_takeaway()})

@online_customer_routes.route('/online_customers/<int:customer_id>/view_order/<int:order_id>', methods=['GET'])
def view_order(customer_id, order_id):
    customer = OnlineCustomer.query.get_or_404(customer_id)
    order = customer.view_order(order_id)
    if order:
        return jsonify(order)
    else:
        abort(404, description="Order not found")
