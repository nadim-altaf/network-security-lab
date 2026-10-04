# Experiment 8: Symmetric Encryption using AES (CBC mode)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = bytes.fromhex("00112233445566778899aabbccddeeff")   # 128-bit key
iv  = bytes.fromhex("0f0e0d0c0b0a09080706050403020100")   # 128-bit IV
plaintext = b"Network Security Lab - AES Demo"

cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(plaintext, AES.block_size))
print("Plaintext      :", plaintext.decode())
print("Key (hex)      :", key.hex())
print("IV  (hex)      :", iv.hex())
print("Ciphertext(hex):", ct.hex())

dec = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), AES.block_size)
print("Decrypted      :", dec.decode())
