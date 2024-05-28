from flask import Blueprint

# Import individual route files
from .employee_routes import employee_routes
from .manager_routes import manager_routes
from .waitstaff_routes import waitstaff_routes
from .kitchen_staff_routes import kitchen_staff_routes
from .delivery_staff_routes import delivery_staff_routes

# Create blueprints for each set of routes
blueprints = [
    employee_routes,
    manager_routes,
    waitstaff_routes,
    kitchen_staff_routes,
    delivery_staff_routes
]

# Register all blueprints
def register_routes(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

# You might also add a convenience function to register routes in your app
def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app
