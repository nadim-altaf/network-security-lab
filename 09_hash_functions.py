# Experiment 9: Message Digest / Hash Functions and Integrity Check
import hashlib

def digest(msg, algo):
    return hashlib.new(algo, msg.encode()).hexdigest()

m1 = "Network Security Lab"
m2 = "Network Security Lab."   # one character added
for algo in ("md5", "sha1", "sha256", "sha512"):
    print(f"{algo.upper():7s}: {digest(m1, algo)}")

print("\nAvalanche effect (SHA-256):")
print("Message 1:", m1, "->", digest(m1, "sha256"))
print("Message 2:", m2, "->", digest(m2, "sha256"))

h1, h2 = digest(m1, "sha256"), digest(m2, "sha256")
diff = bin(int(h1, 16) ^ int(h2, 16)).count("1")
print(f"Bits differing: {diff} out of 256 ({diff/256*100:.1f}%)")
print("Integrity check:", "PASSED" if h1 == h2 else "FAILED - message was modified")
