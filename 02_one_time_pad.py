# Experiment 2: One-Time Pad Cipher
import random

def generate_key(length, seed=2024):
    # A fixed seed is used ONLY so that the lab output is repeatable.
    # In real use the key must come from a true random source (e.g. secrets module).
    rng = random.Random(seed)
    return "".join(chr(rng.randrange(26) + 65) for _ in range(length))

def otp(text, key, decrypt=False):
    out = ""
    for t, k in zip(text, key):
        shift = ord(k) - 65
        if decrypt:
            shift = -shift
        out += chr((ord(t) - 65 + shift) % 26 + 65)
    return out

plaintext = "NETWORKSECURITYLAB"
key = generate_key(len(plaintext))          # key length == message length
cipher = otp(plaintext, key)
print("Plaintext  :", plaintext)
print("Key (pad)  :", key)
print("Ciphertext :", cipher)
print("Decrypted  :", otp(cipher, key, decrypt=True))

# Same plaintext letters map to different ciphertext letters
print("\nLetter-by-letter mapping:")
for p, k, c in zip(plaintext, key, cipher):
    print(f"  {p} + {k} -> {c}")
