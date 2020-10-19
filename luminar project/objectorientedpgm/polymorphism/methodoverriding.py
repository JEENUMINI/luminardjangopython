class Parent:
    def phone(self):
        print("i have a nokia")

class Child(Parent):
    def phone(self):
        print("iphone")

c=Child()
c.phone()

#parent->child
#super class->sub class
#base class->derived class