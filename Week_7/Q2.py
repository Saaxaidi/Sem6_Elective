# Simplified Blowfish (Feistel-based)

P = [3, 5, 7, 11]   # small P-array (keys)

def F(x):
    return (x * 3) % 256   # simple function

def encrypt(text):
    left = ord(text[0])
    right = ord(text[1])

    for i in range(2):   # 2 rounds (simplified)
        left = left ^ P[i]
        right = right ^ F(left)
        left, right = right, left   # swap

    left, right = right, left  # final swap

    right = right ^ P[2]
    left = left ^ P[3]

    return chr(left) + chr(right)


def decrypt(cipher):
    left = ord(cipher[0])
    right = ord(cipher[1])

    left = left ^ P[3]
    right = right ^ P[2]

    for i in range(1, -1, -1):  # reverse rounds
        left, right = right, left
        right = right ^ F(left)
        left = left ^ P[i]

    return chr(left) + chr(right)


# Example
text = "HI"

enc = encrypt(text)
dec = decrypt(enc)

print("Original  :", text)
print("Encrypted :", enc)
print("Decrypted :", dec)