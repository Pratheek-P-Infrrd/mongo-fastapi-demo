import os
from dotenv import load_dotenv

load_dotenv()

class ApplicationConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.DB_NAME = os.getenv("DB_NAME")
        self.BATCH_SIZE = os.getenv("BATCH_SIZE")

        # Basic validation
        if not self.MONGO_URI:
            raise ValueError("❌ Missing MONGO_URI in .env")
        if not self.DB_NAME:
            raise ValueError("❌ Missing DB_NAME in .env")

app_config = ApplicationConfig()