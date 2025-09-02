class Bank:
    def __init__(self,account_num,account_holder,bal=0.0):
        self.account_num = account_num
        self.account_holder = account_holder
        self.bal = bal

    def deposit(self,amt):
        self.bal = self.bal+amt
    
    def withdraw(self,amt):
        if(self.bal<amt):
            print("Insufficient Funds")
        else:
            self.bal = self.bal-amt
            print("Details after withdraw :")
            self.getBalance()

    def getBalance(self):
        print("Account Number :",self.account_num)
        print("Account Holder :",self.account_holder)
        print("Available Balance :",self.bal)


    def __str__(self):
        return f"Account Number :{self.account_num} Account Holder :{self.account_holder} Balance :{self.bal}"

class SavingsAccount(Bank):
    def apply_interest(self,interestrate):
        self.bal = self.bal + ((self.bal*interestrate)//100)

class CurrentAccount(Bank):
    def __init__(self,account_num,account_holder,bal,overdraft_limit):
        super().__init__(account_num,account_holder,bal)
        self.overdraft_limit = overdraft_limit
        self.bal = self.bal + self.overdraft_limit
    def withdraw(self,amt):
        if (self.bal > amt):
            self.bal = self.bal - amt
            print("Amount withdrawed")
            print("Details after withdraw: ")
            self.getBalance()
        else:
            print("Insufficient Funds")
            self.getBalance()


b1 = SavingsAccount(10,'Bharath',30000)
b1.getBalance()
b1.__str__()
b1.apply_interest(10)
b1.getBalance()
b1.withdraw(5000)

b2 = CurrentAccount(11,'Vijay' ,20000,10000)
b2.getBalance()
b2.withdraw(25000)
