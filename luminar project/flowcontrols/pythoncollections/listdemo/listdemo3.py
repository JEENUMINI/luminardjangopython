lst=[10,11,12,13,14,15,16,17]
sumeven=0
sumodd=0
for item in lst:
    if(item%2==0):
        sumeven=sumeven+item
    else:
        sumodd=sumodd+item

print(sumeven)
print(sumodd)