limit=int(input("enter limit"))
sumeven=0
sumodd=0
for i in range(1,limit):
    if(i%2==0):
        sumeven=sumeven+i
    else:
        sumodd=sumodd+i
    i+=1
print("sum of even numbers", sumeven)
print("sum of odd numbers", sumodd)