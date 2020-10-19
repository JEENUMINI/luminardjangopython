lst=[10,11,12,13,14,15,16,17]


search=int(input("serach element"))
flg=0
for item in lst:
    if(item==search):

        flg=1
        break
    else:

        flg=0

if(flg>0):
    print("element found")
else:
    print("element not found")

#     or
#
#
# piu=[2,4,5,8,10,1,3,5,7,9]
# search=int(input("search element"))
# count=0
# for item in piu:
#     if(item==search):
#         count=count+1
#         break
#     else:
#         count=0
#
# if(count>0):
#     print("element is found")
# else:
#     print("element is not found")
