import hashlib

# Input text
text = "Cyber Security"

# Convert text to bytes
data = text.encode()

# Create SHA-1 hash
hash_object = hashlib.sha1(data)

# Get hexadecimal digest
digest = hash_object.hexdigest()

print("Text   :", text)
print("SHA-1  :", digest)