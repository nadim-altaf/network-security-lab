from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b"8bytekey"
iv = b"01234567"
plaintext = b"Network Security Lab - DES Demo"

cipher = DES.new(key, DES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(plaintext, 8))

print("Plaintext      :", plaintext.decode())
print("Key (hex)      :", key.hex())
print("IV  (hex)      :", iv.hex())
print("Ciphertext(hex):", encrypted.hex())

decipher = DES.new(key, DES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(encrypted), 8)
print("Decrypted      :", decrypted.decode())

block = b"ABCDEFGH"
ecb = DES.new(key, DES.MODE_ECB).encrypt(block * 2)
print("\nECB mode, two identical blocks:")
print("Block 1:", ecb[:8].hex())
print("Block 2:", ecb[8:].hex())

cbc = DES.new(key, DES.MODE_CBC, iv).encrypt(block * 2)
print("CBC mode, same two blocks:")
print("Block 1:", cbc[:8].hex())
print("Block 2:", cbc[8:].hex())
