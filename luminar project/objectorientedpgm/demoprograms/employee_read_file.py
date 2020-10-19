class Employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.designation=desig
        self.experience=exp
        self.salary=salary

    def printEmployee(self):
        print("id=",self.id)
        print("name=",self.name)
        print("designation=",self.designation)
        print("experience=",self.experience)
        print("salary=",self.salary)

    def __str__(self):
        return self.name

f=open("employeeoop","r")
lst=[]
for lines in f:
    employee_data=lines.rstrip("\n").split(",")
    id=employee_data[0]
    name=employee_data[1]
    desig=employee_data[2]
    exp=employee_data[3]
    salary=employee_data[4]
    obj=Employee(id,name,desig,exp,salary)
    lst.append(obj)

salary=[]
for obj in lst:
    salary.append(obj.salary)
maximum=max(salary)
for obj in lst:
    if((obj.salary)==maximum):
        print(obj)




