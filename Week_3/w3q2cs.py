def is_mersenne_prime(n):
    k = 1
    while (2 ** k) - 1 <= n:
        if (2 ** k) - 1 == n:
            return True
        k += 1
    return False

num = int(input("Enter a prime number: "))

if is_mersenne_prime(num):
    print(num, "is a Mersenne prime")
else:
    print(num, "is NOT Mersenne prime")
