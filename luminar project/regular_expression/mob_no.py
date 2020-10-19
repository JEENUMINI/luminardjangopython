import re
mob=input("enter mob no")
#rule="[0-9]{10}"
#rule="\d{10}"
rule='(91)?\d{10}'
match=re.fullmatch(rule,mob)
if(match==None):
    print("invalid")
else:
    print("valid")