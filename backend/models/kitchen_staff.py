from .db import db
from .employee import Employee
from .order import Order
from flask import abort

class KitchenStaff(Employee):
    __tablename__ = 'kitchen_staff'
    id = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'kitchen_staff',
    }

    def prepare_order(order_id):
        order = Order.query.get(order_id)
        if order is None:
            abort(404, "Order not found")

        if order.status != "Confirmed":
            abort(400, "Order must be confirmed before preparation")

        order.status = "In Preparation"
        db.session.commit()

        # perform additional actions like notifying the customer or updating inventory

        return "Order preparation started successfully"
