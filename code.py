from flask import Flask, jsonify, request

app = Flask(__name__)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        if product.quantity > 0:
            self.items.append(product)
            product.quantity -= 1
        else:
            raise ValueError("Product is out of stock.")

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
            product.quantity += 1
        else:
            raise ValueError("Product is not in the cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_item(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_item(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        self.send_email(total)
        return total

    def send_email(self, total):
        # Code for sending email

    # Create sample products
        products = {
            "T-shirt": Product("T-shirt", 10, 5),
            "Jeans": Product("Jeans", 50, 3),
            "Shoes": Product("Shoes", 30, 2)
        }

# Create a customer
customer = Customer("John", "john@example.com")

products = {
    "T-shirt": Product("T-shirt", 10, 5),
    "Jeans": Product("Jeans", 50, 3),
    "Shoes": Product("Shoes", 30, 2)
}

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_name = request.json.get("product_name")

    product = products.get(product_name)
    if product:
        try:
            customer.add_to_cart(product)
        except ValueError as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Product added to cart"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_name = request.json.get("product_name")

    product = products.get(product_name)
    if product:
        try:
            customer.remove_from_cart(product)
        except ValueError as e:
            return jsonify({"message": str(e)}), 400
        return jsonify({"message": "Product removed from cart"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route("/calculate_total", methods=["GET"])
def calculate_total():
    total = customer.shopping_cart.calculate_total()
    return jsonify({"total": total})

@app.route("/checkout", methods=["POST"])
def checkout():
    total = customer.checkout()
    return jsonify({"total": total, "message": "Checkout completed"}), 200

if __name__ == "__main__":
    app.run()
