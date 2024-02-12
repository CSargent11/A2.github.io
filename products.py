# products.py
from flask import app, jsonify, request
from models import Product

# Display product information
@app.route("/products/<int:product_id>", methods=['GET'])
def get_product(product_id):
    product_name = products.get(product_id).name
    product_price = products.get(product_id).price
    product_quant = products.get(product_id).quantity
    product_str = f"{{product_name : {product_name}, : {product_price},product_quantity : {product_quant}}}"
    return product_str

class Product:
    def __init__(self,id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

# Product dictionary containing product information
products = {
    1 : Product(1, "T-shirt", 10, 25),
    2 : Product(2, "Jeans", 50, 20),
    3 : Product(3, "Shoes", 30, 30)
}

# Add a new product
new_product = Product(4, "Hat", 15, 10)
products[new_product.id] = new_product

# Delete a product
del products[3]

# Cart dictionary to store cart data
cart = {}

# Add a product to the cart
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

# Remove a product from the cart
@app.route("/delete-from-cart/<int:product_id>", methods=["POST", "GET"])
def delete_from_cart(product_id):
    if product_id not in cart:
        return jsonify({"error": "Product not found in cart"}), 404

    # Remove the product from the cart dictionary
    del cart[product_id]

    return jsonify({"message": "Product removed from cart successfully"}), 200