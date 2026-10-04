import hashlib

p = 1000000007
q = 998244353
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi)

def get_hash(message):
    h = hashlib.sha256(message.encode()).hexdigest()
    return int(h, 16) % n

def sign(message):
    return pow(get_hash(message), d, n)

def verify(message, signature):
    return pow(signature, e, n) == get_hash(message)

print("Public key  (e, n) =", (e, n))
print("Private key (d, n) =", (d, n))

message = "Transfer Rs. 5000 to account 123456"
print("\nMessage      :", message)
print("SHA-256 hash :", hashlib.sha256(message.encode()).hexdigest())

signature = sign(message)
print("Signature    :", signature)

if verify(message, signature):
    print("\nOriginal message  : signature is VALID")
else:
    print("\nOriginal message  : signature is INVALID")

tampered = "Transfer Rs. 50000 to account 123456"
print("Tampered message  :", tampered)
if verify(tampered, signature):
    print("Tampered message  : signature is VALID")
else:
    print("Tampered message  : signature is INVALID - message was changed")
