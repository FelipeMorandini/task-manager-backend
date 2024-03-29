import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_URL = os.getenv('DB_URL')
    JWT_SECRET = os.getenv('JWT_SECRET')