class Parent:
    def m1(self):
        print("inside parent")

class Child(Parent):
    def m2(self):
        print("inside child")

class subChild(Child):
    def m3(self):
        print("inside subchild")

sb=subChild()
sb.m3()
sb.m2()
sb.m1()

sb2=Child()
#sb2.m3()//error
sb2.m2()
sb2.m1()

p=Parent()
# p.m3() //error
# p.m2() //error
p.m1()
