import datetime
class Bank:
    def createAccount(self,acno,personname,bname,balance):
        self.acno=acno
        self.person_name=personname
        self.bank_name=bname
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("your",self.bank_name,"has been credited with",amount,"aval balance",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficient balance in your account")
        else:
            self.balance-=amount
            print("your",self.bank_name,"has been debited with",amount,"on",datetime.date.today(),"aval balance",self.balance)

    def balenq(self):
        print("your account balance",self.balance)

obj=Bank()
#obj.createAccount(1001,"dinu","sbk",5000)
#obj.withdraw(10000)

#obj.createAccount(1002,"dinu","sbk",50000)
# obj.withdraw(10000)

#obj.createAccount(1002,"dinu","sbk",50000)
#obj.deposit(10000)

obj.createAccount(1002,"dinu","sbk",50000)
obj.balenq()