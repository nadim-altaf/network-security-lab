# Experiment 1: Caesar Cipher
def caesar(text, key, decrypt=False):
    if decrypt:
        key = -key
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch
    return result

plaintext = "Network Security Lab at Central University of Kashmir"
key = 5
cipher = caesar(plaintext, key)
print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", caesar(cipher, key, decrypt=True))

print("\nBrute-force attack on ciphertext:")
for k in range(1, 26):
    print(f"Key {k:2d} -> {caesar(cipher, k, decrypt=True)}")
