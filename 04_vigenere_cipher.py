# Experiment 4: Vigenere Cipher (polyalphabetic substitution)
def vigenere(text, key, decrypt=False):
    key = key.upper()
    out, j = "", 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            if decrypt:
                shift = -shift
            base = 65 if ch.isupper() else 97
            out += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            out += ch
    return out

plaintext = "Attack the server at dawn"
key = "KASHMIR"
cipher = vigenere(plaintext, key)
print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", vigenere(cipher, key, decrypt=True))
