class Student:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total

    def printStudent(self):
        print("rol no=",self.rol)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)

    def __str__(self):
        return self.name # for indicating object by name instead of refernce adds

f=open("student","r")
lst=[]

for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    id=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])
    obj=Student(id,name,course,total)
    lst.append(obj)


# print all student name who have total>450
for obj in lst:
    #print(obj)
    if obj.total>450:
        print(obj)


# print highest total

total=[]
for obj in lst:
    total.append(obj.total)
maximum=max(total)
for obj in lst:
    if obj.total==maximum:
        print(obj)
