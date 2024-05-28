from flask import Blueprint, jsonify, abort
from . import db
from .models import KitchenStaff, Order

kitchenstaff_routes = Blueprint('kitchenstaff_routes', __name__)

@kitchenstaff_routes.route('/kitchenstaff/orders/<int:order_id>/prepare', methods=['PUT'])
def prepare_order(order_id):
    kitchen_staff = KitchenStaff.query.first()
    if not kitchen_staff:
        abort(404, description="Kitchen staff not found")

    order = Order.query.get(order_id)
    if not order:
        abort(404, description="Order not found")

    if order.status != "Confirmed":
        abort(400, description="Order must be confirmed before preparation")

    order.status = "In Preparation"
    db.session.commit()

    # Perform additional actions like notifying the customer or updating inventory

    return jsonify({'message': "Order preparation started successfully"})
