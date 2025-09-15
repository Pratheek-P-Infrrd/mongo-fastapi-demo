from pymongo import MongoClient
from application_config import app_config

def get_mongo_clients():
    return MongoClient(app_config.MONGO_URI)

def get_db():
    return MongoClient(app_config.DB_NAME)