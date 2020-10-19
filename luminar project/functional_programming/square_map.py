def squares(num):
    return num*num

numbers=[1,2,3,4,5,6]

data=list(map(squares,numbers)) # args function,iterable
print(data)


#  using lambda function

data=list(map(lambda num:num*num,numbers))
print(data)
