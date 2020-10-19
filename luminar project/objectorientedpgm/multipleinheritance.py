class Parent1:
    def m1(self):
        print("inside parent1")


class Parent2:
    def m2(self):
        print("inside parent2")

class Child(Parent1,Parent2):
    def m3(self):
        print("inside child")


c=Child()
c.m3()
c.m2()
c.m1()