# app.py
from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
from flask_sslify import SSLify
from config import Config
from models import User, Product
from users import login_user_custom
from products import products, cart

app = Flask(__name__)
app.config.from_object(Config)
sslify = SSLify(app)

# ... (The rest of your app code remains mostly unchanged)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
