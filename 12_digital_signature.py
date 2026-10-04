# Experiment 12: Digital Signature using RSA with SHA-256 (PKCS#1 v1.5)
import random, textwrap
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Fixed seed only to make the lab output repeatable
rng = random.Random(7)
key = RSA.generate(1024, randfunc=rng.randbytes)
public_key = key.publickey()
print("RSA key size :", key.size_in_bits(), "bits")
print("Public exp e :", key.e)
print("Modulus n    :", hex(key.n)[:34] + "...")

message = b"Transfer Rs. 5000 to account 123456"
h = SHA256.new(message)
print("\nMessage      :", message.decode())
print("SHA-256 hash :", h.hexdigest())

signature = pkcs1_15.new(key).sign(h)            # sign with PRIVATE key
print("Signature    :")
print(textwrap.indent("\n".join(textwrap.wrap(signature.hex(), 64)), "  "))

def verify(msg, sig):
    try:
        pkcs1_15.new(public_key).verify(SHA256.new(msg), sig)   # PUBLIC key
        return "VALID - authentic and unmodified"
    except (ValueError, TypeError):
        return "INVALID - message or signature was altered"

print("\nVerification of original message :", verify(message, signature))
tampered = b"Transfer Rs. 50000 to account 123456"
print("Tampered message                 :", tampered.decode())
print("Verification of tampered message :", verify(tampered, signature))
