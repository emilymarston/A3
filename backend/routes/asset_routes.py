from flask import Blueprint, jsonify
from . import db
from models import Asset

assets_routes = Blueprint('assets_routes', __name__)

@assets_routes.route('/assets', methods=['GET'])
def get_assets():
    assets = Asset.query.all()
    return jsonify([asset.to_dict() for asset in assets])