from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/products/<int:product_id>')
def view_product(product_id):
    product_name = products.get(product_id).name
    product_price = products.get(product_id).price
    product_quant = products.get(product_id).quantity
    product_str = f"{{product_name : {product_name},product_price : {product_price},product_quantity : {product_quant}}}"
    return product_str

if __name__ == "__main__":
    app.run()
