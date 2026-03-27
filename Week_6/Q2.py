def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces and symbols unchanged
    
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Reverse shift


# Example usage
plaintext = "Cyber Security"
shift = 3

encrypted = encrypt(plaintext, shift)
decrypted = decrypt(encrypted, shift)

print("Original  :", plaintext)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)