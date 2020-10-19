line="ABCDABCC"

dict={}
for character in line:
    if(character not in dict):
        dict[character]= 1
    else:
        print(character,"is the first recursive character")
        break





