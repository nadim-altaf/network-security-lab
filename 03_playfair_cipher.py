# Experiment 3: Playfair Cipher
def build_matrix(key):
    key = key.upper().replace("J", "I")
    seen, matrix = set(), []
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

def prepare(text):
    text = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def process(pairs, matrix, step):
    out = ""
    for a, b in pairs:
        r1, c1 = find(matrix, a)
        r2, c2 = find(matrix, b)
        if r1 == r2:
            out += matrix[r1][(c1 + step) % 5] + matrix[r2][(c2 + step) % 5]
        elif c1 == c2:
            out += matrix[(r1 + step) % 5][c1] + matrix[(r2 + step) % 5][c2]
        else:
            out += matrix[r1][c2] + matrix[r2][c1]
    return out

key = "MONARCHY"
plaintext = "Instruments"
matrix = build_matrix(key)
print("Key matrix:")
for row in matrix:
    print("  ", " ".join(row))
pairs = prepare(plaintext)
print("Digraphs   :", " ".join(pairs))
cipher = process(pairs, matrix, 1)
print("Ciphertext :", cipher)
dec = process([cipher[i:i+2] for i in range(0, len(cipher), 2)], matrix, -1)
print("Decrypted  :", dec)
