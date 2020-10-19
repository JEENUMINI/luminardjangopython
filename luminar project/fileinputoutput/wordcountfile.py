f=open("words","r")
dict={}

for lines in f:
    words=lines.rstrip("\n").split(" ")

    for word in words:
        word=word.lower()#some may be in caps
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1

print(dict)
