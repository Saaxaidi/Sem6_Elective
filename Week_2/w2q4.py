def narcissistic(n):
    for num in range(10**(n-1), 10**n):
        sum = 0
        temp = num

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** n
            temp = temp // 10

        if sum == num:
            print(num, end=", ")

n = int(input("Enter value of n: "))
narcissistic(n)
