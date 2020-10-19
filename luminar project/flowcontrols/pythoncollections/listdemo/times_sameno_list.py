lst=[1,2,2,2,4,4]
num=int(input("enter number"))
count=0
for item in lst:
    if(item==num):
        count+=1
print(count)