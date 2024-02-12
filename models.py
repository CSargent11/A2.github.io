# models.py
from werkzeug.security import generate_password_hash, check_password_hash
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class User:
    def __init__(self, username, password):
        self.username = username
        self.salt = get_random_bytes(16)
        self.set_password(password)

    def set_password(self, password):
        key = PBKDF2(password, self.salt, dkLen=32)
        self.password_hash = key

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
