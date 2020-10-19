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

task1=[obj.name for obj in lst if obj.desig=="developer"]
print(task1)

# convert all employees name to uppercase

task2=[obj.name.upper() for obj in lst]
print(task2)




# find total salary of all employees

task3=sum([obj.salary for obj in lst])
print(task3)

# find highest salaried employee

task4=max([obj.salary for obj in lst])
print(task4)

# task5=[obj.name for obj in lst if max(obj.salary)]
# print(task5)



