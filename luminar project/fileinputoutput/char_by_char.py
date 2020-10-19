f=open("cat","r")
lst=[]
for lines in f:
    line=lines.rstrip("\n")
    words=line.split(" ")
    for word in words:
        for char in word:
            lst.append(char)

print(lst)





