# Experiment 7: DES (Data Encryption Standard) in CBC mode
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b"8bytekey"                      # 64-bit key (56 effective bits)
iv  = bytes.fromhex("0001020304050607")
plaintext = b"Network Security Lab - DES Demo"

enc = DES.new(key, DES.MODE_CBC, iv)
ct = enc.encrypt(pad(plaintext, DES.block_size))

print("Plaintext      :", plaintext.decode())
print("Key (hex)      :", key.hex(), "(64 bits incl. parity)")
print("IV  (hex)      :", iv.hex())
print("Block size     :", DES.block_size * 8, "bits")
print("Ciphertext(hex):", ct.hex())

dec = unpad(DES.new(key, DES.MODE_CBC, iv).decrypt(ct), DES.block_size)
print("Decrypted      :", dec.decode())

# Effect of ECB mode: identical blocks give identical ciphertext
blk = b"ABCDEFGH"
ecb = DES.new(key, DES.MODE_ECB).encrypt(blk * 2)
print("\nECB mode, two identical blocks:")
print("Block 1:", ecb[:8].hex())
print("Block 2:", ecb[8:].hex(), "(same -> pattern leaks)")
cbc = DES.new(key, DES.MODE_CBC, iv).encrypt(blk * 2)
print("CBC mode, same two blocks:")
print("Block 1:", cbc[:8].hex())
print("Block 2:", cbc[8:].hex(), "(different -> pattern hidden)")
