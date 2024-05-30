from flask import Blueprint

# Define blueprints
employee_routes = Blueprint('employee_routes', __name__)
manager_routes = Blueprint('manager_routes', __name__)
waitstaff_routes = Blueprint('waitstaff_routes', __name__)
kitchen_staff_routes = Blueprint('kitchen_staff_routes', __name__)
delivery_staff_routes = Blueprint('delivery_staff_routes', __name__)
reservation_routes = Blueprint('reservation_routes', __name__)
feedback_routes = Blueprint('feedback_routes', __name__)
membership_routes = Blueprint('membership_routes', __name__)
asset_routes = Blueprint('asset_routes', __name__)
customer_data_record_routes = Blueprint('customer_data_record_routes', __name__)
customer_routes = Blueprint('customer_routes', __name__)
in_store_customer_routes = Blueprint('in_store_customer_routes', __name__)
online_customer_routes = Blueprint('online_customer_routes', __name__)
order_routes = Blueprint('order_routes', __name__)
menu_item_routes = Blueprint('menu_item_routes', __name__)
bill_routes = Blueprint('bill_routes', __name__)
payment_method_routes = Blueprint('payment_method_routes', __name__)

# Import routes after db initialization
from . import employee_routes
from . import manager_routes
from . import waitstaff_routes
from . import kitchen_staff_routes
from . import delivery_staff_routes
from . import reservation_routes
from . import feedback_routes
from . import membership_routes
from . import asset_routes
from . import customer_data_record_routes
from . import customer_routes
from . import in_store_customer_routes
from . import online_customer_routes
from . import order_routes
from . import menu_item_routes
from . import bill_routes
from . import payment_method_routes

# List of all blueprints
blueprints = [
    employee_routes,
    manager_routes,
    waitstaff_routes,
    kitchen_staff_routes,
    delivery_staff_routes,
    reservation_routes,
    feedback_routes,
    membership_routes,
    asset_routes,
    customer_data_record_routes,
    customer_routes,
    in_store_customer_routes,
    online_customer_routes,
    order_routes,
    menu_item_routes,
    bill_routes,
    payment_method_routes
]

def register_routes(app):
    from models.db import db

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
