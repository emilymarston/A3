from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

class Employee(db.Model):
    __tablename__ = 'employees'

    employeeID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': role
    }

    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number

    def to_dict(self):
        return {    
            "id": self.employeeID,
            "name": self.name,
            "role": self.role,
            "contact_number": self.contact_number
        }
    
    def start_work():
        start_time = datetime.now()
        return start_time

    def end_work():
        end_time = datetime.now()
        return end_time
        
    def update_order_status(self, order, status):
        order.status = status
        order.save()

    def get_order_id(order):
        return order.id