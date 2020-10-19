#print all employee name who have salary > 25000
employees=[
        [100,"ajay",25000],
        [101,"vijay",22000],
        [102,"binoy",27000],
        [103,"jino",30000],
        ]

for data in employees:
    if(data[2]>25000):
        print(data[1])