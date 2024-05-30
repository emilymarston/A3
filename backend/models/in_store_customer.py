from .db import db
from .customer import Customer

class InStoreCustomer(Customer):
    __tablename__ = 'instore_customers'
    __mapper_args__ = {
        'polymorphic_identity': 'instore_customer',
    }

    id = db.Column(db.Integer, db.ForeignKey('customers.customer_id'), primary_key=True)
    reservation_made = db.Column(db.Boolean, default=False)

    def made_reservation(self):
        self.reservation_made = True
        db.session.commit()

    def has_made_reservation(self):
        return self.reservation_made
