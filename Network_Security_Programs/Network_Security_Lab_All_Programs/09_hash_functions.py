import hashlib

msg1 = "Network Security Lab"
msg2 = "Network Security Lab."

print("MD5     :", hashlib.md5(msg1.encode()).hexdigest())
print("SHA1    :", hashlib.sha1(msg1.encode()).hexdigest())
print("SHA256  :", hashlib.sha256(msg1.encode()).hexdigest())
print("SHA512  :", hashlib.sha512(msg1.encode()).hexdigest())

h1 = hashlib.sha256(msg1.encode()).hexdigest()
h2 = hashlib.sha256(msg2.encode()).hexdigest()

print("\nAvalanche effect (SHA-256):")
print("Message 1:", msg1, "->", h1)
print("Message 2:", msg2, "->", h2)

diff = bin(int(h1, 16) ^ int(h2, 16)).count("1")
print("Bits differing: %d out of 256 (%.1f%%)" % (diff, diff / 256 * 100))

if h1 == h2:
    print("Integrity check: PASSED")
else:
    print("Integrity check: FAILED - message was modified")
