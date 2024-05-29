from flask import Blueprint, request, jsonify, abort
from . import db
from models import Order

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@order_routes.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify(order.to_dict())

@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    try:
        order = Order(
            customer_id=data['customer_id'],
            order_status=data['order_status'],
            order_items=json.dumps(data['order_items']),  # Convert list/dict to JSON string
            order_type=data['order_type']
        )
        db.session.add(order)
        db.session.commit()
        return jsonify(order.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@order_routes.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json
    try:
        order.update_status(data['new_status'])
        return jsonify(order.to_dict())
    except Exception as e:
        abort(400, description=str(e))

@order_routes.route('/orders/<int:order_id>/items', methods=['PUT'])
def add_order_item(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json
    try:
        order.add_item(data['item_id'], data['quantity'])
        return jsonify(order.to_dict())
    except Exception as e:
        abort(400, description=str(e))

@order_routes.route('/orders/<int:order_id>/items', methods=['DELETE'])
def remove_order_item(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json
    try:
        order.remove_item(data['item_id'], data['quantity'])
        return jsonify(order.to_dict())
    except Exception as e:
        abort(400, description=str(e))

@order_routes.route('/orders/<int:order_id>/get_id', methods=['GET'])
def get_order_id(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify({"order_id": order.get_order_id()})
