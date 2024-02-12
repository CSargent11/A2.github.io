A2 Readme file:

Flask Authentication and Encryption Example

This is a Flask application that demonstrates user authentication and encryption using the Flask framework.

Features:

•	User login and session management with Flask-Login
•	Password-based key derivation with PBKDF2
•	Data encryption and decryption with AES
•	Protected routes accessible only to authenticated users
•	User profile creation

Prerequisites:

•	Python 3.x
•	Flask
•	Flask-RESTful
•	Flask-Login
•	Flask-SSLify
•	Crypto (pycryptodome)	

Usage:

Open your web browser and navigate to http://localhost:5000. You will see the home page.
Use the web browser to navigate to the desired locations, eg; http://localhost:5000/login, then click on the “Login” link to access the login page. Enter the username and password provided in the users dictionary in app.py and click “Login”.
After successful login, you will be redirected to the protected page, where you can see an example of data encryption and decryption using AES.
You can also access the user profile page by using the web browser again and typing http://localhost:5000/proflie. Finally type  http://localhost:5000/create-user and click on the “Create User” link and fill in the required information.

Configuration:
The following configuration options are available in app.py:
app.secret_key: Secret key for session management. This should be an environment variable in production.


Flask Product/Cart API

This is a Flask API that allows users to view products, add products to a cart, and remove products from the cart.

Usage:
Open your web browser and navigate to http://localhost:5000/products/<product_id> to view the details of a product. Replace <product_id> with the desired product ID number (1,2,3 or 4).
To add a product to the cart, make a POST or GET request to http://localhost:5000/add-to-cart/<product_id> with the desired product ID and quantity as parameters.
To remove a product from the cart, make a POST or GET request to http://localhost:5000/delete-from-cart/<product_id> with the product ID as a parameter.
API Endpoints
GET /products/<product_id>: Retrieves the details of a product.
POST /add-to-cart/<product_id>: Adds a product to the cart.
POST /delete-from-cart/<product_id>: Removes a product from the cart.
![image](https://github.com/CSargent11/A2.github.io/assets/132493037/684462f1-c5b0-4078-ac3f-d9d011ac0d2a)
