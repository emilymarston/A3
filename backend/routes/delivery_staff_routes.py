from flask import Blueprint, jsonify, request, abort
from . import db
from models import DeliveryStaff, Order

deliverystaff_routes = Blueprint('deliverystaff_routes', __name__)

@deliverystaff_routes.route('/deliverystaff/orders/<int:order_id>/deliver', methods=['PUT'])
def deliver_order(order_id):
    delivery_staff = DeliveryStaff.query.first()
    if not delivery_staff:
        abort(404, description="Delivery staff not found")

    order = Order.query.get(order_id)
    if not order:
        abort(404, description="Order not found")

    if order.delivery_staff_id != delivery_staff.id:
        abort(403, description="This order is not assigned to you")

    if order.status != "In Preparation" and order.status != "Ready":
        abort(400, description="Order is not ready for delivery")

    order.status = "Out for Delivery"
    db.session.commit()

    return jsonify({'message': "Order successfully marked as out for delivery"})

@deliverystaff_routes.route('/deliverystaff/location', methods=['PUT'])
def update_delivery_location():
    data = request.json
    delivery_staff = DeliveryStaff.query.first()
    if not delivery_staff:
        abort(404, description="Delivery staff not found")

    delivery_staff.update_delivery_location(data.get('latitude'), data.get('longitude'))
    return '', 204
