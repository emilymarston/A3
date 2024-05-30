from flask import Blueprint, request, jsonify, abort
from . import db
from models import MenuItem

menu_item_routes = Blueprint('menu_item_routes', __name__)

@menu_item_routes.route('/menu_items', methods=['GET'])
def get_menu_items():
    menu_items = MenuItem.query.all()
    return jsonify([item.to_dict() for item in menu_items])

@menu_item_routes.route('/menu_items/<int:menu_item_id>', methods=['GET'])
def get_menu_item(menu_item_id):
    menu_item = MenuItem.query.get_or_404(menu_item_id)
    return jsonify(menu_item.to_dict())

@menu_item_routes.route('/menu_items', methods=['POST'])
def create_menu_item():
    data = request.json
    try:
        menu_item = MenuItem(
            menu_description=data['menu_description'],
            price=data['price']
        )
        db.session.add(menu_item)
        db.session.commit()
        return jsonify(menu_item.to_dict()), 201
    except Exception as e:
        abort(400, description=str(e))

@menu_item_routes.route('/menu_items/<int:menu_item_id>', methods=['PUT'])
def update_menu_item(menu_item_id):
    menu_item = MenuItem.query.get_or_404(menu_item_id)
    data = request.json
    try:
        menu_item.menu_description = data.get('menu_description', menu_item.menu_description)
        menu_item.price = data.get('price', menu_item.price)
        db.session.commit()
        return jsonify(menu_item.to_dict())
    except Exception as e:
        abort(400, description=str(e))

@menu_item_routes.route('/menu_items/<int:menu_item_id>', methods=['DELETE'])
def delete_menu_item(menu_item_id):
    menu_item = MenuItem.query.get_or_404(menu_item_id)
    db.session.delete(menu_item)
    db.session.commit()
    return '', 204
