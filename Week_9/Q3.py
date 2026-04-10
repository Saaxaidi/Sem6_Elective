import hmac
import hashlib

# Secret key (shared between sender and receiver)
key = b'secret_key'

# Message
message = b'Hello World'

print("Message:", message.decode())

# Create HMAC using SHA-256
hmac_obj = hmac.new(key, message, hashlib.sha256)

# Generate HMAC (digest)
hmac_value = hmac_obj.hexdigest()

print("HMAC (SHA-256):", hmac_value)
