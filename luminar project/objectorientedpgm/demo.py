#class-plan,design pattern,blue print
#object-real world entity
#reference-remote(in case of tv)
#s/x-
#class ClassName
     # methos



class Person:
    def setValues(self,ag,nam):
        self.age=ag
        self.name=nam

    def printValues(self):
        print("age=",self.age)
        print("name=",self.name)

    #object syntax referncename=ClassName()

obj=Person() #CREATING OBJECT
obj1=Person()
obj.setValues(27,"ajay")
obj1.setValues(26,"vijay")
obj.printValues()
obj1.printValues()
