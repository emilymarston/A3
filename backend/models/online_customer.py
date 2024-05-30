from .db import db
from .customer import Customer
from .order import Order

class OnlineCustomer(Customer):
    __tablename__ = 'online_customers'
    __mapper_args__ = {
        'polymorphic_identity': 'online_customer',
    }

    id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), primary_key=True)
    delivery = db.Column(db.Boolean, default=False)
    takeaway = db.Column(db.Boolean, default=False)

    def is_delivery(self):
        return self.delivery

    def is_takeaway(self):
        return self.takeaway

    def view_order(self, order_id):
        order = Order.query.filter_by(customer_id=self.customer_id, order_id=order_id).first()
        if order:
            return order.to_dict()
        else:
            return None
