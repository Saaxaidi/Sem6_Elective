# Diffie-Hellman Key Exchange

# Public values
p = 23   # prime number
g = 5    # generator

# Private keys (secret)
a = 6    # Alice's private key
b = 15   # Bob's private key

# Public keys
A = (g ** a) % p   # Alice sends to Bob
B = (g ** b) % p   # Bob sends to Alice

# Shared secret key
key_A = (B ** a) % p
key_B = (A ** b) % p

print("Public values: p =", p, ", g =", g)
print("Alice Public Key:", A)
print("Bob Public Key  :", B)

print("Shared Key (Alice):", key_A)
print("Shared Key (Bob)  :", key_B)