f=open("gmail_textfile","r")
import re
for lines in f:
    gmail_data=lines.rstrip("\n")
    #print(gmail_data)
    rule = "[a-z0-9.]*@gmail.com"
    match = re.fullmatch(rule,gmail_data)
    if (match != None):
        print(gmail_data)






