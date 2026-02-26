def is_power_of_two(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1

num = int(input("Enter a number: "))

if is_power_of_two(num):
    k = 0
    temp = num
    while temp > 1:
        temp = temp // 2
        k += 1
    print(num, "is in the form of 2k (for k =", k, ")")
else:
    print(num, "is NOT in the form of 2k")
