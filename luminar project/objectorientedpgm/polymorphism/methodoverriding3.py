#we are doing method overriding on to string method

class Student:
    def setStudent(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total
    def printStudent(self):
        print(self.rol)
        print(self.name)
        print(self.course)
        print(self.total)

    def __str__(self):
        return  self.name
        #return  self.name+str(self.course)+str(self.total)

obj=Student()
obj.setStudent(1001,"mini","mca",500)
#obj.printStudent()


print(obj) # Here we are printing object __str__(self) called to string() method