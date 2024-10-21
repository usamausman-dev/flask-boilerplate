# routes/example_routes.py
from flask import Blueprint, jsonify, request
from controllers.example_controller import get_items, add_item

example_bp = Blueprint('example_bp', __name__)

@example_bp.route('/items', methods=['GET'])
def fetch_items():
    items = get_items()
    return jsonify(items), 200

@example_bp.route('/items', methods=['POST'])
def create_item():
    data = request.json
    item_id = add_item(data)
    return jsonify({"id": item_id}), 201
