p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17

d = 1
while (d * e) % phi != 1:
    d += 1

print("p =", p, ", q =", q)
print("n = p*q =", n)
print("phi(n) =", phi)
print("Public key  (e, n) =", (e, n))
print("Private key (d, n) =", (d, n))

message = "HELLO"
numbers = []
for ch in message:
    numbers.append(ord(ch))

encrypted = []
for m in numbers:
    encrypted.append(pow(m, e, n))

decrypted = []
for c in encrypted:
    decrypted.append(pow(c, d, n))

text = ""
for x in decrypted:
    text += chr(x)

print("\nMessage    :", message, numbers)
print("Encrypted  :", encrypted)
print("Decrypted  :", decrypted, "->", text)

m = 65
s = pow(m, d, n)
print("\nDigital signature:")
print("Message value m =", m)
print("Signature s = m^d mod n =", s)
print("Verification s^e mod n =", pow(s, e, n))
if pow(s, e, n) == m:
    print("Signature is VALID")
else:
    print("Signature is INVALID")
