from .db import db
from datetime import datetime

class Membership(db.Model):
    __tablename__ = 'memberships'

    membership_id       = db.Column(db.Integer, primary_key=True)
    customer_id         = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), nullable=False)
    membership_type     = db.Column(db.String(100), nullable=False)
    start_date          = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def get_membership_details(self):
        return {
            "membership_id": self.membership_id,
            "customer_id": self.customer_id,
            "membership_type": self.membership_type,
            "start_date": self.start_date.isoformat()
        }

    @staticmethod
    def sign_up_membership(customer_id, membership_type):
        new_membership = Membership(customer_id=customer_id, membership_type=membership_type)
        db.session.add(new_membership)
        db.session.commit()

    @staticmethod
    def has_membership(customer_id):
        return Membership.query.filter_by(customer_id=customer_id).first() is not None