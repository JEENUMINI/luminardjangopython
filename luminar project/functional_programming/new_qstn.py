text="HHHPPSDAA"
dict={}
for cnt in text:
    if(cnt not in dict):
        dict[cnt]=1
    else:
        dict[cnt]+=1
#print(dict)

op=""
for k,v in dict.items():
    op=op+str(v)+k
print(op)

