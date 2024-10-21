# libs/db.py
from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()  # This gets the MongoDB database
