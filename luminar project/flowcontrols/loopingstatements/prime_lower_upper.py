lower=int(input("enter lower"))
upper=int(input("enter upper"))

flag=0
for i in range(lower,upper):
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    else:
        flag=0

    if(flag==0):
        print(i)


