import datetime

class Person:
    def setPerson(self,name,age):
        self.name=name
        self.age=age

    def printPerson(self):
        print(self.name,",",self.age)

class Bank(Person):
    bank_name="sbk" #static variable
    def createAccount(self,acno):
        self.acno=acno


        self.balance=3000 #min balance

    def deposit(self,amount):
        self.balance+=amount
        print("your",Bank.bank_name,"has been credited with",amount,"aval balance",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient balance in your account")
        else:
            self.balance-=amount
            print("your",Bank.bank_name,"has been debited with",amount,"on",datetime.date.today(),"aval balance",self.balance)

    def balenq(self):
        print("your account balance",self.balance)

obj=Bank()
obj.setPerson("ajay",27)
obj.printPerson()
#obj.createAccount(1001,"dinu","sbk",5000)
#obj.withdraw(10000)

#obj.createAccount(1002,"dinu","sbk",50000)
# obj.withdraw(10000)

#obj.createAccount(1002,"dinu","sbk",50000)
#obj.deposit(10000)

obj.createAccount(1002)
#obj.balenq()
obj.deposit(10000)