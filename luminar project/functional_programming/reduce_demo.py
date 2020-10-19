# print total of the list

from functools import *
numbers=[10,11,12,13,14]

total=(reduce(lambda num1,num2:num1+num2,numbers))
print(total)

# print total of the list

maximum=reduce(lambda num1,num2:num1 if num1>num2 else num2,numbers)
print(maximum)