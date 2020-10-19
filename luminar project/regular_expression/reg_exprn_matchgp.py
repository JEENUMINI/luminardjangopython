string="ababababbbbbbabbb"
    #   0123456789abcdefg
import re
pattern="ab"
matcher=re.finditer(pattern,string)

for match in matcher:
    print(match.group()) # group returns match founds with which object
