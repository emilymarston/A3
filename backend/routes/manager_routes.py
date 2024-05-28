from flask import Blueprint, jsonify, abort
from . import db
from models import Manager

manager_routes = Blueprint('manager_routes', __name__)

@manager_routes.route('/manager/meetings', methods=['POST'])
def conduct_meeting():
    manager = Manager.query.first()
    if not manager:
        abort(404, description="Manager not found")

    # Perform actions to conduct a meeting
    manager.conduct_meeting()
    
    return jsonify({'message': "Meeting conducted successfully"})

@manager_routes.route('/manager/feedback', methods=['GET'])
def review_customer_feedback():
    manager = Manager.query.first()
    if not manager:
        abort(404, description="Manager not found")

    # Perform actions to review customer feedback
    manager.review_customer_feedback()
    
    return jsonify({'message': "Customer feedback reviewed"})

@manager_routes.route('/manager/reports/<report_type>', methods=['GET'])
def review_report(report_type):
    manager = Manager.query.first()
    if not manager:
        abort(404, description="Manager not found")

    # Perform actions to review a report
    manager.review_report(report_type)
    
    return jsonify({'message': f"{report_type} report reviewed"})
