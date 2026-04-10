from sage.all import *

# Step 1: Define a finite field (mod prime)
p = 17
F = GF(p)

# Step 2: Define Elliptic Curve: y^2 = x^3 + ax + b
a = 2
b = 2
E = EllipticCurve(F, [a, b])

print("Elliptic Curve:", E)

# Step 3: Define a base point (generator)
G = E(5, 1)   # make sure this point lies on the curve
print("Base Point G:", G)

# Step 4: Private keys (chosen secretly)
dA = 3   # Alice's private key
dB = 5   # Bob's private key

# Step 5: Public keys
PA = dA * G
PB = dB * G

print("Alice Public Key:", PA)
print("Bob Public Key:", PB)

# Step 6: Shared secret key
SA = dA * PB
SB = dB * PA

print("Shared Key (Alice):", SA)
print("Shared Key (Bob):", SB)

# Verify both are same
if SA == SB:
    print("Key Exchange Successful")
else:
    print("Error")