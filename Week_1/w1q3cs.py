n = int(input("Enter a number: "))
temp = n
sum = 0

digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
