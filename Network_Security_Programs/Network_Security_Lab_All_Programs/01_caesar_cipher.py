def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch
    return result

def decrypt(text, key):
    return encrypt(text, -key)

plaintext = "Network Security Lab at Central University of Kashmir"
key = 5
cipher = encrypt(plaintext, key)

print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", decrypt(cipher, key))

print("\nBrute-force attack on ciphertext:")
for k in range(1, 26):
    print("Key %2d -> %s" % (k, decrypt(cipher, k)))
