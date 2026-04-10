from sage.all import *
import hashlib

# Input message
text = "Hello World"

# Convert to bytes
data = text.encode()

print("Original Text:", text)

# 🔸 SHA-1
sha1_hash = hashlib.sha1(data).hexdigest()
print("\nSHA-1 :", sha1_hash)

# 🔸 SHA-2 (using SHA-256)
sha2_hash = hashlib.sha256(data).hexdigest()
print("SHA-2 (SHA-256):", sha2_hash)

# 🔸 SHA-3 (using SHA3-256)
sha3_hash = hashlib.sha3_256(data).hexdigest()
print("SHA-3 (SHA3-256):", sha3_hash)