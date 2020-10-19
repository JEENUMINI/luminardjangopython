import re
#kl08bn1375
vechicle=input("enter vechile no")
#rule="kl[0-9]{2}[a-z]{2}\d{4}"
rule="kl[0-9]{2}[a-z]{1,2}\d{4}" # in case of one alphabet after kl\d{2}
match=re.fullmatch(rule,vechicle)
if(match==None):
    print("invalid")
else:
    print("valid")