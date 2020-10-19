num1 = int(input("enter element"))
for i in range(1, (num1 + 1)):
    for j in range(1, (num1 + 1)):
        if ((i + j) == num1):
            print(i, j)
