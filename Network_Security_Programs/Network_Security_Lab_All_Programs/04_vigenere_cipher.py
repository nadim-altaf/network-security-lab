def vigenere(text, key, mode):
    key = key.upper()
    result = ""
    j = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            if mode == "decrypt":
                shift = -shift
            if ch.isupper():
                base = 65
            else:
                base = 97
            result += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

plaintext = "Attack the server at dawn"
key = "KASHMIR"
cipher = vigenere(plaintext, key, "encrypt")

print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", vigenere(cipher, key, "decrypt"))
