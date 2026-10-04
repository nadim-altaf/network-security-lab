# Experiment 11: RSA Encryption, Decryption and Signature
from math import gcd

def modinv(e, phi):
    return pow(e, -1, phi)

p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17
assert gcd(e, phi) == 1
d = modinv(e, phi)
print(f"p = {p}, q = {q}")
print(f"n = p*q = {n}")
print(f"phi(n) = {phi}")
print(f"Public key  (e, n) = ({e}, {n})")
print(f"Private key (d, n) = ({d}, {n})")

msg = "HELLO"
nums = [ord(c) for c in msg]
cipher = [pow(m, e, n) for m in nums]
plain = [pow(c, d, n) for c in cipher]
print("\nMessage          :", msg, nums)
print("Encrypted        :", cipher)
print("Decrypted        :", plain, "->", "".join(chr(x) for x in plain))

# Digital signature on a small message value
m = 65
sig = pow(m, d, n)
print("\nDigital signature:")
print("Message value m =", m)
print("Signature s = m^d mod n =", sig)
print("Verification s^e mod n =", pow(sig, e, n), "->",
      "VALID" if pow(sig, e, n) == m else "INVALID")
