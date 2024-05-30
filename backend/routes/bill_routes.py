from flask import Blueprint, request, jsonify, abort
from . import db
from models import Bill

bill_routes = Blueprint('bill_routes', __name__)

@bill_routes.route('/bills', methods=['GET'])
def get_bills():
    bills = Bill.query.all()
    return jsonify([bill.to_dict() for bill in bills])

@bill_routes.route('/bills/<int:bill_id>', methods=['GET'])
def get_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    return jsonify(bill.to_dict())

@bill_routes.route('/bills', methods=['POST'])
def create_bill():
    data = request.json
    try:
        bill = Bill(
            order_id=data['order_id'],
            total_amount=data['total_amount']
        )
        db.session.add(bill)
        db.session.commit()
        return jsonify(bill.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@bill_routes.route('/bills/<int:bill_id>', methods=['PUT'])
def update_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    data = request.json
    try:
        if 'discounts' in data:
            bill.apply_discount(data['discounts'])
        if 'service_charges' in data:
            bill.add_service_charge(data['service_charges'])
        if 'taxes' in data:
            bill.apply_surcharge(data['taxes'])
        db.session.commit()
        return jsonify(bill.to_dict())
    except Exception as e:
        abort(400, description=str(e))

@bill_routes.route('/bills/<int:bill_id>', methods=['DELETE'])
def delete_bill(bill_id):
    bill = Bill.query.get_or_404(bill_id)
    db.session.delete(bill)
    db.session.commit()
    return '', 204
