f=open("random","r")
lst=[]
for lines in f:
    line=lines.rstrip("\n")
    words=line.split(" ")
    for j in words:
        lst.append(j.upper())
print(lst)