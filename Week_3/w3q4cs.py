def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def order(r, n):
    if gcd(r, n) != 1:
        return -1   # order does not exist

    k = 1
    value = r % n

    while value != 1:
        value = (value * r) % n
        k += 1

    return k

r = int(input("Enter value of r: "))
n = int(input("Enter value of n: "))

ord_val = order(r, n)

if ord_val == -1:
    print("Order does not exist since r and n are not coprime")
else:
    print("Order of", r, "under modulo", n, "is", ord_val)
