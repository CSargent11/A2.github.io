from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

salt = b'\xeb\xd6Uf\xf7\x120\x1dM\xcd,j\x03_\x8e\xcb\xf8\xc8\x86\xac-\x16;\xee\xc97[Dx\xa6\x99\xa0'
password = 'mypassword'

key = PBKDF2(password, salt, dkLen=32)

message = b'Hello Secret World!'

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as file:
    file.write(cipher.iv)
    file.write(ciphered_data)

with open('encrypted.bin', 'rb') as file:
    iv = file.read(16)
    decrypt_data = file.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original_message = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print(original_message)