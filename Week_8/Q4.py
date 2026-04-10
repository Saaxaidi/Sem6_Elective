from sage.all import *

# Step 1: Define finite field
p = 17
F = GF(p)

# Step 2: Define elliptic curve: y^2 = x^3 + ax + b
a = 2
b = 2
E = EllipticCurve(F, [a, b])

print("Elliptic Curve:", E)

# Step 3: Choose a base point (generator)
G = E(5, 1)
print("Base Point G:", G)

# Step 4: Private keys (secret)
dA = 3   # Alice
dB = 5   # Bob

# Step 5: Public keys
PA = dA * G
PB = dB * G

print("Alice Public Key:", PA)
print("Bob Public Key:", PB)

# Step 6: Shared secret (ECDH)
SA = dA * PB
SB = dB * PA

print("Shared Secret computed by Alice:", SA)
print("Shared Secret computed by Bob:", SB)

# Step 7: Verification
if SA == SB:
    print("ECDH Key Exchange Successful")
else:
    print("Error in Key Exchange")