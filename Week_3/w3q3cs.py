def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euler_totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count


num = int(input("Enter a number: "))
print("Euler Totients of", num, "is", euler_totient(num))
