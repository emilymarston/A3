from flask import Blueprint, jsonify, request
from . import db
from models import Employee

employee_routes = Blueprint('employee_routes', __name__)

@employee_routes.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@employee_routes.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.to_dict())

@employee_routes.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee = Employee(**data)
    db.session.add(employee)
    db.session.commit()
    return jsonify(employee.to_dict()), 201

@employee_routes.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify(employee.to_dict())

@employee_routes.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return '', 204
