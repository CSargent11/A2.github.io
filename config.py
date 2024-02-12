# config.py
import os

class Config:
    # Load secret key from environment variable
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
