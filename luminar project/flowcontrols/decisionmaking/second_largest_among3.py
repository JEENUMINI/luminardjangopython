num1=int(input("enter value for num1"))
num2=int(input("enter value for num2"))
num3=int(input("enter value for num3"))
if((num1>num2) & (num1>num3)):
    if(num2>num3):
        print("num2 is 2nd largest")
    else:
        print("num3 is 2nd largest")
elif((num2>num1) & (num2>num3)):
    if(num1>num3):
        print("num1 is 2nd largest")
    else:
        print("num3 is 2nd largest")
elif((num3>num1) & (num3>num2)):
    if(num1>num2):
        print("num1 is 2nd largest")
    else:
        print("num2 is 2nd largest")
else:
    print("all numbers are equal")