employees=[
        [100,"ajay",2300],
        [101,"vijay",200],
        [100,"sajay",290],
        ]
sum=0
for data in employees:
    if(data[2]>200):
        sum=sum+data[2]
print(sum)