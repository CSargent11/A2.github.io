from flask import Flask, jsonify, request, redirect, session, url_for
from flask_restful import Api, Resource, reqparse
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key. This would be an environment variable in production.

login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
def home():
    return "Home"

@app.route("/create-user", methods=["POST","GET"])
def create_user():
    user_data = {
        "name": "Claire",
        "email": "claire.s@example.com"
    }
    return jsonify(user_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    user_id = session.get('user_id')
    username = session.get('username')
    # ...

@app.route("/products/<int:product_id>")
def view_product(product_id):
    product_name = products.get(product_id).name
    product_price = products.get(product_id).price
    product_quant = products.get(product_id).quantity
    product_str = f"{{product_name : {product_name},product_price : {product_price},product_quantity : {product_quant}}}"
    return product_str

class Product:
    def __init__(self,id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

products = {
    1 : Product(1, "T-shirt", 10, 5),
    2 : Product(2, "Jeans", 50, 4),
    3 : Product(3, "Shoes", 30, 6)
}

# Define a dictionary to store the cart data
cart = {}

@app.route("/add-to-cart/<int:product_id>", methods=["POST", "GET"])
def add_to_cart(product_id):
    quantity = request.args.get("quantity", type=int)
    if quantity is None:
        return jsonify({"error": "Invalid quantity"}), 400

 # Add the product and quantity to the cart dictionary
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    return jsonify({"message": "Product added to cart successfully"}), 200

@app.route("/delete-from-cart/<int:product_id>", methods=["POST", "GET"])
def delete_from_cart(product_id):
    if product_id not in cart:
        return jsonify({"error": "Product not found in cart"}), 404

    # Remove the product from the cart dictionary
    del cart[product_id]

    return jsonify({"message": "Product removed from cart successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
