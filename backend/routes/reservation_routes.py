from flask import Blueprint, request, jsonify, abort
from models import db
from models.reservation import Reservation
from datetime import datetime

reservation_routes = Blueprint('reservation_routes', __name__)

@reservation_routes.route('/reservations', methods=['GET'])
def get_reservations():
    try:
        reservations = Reservation.query.all()
        return jsonify([reservation.to_dict() for reservation in reservations]), 200
    except Exception as e:
        abort(500, description=str(e))

@reservation_routes.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    try:
        reservation = Reservation.query.get_or_404(id)
        return jsonify(reservation.to_dict()), 200
    except Exception as e:
        abort(500, description=str(e))

@reservation_routes.route('/reservations', methods=['POST'])
def create_reservation():
    try:
        data = request.json  # Assuming JSON data is sent from frontend
        if not data:
            abort(400, description='No JSON data provided')
        
        # Validate required fields
        required_fields = ['name', 'phoneNumber', 'date', 'time', 'numbOfPeople', 'specialRequests']
        for field in required_fields:
            if field not in data:
                abort(400, description=f'Missing required field: {field}')

        reservation_date = datetime.strptime(data['date'] + ' ' + data['time'], '%Y-%m-%d %H:%M')
        reservation = Reservation(
            name=data['name'],
            phone_number=data['phoneNumber'],
            reservation_date=reservation_date,
            numb_of_people=data['numbOfPeople'],
            special_requests=data['specialRequests']
        )
        db.session.add(reservation)
        db.session.commit()
        return jsonify(reservation.to_dict()), 201
    except Exception as e:
        abort(500, description=str(e))

@reservation_routes.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    try:
        reservation = Reservation.query.get_or_404(id)
        data = request.json
        if not data:
            abort(400, description='No JSON data provided')

        new_date = datetime.strptime(data['reservation_date'], '%Y-%m-%d %H:%M:%S')
        reservation.update_reservation(new_date=new_date)
        return jsonify(reservation.to_dict()), 200
    except Exception as e:
        abort(500, description=str(e))

@reservation_routes.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    try:
        reservation = Reservation.query.get_or_404(id)
        reservation.cancel_reservation()
        return '', 204
    except Exception as e:
        abort(500, description=str(e))
