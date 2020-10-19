import re

gmail_id=input("enter gmail id")
rule="([a-z0-9.]*)@gmail.com"

match=re.fullmatch(rule,gmail_id)
if(match==None):
    print("invalid")
else:
    print("valid")