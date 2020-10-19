text="100,200,300,100,120,200,300"
words=text.split(",")
dict={}
for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1

print(dict)