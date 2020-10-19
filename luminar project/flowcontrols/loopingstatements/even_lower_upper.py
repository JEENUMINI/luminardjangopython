lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
if(lower>upper):
    print("upper limit should be greater than lower limit")
while(lower<upper):
    if(lower%2==0):
        print(lower)
    lower+=1