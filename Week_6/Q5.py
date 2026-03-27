# Simple Feistel Cipher (2 rounds)

def F(right, key):
    return right ^ key   # simple function (XOR)

def feistel_encrypt(text, key1, key2):
    # Convert text to ASCII numbers
    left = ord(text[0])
    right = ord(text[1])

    # Round 1
    temp = right
    right = left ^ F(right, key1)
    left = temp

    # Round 2
    temp = right
    right = left ^ F(right, key2)
    left = temp

    return chr(left) + chr(right)


def feistel_decrypt(cipher, key1, key2):
    # Reverse process (keys in reverse order)
    left = ord(cipher[0])
    right = ord(cipher[1])

    # Round 2 (reverse)
    temp = left
    left = right ^ F(left, key2)
    right = temp

    # Round 1 (reverse)
    temp = left
    left = right ^ F(left, key1)
    right = temp

    return chr(left) + chr(right)


# Example
plaintext = "HI"
key1 = 5
key2 = 7

encrypted = feistel_encrypt(plaintext, key1, key2)
decrypted = feistel_decrypt(encrypted, key1, key2)

print("Original  :", plaintext)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)