# config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI')  # Fetches the MongoDB URI from the .env file
