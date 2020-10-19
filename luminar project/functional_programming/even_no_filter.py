numbers=[1,2,3,4,5,6]

def even(num):
    return num%2==0
evens=list(filter(even,numbers))
print(evens)

#  using lambda function

evens=list(filter(lambda num:num%2==0,numbers))
print(evens)