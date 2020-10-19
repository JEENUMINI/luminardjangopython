lst=[2,1,3,4,7,6,5]
minimum=lst[0]
maximum=lst[0]
for i in lst[1:]:
    if(i<minimum):
        minimum=i


    elif(i>maximum):
        maximum=i
print(minimum)
print(maximum)
