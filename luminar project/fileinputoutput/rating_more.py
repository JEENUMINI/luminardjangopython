f=open("movies.csv","r")
dict={}
for lines in f:
    movies=lines.rstrip("\n").split(",")

    rating=movies[3]
    if(rating not in dict):
        dict[rating]=1
    else:
        dict[rating]+=1
lst=[]
for k,v in dict.items():
    lst.append((k,v))
srt=sorted(lst,reverse=True)
print(srt[0])