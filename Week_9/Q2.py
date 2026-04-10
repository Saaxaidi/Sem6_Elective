from sage.all import *
import hashlib

# Input message
text = "Hello World"

# Convert to bytes
data = text.encode()

print("Original Text:", text)

# MD5 Hash
md5_hash = hashlib.md5(data).hexdigest()

print("MD5 Hash:", md5_hash)