from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b"mysecretkey12345"
iv = b"initialvector123"
plaintext = b"Network Security Lab - AES Demo"

cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(plaintext, 16))

print("Plaintext      :", plaintext.decode())
print("Key (hex)      :", key.hex())
print("IV  (hex)      :", iv.hex())
print("Ciphertext(hex):", encrypted.hex())

decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(encrypted), 16)
print("Decrypted      :", decrypted.decode())
