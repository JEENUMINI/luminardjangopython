lst=[2,3,4,5,6,7]
for item in lst:
    for i in range(2,item):
        if(item%i==0):
            flag=1
            break
    else:
        flag=0
        print(item)
