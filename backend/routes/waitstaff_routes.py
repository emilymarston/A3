from flask import Blueprint, jsonify, request, abort
from . import db
from .models import Waitstaff, Reservation, Order, Membership
from datetime import datetime

waitstaff_routes = Blueprint('waitstaff_routes', __name__)

@waitstaff_routes.route('/waitstaff/reservations/<int:reservation_id>/confirm', methods=['PUT'])
def confirm_reservation(reservation_id):
    waitstaff = Waitstaff.query.first()  # Assuming there is only one waitstaff for simplicity
    if not waitstaff:
        abort(404, description="Waitstaff not found")
    
    waitstaff.manage_reservation(reservation_id)
    return '', 204

@waitstaff_routes.route('/waitstaff/orders/<int:order_id>/serve', methods=['PUT'])
def serve_order(order_id):
    waitstaff = Waitstaff.query.first()
    if not waitstaff:
        abort(404, description="Waitstaff not found")
    
    waitstaff.serve_order(order_id)
    return '', 204

@waitstaff_routes.route('/waitstaff/orders', methods=['POST'])
def take_order():
    data = request.json
    waitstaff = Waitstaff.query.first()
    if not waitstaff:
        abort(404, description="Waitstaff not found")
    
    order_id = waitstaff.take_order(data.get('customer_id'), data.get('menu_items'))
    return jsonify({'order_id': order_id}), 201

@waitstaff_routes.route('/waitstaff/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    data = request.json
    waitstaff = Waitstaff.query.first()
    if not waitstaff:
        abort(404, description="Waitstaff not found")
    
    waitstaff.update_reservation(reservation_id, data.get('new_date'), data.get('new_time'))
    return '', 204

@waitstaff_routes.route('/waitstaff/customers/<int:customer_id>/reservation', methods=['GET'])
def check_reservation(customer_id):
    waitstaff = Waitstaff.query.first()
    if not waitstaff:
        abort(404, description="Waitstaff not found")
    
    has_reservation = waitstaff.has_reservation(customer_id)
    return jsonify({'has_reservation': has_reservation})

@waitstaff_routes.route('/waitstaff/customers/<int:customer_id>/membership', methods=['GET'])
def check_membership(customer_id):
    waitstaff = Waitstaff.query.first()
    if not waitstaff:
        abort(404, description="Waitstaff not found")
    
    has_membership = waitstaff.has_membership(customer_id)
    return jsonify({'has_membership': has_membership})
