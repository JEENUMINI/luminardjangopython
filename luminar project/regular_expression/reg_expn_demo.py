#pattern matching
string="ababababbbbbbabbb"
#count number of ab in given string
import re
pattern="ab"
matcher=re.finditer(pattern,string)
count=0
for match in matcher:
    count+=1
print(count)