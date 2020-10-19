from re import *

pattern="aaaabbbbaaabbabbaaaaa"
#x="a+" # it will return single a and sequences of a
#x="a*" # does same duty of "a+".also check for other positions
#x='a?'  # chk for a's position and also others position
#x="^a" # chk the given pattern is starting with a
#x="a$" # chk the given pattern is ending with a
#x="a{2}" # chk for two number of a
x="a{2,3}" #chk for atleast 2 atmost(max) 3

matcher=finditer(x,pattern)

for match in matcher:
    print(match.start())
    print(match.group())
