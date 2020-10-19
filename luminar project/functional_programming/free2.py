class Employee:
    def __init__(self,id,name,desig,exp,salary):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def printEmployee(self):
        print(self.id)
        print(self.name)
        print(self.desig)
        print(self.exp)
        print(self.salary)
lst=[]
f=open("employee_mapfilterreduce_text","r")
for lines in f:
    employee_data=lines.rstrip("\n").split(",")
    id=employee_data[0]
    name=employee_data[1]
    desig=employee_data[2]
    exp=employee_data[3]
    salary=employee_data[4]
    obj=Employee(id,name,desig,exp,salary)
    lst.append(obj)

