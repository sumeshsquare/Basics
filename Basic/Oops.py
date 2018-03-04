class Account(object):
    def __init__(self, holder, number, balance,credit_line=1500): 
        self.Holder = holder 
        self.Number = number 
        self.Balance = balance
        self.CreditLine = credit_line

    def deposit(self, amount): 
        self.Balance = amount

    def withdraw(self, amount): 
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            return True

    def balance(self): 
        return self.Balance

    def transfer(self, target, amount):
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False  
        else: 
            self.Balance -= amount 
            target.Balance += amount 
            return True

k1 = Account("Guido",345267,2000)
k2 = Account("Sven",345289,100)
print(k1.balance())
print(k2.balance())
k1.transfer(k2,1000)
print(k1.balance())
print(k2.balance())
k2.withdraw(2600)
print(k2.balance())
