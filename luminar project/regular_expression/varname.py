import re
#rule
# first character should be an alphabet with in a to k
# second character must be a number it is divisible by 3
# following by any words

#l3yhk invalid
#a2hjkl invalid
#a6ght valid

rule="[a-k][369][a-zA-Z0-9]*" # if * not it fails in these cases a3hjggjjkjjjj and a3
pattern=input("enter variable name")
match=re.fullmatch(rule,pattern)
if(match==None):
    print("invalid variable name")
else:
    print("valid variable name")