#main.py
from flask import Flask, jsonify, request, redirect, make_response, session, url_for
from flask_restful import Api, Resource, reqparse
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_sslify import SSLify
from werkzeug.datastructures import ImmutableDict
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)
sslify = SSLify(app)

# Secret key. This should be an environment variable in production.
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)

# User class for login
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# User database
users = {
    'testuser': User('testuser', 'testpass')
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Home page
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the home page!"

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = users.get(username)

        if user and user.password == password:
            login_user(user)
            return redirect(url_for("protected"))
        else:
            return jsonify(success=False)

    return '''
        <form action="" method="post">
            <p><input type="text" name="username" placeholder="Username"></p>
            <p><input type="password" name="password" placeholder="Password"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''

# Protected page accessible only to authenticated users
@app.route("/protected")
@login_required
def protected():
    # Salt used for password-based key derivation
    salt = b'\xeb\xd6Uf\xf7\x120\x1dM\xcd,j\x03_\x8e\xcb\xf8\xc8\x86\xac-\x16;\xee\xc97[Dx\xa6\x99\xa0'
    password = 'mypassword'
    key = PBKDF2(password, salt, dkLen=32)

    message = b'Hello Secret World!'

    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(message, AES.block_size))

    with open('encrypted.bin', 'wb') as file:
        file.write(cipher.iv)
        file.write(ciphered_data)

    # Decryption
    with open('encrypted.bin', 'rb') as file:
        iv = file.read(16)
        decrypt_data = file.read()

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original_message = unpad(cipher.decrypt(decrypt_data), AES.block_size)

    return jsonify(access=True, original_message=original_message.decode())

# Logout user
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# User profile page
@app.route("/profile")
@login_required
def profile():
    user_id = current_user.get_id()
    username = current_user.username
    return f"User ID: {user_id}, Username: {username}"

# Create a new user
@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        username = request.form.get("username")
        user_email = request.form.get("user_email")

        user_data = ImmutableDict({
            "name": username,
            "email": user_email
        })
        return jsonify(user_data)

    return '''
        <form action="" method="post">
            <p><input type="text" name="username" placeholder="Username"></p>
            <p><input type="email" name="user_email" placeholder="Email"></p>
            <p><input type="submit" value="Create User"></p>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, port=5000)
