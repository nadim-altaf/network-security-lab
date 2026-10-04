plaintext = "NETWORKSECURITY"
rails = 3

fence = [""] * rails
row = 0
direction = 1
for ch in plaintext:
    fence[row] += ch
    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1
    row += direction

cipher = "".join(fence)

print("Plaintext  :", plaintext)
print("Rails      :", rails)
print("Rail layout:")
for r in fence:
    print("  ", r)
print("Ciphertext :", cipher)

order = []
row = 0
direction = 1
for i in range(len(cipher)):
    order.append(row)
    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1
    row += direction

result = [""] * len(cipher)
k = 0
for r in range(rails):
    for i in range(len(cipher)):
        if order[i] == r:
            result[i] = cipher[k]
            k += 1

print("Decrypted  :", "".join(result))
