from .employee import Employee
from . import db
from .order import Order

class DeliveryStaff(Employee):
    __tablename__ = 'deliverystaff'
    id                          = db.Column(db.Integer, db.ForeignKey('employees.id'), primary_key=True)
    vehicle_number_plate        = db.Column(db.String(10))
    delivery_area               = db.Column(db.String(100))
    current_location_latitude   = db.Column(db.Float)
    current_location_longitude  = db.Column(db.Float)

    __mapper_args__ = {
        'polymorphic_identity': 'deliverystaff',
    }

    def __init__(self, name, contact_number, vehicle_plate_number, delivery_area):
        super().__init__(name, contact_number)
        self.vehicle_number_plate = vehicle_plate_number
        self.delivery_area = delivery_area

    def deliver_order(self, order_id):
        order = Order.query.get(order_id)
        if order is None:
            return "Order not found"

        # Check if the order is assigned to this delivery staff
        if order.delivery_staff_id != self.id:
            return "This order is not assigned to you"

        # Check if the order is ready for delivery
        if order.status != "In Preparation" and order.status != "Ready":
            return "Order is not ready for delivery"

        # Update order status
        order.status = "Out for Delivery"
        db.session.commit()

        return "Order successfully marked as out for delivery"

    # Update the current location of the delivery staff
    def update_delivery_location(self, new_latitude, new_longitude):
        self.current_location_latitude = new_latitude
        self.current_location_longitude = new_longitude
        db.session.commit()