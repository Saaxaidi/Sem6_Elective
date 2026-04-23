# 2x2 Hill Cipher

key = [[3, 3], [2, 5]]   # Key matrix
inv_key = [[15, 17], [20, 9]]  # Inverse key

# Convert text → numbers (A=0,...Z=25)
def text_to_num(text):
    return [ord(c) - 65 for c in text]

# Convert numbers → text
def num_to_text(nums):
    return ''.join(chr(n + 65) for n in nums)

# Clean text (remove spaces/symbols)
def clean_text(text):
    return ''.join([c for c in text.upper() if c.isalpha()])

# Encrypt function
def encrypt(text):
    text = clean_text(text)

    if len(text) % 2 != 0:
        text += "X"   # padding

    nums = text_to_num(text)
    result = []

    for i in range(0, len(nums), 2):
        x, y = nums[i], nums[i+1]

        c1 = (key[0][0]*x + key[0][1]*y) % 26
        c2 = (key[1][0]*x + key[1][1]*y) % 26

        result.extend([c1, c2])

    return num_to_text(result)

# Decrypt function
def decrypt(cipher):
    nums = text_to_num(cipher)
    result = []

    for i in range(0, len(nums), 2):
        x, y = nums[i], nums[i+1]

        p1 = (inv_key[0][0]*x + inv_key[0][1]*y) % 26
        p2 = (inv_key[1][0]*x + inv_key[1][1]*y) % 26

        result.extend([p1, p2])

    return num_to_text(result)

# -------- File Handling --------

# Read input file
with open("Week_6/input.txt", "r") as f:
    text = f.read()

# Encrypt
encrypted = encrypt(text)

# Save encrypted text
with open("Week_6/encrypted.txt", "w") as f:
    f.write(encrypted)

# Decrypt
decrypted = decrypt(encrypted)

# Save decrypted text
with open("Week_6/decrypted.txt", "w") as f:
    f.write(decrypted)

print("Encryption & Decryption Done!")