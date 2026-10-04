plaintext = "NETWORKSECURITYLAB"
key = "PFXSJGXNYWYIRHUXPL"

cipher = ""
for i in range(len(plaintext)):
    c = (ord(plaintext[i]) - 65 + ord(key[i]) - 65) % 26
    cipher += chr(c + 65)

decrypted = ""
for i in range(len(cipher)):
    p = (ord(cipher[i]) - ord(key[i])) % 26
    decrypted += chr(p + 65)

print("Plaintext  :", plaintext)
print("Key (pad)  :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", decrypted)

print("\nLetter-by-letter mapping:")
for i in range(len(plaintext)):
    print(" ", plaintext[i], "+", key[i], "->", cipher[i])
