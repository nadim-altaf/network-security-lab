key = "MONARCHY"
plaintext = "Instruments"

key = key.upper().replace("J", "I")
letters = ""
for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
    if ch not in letters:
        letters += ch

matrix = []
for i in range(0, 25, 5):
    matrix.append(list(letters[i:i + 5]))

print("Key matrix:")
for row in matrix:
    print("  ", " ".join(row))

text = plaintext.upper().replace("J", "I")
pairs = []
i = 0
while i < len(text):
    a = text[i]
    if i + 1 < len(text):
        b = text[i + 1]
    else:
        b = "X"
    if a == b:
        b = "X"
        i += 1
    else:
        i += 2
    pairs.append(a + b)
print("Digraphs   :", " ".join(pairs))

def position(ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

def convert(pairs, shift):
    result = ""
    for pair in pairs:
        r1, c1 = position(pair[0])
        r2, c2 = position(pair[1])
        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5] + matrix[r2][(c2 + shift) % 5]
        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1] + matrix[(r2 + shift) % 5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]
    return result

cipher = convert(pairs, 1)
print("Ciphertext :", cipher)

cipher_pairs = []
for i in range(0, len(cipher), 2):
    cipher_pairs.append(cipher[i:i + 2])
print("Decrypted  :", convert(cipher_pairs, -1))
