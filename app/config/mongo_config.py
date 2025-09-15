# app/config/mongo_config.py
from pymongo import MongoClient
from application_config import app_config

def get_mongo_clients():
    src_client = MongoClient(app_config.DEV_URI)
    dst_client = MongoClient(app_config.LOCAL_URI)
    return src_client, dst_client

def get_db(uri=None):
    """Return MongoDB client for local DB by default"""
    client = MongoClient(uri or app_config.LOCAL_URI)
    return client[app_config.DB_NAME]
