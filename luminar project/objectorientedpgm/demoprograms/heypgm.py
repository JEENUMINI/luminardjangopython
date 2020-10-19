string="HEY" #op=HEEYY

cnt=1
data=""
#print(type(data))
for char in string:
    data+=cnt*char
    cnt+=1
print(data)