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

f=open("student_mapfilterreduce_text","r")
lst=[]

for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    id=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])
    obj=Student(id,name,course,total)
    lst.append(obj)

# convert all students name to uppercase

task1=[obj.name.upper() for obj in lst]
print(task1)


# print all student name who have total>400

task2=[obj.name for obj in lst if obj.total>400]
print(task2)


#print all student name who studies bca course


task3=[obj.name for obj in lst if obj.course=="bca"]
print(task3)


# print sum of total

task4=sum([obj.total for obj in lst])
print(task4)

#print max of total

task5=max([obj.total for obj in lst])
print(task5)


#print min total student name

task6=min([obj.total for obj in lst])
for obj in lst:
    if(obj.total==task6):
        print(obj.name)


