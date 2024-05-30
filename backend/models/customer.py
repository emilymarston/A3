from .db import db
from .order import Order

class Customer(db.Model):
    __tablename__ = 'customers'
    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'polymorphic_on': 'type'
    }

    customer_id     = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(100), nullable=False)
    contact_info    = db.Column(db.String(50), nullable=False)
    address         = db.Column(db.String(200))
    has_membership  = db.Column(db.Boolean, default=False)  # New column for membership status
    type            = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
        'polymorphic_on': type
    }

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
