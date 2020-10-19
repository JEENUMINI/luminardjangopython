num=int(input("enter num"))
first_value=0
second_value=1
for i in range(0,num+1):
    if(i<=1):
        next=i
    else:
        next=first_value+second_value
        first_value=second_value
        second_value=next
    i+=1
    print(next)