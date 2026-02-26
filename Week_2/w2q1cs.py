def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
