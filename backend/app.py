from flask import Flask
from flask_migrate import Migrate
from datetime import datetime

from models.db import db
from models.customer import Customer
from models.order import Order
from models.reservation import Reservation
from models.feedback import Feedback

from models.employee import Employee
from models.manager import Manager
from models.waitstaff import Waitstaff
from models.kitchen_staff import KitchenStaff
from models.delivery_staff import DeliveryStaff

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        import models
        db.drop_all()
        db.create_all()

        # Remove all data from the tables
        db.session.query(Customer).delete()
        db.session.query(Order).delete()
        db.session.query(Reservation).delete()
        db.session.query(Feedback).delete()
        db.session.query(Employee).delete()
        db.session.commit()

        # Add sample data for two customers with orders
        sample_customer1 = Customer(name="John Doe", contact_info="john@example.com", address="123 Glenferrie Road, Hawthorn, VIC 3122")
        db.session.add(sample_customer1)
        db.session.commit()

        sample_order1 = Order(customer_id=sample_customer1.customer_id, order_status="Preparing", order_items="Sandwich", order_type="Online")
        db.session.add(sample_order1)
        db.session.commit()

        sample_customer2 = Customer(name="Jane Smith", contact_info="jane@example.com", address="456 Glenferrie Road, Hawthorn, VIC 3122", has_membership=True)  # Set membership status
        db.session.add(sample_customer2)
        db.session.commit()

        sample_order2 = Order(customer_id=sample_customer2.customer_id, order_status="Delivered", order_items="Coffee", order_type="In-Store")
        db.session.add(sample_order2)
        db.session.commit()

        # Create and attach feedback instance to customer 2
        sample_feedback = Feedback(customer_id=sample_customer2.customer_id, rating=5, content="Great service!")
        db.session.add(sample_feedback)
        db.session.commit()

        # Add sample reservation
        sample_reservation2 = Reservation(reservation_date_str="11-03-2024", table_number=2, number_of_guests=3, customer_id=sample_customer2.customer_id)
        db.session.add(sample_reservation2)
        db.session.commit()

        # Add sample employees
        sample_employee1 = Employee(name="Alice Park", contact_number="0412 345 678", role="manager")
        db.session.add(sample_employee1)

        sample_employee2 = Employee(name="Peter Ng", contact_number="0423 456 789", role="kitchen_staff")
        db.session.add(sample_employee2)

        sample_employee3 = Employee(name="Max Wilson", contact_number="0434 567 890", role="waitstaff")
        db.session.add(sample_employee3)

        sample_employee4 = Employee(name="Olivia Taylor", contact_number="0445 678 901", role="delivery_staff")
        db.session.add(sample_employee4)
        db.session.commit()

    @app.route('/')
    def hello_world():
        # Fetch data from the tables
        customers = Customer.query.all()
        orders = Order.query.all()
        reservations = Reservation.query.all()
        feedbacks = Feedback.query.all()
        employees = Employee.query.all()

        # Render the data as HTML table with headings
        html_content = "<style> table { border-collapse: collapse; } th, td { padding: 5px; } </style>"
        html_content += "<h2>Customers</h2>"
        html_content += "<table border='1'>"
        html_content += "<tr><th>Customer ID</th><th>Name</th><th>Contact Information</th><th>Address</th><th>Membership Status</th></tr>"
        for customer in customers:
            html_content += f"<tr><td>{customer.customer_id}</td><td>{customer.name}</td><td>{customer.contact_info}</td><td>{customer.address}</td><td>{customer.get_membership_status()}</td></tr>"
        html_content += "</table>"
        
        # Display reservations data
        html_content += "<h2>Reservations</h2>"
        html_content += "<table border='1'>"
        html_content += "<tr><th>Reservation ID</th><th>Reservation Date</th><th>Table Number</th><th>Number of Guests</th><th>Customer ID</th></tr>"
        for reservation in reservations:
            html_content += f"<tr><td>{reservation.reservation_id}</td><td>{reservation.reservation_date}</td><td>{reservation.table_number}</td><td>{reservation.number_of_guests}</td><td>{reservation.customer_id}</td></tr>"
        html_content += "</table>"

        # Display orders data
        html_content += "<h2>Orders</h2>"
        html_content += "<table border='1'>"
        html_content += "<tr><th>Order ID</th><th>Order Date</th><th>Customer ID</th><th>Order Status</th><th>Items</th><th>Order Type</th></tr>"
        for order in orders:
            html_content += f"<tr><td>{order.order_id}</td><td>{order.order_date.strftime('%Y-%m-%d')}</td><td>{order.customer_id}</td><td>{order.order_status}</td><td>{order.order_items}</td><td>{order.order_type}</td></tr>"
        html_content += "</table>"

        # Display feedbacks data
        html_content += "<h2>Feedback</h2>"
        html_content += "<table border='1'>"
        html_content += "<tr><th>Feedback ID</th><th>Customer ID</th><th>Rating</th><th>Comment</th></tr>"
        for feedback in feedbacks:
            html_content += f"<tr><td>{feedback.id}</td><td>{feedback.customer_id}</td><td>{feedback.rating}</td><td>{feedback.content}</td></tr>"
        html_content += "</table>"
        html_content += "<br><br>"

        # Display employee data
        html_content += "<h2>Employees</h2>"
        html_content += "<table border='1'>"
        html_content += "<tr><th>ID</th><th>Name</th><th>Role</th><th>Contact Number</th></tr>"
        for employee in employees:
            html_content += f"<tr><td>{employee.id}</td><td>{employee.name}</td><td>{employee.role}</td><td>{employee.contact_number}</td></tr>"
        html_content += "</table>"

        return html_content

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
