from .db import db
from datetime import datetime

class Membership(db.Model):
    __tablename__ = 'memberships'

    membership_id       = db.Column(db.Integer, primary_key=True)
    customer_id         = db.Column(db.Integer, nullable=False)
    membership_type     = db.Column(db.String(100), nullable=False)
    start_date          = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def get_membership_details(self):
        return {
            "membership_id": self.membership_id,
            "customer_id": self.customer_id,
            "membership_type": self.membership_type,
            "start_date": self.start_date.isoformat()
        }

    # update based on customer class
    def check_membership_status(self):
        current_date = datetime.utcnow()
        if current_date < self.start_date:
            return "Pending"
        else:
            # Add logic to check if the membership is still active based on business rules
            # For example, check if the membership is expired or if the customer has renewed it
            return "Active"  # Placeholder, update with actual logic

    @staticmethod
    def sign_up_membership(customer_id, membership_type):
        new_membership = Membership(customer_id=customer_id, membership_type=membership_type)
        db.session.add(new_membership)
        db.session.commit()

    @staticmethod
    def has_membership(customer_id):
        return Membership.query.filter_by(customer_id=customer_id).first() is not None
