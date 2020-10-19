lst=[1,2,3,4,5,6]

#squares
squares=[i*i for i in lst]
print(squares)

square2=[i**2 for i in lst]
print(square2)

#fetch even no from list
even=[i for i in lst if i%2==0]
print(even)

#list placement question
# task=[i+1 if i>5 else i-1 for i in lst]
# print(task)

task=[i+1 if i>5 else (i-1 if i<5 else i) for i in lst]
print(task)