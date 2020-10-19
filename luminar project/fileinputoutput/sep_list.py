f=open("employee","r")
ename=[]
esal=[]

for lines in f:
    line=lines.rstrip("\n")
    data=line.split(",")
    name=data[1]
    salary=data[2]
    ename.append(name)
    esal.append(salary)

print(ename)
print(esal)
