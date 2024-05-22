from . import db
from datetime import datetime

class Reservation(db.Model):
    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True)
    reservation_date = db.Column(db.DateTime, nullable=False)
    table_number = db.Column(db.Integer, nullable=False)
    number_of_guests = db.Column(db.Integer, nullable=False)

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
    
    # Add logic to confirm the reservation
    def confirm_reservation(self):
        print(f"Reservation {self.reservation_id} confirmed.")
    
    # Add logic to cancel the reservation
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
        # Add logic to check for available tables
        reservations = Reservation.query.filter(
            Reservation.reservation_date == datetime.combine(new_date, new_time),
            Reservation.number_of_guests == number_of_guests
        ).all()
        if reservations:
            return False  # Table is not available
        return True  # Table is available
