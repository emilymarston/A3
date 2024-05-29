from flask import Flask
from models import db
from routes import *

def create_app():
    # Create Flask application instance
    app = Flask(__name__)

    # Configure database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints
    register_routes(app)

    return app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)