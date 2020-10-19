f=open("numbers","r")
lst=[]

for numbers in f:
    number=int(numbers.rstrip("\n"))
    lst.append(number)


print(max(lst))
print(min(lst))