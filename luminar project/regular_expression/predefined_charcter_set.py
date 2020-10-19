import re
#predefined characters
#x="[abc]" # it will chk either a,b or c is present in target string
#x="[a-z]"  # it will chk lower case a to z alphabets
#x="[0-9]"   # itwill chk for digits from 0 to 9
#x="[1-9]"   # itwill chk for digits from 1 to 9
#x="[A-Z]" # it will chk upper case A to Z alphabets
#x="[a-zA-z]" # it will chk all lower case and upper case alphabets
#x="[a-zA-Z0-9]" #it will chk all lower case and upper case alphabets and digits from 0-9// chk for all words
#x="[^a-zA-Z0-9]" #except this all others will print=special chars
#x="[^0-9]" #except numbers
#predefined character set
#x="\s" # chk for spaces
#x="\d" # chk for digit==[0-9]
#x="\D" #==[^0-9]
#x="\w" #==[a-zA-Z0-9]
x="\W" #==[^a-zA-Z0-9]


matcher=re.finditer(x,"ab7 c@KZ")
for match in matcher:
    print(match.start())
    print(match.group())