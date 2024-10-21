# controllers/example_controller.py

from libs.db import db


def get_items():
    collection = db['items']
    items = collection.find()
    return [item for item in items]

def add_item(data):
    collection = db['items']
    item_id = collection.insert_one(data).inserted_id
    return str(item_id)
