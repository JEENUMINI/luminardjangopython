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

# convert student name to uppercse

names=list(map(lambda obj:obj.name.upper(),lst))
print(names)

# print all student name who have total>400

stud=filter(lambda obj:obj.total>400,lst)
for st in stud:
    print(st)



#print all student name who studies bca course


task=filter(lambda obj: obj.course=="bca",lst)
for nm in task:
    print(nm)


# print sum of total

from functools import *
task1=reduce(lambda total1,total2:total1+total2,map(lambda obj:obj.total,lst))
print(task1)

#print max of total

task2=reduce(lambda total1,total2:total1 if total1>total2 else total2,map(lambda obj:obj.total,lst))
print(task2)



