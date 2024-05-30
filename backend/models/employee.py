from .db import db
from datetime import datetime
from .reservation import Reservation

class Employee(db.Model):
    __tablename__ = 'employees'

    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(100), nullable=False)
    role                = db.Column(db.String(50), nullable=False)
    contact_number      = db.Column(db.String(15), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': role,
        'polymorphic_identity': 'employee'
    }

    def __init__(self, name, contact_number, role='employee'):
        self.name = name
        self.contact_number = contact_number
        self.role = role

    def to_dict(self):
        return {
            "id": self.employee_id,
            "name": self.name,
            "role": self.role,
            "contact_number": self.contact_number
        }

    def start_work(self):
        self.start_time = datetime.now()
        db.session.commit()
        return self.start_time

    def end_work(self):
        self.end_time = datetime.now()
        db.session.commit()
        return self.end_time

    def update_order_status(self, order, status):
        valid_statuses = ["Confirmed", "Pending", "Cancelled", "In Preparation", "Completed"]
        if status in valid_statuses:
            order.status = status
            db.session.commit()
        else:
            raise ValueError(f"Invalid status: {status}")

    def get_order_id(self, order):
        return order.id
