class Parent1:
    def m1(self):
        print("inside parent1")


class Parent2:
    def m1(self):
        print("inside parent2")

class Child(Parent2,Parent1):
    def m3(self):
        print("inside child")


c=Child()
c.m3()

c.m1()
#here 2 inheritace classes have same method.then python will take method in the given order of  inheritance class.
# here class Child(Parent2,Parent1): means it will take method of parent 2 on the basis of the given order.