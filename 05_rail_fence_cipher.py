# Experiment 5: Rail Fence Transposition Cipher
def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    r, d = 0, 1
    for ch in text:
        fence[r].append(ch)
        if r == 0: d = 1
        elif r == rails - 1: d = -1
        r += d
    return fence, "".join("".join(row) for row in fence)

def decrypt(cipher, rails):
    n = len(cipher)
    pattern, r, d = [], 0, 1
    for _ in range(n):
        pattern.append(r)
        if r == 0: d = 1
        elif r == rails - 1: d = -1
        r += d
    idx = sorted(range(n), key=lambda i: pattern[i])
    res = [""] * n
    for pos, ch in zip(idx, cipher):
        res[pos] = ch
    return "".join(res)

plaintext = "NETWORKSECURITY"
rails = 3
fence, cipher = encrypt(plaintext, rails)
print("Plaintext  :", plaintext)
print("Rails      :", rails)
print("Rail layout:")
for row in fence:
    print("  ", "".join(row))
print("Ciphertext :", cipher)
print("Decrypted  :", decrypt(cipher, rails))
