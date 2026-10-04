# Experiment 10: Diffie-Hellman Key Exchange
p = 23          # public prime
g = 5           # public generator
a = 6           # Alice's private key
b = 15          # Bob's private key

A = pow(g, a, p)   # Alice public value
B = pow(g, b, p)   # Bob public value
print("Public prime p =", p, ", generator g =", g)
print("Alice private a =", a, "-> public A = g^a mod p =", A)
print("Bob   private b =", b, "-> public B = g^b mod p =", B)

s_alice = pow(B, a, p)
s_bob = pow(A, b, p)
print("Shared secret computed by Alice:", s_alice)
print("Shared secret computed by Bob  :", s_bob)
print("Keys match:", s_alice == s_bob)

# Larger example (1536-bit-style numbers are used in practice; here a 61-bit prime)
p = 2305843009213693951
g = 3
a, b = 123456789123, 987654321987
A, B = pow(g, a, p), pow(g, b, p)
print("\nLarger prime example (p = 2^61 - 1):")
print("A =", A)
print("B =", B)
print("Shared secret (Alice):", pow(B, a, p))
print("Shared secret (Bob)  :", pow(A, b, p))
