def fact(x):
    res=1
    for i in range(1,x+1):
        res=res*i
    return res

print(fact(6))