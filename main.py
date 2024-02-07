from flask import Flask, jsonify, request, url_for
from flask_restful import Api, Resource, reqparse
from flask_login import LoginManager
login_manager = LoginManager()

app = Flask(__name__)
login_manager.init_app(app)

@app.route("/")
def home():
    return "Home"

@app.route("/create-user", methods=["POST","GET"])
def create_user():
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
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

products = {
    1 : Product(1, "T-shirt", 10, 5),
    2 : Product(2, "Jeans", 50, 3),
    3 : Product(3, "Shoes", 30, 2)
}

@app.route("/add-to-cart", methods=["POST", "GET"])
def add_to_cart():
    product_id = request.json["product_id"]
    quantity = request.json["quantity"]
    if product_id in products:
        product = products[product_id]
        if product.quantity >= quantity:
            product.quantity -= quantity
            return jsonify({"message": "Product added to cart"}), 200
        else:
            return jsonify({"message": "Not enough quantity"}), 400
    else:
        return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
