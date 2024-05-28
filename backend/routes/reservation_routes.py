from flask import Blueprint, request, jsonify, abort
from . import db
from models import Reservation
from datetime import datetime

reservation_routes = Blueprint('reservation_routes', __name__)

@reservation_routes.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations])

@reservation_routes.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    return jsonify(reservation.to_dict())

@reservation_routes.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    try:
        reservation_date = datetime.strptime(data['reservation_date'], '%Y-%m-%d %H:%M:%S')
        reservation = Reservation(reservation_date=reservation_date, 
                                  table_number=data['table_number'], 
                                  number_of_guests=data['number_of_guests'])
        db.session.add(reservation)
        db.session.commit()
        return jsonify(reservation.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@reservation_routes.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    data = request.json
    try:
        new_date = datetime.strptime(data['reservation_date'], '%Y-%m-%d %H:%M:%S')
        reservation.update_reservation(new_date=new_date)
        return jsonify(reservation.to_dict())
    except Exception as e:
        abort(400, description=str(e))

@reservation_routes.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    reservation.cancel_reservation()
    return '', 204
