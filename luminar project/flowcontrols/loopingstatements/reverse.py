num1=int(input("enter value for num1"))
res=0
while(num1!=0):
    digit=num1%10
    res=(res*10)+digit
    num1=num1//10
print(res)