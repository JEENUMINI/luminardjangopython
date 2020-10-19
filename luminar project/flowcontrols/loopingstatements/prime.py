num1=int(input("enter value for num1"))
flg=0
for i in range(2,num1):
    if(num1%i==0):
        flg=1
        break
    else:
        flg=0
if(flg>0):
    print("not prime")
else:
    print("prime")


