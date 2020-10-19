lst=[1,2,3,4]
element=int(input("enter element"))
lst.sort()
low=0
upp=len(lst)-1#3
while(low<upp):#0<3,1<3
    total=lst[low]+lst[upp]#5,6
    if(total==element):#6==6
        print("pairs=",lst[low],lst[upp])#2,4
        break
    elif(total>element):

        upp=upp-1

    elif(total<element):#5<6
        low=low+1       #1
