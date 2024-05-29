from . import db
from datetime import datetime
from .order import Order

class Bill(db.Model):
    __tablename__ = 'bills'

    bill_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    final_amount = db.Column(db.Float, nullable=False)
    discounts = db.Column(db.Float, default=0.0)
    taxes = db.Column(db.Float, default=0.0)
    service_charges = db.Column(db.Float, default=0.0)
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow)

    order = db.relationship('Order', back_populates='bill')

    def __init__(self, order_id, total_amount):
        self.order_id = order_id
        self.total_amount = total_amount
        self.final_amount = total_amount
        self.discounts = 0.0
        self.taxes = 0.0
        self.service_charges = 0.0

    def to_dict(self):
        return {
            "bill_id": self.bill_id,
            "order_id": self.order_id,
            "total_amount": self.total_amount,
            "final_amount": self.final_amount,
            "discounts": self.discounts,
            "taxes": self.taxes,
            "service_charges": self.service_charges,
            "transaction_date": self.transaction_date
        }

    def calculate_final_amount(self):
        self.final_amount = (self.total_amount - self.discounts) + self.taxes + self.service_charges
        db.session.commit()
        return self.final_amount

    def apply_discount(self, discount):
        self.discounts += discount
        self.calculate_final_amount()

    def add_service_charge(self, charge):
        self.service_charges += charge
        self.calculate_final_amount()

    def set_order_details(self, order_id):
        self.order_id = order_id
        order = Order.query.get(order_id)
        if order:
            self.total_amount = order.total_amount
            self.final_amount = self.total_amount
            db.session.commit()

    def apply_surcharge(self, surcharge):
        self.taxes += surcharge
        self.calculate_final_amount()

    def get_order_details(self):
        order = Order.query.get(self.order_id)
        if order:
            return order.to_dict()
        return None
