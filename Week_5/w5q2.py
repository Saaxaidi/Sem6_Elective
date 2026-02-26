import random
import time
import itertools

def generate_password(length):
    """Generate a random numeric password of given length."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def brute_force(password):
    """Attempt to brute force the given numeric password."""
    length = len(password)
    attempts = 0
    start_time = time.time()

    # Generate all possible combinations
    for guess in itertools.product('0123456789', repeat=length):
        attempts += 1
        guess_password = ''.join(guess)

        if guess_password == password:
            end_time = time.time()
            print(f"\nPassword Cracked: {guess_password}")
            print(f"Total Attempts: {attempts}")
            print(f"Time Taken: {end_time - start_time:.4f} seconds")
            break


# Test for 4, 6, and 8 digit passwords
for length in [4, 6, 8]:
    print(f"\n--- Testing {length}-digit Password ---")
    pwd = generate_password(length)
    print("Generated Password (hidden in real attack):", pwd)
    brute_force(pwd)
