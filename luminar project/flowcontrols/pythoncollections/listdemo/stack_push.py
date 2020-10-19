size=int(input("enter size"))#3= 0 1 2

stk=[]
top=0
def push(elemnt):
    global top
    if(top>=(size-1)):
        print("stack full")
    else:
        stk.append(elemnt)

        top+=1

def pop():
    global top
    if(top<=0):
        print("empty stack")
    else:
        top = top - 1
        print(top)

        print((stk[top]+1),"popped")



def display():
    for i in range(0,top):
        print(stk[i])
n=1
while(n!=0):
    option=int(input("enetrr opertaion 1)push 2)pop 3)display"))
    if(option==1):
        element=int(input("enter elemnt to push"))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
    n=int(input("u do u want to continue press 0 for exit 1 for continue"))

