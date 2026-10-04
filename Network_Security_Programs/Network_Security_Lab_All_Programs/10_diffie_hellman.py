p = 23
g = 5
a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)
print("Public prime p =", p, ", generator g =", g)
print("Alice private a =", a, "-> public A = g^a mod p =", A)
print("Bob   private b =", b, "-> public B = g^b mod p =", B)

alice_key = pow(B, a, p)
bob_key = pow(A, b, p)
print("Shared secret computed by Alice:", alice_key)
print("Shared secret computed by Bob  :", bob_key)
print("Keys match:", alice_key == bob_key)

p = 2305843009213693951
g = 3
a = 123456789123
b = 987654321987
A = pow(g, a, p)
B = pow(g, b, p)
print("\nLarger prime example (p = 2^61 - 1):")
print("A =", A)
print("B =", B)
print("Shared secret (Alice):", pow(B, a, p))
print("Shared secret (Bob)  :", pow(A, b, p))
