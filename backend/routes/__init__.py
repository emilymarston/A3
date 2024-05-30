from flask import Blueprint

# Import individual route files
from .employee_routes import employee_routes
from .manager_routes import manager_routes
from .waitstaff_routes import waitstaff_routes
from .kitchen_staff_routes import kitchen_staff_routes
from .delivery_staff_routes import delivery_staff_routes
from .reservation_routes import reservation_routes
from .feedback_routes import feedback_routes
from .membership_routes import membership_routes
from .asset_routes import asset_routes
from .customer_data_record_routes import customer_data_record_routes
from .customer_routes import customer_routes
from .in_store_customer_routes import in_store_customer_routes
from .online_customer_routes import online_customer_routes
from .order_routes import order_routes
from .menu_item_routes import menu_item_routes
from .bill_routes import bill_routes
from .payment_method_routes import payment_method_routes

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
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
