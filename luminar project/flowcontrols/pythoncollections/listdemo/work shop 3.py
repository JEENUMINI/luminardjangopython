lst=[1,2,3,4]
num1=int(input("enter number"))
sum=0
for item in lst:
    for i in lst:
        sum=item+i
        if(sum==num1):
            print(item,i)






