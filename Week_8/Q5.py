from sage.all import *

# Step 1: Choose two prime numbers
p = 11
q = 13

# Step 2: Compute n and phi(n)
n = p * q
phi = (p - 1) * (q - 1)

print("p =", p)
print("q =", q)
print("n =", n)
print("phi(n) =", phi)

# Step 3: Choose public key e
e = 7   # must be coprime with phi(n)

# Step 4: Compute private key d
d = inverse_mod(e, phi)

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Step 5: Message (must be < n)
m = 9
print("Original Message:", m)

# Step 6: Encryption: C = m^e mod n
c = power_mod(m, e, n)
print("Encrypted Cipher:", c)

# Step 7: Decryption: M = C^d mod n
decrypted = power_mod(c, d, n)
print("Decrypted Message:", decrypted)