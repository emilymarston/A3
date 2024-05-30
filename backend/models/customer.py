from .db import db
from .order import Order
from .reservation import Reservation

class Customer(db.Model):
    __tablename__ = 'customers'

    customer_id     = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(100), nullable=False)
    contact_info    = db.Column(db.String(50), nullable=False)
    address         = db.Column(db.String(200))
    has_membership  = db.Column(db.Boolean, default=False)

    orders = db.relationship('Order', backref='customer')  # Define relationship with Order
    reservations = db.relationship('Reservation', backref='customer')  # Define relationship with Reservation

    def place_order(self, order_items, order_type):
        order = Order(customer_id=self.customer_id, order_items=order_items, order_type=order_type)
        db.session.add(order)
        db.session.commit()
        return order

    def toggle_membership(self):
        self.has_membership = not self.has_membership
        db.session.commit()

    def get_membership_status(self):
        return self.has_membership
