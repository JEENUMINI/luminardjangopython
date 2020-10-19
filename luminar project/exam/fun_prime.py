def prime(low,upp):


    for i in range(low,upp):
        flag = 0
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
        else:
            flag=0
            if(flag==0):
                print(i)

low=int(input("enter low"))
upp=int(input("enter upp"))
prime(low,upp)



