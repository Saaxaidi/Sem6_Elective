import time

def bf(pwd):
    length=len(pwd)
    attempt =0

    start_time =time.time()

    max_num = pow(10,length)

    for num in range(max_num):
        attempt+=1

        guess=str(num).zfill(length)

        if guess==pwd:
            end_time=time.time()
            print("pwd creacked")
            print("password: ",guess)
            print("attempt: ",attempt)
            print("time taken : ",round(end_time-start_time,4),"sec")
            return
    print("pwd not found!")

pwd =input("enter the numeric password(4,6,8) digits: ")
bf(pwd)
