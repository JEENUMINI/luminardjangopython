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



obj=Student()
obj.setStudent(1001,"mini","mca",500)
obj.printStudent()

#self is a keyword used to point current object instance variables

