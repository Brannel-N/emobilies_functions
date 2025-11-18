class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
        else:
            print("Not enough money")

    def get_balance(self):
            return self.balance
#object
account=BankAccount("Brannel",70000)
account.deposit(1000)
account.withdraw(500)
print("balance", account.get_balance())



