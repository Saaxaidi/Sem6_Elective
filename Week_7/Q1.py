# Simple hash function

def simple_hash(text):
    hash_value = 0
    
    for ch in text:
        hash_value += ord(ch)   # add ASCII value
    
    return hash_value % 100   # keep hash small


# Example
text = "Cyber Security"

h = simple_hash(text)

print("Text :", text)
print("Hash :", h)