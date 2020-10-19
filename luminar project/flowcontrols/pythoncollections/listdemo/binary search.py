ar=[6,4,5,2,1,3]
ar.sort() #[1, 2, 3, 4, 5, 6]
#ar=sorted(ar)
print(ar)
low=0
flag=0
upp=len(ar)#6
print(upp)
element=int(input("enter the search element"))
while(low<=upp):#0<6,4<6
    mid=(low+upp)//2  #3,5,4
    if(element>ar[mid]): #5>4,5>6,5>5
        low=mid+1   #4
    elif(element<ar[mid]): #5<6,5<5
        upp=mid-1          #4
    elif(element==ar[mid]):#5=5
        flag=1
        break
if(flag>0):
    print("found")
else:
    print("not found")





