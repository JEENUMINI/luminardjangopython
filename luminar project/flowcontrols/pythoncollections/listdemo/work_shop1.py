

lst=[1,2,3,5]
count=1

out=[]
for item in lst:
    mul=item**count
    count+=1
    out.append(mul)
print(out)