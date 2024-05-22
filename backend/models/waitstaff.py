from .employee import Employee
from . import db
from datetime import datetime
from .reservation import Reservation
from .order import Order
from .membership import Membership
from flask import abort

class Waitstaff(Employee):
    __tablename__ = 'waitstaff'
    id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'waitstaff',
    }

    def manage_reservation(self, reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            reservation.confirm_reservation()
            db.session.commit()
        else:
            abort(404, description="Reservation not found")

    def serve_order(self, order_id):
        order = Order.query.get(order_id)
        if order:
            # Assuming an order status workflow
            order.status = 'Served'
            db.session.commit()
        else:
            abort(404, description="Order not found")

    def take_order(self, customer_id, menu_items):
        new_order = Order(customer_id=customer_id, menu_items=menu_items, status='Pending', created_at=datetime.utcnow())
        db.session.add(new_order)
        db.session.commit()
        return new_order.id

    def update_reservation(self, reservation_id, new_date, new_time):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            reservation.update_reservation(new_date, new_time)
        else:
            abort(404, description="Reservation not found")

    def has_reservation(self, customer_id):
        reservation = Reservation.query.filter_by(customer_id=customer_id).first()
        return reservation is not None

    def has_membership(self, customer_id):
        membership = Membership.query.filter_by(customer_id=customer_id).first()
        return membership is not None
