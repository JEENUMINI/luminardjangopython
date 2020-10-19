class Employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.experience=exp
        self.salary=salary

    def printEmployee(self):
        print("id=",self.id)
        print("name=",self.name)
        print("designation=",self.desig)
        print("experience=",self.experience)
        print("salary=",self.salary)

    def __str__(self):
        return self.name

f=open("employee_mapfilterreduce_text","r")
lst=[]
for lines in f:
    employee_data=lines.rstrip("\n").split(",")
    print(employee_data)
    id=employee_data[0]
    name=employee_data[1]
    desig=employee_data[2]
    exp=employee_data[3]
    salary=int(employee_data[4])
    obj=Employee(id,name,desig,exp,salary)
    lst.append(obj)

# Find all employees whose desig=developer

# for obj in lst:
#     if(obj.desig=="developer"):
#         print(obj)

task1=filter(lambda obj:obj.desig=="developer",lst)
for names in task1:
    print(names)


# convert all employees name to uppercase

task2=list(map(lambda obj:obj.name.upper(),lst))
print(task2)


# find highest salaried employee
from functools import *
task3=reduce(lambda salary1,salary2:salary1 if salary1>salary2 else salary2,map(lambda obj:obj.salary,lst))
print(task3)


# sal_lst=[]
# for obj in lst:
#     sal_lst.append(obj.salary)
# print(sal_lst)
# from functools import *
# task3=reduce(lambda num1,num2:num1 if num1>num2 else num2,sal_lst)
# for obj in lst:
#     if(obj.salary==task3):
#         print(obj)

# find total salary of all employees


task4=reduce(lambda salary1,salary2:salary1+salary2,list(map(lambda obj:obj.salary,lst)))
print(task4)
# op=list(map(lambda obj:obj.salary,lst))
# print(op)

# task4=reduce(lambda num1,num2:num1+num2,sal_lst)
# print(task4)







