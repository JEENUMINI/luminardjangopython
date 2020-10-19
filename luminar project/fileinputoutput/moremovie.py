f=open("movies.csv","r")
dict={}
for lines in f:
    movies=lines.rstrip("\n").split(",")

    year=movies[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

lst=[]
for k,v in dict.items():
    lst.append((v,k))
srt=sorted(lst,reverse=True)
print(srt[0])