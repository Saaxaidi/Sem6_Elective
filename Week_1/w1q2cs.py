number =int(input("Enter the number : "))
sum = 0 
for i in range(1,number):
    if(number%i==0):
        sum+=i

if(sum ==number):
    print(number,"is the perfect number")
else:
    print(number, "is not the perfect number")