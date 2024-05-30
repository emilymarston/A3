from . import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    order_id        = db.Column(db.Integer, primary_key=True)
    order_date      = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    customer_id     = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    order_status    = db.Column(db.String(50), nullable=False)
    order_items     = db.Column(db.Text, nullable=False)
    order_type      = db.Column(db.String(50), nullable=False)

    bill = db.relationship('Bill', back_populates='order', uselist=False)

    def __init__(self, customer_id, order_status, order_items, order_type):
        self.customer_id = customer_id
        self.order_status = order_status
        self.order_items = order_items
        self.order_type = order_type

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "order_date": self.order_date.strftime("%d-%m-%Y"),  # Format the date as 'YYYY-MM-DD'
            "customer_id": self.customer_id,
            "order_status": self.order_status,
            "order_items": self.order_items,
            "order_type": self.order_type
        }

    def update_status(self, new_status):
        self.order_status = new_status
        db.session.commit()

    def add_item(self, item_id, quantity):
        items = json.loads(self.order_items)
        if item_id in items:
            items[item_id] += quantity
        else:
            items[item_id] = quantity
        self.order_items = json.dumps(items)
        db.session.commit()

    def remove_item(self, item_id, quantity):
        items = json.loads(self.order_items)
        if item_id in items:
            if items[item_id] <= quantity:
                del items[item_id]
            else:
                items[item_id] -= quantity
            self.order_items = json.dumps(items)
            db.session.commit()

    def get_order_id(self):
        return self.order_id
