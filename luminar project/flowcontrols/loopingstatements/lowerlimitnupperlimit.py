lower=int(input("enter lower limit"))
upper=int(input("enter lower limit"))
if(lower>upper):
    print("upper limit should be greater than lower limit")
while(lower<upper):
    print(lower)
    lower+=1
