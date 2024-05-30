from .db import db
from datetime import datetime
from .asset import Asset

class Reservation(db.Model):
    __tablename__ = 'reservations'

    reservation_id      = db.Column(db.Integer, primary_key=True)
    reservation_date    = db.Column(db.DateTime, nullable=False)
    table_number        = db.Column(db.Integer, db.ForeignKey('assets.id'), nullable=False)
    number_of_guests    = db.Column(db.Integer, nullable=False)

    table = db.relationship('Asset')

    def __init__(self, reservation_date, table_number, number_of_guests):
        self.reservation_date = reservation_date
        self.table_number = table_number
        self.number_of_guests = number_of_guests

    def to_dict(self):
        return {
            "reservation_id": self.reservation_id,
            "reservation_date": self.reservation_date,
            "table_number": self.table_number,
            "number_of_guests": self.number_of_guests
        }

    def confirm_reservation(self):
        print(f"Reservation {self.reservation_id} confirmed.")

    def cancel_reservation(self):
        db.session.delete(self)
        db.session.commit()
        print(f"Reservation {self.reservation_id} canceled.")

    def update_reservation(self, new_date, new_time):
        self.reservation_date = datetime.combine(new_date, new_time)
        db.session.commit()
        print(f"Reservation {self.reservation_id} updated to {self.reservation_date}.")

    @staticmethod
    def available_table(new_date, new_time, number_of_guests):
        all_assets = Asset.query.all()

        # Check availability for each asset
        for asset in all_assets:
            # Check if the asset is available and can accommodate the specified number of guests
            if asset.is_available(number_of_guests):
                return True  # Table is available
        return False  # No available table found