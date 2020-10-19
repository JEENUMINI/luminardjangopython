f=open("temp","r")
f1=open("output.txt","w")
dt={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    district=data[0]
    temp=data[1]
    if(district not in dt):
        dt[district]=temp
    else:
        maxi=max(temp,dt[district])
        dt[district]=maxi


#print(dt)
#print(sort)

lst=[]
for k,v in dt.items():
    lst.append((k,v))
for val in lst:
    f1.write(str(val))