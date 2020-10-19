class Student:
    college_name="luminar technolab"
    def __init__(self,rol,name,total):
        self.rol=rol
        self.name=name
        self.total=total

    def printStudent(self):
        print("rol=",self.rol)
        print("name=",self.name)
        print("total=",self.total)
        print("college name=",Student.college_name)

obj=Student(1001,"ajay",150)
obj.printStudent()