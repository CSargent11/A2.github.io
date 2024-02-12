# users.py
from flask_login import login_user
from psutil import users
from models import User

def login_user_custom(username, password):
    user = users.get(username)

    if user and user.check_password(password):
        login_user(user)
        return True
    else:
        return False
