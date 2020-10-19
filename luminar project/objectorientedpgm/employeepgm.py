# example for constructor

class Employee:
    company_name="luminar technolab"
    def __init__(self,id,desig,sal):
        self.id=id
        self.desig=desig
        self.salary=sal

    def printEmp(self):
        print("eid=",self.id)
        print("designation=",self.desig)
        print("salary=",self.salary)
        print("company name=",Employee.company_name)

emp=Employee(1001,"develop",30000)
emp.printEmp()