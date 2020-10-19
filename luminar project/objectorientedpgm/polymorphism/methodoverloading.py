class Maths:
    def add(self):
        num1,num2=10,20
        print(num1+num2)

    def add(self,num1):
        num2=50
        print(num1+num2)

    def add(self,num1,num2): # recently added method
        print(num1+num2)

# same method name and different number of arguments
ob=Maths()
ob.add(10,20) # python does not support method overloading.Always work with recently added method.if it is not there then 2nd method will work.
#ob.add(10) not working
#ob.add()
#ob.add(20)

