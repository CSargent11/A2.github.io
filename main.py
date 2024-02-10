from flask import Flask, jsonify, request, redirect, make_response, session, url_for
from flask_restful import Api, Resource, reqparse
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_sslify import SSLify
from werkzeug.datastructures import ImmutableDict

app = Flask(__name__)
sslify = SSLify(app)

# Secret key. This would be an environment variable in production.
app.secret_key = 'your_secret_key'  


@app.route("/")
def home():
    return "Home"

@app.route("/profile")
def profile():
    user_id = session.get('user_id')
    username = session.get('username')
    return "User ID: {user_id}, Username: {username}"

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    username = request.form.get("username")
    user_email = request.args.get("user_email")

    user_data = ImmutableDict({
        "name": username,
        "email": user_email
    })
    return jsonify(user_data)


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

#product dictionary
products = {
    1 : Product(1, "T-shirt", 10, 5),
    2 : Product(2, "Jeans", 50, 4),
    3 : Product(3, "Shoes", 30, 6)
}

# Cart dictionary to store cart data
cart = {}

@app.route("/add-to-cart/<int:product_id>", methods=["POST", "GET"])
def add_to_cart(product_id):
    # get the desired quantity from user post request
    quantity = request.args.get("quantity", type=int)
    
    # Add the product and quantity to the cart dictionary
    if product_id not in cart:
        try:
            cart[product_id] = Product(product_id, 
                                       products[product_id].name, 
                                       products[product_id].price, 
                                       quantity)
            return jsonify({"message": "Product added to cart successfully",
                            "product_id" : product_id,
                            "quantity" : quantity}), 200
        except:
            return jsonify({"message" : "Product not found"})
    else:
        cart[product_id].quantity += quantity
        return jsonify({"message": "Product added to cart successfully",
                            "product_id" : product_id,
                            "quantity" : quantity}), 200

@app.route("/delete-from-cart/<int:product_id>", methods=["POST", "GET"])
def delete_from_cart(product_id):
    if product_id not in cart:
        return jsonify({"error": "Product not found in cart"}), 404

    # Remove the product from the cart dictionary
    del cart[product_id]

    return jsonify({"message": "Product removed from cart successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)