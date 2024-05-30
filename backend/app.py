from flask import Flask
from models.db import db
from routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Import models to register them with SQLAlchemy
        import models
        
        # Optionally, create the database tables if they do not exist
        db.create_all()

    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
