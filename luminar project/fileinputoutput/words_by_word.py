f=open("words","r")
lst=[]
for lines in f:
    line=lines.rstrip("\n")
    words=line.split(" ")
    for word in words:

        lst.append(word)

print(lst)





