import hmac
import hashlib

# MAC (HMAC)
print("----- MAC (HMAC) -----")

key = b'secret_key'
message = b'Hello World'

# Create MAC
mac = hmac.new(key, message, hashlib.sha256).hexdigest()
print("Generated MAC:", mac)

# Verify MAC
mac_verify = hmac.new(key, message, hashlib.sha256).hexdigest()

if mac == mac_verify:
    print("MAC Verification: Success ")
else:
    print("MAC Verification: Failed ")


# Digital Signature (RSA)
print("\n----- Digital Signature (RSA) -----")

# Simple RSA values
p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)

e = 7
# Find d (mod inverse)
def mod_inverse(e, phi):
    for i in range(1, phi):
        if (e * i) % phi == 1:
            return i

d = mod_inverse(e, phi)

# Hash the message
msg_hash = int(hashlib.sha256(message).hexdigest(), 16)

# Sign (using private key)
signature = pow(msg_hash, d, n)
print("Signature:", signature)

# Verify (using public key)
verify = pow(signature, e, n)

if verify == msg_hash % n:
    print("Signature Verification: Success ")
else:
    print("Signature Verification: Failed ")