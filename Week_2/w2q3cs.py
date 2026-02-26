def gcd(a,b):
    while b!=0:
        a, b = b, a % b
    return a
    
x = int(input("enter the number 1 : "))
y = int(input("enter the number 2 : "))

if(gcd(x,y)==1):
    print("two numbers are relatively prime")
else:
    print("two numbers are not relatively prime")