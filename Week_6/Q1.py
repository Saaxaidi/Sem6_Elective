# Plaintext
plaintext = "Cyber Security"

# Keys to test
keys = [0, 1, 5]

for key in keys:
    # Encryption using XOR
    encrypted = ''.join(chr(ord(c) ^ key) for c in plaintext)
    
    # Decryption using XOR (same operation)
    decrypted = ''.join(chr(ord(c) ^ key) for c in encrypted)
    
    print(f"Key = {key}")
    print(f"Original  : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")
    print()