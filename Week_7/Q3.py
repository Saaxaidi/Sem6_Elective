# Simplified Twofish (Feistel-like)

keys = [3, 7, 11, 5]   # round keys

# Simple function (like g-function in Twofish)
def F(x, k):
    return ((x ^ k) * 3) % 256

def encrypt(text):
    left = ord(text[0])
    right = ord(text[1])

    for i in range(2):   # 2 rounds (simplified)
        temp = left
        left = right ^ F(left, keys[i])
        right = temp

    return chr(left) + chr(right)


def decrypt(cipher):
    left = ord(cipher[0])
    right = ord(cipher[1])

    for i in range(1, -1, -1):   # reverse order
        temp = right
        right = left ^ F(right, keys[i])
        left = temp

    return chr(left) + chr(right)


# Example
text = "HI"

enc = encrypt(text)
dec = decrypt(enc)

print("Original  :", text)
print("Encrypted :", enc)
print("Decrypted :", dec)