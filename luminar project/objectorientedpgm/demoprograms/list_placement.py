inp=[4,1,2,5,6,7]
op=[]
# if(x>5), x+1 and if(x<5),x-1 [3,0,1,5,7,8]
for item in inp:
    if(item>5):
        item=item+1
    elif(item<5):
        item=item-1
    op.append(item)
print(op)

