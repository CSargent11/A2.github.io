from flask import Flask, jsonify, request

app = Flask(__name__)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []

    def add_to_cart(self, product):
        self.shopping_cart.append(product)

    def remove_from_cart(self, product):
        if product in self.shopping_cart:
            self.shopping_cart.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.shopping_cart:
            total += product.price * product.quantity
        return total

    def checkout(self):
        # Perform checkout logic here
        pass

# Create sample products
products = {
    "T-shirt": Product("T-shirt", 10, 5),
    "Jeans": Product("Jeans", 50, 3),
    "Shoes": Product("Shoes", 30, 2)
}

# Create a customer
customer = Customer("Paul", "Paul@example.com")

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_name = request.json.get("product_name")

    product = products.get(product_name)
    if product:
        customer.add_to_cart(product)
        return jsonify({"message": "Product added to cart"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_name = request.json.get("product_name")

    product = products.get(product_name)
    if product:
        customer.remove_from_cart(product)
        return jsonify({"message": "Product removed from cart"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route("/calculate_total", methods=["GET"])
def calculate_total():
    total = customer.calculate_total()
    return jsonify({"total": total})

@app.route("/checkout", methods=["POST"])
def checkout():
    customer.checkout()
    return jsonify({"message": "Checkout completed"}), 200

if __name__ == "__main__":
    app.run()