from flask import Flask, jsonify, request, redirect, make_response, session, url_for
from flask_restful import Api, Resource, reqparse
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

# Secret key. This would be an environment variable in production.
app.secret_key = 'your_secret_key'  

login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/login", methods=["POST", "GET"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == 'testuser' and password == 'testpass':
        res = make_response(jsonify(success=True))
        res.set_cookie(key='session', value='logged_in')  # Fixed syntax error and defined the variable 'key'
        return res
    else:
        return jsonify(success=False), 401
      
@app.route("/protected")
def protected():
    session_cookie = request.cookies.get('session')
    if session_cookie == 'logged_in':
        return jsonify(access=True)
    else:
        return jsonify(access=False), 403
    
s = request.session()

login_url = "http://localhost:5000/login"
login_data = {'username': 'testuser', 'password': 'testpass'}

res = s.post(login_url, json=login_data)

saved_cookie = res.cookies
print(saved_cookie)

if res.json().get('success'):
    print("Login successful!")

else:
    print("Login failed!")

protected_url = "http://localhost:5000/protected"

res = s.get(protected_url)

if res.json().get('access'):
    print("Access granted!")
else:
    print("Access denied!")

@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))